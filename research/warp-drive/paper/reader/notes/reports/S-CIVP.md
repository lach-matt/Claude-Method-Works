# S-CIVP: the characteristic initial value problem for five-dimensional Einstein–null dust behind chapter 83's cone data (item m4)

Scoping report for the writer. Nothing under `reader/` was edited; `assemble.py` was not run.

**Read for this report.** Chapter 83 (lines 1–160, 519–602, 1675–1700); chapter 80 (1–330); chapter 81 (1–380, 548–700,
846–1040, 1365–1671); chapter 87 (440–450, 566–580, 1150–1253); chapter 01 (100–130, 180–195); chapter 02 (1–75);
chapter 03 (355–380); chapter 90 (180–225); chapter 95 (1–14, 206–350, 478–490); chapter 98 (all); notes/reviews R2-83,
R3-83, R4-83; INTEGRATION.md 1105–1125 and 1205–1275; STATUS.md line 59; crosswalk/83-localised-data.tsv rows 11–21.

**P-K83c.** There is no `notes/reports/P-K83c.md`. The proof file `proofs/P-K83c.md` was deleted at M-83c ("proof file
deleted", STATUS.md:59) and was never committed (`git log --all` has no trace of it). Its conclusion on m4 survives in
INTEGRATION.md:1255–1257, STATUS.md:59, R2-83 §2(c) (line 82) and the crosswalk row of prop:loc-cones
(crosswalk/83-localised-data.tsv:21, "P-K83c.md:289-292 … Block 4 … the closing paragraph names what is lost for cone
data with dust (item m4; no development asserted)").

## Summary

- **The theorem chapter 83 needs.** Existence (and uniqueness in the gauge) of a development of class
  (T² × both reflections) characteristic data for the **4+1 Einstein equations with two null dusts adapted to the
  double-null foliation**: an ingoing family with phase v, whose density is free on the outgoing hypersurface
  𝒞_out = {u = 0}, and an outgoing family with phase u, whose density is free on the ingoing hypersurface
  𝒞_in = {v = 0}. The data sit on these two transversal null hypersurfaces, which meet in a round corner S³ of radius 5;
  they are not the light cone of a point. The solution is needed in the double-null gauge of eq:loc-double-null, at
  least on a future neighbourhood of both hypersurfaces. A neighbourhood of the corner does not suffice, because the
  dust lies at 3 < v < 4.5 and at 5.7 < u < 7.2. The data are smooth and equal the background's outside an angular band.
- **Literature.** No published theorem covers this, with or without the symmetry. The closest results are
  Luk–Rodnianski [LR20, Theorem 4.6, p. 29], for Einstein–null dust with two measure-valued families in 3+1 only, and
  Chruściel–Tagne Wafo–Gray [CTG23, Theorem 1.1], for vacuum in every dimension. Rendall (1990) covers vacuum or perfect
  fluid in 3+1, near the corner only. Cabet–Chruściel–Tagne Wafo [CCTW16] treat symmetric hyperbolic systems in
  doubly-null form, and apply this to Einstein only in 4D, in vacuum or with wave-type matter. Chruściel–Paetz [CP12]
  assume that the matter evolution is well posed, which fails for null dust in a general gauge. P-K83c's finding
  stands.
- **Recommended route (Tier 1).** A Rendall-type reduction of the characteristic problem to chapter 81's Cauchy theory
  for the augmented class system (Aug1)–(Aug4), off the axes. The perturbation is localised away from the axes by a
  cut-off and finite speed. The wave-gauge data on the two hypersurfaces come from the scheme of [CP12, §3.1], which
  admits null dust as a source. The result: for **small** band-localised data (0 < ϑ_a < ϑ_b < π/2), with or without
  dust, there is a smooth class development in the double-null gauge on the explicit set {uv ≤ δ_*²} of the background
  rectangle, which contains a future neighbourhood of both hypersurfaces. It is unique in the gauge near the background
  and equals the background outside the domain of influence of the band. Expected size 1,100–1,600 lines (22–32 PDF
  pages); most steps reuse confirmed chapter-81 text.
- **What stays open.** Dropping smallness (Tier 2: [CCTW16, Theorem 3.9] applied to the T²-reduced 2+1 double-null
  system, about 1,000–1,400 further lines, with two go/no-go checks). Perturbations that reach the axes (Tier 3).
- **Chapter 87.** The dust work does not close the hypotheses (F1)–(F3) of lem:tl5-continuation. A separate short vacuum
  section would, for smooth data only (geometric uniqueness from [CTG23] + [CCTW16, Theorems 4.1, 4.3], about 300–500
  lines). It changes no result: the data of def:tl5-problem are C³, and (H1)–(H3) are not established.

---

## 1. What is missing

### 1.1 Where chapter 83 rests on it

Opening, 83:8–9:

> "On the null cones the constraints are ordinary differential equations along the generators, and data localised in an
> angular band exist exactly ([[prop:loc-cones]])."

The gauge, 83:527–531:

> "In the double-null gauge of the class, g = −2Ω² (du ⊗ dv + dv ⊗ du) + γ_ϑ (dϑ − b du)² + e^(2A_c) dφ1² + e^(2A_s)
> dφ2², with Ω, γ_ϑ, b, A_c, A_s functions of (u, v, ϑ), the cone 𝒞 := {u = u_c} is ruled by the null generators ∂_v."

prop:loc-cones, 83:572–578:

> "On the outgoing cone 𝒞_out = {u = 0} write γ_ϑ = e^(2ϕ + 2ℓ_1), A_c = ϕ + ℓ_2, A_s = ϕ + ℓ_3 with ℓ_1 + ℓ_2 + ℓ_3 = 0,
> keep Ω the background's, and let the free data (ℓ_1, ℓ_2, ℓ_3) and the null dust densities on 𝒞_out equal the
> background's outside a compact subset of a band {ϑ_a < ϑ < ϑ_b} × [0, v_1], the corner sphere's data (ϕ, ∂_vϕ, b, ∂_v b
> at v = 0) being the background's. Then the constraints Ric(∂_v, ∂_v) = T(∂_v, ∂_v), Ric(∂_v, ∂_ϑ) = T(∂_v, ∂_ϑ) on
> 𝒞_out determine ϕ and b on every generator on which e^ϕ stays positive, and the resulting cone data equal the
> background's on every generator with ϑ ∉ [ϑ_a, ϑ_b]. No smallness is used for the localisation; for small
> perturbations e^ϕ stays positive on [0, v_1]."

### 1.2 The problem, precisely

| Item | What chapter 83 needs |
|---|---|
| Dimension | 4+1. The sections are S³. The corner S := 𝒞_out ∩ 𝒞_in is round with R = 5, R_u = −0.47, R_v = 1/2, mass 3/2 (83:27–30, sec:bg-data). |
| Symmetry | The class G = O(2) × O(2): the T² action and both reflections φ_i ↦ −φ_i (sec:class; 83:59–60). The metric functions depend on (u, v, ϑ) (eq:loc-double-null). The perturbation is supported in an angular band. Tier 1 requires the band to avoid the axes, 0 < ϑ_a < ϑ_b < π/2, as thm:loc-bent-slice (b) does on slices (83:157–158: "ϑ1 < ϑ < π/2 − ϑ1"). |
| Matter | Two null dusts adapted to the double-null foliation. Ingoing: T_in = q_in dv ⊗ dv, transported along g⁻¹dv ∝ ∂_u + b∂_ϑ; background density 𝒜(v)/R³, the shell, on 𝒞_out ∩ {3 < v < 4.5}. Outgoing: T_out = q_out du ⊗ du, transported along g⁻¹du ∝ ∂_v; background density ℬ(u)/R³, the packet, on 𝒞_in ∩ {5.7 < u < 7.2} (eq:two-dust-limit, eq:bg-profiles). q_in is free data on 𝒞_out and q_out on 𝒞_in, both ≥ 0. For adapted families T(∂_v, ∂_ϑ) = 0 on 𝒞_out, so the second constraint of prop:loc-cones is source-free. Further invariant families with densities in the band are an optional generalisation; chapter 81 off the axes allows any N_f. |
| Gauge | The double-null gauge of the class, eq:loc-double-null, with u and v the dust phases. On 𝒞_out, Ω is the background's (this is data). On 𝒞_in the gauge b = 0 is not yet stated in the chapter and must be fixed. The corner data are the background's. |
| Data surfaces | Two transversal null hypersurfaces, 𝒞_out^(v1) = {u = 0, 0 ≤ v ≤ v1} and 𝒞_in^(u1) = {v = 0, 0 ≤ u ≤ u1}. This is not a light cone (no vertex). For the dust cases, v1 > 4.5 and u1 > 7.2. |
| Data regularity | C^∞, as everywhere in the chapter: thm:loc-bent-slice is stated in C^∞, and the bump profiles are C_c^∞ with C^∞ square roots (83:38–40). The perturbations equal the background's outside a compact subset of the band × [0, v1] (and the analogue on 𝒞_in). The densities are C^∞, ≥ 0 and compactly supported. Chapter 83 uses no finite-regularity class and no measure-valued density. Finite regularity arises only in chapter 87 (env is C³). |
| Size | The chapter's regime is "data near the background's data" (90:191–192). prop:loc-cones itself uses no smallness for the localisation. |
| Domain | At least a future neighbourhood of 𝒞_out^(v1) ∪ 𝒞_in^(u1), for parity with the vacuum sentence, which uses the neighbourhood theorem [CTG23]. A neighbourhood of the corner (Rendall's theorem) is useless here, because the dust is far from S. Near the background, the natural domain is the part of the background's development of the rectangle [0, u1] × [0, v1] on which the band's influence stays off the axes. |
| Uniqueness | In the gauge, among smooth class solutions (for small data: near the background). |
| Output | A smooth solution that induces the given data and equals the background outside the domain of influence of the band (localisation is the chapter's subject). |

Two points of formulation for the writer:

- prop:loc-cones is stated on 𝒞_out only, while the closing paragraph also names "the packet on 𝒞_in". The 𝒞_in analogue
  is **not** the literal swap u ↔ v, because eq:loc-double-null puts the shift in du. With b = 0 on 𝒞_in, the
  Raychaudhuri constraint Ric(∂_u, ∂_u) = q_out fixes the conformal factor on 𝒞_in. The ϑ-constraint on 𝒞_in becomes a
  transport equation for the torsion, which holds ∂_v b: it determines a transverse derivative (a jet), not data. This
  needs one lemma, about one page.
- The data are two hypersurfaces through a corner, so no vertex regularity (the difficulty of [CBCM10]) arises.

### 1.3 What chapter 83 states in its place, and the loss

83:593–600:

> "When these cone data carry no dust, their vacuum development near the two cones exists by [CTG23, Theorem 1.1]
> ([[thm:std-ctg-neighbourhood]]): this is the case when v_1 < 3, so that 𝒞_out ∩ {v ≤ v_1} lies before the shell, the
> dust densities are left zero there, and 𝒞_in is taken only on u < 5.7, before the packet; both cones then carry
> vacuum data of Tangherlini's metric of mass 3/2 outside the band, and the two cones meet transversally in the corner
> sphere. [CTG23, Theorem 1.1] concerns vacuum data only. For cone data that carry dust, among them every perturbation
> of the shell on 𝒞_out ∩ {3 < v < 4.5} or of the packet on 𝒞_in ∩ {5.7 < u < 7.2} and every density added in the band,
> no development is asserted here: [[prop:loc-cones]] gives the cone data only, and no result of this paper uses their
> development."

**The loss.** For every set of cone data that carries dust, no spacetime is known to have those data. This includes
every localised perturbation of the shell or of the packet and every added density. A development is asserted only
for vacuum data before the shell and before the packet. The record agrees. R-83 m4: "cone development with null dust
needs an Einstein-null-dust characteristic existence theorem" (INTEGRATION.md:1214–1216). P-K83c: "chapter 83's cone
data with dust (m4) rests on a characteristic initial value problem for five-dimensional Einstein-null dust that no
published theorem covers (Luk-Rodnianski is 3+1 only); the chapter states only what holds and names the loss"
(INTEGRATION.md:1255–1257). R2-83 (c) confirms that this wording is the narrowest true statement and that "No other place
claims more" (R2-83:82); R3-83 and R4-83 leave it unchanged.

### 1.4 What is weakened

- **Chapter 83.** prop:loc-cones remains a statement about constraint data. The opening (83:8–9) is accurate as stated:
  it claims cone data, not developments. Because of the loss:
  1. Localisation on null hypersurfaces is not localisation of a spacetime once dust is present, which is exactly the
     case of the shell and the packet.
  2. The cone result cannot be compared with, or carried to, the slice results (thm:loc-bent-slice, thm:charge-sign),
     since no dust-carrying cone data are evolved.
  3. Even in vacuum, the development is used only via [CTG23]. That theorem gives neither uniqueness in the gauge
     (87:1180–1194) nor localisation of the development.
- **Chapters 01, 03, 90.** Nothing in these chapters depends on the cone development. 01:188–192 only names chapter 83.
  03:362–372 summarises thm:charge-sign, which is about data on Σ_τ0. 90:191–200 states the slice results only. They are
  not weakened, but they are silent about the cone result and its loss. Chapter 90 could add one sentence, now or after
  the work (§4).

---

## 2. Literature survey (each source opened and read at the pages cited)

| Source | Dimension | Matter | Data surfaces | Regularity | Domain | Covers? |
|---|---|---|---|---|---|---|
| Rendall 1990 | 3+1 (Einstein part) | vacuum, perfect fluid | two null hypersurfaces | C^∞ | neighbourhood of S | no |
| CCTW16 | any n for systems; 4D for Einstein | vacuum, wave-type matter | two null hypersurfaces | H^ℓ, ℓ > (n+9)/2; smooth | neighbourhood theorem | no |
| CTG23 | n+1 ≥ 5 | vacuum (Λ) | two null hypersurfaces | smooth (Sobolev remark) | neighbourhood theorem | no |
| CP12 | n+1 | vacuum; sources with T·ℓ tangential, *assuming* a well-posed matter evolution | two hypersurfaces, light cone | smooth | near S | no |
| CBCM10 | n+1 ≥ 3 | vacuum; scalar, Maxwell for constraints | light cone (vertex) | smooth | near vertex | no |
| Choquet-Bruhat–Chruściel 2012 | n+1 | massive Vlasov, smooth f | light cone | smooth | near vertex (sketch) | no |
| Luk 2012 | 3+1 | vacuum | two null hypersurfaces | smooth (H⁵-type sizes) | neighbourhood theorem, unique in double null | no |
| LR20 | 3+1 | **two null dusts, measure-valued** | two null hypersurfaces | strongly angularly regular | strip [0, u*] × [0, u̲*], u* ≤ ε | no (3+1) |
| RSR18 | all n+1 | vacuum | two null hypersurfaces | smooth | neighbourhood (Thm A.1 by reference to Luk) | no |
| Moschidis 2017, 2018 | 3+1 | null dust / massless Vlasov, Λ < 0 | light cone, two hypersurfaces | smooth | local; maximal development | no (spherical symmetry) |
| Shen–Song–Wan 2026 | 3+1 | Vlasov, smooth f | two hypersurfaces | smooth | slab (stated) | no |
| Huneau–Luk 2018, 2025 | 3+1, U(1) | null dust / Vlasov | Cauchy, elliptic gauge | small | fixed interval | no (not characteristic) |

The entries in detail:

1. **Rendall**, *Reduction of the characteristic initial value problem to the Cauchy problem and its applications to
   the Einstein equations*, Proc. R. Soc. Lond. A 427 (1990) 221–239, doi:10.1098/rspa.1990.0009.
   - Read: the abstract on NASA ADS, which says "the characteristic initial value problem for the Einstein equations in
     vacuum or with perfect fluid source is well posed when data are given on two transversely intersecting null
     hypersurfaces".
   - Scope, as described by three sources that quote it: a reduction to the Cauchy problem for quasilinear wave
     equations and symmetric hyperbolic systems [CCTW16, p. 5]; existence in a neighbourhood of the intersection only
     [Luk12, pp. 1, 10, Theorem 3]; the Einstein application on "two three-dimensional characteristic hypersurfaces",
     extended to higher dimensions in [CBCM10] [CTG23, p. 2].
   - The full text is paywalled and was not read, so no lemma numbers are given. If the writer quotes a lemma, obtain
     the paper first. Otherwise prove the jet-extension step in-house (§3.3, L3) and cite Rendall for the method only.
   - Not covered: null dust, which is the pressureless null limit of a perfect fluid and has characteristics tangent to
     the data hypersurfaces; 4+1; anything beyond a neighbourhood of S.
2. **CCTW16**: A. Cabet, P. T. Chruściel, R. Tagne Wafo, Dissertationes Math. **515** (2016), 72 pp.,
   arXiv:1406.3009v2. Read pp. 4–11, 13–16, 21–22, 26, 29–35, 37–56.
   - Theorem 3.9 (p. 32) and Corollary 3.11 (p. 35). Quasilinear first-order symmetric hyperbolic systems in
     *doubly-null form* (2.7)–(2.8) (p. 7): A^u is nonzero only in the ϕϕ block, A^v only in the ψψ block, and both are
     positive. They live on [0, a0] × [0, b0] × Y, with Y compact without boundary of dimension n − 1. The data are ϕ on
     N₋ and ψ on N₊, in ∩_j C^j(H^(ℓ−j)(Y)) with ℓ > (n+9)/2, and the transport equations on N± must be globally
     solvable ((3.100)–(3.101)). Then there is a unique solution on ([0, a*] × [0, b0] ∪ [0, a0] × [0, b*]) × Y; see
     also Remark 3.12 (p. 35).
   - Theorem 4.1 (p. 40): eikonal functions near the hypersurfaces, any n. Theorem 4.3 (p. 48): semilinear wave systems,
     neighbourhood of the maximal domain of the transport equations, any n, smooth for smooth data.
   - Theorem 5.3 (p. 54): smooth 4D vacuum, "unique up to diffeomorphism when U is appropriately chosen". §5.2 (p. 56):
     sources satisfying wave equations. §5.3: conformal field equations.
   - The restriction to dimension 4 is explained on pp. 40 and 50: harmonic coordinates lose a derivative on passing to
     double-null coordinates.
   - Not covered: null dust; Einstein in 4+1.
   - Bibliographic nit: the edition's [CCTW16] entry (98:26–28) prints "Dissertationes Math. (2016), 1–72" without the
     volume 515.
3. **CTG23**: arXiv:2305.07306v1, still a preprint (no journal version found). Read in full.
   - Theorem 1.1 (pp. 2–3), quoted correctly in thm:std-ctg-neighbourhood.
   - Method: a higher-dimensional NP/Christodoulou–Klainerman frame system whose Bianchi subsystems are symmetric
     hyperbolic (§3, after Senovilla), plus the proof of [CCTW16, Theorem 5.3] (§4).
   - Vacuum with Λ, smooth data ("remains true in suitable Sobolev spaces", p. 3). [RSR18, Theorem A.1] is noted as an
     alternative proof.
   - Not covered: matter. Adding null dust is new work. The Ricci terms J_jkl of their (2.17)–(2.18) bring angular
     derivatives of the densities into the Bianchi subsystems (for example J_00a in (B.6e)), and these would have to be
     renormalised away.
4. **CP12**: Class. Quantum Grav. 29 (2012) 145006, arXiv:1203.4534v2. Read pp. 1–16, 22. Everything is in n+1.
   - Theorem 2.1 (p. 5): Rendall's theorem in n+1 dimensions. The text says it "extends easily to non-vacuum models"
     with T_22, T_2A, T_12 of the stated forms.
   - §3.1 (pp. 6–10): all components of the metric are taken as data, and a gauge source W̊ on N₁ ∪ N₂ is computed from
     the wave-map gauge constraints ((19), (22), (26), (29), (31)–(36)). This is for matter with
     T_μν ℓ^ν = T_μ(g, φ, ∂_∥g, ∂_∥φ, x) (15). It produces a solution near S only "assuming that the reduced Einstein
     equations can be complemented by well-posed evolution equations for the matter fields" (p. 9).
   - §4.3 (p. 16): uniqueness is "understood locally".
   - Not covered: null dust fails the standing assumption. In a general gauge its evolution loses a derivative
     (chapter 81, the paragraph after def:class-system; prop:class-augmented (a)).
   - Usable: null dust does satisfy (15), so the constraint scheme of §3.1 is exactly the data step L1 of Tier 1.
5. **CBCM10**: Choquet-Bruhat, Chruściel, Martín-García, Ann. Henri Poincaré 12 (2011) 419–482, arXiv:1006.4467.
   Read pp. 1–14, 26, 32, 46–50, 60, 67–74.
   - The light cone of a point, n+1 ≥ 3. The wave-map gauge constraints form hierarchical ODEs (§§6–12, Theorem 12.1,
     p. 67), with sources of the form (7.7) (scalar and Maxwell fields, §7.7, pp. 46–47).
   - Theorem 5.1 (p. 26): S_αβ ℓ^β = L_α + C_α on a null hypersurface.
   - Existence near the vertex via Cagnac–Dossa (Theorems 3.1–3.2, pp. 12–13); vacuum geometric uniqueness near the
     vertex (Theorem 13.1, p. 69).
   - Not covered: a vertex problem, no dust.
6. **Choquet-Bruhat–Chruściel**, *Cauchy problem with data on a characteristic cone for the Einstein–Vlasov equations*,
   arXiv:1206.0390. Read in full.
   - n+1 dimensions, particles with a continuous spectrum of positive masses, smooth f; existence near the vertex is
     sketched (§§3, 9).
   - Not covered: null dust is a massless, measure-valued Vlasov field.
7. **Luk12**: IMRN 2012, no. 20, 4625–4678, arXiv:1107.0898. Read pp. 1–3, 7, 9–14, 23, 38–42.
   - Theorems 1 and 2 (pp. 2, 9): 3+1 vacuum in double-null gauge, existence on {0 ≤ u ≤ ε, 0 ≤ u̲ ≤ I}, unique in
     double-null coordinates (Theorem 5, p. 14).
   - §3 re-proves Rendall's theorem in double null; §6 is the last-slice argument with harmonic-gauge Cauchy problems.
   - Not covered: vacuum, 3+1.
8. **LR20**: Luk–Rodnianski, *High-frequency limits and null dust shell solutions in general relativity*,
   arXiv:2009.08968, still a preprint. Read pp. 1, 4, 6, 10–11, 28–29, 85.
   - Theorem 4.6 (p. 29; informal Theorem 1.13, p. 6): the 3+1 Einstein–null dust system with two families, possibly
     measure-valued, in double-null gauge, with no symmetry.
   - Data are "strongly angularly regular" (Definition 4.5, p. 28: W^(6,∞) in the angular directions, ∂_u γ̂ in L², and
     Radon measures with six angular derivatives, (4.4)–(4.5)).
   - Result: existence and uniqueness of an angularly regular weak solution on [0, u*] × [0, u̲*] × S², with u̲* ≤ I and
     u* ≤ ε.
   - Not covered: 3+1 with S² sections (Hodge systems on 2-spheres; the hairy-ball restriction of Remark 4.9, p. 29). It
     is the exact 3+1 analogue of what chapter 83 needs.
9. **RSR18**: Rodnianski, Shlapentokh-Rothman, Geom. Funct. Anal. 28 (2018) 755–878, arXiv:1705.09674. Read pp. 1–6,
   11, 21, 25, 35, 75–76, 85.
   - §3: the double-null equations in all dimensions, with Ricci terms in the constraints (Proposition 3.3, p. 25).
   - Theorem A.1 (p. 75): vacuum local existence in all dimensions, proved by "an examination of the proof in [Luk12]".
   - Not covered: vacuum only. It is the template formalism for a Luk-type proof in 4+1.
10. **Moschidis**: arXiv:1704.08685 (Theorem 1, p. 4; §5.2) and arXiv:1812.04274 (Theorem 1.1, p. 4; Proposition 4.2,
    p. 43). Read the introductions and statements.
    - Einstein–null dust and Einstein–massless Vlasov in spherical symmetry, 3+1, Λ < 0, characteristic
      initial-boundary problems.
    - Not covered: spherical symmetry only. The round 4+1 problem is already chapter 80's prop:two-dust-background.
11. **Shen–Song–Wan**, arXiv:2611.15318 (November 2026), §1. A 3+1 Einstein–Vlasov characteristic problem with smooth f
    and compact momentum support. Theorems 1.11–1.12 (p. 8) state a Luk-type slab theorem, taken from earlier work. Not
    covered.
12. **Huneau–Luk** [HL18, HL25], as quoted in rem:class-polarised: the Cauchy problem in elliptic gauge with smallness,
    polarised U(1), 3+1. Not characteristic.

**Combinations.**

- [CTG23] with the renormalisation of [LR20] would give a 4+1 frame system with dust in the form of [CCTW16]. This is
  plausible but unproved (Route C below).
- [RSR18, §3], [LR20] and [Luk12] would give a Luk-type proof in 4+1. Plausible, but long (Route L).
- Rendall's reduction with chapter 81 is Tier 1 (Route R). It needs lemmas of our own.
- [CCTW16, Theorem 3.9] applied to the T²-reduced 2+1 system is Tier 2 (Route CQ).

None of these is published. **P-K83c's finding is confirmed.**

---

## 3. Recommended route and full proof plan

### 3.1 Routes considered

| Route | Idea | Delivers | Length | Risk | Verdict |
|---|---|---|---|---|---|
| **R** | Rendall reduction to chapter 81's augmented Cauchy system, off the axes; cut-off localisation; [CP12, §3.1] data | small band-localised data; region {uv ≤ δ_*²}; uniqueness near the background | 1,100–1,600 lines | moderate (interfaces) | **recommended (Tier 1)** |
| CQ | T²-reduced 2+1 double-null system (prop:reduction with dust) in the form of [CCTW16] (2.8); localised; Theorem 3.9 | no smallness; neighbourhood theorem; uniqueness in gauge | +1,000–1,400 | moderate to high (fit, identification) | Tier 2 |
| Q | as CQ, but Luk-type a priori estimates in 2+1 instead of the black box | as CQ | +1,300–1,800 | moderate | alternative to CQ |
| L | Luk-type proof in full 4+1 ([RSR18] formalism, [LR20] renormalisation) | no symmetry needed | 3,000+ | high (Hodge theory on S³) | not recommended |
| C | [CTG23] frame system with dust, renormalised; [CCTW16, Theorem 3.9] | 4+1, no symmetry | +1,500–2,500 | high (derivation, closure) | not recommended |
| 1+1 | radial reduction | round data only | — | — | already chapter 80; insufficient |

Why R. The class structure makes chapter 81's augmented system lossless off the axes (prop:class-structure,
prop:class-augmented (a)). Chapter 81 already proves its Cauchy theory, stability, G-invariance and constraint
propagation (thm:class-kato, thm:class-kato-stability, rem:class-kato-local, Steps 9–10 of thm:class-stability-off-axes),
and that text has been confirmed by four readings. Rendall's trick needs only finite speed and Cauchy uniqueness for a
**local** smooth symmetric hyperbolic system. Localising away from the axes removes the only non-local piece (the planar
shear) and the axis singularities of the reduction. Dust adapted to the double-null foliation is exactly two families,
one ingoing and one outgoing, which are separated at the axes (prop:class-separation (b)). Near the axes nothing changes:
the solution there is the background.

### 3.2 The Tier 1 theorem (draft statement)

Setting: the background g0 of sec:loc-setting and sec:bg-data, with 𝒞_out = {u = 0}, 𝒞_in = {v = 0} and corner S.
Fix u1, v1 > 0 with the rectangle Q1 := [0, u1] × [0, v1] in the set G of prop:two-dust-background (d), transported to
chapter 83's chart by lem:two-dust-reparametrisation. Fix 0 < ϑ_a < ϑ_b < π/2, and integers k ≥ 6 and m ≥ m0(k)
(§3.4).

**Theorem (development of localised cone data near the two-dust background).** Assume:

- class data in the gauge of eq:loc-double-null: on 𝒞_out^(v1), (ℓ_1, ℓ_2, ℓ_3) and q_in ≥ 0, with Ω the background's;
  on 𝒞_in^(u1), the analogous conformal data and q_out ≥ 0, with b = 0; the corner data the background's;
- all of these smooth, equal to the background's outside compact subsets K_out ⊂ (ϑ_a, ϑ_b) × [0, v1] and
  K_in ⊂ (ϑ_a, ϑ_b) × [0, u1], and within ε of the background's in C^m.

Then there are ε0, C, ε2 > 0, depending only on the background, Q1, the band, k and m, such that for ε ≤ ε0:

- **(a) Existence.** On G_* := {(u, v) ∈ Q1 : uv ≤ δ_*²} × S³ there is a smooth class solution (g, u, v, q_in, q_out)
  of eq:class-system with N_f = 2 and phases u, v. It is in the gauge of eq:loc-double-null, induces the given data, and
  completes the 𝒞_in analogue of prop:loc-cones. Here δ_* := η/C_0, η := ½ min(ϑ_a, π/2 − ϑ_b), and C_0 := 2 sup over
  Q1 of √2 e^σ/R (background bounds). So G_* contains the strips {u ≤ δ_*²/v1} and {v ≤ δ_*²/u1}, a future
  neighbourhood of both hypersurfaces. The same proof gives the larger set G of L7.
- **(b) Localisation.** g = g0 and q = q0 outside the causal future of K_out ∪ K_in. That causal future lies in
  {ϑ_a − η ≤ ϑ ≤ ϑ_b + η} on G_*.
- **(c) Estimate.** ‖g − g0‖_(C^j(G_*)) ≤ C_j ε for j ≤ k − 3, and the solution is smooth.
- **(d) Uniqueness.** A smooth class solution in the same gauge, on a past subset of G_*, with the same data and within
  ε2 of g0 in C^k, equals it there.

Vacuum data are included. For vacuum data of any size, [CTG23] remains the existence statement; the theorem adds
uniqueness in the gauge and localisation for small data.

Placement. The general form belongs in chapter 81: the same statement around any smooth class solution ů defined on a
neighbourhood of a double-null rectangle, with two adapted families and any further families supported in the band.
The background case is then a corollary in chapter 83. The background-specific input is only the collar (L0) and the
explicit δ_*.

### 3.3 Lemmas and outline proofs

The unknowns are chapter 81's U = (g, p_A, Θ_A, q_A), A ∈ {in, out}, written in first-order form as in Step 9 of
thm:class-stability-off-axes. 𝔄(U) = 0 denotes (Aug1)–(Aug4), with the gauge vector D(g) replaced by D̃ := D(g) − W̊
for a fixed smooth gauge source W̊ (L1). Ů is the background with p̊_A = dů_A and Θ̊_A = □ů_A. F := {u ≥ 0, v ≥ 0} is the
future region and P its complement near the hypersurfaces.

- **L0 (collar).** g0 extends to a smooth class two-dust solution on an open neighbourhood 𝒩 of Q1 × S³ together with a
  past collar. The extension is ingoing Vaidya on {u ≤ 0}, outgoing Vaidya on {v ≤ 0}, and Tangherlini of mass 3/2 on
  {u, v ≤ 0}. It is smooth across the hypersurfaces because on both sides near 𝒞_out the metric is the same ingoing
  Vaidya metric, and near 𝒞_in the same outgoing one (prop:two-dust-background (a)). About 1 page.

  For general ů (the chapter-81 version), use instead any smooth extension Ů_ext with ů's jets on the hypersurfaces.
  Its residual F̊ := 1_P 𝔄_χ(Ů_ext) is then smooth and is carried as a fixed forcing term, allowed by
  rem:class-kato-local.
- **L1 (wave-gauge data with dust).** On 𝒞_out ∪ 𝒞_in, take all metric components to be the double-null form of the data,
  transported to chapter 81's chart X = (τ, x) by the background's coordinate map.
  - Compute W̊ on each hypersurface by the scheme of [CP12, §3.1] in n+1 = 5, with κ := 2∂_v ln Ω on 𝒞_out (as in
    lem:loc-cone-equations), the analogue on 𝒞_in, and sources T_vv = q_in, T_vA = T_uv = 0 on 𝒞_out (symmetrically on
    𝒞_in). The scheme uses their (19), (22), (26), (29), (31)–(36); the matter terms enter only through T·ℓ, which is
    tangential.
  - prop:loc-cones and its 𝒞_in analogue are the constraints (19) and (26).
  - Then D̃ = 0 on both hypersurfaces, W̊ is continuous at S (CP12 (31)), smooth on each hypersurface, zero where the data
    are the background's (the background satisfies D(g0) = 0 relative to itself), and O(ε).
  - Extend W̊ to a G-invariant smooth field supported near the band region.
  - The dust fields on the hypersurfaces: on 𝒞_out, p_in has tangential part dv and transverse part the root of the null
    condition, as chapter 81 does on slices; Θ_in = □v uses the transverse derivative of p_in from (Aug2), which is
    algebraic because P_in is transverse. p_out = λ·(conormal of 𝒞_out), with λ fixed by (Aug2) along the generators
    with λ = 1 at S, and Θ_out, q_out solve their transports along the generators. Symmetrically on 𝒞_in.
  - Check: the normalisation κ makes λ ≡ 1, so that the solution's Ω on 𝒞_out is the data's. This must be verified
    (risk R2).
  - Chapter 81's (Aug1) with D̃ in place of D keeps its principal part, and prop:class-augmented (e) holds for D̃ with an
    unchanged proof.
  - About 4–6 pages; verify by computer algebra in the class chart.
- **L2 (jets).** On 𝒞_out, all ∂_u^j U, j ≥ 1, are determined by linear ODEs in v along the generators, with initial
  values at S from the 𝒞_in data:
  - the wave block: the restriction of the reduced equation, as in Rendall's lemma;
  - the out-family transports (tangent to 𝒞_out): differentiate j times in u;
  - the in-family transports (transverse): algebraic.

  The same holds on 𝒞_in with u ↔ v. The mixed jets at S agree, by induction on the order. The constraint quantities
  ν_A, dp_A, Δ_A and D̃ vanish to infinite order on both hypersurfaces: they vanish there by L1, and their transverse
  derivatives satisfy the homogeneous identities of prop:class-augmented (b), (d), (e) restricted to the hypersurfaces,
  which are ODEs with zero initial values. About 3–4 pages.
- **L3 (extension).** There is a smooth G-invariant Û on 𝒩 with the jets of L2 on both hypersurfaces. It equals Ů outside
  a neighbourhood of the band region of width ≤ η in ϑ, and ‖Û − Ů‖_(C^(k+2)) ≤ Cε.
  - Construction: Borel's lemma along each hypersurface (with tails small in C^(k+2)), a corner correction, and averaging
    over G (as in the definition of d_B in def:class-adapted).
  - A finite-order version with [See64] (thm:std-seeley) is also possible; then smoothness comes from persistence of
    regularity.
  - The residual 𝔄(Û) vanishes to infinite order on 𝒞_out ∪ 𝒞_in and is O(ε) in C^(k+1). About 2 pages.
- **L4 (the modified system).** Let χ(ϑ) be a G-invariant cut-off, equal to 1 on [ϑ_a − 2η, ϑ_b + 2η] and to 0 within η
  of the axes. Put 𝔄_χ(U) := χ 𝔄(U) + (1 − χ) A^0(Ů) ∂_τ(U − Ů).
  - It is quasilinear symmetric hyperbolic with smooth coefficients. A^0 is χA^0(U) + (1 − χ)A^0(Ů) > 0 and the A^j are
    χA^j(U).
  - It is local: ζ_A ≡ 1 on supp χ, and no planar shear enters. Ů solves it, and it is the augmented system on {χ = 1}.
  - Extend it to ℝ⁴ as in Step 9 (i)–(iii).
  - Rendall's forcing F̃ := 1_P 𝔄_χ(Û) is smooth, because a function flat on ∂F times the indicator of the complement of
    the quadrant F is smooth. It is supported in {χ = 1} ∩ P near the band region, with ‖F̃‖_(H^k) ≤ Cε. About 2 pages.
- **L5 (the Cauchy problem).** Solve 𝔄_χ(U) = F̃ with data Û on a slice Σ_init in the collar. By
  thm:class-kato-stability (a) and rem:class-kato-local, around ū = Ů and with R = −F̃, the solution exists on the whole
  time interval needed, with 𝒩_k(U − Ů) ≤ Cε. It is smooth by the persistence argument at the end of Step 9, and
  G-invariant by uniqueness (Step 9). About 1–2 pages.
- **L6 (past region).** U = Û on P. The difference Z := U − Û satisfies a linear symmetric hyperbolic system.
  - Use the energy identity of lem:class-transport and the energy lemma on regions bounded by Σ_init and slightly tilted
    spacelike hypersurfaces converging to the null boundary 𝒞_out ∪ 𝒞_in. The boundary terms have the good sign for
    the wave block (ν_0 ≥ 0, g⁻¹(ν, ν) ≤ 0, Step 9) and for future causal transports.
  - Hence U has Û's jets on the hypersurfaces. About 1–2 pages.
- **L7 (finite speed; the region).** supp(U − Ů) lies in the causal future of supp(Û − Ů) for a cone field Cε-wider than
  g0's. The proof is an energy estimate on lens domains with spacelike lateral faces, as in lem:loc-lens-dependence.
  - A future causal curve from K_out ∪ K_in into Q1 has |Δϑ| ≤ C_0 (ΔuΔv)^(1/2), by Cauchy–Schwarz in
    g0 = −2e^(2σ) du dv + R² dΩ₃².
  - So on G_*, U − Ů is supported in {χ = 1}, and the true augmented system holds there. Elsewhere U = Ů.
  - The general region is G := {p : J⁻(p) ∩ J⁺(K) ⊂ {η ≤ ϑ ≤ π/2 − η}} ⊇ G_*. About 2 pages.
- **L8 (constraints).** On G_* ∩ F:
  - ν_A ≡ 0 and dp_A ≡ 0, by prop:class-augmented (b) along P_A from the hypersurfaces. Hence p_A = du_A with u_A
    eikonal; F ∩ G_* is simply connected.
  - D̃ ≡ 0 and Δ_A ≡ 0. Both vanish to infinite order on the hypersurfaces (L2, L6). Extended by zero into P, they solve
    the homogeneous linear system eq:class-gauge-wave and eq:class-defect with zero Cauchy data on Σ_init, so they
    vanish by the Gronwall argument of Step 10.
  - So Ric(g) = T and the dust conservation law hold, and near the axes U = Ů. About 2 pages.
- **L9 (double-null gauge).**
  - (u, v) := (u_out, v_in) are double-null coordinates close to the background's: u_out equals the data's u on 𝒞_in and
    0 on 𝒞_out; v_in equals the data's v on 𝒞_out and 0 on 𝒞_in.
  - ϑ takes the data's values on 𝒞_in and is transported along the outgoing null generators.
  - G-invariance puts g in the form of eq:loc-double-null, and the induced data are the given ones (L1, with b = 0 on
    𝒞_in).

  About 2–3 pages.
- **L10 (uniqueness).** Take a second solution g′ on G′ ⊂ G_*, in the gauge, within ε2 of g0.
  - Extend it smoothly across the hypersurfaces (Seeley). Solve the semilinear wave-map system for a coordinate map with
    gauge source W̊ and characteristic data the identity, by the L3–L7 argument; this is semilinear with smooth
    coefficients.
  - In the new coordinates g′ solves 𝔄 with the same data, hence has Û's jets. Glued to Û on P, it solves 𝔄_χ = F̃ with
    the same data on Σ_init, so it equals U (uniqueness in thm:class-kato (a)).
  - Both are in the double-null gauge with the same data, so they coincide. About 2–3 pages.
- **L11 (optional): continuation to Ω₂ and Σ_τ0.** From a spacelike slice inside G, apply thm:class-stability, with the
  dust at the axes and adapted lateral boundaries. This would carry the cone-localised dust data to data on Σ_τ0, a new
  link with thm:loc-bent-slice and cor:class-two-dust. It needs a check of (H2′) for the chosen domain. About 2 pages,
  if wanted.

### 3.4 Estimates, regularity in and out

- **In.** C^∞ data, small in C^m on the two finite hypersurfaces. Each transverse order in Rendall's ODEs costs two
  tangential derivatives (the angular Laplacian in the restricted wave operator). With jets to order k + 2, a safe choice
  is m0(k) = 2k + 6, to be fixed when L2 is written. Densities: C^∞, ≥ 0, compact support allowed.
- **Out.** A smooth solution with 𝒩_k(U − Ů) ≤ Cε, k ≥ 6, as in chapter 81, and |g − g0|_(C^(k−3)) ≤ Cε on G_*.
- **The constants** are those of thm:class-kato-stability (a) for the background over a fixed time interval, plus C_0
  and η.
- **Not covered by Tier 1.** C³ or lower data, densities that are only L^∞ or BV, and measure-valued shells. These would
  need a [LR20]-type weak double-null theory in 4+1 (Tier 3).

### 3.5 Results to quote (new Appendix A entries)

Appendix A currently has no entry for [CCTW16], [LR20], [CP12] or Rendall; [CTG23] and [CBCM10] are present.

| Entry | Use | Status |
|---|---|---|
| [CP12, §3.1, pp. 6–10, (15), (16)–(36), with Theorem 2.1, p. 5] | L1: wave-map gauge data with the full metric prescribed and gauge source W̊, sources with tangential T·ℓ, n+1 dimensions | arXiv text read; the entry needs exact quotes of (19), (22), (26), (31)–(36) |
| [CBCM10, Theorem 5.1, p. 26] | L1/L2: S_αβ ℓ^β = L_α + C_α on a null hypersurface (gauge preservation), n+1 | read; already in the bibliography |
| [See64] and Borel's lemma | L3 | [See64] already quoted (thm:std-seeley); Borel's lemma proved in two lines |
| Rendall [Ren90] | attribution of the reduction; quote a lemma only if the paper is obtained | add to chapter 98: Proc. R. Soc. Lond. A 427 (1990) 221–239, doi:10.1098/rspa.1990.0009 |
| [LR20, Theorem 4.6, p. 29]; [Luk12, Theorem 2, p. 9] | comparison sentences in chapter 83 only (no proof uses them) | [LR20] in the bibliography; add [Luk12]: IMRN 2012, no. 20, 4625–4678, arXiv:1107.0898 |
| Tier 2: [CCTW16, (2.7)–(2.8) p. 7; Theorem 3.9 p. 32; Corollary 3.11 and Remark 3.12 p. 35; §§3.5–3.6] | strip solution of the reduced system | read |
| Vacuum section (§3.8): [CCTW16, Theorem 4.1 p. 40; Theorem 4.3 p. 48]; [CTG23, Theorem 1.1] (present) | eikonal functions and linear waves near the hypersurfaces | read |

Internal results used: thm:class-kato, thm:class-kato-stability (a), rem:class-kato-local, prop:class-structure,
prop:class-augmented, lem:class-transport, Steps 9–10 of thm:class-stability-off-axes, def:class-admissible,
lem:loc-cone-equations, prop:loc-cones, prop:two-dust-background, lem:two-dust-reparametrisation, lem:gauge-propagation
(03:116).

### 3.6 Tier 2: dropping smallness (Route CQ)

1. **The 2+1 reduction with dust.** With h := e^(2(A+B)) g3, ψ = A + B and ω = (B − A)/2, prop:reduction and
   Ric[g5] = T (R11 = R22 = 0 for adapted dust) give

       Ric[h] = T + (3/2) dψ² + 2 dω²,      □_h ψ = □_h ω = 0,

   with the dust conservation laws rewritten with weights e^ψ. In 2+1 the curvature is Ricci, which here is matter. So
   there are no Weyl or Bianchi unknowns: only two linear waves, the transports and the dust.
2. **The double-null frame formalism for h**, with one-dimensional sections. Unknowns: Ω̃, γ̃, b, the Ricci coefficients
   (χ, χ̲, η, η̲, ω̃, ω̲̃), the frame derivatives of (ψ, ω), and q_in, q_out. Each Ricci coefficient has a transport
   equation, along e_3 or e_4, with no angular derivative of the unknowns (Luk's ordering). The dust density enters only
   the Raychaudhuri equations.
3. **Go/no-go G1.** Verify item 2 by computer algebra (2–3 pages).
4. **Go/no-go G2.** The evolution subsystem is in the doubly-null form (2.7)–(2.8) of [CCTW16]:
   - fields transported by e_3 = Ω̃⁻¹(∂_u + b∂_ϑ) go in the ϕ block, those transported by e_4 in the ψ block;
   - the waves are written as in CCTW (4.47)–(4.50);
   - check the scalar product and that the connections preserve the splitting.
5. **Localisation.** Use a ϑ cut-off that keeps (2.8): A^u = χA^u_ϕϕ + (1 − χ)I, and likewise for A^v. Periodise in ϑ,
   so that Y is a circle. Apply [CCTW16, Theorem 3.9 and Corollary 3.11] with n = 2 and ℓ ≥ 6. Finite speed keeps the
   perturbation where χ = 1 on a set {uv ≤ δ²} whose δ depends on the size of the data.
6. **Identification with Einstein–null dust.** Either (i) propagate the dropped double-null equations as a homogeneous
   transport system (go/no-go G3); or (ii) follow the argument of [CCTW16, Theorem 5.3] (pp. 54–56). For (ii), a genuine
   local solution comes from the Tier-1 engine without smallness (Rendall trick plus thm:class-kato (a) for short times
   near any corner sphere and any slice). It agrees with the CCTW solution by uniqueness, and it is continued by local
   Cauchy and corner problems. Option (ii) needs no new constraint-propagation work.
7. **Back to 4+1** in the gauge of eq:loc-double-null. Uniqueness in the gauge comes from Theorem 3.9. For small data on
   larger regions use [CCTW16, §§3.5–3.6].

Route Q replaces items 5–6 by Luk-type a priori estimates in 2+1 (characteristic energies for ∂_ϑ^i ψ and ∂_ϑ^i ω,
transport estimates) plus the same engine and continuation argument.

### 3.7 What stays open (Tier 3)

- **Perturbations that reach the axes on the hypersurfaces.** These need a domain-of-dependence lemma for chapter 81's
  non-local augmented system with null faces near an axis (an analogue of lem:loc-lens-dependence), so that the Rendall
  trick can run with the axis machinery of thm:class-stability.

  Round perturbations of 𝒜 and ℬ within def:two-dust-data are already covered: they define a new two-dust background
  (prop:two-dust-background), around which Tier 1 applies.
- **Non-adapted families at the axes.** By rem:class-scope only one ingoing and one outgoing family are separated there.
- **Low regularity.** Measure-valued shells and C³ data.
- **General 4+1 without symmetry** (Routes C and L). That is a separate paper.

### 3.8 Chapter 87's continuation lemma

The record (87:1179–1194) names three facts behind (F1)–(F3): symmetry extension, double-null coordinates covering a
D_(s′), and uniqueness in the gauge. **Tier 1 does not provide them.** The 10 l5 problem:

- is vacuum and is not near any explicit background;
- needs the solution on regions D_s that contain the axes;
- needs uniqueness in the gauge on the whole of D_s.

In vacuum the axis difficulty is absent: the wave-gauge class system is a local quasilinear wave system, smooth through
the axes. So a separate **vacuum section** (about 300–500 lines) would close (F1)–(F3) **for smooth data**:

1. Geometric uniqueness on a neighbourhood of N₀ ∪ N₁. Existence is [CTG23]. On each development, build wave-map
   coordinates by solving the linear characteristic problem near the whole of the hypersurfaces ([CCTW16, Theorem 4.3]).
   Both metrics then solve the reduced equations with the same data ([CP12, Theorem 2.1] scheme; [CBCM10, Theorem 5.1]),
   and the difference satisfies a linear system with zero characteristic data, so it vanishes ([CCTW16, Theorem 4.3]
   uniqueness).
2. Symmetry extension by uniqueness, applied to each element of G.
3. Double-null coordinates on a strip along N₀ ([CCTW16, Theorem 4.1]), with angular coordinates transported.
4. Uniqueness in the gauge on all of D_s, and (F3), by a continuity argument in s, gluing the developments of the data on
   {v = s} ∩ D ∪ (N₁ ∩ {v ≥ s}).

This changes no result. The lemma is used by no proof. The data of def:tl5-problem are C³, not smooth (rem:tl5-beyond).
(H1)–(H3) are established for no region. So rem:tl5-beyond and 90:212–220 stand; only the sentence "So (F1)–(F3) are
hypotheses of the lemma" (87:1194–1195) could become "for smooth data (F1)–(F3) hold by …; for the data of
def:tl5-problem no version is stated". A finite-regularity version would need a Luk–Rodnianski-type double-null theory,
which is Tier 3.

Side observation, independent of this report's work: the shift constraint Ric_vx on N that chapter 87 leaves
untreated (87:447, 571) is the second line of eq:loc-cone (lem:loc-cone-equations). That line is a linear first-order
ODE for ∂_v of the shift along the generators. Chapter 87 could treat it by citing that lemma, after checking that 87's
variables (R, P, Q, W, β) correspond to 83's (Ω, γ_ϑ, b, A_c, A_s).

---

## 4. What changes in the edition

- **Chapter 83.**
  - Add the theorem of §3.2 (for example thm:loc-cone-development), with the 𝒞_in analogue of prop:loc-cones, after
    prop:loc-cones. Its proof is either a citation of the chapter-81 version or the lemmas of §3.3 written as a new
    section.
  - Replace 83:593–600. The vacuum case keeps [CTG23], with no smallness. For small band-localised data with dust (the
    shell, the packet, added densities) there is a development on G_*, unique in the gauge and localised. The loss
    sentence remains only for data that are not small, and for perturbations that reach the axes ("no development is
    asserted for … ; [LR20, Theorem 4.6] is the 3+1 analogue with measure-valued dust").
  - Extend 83:8–9: "…exist exactly ([[prop:loc-cones]]), and for small data they have a localised development
    ([[thm:…]])".
  - Add crosswalk rows for every new label.
- **Chapter 81** (if it hosts the general theorem). A new section "The characteristic problem off the axes" after
  sec:class-off-axes, and one sentence in rem:class-scope.
- **Chapter 80.** No change needed. Optionally, one sentence noting that small non-round band-localised perturbations of
  the background's characteristic data develop (the characteristic counterpart of cor:class-two-dust).
- **Chapter 82.** No change. The method extends to characteristic data for restricted Vlasov fields off the axes; a remark
  at most.
- **Chapter 87.** Unchanged under Tier 1. With the vacuum section of §3.8, the sentence at 87:1194–1195 and its echo in
  rem:tl5-beyond change as described there. The side observation on Ric_vx is optional.
- **Chapter 90.** After 90:200, one sentence: data localised in angle on the two null cones exist exactly, and develop for
  small perturbations, dust included, on a neighbourhood of the cones; developments of large dust-carrying data and of
  perturbations reaching the axes are not established.
- **Chapters 01 and 03.** Optionally one clause each (01:190–191; the "more families" bullet at 03:358–372).
- **Chapter 95.** The entries of §3.5.
- **Chapter 98.** Add [Ren90] (if cited) and [Luk12]. Add the volume "515" to [CCTW16]. Add [RSR18] only if Route Q or L
  is taken.
- **INTEGRATION.md and STATUS.md.** Update the "FOR THE FINAL REPORT" item of P-K83c to the new status.

---

## 5. Estimate and risks

**Size** (about 49.5 chapter lines per PDF page; chapter 81 is 1,671 lines):

- Tier 1: 1,100–1,600 lines (22–32 pages).
- Appendix A additions: 60–120 lines. Edits to chapters 83 and 90: 40–80 lines.
- Tier 2 (CQ, with option (ii)): a further 1,000–1,400 lines.
- Vacuum section for chapter 87: 300–500 lines.

Expect the usual cycle of a writer and two to four confirming readings. L1 and the 2+1 structure equations should be
checked privately by computer algebra.

**Order of work.** First the 𝒞_in analogue of prop:loc-cones. Then L1 (the first risk). Then L2–L3, L4–L8, L9–L10, and
the chapter-83 corollary and edits. The go/no-go checks G1–G2 for Tier 2 can run in parallel.

**Risks:**

- **R1 (moderate): jets for the first-order augmented system** (L2), including corner compatibility. Mitigation: derive
  them from the second-order wave equation and the transports, by Rendall's induction.
- **R2 (moderate): the wave-gauge data with dust** (L1). The formulas of [CP12, §3.1] must be re-derived in the class
  chart in 4+1, with the T terms. The κ normalisation must make the conormal factor λ ≡ 1, so that the solution's Ω on
  𝒞_out is the data's.
- **R3 (low): uniqueness on the past region** with a null boundary (L6). Mitigation: tilted spacelike faces and a limit.
- **R4 (low to moderate): finite speed and an explicit δ_*** (L7). Numbers in the chapter's style need bounds on e^σ/R
  over Q1 from sec:tab-bg.
- **R5 (low): the regularity count m0(k)** (§3.4).
- **R6 (moderate): uniqueness by conversion** (L10). If it proves heavy, state uniqueness for solutions constructed in
  wave gauge only, and say so.
- **R7 (structural): smallness and the band avoiding the axes are real restrictions.** The theorem must say so, and the
  loss sentence must stay for the remaining cases.
- **R8 (low): consistency with chapter 81.** Tier 1 uses the whole-space form (a) of thm:class-kato-stability after
  the extension of Step 9. The domain form (b), which "no result of this paper uses", is not needed.
- **R9 (Tier 2, moderate to high).** The fit to (2.8) (G2), the identification step (G3, or the engine argument), and the
  large-data finite-speed step for the cut-off system.
- **R10 (literature).**
  - Rendall 1990 was read only in abstract and through three sources that quote it. Do not quote its lemma numbers
    without the paper.
  - The Moschidis papers were read at the level of their statements.
  - [LR20], [CTG23] and Shen–Song–Wan are preprints.
  - No journal version of [CTG23] was found as of 2026-11-20.
