# The engine is a coupler, not a source

### A drive that satisfies every energy condition because it has nothing exotic in it

**Status:** working paper. Instrument: `slingshot.py` (stdlib-only, 14 fixtures, `--selftest`).
Primary source for the gain law: Zhang, *Gravitational slingshots around black holes in a binary*,
arXiv:2001.09385 (2020). Nothing in this paper touches the Method volumes; they are research
resources only.

---

## 1. The question was wrong

Fourteen papers in this series asked whether a warp drive can be built, and answered by optimising
the only known object that satisfies all four pointwise energy conditions while carrying a shift
vector — the Fuchs *et al.* warp shell. The answer that came back:

| | |
|---|---|
| shell mass for a 20 m interior | 4.49 × 10²⁷ kg = **751 Earth masses** |
| shell density | 1.53 × 10²³ kg/m³ = **666,000 × nuclear** |
| energy density required | 1.38 × 10⁴⁰ J/m³ |
| best sustained laboratory field (45.5 T) | 8.24 × 10⁸ J/m³ |
| **gap** | **1.7 × 10³¹** |
| top speed after every optimisation in this series | 0.0378 c |
| self-acceleration | **forbidden**, by ADM 4-momentum conservation at positive ADM mass |

No profile, no geometry, no density shaping moves a number like 10³¹. And the two lethal facts —
the mass and the no-self-acceleration theorem — are not independent. They come from **one shared
assumption**, which the series never examined:

> *that the engine is an isolated, asymptotically flat system which **sources** the metric it uses.*

Manufacture the well, carry the well, be the well. Under that definition the answer is no, and it is
no for a reason no engineering can touch: the coupling constant of general relativity is
`c⁴/G = 1.2 × 10⁴⁴ N`. To curve spacetime appreciably you must supply stress of that order. Nothing
made of matter does.

Drop the assumption and both theorems lapse. ADM conservation forbids self-acceleration for an
**isolated** system; it says nothing whatsoever about a system exchanging momentum with an ambient
field. And an engine made of ordinary matter satisfies the null, weak, strong and dominant energy
conditions **trivially** — there is no exotic source, so there is nothing to prove.

**The redefinition.** An engine is not a device that makes a gradient. It is a device that
*modulates its coupling to a gradient it did not make.* A coupler, not a source.

---

## 2. Two couplers, and why one of them is dead

### 2.1 The curvature swimmer — recorded, not pursued

Wisdom (2003) showed that a body performing a **cyclic** change of shape in curved spacetime
undergoes net translation. Ordinary matter, no propellant, no exotic energy; forbidden in Newtonian
gravity, permitted by general relativity. It is exactly a coupler, and it is the obvious first
candidate.

It is also dead, and the reason is a clean bound. The displacement per cycle goes as
`Δs ~ (m₁m₃/M²)·A·L·R` with `A` the stroke area and `R ~ r_s/r³` the curvature. The tidal
acceleration across the *same* body is `a_tide = R c² d`, and with `L ~ d` the curvature cancels:

> **Δs per cycle ≈ (mass factor) · A · a_tide / c²**

The black hole drops out entirely. A swimmer's reach is set by the tide it can survive, divided by
`c²` — and `c²` is 9 × 10¹⁶. A generous machine, 100 m² of stroke area at a survivable 1 g, moves
**2.7 × 10⁻¹⁵ m per cycle**. At a kilohertz that is 3 × 10⁻¹² m/s per second of running. Going to a
bigger or closer black hole does not help: swimming rate and tidal stress are *proportional*, so the
bound is scale-free.

This is a bound, so by P8 it is a coordinate, and it is recorded rather than repaired. **Caveat:**
the estimate above is an upper envelope. A general theory of swimming (arXiv:2211.04654) and the
"swimming versus swinging" critique (gr-qc/0510054) both argue parts of the original effect are
smaller than first proposed — which only strengthens the conclusion. This paper does not depend on
the swimmer's exact magnitude, only on the `1/c²`.

### 2.2 The binary slingshot — the engine

A black hole binary is a **flywheel**. Two masses in relativistic counter-orbit, storing kinetic
energy at a scale nothing built could approach, already assembled, already spinning. A slingshot
taps it. The payload is ordinary matter on a geodesic; all four energy conditions hold with nothing
to check.

Zhang (2020) derived the general-relativistic slingshot formulae for exactly this configuration and
found the property that makes it an engine rather than a one-off kick:

> **The fractional gain in the Lorentz factor per pass is universal in energy** — it does not decline
> as the payload speeds up. (Zhang §3.2.3.)

