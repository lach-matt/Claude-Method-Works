# The steering law was a malformed request

### Applying *The Three-Body Problem for Unknown Masses* to the slingshot engine

**Status:** working paper. Instrument: `navigate.py` (stdlib-only, 15 fixtures, `--selftest`).
Source: M. Lach, *The Three-Body Problem for Unknown Masses — A Closed Index of Families*, the
seated member behind Chapter 36 and registers 1713–1724, with `TB1-README.md`'s reconstruction
record. Nothing here edits the volumes; the chat-67 hold governs.

---

## 1. What I asked for, and why it does not exist

`THE-ENGINE.md` left one pass per binary orbit **ASSUMED** and said a real pass budget "needs a
three-body integration with a steering law". The corpus already answers that, and the answer is that
the request was malformed:

> **Law 4 (Completeness–prediction exclusion).** *The three-body index is complete and therefore
> predictive of nothing. "Completely solvable" and "envelope precision only" are one statement.*

There is no trajectory to integrate toward. What exists is a complete index of **families** —
`E(Λ₃) = 0` on five strata `{KAM, per, chaos, erg, coll}`, exhaustive by the Chazy classification and
disjoint up to measure zero by Saari and Painlevé. By §25.6 the number of predictions an index can
make is `E(X)`, so a complete index makes none. Asking for a computed path is asking a complete index
to be incomplete.

That is not a limitation to work around. It is the specification of what a steering law can be.

---

## 2. Fly the periodic stratum — it is the only one with a flight plan

