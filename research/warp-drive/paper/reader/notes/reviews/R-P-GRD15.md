# R-P-GRD15: an independent review of proofs/P-GRD15.md (sec:tl5-hff)

**File reviewed.** research/warp-drive/paper/reader/proofs/P-GRD15.md at a38abede, md5 4e071f06170039c3cd07f3bec8db4994,
365 lines. Its parts are:
- the chapter text, P:1–191 (11 labels);
- the Placement, P:193–215;
- the Comparison, P:217–349;
- the crosswalk rows, P:351–365.

The writer's report is notes/reports/P-GRD15.md, and the plan it was drafted from is notes/reports/P-GRD15-handoff.md.

**Base.** chapters/87-ten-l5.md, md5 532817d39a2b15e2f13150143c0678fc, 7642 lines and 5,320 labels. The file is the same
at bea115c4, the base the Placement names, and at a38abede (that commit adds only the proof and the report). Citations
below are P:n for the proof file and 87:n for the chapter.

**Verdict: CONFIRMED WITH THE FIXED COPY.** 0 Major, 1 minor, 9 nits.
- Both lemmas hold, the theorem holds, and the containment of thm:tl5-hfc holds.
- The minor finding (m1) is a replacement that the definition leaves out. It matters only for 𝔶₀^h ≠ 𝔶₀. The proof
  already forms the constant correctly, so one clause in the definition supplies it.
- A tested fixed copy applies m1 and all nine nits.

## 1. Mechanics

The scratch tree is `git archive HEAD` of paper/reader, with the Placement applied by my own merge script.

- **Placement.**
  - Item 2's two old lines occur once, at 87:7641–7642, and they are the last lines of the chapter.
  - The new pointer line has 117 characters, as stated, and fewer once its labels resolve ("Section 57.30",
    "Theorem 57.248").
  - The section then goes after a blank line. "Line 7643, as changed by item 2" is right. The chapter becomes 7835 lines.
- **Checks.**
  - `lint.py --chapters`: 62 files, 5331 labels, 0 hits.
  - `assemble.py --check`: labels 5331, 0 problems.
  - In-memory check: `[] 0`. I did not run plain `assemble.py`.
- **Numbering.**
  - 0 of the 5,320 existing printed numbers changes; 11 are added.
  - sec:tl5-hff is Section 57.30. It contains Lemma 57.245 (lem:tl5-hff-rho), Lemma 57.246 (lem:tl5-hff-zero),
    Definition 57.247, Theorem 57.248 and Remark 57.249, with displays (57.170)–(57.174). The report agrees.
- **Crosswalk.**
  - 11 of 11 rows give the line of their label: 1, 21, 29, 52, 60, 106, 116, 125, 127, 132, 171.
  - Each row is indented by 4 spaces, has 4 tab-separated columns and is ASCII.
  - Merged, the crosswalk has 480 rows for 480 labels, in the same order. The new labels are lowercase.
- **Format.**
  - The longest chapter-text line has 120 characters, also with every label resolved. The notes are at most 121.
  - No wrapped chapter-text line starts with a forbidden marker. The START flags fall only on Comparison bullets.
  - The chapter text names no file or program and has no code and no AI language.
  - The index letter f is free, as the handoff says. ε^f, 𝔯^f, η_f, A_f, B_f, Y_f, C_P⁰, C_(P,0)⁰ and 𝔯_ϱ^f occur
    nowhere else in 87.
  - The superscript ^h (𝔶₀^h, 𝔶^h, C_S^h, C_(0,0)^h) occurs nowhere else in 87. It means "of the word h", the
    solution itself, so it does not clash with the handoff's warning against h as an index letter.
  - One local symbol does clash, s in the proof of the theorem (n3).
- **Sources.** The writer's one-line source (scratchpad/reader/pgrd15/src.md), wrapped and padded by their tools,
  reproduces P:1–191. With rest.md and build.py it rebuilds the file to md5 4e071f06. I made the fixed copy the same way
  (§7).

## 2. lem:tl5-hff-rho (P:21–50) holds

**𝒮 and e^(−φ).**
- By eq:tl5-hf-source (87:3876–3878), ‖f‖²_(1,t) = ∫_(Σ₁(t,b)) e^(−φ) f² dμ dτ₂/(1 − κκ′), and ‖·‖_(2,t) likewise.
- So ‖e^(φ/2) f‖_(i,t) is the norm with φ replaced by 0, and 𝒮[e^(φ/2) f] = 𝒮₀[f]. ✓
- 𝒮 is subadditive, by Minkowski's inequality in each norm and the additivity of the outer integrals. ✓
- It is positively homogeneous: a factor c ≥ 0 that is a number comes out of each norm. ✓
- It is monotone on s ≥ 0, since the norms are. ✓
- rem:tl5-hfw-what (87:6291–6293) already uses the first two properties.

