# ACCELERATION

### Why a physical warp drive cannot start, and what starting one would cost

**Prepared under the protocols of The Method v1.6.** Draft v1.0.
Sixth of six. Reads on `WARP-DRIVE.md` §5 and `SHELL-PROFILE.md` §5.

> **Scope.** Writes nothing into `method/` or `drive/`.

> **§3 is WITHDRAWN, 2026-09-06.** It prices a fill-0.1 shell at 4.6 Earth masses of propellant
> against 30.7 and calls it "a 6.67x saving for five per cent of the top speed". The five per cent
> was a 74 % loss: `WHAT-BINDS.md` measures that shell's ceiling at **0.0058 c**, not 0.055 c. The
> propellant saving is real and buys a far slower ship; read the trade off `WHAT-BINDS.md` §1.4
> instead. **Everything else here stands** — the ADM conservation argument, the photon-rocket floor
> of 30.7 Earth masses, and the 4.5e21 multiplier are untouched.

---

## Abstract

Every paper in this series has deferred the same item, and Fuchs *et al.* call it *"one of the
foremost problems in the field of warp drive research"*: their solution is constant-velocity, and
nobody knows how to accelerate it. This paper states why the problem is structural rather than
technical, and prices it.

**The obstruction is a conservation law.** ADM 4-momentum is conserved for an isolated asymptotically
flat system up to what it radiates or ejects to infinity. No internal rearrangement changes it. So a
warp shell with **positive ADM mass cannot self-accelerate** — and positive ADM mass is precisely what
lets it satisfy the energy conditions in the first place. The Alcubierre drive appears to
self-accelerate only because its ADM mass is **zero**, which is the same truncation of the exterior
that forces its negative energy density.

> **The energy conditions and self-acceleration are traded against each other through the ADM mass.**
> A drive that can start itself must have `M_ADM = 0` and therefore violates the energy conditions; a
> drive that satisfies them has `M_ADM > 0` and therefore cannot. This is not an engineering gap in
> either direction. It is the same quantity read twice.

**The price, computed.** Bringing the published shell to its own design speed of 0.04 c requires
supplying **5.39 × 10³⁴ kg m s⁻¹** of momentum from outside. The best any radiative scheme can do is
the photon rocket — and it is the *universal* radiative bound, since massless radiation carries
`p = E/c` and gravitational waves therefore do no better. That bound is **30.7 Earth masses annihilated
at 100 % efficiency into a perfectly collimated beam**, or **1.65 × 10⁴³ J** — 1.4 billion years of the
Sun's entire output. With rest-mass exhaust it is worse: 107 Earth masses at an antimatter-grade
0.3 c exhaust, 370 at a fusion-grade 0.1 c.

**And this is what the shell costs, not what the journey costs.** The same manoeuvre on a bare
1,000-tonne payload needs 4.08 × 10⁴ kg and 3.67 × 10²¹ J. **The shell multiplies the propulsion
problem by 4.5 × 10²¹.**

> A warp drive is not a propulsion system. **It is an inertial-isolation system with a propulsion
> problem attached**, and the isolation makes the propulsion problem twenty-one orders of magnitude
> worse. Fuchs *et al.* and Bobrick–Martire both say the first half; this paper prices the second.

One thing helps, and it is `SHELL-PROFILE.md` §5's design rule. Dropping the fill fraction from the
published 0.667 to 0.1 costs five per cent of the velocity ceiling and saves **6.67×** on the
propellant — 4.6 Earth masses instead of 30.7. It is the only lever in this paper that moves the
number by more than a rounding.

---

## 1. The obstruction is a conservation law

### 1.1 ADM 4-momentum

For an isolated system in an asymptotically flat spacetime, the ADM 4-momentum `P^µ_ADM` is a
well-defined surface integral at spatial infinity, and it is **conserved** up to flux radiated or
ejected through that boundary. Nothing a system does internally — no rearrangement of matter, no field
configuration, no shift vector, no metric engineering — changes it.

A warp shell moving at velocity `v` has `P_ADM = γMv`. If it starts at rest, that momentum must come
from somewhere outside the shell.

> **A positive-ADM-mass warp drive cannot self-accelerate.** Not "cannot yet"; cannot. Any scheme that
> claims otherwise has either radiated something it did not account for, or has `M_ADM = 0`.

### 1.2 The trade

This is not a defect peculiar to the Fuchs shell, and the reason is worth stating carefully.

