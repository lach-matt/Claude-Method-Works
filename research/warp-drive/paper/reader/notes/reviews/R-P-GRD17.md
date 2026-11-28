# R-P-GRD17: an independent review of proofs/P-GRD17.md (sec:tl5-hfn)

**File reviewed.** research/warp-drive/paper/reader/proofs/P-GRD17.md at 076b34f2 (branch ccr-af9edcf6-9a60sz), md5
10d83c5cc91169a32fb89658a1aa7f3f, 396 lines. Its parts are:
- the chapter text, P:1–187 (10 labels; the report's "1–186" is one short, as P:187 is the Remark's last line);
- the Placement, P:189–211;
- the Comparison, P:213–381;
- the crosswalk rows, P:383–396.

The writer's report is notes/reports/P-GRD17.md. The previous reading, R-P-GRD16, gives the form of this one, and
notes/reports/P-GRD15-handoff.md gives the conventions it enforces.

**Base.** chapters/87-ten-l5.md, md5 2a1029369f4471db042ced7152c08f6b, 8038 lines, 491 labels. The file is the same at
f76dfef5, the base the Placement names, and at 076b34f2 (that commit adds only the proof and the report). Citations below
are P:n for the proof file and 87:n for the chapter.

**Verdict: CONFIRMED WITH THE FIXED COPY.** 0 Major, 2 minor, 7 nits.
- Both lemmas hold, the theorem holds, and the containment of thm:tl5-hff at N ≥ 6 holds for every weight, route and
  option. At N = 4 nothing changes, and thm:tl5-hfk stands.
- The scoping is right. The step bounds a maximum over the words, and in the part with ℰ_g only the couplings 𝔄_BJ need
  other words. The commutators all enter through 𝔄_BJ and 𝔔_BJ, and the residual and the absorption count no family.
  The parts with ϱ and η₀ of the step do count all the words, through (2𝔐^(m))^(1/2). The section keeps them, and
  proves rightly that its own are smaller.
- Both minor findings are in the Comparison.
  - m1: G0r's ratio C₁^l({ZB})/𝔐_p^(2) is placed at the wrong point, and the lower figures mix two points. The printed
    lower figures still stand.
  - m2: one sentence states the containment the wrong way round.
- The nits are three in the chapter text and four in the Comparison.
- A tested fixed copy applies all nine.

## 1. Mechanics

The scratch tree is `git archive 076b34f2` of paper/reader. The Placement is applied by my own merge script
(scratchpad/reader/rpgrd17/tools/merge.py, adapted from rpgrd16). It reads item 2's old and new text from the proof file
itself, and checks that the old text occurs once and ends the chapter.

- **Placement.**
  - Item 2's two old lines occur once, at 87:8037–8038, and they are the last lines of the chapter.
  - The new pointer line has 112 characters, as stated, and 109 once its labels resolve ("Section 57.32",
    "Theorem 57.258").
  - The section then goes after a blank line. "Line 8039, as changed by item 2" is right. The chapter becomes 8227 lines.
- **Checks.**
  - `lint.py --chapters`: 62 files, 5352 labels, 0 hits.
  - `assemble.py --check`: labels 5352, 0 problems.
  - In-memory check: `[] 0`. I did not run plain `assemble.py`.
- **Numbering.**
  - 0 of the 5,342 existing printed numbers changes; 10 are added.
  - sec:tl5-hfn is Section 57.32. It contains Lemma 57.255 (lem:tl5-hfn-fam), Lemma 57.256 (lem:tl5-hfn-low),
    Definition 57.257, Theorem 57.258 and Remark 57.259, with displays (57.180)–(57.183). The report agrees.
- **Crosswalk.**
  - 10 of 10 rows give the line of their label: 1, 20, 30, 62, 68, 121, 132, 134, 139, 168.
  - Each row is indented by 4 spaces, has 4 tab-separated columns and is ASCII.
  - Merged, the crosswalk has 501 rows for 501 labels, in the same order. The new labels are lowercase.
- **Format.**
  - The longest chapter-text line has 120 characters (P:5), also with every label resolved. Apart from the crosswalk
    rows, the notes are at most 121.
  - No wrapped chapter-text line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|".
  - The chapter text names no file or program, and has no code and no AI language.
- **Sources.** The writer's one-line source (scratchpad/reader/pgrd17/src.md) rebuilds the file to md5 10d83c5c, with
  rest.md, ptr.txt and the writer's wrap.py, pad.py and build.py. I made the fixed copy the same way (§9).

## 2. The scoping (P:3–18, Comparison item 1)

**𝔰_g^(m) is a maximum.**
- def:tl5-hfg-graded (87:5051–5052) defines 𝔰_g^(m) as the maximum of μ|H|, μ^((|B|+2)/2)|Ψ_B|, μ^((|B|+3)/2)|D̂Ψ_B|
  and μ^((|B|+4)/2)|D̂²Ψ_B| (|B| ≤ m) over the words.
- The step at low levels (87:5185–5193; 87:5585–5590; 87:5873–5879; 87:5887–5889; 87:6827–6834) bounds each
  μ^((|B|+4)/2)|D̂²Ψ_B(p)| and then takes the largest of the four steps. So a bound of each D̂²Ψ_B separately suffices. ✓

**What the recovery of Ψ_B at p needs.**
- Through lem:tl5-hfz-rec with 𝔥 = 𝔰₁^v (87:6482–6483) and 𝔣 as in the proof of lem:tl5-hfz-words (b) (87:4332–4333,
  87:6513–6515), it needs three things:
  - the seven D̂ℒ_ZΨ_B = D̂Ψ_(ZB);
  - D̂Ψ_B and Ψ_B, in 𝔷_Z and 𝔯_♯|Ψ_B|;
  - |𝔣|. ✓
