# S-T3: Tier 3 of the characteristic problem for five-dimensional Einstein–null dust (perturbations that reach the axes)

This is a scoping report for the writer. Nothing under `reader/` was edited, and `assemble.py` was not run.

**Read for this report.**
- notes/reports/S-CIVP.md: all of it.
- Chapter 81: 1–380, 540–700, 848–1040 and 1038–1671 in full (the axes, the planar shear, def:class-adapted,
  thm:class-stability, cor:class-two-dust, rem:class-scope).
- Chapter 83: 1–72 and 137–602 (thm:loc-bent-slice, lem:loc-lens-dependence, sec:loc-cones).
- Chapter 80: 150–240 and 360–420 (eq:two-dust-chart, prop:two-dust-background, lem:two-dust-domain).
- Chapter 02: 1–80 (prop:reduction).

**Tier 1 and Tier 2 files.** proofs/P-CIVP.md and proofs/P-CIVP2.md do not exist yet (checked 2026-11-20; `find` finds
only S-CIVP.md). This report therefore refers to the Tier 1 lemmas L0–L11 of S-CIVP §3.3 and the Tier 2 items of §3.6 by
those names.

---

## Summary

- **Verdict: feasible** for small perturbations of the background's characteristic data, with the two adapted families
  (ingoing phase v, outgoing phase u). The perturbation may be supported anywhere on 𝒞_out and 𝒞_in, axes included.
  Three cases remain out of reach with the tools in the paper: large data at the axes; non-adapted families that cross a
  hypersurface where it meets an axis (the exact condition is in §5.2); and low regularity.
- **The difficulty is the dust, not the metric.** In chapter 81's 4+1 wave gauge the metric equations (Aug1) and the
  transports (Aug2) and (Aug4) are regular through the axes. What fails at an axis is the closure (Aug3) of the
  expansion, where κ_A2 holds a second derivative of the phase (prop:class-axis (b)). Chapter 81 recovers that second
  derivative from the planar shear σ_A, and it computes σ_A by a Volterra integral from the axis along the leaf, the
  section of the family's null hypersurface by the slice (eq:class-leaf-volterra). This makes the right side non-local
  along leaves. A domain-of-dependence argument then needs each slice of the domain to contain the leaf arc of each of
  its points. That is the locality hypothesis (F4) of thm:class-kato (b), restricted to the leaves.
- **The obstruction with null faces, and why it can be removed.**
  - The face 𝒞_out = {u = 0} is a level set of the outgoing phase, but the ingoing dust crosses it, and the shell is
    present at the axes. Near an axis point, the ingoing leaves and the face section have second-order contact. They
    can cross at distance O(ε)|y|². Chapter 81 meets the same effect at lateral boundaries: "The leaves of another
    family A′ can cross an adapted boundary B at distance O(ε)" (81:1507). There it is removed by cutting off the
    other family, (H2′). That is impossible here, because both families are present.
  - **The way out:** chapter 81's own chart time τ = v − R of the two-dust background meets 𝒞_out and 𝒞_in in the data's
    double-null spheres {u = 0, v = c} and {u = c′, v = 0}. This holds because R is a function of v on 𝒞_out and of u
    on 𝒞_in (80:399, lem:two-dust-domain).
  - So every face section is a leaf of both families, for every state that carries the formal solution's 1-jets on the
    faces (Volterra uniqueness, lem:class-volterra). Leaves of one family foliate a neighbourhood of the axis, so they
    never cross a face section.
  - Hence the past region P and the future quadrant F are both closed under the leaves of the right state. Step (6) of
    lem:loc-lens-dependence then carries over. In P the two states swap roles: the known extension Û supplies the
    leaves, and the unknown solution is the one extended.
- **Recommended route: Route B.** Run Rendall's trick on ℝ⁴ for chapter 81's system with its axis closure.
  - There is no angular cut-off and no adapted lateral boundary. The axis-phase and T_(τ,U) machinery of
    def:class-adapted is not needed.
  - Five lemmas are new. Each has a template in the paper.
  - Route A ("4+1 wave gauge, where the axes are not special") is not an alternative. Chapter 81's augmented system
    already *is* the 4+1 wave-gauge system. Without its class closure the dust loses a derivative. With the closure, the
    axes bring in the non-local σ_A, and that is Route B.
- **What it delivers.** A smooth class development on the **whole rectangle** Q1 × S³ (any Q1 in the background's set
  G), in the double-null gauge. It is unique in the gauge near the background and localised. For small data this
  supersedes Tier 1's region G_* = {uv ≤ δ_*²}. Tier 1 keeps its explicit δ_* and its simpler local proof.
- **Size.** 650–1,000 chapter lines (13–20 PDF pages) on top of Tier 1, written as "the proof of [Tier 1] holds with the
  following changes", the way thm:class-stability is written on top of thm:class-stability-off-axes. Alternatively, if
  Tier 1 is folded into this form, 1,450–2,100 lines for both together. There are three go/no-go checks (§6).

---

## 1. The difficulty

### 1.1 Where the T² orbits degenerate

- **Where the Killing fields vanish.** K1 = ∂_(φ1) vanishes on axis 1, {ρ1 = 0} = {ϑ = π/2}. K2 = ∂_(φ2) vanishes on
  axis 2, {ρ2 = 0} = {ϑ = 0} (81:27–33).
- **What the axes are, in each picture.**
  - In space-time each axis is a three-dimensional timelike submanifold. Axis 2, for example, is (τ, x1, x2) with
    x3 = x4 = 0.
  - In the orbit space (u, v, ϑ) the axes are the two timelike boundary surfaces ϑ = 0 and ϑ = π/2.
  - On a section S³ of 𝒞_out or 𝒞_in each axis is a circle. On each null hypersurface it is a two-dimensional null
    surface ruled by generators. The corner S meets each axis in a circle.
- **The two axes never meet** in the region concerned: they meet only at x = 0, and every domain lies in R ≥ a > 0.
- **At an axis point, every phase in the class has its gradient in span(dτ, dr).** This is lem:class-phase-axis: the
  gradient is parallel to dv or to the outgoing covector, so the ray runs along the axis.
- **Every leaf near the axis is flat to first order.** Near an axis point the leaves (sections of {u_A = c} by a slice,
  restricted to M3) are graphs z = h(y) over a disc in the plane of the degenerate circle, with |h(y) − h(0)| ≤ C_L |y|²
  (lem:class-leaf, lem:class-volterra; the constant C_L is used in def:class-adapted).