**The term with ϱ(p) and Φ₁.**
- By lem:tl5-hfe-rho (b) (87:7377–7385), a monomial of 𝔑^L_I has a term with ϱ(p) only if Φ₂ = D̂²Ψ_C.
- The proof of hfs-products (87:5604–5606) shows that Φ₁ then carries no D̂, as there are at most two in all. So Φ₁ is
  H, h or Ψ_B, low, with |B| ≤ N − 2.
- 𝔰_P⁰ := max(μ|H|, μ^((|B|+2)/2)|Ψ_B|) for |B| ≤ N − 2 (87:5474), and B = ∅ gives μ|h|. With ℓ_P(Φ) = o + 2
  (87:5205), |Φ₁| ≤ μ^(−ℓ_P(Φ₁)/2) 𝔰_P⁰. ✓
- A monomial whose factor D̂²Ψ_B is not chosen as Φ₂ has its D̂²Ψ_B as Φ₁, bounded through 𝔰_P. It has no term with
  ϱ(p) in the products lemma, so nothing is missed.

**The weight of Φ₂'s part with ϱ.**
- With option (b), the bound of M_g^(j) in lem:tl5-hft-small (b) (87:5860) gives |D̂²Ψ_C| ≤ μ^(−(|C|+1)/2)(… + 2k₂
  ϱ(p)).
- The replacements of hfy-abs and hfz-abs (87:6364–6365, 87:6474) turn 2k₂ ϱ(p) into k₂^z ϱ(p)/(1 − 𝔵^z).
- As ℓ_E(D̂²Ψ_C) = |C| + 1, the part with ϱ is μ^(−ℓ_E(Φ₂)/2) k₂^z ϱ(p)/(1 − 𝔵^z). ✓
- hfp-abs (b) changes only the part with 𝒥_g.

**The count.**
- hfs-products (87:5603–5604) gives ℓ_P(Φ₁) + ℓ_E(Φ₂) ≤ n − b + 3. For Φ₂ = D̂²Ψ_C, ℓ_E = o₂ − 1, so ℓ_P + ℓ_E ≤
  o₁ + o₂ + 1 ≤ n − b + 3.
- So μ^((n − ℓ_P − ℓ_E)/2) ≤ μ^((b−3)/2) = μ^(−3/2) μ^(b/2), as μ ≤ 1. ✓
- The old bound, from hft-products (87:5899–5901, with the replacements), is ν 𝔰^(q−1) μ^(−1/2) μ^(b/2) k₂^z
  ϱ/(1 − 𝔵^z). The ratio of the new bound to it is μ⁻¹ 𝔰_P⁰/𝔰, as stated.
- hfe-rho (a) with ν′ = μ bounds Σ ν μ^(b/2) 𝔰^(q−2) over the monomials with a factor D̂²Ψ_C by 𝔠^ϱ_n(μ). That sum
  runs over a superset of the monomials whose Φ₂ is D̂²Ψ_C. This gives the first line of eq:tl5-hff-rho. ✓

**The second line.**
- For |J| < n ≤ N, 𝔑_J = 𝔑^L_J, as N ≥ 6.
- The first line for J, times μ^((n−|J|)/2), gives μ^((n−|J|−3)/2) 𝔠^ϱ_(|J|)(μ).
- In H D̂²Ψ_J, |H| ≤ μ⁻¹ 𝔰_P⁰ (ℓ_P(H) = 2), and the part with ϱ of D̂²Ψ_J carries μ^(−(|J|+1)/2). So μ^(n/2) μ⁻¹
  μ^(−(|J|+1)/2) = μ^((n−|J|−3)/2), against μ^((n−|J|−1)/2) 𝔰 at 87:5902.
- The two add to (𝔠^ϱ_(|J|)(μ) + 1). ✓
- The parts 𝔡_n and 𝔡′_(j′) of eq:tl5-hfd-words are those of the lemma in use, as in hfe-rho (b). ✓

**Step 3 has no part with ϱ.** 87:5712 reads 𝔰_P⁰ ≤ 2C_S e^(φ/2) Y_s + 2C_(0,0) η₀. Its source is the zeroth-order
step, which has no ϱ (87:5575–5576, 87:6692–6694), and the factor |H| ≤ 𝔤₁|h| does not add one. With the constants with
index f it is 𝔰_P⁰ ≤ C_P⁰ e^(φ/2) Y_s + C_(P,0)⁰ η₀. ✓

**The split.**
- The bulk part 2Ω̂² μ⁻¹ (1 − 𝔵^z)⁻¹ 𝔤^l_(ϱ,t) k₂^z 𝔰_P⁰ ϱ (√e_o + √c √e_i) replaces the one with 𝔰₁^v, which is what
  ε^l (87:7426) carries.
- With the bound of 𝔰_P⁰ it is 2Ω̂²(s₀ + Y_s s₁)(…). Subadditivity and homogeneity give 𝒮[s_N + s₀ + Y_s s₁] ≤ ε^f +
  Y_s 𝔯_ϱ^f.