- **The commutators.** By def:tl5-hf-coupling (87:4077–4098), every term (𝔏_(Z_S)𝒦[π^(Z_k)])Ψ_(J(k,S)) of
  eq:tl5-hf-system goes into the maps 𝔄_BJ and 𝔔_BJ. The words J(k, S) have length below |B|.
  - Their D̂²Ψ_J are replaced by ℛ_p, recursively. This brings in D̂Ψ_(ZJ), with |ZJ| ≤ |B|, and L̂Ψ_J.
  - So the 𝔄_BJ act on jets of words with |J| ≤ |B|, none of the form ZB. 𝔄_∅J = 0, as L̂Ψ_∅ = 𝔤. ✓
- **Anything else summed over the words?**
  - The residual (1 − 𝔰₁^v)⁻¹|Σ_J 𝔔_BJ ℒ^J(2R̂ic)| ≤ k₂^zϱ(p) sums coupling norms through q₁, not a family of jets.
  - The nonlinear part 𝔑′_B is absorbed through k₃ (87:5190–5192, 87:5888), with the factor of largest order bounded
    by 𝔰_g^(m).
  - Neither counts the 7^b words.
  - In the part with ℰ_g, all words enter only through L_g, and only the couplings need L_g. ✓
- **The parts with ϱ(p) and η₀(p).** These do count all the words: in lem:tl5-hfp-low (87:6831–6832), L_g's parts are
  (2𝔐^(m))^(1/2) times the largest part of one jet.
  - The section keeps them, and the chapter text says so in the opening, the lemma and the Remark.
  - It proves its own parts smaller (§4), so keeping them is a valid choice, not a gap.
  - The Comparison's "Not done" leaves only the couplings' share of L_g. That share is 0.2–0.3 % of k₁.

## 3. lem:tl5-hfn-fam (P:20–60) holds

**The family.** For |B| ≤ N − 4 the words ZB are distinct and have the one length b = |B| + 1 ≤ N − 3. So
lem:tl5-hfp-words and lem:tl5-hfp-c1 apply to ΓB: their proofs use of a family only that its words are distinct and of
one length at most N − 3, and so does the form that the proof of thm:tl5-hfe gives (87:7450–7459).
- **Weights.** 𝔬_J = (𝔶_(|J|)μ^(|B|+4))^(1/2) ≤ μ^((|JZB|+1)/2), as 𝔶_k ≤ μ^(k−2). Also
  𝔶_(|J|)μ^(|B|+4) ≤ μ·μ^(|JZB|). The step divides by μ^((b+3)/2) = μ^((|B|+4)/2). So "μ^(|B|+4) and μ^(−(|B|+4)/2) in
  place of μ⁴ and μ^(−2)" is right, and so is the exponent of eq:tl5-hfn-fam. ✓
- **What lem:tl5-hfk-fam uses of Γ and N = 4.** I reread 87:7897–7953. Beyond the family's being of one length, it
  uses only these:
  - that the members are indexed by the seven fields, so that 𝒳_p acts on the index Z;
  - that the coefficients |T(p)|⁻¹ and c^ab_j(p) are numbers, so that ℒ^J and D̂ pass through the combinations Ã_i;
  - lem:tl5-hf-fields (a) at p, which acts on the tensors at every point of the face and of S_a in the norm there.
  The lemma in use, 𝔗(𝔶), w, P_ϱ and E₀ are all defined for every N. At N ≥ 6 the lemma in use is
  lem:tl5-hfs-linfty, or lem:tl5-hft-small (a) or (b). lem:tl5-hfq-theta is level four only (def:tl5-hfq-constants).
  So the carry-over is sound. ✓
- **The face estimate.** Ã₀ = |T(p)|⁻¹D̂Ψ_(TB) and Ã_j = Σ c^ab_j(p)D̂Ψ_(K_ab B) are fields of rank three on Q(a, b).
  Their regularity is that of the D̂Ψ_(ZB), |ZB| ≤ N − 3, as for lem:tl5-hfp-c1. eq:tl5-hfe-face applies to them. ✓

**The three kinds, for the words JZB, Z′JZB and σZB.**
- *First kind.* There are three families: the leading terms D̂Ψ_(JZB), the remainders R′_(J,ZB) and D̂R′_(J,ZB), and,
  in the face recovery of D̂²Ψ_(JZB) at q, the leading term through Z′JZB and the terms with 𝔷_(Z′) and 𝔯_♯.
  - Each family is bounded in the Euclidean norm through 𝒟_g or 𝒥_g. The words are distinct for distinct indices:
    (J, Z) ↦ JZB, (Z′, J, Z) ↦ Z′JZB, and Z ↦ σZB for each σ. Minkowski's inequality runs over the monomials.
  - |y|_Γ ≤ K_rec(p)|y|, so each part takes K_rec(p). K_rec(q) stays inside k₁^D on the face, as at level four. ✓
- *Second kind.* These are the nonlinear part, the part with ϱ, and the terms on S_a.
  - The nonlinear part is 𝔬_J(1 − 𝔰₁^v)⁻¹|𝔑′_(JZB)| ≤ 𝔵^z(k₁^D𝒟_g + (k₁^p − k₁^D + 2)𝒥_g)/(1 − 𝔵^z). Its 𝔐 bounds
    the words of length |JZB| = |J| + |B| + 1, so it depends on J only.
  - The part with ϱ is 𝔬_J𝔢_(|J|)P_ϱ, with w fixed by b. It too depends on J only.
  - On S_a, |JZB| ≤ N − 1, so η₀ bounds D̂Ψ_(JZB), and the bound of the remainders is the same for all Z.
  - So y_(J,Z) = u_J, and |y|_Γ = 𝔨_Γ(Σ_J u_J²)^(1/2) against √7(Σ_J u_J²)^(1/2). ✓
