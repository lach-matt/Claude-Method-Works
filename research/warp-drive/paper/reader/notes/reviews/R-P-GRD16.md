# R-P-GRD16: an independent review of proofs/P-GRD16.md (sec:tl5-hfk)

**File reviewed.** research/warp-drive/paper/reader/proofs/P-GRD16.md at 8776cb9a, md5 31c985083f6805f0c092efaf5e76932d,
397 lines. Its parts are:
- the chapter text, P:1–198 (11 labels);
- the Placement, P:200–222;
- the Comparison, P:224–381;
- the crosswalk rows, P:383–397.

The writer's report is notes/reports/P-GRD16.md. The previous reading, R-P-GRD15, gives the form of this one, and
notes/reports/P-GRD15-handoff.md gives the conventions it enforces.

**Base.** chapters/87-ten-l5.md, md5 6b2492554f48f2c850e5c2bb0dad4efb, 7837 lines by `wc -l` (the file ends with a
newline) and 5,331 labels. The file is the same at 5d38849f, the base the Placement names, and at 8776cb9a (that commit
adds only the proof and the report). Citations below are P:n for the proof file and 87:n for the chapter.

**Verdict: CONFIRMED WITH THE FIXED COPY.** 0 Major, 1 minor, 7 nits.
- Both lemmas hold, the theorem holds, and the containment of thm:tl5-hff at N = 4 holds, with equality at
  |T|⁻¹ = λ_M^(−1/2).
- The classification into three kinds is complete and right: every term of lem:tl5-hfp-c1 and lem:tl5-hfp-words is
  placed, and each takes the factor the text gives it.
- The minor finding (m1) is in the Comparison. Two of the "at most" figures through the theorem are not upper figures,
  because the 𝔷₁ term falls as well and G0q's price leaves it at full size. A reworded passage, with the writer's own
  numbers, fixes it.
- The nits are four in the chapter text (a count in the opening, a missing K_rec, and two letters reused within one
  proof) and three in the Comparison.
- A tested fixed copy applies all eight.

## 1. Mechanics

The scratch tree is `git archive 8776cb9a` of paper/reader. The Placement is applied by my own merge script
(scratchpad/reader/rpgrd16/tools/merge.py). It reads item 2's old and new text from the proof file itself, and checks
that the old text occurs once and ends the chapter.

- **Placement.**
  - Item 2's two old lines occur once, at 87:7836–7837, and they are the last lines of the chapter.
  - The new pointer line has 119 characters, as stated, and 116 once its labels resolve ("Section 57.31",
    "Theorem 57.253").
  - The section then goes after a blank line. "Line 7838, as changed by item 2" is right. The chapter becomes 8037 lines.
- **Checks.**
  - `lint.py --chapters`: 62 files, 5342 labels, 0 hits.
  - `assemble.py --check`: labels 5342, 0 problems.
  - In-memory check: `[] 0`. I did not run plain `assemble.py`.
- **Numbering.**
  - 0 of the 5,331 existing printed numbers changes; 11 are added.
  - sec:tl5-hfk is Section 57.31. It contains Lemma 57.250 (lem:tl5-hfk-rec), Lemma 57.251 (lem:tl5-hfk-fam),
    Definition 57.252, Theorem 57.253 and Remark 57.254, with displays (57.175)–(57.179). The report agrees.
- **Crosswalk.**
  - 11 of 11 rows give the line of their label: 1, 23, 37, 57, 66, 115, 122, 137, 139, 143, 177.
  - Each row is indented by 4 spaces, has 4 tab-separated columns and is ASCII.
  - Merged, the crosswalk has 491 rows for 491 labels, in the same order. The new labels are lowercase.
- **Format.**
  - The longest chapter-text line has 120 characters (P:18), also with every label resolved. The notes are at most
    121, apart from the crosswalk rows.
  - No wrapped chapter-text line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|".
  - The chapter text names no file or program and has no code and no AI language.
- **Sources.** The writer's one-line source (scratchpad/reader/pgrd16/src.md), with rest.md and ptr.txt and the writer's
  wrap.py, pad.py and build.py, rebuilds the file to md5 31c98508. I made the fixed copy the same way (§8).

## 2. lem:tl5-hfk-rec (P:23–55) holds

**The quantity of lem:tl5-hf-recovery.**
- In its proof (87:4057–4064), D̂_A(ℒ_ZΨ) = Z^B D̂²Ψ(A, B) + 𝔷_(Z,A). T = |T| E₀ gives D̂²Ψ(A, 0) =
  |T|⁻¹(D̂_Aℒ_TΨ − 𝔷_(T,A)), and f_j = Σ c^ab_j K_ab gives D̂²Ψ(A, j) = Σ c^ab_j (D̂_Aℒ_(K_ab)Ψ − 𝔷_(K_ab,A)).
- X is the sum of |D̂²Ψ(A, B)|² over all A and B ∈ {0, 2, 3, 4}. With u_Z = D̂ℒ_ZΨ and w_Z(F_A, ·, ·) = 𝔷_(Z,A), and the
  frame k-orthonormal, X = |T|⁻²|u_T − w_T|² + Σ_j |Σ c^ab_j (u_(K_ab) − w_(K_ab))|² = |𝒳_p(u − w)|² exactly. ✓