- **On the background the two foliations coincide.** On each slice Σ_τ = {v − R = τ} the ingoing phase is v = τ + R, and
  the outgoing phase is a strictly decreasing function of R (proof of cor:class-two-dust). So both families' leaves are
  the spheres R = const.
- **After a perturbation they separate at second order.** Two leaves of different families through one axis point agree
  to first order and separate like O(ε)|y|².

### 1.2 The reduced 2+1 system there

- **The reduction.** prop:reduction (02:55–74) puts ψ = A + B, ω = (B − A)/2 and h = e^(2ψ) g3, and gives
  Ric[h] = (3/2) dψ² + 2 dω² (plus the dust), □_h ψ = □_h ω = 0.
- **It degenerates at an axis.** Near axis 2, e^(2B) = g(K2, K2) = a_⊥ ρ2² (prop:class-axis (a)), so:
  - B = log ρ2 + ½ log a_⊥ → −∞, and ψ and ω have logarithmic singularities;
  - the conformal factor e^(2ψ) of h vanishes like ρ2², so h degenerates;
  - □_h acquires coefficients singular like 1/ρ2.
- **The regular variables are known.** They are B − log ρ2, even in ρ2, together with the conical condition
  ĝ(∂_3, ∂_3) = a_⊥ at the axis (eq:class-axis-metric). In the double-null gauge eq:loc-double-null:
  - A_s = log sin ϑ + (smooth, even);
  - e^(2A_s)/(γ_ϑ sin² ϑ) → 1 at ϑ = 0;
  - b is odd in ϑ.
- **Consequence for Tier 2.** The 2+1 system cannot be put into the doubly-null form of [CCTW16] (Y compact without
  boundary) up to the axes without rewriting it in such variables. Tier 2 avoids this by periodising in ϑ away from the
  axes (S-CIVP §3.6, item 5).
- **The same consequence for the cone data.** prop:loc-cones writes the data through
  e^ϕ = (γ_ϑ^(1/2) e^(A_c + A_s))^(1/3). On the background this is e^ϕ = R (sin ϑ cos ϑ)^(1/3), which vanishes on the
  axis generators.
  - So "every generator on which e^ϕ stays positive" (83:576–577) excludes the axis generators.
  - The term r of eq:loc-cone-r contains ∂_ϑϰ_3 = cot ϑ + O(ϑ). It is regular only through the conical condition.
  - Tier 3 therefore needs a restated data lemma (T3-0 in §4).

### 1.3 The 4+1 picture: the metric is regular at the axes, the dust is not

- **The system is already a 4+1 system.** Chapter 81 never reduces to 2+1. Its unknowns are the 4+1 metric in wave gauge
  relative to a G-invariant g̊, together with p_A, Θ_A and q_A (sec:class-augmented).
- **Every equation but one is regular through the axes.**
  - (Aug1) is a quasilinear wave system with smooth coefficients there.
  - (Aug2) and (Aug4) are transports along P_A, which is smooth.
  - κ_A1, the curvature of the circle that does not degenerate, is smooth near axis 2 (prop:class-axis (b)).
- **The one exception is the closure (Aug3) of the expansion.** Off the axes, S_A is a function of first-order quantities
  because ∇²u has the eigenvalues (Θ_h, κ1, κ2), with κ_i = P(ψ_i) algebraic (prop:class-structure). At an axis, κ2 holds
  ∂_3²u (prop:class-axis (b)), with the coefficient 1/(a_⊥ ρ2) of ∂_3 u (prop:class-axis (c)). This is the third lossy
  variant of prop:class-augmented (a).
- **Neither alternative closure works.** Taking Θ_A := div_g P_A, or carrying the Hessian with its Riccati equation, also
  loses a derivative (prop:class-augmented (a); the Riccati equation brings in the Riemann tensor).
- **The quantity to recover is σ.** By eq:class-x, |χ|² = κ1² + ½ (Θ − κ1)² + ½ σ², so the one quantity to recover at an
  axis is the planar shear σ.

### 1.4 Why chapter 81's augmented system is non-local

- **The axis closure.** Near an axis the right side of (Aug3) is
  S_A^ax = −κ_A1² − ½ (Θ_A − κ_A1)² − ½ σ_A[Θ_A]² − Σ_B q_B g⁻¹(p_A, p_B)² (81:1500–1503).
- **How σ_A[Θ_A](x) is computed.**
  1. Build H_L from Θ_A, the spatial part of p_A and the 1-jet of g (step (1) of lem:class-planar-shear).
  2. Solve the Volterra equation eq:class-leaf-volterra from the axis point of the leaf, r h′(r) = ∫_0^r (…) dρ,
     uniquely (lem:class-volterra).
  3. Read the leaf's second fundamental form at x (eq:class-shear-leaf).
- **This is non-local.** The value at x depends on the state along the whole arc of the leaf in Σ_τ, from the axis to x:
  - "Near the axes the right side of the augmented system is non-local in the planar directions, an integral from the
    axis along each leaf" (81:1528–1529);
  - "the recovery … is an integral in ρ from the axis, across every generator: no transport along P_A supplies it"
    (81:1133–1134).
- **The non-locality is the price of no loss.** The averaging operator 𝒜 is bounded on every Ḣ^j
  (prop:class-flat-model (b)), and the local alternatives all lose a derivative (§1.3).

### 1.5 Why that obstructs a domain-of-dependence statement with null faces

- **What an energy argument needs.** It shows that two states agreeing on the base of a domain agree on the domain. It
  needs the right sides to agree pointwise on each slice of the domain wherever the states agree there. That is (F4) of
  thm:class-kato (b): "for (t, u), (t, v) ∈ 𝒟_ρ with u = v on Σ_t, F(t, u) = F(t, v) on Σ_t" (81:576–577).
- **For σ_A this means:** for every point x of a slice D_τ near the axis, the leaf arc from the axis to x lies in D_τ.
  The paper meets this requirement twice.
  - **Adapted domains (thm:class-stability, 81:1540–1567).**
    - The lateral boundary near an axis point is itself a leaf of the family A(B) present there.
    - Every other family is cut off there (ζ_(A′) = 0), which (H2′) allows because no tube of A′ comes near.
  - **The lens (lem:loc-lens-dependence, 83:334–517).**
    - The faces are {v_in = c_a + c_v t} and {v_in = c_b − c_v t}, level sets of the one family on each slice, plus
      the angular face {ϑ = α′ − W t}.
    - Step (6) shows that the arc of a level set from the axis to y keeps v_in constant and ϑ increasing, so it stays
      in 𝒟_s (83:459–466).
    - Step (3) shows that "only the ingoing family carries dust in 𝒟" (83:411).