- *Third kind.* Component (J, Z) of the map of 𝔞_𝔄(ΓB) is Σ_K(𝔶_(|J|)μ^(b+3−|K|))^(1/2)𝔄_(JZB,K)ξ_K, with b = |B| + 1.
  - Weighted by |T(p)|⁻¹ on Z = T and by λ_M(p)^(−1/2) on the rotations, the family has the norm |·|_Γ at most
    (1 − 𝔰₁^v)⁻¹𝔞_𝔄^k(ΓB)𝒥_g. ✓

**The last claims.**
- 𝔞_𝔄^k(ΓB) ≤ K_rec(p)𝔞_𝔄(ΓB): a diagonal of norm at most K_rec(p) follows the map.
- 43^(1/2)𝔨_Γ/K_rec(p) ≤ 301^(1/2), as 𝔨_Γ ≤ √7K_rec.
- The integrands of C₁^(U,l), C₁^(D,l) and C₁^(J,l) depend on the family only through (43n)^(1/2) and 𝔞_𝔄. Both enter
  with nonnegative coefficients: k₁^D𝔵^z/(1 − 𝔵^z), 𝔵^z(k₁^p − k₁^D + 2)/(1 − 𝔵^z) and (1 − 𝔰₁^v)⁻¹, as k₁^p ≥ k₁^D.
  The minimum of nondecreasing functions is nondecreasing. So C₁^k(ΓB) ≤ K_rec(p)C₁^l(ΓB). ✓
- The sentence that draws these claims runs them together. "…numbers at most K_rec(p), 43^(1/2) 𝔨_Γ/K_rec(p) ≤
  301^(1/2)…" reads as a list of numbers (n3).
- **Random test** (scratchpad/reader/rpgrd17/tools/spot.py, nice 19), 1500 random maps with 7·k rows:
  - restricting the output components never raises the operator norm;
  - weighting the rows by |T|⁻¹ and λ_M^(−1/2) never exceeds K_rec times it;
  - 0 failures.

## 4. lem:tl5-hfn-low (P:62–119) holds

**The step through lem:tl5-hfk-rec (b).** |H(p)| ≤ 𝔰(p) ≤ 𝔰₁^v, so lem:tl5-hfk-rec (b) with 𝔥 = 𝔰₁^v applies to Ψ_B at
p. Times μ^((|B|+4)/2), each term of the linear part is bounded as follows.
- **Leading term:** by eq:tl5-hfn-fam, C₁^k(ΓB)ℰ_g^(1/2) plus 𝔨_Γ times the parts of one jet D̂Ψ_(ZB), whose weight
  in the step is μ^((|B|+4)/2). ✓
- **𝔷₁^k|D̂Ψ_B|:** μ^((|B|+4)/2) = μ^(1/2)μ^((|B|+3)/2), and eq:tl5-hfp-family with 𝔚 = {B} (n = 1) gives
  μ^(1/2)C₁^l({B}). That is sharper than the step's C₁^l, and admissible. ✓
- **𝔷₂^k|Ψ_B| and 𝔯_♯|Ψ_B|:** the weight is μ·μ^((|B|+2)/2), giving μC_S^f.
  - lem:tl5-hff-zero gives C_S^f for 1 ≤ |B| ≤ N − 2 and C_S^h for h, in every lemma in use, so in both options.
  - The routes do not touch the zeroth order.
  - So C_S^h for B = ∅ and C_S^f otherwise is right everywhere. 𝔐_p^(m) in its form with index f carries the same two
    (87:7755–7756), so the comparison with 𝔐_p^(m) uses like for like. ✓
- **Couplings:** μ^((|B|+4)/2)(|D̂Ψ_J|² + |Ψ_J|²)^(1/2) ≤ μ^((|B|+1−|J|)/2)L_g for |J| ≤ |B|.
  - So the part is at most (1 − 𝔰₁^v)⁻¹2^(−1/2)α_𝔄^(m,μ)L_g ≤ (1 − 𝔰₁^v)⁻¹α_𝔄^(m,μ)(𝔐_p^(m)ℰ_g^(1/2) + …).
  - L_g covers |C| ≤ m + 1 ⊇ |J| ≤ |B|. So the coupling part is rightly bounded by 𝔐_p^(m). ✓
- **lem:tl5-hft-small (a).** Here the step is unweighted, and the same bounds give μ^(−(|B|+4)/2)𝔐_n^(m)ℰ_g^(1/2), as
  w = 1 and E₀ is the unweighted part there. ✓
- **So** 𝔨_rec^n(B) + (1 − 𝔰₁^v)⁻¹α_𝔄^(m,μ)𝔐_p^(m) bounds the part with ℰ_g for each B, and the maximum is 𝔐_n^(m). ✓

**The parts with ϱ and η₀ are at most those of the step.**
- The two displays at P:100–101 recompute exactly from the per-term parts, with ν′ = μ in lem:tl5-hfs-linfty and
  lem:tl5-hft-small (b), and ν′ = 1 in lem:tl5-hft-small (a). The weights are as follows:
  - the jet D̂Ψ_(ZB) carries 1;
  - D̂Ψ_B carries ν′^(1/2);
  - Ψ_B carries ν′.
- The step's parts are k₁^(m,ν′,p)(2𝔐^(m))^(1/2)ē_ϱ and the same times ē₀. They match C_((∞,ϱ),μ)^(m) and
  C_((∞,0),μ)^(m) in their index-f forms, with max(C_(0,0)^h, C_(0,0)) in ē₀ (87:7756–7757). In (a) they carry
  k₁^(N−4,1,p) (87:5876–5877).
- **The inequalities.**
  - 𝔐^(m) ≥ 8 gives (2𝔐^(m))^(1/2) ≥ 4 ≥ √7.
  - 𝔨_Γ ≤ √7K_rec.
  - 𝔷₁^k + 𝔷₂^k ≤ K_rec(𝔷₁′ + 𝔷₂′) ≤ √2K_rec𝔷′.
  - ν′ ≤ ν′^(1/2) ≤ 1.
  Each coefficient is then at most k₁^(m,ν′,p)(2𝔐^(m))^(1/2), term by term. The coupling terms are equal. ✓
