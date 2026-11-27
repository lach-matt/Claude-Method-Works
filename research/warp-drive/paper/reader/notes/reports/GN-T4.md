# GN-T4: go/no-go checks for Tier 4 (large data reaching the axes)

Nothing under `reader/` was edited, `assemble.py` was not run, and nothing was committed. All scripts and outputs are
in `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/gnt4/` (file list in
§8). Nothing in this report counts as proved. Numbers are labelled **computed** (by a script here), **deduced** (by an
argument written here) or **cited** (read in a source, with page).

**Read for this report.** notes/reports/S-T4.md (all) and S-T3.md (all). Chapter 81: 381–700 (thm:class-kato and its
proof), 848–1037, 1038–1671 (the axes, lem:class-leaf to rem:class-leaf-numerics, def:class-adapted,
thm:class-stability). Chapter 83: 334–600. proofs/P-CIVP.md (all of it as it stands, 656 lines; it now exists, being
written) and proofs/P-CIVP2.md: 1–60 and 391–605 (prop:civp-large-corner, thm:civp-large). The Tier 3 go/no-go report
`scratchpad/reader/reports/GN-T3.md` appeared while this work ran; it was read in full and is used where stated.

---

## Verdict: GO WITH CONDITIONS

| Check | Result | One line |
|---|---|---|
| **GN4-1** (K-ax) | **passed** | The proof of lem:class-leaf-differences holds for a smooth state V that is not a solution, with four changes and one definitional clause, all written out in §1. Its part (b) holds on bounded sets, with no ball, when proved leaf by leaf. Numerics at a large non-solution state: foliation to the edge of the grid, Lipschitz quotient bounded as the perturbation concentrates at the axis. |
| **GN4-2** (uniform corner time), preliminary | **open, no obstruction found** | Every constant of thm:class-kato (a) with u_* = Û, and of the Tier 3 steps as S-T3 and GN-T3 describe them, traces to C^M bounds of the face data near the corner and to κ. Seven items need care (§2.3); none is a dependence on the background, on face lengths or on smallness that cannot be removed. The complete trace waits for the Tier 3 text. |
| **GN4-3** (face jets through the axes) | **passed** | With frame-normalised equations the ∂_v-principal matrix has determinant −γ_ϑ/(4Ω⁹) (computed), so it does not degenerate at the axes; S-T4's sin²ϑ was an artefact of coordinate components. In axis-regular variables the first and second jets are linear, triangular and regular at both axes, and the conical condition propagates (computed). All orders follow by a structural induction and by naturality of the equations on S³ (deduced). |
| **GN4-4** (the continuation) | **passed** | T4-5 is written in full (§4.1). T4-2 accepts a general ingoing face and a short ingoing piece (§4.2), and Lemma R glues without smallness (§4.3). Model test: □φ = ∂_uφ ∂_vφ succeeds (hypotheses checked; numerics give a strip of width ≥ 0.82 along the whole face while the interior blows up). Luk's □φ = (∂_uφ)² fails exactly at hypothesis (J), bounded jets: the first transverse jet obeys a Riccati equation along the face. |
| **GN4-5** (literature) | **partly done** | Chruściel 1990: read in the author's scan (pp. 100–102 in full, Lemma 5.1 by extraction). Choquet-Bruhat: the 2009 monograph's text was not obtained (table of contents read); her 2014 textbook was read at pp. 208–209 and asserts equations, not well-posedness, for null dust. Rendall 1990: not obtained; two secondary statements of his theorem read, neither states how the neighbourhood depends on the data. |

**Conditions for GO.**
1. **Tier 3 as amended by GN-T3.** T3-2 split into an extension version (a) and a leaf-wise version (b); the slice
   triangle for T3-6; the τ-continuity step of GN3. Tier 4 inherits all of it (S-T4 R4). GN-T3 reports GO on GN1–GN3.
2. **K-ax** written as in §1.3, including part (b′) (leaf-wise, on bounded sets).
3. **T4-2** written without a background: the gauge reference is the extension Ĝ (as P-CIVP already does), the chart
   scale and T0 are fixed by (K, κ), thm:class-kato (a) runs with u_* = Û from an initial slice placed T*/2 before the
   corner, and its T* is stated as a function of norms of Û (§2.3, items 1–4).
4. **T4-3** written in natural (tensorial) form on the sections, with the conical condition and the two regularity
   indices of §3.5.
5. **T4-4** structured as a local-to-global continuity argument (local wave maps at corners plus Lemma R about the first
   solution, which is a genuine solution, so K-ax is not needed there).
6. **No outside result in a proof step.** [HL17, p. 1]'s null-dust sentence stays out of the argument (§5).

**What the verdict rests on.** R1 of S-T4 (the continuation) is now written and checked against a model and against
Luk's counterexample, and its hypotheses are isolated: (C) a corner time depending only on local norms, (J) bounded
jets, (U) uniqueness without smallness, (E) short pieces. (J) is passed (GN4-3), (U) and (E) are confirmed (§4), and (C)
is the one hypothesis whose full trace waits for written text (GN4-2). That is the remaining moderate risk.

---

## 1. GN4-1: K-ax, the planar shear about a smooth reference that is not a solution

### 1.1 Where lem:class-leaf-differences uses that ů is a solution

Reading 81:1324–1353 line by line, "ů is a smooth class solution" is used in exactly five places.
- (i) "let h̊ be the leaves of ů_A": they are level sets of ů_A (81:1325).
- (ii) "for U near ů they are C¹-close to the leaves of ů and foliate a neighbourhood of the axis" (81:1328–1329): the
  foliation by ů's leaves comes from ∂_z ů_A ≠ 0 and the implicit function theorem (lem:class-leaf (b)).
- (iii) the smoothness of h̊, which makes L_ů "smooth and uniformly elliptic" (81:1341–1342).
- (iv) "Derivatives transverse to the disc" and "the shift δc of the foliation enters as (∂_c σ[ů]) δc, the derivative
  falling on ů" (81:1344–1347): the leaves are labelled by the value c of ů_A.
- (v) the norm 𝒩_k of eq:class-energy, which measures U − ů.

Nowhere does the proof use an equation that ů satisfies. The leaf equation, interior regularity, the Volterra
uniqueness and the bound of step (3) of lem:class-planar-shear are statements about a given H_L and a given γ3.

### 1.2 Statement (K-ax)

Near a point of axis 2 with ρ1 > 0, on a slice Σ_τ, let V = (g_V, p_V, Θ_V, q_V) be smooth and G-invariant, with g_V
Lorentzian, Σ_τ spacelike for g_V, and p_V(∂_z) ≥ c > 0 on the axis (the sign fixed). For a state U let:
- **H_L[U]** := (Θ_A − κ_A1 + p_A(n) tr K_Σ|_E)/|p_A^Σ|, times the sign of p_A(∂_z), where E is the γ3-orthogonal
  complement of p_A^Σ in TM3. This is the definitional clause GN-T3 §1.2 asks for: E must be fixed by the state, since
  lem:class-volterra takes H as a function of position.
- **the leaves of U**: for each axis point z0, the solution h_U(·; z0) of eq:class-leaf-volterra with H_L(ρ) :=
  H_L[U](h(ρ), ρ) and h(0) = z0 (lem:class-volterra);
- **σ[U](x)**: eq:class-shear-leaf for the leaf of U through x, with |p_A^Σ| for |∇_M3 u| and p_A(n) for n(u);
- **𝒩_k^V(U)**: eq:class-energy with V in place of ů (U − V in every component).

Then:
- **(o) Foliation.** There are r_V > 0 and an interval I_V about the axis point such that the leaves of V with
  z0 ∈ I_V are graphs over 𝔻_(r_V), (z0, y) ↦ h_V(y; z0) is smooth with ∂_(z0) h_V ≥ 1/2, and they foliate a
  G-invariant neighbourhood of the axis point. r_V and |I_V| depend only on lower bounds for A3, B3, det₂, on C² bounds
  of γ3 (that is, of g_V), on C¹ bounds of (p_V, Θ_V) and on c.
