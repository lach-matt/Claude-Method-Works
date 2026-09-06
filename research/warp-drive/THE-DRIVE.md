# The drive

### Engineering specification — a warp shell at the scale where matter can actually build it

**Status:** design specification. Instrument: `drivespec.py` (stdlib-only, 17 fixtures, `--selftest`).
Supersedes the mass and density figures used throughout this series. Nothing here touches the Method
volumes.

---

## 0. The error this document corrects

Fourteen papers quoted the warp shell's cost as **751 Earth masses at 666,000 × nuclear density** and
concluded that no material could ever supply it. That conclusion was wrong, and the reason is
embarrassing: **every one of those papers fixed the ship at the published example's R₁ = 10 m and
never varied it.**

Size is a free parameter, and the two scalings run in opposite directions:

> **M = f R₁ c² / 2G** — mass grows **linearly** with size
> **ρ = 3 f c² / 8πG R₁²(γ³−1)** — density falls as **1/R²**

"666,000 × nuclear" is a property of a 20 m ship. It is not a property of warp shells. Make the ship
bigger and the material requirement collapses quadratically.

---

## 1. The materials trade, in full

Solving `ρ(R₁) = ρ_material` for each candidate, at the derived optimal geometry `γ = 1+√3`:

| material | density (kg/m³) | minimum radius | shell mass |
|---|---|---|---|
| steel | 7.85 × 10³ | 2.65 × 10⁷ km | 5.99 × 10⁶ M☉ |
| osmium | 2.26 × 10⁴ | 1.56 × 10⁷ km | 3.53 × 10⁶ M☉ |
| white-dwarf matter | 1.0 × 10⁹ | 7.43 × 10⁴ km | 1.68 × 10⁴ M☉ |
| neutron-star crust | 1.0 × 10¹⁴ | 235 km | 53.1 M☉ |
| **nuclear matter** | **2.3 × 10¹⁷** | **4.9 km** | **1.11 M☉** |
| NS core | 1.0 × 10¹⁸ | 2.35 km | 0.53 M☉ |

Read it the right way round. **There is no material that makes a small warp shell** — shrinking it
drives density up as 1/R² and no substance follows. But there is a size at which ordinary dense
matter suffices, and the price of reaching it is mass, which grows linearly the whole way.

The knee is at **nuclear matter, ~5 km**. That is not a coincidence. It is the statement that a warp
shell of this class *is a compact star*. And unlike 751 Earth masses at 666,000 × nuclear — which is
nothing that exists anywhere — there are of order **10⁸ objects of that description in this galaxy.**

---

## 2. The point design

```
GEOMETRY
  Interior radius       R1 = 4,902 m          (habitable volume 4.9e11 m^3)
  Outer radius          R2 = 13,391 m         gamma = R2/R1 = 1+sqrt(3) = 2.7321
  Wall thickness        d  = 8,489 m
  Geometry factor       G(gamma) = 3+2sqrt(3) = 6.4641   [the derived minimum]

SHELL
  Mass                  2.200e30 kg = 1.11 Msun
  Density               2.3e17 kg/m^3 (nuclear saturation) -- uniform
  Compactness           f = r_s/R1 = 0.667
  Schwarzschild radius  r_s = 3,268 m  (< R1: no horizon, the interior is open)

SHIFT
  Profile               raised cosine, S(t) = (1+cos pi t)/2
  Curvature norm        C = max|S''|d^2 = pi^2/2 = 4.9348
                        [bang-bang lower bound is 4.000; this is 23% above optimal
                         and is C^1; the published compactSigmoid sits at 9.841]

PERFORMANCE
  Cruise velocity       v_warp = 0.0476 c = 1.43e7 m/s
  Interior              flat -- g_uv = eta_uv; crew in free fall, zero felt acceleration
  Energy conditions     null, weak, strong, dominant -- all satisfied pointwise

MECHANISM
  Internal circulation  0.330 c
  Gearing               k = k_hat/f = 6.94 : 1
  Wall dynamic stress   2.25e33 Pa      [NS matter sustains ~1e34 Pa here: 4.4x margin]
  Spin-up energy        1.17e46 J = 5.93% of shell rest mass
```

---

## 3. The mechanism, stated plainly

**The shell does not move. Its matter circulates.**

The metric needs a momentum flux `T^0x` in the shell wall — momentum density with *zero net
momentum*, which is exactly what a closed circulation loop provides. The gearing is
`k = k̂/f = 6.94`: circulate the wall matter at **0.330 c** and the interior translates at
**0.0476 c**. You pay a 7:1 loss and you buy geodesic transport — the interior is flat, so there is
no acceleration inside, no matter what the shell does.

This is precisely the topology of **Architecture B in the original deliverable**: counter-rotating
mass, net angular momentum zero, momentum flux directed along the axis. That architecture was never
the wrong idea. It was wrong by a factor of ~500,000 in **scale** and about twelve orders of magnitude
in **material**. Copper at 20 m cannot do it. Nuclear matter at 5 km can.

---

## 4. Subsystems

**4.1 Shell.** 1.11 M☉ of nuclear-density matter, spherical, uniform density, 8.5 km wall. Held
against its own gravity by degeneracy pressure — the same equilibrium that holds a neutron star.
This is not fabricated; it is a neutron star **remachined** (see §6).