- **Random test.** In 200,000 trials (random |T|⁻¹, λ_M^(−1/2), |D̂Z|, |D̂²Z|, 𝔨_♯ ∈ [√5, 2.45], 𝔰₁^v ≤ 1/16,
  ν′ ∈ {1} ∪ (0, 1], m ≤ 4) I checked both coefficient inequalities and 𝔷₁^k + 𝔷₂^k ≤ √2K_rec𝔷′. There were
  0 failures.

**𝔐_n^(m) ≤ k₁^(m,μ,p)𝔐_p^(m).**
- C₁^k(ΓB) ≤ K_rec C₁^l(ΓB) ≤ K_rec C₁^l(𝔚_(|B|+1)) ≤ K_rec𝔐_p^(m), as |B| + 1 ≤ m + 1.
- **Subfamily monotonicity.**
  - The map of 𝔞_𝔄(𝔚′) is that of 𝔞_𝔄(𝔚) followed by a coordinate projection. Both have the same input space, the
    jets of length at most b + 2, as the length is the same.
  - The integrands are nondecreasing in the count and in 𝔞_𝔄, pointwise on the face, so their suprema are too.
  - {B} ⊂ 𝔚_(|B|) is equality for B = ∅. ✓
- By Cauchy–Schwarz, 𝔷₁^kμ^(1/2)C₁^l({B}) + 𝔷₂^kμC_S^f ≤ μ^(1/2)(𝔷₁^k² + 𝔷₂^k²)^(1/2)(C₁^l(𝔚_(|B|))² + C_S^f²)^(1/2),
  and this is at most μ^(1/2)K_rec𝔷′𝔐_p^(m).
  - The two numbers in the root are the terms of 𝔐_p^(m) with b = |B| ≤ m (C_S^h for b = 0).
  - μ𝔯_♯C_S^f ≤ μ^(1/2)𝔯_♯𝔐_p^(m).
  - This holds for all weights, routes and options, as it is pointwise algebra. ✓
- **Random test.** In the same 200,000 trials, with families constrained as in the lemma, 𝔨_rec^n(B) never exceeded
  (𝔨_♯K_rec(1 + μ^(1/2)𝔷′) + (1 − 𝔰₁^v)⁻¹μ^(1/2)𝔯_♯)𝔐_p^(m), and 𝔐_n^(m) never exceeded k₁^(m,μ,p)𝔐_p^(m).
- **A letter.** In the paragraph of the last claims, B names both a member of 𝔚′ and the fixed word of the lemma (n2).

## 5. The definition, the theorem, the closing condition and the Remark

**The sites of the entry.** I grepped every C_(∞,μ), C_∞^(m), C_P^♮ and 𝔐_p in 87.
- The entry k₁^(m,μ,p)𝔐_p^(m) is formed at 87:5139, with the replacements of 87:5548–5549, 6681, 7413–7414, 7570 and
  7755–7756.
- At N ≥ 6 it enters only in two places:
  - **C_P^♮ = C_(∞,μ)^(m_P), m_P = 1** (87:5648). It reaches 𝔎 (87:5655, in index f max(C_P⁰𝔨_A, C_P^♮𝔨_B)),
    𝔞_(o,s) and 𝔞_(i,s), 𝔎^D (87:7197–7198) and S_F, so B and the closing condition. Through B it also reaches Y.
  - **The term of 𝔰_* with A,** through C_(∞,μ)^(N−4) in both options (87:5910–5915).
- So both 𝔐_p^(1) and, at N = 6, 𝔐_p^(2) are replaced.
- The forms with ν (87:6026, 6098) are level four only. The definition names the sites: C_P^♮, 𝔎, 𝔎^D, S_F and 𝔰_*. ✓
- **𝔯 and ε do not move.**
  - 𝔯 has 𝔣₀ and 𝔣₁ times C_(P,ϱ) and C_(P,0), 𝔎_ϱ, 𝔎₀, 𝔎^D_ϱ, 𝔎^D₀ (87:5657–5658, 7199–7200), and on route (𝔯)
    𝔯_ϱ^f with C_P⁰ (87:7762). None carries the entry.
  - ε^f has no C_P on either route.
  - 𝔰₁^v does not involve the entry (87:5652, 5909, 5912 and 6216).
  - So 𝔯^n = 𝔯^f, η_n = η_f and A_n = A_f. The theorem states ε^n = ε^f, η_n ≥ η_f and A_n ≤ A_f, which is correct and
    suffices. The Comparison records the equalities as deduced. ✓

**The theorem.**
- (a)–(c) are those of thm:tl5-hff with index n, with S_M = ε_M = 0 at N ≥ 6.
- eq:tl5-hfn-closing is 4A_nB_n = 4η_n^(−3/2)(δ_w + η_n^(−1/2)ε^n)S_F^n. ✓
- The setting of thm:tl5-hff carries 𝔶₀^h, the option and the route. No hypothesis is missing.
- 𝔰 ≤ 𝔰₁^v on Q(a, b) holds where the bounds at a point are formed: in Step 1 for σ ∈ Σ_* (as in the proof of
  thm:tl5-hfz, 87:6576–6578), and in Steps 2 and 3 on D^κ_s. So lem:tl5-hfn-low applies.
- The bounds at a point are formed from the four steps, the absorption ((1 − 𝔵^z)⁻¹, lem:tl5-hfy-abs) and the maximum,
  in the same way for all constants.
- Step 2 uses 𝔰_P (87:5704–5705) and Step 3 bounds it through C_P^♮ (87:5711). Route (𝔯) uses 𝔰_P⁰ only (87:7802–7803).
  So the one change suffices. ✓

**Containment.**
- Every constant with index f is nondecreasing in the entry, so each constant with index n is at most the one it
  replaces. Then 4A_nB_n ≤ 4A_fB_f < 1.