- **What changes for the characteristic problem.**
  - The data surfaces are null hypersurfaces of *both* families: 𝒞_out = {u = 0} and 𝒞_in = {v = 0}.
  - The dust of each family crosses the other family's face: the ingoing shell crosses 𝒞_out at 3 < v < 4.5, and the
    outgoing packet crosses 𝒞_in at 5.7 < u < 7.2. Both are round, so present at the axes.
  - Hence near a point where 𝒞_out meets an axis, the ingoing family needs S^ax.
  - Its leaves have second-order contact with the section of 𝒞_out (§1.1). Through a point x on the P-side of the
    section, at distance d with |y(x)| = r, the ingoing leaf can reach the F-side if d ≲ ε r².
- **What this breaks in Rendall's trick.** Three steps need locality, and with crossing leaves all three fail:
  - U = Û on P (L6): a leaf from P dips into F, where U is not yet known;
  - constraint propagation in F (L8): a leaf from F dips into P, where the defect of the extension Û does not vanish,
    so Tier 1's extension of Δ_A by zero no longer gives a homogeneous equation;
  - uniqueness by gluing (L10): the glued state may not solve the non-local system.
  Even the forcing F̃ = 1_P 𝔄(Û) would not obviously be smooth, since its non-local part at x ∈ P would read Û off P.

### 1.6 What the analogue of lem:loc-lens-dependence has to say

It must say three things. All three rest on one geometric fact, Lemma A (T3-1 in §4).

- **Lemma A (the faces are leaves).** On every slice Σ_τ of the chart time τ = v − R, Σ_τ ∩ 𝒞_out and Σ_τ ∩ 𝒞_in are
  data spheres. Near each of their axis points each of them is the leaf, for both families, of every state that carries
  the formal solution's 1-jets on 𝒞_out ∪ 𝒞_in.
- **(P) Dependence on the past.** Let U solve 𝔄_ξ(U) = F̃ on ℝ⁴, and let Û be the extension with 𝔄_ξ(Û) = F̃ on P. If
  U = Û on Σ_init, then U = Û on the closure of P. This is the statement used in L6.
- **(F) Constraints in the quadrant.** Suppose U solves the system on F, and D and Δ_A vanish to infinite order on
  ∂F = 𝒞_out ∪ 𝒞_in. Then D = 0 and Δ_A = 0 on F, with the energy taken on F itself. This is the statement used in L8.
- **(R) Characteristic dependence for genuine solutions.** Two smooth class solutions near g0, in the same wave gauge,
  that induce the same data on the two past faces of a double-null rectangle agree on it. This is used for uniqueness
  and localisation in L7 and L10.
  - Here the slicing is the solution's own t := u + v. Its slices meet the faces of the rectangle in that solution's
    double-null spheres.
  - The planar shear of a genuine solution is intrinsic to its null hypersurface, so the axis closure holds in any
    slicing.

The proofs follow step (6) of lem:loc-lens-dependence, with one change in (P): the state whose leaves are known to stay
in the domain is the extension Û, so the unknown U is the one extended, Ŭ := U − 𝔼(U − Û) (§4.3, T3-2).

---

## 2. Literature, verified

Search route: alphaXiv and the Firecrawl research index (arXiv). OpenAlex was refused by the proxy. Each source below
was opened at the pages cited unless marked otherwise.

| Source | Setting | At an axis | Characteristic? | Null dust? | Use for Tier 3 |
|---|---|---|---|---|---|
| Berger–Chruściel–Moncrief 1995 | 3+1, G2 = R × U(1), electro-vacuum | regularity conditions; development from the unreduced Cauchy theory | no | no | confirms the pattern and its hypothesis |
| Chruściel 1990 | 3+1, U(1) × U(1), compact Cauchy surfaces | coordinate changes smooth at the axes (App. C, as cited by BCM) | no | no | none (not read) |
| Andersson–Gudapati–Szeftel 2017 | 2+1 equivariant Einstein–wave map | parity and no-cone conditions; double-null coordinates normalised on the axis; lift to a 4D radial wave operator | no (Cauchy) | no | technique only |
| Rinne–Stewart 2005 | 3+1 axisymmetric, (2+1)+1, generalised harmonic gauge | first-order system "manifestly regular on axis" | no | perfect fluid, not dust | model for Route C |
| Huneau–Luk 2018 | 3+1, polarised U(1), elliptic gauge | none: the U(1) acts freely | no | yes | none at the axes |
| Andersson–Moncrief 2003 | n+1, CMC + spatially harmonic (elliptic) gauge | none: closed M | no | no | no domain-of-dependence lemma to cite |
| Luk–Rodnianski [LR20] | 3+1, double null | none (S² sections) | yes | two families, measure-valued | Route D only |
| [CCTW16] | doubly-null symmetric hyperbolic systems | Y compact without boundary | yes | no | Route C would need an axis-regular form |

The entries in detail:

1. **Berger, Chruściel, Moncrief**, *On "asymptotically flat" space-times with G₂-invariant Cauchy surfaces*,
   Ann. Phys. 237 (1995) 322–354, arXiv:gr-qc/9404005. Read pp. 1–5, 8–12, 15–19, 21–23, 25–27, 29–32.
   - The symmetric development comes from the unreduced theory (p. 4): "Let (M, g) be a globally hyperbolic development
     of the initial data on which G acts by isometries (such a development always exists if one solves the vacuum
     equations, cf. e.g. [10] or [8][Section 2.1]; more generally, this result still holds if the matter fields satisfy
     some well–behaved equations of hyperbolic type)."
   - The regularity conditions at the axis are (3.4)–(3.5) (p. 12).
   - Coordinate changes near the axes are made smooth "using e.g. the methods of [7] [Appendix C]" (p. 10), and "the
     axes of symmetry, again, can be taken care of by the methods of Appendix C of [7]" (p. 11), where [7] is
     Chruściel 1990.
   - Not covered: characteristic data and null dust. The quoted hypothesis is exactly what null dust fails in a general
     gauge (chapter 81, the paragraph after def:class-system).
