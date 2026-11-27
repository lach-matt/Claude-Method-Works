# R-I2: confirming reading of the I-2 integration round

Reader R-I2. Scope: every hunk of scratch/i2/i2.diff (base 92bc9519: chapters 06, 07, 09, 10, 20, 24, 27, 30, 35, 46,
48, 65, 81, 87, 95 and crosswalk/95), and the two R-I1b fixes of commit 9cbb2b5c (46:1728, 46:1769, 36:1622). Read
first: READER-BRIEF.md, STYLE.md, OUTLINE.md (notation), WRITER-BRIEF(-S).md, notes/reports/I-2.md, R-I1a.md, R-I1b.md,
R4-83.md and R-96.md.

## Method

- The working tree is clean in chapters/ and crosswalk/. The +/− lines of `git diff 92bc9519 HEAD -- chapters crosswalk`
  are identical to those of i2.diff (rechecked at HEAD 03332727; the later snapshots touch proofs/ only). Commit
  9cbb2b5c, which carries the R-I1b fixes, is an ancestor of 92bc9519, so those three sites were read in place.
- Verbatim texts were checked on the whitespace-split word sequence against the reviewer's fenced text (N3, N4, R4-83's
  sentence). Renames were checked by mapping the new letter back in the new file and comparing with the base file.
- Line lengths were counted in code points, as lint.py does. The source of the new Appendix A entry was read in
  arXiv:2408.06651v1, pp. 6, 27–40 (alphaXiv full-page text).

## 1. R-I1a nits N1–N6

- **N1, 09:46.** Applied: "< 0 wherever r > 0". True: g0⁻¹(dτ, dτ) = −1 − μ/r² with μ ≥ μ0 > 0, so it is ≤ −1 wherever
  g0 is defined, which matches (a) "each Σ̂_τ", Σ̂_τ being the whole level set (09:23).
- **N2, 10:172.** Applied: "τ' ≤ τ", now the ASCII apostrophe of 10:178, 191, 193, 236 and 237.
- **N3, 24:1666–1667.** R-I1a's text verbatim. True: the displayed bounds give sup t_*^(ℓ_K)|∂^αφ̃^(u/s)| ≤ Cϵ, so
  ϵ₂ := 1/C works.
- **N4, 06:329–337.** R-I1a's paragraph verbatim (word sequence identical). True in place: the bounds of (i) are
  δ/2 ≤ γ ≤ Θ with δ the Euclidean metric, ν ≥ ν_min = (2Θ⁴)^(−1/2) (06:316), and the convex interpolation to (1, 0, δ)
  keeps both. So c_0 and ε2 depend on Θ and, through y, on DΦ_Z and its inverse. Those are uniform in λ by Gronwall,
  since |∂β_ext| ≤ C follows from |∂g_app| ≤ C (06:75, 413–414).
