# Wall C, third piece: what the global bulk must do, for a held corridor and for a lasting one (M-RULINGS items 86, 136, 149; computed, deduced and READ; verified once; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)". The first draft put the hold's bound on a slice that never
reaches the throat, said the global bulk "does not bear on the corridor during its hold", copied the series radius in as
constants, and presented Maartens–Koyama's eq. (155) coefficient as the Randall–Sundrum II far field. All four are
corrected (History).

## What you said

- **Item 136 E:** the hold is *"Instantaneous or near instantaneous"*.
- **Item 86, answer 5 (H-BRIEF-HOLD):** *"incredibly short, maybe even immeasurable but not zero"*, and *"this answer is
  also a relative one"*.
- **Item 149:** *"You have to work the math now"*.
- **The instrument:** `globalbulk.py`. It imports throatbulk.py, kscale.py, bulkseries.py and stability.py by path.
  Selftest 6/6.
  - **Genuine checks:** three. Two more re-read checked numbers from their owners.
  - **Control:** one.
  - **Marked STRUCTURAL:** one.

## What passes

### 1. A held corridor's evolution is decided by local data (G1)

- **Stated invariantly:** the part of the plane inside the five-dimensional domain of dependence of a slab of bulk data
  around the plane is determined by that slab alone.
- **This rests on finite propagation, with the plane as a timelike boundary carrying its junction condition.** That makes
  it an initial–boundary value problem, not the standard Cauchy problem. So it is labelled H-IBVP, the board's.
- **The slab cannot sit on a static slice.** Static slices never reach the throat: the proper radial distance diverges
  logarithmically there.
  - It lies on a slice through the horizon, in stability.py's (v, ρ) chart.
  - It must span the plane laterally.
  - Its thickness δ(r) is known only at the throat.
- **There δ is the series radius**, imported from bulkseries.py:
  - 1.29m to 1.46m when ℓ = r₀;
  - 2.70m to 3.16m when ℓ ≫ r₀.
  - In the corridor's clocks m/c, along the chart's advanced time, that is a span of order one to three clocks:
    **0.9×10⁻³⁶ s to 2.1×10⁻³⁶ s at the board's example README.**
  - This holds for ℓ ≳ r₀ only. Under H-ONE-BIT-SCALE, ℓ ≪ r₀, the span shrinks by about √N (OPEN).
- **This is an estimate of order** (H-DELTA-ORDER). Your *"relative"* bears on it, because near a degenerate horizon the
  conversion to other clocks is unbounded.
- **What G1 shows, and what it does not.**
  - It shows that the hold's evolution does not depend on which global extension exists.
  - It does not make existence irrelevant: some regular extension of the slab data must exist for there to be a spacetime
    at all.

## What does not pass: a lasting static corridor

### 2. Eq. (17) on the whole plane cannot sit in a Randall–Sundrum II bulk with a compact core (G2)

- **Your corridor's own Weyl term at large r** is r²E^θ_θ = −m/(4r) (computed). It is a tail independent of ℓ.
- **A black hole on that bulk falls off as ℓ²/r³.**
  - In Maartens–Koyama's eq. (155) form (READ in throatbulk.py; MK place the eq. (41) correction in H only), it is
    +2ℓ²m/(3r³), and the ratio to the corridor's term is −(3/8)(r/ℓ)².
  - Garriga–Tanaka's full linear metric (not READ; the verifier's) gives +3ℓ²m/r³, and a ratio of −(1/12)(r/ℓ)².
  - **The robust content is the fall-off: 1/r against ℓ²/r³, a ratio unbounded as r grows.** The coefficient and sign
    are not the Randall–Sundrum II far field.
  - **Control:** the Schwarzschild member reads no Weyl term.
- **Equivalently:** γ = 5/4 for your corridor (kscale.py, Casadio–Fabbri–Mazzacurati eq. 8), against γ = 1 + O(ℓ²/r²)
  (Maartens–Koyama eq. 41, p.10).
- **So KSCALE.md's way out (c), read as eq. (17) on the whole plane, does not survive for a lasting corridor.**
  - Its weaker form is not addressed: eq. (17) in the near zone only, matched to a γ = 1 exterior beyond a few ℓ.
  - KSCALE's own sentence already held the argument: *"an ℓ-independent 1/r term. That bulk does not produce it."*
- **One step is the board's extension (H-COMPACT-CORE).** A compact core acts at r ≫ ℓ as a compact source in the linear
  theory. The hypothesis includes regularity at the Poincaré horizon.

### 3. So the two readings of the hold part (G3)

- **Under H-BRIEF-HOLD,** the hold's evolution is local (G1).
- **A lasting corridor** needs a bulk whose departure from Randall–Sundrum is not compact: one that reaches the bulk's
  far horizon, as the black string's does (Maartens p.19, READ in CLOSEDBULK.md and MANYPLANES.md). No such bulk is
  built here.
- **CENSOR5D.md bears on this from censorship.**
  - A departure from Randall–Sundrum that reaches the far horizon meets every far sphere centred on the plane. That is
    its escape (b).
  - Theorem W binds the whole spacetime, however brief the hold. So G1's locality concerns the hold's dynamics only, not
    whether the corridor is permitted at all.

## Named hypotheses

- **Yours:**
  - H-BRIEF-HOLD (86.5), with its *"relative"*;
  - item 136 E;
  - H-STATIC-PLANES (141);
  - M-WORK-THE-MATH (149).
- **The board's:**
  - H-BK-CORRIDOR;
  - H-ONE-PLANE-NEAR;
  - H-COMPACT-CORE (with regularity at the Poincaré horizon);
  - H-DELTA-ORDER;
  - H-IBVP;
  - H-NO-LASTING-FIELD (STATIC.md). G1 is what that hypothesis needs in the bulk.

## OPEN

1. A lasting corridor's bulk: a departure from Randall–Sundrum reaching the far horizon. Is it regular?
2. G1 made exact: the domain of dependence computed in the series' own metric, along the whole plane.
3. G1 for ℓ < r₀ (bulkseries OPEN 2).
4. How the hold starts and ends. G1 covers the hold itself, not its making (CHAIN.md's H-PRIOR-SETUP).
5. Way out (c) in its weaker form: eq. (17) near the throat, matched to a γ = 1 exterior.

## History (verifier, 2026-10-07)

One must-fix and five should-fix, all applied:

1. **G1 had no well-defined slice or observer.** Static slices never reach the throat. G1 is now stated invariantly, as
   a domain of dependence of a slab on a slice through the horizon, with δ known only at the throat.
2. **δ was used outside the range computed.** The figure is now scoped to ℓ ≳ r₀.
3. **"Finite propagation (standard)" understated the problem.** It is an initial–boundary value problem: H-IBVP.
4. **"Does not bear on the corridor during its hold" was too strong.** Existence of some extension still matters.
5. **The series radius was copied in as constants.** It is now imported from bulkseries.radius_estimates().
6. **The black hole's coefficient is Maartens–Koyama's loose form.** The fall-off is now the claim. Eq. (41) is cited at
   p.10, and way out (c) is scoped.

The notes are taken up too: H-COMPACT-CORE names regularity at the Poincaré horizon, and the counts of genuine checks are
stated plainly.