2. **Chruściel**, *On space-times with U(1)×U(1) symmetric compact Cauchy surfaces*, Ann. Phys. 202 (1990) 100–150.
   - **Not read**: paywalled and not on arXiv.
   - The bibliographic data are confirmed by BCM's reference [7] (p. 31) and by the reference list of Ringström,
     Ann. of Math. 170 (2009).
   - Its content is known here only through BCM's citations of its Appendix C. Cite it for nothing beyond that.
3. **Andersson, Gudapati, Szeftel**, *Global regularity for the 2+1 dimensional equivariant Einstein-wave map system*,
   arXiv:1501.00616 (v4, 2017). Read pp. 1–7, 13–14, 38–40, 59, 90, 115.
   - Theorem 1.6 (p. 5): "The proof by Choquet-Bruhat and Geroch [8] … together with the equivariance of the Cauchy
     data, is readily generalized". This is again the unreduced-plus-equivariance pattern.
   - Parity and no-cone conditions (p. 4): "α(t, r), β(t, r) are even functions of r. In order to avoid a conical
     singularity at the axis, it must hold that β(t, 0) = 0".
   - Double-null coordinates are normalised on the axis by (2.1) (p. 7).
   - The singular terms are handled by lifting: "the left-hand side of the wave equation for w in Lemma 9.1 is the
     4-dimensional radial wave operator" (p. 90, §9.2).
   - Not covered: a characteristic problem with transversal data, and dust.
   - Useful as the standard technique: lift to a higher-dimensional space in which the axis is interior. Chapter 81's
     choice of coordinates (z, y) on M3 is already that lift.
4. **Rinne, Stewart**, *A strongly hyperbolic and regular reduction of Einstein's equations for axisymmetric
   spacetimes*, Class. Quantum Grav. 22 (2005) 1143, arXiv:gr-qc/0502037. **Abstract only**; the abstract of the
   thesis, gr-qc/0601064, was also read.
   - The abstract describes: a Kaluza–Klein reduction followed by (2+1)+1; a generalised harmonic gauge; vacuum and
     perfect fluid; and a strongly hyperbolic first-order system in which "each and every term is manifestly regular on
     axis".
   - It is a formulation for numerical evolution. No well-posedness theorem is claimed in the abstract, and the body
     was not checked.
   - Not covered: characteristic data and null dust.
   - It is the model one would follow to make Tier 2's 2+1 system regular at the axes (Route C).
5. **Huneau, Luk**, *Einstein equations under polarized U(1) symmetry in an elliptic gauge*, arXiv:1706.09499.
   **Abstract read**; the paper is also quoted in rem:class-polarised.
   - It proves local existence for Einstein–null dust in an elliptic gauge, with smallness.
   - The U(1) acts without fixed points ([HL18, p. 3, footnote 5], as quoted at 81:231–232), so there is no axis.
6. **Andersson, Moncrief**, *Elliptic–hyperbolic systems and the Einstein equations*, Ann. Henri Poincaré 4 (2003),
   arXiv:gr-qc/0110111. Read pp. 1–29 (the relevant parts).
   - Non-local gauge: lapse and shift are solved from elliptic equations (1.11).
   - Theorem 3.1 gives strong local well-posedness, and §4 (Lemma 4.1) propagates the constraints by a global energy
     on M.
   - M is "a compact, connected, orientable C^∞ manifold" (p. 1). No finite-speed or domain-of-dependence statement
     appears in the pages read.
   - Conclusion: for a non-local gauge-fixed system the literature works on closed manifolds, and a PDE-level
     domain-of-dependence lemma has to be proved in-house.
7. **[LR20]**: arXiv:2009.08968, read in S-CIVP (Theorem 4.6, p. 29), abstract re-read.
   - Near axis 2, the quotient by the free circle K1 turns the problem into a 3+1 Einstein–massless scalar–null dust
     system, axisymmetric, with a regular axis. (The reflection φ1 ↦ −φ1 removes the Kaluza–Klein vector; du_A has no
     dφ1 part.)
   - [LR20] covers 3+1 Einstein–null dust without the scalar field. This picture is local in angle: S³/K1 is a disc
     whose boundary is axis 1.
8. **[CCTW16]**: read in S-CIVP. Theorem 3.9 needs Y compact without boundary. At the axes the 2+1 unknowns of
   prop:reduction are singular (§1.2), and no axis-regular doubly-null form of the reduced system is in the literature.

**Conclusion.**
- The standard practice at axes (BCM, AGS) is to solve an unreduced hyperbolic system and get invariance from
  uniqueness. That presupposes matter of hyperbolic type.
- No source treats a characteristic problem near a symmetry axis for a system whose closure is non-local along leaves.
  Nor does any source give a domain-of-dependence lemma for such a system.
- The two templates are in the paper itself: lem:loc-lens-dependence step (6), and thm:class-stability, "The adapted
  domain is a domain of dependence".

---

## 3. Routes and the recommended one

| Route | Idea | At the axes | Delivers | Length | Risk | Verdict |
|---|---|---|---|---|---|---|
| A | Rendall in 4+1 wave gauge, invariance by uniqueness, then double null | the 4+1 wave-gauge augmented system *is* chapter 81's; without the class closure, (Aug4) loses a derivative | as B (it becomes B) | — | — | not distinct from B |
| A′ | 4+1 double-null gauge with the dust phases as coordinates, Luk or CTG23 type | no axis issue | any size, no symmetry needed | 3,000+ | high | S-CIVP Routes L and C; not recommended |
| **B** | Rendall on ℝ⁴ with chapter 81's axis closure; faces adapted by the chart time τ = v − R | non-local σ_A, made local on P and F by Lemma A | small data, whole rectangle Q1 | +650–1,000 | moderate | **recommended** |
| C | Tier 2's 2+1 doubly-null system rewritten in axis-regular variables on Y = S³, then [CCTW16, Theorem 3.9] | regular variables (Rinne–Stewart type) | large data at the axes | +1,500? | high: the fit to (2.8) is unverified, and e^(2ψ) of h degenerates | open |
| D | near each axis, quotient by the free circle: 3+1 Einstein–scalar–null dust with a regular axis, Luk/[LR20]-type theory, glued to Tier 2 | interior in 3+1 | large data, possibly low regularity | 3,000+ | high | not recommended |
| E | glue Tier 2 (large off the axes) and Tier 3 (small near them) by uniqueness | — | data large off the axes and small near them, on a strip | +100–200 | low once both exist | optional corollary |

**Why A is not a separate route.**
- Chapter 81 already works in 4+1 wave gauge relative to a G-invariant g̊, with invariant unknowns. It gets G-invariance
  from uniqueness (Step 9 of thm:class-stability-off-axes). The axes are special in that system only through the dust's
  expansion (§1.3).