- Y = 2A/(1 + (1 − 4AB)^(1/2)) is nondecreasing in A and in B, so Y_n ≤ Y_f.
- 𝔰_*^n ≤ 𝔰_*^n[Y_f] ≤ 𝔰_*^f < 𝔰₁^v.
- So the hypotheses of thm:tl5-hff at N ≥ 6 imply those of thm:tl5-hfn, for every admissible weight, route and option,
  with no new choice. ✓
- At N = 4 nothing changes: every new object carries N ≥ 6, and thm:tl5-hfk is untouched. ✓
- The Comparison states this correctly at P:219–221, but once the wrong way round at P:234–235 (m2).

**The opening (P:3–18) and the Remark (P:168–187), word by word.**
- Each mechanism matches the proofs:
  - the scoping;
  - the family ΓB through 𝒳_p, as lem:tl5-hfk-fam;
  - 𝔷₁^k, 𝔷₂^k and C₁^l({B}), C_S^f or C_S^h for the one word;
  - only the couplings through L_g;
  - the parts with ϱ and η₀ kept;
  - the sites C_P^♮ and the term of 𝔰_* with A.
- The Remark's "nonlinear parts carrying 43^(1/2)𝔨_Γ where those of the family of length b carried
  K_rec(p)(43·7^b)^(1/2)" is right, with 𝔨_♯ outside both.
- "In C₁^k(ΓB) … the terms with one bound for the seven words take 𝔨_Γ" is right, as within C₁^k(ΓB) those are the
  nonlinear parts.
- "𝔨_rec^n(∅) has the form of 𝔨_rec^k … with C₁^l({∅}) in place of C₁^l" is exact against eq:tl5-hfk-krec (87:7959).
- One sentence differs from the definition: "The quantity 𝔰_g^(m) is the largest of the low quantities" (P:168). That
  largest is 𝔰. 𝔰_g^(m) is the largest of the weighted low quantities, with the second derivatives only for |B| ≤ m, as
  the opening says (n1).
- The chapter text records no obstruction. Lever B's obstruction is in the notes only (§6).

## 6. The Comparison

**The figures, each checked against G0r.**
- **§G0r.1.** These are all quoted exactly:
  - f binds alone, with f ∝ 𝔰₁^v/sup(C_(∞,μ)^(2)μ^(−3)e^(φ/2));
  - ϱ is 4.0–7.9 decades above f, and the closing 2.9–5.2 away;
  - 𝔰₁^v = 𝔰₀/2 = 1/(4k₃) in D_A;
  - ϑ's cap is 1.48 and 1.14 times higher;
  - k₁ is the recovery factor to 99.7 %. ✓
