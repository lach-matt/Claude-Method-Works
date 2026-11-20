# Report: P-CIVP4 (Tier 4 of the characteristic initial value problem: data of any size reaching the axes)

File written: `research/warp-drive/paper/reader/proofs/P-CIVP4.md`, 1154 lines, md5 436d17be962a9c34358832bfce3c00b9.
No chapter, crosswalk, Appendix A or bibliography file, and neither P-CIVP.md nor P-CIVP2.md, was edited. Nothing under
method/, drive/, extracted/ or recovered/ was read. Nothing was committed. P-CIVP3.md (Tier 3) does not exist yet; its
results are cited by pending markers, and only where Tier 4 cannot do without them.

## 1. The theorem as stated (thm:civp-axes)

Cone data in the sense of def:civp-axes-data on edges N_o = {0} × [0, λ_v], N_i = [0, λ_u] × {0}: G-invariant smooth
families of Ω > 0, a vector field b and a Riemannian metric γ on S³ (the natural double-null form eq:civp-axes-form,
smooth through the axes because they are tensor fields on S³), densities q_in ≥ 0, q_out ≥ 0, the constraints, any Ω
on both edges and any b on N_i, any size, no condition at the axes beyond smoothness. Q := [0, λ_u] × [0, λ_v].
(The face lengths are λ_u, λ_v, not u1, v1, to avoid the chapter's u1 = 5.7.)

- (a) Corner: a class solution in the gauge on [0, σ]² × S³, σ depending only on k, the size Λ in C^(6k+19) of the data
  within distance l := min(1, λ_u, λ_v) of the corner, their nondegeneracy κ (γ ≥ κγ̊) there, and l.
- (b) Neighbourhood of the cones: u*, v* > 0 and a development on ([0, u*] × [0, λ_v]) ∪ ([0, λ_u] × [0, v*]).
- (c) Uniqueness in the gauge without smallness; the maximal development D_max (relatively open past set); it contains
  the developments of (a), (b), Tier 1 (thm:loc-cone-development), Tier 2 (thm:civp-large) and Tier 3 when their
  hypotheses hold.
- (d) Continuation criterion on rectangles R_(a,b): bounded derivatives of order ≤ 6k + 26 and γ ≥ κγ̊ on R_(a,b) ∖ {(a,b)}
  give a neighbourhood of R_(a,b).
- (e) Localisation: a development on any relatively open past set (e.g. the background on a rectangle) is the maximal
  development there.

Corollaries: cor:civp-axes-cones (the chapter's cone data of prop:loc-cones / lem:loc-cone-in, any size and support,
axes included, with γ̂ smooth on S³ and e^ϕ > 0 on every generator, develop near both cones, unique in the gauge);
cor:civp-axes-perturbations (Corollary P: small non-round perturbations of a round two-dust background develop on every
rectangle in its G, conditional on Tier 3 written about a general such background).

## 2. What is proved in the file (all proofs written out; 14 proofs, 14 end marks)

Block A (chapter 81, after rem:class-leaf-numerics): **lem:class-leaf-reference** (K-ax).
- (o) foliation by the Volterra leaves of a smooth non-solution V: radius r_V and constants from c, lower bounds of
  A3, B3, det₂, C² of g_V, C¹ of (p_V, Θ_V); the difference-quotient bound [1/2, 3/2] (eq:class-leaf-lipschitz) proved
  from the contraction constants of lem:class-volterra; smoothness from step (3) of lem:class-planar-shear and the
  implicit function theorem in C([0, r_V]).
- (a), (b) about V: the proof of lem:class-leaf-differences with five listed changes (leaves h_V, same-axis-point
  differences with the zero-order term −∂_z H_L[V] δh, derivatives in z0 with Jacobian ∂_(z0) h_V ∈ [1/2, 3/2], the shift
  (∂_(z0) σ_V) δz0, balls about V).
- (b′) leaf by leaf, eq:class-leaf-wise: no ball, no extension, constant independent of D; needs C³ of g and C¹ of
  (p_A, Θ_A). Proof: the Volterra difference with the bounds |∂_z G|, |∂_q G| ≤ C_4 r along leaves, the Hardy operator
  𝒜 (norm 1 on L²(r dr)) and two operators with small norm on [0, R], then the shift term via Lipschitz dependence of
  σ on the axis point, then integration over axis points. (GN-T4's mean-value form is replaced by this direct estimate;
  the H² interior estimate is not needed.)
- Placement item 2: the definitional clause (TΣ_L := γ3-orthogonal complement of p_A^Σ) in lem:class-leaf-differences.

Block B (chapter 83, a new section after Tier 3's):
- def:civp-axes-data; eq:civp-axes-raychaudhuri (the cone constraint for ỹ = (μ_γ/μ_γ̊)^(1/3), regular at the axes).
- **lem:civp-axes-principal** (T4-3, natural form): in any chart of S³, the evolution components contain no ∂_u²; the
  ∂_v-principal part, computed by hand from the coordinate formula for Ricci, is block-triangular and invertible
  ((1/(2Ω²)) on γ, −2/Ω on Ω, −(1/(4Ω²))γ on b) at every point, axes included; angular derivatives of the top jet only in
  the b-row; affine in the top jet for j ≥ 2; for the class, affinity at j = 1 and the absence of b-jets in the (Ω, γ)-rows
  from eq:loc-cone-frame-ricci off the axes and continuity (invariant vector fields vanish at the axes). GN-T4's
  frame-normalised determinant −γ_ϑ/(4Ω⁹) is the coordinate form of this; the conical condition and its propagation are
  the smoothness of the tensor jets, so no separate defect equation is needed.
- **lem:civp-axes-jets**: jets at all orders through the axes by linear triangular ODEs along the generators (no
  Riccati term), on the whole edges; corner compatibility (Tier 1's proof, local in ϑ, plus continuity); bounds with the
  loss of 4 derivatives per order; every solution has them.
- **lem:civp-axes-extension**: (a) extension past an end with C^m bound, from the coefficients a_j, b_j of [LY22,
  Theorem 1 (i)] (thm:std-ly-extension, already in Appendix A), the extension property proved in the text; (b) short
  pieces: Taylor polynomial of order m plus the extension of the remainder at the scale a (GN-T4's "rescaled Seeley");
  (c) solving the constraints past an end with positivity for a length ℓ(m, Λ, κ), loss of 3 derivatives; (d) the change
  of angle making b = 0 on N_i.
- **prop:civp-axes-formal**: Borel about X_0(u, v) = a_0(v) + b_0(u) − a_0(0), with |X̂ − X_0| ≤ C_b(|u| + |v|), C_b
  independent of δ_e (no background is available to fall back on away from N).
- **prop:civp-axes-corner** (T4-2): Steps 0–7, constants traced: Λ, κ, l → δ_1 = min(l/3, d/4, δ_2), δ_c = δ_1/32,
  ‖X̂‖_(C^(k+3)), the K-ax constants for Û, ρ, T* of thm:class-kato (a) with reference path 0 in Z := 𝐔 − 𝐔̂, initial slice
  T*/2 before the corner (GN4-2 item 3), σ = δ_c(e^(T*/4) − 1)/2. Two observations remove two of Tier 3's ingredients
  from this proof: the formal metric Ĝ is double-null in the chart's own (u, v), so its leaves in every slice are the
  round spheres |y| = r, and the face sections and the far cuts are Û-leaves (no Lemma A needed for Û); and the residual
  of the axis closure at Û is −E(P̂_A, P̂_A), local and flat on N (no GN3 argument needed). The past region uses the
  extension version about Û with K-ax (b) on annuli of uniform shape; the constraints use K-ax (b′) on the shells of the
  slice triangle (GN4-2 item 6 avoided); the double-null gauge through the axes as in lem:loc-cone-gauge with the
  displacement estimate |Ψ − id| ≤ Cρ·dist(·, N). The timelike character of ∂_τ for Ĝ (Tier 1's "reference metric"
  paragraph) is re-proved on the set 𝒮′, since here b̂ = a_0^b(v) + correction does not vanish off the correction's support.
- **prop:civp-axes-unique** (T4-4), proved in full: reduction to compact rectangles; first disagreement time t* in
  t = u + v; a wave map from g′ to g on a layer, solved as a Cauchy problem from {t = t*} with cut-offs
  (thm:class-kato (a), local forcing); comparison in the wave gauge of g, the non-local term by K-ax (b′) while both ends
  of D_t lie on the cones and by the extension version about the genuine solution g (lem:class-leaf-differences (b))
  otherwise; the coordinates recovered as in lem:loc-cone-unique. **cor:civp-axes-maximal** (D_max).
- **prop:civp-axes-faces** (T4-5) with (C), (E), (J), (U), as GN-T4 §4.1, with the gluing done on D_max ∩ Q′ (so no
  hidden assumption that D_max stops at v_η + η/2), and the ingoing edge by symmetry. **rem:civp-axes-riccati**: the
  model □φ = (∂_uφ)² derived in the text (Riccati, blow-up at v = 4/|w_0|) and □φ = ∂_uφ ∂_vφ (linear); no citation.
- **prop:civp-axes-criterion** (T4-6); **lem:civp-axes-free-data** (cone data from free data through the axes, which is
  what T3-0 would give for the corollary, proved here); thm:civp-axes; the two corollaries; **rem:civp-axes-scope**.

## 3. Pending markers and exactly what each needs

- `[[pending:tier3-section]]` (intro of the section and the Placement): the label of the Tier 3 section; only a
  cross-reference.
- `[[pending:tier3-theorem]]` (thm:civp-axes (c), its proof, rem:civp-axes-scope (i)): the Tier 3 theorem for chapter
  83's background, as GN-T3 §6 plans it: small cone data, axes included, have a class solution in the gauge on Q1 (a
  past set relatively open in the rectangle, smooth through the axes). Used only to say that D_max contains it.
- `[[pending:tier3-theorem-general]]` (cor:civp-axes-perturbations): the Tier 3 theorem written about a general round
  two-dust background g_0 of prop:two-dust-background on a rectangle Q_0 ⊂ G: there is ε_0 > 0 such that cone data within
  ε_0 of g_0's on the edges of Q_0 (in Tier 3's norm, no condition in angle) have a class solution in the gauge on
  Q_0 × S³. If Tier 3 is stated only for chapter 83's background, Corollary P holds only for that background.

No Tier 3 lemma is needed in a proof step of (a)–(e): Lemma A and GN3 are not needed for Û (above), and Lemma R is
replaced by the full proof of prop:civp-axes-unique. Tier 2's own pending markers remain in its texts that my Placement
items 4–7 quote; they are replaced by the Tier 2 wiring round.

## 4. What remains open

- No lower bound for u*, v* in terms of norms (S-T4's N′, T4-6′, not written); an explicit width needs estimates near the
  axes on a strip of fixed width.
- The whole rectangle (not asserted; can fail by focusing).
- Further families (only the two adapted families are treated; rem:civp-axes-scope (iii)).
- Finite regularity, measure-valued densities, no symmetry.
- Not done (optional in S-T4): cor:class-short-time at the axes in chapter 81; the remark on [HL17, p. 1] (the paper is
  not in the bibliography and its text was not re-checked); no change to rem:class-scope.

## 5. Points a reader should check

1. lem:civp-axes-principal (c): the continuity arguments (affinity at j = 1, b-independence) rely on the class
   formulas eq:loc-cone-frame-ricci off the axes and on invariant vector fields vanishing at the axes.
2. lem:class-leaf-reference (a), (b) are written as changes to the proof of lem:class-leaf-differences, which is itself a
   sketch in chapter 81; (o) and (b′) are self-contained.
3. Corner Step 5: the uniform Stein constant for the annuli P ∩ 𝒰 ∩ Σ_τ (bounded by face sections and far cuts, all
   round spheres) for τ ∈ [τ_init, τ_end].
4. prop:civp-axes-unique Step 4 (ii) applies lem:class-leaf-differences in the slicing by t = u + v; its constants depend
   on that slicing (S-T3 R5, GN-T3 R2), which is fixed by the solution g.
5. prop:civp-axes-faces Step 0: K″ (the jets after the change of angle of a piece of {v = const}) is described, not
   computed; it is a polynomial bound in K′.

## 6. Interactions with the Tier 1 and Tier 2 rounds

Labels of P-CIVP and P-CIVP2 are cited as they stand. Names of Tier 1 that my text uses and that its fix round renames:
"ε_0" of lem:loc-cone-borel in the proof of prop:civp-axes-formal (→ ε_B); Tier 1's "η" appears in no text of mine
(my axis partition function is χ_ax, chosen to avoid Tier 1's new ϖ). I also use Tier 1's δ_1, δ_c, δ_e, c_+, 𝒮, 𝒰,
case (II), the "reference metric" paragraph, A^μ_♭, ϒ, r_0, c_0, by name. Placement items 4, 6 and 7 quote Tier 2's new
texts as they stand in P-CIVP2.md (lines 694–695, 720–721, 744); item 5 is a sentence to insert at a described position.

## 7. Check outputs

On a scratch copy (scratchpad/pcivp4/tree: chapters/, crosswalk/, assemble.py, lint.py, OUTLINE.md), with Tier 1's
Blocks A and B, Tier 2's placement (its own apply script) and this file's items 1–7 applied, and the chapter-83 opening
paragraph reflowed after the item-5 insertion:

- `python3 lint.py --chapters`: "chapters: 62 file(s), 4764 label(s) defined, 19 hit(s)", all 19 "pending" (13 lines with Tier 2's
  markers for Tier 1, 6 with Tier 4's markers for Tier 3), no other hit.
- `python3 assemble.py --check`: "labels 4764, computations cited 0, problems 0".
- On the file itself: every line ≤ 121 code points raw and with each reference replaced by a worst case ("Proposition
  83.123", "(83.123)", "Section 83.12.4"); no wrapped line starting with "+ ", "- ", "* ", "> ", "#", "=" or "|"; no
  backslash; labels lowercase; 14 proofs, 14 end marks. `python3 lint.py proofs/P-CIVP4.md` reports, besides the
  pending markers and the chapter labels a single-file run cannot see, only file names in the Placement and Crosswalk
  sections (which are not merged into chapters).