- So the quantity that the chapter bounds by K_rec times the family norm is |𝒳_p(D̂ℒ_ZΨ − 𝔷_(Z,·))_Z|, as the writer
  says. Only after that does it use the operator norm. ✓

**(a).**
- By lem:tl5-hf-fields (a), Σ_j |Σ c^ab_j v_ab|² ≤ λ_M⁻¹ Σ |v_ab|² for vectors of any Euclidean space, here the tensors
  of one type at p. So |𝒳_p x| ≤ |(|x_Z|)_Z|_Γ. ✓
- The definition |y|_Γ² = |T|⁻² y_T² + λ_M⁻¹ Σ_(a<b) y_(K_ab)² puts λ_M on the six rotation columns and |T|⁻¹ on the one
  column of T, which matches the rows of the map: one row |T|⁻¹ x_T, three rows Σ c^ab_j x_(K_ab), the 3 × 6 block C
  having operator norm λ_M^(−1/2) (CCᵀ = M⁻¹, 87:3951–3952).
- The factor 6 is the number of rotations K_ab, a < b in {1, 2, 3, 4}. So |y_Z| ≤ u for all seven Z gives
  |y|_Γ ≤ (|T|⁻² + 6λ_M⁻¹)^(1/2) u = 𝔨_Γ u. ✓
- |T|⁻², λ_M⁻¹ ≤ K_rec² gives the second inequality and 𝔨_Γ² ≤ 7K_rec². 𝔷₁^k ≤ K_rec 𝔷₁′ and 𝔷₂^k ≤ K_rec 𝔷₂′ follow
  with 𝔷₁′ = 3(Σ|D̂Z|²)^(1/2) and 𝔷₂′ = 2(Σ|D̂²Z|²)^(1/2) (87:6648). ✓
- **Random test.** In 3000 trials (random 3 × 6 matrices G = (ĝ(K_ab, f_l)), M = GGᵀ, C = M⁻¹G, random |T|⁻¹, random
  families of vectors in dimensions 1, 3 and 5) I checked: CGᵀ = I, |𝒳_p x|² ≤ |x|_Γ² ≤ K_rec²|x|², the second-kind
  bound, and min(w) 𝔞 ≤ 𝔞^k ≤ K_rec 𝔞 for a weighted 7 × 4 map. There were 0 failures. The largest ratio
  |𝒳_p x|²/|x|_Γ² was 0.995.

**(b).**
- |w_Z| ≤ 𝔷_Z by (Σ_A |𝔷_(Z,A)|²)^(1/2) ≤ 𝔷_Z (87:4060). ✓
- Minkowski's inequality gives X^(1/2) ≤ |𝒳_p u| + |𝒳_p w|. Then |𝒳_p w| ≤ |(|w_Z|)|_Γ ≤ |(𝔷_Z)|_Γ, by (a) and the
  monotonicity of |·|_Γ, and Minkowski in |·|_Γ splits it into 𝔷₁^k|D̂Ψ| + 𝔷₂^k|Ψ|. ✓
- **The use of X in lem:tl5-hfz-rec** (87:6421–6437). That proof takes X^(1/2) ≤ K_rec(…) from the proof of
  hf-recovery (87:6422–6423). The rest works with X, X₀ = s²X and R. It ends with |D̂²Ψ| ≤ g(s)^(1/2) X^(1/2) +
  (1 − 𝔥)⁻¹(|𝔣| + 𝔯_♯|Ψ|) ≤ 𝔨_♯(𝔥) X^(1/2) + …, using ‖𝒞‖ + 𝔥‖𝒞‖/(1 − 𝔥) = ‖𝒞‖/(1 − 𝔥), and only then inserts the
  bound of X. So X enters only through a number 𝔟 ≥ X^(1/2), and 𝔟 := |𝒳_p u| + 𝔷₁^k|D̂Ψ| + 𝔷₂^k|Ψ| gives
  eq:tl5-hfk-rec. ✓
- **The last claim** follows from (a) alone: each of the three terms is at most K_rec times its counterpart in the form
  that lem:tl5-hfp-rec uses (87:6816–6817). The proof's clause on Minkowski over Z explains why that form is a form of
  eq:tl5-hfz-rec. It is right, though not needed for the inequality. Note that eq:tl5-hfk-rec is not claimed to be at
  most eq:tl5-hfz-rec with (Σ 𝔷_Z²)^(1/2) itself. That would be false, since 𝔷₁^k|D̂Ψ| + 𝔷₂^k|Ψ| ≥ |(𝔷_Z)|_Γ, and the
  text rightly does not claim it.
- K_rec is used in (a) but is not among the data the lemma takes from lem:tl5-hfz-rec (n2). Two letters clash in the
  proof of (b) (n3).

## 3. lem:tl5-hfk-fam (P:57–113) holds

**The face estimate for the four fields.**
- eq:tl5-hfe-face (87:7287–7296) holds for every tensor field A of rank r on Q(a, b) of the regularity of
  lem:tl5-hf-sobolev. Ã₀ = |T(p)|⁻¹ D̂Ψ_T and Ã_j = Σ c^ab_j(p) D̂Ψ_(K_ab) are such fields of rank three.
- **Do the operations commute with the frozen coefficients?** The coefficients are constants on Q(a, b). ℒ_X(cA) =
  X(c)A + cℒ_XA = cℒ_XA, D̂(cA) = cD̂A, and ℒ_(∂_γ) likewise. The transport along the curves is the proof of the face
  estimate itself, applied to the field Ã_i. So nothing needs to commute beyond this linearity. ✓