- **§G0r.0.** 𝔰₁^v = 4.0 × 10⁻⁵ at seed 1 D_A, so 𝔰_♭/𝔰₀ = 10⁻⁴/(8 × 10⁻⁵) = 1.25 (deduced). ✓
- **§G0r.3 items 1–3.** These are all exact:
  - the T part leads K_rec at every level-4 face point (100 %);
  - the ÷ 2 prices +0.285 / +0.254 / +0.295 / +0.293 (𝔨_rec^p's C₁ term) and +0.286 / +0.295 / +0.276 / +0.295
    (𝔐_p's C₁ part);
  - sup C_P^v/sup C_P⁰ = +1.02 / +1.17 / +1.20 / +1.43. ✓
- **§G0r.4 item 1.** These are all exact:
  - kind 1 is 68.8 / 69.6 / 71.2 / 70.9 %;
  - kind 2 is 28–30 % (29.7 / 30.1 / 28.0 / 28.0);
  - round 16's gains are +0.035 to +0.077;
  - ω = 𝔨_Γ/(√7K_rec);
  - C₁^k/(K_rec C₁^(Γ,l)) = 0.850 / 0.866 / 0.901 / 0.902, so w = −log₁₀ = 0.0706 / 0.0625 / 0.0453 / 0.0448, printed
    0.071 / 0.062 / 0.045 / 0.045. ✓
- **§G0r.4 item 2.** The values are all exact:
  - −0.62 / −0.61 / −0.61 / −0.59 and −0.70 / −0.70 / −0.66 / −0.68 (suprema apart −0.62 / −0.60 / −0.62 / −0.59 and
    −0.70 / −0.69 / −0.67 / −0.68);
  - +0.08 and +0.11 / +0.11 / +0.09 / +0.10 above the one-word C₁;
  - α_𝔄 0.3 / 0.3 / 0.2 / 0.3 % at the point holding sup k₁𝔐_p^(2);
  - C₁ 1.1–1.3 decades below k₁𝔐_p^(2);
  - C₁^l({ZB})/𝔐_p^(1) 0.32–0.37 below. My recomputation from −0.62 + 0.26 etc. gives 0.32–0.37. ✓
  - **But the point is mis-stated.** G0r measures every ratio of that table at "the point holding sup C_P^v, where
    k₁𝔐_p^(1) leads". Only the α row the Comparison uses is at the point holding sup k₁𝔐_p^(2). At G0r's point α is
    0.1 / 0.2 / 0.1 / 0.1 % (m1).
- **The line citations** of items 1–4 (87:4028, 4096–4097, 4332–4333, 4355–4360, 5051–5052, 5185–5193, 5585–5590,
  5873–5879, 5887–5889, 6241–6243, 6467–6468, 6482–6483, 6794, 6827–6834, 7197–7198, 7604–7605, 7720, 7802,
  7914–7918) all point at the passages named. The quotation "the terms with D̂Ψ_(ZB) are bounded by L_g as there" is
  exact (87:5585–5586).

**The arithmetic, recomputed** (scratchpad/reader/rpgrd17/tools/figs.py).
- The lower figures −log₁₀(r + (1 − r)α) are:
  - with the printed r and α = 0.3 / 0.3 / 0.2 / 0.3 %: 0.6159 / 0.6060 / 0.6073 / 0.5863 and
    0.6948 / 0.6948 / 0.6569 / 0.6751;
  - with the suprema apart: 0.6159 / 0.5961 / 0.6173 / 0.5863 and 0.6948 / 0.6850 / 0.6668 / 0.6751.
  All match the printed figures. ✓
- With G0r's α at G0r's point they would be 0.619 / 0.607 / 0.609 / 0.589 and 0.698 / 0.697 / 0.659 / 0.678. So the
  printed lower figures are the smaller, and stand.
- **Lever C.**
  - log₁₀ 1.25 = 0.097, log₁₀ 1.48 = 0.170 and log₁₀ 1.14 = 0.057: printed +0.10, +0.17 and +0.06. ✓
  - 𝔵^z = 𝔰₁^v(5/8)(1 − 𝔰₁^v)⁻¹ sup k₃ goes from 5/32 at 𝔰₁^v = 1/(4 sup k₃) to about 1/4 at (8/5)(1 − 𝔥) times that. ✓

**The deductions.**
- The bound 𝔐_n^(2)/(k₁𝔐_p^(2)) ≤ r + (1 − r)α is right. Every non-coupling term is at most r times its counterpart:
  the 𝔷 terms because (C₁^l² + μC_S²)^(1/2) ≤ C₁^l({ZB}), with μC_S² ≈ 10⁻⁵·0.02𝔐_p² against 0.45C₁^l².
- The upper figure (i) is right: the entry is at least 𝔨_♯C₁^k(ΓB) = 10^(−w)𝔨_♯K_rec C₁^l(ΓB).
- The caps (ii) are hard: the other entries do not move.
- **Marking.**
  - The figures are marked deduced, not evaluated.
  - The falls carry "every supremum at one point".
  - The lower figures are labelled as such.
  - Upper and lower are kept apart.
- **Two qualifications are missing.**
  - "Upper figures" for the gains of the target hold at the parameters of the P-GRD15 optimum. A re-optimisation of μ,
    x or ϑ may add to them: round 15's gains exceeded both fixed-parameter figures, through the move of 𝔰₁^v
    (G0r §G0r.0). The text says "at fixed parameters" for the lower figures but not for the gain (n7).
  - "Worth log₁₀ q for a factor q as G0r says" (P:320) is not in G0r. It follows from G0r's f ∝ 𝔰₁^v and
    𝔰₁^v = 1/(4k₃) (n6).
- **Not beyond what is proved.**
  - Lever B is stated as an obstruction for these bounds, with its needs, and nothing is drafted.
  - Lever C is scoped, with its sketch marked unchecked.
  - "Not done" names the couplings' 𝔐_p^(m−1) with its share.
  - P-GRD16's scoping did propose new parts with ϱ and η₀ (P-GRD16 at 810ef3a6, its lines 369–377), so "not needed" is
    a fair account.
- **On the report, not the file.** Its §5 says the level-6 gain is "at least 0.69 / 0.69 / 0.65 / 0.67 at fixed
  parameters". That holds only under the first assumption. The file itself claims no lower figure for the gain.

**Smaller points in the notes.**
- "the second kind of C₁(ΓB) (the nonlinear part, the part with ϱ, the terms on S_a)" (P:279). The part with ϱ and the
  terms on S_a lie in the parts with ϱ(p) and η₀ of eq:tl5-hfn-fam, not in C₁(ΓB), as G0r §G0r.4 item 1 notes for Γ
  (n4).
- θ is listed among the unchanged weights (P:247) and then names an energy share (P:292–294) (n5).

## 7. Form, and the index letter n

- The form checks of §1 pass on the original and on the fixed copy.
- **The index letter n.** I judge that it does not confuse a reader, so no fix is proposed.
  - η_n, A_n, B_n, Y_n, 𝔐_n, S_F^n, 𝔯^n, ε^n, 𝔰_*^n and 𝔨_rec^n occur nowhere else in 87 (grep). The only other n
    subscripts in 87 are the counts and levels 𝔠_n, 𝔠^♮_n, 𝔠^ϱ_n, Σ^m_n, Λ_n and I_n of earlier sections, and n := |I|
    inside lem:tl5-hff-rho.
  - Within sec:tl5-hfn, n is never a count or a level. The cited counts are written out: 301^(1/2), "the count
    (43 · 7)^(1/2) of the family", "the factor √7", "the number of the words of the family". The text never writes
    (43n) or n^(1/2), where a reader would meet the clash.
  - The pattern "the constants with index n", with η_n, A_n, B_n and Y_n, is that of indexes f, c, l and k, and the
    definition states it. 𝔐_n^(m) always carries its (m) and stands beside 𝔐_p^(m) as 𝔨_rec^n stands beside 𝔨_rec^p.
  - A_n and B_n beside A_j and B_j of the proof of prop:tl5-hfs-bootstrap (87:5699) are in different sections and
    roles. The writer chose n over j for that reason.
- **Local letters.**
  - ē_ϱ, ē₀ and ν′ are new or reused in the proof of lem:tl5-hfn-low only. The use of ν′ (= μ or 1) is the chapter's
    own, as in k₁^(j,ν′,p).
  - The one clash inside a proof is n2.

## 8. Findings

**m1 (minor), P:345–349 and P:355, Comparison: where G0r measured r, and which α the figures use.**
- **The text.**
  - "The entry at the point holding sup k₁𝔐_p^(2), seed 1 D_A / … G0r §G0r.4 item 2: log₁₀ C₁^l({ZB})/𝔐_p^(2) = −0.62
    / … ; α_𝔄 is 0.3 / 0.3 / 0.2 / 0.3 % of k₁ there."
  - Later: "… with the printed r and α".
- **What is wrong.**
  - G0r §G0r.4 item 2 fixes its point in its heading: "the point is the one holding sup C_P^v, where k₁𝔐_p^(1) leads".
    The rows of C₁^l({ZB})/𝔐_p^(2), of 𝔐_p^(1)/𝔐_p^(2) and of C₁^l({ZB})/C₁ are at that point.
  - Only the row "the same at the point holding sup k₁𝔐_p^(2) (in 𝔰_*'s supremum)", α_𝔄's share 0.3 / 0.3 / 0.2 /
    0.3 %, is at the point the bullet names. At G0r's point α_𝔄 is 0.1 / 0.2 / 0.1 / 0.1 %.
  - So the bullet places r at the wrong point, and the lower figures combine figures from two points. The Comparison's
    own bullet at P:369–370 cites the same item correctly, "at the point holding sup C_P^v".
- **Why it is minor.**
  - It is in the notes, and every value is printed right.
  - Under the first assumption the two points are one.
  - The larger α gives the smaller lower figures, so the printed 0.616 / … and 0.695 / … stand as lower figures at G0r's
    point.
- **Fix (applied).**
  - The bullet becomes: "The entry, seed 1 D_A / seed 2 D_A / seed 1 D* / seed 2 D*, at the point where G0r §G0r.4 item
    2 measures it, the one holding sup C_P^v, where k₁𝔐_p^(1) leads: log₁₀ C₁^l({ZB})/𝔐_p^(2) = [as printed] (… with
    the suprema taken apart), C₁^l({ZB}) being C₁^l(ΓB); C₁^l({ZB}) is [as printed] above the one-word C₁; α_𝔄 is 0.1 /
    0.2 / 0.1 / 0.1 % of k₁ there and 0.3 / 0.3 / 0.2 / 0.3 % at the point holding sup k₁𝔐_p^(2), where 𝔰_*'s supremum
    sits. The figures below take r at G0r's point and the larger α, as if the two points were one (the first assumption);
    the larger α gives the smaller lower figures."
  - "with the printed r and α" becomes "with the printed r and the larger α".

**m2 (minor), P:234–235, Comparison, "Containment": the direction.**
- **The text.** "… no earlier theorem is changed, and thm:tl5-hff at N ≥ 6 is implied by the hypotheses of thm:tl5-hfn."
- **What is wrong.** The hypotheses of thm:tl5-hfn are the weaker ones. They do not imply those of thm:tl5-hff: Y_f
  need not even exist when 4A_nB_n < 1 ≤ 4A_fB_f. The containment the section proves is the converse. That converse is
  stated rightly in thm:tl5-hfn and at P:219–221.
- **Why it is minor.** It is in the notes, and the chapter text is right. But it misstates the one property the
  conventions require to be stated exactly.
- **Fix (applied).** "… no earlier theorem is changed, and the hypotheses of thm:tl5-hff at N ≥ 6 imply those of
  thm:tl5-hfn."

**n1 (nit), P:168, rem:tl5-hfn-what: what 𝔰_g^(m) is.**
- **The text.** "The quantity 𝔰_g^(m) is the largest of the low quantities, so …"
- **Why.** The largest of the low quantities is 𝔰. 𝔰_g^(m) is the largest of the weighted ones, with the second
  derivatives only for |B| ≤ m (def:tl5-hfg-graded). The opening says "the largest of its quantities", and summaries are
  held to the proof word for word.
- **Fix (applied).** "The quantity 𝔰_g^(m) is the largest of its weighted quantities, so …"

**n2 (nit), P:110–111, proof of lem:tl5-hfn-low: the letter B.**
- **The text.** "… followed by the restriction to the components of the pairs (J, B) with B ∈ 𝔚′, of norm at most 1 …"
- **Why.** In the same paragraph B is the fixed word of the lemma (ΓB ⊂ 𝔚_(|B|+1), {B} ⊂ 𝔚_(|B|)).
- **Fix (applied).** "… the pairs (J, C) with C ∈ 𝔚′ …"

**n3 (nit), P:57–60, proof of lem:tl5-hfn-fam: the last claims.**
- **The text.** "… followed by the multiplication of its components by numbers at most K_rec(p), 43^(1/2) 𝔨_Γ/K_rec(p) ≤
  301^(1/2) by [[lem:tl5-hfk-rec]] (a), and the functions … are nondecreasing in that count and in 𝔞_𝔄(ΓB), as k₁^p ≥
  k₁^D. ∎"
- **Why.** The comma makes 43^(1/2)𝔨_Γ/K_rec(p) read as one of the "numbers at most K_rec(p)". Neither conclusion,
  𝔞_𝔄^k(ΓB) ≤ K_rec𝔞_𝔄(ΓB) nor C₁^k(ΓB) ≤ K_rec C₁^l(ΓB), is drawn.
- **Fix (applied).** "… by numbers at most K_rec(p), so 𝔞_𝔄^k(ΓB) ≤ K_rec(p) 𝔞_𝔄(ΓB); 43^(1/2) 𝔨_Γ/K_rec(p) ≤ 301^(1/2)
  by [[lem:tl5-hfk-rec]] (a); and the functions … are nondecreasing in that count and in 𝔞_𝔄(ΓB), as k₁^p ≥ k₁^D, so
  C₁^k(ΓB) ≤ K_rec(p) C₁^l(ΓB). ∎" This adds one line.

**n4 (nit), P:279, Comparison item 1: the second kind.**
- **The text.** "So the second kind of C₁(ΓB) (the nonlinear part, the part with ϱ, the terms on S_a) takes 𝔨_Γ …"
- **Why.** Only the nonlinear part is in C₁(ΓB). The part with ϱ and the terms on S_a lie in the parts with ϱ(p) and η₀
  of eq:tl5-hfn-fam, as G0r §G0r.4 item 1 notes for Γ.
- **Fix (applied).** "So the second kind (the nonlinear part of C₁(ΓB), and the part with ϱ and the terms on S_a, which
  lie in the parts with ϱ(p) and η₀ of eq:tl5-hfn-fam) takes 𝔨_Γ …" The sub-bullet is re-wrapped.

**n5 (nit), P:292–294, Comparison item 2: the letter θ.**
- **The text.** "E_T ≤ θℰ_g(p) at the supremum with θ < 1, … (θ|T|⁻² + (1 − θ)λ_M⁻¹)^½ … Nothing in the chapter gives θ"
- **Why.** θ is the level-four parameter of def:tl5-hfq-constants, which P:247 lists among the unchanged numbers.
- **Fix (applied).** θ_T in place of θ, four times.

**n6 (nit), P:320, Comparison item 3: "as G0r says".**
- **The text.** "A smaller k₃ that keeps 𝔵^z, worth log₁₀ q for a factor q as G0r says, …"
- **Why.** G0r does not state this. It follows from G0r's f ∝ 𝔰₁^v/sup(…) and 𝔰₁^v = 1/(4k₃) in D_A (§G0r.1).
- **Fix (applied).** "… worth log₁₀ q in D_A for a factor q, as f ∝ 𝔰₁^v = 1/(4 sup k₃) there (G0r §G0r.1; deduced), …"

**n7 (nit), P:339–341 and P:365, Comparison: the gains at fixed parameters.**
- **The text.** "… and the gains through the theorem are upper figures;" and "So the gain of the level-6 target is at
  most the smaller of 1.1–1.3 and the fall, …"
- **Why.** These are upper figures at the parameters of the P-GRD15 optimum. A re-optimisation may add to them, as round
  15's gains exceeded both of its writer's fixed-parameter figures (G0r §G0r.0). The lower figures are already marked
  "at fixed parameters".
- **Fix (applied).**
  - "… and the gains through the theorem are upper figures at the parameters of that optimum (a re-optimisation of μ, x
    or ϑ may add to them, as round 15's did, G0r §G0r.0);"
  - "So at fixed parameters the gain of the level-6 target is at most …"

## 9. The fixed copy

/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd17/P-GRD17.fixed.md

- md5 abb90f19833dbbaa8b102717289f41bb, 402 lines. Chapter text is P:1–188 (10 labels), then the Placement, the
  Comparison and the crosswalk rows.
- **How it was made.** /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd17/tools/fix.py
  applies the fixes to copies of the writer's sources, in
  /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd17/fixbuild/.
  - Each old text occurs exactly once. Each notes block is checked against its text before it is re-wrapped.
  - The writer's wrap.py and pad.py re-wrap the chapter text, and build.py rebuilds the file with the crosswalk rows
    at their labels.
  - The re-wrapped notes are at most 120 characters, with "~" as an unbreakable space inside two formulas.
- **Re-merged in a fresh tree** (`git archive 076b34f2`), it passes every check:
  - item 2 is found at 87:8037, the new line at 112 characters;
  - lint: 0 hits, 5352 labels;
  - check: 0 problems;
  - `[] 0`;
  - 0 of 5342 existing numbers change, and the 10 added have the same numbers as before;
  - the crosswalk has 501 rows for 501 labels, in order;
  - chapter-text lines are at most 120 characters, also resolved, and the notes at most 121 apart from the rows;
  - no forbidden line start in the chapter text.
- **Crosswalk lines that moved.**
  - Unchanged: sec:tl5-hfn at 1, lem:tl5-hfn-fam at 20 and eq:tl5-hfn-fam at 30.
  - Each later label moves by one line, because n3 adds a line to the proof of lem:tl5-hfn-fam:
    lem:tl5-hfn-low 62 → 63, eq:tl5-hfn-low 68 → 69, def:tl5-hfn-constants 121 → 122, eq:tl5-hfn-constants 132 → 133,
    thm:tl5-hfn 134 → 135, eq:tl5-hfn-closing 139 → 140 and rem:tl5-hfn-what 168 → 169.
  - The row notes are unchanged. The rows are regenerated with the new numbers.
- The repository was not touched, and nothing was committed.

## Verdict

**CONFIRMED WITH THE FIXED COPY.** 0 Major, 2 minor, 7 nits. All of them are applied in the fixed copy, md5
abb90f19833dbbaa8b102717289f41bb, and checked.
- The scoping is right. 𝔰_g^(m) is a maximum over the words, and in the part with ℰ_g of the step only the couplings
  𝔄_BJ, on jets with |J| ≤ |B| (𝔄_∅J = 0), need other words. The commutators enter only through 𝔄 and 𝔔, and the
  residual and the absorption count no family. The parts with ϱ and η₀ do count all the words, and they are kept.
- lem:tl5-hfn-fam is correct. The proof of lem:tl5-hfk-fam carries over to the words JZB, Z′JZB and σZB with the
  coefficients frozen at p, the weights μ^(|B|+4) and 𝔬_J at length |B| + 1, and each of the three kinds in its place.
  C₁^k(ΓB) ≤ K_rec C₁^l(ΓB).
- lem:tl5-hfn-low is correct:
  - C_S^h for B = ∅ and C_S^f otherwise are right in every option and route;
  - the couplings are rightly bounded through 𝔐_p^(m);
  - the new parts with ϱ and η₀ are at most the old;
  - 𝔐_n^(m) ≤ k₁^(m,μ,p)𝔐_p^(m) for all weights, routes and options;
  - C₁^l is monotone on subfamilies.
- The definition reaches every site of the entry: C_P^♮, 𝔎, 𝔎^D, S_F and the term of 𝔰_* with A, so both 𝔐_p^(1) and
  𝔐_p^(2) at N = 6. 𝔯 and ε do not change, and the theorem's inequalities say so correctly. The hypotheses are complete.
- The hypotheses of thm:tl5-hff at N ≥ 6 imply those of thm:tl5-hfn, with no new choice. At N = 4 nothing changes, and
  thm:tl5-hfk stands.
- The opening and the Remark state each mechanism as proved, after n1. The chapter text records no obstruction, and the
  notes' obstruction for kind 1 is stated as one for these bounds.
- The Comparison's figures are cited exactly in value. Their upper and lower figures are marked and hold after m1
  and n7.
- The index letter n needs no change.