- Times Y_s, this gives Y_s ε^f + 𝔯_ϱ^f Y_s². So there is a Y_s² term in 𝔯 and a ϱη₀ term in ε, and no ϱ² term, as
  the bound of 𝔰_P⁰ has no ϱ.
- Step 3's inequality then gives η_f = 1 − max(ϑ) − 𝔯^f, A_f and B_f in the form of hfv. ✓

**N ≥ 6 with option (b).**
- *Sufficient.* The proof uses exactly hft-small (b), hft-products, hfe-rho at ν′ = μ and 𝔤^l_(ϱ,t), which is
  𝔤_ϱ^l for option (b) (87:7421).
- *Needed, for option (a).* There eq:tl5-hfs-m2 has the part with ϱ unweighted. The count would then give
  μ^((n − ℓ_P)/2), not μ^(−3/2) μ^(b/2), so the lemma's factor needs option (b).
- *Not needed, for N = 4.* lem:tl5-hfq-theta gives hft-products at level four as well (87:6029), and 𝔑_J = 𝔑^L_J
  for |J| ≤ 3. So the lemma's own argument would apply to 𝔑^L_I there.
- What is missing at N = 4 is the level-four theorem: 𝔤_ϱ^l is a minimum there, and the 𝔑^M_I stand apart. The
  restriction is a stated choice of scope ("not proved here"), which is legitimate. The Comparison's reason for it is
  incomplete (n6).

## 3. lem:tl5-hff-zero (P:52–104) holds

**The face term.**
- By the proof of hfe-face (b) (87:7325–7330), the face integrand for A = Ψ_B is Σ_J 𝔶_(|J|) 𝔳₀⁴ R⁻³ (𝔲₀^♯
  |Ψ_(JB)|² + 2𝔲₀⁻¹ |D̂_(∂_γ)Ψ_(JB)|²), with 𝔲₀^♯ = 𝔲₀ + 8𝔲₀⁻¹|D̂∂_γ|². ✓
- The first way gives C_S^l exactly (87:7399). ✓

**The bound |Ψ_(ZC)|² ≤ 𝔷² 𝔨₂ (e_o + κ′e_i)[Ψ_C] and its source.**
- The first factor comes from the proof of (∗) of hfg-products (87:5211–5213): eq:tl5-hf-lie gives |ℒ_ZΨ| ≤ |Z||D̂Ψ| +
  2|D̂Z||Ψ|, and Cauchy–Schwarz with 𝔷 := max_(Z∈Γ)(|Z|² + 4|D̂Z|²)^(1/2) finishes it.
- The second comes from eq:tl5-hf-coercive and 𝔨₂ = (1/z̲ + max(1/c, 1/κ′))/(2Ω̂²) (87:4318). I checked it: |Ψ|² +
  Σ_M|D̂_(F_M)Ψ|² ≤ e_o/(2Ω̂²z̲) + e_o/(2cΩ̂²) + e_i/(2Ω̂²) ≤ 𝔨₂ (e_o + κ′e_i), the coefficient of e_i being ≤ κ′ ·
  (1/κ′).
- Both bounds are pointwise, and they are used in the same way in the proof of hfz-c1. ✓
- Z runs over Γ, which contains the six rotations and T. So the bound covers both the first letter of J and the first
  letter of B. ✓

**The weights.**
- For J = ZJ′, 𝔶_(|J|) μ^(|B|+2) ≤ μ^(|J|−2+|B|+2) = μ μ^(|J′B|).
- For J = ∅ and B = ZB′, 𝔶₀ μ^(|B|+2) ≤ μ^(|B|) = μ μ^(|B′|).
- A random test of 10⁴ (μ, 𝔶₀ ≤ μ⁻², 𝔶₁ ≤ μ⁻¹) found no failure. ✓

**The preimage counts.** I brute-forced them over Γ = {T, six rotations}, J over the 43 words, b = 1, 2, 3, for a single
word and for the family 𝔚_b of all 7^b words. The table gives, for each class, its own D̂_(∂_γ) parts and the |Ψ|²
parts passed to it:

| class | length | own | passed, single word | passed, family 𝔚_b |
|---|---|---|---|---|
| JB, \|J\| = 2 | b + 2 | 1 | 0 | 0 |
| JB, \|J\| ≤ 1 | b + 1 or b | 1 | 6 | 6 |
| B′ | b − 1 | 0 | 1 | 7 |

- The words JB are distinct. The classes are disjoint by length, and the words in each are distinct.
- This is exactly the text's 2𝔲₀⁻¹𝔨₁; 2𝔲₀⁻¹𝔨₁ + 6μ𝔷²𝔨₂𝔲₀^♯; and 7μ𝔷²𝔨₂𝔲₀^♯ (1 for a single word). ✓
- For any family of one length, the B′ have at most 7 preimages, one per Z ∈ Γ. ✓