- The c^ab_j(p) refer to the leaf frame f_j at p. As a field, Ã_j is a fixed linear combination of the D̂Ψ_(K_ab), and
  Σ_j |Σ c^ab_j(p) v_ab|² does not depend on the choice of the f_j at p.
- **lem:tl5-hf-fields (a) away from p.** The inequality is algebraic: the matrix C(p), whose norm is λ_M(p)^(−1/2), acts
  on vectors of any Euclidean space. At a point q of the face or of S_a it acts on the tensors at q in the k-norm at q.
  So Σ_i |ℒ^JÃ_i|² ≤ |(|ℒ^J A_Z|)_Z|_Γ², and likewise with D̂ℒ^J, hold there with the weights of p. ✓
- Σ_i |Ã_i(p)|² = |𝒳_p(A_Z(p))_Z|² by definition. The weights 𝔶 and 𝔲₁ and the constant C_(E,0)(𝔶) are those of
  the step, as the proof of thm:tl5-hfe uses them (87:7450–7455). ✓

**The classification.** I went through the proofs of lem:tl5-hfp-c1 (87:6772–6802) and lem:tl5-hfp-words
(87:6744–6758) term by term. The Comparison's line citations are all right.

| term of the family bound | where | kind | why |
|---|---|---|---|
| leading terms D̂Ψ_(JZ) of ℒ^J A_Z | 87:6775–6776 | first | depends on (J, Z); Euclidean norm ≤ μ^(1/2) 𝒟_g |
| remainders R′_(J,Z), D̂R′_(J,Z) (Ψ_(σZ)) | 87:6776–6780 | first | depends on (J, Z); ≤ ϖ′^(1/2) 𝒥_g, (2ϖ′)^(1/2) 𝒥_g |
| face recovery of D̂²Ψ_(JZ): leading term through Z′JZ | 87:6747–6748 | first | ≤ k₁^D 𝒟_g, k₁^D with K_rec(q) |
| its terms with 𝔷_(Z′) and 𝔯_♯\|Ψ_(JZ)\| | 87:6748–6749 | first | ≤ μ^(1/2)(k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) 𝒥_g |
| its couplings 𝔄 | 87:6749–6750 | third | row (J, Z) of the map of 𝔞_𝔄(Γ) |
| its part with ϱ, 𝔬_J P_C | 87:6750–6751, 6754–6755 | second | P_C = 𝔢_(\|J\|) P_ϱ depends on J only |
| its nonlinear part 𝔵^z(…)/(1 − 𝔵^z) | 87:6751–6754 | second | 𝔐 is the bound for all words of length \|C\| |
| the terms on S_a | 87:6796–6801 | second | bound by η₀(p) and Λ_a, per J only |
| the coefficients f, W (18\|D̂∂_γ\|², 2\|∂_γ\|²) | 87:6774 | — | multiply the integrands, unchanged |

- Every term is placed, and the writer's placement is mine.
- *First kind.* |y|_Γ ≤ K_rec(p)|y| for every family of numbers, so each part is K_rec(p) times its old bound. That is
  the old route's own factor (𝔨_rec^p carries K_rec(p) on the whole of C₁^Γ), so there is no gain and no loss. ✓
- *Second kind.* A bound u_J for all seven Z gives |(u_J)_(J,Z)|_Γ = 𝔨_Γ(Σ_J u_J²)^(1/2), against the Euclidean
  √7(Σ_J u_J²)^(1/2). The nonlinear part is one number u for all 301 pairs, so (43n)^(1/2) u = 301^(1/2) u becomes
  43^(1/2) 𝔨_Γ u. The ϱ part gives (Σ_J 𝔬_J² P_C²)^(1/2) = (43 𝔗² μ⁴)^(1/2) P_ϱ times 𝔨_Γ, so V, and with it the
  part with ϱ(p) of eq:tl5-hfp-family, takes 𝔨_Γ for n^(1/2). The terms on S_a give 𝔨_Γ² times one word's, so E₀
  takes 𝔨_Γ for n^(1/2). ✓
- *Third kind.* Output component (J, Z) of the map of 𝔞_𝔄(Γ) is 𝔬_J Σ_K 𝔄_(JZ,K) ξ_K. It is normed, as in
  def:tl5-hfz-constants (87:6455–6457), by the Euclidean norm of the family of tensors. The weighted norm of the family
  of their norms is the Euclidean norm of the components multiplied by |T(p)|⁻¹ or λ_M(p)^(−1/2). So it is at most
  𝔞_𝔄^k 𝒥_g, with 𝔞_𝔄^k as defined. ✓ Also λ_M^(−1/2)𝔞 ≤ 𝔞^k ≤ K_rec 𝔞 (the "floor" of the Comparison), by
  ‖D⁻¹‖‖DM‖ ≥ ‖M‖ for the diagonal D.

**The new bounds.**
- I recomputed both displays at P:100–101 from the per-pair bounds. K𝔩_D^k = K k₁^D + 43^(1/2) 𝔨_Γ k₁^D 𝔵^z/(1 − 𝔵^z),
  and K𝔩_J^k = Kμ^(1/2)(k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) + (1 − 𝔰₁^v)⁻¹ 𝔞_𝔄^k + 43^(1/2) 𝔨_Γ 𝔵^z(k₁^p − k₁^D + 2)/(1 − 𝔵^z).
  Both are 𝔩_D(Γ) and 𝔩_J(Γ) of 87:6659–6660 with 43^(1/2)𝔨_Γ/K for 301^(1/2) and 𝔞_𝔄^k/K for 𝔞_𝔄(Γ), times K. ✓