So `γ` grows **geometrically**: `γ_n = γ₀(1+g)ⁿ`. A payload at `γ = 100` doubles in the same number
of passes as one at `γ = 1`. The gain per pass is near-linear in the hole's own orbital speed,
anchored at Zhang's stated upper limit of **50 % per pass at |v_A| = 0.2 c**.

**A steered vehicle beats a cosmic ray, and this matters.** Zhang notes that averaged over a random
population the law degrades to *second-order* Fermi — quadratic in `|v_A|` — because decelerating
encounters happen as often as accelerating ones. A spacecraft is not a random population. It can
choose the head-on geometry every time, and keeps the **first-order, linear** law. Navigation buys a
whole order in the exponent.

---

## 3. Why the merger clock does not bind a spacecraft

The obvious objection: a binary tight enough to orbit at relativistic speed is about to merge. That
objection is correct, quantitative, and fatal — to *cosmic-ray production*, not to a ship.

For an equal-mass circular binary, `β_A² = r_s/8a`, and combining Peters' merger time with the
orbital period gives a result that depends on **nothing but `β_A`**:

> **N_orbits before merger = (5 / 16π√2) · (a/r_s)^{5/2} = 3.91 × 10⁻⁴ / β_A⁵**

The number of passes a binary can offer is **scale invariant** — identical for a stellar binary and a
supermassive one. And it collides with the gain law in the useful direction:

| `\|v_A\|` | gain/pass | `a/r_s` | orbits left | passes to 0.87 c | passes to γ=10⁹ (Zhang Eq. 31) |
|---|---|---|---|---|---|
| 0.20 c | 0.500 | 3.1 | **1.2** | 1.7 | ~50 ✗ |
| 0.10 c | 0.250 | 12.5 | **38.9** | 3.1 | ~100 ✗ |
| 0.04 c | 0.100 | 78.1 | **3,795** | 7.3 | ~250 ✓ |
| 0.01 c | 0.025 | 1250 | 3.9 × 10⁶ | 28 | ~1000 ✓ |

Zhang needs `γ = 10⁹` and is squeezed: at `|v_A| = 0.2 c` the binary merges long before 50 passes.
A ship needs `γ ≈ 2`. **Three passes.** The clock that kills the cosmic-ray story is not even close
to binding here, and the reason is simply that a spacecraft's target is nine orders of magnitude
lower.

---

## 4. The specification

The one hard constraint is tides, and it bounds the deflector **from below**, because tidal
acceleration at fixed `r_p/r_s` falls as `1/M²`:

> **M_min = c³√(d/a_max) / (2G · (r_p/r_s)^{3/2})**

| payload | tide limit | minimum hole mass |
|---|---|---|
| 20 m hull | 1 g | **27,902 M☉** |
| 20 m hull | 10 g | 8,823 M☉ |
| 2 m probe | 1 g | 8,823 M☉ |

A stellar-mass binary is out of the question — a 2 m probe at 3 `r_s` of a 10 M☉ hole sees
**780,000 g**. The engine must be an **intermediate-mass black hole binary**.

### The worked engine

```
  Two IMBHs of 27,902 M☉ each (5.55e34 kg), circular, |v_A| = 0.10 c
  Separation                       12.5 r_s = 2.06e9 m
  Binary orbital period                215.9 s
  Orbits remaining before merger        38.9
  Passes to reach 0.87 c                 3.1        [ASSUMED: one pass per binary orbit]
  Mission time to 0.87 c               670.7 s  =  11.2 minutes
  Tide across the 20 m hull at r_p = 3 r_s      9.8 m/s^2  =  1.00 g
  Propellant for the transport itself            ZERO
```

**Eleven minutes to 0.87 c at one gravity, with no propellant and no exotic matter.** Against the
shell's 751 Earth masses that cannot accelerate at all.

The ship's own thrust is spent entirely on **steering** — holding the accelerating geometry across
three passes of a chaotic three-body encounter. That is this design's engineering problem, and it is
a **navigation** problem, not a propulsion one. It is the kind of problem that has solutions.

---

## 5. What is not solved, stated plainly

1. **The bootstrap, and it is the big one.** The engine is a *found object*. Reaching an IMBH binary
   is the very problem the drive was meant to solve, and no IMBH binary is confirmed anywhere near
   the solar system. This drive does not get you out of the solar system; it is what you use *once
   you are at one.* Honest consequence: **feasibility reduces to an observational question**, and
   LISA is built to answer exactly it — IMBH binaries are among its design targets. That is a far
   cheaper program than 10³¹.
