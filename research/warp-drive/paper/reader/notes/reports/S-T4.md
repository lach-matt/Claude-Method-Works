# S-T4: large data at the axes for the characteristic problem of five-dimensional Einstein–null dust

This is a scoping report for the writer. Nothing under `reader/` was edited, and `assemble.py` was not run. The scratch
work is in `scratchpad/st4/` (`jets.py`, `jets2.py`, `jets3.py`, `jets_out.txt`).

**Read for this report.**
- notes/reports/S-CIVP.md and S-T3.md, all of both.
- Chapter 81: 1–380, 540–1040 and 1038–1671 (thm:class-kato, thm:class-kato-stability, Steps 1–10 of
  thm:class-stability-off-axes, cor:class-short-time, the axes, lem:class-leaf-differences, def:class-adapted,
  thm:class-stability, rem:class-scope).
- Chapter 83: 334–600 (lem:loc-lens-dependence, sec:loc-cones, prop:loc-cones).
- Chapter 80: 195–260 (prop:two-dust-background).
- Chapter 02: 40–80 (prop:reduction, which is in chapter 02, not chapter 03).

**Not available.** GN-T3.md (the Tier 3 go/no-go report), proofs/P-CIVP.md and proofs/P-CIVP2.md do not exist yet
(checked 2026-11-20). This report therefore uses the names of S-CIVP (L0–L11, Tier 2 items) and S-T3 (T3-0 to T3-9,
Lemma A, Lemma R, GN1–GN3). Everything below assumes that S-T3's Route B survives GN1–GN3. If GN-T3 refutes Lemma A
or T3-2, this plan falls with it (§6, R4).

---

## Summary

- **What "large data at the axes" can mean.** Existence on the whole rectangle Q1 × S³ is false in general for large
  data. Large dust focuses: prop:loc-cones gives e^ϕ > 0 on the faces "for small perturbations" only (83:577–578),
  and the background's own existence set G of prop:two-dust-background (d) depends on the profiles. So the right
  large-data statements are those of [CTG23], [Luk12] and [LR20]: a development on a neighbourhood of both faces;
  the corner; a maximal development with a continuation criterion.
- **The obstruction is narrower than it looks.** Tier 3 uses smallness for three things:
  1. to stay, for the whole rectangle, in the ball about the background on which the non-local forcing is defined;
  2. because the leaf machinery, lem:class-leaf-differences, is stated on balls about a *solution*;
  3. for the uniformity of the leaf constants C_L, r_L and δ_*.

  The face-leaf fact (Lemma A), the extension trick (T3-2), the energy at the faces (T3-5, T3-6) and Lemma R do not
  use smallness. So **short time near a corner, for large data and with the axes, is reachable.** It needs one new
  lemma, the leaf machinery about a smooth state that is not a solution ("K-ax"), which looks routine.
- **New finding: the corner theorem gives a neighbourhood of both faces.** Cover each face by corner problems, glue
  them by uniqueness in the gauge, and let the width of the strip shrink as one moves along the generators. This
  continuation along the generators then gives existence on a neighbourhood of 𝒞_out^(v1) ∪ 𝒞_in^(u1), with the
  axes, for data of any size.
  - It needs no a priori estimate. It needs only three things:
    - (i) a corner time T that depends only on local C^M bounds and nondegeneracy constants;
    - (ii) transverse jets that stay bounded along the faces;
    - (iii) uniqueness without smallness.
  - Luk's counterexample [Luk12, §7.2] shows that (ii) is the essential hypothesis. A scratch computer-algebra check
    in the class double-null chart finds the first transverse jets on 𝒞_out to be a **triangular linear ODE system
    along the generators**, with no Riccati term (§4.4, GN4-3). That check is off the axes; at the axes regular
    variables are still to be written.
  - None of the sources read states this continuation argument. [Luk12, §6] and [CCTW16, proof of Thm 5.3] both sweep
    a strip of fixed width with a priori bounds. It is the main go/no-go (GN4-2, GN4-4).
- **Verdict: provable, at moderate risk.** The strongest theorem I expect to be provable is Theorem T4 (§4.1):
  - a corner theorem;
  - the neighbourhood theorem through the axes for data of any size, with the width bounded below non-explicitly by
    compactness (via Tier 3 around a general reference solution);
  - uniqueness in the gauge and a maximal development D_max containing every Tier 1–3 development;
  - a continuation criterion on double-null rectangles.

  Tier 2 then adds only its explicit strip off the axes.
- **What stays open.** An explicit width in terms of the data, which needs a priori estimates at the axes (a
  doubly-null formulation regular there; Routes C, D, L). Non-adapted families near the axes anywhere in the swept
  region. Finite regularity. 4+1 without symmetry.
- **Literature (§2).** No source treats null dust at a symmetry axis.
  - At axes, large-data local existence is known for vacuum and wave-type matter only. It comes from the unreduced
    theory plus invariance ([BCM95], [AGS17, Thm 1.6]) or from regularised reduced variables (Chruściel 1990 for S³
    Gowdy, known here through [Stå01]; [RS05] as a formulation only).
  - **One sentence needs care.** [HL17, p. 1] asserts large-data local existence for Einstein–null dust in wave
    coordinates without symmetry. Its footnote cites [CBF06] for massive dust. [CBF06, Thm 2.1] needs a timelike
    velocity: its characteristic set is "the union of the light cone and of a spacelike hyperplane exterior to it, if
    u is a timelike vector" (p. 6). For null dust that hyperplane touches the cone along p_A, the double
    characteristic of prop:class-augmented (f). So the claim is unproved for null dust in any source read, and the
    edition should not rely on it.
- **Size.** 610–1,030 chapter lines on top of Tier 3, written as modifications (12–21 PDF pages). Optional pieces add
  100–180 lines. There are five go/no-go checks.

---

## 1. The obstruction

### 1.1 What can be true for large data

- **The whole rectangle is out of reach in general.**
  - The cone data themselves can fail. prop:loc-cones solves the Raychaudhuri constraint "on every generator on which
    e^ϕ stays positive", and "for small perturbations e^ϕ stays positive on [0, v_1]" (83:576–578). A large shell
    perturbation can make e^ϕ vanish on a face: the face then reaches a focal point, and no double-null development
    with those faces exists beyond it.
  - Even round data exist only on G = {p ∈ 𝒟 : R ≥ a on J⁻(p)} (prop:two-dust-background (d), 80:241–242). G shrinks
    as the profiles grow, through trapped spheres (prop:two-dust-background (c)).