- In the per-pair nonlinear bound, 𝔬_J(𝔵^z(2μ^(…)𝒥_g + 𝔐)) + 𝔬_J(1 − 𝔵^z)P_C gives the coefficient (k₁^p − k₁^D + 2)
  and the whole 𝔬_J P_C, as stated. ✓
- K = K_rec(p) is a number on the face, so K² leaves the integrals F_D², P_D², F_J², P_J², F² and P². This gives
  K C₁^(D,·), K C₁^(J,·) and K C₁^(U,·) so formed, and C₁^k is the smaller bound. ✓
- **The last claims.** 𝔞_𝔄^k ≤ K𝔞_𝔄(Γ) and 43^(1/2)𝔨_Γ/K ≤ 301^(1/2). The integrands are nondecreasing in both, their
  coefficients being nonnegative: k₁^p ≥ k₁^D = 𝔨_♯K_rec by 87:6649–6650. The minimum of nondecreasing functions is
  nondecreasing, so C₁^k ≤ K C₁^(Γ,l). ✓
- Within the proof, y names both the generic family of numbers and the term y of lem:tl5-hfp-c1 (n4).

## 4. The definition, the theorem, the closing condition and the Remark

**The sites.** I grepped every occurrence of 𝔨_rec in 87.
- The 𝔨_rec^(·,p) enter only C_P^v, C_(P,ϱ)^v and C_(P,0)^v (87:6199–6200; through 𝔨_rec^z, 87:6449, and the index-p,
  d, l and f forms, 87:6675–6677, 7193, 7413, 7755).
- At N = 4 these enter 𝔎, 𝔎_ϱ and 𝔎₀ (87:5655, with def:tl5-hfs-constants covering N = 4 and def:tl5-hfv-constants
  replacing C_P^♮), 𝔎^D, 𝔎^D_ϱ and 𝔎^D₀ (87:7197–7200), S_F and 𝔯 (𝔯_q = 𝔯_(w,s) + 𝔯_(M,q), 87:6097), and 𝔰_*.
- The definition names all of these. The three new numbers are those of def:tl5-hfp-constants in their index-f forms:
  C₁^(Γ,l), C₁^l, C_(1,ϱ)^l, C_(1,0)^p of index l, and C_S^h, C_(0,0)^h of lem:tl5-hff-zero (87:7755). The four
  replacements are exactly as listed. ✓
- I rederived the three formulas of eq:tl5-hfk-krec from the theorem's proof: μ² times the leading term, μ^(3/2)|D̂h|
  through C₁^l, C_(1,ϱ)^l, C_(1,0)^p, and μ|h| through C_S^h, C_(0,0)^h (no ϱ). ✓
- ε^k = ε^f, as route (𝔰) puts no C_P in ε (ε^l, 87:7426).

**N = 4.**
- The restriction is stated in lem:tl5-hfk-fam, the definition and the theorem, and it is needed: 𝔨_rec^p and C₁^(Γ,l)
  exist only at N = 4, where lem:tl5-hfv-rec bounds 𝔰_P through the recovery of D̂²h.
- lem:tl5-hfk-rec is pointwise and carries no level, rightly.
- At N ≥ 6, 𝔰_P comes from the step at low levels with 𝔐_p, which the section leaves alone. "At the levels N ≥ 6
  nothing changes" is right. The Comparison's scoping of that step under "Not done" is plausible and marked not drafted.
- At N = 4 only route (𝔰) exists (87:7757–7758), so "with route (𝔰)" is a statement, not a restriction.

**The hypotheses.**
- (a)–(c) are those of thm:tl5-hff with index k. The setting of thm:tl5-hff carries 𝔶₀^h, 𝔲₀, 𝔲₁ and 𝔲_M. No hypothesis
  is missing.
- In the proof, 𝔰 ≤ 𝔰₁^v on Q(a, b) gives |H(p)| ≤ 𝔰₁^v, so lem:tl5-hfk-rec (b) applies with 𝔥 = 𝔰₁^v. lem:tl5-hfk-fam
  applies in the setting of lem:tl5-hfp-rec.
- The bound of 𝔰_P is the only place where the 𝔨_rec^(·,p) enter, so the one change suffices. ✓

**Containment.**
- 𝔨_Γ ≤ √7K_rec, 𝔷^k ≤ K_rec𝔷′ and C₁^k ≤ K_rec C₁^(Γ,l) give the three numbers term by term below those they replace.
- Every constant with index f is nondecreasing in them, through maxima, sums and suprema with nonnegative coefficients.
  So each constant with index k is at most its counterpart, ε^k = ε^f, η_k ≥ η_f, A_k ≤ A_f, B_k ≤ B_f and
  4A_kB_k ≤ 4A_fB_f < 1.
- Y = 2A/(1 + (1 − 4AB)^(1/2)) is nondecreasing in A and in B, and 𝔰_*^k[𝔜] is nondecreasing in 𝔜 and the constants.
  So Y_k ≤ Y_f, 𝔰_*^k ≤ 𝔰_*^k[Y_f] ≤ 𝔰_*^f < 𝔰₁^v, and the hypotheses of thm:tl5-hff at N = 4 imply those of thm:tl5-hfk.
  ✓
