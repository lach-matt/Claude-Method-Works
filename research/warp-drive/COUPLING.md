# The drive is a coupling

### There is no acceleration created by the drive; the pull comes from the far side

**Status:** working paper and a correction. Instrument: `coupling.py` (stdlib-only, 12 fixtures,
`--selftest`). Nothing here touches the Method volumes.

---

## 1. A correction: ADM was over-applied

Six papers in this series treated ADM 4-momentum conservation as a general prohibition on drives,
writing "the shell cruises; it cannot start itself" and reading it as a wall across the whole
programme. **That is too strong, and the over-application was mine.**

What the theorem says: *an isolated system cannot change its own total 4-momentum.* What it does not
say: anything at all about a body in **free fall**. A falling body changes its momentum continuously,
and violates nothing, because the field supplies the momentum. It is not an isolated system.

So a drive that never pushes on itself is **outside the theorem's scope**. Every time this series
invoked ADM against a coupling mechanism, it was invoking a theorem about a different object.

The theorem still binds the **warp shell** of `THE-DRIVE.md`, because a shell trying to translate
itself is precisely the isolated self-accelerating system ADM forbids. It does not bind the drive
described here.

---

## 2. The frame

> The drive creates no acceleration. It establishes a **coupling** to the destination, and the
> destination pulls. The ship is on a geodesic the whole way and feels nothing.

No thrust. No reaction mass. No exhaust. No power plant sized to the trip. The interior is in free
fall from departure to arrival, which is the same comfort the warp shell buys at 10⁴⁶ J — obtained
here for nothing, because falling is free.

This also removes the launch problem the shell had. There is no ignition and no burn: you release,
and you fall.

---

## 3. What actually binds — two things, and neither is ADM

### 3.1 The pull must come from mass you did not bring

The tempting bootstrap: project mass ahead, let it collapse, fall toward it, repeat. It is exactly
the "pull/collapse ignition" the original design deliverable reached for, and it fails **identically,
not approximately**:

> **M_total · a_cm = Σ(external forces) = 0**

Any *internal* coupling — gravitational tractoring included — moves the parts and never the whole.
Measured over projectile masses spanning twelve orders of magnitude, the centre-of-mass displacement
after ship and projectile fall together is zero to machine precision (1.2 × 10⁻¹⁶ relative, which is
double-precision epsilon, not physics).

This is the precise, coupling-language content of what ADM was gesturing at, and it is the version
worth keeping: **a coupling drive is legitimate; a self-coupled one is not.** The mass at the far end
has to be already there.

### 3.2 The reach is the depth of the destination's well

Falling from rest at large distance to distance `d` from mass `M`:

> **v = c √(r_s/d)**

which is `THE-BORROWED-WELL.md`'s closed form, and it is the entire performance of a coupling drive.

| destination | arrival speed | pull | fall time from 1 pc |
|---|---|---|---|
| Sun, at 1 AU | 0.00014 c | 6 × 10⁻⁴ g | 16.6 Myr |
| Sun, at its surface | 0.0021 c | 28 g | 16.6 Myr |
| Sirius B (white dwarf) | 0.023 c | 4 × 10⁵ g | 16.4 Myr |
| neutron star, at 100 km | 0.203 c | 1.9 × 10⁹ g | 14 Myr |
| 10 M☉ BH, at 100 r_s | 0.100 c | 1.6 × 10⁷ g | 5.2 Myr |
| **Sgr A\*, at 10 r_s** | **0.316 c** | **3.6 × 10³ g** | **8 × 10³ yr** |

Relativistic arrival needs `d ~ 100 r_s` or closer — the thing you couple to must be **compact**.

Note the last row against the rest. Sgr A\* gives 0.316 c at a *survivable-order* 3,600 g and an
8,000-year fall, because tides and fall time both improve with mass while `v = c√(r_s/d)` at fixed
`d/r_s` does not depend on it at all. **Coupling favours the largest available mass** — the same
`1/M²` tidal scaling that made an IMBH the minimum instrument for the flyby.

---

## 4. The bind, stated exactly

> **Depth and habitability are anti-correlated.**

Couple to somewhere you would want to *be* — a star, a planetary system — and the well is shallow:
falling on the Sun from interstellar distance buys 42 km/s, which crosses 4.2 ly in 30,000 years.
Couple to something deep enough for a relativistic pull and the destination is a black hole, which is
not a place.

That is the real constraint on a coupling drive. Not ADM. Not the energy conditions. Not 10³¹.

---

## 5. Where it breaks open

Falling in is free **and arriving is automatic** only when the mass you couple to *is* the
destination. Otherwise the well gives back on the way out exactly what it gave on the way in:

> **A static well is a lens, not a pump.**

A **moving** well is a pump. That is the one loophole, and it is not small — it is the slingshot of
`THE-ENGINE.md`, where the closed form stops being

  `Δv = c√(r_s/b)`   (bounded by the well's *depth*)

and becomes

  **`Δv = 2U/(1+U²)`**   (bounded by the well's *speed*).

Depth is capped by what you can survive. Speed is not. That is how a coupling drive reaches 0.87 c
without ever accelerating itself, and it is why the binary — two deep wells already moving at 0.1 c —
is the right object to couple to.

**The two loopholes are the same loophole.** A binary is a moving well; the slingshot is a coupling;
the gain per pass does not saturate. Read in this frame, `THE-ENGINE.md` is not a separate proposal
from the borrowed well — it is the borrowed well with the one modification that turns a lens into a
pump.

---

## 6. What this changes in the series

- **Withdrawn:** the blanket use of ADM against coupling mechanisms (`ACCELERATION.md`,
  `THE-ENGINE.md` §1, `THE-DRIVE.md` §5 as a general claim). ADM still binds the *shell*, which is
  genuinely a self-accelerating isolated system; it never bound the flyby, the slingshot, or the
  borrowed well, and those papers should not have been written as though it did.
- **Stands:** the centre-of-mass theorem replaces it, and is stronger where it applies — it kills the
  collapse-ignition bootstrap exactly rather than by an order-of-magnitude argument.
- **Reframed:** `THE-BORROWED-WELL.md` is not a curiosity beside the engine. It is the engine's
  static limit, and `THE-ENGINE.md` is what it becomes when the well moves.

---

## 7. Conclusions

1. **The drive creates no acceleration.** It is a coupling; the destination pulls; the ship is
   geodesic throughout and feels nothing. There is no ignition and no burn.
2. **ADM does not apply to it.** The theorem forbids self-acceleration, not falling. This series
   over-applied it and that is withdrawn.
3. What replaces it is exact: **an isolated system cannot move its own centre of mass.** The pull
   must come from mass you did not bring. Collapse-ignition fails identically.
4. Reach is **v = c√(r_s/d)**, so the coupling target must be **compact**, and — because tides and
   fall time both improve as mass rises while the speed law does not care — **as massive as
   available**.
5. The binding constraint is that **depth and habitability are anti-correlated**.
6. **A static well is a lens; a moving well is a pump.** `Δv = 2U/(1+U²)` is bounded by the
   deflector's speed rather than its depth, and speed has no survivability cap. That is the whole
   engine.

---

## Reproduction

```
python3 research/warp-drive/coupling.py --selftest   # 12 fixtures, textbook values
python3 research/warp-drive/coupling.py              # the depth table and the bind
```
