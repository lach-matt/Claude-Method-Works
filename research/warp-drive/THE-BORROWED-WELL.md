# THE BORROWED WELL

### The method equation read backwards, and a closed form for transport without a drive

**Prepared under the protocols of The Method v1.6.** Draft v1.0.
Thirteenth of thirteen. Method: **register 1206**, read in reverse.

> **§6's caveat is DISCHARGED and §4's horizon-limited rows are SUPERSEDED, 2026-09-06.**
> `THE-GR-FLYBY.md` does the flyby in Schwarzschild geometry. Strong-field lensing makes the
> deflection diverge at the capture boundary, so a **full reversal is reachable at every approach
> speed** — the 90° optimum below is an artefact of weak-field deflection. The bound `√(r_s/b)`
> dissolves and is replaced by **Δv = 2U/(1+U²)**, limited by the deflector's speed: **0.624 c at
> U = 0.35 c** against 0.500 c here. **The tide-limited rows — neutron star, stellar black hole —
> stand exactly** (GR/Newtonian = 1.002). The cost is a mass floor: a full-reversal pass at 1 g needs
> a deflector above ~8,570 M☉.

> **Scope.** Writes nothing into `method/` or `drive/`.

---

## Abstract

Register 1206 states the architecture of the method equation and, in doing so, diagnoses this series:

> ***"E_W = 0 was the Method equation reporting that no STEP could carry a value. The equation is not
> a step — it is a closed form on the index's own coordinates, and that is what closes the gap."***

Every result after `THE-DESIGN-EQUATION.md` was a **step** — try a shift profile, try a density, try
a deformation — and each returned zero. Read backwards, those zeros were never reports about warp
drives. They were reports that **no step in that space carries the value**. The remedy 1206 gives is
not another step. It is to invert the closed form.

**Inverted, the question stops being "how fast can this machine go" and becomes "what does the
transport require, and what is the cheapest thing that supplies it."** The requirement is a potential
gradient along the path plus geodesic motion in it. There are three sources and this series had
costed exactly one.

| source | cost |
|---|---|
| **build** a gradient — the warp shell | 6.73 × 10²⁶ kg per metre of ship, then ΔP must be sourced. Closed. |
| **find** one — free-fall past a compact object | free, geodesic, but you do not choose its direction |
| **borrow** one — a flyby taking momentum from a *moving* deflector | **never costed here** |

**The borrow route has a closed form.** Maximising `Δv = 2U sin(θ/2)` against
`tan(θ/2) = GM/(bc²U²)` gives `sin 2t = 1`, so the **optimal turn is exactly 90°, at every scale**,
and

> **Δv_max / c = √( r_s / b )**,  `U_opt = Δv_max / √2 c`

**The speed you can borrow is `c` times the square root of the deflector's compactness at closest
approach.** Verified against a numerical scan to four decimals across four decades of mass.

Two regimes: **tide-limited**, where `b = (2GMd/a)^{1/3}` and `Δv ∝ M^{1/3}`; and
**horizon-limited**, where `b = 4r_s` and `Δv = c/2` independent of mass.

**A ten-solar-mass black hole at one gravity of tide gives 0.0410 c** — already better than the
0.0378 c this series can specify for a 4.49 × 10²⁷ kg shell costing 29 Earth masses of propellant.
And the 0.0378 c itself needs only a pass at **700 r_s**: distant, gentle, off any black hole.

**Zero construction. Zero propellant. Geodesic by construction.**

---

## 1. Reading 1206 backwards

The method equation has two halves: **ℛ places cells, the channel equation values them.** Register
1206 records the moment they met — ℛ placed 1,648 cells the compendium did not hold, the *walk*
valued **none** of them, and the *equation* valued **all** of them.

The operative sentence is the diagnosis of the zero. `E_W = 0` was not "nothing here." It was **the
equation reporting that no step could carry a value** — a statement about the method, not the object.

Set against this series:

| step taken | result |
|---|---|
| shaped density, symmetric | 1.019 × — noise |
| shaped density, inner-weighted | 0.663 ×, 0.398 × — worse |
| sharpness σ | already optimal at 0 |
| oblate deformation | control failed |