- **Equality at |T|⁻¹ = λ_M^(−1/2) at every p.** Both weights are then K_rec², so |y|_Γ = K_rec|y|, 𝔨_Γ = √7K_rec,
  𝔷^k = K_rec𝔷′, and 𝔞_𝔄^k = K_rec𝔞_𝔄(Γ) (the diagonal is K_rec·I). So C₁^k = K_rec C₁^(Γ,l), and every constant is
  equal. The Comparison states this. ✓

**The opening (P:3–21) and the Remark (P:177–198), word by word.**
- Each mechanism matches the proofs: the image under 𝒳_p, the face estimate for the four fields with frozen
  coefficients, the three kinds with their factors, the weights on the 𝔷_Z, and the sites through C_P^v, C_(P,ϱ)^v and
  C_(P,0)^v.
- The Remark's ratio of 𝔨_Γ/(√7K_rec) is right. A test of 2·10⁵ random (|T|⁻², λ_M⁻¹) gave a maximum of 1 and infima
  0.3781 (7^(−1/2) = 0.3780) and 0.9258 ((6/7)^(1/2) = 0.9258).
- One count differs. The opening says "two kinds of terms take different factors" and then gives three: K_rec(p),
  𝔨_Γ and the weighted norm of the couplings. The proof sorts the bounds into three kinds (n1).
- The Remark's "ending in" is right in the chapter's convention ℒ^J Ψ_B = Ψ_(JB). The words JZ, Z′JZ and σZ of the face
  energies end in the field Z. rem:tl5-hfp-what (87:6881–6882) says "beginning with T", but it speaks of the words ZC
  that the recovery at a point takes, so the two remarks do not contradict each other.

**The obstruction for the first kind.**
- The first-kind parts need Σ_J(|T|⁻² y_(J,T)² + λ_M⁻¹ Σ y_(J,ab)²) over the words ending in T and in a rotation. The
  chapter enters the face energies only through ℰ_g(p). I checked the cited sites: 87:6794, 87:7720, 87:7604–7605,
  87:7802 and 87:6241–6243.
- Given only E_T + E_R ≤ ℰ_g(p), the supremum of |T|⁻²E_T + λ_M⁻¹E_R is K_rec²ℰ_g(p). So "a smaller factor for them
  would need bounds that separate the face energies …, which ℰ_g(p) does not give" is exact for these bounds.
- The Comparison qualifies it "by this route". There is no overclaim and no underclaim.
- The remark that the face recovery would give its leading term only as a first-kind term is right: the words Z′JZ
  begin with each of the seven fields.
- **The sketch of a weighted bootstrap** (P:293–301) is marked deduced and a sketch. Its reading of lem:tl5-hf-system
  (87:4028–4031) and lem:tl5-hf-fields (b) (87:3940) is right. One small point, not a finding: for k = j the last
  letter of J(j, S) "changes" unless it is the same field.

## 5. The Comparison

**The figures, each checked against its report.**
- **G0q §G0q.2 item 2.** |T|⁻¹ = 1.098 / 1.088 / 1.578 / 1.371, λ_M^(−1/2) = 0.380 / 0.399 / 0.866 / 0.757, K_rec the
  T part. The equal-shares figures 0.495 (−0.31) / 0.508 (−0.29) / 0.633 (−0.20) / 0.636 (−0.20), the floor figures
  0.346 (−0.46) / 0.367 (−0.44) / 0.549 (−0.26) / 0.552 (−0.26), and the shares 95.8 / 94.2 / 98.6 / 98.0 %, the
  rest the 𝔷₁ term with 𝔷₂ and 𝔯_♯ ≤ 0.1 %. All match. ✓
- **G0q §G0q.2 item 1.** sup 𝔨_rec^p over sup 𝔤₁C_S is 0.098 / 0.402 / 0.185 / 0.515 (cited 0.098 / 0.185 and 0.10–0.52).
  At level 6 it is 0.79 / 1.20 / 1.01 / 1.39. ✓
- **G0q §G0q.2 item 3.** C₁ term ÷ 2: +0.09 / +0.24 / +0.06 / +0.29. Both together: +0.26 / +0.25 / +0.30 / +0.29. ✓
- **G0q §G0q.0.** 𝔰_♭ = 10⁻⁴ / 10⁻⁴ / 10⁻² / 10⁻⁴; lever 2 pays 0.00 at level 6; 𝔰_* sets ε 3.45–5.82 below the
  closing. ✓
- **G0q §G0q.1.** ϱ is 0.04–0.44 above f, with f binding. ✓
- **G0p.** §G0p.0 gives 𝔵^z = 0.068 / 0.047 / 0.109 / 0.122. §G0p.4 gives 𝔐_p^(2)/C₁ = 0.92–1.29 at x = 0.05. ✓
- **P-GRD15 at 7cad931e.** "needs the face energies split by the last letter of the words" (P-GRD15:355) and
  "(43|T|⁻² + 258λ_M⁻¹)^½ against 301^½ K_rec" (P-GRD15:349–350) are quoted exactly. 43^(1/2)𝔨_Γ equals the latter. ✓