- **N5.** Chapter 27: 27 occurrences of R_(ℐ⁺, on 22 lines (base: 27 of R_(I⁺, and 0 of R_(ℐ⁺,). Chapter 35: 1 (35:900).
  No Latin I⁺ and no "R_(I" is left in any chapter. Line lengths are unchanged.
- **N6.** 30: 3 sites (1227, 1483), no 𝓗 left. 95: 4 sites, all in thm:std-analytic-fredholm, no 𝓗 left. All of them
  are generic Hilbert spaces: "for any Hilbert space ℋ" (30:1227), the value space of (M1) (30:1483), and the space of
  [RS1, Theorem VI.14]. No clash with the horizon: neither chapter writes ℋ⁺ or ϑ_ℋ. In 30, ℋ also names ℋ_l and ℋ_d
  (harmonic polynomials, 154–516) and ℋ(H) (the set of hypersurfaces meeting H, 1162–1165). These always carry a
  subscript or an argument, and none occurs in the same result as the bare ℋ: 1162 is the paragraph (5) before
  lem:iii-a-1-1, and 1227 is in the proof of lem:iii-a-1-2. In 95, ℋ occurs nowhere else. Chapter 22 (127) and
  chapter 36 (653) write a Hilbert space ℋ in the same way. The 30:1483 site is undeclared: see nit 5. Chapter 25 still
  writes 𝓗, which is the deferred item for its worker.

## 2. 07:230 and 07:264

I redid the derivation of the proof of (a), J (07:264–293) for a general Riemannian γ and any α with 1 + αγ^(rr) > 0:

- Π_A^k = δ_A^k, because ∂_A r = 0.
- Π^(rk) = 0, and q(γ⁻¹dr) = 0 by the choice of q_r.
- γ_U⁻¹dr = (1 + αγ^(rr))⁻¹γ⁻¹dr, tr_(γ_U)Π = 3 and tr_(γ_U)(q ⊗ dr + dr ⊗ q) = 0.
- The principal part of J_i follows, and so do the contractions with γ⁻¹dr and the angular rows.

The result is 𝒮A0 = diag(6, γ_U^(rr)Π^(AB)) and the displayed 𝒮A^C, whose off-diagonal blocks −2Π^(CB), −2Π^(AC)
are transposes and whose diagonal blocks are symmetric. No step uses γ_rA small. Smallness enters only the last
sentence, where the one-dimensionality persists under small changes. Further:

- 𝒮 = [[1, γ^(rB)/γ^(rr)], [0, −½Π^(AB)]] is block upper triangular. Its diagonal blocks are 1 and −½Π^(AB), and
  Π^(AB) is the inverse of the induced metric of the spheres, so 𝒮 is invertible.
- γ_U^(rr) = γ^(rr)/(1 + αγ^(rr)) > 0, so 𝒮A0 > 0.

Both new sentences are true. The invertibility clause is needed: lem:linear-evolution (07:349–351) asks for "an
invertible symmetrizer 𝒮 with 𝒮A0 ≥ A00 > 0 and 𝒮A^B symmetric", and the uniform A00 follows from pointwise
positivity, continuity and compactness. The texts agree with lem:vlasov-symmetrizer (82:764–776): same hypotheses, same
conclusions, the same block-triangular argument, and "the smallness … enters only the uniqueness of the symmetrizer,
which [[lem:linear-evolution]] does not use".

## 3. 81:1661, 81:1022, 87:352

- **81:1660–1663.** R4-83's accepted text verbatim, after "with" at 81:1660. It is grammatical in place.
- **81:1022.** Both claims of the parenthesis are true. lem:vlasov-symmetrizer holds for every Riemannian γ on Σ and
  every α with 1 + αγ^(rr) > 0 (82:764–766). prop:vlasov-scaled-correction gives η and C "depending on k, b1 − a, η0,
  p0, δ_e, A00 and the class bounds, and not on λ" (82:894–897). On how the parenthesis reads against its clause, see
  nit 2.
- **87:351–353.** R-96 nit 3 verbatim. The checkpoints are printed with those tables (96:2661 and 96:2697, after
  sec:cone-table-n1 at 96:2639 and sec:cone-table-n2 at 96:2667).

## 4. 𝒦 → 𝔒 in 46, 48, 65

- 46: base 114 𝒦 on 82 lines, now 0 𝒦 and 114 𝔒 on 82 lines. 48: 18 on 13 lines. 65: 7 on 5 lines.
- In each chapter, mapping 𝔒 back to 𝒦 in the new file reproduces the base file byte for byte. So the hunks change
  nothing else, and there is no rewrap.
- Every base occurrence is 𝒦, 𝒦⁺, 𝒦⁻ or 𝒦′, with no subscript. I read every bare 𝒦 in context. All are lem:s27-cover's
  compact part, its parts 𝔒^± ((e)), or sec:s27-local's 𝒦′, which 48:196 sets to 𝒦⁻. None is a Kretschmann scalar:
  46, 48 and 65 had none.
- 𝔒 occurs in no other chapter. No other chapter cites the cover's compact part (grep of s27-cover, s27-local and
  "compact part"). The remaining 𝒦 elsewhere are the Kretschmann scalar and unrelated objects: 47's kernel 𝒦₀ of [CD03],
  39's compact set 𝒦_0, 95:336's quoted ∂𝒦⁺. So the rename is complete and one family.
- R_K keeps its name and is defined at use (46:647, "the largest value of r on the compact set 𝔒"). No finding.

## 5. 24:957, 979, 981

lem:ii-a-2-5 (23:207–220) holds on a neighbourhood U of ℐ⁺. In the region of the lemma, {x_I < c} lies in U for c small,
so c_V is fixed by that lemma alone. It does not involve ρ_a. The order of choices is then:

1. c_V.
2. The frame bounds on {x_I < c_V}, hence C₁ and C₂, which may depend on c_V.
3. ρ_a < c_V² and ϵ_a, small depending on ℓ and C₂.
4. The gluing constant C, with 2/C ≤ ρ_a (24:1013).
5. c = (2C)^(−1/2) for the region away from ℐ⁺.
6. ϵ_G small depending on C.

Nothing is chosen before what it depends on, so the order is not circular. The gap the writer found is real: the
displayed bound uses the coefficients "in the basis above", which exist only on {x_I < c_V}. ρ ≤ ρ_a < c_V² gives
x_I = ρ^(1/2) < c_V, so the bound now applies.

The V-argument at 981–984 uses the frame exactly on {x_I < c_V} and the e3b membership with C(c_V) on {x_I ≥ c_V}. I
rechecked the inequality ½(t_*² + 2t_*r) ≥ c_V²(1 + 2c_V²)⁻¹(t_* + r)² for r ≤ c_V⁻²t_*. The function
(1 + 2s)/(2(1 + s)²) decreases in s, and its value at s = c_V⁻² is c_V²(c_V² + 2)/(2(c_V² + 1)²) ≥ c_V²/(1 + 2c_V²),
since 2c⁴ + 5c² + 2 ≥ 2c⁴ + 4c² + 2.

The only later use of ρ_a in the chapter is 24:1013 ("ρ⁺ ≤ 2/C ≤ ρ_a"). It holds, because C is fixed after ρ_a. Outside
the chapter, 46:897 ("on {ρ_I ≤ ρ_a} … with 2/C_g ≤ ρ_a") and 46:903 ("where x_I ≥ c_V the membership of h in its
frames") are consistent with the new order. The new order is in fact what makes 46:897's "they hold on the same set"
correct.

## 6. The notation paragraph, 20:24–28

- **N.** No chapter from 20 to 48 (38a included) uses the number of stages: "approximant" occurs only in 20:1574
  ("Schwartz approximants"), and 47:34 says so explicitly. N occurs as the normal operator N(A, ι) (22, 30, 32), the
  conormal bundle N*ℋ (24, 31, 32, 35), large orders H^(−N) (23, 25, 39), the nilpotent N (24:852), a polynomial N(x)
  (33:369), the norm N(w) (29:601), the closed manifold N (38:304), the data norm N(f, …) (45:1144), a Neumann-series
  order (38:408) and the lapse N (47:33).
- **λ, the wavelength.** It occurs only in 47: in cor:vii-2-3 and its proof (47:816–831), and in the two sentences that
  announce it (47:21, 47:812). This matches "only where [[ch:s28]] applies the gluing to the data of the solution g_λ".
  A flat "λ does not occur" would have been false, as the writer says.
- **λ elsewhere.** Sampled at first use in 20, 23–26, 29, 30, 32–34, 36, 38–46 and 48, every λ is defined where it is
  introduced or is a tensor index:
  - an elliptic weight (23:372);
  - cut-off parameters λ ∈ (0, ⅛] (25:545) and λ ∈ (0, ω_0/4] (26:600);
  - a tensor index (24:720, 32:304, 48:610);
  - an interpolation exponent (29:398, 45:1111, 46:470);
  - a scalar (33:356);
  - λ_max and λ_min (20, 24, 32–34, 38);
  - λ_♯ (36:587, 39:54, 40:28);
  - ι⁺-exponents and Mellin variables (36:664, 40:94, 41:22, 43:227, 44:53).
- The paragraph is true for chapters 20–48.

## 7. rem:std-sbg-sobolev (95:1045–1070)

Checked against arXiv:2408.06651v1:

- (3.4) is on p. 29 and reads (ρ_α∂_x)^γ = Π_i (ρ_(α,i)∂_(x^i))^(γ_i).
- The norm ‖u‖_(H^s(ℝⁿ)) := ‖⟨ξ⟩^s û‖_(L²(ℝⁿ_ξ)) is on p. 34.
- Definition 3.14, with (3.13) and (3.14), is on p. 34. The quotation is word for word, apart from the footnote mark 10.
- Remark 3.15, with (3.15), is on p. 35. It is word for word, with the source's typo "defined in the usual" stepped
  around correctly, and "…" standing for "As an illustration for general scalings ρ_α,".
- On p. 36, the cut-off sentence and the boundedness of V : wH^s_𝒱 → wH^(s−1)_𝒱 are word for word. The first sentence
  is paraphrased (nit 3).
- The numbers and pages are right. crosswalk/95 matches the chapter's label sequence, 68 of 68, with the new row in place
  after thm:std-sbg-calculus.

**The three uses in 30 (1292, 1318, 1345).** Each asserts that the norm ‖u‖_(H^k) := Σ‖X_(i₁)⋯X_(i_l)u‖_(L²(μ)),
built from smooth fields spanning T∂M (resp. TZ), is equivalent to the usual Sobolev norm. The entry gives three things:

- with all scalings 1 and w = 1, H^s_𝒱 is the usual (Shubin) space;
- for s ∈ ℕ its norm is equivalent to the chart sums (3.15);
- every V ∈ 𝒱 is bounded H^s_𝒱 → H^(s−1)_𝒱.

The third gives ‖u‖_(H^k) ≤ C × (usual norm). It does not give the reverse bound, usual norm ≤ C‖u‖_(H^k). That bound
needs the coordinate fields written as combinations of the X_i, and it is used: the transfer of Shubin's (1.5) to (EE)
at 30:1345–1352 needs both directions, the bound on ‖Pv‖ included. See finding 1.

## 8. Contract and tools

- Every line of the 16 touched chapter files has at most 121 code points (maximum 121). The one longer added line is the
  crosswalk row, which is a TSV working file.
- No added or rewrapped line, including the R-I1b rewrap 36:1620–1630, starts with "+ ", "- ", "* ", "> ", "#", "=" or
  "|". The exception is 48:191 "- *Backward part.*", which is a list item of the base file and is unchanged apart from
  𝔒.
- No added line contains process, file, program or AI words. The "now a source" lines of 27 are mathematical and
  unchanged apart from ℐ⁺. "the record" occurs only in the crosswalk note.
- `PYTHONDONTWRITEBYTECODE=1 python3 lint.py --chapters`: 62 files, 4406 labels, 1 hit (90:66, the pending marker), as
  expected.
- `python3 assemble.py --check`: labels 4406, computations cited 0, problems 0.
- git status of chapters/ and crosswalk/ is clean before and after both runs.

## The writer's two "no entry" claims, and 61 (a)

- **61 (a).** lem:np-10-50-a (60:116–122) gives g_app = g0 + Σλ^j m_j with g0 = η + (μ_end/r²)(dτ + dr)², and does not
  state the Kerr–Schild identification. The proof of 61 (a) supplies it in its last sentence (61:113–115: "As
  dv = dτ + d|x|, … g^KS_(μ_end,0) of [[def:iii-b-3-2]] at A = 0 ([[prop:iii-b-3-4]]) with t = τ"). That is correct: at
  A = 0, H = m/|x|² and k = dt + d|x|. Leaving (a) unchanged is right.
- **[Hin26c, Lemma 3.5].** 23:358–365 quotes it and says "Neither statement is used below". lem:ii-a-8-5 (23:1060) is
  "the part of [Hin26c, Lemma 3.5] that is used", proved in the chapter, and no other chapter cites the lemma. No entry
  is needed.
- **[Hin23a, Corollary 3.36].** It is cited only at 45:777, 1302 and 1407, as a comparison. thm:iv2-3-1 (45:1304) is
  stated and proved in the chapter (proof from 45:1313). No entry is needed, and footnote 17 is used nowhere.

## R-I1b's fixes

- **46:1728 and 46:1769.** These now read 𝒴_ψ and T_(ψ,b), as in 41:1065–1066 and 41:1669. In 46, ψ is otherwise only
  the subscript of ψ_IVP and ψ_(S…), and the row index of Y_(ψ,rem) at 1386–1408, so there is no clash. 𝒲_τ (defined
  at 40:1321 and 41:103) and the type-indexed 𝒴_τ of 46:1752, 1764 (defined at 35:1440) are other objects and correctly
  kept.
- **36:1622–1624.** R-I1b's text verbatim, rewrapped within 121. True: (E1) inverts N(A, ι) for |Im ι| ≥ R in a strip
  with the displayed bounds. (E2) bounds N(A, ι)⁻¹ uniformly on compact sets of non-poles, and the rest of the line is
  such a set, since by (E3) the line holds no root.

## Findings

**1. minor — 30:1291–1293 (used again at 1318 and 1345): the cited statement gives one direction of the norm
equivalence.**

- *Evidence.* rem:std-sbg-sobolev states the chart norm (3.14), its equivalence with the sums (3.15), its
  identification with the usual uniform Sobolev space at scalings 1, and the boundedness of every V ∈ 𝒱 from H^s_𝒱 to
  H^(s−1)_𝒱 (p. 36). Applied to the X_i, the last gives ‖u‖_(H^k) ≤ C‖u‖_(H^k_𝒱). The reverse bound is stated nowhere in
  the edition. It follows from writing each ∂_(x^j) as a combination of the X_i with smooth coefficients on small charts.
  30:1345 needs it to pass from Shubin's (1.5) in W^s_2-norms to (EE) in the norms of the section, because ‖Pv‖ appears
  on the right-hand side. The mathematics is the standard equivalence and is true. What is missing is a two-line
  derivation, not a result.
- *Fix.* Replace 30:1291–1293, from "this is the usual Sobolev norm up to" to "for k ≥ 1.", by the following (lines of
  at most 119 code points; the sentence "For A ∈ Diff^m_b…" then follows):

      and ‖u‖²_(L²(∂M,μ)) := ∫ |u|² μ with |·| the Euclidean norm of ℂ^(N_E); this is the usual Sobolev norm up to
      equivalence, for each component. Indeed, let 𝓑 be a finite atlas of ∂M with all scalings 1 (so that 𝒱 consists of all
      smooth vector fields), its charts so small that on each of them some dim ∂M of the X_i form a frame. Then H^k_𝒱(∂M) is
      the usual space, normed up to equivalence by the sum (3.15) of [[rem:std-sbg-sobolev]] ([Hin26d, Definition 3.14 and
      Remark 3.15, pp. 34–35]). Every X_i is bounded from H^s_𝒱 to H^(s−1)_𝒱 (p. 36 there), which bounds ‖u‖_(H^k) by that
      norm; and on each chart every ∂_(x^j) is a combination of those X_i with smooth coefficients, which bounds that norm by
      ‖u‖_(H^k), by induction on k (at k = 0 both are comparable to ∫ |u|² μ, μ being smooth and positive). Also
      ‖u‖_(H^k) = ‖u‖_(L²) + Σ_i ‖X_iu‖_(H^(k−1)) for k ≥ 1.

  1318 and 1345 can stay: 1345 already says "as on ∂M above".

**2. nit — 81:1021–1024: the parenthesis is true, but its clause now reads against it.**

- *Evidence.* The clause says that "a small non-round dust density, with regularity at the axes …, is not examined",
  and the parenthesis then says that ch:vlasov carries the solve out. Chapter 82 does construct small non-round dust
  data on the whole slice, smooth up to the axes, by prop:vlasov-scaled-correction with λ = 1 and no phases: the n-dust
  datum D_n (82:1094–1097), prop:vlasov-nonempty (82:1710–1715), and lem:vlasov-axis-commutator for the axes. What is
  not examined is the data of this corollary. Also, "with constants independent of λ" stresses the feature that does
  not matter for these data.
- *Fix.* "… is not examined here (the symmetrizer of that solve exists on every slice, [[lem:vlasov-symmetrizer]], and
  [[ch:vlasov]] carries the solve out for its own data, with constants independent of λ,
  [[prop:vlasov-scaled-correction]]); data localised in an angle …". Rewrap within 121.

**3. nit — 95:1066–1067: the first sentence of p. 36 is paraphrased loosely.**

- *Evidence.* The entry has "unchanged '(up to equivalence of norms)' when defined with respect to a compatible
  structure". The source says "when defined with respect to a b.g. structure compatible with ρB; correspondingly, these
  spaces are unchanged when defined with respect to a scaled b.g. structure compatible with B^×".
- *Fix.* Quote it: unchanged "(up to equivalence of norms) when defined with respect to a b.g. structure compatible
  with ρ𝓑" ((S13)), and "these spaces are unchanged when defined with respect to a scaled b.g. structure compatible with
  𝓑^×". Optionally, add that weights and weight families are those of [Hin26d, Definition 3.4, p. 29] (S2 only points
  to them), and that chapter 30 takes w = 1.

**4. nit — 30:1318–1320: a ragged rewrap.**

- *Evidence.* The I-2 insertion left the 21-character line "also uses the compact" between two full lines. It renders
  correctly.
- *Fix.* Rewrap 1318–1320.

**5. nit (inherited, in a renamed site) — 30:1483: the bare ℋ is not declared.**

- *Evidence.* "(M1): for g supported in ρ < ρ₀, g ∈ ρ^γ L²(|dρ/ρ|; ℋ)". The only declaration is "for any Hilbert space
  ℋ" in the proof of another lemma (30:1227), 250 lines earlier. The base file had 𝓗 here in the same way.
- *Fix.* "…; ℋ), ℋ a Hilbert space, if and only if …".

## Verdict

**NOT CONFIRMED**: 0 Major, 1 minor (finding 1), 4 nits (2–5).

Every I-2 item is applied as reported and is true in place: N1–N6, 07:230 and 264, 81:1022 and 1661, 87:352, 𝒦 → 𝔒,
24:957–981, the notation paragraph, the Appendix A entry against its source, and the two "no entry" decisions. The R-I1b
fixes are correct. The one gap is that rem:std-sbg-sobolev covers only one direction of the norm equivalence that
chapter 30 cites it for.