- A literal Route A, an unreduced 4+1 wave-gauge system with null dust, cannot be solved by energy methods at all. That
  is the derivative loss of the paragraph after def:class-system, and BCM's hypothesis of matter "of hyperbolic type"
  fails.
- Route A works as stated only where no dust is near the axes. Pure vacuum is that case (S-CIVP §3.8: "In vacuum the
  axis difficulty is absent"). The background's shell and packet are round and present at the axes, so Route A cannot
  reach Tier 3.

**Why B works: one observation and three consequences.**
- **Observation (the face-adapted slicing).**
  - In the chart (τ, x), τ = v − R, of lem:two-dust-domain, consider a point of 𝒞_out. There R = R(0, v) with
    R_v = f/2 ≤ 1/2, so v − R(0, v) is strictly increasing (80:399). Hence Σ_τ ∩ 𝒞_out = {u = 0, v = c(τ)}.
  - On 𝒞_in, v = 0 and R_u < 0 (prop:two-dust-background (c)). Hence Σ_τ ∩ 𝒞_in = {u = c′(τ), v = 0}.
  - Tier 1's L1 transports the data to this chart by the background's map, and the data's u and v on the faces are the
    background's (L9). So these are the data's double-null spheres.
- **Consequence 1 (Lemma A).** The formal solution's phases ũ and ṽ are both constant on each face section.
  - Each section is therefore a level set of both phases within the slice.
  - It solves eq:class-leaf-volterra for any state whose 1-jet on it is the formal one. H_L depends only on that 1-jet:
    Θ_A, p_A, K_Σ, and γ3 with its first derivatives.
  - By lem:class-volterra it is that state's leaf, for both families.
- **Consequence 2.** Leaves of one family foliate a neighbourhood of the axis (lem:class-leaf-differences), so they
  never cross a leaf. So P ∩ Σ_τ and F ∩ Σ_τ are closed under the leaves of the right state. P ∩ Σ_τ has two components,
  inside Σ_τ ∩ 𝒞_in and outside Σ_τ ∩ 𝒞_out.
- **Consequence 3.** Step (6) of lem:loc-lens-dependence goes through: Stein extension averaged over G, uniqueness in
  lem:class-volterra, then lem:class-leaf-differences (b). It needs one change in P, where the extension Û (not a
  solution) supplies the leaves and the unknown U is extended.

**What B no longer needs.**
- Lateral boundaries: on ℝ⁴ with a space-time cut-off ξ deep in P there are none. So the adapted-domain machinery of
  def:class-adapted (axis phase, T_(τ,U), restarts on Ω_U) is not used.
- The angular cut-off χ of Tier 1.
- Tier 1's finite-speed region G_*.

---

## 4. Plan

### 4.1 The Tier 3 theorem (draft statement)

**Setting.**
- The background g0 of sec:loc-setting and sec:bg-data, with 𝒞_out = {u = 0}, 𝒞_in = {v = 0} and corner S.
- The rectangle Q1 = [0, u1] × [0, v1] lies in the set G of prop:two-dust-background (d), transported by
  lem:two-dust-reparametrisation, as in Tier 1.
- Integers k ≥ 6 and m ≥ m0(k), as in Tier 1 §3.4.

**Hypotheses.**
- Class data in the gauge of eq:loc-double-null on 𝒞_out^(v1) and 𝒞_in^(u1), smooth on S³ in the sense of T3-0 below.
  - The corner data are the background's.
  - The data are within ε of the background's in C^m.
  - There is **no support restriction in angle**.
- Densities q_in ≥ 0 on 𝒞_out and q_out ≥ 0 on 𝒞_in, smooth.
- Optionally, further families: invariant phases that are eikonals of g0 without caustics near Q1 × S³, with smooth
  densities that vanish near the points where 𝒞_out ∪ 𝒞_in meets the axes.

**Conclusions.** There are ε0, C and ε2 such that for ε ≤ ε0:
- **(a) Existence.** There is a smooth class solution of eq:class-system on Q1 × S³, in the gauge of eq:loc-double-null
  (the metric functions satisfy the axis conditions of §1.2), that induces the data.
- **(b) Estimate.** ‖g − g0‖_(C^j(Q1 × S³)) ≤ C_j ε for j ≤ k − 3, and the solution is smooth.
- **(c) Uniqueness.** On Q1 × S³, or on any sub-rectangle, a smooth class solution in the same gauge with the same data
  and within ε2 of g0 in C^k equals it.
- **(d) Localisation.**
  - g = g0 on every sub-rectangle [0, u′] × [0, v′] on whose two faces the data are the background's.
  - If the angular supports avoid {ϑ < α}, the solution equals g0 on a neighbourhood of axis 2 that shrinks at the
    angular speed of Tier 1's L7. The same holds at axis 1 with π/2 − ϑ in place of ϑ.

Tier 1's theorem is the special case of band data. It differs only in that Tier 1 states the region G_* explicitly.

### 4.2 The system

Keep Tier 1's unknowns U = (g, p_A, Θ_A, q_A) and the gauge vector D̃ = D(g) − W̊ of L1. Replace L4 by the following.

- **(i) Both adapted families use the axis closure.** Away from the axes they use S_A; within δ_* of the axes they use
  S_A^ax, joined by a partition of unity as in Step 6 of thm:class-stability (81:1500–1505).
  - No ζ_A is used for the two adapted families. Their phases have no caustics on a neighbourhood of Q1 × S³ and the
    collar.
  - The further families keep the cut-offs ζ_A of sec:class-augmented, vanishing near the face-axis points.
- **(ii) A space-time cut-off ξ replaces the angular cut-off χ.**
  - ξ equals 1 on a neighbourhood of Q1 × S³ and of the strip of P along the faces, and supp ξ ⊂ 𝒩 (the neighbourhood of
    L0 on which the background is defined).
  - The system is 𝔄_ξ(U) := ξ 𝔄(U) + (1 − ξ) A^0(Ů) ∂_τ(U − Ů).
  - It is symmetric hyperbolic, trivial outside a compact set, and exactly solved by Ů.
- **(iii) The forcing.** On a ball 𝒟_ρ about Ů in H^k, the right side satisfies (F1)–(F3): by lem:class-leaf-differences
  (a) and (b) near the axes, and by rem:class-kato-local elsewhere. This is Step 9 of thm:class-stability without the
  restarts.

### 4.3 Lemmas and outline proofs

The sizes are chapter lines.

- **T3-0 (cone data through the axes). New; 60–90 lines.**
  - *Statement.* prop:loc-cones and the 𝒞_in analogue that S-CIVP §1.2 asks for hold for data that reach the axes, on
    every generator including the axis generators. The variables are
    - ϕ̃ := ϕ − ϕ0 and ℓ̃_i := ℓ_i − ℓ_i^0, smooth on S³ with the parity and conical conditions;
    - the shift as the smooth vector field b ∂_ϑ, so b is odd at the axes.
  - *Proof, first constraint.* With y = y0 ỹ, where y0 = e^(ϕ0) = R (sin ϑ cos ϑ)^(1/3), the first line of eq:loc-cone
    becomes a linear ODE for ỹ with smooth coefficients, regular on the axis generators. Only ∂_v ℓ_i enters.
  - *Proof, second constraint.* The second line is the ϑ-component of the 1-form (Ric − T)(∂_v, ·) on the sections, a
    tensorial ODE for the shift with coefficients smooth on S³. The cot ϑ terms of r combine into
    cot ϑ ∂_v(ϰ_1 − ϰ_3 + log sin ϑ) = O(ϑ), by the conical condition.
  - *Localisation.* Localisation by generators is as before.
  - Tier 1's L2 on the axis generators uses this lemma.
- **T3-1 (Lemma A: the faces are leaves). New; 40–60 lines.**
  - *Statement.* (i) Σ_τ ∩ 𝒞_out = S_(0,c(τ)) and Σ_τ ∩ 𝒞_in = S_(c′(τ),0), with c and c′ increasing. (ii) For every
    G-invariant state V in the ball 𝔅′ of lem:class-leaf-differences (in the τ-slicing, about Ů) whose 1-jet on
    𝒞_out ∪ 𝒞_in is the formal solution's, each section near each of its axis points is V's leaf of both families
    through that point.
  - *Proof.* (i) is the Observation of §3. (ii) is Consequence 1 there.
  - It is the counterpart of the first half of step (6) of lem:loc-lens-dependence ("The leaves stay in 𝒟_s").
- **T3-2 (non-local terms on sets closed under leaves). New; 80–120 lines.**
  - *Statement.* Let D ⊂ Σ_τ be a finite union of components, each bounded near the axes by sections that are V-leaves
    of every family whose S^ax is used there, for some V ∈ 𝔅′. Then for every U ∈ 𝔅′,
    ‖σ_A[U] − σ_A[V]‖_(L²(D ∩ 𝒰_δ)) ≤ C ‖U − V‖_(L²(D)), with C depending on the Lipschitz character of the components.
  - *Proof.* Work on one component at a time.
    1. Put Ŭ := U − 𝔼(U − V), where 𝔼 is Stein's extension (thm:std-sy-extension) averaged over G, as in the proof of
       lem:loc-lens-dependence. Then Ŭ = V on D, with first derivatives.
    2. For x ∈ D near the axis, V's leaf through x lies in D, by T3-1 and the foliation. So it solves Ŭ's leaf equation
       and is Ŭ's leaf (lem:class-volterra). Hence σ_A[Ŭ](x) = σ_A[V](x).
    3. Conclude with lem:class-leaf-differences (b) for U and Ŭ.
  - Taking the components one at a time keeps the constants uniform near the corner time, where the annulus F ∩ Σ_τ is
    thin.
  - When V is a genuine solution, roles may be exchanged as in the lens lemma.
- **T3-3 (the system, jets, the forcing). Modifies L4 and adds to L2; 70–110 lines.**
  - The system is that of §4.2.
  - *Jets.* Compute them as in L2 with the local equations. Then ν_A, dp_A, Δ_A and D̃ vanish to infinite order on the
    faces.
  - *Infinite-order vanishing of the non-local residual.* Take x ∈ P at distance d from a face. Û's leaf through x lies
    between x and the face section (T3-1), within O(d) of it, and there Θ_A − □ũ_A = O(d^∞). The smooth dependence of
    the Volterra leaves (proof of lem:class-leaf-differences (a)) then gives σ_A[Û] − σ_A^true = O(d^∞) with all
    derivatives.
  - Hence F̃ := 1_P 𝔄_ξ(Û) is smooth, supported in P ∩ supp ξ near the faces, with ‖F̃‖_(H^k) ≤ C ε.
- **T3-4 (existence on ℝ⁴). Modifies L5; 60–100 lines.**
  - thm:class-kato (a) on 𝒟_ρ gives local existence and continuation while ‖U − Ů‖_(H^k) ≤ η_ρ ρ.
  - *A priori bound.* 𝒩_k(U − Ů) ≤ C(ε + sup ‖F̃‖_(H^k)) on [τ_init, τ_fin], by Steps 4–8 of
    thm:class-stability-off-axes with Step 6 of thm:class-stability. The proof is on ℝ⁴, with no lateral boundaries and
    no restarts. Ů solves 𝔄_ξ exactly, so the top-order energy of the difference closes.
  - thm:class-kato-stability (a) cannot be cited, because it needs ρ = ∞ and the non-local forcing is defined only on a
    ball.
  - Smoothness follows as in thm:class-stability ("Smoothness"); G-invariance by uniqueness.
- **T3-5 (the past region). Replaces L6; 60–90 lines.**
  - *Statement.* U = Û on the closure of P.
  - *Proof.*
    1. Write the difference equation with the coefficients at Û: A^μ(Û) ∂_μ z = F(U) − F(Û) − (A^μ(U) − A^μ(Û)) ∂_μ U.
       The faces are exactly null for Û's metric and P_A(Û) is causal there. So the boundary form is ≥ 0 (Step 9 of
       thm:class-stability-off-axes, "spacelike or null"), and no tilted faces are needed.
    2. The local part of the forcing difference is ≤ C |z|. The non-local part is bounded by T3-2 with V = Û and
       D = P ∩ Σ_τ.
    3. Gronwall from z = 0 on Σ_init.
  - *Consequence.* U carries the formal jets on the faces, so T3-1 applies to U.