**The arithmetic, recomputed** (scratchpad/reader/rpgrd16/tools/numcheck.py, at nice 19).
- Equal shares 0.4955 / 0.5081 / 0.6333 / 0.6357; floor 0.3461 / 0.3667 / 0.5488 / 0.5522. ✓
- u = 1.266 / 0.856 / 2.122 / 2.411; nonlinear share 0.559 / 0.461 / 0.680 / 0.707. ✓
- The fall of 𝔩_D(Γ) is 0.1438 / 0.1117 / **0.1245** / 0.1293, printed 0.14 / 0.11 / 0.13 / 0.13. The third rounds to
  0.12, and stays below 0.125 across the rounding of 𝔵^z (n6).
- 𝔨_rec^k at seed 1 D_A, with the 𝔷₁ term at the floor: 0.3105, printed 0.311. ✓
- log₁₀(𝔨_Γ|T|) = 0.118 / 0.129 / 0.224 / 0.226, printed 0.12 / 0.13 / 0.22 / 0.23. ✓
- log₁₀ 1.01 = 0.0043; log₁₀ 1.0001 = 4.3 × 10⁻⁵; ¼ log₁₀ 3 = 0.119. ✓

**Marking.** The figures are marked deduced, not evaluated, and as upper figures. They carry the assumption "every
supremum at one point", and the caveat that G0q is on P-GRD14 and the 𝔵^z on P-GRD13. ✓

**Beyond what is proved.**
- The bracket "between the floor ratio and 1, at least the equal-shares ratio where the part with 𝔞_𝔄 is negligible"
  is right.
- **Through the theorem**, two of the "at most" figures are not upper figures (m1). G0q's price halves the C₁ term
  alone, which on 𝔨_rec^p is a fall of 0.283 / 0.277 / 0.295 / 0.292. Here the 𝔷₁ term falls too, and 𝔨_rec^k may
  fall by up to 0.311 / 0.301 / 0.199 / 0.198. This holds at seed 2 D_A "alone" and at both D_A points "together",
  where 𝔤₁C_S, lowered as well, no longer caps seed 1.
- "Both constraints" omits the entries of 𝔯 with C_(P,ϱ) and C_(P,0) themselves (n5). In "A deduced figure for the
  split", Y carries a stray 𝔲₁⁻¹ (n7).

## 6. Form, and the index letter k

- The form checks of §1 pass on the original and on the fixed copy.
- **The index letter k.** k is free as an index in 87. C₁^k, 𝔷^k, 𝔨_rec^(·,k), 𝔞_𝔄^k, 𝔩^k, ε^k, 𝔯^k, S_F^k, η_k,
  A_k, B_k and Y_k occur nowhere else.
  - The frame metric is written k once, in def:tl5-hf-frame, and k̂ elsewhere, always as a norm |·|_k̂ or in the phrase
    "the norm induced by k". The section never writes it.
  - k occurs elsewhere in 87 as a running subscript (Λ_k, λ^♮_k, 𝔶_k, 𝔢_k) and in the constants k₁, k₂, k₃. None of
    these sits where it could be read as the new index. Within the section k is never a running index, and k₁^D, k₁^p
    sit beside 𝔩_D^k only as named constants.
  - The pattern "the constants with index k", with η_k, A_k, B_k and Y_k, is that of indexes f, c and l, and the
    definition states it.
  - I judge that it does not confuse a reader, so no fix is proposed.
- **Local letters.** w_Z (a tensor in the proof of lem:tl5-hfk-rec) and w (the weight of P_ϱ in lem:tl5-hfk-fam), and
  A_Z (fields) beside A_k (a number), are in different lemmas or roles. A_B and A_p stood together in sec:tl5-hfp the
  same way. The two clashes inside a single proof are n3 and n4.

## 7. Findings

**m1 (minor), P:326–328 and P:337–344, Comparison: the prices through the theorem as upper figures.**
- **The text.**
  - "so 𝔨_rec^k falls by at most about the first figures (0.311 at seed 1 D_A with the 𝔷₁ term at the floor), and by at
    most the second in all cases."
  - "Alone, on the P-GRD14 constants: at most G0q's price of the C₁ term ÷ 2 (a fall of 0.30), +0.09 / +0.24 / +0.06 /
    +0.29. … at seed 2 the falls above are at most 0.29 (D_A) and 0.26 (D*), unless the part with 𝔞_𝔄 leads …"
  - "With C_P⁰ lowered by 0.30 as well …: at most G0q's price of both together, +0.26 / +0.25 / +0.30 / +0.29."
- **What is wrong.**
  - G0q's lever halves the C₁ term only (§G0q.2 item 3, "𝔨_♯K_rec C₁^Γ ÷ 2"). With the shares of item 2, that is a fall
    of 𝔨_rec^p of 0.283 / 0.277 / 0.295 / 0.292 at the supremum.
  - Here the 𝔷₁ term falls too, by up to the floor figure, so 𝔨_rec^k may fall by up to 0.311 / 0.301 / 0.199 / 0.198
    where the part with 𝔞_𝔄 is negligible. It may fall by up to 0.46 / 0.44 / 0.26 / 0.26 if the couplings led.
  - "Alone": seed 1 is capped (0.098 / 0.185 < 0.283 / 0.295) and seed 2 D* falls less (≤ 0.258 < 0.292). Seed 2 D_A
    may exceed the priced fall by 0.025 through the 𝔷₁ term alone, so "+0.24" is not an upper figure there. The
    sentence compares the C₁ term's fall (0.29), not 𝔨_rec^p's.
  - "Together": with C_S ÷ 2, 𝔤₁C_S no longer caps seed 1 D_A before a fall of 0.098 + 0.301 = 0.40. Both D_A points
    may exceed the priced fall, by 0.027 and 0.025, or 0.18 and 0.16 if the couplings led. Only the D* entries are
    upper figures.
