# What shape of the higher dimension makes a destination close (BULK-O1; not verified; not seated; 2026-10-05)

## What M asked

M's order (rulings item 59) was *"4, then 3 please."*: `bulk.py` seated (done, section 8i), then the pairing shape,
then entering and leaving (O6). M's H-DETACH and H-CORRIDOR-STASIS are folded into O6 (item 61).

**The question.** `bulk.py` found that whether the corridor lands far away depends on the shape of the higher dimension.
So: what shapes make two far-apart places close through it, and what does each shape need?

H-HIGHER-CORRIDOR and H-NO-SPEED are carried as M's hypotheses, never as results. O9 stays OPEN.

Every number below is printed by `pairing.py`. Its selftest runs 4/4 checks, 1 of them a control, with 3 STRUCTURAL
lines printed and not counted. It computes the stress-energy symbolically with sympy, and it asks `bulk.py` for its
inputs.

## Sources READ (2026-10-05, via alphaXiv)

- **Chung & Freese** (hep-ph/9910235v2), eq. 3 and eq. 37 (p.8).
- **Ishihara** (gr-qc/0007070v2).
  - A brane carrying matter is "concave towards M in the null direction", which gives bulk shortcuts (eq. 11, p.5).
  - "The magnitude of the apparent causality violation becomes larger when the matter on the brane becomes more dense"
    (p.5).
- **The Manyfold** (hep-ph/9911386v1).
- **Gao & Wald** (gr-qc/0007021v2): two time-delay theorems under the null energy condition.
  - Theorem 1 (a null-geodesically complete spacetime): the fastest null paths between far points avoid a given compact
    region.
  - Theorem 2 (a timelike conformal boundary): the fastest path between boundary points lies in the boundary, so
    "generic perturbations of anti-de Sitter spacetime always produce a time delay" (abstract).
  - **Scope:** a brane is not AdS's conformal boundary, so Theorem 2 does not apply to brane-worlds directly.

## The three published shapes, and what each needs

### 1. A warped second plane (Chung–Freese)

- **What the higher dimension must contain.** Computed from their metric, the Einstein tensor is G^M_N = (−6, −3, −3,
  −3, −3)·k². That reproduces their own eq. 37, which is the check.
- **The null energy condition is violated in every direction tested** (R_ab k^a k^b = −3k²).
  - **Control:** Randall–Sundrum's bulk gives exactly zero; a pure cosmological constant saturates the condition.
- **What this means.** Warping the other plane so that it brings a destination close needs **negative-energy-type
  matter in the higher dimension**. That is the bulk analogue of the board's 4D theorem D5 (Olum), which puts the same
  price on faster-than-light travel (H-D5-ANALOGUE).
- **Design figures for the Proxima span,** at L = 1 mm, on Chung–Freese's patched, fine-tuned path:

  | our clock reads | warp needed, kL | distance compression | k |
  |---|---|---|---|
  | 1 year | 1.45 | 4.25× | 1.45×10³ /m |
  | 1 day | 7.35 | 1.55×10³ | 7.35×10³ /m |
  | 1 hour | 10.52 | 3.72×10⁴ | 1.05×10⁴ /m |
  | 1 second | 18.71 | 1.34×10⁸ | 1.87×10⁴ /m |

  - Chung–Freese's own value is kL = 11.51.
  - The violation's size is set by k. Pricing it in kg/m³ needs the 5D Planck scale, which no source fixes (H-M5).

### 2. A bent plane (Ishihara)

- **No negative energy needed:** the bulk satisfies the null energy condition.
- **Where the shortcut comes from:** matter on the brane bends it, and the shortcut grows with the matter's density.
- **For a local body it is negligible.** Caldwell–Langlois's scale for the Earth is 2.4×10¹³ cm.
- **So this shape needs extreme density on the plane itself.** Ishihara points to gravitational collapse and the early
  universe.

### 3. A folded plane (the Manyfold)

- **No negative energy needed:** the bulk is flat.
- **Light can't see the fold.** Folding is extrinsic, so light travelling along the plane notices nothing.
- **Gravity can.** Gravity crosses the higher dimension, so a place brought close through it pulls from that close
  distance.
  - Proxima within 1 mm through the bulk would pull at **1.6×10²⁵ m/s²**, against 1.0×10⁻¹⁴ m/s² at its distance along
    the plane (H-FOLD-NEWTON).
  - **So the observed Proxima is not close through the higher dimension.** A quantitative bound needs solar-system
    ephemeris limits, which are OPEN.
- **The fold must be held open.** A folded brane is not a stable (BPS) state and tends to collapse; it needs
  stabilization (ADDK §7).

## For M

- **Each published shape that brings a far place close pays a different price:**
  - **Warping the other plane** needs negative-energy-type matter in the higher dimension. That is the same kind of price
    the board found for faster-than-light travel in four dimensions, now moved into the fifth.
  - **Bending the plane** needs extreme density on the plane itself.
  - **Folding the plane** needs nothing negative and is invisible to light. But gravity sees it, so a destination that is
    really close through the fold would be felt here by its gravity. Proxima is not.
- **On your picture, the fold matters most.** It is the one shape where the two places are truly separate planes to
  light (your "position 1, then position 2") while being close through the higher dimension. What it costs is that
  nothing with mass can sit close through the fold without being felt.
- **Your next step, O6,** now has a sharper question: what can cross a fold or a warped bulk, and how does it go in and
  come out? That is where your three states sit (leaving, stasis in the corridor, arriving).

## Named hypotheses

- H-THREE-ROUTES: the published routes, not shown to be exhaustive (a SURVEY).
- H-CF-STATIC and H-L-ILLUSTRATIVE.
- H-FOLD-NEWTON.
- H-D5-ANALOGUE.
- H-M5.
- M's H-HIGHER-CORRIDOR and H-BULK-PAIRING.

## OPEN

1. A shape outside the three, or a proof that they exhaust the possibilities.
2. The 5D Planck scale that prices route 1 in kg/m³.
3. An ephemeris bound on how close through the bulk an observed star can be.
4. Stabilizing a fold (ADDK §7) at a gap that carries anything.