- **T3-6 (constraints in F). Replaces L8; 80–120 lines.**
  - *ν_A and dp_A.* Every point of F lies on an integral curve of P_A that leaves F through the face transverse to P_A
    (P_in through 𝒞_out, P_out through 𝒞_in). So ν_A ≡ 0 and dp_A ≡ 0 by prop:class-augmented (b), and p_A = du_A.
  - *D and Δ_A.* Use the energy on F itself (and, for Δ_A, on F ∩ 𝒯′_A, the P_A-tube from the faces of the supports
    together with an axis neighbourhood, as in Step 10 of thm:class-stability).
    - Through the faces the flux is zero, because the data vanish to infinite order there.
    - The lateral part of the tube is ruled by integral curves of P_A, so there is no flux through it.
    - The non-local term ½(σ_A[Θ_A]² − σ_A[div_g P_A]²) is bounded by T3-2. Take V := U, whose face sections are
      leaves by T3-5 and T3-1, and U′ := U with Θ_A replaced by div_g P_A. U′ lies in 𝔅′ because 𝒩_k controls
      div_g P_A at order k − 1 (81:1615–1617).
  - Tier 1's extension of D and Δ_A by zero into P is the step that breaks with a non-local term. It must not be used
    here.
- **T3-7 (double-null gauge through the axes). Extends L9; 30–50 lines.**
  - (u, v) := (u_out, v_in), as in L9.
  - ϑ is transported along the outgoing generators from 𝒞_in. Generators through axis points stay in the axis, since
    [P_A, K_i] = 0.
  - G-invariance gives the form eq:loc-double-null off the axes, and the axis conditions of §1.2 follow from smoothness
    in 4+1.
