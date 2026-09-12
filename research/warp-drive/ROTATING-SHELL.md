# THE ROTATING SHELL

### Counter-rotation on a positive-energy warp drive, and why it is required rather than permitted

**Prepared under the protocols of The Method v1.6.** Draft v1.0.
Third of three. Read `WARP-DRIVE.md` and `ENGINE-ASSESSMENT.md` first.

> **Scope.** Writes nothing into `method/` or `drive/`. Findings recorded, never repaired.

---

## Abstract

`ENGINE-ASSESSMENT.md` concluded that *Warp Drive Theory*'s Architecture B has the right geometry and
the wrong source, and that its one unambiguously sound idea — cancelling angular momentum by
counter-rotating two concentric shells — deserves to be carried onto the Fuchs *et al.* positive-energy
warp shell. This paper does that calculation.

**The result is stronger than compatibility.** A single rotating shell carries ADM angular momentum,
so its exterior is Kerr rather than Schwarzschild — and the Fuchs construction is built on a
Schwarzschild exterior. **Counter-rotation sets `J = 0` exactly, the `g_tφ` frame-dragging term
vanishes, and the exterior is restored.** Counter-rotation is therefore not one way to spin the shell;
it is the only way to spin it without destroying the boundary condition the solution depends on. The
design document proposed it for gyroscopic freedom and was right for a reason it did not state.

**It is also nearly free.** A boost does not change the eigenvalues of the stress-energy tensor, so
rotating matter that satisfies the energy conditions at rest still satisfies them. The genuine cost is
the centrifugal hoop tension the shell must supply to hold itself together, `|Δp_φ|/ρ = β²` — quadratic
in rim speed, not linear. The static solution spends **36 %** of its dominant-energy-condition budget
and leaves **64 %** free, which permits rim speeds up to **β = 0.798** on the eigenvalue budget and
**0.637** on Fuchs *et al.*'s more conservative Eulerian rule. At the rim speed ordinary material
actually survives — 1,768 m s⁻¹, from `ENGINE-ASSESSMENT.md` §3.3 — the cost is **3.5 × 10⁻¹¹**.

**And it buys nothing but the gyroscopic freedom.** Rotation would support the shell against its own
gravity only at **β = 0.577**; attainable rim speed is short of that by a factor of **10⁵**. Rotation
is free, and it is structurally useless. That is a clean result rather than a disappointing one,
because gyroscopic freedom was the only thing being asked of it.

Two corrections to the design document follow. Its stated motive for relativistic rim speed was the
Dynamic Casimir Effect, which does not work (§3.2 of the assessment); **the angular-momentum
cancellation it actually delivers needs no speed at all**, so dropping the relativistic requirement
costs nothing. And electromagnetic levitation cannot be structural — it is 30 orders of magnitude
below the shell's own stresses — but by the shell theorem **no structural bearing is needed**: a
concentric shell inside a hollow shell feels no net gravitational force, the pair is neutrally stable,
and centring against perturbation is the only job on offer.

One design rule emerges that the document had already satisfied by accident: **put the spin axis on
the thrust axis.** The shift vector's momentum flux lies along `x`; rotation about `x` puts its flux in
the `y`–`z` plane. Orthogonal fluxes add in quadrature, so at `β = 0.5` the combined Eulerian flux is
**0.618**, still inside budget, where linear addition would have breached it.

---

## 1. The question

Fuchs *et al.* (2024) exhibit the only warp drive satisfying the null, weak, dominant and strong
energy conditions simultaneously: a stable matter shell with a Schwarzschild exterior, positive ADM
mass, and a shift vector added on its interior producing geodesic transport by linear frame dragging.
Its published parameters are in `WARP-DRIVE.md` §5.2.

*Warp Drive Theory* proposes something the Fuchs solution does not have: **two concentric shells
counter-rotating at equal and opposite rates**, so that

`L_total = Iω + I(−ω) = 0`

