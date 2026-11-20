# P-HF report: L3–L5, the weighted bootstrap, and lem:tl5-continuation restated

File: research/warp-drive/paper/reader/proofs/P-HF.md (section sec:tl5-hf, 84 labels; Placement items 1–7; 84 crosswalk
rows). Nothing committed; no chapter or crosswalk file edited.

## What is proved (chapter text, every proof closed)
- L3 (level 0): current J = −𝕋(T,·) + |Ψ|²𝒵, divergence identity with the tensor commutator term
  (lem:tl5-hf-divergence); weighted identity on tilted corner regions Q(a,b) = {τ₁≤a, τ₂≤b}, no axis boundary, face
  densities ε₁ = (e_o+κ′e_i)/(1−κκ′), ε₂ = (e_i+κe_o)/(1−κκ′) (lem:tl5-hf-identity); bulk matrix 𝔅 = exact block norms
  of the bulk form (lem:tl5-hf-pointwise, rem:tl5-hf-blocks lists the blocks); admissibility = pointwise copositivity,
  monotone in the tilt (def:tl5-hf-rates); explicit rates from a measurable allocation θ and Young parameters t
  (lem:tl5-hf-allocation); weighted estimate Y ≤ Y_d + 2𝒮, F² = 2e^(Φ_o+Φ_i) (prop:tl5-hf-linear).
- L4 (level N, general): Γ = {T, six rotations}; null structure π^Z(ê₄,ê₄)=π^Z(ê₃,ê₃)=0, π^K(ê₄,leaf)=0 (checked
  privately with sympy); exact commutator L̂ℒ_Z = ℒ_Z L̂ − 𝒦[π^Z] with 𝒦 written out (lem:tl5-hf-commutator); exact
  commuted equation with all lower-level terms (lem:tl5-hf-system) — G0b's "non-adjacent terms, 50 % margin" is replaced
  by exact maps; recovery with explicit constant (lem:tl5-hf-recovery); couplings ℭ, 𝔮 as operator norms of explicit maps
  and the level-N matrix 𝔅_N (def:tl5-hf-coupling, eq:tl5-hf-bn); prop:tl5-hf-linear-n.
- Sobolev: H²→L^∞ on S³, C_(S³)² = Σ(n+1)²/(2π²(1+n(n+2))²); trace along the tilted faces (lem:tl5-hf-sobolev, C_S
  in eq:tl5-hf-cs, rank r in eq:tl5-hf-cs-r).
- L5: exact expansion −2Ric^W(ĝ+h) = −2R̂ic + L̂h + N(h) with 𝔠 and 𝔮 written out (lem:tl5-hf-reduced); Lemma G
  |ℒ^I N − H·D̂²Ψ_I| ≤ 𝔠_|I| 𝔰 𝔧 with the explicit majorant 𝔠_n of eq:tl5-hf-cn (Fubini numbers, β₁, β₂, b_g, b_H,
  𝔤₀ = √5+1/4, Λ); pointwise bounds of the low quantities (lem:tl5-hf-linfty, C_∞, C_(∞,ϱ), k₁, k₂, k₃ explicit);
  quasilinear term by an integrated current, θ_H explicit (lem:tl5-hf-quasilinear).
- Bootstrap (G0 §8.2 form): (H1) Y ≤ A_w + B_w Y², A_w = √2δ_w + 4ε_w, B_w = 2S_F, closing 8(√2δ_w+4ε_w)S_F < 1,
  linear in F through e^(φ/2) in S_F (prop:tl5-hf-bootstrap); shared faces cost nothing (one region, one identity);
  Sobolev local (only the past corner of p). (H2) qualitative (lem:tl5-hf-persistence). thm:tl5-hf: existence on D^κ,
  vacuum, |h|_k̂ < κ_m/2, ε ≤ ε_𝔰 𝔰_*, and double-null form via thm:tl5-dn.
- Conversions asked for: |A|_k̂ ≤ c^(−r/2)|A| (lem:tl5-hf-khat); strict tilt from 𝔰 < c_* κ_m/2, c_* = f(−u*)/2;
  slice distance ε ≤ ε_𝔰 sup max(|h|,|D̂h|,|D̂²h|), ε_𝔰 = sup max(ν², ν³+2νΓ̂_s, ν⁴+5ν²Γ̂_s+2νΓ̂′_s+2Γ̂_s²)
  (lem:tl5-hf-conversions).