**4.2 Circulation system.** The drive proper. Wall matter in a closed poloidal loop at 0.330 c, net
linear and angular momentum zero. Dynamic pressure 2.25 × 10³³ Pa against a material limit near
10³⁴ Pa — a **4.4× structural margin**, which is the tightest margin in the design and the number
most likely to move under a real equation of state.

**4.3 Shift-profile control.** The velocity is set by the radial profile `S(r)` of the circulation,
not by its peak speed. Steering `v_warp` means re-shaping the circulation profile. The raised cosine
is 23% off the bang-bang bound of `4/d²` and is the best `C¹` profile available; going below it
requires discontinuous `S″`, i.e. a discontinuity in circulation gradient at mid-wall.

**4.4 Interior.** 4.9 × 10¹¹ m³ of flat spacetime. No tidal field, no acceleration, no shielding
requirement from the drive itself. This is the payoff and it is total: the crew cannot tell the
drive is running.

**4.5 What is absent.** No propellant, no reaction mass, no exotic matter, no negative energy
density, no field generators, no Faraday hull, no muon source. Every one of those was in the original
architecture and none of them is needed.

---

## 5. The limit that does not move

**ADM 4-momentum conservation forbids self-acceleration at positive ADM mass.** This is analytic, it
does not depend on any measurement in this series, and it is not negotiable. The shell **cruises**;
it cannot start itself. Something external must supply the initial 0.0476 c.

That is not a defect to engineer around — it is a specification of the launch system, and this
project already has one. `THE-ENGINE.md` derives a binary-slingshot launcher delivering **0.87 c at
zero propellant**. The two designs are complements:

| | role | speed | cost |
|---|---|---|---|
| **binary slingshot** | launcher | 0.87 c | zero propellant, found object |
| **warp shell** | cruiser | 0.0476 c | 1.11 M☉, geodesic interior |

And the honest reading of that table is that **the launcher is eighteen times faster than the
cruiser**. On these numbers you build the launcher and skip the shell — the shell's only unique
offering is the flat interior, and a slingshot payload on a geodesic is in free fall too. The shell
buys comfort at close approach, not speed.

---

## 6. Construction

The shell is **found and modified**, not fabricated. No industrial process produces nuclear-density
matter in stellar quantities; gravity does, routinely.

1. **Source.** A neutron star of ~1.1 M☉. The galaxy holds ~10⁸; the nearest candidates are ~200 pc.
2. **Reshape.** The design wants a *shell* (hollow, R₁ = 4.9 km) where nature supplies a *ball*. This
   is the hardest unsolved step and this document does not solve it. Hollowing a neutron star against
   its own binding energy is a ~10⁴⁶ J operation at minimum — comparable to the spin-up cost, and to
   within an order of magnitude of a supernova.
3. **Spin up the circulation.** 1.17 × 10⁴⁶ J, 5.93% of rest mass, to 0.330 c. For scale, millisecond
   pulsars already reach ~0.2 c equatorially by accretion alone, so the *speed* is within a factor of
   two of something nature does unaided. The *pattern* — a closed poloidal loop with zero net angular
   momentum — is not.
4. **Profile and trim.** Shape `S(r)` to the raised cosine; verify the null condition margin.

**Steps 2 and 3 are each ~10⁴⁶ J.** That is the real bill, and it is the honest headline: this drive
costs a supernova's worth of energy and requires machining a neutron star. It is not 10³¹ times
beyond physics, as this series previously claimed — it is roughly one stellar catastrophe, which is a
different kind of impossible and a much smaller one.

---

## 7. Open items

1. **The re-measure is not done.** The corrected NEC threshold is ≈0.045 c (`NEC-CORRECTION.md`), and
   `Φ = 0.33` was measured on the contaminated slice. `v_warp` here is therefore good to about a
   factor of 1.5, not to three digits.
2. **Uniform density is assumed.** `DENSITY-IS-CLOSED.md` found inner-weighting *hurts* — but that was
   measured on the contaminated slice too, and needs redoing.
3. **A real equation of state**, not a constant 2.3 × 10¹⁷. The 4.4× stress margin is the number this
   would move most.
4. **Hollowing.** Step 6.2 has no proposed method.
5. **Circulation stability.** A 0.33 c poloidal loop in degenerate matter against MHD and
   Kelvin–Helmholtz instability is unaddressed.
6. **Sphericity** remains untested (`SPHERICITY.md`'s oblate trial failed its own control).

---

## 8. Conclusions

1. The **"no material can do it"** conclusion of this series was an artefact of never varying the
   ship's size. Withdrawn.
2. `M ∝ R` and `ρ ∝ 1/R²`: there is **no material that makes a small warp shell**, and **nuclear
   matter makes a 5 km one**.
3. Point design: **R₁ = 4.9 km, 1.11 M☉, nuclear density, 0.0476 c, flat interior, all four energy
   conditions satisfied.**
4. The mechanism is **internal circulation at 0.330 c**, geared 6.94:1 — the original Architecture B
   topology at the right scale and material.
5. Structural margin **4.4×** against the material limit. It closes.
6. **ADM conservation still forbids self-starting.** The shell is a cruiser and needs the slingshot
   launcher — which is 18× faster than the cruiser, and is the reason to build it first.
7. The bill is **~10⁴⁶ J twice over** and a neutron star. One stellar catastrophe, not 10³¹.

---

## Reproduction

```
python3 research/warp-drive/drivespec.py --selftest   # 17 fixtures
python3 research/warp-drive/drivespec.py              # the trade and the point design
python3 research/warp-drive/slingshot.py              # the launcher
```