- **T3-8 (Lemma R: characteristic dependence; uniqueness; localisation). Replaces L7 and L10; 120–180 lines.**
  - *Lemma R.* Two smooth class solutions near g0, in the same wave gauge (with the same W̊ on the rectangle), that agree
    to infinite order on the past faces of a double-null rectangle R′ agree on R′.
  - *Proof.*
    1. Use the time function t := u + v of the first solution. Its slices meet R′ in unions of that solution's
       double-null spheres, which are its common leaves.
    2. For a genuine solution σ_A is intrinsic (Θ_h and κ2 do not depend on the choice of screen), so the axis closure
       holds in the t-slicing.
    3. Apply T3-2 with V := the first solution, and use the energy with coefficients at V.
  - *Uses.*
    - The solution on Q1 does not depend on how Û extends the data beyond v1 and u1.
    - Localisation in (u, v): apply Lemma R with the background as the first solution.
    - Uniqueness: L10's conversion to wave gauge is a semilinear and local problem, so it needs no region restriction.
    - Angular localisation near an axis not reached by the supports: the angular face {ϑ = α − W t} of
      lem:loc-lens-dependence is closed under leaves from the axis (83:464–466).
- **T3-9 (statement, the chapter-83 corollary, remarks). 60–100 lines.**
  - Add one remark that names the families condition of §5.2, and one that names what is not covered (§5).

### 4.4 How this interacts with Tier 1 and Tier 2

| Tier 1 lemma | In Tier 3 |
|---|---|
| L0 (collar) | reused verbatim |
| L1 (wave-gauge data) | reused; drop "supported near the band region" in the extension of W̊; make the extension local, so that W̊ on Q1 depends only on the face data of Q1 (needed in T3-8) |
| L2 (jets) | reused; on the axis generators it needs T3-0; plus the addendum on the non-local residual (T3-3) |
| L3 (extension) | reused verbatim, without the band |
| L4 (modified system) | replaced: ξ in place of χ, plus the axis closure (§4.2) |
| L5 (Cauchy problem) | replaced: a ball version with the bootstrap (T3-4) |
| L6 (past region) | replaced: coefficients at Û and T3-2 (T3-5) |
| L7 (finite speed, region) | not needed for the region; localisation by T3-8 |
| L8 (constraints) | replaced: energy on F (T3-6) |
| L9 (double null) | reused, plus the axis remark (T3-7) |
| L10 (uniqueness) | the wave-map conversion is reused; the gluing is replaced by Lemma R (T3-8) |
| L11 (continuation to Σ_τ0) | unchanged and optional; with Tier 3 it needs no band condition on the slice |

- **Reuse.** About half of Tier 1's text is reused unchanged (L0, L1, L3, L9 and the core of L2 and L10). The new
  analytic content is T3-0, T3-1, T3-2, T3-6 and Lemma R.
- **Advice to the Tier 1 writer.** No edit was made; these suggestions keep Tier 1 citable by Tier 3.
  1. State L1–L3 without the band. They do not use it.
  2. In L6, prefer coefficients at Û to tilted faces.
  3. In L8, prefer the energy on F with null-boundary flux to the extension by zero.
  4. If P-CIVP has not yet passed its first reading, consider writing it in the Tier 3 form directly: one theorem
     covering both, about 1,450–2,100 lines in place of 1,750–2,600 for two.
- **Tier 2.** It shares no engine with Tier 3.
  - Tier 2 is large data off the axes, by [CCTW16] on the 2+1 system. Tier 3 is small data through the axes, by
    chapter 81.
  - Together they give data that are large away from the axes and small near them, on a strip where the influence of
    the large part stays off the axes (Route E). They do not give large data at the axes.
  - Tier 2's identification option (ii) uses the Tier-1 engine "without smallness" for short times. Its axis version is
    open item §5.1 (b).

### 4.5 Placement and edits

- **Chapter 81.** A section "The characteristic problem through the axes" after Tier 1's, written as modifications. It
  holds T3-1, T3-2, Lemma R and the theorem for a general smooth class two-family solution ů on a neighbourhood of a
  double-null rectangle. One sentence in rem:class-scope.
- **Chapter 83.** T3-0 next to prop:loc-cones, and the corollary for the background. The loss sentence at 83:593–600
  shrinks to three cases: large data; non-adapted families that cross a face where it meets an axis; finite regularity
  (with [LR20, Theorem 4.6] named as the 3+1 analogue for measures).
- **Chapter 90.** The sentence planned in S-CIVP §4 becomes: data on the two null cones develop for small perturbations
  on the whole rectangle, dust included, with the axes included.
- **Chapter 95.** No new outside result is used beyond Tier 1's entries. BCM and AGS may be cited in a remark on the
  standard practice at axes. Chruściel 1990 should not be cited unless it is read.

---

## 5. What stays open

### 5.1 Large data reaching the axes

- **Why it stays open.**
  - Chapter 81's axis machinery is perturbative around a smooth solution: lem:class-leaf-differences works on balls
    about ů.
  - cor:class-short-time, the one large-data result, assumes densities that vanish within 2δ of the axes (81:1026–1032).
  - Tier 2's [CCTW16] route stops at the axes, because the 2+1 unknowns are singular there (§1.2).