- Restated lem:tl5-continuation (items 3–6): tilted D^κ_s, reduced-problem solutions, (H1)/(H2)/(H4) only below 2A,
  (H4) the strict tilt for (F3_W); proof cites thm:tl5-wg. Item 2 (sec:tl5-beyond opening) and item 7 (rem:tl5-beyond)
  keep the chapter consistent. ch:scope line 249 still describes the old lemma; not edited (coordinator's call).

## Findings that change the plan
1. **Level.** G0's C_S claims |∇²h|_∞ from level-3 cone fluxes; I could not establish it. On a ĝ-null cone the
   transversal derivative of the top level is uncontrolled, and the commutator contains π^T(ê₄,f)≠0 (twist) and the
   orbit–leaf block of π^K; the quasilinear H^uu term blocks the null trick. With tilted faces and the S³ Sobolev, a
   level-N norm bounds Ψ_(≤N−2), D̂Ψ_(≤N−3), D̂²Ψ_(≤N−4) at a point; products need N ≥ 5 (Lemma G), persistence N ≥ 6.
   The theorem is stated for N ≥ 6. G0/G0b numbers (level 3) do not apply; L7 must evaluate at the chosen N. Level 3–4
   would need Gagliardo–Nirenberg/L⁴ product estimates with explicit constants (G0b lever (i)); not written.
2. **Hypothesis (a) of thm:tl5-hf:** G^♯ − ĝ vanishes to order N+1 on N₀ (so every Ψ_I and H vanish there). L1/L6
   must build ĝ this way.
3. thm:tl5-wg-data's (X) and (T) (and W4) are hypotheses about the background on N⁺; I did not verify them for the
   seeds — they need a separate verification once ĝ is fixed (same for thm:tl5-dn's hypotheses).

## Pending markers
None in the file. Assumed from P-H29 (cited as labels): def:tl5-wg-background, eq:tl5-wg-khat, def:tl5-wg-gauge/
eq:tl5-wg-def, eq:tl5-wg-reduced, lem:tl5-wg-linear (eq:tl5-wg-lin), def:tl5-wg-domains, eq:tl5-wg-tilted,
lem:tl5-wg-norms, lem:tl5-wg-domains, def:tl5-wg-data, def:tl5-wg-solution, prop:tl5-wg-vacuum, thm:tl5-wg,
rem:tl5-wg-continuation, thm:tl5-wg-data, cor:tl5-wg-data-first-stage, def:tl5-dn-slice, eq:tl5-dn-eps, thm:tl5-dn,
sec:tl5-wg. From chapter 87: lem:tl5-cip-form, def:tl5-cip-development, eq:tl5-cip-constraints, thm:tl5-cip,
cor:tl5-cip-staged, lem:tl5-seed, lem:tl5-connection, eq:tl5-radii, sec:cone-constraint, def:tl5-problem,
sec:tl5-residuals, eq:tl5-region; ch:setting lem:warped-ricci.

## What L7 must certify (enclosures, no new mathematics)
Rates: (1−ϑ)⁻¹𝔅_N-admissibility of a_o, a_i on boxes (LDLᵀ/Gershgorin on interval entries, φ-boxes for the
non-T²-invariant norms — G0b's "sup over φ from two phases" must become box enclosures); the block norms 𝔟, the
coupling norms ℭ, 𝔮 (exact maps from the 3-jet up to order N+3), Λ, K_rec, λ_M, 𝔡, ‖𝒞‖, ‖𝓡̂‖; C_S, C₁, C_∞,
C_(∞,ϱ), k₁–k₃, 𝔠_n, 𝔤_N, 𝔞_o, 𝔞_i, S_F, 𝔯_w, 𝔰₀, 𝔰_θ, 𝔰₁, 𝔰_*, ε_𝔰; δ_w (L1), ε_w and ϱ (L6). No floating-point
number from the gates appears in the file.

## Checks (scratch copy with P-H29's sections and this placement applied)
- python3 lint.py --chapters: "chapters: 62 file(s), 4968 label(s) defined, 0 hit(s)".
- python3 assemble.py --check: "labels 4968, computations cited 0, problems 0".
