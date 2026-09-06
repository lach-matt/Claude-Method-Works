# THE GR FLYBY

### Discharging the one soft number, and the bound that dissolves when you do

**Prepared under the protocols of The Method v1.6.** Draft v1.0.
Fourteenth of fourteen. **Discharges the caveat of `THE-BORROWED-WELL.md` §6** and **supersedes its
horizon-limited rows**; that paper is preserved unaltered.

> **Scope.** Writes nothing into `method/` or `drive/`.

---

## Abstract

`THE-BORROWED-WELL.md` derived `Δv_max/c = √(r_s/b)` with an optimal 90° turn, Newtonianly, and marked
its strong-field rows *"indicative only: scale trustworthy, digits not."* This does the calculation in
Schwarzschild geometry — exact geodesic deflection, relativistic velocity composition, the true
capture boundary — and the caveat was warranted in a way I did not anticipate. **The number went up,
and the structure of the answer changed.**

**Strong-field lensing makes the deflection diverge at the capture boundary.** At `v = 0.35 c` the
deflection runs 9° at `b = 60 r_s`, 176° at `6.6 r_s`, and **661° at 1.0001 × b_crit**. So a **net
reversal is reachable at every approach speed**, by choosing `b`. The Newtonian treatment could not
do this — weak-field deflection cannot turn a fast particle far — and its 90° optimum was an artefact
of that failure, not a feature of the physics.

With a full reversal always available, the geometric bound dissolves:

> **Δv = 2U / (1 + U²)** — set by the **deflector's speed**, not by the geometry.

Like for like, at the same `(b, U)`:

| `b` [r_s] | `U/c` | Newtonian | **GR** | ratio |
|---|---|---|---|---|
| 2205 | 0.015 | 0.0213 | 0.0213 | **1.002** |
| 595 | 0.029 | 0.0410 | 0.0413 | 1.007 |
| 12.0 | 0.20 | 0.2886 | 0.3846 | 1.333 |
| 6.6 | 0.35 | 0.3686 | **0.6236** | 1.692 |
| 4.7 | 0.50 | 0.3930 | **0.8000** | **2.036** |

**The weak-field rows are unchanged**, so `THE-BORROWED-WELL.md`'s neutron-star and stellar-black-hole
results stand exactly. Only the strong field moves, by up to a factor of two.

**What it costs is a bigger deflector.** A full-reversal pass sits at 3.5–27 r_s, and tides at fixed
`b/r_s` scale as `1/M²`, so the mass is bounded **below**: at `U = 0.35 c` and one gravity across a
20 m payload, the deflector must exceed **8,570 M☉**. **An intermediate-mass black hole is the minimum
instrument.** Below that you are tide-limited and the Newtonian weak-field answer is the right one.

The instrument is stdlib-only and validates against four closed forms of general relativity, including
the photon capture parameter at **3√3/2** to five digits.

---

## 1. What is being computed

**The orbit.** Schwarzschild geodesic for a massive particle, `u = r_s/r`, with `r_s = 1`:

`(du/dφ)² = u³ − u² + u/(γ²v²b²) + 1/b²`

The turning point is the smallest positive root — solved as a **cubic in closed form**, not scanned.
No positive root means capture.

**The deflection.** `θ = 2∫₀^{u₁} du/√f − π`. The integrand has an inverse-square-root singularity at
`u₁`; substituting `u = u₁ sin²ψ` and dividing out the known root (`f = (u−u₁)q(u)`, `q` the deflated
quadratic) removes it exactly, so **nothing is evaluated as 0/0**.

**The slingshot.** Ship at rest in the lab, deflector moving at `U`. Boost in: the ship arrives at
speed `U`, is turned by `θ`, leaves at speed `U`. Boost out by relativistic velocity addition on both
components. For `θ = π` this reduces to `2U/(1+U²)`.

### 1.1 Validation

*(COMPUTED, `grflyby.py --selftest`.)*

| limit | closed form | computed |
|---|---|---|
| photon bending | `2 r_s / b` | ratio 1.00007 at `b = 10⁵` |
| Newtonian deflection | `tan(θ/2) = GM/bv²` | ratio 1.00005 at `b = 10⁵`, `v = 0.005` |
| **photon capture** | **`3√3/2 = 2.59808`** | **2.59808** |
| slow-particle capture | `2 r_s / v` | 2.00010 at `v = 0.01` |
| full-reversal composition | `2U/(1+U²)` | exact to 1e-9 |

---

## 2. The capture boundary

*(COMPUTED, `r_s` units.)*

| `v/c` | 0.01 | 0.1 | 0.2 | 0.35 | 0.5 | 0.9 | → 1 |
|---|---|---|---|---|---|---|---|
| `b_crit` | 200.0 | 20.10 | 10.19 | 6.024 | 4.404 | 2.792 | **2.598** |

Slow particles are captured from far out (`b_crit ≈ 2r_s/v`); fast ones must aim within a few `r_s`.
The limit is the photon value, exactly.

---

## 3. The deflection diverges — and that is the whole result

At `v = 0.35 c`, `b_crit = 6.0238 r_s`: *(COMPUTED.)*

| `b` [r_s] | 60.2 | 18.1 | 9.04 | 6.626 | 6.084 | 6.030 | 6.0244 |
|---|---|---|---|---|---|---|---|
| `θ` [deg] | 9.05 | 33.5 | 85.0 | **176.0** | 332 | 496 | **661** |

Approaching the capture boundary the particle winds arbitrarily many times before escaping. So for
**any** approach speed there is a `b` giving a net deflection of exactly 180°.