Bobrick–Martire §3.1 show that the Alcubierre and Natário metrics require negative energy **because
they are truncated** — the exterior is forced strictly flat, so `∫ 4πw r'² dr' = 0` and the total
energy integrates to zero. That is the same statement as `M_ADM = 0`. Fuchs *et al.* build their shell
the other way: a Schwarzschild exterior with **positive ADM mass**, which is what lets the energy
conditions hold.

The two facts are one fact seen twice:

| | `M_ADM = 0` (Alcubierre) | `M_ADM > 0` (Fuchs shell) |
|---|---|---|
| exterior | truncated flat | Schwarzschild |
| energy conditions | **violated**, necessarily | satisfiable |
| momentum to supply for `v` | zero | `γMv` |
| self-acceleration | apparently free | **forbidden by conservation** |

> The Alcubierre drive looks like it can start itself for exactly the reason it is unphysical. Make it
> physical and the starting problem appears, fully formed, as the bill for the ADM mass that made it
> physical.

Schuster, Santiago & Visser reached the same wall from the other side: naively translating the centre
of a positive-mass drive through the timeslices — the "Schwarzschild Drive" — reintroduces negative
energy density throughout space. That is the conservation law asserting itself in coordinates.

---

## 2. The price

### 2.1 What must be supplied

*(COMPUTED, published shell `M = 4.49 × 10²⁷ kg`, target `β = 0.04`.)*

**`P_ADM = γMβc = 5.3886 × 10³⁴ kg m s⁻¹`**

### 2.2 The universal radiative bound

Any massless radiation carries momentum `p = E/c`. Perfectly collimated, that is the best possible
momentum per joule, and it is the same for photons, neutrinos and gravitational waves alike.
**Gravitational-wave recoil is therefore not a cheaper option than a photon rocket; it is the same
bound wearing a different hat.**

Relativistically, `M_i/M_f = √((1+β)/(1−β))`:

| quantity | value |
|---|---|
| mass ratio | 1.040833 |
| propellant, **fully annihilated** | 1.8334 × 10²⁶ kg |
| — in Earth masses | **30.7** |
| energy | **1.6478 × 10⁴³ J** |
| — as total solar output | **1.36 × 10⁹ years** |
| — as world primary energy consumption | 2.7 × 10²² years |

*(COMPUTED.)* This is a floor. It assumes 100 % mass-to-radiation conversion and perfect collimation,
neither of which exists.

### 2.3 With rest-mass exhaust

*(COMPUTED, Newtonian rocket equation at `β = 0.04`.)*

| exhaust | `v_e` | mass ratio | propellant |
|---|---|---|---|
| antimatter-grade | 0.3 c | 1.1426 | **107 Earth masses** |
| fusion-grade | 0.1 c | 1.4918 | **370 Earth masses** |

Lower exhaust velocity costs reaction mass exponentially, and the reaction mass must itself be
accelerated. The photon rocket is not merely better; below about 0.3 c exhaust the problem changes
category.

### 2.4 What the shell costs, as distinct from the journey

The same 0.04 c manoeuvre for a bare 1,000-tonne payload, photon rocket *(COMPUTED)*:

| | propellant | energy |
|---|---|---|
| bare payload, 10⁶ kg | 4.083 × 10⁴ kg | 3.670 × 10²¹ J |
| warp shell, 4.49 × 10²⁷ kg | 1.833 × 10²⁶ kg | 1.648 × 10⁴³ J |
| **ratio** | | **4.49 × 10²¹** |

> The shell exists to give its passengers geodesic transport — to let them arrive without ever feeling
> an acceleration. **That comfort costs twenty-one orders of magnitude in the propulsion budget**, and
> the propulsion is still entirely conventional.

This is the honest summary of what a physical warp drive is. Bobrick–Martire state the qualitative
half plainly — *"any warp drive requires propulsion"* — and Fuchs *et al.* concur. The quantitative
half is the number above.

---

## 3. The one lever that moves it

`SHELL-PROFILE.md` §5 found the velocity ceiling nearly independent of the horizon fill fraction: 0.1
to 0.9 moves the mass ninefold and the ceiling by seven per cent. Priced here *(COMPUTED)*:

| fill | `M` [kg] | `v_max` | propellant (photon) | Earth masses |
|---|---|---|---|---|
| **0.100** | 6.733 × 10²⁶ | 0.0554 c | 2.749 × 10²⁵ kg | **4.6** |
| 0.667 (published) | 4.491 × 10²⁷ | 0.0579 c | 1.833 × 10²⁶ kg | 30.7 |