eliminating gyroscopic resistance and granting the vessel free reorientation. `ENGINE-ASSESSMENT.md`
§2 found this to be the soundest idea in the document and independently useful. The question this
paper answers is whether it can be added to the Fuchs shell **without breaking the energy conditions
that make that shell physical** — and, if so, what it costs.

Four budgets have to be checked separately, because they are different questions with different
answers: the exterior boundary condition, the local energy conditions, the structural contribution,
and the mechanical one.

---

## 2. The exterior boundary condition — and the result that matters

The Fuchs construction depends on the exterior being **Schwarzschild**. That is what gives it positive
ADM mass, what makes the matching at `R₂` work, and what distinguishes it from the truncated Alcubierre
and Natário metrics whose flat exteriors force the negative energy (Bobrick–Martire §3.1).

**A rotating body does not have a Schwarzschild exterior.** Angular momentum `J` produces a
`g_tφ ≈ −2GJ/rc²` frame-dragging term; the exterior is Kerr with `a = J/Mc`. A single rotating shell
therefore breaks the construction at its boundary, before any question of energy conditions arises.

> **Counter-rotation sets `J = 0` identically.** The two shells' angular momenta cancel exactly, the
> `g_tφ` term vanishes, and the exterior is Schwarzschild again at that order.

What survives is a **mass quadrupole** induced by rotational oblateness, scaling as `β²`:

| rim speed `β` | residual quadrupole |
|---|---|
| 5.9 × 10⁻⁶ (material limit) | 3.5 × 10⁻¹¹ |
| 0.01 | 1.0 × 10⁻⁴ |
| 0.5 | 2.5 × 10⁻¹ |

*(COMPUTED.)* At attainable rim speed the exterior is Schwarzschild to eleven significant figures. At
`β = 0.5` the quadrupole is a quarter and the matching would have to be redone in a
Hartle–Thorne-style expansion rather than against pure Schwarzschild.

> **This is the paper's principal result.** Counter-rotation is not merely *permitted* on a Fuchs-type
> shell. It is the **only** way to rotate one at all, because any uncancelled angular momentum replaces
> the exterior the solution is built on. The design document proposed counter-rotation for gyroscopic
> freedom; it turns out to be load-bearing for a reason the document does not state and, on the
> evidence of the text, did not know.

---

## 3. The local energy-condition budget

### 3.1 A boost is not a violation

The first thing to get right is what rotation does *not* cost.

The energy conditions are statements about the **eigenvalues** of the stress-energy tensor — for
Hawking–Ellis type I, `NEC ⟺ ρ + pᵢ ≥ 0`, `DEC ⟺ |pᵢ| ≤ ρ`, and so on (Santiago–Schuster–Visser
§5, eqs. 5.6–5.9). Eigenvalues are **invariant under a local boost**. Rigid rotation is a local boost.

> **Matter that satisfies the energy conditions at rest still satisfies them when rotating.** Rotation
> is not, in itself, a cost at all.

This is worth stating plainly because the opposite error — reading a frame-dependent component as
though it were the condition — is exactly what Santiago–Schuster–Visser found in three separate
positive-energy warp-drive claims.

### 3.2 What rotation does cost

The real cost is that a spinning shell needs **centrifugal hoop tension** to hold together, and that
tension is a new entry in the eigenvalue spectrum. For a shell element of mass density `ρ_m` at rim
speed `v`, the hoop stress is `σ = ρ_m v²`, a tension, so `p_φ` acquires a negative contribution of
magnitude `ρ_m v²`. Normalised to the energy density `ρ = ρ_m c²`:

**`|Δp_φ| / ρ = v²/c² = β²`**

Quadratic, not linear. Meanwhile Fuchs *et al.* work to the **sufficient** rule of thumb that every
Eulerian pressure and momentum flux stay below the energy density; boosted momentum flux is
`T^{0φ}/T^{00} ≈ β`, linear. That rule is conservative and is not the energy condition, so both are
reported.

### 3.3 The margin available