- **Why it is minor.** It is in the notes, not the chapter text. The magnitudes are small without the couplings. Every
  number the fix needs is the writer's own or G0q's.
- **Fix (applied).**
  - P:327–328 becomes "so 𝔨_rec^k falls by at most 0.311 / 0.301 / 0.199 / 0.198 (the first figures with the 𝔷₁ term
    at the floor) where the part with 𝔞_𝔄 is negligible, and by at most the second figures in all cases."
  - The two bullets P:337–344 become:
    - "The gain is nondecreasing in the fall of 𝔨_rec^p. G0q's price of the C₁ term ÷ 2 halves that term alone, a fall
      of 𝔨_rec^p of 0.283 / 0.277 / 0.295 / 0.292 at the supremum, the 𝔷₁ term keeping its size; here 𝔨_rec^k falls by
      at most 0.311 / 0.301 / 0.199 / 0.198, or 0.46 / 0.44 / 0.26 / 0.26 if the couplings led C₁^(Γ,l) (above).
      Alone, on the P-GRD14 constants: at most that price, +0.09 / +0.24 / +0.06 / +0.29, except at seed 2 D_A. At
      seed 1 the price is already capped by 𝔤₁C_S, which takes the supremum back once 𝔨_rec^p has fallen by 0.098 /
      0.185 (sup 𝔨_rec^p over sup 𝔤₁C_S, item 1), so a larger fall gives no more there; at seed 2 D* the fall here is
      the smaller. At seed 2 D_A it may exceed the priced fall by 0.02, through the 𝔷₁ term, or by 0.16 if the
      couplings led, so +0.24 is not an upper figure there; the excess is not priced."
    - "With C_P⁰ lowered by 0.30 as well (P-GRD15's lever 3a, C_S ÷ 2 in G0q): G0q's price of both together, +0.26 /
      +0.25 / +0.30 / +0.29, is an upper figure at the two D* points, where the fall here is the smaller. At the two
      D_A points it may exceed the priced fall by 0.03 / 0.02, or by 0.18 / 0.16 if the couplings led, and at seed 1
      D_A 𝔤₁C_S, lowered as well, no longer caps it before a fall of 0.40; this excess is not priced. A larger fall of
      C_P⁰ is not priced; how far C_P⁰ falls at the supremum is G0r's measurement."

**n1 (nit), P:11–12, the opening: the number of kinds.**
- **The text.** "In the bound of the family that results, two kinds of terms take different factors
  ([[lem:tl5-hfk-fam]])." Three are then described.
- **Why.** The proof sorts the bounds "of three kinds" (P:83), and the Comparison speaks of three kinds. Summaries are
  held to the proof word for word.
- **Fix (applied, same length).** "… three kinds of terms take different factors ([[lem:tl5-hfk-fam]])."

**n2 (nit), P:23, lem:tl5-hfk-rec: K_rec among the data.**
- **The text.** "Let p, H, Ψ, 𝔣, 𝔷_Z, ‖𝓡̂‖, ‖𝒞_(·1)‖, 𝔥, 𝔨_♯(𝔥) and 𝔯_♯ be as in [[lem:tl5-hfz-rec]]".
- **Why.** (a) uses K_rec, which lem:tl5-hfz-rec lists among its data and this list leaves out.
- **Fix (applied).** "Let p, H, Ψ, 𝔣, K_rec, 𝔷_Z, ‖𝓡̂‖, ‖𝒞_(·1)‖, 𝔥, 𝔨_♯(𝔥) and 𝔯_♯ be as in [[lem:tl5-hfz-rec]]".

**n3 (nit), P:49, proof of lem:tl5-hfk-rec (b): the letter B.**
- **The text.** "as |B|² = Σ_A |B(F_A, ·, ·)|² for a tensor B of rank three, the number X of that proof, the sum of the
  |D̂²Ψ(A, B)|² over all A and all B ≠ 1, …"
- **Why.** In one sentence B is a tensor of rank three and a frame index.
- **Fix (applied).** "as the squared norm of a tensor of rank three is the sum over A of those of its values at (F_A,
  ·, ·), the number X of that proof, …"

**n4 (nit), P:93, proof of lem:tl5-hfk-fam: the letter y.**
- **The text.** "… in the nonlinear parts of 𝔩_D(Γ) and 𝔩_J(Γ) and in y, …"
- **Why.** This y is the term y := (43n)^(1/2) 𝔗(𝔶) μ^((b+3)/2) P_ϱ of the proof of lem:tl5-hfp-c1 (87:6785). The
  same proof uses y at P:80 and P:90 for a family of numbers over the pairs.
- **Fix (applied).** "… and in the term y of that proof, …"