**8𝔲₀⁻¹|D̂∂_γ|².** It multiplies |Ψ_(JB)|², so it goes inside 𝔲₀^♯ with the rest of that part, as stated. ✓

**The pointwise minimum.**
- At each point both ways bound the same integrand. In each way, every word's coefficient is at most that way's
  largest, which is at most the corresponding entry of eq:tl5-hff-cs. For a single word the B′ coefficient μ𝔷²𝔨₂𝔲₀^♯
  lies below 6μ𝔷²𝔨₂𝔲₀^♯, so the max with 7 is a valid upper bound.
- So the integrand is at most 𝔳₀⁴R⁻³ min(…) Σ_W μ^(|W|) ε₁[Ψ_W] at each point. Taking the supremum and Σ_W μ^(|W|)∫ε₁ ≤
  ℰ_g(p) gives C_S^f. ✓
- Using one way for all the pairs at a point is what keeps a word from being charged both its own X and the six passed
  parts. The text says "for all the pairs at once".
- The closedness remark is not needed, since the bound is pointwise, but it is true.
- C_S^f ≤ C_S^l for all weights, because the first entry of the minimum is C_S^l's function. ✓

**Families and 𝔐_p.**
- The family bound adds the inequality over B ∈ 𝔚, as in hfp-abs (c) (87:6721–6723). The counts above hold for every
  family of one length, and the parts with η₀ stay n^(1/2) times one word's. ✓
- In 𝔐_p^(m) the word of length 0 is h, so it carries C_S^h, and b ≥ 1 carries C_S^f, as the definition says. The parts
  with η₀ of the same step are taken up in m1.

**The word h and its own leaf weight.**
- eq:tl5-hfd-leaf (87:7107) is a pointwise inequality on one leaf, valid for every 𝔶₀, 𝔶₁ > 0. hfe-face (b) takes any
  such weights with C_(E,0)(𝔶), and the S_a part of hfp-abs (c) works for any weights through 𝔗(𝔶).
- The zeroth-order step for h is its own application of hfe-face (b), at each point p. So it may take its own 𝔶^h =
  (𝔶₀^h, 𝔶₁), and the leaf inequality allows this. The step needs only 𝔶₀^h μ² ≤ 1 and 𝔶₁ μ ≤ 1, which is 𝔶₀^h ≤ μ⁻²
  as stated. ✓
- I checked the counts in h's step: |J| = 2 carries 2𝔲₀⁻¹𝔨₁; |J| = 1 carries 2𝔲₀⁻¹𝔨₁ + 6μ𝔷²𝔨₂𝔲₀^♯; h carries 𝔶₀^hμ²(…)
  + 6μ(𝔶₁μ)𝔷²𝔨₂𝔲₀^♯. All three are at most the second entry of C_S^h. ✓
- C_S^h ≤ C_S^l and C_(0,0)^h = C_(0,0) at 𝔶₀^h = 𝔶₀. ✓
- Every use of the bound of h(p) must then take C_S^h and C_(0,0)^h. The definition names every such use except one,
  the parts with η₀ of the step at low levels (m1).

## 4. The definition, the theorem, the closing condition and the Remark

**Defined before use.**
- In the chapter text every new constant is defined before it is used: 𝔲₀^♯, 𝔶^h, C_S^f, C_S^h and C_(0,0)^h in
  lem:tl5-hff-zero; C_P⁰, C_(P,0)⁰, ε^f, 𝔯_ϱ^f, 𝔯^f, η_f, A_f, B_f, 𝔰_*^f[𝔜], Y_f and 𝔰_*^f in the definition.
- The opening paragraph refers ahead, as the openings of earlier sections do.

**Sites.**
- I checked each replaced site against 87: the sites of lem:tl5-hfc-h, which are eq:tl5-hfs-linfty, eq:tl5-hfg-cinf
  and its forms, hft-small (a), hfq-theta, and C_P^v and C_(P,0)^v of hfv-rec; 𝔎 and 𝔎₀ (87:5655); 𝔨_rec^p and
  𝔨_rec^(0,p) (87:6675–6677), where C_S^p and C_(0,0)^p bound only μ|h|; and 𝔐_p^(m) (87:6672–6673).
- C_P⁰ = max(𝔤₁C_S^h, C_S^f) covers μ|H| ≤ 𝔤₁μ|h|, the word ∅ (C_S^h ≤ 𝔤₁C_S^h) and the words of length ≥ 1.
  C_(P,0)⁰ covers the same for η₀.
- **One site is missing (m1).** In lem:tl5-hfp-low (87:6822–6834) the part with η₀ is (2𝔐^(m))^(1/2) times the
  largest of the parts of one word, b = 0, …, m + 1. These are the third entries max(C_(0,0), C_(1,0)) of C_(∞,0)^(m) and
  of its forms, which enter 𝔰_* and, through C_(P,0), 𝔎₀ and 𝔯.