Four steps, four zeros. Read forwards, that is a wall. Read backwards, it is the equation saying
**the value is not in the space being stepped through**, and the closed form is what reaches it.

**The inversion.** Forwards: choose `(fill, C, γ)` → get `v_max`. Backwards: fix the transport → ask
what supplies it. And what the transport actually requires is *not a machine*. It is a potential
gradient and geodesic motion in it.

---

## 2. The three sources

**Build.** The warp shell manufactures the gradient. `M ≥ (c²/2G)·R₁·v·k̂/Φ`, and `c²/2G` is
6.73 × 10²⁶ kg per metre of ship. Then `ΔP = γMv` must be radiated — `ACCELERATION.md` — and it
cannot be. **Closed.**

**Find.** Free-fall past a compact object is geodesic and costs nothing; a neutron star surface gives
0.587 c. But a static well returns what it takes: you fall in and climb out. It changes direction,
not speed.

**Borrow.** A flyby past a *moving* deflector takes momentum from it. This is a slingshot, it is
ordinary celestial mechanics, and this series never costed it.

---

## 3. The closed form

`Δv = 2U sin t` with `t = θ/2`, and the deflection satisfies `tan t = GM/(b w²) = k/U²` for
`k = GM/(bc²)` and approach speed `w = Uc`. Substituting `U = √(k / tan t)`:

`Δv/c = 2√k · √(sin t cos t) = √(2k) · √(sin 2t)`

which is maximised at `sin 2t = 1`:

> **`t = 45°` — the optimal turn is exactly 90°, at every mass, every distance, every scale.**
>
> **`Δv_max / c = √(2k) = √(2GM/bc²) = √(r_s / b)`**
> **`U_opt = √k = Δv_max / (√2 c)`**

**Verified against a numerical optimisation** *(COMPUTED)*:

| deflector | `r_s` [m] | `b` [m] | `√(r_s/b)` | scan |
|---|---|---|---|---|
| neutron star | 4.136e3 | 9.120e6 | **0.0213** | 0.0213 |
| stellar black hole | 2.954e4 | 1.756e7 | **0.0410** | 0.0410 |
| IMBH | 2.954e7 | 1.756e8 | **0.4101** | 0.4101 |
| Sgr A* | 1.270e10 | 5.081e10 | **0.5000** | 0.5000 |

---

## 4. The two regimes

`b` is bounded below by tides across the payload **and** by capture near a horizon:

`b ≥ max[ (2GMd/a)^{1/3},  4 r_s ]`

**Tide-limited** — small deflectors. `b ∝ M^{1/3}`, so `r_s/b ∝ M^{2/3}` and
**`Δv ∝ M^{1/3}`**. Bigger is better, slowly.

**Horizon-limited** — above ~10⁴ M☉. Tides at fixed `b/r_s` scale as `1/M²`, so they vanish and only
capture bounds you: `b = 4r_s` gives **`Δv = c/2`, independent of mass.**

*(COMPUTED, 20 m payload, 1 g tidal limit, `b ≥ 4r_s`.)*

| deflector | M [M☉] | `b/r_s` | `U_opt/c` | **`Δv/c`** | limited by |
|---|---|---|---|---|---|
| neutron star | 1.4 | 2205 | 0.0151 | **0.0213** | tide |
| stellar black hole | 10 | 595 | 0.0290 | **0.0410** | tide |
| IMBH | 10⁴ | 5.9 | 0.2900 | **0.4101** | tide |
| Sgr A* | 4.3 × 10⁶ | 4.0 | 0.3536 | **0.5000** | 4 r_s |
| M87* | 6.5 × 10⁹ | 4.0 | 0.3536 | **0.5000** | 4 r_s |

---

## 5. Against the build route

| | construction | propellant | transport |
|---|---|---|---|
| build the shell | **4.49 × 10²⁷ kg** at 6.7 × 10⁵ × nuclear density | **29 Earth masses** annihilated | geodesic |
| borrow a well | **none** | **none** | geodesic |