- **Partial routes.**
  - **(a) Short time near the corner (Rendall's original scope at the axes).** Run thm:class-kato (a) with the
    reference path u_* := Û. This needs a version of lem:class-leaf-differences around a smooth state that is not a
    solution. That looks routine: the proof uses only the foliation and ellipticity. It was not checked; 1–2 pages if
    wanted.
  - **(b) Neighbourhood of both hypersurfaces.** Route C, the axis-regular doubly-null form; open, high risk.
  - **(c) Route D;** long.

### 5.2 Non-adapted families at the axes: the precise condition

- **What actually obstructs.** S-CIVP §3.7 attributes this case to rem:class-scope ("only one ingoing and one outgoing
  family are separated there"). But rem:class-scope concerns the high-frequency construction ("the high-frequency
  construction over a non-round background needs more", 81:1665–1668). For the Einstein–null-dust development,
  thm:class-stability allows several families at axis points in the interior (cor:class-two-dust: further families
  whose tubes avoid only the points where a lateral boundary meets an axis).
- **The Tier 3 obstruction** is the characteristic analogue of (H2′). Near a point where a face meets an axis, every
  family whose density is nonzero there must have the face section as a leaf.
  - The two adapted families satisfy this by T3-1: on 𝒞_out, v is the data's coordinate and u ≡ 0.
  - A further family satisfies it only if its phase, restricted to the face near that point, is a function of the
    face's double-null coordinate. Generically it is not.
- **Partial remedy.** A slicing bent near such points can be chosen so that its face sections are level sets of the
  restricted phases. This is possible when the phases present at that point are functionally dependent on the face; an
  example is one transverse family, or resonant families f_A(v) (prop:class-separation (d)).
- **Genuinely open:** two functionally independent transverse phases at one face-axis point.
- **What Tier 3 covers.** Further families whose densities vanish near the face-axis points. They may still reach the
  axes inside F (their tubes meet an axis only at positive distance from the faces), with the ζ cut-offs of Step 6 of
  thm:class-stability.

### 5.3 Low regularity

- The axis machinery needs H^k with k ≥ 6 (lem:class-planar-shear needs k ≥ 5; thm:class-stability needs k ≥ 6).
- Finite-regularity data in C^m with m ≥ m0(k) are within reach, as in Tier 1.
- C³ data (chapter 87) and measure-valued shells are not. Both need an [LR20]-type weak double-null theory in 4+1, which
  would be a separate paper.

### 5.4 General 4+1 without symmetry

Unchanged: a separate paper (Routes A′, C and L of S-CIVP).

### 5.5 Not affected

Chapter 87's vacuum section (S-CIVP §3.8). Vacuum has no axis difficulty, and Tier 3 adds nothing there.

---

## 6. Estimate and risks

**Size.** Chapter lines, at about 49.5 per PDF page:

| Piece | Lines |
|---|---|
| T3-0 | 60–90 |
| T3-1 | 40–60 |
| T3-2 | 80–120 |
| T3-3 | 70–110 |
| T3-4 | 60–100 |
| T3-5 | 60–90 |
| T3-6 | 80–120 |
| T3-7 | 30–50 |
| T3-8 | 120–180 |
| T3-9 | 60–100 |
| **Total** | **≈ 650–1,000 (13–20 PDF pages)** |

- Edits to chapters 83 and 90: 30–60 lines.
- If folded into Tier 1: 1,450–2,100 lines for both together.
- Expect a writer and two to four confirming readings, as for Tier 1.

**Order of work.**
1. T3-0, together with Tier 1's 𝒞_in lemma.
2. T3-1 and T3-2 (go/no-go checks GN1 and GN2).
3. T3-3 (GN3).
4. T3-4 and T3-5.
5. T3-6.
6. T3-8.
7. Theorem and corollary.

**Go/no-go checks.**
- **GN1 (Lemma A in the actual chart).**
  - Check that Tier 1's L1 chart keeps the faces at the background's 𝒞_out and 𝒞_in, parametrised by the data's (v, ϑ)
    and (u, ϑ).
  - On a perturbed example, check by computer algebra that the formal 1-jet makes Σ_τ ∩ 𝒞_out solve both families'
    eq:class-leaf-volterra. The same machinery as chapter 81's cas checks will do.
- **GN2 (the extension in T3-2, uniformly in τ).** Near τ_c = τ(S) the two face sections approach each other.
  Extending one component at a time keeps Stein's constants uniform. Check that lem:class-leaf-differences (b) is
  applied on 𝒰_(2δ) for one component only.
- **GN3 (smoothness of F̃).** Check the infinite-order vanishing of the non-local residual of Û at the faces (T3-3),
  including all derivatives of the Volterra leaves in the leaf parameter.

**Risks.**
- **R1 (moderate): T3-2 and T3-1.** All of Route B rests on them. They fail if any family whose S^ax is active near a
  face-axis point does not have the face section as a leaf. This is the reason for the family hypothesis.
- **R2 (moderate): T3-3.** Infinite-order vanishing of the non-local residual (GN3).
- **R3 (low to moderate): T3-4.** The ball-restricted Cauchy stability on ℝ⁴. thm:class-kato-stability (a) does not
  apply, because ρ < ∞. The bootstrap of thm:class-stability-off-axes on ℝ⁴ with the axis Step 6 has to be written out
  (about one page).
- **R4 (moderate): T3-6.** The energy region for Δ_A in F: it must contain a full axis neighbourhood (as 𝒯′_A in Step 10
  of thm:class-stability), be ruled by P_A curves on its lateral part, and be closed under leaves by the face
  separation.
- **R5 (low to moderate): Lemma R.**
  - It uses the time function u + v of one solution, with a chart adapted to it.
  - lem:class-leaf-differences must be applied in that slicing (its constants depend on the slicing).
  - W̊ on Q1 must depend only on the face data of Q1 (choose the extension in L1 accordingly).
- **R6 (low): T3-0.** The tensorial form of the second cone constraint, and the conical condition in the data.
- **R7 (structural): smallness and the families condition are real restrictions.** The theorem must state them, and the
  loss sentence in chapter 83 must keep them.
- **R8 (literature).**
  - Rinne–Stewart and Huneau–Luk were read only in abstract.
  - Chruściel 1990 was not read.
  - No outside result is used in any proof step of the plan. Every step cites chapter 81, chapter 83, or Tier 1.