**A 6.67× saving for five per cent of the top speed.** That is the whole of the good news in this
paper, and it is worth having: it moves the requirement from "annihilate thirty Earths" to "annihilate
five", which is a change of adjective rather than of category, but it is the correct design choice and
it is free.

---

## 4. Routes that do not work, and one that might

**Translating the coordinate centre.** Reproduces the Schwarzschild Drive pathology — negative energy
density throughout space, asymptotically approaching zero. This is the conservation law refusing to be
evaded by a coordinate choice. *(CITED, Schuster–Santiago–Visser.)*

**Gravitational-wave recoil.** Real — binary black-hole mergers reach recoil velocities near
0.017 c — but subject to the same `p = E/c` bound as photons (§2.2), so no cheaper, and the mechanism
requires merging two compact objects, which does not leave a ship. *(CITED + COMPUTED.)*

**Rocket-like mass shedding.** §2.3. Untenable for the reasons priced there.

**Assembly at speed.** The one route the conservation law does not forbid outright: a shell is a
*class of solutions parametrised by `v`*, not one object changing `v` — Bobrick–Martire make this
point sharply. Nothing requires the shell to be *accelerated*; it requires the shell to *exist* in the
moving frame. Build it there and no acceleration ever occurs.

> This does not make the momentum free. It relocates the bill: the construction material must arrive
> in the moving frame, and 4.49 × 10²⁷ kg of it. It is only a gain if the material is *sourced* at
> speed rather than carried there — interstellar matter swept up along the way, for instance.

**Nothing here evaluates whether that is achievable.** It is recorded as the only route in the list
that a conservation law does not close in advance, which is a much weaker statement than promise.

---

## 5. Results

**1. ADM 4-momentum conservation forbids self-acceleration** of any warp drive with positive ADM mass.
Not a technical gap — a conservation law. *(INFERRED from CITED.)*

**2. The energy conditions and self-acceleration are traded through the ADM mass.** `M_ADM = 0` gives
apparent self-acceleration and forces negative energy; `M_ADM > 0` permits the energy conditions and
forbids self-acceleration. The Alcubierre drive is free to start for the same reason it is
unphysical. *(INFERRED — this paper's principal result.)*

**3. The momentum to supply is 5.39 × 10³⁴ kg m s⁻¹**, and the universal radiative floor to supply it
is **30.7 Earth masses annihilated, 1.65 × 10⁴³ J** — 1.4 billion years of total solar output.
Gravitational waves obey the same `p = E/c` bound and are not cheaper. *(COMPUTED.)*

**4. Rest-mass exhaust is worse by category**: 107 Earth masses at 0.3 c exhaust, 370 at 0.1 c.
*(COMPUTED.)*

**5. The shell multiplies the propulsion problem by 4.5 × 10²¹** over a bare payload making the same
manoeuvre. **A warp drive is an inertial-isolation system with a propulsion problem attached.**
*(COMPUTED.)*

**6. Minimising the fill fraction saves 6.67× of that** for five per cent of the top speed — the only
lever in this paper that moves the number, and it is free. *(COMPUTED.)*

**7. Assembly at speed is the only route a conservation law does not close in advance**, and it
relocates the bill rather than cancelling it. *(INFERRED.)*

---

## 6. Open

| item | state |
|---|---|
| whether a shell can be assembled in a moving frame from swept material | the only open route; nothing here evaluates it |
| whether the solution family is continuously deformable in `v` at all | Bobrick–Martire note the family is parametrised by `v`; whether a dynamical path exists between members is unproven either way |
| radiated flux during any such deformation | would show up as exactly the momentum the conservation law demands, and nobody has computed it |
| a numerical-relativity evolution of the Fuchs shell | has never been done, and would settle several items across all six papers |
| whether 100 % conversion and perfect collimation admit any relaxation | §2.2 is a floor; every real scheme is above it |

---

## Appendix · Reproduction

```
python3 research/warp-drive/warpdrive.py --selftest    # 45 fixtures
python3 research/warp-drive/warpdrive.py               # full report
```

---

**Correction note (added later).** This paper applies ADM 4-momentum conservation more broadly than
the theorem supports. ADM forbids an isolated system from accelerating *itself*; it says nothing
about a body in free fall, which changes momentum continuously and violates nothing. The claim binds
the warp shell, which is genuinely a self-accelerating isolated system. It does not bind a coupling
drive, a flyby, or a slingshot, and those should not have been argued against on this basis. The
exact replacement is the centre-of-mass theorem. See `COUPLING.md`.
