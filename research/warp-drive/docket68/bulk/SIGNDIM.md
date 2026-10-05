# The sign of energy by dimension (M-RULINGS items 74–76; READ, then modelled by deduction; not verified; not seated; 2026-10-05)

## What M asked

- **Item 74:** *"Perhaps positive energy is negative energy in the dimension it's corridor moves through, and what"*.
- **Item 75:** *"- Alcubierre was measuring was partially right"*.
- **Item 76:** *"READ, then model (Recommended)"*.

These are carried as M's hypotheses H-SIGN-BY-DIMENSION and H-ALCUBIERRE-PARTIAL, never as results. O9 stays OPEN.

**The question deduced:** can a warp's negative energy on our plane be the plane's reading of a bulk that satisfies the
energy conditions?

Every number is printed by `signdim.py`.
- **Selftest:** 18/18 checks, 7 of them controls, with 6 STRUCTURAL lines printed and not counted.
- **Verification:** not yet verified.

## What was READ (alphaXiv, open arXiv copies, printed pages)

| source | what bears on this |
|---|---|
| **Shiromizu, Maeda & Sasaki** (SMS), gr-qc/9910076 | The plane's field equations: G = −Λ₄q + 8πG_N τ + κ₅⁴π − E (eq. 17). E is bulk Weyl curvature and "is traceless" (eq. 9, p.2). G_N = κ₅⁴λ/48π (eq. 19): "we would have the wrong sign of G_N if λ < 0" (p.3). RS1's negative-tension brane "is an anti-gravity world" (abstract). E's divergence is fixed by the matter (eq. 22). Its transverse part is 5D gravitational waves, and "one must solve the gravitational field in the bulk at the same time" (p.4). |
| **Garriga & Tanaka** (GT), hep-th/9911055 | Two branes of opposite tension: "linearized Brans-Dicke (BD) gravity is recovered on either wall" (abstract). Newton's constant G(±) (eq. 26) is positive on both. On the negative-tension wall "the BD parameter is always negative but greater than -3/2" (p.7). Observations require ω > 3000 (p.7). |
| **Bronnikov & Kim** (BK), gr-qc/0212112 | The brane vacuum obeys G = −E (eq. 1). E "does not necessarily satisfy the energy conditions applicable to ordinary matter" (p.1). "Negative energies on the brane are induced by gravitational waves or black strings in the bulk" (p.1). They give R = 0 wormholes supported by E alone, with ρ + p_rad < 0 (eq. 18). Embedding in a 5D bulk is an open problem (pp.2, 6). |
| **Maartens**, gr-qc/0312059 | E acts on the plane as a "fluid" with pressure ρ_E/3 (eq. 3.47), and vanishes for an AdS bulk (eq. 3.48). It is possible "to avoid a naked singularity with negative m when K = −1, provided \|m\| ≤ ℓ²/4" (p.26). A charged bulk black hole imprints "an effective negative energy density −3q²/(κ²a⁶), which redshifts like stiff matter (w = 1)", through F, not E (p.32). The tidal-charge metric (eq. 4.17), with Q = −2M for r ≪ ℓ (eq. 4.20): negative Q "strengthens the gravitational field" (p.21). |
| **Alcubierre**, **Natário** (as READ in `horizon.py`) | Alcubierre's energy density is negative (eq. 19). "Nonflat warp drive spacetimes violate either the weak or the strong energy condition" (Natário Thm 1.7). |

NAMED-NOT-READ: Vollick, BK's reference 29.

## What follows

- **S1. The bulk's reading cannot carry a warp's trace.**
  - E is traceless, so the trace of the plane's curvature must come from the plane's matter or vacuum energy.
  - Alcubierre's four-dimensional curvature scalar is not zero: computed, it runs from −30 to +39 across his bubble.
    His metric is therefore not in Bronnikov and Kim's class of geometries carried by E alone.
  - The trace is no energy-condition obstacle: ordinary matter can carry either sign of it. But that matter must be
    conserved.
- **S2. The bulk's reading can carry every null projection.**
  - E has 9 of the curvature's 10 components (SMS eq. A5): all but the trace. The null energy test sees no trace, so it
    is entirely open to E.
  - Alcubierre's metric violates the null energy condition as well as the weak one (computed: G_kk < 0 in all four
    probe directions at the bubble's equator).
  - **At a point, then, the plane's equations admit his metric with ordinary matter plus a bulk reading.** That is only
    at a point: E's divergence is fixed by the matter, and its wave part must come from solving the bulk.
- **S3. A bulk that satisfies the energy conditions can be read on the plane as violating them.** Two READ cases, both
  homogeneous:
  - **An empty bulk** (vacuum energy only, which satisfies the null energy condition exactly) around a small
    negative-mass black hole in an open universe. Computed: it has a horizon for m = −0.2ℓ² and none for −0.3ℓ²,
    matching Maartens' bound. The plane reads negative "dark radiation", and ρ + p = (4/3)ρ_E < 0.
  - **A bulk electric field** (computed: a 5D Maxwell field satisfies the null energy condition). The plane reads
    negative stiff matter, and ρ + p = 2ρ < 0.
  - A warp needs a local reading, not a homogeneous one.