2. **One pass per binary orbit is ASSUMED**, not derived. Zhang's Fig. 1 shows generic trajectories
   getting fewer deflections than that. A real pass budget needs a three-body integration with a
   steering law, which this paper does not do.
3. **The gain law is an upper envelope.** `g = 2.5 β_A` is anchored on Zhang's stated 50 % at 0.2 c
   and his "roughly, slightly more aggressively than, linear" scaling. It is optimised over impact
   parameter and approach phase — a real trajectory will not sit at the optimum every pass.
4. **Schwarzschild, not Kerr**; patched two-body encounters, not a full three-body integration.
   Zhang notes a spinning hole should *increase* the gain and help prevent capture, so this is
   conservative in the useful direction.
5. **Arrival is uncosted.** A slingshot amplifies; stopping at the far end is a separate problem.
6. **Capture and radiation** at 3 `r_s` of an accreting IMBH are not modelled.

---

## 6. A note on the original design deliverable

M's *Warp Drive Theory* proposed, as Architecture B, two **counter-rotating** cylinders whose angular
momenta cancel, projecting a pinched filament along the axis. Reviewed against the physics
(`ENGINE-ASSESSMENT.md`), the electromagnetic realisation fails by the same ~10³¹ that kills every
sourcing design.

The structural intuition was right. Two masses in relativistic counter-rotation, angular momentum
cancelling, transferring momentum to a payload on the axis, *is* the engine — it simply cannot be
made of copper. It has to be made of black holes, and they have to be found rather than built. The
original document had the topology and the wrong substrate.

---

## 7. Conclusions

1. The 10³¹ gap and the no-self-acceleration theorem share one assumption: that the engine **sources**
   its metric. Dropping it voids both.
2. **An engine is a coupler.** Made of ordinary matter, it satisfies all four energy conditions with
   nothing to prove.
3. The **curvature swimmer** is a real coupler and a dead engine, bounded by
   `Δs ≤ A·a_tide/c²` ≈ 10⁻¹⁵ m/cycle. Recorded as a bound.
4. The **binary slingshot** is a live engine: geometric, non-saturating gain in `γ`, at up to 50 % per
   pass, with zero propellant.
5. A **steered** vehicle keeps the first-order (linear) gain law that a random population loses to
   second-order Fermi averaging.
6. `N_orbits = 3.91 × 10⁻⁴/β_A⁵` is **scale invariant**; the merger clock binds cosmic rays at `γ=10⁹`
   and does not bind a ship at `γ=2`.
7. Tides bound the deflector **below** at ~2.8 × 10⁴ M☉ for a 20 m hull at 1 g: the engine is an
   **IMBH binary**.
8. Worked point design: **0.87 c in 11 minutes at 1 g, zero propellant.**
9. The remaining barrier is not physics but **inventory** — and LISA is the instrument that settles it.

---

## Reproduction

```
python3 research/warp-drive/slingshot.py --selftest   # 14 fixtures, Zhang's printed figures
python3 research/warp-drive/slingshot.py              # the full report
```

## References

- F. Zhang, *Gravitational slingshots around black holes in a binary*, arXiv:2001.09385 (2020).
- J. Wisdom, *Swimming in spacetime: motion by cyclic changes in body shape*, Science **299**, 1865 (2003).
- E. Guéron, C. Maia & G. Matsas, *"Swimming" versus "swinging" in spacetime*, gr-qc/0510054 (2005).
- *General theory of swimming in curved spacetimes*, arXiv:2211.04654 (2022).
- P. C. Peters, *Gravitational radiation and the motion of two point masses*, Phys. Rev. **136**, B1224 (1964).
- J. Fuchs *et al.*, *Constant velocity physical warp drive solution*, CQG **41** (2024) 095009.

---

**Correction note (added later).** This paper applies ADM 4-momentum conservation more broadly than
the theorem supports. ADM forbids an isolated system from accelerating *itself*; it says nothing
about a body in free fall, which changes momentum continuously and violates nothing. The claim binds
the warp shell, which is genuinely a self-accelerating isolated system. It does not bind a coupling
drive, a flyby, or a slingshot, and those should not have been argued against on this basis. The
exact replacement is the centre-of-mass theorem. See `COUPLING.md`.

**Supersession note (added later).** §4's worked engine specifies an **equal-mass** binary. That is
the worst available choice: its Lagrange points are unstable at thirteen times the Routh bound and it
merges soonest. A 25:1 binary gives the same gain per pass with 178x more orbits and stable L4/L5.
The scale-invariant orbit count is 3.8855e-4/beta^5, not the 3.91e-4 quoted here. See
`NAVIGATION.md`, which derives both from M's own three-body result.