- **(a), (b)** of lem:class-leaf-differences hold verbatim with ů replaced by V, 𝒩_k by 𝒩_k^V and δ ≤ min(ρ1(p)/4,
  r_V/2); the balls 𝔅, 𝔅′ and C depend on C^(k+2) bounds of V, on c and on r_V.
- **(b′) Leaf-wise, on bounded sets.** Let U, U′ have C² bounds of g, C¹ bounds of (p_A, Θ_A) at most 𝔐 and the
  axis nondegeneracy c, and let D ⊂ Σ_τ be closed under the leaves of both (each leaf through a point of D ∩ 𝒰_δ lies,
  as a graph over 𝔻_(2δ), in D). Then
  ‖σ[U] − σ[U′]‖_(L²(D∩𝒰_δ)) ≤ C(𝔐, c) ‖U − U′‖_(L²(D∩𝒰_(2δ))), U including ∂g.
  No ball and no extension operator enter, and C does not see the width of D.

### 1.3 The proof, line by line

**(o).**
1. lem:class-volterra gives, for each z0 near the axis point, a unique leaf on [0, r0] with |h′(r)| ≤ C_0 r. Its
   constants are exactly those listed in (o): C_0 bounds |G(r, z, 0)|/r with G = r H/a_L − E_L, so it uses sup |H_L[V]|
   and the 1-jet of γ3; C_1 bounds ∂_z G, which uses ∂_z H_L[V] (C¹ of p_V, Θ_V, C² of g_V); C_2 uses the 1-jet of γ3.
2. The fixed point depends C¹ on z0 (uniform contraction with a parameter). Put π := ∂_(z0) p, p = h′. Differentiating
   r p(r) = ∫_0^r G(ρ, h(ρ), p(ρ)) dρ with h = z0 + ∫_0^ρ p gives
   r π(r) = ∫_0^r (∂_z G · (1 + ∫_0^ρ π) + ∂_p G · π) dρ.
   On the contraction domain |∂_p G| ≤ 1/4, so sup_[0,r] |π| ≤ (C_1 r/2)(1 + r sup |π|) + (1/4) sup |π|, hence
   |π| ≤ C r and |∂_(z0) h − 1| ≤ C r²/2 ≤ 1/2 for r ≤ r_V (deduced).
3. So for each fixed y, z0 ↦ h_V(y; z0) is strictly increasing: the leaves foliate the region between the leaves of the
   two end points of I_V.
4. Smoothness in y at fixed z0: step (3) of lem:class-planar-shear proves h ∈ H^(k+2)(𝔻_δ) from H_L ∈ H^k(𝔻_(2δ))
   for any graph solving eq:class-leaf-cartesian; it never uses that H_L comes from a phase. With H_L[V] smooth, h_V is
   smooth (every k). Joint smoothness in (z0, y): differentiate the leaf equation in z0; ∂_(z0)^j h solves the
   linearised equation with a right side of lower order, as in step (4) of lem:class-planar-shear with z0 in place of c.

**(a).** Change only (i)–(v) of §1.1.
1. "h̊ the leaves of ů_A" becomes "h_V(·; z0) the leaves of V of (o)". Their smoothness comes from (o) step 4, not from
   level sets of ů_A.
2. The difference δh := h_U(·; z0) − h_V(·; z0) of leaves **with the same axis point** solves
   L_V δh = δH_L − (terms in δγ3 and its first derivatives) + Q(δh),
   with L_V the operator of eq:class-leaf-cartesian linearised at h_V, plus the zero-order term −∂_z H_L[V] δh. It is
   smooth and uniformly elliptic on 𝔻_(2δ) with the axis interior (positive definiteness holds at any graph,
   lem:class-leaf (b)). The derivation subtracts the two leaf equations; no equation for V is used.
3. lem:class-interior-regularity with j = k and absorption of Q on 𝔅 are unchanged.
4. Derivatives transverse to the disc are taken in z0 and τ. They commute with L_V up to lower order with smooth
   coefficients because h_V is smooth in (τ, z0, y) by (o). The Jacobian 1/∂_z u of the chart change (c, y) ↔ (z, y)
   becomes 1/∂_(z0) h_V ∈ [1/2, 2].
5. The shift of the foliation: at a point x, z0^U(x) and z0^V(x) are the axis points of the two leaves through x;
   σ[U](x) − σ[V](x) = (σ_U − σ_V)(z0^U(x), y) + (σ_V(z0^U(x), y) − σ_V(z0^V(x), y)).
   The second term is (∂_(z0) σ_V) δz0 + O(δz0²), the derivative falling on V (smooth by (o)), with
   δz0 = −δh(y; z0^V)/∂_(z0) h_V + O(δh²).

**(b).** Unchanged with 𝔅′ about V. The sup norms of the coefficients of L_U and their first derivatives (first and
second derivatives of the leaves, first derivatives of g) are bounded on 𝔅′ by lem:sobolev and by step (3) of
lem:class-planar-shear, where now sup |∂h| ≤ C_0 r comes from lem:class-volterra rather than from ∂h = −∂_y u/∂_z u. The
shift costs ∂_(z0) σ_(U′), bounded on 𝔅′.

**(b′).** This is GN-T3's T3-2(b), with the absorption removed.
1. For U, U′ and one axis point z0, write the difference of the two leaf equations by the mean value formula:
   ∫_0^1 L_s ds δh = ∫_0^1 (δH + ∂_z H^s δh − (∂_γ 𝔐)_s δγ3) ds,
   where L_s is the mean curvature operator linearised at the graph h_s := s h_U + (1 − s) h_(U′) for the metric
   γ_s := s γ3^U + (1 − s) γ3^(U′). Every γ_s is Riemannian and every h_s is a graph, so every L_s is uniformly elliptic
   by lem:class-leaf (b). Its coefficients and their first derivatives are bounded by C² bounds of both leaves, which
   step (3) of lem:class-planar-shear bounds by 𝔐. No smallness of U − U′ is used.
2. lem:class-interior-regularity with j = 0 on the disc: ‖δh‖_(H²(𝔻_δ)) is bounded by C times the L²(𝔻_(2δ)) norms
   of δH, of δγ3 and its first derivatives along the leaf, and of δh.
   All three right-hand quantities are evaluated on the leaves, which lie in D.
3. The L² bound on δh: subtract the Volterra equations. For r ≤ r0 the contraction gives
   sup_[0,r] |δp| ≤ C sup_(ρ≤r) ρ⁻¹ ∫_0^ρ (t |δH|(t) + |δ(a_L, E_L)|(t)) dt;
   for r0 ≤ r ≤ 2δ the equation (r h′)′ = r H/a_L − E_L is a regular ordinary differential equation and Gronwall
   applies. The operator f ↦ r⁻¹ ∫_0^r t f(t) dt is bounded on L²(r dr; [0, 2δ]) with norm ≤ δ (Cauchy–Schwarz:
   |Tf(r)|² ≤ (1/2) ∫_0^r t f² dt; deduced). So ‖δh‖_(L²(𝔻_(2δ))) ≤ C ‖U − U′‖ on the leaf.
4. The shift term at x uses U′-leaves with axis points between z0^U(x) and z0^(U′)(x). Both lie in the axis interval of
   D, so those leaves lie in D (GN-T3 §2.3).
5. Integrate over z0 with ∂_(z0) h ∈ [1/2, 2]: L² norms over the leaves become L²(D) norms.

**Status: passed (deduced).** Size: 100–160 chapter lines with (b′), against S-T4's 80–140.

### 1.4 Numerics at a large non-solution state (optional part)

