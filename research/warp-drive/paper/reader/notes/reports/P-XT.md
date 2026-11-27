# P-XT report: (X) and (T) of thm:tl5-wg-data at the first stage (data item L1)

File: research/warp-drive/paper/reader/proofs/P-XT.md (525 lines; md5 a9e3d28426e8bd4103ac04fcd94789b2). New subsection
sec:tl5-xt, 21 labels, placement after cor:tl5-wg-data-first-stage (87:2757) and before sec:tl5-dn (87:2759) at HEAD
edafc288; 21 crosswalk rows at @PENDING:N. Nothing committed; no other file edited.

## Results (all proved in the text, every number a written chain of outward-rounded arithmetic)

- **lem:tl5-xt-implies: (T) implies (X)** for every background (uses κ_m ≤ 1/4 and lem:tl5-wg-norms (b)). So only (T)
  needs checking.
- **N₀⁺ (item 2 of the review), written in full.** lem:tl5-xt-seed-jets (a): the development has the seed's partial
  derivatives of order ≤ 3 on N₀⁺ (lem:tl5-cip-jets (a), m = 3; data C³ across S). lem:tl5-xt-order: if ĝ − g′ vanishes to
  order m ≥ 1 on N₀⁺, then Υ(g′) vanishes to order m − 1, Ψ − id to order m, **G^♯ − ĝ to order m − 1**, Y₀ = ξ₀ = 0,
  ξ = 0, G^♯ = g_N on N₀⁺, and (X), (T) hold on N₀⁺ for every κ_m. So **Y₀ = 0, ξ₀ = 0** for every background with the
  seed's 1-jet on N₀⁺.