- For b = 0 the word is h. Under the new step its part is C_(0,0)^h η₀, which exceeds C_(0,0) η₀ when
  C_(E,0)(𝔶^h)𝔗(𝔶^h) > C_(E,0)(𝔶)𝔗(𝔶). That can happen for 𝔶₀^h < 𝔶₀.
- The definition replaces nothing there. Yet the theorem's proof (P:147–149) says these bounds are "formed from the
  bounds of the step in the same way", and that needs max(C_(0,0)^h, C_(0,0)).

**The hypotheses and the conclusion.**
- (a)–(c) are those of thm:tl5-hfc with index f. Route (𝔯) is restricted in the definition. No hypothesis is missing,
  given m1's clause.
- The proof's two changes are right.
- *The zeroth order.* I checked the list of the uses of the zeroth-order step: the quantities of 𝔰_P⁰, the entries of
  hfc-h, 𝔎 and 𝔎₀, μ|h| in hfp-rec, and the families in hfp-low. I found no other use. hfu's products with no factor at
  a point use face norms, not bounds at a point.
- *The parts with ϱ.* After Step 1, 𝔰 ≤ 𝔰₁^v on D^κ_s, so the lemma and the zeroth-order step apply at every point of
  D^κ_s.
  - ℰ_g(q) ≤ e^(φ(q)) Y_s² uses Y_s itself, not the a priori bound, as (i) of hfc requires.
  - Y_s is a number, so homogeneity applies.
  - The rest of hfc's proof carries over: the case A_f = 0, B_f > 0 as S_F^f > 0, the choice of 𝔜, (i)–(iii), and the
    final re-run with Y_f. ✓

**The closing condition and the root.**
- A_f B_f = η_f^(−3/2)(δ_w + η_f^(−1/2)(ε^f + ε_M^f))(S_F^f + S_M^f), as displayed. ✓
- Y_f = 2A/(1 + (1 − 4AB)^(1/2)) is the smaller root of By² − y + A, and it is nondecreasing in A and in B.
- 2·10⁵ random pairs gave 0 failures of the monotonicity, and the root equation held to 10⁻⁹. ✓

**Containment.**
- At 𝔶₀^h = 𝔶₀ and route (𝔰), C_S^h ≤ C_S^l, C_S^f ≤ C_S^l and C_(0,0)^h = C_(0,0). So C_P⁰ ≤ 𝔤₁C_S^l and C_(P,0)⁰ =
  𝔤₁C_(0,0), as 𝔤₁ ≥ 1.
- The 𝔨_rec, 𝔐_p and (after m1) η₀ entries do not increase.
- 𝔯_ϱ^f = 0 and ε^f = ε^l = ε^c.
- Every constant with index c is nondecreasing in these numbers. So η_f ≥ η_c, A_f ≤ A_c, B_f ≤ B_c, 4A_fB_f ≤ 4A_cB_c
  < 1, Y_f ≤ Y_c, and 𝔰_*^f ≤ 𝔰_*^f[Y_c] ≤ 𝔰_*^c[Y_c] = 𝔰_*^c < 𝔰₁^v.
- Hence the hypotheses of thm:tl5-hfc imply those of thm:tl5-hff. ✓

**The opening (P:3–19) and the Remark (P:171–191), word by word.**
- Each statement in the Remark matches the proofs. That includes the reason for option (b), "where the bounds of the
  second derivatives carry the weight μ^(−(|C|+1)/2) on their parts with ϱ".
- The opening is right in substance, with three nits:
  - its lever-4 sentence omits that same weight, which is what produces the factor, and puts "Φ₁ is a quantity of
    𝔰_P⁰" under the level condition (n1);
  - it calls the bound |Ψ_(ZC)| ≤ … a bound "of (∗)" where it is from the proof of (∗) (n2);
  - the pointer line it adds to rem:tl5-hfc-what states the optional route as a fact (n4).

## 5. The Comparison

**The figures, each checked against its report.**
- **G0p §G0p.4.**
  - f / ϱ: −31.96 / −32.01, −28.82 / −28.75, −40.52 / −40.54, −34.82 / −34.80.
  - Shares 0.03 / 0.5 / 0.1 / 0.4.
  - 𝔰_* sets ε 4.94 / 3.74 / 6.11 / 4.98 decades below the closing.
  - Price of ×0.1, +0.90 / +0.61 / +0.81 / +0.40; price of C_S ÷ 2, +0.22 / +0.06 / +0.18 / +0.02.
  - The level-6 μ's 10⁻⁵ / 10⁻⁴ / 3 × 10⁻⁶ / 10⁻⁵, and 𝔐_p^(2)/C₁ = 0.92–1.29.
  - All match. ✓
- **G0p §G0p.0.** η₀ = 10^−18.6 / −18.0 / −20.1 / −19.3; 𝔰₁^v = 5.0 / 2.0 / 4.5 / 1.4 × 10⁻⁵; 𝔵^z = 0.068 at seed 1
  D_A; the level-4 μ's. All match. ✓