- **The targets** are therefore the standard large-data local statements:
  - (A) a development near the corner sphere (Rendall's scope);
  - (N) a development on a neighbourhood of both faces ([CTG23, Thm 1.1]; [Luk12, Thm 1]; [LR20, Thm 4.6]);
  - (M) a maximal development in the gauge, with a continuation criterion.
- **(A) alone does not serve chapter 83**, because its dust is far from the corner: the shell at 3 < v < 4.5 and the
  packet at 5.7 < u < 7.2 (S-CIVP §1.1). (N) is what parity with the vacuum sentence (83:593–600) needs.

### 1.2 Why Tier 1 does not reach the axes

- **The angular cut-off.** Tier 1's angular cut-off χ (L4) presupposes that the band, and its domain of influence on
  G_*, stay off the axes. Data reaching the axes are cut by it.
- **The engine.** Its engine, thm:class-kato-stability (a) with ρ = ∞, needs a local forcing (81:670–672;
  rem:class-kato-local). At an axis the closure S_A^ax is non-local and is defined only on a ball (Step 9 of
  thm:class-stability, 81:1533–1538).
- **What smallness buys in Tier 1** is only the explicit region G_* = {uv ≤ δ_*²}. Without smallness, Tier 1's engine
  gives a short-time corner result off the axes (S-CIVP §3.6 item 6 (ii)).

### 1.3 Why Tier 2 degenerates at the axes

- **The reduction is singular there.** prop:reduction (02:55–63) uses ψ = A + B and h = e^(2ψ) g3. Near axis 2,
  e^(2B) = a_⊥ ρ2² (prop:class-axis (a)), so:
  - B → −∞, and ψ, ω are logarithmically singular;
  - h degenerates like ρ2²;
  - □_h has coefficients singular like 1/ρ2 (S-T3 §1.2).
- **[CCTW16, Thm 3.9] needs Y compact without boundary.** Tier 2 periodises ϑ away from the axes (S-CIVP §3.6 item 5),
  and finite speed keeps the influence off the axes on {uv ≤ δ²}.
- **No doubly-null form that is regular at the axes is known.**
  - The vacuum S³ Gowdy precedent is instructive. Garfinkle's regular parametrisation gives "evolution equations
    [that] contain coefficients that are singular at the axes" [Stå01, p. 5]. Regular coefficients need an Ernst
    potential and Cartesian coordinates near the axis [Stå01, pp. 6–8, after Chruściel 1990].
  - Rinne–Stewart's regular variables make the characteristic speeds "behave like ∼ r" in (r², z²) [RS05, p. 13]:
    the system becomes degenerate at the axis.
  - None of this treats dust.

### 1.4 Exactly where Tier 3 uses smallness

Tier 3 runs Rendall's trick on ℝ⁴ for chapter 81's system with the axis closure S_A^ax, in the face-adapted slicing
τ = v − R (S-T3 §3–4). Smallness enters at six places.

| # | Where | What fails for large data |
|---|---|---|
| (a) | T3-4: thm:class-kato (a) on 𝒟_ρ about Ů, continued "while ‖U − Ů‖_(H^k) ≤ η_ρ ρ" over the whole rectangle (81:583–586, 1537–1538) | the solution leaves the ball about the background; the forcing (S_A^ax through σ_A) is defined only on that ball |
| (b) | lem:class-leaf-differences is stated for "ů a smooth class solution", on balls 𝔅, 𝔅′ about ů (81:1324–1334) | with large data the natural reference is the extension Û, which is not a solution; for long times there is no reference at all |
| (c) | Cauchy stability: thm:class-kato-stability needs ρ = ∞ (81:670) | with the non-local term only local existence holds, with T* depending on ‖u0‖, ρ and u_* (81:583–586) |
| (d) | leaf constants: C_L and r_L are "valid … for the leaves of ů and of the states near ů" (81:1373–1374); Step 6 needs 3 C_L δ_*² + C ε < r_B, and "the leaves of another family A′ can cross an adapted boundary B at distance O(ε)" (81:1507, 1524–1525) | for large data C_L, r_L and δ_* depend on the solution and are not uniform over long times; two families' leaves through one axis point separate like O(1)|y|², not O(ε)|y|² |
| (e) | L3: ‖Û − Ů‖_(C^(k+2)) ≤ Cε, and ‖F̃‖_(H^k) ≤ Cε in T3-4's a priori bound | Û is O(1) away from the background |
| (f) | cone data: e^ϕ > 0 on the faces only for small perturbations (83:577–578) | must become a hypothesis (no focal point on the faces) |

Two further facts.
- **The paper has no large-data result with dust at the axes, not even for the Cauchy problem.**
  cor:class-short-time, the one large-data result of chapter 81, assumes "densities vanishing within 2δ of the axes"
  (81:1026–1032). The reason is that its proof is Step 9 of the off-axis theorem (81:1034–1036): the axis machinery
  is written only perturbatively, around a solution.
- **Leaf separation is not the real obstruction at the faces.** Lemma A (S-T3 §1.6, T3-1) makes each face section a
  leaf of *both* families for every state carrying the formal 1-jets. That uses no smallness, so the O(ε)|y|²
  separation is never needed at a face. Separation matters only for boundaries that are not face sections: the
  adapted lateral boundaries of thm:class-stability, and the angular face of T3-8's localisation.

### 1.5 What does not depend on smallness

- **Lemma A** (T3-1): the face sections are leaves for any state with the formal 1-jets. This is Volterra uniqueness
  (lem:class-volterra), whose constants are bounds, not smallness.
- **T3-2** (non-local terms on sets closed under leaves). It is the extension Ŭ := U − 𝔼(U − V) plus
  lem:class-leaf-differences (b) on a ball about V. It is small only in U − V.
- **T3-3** (infinite-order vanishing of the non-local residual at the faces).
- **T3-5** (the boundary form at Û is ≥ 0 because the faces are null for Û). **T3-6** (energy on F, flux zero at the
  faces).
- **Lemma R** (the slicing t = u + v of a solution meets every double-null rectangle in common leaves). For two
  solutions of any size it can be run by a continuity argument in t (§4.3, T4-4).
- **lem:class-volterra and lem:class-planar-shear**, whose constants depend on C² norms of g, C¹ norms of u and sup |Θ|
  (81:1233–1236, 1283–1285).

So the obstruction reduces to two things: **long time**, and **the reference being a solution**. Long time is
unavoidable (§1.1). The second is removable (K-ax, §4.3).

### 1.6 The 4+1 picture at the axes

- **The metric is regular through the axes; the dust is not.**
  - In chapter 81's 4+1 wave gauge the metric equations and the transports are regular through the axes (S-T3 §1.3).
  - Without the class closure the dust loses one derivative (81:149–156). The cause is the double characteristic of
    prop:class-augmented (f): the transport symbol ξ(P_A) and the light cone meet along p_A (81:312–316).
- **Why [CBF06]'s device does not transfer.** For massive dust, [CBF06] applies u·∇ to the wave-gauge equations and
  obtains a Leray system of order 3 ([CBF06, (2.8) and Thm 2.1], pp. 5–6). Its characteristic set is the light cone
  together with "a spacelike hyperplane exterior to it, if u is a timelike vector" (p. 6). Strict hyperbolicity of
  that product is what gains the extra derivative.
  - Count derivatives: a strictly hyperbolic operator of order 3 gives g ∈ H^(σ+2) from a right side in H^(σ−1). The
    factorised estimate (transport, then wave) gives only g ∈ H^(σ+1), which is the loss.
  - For null u the hyperplane ξ(u) = 0 is tangent to the cone along u♭. The product then has a double root, and that
    extra derivative is exactly what is lost.
- **This is consistent with chapter 81, and it disposes of the plain 4+1 wave-gauge route** (§3, Route W1).

---

## 2. Literature, verified

Search route: alphaXiv full text (arXiv), plus the CCTW16 text already in scratch (`scratchpad/lit/`). Each source
was opened at the pages cited unless marked otherwise. Sources already verified in S-CIVP and S-T3 are re-used and
marked so.

| Source | Setting | At an axis? | Null dust? | Large data? | Covers our case? |
|---|---|---|---|---|---|
| [Luk12] | 3+1 vacuum, characteristic, double null | no (S²) | no | yes, strip of width ε(data) | no; template for the continuation (§6 last slice) and for the role of the jets (§7.2) |
| [CCTW16] | doubly-null symmetric hyperbolic; 4D Einstein | no (Y compact, no boundary) | no | yes | no; template for identification (proof of Thm 5.3) |
| [CTG23] | n+1 vacuum, characteristic | no | no | yes | no (S-CIVP) |
| [LR20] | 3+1, two null dusts, characteristic | no (S²) | yes, measure-valued | yes, u* ≤ ε | no (3+1; S-CIVP) |
| [BCM95] | 3+1, G₂ = ℝ × U(1), Cauchy | yes, unreduced plus invariance | no | yes | no (S-T3) |
| [AGS17] | 2+1 equivariant Einstein–wave map, Cauchy | yes | no | yes, global | no; technique only |
| [RS05] | 3+1 axisymmetric, (2+1)+1, GH gauge | yes, regular variables | perfect fluid | formulation | no |
| [HL17] | 3+1 polarised U(1), elliptic gauge, Cauchy | no (free translation) | yes | small in L^∞, large high norms | no |
| [Tou21] | 3+1 U(1), elliptic gauge, vacuum | no (free) | no | small in W^(1,4) | no |
| [CBF06] | n+1 Einstein–(charged) dust, wave gauge | no | massive only | yes | no; method fails for null u |
| Chruściel 1990 (via [Stå01]) | 3+1 Gowdy on S³, S² × S¹ | yes | no | global existence | no (vacuum); precedent for regularising at axes |

1. **[Luk12]** J. Luk, IMRN 2012, arXiv:1107.0898. Read pp. 1–4, 9–12, 23, 29, 38–43.
   - Abstract: Rendall gives a solution "in a small neighborhood of S"; Luk gives one "in a neighborhood in the future
     of the cones".
   - Theorem 1 (p. 2): the width ε "depends only on the size … of the initial data".
   - **§6 (pp. 38–39).** The last-slice argument sweeps the fixed region D = {0 ≤ u ≤ ε, 0 ≤ u̲ ≤ I} by t = u + u̲.
     It uses the a priori estimates of §5, and local existence near S_(0,t*) "as in section 3".
   - **§7.2 (p. 41), the counterexample.** "without a null condition, the theorem no longer holds. This is in contrast
     with Rendall's theorem, which holds for general quasilinear wave equations". The example is □_m φ = (∂_u φ)²,
     where the transverse derivative obeys a Riccati equation along the cone and blows up.
   - Use here: (a) the jets along the faces must be globally bounded, the hypothesis of the continuation of §4.3;
     (b) Rendall's theorem reproved in double null (§3), including the jet ODEs.
2. **[CCTW16]** Cabet–Chruściel–Tagne Wafo, Dissertationes Math. 515 (2016), arXiv:1406.3009. Re-read p. 5 and pp.
   53–56.
   - Rendall "proved existence of a solution in a neighborhood of the intersection" (p. 5). Cabet, Dossa and Luk
     obtained "the neighborhood theorem" under structure conditions (p. 5).
   - Proof of Thm 5.3 (pp. 55–56). It sweeps [0, a*] × [0, b0] by t = u + v with Rendall's Thm 5.1 and the mixed
     Cauchy problems of Figs. 5.3–5.4. The a priori control is the solution of their Thm 3.9: "Since (ϕ, ψ) extend
     smoothly to the boundary t = t*, so do (ϕ_E, ψ_E)".
   - So a sweep over a strip of fixed width needs a priori bounds. The continuation of §4.3 avoids this by letting
     the width shrink.
3. **[BCM95]** (verified in S-T3). The development comes from the unreduced theory "if the matter fields satisfy some
   well–behaved equations of hyperbolic type" (p. 4). Null dust fails that (§1.6).
4. **[AGS17]** Andersson–Gudapati–Szeftel, arXiv:1501.00616 v4. Read pp. 1–7, 13, 15–18, 38–40.
   - Thm 1.6 (p. 5): the maximal Cauchy development comes from Choquet-Bruhat–Geroch "together with the equivariance
     of the Cauchy data". There is no reduced local theory.
   - Parity and no-cone conditions (p. 4).
   - Double-null coordinates normalised on the axis by (2.1) (p. 7).
   - §3, "The first singularity occurs on the axis": for large data the axis is where the analysis concentrates.
   - Cauchy problem only; not characteristic; no dust.
5. **[RS05]** Rinne–Stewart, CQG 22 (2005) 1143, arXiv:gr-qc/0502037. Read pp. 1–3, 6, 8, 11–14, 18–21. S-T3 had
   read the abstract only.
   - A strongly hyperbolic first-order system, symmetric hyperbolic for f = 1 (p. 2), "manifestly regular on axis"
     after a change of variables (§VIII, pp. 11–12).
   - In (r², z²) "the characteristic speeds behave like ∼ r" (p. 13).
   - The matter is vacuum and a perfect fluid (Appendix D). The IBVP is called "well-posed" (p. 11) with no theorem.
   - A numerical formulation. No existence theorem, no characteristic data, no null dust.
6. **[HL17]** Huneau–Luk, *Einstein equations under polarized U(1) symmetry in an elliptic gauge*, arXiv:1706.09499.
   Read pp. 1–9 and the references. S-T3 had read the abstract only.
   - Theorem 5.4 (p. 6): local well-posedness for Einstein–null dust (finitely many families) under the smallness
     (5.5) "‖φ̇‖_(L^∞) + ‖∇φ‖_(L^∞) + max_A ‖F̆_A‖_(L^∞) ≤ ε", with large high norms.
   - The U(1) is the translation ∂_(x³) on I × ℝ³ (p. 4): there is no axis.
   - **p. 1 states** "a local, geometrically unique (large data) solution to the Einstein–null dust system exists in a
     wave coordinate gauge, even without the polarized U(1) symmetry assumption [3]". Its footnote 1 adds
     "[3] deals with the case where the dust is massive, the methods apply to the null case with little
     modifications, cf. [2]". Here [3] is [CBF06] and [2] is Choquet-Bruhat's 2009 monograph.
   - Item 7 and §1.6 show why [CBF06]'s method does not apply as written. The monograph was not read, so the claim
     stays **unverified for null dust**. If the monograph proves it in C^∞, Route W1 (§3) opens; that is GN4-5 (ii).
7. **[CBF06]** Choquet-Bruhat–Friedrich, *Motion of isolated bodies*, CQG 23 (2006) 5941, arXiv:gr-qc/0605096. Read
   pp. 1–13.
   - Thm 2.1 (p. 5): Einstein–dust in wave gauge is "a hyperbolic Leray system for g, u and r, which is causal as long
     as g is Lorentzian and u is timelike", with Leray–Volevič indices ℓ(g) = 3, ℓ(u) = 2, ℓ(r) = 1 and the
     u-derivative (2.8) of the reduced equations.
   - The characteristic set is "the union of the light cone and of a spacelike hyperplane exterior to it, if u is a
     timelike vector" (p. 6).
   - Massive dust only. For null u this is the double characteristic of prop:class-augmented (f).
8. **[Tou21]** Touati, arXiv:2101.09093. Read pp. 1–9, 43–47. Vacuum U(1) (translation) on I × ℝ², elliptic gauge,
   smallness in W^(1,4), large H³. No axis and no dust; listed because it is the large-high-norm U(1) local theory.
9. **Chruściel 1990** (*On space-times with U(1) × U(1) symmetric compact Cauchy surfaces*, Ann. Phys. 202). **Not
   read** (paywalled). [Stå01] (Ståhl, arXiv:gr-qc/0109011, read pp. 1–8, 14–15, 21–23) cites it for three things:
   - "The global existence theorem for Gowdy spacetimes over S² × S¹ and S³ [10]" (p. 15);
   - the axis smoothness criterion "Lemma 5.1 of [10]" (p. 6);
   - the Ernst-potential reparametrisation that gives coefficients regular at the axis (p. 7).

   Ståhl also states that local solutions near and away from the axis are patched by domain of dependence (p. 4).
   This is vacuum, where domain of dependence is local; with null dust at an axis it is not (S-T3 §1.5). Cite it for
   nothing beyond what [Stå01] attributes to it.
10. **Shatah–Tahvildar-Zadeh** (CPAM 1992, 1994): equivariant wave maps. Not read; known here only through
    [AGS17, pp. 2–3].
11. **Rendall 1990**: not read (S-CIVP). [Luk12, §3] reproduces its double-null version and states it as Theorem 3,
    "for general quasilinear wave equations", with "a small neighborhood of S_(0,0)". The dependence of that
    neighbourhood on the data is not stated there; §4.3 needs it and proves it in-house.

**Conclusions.**
- **At axes**, large-data local existence in reduced Einstein problems is known only for vacuum or matter of wave
  type. It comes either from the unreduced theory plus invariance (BCM, AGS), or from reduced variables made regular
  at the axis (Chruściel 1990 through Ståhl; RS05 as a formulation).
- **With null dust**: nothing at an axis, Cauchy or characteristic. The one large-data claim without symmetry
  ([HL17, p. 1]) rests on a massive-dust method that needs a timelike velocity.
- **Characteristic neighbourhood theorems** ([Luk12], [CCTW16], [CTG23], [LR20]) are all quantitative, through a
  priori estimates on a strip of fixed width. None, as checked, states the qualitative neighbourhood theorem by
  continuation along the generators. [Luk12, §7.2] marks its hypothesis.

---

## 3. Routes

| Route | Idea | At the axes | Delivers | Length over Tier 3 | Risk | Verdict |
|---|---|---|---|---|---|---|
| **S** | Tier 3 with reference path u_* := Û and short time; K-ax | Lemma A plus K-ax | corner theorem (A), any size | 300–500 | low to moderate | needed; useless alone for ch. 83 |
| **N** | S plus continuation along the generators (corner problems on the faces and on null hypersurfaces of the solution, glued by uniqueness) | as S | neighbourhood theorem (N) and (M), any size | +310–530 | moderate (GN4-2, GN4-4) | **recommended** |
| N′ | N plus compactness plus Tier 3 around a general reference ů | as S | width bounded below by C^M bounds (not explicit) | +60–100 | moderate | optional |
| P | Tier 3 around a general smooth reference ů | as Tier 3 | small non-round perturbations of any known large solution, e.g. every round two-dust background on its G | +40–60 | low | cheap corollary |
| K (user's "continuation on the whole rectangle") | t-sweep of Q1 combining Tier 2 off the axes with a local axis theory | needs bounds at the axes | — | — | fails as stated | no |
| W1 (user's "4+1 near the axes", plain wave gauge) | unreduced 4+1 wave gauge, invariance by uniqueness | regular metric, lossy dust | — | — | the double characteristic | no |
| W2 | 4+1 wave gauge with chapter 81's closure | planar shear | = S / N | — | — | this is S / N |
| W3 | 4+1 double null, dust phases as coordinates, [CTG23] frame plus [LR20] renormalisation | frames cannot be T²-invariant at an axis | explicit width, low regularity | 1,500–3,000+ | high | separate paper |
| D | near each axis, quotient by the free circle: 3+1 Einstein–scalar–null dust, axisymmetric, [LR20]/[CCTW16]-type, glued | interior in 3+1 | explicit width | 3,000+ | high | not recommended (S-T3) |
| G | W1 in Gevrey classes (Leray–Ohya, double characteristic of multiplicity 2) | none | Gevrey data only | unknown | high, unread theory | not for the edition |
| E | Tier 2 (large off the axes) plus Tier 3 (small near them) | — | — | — | — | superseded by N |

**S (short time near the corner).**
- **What changes from Tier 3.**
  - The reference path is the extension Û (L3 without smallness), not Ů.
  - The modified system is 𝔄_ξ(U) := ξ 𝔄(U) + (1 − ξ) A^0(Û) ∂_τ(U − Û). Its forcing is F̃ := 1_P 𝔄_ξ(Û) (smooth by
    T3-3).
  - thm:class-kato (a) is applied with u_* := Û and data Û(τ_init) = u_*(τ_init). T* depends only on ‖Û‖, ρ and the
    path (81:583–586).
  - Σ_init = {t = t_c − δ} lies in P (every slice before the corner time does). Take δ < T*/2.
- **The slicing.** For large data the slicing is not v − R of the background. Take t := u + v built from the data's
  double-null coordinates on the faces and extended. It is spacelike for Û near the corner, and it meets the faces in
  the data's double-null spheres, which is all Lemma A needs.
- **The rest is unchanged.** T3-5, T3-6, T3-7 and Lemma R run with V := Û, or with the solution, on balls given by
  K-ax. The bootstrap of T3-4 is not needed: short time replaces smallness.
- **Gain and cost.** The gain is (A), the corner, through the axes, for any size. The new ingredient is K-ax. S-T3
  §5.1 (a) estimated this route at 1–2 pages and found it routine-looking; I agree, and §4.3 lists exactly what
  changes.

**N (the continuation along the generators).** The argument is in §4.3 (T4-5). In outline:
- Let V be the supremum of the v' for which the maximal development D_max contains a relative neighbourhood of
  𝒞_out ∩ {v ≤ v'}. Suppose V < v1.
- For η > 0 the ingoing null hypersurface N_η = {v = V − η} of the existing solution exists for 0 ≤ u ≤ w(η), with
  w(η) > 0 though possibly → 0 as η → 0.
- The data it induces near u = 0 are C^M-close to the formal jets at S_η, which are bounded uniformly in η (T4-3).
- So the corner theorem at S_η, with data on 𝒞_out ∩ {v ≥ V − η} and N_η ∩ {u ≤ u′(η)}, has a time T independent
  of η (T4-2). With η := T/4 it extends D_max past V. This is a contradiction.
- Then the same along 𝒞_in. By compactness, D_max ⊃ ([0, u*] × [0, v1] ∪ [0, u1] × [0, v*]) × S³.
- **No a priori estimate is used.** The strip width can shrink at each step; it stays positive, and compactness does
  the rest. This is why N is not refuted by the need for estimates in [Luk12, §6] and [CCTW16, Thm 5.3]: they sweep
  a strip of *fixed* width.
- **Luk's counterexample is consistent with it.** There the jets blow up on the face, so T_η → 0.
- **N also makes Tier 2 unnecessary for existence.** The same argument with Tier 1's engine without smallness (off the
  axes, local forcing) gives the off-axis neighbourhood theorem. Tier 2 keeps its explicit dependence of a* on the
  data.

**K (the user's whole-rectangle continuation).**
- A sweep of Q1 by t = u + v, using Tier 2's solution off the axes and local axis problems near them, needs at every
  t* a bound on the solution near the axes. That is the role Thm 3.9's solution plays in [CCTW16, proof of Thm 5.3].
- No such bound exists at the axes: Tier 2's estimates stop there, and chapter 81's axis machinery is perturbative.
- What survives is N, which sweeps along the faces instead and uses neither Tier 2 nor any bound.

**W (the 4+1 picture).**
- **W1, the plain wave gauge, is lossy.** The obstacle is the double characteristic (§1.6). [HL17, footnote 1] is the
  only claim otherwise, and its source ([CBF06]) needs a timelike velocity. W1 would become available only if
  GN4-5 (ii) finds a C^∞ proof for null dust in [Choquet-Bruhat 2009]. Then it would give large-data local Cauchy
  existence through the axes with no planar shear, and invariance by uniqueness. Even then the characteristic
  problem would still need the Rendall step and the continuation of N.
- **G, the Gevrey version, is not for the edition.** Leray–Ohya theory for nonstrict hyperbolicity is plausibly
  applicable in Gevrey classes G^s with 1 < s < 2 (multiplicity 2). It is not read; it is outside the edition's C^∞
  framework; and the chapter 83 profiles would have to be chosen Gevrey.
- **W2 is S/N.** The eikonal/phase formulation of chapter 81 (p_A, Θ_A as unknowns, (Aug1)–(Aug4)) *is* the 4+1
  hyperbolic formulation with the dust, and its axis closure is the planar shear.
- **W3, 4+1 double null, avoids the dust loss but is a separate paper.**
  - With the two adapted phases as coordinates, q_in and q_out are transported along coordinate directions. The
    expansions are Ricci coefficients, closed by the null structure and Bianchi equations ([CTG23] frame; [LR20]
    renormalisation of the dust terms with angular derivatives in the Bianchi equations).
  - With symmetry the analysis does not simplify at the axes. At an axis point the isotropy circle rotates the normal
    plane, so an invariant vector there is tangent to the axis circle. Hence no T²-invariant frame of the sections
    exists near an axis, and the frame formalism has to be run in full 4+1 with a non-invariant frame, invariance
    following by uniqueness.
  - This is S-CIVP's Route C. It is the route to an explicit width and to low regularity.

---

## 4. Verdict and plan

### 4.1 Verdict and the theorem

**Verdict.** Large data reaching the axes can be proved in the sense of [CTG23, Thm 1.1]: a development on a
neighbourhood of both faces, unique in the gauge, plus the corner, a maximal development and a continuation
criterion. The cost is 610–1,030 lines on top of Tier 3, at moderate risk. An explicit width in terms of the data,
and existence on the whole rectangle (false in general, §1.1), cannot be reached with the paper's tools.

**Theorem T4 (draft).** Setting as in Tier 3 (S-T3 §4.1): the class G = O(2) × O(2), the gauge of eq:loc-double-null,
faces 𝒞_out^(v1) = {u = 0, 0 ≤ v ≤ v1} and 𝒞_in^(u1) = {v = 0, 0 ≤ u ≤ u1}, corner S. Assume:
- **(H1) Class data of any size.**
  - On 𝒞_out: the free data (ℓ_1, ℓ_2, ℓ_3), Ω and q_in ≥ 0.
  - On 𝒞_in: the analogous conformal data, the gauge data (Ω, b) and q_out ≥ 0.
  - Corner data on S.
  - All smooth on S³ in the axis-regular sense of T3-0.
- **(H2) Nondegeneracy.** The constraint ODEs of prop:loc-cones and of its 𝒞_in analogue have solutions on the whole
  faces with ỹ = e^ϕ/e^(ϕ0) > 0 on every generator, axis generators included (no focal point on the faces). The
  corner sphere is spacelike, with the two faces its null normal hypersurfaces.
- **(H3) Families.** The two adapted families only. Further families are allowed if their densities vanish on a
  neighbourhood of the axes in the region concerned. This is stronger than Tier 3's condition at face-axis points
  (§5).

Fix M ≥ M0(k), k ≥ 6. Let K bound the C^M norms of the data on the faces, and let κ be the nondegeneracy constants:
lower bounds for Ω, ỹ and a_⊥ and for the axis derivative of the phases, and upper bounds for their inverses. Then:

- **(a) Corner.** There is T = T(K, κ) > 0 and a smooth class solution of eq:class-system on
  {(u, v) ∈ Q1 : u + v ≤ T} × S³, in the gauge of eq:loc-double-null with the axis conditions, inducing the data.
- **(b) Neighbourhood of the faces.** There are u*, v* > 0 and a smooth class solution on
  ([0, u*] × [0, v1] ∪ [0, u1] × [0, v*]) × S³ inducing the data. Optionally (N′), u* ≥ u*(K, κ) and
  v* ≥ v*(K, κ) > 0, with no explicit form.
- **(c) Uniqueness and the maximal development.** Two smooth class developments in the gauge on past subsets of Q1
  agree on their common domain. So there is a largest one, D_max, a relatively open past subset of Q1 × S³. It
  contains the developments of (a) and (b), of Tier 1 (G_*), of Tier 2 (its strip off the axes) and of Tier 3 (the
  whole Q1, for small data).
- **(d) Continuation criterion.** For a rectangle R_(a,b) := [0, a] × [0, b] × S³ ⊂ Q1: if D_max ⊃ R_(a,b) ∖ {(a, b)}
  and the C^M norms of the solution and its nondegeneracy constants are bounded on D_max ∩ R_(a,b), then
  D_max ⊃ R_(a,b) and more.
- **(e) Localisation.** g = g0 on every sub-rectangle on whose two faces the data are the background's (Lemma R
  without smallness).

**How it glues with Tier 2.** Tier 2's solution is in the same gauge (S-CIVP §3.6 item 7). By (c) it is the
restriction of D_max to Tier 2's strip off the axes. Tier 2 adds the explicit dependence of its width a* on the data
there, which T4 does not give at the axes. With (b) and N′ the two widths are both bounded below in terms of norms;
only Tier 2's is constructive, through [CCTW16, Thm 3.9].

**Corollary for chapter 83.** Every dust-carrying cone data set of prop:loc-cones and its 𝒞_in analogue satisfying
(H2) has a development on a neighbourhood of both cones, axes included, unique in the gauge. This covers every
perturbation of the shell or the packet, and every added density, of any size; for large ones (H2) is a hypothesis.
This is exact parity with the vacuum sentence that uses [CTG23] (83:593–597).

**Corollary P (cheap, from Tier 3 written around a general ů).** Take any round two-dust background of
prop:two-dust-background, of any admissible size, on any Q1 inside its G. Small non-round perturbations of its
characteristic data, axes included, develop on the whole Q1. This is "large data at the axes" in the sense of being
far from Tangherlini, on the whole rectangle.

### 4.2 Why the continuation along the generators is sound

- **Bounded jets.** The jets (all transverse derivatives) of the formal solution exist and are bounded on the compact
  faces whenever they solve linear ODE hierarchies along the generators. GN4-3 checks this; §4.4 has the first-order
  result.
- **Local data near the corner.** The data the solution induces on N_η near u = 0 converge to those jets as the length
  of the piece shrinks. This is continuity of a smooth solution up to the face, at fixed η. So their C^M norms on a
  short piece are at most 2K′, with K′ the jet bound.
- **Short pieces are allowed.** The corner theorem accepts a short piece [0, u′] of the ingoing face. Extend the free
  data beyond u′ by a Taylor polynomial (C^M-controlled), and solve the constraint ODEs on N_η for a uniform length
  (ỹ stays positive for a time depending on bounds). The development on {u ≤ u′} does not depend on the extension,
  by Lemma R.
- **T is uniform.** T depends on the data only through Û near S_η. Û is built from jets on both faces near S_η: on
  𝒞_out from the data, on N_η from the solution. Kato's T* depends only on ‖Û‖, ρ and the path. The leaf constants
  of K-ax depend only on C² bounds and κ. **Nothing depends on η, on the lengths of the faces, or on the background.**
- **Gluing.** The developments are glued by uniqueness in the gauge (T4-4).

The literature does not contain this argument in this form (§2). It must be written and confirmed (GN4-2, GN4-4).

### 4.3 Lemmas and outline proofs

The line counts are chapter lines, written as "the proof of [Tier 3] holds with the following changes", the way
thm:class-stability is written on top of thm:class-stability-off-axes.

- **T4-1 (K-ax: the planar shear about a smooth reference that is not a solution). 80–140 lines.**
  - *Statement.* lem:class-leaf-differences (a), (b) hold with "ů a smooth class solution" replaced by "V a smooth
    G-invariant state (g, p_A, Θ_A, q_A)". Here g is Lorentzian, P_A is future causal and transverse to the slices,
    and |∂_z (spatial p_A)| ≥ c > 0 on the axis.
  - *Where V's leaves come from.* They are the Volterra leaves of eq:class-leaf-volterra with H_L[Θ_A(V)]
    (lem:class-volterra). They foliate a disc of radius r_V depending on C² bounds and c, because ∂_(z0)h = 1 on the
    axis.
  - *The constants* depend on C^(k+2) bounds of V, on c and on r_V.
  - *Proof: what changes.*
    1. Smoothness of V's leaves comes from lem:class-interior-regularity at every order applied to the leaf equation
       with smooth H_L. It no longer comes from "level sets of ů_A".
    2. Derivatives across the leaves are taken in the axis-point parameter z0, not in c = u. The Jacobian 1/∂_z u
       becomes 1/∂_(z0) h.
    3. The shift of the foliation enters as (∂_(z0) σ[V]) δz0.
    4. The rest of (a) and (b) is unchanged.
  - *Byproduct, optional, 40–80 lines in chapter 81.* cor:class-short-time without "densities vanishing within 2δ of
    the axes": Step 9 of thm:class-stability, with the datum (constant in τ) as u_* and K-ax, plus Step 10 on a short
    interval. This is the first large-data result of the paper with dust at the axes.
- **T4-2 (the corner theorem). 150–250 lines; replaces T3-4 and generalises L1–L3.**
  - Faces: an outgoing null hypersurface and an ingoing one through a spacelike sphere, with general gauge data (Ω on
    both, b on the ingoing face). This is needed for the corners S_η of T4-5, where b ≠ 0.
  - The slicing t := u + v of the data, extended; the reference Û; the system 𝔄_ξ about Û; thm:class-kato (a) with
    u_* := Û.
  - Then T3-5 (U = Û on P, with V = Û in T3-2 by K-ax), T3-6 (constraints in F), T3-7 (double null) and T3-8's
    Lemma R.
  - **The output to state:** T depends only on C^M bounds of the face data within distance T0 of the corner and on κ.
    Also: a short ingoing piece is allowed (the extension argument of §4.2).
  - Corner-time uniformity (S-T3's GN2) at large data.
- **T4-3 (the jets along the faces through the axes). 100–160 lines; extends T3-0 and L2.**
  - All transverse jets of (Ω, γ_ϑ, b, A_c, A_s, q_in, q_out) on 𝒞_out solve a linear hierarchy along the generators,
    triangular in the unknowns, with coefficients smooth on the compact face in axis-regular variables. Likewise on
    𝒞_in.
  - Hence they are bounded on the faces by constants depending on K and κ.
  - First order is checked off the axes in §4.4. The dust jets are algebraic (q_in, transverse) or linear ODEs (q_out,
    tangent).
  - The wave-gauge jets needed by T4-2 are local to each corner (length ≤ T0), so nothing global in wave gauge is
    needed.
- **T4-4 (uniqueness without smallness; D_max). 80–130 lines; replaces the smallness in L10 and T3-8.**
  - Lemma R for two solutions of any size: a continuity argument in t := u + v of the first solution. Where they agree
    up to t1, the second lies in the K-ax ball about the first for t ∈ [t1, t1 + θ] (smoothness), and the energy of
    T3-8 gives agreement there.
  - The conversion of a solution in double null to wave gauge (L10) is a semilinear coordinate problem. It is solved
    near the faces by the same corner-plus-continuation argument (linear jets).
  - D_max is the union of all developments on past sets (each a union of rectangles R_(a,b)), well defined by
    Lemma R.
- **T4-5 (continuation along the generators; the neighbourhood theorem). 80–130 lines.** The argument of §3 (N) and
  §4.2, along 𝒞_out and then 𝒞_in, ending with compactness (a relatively open set containing a compact face contains
  a strip of uniform width).
- **T4-6 (continuation criterion). 50–90 lines.**
  - At a point p = (a, b) with D_max ⊃ R_(a,b) ∖ {p} and bounded norms, apply T4-2 at the corner
    S_(a − η, b − η). The data are on the two null pieces through it inside D_max, of length η plus the small θ(η)
    that relative openness gives. With η = T/4, p becomes interior.
  - A sweep in t over R_(a,b) and compactness give (d).
  - No spacelike lens near an interior axis point is needed. (Such a lens is not closed under the leaves of both
    families. Double-null rectangles in the solution's own slicing are, which is Lemma R.)
- **T4-6′ (optional: the width bounded below). 60–100 lines.**
  - Suppose data D_n with C^M ≤ K and nondegeneracy ≥ κ had widths u*_n → 0. Pass to a limit D_∞ in C^(M−1)
    (Arzelà–Ascoli), with width w_∞ > 0 by (b).
  - Tier 3 around the general reference ů := the development of D_∞ on [0, w_∞/2] × [0, v1] gives developments on
    that strip for every datum C^(M−1)-close to D_∞. This contradicts u*_n → 0.
  - It needs Tier 3 for references of finite regularity C^N, N = N(k), with constants uniform for C^(M−1)-close data.
- **T4-7 (statement, chapter-83 corollary, Corollary P, remarks). 70–120 lines.**
  - A remark names what is not covered (§5).
  - A remark on [HL17, p. 1] versus the derivative loss (§1.6, §2 item 6), so that a reader does not take that
    sentence as covering the case.

### 4.4 Go/no-go checks

- **GN-T3 (prerequisite).** S-T3's GN1–GN3 (Lemma A in the actual chart; the extension in T3-2 uniformly in τ;
  smoothness of F̃) must pass. In GN1 the chart time should be the data's t = u + v, as T4 needs, not only τ = v − R.
- **GN4-1 (K-ax).** Rewrite the proof of lem:class-leaf-differences for a non-solution V, line by line (the four
  points of T4-1). Optionally repeat rem:class-leaf-numerics for a large non-solution state: Volterra leaves,
  foliation radius, the Lipschitz quotient of (b).
- **GN4-2 (uniform corner time).**
  - Trace every constant of T3-3 to T3-6 and of thm:class-kato (a) with u_* = Û to C^M bounds of the face data near
    the corner and to κ. Check explicitly that no constant depends on the background, on the lengths of the faces, or
    on smallness.
  - Include S-T3's GN2: one component at a time near the corner time, where the two face sections approach each
    other.
- **GN4-3 (linear face jets through the axes).** Status:
  - *First order, off the axes, done in scratch* (`st4/jets*.py`, `jets_out.txt`). In the metric of
    eq:loc-double-null, restricted to u = 0, the five source-free evolution equations Ric_uv, Ric_uϑ, Ric_ϑϑ,
    Ric_φ1φ1 and Ric_φ2φ2 contain no second transverse jet and are of degree ≤ 1 in the first jets.
  - The ∂_v-principal matrix has rank 5, with determinant −γ_ϑ e^(2A_c + 2A_s)/(4Ω⁹).
  - The system is triangular: (∂_u γ_ϑ, ∂_u A_c, ∂_u A_s) solve a closed 3 × 3 linear ODE along each generator; then
    ∂_u Ω (from Ric_uv); then ∂_u b (from Ric_uϑ, which holds ∂_ϑ of jets already known).
  - The constraints Ric_vv and Ric_vϑ hold no transverse jet, which matches lem:loc-cone-equations. Ric_uu (the
    transverse Raychaudhuri equation, not used on 𝒞_out) is quadratic in the first jets, as expected.
  - The adapted dusts do not enter the evolution equations (T_uv = T_uϑ = T_ϑϑ = T_φφ = 0).
  - *Open.* At the axes the determinant vanishes like e^(2A_s) ∝ sin² ϑ. So the hierarchy must be rewritten in the
    axis-regular variables of T3-0 (A_s = log sin ϑ + even smooth part, b odd, the conical condition), and its
    regularity checked. Higher orders follow by induction (the top jet enters linearly), to be confirmed in the same
    chart.
- **GN4-4 (the continuation argument).**
  - Write T4-5 in full.
  - Confirm that T4-2 accepts a general ingoing face (b ≠ 0, Ω not normalised, any corner data) and a short ingoing
    piece.
  - Confirm that Lemma R without smallness glues the pieces.
  - A cheap independent test: run the argument first for a semilinear model whose jet ODEs are linear on both faces,
    e.g. □φ = ∂_u φ ∂_v φ in flat space. On {u = 0} the jet w = ∂_u φ obeys −4∂_v w + Δφ = w ∂_v φ, and on {v = 0}
    the jet z = ∂_v φ obeys −4∂_u z + Δφ = z ∂_u φ. Then check it against Luk's counterexample □φ = (∂_u φ)², where it
    must fail.
- **GN4-5 (literature).**
  - (i) Obtain Rendall 1990 to see whether the dependence of the corner region on the data is stated.
  - (ii) Read [Choquet-Bruhat 2009] for the null-dust claim of [HL17, footnote 1]. If it is proved in C^∞, Route W1
    could shorten T4-1 and T4-2 for the Cauchy part.
  - (iii) Obtain Chruściel 1990 before citing anything from it.

**Order of work.**
1. GN-T3.
2. GN4-1 with T4-1.
3. GN4-3 at the axes (computer algebra in T3-0's variables), in parallel.
4. T4-2 and GN4-2.
5. T4-4.
6. T4-5 and GN4-4.
7. T4-6.
8. Statement and corollaries. N′ last.

### 4.5 Advice to the Tier 1 and Tier 3 writers

No edit was made. These keep T4 citable.
1. State L1–L3 for general gauge data on both faces (Ω on both, b on the ingoing face) and any corner data.
2. In T3-1, state Lemma A for any time function whose level sets meet the faces in the data's double-null spheres, not
   only for τ = v − R.
3. In T3-8, prove Lemma R by a continuity argument in t that does not use the size of either solution.
4. Write T3-0 so that it covers the transverse jets, not only the constraints.
5. Keep track of which constants of T3-3 to T3-6 depend on the size of Û.

### 4.6 Placement and edits

- **Chapter 81.**
  - A section "The characteristic problem for large data" after Tier 3's: T4-1 to T4-6 for a general smooth class
    two-family problem.
  - Optionally the axis version of cor:class-short-time.
  - One sentence in rem:class-scope.
- **Chapter 83.** The corollary. The loss sentence (83:597–600) shrinks to three items:
  - explicit dependence of the neighbourhood on the data, and developments beyond a neighbourhood of the cones, which
    for large data need not exist;
  - families other than the two adapted ones near the axes;
  - finite regularity, with [LR20, Thm 4.6] named as the 3+1 analogue for measures.
- **Chapter 90.** Data on the two null cones develop on a neighbourhood of the cones for any size, dust and axes
  included; small perturbations develop on the whole rectangle.
- **Chapter 95.** No new outside result is used in a proof step. [Luk12] (§6 and §7.2) and [CBF06] are cited in
  remarks only. [Luk12] is already proposed in S-CIVP §3.5; [CBF06] is new to chapter 98 if the remark of T4-7 is
  kept.

---

## 5. What stays open

- **An explicit width; a quantitative large-data theory at the axes.** T4 gives the width only non-constructively
  (N′). An explicit one needs a priori estimates near the axes on a strip of fixed width. That means a doubly-null
  structure regular at the axes, which no source has: Route W3 (4+1 double null with [LR20]-type renormalisation),
  Route D (quotient by the free circle, then 3+1 axisymmetric Einstein–scalar–null dust), or S-T3's Route C. Each is
  a separate paper of 1,500–3,000+ lines. Continuous dependence with a uniform width beyond compactness is open for
  the same reason.
- **The whole rectangle for large data.** False in general (§1.1). The right replacement is (c) and (d) of T4, with
  breakdown characterised by the continuation criterion. A finer breakdown statement, such as [AGS17, §3]'s "the
  first singularity occurs on the axis", is not examined here.
- **Families other than the two adapted ones near the axes.**
  - T4's corners lie on the faces *and* on null hypersurfaces of the solution (N_η, and the rectangles of T4-6).
    Lemma A needs every family active near an axis point of such a corner sphere to have the sphere's sections as
    leaves.
  - A further family has this only if its phase is a function of the double-null coordinate there (S-T3 §5.2).
  - So T4 requires further families to avoid the axes in the swept region. Tier 3 required this only near face-axis
    points.
- **Finite regularity.** T4 works in C^M, M ≥ M0(k), with k ≥ 6 (the axis machinery). C³ data (chapter 87) and
  measure-valued shells need an [LR20]-type weak theory in 4+1.
- **4+1 without symmetry.** Unchanged (S-CIVP Routes C and L).
- **Null dust in plain wave gauge.** Whether [HL17, p. 1]'s large-data claim holds for null dust in C^∞ (GN4-5 (ii)),
  or only in Gevrey classes (Route G). This does not affect T4.

---

## 6. Estimate and risks

**Size** (chapter lines, about 49.5 per PDF page), on top of Tier 3:

| Piece | Lines |
|---|---|
| T4-1 (K-ax) | 80–140 |
| T4-2 (corner theorem) | 150–250 |
| T4-3 (face jets through the axes) | 100–160 |
| T4-4 (uniqueness without smallness; D_max) | 80–130 |
| T4-5 (continuation along the generators) | 80–130 |
| T4-6 (continuation criterion) | 50–90 |
| T4-7 (statement, corollaries, remarks) | 70–120 |
| **Core total** | **≈ 610–1,030 (12–21 PDF pages)** |
| optional: T4-6′ (width bounded below) | 60–100 |
| optional: Corollary P | 40–60 |
| optional: cor:class-short-time at the axes (chapter 81) | 40–80 |

- Edits to chapters 81, 83 and 90: 30–70 lines.
- With Tier 3 (650–1,000) and Tier 1 (1,100–1,600), the characteristic problem through the axes for any size comes to
  about 2,400–3,600 lines. If Tier 3 is folded into Tier 1 (S-T3 §4.4), it comes to 2,050–3,100.
- Expect a writer and two to four confirming readings, as for Tiers 1 and 3. GN4-3 should be done by computer algebra.

**Risks.**
- **R1 (moderate to high): the continuation along the generators (T4-5).** It is not in the literature in this form,
  and the whole neighbourhood theorem rests on it, through uniform T (GN4-2) and bounded jets (GN4-3).
  - Mitigation: GN4-4's model test, and writing T4-5 before T4-6.
  - If it fails, T4 drops to (a), the corner, plus Corollary P. The large-data part of the loss sentence then stays.
- **R2 (moderate): K-ax (T4-1).** It looks routine: four points change, all listed. But lem:class-leaf-differences is
  dense, and its constants feed GN4-2.
- **R3 (moderate): the face jets at the axes (GN4-3).** First order off the axes is triangular and linear. At the axes
  the ∂_v-principal matrix degenerates like sin² ϑ in the naive variables. The regular form must be written, and a
  hidden Riccati term in the regular variables would break T4-5.
- **R4 (moderate, external): dependence on Tier 3.** T4 inherits Lemma A, T3-2, T3-3, T3-5, T3-6 and Lemma R. GN-T3
  is not yet reported.
- **R5 (low to moderate): uniqueness without smallness (T4-4).** The continuity argument is standard. The conversion to
  wave gauge for a second solution has to be run through the same corner-plus-continuation argument.
- **R6 (structural).** The width is not explicit. (H2) is a hypothesis that genuinely fails for some large data. (H3)
  is stronger than in Tier 3. The theorem and the loss sentence must say all three.
- **R7 (literature).**
  - [HL17, p. 1] contradicts the paper's derivative loss on its face. It is resolved by [CBF06]'s timelike hypothesis
    (verified), but the monograph [Choquet-Bruhat 2009] was not read.
  - Rendall 1990, Chruściel 1990 and Shatah–Tahvildar-Zadeh were not read. Chruściel 1990 is known through [Stå01]
    only; the other two through quotations.
  - [LR20] and [CTG23] remain preprints (S-CIVP).
  - No outside result enters a proof step of T4. Every step cites chapter 81, chapter 83, Tier 1 or Tier 3.

**References used here and not in S-CIVP or S-T3.**
- [HL17] C. Huneau, J. Luk, *Einstein equations under polarized U(1) symmetry in an elliptic gauge*, arXiv:1706.09499
  (Comm. Math. Phys. 2018).
- [CBF06] Y. Choquet-Bruhat, H. Friedrich, *Motion of isolated bodies*, Class. Quantum Grav. 23 (2006) 5941–5949,
  arXiv:gr-qc/0605096.
- [Tou21] A. Touati, *Einstein vacuum equations with U(1) symmetry in an elliptic gauge: local well-posedness and
  blow-up criterium*, arXiv:2101.09093.
- [Stå01] F. Ståhl, *Fuchsian analysis of S² × S¹ and S³ Gowdy spacetimes*, arXiv:gr-qc/0109011 (Class. Quantum Grav.
  19 (2002)).
- [RS05] O. Rinne, J. M. Stewart, Class. Quantum Grav. 22 (2005) 1143, arXiv:gr-qc/0502037 (now read in the body).
- [AGS17] L. Andersson, N. Gudapati, J. Szeftel, arXiv:1501.00616 v4 (re-read).
- [Luk12] and [CCTW16]: as in S-CIVP, re-read at the pages cited in §2.

The journal data for [HL17] and [Stå01] are given as commonly cited and were not checked against the publisher. Check
them before chapter 98 uses them.