- **The level change (coordinator's question).** (X) and (T) involve only 1-jets; the level N changes nothing in them.
  But thm:tl5-hf (a) (G^♯ − ĝ to order N + 1 on N₀) needs ĝ − g′ to order N + 2 on N₀⁺ (lem:tl5-xt-order), and
  lem:tl5-xt-seed-jets (b) proves the development's fourth v-derivatives of the leaf metric on N₀⁺ are NOT the seed's
  (δ∂_v⁴γ_φ1φ1 = (4λπ⁴/81) r_s^(1/2)(1 + x)h(x)(2(1 + x)cos(1/(2λ)) − (1 − x)sin(1/(2λ))) at S, propagated by a linear
  homogeneous ODE), off at most one torus. Hence any "seed + (v − ½)^κ G" background gives ĝ − g′ to order exactly 3 and
  G^♯ − ĝ to order 2 (higher not shown). Agrees with N-APP1 finding (2). Ways out: carry the development's v-jets of
  orders 4..N+2 on N₀⁺ (linear transport with seed coefficients, initial values the data's one-sided v-derivatives at S),
  or give the estimate a data term on N₀.
- **N₁, exact structure (lem:tl5-xt-gauge (b)).** If ĝ = g_N at the points of N₁ (values), then on N₁
  Υ(g′) = (3e^(−2W)/(2R)) ∂_u(R′ − R̂) ∂_v and e^(2W)|Υ| = (3e^W/(√2 R))|∂_u(R′ − R̂)|: **only the transverse derivative of R
  enters**; the other transverse derivatives (W, b, traceless γ) do not.
- **The development's ∂_uR on N₁ in closed form (lem:tl5-xt-rho).** From the trace of Ric(∂_A, ∂_B) = 0:
  ∂_v(R²∂_uR) = (R³/3)e^(2W)(2Δ̸W + 2|dW|² + 2|ζ|² − R̸) − (R³/6)(∂_v div b + 3b(∂_vR/R) + 6(∂_vR/R) div b) for every
  vacuum double-null metric; on N₁ this is a quadrature of the data:
  ρ = R⁻²(−r_s² f(r_s)/f(10) + ∫_(1/2)^v 𝒢 dv′), 𝒢 explicit (R̸ written out in ϰ₁, ϰ₂, ϰ₃). Checked on the seed.
- **K₁ (lem:tl5-xt-k1, with lem:tl5-xt-rx for ∂_xR, ∂_x∂_rR).** For any background equal to the data on N₁, every
  v* ≤ 7/2: K₁ = max(√2((∂_vW)² + e^(2W)|ζ|²)^(1/2) + (3/2)∂_vR/R) ≤ **0.1038 (seed 1), 0.09194 (seed 2)**. Pieces:
  (3/2)∂_vR/R ≤ 0.072657; ∂_vW ≤ 4.6464×10⁻⁴; shift 1-form |ζ|_γ ≤ 0.03106 / 0.01924 (via the shift constraint,
  |𝔣| ≤ 0.05251 / 0.03275); |∂_xR| ≤ 0.025895 / 0.011112, |∂_x∂_rR| ≤ 0.034817 / 0.014940. e^(3K₁) ≤ 1.3654 / 1.3177.
  General formula for any background: K₁ = max(√2((∂_vŴ)² + Ω̂²|dŴ + ζ̂|²)^(1/2) + (3/2)∂_vR/R) (only values and
  tangential derivatives of ĝ on N₁).
- **thm:tl5-xt (conditions as functions of κ_m).** ĝ with the seed's 1-jet on N₀⁺:
  (b) ĝ = data on N₁, ε_R := max|∂_uR̂ − ρ|: Y₁ ≤ 3e₊ε_R/(√2 r_s) (= 0.14657 ε_R), ξ₁ ≤ Y₁(v* − ½)e^(K₁(v* − ½)), and (T)
  holds iff-sufficient 3(e₊/e₋)(v* − ½)e^(𝔎(v* − ½))ε_R < r_s κ_m; **at v* = 7/2: ε_R ≤ 0.8329 κ_m (seed 1),
  ε_R ≤ 0.8630 κ_m (seed 2)**; smaller v* is easier (monotone). e₋ ≥ 0.707277, e₊/e₋ ≤ 1.001142.
  (c) General ĝ with ε₀ := max_N₁|g_N − ĝ|, ε₁ := max_N₁|D̂(g′ − ĝ)| (k̂ norms): (T) holds if
  **2ε₀ + 4.996 (v* − ½) e^(K̄₁(v* − ½)) ε₁ < κ_m**; at v* = 7/2 and K̄₁ ≤ 0.11: 2ε₀ + 20.9 ε₁ < κ_m. In P-HF's E₀-norm
  (lem:tl5-hf-khat, c(−10) = 0.495): ε₀ ≤ ε₀′/0.495, ε₁ ≤ ε₁′/0.3482. Linear in κ_m; N₀⁺ does not enter.
- **The constructed background ĝ_♮ (def/lem:tl5-xt-natural), for u* < −1.** Fields Ŵ := W_s, b̂ := χ(u)E b_N,
  γ̂ := γ_s + χ(u)(E(γ_N − γ_s(−10,·)) + (u + 10)E(λγ_N)), λ := 2ρ/R − (2ρ_s/(3r))tr_(γ_N)γ_s(−10,·), χ a cut-off to
  |u + 10| < η₁, E Seeley's extension in v. It is a G-invariant double-null background on a set ⊃ D̄ ∪ N⁺, equal to the
  seed off the strip, with the seed's 3-jet on N₀⁺ (needs λ, D, b_N to vanish to order 3 at v = ½: proved), equal to the
  data on N₁ with ∂_uR̂ = ρ. **cor:tl5-xt-data: Y₀ = Y₁ = ξ₀ = ξ₁ = 0, (X) and (T) hold for both seeds, every
  u* ∈ (−10, −1), u⁺ ∈ (u*, u₀), v* ∈ (½, 7/2] and every κ, κ′**; margins: (X) left side 0 against √2 min Ω̂ ≥ 1.0002,
  (T) left side 0 against κ_m. G^♯ = g_N on all of N⁺, G^♯ − ĝ_♮ to order 2 on N₀⁺. So cor:tl5-wg-data-first-stage and
  thm:tl5-wg hold unconditionally for this background.
- **The seed as background fails (prop:tl5-xt-seed).** |g_N⁻¹ − ĝ_seed⁻¹| ≥ 0.01967 at (v, x) = (9/4, 1), seed 1
  (v* ≥ 9/4), and ≥ 0.01100 at (2, 1), seed 2 (v* ≥ 2); so (T) fails for κ_m ≤ 0.01967 / 0.01100 — by a factor ≥ 197 /
  110 at κ_m = 10⁻⁴. (Value term only; for larger κ_m undecided.)

## What is not proved / not done
- ĝ_♮ serves the local theory only: its Ricci tensor in the strip is not small, so it is not the background of the a
  priori estimate (rem:tl5-xt-background). For the certified approximant, (X), (T) reduce to thm:tl5-xt (b) or (c) on N₁,
  but its ε_R or ε₀, ε₁ and K̄₁ need its printed fields and the development's 1-jet on N₁ (ρ for R; the transport of
  lem:tl5-cip-jets (b) for the rest when (c) is used) enclosed — an L1 item; no coefficients exist yet. The targets
  (ε ≈ κ_m) are far above the closing's data-error targets.
- ρ itself is not enclosed numerically (not needed for ĝ_♮). Whether the simplest data-matching choice ∂_uR̂ = seed's
  ∂_uR meets ε_R ≤ 0.83 κ_m is not decided.
- No background with ĝ − g′ to order N + 2 on N₀⁺ is constructed (finding above).
- The argument uses the merged text of thm:tl5-wg-data with the gluing fix (g′ = development on 𝒩_δ ∩ 𝒰).

## Checks
- Scratch copy (chapters + crosswalk at HEAD edafc288, placement items 1–3 applied, 21 rows added after
  cor:tl5-wg-data-first-stage in crosswalk/87-ten-l5.tsv): `python3 lint.py --chapters` → 62 files, 4949 labels, 0 hits;
  `python3 assemble.py --check` → labels 4949, problems 0. Text part: lines ≤ 121, no wrapped line starting with a
  marker, no lint hit (hits only in Placement/crosswalk: file names, quoted 4-space-indented old texts).
- Arithmetic re-run with outward interval enclosures (scratch, pxt/chain2.py, xt_numbers.py, seedlb.py); every printed
  bound dominates.

---

# Fix round (review R-P-XT, NOT CONFIRMED on a9e3d284)

New file: proofs/P-XT.md, 535 lines, **md5 5fa426c0e7a53e4f7787090732711b2f** (the snapshot 6bf3f7d7 holds an
intermediate 22e141d6 that differs from it in one Placement line, the HEAD reference).

Applied: the reader's apply.py verbatim (M1, m1–m4, n1–n7; its output P-XT.reviewed.md c5cf16af) plus:
- n8: "K₀ being that of [[thm:tl5-wg-data]]" in the proof of lem:tl5-xt-order (a).
- the opening paragraph rewrapped (the patch left "possible." alone on a line); no word changed.
- N1 (report): Y₁ ≤ 0.14658 ε_R (3e₊/(√2 r_s) = 0.1465786, not 0.14657).
- N2: Placement 6 (i) now states exactly what lem:tl5-xt-seed-jets (b) shows (the development's fourth v-derivatives of
  the leaf metric on N₀⁺ are not the seed's, off one torus); "seed + (v − ½)⁵ G" gives ĝ − g′ to order 3 exactly and
  G^♯ − ĝ to order 2; for "seed + (v − ½)⁴ G" order 4 holds exactly when G(·, ½) equals the difference of the fourth
  derivatives over 4!; the jets route is sufficient, necessity not shown. 6 (ii) phrased as sufficiency.
- N3: item 5 cites lem:tl5-cip-form (a) only; HEAD reference updated to 6bf3f7d7 (chapter lines 1–2760 identical to
  edafc288; anchors 2151–2153, 2500, 2757/2759 unchanged; P-HF's sec:tl5-hf, now merged at the end, is not touched).
- N4: crosswalk notes: sec:tl5-xt and cor:tl5-xt-data say u* < −1; thm:tl5-xt says ≤ and "(sufficient)".
- All 21 @PENDING:N re-pinned (now 1, 22, 27, 41, 78, 122, 133, 174, 191, 219, 241, 244, 289, 298, 306, 333, 346, 348,
  390, 401, 425); all checked against the label lines.

Delta in the chapter text (vs a9e3d284): opening and the two one-sentence edits restricted to u* < −1 and to
backgrounds with the seed's 1-jet on N₀⁺, with "follow from" (M1); lem:tl5-xt-rx second-seed chain 0.0111012/0.999054
and 1.271898 × 10⁻³ × 11.746212, citation to the proof of cor:cone-compare (m1, n4); rem:tl5-xt-background says only
what is proved, restores v* ≥ 9/4 and v* ≥ 2, sufficiency wording (m2); lem:tl5-xt-gauge (a) justifies (1/2)|trχ| =
(3/2)∂_vR/R by ∂_vR = (f/2)∂_rR > 0 (m3); "the proof of [[lem:tl5-seed]] (d)" for R_s(−10, v) = r and W_s(−10, v) = W
(m4); n1 (G^♯ = g_N on N₀⁺ by (a)), n2 (thm:tl5-wg applies: g_N smooth data, ĝ_♮ a background), n3 (the coefficient
3e^(−2W)/(2R)), n5 (Cauchy–Schwarz for |P + Q| ≤ 2φ/3), n6 (K̄₁ = K₁ itself), n7 ("the departure they admit"), n8.
No number, statement or proof changed in substance.

Checks (scratch copy of chapters + crosswalk at HEAD 6bf3f7d7, items 1–3 applied, 21 rows added after
cor:tl5-wg-data-first-stage): lint.py --chapters → 62 files, 5061 labels, 0 hits; assemble.py --check → labels 5061,
problems 0; in that scratch copy only, a full assemble shows every line of the subsection ≤ 121 after the labels
resolve and no unresolved reference. Source lines ≤ 121 (except the 4-space-indented quotes and crosswalk rows), no
wrapped line starts with a marker.