- **G0p §G0p.1.** log₁₀ sup 𝔨_rec^p / sup 2C_S = −0.195 / +0.109 / −0.108 / +0.223, and ϱ's 𝔯 budget 2.2–4.4 decades.
  Both match. ✓
- **G0j §G0j.1.** The share of 1/z̲ in 𝔨₂'s numerator, 0.75 / 0.73 / 0.81 / 0.81, at the supremum of C₁^x. ✓
- **G0g §G0g.3.** The row "𝔨_B = max(𝔷, 2)" reads 0.75 / 0.68 / 0.67 / 0.59 at the supremum of S_F. These are logs
  above log 2, so they are 𝔷. ✓

**The arithmetic, recomputed.**
- log₁₀(1/share) = 1.523 / 0.301 / 1.000 / 0.398, and with the margins of f, +1.57 / +0.30 / +1.02 / +0.40. ✓
- log₁₀(X/X′) at level 4 is 2.597 / 2.248 / 3.790 / 3.473. At level 6 it is 2.597 / 1.725 / 3.313 / 2.950.
- ¼–½ of these give every printed range: the last is 0.738–1.475, printed 0.74–1.48. ✓
- The 𝔤₁ offsets give +0.106 / +0.410 / +0.193 / +0.524. ✓
- 1 + 301^½ · 0.068/0.932 = 2.27. ✓
- (258/301)^½ = 0.926 and (43/301)^½ = 0.378. ✓
- The fall C_S^f/C_S^l = (X′Y′/(XY))^¼ lies in [¼, ½] log₁₀(X/X′) for Y = aX + b. 2·10⁵ random cases gave 0
  failures. ✓

**Marking.** The figures are marked deduced, not evaluated, and as upper figures. They carry the "every supremum at one
point" assumption and the caveat that G0g and G0j were measured at other suprema, and that G0p predates P-GRD14. ✓

**Beyond what is proved.**
- The level-4 conclusion, about 0 through 𝔰_* because 𝔨_rec^p leads after 𝔤₁, is argued correctly.
- The level-6 "lever 3a pays at least it" is conditional on both C_S^f and C_S^h falling by 0.30. The next clause then
  cites falls that are C_S^f's only (n7).
- The scoping of the C₁ lever states the factor's range incompletely (n8).
- The reason given for leaving out N = 4 is incomplete (n6).
- Item 1's site list mis-cites one line range and omits the site of thm:tl5-hfz (n5).
- Item 2's list lacks m1's site; the fixed copy adds it.

## 6. Findings

**m1 (minor), P:110–111, def:tl5-hff-constants: the parts with η₀ of the step at low levels.**
- **The text.** "… and with C_S^h for b = 0 and C_S^f for b ≥ 1 in place of C_S^p in 𝔐_p^(m), each in its form with
  index l, and in every constant formed from these."
- **What is missing.** In lem:tl5-hfp-low (87:6822–6834) the part with η₀ of the step at low levels is (2𝔐^(m))^(1/2)
  times the largest of the parts of one word. That is the entry max(C_(0,0), C_(1,0)) in the third term of C_(∞,0)^(m)
  and its forms, in 𝔰_* and, through C_(P,0), in 𝔎₀ and 𝔯.
- **Why it matters.** The word of length 0 is h. Under the new step its part is C_(0,0)^h η₀, which exceeds C_(0,0) η₀
  when 𝔶^h raises C_(E,0)(𝔶)𝔗(𝔶). As written, the definition leaves C_(0,0) there.
- **Why it is minor.** The proof (P:147–149) already forms these bounds "in the same way" from the step, and
  containment is unaffected, since C_(0,0)^h = C_(0,0) at 𝔶₀^h = 𝔶₀.
- **Fix (applied).** "…, with C_S^h for b = 0 and C_S^f for b ≥ 1 in place of C_S^p in 𝔐_p^(m), and with
  max(C_(0,0)^h, C_(0,0)) in place of C_(0,0)^p in the parts with η₀ of the step of [[lem:tl5-hfp-low]], each in its
  form with index l, and in every constant formed from these."
  - The ", and with C_S^h for b = 0" before it becomes ", with C_S^h for b = 0".
  - Item 2's site list in the Comparison gains "87:6824–6825 (lem:tl5-hfp-low, …) → max(C_(0,0)^h, C_(0,0)) in place
    of C_(0,0)^p", and the definition's crosswalk note gains the clause in ASCII.

**n1 (nit), P:5–7, the opening: what option (b) contributes.**
- **The text.** "At the levels N ≥ 6 with option (b) of [[def:tl5-hft-constants]], Φ₁ is a quantity of 𝔰_P⁰, and |Φ₁|
  ≤ μ^(−ℓ_P(Φ₁)/2) 𝔰_P⁰ leaves the factor μ^(−3/2) μ^(b/2) …"