- **S4. Around a mass on the plane, the bulk's reading is a negative energy.**
  - In Maartens' tidal-charge solution, the curvature scalar is zero (computed). With Q = −2M, the effective energy
    density is negative and violates the null energy condition sideways. Yet it *strengthens* the attraction.
  - Positive mass on the plane; negative energy in its reflection from the bulk.
  - This is scoped to r ≪ ℓ and to an assumed metric form; Maartens says it "cannot describe the end-state of collapse".
    The negative energy outside radius r is 2ℓ/r of the mass.
- **S5. On a negative-tension plane, the plane's own term reads positive energy as negative.**
  - From SMS's equations with E = 0 (computed): G_kk = (κ⁴/6)(ρ + P)(λ + ρ). For λ < 0, which is RS1's visible plane and
    so ours, matter that keeps the null energy condition is read as violating it whenever ρ < |λ|. Its energy density
    is read as negative whenever ρ < 2|λ|.
  - In our units |λ| = (4.88 TeV)⁴ = **1.2×10⁵² J/m³**, from `crossing.py`'s tension.
  - The plane cannot read its tension's sign through its vacuum energy, which depends on λ² (Λ₄ = 0 for either sign).
    It reads the sign only through Newton's constant.
- **S6. But the attraction on our plane is the bulk's reading.**
  - The two papers' conventions agree where they should. SMS's vacuum-energy formula with GT's values gives Λ₄ = 0, and
    SMS's G_N equals GT's G(+) on the positive plane (computed, to 10⁻¹²).
  - On the negative plane, SMS's plane term has G_N < 0, yet GT find attraction, G(−) > 0.
  - SMS's equation is exact given its premises, so the difference is carried by E. **On our plane, if RS1, the sign with
    which matter gravitates is set by the bulk's reading, not by the plane's own term** (under H-SAME-CONFIGURATION).
  - The cost: ω(−) = −3/2 + 10⁻³⁰ at the board's kπr_c fails ω > 3000 unless the radion is stabilised (H-STABILISED).
- **S7. What Alcubierre measured.**
  - His negative energy density is G_nn/8π: computed from his metric, it reproduces his eq. 19 to 10⁻¹⁸. It is the
    plane's total reading, and no way of splitting it changes it.
  - What a four-dimensional computation cannot determine is what supplies it: matter on the plane, or the plane's reading
    of a bulk that satisfies the energy conditions. Natário's theorem binds the reading, not the bulk.
  - So "partially right" has a deduced form: **right about the reading, silent about the source.**
  - The size stays: the bulk's reading must supply the warp's whole null curvature. The source is relocated, not
    reduced.
- **S8. What is not shown.**
  - No bulk satisfying the energy conditions is known that induces a warp on the plane. Bronnikov and Kim leave the
    embedding open, and E vanishes for the plain AdS bulk. The bulk must carry Weyl curvature (gravitational waves or
    black strings).
  - Whether the time-delay theorems (`pairing.py`'s Gao–Wald scope) constrain such a bulk is OPEN.

## For M

- **Your item 74 has READ counterparts, in both directions:**
  - A bulk that keeps the energy conditions can be read on our plane as negative energy (S3, and Bronnikov–Kim's
    wormholes).
  - Around a positive mass, the bulk's reflection reads as negative energy, and it strengthens gravity (S4).
  - On a negative-tension plane, which in RS1 is ours, the plane's own term reads positive energy as negative. The
    attraction we feel would then be the bulk's reading (S5–S6).
- **Your item 75 has a deduced form.** Alcubierre measured the plane's total reading correctly. What his
  four-dimensional computation cannot say is whether exotic matter supplies it, or a well-behaved bulk read through our
  plane.
- **What it does not buy:** the size. The bulk must still supply the warp's whole curvature, so the source moves but
  does not shrink. And no bulk that does this for a warp has been constructed by anyone; that is OPEN.

## Named hypotheses

- **H-SAME-CONFIGURATION:** SMS's equations and GT's linear solution describe the same two-brane RS1 at linear order,
  with the hidden plane empty.
- **H-POINTWISE:** S2 is algebra at a point, not a solution.
- **H-ALCUBIERRE-ILLUSTRATIVE:** σ = 8, R = 1, v_s = 1, in geometric units.
- **Carried:** H-STABILISED and H-UNSTABILISED; H-RS1 and H-K-PLANCK from `bulk.py`.
- **M's:** H-SIGN-BY-DIMENSION, H-ALCUBIERRE-PARTIAL, H-HIGHER-CORRIDOR and H-TWO-PERSPECTIVE-TENSION.

## OPEN

1. A five-dimensional bulk satisfying the null energy condition whose Weyl reading induces a warp on the plane.
2. Whether matter conservation and SMS eq. 22 allow that reading for a moving bubble.
3. What sustains the bulk Weyl curvature (gravitational waves, black strings; Vollick unread).
4. The time-delay theorems against such a bulk.
5. Gravity on our plane with the radion stabilised: E's role there.