Script `gn41_leaves.py` (computed, floating point, DOP853, rtol 10⁻¹¹). Metric of eq:class-m3-metric with
A3 = 1 + 0.4z + 0.3r², B3 = 1.2 − 0.3z + 0.2r², C3 = 0.3 + 0.2z, D3 = 0.25 + 0.1z, and prescribed mean curvature
H_V = 2 + 1.5z + r² + 0.8 sin 3z. Any such H is H_L[V] for some state V (choose Θ_A); no phase is involved.

- **Code check.** A prescribed graph is recovered from its own mean curvature to 4.25 × 10⁻¹³ in h and 4.27 × 10⁻¹² in
  h′/r.
- **Foliation.** min over z0 ∈ [−0.3, 0.3] of ∂_(z0) h at r = 0.1, 0.25, 0.4, 0.6:

  | state | r = 0.1 | 0.25 | 0.4 | 0.6 |
  |---|---|---|---|---|
  | large V | 0.9902 | 0.9365 | 0.8234 | 0.2319 |
  | H = 0, same metric | 0.9999 | 0.9991 | 0.9976 | 0.9936 |

  The leaves of V foliate to the edge of the grid, r = 0.6, although they move by up to 0.361 in z for r ≤ 0.5
  (against 0.056 for H = 0).
- **Lipschitz quotient of (b)**, Q := ‖σ_L[U] − σ_L[V]‖_(L²(𝒰_δ))/‖H_U − H_V‖_(L²(𝒰_2δ)), weight r dr dz,
  𝒰_δ = {|z| ≤ 0.15, r ≤ 0.25}, 𝒰_2δ = {|z| ≤ 0.3, r ≤ 0.5}, compared at the same points (foliation shift included):

  | perturbation | Q | Q with 𝒰_δ in the denominator |
  |---|---|---|
  | 0.01 e^(−r²/ε²)(1 + 0.5 cos 4z), ε = 0.2 | 0.15695 | 0.21480 |
  | ε = 0.1 | 0.31596 | 0.42282 |
  | ε = 0.05 | 0.36205 | 0.48450 |
  | ε = 0.025 | 0.37129 | 0.49686 |
  | A e^(−r²/0.15²)(1 + z), A = 0.4, 0.2, 0.1, 0.05, 0.025 | 0.22809, 0.22773, 0.22756, 0.22747, 0.22743 | — |
  | A z, A = 0.2, 0.1, 0.05 (tilts the foliation) | 0.01698, 0.01695, 0.01693 | — |

  The quotient stays bounded as the perturbation concentrates at the axis (no derivative loss at order 0); the
  same-box quotient tends to the flat value 1/2 of rem:class-leaf-numerics. In amplitude it converges (Lipschitz, not
  only linearised). These are observations on a model of the leaf equation; no proof uses them.

---

## 2. GN4-2 (preliminary): uniform corner time

### 2.1 What T4-2 consists of

From S-T4 §4.3 and the Tier 1 text as it stands (P-CIVP Block B, case (II)), the corner theorem is:
1. jets near the corner (lem:loc-cone-jets);
2. the formal extension Û (prop:loc-cone-formal), with the gauge reference Ĝ := its metric;
3. the cut-off system 𝔄_ξ(U) = F̃, F̃ := 1_P 𝔄_ξ(Û), on [t_init, t_init + T*] × ℝ⁴, solved by thm:class-kato (a) with
   u_* := Û on a ball 𝒟_ρ about Û;
4. T3-5 (U = Û on P), T3-6 (constraints on the slice triangle F ∩ {t ≤ s}), T3-7 (double null), Lemma R.

### 2.2 The constants of thm:class-kato (a) with u_* = Û (81:594–640)

Read off the proof (deduced):
- **c0**, the lower bound of A^0 = diag(1, −g^(tt), g^(ab)) and P_A^t. With t = u + v, −g^(tt) = 1/Ω² and
  P_out^t = P_in^t = 1/(2Ω²) (the inverse metric in the proof of lem:loc-cone-equations). So c0 depends on upper
  bounds of Ω and on the positivity of g^(ab) on the slice: part of (K, κ).
- **C_A, C_u**: bounds of |A^0| on |u| ≤ C_S(sup_t ‖Û(t)‖_(H^s) + ρ).
- **Bounds of order s for the A^μ**: the coefficients depend on x through Ĝ and its derivatives of order ≤ 2 (P-CIVP,
  the paragraph before lem:loc-cone-system) and through ξ and the chart. So they need C^(s+2) of Ĝ.
- **𝔐, 𝔐′, K_*.** K_* bounds F(t, u^n) − 𝐀^0 ∂_t u_* − 𝐀^j ∂_j u_* in H^s, so it uses sup_t ‖u_*‖_(H^(s+1)) and
  sup_t ‖∂_t u_*‖_(H^s). The first iterate needs T* sup_t ‖∂_t u_*‖_(H^s) ≤ 𝔐 − ‖u0‖_(H^s).
- **C_F(𝔐), L(𝔐)**: the local part through bounds of order s and ‖F̃‖_(H^s) (rem:class-kato-local); the non-local part
  through K-ax (a) and (b) with V = Û.
- **ρ**: the K-ax balls 𝔅, 𝔅′ about Û must contain 𝒟_ρ; ρ depends on C^(k+2) bounds of Û, c and r_Û.

So T* = T*(‖Û‖_(C^(s+3)(supp ξ)), κ, r_Û, δ, chart). Each of these traces to C^M bounds of the face data within T0 of
the corner and to κ, once the chart and T0 are fixed by (K, κ) (deduced).

### 2.3 Items that need care (flags)