Read from Fuchs *et al.* fig. 9: energy density `ρ ≈ 1.376 × 10⁴⁰ J m⁻³`, with pressures and momentum
flux peaking near `5 × 10³⁹ J m⁻³`. *(CITED, read off plotted profiles — approximate, and the least
precise input in this paper.)*

| | value |
|---|---|
| DEC budget spent by the static solution | **36 %** |
| DEC budget free | **64 %** |
| largest `β`, eigenvalue budget (`β² ≤ free`) | **0.798** |
| largest `β`, Eulerian budget (`β ≤ free`) | **0.637** |

**Cost at candidate rim speeds** *(COMPUTED)*:

| rim speed | eigenvalue cost `β²` | Eulerian cost `β` |
|---|---|---|
| 1,768 m s⁻¹ — the material limit | **3.48 × 10⁻¹¹** | 5.90 × 10⁻⁶ |
| 0.01 c | 1.00 × 10⁻⁴ | 1.00 × 10⁻² |
| 0.1 c | 1.00 × 10⁻² | 1.00 × 10⁻¹ |
| 0.5 c | 2.50 × 10⁻¹ | 5.00 × 10⁻¹ |

> At the rim speed real material survives, counter-rotation consumes **three parts in a hundred
> billion** of the shell's energy-condition margin. It is free.

---

## 4. Rotation does not help hold the shell up

The natural hope is that centrifugal support offsets the gravitational compression that makes the
shell hard to build. It does not, and the shortfall is not marginal.

Rotation balances the shell's own gravity when `v² ≈ GM/R`, giving **`β_orbital = 0.577`** at
`R₁ = 10 m` and `M = 4.49 × 10²⁷ kg`. *(COMPUTED.)* Ordinary material survives `β = 5.9 × 10⁻⁶`
(`ENGINE-ASSESSMENT.md` §3.3). The shortfall is a factor of **1.0 × 10⁵**, so the centrifugal
contribution to support is one part in **10¹⁰**.

> **Rotation is free and it is structurally useless.** It buys gyroscopic freedom and nothing else.

This is not a defect in the proposal, because gyroscopic freedom is all the proposal claimed for it.
It does dispose of any hope that spinning the shell might relax the density requirement of
`WARP-DRIVE.md` §5.4 — it cannot, and the 8.16 km / 1.84 M☉ scaling stands unaltered.

---

## 5. The mechanical question, correctly posed

The document replaces mechanical gyroscopes with "solid-state electromagnetic levitation". Two
separate things have to be said, and the first is favourable.

**No structural bearing is required.** By the shell theorem, a concentric shell inside a hollow shell
experiences **no net gravitational force anywhere inside it**. Each shell is already self-supporting
through its own TOV pressure profile. The pair is therefore neutrally stable, and the mechanical task
is *centring against perturbation*, not carrying weight.

**Levitation cannot be structural.** *(COMPUTED)*: magnetic pressure at an extreme 100 T is
`B²/2µ₀ = 3.98 × 10⁹ Pa`, against the shell's own internal pressure of `~5 × 10³⁹ Pa` — a ratio of
**8.0 × 10⁻³¹**. Electromagnetic forces are thirty orders of magnitude below the shell's own stresses
and can never act as a structural element at this density.

> Fortunately, structure is not the job. Centring is, and that is a small-perturbation task. **Sizing
> it requires a perturbation spectrum that does not exist**, since nobody has evolved this solution
> dynamically — see §8.

**Stored angular momentum**, for scale *(COMPUTED)*: moment of inertia `3.98 × 10²⁹ kg m²` per shell,
`ω = 88.4 rad s⁻¹` at the material-limit rim, giving `|L| = 3.52 × 10³¹ kg m² s⁻¹` per shell and
`L_total = 0`.

---

## 6. One design rule, already satisfied

The shift vector places momentum flux along the direction of travel, `x`. Rotation about an axis places
its momentum flux in the plane perpendicular to that axis.

> **Put the spin axis on the thrust axis.** Then the two momentum fluxes are orthogonal and add in
> **quadrature** rather than linearly.

*(COMPUTED)*, with the static shift flux at 0.363:

| rim speed `β` | combined Eulerian flux | within budget? |
|---|---|---|
| 5.9 × 10⁻⁶ | 0.3634 | yes |
| 0.1 | 0.3769 | yes |
| 0.5 | 0.6181 | yes |

Linear addition at `β = 0.5` would give 0.863 and crowd the budget; quadrature gives 0.618 and does
not. **Architecture B already spins about its thrust axis**, so the document had this right — again,
apparently without stating why.

---

## 7. Results

**1. Counter-rotation is required, not permitted.** A single rotating shell has `J > 0` and hence a
Kerr exterior, which destroys the Schwarzschild boundary condition the Fuchs solution is built on.
Counter-rotation sets `J = 0` and restores it. *(INFERRED from CITED; the paper's principal result.)*

**2. The residual is a `β²` mass quadrupole**, 3.5 × 10⁻¹¹ at attainable rim speed and 0.25 at
`β = 0.5`, where the matching would need a Hartle–Thorne expansion instead of pure Schwarzschild.
*(COMPUTED.)*

**3. Rotation costs `β²`, not `β`.** Eigenvalues are boost-invariant, so the boost itself is free; the
cost is the centrifugal hoop tension entering the eigenvalue spectrum. Fuchs *et al.*'s Eulerian rule
of thumb costs `β` linearly and is conservative rather than necessary. *(COMPUTED.)*

**4. The margin is ample.** The static solution leaves 64 % of the DEC budget free, permitting
`β ≤ 0.798` on eigenvalues and `β ≤ 0.637` on the Eulerian rule. At the material limit the cost is
3.48 × 10⁻¹¹. *(COMPUTED, on a margin read off plotted profiles.)*

**5. Rotation gives no structural support.** Balancing gravity needs `β = 0.577`; material allows
5.9 × 10⁻⁶. The density and mass scaling of `WARP-DRIVE.md` §5.4 is unchanged. *(COMPUTED.)*

**6. The relativistic requirement can be dropped for free.** The document wanted relativistic rim speed
for the Dynamic Casimir Effect, which does not work. **Angular-momentum cancellation needs no speed
whatsoever** — only equality and opposition. Dropping the requirement costs the design nothing it was
actually getting. *(INFERRED.)*

**7. No structural bearing is needed** — the shell theorem gives neutral stability — and none is
available: levitation is 8.0 × 10⁻³¹ of the shell's own stresses. The residual centring task is the
only mechanical job, and it is unsized. *(COMPUTED + INFERRED.)*

**8. Spin axis on thrust axis**, so the momentum fluxes add in quadrature. Architecture B already does
this. *(COMPUTED.)*

**9. The design document's best idea transplants intact and becomes load-bearing.** Of everything in
*Warp Drive Theory*, the counter-rotation survives review, survives transplant onto a solution that
actually satisfies the energy conditions, and turns out to be necessary there. *(INFERRED.)*

---

## 8. Open

| item | state |
|---|---|
| the exact DEC margin | read off Fuchs *et al.* fig. 9 by eye at 36 % spent; the published data would sharpen every figure in §3.3, and none of the conclusions depends on the third digit |
| Hartle–Thorne matching for `β ≳ 0.1` | not attempted; needed only if a rotation regime is ever reachable, which §4 says it is not |
| the perturbation spectrum for the centring problem | does not exist; nobody has evolved this solution dynamically. This is the one open item in this paper that blocks a real design |
| whether the shift vector and rotation interact beyond quadrature | §6 treats the fluxes as independent. A full numerical evaluation in Warp Factory would settle it, and is the natural next computation |
| acceleration | untouched here and still the field's foremost open problem (`WARP-DRIVE.md` §5.5) |

---

## Appendix · Reproduction

```
python3 research/warp-drive/warpdrive.py --selftest    # 33 fixtures
python3 research/warp-drive/warpdrive.py               # full report
```

The rotation section's fixtures are the DEC margin, the `β²` scaling, the orbital rim speed at the
published shell parameters, and the levitation ratio. A `FAIL` means this paper is wrong.