- **Why it is a nit.** Φ₁ is a quantity of 𝔰_P⁰ at every level. The factor comes from Φ₁'s weight together with the
  weight μ^(−(|C|+1)/2) that option (b) puts on the part with ϱ of D̂²Ψ_C, as the Remark (P:179–180) says.
- **Fix (applied).** "But Φ₁ is a quantity of 𝔰_P⁰, and at the levels N ≥ 6 with option (b) of
  [[def:tl5-hft-constants]], where the part with ϱ of the bound of D̂²Ψ_C carries the weight μ^(−(|C|+1)/2), |Φ₁| ≤
  μ^(−ℓ_P(Φ₁)/2) 𝔰_P⁰ leaves …"

**n2 (nit), P:12, the opening: the source of |Ψ_(ZC)| ≤ ….**
- **The text.** "… of (∗) in the proof of [[lem:tl5-hfg-products]] …"
- **Why.** The bound is a step in the proof of (∗), not (∗) itself. The lemma's proof (P:79) says this correctly.
- **Fix (applied, same length).** "… in the proof of (∗) of [[lem:tl5-hfg-products]] …"

**n3 (nit), P:158–161, the proof of thm:tl5-hff: the symbol s.**
- **The text.** "2Ω̂² s (…), with s := s_N[2R̂ic] + s₀ + Y_s s₁, s₀ := … and s₁ := …; … at most Y_s 𝒮[s]; … so Y_s 𝒮[s]
  ≤ …"
- **Why.** In the same sentences s is the parameter of D^κ_s and Y_s. Also s₀ sits beside the threshold 𝔰₀.
- **Fix (applied).** Write s^f, s₀^f and s₁^f for the three functions: "2Ω̂² s^f (…), with s^f := s_N[2R̂ic] + s₀^f +
  Y_s s₁^f, s₀^f := … and s₁^f := …; … Y_s 𝒮[s^f]; … Y_s 𝒮[s^f] ≤ …"

**n4 (nit), P:212, the pointer line added to rem:tl5-hfc-what.**
- **The text.** "[[sec:tl5-hff]] moves the parts with ϱ into 𝔯 and takes …"
- **Why.** Route (𝔯) is one of two routes, offered only at N ≥ 6 with option (b), and the theorem takes either.
- **Fix (applied, still 117 characters).** "[[sec:tl5-hff]] can put the parts with ϱ in 𝔯 and takes the zeroth order
  through the shorter words ([[thm:tl5-hff]])."

**n5 (nit), P:253 and P:257, Comparison item 1: the sites.**
- **The text.** "87:5898–5899 (lem:tl5-hft-products, "is then at most ν 𝔰^(q−1) μ^((n − ℓ_E(Φ₂))/2) 2k₂ ϱ(p)")". The
  list then names hfw, hfy and hfe.
- **Why.** The quoted words stand on 87:5899–5900; 87:5898 is the bound of Φ₂. The proof of thm:tl5-hfe takes its step
  "as in the proofs of thm:tl5-hfw, thm:tl5-hfy and thm:tl5-hfz", and hfz's own site is missing.
- **Fix (applied).** "87:5899–5900 (…)"; and "…, 87:6578–6579 (thm:tl5-hfz, "k₂^z 𝔰 ϱ/(1 − 𝔵^z) ≤ 𝔰₁^v k₂^z
  ϱ/(1 − 𝔵^z)") and 87:7471 (proof of thm:tl5-hfe, …)".

**n6 (nit), P:261–262, Comparison item 1: why the route is not offered at N = 4.**
- **The text.** "Not offered at N = 4 or with option (a), where the products carry 𝔠^ϱ at other arguments (ν; 1 with the
  level weights μ^(n/2)) …"
- **Why.** At N = 4, 𝔤_ϱ^l is min(𝔤^l_(ϱ,q), 𝔤^l_(ϱ,t)). lem:tl5-hfq-theta gives hft-products there as well, so the
  products also carry 𝔠^ϱ(μ). The lemma's argument would apply; what is not done is the level-four theorem.
- **Fix (applied).** "Not offered with option (a), where the products carry 𝔠^ϱ at the argument 1 with the level
  weights μ^(n/2), nor at N = 4, where 𝔤_ϱ^l is a minimum with 𝔤^l_(ϱ,q), of argument ν, and the parts 𝔑^M_I stand
  apart; their forms with 𝔰_P⁰ are not proved here. The argument of lem:tl5-hff-rho itself uses only
  lem:tl5-hft-products, which lem:tl5-hfq-theta gives at N = 4 as well; the level-four theorem with the route is not
  drafted."

**n7 (nit), P:273–274, Comparison item 2: the two options for h.**
- **The text.** "The second option is the case 𝔶₀^h = 𝔶₀ of the first …"
- **Why.** At 𝔶₀^h = 𝔶₀ the first option gives C_S^h ≤ C_S^l, possibly strictly, while the second keeps C_S^l for h.
  The first dominates the second rather than containing it as a case.
