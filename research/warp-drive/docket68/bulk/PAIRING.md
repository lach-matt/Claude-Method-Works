# What shape of the higher dimension makes a destination close (BULK-O1; verified once; SEATED in ledger.py section 8j on M's item 64; 2026-10-05)

*Headed before seating* "(BULK-O1; verified once; not seated; 2026-10-05)". *First headed* "(BULK-O1; not verified; not seated; 2026-10-05)".

## What M asked

M's order (rulings item 59) was *"4, then 3 please."*: `bulk.py` seated (done, section 8i), then the pairing shape,
then entering and leaving (O6). M's H-DETACH and H-CORRIDOR-STASIS are folded into O6 (item 61).

**The question.** `bulk.py` found that whether the corridor lands far away depends on the shape of the higher dimension.
So: what shapes make two far-apart places close through it, and what does each shape need?

H-HIGHER-CORRIDOR, H-NO-SPEED and H-UNOBSERVED-UNBUILT (item 62: this is part of the device line of work) are carried
as M's hypotheses, never as results. O9 stays OPEN.

Every number below is printed by `pairing.py`.
- **Selftest:** 5/5 checks, 2 of them controls, with 4 STRUCTURAL lines printed and not counted.
- **Method:** it computes the stress-energy symbolically with sympy, and it asks `bulk.py` for the Chung–Freese and
  Proxima inputs.
- **Constants:** its Sun, Earth, AU and Proxima constants are restated from `cmb/localclock.py` and `seat.py`. The
  selftest checks each one against its owner.

## Sources READ (2026-10-05, via alphaXiv)

- **Chung & Freese** (hep-ph/9910235v2).
  - Eq. 3 (p.3) and eq. 37 (p.8).
  - "Patched" (p.4) and "fine tuned" (p.8).
  - §II B–C (pp.5–7), a fourth shape (below).
- **Ishihara** (gr-qc/0007070v2).
  - A brane carrying matter is "concave towards M in the null direction", giving bulk shortcuts (eq. 11, p.5).
  - "The magnitude of the apparent causality violation becomes larger when the matter on the brane becomes more dense"
    (p.5).
  - Near the initial singularity there is "no particle horizon" (pp.7–8).
- **Caldwell & Langlois** (gr-qc/0103070v1).
  - At high brane energy, the ratio of the bulk to brane horizon reaches about 10³, or about 10⁴ on the
    Big Bang nucleosynthesis constraint alone (eq. 25, p.7).
  - For a local body the shortcut is negligible, λ ∼ 10¹³ cm for the Earth (p.8). That figure rests on their stated
    assumption that ℓ/λ plays the role of ℓH.