**n5 (nit), P:246, Comparison, "Both constraints": the entries of 𝔯.**
- **The text.** "… and through 𝔯 (𝔎_ϱ, 𝔎₀, 𝔎^D_ϱ, 𝔎^D₀), …"
- **Why.** 𝔯 = 𝔯_(w,s) + 𝔯_(M,q) (87:6097), and 𝔟_(o,s), 𝔟_(i,s) carry 𝔣₀ and 𝔣₁ times C_(P,ϱ) ϱ + C_(P,0) η₀ directly
  (87:5657–5658), as S_F carries 𝔣₀C_P and 𝔣₁C_P. The list gives these for S_F but not for 𝔯.
- **Fix (applied).** "… and through 𝔯 (𝔣₀ and 𝔣₁ times C_(P,ϱ) and C_(P,0), 𝔎_ϱ, 𝔎₀, 𝔎^D_ϱ, 𝔎^D₀), …" The paragraph
  is re-wrapped.

**n6 (nit), P:331, Comparison: the fall of 𝔩_D(Γ) at seed 1 D\*.**
- **The text.** "is a fall of 0.14 / 0.11 / 0.13 / 0.13 decades of 𝔩_D(Γ)".
- **Why.** log₁₀((1 + u)/(1 + 0.633u)) with u = 2.122 is 0.1245, and at most 0.1248 across the rounding of 𝔵^z = 0.109.
- **Fix (applied).** "0.14 / 0.11 / 0.12 / 0.13".

**n7 (nit), P:333, Comparison: Y of rem:tl5-hfe-what.**
- **The text.** "so where 2𝔲₁⁻¹|∂_γ|²𝔩′² leads Y the fall of C₁ is half that of 𝔩′".
- **Why.** In rem:tl5-hfe-what the bracket is 𝔲X + 𝔲⁻¹Y with Y = 18|D̂∂_γ|²X + 2|∂_γ|²𝔩′². Y carries no 𝔲₁⁻¹.
- **Fix (applied).** "so where 2|∂_γ|²𝔩′² leads Y …"

## 8. The fixed copy

/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd16/P-GRD16.fixed.md

- md5 03dc1572052d64806e62090708ef6636, 403 lines: chapter text P:1–199 (11 labels), then the Placement, the
  Comparison and the crosswalk rows.
- **How it was made.** /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd16/tools/fix.py
  applies the fixes to copies of the writer's sources.
  - Each old text occurs exactly once.
  - The sources are in /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd16/build/
    (src.md, rest.md, ptr.txt). They are verified to rebuild the original to md5 31c98508.
  - The writer's wrap.py and pad.py re-wrap the chapter text, and build.py rebuilds the file with the crosswalk rows
    at their labels. The re-wrapped notes paragraphs use the same rule.
- **Re-merged in a fresh tree,** it passes every check:
  - item 2 found at 87:7836, the new line at 119 characters;
  - lint: 0 hits, 5342 labels;
  - check: 0 problems;
  - `[] 0`;
  - 0 of 5331 existing numbers changed, 11 added with the same numbers as before;
  - the crosswalk has 491 rows for 491 labels, in order;
  - chapter-text lines are at most 120 characters, also resolved, and the notes at most 121;
  - no forbidden line start in the chapter text.
- **Crosswalk lines that moved.**
  - Unchanged: sec:tl5-hfk at 1, lem:tl5-hfk-rec at 23 and eq:tl5-hfk-rec at 37.
  - Each later label moves by one line, because n3's re-wrap adds a line to the proof of lem:tl5-hfk-rec:
    lem:tl5-hfk-fam 57 → 58, eq:tl5-hfk-fam 66 → 67, def:tl5-hfk-constants 115 → 116, eq:tl5-hfk-krec 122 → 123,
    eq:tl5-hfk-constants 137 → 138, thm:tl5-hfk 139 → 140, eq:tl5-hfk-closing 143 → 144 and rem:tl5-hfk-what
    177 → 178.
  - The row notes are unchanged. The rows are regenerated with the new numbers.
- The repository was not touched, and nothing was committed.

## Verdict

**CONFIRMED WITH THE FIXED COPY.** 0 Major, 1 minor, 7 nits. All of them are applied in the fixed copy, md5
03dc1572052d64806e62090708ef6636, and checked.
- lem:tl5-hfk-rec is correct. The quantity that lem:tl5-hf-recovery bounds by K_rec times the family norm is exactly
  |𝒳_p(D̂ℒ_ZΨ − 𝔷_(Z,·))_Z|, and lem:tl5-hfz-rec uses it only through a number above X^(1/2). (a) holds, with the factor
  6 and λ_M on the six rotation columns.
- lem:tl5-hfk-fam is correct. The face estimate admits the four fields with frozen coefficients, and lem:tl5-hf-fields
  (a) holds at every point of the face and of S_a with the weights of p. Every term is placed in its kind: the first
  keeps K_rec(p), the second takes 𝔨_Γ, the third 𝔞_𝔄^k ≤ K_rec𝔞_𝔄(Γ). C₁^k ≤ K_rec C₁^(Γ,l).
- thm:tl5-hfk holds at N = 4, the restriction being needed and stated. Its hypotheses are complete.
- The hypotheses of thm:tl5-hff at N = 4 imply those of thm:tl5-hfk, with equality at |T|⁻¹ = λ_M^(−1/2).
- The opening and the Remark state each mechanism as proved, after n1. The obstruction for the first kind is stated
  exactly.
- The Comparison's figures are cited exactly, and its upper figures hold after m1.
