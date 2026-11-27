# Report P-HF34: the a priori estimate at level four

File: research/warp-drive/paper/reader/proofs/P-HF34.md, md5 b06b3e6ccc316b68679ecaa9ea061242, 535 lines.
Nothing else in the repository was edited; nothing committed. (Note: a coordinator snapshot commit picked up an earlier
draft of P-HF34.md, so git shows it as modified rather than untracked.)

## Level reached, and why

Level N = 4, written as an addition beside sec:tl5-hf (author's decision 2026-11-27), not a replacement.

- Level 3 is not possible for the theorem as the paper uses it: the double-null step needs |D̂²h| at every point
  (C² distance ε of thm:tl5-dn); level-3 face energies put D̂²h in H² of 4-dimensional faces, which does not embed in
  L^∞ (as rem:tl5-hf-level and R-P-HF say). I first designed a level-3 version (mixed norms plus an explicit L⁴(S³)
  inequality by dyadic spherical-harmonic blocks, C₄² ≤ (2+√2)√7/(√6π) < 6/5); it would give existence but not the
  ε-bound, so I dropped it on the coordinator's instruction.
- At N = 4, the pointwise scheme of sec:tl5-hf works for every monomial except two products at |I| = 4:
  D̂Ψ₂·D̂Ψ₂ and Ψ₃·D̂²Ψ₁ (Ψ_B, |B| = 3, from ℒ³H, against D̂²Ψ_Z). They are bounded on the faces by a mixed-norm Hölder
  split, L²_v L^∞_ω against L^∞_v L²_ω, using only lem:tl5-hf-sphere (C_(S³)² = 1/12) and the trace along the face.
  No L⁴ inequality is needed at level 4.
- lem:tl5-hf-linfty holds verbatim at N = 4 (it uses Lemma G only for words of length ≤ N − 1 and the empty word),
  so the low quantities, the smallness 𝔰 and Step 1 of the bootstrap are unchanged in form.

## New results (labels tl5-hf4-…, 22 labels, Section 57.15 in the assembled paper)

- def:tl5-hf4-levels: 𝔰, 𝔧, Λ, 𝔠_n at N = 4; orders of factors; 𝔭_M² (eq:tl5-hf4-pm) =
  Σ_(|B|=|B′|=2)|D̂Ψ_B|²|D̂Ψ_(B′)|² + Σ_(|B|=3, Z)|Ψ_B|²|D̂²Ψ_Z|².
- lem:tl5-hf4-quadratic (Lemma G at level 4): (a) any level: ≥ 2 solution factors, disjoint letters, ≤ 2 derivatives
  D̂ in all, orders sum ≤ |I| + 2, each ≤ |I| + 1; (b) |I| ≤ 4: 𝔑_I = 𝔑^L_I + 𝔑^M_I, |𝔑^L_I| ≤ 𝔠𝔰𝔧,
  |𝔑^M_I| ≤ 𝔠_(|I|)𝔭_M, 𝔑^M_I = 0 for |I| ≤ 3 (eq:tl5-hf4-g).
- lem:tl5-hf4-face (mixed norms on a face, with the value at v = 1/2): for rank r ≤ 4,
  (a) ⟦A⟧²_(∞,2) ≤ [𝔳^(2r)]_t ∫_(S_t)|A|² + 𝔱_r(t)(‖A‖² + ‖D̂A‖²),
  (b) ⟦A⟧²_(2,∞) ≤ (1/2)𝔭_r 𝔵_r(t) Σ_(|J|≤2)‖ℒ^J A‖²,
  (c) ‖f‖ ≤ e^(φ(t,b)/2) 𝔪(t) ⟦X⟧_(2,∞)⟦Y⟧_(∞,2) for |f| ≤ |X||Y|, r_X + r_Y ≤ 6 (eq:tl5-hf4-holder);
  constants: 𝔭_r = 1 + 12r² + 144r⁴, 𝔵_r = [𝔳^(2r)R⁻³]_t, 𝔱_r = [𝔳^(2r)R⁻³max(1 + 2r²|D̂∂_γ|², 2|∂_γ|²)]_t,
  𝔪 = [max(1,𝔴)⁶R^(3/2)]_t, [·]_t = sup over Σ₁(t, v*).
- lem:tl5-hf4-linfty: lem:tl5-hf-linfty at N = 4, plus the pointwise M₂ ≤ 2(k₁+1)𝒥₁ + 2k₂ϱ (eq:tl5-hf4-m2).
- lem:tl5-hf4-mixed: ‖𝔭_M‖_Σ ≤ 2e^(φ(t,b)/2)𝔪(t)𝔵_t𝔶_t(𝔍 + ϱ)(𝔍 + ϱ + η₀), 𝔍 = ‖𝒥₁‖_Σ, with
  λ_t = 2([k₁]_t + 1), ς_t = 2[k₂]_t|Σ₁(t,v*)|^(1/2),
  𝔵_t = max((𝔭₃𝔵₃(1 + 64680[Λ]²))^(1/2), (𝔭₄𝔵₄/2)^(1/2)(√602 λ_t + 789[Λ]²), (𝔭₄𝔵₄/2)^(1/2)√602 ς_t),
  𝔶_t = max(𝔱₃^(1/2)(1 + 7λ_t), 7𝔱₃^(1/2)ς_t, 𝔱₂^(1/2), π(98[𝔳⁶]_t)^(1/2), π(686[𝔳⁴]_t)^(1/2)).
- def:tl5-hf4-constants, prop:tl5-hf4-bootstrap, lem:tl5-hf4-persistence, thm:tl5-hf4, rem:tl5-hf4-level.

## The closing condition and S_F at level 4

    m_t := 98 e^(φ(t,v*)/2) [2Ω̂²(1 + c/κ′)^(1/2)]_t [𝔠₄]_t 𝔪(t) 𝔵_t 𝔶_t,
    S_M := μ⁻² ∫ m_t [𝔨₂]_t dt,   𝔯_M := ∫ m_t [𝔨₂]_t^(1/2)(2ϱ + η₀) dt,   ε_M := μ²ϱ(ϱ + η₀)∫ m_t dt,
    S_(F,4) = S_F + S_M,   𝔯_(w,4) = 𝔯_w + 𝔯_M,   ε_(w,4) = ε_w + ε_M,   A_(w,4) = √2δ_w + 2ε_(w,4),   B_(w,4) = 2S_(F,4),
    closing (eq:tl5-hf4-closing):  8 (√2 δ_w + 2ε_w + 2ε_M)(S_F + S_M) < 1,

δ_w, ε_w, S_F, 𝔯_w, 𝔰₀, 𝔰₁, 𝔰_* by the formulas of def:tl5-hf-constants at N = 4 (𝔰_* with A_(w,4)). Smallness:
𝔯_(w,4) ≤ 1/4, η₀ < 𝔰₁, 𝔰_* < 𝔰₁. Hypothesis (a) is in the merged M1 form: η₀ < 𝔰₁, η₀ from derivatives of
G^♯ − ĝ of order ≤ 4 on N₀; the N₀ fluxes are in δ_w; rem:tl5-hf4-level states (citing lem:tl5-xt-order (c) with
m = 5 and lem:tl5-xt-seed-jets) that η₀ and the N₀ fluxes vanish when ĝ − g′ vanishes to order 5 on N₀⁺, so the
background must carry g′'s v-jets of orders 4 and 5 (N-APP1's κ = 6), and a seed-jet background does not satisfy this
sufficient condition.