Both deliver 0.0378 c. And read backwards, the build target is undemanding as a *trajectory*:

> **0.0378 c needs only `b = 700 r_s`** — a distant, gentle pass off any black hole. A ten-solar-mass
> hole at one gravity of tide already **exceeds** it, at 0.0410 c.

The shell's entire function is geodesic transport where there is no well. A flyby is geodesic
transport *using* a well. **They are alternatives, and one of them is free.**

---

## 6. What is defensible, and what is not

**Newtonian throughout.** Sound where `U_opt ≪ 1`: the neutron star (0.0151 c) and the stellar black
hole (0.0290 c) rows are solid. At `b = 4 r_s` the optimum sits at `U = 0.354 c` and the treatment is
**not** valid — the deflection needs the relativistic hyperbolic orbit and the composition is not
`2U sin(θ/2)`. **Those rows are order 0.3–0.5 c: scale trustworthy, digits not.**

**A slingshot amplifies; it does not start.** You must arrive at the deflector. Arrival may be slow
and cheap — it is not subject to the shell's ΔP problem, because a light probe is light — but it is a
real prerequisite and it is not costed here.

**Chaining is not priced.** A first attempt gave 0.56 c in five passes and was **wrong**: it held the
deflection angle fixed while the approach speed grew, and faster encounters deflect *less*. Doing it
self-consistently is what produced §3's closed form. No chained figure is asserted.

**Environments.** Neutron-star and black-hole neighbourhoods are radiation-hostile and, near an
accreting hole, lethal. Nothing here prices shielding.

**It is not a warp drive.** It is celestial mechanics. Whether that counts depends on what was
wanted — but it delivers the stated requirement, and the manufactured object does not.

---

## 7. Results

**1.** Register 1206, read backwards, diagnoses four consecutive zeros in this series as reports about
the *walk*, not the object. The remedy is inversion, not another step. *(Method.)*

**2.** Inverted, the requirement is a potential gradient plus geodesic motion, with three sources.
Only *build* had ever been costed here. *(Recorded.)*

**3.** The borrow route has a closed form: **`Δv_max/c = √(r_s/b)`**, with the **optimal turn exactly
90° at every scale**. Verified against numerical optimisation to four decimals over four decades of
mass. *(DERIVED + COMPUTED — the paper's principal result.)*

**4.** Two regimes: tide-limited `Δv ∝ M^{1/3}`; horizon-limited `Δv = c/2`, mass-independent.
*(COMPUTED.)*

**5. A ten-solar-mass black hole at 1 g gives 0.0410 c**, exceeding the 0.0378 c this series can
specify for a shell of 4.49 × 10²⁷ kg plus 29 Earth masses of propellant. *(COMPUTED.)*

**6.** The build target needs only a **700 r_s** pass. *(COMPUTED.)*

**7.** The horizon-limited rows need general relativity and are indicative only; chaining is not
priced, and the earlier chained figure was withdrawn on discovery. *(Recorded.)*

---

## 8. Open

| item | state |
|---|---|
| relativistic flyby near a horizon | the `c/2` figure needs the GR hyperbolic orbit; the Newtonian derivation does not survive `U = 0.354 c` |
| chained passes, self-consistently | possible in a bound binary; the gain per pass falls as the approach speed rises, and the composition has not been done |
| the arrival problem | a slingshot amplifies. Reaching the deflector is a separate, cheaper problem, uncosted here |
| whether "warp drive" survives this reframing | a question about the object, not the physics. The physics is settled: the manufactured well is dominated by borrowed ones |
| oblate initial data | still the last open lever *inside* the build route, and now clearly the less interesting branch |

---

## Appendix · Reproduction

```
python3 research/warp-drive/warpdrive.py --selftest    # 104 fixtures
python3 research/warp-drive/warpdrive.py               # full report
```

`slingshot_dv()` carries the closed form and `closest_approach()` the two bounds on `b`. The
90° optimum, the `M^{1/3}` scaling, the agreement with the scan and the 700 r_s inversion are
fixtures.