| # | Where | What depends on what | Remedy | Kind |
|---|---|---|---|---|
| 1 | thm:class-kato (a) (81:583–584) | T* "depending only on an upper bound for ‖u0‖, on ρ and on u_*": the dependence on u_* is not quantified in the statement | add (in a remark or in T4-2's proof): u_* enters only through sup_t ‖u_*‖_(H^(s+1)), sup_t ‖∂_t u_*‖_(H^s) and C_A | edit of wording, 1–2 lines |
| 2 | P-CIVP case (II) | uses thm:class-kato-stability (a), which needs ρ = ∞; with the axis closure the forcing is non-local and defined on a ball | use thm:class-kato (a) with u_* = Û, as S-T4 says | already planned |
| 3 | P-CIVP chart τ = ln((u + δ_c)(v + δ_c)) | the corner is at τ_init + ln 4, so a fixed τ_init needs T* ≥ ln 4 | put Σ_init at τ = 2 ln δ_c − T*/2 (it lies in P for every T* > 0: on F, (u + δ_c)(v + δ_c) ≥ δ_c²); the corner region covered is [0, σ]² with σ ≈ δ_c(e^(T*/4) − 1) | writer's detail |
| 4 | P-CIVP def:loc-cone-data (iii), lem:loc-cone-strips, A^μ_♭, c_+ = (min(δ_1, η/C_*)/4)² | the corner time σ_1 = δ_c/8 depends on a round **background** (δ_1, C_*) and on the band's distance η from the axes | reference Ĝ everywhere (A^μ_♭ included); δ_1 → T0(K, κ); C_* → a bound from (K, κ); η removed (axes handled by Tier 3) | genuine change to Tier 1's statement of case (II) |
| 5 | lem:loc-cone-jets (iii), prop:loc-cone-formal (a) | sizes are measured relative to the background (C_j depends on "Λ and the background") | restate in absolute C^M norms; the proofs are linear ODE bounds and do not need a background | wording |
| 6 | T3-6 | U′ (Θ_A replaced by div_g P_A) must lie in the K-ax ball about Û. In Tier 3 this came from smallness (81:1615–1617). Here Δ_A(Û) is not small away from the faces | on the triangle {u + v ≤ T}, |Δ_A(Û)| ≤ C_N T^N (flat on the faces), so U′ − Û = O(ρ + T^N); or use K-ax (b′), which needs no ball | condition on T |
| 7 | face lengths and regularity | the jet bound K′ on the whole face grows like e^(C v1) (Gronwall); the hierarchy loses 4 angular derivatives per order (P-CIVP lem:loc-cone-jets (iii)) | T depends on K′ but not otherwise on v1; state T4 with two indices: T depends on C^M norms near the corner (M = M0(k), e.g. 6k + 12 as in P-CIVP), and the jet bound needs the face data in C^(M′), M′ ≥ 4M | statement |

**S-T3's GN2 (one component at a time near the corner time).** GN-T3 §2 settles it, and the settlement carries over:
the two components of P ∩ Σ_t are each bounded by one sphere, so the extension version is uniform; F ∩ Σ_t is a thin
shell, no extension from it is uniform (GN-T3's capacity bound), and the leaf-wise version (K-ax (b′) here) needs none.
For T4-2 the energy region of T3-6 is the triangle {u + v ≤ s}, whose slice sections are bounded by face sections only,
so GN-T3's §4 obstruction (a future face that is a leaf of one family only) does not arise inside a corner theorem.

**Lemma R** needs no K-ax at all: its reference V is the first solution, a genuine smooth solution of any size, so
lem:class-leaf-differences applies with ů := that solution (§4.3).

**Status: open, no obstruction found.** The trace above is of the steps as described. It must be repeated on the
written T3-4 and T3-6.

---

## 3. GN4-3: linear face jets through the axes

### 3.1 Set-up

Metric eq:loc-double-null with A_c = log cos ϑ + a, A_s = log sin ϑ + s. Axis conditions (S-T3 T3-0):
- at axis 2 (x := ϑ → 0): Ω, γ_ϑ, a, s even in x, b odd, and the conical condition e^(2s) = γ_ϑ at x = 0;
- at axis 1 (x := π/2 − ϑ): the same with a in place of s (b is again odd in x: a smooth radial field is f(x²) x ∂_x
  and ∂_ϑ = −∂_x).

The five evolution components on 𝒞_out = {u = 0}, normalised as frame components that are smooth through the axes:
E_uv = Ric(∂_u, ∂_v), E_uϑ = Ric(∂_u, ∂_ϑ), E_ϑϑ = Ric(∂_ϑ, ∂_ϑ), E_1 = e^(−2A_c) Ric(∂_φ1, ∂_φ1),
E_2 = e^(−2A_s) Ric(∂_φ2, ∂_φ2). The adapted dusts T = q_in dv² + q_out du² have no component in any of them.

### 3.2 Structure (computed, `gn43_structure.py`, exact sympy)

In both the raw and the regular variables:
- **No ∂_u² anywhere.** The second derivatives in the five components are: E_uv: Ω_ϑϑ, Ω_vϑ, Ω_uv, a_uv, b_vϑ, b_vv,
  γ_vϑ, γ_uv, s_uv; E_uϑ: Ω_ϑϑ, Ω_uϑ, a_uϑ, b_vϑ, b_uv, γ_vϑ, γ_uv, s_uϑ; E_ϑϑ: Ω_ϑϑ, a_ϑϑ, b_vϑ, γ_vϑ, γ_uv, s_ϑϑ; E_1:
  a_ϑϑ, a_vϑ, a_uv; E_2: s_ϑϑ, s_vϑ, s_uv.
- **Coefficients of second derivatives** contain no derivative (they depend on the undifferentiated functions and ϑ).
- **u-derivatives present**: E_ϑϑ, E_1, E_2 hold only (γ, a, s)_u and one of γ_uv, a_uv, s_uv; no Ω_u, no b_u. E_uv
  holds no b_u. Only E_uϑ holds b_uv and the angular derivatives Ω_uϑ, a_uϑ, s_uϑ.
- **First jets** (f = J0 + u J1 + u² J2/2 at u = 0): every row is of degree ≤ 1 in J1 and free of J2; E_vv and E_vϑ hold
  no transverse jet; E_uu is quadratic in J1 and holds J2 (the transverse Raychaudhuri equation, not used on 𝒞_out).
- **The ∂_v-principal matrix** on (Ω1, γ1, b1, a1, s1), rows (E_uv, E_uϑ, E_ϑϑ, E_1, E_2):

      ( −2/Ω0   −1/(2γ0)    0          −1        −1      )
      (  0      −b0/(2Ω0²)  −γ0/(4Ω0²)  0         0      )
      (  0       1/(2Ω0²)   0           0         0      )
      (  0       0          0           1/Ω0²     0      )
      (  0       0          0           0         1/Ω0²  )

  with determinant **−γ0/(4Ω0⁹)**, nonzero wherever Ω0, γ0 > 0, axes included. S-T4's determinant
  −γ0 e^(2A_c+2A_s)/(4Ω0⁹) came from the coordinate components Ric_φφ; normalising those two rows removes the sin²ϑ.
- **Triangularity.** (γ1, a1, s1) solve a closed 3 × 3 linear system, pointwise in ϑ (no angular derivative of a jet in
  E_ϑϑ, E_1, E_2); then Ω1 from E_uv (no angular derivative of a jet); then b1 from E_uϑ, which holds ∂_ϑ of Ω1, a1, s1,
  already known. This agrees with P-CIVP lem:loc-cone-jets ("first the three ϰ-components, then ln Ω, then b").

### 3.3 The axes (computed, `gn43_axis.py`, `gn43_defect.py`)

Solve the five rows for ∂_v J1 and expand at each axis, with J0 and J1 truncated Taylor series in x (degree 6, output to
O(x³); and degree 8, output to O(x⁵)) satisfying parity and the conical condition at orders 0 and 1, that is
γ0(0) = e^(2s0(0)) and γ1(0) = 2 s1(0) γ0(0) at axis 2 (a in place of s at axis 1). The cone constraints on J0 were
**not** imposed, so the check is stronger than needed.
- **Regularity.** At both axes no component of ∂_v J1 has a negative power of x, and every component has the right
  parity (even for Ω, γ, a, s; odd for b).
- **Conical condition propagates.** ∂_v(γ1 − 2 s1 γ0) = 0 at x = 0 (axis 2), and ∂_v(γ1 − 2 a1 γ0) = 0 at axis 1.
- **The condition is needed.** Without the first-order conical condition, ∂_v b1 acquires a pole:
  - axis 2: x⁻¹ · 2 (γ1(0) − 2 s1(0) e^(2s0(0))) Ω0(0)² e^(−4s0(0));
  - axis 1: x⁻¹ · 2 (2 a1(0) e^(2a0(0)) − γ1(0)) Ω0(0)² e^(−4a0(0)).
- **Its defect obeys a homogeneous linear equation along the axis generator.** With d1 := γ1 − 2 s1 γ0 at x = 0
  (not imposed): ∂_v d1 = −(1/2)(∂_v a0 − 2 ∂_v s0) d1 at axis 2, and ∂_v d1 = (1/2)(2 ∂_v a0 − ∂_v s0) d1 at axis 1.
  At the corner d1 = 0, because the 𝒞_in data are smooth on S³. So d1 ≡ 0 (deduced).

### 3.4 Higher orders (computed at k = 2, `gn43_order2.py`, `gn43_defect2.py`; deduced for all k)

**At k = 2** (∂_u of the five rows at u = 0, with jets to order 3):
- J3 does not occur; J2 occurs linearly with **the same principal matrix**; the same rows hold the same kinds of
  J2-terms (triangularity unchanged).
- Axis expansion (degree 5, output to O(x²)) with J0, J1, J2 axis-regular and the second-order conical condition
  γ2(0) = (2 s2(0) + 4 s1(0)²) γ0(0): no negative powers, right parity, at both axes.
- The second-order conical defect d2 := γ2 − (2 s2 + 4 s1²) γ0 at x = 0 has ∂_v d2 = 0 once the first-order equation
  for s1 (axis 2), respectively a1 (axis 1), is substituted. Before substitution ∂_v d2 equals 2 s1 e^(−2s0) times the
  residual of that equation.

**All orders (deduced).** By §3.2 the five rows are F(f, ∂f, ∂²f) = 0 with no ∂_u² f, linear in second derivatives with
coefficients depending on f and ϑ only. Apply ∂_u^(k−1) and set u = 0:
- ∂_u^k f enters only through ∂_u^(k−1)(∂_u f), ∂_u^(k−1)(∂_u ∂_v f) = ∂_v J_k and ∂_u^(k−1)(∂_u ∂_ϑ f) = ∂_ϑ J_k, each
  linearly, and no J_(k+1) occurs;
- the coefficient of ∂_v J_k is that of ∂_u∂_v f, a function of J0: the same matrix M;
- the coefficient of J_k is a function of (J0, J1); the rest is a polynomial in J0, …, J_(k−1) and their tangential
  derivatives;
- the rows E_ϑϑ, E_1, E_2 contain no Ω_u, b_u (as functions, since the J1-coefficients vanish identically), so Ω_k and b_k
  never enter them; E_uv contains no b_u. The triangular order is the same at every k.

So each J_k solves M ∂_v J_k = N(J0, J1) J_k + P(J0) ∂_ϑ(Ω_k, a_k, s_k) + S_k(J0, …, J_(k−1)), triangular, along each
generator, with initial value at the corner given by the 𝒞_in data. **No Riccati term at any order.**

**Regularity at all orders by naturality (deduced).** The double-null form with general angular coordinates θ^A on the
sections is preserved by changes of θ^A independent of (u, v), under which (Ω, b^A, γ_AB) transform as a scalar, a
vector and a tensor on S³. The jets J_k = (∂_u^k Ω, ∂_u^k b, L_(∂_u)^k γ) at u = 0 are therefore functions, vector fields
and symmetric tensors on S³ (smooth through the axes when the metric is), and the equations ∂_u^(k−1)E|_(u=0) are natural
differential expressions on S³ built from γ0 and its connection. So the coefficients of the hierarchy, written
tensorially, are smooth tensor fields on S³, the ODE in v is one for sections of a vector bundle over S³, and its
solution is a smooth section; G-invariance follows by uniqueness. The cot ϑ and 1/sin²ϑ in the (ϑ, φ) components are
removable, and the conical conditions at every order are just the statement that the solution is a smooth tensor. The
computer algebra of §3.3–3.4 is the coordinate confirmation at orders 1 and 2.

**Other pieces.**
- **𝒞_in.** The change of angle ϑ̃ with L̲ϑ̃ = 0 turns the metric into eq:loc-double-null with u and v exchanged
  (P-CIVP, proof of lem:loc-cone-ricci (a)). So the same computation covers the ingoing face. On N_η, where b ≠ 0, b is
  odd, so the flow of b∂_ϑ fixes the axes and the change of angle is a G-equivariant diffeomorphism of S³.
- **Densities (deduced).** ∂_u q_in = −b ∂_ϑ q_in − q_in(∂_ϑ b + b ∂_ϑ log 𝒱 + ∂_u log 𝒱), 𝒱 = γ_ϑ^(1/2) e^(A_c+A_s).
  The singular terms are b cot ϑ at axis 2 and b tan ϑ at axis 1, both smooth and even since b is odd; ∂_ϑ b + b ∂_ϑ log
  𝒱 is the divergence of the smooth field b∂_ϑ. Higher jets: ∂_u^k ρ_in = −∂_u^(k−1) ∂_ϑ(b ρ_in), algebraic in lower
  jets. q_out along 𝒞_out: ∂_v ρ_out = 0.

### 3.5 Bounds and the regularity bookkeeping (deduced)

- A linear ODE along generators of length ≤ v1 with coefficients smooth on the compact face gives
  sup_(𝒞_out) |∂_ϑ^α J_k| ≤ K′(K, κ, v1), with K′ growing like e^(C v1).
- P-CIVP lem:loc-cone-jets (iii) records a loss of 4 angular derivatives per order. So the jets up to order M in C^(M−j)
  need the face data in C^(M′), M′ ≥ 4M. With smooth data this is only bookkeeping, but T4's statement must say which
  norm K bounds.

**Status: passed (computed at orders 1 and 2; deduced for all orders).** R3 of S-T4 drops to low.

---

## 4. GN4-4: the continuation argument

### 4.1 T4-5 written out

**Setting.** Data on 𝒞_out^(v1) and 𝒞_in^(u1) as in T4 (H1)–(H3). A *development* is a smooth class solution in the gauge
of eq:loc-double-null on D × S³, D ⊂ Q1 a relatively open past set ([0, u] × [0, v] ⊂ D for (u, v) ∈ D), inducing the
data on the faces in D. D_max is the union of all developments' domains, well defined by T4-4 (two developments agree on
the intersection of their domains, itself a past set). D_max is a relatively open past set.

**Hypotheses used.**
- **(C) Corner time.** There are T0 = T0(K, κ) and T = T(K, κ) > 0 such that, for any corner sphere with an outgoing
  piece and an ingoing piece of length T0, carrying data in the gauge (any Ω on both, any b on the ingoing piece, any
  compatible corner values) with C^M norm ≤ K and nondegeneracy ≥ κ, there is a development on
  {u′ + v′ < T} (u′, v′ measured from the corner).
- **(E) Short pieces.** (C) holds when the ingoing piece has any length u′ > 0, the development being asserted on
  {u′′ ≤ u′, u′′ + v′ < T}, provided the C^(M+1) norm on the piece is finite and its C^M norm is ≤ K (§4.2).
- **(J) Bounded jets.** The transverse jets J_k (k ≤ M) of the data on 𝒞_out exist on the whole face and satisfy
  sup |∂_ϑ^α J_k| ≤ K′, |α| + k ≤ M (§3.5). Every development smooth up to 𝒞_out has ∂_u^k X = J_k there
  (P-CIVP lem:loc-cone-jets (iv) off the axes; at the axes by continuity in ϑ).
- **(U) Uniqueness.** Two developments in the gauge on a double-null rectangle R′ that induce the same data on its past
  faces agree on R′ (§4.3).

**Claim.** (0, v1) ∈ D_max. Hence, D_max being a relatively open past set, [0, u*] × [0, v1] ⊂ D_max for some u* > 0.
The same along 𝒞_in gives v*, which is T4 (b).

**Proof (deduced).**
1. Let V := sup{v ∈ [0, v1] : (0, v) ∈ D_max}. By (C) at S, V ≥ T_S/2 > 0. Since D_max is a past set,
   (0, v) ∈ D_max for every v < V. Suppose (0, V) ∉ D_max or V < v1. Fix η := min(T_c/4, V/2), where
   T_c := T(K_c, κ/2) and K_c := C_M(K + K′ + 1), C_M the constant of §4.2; T_c does not depend on η.
2. **The ingoing hypersurface.** (0, V − η) ∈ D_max, so by relative openness and the past property there is
   w(η) > 0 with [0, w(η)] × [0, V − η/2] ⊂ D_max. Let N_η := [0, w(η)] × {V − η}. The development induces on N_η
   functions (Ω, γ_ϑ, b, A_c, A_s, q_out) of (u, ϑ), smooth up to u = 0, satisfying the ingoing constraint, equal at
   S_η := {(0, V − η)} × S³ to the 𝒞_out data there. b ≠ 0 and Ω is not normalised on N_η, in general.
3. **Their norms near u = 0.** By (J), ∂_u^k of these functions at u = 0 are J_k(V − η, ·), bounded by K′ uniformly in
   η. The (M+1)-th u-derivatives are bounded on [0, w(η)] × S³ by some L(η) < ∞ (smoothness at fixed η). By Taylor's
   formula (L(η) bounding all derivatives of order M + 1, angular ones included), for u′(η) := min(w(η), 1/L(η)) the
   C^M norm of the N_η data on [0, u′(η)] × S³ is ≤ K′ + 1, and the
   nondegeneracy constants there are ≥ κ/2 for u′(η) smaller still (continuity at S_η, where they are the 𝒞_out data's).
4. **The corner problem at S_η.** Outgoing piece: 𝒞_out ∩ {V − η ≤ v ≤ V − η + T0} (data, C^M ≤ K; if
   V − η + T0 > v1, extend the free data past v1 as in §4.2 and solve the outgoing constraint, nondegenerate for a length
   depending on (K, κ)). Ingoing piece: N_η ∩ {u ≤ u′(η)}. By (E) and (C) there is a development g_η on
   {(u, v) : 0 ≤ u ≤ u′(η), V − η ≤ v, u + v − V + η < T_c}; it contains R_new := [0, ū] × [V − η, V − η + T_c/2]
   with ū := min(u′(η), T_c/2).
5. **Gauge.** g_η is in the same double-null gauge as D_max: v on 𝒞_out is the data's; u and ϑ on N_η are those of
   D_max, and in D_max ϑ is constant along the outgoing generators, which pass through N_η.
6. **Agreement.** On R_old := [0, min(ū, w(η))] × [V − η, V − η/2] both are developments in the gauge, with the same
   data on its past faces: the 𝒞_out data on {u = 0}, the N_η data on {v = V − η, u ≤ ū} (g_η induces them on
   u ≤ u′(η)). By (U), g_η = g there.
7. **Gluing.** D_max ∪ R_new is a past set: for (u, v) ∈ R_new, [0, u] × [0, V − η] ⊂ D_max (as u ≤ w(η)) and
   [0, u] × [V − η, v] ⊂ R_new. The function equal to g on D_max and to g_η on R_new is well defined by step 6 and
   smooth (each point has a neighbourhood where it equals one of the two). So it is a development, and
   (0, V − η + T_c/2) ∈ D_max with V − η + T_c/2 ≥ V + T_c/4 > V, against the definition of V (or, if that exceeds
   v1, (0, v1) ∈ D_max). ∎

**What is not used.** No a priori estimate, no bound on the solution inside D_max beyond smoothness at fixed η, and no
dependence of w(η) or u′(η) on η: both may tend to 0 as η → 0. Only T_c must be uniform, and it is, because the corner
data at S_η are bounded by K and K′.

**The continuation criterion T4-6 has the same shape (deduced).** If D_max ⊃ R_(a,b) ∖ {(a, b)} and the C^(M+1) norms
and nondegeneracy of the solution are bounded on D_max ∩ R_(a,b), take the corner S_(a−η, b−η) with η := T/4 and the two
null pieces through it, of length η plus the margin that relative openness gives, extended as in §4.2. (C) puts (a, b)
inside a development, glued by (U).

### 4.2 T4-2 accepts a general ingoing face and a short ingoing piece

**General gauge data and corner values (confirmed against the Tier 1 and Tier 2 texts).**
- P-CIVP def:loc-cone-data: "The data consist of the gauge functions ln Ω on both edges and b on N_i, which are free, of
  the conformal data and densities, which are free, and of the functions that (ii) determines; the corner values are
  arbitrary, subject to (i)." The constraint on N_i is written for L̲ = ∂_u + b∂_ϑ with general Ω (last line of
  eq:loc-cone-frame-ricci), and lem:loc-cone-jets solves the N_i hierarchy along the integral curves of L̲.
- At the axes the integral curves of L̲ starting on an axis stay on it, because b is odd (b = 0 there).
- Tier 2's prop:civp-large-corner normalises instead: Φ(u, ϑ) with (∂_u + b∂_ϑ)Φ = 0 maps eq:loc-double-null to itself
  with γ_ϑ/(∂_ϑΦ)², ∂_uΦ + b∂_ϑΦ in place of γ_ϑ, b, commutes with G, is the identity on N_o and makes b = 0 on N_i
  (P-CIVP2, Step 4, "The corner step"). It costs one derivative of b.
- **What Tier 1 does not yet provide** (flag 4 of §2.3): def:loc-cone-data (iii) requires the data to equal a round
  background near the axes, the size is measured against that background, and the corner time of case (II) depends on
  it and on the band's distance η from the axes. T4-2 is case (II) with those three removed, which is Tier 3's job at the
  axes and a restatement elsewhere.

**Short ingoing piece (deduced).** Let f be a datum on [0, u′] × S³ (a free function on N_η) with ‖f‖_(C^M) ≤ K₁ and
‖∂_u^(M+1) f‖_(L^∞) ≤ L. Let P(u, ϑ) := Σ_(j≤M) ∂_u^j f(0, ϑ) u^j/j!. Then g := f − P has vanishing M-jet at u = 0 and
|∂_u^i ∂_ϑ^α g| ≤ C L u′^(M+1−i) on [0, u′] (only the u-derivatives need the Taylor bound; angular derivatives are
handled in the same way with C^(M+1) in place of L). Rescale, g̃(s) := g(u′s), s ∈ [0, 1]: |∂_s^i g̃| ≤ C L u′^(M+1).
Seeley's reflection extends g̃ to s ∈ [0, 2] with the same bound, a cut-off makes it vanish for s ≥ 3/2, and scaling back
gives an extension Eg on [0, 2u′] with |∂_u^i Eg| ≤ C L u′^(M+1−i). So F := P + Eg (Eg := 0 beyond 2u′) equals f on
[0, u′] and ‖F‖_(C^M([0, T0])) ≤ C(K₁ + L u′) ≤ 2C K₁ once L u′ ≤ K₁. Then solve the ingoing constraint (Raychaudhuri
for ỹ along L̲) from S_η with the extended free data: on [0, u′] it reproduces the given data (ODE uniqueness), and ỹ
stays ≥ κ/4 on [0, T1] with T1 = T1(K₁, κ). The development on {u ≤ u′} does not depend on the extension, by (U).
This is the precise form of S-T4's "extend the free data beyond u′ by a Taylor polynomial": a polynomial alone is not
enough, since it does not agree with f on [0, u′].

### 4.3 Lemma R without smallness glues the pieces (confirmed)

- **Reference.** In Lemma R both states are genuine solutions; the reference V := the first solution is a smooth class
  solution of any size, so lem:class-leaf-differences applies with ů := V as written. Its balls are balls about V.
- **Continuity in t := u + v of the first solution** (GN-T3 §2.5).
  - Near the past corner the slice section is bounded by past-face sections, which are leaves of both solutions (they
    agree to infinite order on the past faces, so GN-T3's criterion holds for both): leaf-wise (b′), uniform in the
    width.
  - Elsewhere, until a neighbourhood of the far corner, the section has positive width and one boundary sphere on a
    future face, a double-null sphere of the first solution, hence a common leaf of both of its families: extension
    version with V := the first solution. If the solutions agree up to t*, then U2 − U1 is flat on D_(t*), so U2 lies in
    the ball about U1 on [t*, t* + θ] for small θ; this uses only smoothness, not size.
  - Near the far corner the width tends to 0: stop at t_end − θ and let θ → 0.
- **Gauge.** Lemma R is in wave gauge. Two developments in the double-null gauge are compared through a wave map, which is
  itself a semilinear characteristic problem; its local solvability at each corner (Rendall's reduction for a semilinear
  system, with linear jets) gives a local wave gauge in which Lemma R applies near that corner. T4-4 is then a
  continuity argument over the past set (sweep in u + v with corner problems of uniform size, as in T4-6), which needs
  no smallness because both developments are smooth on the compact rectangle (deduced).

So (U) holds without smallness (deduced), provided Tier 3's Lemma R is written as GN-T3 §2.5 and §6 (T3-8) specify.

### 4.4 Model test: □φ = ∂_uφ ∂_vφ (must succeed) and Luk's □φ = (∂_uφ)² (must fail)

Flat 1+2 dimensions, u = t − x, v = t + x, y ∈ S¹: □ = −4∂_u∂_v + ∂_y².

**Model A, □φ = ∂_uφ ∂_vφ: the hypotheses hold (deduced).**
- (J): on {u = 0}, w := ∂_uφ solves ∂_v w = −(∂_vφ/4) w + ∂_y²φ/4, linear; at order k, ∂_v(∂_u^kφ) =
  −(∂_vφ/4) ∂_u^kφ + (lower), linear in the top jet. So the jets are bounded on the whole face.
- (C): Rendall's reduction for a semilinear wave equation, with the time of the standard local existence theorem
  depending on norms of the extended data, gives T = T(C^M near the corner).
- (E), (U): as in §4.2 and by standard energy uniqueness.
- So the argument of §4.1 gives a development on a neighbourhood of both faces.
- Note: ∂_uφ ∂_vφ is not a null form in the sense of [Luk12, Definition 3, p. 40] when there are transverse directions:
  for null ξ, 4ξ_uξ_v = |ξ_y|², so ξ_uξ_v ≠ 0 when ξ_y ≠ 0. [Luk12, Theorem 6, p. 40] therefore does not cover it, and
  the argument here does. Its hypothesis is a linear jet hierarchy, not the null condition (deduced).
- In 1+1 dimensions ψ := e^(φ/4) solves ψ_uv = 0 exactly, so ψ = F(v) + G(u) − ψ(0, 0). This is positive near u = 0
  uniformly in v (strip exists) and can vanish inside (the solution blows up inside the rectangle) (deduced).

**Model B, Luk's □φ = (∂_uφ)²: where the argument fails (deduced).** On {u = 0}, w := ∂_uφ solves the Riccati equation
∂_v w = −w²/4 + ∂_y²φ/4. With φ = 0 on {u = 0} and w(0) = w0 < 0 it blows up at v* = 4/|w0|. Hypotheses (C), (E), (U)
and the identification of jets all hold; only **(J)** fails: the first transverse jet is a solution of an equation
**quadratic in itself**, so no bound K′ exists on a face reaching v*. In step 3 of §4.1 the corner data at S_η have
|∂_uφ| ~ 4/(v* − V + η), so T_η ≤ v* − V + η → 0, and the contradiction in step 7 is unavailable. This is [Luk12, §7.2,
pp. 41–42] (cited): "without a null condition, the theorem no longer holds. This is in contrast with Rendall's theorem,
which holds for general quasilinear wave equations" (p. 41), with the data "Prescribe φ = 0 on H_0 and φ spherically
symmetric on H_0 such that ∂_uφ < −C for some large positive C" (p. 41) and the conclusion "This is an ODE in
∂_uφ + 1/(2r^(1/2)) for each fixed u, which clearly blows up before u = 1 if C is chosen to be sufficiently large.
Thus a C¹ solution does not exist in 0 ≤ u ≤ 1, 0 ≤ u ≤ ε for any ε" (p. 42). The text extraction drops Luk's
underlines, which distinguish u from u̲ and H_0 from H̲_0; read with the set-up of p. 2, the blow-up is along the
outgoing cone in its own parameter, for the transverse derivative, as in model B.

**Numerics (computed, `gn44_model.py`, second-order diamond scheme, spectral ∂_y², 32 modes).**
- Model A data: φ(0, v, y) = −2.5 sin v (1 + 0.4 cos y), φ(u, 0, y) = 4 log(1 − 0.5u(1 + 0.2 sin y)), U1 = 1, V1 = 3.
  - Jets on u = 0: max_y |∂_uφ| = 2.4000, 4.3813, 4.4635, 2.7011 at v = 0, 1, 2, 3 (bounded).
  - Width W(v) of the region where the solution stays bounded: at v = 0, 1, 2, 3 it is 1.000, 0.940, 0.820, 0.820
    (h = 0.02) and 1.000, 0.930, 0.830, 0.830 (h = 0.01); minimum over the face 0.82–0.83 > 0, with blow-up inside the
    rectangle (W < U1). A neighbourhood of the face, not the rectangle.
- Model B data: φ(0, v, y) = 0, φ(u, 0, y) = −2u(1 + 0.2 cos y).
  - Jets on u = 0: 2.4000, 3.4293, 5.9978, 24.0000 at v = 0, 0.5, 1, 1.5; blow-up at v* = 1.6680 (exact 4/2.4 = 1.6667).
  - W(v) = 1 for v ≤ 1.65 and W = 0 from v = 1.70, 1.68, 1.675 (h = 0.02, 0.01, 0.005), converging to v*: no strip
    along a face that reaches v*.

**Status: passed (deduced; numerics consistent).**

---

## 5. GN4-5: literature

Search routes: Parallel web search and fetch, alphaXiv full text, Firecrawl (PDF OCR). royalsocietypublishing.org does
not resolve in this session, archive.org's search-inside is refused (403), and homepage.univie.ac.at is refused to the
shell but reachable through Firecrawl.

**(i) Rendall 1990** (Proc. R. Soc. Lond. A 427, 221–239, doi 10.1098/rspa.1990.0009). **Not obtained.** Abstract only,
via Semantic Scholar: "A method is described by means of which the characteristic initial value problem can be reduced to
the Cauchy problem … the characteristic initial value problem for the Einstein equations in vacuum or with perfect fluid
source is well posed when data are given on two transversely intersecting null hypersurfaces." Two secondary statements
were read:
- [Luk12, Theorem 3, p. 10]: "Then, there exists a small neighborhood of S_(0,0) in the future of S_(0,0) such that a
  unique solution to (12) exists."
- Chruściel–Paetz, *The many ways of the characteristic Cauchy problem*, arXiv:1203.4534v2, Theorem 2.1 (Rendall),
  p. 5: "Then there exists an open neighbourhood U of S in the region {x¹ ≥ 0, x² ≥ 0}, a unique function Ω on
  (N₁ ∪ N₂) ∩ U and a unique smooth Lorentz metric g_μν on U such that …"; and p. 2: "Rendall's elegant approach works
  well in vacuum, and more generally for a class of matter fields that includes scalar, Maxwell, or Yang-Mills fields."
- Neither states how the neighbourhood depends on the data. So T4-2's uniformity must be proved in-house, as S-T4 said.
  [Luk12, Theorem 1, p. 2] gives the dependence for vacuum through a priori estimates: "the size of the neighborhood
  can be made to depend only on the size of the initial data."

**(ii) Choquet-Bruhat, General Relativity and the Einstein Equations (OUP 2009).** **Text not obtained**: the
archive.org copy is access-restricted, and no preview was reachable.
- Read: the table of contents (OUP, via a library scan): chapter IX "Relativistic fluids … 2 Case of dust 260; 2.1
  Equations 260; 2.2 Motion of isolated bodies (Choquet-Bruhat and Friedrichs 2006); [3] Charged dust 3.1 Equations;
  3.2 Existence and uniqueness theorem in wave and Lorentz gauges; 3.3 Motion of isolated bodies" (the page numbers
  after 260 are garbled in the scan). There is no entry for null dust or massless dust. A table of contents cannot show that the text says
  nothing; it shows only that there is no section on it.
- Read instead: Choquet-Bruhat, *Introduction to General Relativity, Black Holes, and Cosmology* (OUP 2014), the same
  author's later textbook, §IX.1–IX.2:
  - p. 208: "One may also consider null fluids, with flow lines trajectories of a null vector field u, i.e. such that
    u^α u_α = 0."
  - p. 209, after the dust equations (IX.2.1)–(IX.2.4), which take u^α u_α = −1: "Similar equations are obtained for a
    null-dust model where u^α u_α = 0."
  - p. 209, the existence statement that follows is for dust only: "It can be proved [footnote 2: Fourès
    (Choquet)-Bruhat (1958). For more refined statements on the required regularity, see YCB-OUP2009, Chapter IX.] that
    an initial data set (M, ḡ, K, r̄, v̄) satisfying the constraints for the Einstein equations with dust source admits a
    globally hyperbolic and maximal Einsteinian development (V, g), unique up to isometries, with dust source (r, u)."