## Comparison with level 6 (also in the file's non-chapter section)

- μ powers (the file keeps sec:tl5-hf's bookkeeping, every level bounded by the top one): S_F leading μ^(−N):
  μ⁻⁶ vs μ⁻⁴ (10^24 vs 10^16 at μ = 10⁻⁴, computed); part without 𝔤_N μ⁻³ vs μ⁻²; S_M μ⁻² (level 4 only); 𝔰_* data
  term μ⁻³ vs μ⁻². NB: G0b's level-3 scoping priced μ^(−3/2); with this bookkeeping level 4 costs μ⁻⁴. Deduced but not
  written: for every monomial of level n the two norms need levels ℓ₁ + ℓ₂ ≤ n + 3, so a graded count would give
  μ^(−3/2) at any level; it needs graded versions of lem:tl5-hf-linfty and Step 2 (not done).
- 𝔅_N: 28×28 vs 20×20; coupling level pairs 28 vs 15; jets of ĝ and Γ to order N + 3 = 9 vs 7; 𝔏-iterates with
  ≤ N − 1 = 5 vs 3 Lie derivatives; Λ for |B| ≤ N.
- Words ≤ N: 137,257 vs 2,801; length N: 117,649 vs 2,401; 𝔐 = Σ_(j≤N−3)7^j: 400 vs 8; F_N: 4,683 vs 75;
  𝔠_N at Λ = 1: 9.75e10 vs 4.44e7; Λ = 3: 8.54e12 vs 9.64e8 (computed, floating point).
- Data: δ_w needs derivatives of G^♯ − ĝ of order ≤ N + 1 (7 vs 5; 𝔟 terms); η₀ order ≤ N (6 vs 4).
- Jets carried on N₀⁺: orders 4–7 (κ = 8) vs 4–5 (κ = 6).
- Residual: s_N uses ℒ^J(2R̂ic), |J| ≤ N (6 vs 4); ϱ uses |J| ≤ N − 1 (5 vs 3).
- Level-4-only numerical constants (computed): 𝔭₃ = 11,773, 𝔭₄ = 37,057, 64,680, √602 ≈ 24.5, 789, π√98 ≈ 31.1,
  π√686 ≈ 82.3 (crude monomial counts; they enter S_M, 𝔯_M, ε_M linearly).

## Placement (against chapters/87-ten-l5.md at HEAD f99f4a13, unchanged at 60527421)

1. Insert the section after rem:tl5-hf-level (line 4609, end of the chapter).
2. rem:tl5-hf-level: append one sentence pointing to sec:tl5-hf4 (old/new pair quoted from HEAD).
3. Nothing else changes. Crosswalk: 22 rows (PENDING line numbers of the file) and one note for rem:tl5-hf-level.

## Checks (scratch tree /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/phf34/tree)

Built by git archive of HEAD plus P-HF34's items 1–3 (tools/merge34.py in the scratchpad; P-HF and P-XT are already
merged at HEAD).

- lint.py --chapters: "chapters: 62 file(s), 5085 label(s) defined, 0 hit(s)" (HEAD alone: 5063; +22).
- assemble.py --check: "labels 5085, computations cited 0, problems 0".
- in-memory check: "[] 0".
- No chapter-text line over 121 characters; no wrapped line starts with a Markdown marker. The crosswalk rows (TSV) are
  longer than 121, as in P-HF.

## Points for the reader

- Proofs that cite sec:tl5-hf steps "with replacements" (Step 1, 2, 3 of prop:tl5-hf-bootstrap; the proof of
  lem:tl5-hf-linfty; the proof of thm:tl5-hf; the last paragraph of lem:tl5-hf-persistence): check that nothing in
  those texts uses N ≥ 5 beyond what is named.
- Persistence (lem:tl5-hf4-persistence) is a full face-norm induction from m = 5: mixed products occur only for
  m ≤ 6; in each, at most one of the two norms involves level-(m+1) quantities; recovery at level m − 1 uses only known
  quantities; constant rates A + Ã absorb the linear-in-energy terms; N₀ fluxes and traces are data (M2 respected).
- The constants are crude (monomial counts, max over words); they are explicit.