- **The Manyfold** (ADDK, hep-ph/9911386v1).
- **Gao & Wald** (gr-qc/0007021v2): two time-delay theorems, each needing the null energy condition (NEC, "R_ab k^a k^b ≥
  0", eq. 2) and the null generic condition.
  - Theorem 1 (a null-geodesically complete spacetime): the fastest null paths between far points avoid a given
    compact region. Gao and Wald hedge its interpretation themselves: "it is difficult to make a strong argument for
    this interpretation" (p.5).
  - Theorem 2 (a timelike conformal boundary): the fastest path between boundary points lies in the boundary, so
    "generic perturbations of anti-de Sitter spacetime always produce a time delay" (abstract).
  - **Scope (STRUCTURAL):** neither theorem covers these shapes.
    - A brane is not AdS's conformal boundary, so Theorem 2 does not apply.
    - Theorem 1 needs null-geodesic completeness and the null generic condition. A slab of bulk bounded by branes, and a
      flat bulk, are not shown to meet them.

## Three published shapes, and what each needs

**These three are surveyed, not exhaustive (H-THREE-ROUTES).** Chung–Freese's own §II B–C give a fourth: a curved brane
in a flat bulk, with continuous, unpatched shortcuts (eq. 25, p.6). It needs no NEC violation, and its price is an
inhomogeneous universe with a singular special point (p.7). Kalbermann & Halevi, *Nearness through an extra dimension*
(gr-qc/9810083, CF's ref. 4), is NAMED-NOT-READ.

### 1. A warped second plane (Chung–Freese)

- **What the higher dimension must contain.** Computed from their metric, the Einstein tensor is G^M_N = (−6, −3, −3,
  −3, −3)·k². That reproduces their own eq. 37, which is the check.
- **The null energy condition is violated in every null direction.**
  - For a general null vector over three angles, R_ab k^a k^b = −3k², because static Chung–Freese is ultrastatic (ℝ × H⁴).
  - In matter terms, ρ + p = −3k²/κ₅² < 0.
  - **Control:** Randall–Sundrum's bulk gives exactly zero; a pure cosmological constant saturates the condition.
- **This is the price of Chung–Freese's exponential warp, not of every warp.**
  - **Control, computed:** a static warp with time unwarped and e^{3B} = 1 − cu² still compresses the hidden plane's
    distances. It gives ×4.64 at cL² = 0.99, with the NEC **positive** in both directions. It pays instead with a
    curvature singularity at u = 1/√c.
  - Junction conditions may move the price onto the hidden brane. On the verifier's reading of CF eq. 36 with the normal
    reversed (H-ORIENTATION), Chung–Freese's own hidden brane has ρ + P < 0.
  - **Whether every warp that brings a destination close needs NEC violation somewhere is OPEN.**
- **The early universe does not rescue it.** With Chung–Freese's time-dependent metric in the radiation era (a ∝ t^{1/2}),
  the NEC holds only at kt ≲ 0.1: it is +42k² at kt = 0.1, −4.67k² at 0.3 and −3.13k² at 23. The path needs kt > 2kL ≈
  23 before it can be completed.
- **Treating this as the bulk analogue of D5 (Olum) is a hypothesis (H-D5-ANALOGUE).** D5 prices faster-than-light travel
  in NEC violation for leads *without* a reference geometry. Chung–Freese's shortcut is a lead against the brane's own
  geometry.
- **Design figures for the Proxima span,** at L = 1 mm, on Chung–Freese's patched, fine-tuned path:

  | our clock reads | warp needed, kL | distance compression | k |
  |---|---|---|---|
  | 1 year | 1.45 | 4.25× | 1.45×10³ /m |
  | 1 day | 7.35 | 1.55×10³ | 7.35×10³ /m |
  | 1 hour | 10.52 | 3.72×10⁴ | 1.05×10⁴ /m |
  | 1 second | 18.71 | 1.34×10⁸ | 1.87×10⁴ /m |

  - Chung–Freese's own value is kL ∼ ln 10⁵ = 11.51 (p.4). The one-second row lies beyond it.
  - The table inverts the static reading, which is arithmetic, not a test (STRUCTURAL).
  - The violation's size is set by k. Pricing it in kg/m³ needs the 5D Planck scale, which no source fixes (H-M5).
  - `SEARCHES.md`: these values of 1/k (53–691 μm) lie inside the range the torsion balances tested.

### 2. A bent plane (Ishihara)

- **No NEC violation needed:** the AdS bulk saturates it, as in the Randall–Sundrum control. (An AdS bulk does have a
  negative energy density; the NEC is what separates the shapes.)
- **Where the shortcut comes from:** matter on the brane bends it, and the shortcut grows with the matter's density.
- **At brane densities above the brane tension** the shortcut reaches up to about 10³ in distance (Caldwell–Langlois, p.7).
  Near the initial singularity Ishihara finds no particle horizon.
- **For today's local bodies it is negligible.** Caldwell–Langlois's estimate for the Earth is ∼10¹³ cm; the 2.42×10¹³ cm
  figure is computed here from IAU constants with their formula.
- **So this shape needs extreme density on the plane itself.**

### 3. A folded plane (the Manyfold)

- **No NEC violation needed:** the bulk is flat.
- **Light sees no fold locally.** Folding is extrinsic, so light reaches the other fold only by going round the tip, the
  long distance along the plane ("old light", p.3).
- **Gravity crosses the higher dimension.** ADDK name "two different minimal distances: gravitational … and
  electromagnetic" (p.2). In their model the gravity of matter on nearby folds **is felt**: "Nearby matter on other
  folds can be detected gravitationally as dark matter" (abstract).
- **Proxima is not close through the higher dimension to the solar system.**
  - At planetary distances, much larger than the bulk's size, gravity is 4D; that is ADDK's own dark-matter premise.
  - So Proxima's mass, within about 1 mm of any point in the solar system through the bulk, would pull like a
    0.12 M☉ body there. At 1 AU that is **7.24×10⁻⁴ m/s², 12.2 % of the Sun's pull** (H-FOLD-NEWTON).
  - H-FOLD-NEWTON is 4D Newton, which is a **floor** when the gap is no larger than the bulk: below that size gravity is
    (4+N)-dimensional and stronger (ADDK p.10, eq. 32).
  - The point-mass figure at 1 mm (1.6×10²⁵ m/s²) is an idealisation.
  - **This rules out one fold arrangement for one star. It does not rule out the fold shape.**
- **The fold must be held open.** A folded brane "becomes unstable, with a tendency to collapse" (ADDK p.21). ADDK then
  give mechanisms, a kink and anti-kink pair and a fold at a domain wall, and conclude "a Manyfold universe may be stable
  despite the tendencies towards self-annihilation" (p.23).
- `SEARCHES.md`: in a flat higher dimension shaped like a circle, a gap is at most about 94 μm (torsion balances).

## For M

- **Of the shapes surveyed (not exhaustive, H-THREE-ROUTES), each that brings a far place close pays a different price:**
  - **Warping the other plane, Chung–Freese's way,** needs matter in the higher dimension that violates the null energy
    condition. That is the same kind of price the board found for faster-than-light travel in four dimensions; whether
    it is the same theorem is a hypothesis (H-D5-ANALOGUE). A different warp avoids it but sits beside a singularity.
    Whether every warp pays it somewhere is OPEN.
  - **Bending the plane** needs extreme density on the plane itself, as in the early universe.
  - **Folding the plane** needs nothing that violates the condition.
- **On your picture, the fold matters most.** ADDK's own words fit it: "two different minimal distances: gravitational …
  and electromagnetic". It is your "position 1, then position 2", two places far apart to light and close through the
  higher dimension.
  - In the fold model, the places that are close through the bulk are exactly the ones light cannot reach quickly.
    Their gravity **is** felt, and ADDK propose it is what we call dark matter.
  - So the fold's candidate destinations are far to light and near to gravity, and that is consistent with what we
    observe. Proxima is not one of them. ADDK favour fold tips beyond the Hubble radius (p.5; the deuterium argument,
    p.10).
- **Your next step, O6,** now has a sharper question: what can cross a fold or a warped bulk, and how does it go in and
  come out? That is where your three states sit (leaving, stasis in the corridor, arriving).

## Named hypotheses

- **H-THREE-ROUTES:** the shapes surveyed, not shown to be exhaustive (a SURVEY).
- **H-CF-STATIC:** Chung–Freese's static reading.
- **H-L-ILLUSTRATIVE:** L = 1 mm.
- **H-FOLD-NEWTON:** 4D Newton for gravity through a fold, a floor when the gap is no larger than the bulk.
- **H-D5-ANALOGUE:** route 1 as the bulk analogue of D5.
- **H-ORIENTATION:** the junction reading of CF eq. 36 with the normal reversed.
- **H-M5:** the 5D Planck scale, unfixed.
- **M's hypotheses:** H-HIGHER-CORRIDOR, H-NO-SPEED, H-BULK-PAIRING and H-UNOBSERVED-UNBUILT.

## OPEN

1. A shape outside those surveyed (Chung–Freese §II B–C is one; Kalbermann & Halevi is NAMED-NOT-READ), or a proof that
   a list is exhaustive.
2. Whether every warp that brings a destination close needs NEC violation somewhere (in the bulk or on the hidden
   brane).
3. The 5D Planck scale that prices route 1 in kg/m³.
4. An ephemeris bound on how close through the bulk an observed star can be to the solar system.
5. A stabilised fold at a gap that carries anything (ADDK give toy mechanisms, not a gap).

## History (verifier, 2026-10-05; first-written claims kept)

- **"The null energy condition is violated in every direction tested"** covered three directions. It is now computed for
  a general null vector.
- **"Negative-energy-type matter" and "No negative energy needed"** were wrong: an AdS bulk has negative energy density
  too. What separates the shapes is the NEC.
- **"Warping the other plane … needs negative-energy-type matter … That is the bulk analogue of … D5"** stated the price
  for any warp, and the analogy as fact. It is Chung–Freese's warp's price, a NEC-keeping warp exists, and the analogy
  is H-D5-ANALOGUE.
- **Gao–Wald's scope.** It was said that route 1 "evades both theorems' premise by violating the NEC". Neither theorem's
  other premises are shown to hold for any of the shapes.
- **H-FOLD-NEWTON was glossed as** "4D Newton at r, as ADDK's own sub-mm folds assume gravity is 4D at the fold gap".
  ADDK say gravity is not inverse-square there (p.10, eq. 32), so 4D Newton is a floor. The headline is now the 1 AU
  figure.
- **"So the observed Proxima is not close through the higher dimension"** and **"nothing with mass can sit close
  through the fold without being felt"** undersold the fold. In ADDK such matter is felt, as dark matter, and the
  finding is one arrangement for one star.
- **"It needs stabilization (ADDK §7)"** omitted ADDK's own stabilising mechanisms.
- **"The three published shapes"** omitted Chung–Freese §II B–C.
- **"Caldwell–Langlois's scale for the Earth is 2.4×10¹³ cm"** presented a computed figure as READ. Caldwell–Langlois
  print ∼10¹³ cm under an assumption.
- **"Chung–Freese's own value is kL = 11.51"** now carries its source: "kL ∼ ln(10^5)", p.4.
- **The design inversion was counted as a check.** It is an identity round trip, now STRUCTURAL; the selftest is now 5/5
  with 2 controls, from 4/4 with 1.
- **The dense-brane regime** of route 2 was READ, then dropped. It is now carried.
- **The constants** were said to be asked of `seat.py`. They are restated, and the selftest checks them against their
  owners.