- **Conclusion.** No well-posedness statement for null dust was found in any text read. [HL17, footnote 1]'s
  "cf. [2]" stays unverified, and S-T4's remark on [HL17, p. 1] (T4-7) should be kept. Route W1 stays closed.

**(iii) Chruściel 1990** (Ann. Phys. 202, 100–150). Read in the author's scan (`papers/chrusciel/ANoPGowdyChrusciel.pdf`
on his homepage, linked as "scanned pages (pdf)"), through Firecrawl's OCR.
- p. 100 (abstract): "When the spatial topology is S³ or S² × S¹ or L(p, q) we show that no singularities form before
  'the spacelike boundary of Gowdy's square' is reached."
- p. 102: "According to the standard theory (cf., e.g., [3]) there exists an ε > 0 and a four dimensional Lorentzian
  manifold (⁴M, g_μν), ⁴M ≈ (−ε, ε) × ³Σ, called a development of (g_ij, P_ij, ³Σ), on which vacuum Einstein equations
  are satisfied … From the uniqueness of g_μν in harmonic coordinates it follows that if t is harmonic, then the action
  of G on ⁴M defined by g(t, p) = (t, gp) … is an action by isometries."
- Lemma 5.1, read in the OCR text with the phrase before it ("Let us recall the following well-known result which we
  prove for completeness in Appendix C"): "Let A_ij be a smooth tensor field on the open ball B(ε) ⊂ R³, ε > 0, A_ij
  invariant under rotations around the z-axis. There exist smooth functions α, β, γ, δ, ε, φ, invariant under rotations
  around the z-axis, such that A_ij takes the form (r, φ, z-cylindrical coordinates) A_ij dx^i dx^j = α dz² + r²β dz dφ
  + γ r dz dr + δ r² dr² + ε(dr² + r² dφ²) + φ r³ dr dφ." The extraction tool placed it on p. 130 and placed on p. 107
  the sentence "the parametrization (2.26) is not very useful either on S² × S¹ or on S³ because on the axes of symmetry
  λ₁₁λ₂₂ = 0, R = 0, and (2.26) becomes singular there"; those two page numbers and the second sentence were not
  checked against the page images.
- **Use.** This confirms the pattern S-T3 and S-T4 attribute to the literature: local existence through the axes from the
  unreduced theory plus invariance by uniqueness (vacuum, harmonic gauge), and an axis-smoothness lemma of the same kind
  as eq:class-axis-metric. It treats vacuum only. Cite it, if at all, for p. 102 and Lemma 5.1, with the page of Lemma
  5.1 checked first.

**Status: partly done.** (i) and (ii) remain open as stated; neither affects T4, since no outside result enters a proof
step.

---

## 6. What changes in S-T4's plan

1. **GN4-3 and R3.** The face hierarchy does not degenerate at the axes once the φ-rows are frame-normalised
   (det = −γ_ϑ/(4Ω⁹)). Write T4-3 in natural form on the sections (§3.4), with one remark on the conical condition and
   its propagation, and record the computer algebra as confirmation. R3 drops from moderate to low. T4-3 can probably be
   shorter (70–130 lines rather than 100–160).
2. **K-ax (T4-1)** gains part (b′), the leaf-wise estimate on bounded sets (§1.2–1.3). It serves T3-6 in T4-2 and makes
   GN-T3's T3-2(b) available without a ball. Add the definitional clause fixing E = (p_A^Σ)^⊥ in H_L. Estimate 100–160
   lines.
3. **T4-2.** State it as P-CIVP's case (II) without the background (flag 4), with thm:class-kato (a) in place of
   thm:class-kato-stability (a), the initial slice T*/2 before the corner (flag 3), the quantified dependence on u_*
   (flag 1), and the condition of flag 6 on T. Its natural region is the slice triangle {u + v ≤ T}, which avoids GN-T3's
   future-face obstruction.
4. **Two regularity indices** in T4's statement (flag 7, §3.5): T depends on C^M near corners; the jets need C^(M′),
   M′ ≥ 4M, on the faces.
5. **T4-5** as written in §4.1. Its hypotheses are (C), (E), (J), (U); the scope is "linear jet hierarchy", not "null
   condition" (§4.4). S-T4's "extend by a Taylor polynomial" should read "Taylor polynomial plus a rescaled Seeley
   extension of the remainder" (§4.2).
6. **T4-4** needs no K-ax: Lemma R's reference is the first solution, a genuine solution. Structure it as local wave maps
   at corners plus Lemma R (GN-T3 §2.5), swept in u + v.
7. **Literature.** Replace "Rendall 1990: not read" by the two secondary statements of §5 (i). For [HL17, footnote 1], add
   the 2014 textbook's sentence (p. 209), which gives equations and no well-posedness for null dust. Chruściel 1990 can
   now be cited for p. 102 and Lemma 5.1 (after checking that page).
8. **R1** (the continuation) drops from moderate–high to moderate: the argument is written and checked, and what is left
   is (C), whose full trace waits for the Tier 3 text (GN4-2).

Size: the core total stays within S-T4's 610–1,030 lines (T4-1 +20, T4-3 −30, T4-2 +20 for the flags).

---

## 7. Risks that remain

1. **(C), the corner time (moderate).** The trace of §2 is of steps as described. thm:class-kato (a) on a ball about the
   non-solution Û, K-ax constants and the T3-6 condition (flag 6) must be checked on written text.
2. **Tier 3 itself (moderate, external).** T4 inherits Tier 3 as amended by GN-T3, including the re-proof of
   lem:class-leaf-differences (b) leaf by leaf (GN-T3 R1), which K-ax (b′) supplies.
3. **Uniqueness in the double-null gauge (low to moderate).** The local wave-map step of T4-4 must be written; it is a
   semilinear corner problem with linear jets, so (C), (E), (J) hold for it, but nobody has written it.
4. **Numerics are models.** §1.4 is a model of the leaf equation with chosen coefficients; §4.4 is a flat model. They
   confirm mechanisms, not constants. No proof should cite them.
5. **Literature (low).** Rendall 1990 and the 2009 monograph's text were not read.

---

## 8. Files

All in `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/gnt4/`:

| File | What it does | Output |
|---|---|---|
| `ricci_dn.py` | Ricci tensor of eq:loc-double-null in raw and axis-regular variables; the five normalised rows (cached in `ricci_raw.pkl`, `ricci_reg.pkl`) | — |
| `gn43_structure.py` | second derivatives, coefficients, first jets, principal matrix and determinant, triangularity | `gn43_structure.out` |
| `gn43_axis.py` | ∂_v J1 expanded at both axes with axis-regular inputs; conical propagation; pole without the conical condition (arguments: Taylor degree, output order) | `gn43_axis_K6.out`, `gn43_axis_K8.out` |
| `gn43_defect.py` | the linear equation for the first-order conical defect | `gn43_defect.out` |
| `gn43_order2.py` | second jets: J3 absent, J2 linear, same matrix; axis regularity | `gn43_order2.out` |
| `gn43_defect2.py` | second-order conical defect after the first-order equation | `gn43_defect2.out` |
| `gn41_leaves.py` | Volterra leaves of a large non-solution state: code check, foliation, Lipschitz quotients | `gn41_leaves.out` |
| `gn44_model.py` | model A and Luk's model B: jets on the face, characteristic solves, widths | `gn44_model.out` |

Run with python3 (sympy 1.14, numpy 2.5, scipy 1.18). Run times: structure 3 s; axis checks 1–4 min each; order 2 about
3 min; leaves about 8 min; model about 1 min.