| stratum | description | usable as a route? |
|---|---|---|
| `chaos` | Bernoulli-shift symbolic dynamics; Brudno: `K(s) ~ h·\|s\|`, `h > 0` | **No finite plan exists** — only real-time correction |
| `KAM` | invariant tori, quasi-periodic, predictable | Tori make no close encounters. **Predictable and useless** |
| **`per`** | **periodic orbits classified by braid words in B₃** (Montgomery 1998; Moore's figure-eight, Chenciner–Montgomery 2000) | **A braid word is finite. It IS the flight plan** |
| `erg` | a distribution `P(ε)` of escape energies | Statistics, not a route |
| `coll` | measure zero (Saari 1971/73) | Regularise or stop |

Brudno's theorem is the operative fact. On the chaotic stratum the Kolmogorov complexity of an orbit
grows at the rate of its entropy, so **no finite description shortens a chaotic path** — a flight
plan for a chaotic trajectory is as long as the trajectory. Zhang's cosmic rays are swept into
exactly that stratum, which is precisely why he needs 50–1000 passes and cannot aim.

A steered vehicle is not a cosmic ray. It flies `per`, and the braid word is the only finite object
in the whole index that can serve as a route.

---

## 3. Navigate by join, never by meet

From the project's own closure test on the triangle form `{|a−b| ≤ c ≤ a+b}` (`caps_table.py`, its
*own* min/max operator, not the book's `tower-2.py`):

| cap | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|
| meet failures | 12 | 111 | 477 | 1488 | 3780 | 8385 | 16812 | 31227 | 54555 | 90705 |
| join failures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Certainty survives upward and dies downward.** Operationally: a steering law may narrow *where the
ship cannot fail to be*, and may never resolve *where it will be*. Brackets combine; they do not
refine. That is Law 3 — `K₃` has treewidth 2 and needs strong 3-consistency where `ℛ` delivers 2, so
the exact region is not a lattice but a monotone envelope.

The engine's guidance system is therefore a bracket propagator, not a trajectory tracker. It is the
same discipline Jacobi's zero-velocity surfaces and Hill's spheres already use, made exact.

---

## 4. The masses need not be known

**Law 5 (Mass-uniformity).** Masses enter through six numbers only — three `c_ij` and three `b_ij`.
The shape sphere, `K₃` and the degree-8 norm are mass-free, and the five fixed points exist for all
thirteen mass order-types (audit 78/78). Changing the masses moves the five points and rescales the
rays; *it cannot create a sixth point, close a meet, or open a join.*

For a real mission this is the difference between possible and not. A vehicle arriving at a binary
whose component masses are known to 20% — which is the state of the art for anything not caught
mid-merger by LIGO — has the **same navigational structure** as one with perfect knowledge. The
uncertainty moves the anchors; it does not change their number, their character, or the topology of
the route.

---

## 5. The design decision that falls out of Routh

L4/L5 are linearly stable iff `μ = m₂/(m₁+m₂) < (9−√69)/18 = 0.0385208965` — computed in
`routh_check.py` as object 7 of the delivery, where the book had only cited it. That is a mass ratio
of **24.96 : 1**.

All rows below at the same light-component speed `β = 0.10 c`, so **the gain per pass is identical in
every row**:

| binary | η | a/r_s | orbits to merger | L4/L5 |
|---|---|---|---|---|
| **equal mass** | 0.2500 | 12.5 | **39** | unstable |
| 4:1 | 0.1600 | 32.0 | 637 | unstable |
| **25:1** | 0.0370 | 46.2 | **6,909** | **STABLE** |
| 100:1 | 0.0098 | 49.0 | 30,171 | STABLE |

`THE-ENGINE.md` specified an **equal-mass** binary, and that is the worst available choice on every
axis at once:

- its Lagrange points are unstable at `μ = 0.5`, **thirteen times the Routh bound**, so every
  station-keeping manoeuvre between passes is a fight against a divergence;
- it is the tightest configuration at a given light-body speed, so it merges soonest;
- and it gains nothing for it, because the light component's speed — which sets the gain — is a free
  parameter matched across the table.

A **25:1 binary** sits just inside the Routh bound. Same gain per pass, **178× more orbits**, and
stable L4/L5 to station at between passes. The lighter body also moves faster than either component
of an equal-mass binary at the same total mass and separation, by a factor approaching 2.

**`THE-ENGINE.md`'s equal-mass point design is superseded.** The correction came from a threshold the
corpus had already computed and this project had not thought to ask for.

---

## 6. What remains ASSUMED

**Which braid word, and its drift rate.** And there is a real tension to resolve first: strict
periodicity conserves the Jacobi constant and therefore *forbids secular gain* — a closed orbit
returns exactly what it takes. The gain exists because the binary is **not stationary**. Zhang says
so explicitly: *"E is only conserved during each individual slingshot, and not when the geodesic is
threading through the binary, whose metric is not stationary."*

So the flight plan is a braid word that **drifts**, and its drift is fed by the inspiral. **The gain
and the deadline are one mechanism** — which is why the scale-invariant orbit count
`N = 3.8855 × 10⁻⁴/β⁵` is the right budget and not a coincidence.

Selecting the word is open. That it must be a *word* and not a *trajectory* is now settled.

---

## 7. A correction found on the way

Checking `navigate.py` against `slingshot.py` surfaced two fixtures in the latter that were wrong and
had passed on a 6% tolerance: the equal-mass orbit count at `β = 0.1` is **38.856**, not the 39.08 I
hand-computed, and at `β = 0.04` it is **3794.5**, not 3813. The scale-invariant constant is
**3.8855 × 10⁻⁴/β⁵**, not the 3.91 × 10⁻⁴ quoted in `THE-ENGINE.md`. The code was right in both
instruments; the hand-checked fixtures were not, and the tolerance was too loose to catch them. Both
are now pinned to 1 × 10⁻⁴.

---

## 8. Conclusions

1. **A steering law that computes a trajectory cannot exist.** Law 4: the three-body index is
   complete, and a complete index makes zero predictions. The request in `THE-ENGINE.md` was
   malformed.
2. Navigation is by **stratum and family**. Of the five strata, only `per` carries a finite
   description — **a braid word in B₃ is the flight plan**, and Brudno's theorem says it is the only
   candidate.
3. Guidance propagates **brackets upward and never refines downward**: 0 join failures at every cap
   against meet failures growing to 90,705.
4. **The masses need not be known** (Law 5), which is what makes a real mission possible.
5. **Use a 25:1 binary, not an equal-mass one**: same gain per pass, 178× more orbits, and stable
   L4/L5 — from the Routh threshold `(9−√69)/18`.
6. The braid word must **drift**, fed by the inspiral; **the gain and the deadline are one
   mechanism.**

---

## Reproduction

```
python3 research/warp-drive/navigate.py --selftest   # 15 fixtures, the corpus's own figures
python3 research/warp-drive/navigate.py              # the strata, the closure table, the trade
```

## Source

M. Lach, *The Three-Body Problem for Unknown Masses — A Closed Index of Families*
(`method/members/The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md`; Chapter 36; registers
1713–1724; `TB1-README.md` for the reconstruction record and the 78/78 audit).
