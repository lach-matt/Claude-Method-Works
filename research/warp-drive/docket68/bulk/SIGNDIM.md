# The sign of energy by dimension (M-RULINGS items 74–78; READ, then modelled by deduction; verified once; not seated; 2026-10-05)

*First headed* "(M-RULINGS items 74–76; READ, then modelled by deduction; not verified; not seated; 2026-10-05)".

## What M asked

- **Item 74:** *"Perhaps positive energy is negative energy in the dimension it's corridor moves through, and what"*.
- **Item 75:** *"- Alcubierre was measuring was partially right"*.
- **Item 76:** *"READ, then model (Recommended)"*.
- **Item 77:** item 75 restated verbatim.
- **Item 78:** *"I had no specific part in mind, however, you took the principle and derived the conclusion, which is what my
  statement required."* The one assumption S6 named was to be searched for in the literature: *"If none is found, it
  is ours to hypothesis using deduction from first principles"*. It was found (S6, History).

These are carried as M's hypotheses H-SIGN-BY-DIMENSION and H-ALCUBIERRE-PARTIAL, never as results. O9 stays OPEN.

**The question deduced:** can a warp's negative energy on our plane be the plane's reading of a bulk that satisfies the
null energy condition? *First written* "the energy conditions": the AdS bulk itself violates the weak one.

Every number is printed by `signdim.py`.
- **Selftest:** 26/26 checks, 11 of them controls, with 8 STRUCTURAL lines printed and not counted.
- **Verification:** verified once, with its findings applied (History).

## What was READ (alphaXiv, open arXiv copies, printed pages)