- **Fix (applied).** "At 𝔶₀^h = 𝔶₀ the first gives C_S^h ≤ C_S^l, the constant the second keeps for h, so nothing is
  lost by taking the first."

**n8 (nit), P:324–325, Comparison, lever 3a at level 6.**
- **The text.** "Where both C_S^f and C_S^h fall by 0.30 or more …, so lever 3a pays at least it; the falls above at the
  level-6 μ exceed 0.30 in every case."
- **Why.** The falls above are those of C_S^f. C_S^h's fall needs 𝔶₀^h μ² of about X′/X or less (P:316–317), and its
  cost C_(E,0)(𝔶^h)/C_(E,0)(𝔶) is not evaluated. So the condition is met for one of the two only.
- **Fix (applied).** "… the falls of C_S^f above at the level-6 μ exceed 0.30 in every case, while that of C_S^h needs
  𝔶₀^h μ² of about X′/X or less and its cost is not evaluated."

**n9 (nit), P:342–344, "Not done": the range of the factor.**
- **The text.** "the factor is between (258/301)^½ = 0.93 (λ_M^(−½) ≥ |T|⁻¹) and (43/301)^½ = 0.38 (|T|⁻¹ ≫ λ_M^(−½))"
- **Why.** With x := |T|⁻²λ_M, the factor is ((43x + 258)/301)^½ for x ≤ 1 and ((43 + 258/x)/301)^½ for x ≥ 1. So it
  is 1 at |T|⁻¹ = λ_M^(−½), and it lies in (0.38, 1]. The figure 0.93 is its infimum for x ≤ 1, not one end of a range.
- **Fix (applied).** "the factor is at most 1, with equality at |T|⁻¹ = λ_M^(−½), and at least (258/301)^½ = 0.93 for
  λ_M^(−½) ≥ |T|⁻¹ and (43/301)^½ = 0.38 in all, the two bounds approached as λ_M^(−½)/|T|⁻¹ grows or falls"

## 7. The fixed copy

/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd15/P-GRD15.fixed.md

- md5 21ef7990fde81ae7fec86db25797f255, 375 lines: chapter text P:1–193 (11 labels), then the Placement, the
  Comparison and the crosswalk rows.
- **How it was made.** /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd15/tools/fix.py
  applies the fixes to copies of the writer's sources.
  - Each old text occurs exactly once.
  - The sources are /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd15/build/src.md,
    rest.md and build.py. They are verified to rebuild the original to md5 4e071f06.
  - The writer's wrap.py and pad.py re-wrap the changed paragraphs, and build.py rebuilds the file with the crosswalk
    rows at their labels.
- **Re-merged in a fresh tree,** it passes every check:
  - item 2 found at 7641, with the new line at 117 characters;
  - lint: 0 hits, 5331 labels;
  - check: 0 problems;
  - `[] 0`;
  - 0 existing numbers changed;
  - the crosswalk has 480 rows for 480 labels, in order;
  - chapter-text lines are at most 120 characters, also resolved, and the notes at most 121;
  - no forbidden line start in the chapter text.
- **Crosswalk lines that moved.**
  - Unchanged: sec:tl5-hff at 1.
  - lem:tl5-hff-rho 21 → 22, eq:tl5-hff-rho 29 → 30, lem:tl5-hff-zero 52 → 53 and eq:tl5-hff-cs 60 → 61. This is
    n1's extra line in the opening.
  - def:tl5-hff-constants 106 → 107.
  - eq:tl5-hff-routes 116 → 118, eq:tl5-hff-constants 125 → 127, thm:tl5-hff 127 → 129, eq:tl5-hff-closing 132 → 134
    and rem:tl5-hff-what 171 → 173. These follow m1's extra line in the definition.
- The rows are regenerated with the new numbers. The definition's note adds "max(C_(0,0)^h, C_(0,0)) in the eta_0
  parts of lem:tl5-hfp-low".

## Verdict

**CONFIRMED WITH THE FIXED COPY.** 0 Major, 1 minor, 9 nits. All of them are applied in the fixed copy, md5
21ef7990fde81ae7fec86db25797f255, and checked.
- lem:tl5-hff-rho is correct. The ϱ term arises only with Φ₂ = D̂²Ψ_C, Φ₁ is a quantity of 𝔰_P⁰, the count gives
  μ^(−3/2)μ^(b/2), Step 3's bound has no part with ϱ, and the split is a Y_s² term in 𝔯 and a ϱη₀ part in ε.
- Option (b) is needed for its factor and sufficient. N ≥ 6 is a choice of scope.
- lem:tl5-hff-zero is correct, with its counts 6, 7 and 1, its weights and its pointwise minimum. The word h may take
  its own leaf weight, since eq:tl5-hfd-leaf holds for every weight at every application.
- thm:tl5-hff holds, once m1's clause is in the definition.
- At 𝔶₀^h = 𝔶₀ and route (𝔰), the hypotheses of thm:tl5-hfc imply those of thm:tl5-hff.