> **Newtonian:** the deflection saturates at small angles for fast approaches, so `Δv = 2U sin(θ/2)`
> is maximised at a compromise — `θ = 90°`, `Δv = c√(r_s/b)`. **Geometry-limited.**
>
> **General relativity:** a full reversal is always reachable, so `Δv = 2U/(1+U²)`.
> **Deflector-speed-limited.**

The Newtonian 90° optimum was not wrong arithmetic. It was a correct optimum **inside a weak-field
approximation that cannot produce strong deflections**, and the constraint it optimised against is
not there in the full theory.

---

## 4. Full reversal, priced

*(COMPUTED.)*

| `U/c` | `b_crit` [r_s] | `b(θ=π)` [r_s] | **`Δv/c`** | Newtonian at same `b` | ratio |
|---|---|---|---|---|---|
| 0.05 | 40.05 | 63.31 | 0.0998 | 0.0953 | 1.047 |
| 0.10 | 20.10 | 26.86 | 0.1980 | 0.1840 | 1.076 |
| 0.20 | 10.19 | 11.96 | 0.3846 | 0.2886 | 1.333 |
| 0.35 | 6.024 | 6.589 | **0.6236** | 0.3686 | 1.692 |
| 0.50 | 4.404 | 4.680 | **0.8000** | 0.3930 | **2.036** |
| 0.70 | 3.356 | 3.502 | 0.9396 | — | — |

---

## 5. The price: a bigger deflector

A full-reversal pass sits at a few `r_s`, and tidal acceleration at fixed `b/r_s` is

`a = d c⁶ / (4 (b/r_s)³ G² M²)` — **`∝ 1/M²`**

so the deflector mass is bounded **below**. *(COMPUTED, 20 m payload.)*

| `U/c` | `b(π)/r_s` | min M at 1 g | min M at 10 g |
|---|---|---|---|
| 0.10 | 26.86 | 1.04 × 10³ M☉ | 3.29 × 10² |
| 0.20 | 11.96 | 3.51 × 10³ | 1.11 × 10³ |
| **0.35** | 6.59 | **8.57 × 10³** | 2.71 × 10³ |
| 0.50 | 4.68 | 1.43 × 10⁴ | 4.53 × 10³ |

> **An intermediate-mass black hole is the minimum instrument** for a full-reversal slingshot at one
> gravity. Below ~10³–10⁴ M☉ you cannot get close enough to turn, the flyby stays weak-field, and
> `THE-BORROWED-WELL.md`'s Newtonian answer is the correct one.

**The two regimes are therefore both right, in their own domains** — and the boundary between them is
now computed rather than asserted.

---

## 6. What is still not settled

**Schwarzschild only.** A spinning deflector has a closer prograde ISCO and frame dragging; Kerr can
only help, and by how much is not computed here.

**Patched conics.** The deflector is treated as moving inertially. A black hole in a binary is
*accelerating*, so a real slingshot there is a three-body problem and the two-body composition is an
approximation — the standard one in mission design, but an approximation.

**Test particle.** The ship's own mass is neglected. At 10⁶ kg against 10⁴ M☉ that is exact to 26
orders; it is stated because it is an assumption, not because it is doubtful.

**Environment.** An IMBH with an accretion flow is a lethal radiation source, and nothing here prices
shielding. A quiescent one is not, and quiescent IMBHs are the ones hardest to find.

**Arrival.** Unchanged from `THE-BORROWED-WELL.md` §6: a slingshot amplifies, it does not start.

---

## 7. Results

**1.** The Schwarzschild deflection integrator validates against four closed forms, including the
photon capture parameter at **3√3/2 to five digits**. *(COMPUTED.)*

**2.** The deflection **diverges at the capture boundary** — 661° at 1.0001 `b_crit` — so a **net
reversal is reachable at every approach speed**. *(COMPUTED.)*

**3.** The Newtonian 90° optimum is therefore an artefact of weak-field deflection, and the geometric
bound `√(r_s/b)` dissolves. **`Δv = 2U/(1+U²)`, limited by the deflector's speed.** *(DERIVED —
principal result.)*

**4.** Like for like, GR equals Newtonian in weak field (1.002 at 2205 `r_s`) and **exceeds it by up
to 2.04×** in strong field. **`THE-BORROWED-WELL.md`'s tide-limited rows stand unchanged**; only its
horizon-limited rows move. *(COMPUTED.)*

**5.** At `U = 0.35 c`, a full reversal gives **0.624 c**, against 0.500 c Newtonian and 0.0378 c for
the best shell this series can build. *(COMPUTED.)*

**6.** The cost is a mass floor on the deflector: **≥ 8,570 M☉ at 1 g** for `U = 0.35 c`. **An IMBH is
the minimum instrument.** *(COMPUTED.)*

**7.** The two regimes — tide-limited Newtonian and horizon-limited relativistic — are both correct,
and their boundary is now computed. *(Recorded.)*

---

## 8. Open

| item | state |
|---|---|
| Kerr | a spinning deflector allows closer approach and adds frame dragging; can only help, unquantified |
| the three-body problem | patched conics is an approximation; a real binary flyby needs integration |
| chained passes | still unpriced, and still the place a wrong answer was produced once |
| quiescent IMBHs | the instrument this needs; their population is poorly constrained |
| arrival | unchanged |

---

## Appendix · Reproduction

```
python3 research/warp-drive/grflyby.py --selftest   # 10 fixtures, closed-form limits
python3 research/warp-drive/grflyby.py              # the tables of §4 and §5
python3 research/warp-drive/warpdrive.py --selftest # 104 fixtures, the rest of the series
```

`grflyby.py` is stdlib-only: the cubic turning point is solved in closed form and the deflection
integral's singularity is removed analytically rather than dodged numerically.