| source | what bears on this |
|---|---|
| **Shiromizu, Maeda & Sasaki** (SMS), gr-qc/9910076 | The plane's field equations: G = −Λ₄q + 8πG_N τ + κ₅⁴π − E (eq. 17). E is bulk Weyl curvature and "is traceless" (eq. 9, p.2). G_N = κ₅⁴λ/48π (eq. 19): "we would have the wrong sign of G_N if λ < 0" (p.3). RS1's negative-tension brane "is an anti-gravity world" (abstract), a conclusion its first author later withdrew (next row). Its transverse part is 5D gravitational waves, and "one must solve the gravitational field in the bulk at the same time" (p.4). |
| **Shiromizu & Koyama** (SK), hep-th/0210066 | The same formalism applied to two planes. "For the two brane systems, on the other hand, we have to carefully evaluate E_μν due to the existence of the radion fields. Otherwise, we have a wrong prediction" (p.2). On the negative-tension plane, G = −(κ²/ℓ)T₂ − E (eq. 31); E is fixed by both planes' matter and the radion (eq. 33), giving attractive scalar-tensor gravity (eq. 34). "In Ref [13], we thought that the anti-gravity appears on the negative tension brane supposing E_μν is negligible. However, this is not correct and E_μν is not negligible even at the low energy" (p.4). "It is supposed that the visible brane where we are is the negative tension one" (p.1). |
| **Kanno & Soda** (KS), hep-th/0207029 | "The radion plays an essential role to convert the non-local Einstein gravity with the generalized dark radiation to the local quasi-scalar-tensor gravity" (abstract). Their dark-radiation tensor (E's counterpart) "is now a secondary entity" (p.7). The linearised result "is the same as the one derived by Garriga and Tanaka" (p.16). |
| **Chiba**, gr-qc/0001029 | On the negative-tension plane "G_eff → 0 and ω → −3/2", which "does not satisfy the constraint by the solar system experiment", but this "does not immediately mean that the scenario of [RS1] is not valid", because stabilisation is not included (p.5). |
| **Garriga & Tanaka** (GT), hep-th/9911055 | "Linearized Brans-Dicke (BD) gravity is recovered on either wall" (abstract). G(±) (eq. 26) and ω(±) (eq. 27). "Observations require that ω_BD > 3000"; on the negative wall ω is "always negative but greater than -3/2"; the system is "well behaved in spite of the negative tension" (p.7). Shadow matter bends light "25% smaller" (p.8). The extracted text of eq. 25 shows an exponent that contradicts their own eq. 24; it is RECONSTRUCTED and tested (S6c). |
| **Bronnikov & Kim** (BK), gr-qc/0212112 | The brane vacuum obeys G = −E (eq. 1). E "does not necessarily satisfy the energy conditions applicable to ordinary matter. Thus, examples are known [Vollick] when negative energies on the brane are induced by gravitational waves or black strings in the bulk" (p.1). They give R = 0 wormholes supported by E alone, with ρ + p_rad < 0 (eq. 18). They quote Vollick's claim that "any 4-dimensional space-time with R = 0" embeds without surface stresses, and add that "a complete model requires knowledge of the full 5-dimensional space-time" (p.6). |
| **Maartens**, gr-qc/0312059 | "The gravitational influence of the second brane is felt via its contribution to E_μν" (p.11). E acts on the plane as a "fluid" with pressure ρ_E/3 (eq. 3.47), and vanishes for an AdS bulk (eq. 3.48). "The system of equations is not closed" (p.19). It is possible "to avoid a naked singularity with negative m when K = −1, provided \|m\| ≤ ℓ²/4" (p.26). A charged bulk black hole imprints "an effective negative energy density −3q²/(κ²a⁶) ... (w = 1)", through F, not E (p.32). The tidal-charge metric (eqs. 4.17, 4.20): negative Q "strengthens the gravitational field" (p.21). For such solutions "the bulk metric ... has not been found" (p.20). |
| **Alcubierre**, **Natário** (as READ in `horizon.py`) | Alcubierre's energy density is negative (eq. 19). "Nonflat warp drive spacetimes violate either the weak or the strong energy condition" (Natário Thm 1.7). |

NAMED-NOT-READ: Vollick's papers; Csáki et al. and Goldberger–Wise on radion stabilisation; the Campbell–Magaard
embedding theorem.

## What follows

- **S1. The bulk's reading cannot carry a warp's trace.**
  - E is traceless, so the trace of the plane's curvature must come from the plane's matter or vacuum energy.
  - Alcubierre's four-dimensional curvature scalar is not zero: computed, it runs from −30 to +39 across his bubble.
    His metric is therefore in neither Bronnikov and Kim's class (E alone) nor Vollick's embedding class.
  - Ordinary matter can carry either sign of the trace, so the trace is no energy-condition obstacle.
- **S2. The bulk's reading can carry every null projection.**
  - E has 9 of the curvature's 10 components (SMS eq. A5): all but the trace. The null energy test sees no trace.
  - Alcubierre's metric violates the null energy condition as well as the weak one (computed: G_kk < 0 in all four
    probe directions at the bubble's equator).
  - This holds locally, not just at a point. For any conserved matter of the right trace, E defined by SMS's equation
    meets SMS's constraint (eq. 22) automatically. The plane's equations alone do not exclude his metric: "the system of
    equations is not closed" (Maartens).
  - **Not shown:** such matter that also keeps the energy conditions, and a bulk whose curvature gives that E.
- **S3. A bulk that keeps the null energy condition can be read on the plane as violating it.** Two READ cases, both
  homogeneous:
  - **An empty bulk** (vacuum energy only, which keeps the null condition exactly, though its negative vacuum energy
    violates the weak one, as Randall–Sundrum's bulk always does) around a small negative-mass black hole in an open
    universe. Computed: it has horizons for m = −0.2ℓ² and none for −0.3ℓ², matching Maartens' bound. The inner
    horizon is a Cauchy horizon, so a regular bulk is not claimed. The plane reads negative dark radiation, with
    ρ + p = (4/3)ρ_E < 0.
  - **A bulk electric field** (computed: a 5D Maxwell field keeps the null condition). The plane reads negative stiff
    matter, with ρ + p = 2ρ < 0.
  - A warp needs a local reading, not a homogeneous one.
- **S4. Around a mass on the plane, in the tidal-charge solution, the bulk's reading is a negative energy.**
  - Computed: the curvature scalar is zero. With Q = −2M, the effective energy density is negative and violates the
    null condition sideways, yet it *strengthens* the attraction.
  - Positive mass on the plane; negative energy in its reflection from the bulk.
  - **Scope:** an assumed metric form whose bulk "has not been found" (Maartens), so that bulk is not shown to keep the
    null condition. Within the solution's scope (r ≪ ℓ), the negative energy outside r exceeds the mass itself.
- **S5. On a negative-tension plane, the plane's own term reads positive energy as negative.**
  - From SMS's equations with E = 0 (computed): G_kk = (κ⁴/6)(ρ + P)(λ + ρ), and G₀₀ = (κ⁴/6)ρ(λ + ρ/2).
  - For λ < 0, which is ours under H-RS1, matter that keeps the null condition is read as violating it whenever
    ρ < |λ| = **1.2×10⁵² J/m³**. Its energy density is read as negative below twice that.
  - Randall–Sundrum already put a negative vacuum energy on our plane, and Garriga and Tanaka find the system "well
    behaved". In this framework the weak energy condition is not the obstacle; the null one is.
- **S6. The attraction on our plane is the bulk's reading.** This is now READ, not assumed.
  - **(a) The prior art.** Shiromizu and Koyama (Shiromizu is the S of SMS) withdraw the antigravity conclusion because
    E "is not negligible even at the low energy". On our plane G = −(κ²/ℓ)T₂ − E. The plane's own term repels, and E,
    fixed by both planes' matter and the radion, turns the total into attractive gravity. Kanno and Soda reach the same
    result and reproduce Garriga–Tanaka.
  - **(b) Computed.**
    - The papers agree: SMS's Newton constant with Shiromizu–Koyama's tension gives their eq. 31 coefficient exactly.
      Their ω equals Garriga–Tanaka's on each plane.
    - The bulk's reading cancels the plane's own repulsion to one part in 10³⁰ at the board's geometry, and adds the
      radion's attraction.
  - **(c) A sign by direction** (computed, unstabilised radion).
    - On our plane a positive mass gives an attractive Newtonian pull (time part), but the spatial curvature keeps the
      plane term's repulsive sign: γ_PPN = −1 + 6×10⁻³⁰. Light bends at 3×10⁻³⁰ of what Einstein's gravity gives for
      the same mass.
    - Observation excludes this unstabilised form (ω > 3000; Chiba).
  - **(d) A form that needs neither paper's linear solution nor an unstabilised radion.** If our plane has negative
    tension (H-RS1), and gravity is observed to attract (P-ATTRACT), then the plane's own term repels. The attraction
    must therefore come from the bulk terms: E, or F from whatever bulk field stabilises the radion.
- **S7. What Alcubierre measured.**
  - His negative energy density is G_nn/8π: computed from his metric, it reproduces his eq. 19 to 10⁻¹⁸. It is the
    plane's total reading, and no way of splitting it changes it.
  - What a four-dimensional computation cannot determine is what supplies it: matter on the plane, or the plane's reading
    of a bulk that keeps the null energy condition. Natário's theorem binds the reading, not the bulk.
  - So "partially right" has a deduced form: **right about the reading, silent about the source.**
  - **The size of the reading is fixed by the metric.** On a positive-tension plane the bulk's reading must supply at
    least the warp's whole null curvature. On a negative-tension plane the plane's own term can supply part (S5).
  - **Whether the bulk needs anything beyond its vacuum energy to produce it is OPEN.** E is vacuum curvature, and Bronnikov and
    Kim's wormholes need no matter on the plane. The demand is relocated; whether it is reduced is not shown.
- **S8. What is not shown.**
  - No bulk keeping the null energy condition is known that induces a warp on the plane. The embedding is open, and E
    vanishes for the plain AdS bulk.
  - Vollick's embedding claim covers only R = 0 geometries, which excludes Alcubierre's.
  - Whether the time-delay theorems constrain such a bulk is OPEN; beside them, Maartens READS that 5D graviton signals
    can take "short-cuts" through the bulk.

## For M

- **Your item 78:** the connection the board had to assume is in the literature, and from SMS's own first author.
  Antigravity on our plane was a mistake: the bulk's reading is not negligible there. The board's one assumption is
  retired and replaced by READ.
- **What that gives your item 74, all READ or computed:**
  - On our plane (if we are on the negative-tension one), the plane's own term reads positive matter as repulsive. The
    attraction we feel is the bulk's reading, cancelling the plane's term to one part in 10³⁰ and adding its own pull.
  - With the radion unstabilised, the reversal is only partial: positive mass pulls in time but curves space with the
    opposite sign (γ = −1). That form is excluded by observation, but it is a sign set by direction, computed.
  - A bulk that keeps the null energy condition can be read on our plane as negative energy (S3). Around a positive
    mass, the bulk's reflection reads as negative energy and strengthens gravity (S4).
- **Your item 75:** right about the reading, silent about the source (S7).
- **Still OPEN:** a bulk that does this for a warp; whether it needs any stress-energy at all beyond its vacuum energy.

## Named hypotheses and premises

- **P-ATTRACT:** gravity on our plane is observed to attract.
- **P-BD-MAP:** the linearised Brans–Dicke source (Will, cited by GT). NAMED-NOT-READ, and used only to test the eq. 25
  reconstruction.
- **P-KAPPA:** κ² = 8πG₅.
- **H-ALCUBIERRE-ILLUSTRATIVE:** σ = 8, R = 1, v_s = 1.
- **Carried:** H-RS1 and H-K-PLANCK from `bulk.py`; H-STABILISED and H-UNSTABILISED (S6c needs the latter, S6d
  neither).
- **M's:** H-SIGN-BY-DIMENSION, H-ALCUBIERRE-PARTIAL, H-HIGHER-CORRIDOR and H-TWO-PERSPECTIVE-TENSION.

## OPEN

1. A five-dimensional bulk keeping the null energy condition whose Weyl reading induces a warp on the plane
   (Campbell–Magaard NAMED-NOT-READ).
2. Conserved matter of the right trace that also keeps the energy conditions, for a moving bubble.
3. What sustains the bulk Weyl curvature (gravitational waves, black strings; Vollick unread).
4. The time-delay theorems against such a bulk, beside the READ bulk short-cuts.
5. Gravity on our plane with the radion stabilised: E's and F's shares (Csáki et al., Goldberger–Wise unread).

## History (verifier and item 78, 2026-10-05; first-written claims kept)

- **S6 first rested on H-SAME-CONFIGURATION**, the assumption that SMS's equations and Garriga–Tanaka's linear solution
  describe the same setup. On item 78 the literature was searched: Shiromizu and Koyama derive the two-plane result in
  SMS's own formalism and withdraw the antigravity conclusion, and Kanno and Soda reproduce Garriga–Tanaka. The
  hypothesis is retired, replaced by READ.
- **"On our plane the sign with which matter gravitates is set by the bulk's reading."** Too broad, and not scoped to the
  unstabilised radion: the reading flips the time part, while the spatial part keeps the plane term's sign. Now S6c,
  scoped, with S6d the stabilisation-independent form.
- **"Energy conditions" where only the null condition holds** (the question, S3, S8, For M). The AdS bulk violates the
  weak one.
- **S2's "Pointwise only: E's divergence is fixed by the matter".** That constraint holds automatically; H-POINTWISE is
  withdrawn.
- **S7's "must supply the warp's whole null curvature" and "relocated, not reduced".** The first hid the plane term's
  sign; the second undersold that E is vacuum curvature.
- **S4's "the negative energy outside r is 2ℓ/r of the mass, on the scope r ≪ ℓ".** Within that scope it exceeds the
  mass. The heading had dropped "in the tidal-charge solution".
- **S5's "RS1's visible plane and so ours"**, now under H-RS1; and "reads its sign only through G_N", contradicted by S6.
- **Bronnikov–Kim's "examples are known" was dropped from the quote.**
- **The selftest.**
  - Control 2's label named the wrong change.
  - The ghost control ran a different code branch; it now runs the Maxwell branch with a spacelike vector.
  - The ω(−) and G(±) checks were fixed by their own formulas. They are now STRUCTURAL, replaced by cross-paper checks.
  - The energy-density crossover was unchecked.
