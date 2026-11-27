# R-F-G3: review of the G3 fix (thm:own-data (3), lem:own-maximal, thm:std-sbierski (7))

## Verdict

**CONFIRMED.** Major 0, minor 3, nit 5.

The fix closes G3. Statement (3) is now precise and true. lem:own-maximal is correct, and every cited result says
what the proof uses. No step is false or unproved. The three minors are a statement that the proof establishes but the
lemma does not state, one missing citation (Seeley extension), and one sentence that the new lemma makes misleading.
None of them changes what is proved.

Line numbers refer to chapters/63-own-data.md at HEAD 6234da7f unless another file is named.

## Findings

### m1 (minor, wrong pointer). The proof of thm:own-data (3) cites the lemma for a fact its statement does not contain

- **Where:** 63:2019, "defined on {t_IVP ≥ 0} ([[lem:own-maximal]])". Statement (3) at 63:59 also asserts a
  development "on {t_IVP ≥ 0}".
- **What is wrong:** the statement of lem:own-maximal says only "Then ǧ is defined on M₊" (63:1875), and
  M₊ = {r > r_♭, t_IVP ≥ 0} leaves out the inner boundary. The larger set {t_IVP ≥ 0} is established in the proof
  (63:1887: "So Ω_* ∪ 𝒟_(0,0) is the part {t_IVP ≥ 0} of the spacetime of [[ch:s27]], which contains M₊"), not in
  the statement.
- **Replacement, in the lemma statement (63:1875; re-wrap the paragraph):**
  - old: "Then ǧ is defined on M₊; (Σ̊, γ, k) is initial data"
  - new: "Then ǧ is defined on {t_IVP ≥ 0}, which contains M₊; (Σ̊, γ, k) is initial data"

### m2 (minor, missing justification). "Smooth up to the boundary" is used as "restriction of a smooth metric" without Seeley

- **Where:** 63:1889–1891, "it is smooth on 𝒟 up to its boundary (the proof of [[prop:iii-k-1-2]]) … So near each
  point of Σ̊, ǧ is the restriction of a smooth Lorentzian metric".
- **What is wrong:**
  - For r > R_ν, 𝒟 is a two-sided neighbourhood of Σ^IVP ([[prop:iii-k-1-2]] (1)). There g_(0,0) itself is the
    smooth extension.
  - On r_♭ < r ≤ R_ν, however, 𝒟 ends at Σ^IVP. There "smooth up to its boundary" gives a smooth extension across
    Σ̊ only by an extension theorem.
  - The extension is needed: the charts step builds Ẽ(s, x) = exp^(g̃)_x(s n) for s of both signs, and the template
    lists it as a hypothesis (63:1919).
  - Appendix A quotes Seeley's theorem as [[thm:std-seeley]], and the proof does not cite it.
  - The template sentence 62:231–232 has the same omission. It lies outside this change, but the new lemma repeats
    the inference with an explicit "So".
- **Replacement (63:1889–1891; re-wrap):**
  - old: "it is smooth on 𝒟 up to its boundary (the proof of [[prop:iii-k-1-2]]), and dt_IVP is past timelike for it
    on 𝒟 ([[lem:iii-k-6-2]] (a)). So near each point of Σ̊, ǧ is the restriction of a smooth Lorentzian metric,"
  - new: "it is smooth on 𝒟 up to its boundary (the proof of [[prop:iii-k-1-2]]), and dt_IVP is past timelike for it
    on 𝒟 ([[lem:iii-k-6-2]] (a)). So near each point of Σ̊, ǧ is the restriction of a smooth Lorentzian metric: of
    g_(0,0) where r > R_ν, 𝒟 being a two-sided neighbourhood of Σ^IVP there, and, where r ≤ R_ν, of an extension of
    g_(0,0) across {t_IVP = 0} in the coordinates (t_IVP, x) by [[thm:std-seeley]], which is Lorentzian near Σ̊;"

### m3 (minor, misleading claim). "No gluing is used" now sits right after a proof step that glues

- **Where:** 63:2024, "Ψ^*ĝ = ǧ there satisfies the same bound. No gluing is used, and no value of λ …".
- **What is wrong:**
  - The sentence means that no data are glued, unlike [[thm:settling]] (i).
  - The same paragraph has just invoked [[lem:own-maximal]], whose proof glues spacetimes: "We glue the past half of
    N to M₊", "The glued space", M_gl. Read in place, the sentence contradicts the step before it.
  - The old proof had no such conflict, because it gave no argument for the embedding.
- **Replacement (63:2024–2025; re-wrap):**
  - old: "No gluing is used, and no value of λ ∈ (0, λ_2] is excluded:"
  - new: "No data are glued (the gluing in [[lem:own-maximal]] joins two developments of the same data), and no value of
    λ ∈ (0, λ_2] is excluded:"

### n1 (nit). S = S⁰ = 0 reuses S, which this chapter fixes as the far part of Σ^IVP

- **Where:** 63:1874, 63:1888 and 63:2019. S := Σ^IVP ∩ {r ≥ 4R} is set in statement (1) and at 63:76, and item (2)
  of the same proof uses it ("its norm on S").
- **Replacement:** at the first occurrence in the lemma (63:1874), "with S = S⁰ = 0 ([[prop:vii-3-2]])" becomes
  "with vanishing boost and translation parameters, S = S⁰ = 0 in the notation of [[ch:s27]] ([[prop:vii-3-2]])". In
  proof item (3) (63:2019), "and S = S⁰ = 0 ([[prop:vii-3-2]])" becomes "and vanishing boost and translation
  ([[prop:vii-3-2]])".

### n2 (nit). The third Theorem 2.8 citation lacks the Appendix A pointer

- **Where:** 63:1971. The citations at 1877 and 1899 carry "([[thm:std-sbierski]] (7))"; this one does not.
- **Replacement:** "*The embedding.* By [Sbi15, Theorem 2.8] ([[thm:std-sbierski]] (7)), (M̂, ĝ, ι̂) is an extension of
  (D_gl, g_gl, ι):"

### n3 (nit). R_s ≥ 5R₁ is reached the long way, and r^♮ is pointed to the wrong place

- **Where:** 63:1964–1966.
- **What is wrong:**
  - The proof gets R_s ≥ 5R₁ from "t_IVP = t − C″ holding on {r ≥ R_s} and ψ_IVP = ψ increasing strictly on
    [3R₁, 5R₁]". The deduction is correct, but only r^♮ ≤ R_s is needed, and that is immediate: [[lem:iii-k-6-2]]
    takes R ≥ R_5, and R_5 := max(R₃, 3R₁) (46:83).
  - r^♮ := ½(r₀ + r₂) is defined in [[lem:ii-c-3-2]]. [[def:s12-radii]] gives only r₀ = r_♭ and r₂ = 7R₁/8.
- **Replacement (63:1964–1966):**
  - old: "as r^♮ = ½(r_♭ + 7R₁/8) < R₁ ([[def:s12-radii]]) while R_s ≥ 5R₁, t_IVP = t − C″ holding on {r ≥ R_s} and
    ψ_IVP = ψ increasing strictly on [3R₁, 5R₁] ([[lem:iii-b-3-7]] and its proof)."
  - new: "as r^♮ = ½(r_♭ + 7R₁/8) < R₁ ([[lem:ii-c-3-2]], [[def:s12-radii]]) while R_s ≥ R_5 ≥ 3R₁
    ([[lem:iii-k-6-2]], [[sec:iii-k-0]])."

### n4 (nit). "contains it" says more than the embedding gives

- **Where:** 63:63, statement (3), "(M̂, ĝ, ι̂) … contains it: there is …"; also the opening at 63:6, "which contains
  it".
- **What is wrong:** ǧ lives on {t_IVP ≥ 0}, inner boundary included. Only its part over {r > r_♭} embeds, as the
  colon clause then says.
- **Replacement (63:63):** "contains ǧ off the inner boundary {r = r_♭}: there is a time-orientation-preserving
  isometric embedding". At 63:6, "which contains it" becomes "which contains it off the inner boundary".

### n5 (nit). The substitution list is easy to misparse

- **Where:** 63:1915–1916, "with N₋, g_N, N, h_N, n_N and E_N(s, y) := … in place of A, g_λ, V and D_V(Σ), t_IVP on
  the side of A, n_λ and E_λ".
- **What is wrong:** the two lists match term by term only if "V and D_V(Σ)" is read as one item. Read as two items,
  the lists are 6 against 7.
- **Replacement:** "with N₋ in place of A, g_N in place of g_λ, N in place of both V and D_V(Σ), h_N in place of
  t_IVP on the side of A, n_N in place of n_λ, and E_N(s, y) := exp^(g_N)_(ι_N(y))(s n_N), n_N the future unit normal
  of Σ_N, in place of E_λ,"

*Not counted.* The ragged wrapping at 63:1901–1903 ("…Σ_N = h_N⁻¹(0)" / "([[thm:std-bgp-causal]] (3)); its gradient"
/ "is past directed…") and at 63:1923–1925 is cosmetic. It does not break the contract.

## What I checked

### 1. Statement (3), lem:own-maximal and proof item (3), line by line

**Σ̊.**
- Σ̊ is the graph t = ψ_IVP(|x|) over {|x| > r_♭} ⊂ ℝ⁴, which is connected and open, so Σ̊ is a connected manifold
  without boundary.
- γ is Riemannian, because dt_IVP is past timelike for g_(0,0) on 𝒟 ([[lem:iii-k-6-2]] (a)).
- (γ, k) are smooth, being induced by ǧ, and they satisfy the constraints by Gauss–Codazzi for the Ricci-flat ǧ.
- ǧ induces (γ, k) on Σ^IVP by [[thm:iii-k-4-3]] (2), since φ_(0,0) = ψ_0 ∘ φ_0 is the identity ([[prop:vii-3-2]]).
- So (Σ̊, γ, k) is initial data as [Sbi15, p. 11] defines it.

**[Sbi15].** I checked the quotations against arXiv:1309.7591v3:
- Theorem 2.8 (Existence of MGHD) is on p. 12 and is quoted verbatim in [[thm:std-sbierski]] (7).
- The proof of Theorem 2.8 runs from p. 22 ("Proof of Theorem 2.8") to p. 24 ("This finally finishes the proof of the
  existence of the MGHD").
- "a priori, only maximal among smooth GHDs" is on p. 10.
- The header's citation list (Theorems 2.6, 2.7 and 2.8, p. 12; proof of Theorem 2.8, pp. 22–24) is correct.

The lemma uses:
- Theorem 2.8 for existence, uniqueness up to isometry, and an extension of D_gl. This matches item (7).
- Theorem 2.6 for one GHD (N, g_N, ι_N). This matches item (3).
- Definitions 2.1 and 2.2, including the footnote "diffeomorphism onto its image" used for j. These match items (1)
  and (2).

**The Cauchy time function.**
- [BGP, Theorem 1.3.13] is quoted in Appendix A as [[thm:std-bgp-causal]] (3), with its page (p. 24). The lemma cites
  that item, as chapters 04, 45 and 48 cite this appendix entry, which meets the policy.
- Its hypotheses hold: N is globally hyperbolic, and Σ_N is a smooth spacelike Cauchy hypersurface (Definition 2.1;
  γ Riemannian).
- "Gradient past directed timelike" is part of the definition of a Cauchy time-function quoted in item (2), so dh_N is
  past timelike and h_N increases to the future.

**The gluing.**
- *Closedness.* For closed F ⊂ N₋, π⁻¹(π(F)) = F ⊔ ι_N⁻¹(F ∩ Σ_N), which is closed. So π restricted to each half is a
  closed embedding.
- *Charts and smooth structure.* I read the template paragraphs 62:228–301 with the substitutions applied:
  - dh_N(n_N) > 0;
  - O_N ∩ {h_N ≤ 0} = O_N ∩ N₋, since O_N ⊂ N;
  - O ∩ {t_IVP ≥ 0} = O ∩ M₊ for O ⊂ {|x| > r_♭};
  - W_Π is open in the quotient topology;
  - Φ_Π is a homeomorphism by the pasting lemma on the two closed halves;
  - the transition maps are smooth.
- *Metric.* Gaussian normal coordinates on both sides, both metrics Ricci-flat and both inducing (γ, k) with respect to
  the future normal. Definition 2.1 gives this for g_N.
- *Time orientation.*
- *Connectedness.* The connectedness of N₋ comes from the replacement sentence: timelike curves to the Cauchy
  hypersurface Σ_N, with h_N ≤ 0 along them. M₊ ∖ Σ̊ is connected as the region above a graph.
- *Acausality.* Part (ii) of the template needs only that Σ̊ is closed and that s increases along future causal curves.
- *Hausdorff.* All three cases hold. In the case of a point of Σ̊ against a point of N₋ ∖ Σ_N: π(U′) is open and
  misses W_Π, because π is injective on N₋ and U′ ∩ U_y = ∅. In the case of two points of Σ̊: the charts' halves lie
  in disjoint sets.
- *Second countable.* Σ̊ is Lindelöf, so countably many W_Π cover it, and the two open halves are second countable.
- The template's common chart supplied the Hausdorff property, second countability and the openness of W_Π. All three
  are replaced correctly.
- *D_gl.* By [[thm:std-bgp-development]], D_gl is open and globally hyperbolic with Σ̊ Cauchy. It is connected by the
  "later use" argument of 62:293–301. With ι it is a GHD in the sense of Definition 2.1.

**M₊ ⊂ D_gl.**
- *Reduction.* The past half 𝔠 from p, if it misses Σ̊, stays in the open set π(M₊ ∖ Σ̊) by connectedness, and it is
  past inextendible there.
- *First step.*
  - {t^♭_* > 3/2} ∩ {r > r_♭} ⊂ Ω°_*, since Ω_* = cl{t^♭_* ≥ 1} (46:52). Also Ω°_* ⊂ {t_IVP > 0}, since
    Ω_* ⊂ {t_IVP ≥ 1}, with t_IVP ≥ t_* ≥ t^♭_* (46:82–83 and [[lem:ii-c-3-2]] (b)).
  - [[lem:iii-k-6-1]] (c) with c = 3/2, T = t^♭_*(p) and X = Y = Ω°_* gives L_p ⊂ Ω°_*, compact, containing
    J⁻_X(p) ∩ {t^♭_* ≥ 3/2}. Its smallness hypothesis is the one [[prop:iii-k-4-2]]'s proof verifies for this metric
    on Ω_*.
  - The argument of [[lem:ii-f-1-3]] (27:262–267) then excludes a past-inextendible curve in X along which
    t^♭_* > 3/2. This is exactly how [[prop:iii-k-4-2]] (46:1647–1651) applies it.
- *Second step.* On a maximal interval in {t^♭_* > 3/2} that starts at the value 3/2, t^♭_* is a time function and
  decreases to the past, which is a contradiction. The step is correct.
- *Third step.*
  - The set {t_IVP > 0, t^♭_* ≤ 3/2} lies in 𝒟 = N_ν ∩ {t^♭_* ≤ T̂ + 3} (46:223).
  - ǧ = g_(0,0) there, by [[prop:iii-k-4-2]] with S = S⁰ = 0 on 𝒟_(0,0) ∩ {t^♭_* ≤ T̂ + ¼c_0}.
  - dt_IVP is past timelike by [[lem:iii-k-6-2]] (a).
  - The radius bound is [[lem:iii-k-6-2]] (c) at the level c = 0, read correctly: R_𝔠 = max(R_s, r(p_1)) + 2t_IVP(p_1).
  - L_𝔠 is compact in the chart.
  - The curve converges, parametrised by t_IVP, since {V causal : dt_IVP(V) = 1} is compact over L_𝔠.
  - The limit q cannot lie in the open part or on Σ̊, so r(q) = r_♭.
  - dr is future timelike near r = r_♭ for g_(b₀): 46:950–951, the proof of [[lem:s27-below]] (iv).
  - It stays so for ǧ, by the C⁰-smallness of h_0 on 𝒟 ∩ {r ≤ R_s} (46:1050–1052) and the time orientation
    continued from g_(b₀). So r increases strictly towards q along 𝔠, and r(q) > r_♭, a contradiction.
  - The smallness needed for dr to stay timelike is the same as the inner-boundary condition chapter 46 already uses:
    lem:s27-cover (c) (46:293–296) and the proof of [[prop:iii-k-1-2]] (46:256–257). The new argument therefore needs
    no new threshold.

**Maximality.**
- Theorem 2.8 with Definition 2.2 gives j : D_gl → M̂, time-orientation-preserving, an isometric embedding, with
  j ∘ ι = ι̂.
- Ψ = j ∘ π is continuous on M₊ and equals ι̂ on Σ̊. On M₊ ∖ Σ̊ it is a time-orientation-preserving isometric
  embedding, since π is an isometric diffeomorphism there onto an open set.
- On {r_♭ < r ≤ R′, t_* ≥ t_1}, t_IVP ≥ t_* ≥ t_1 ≥ 1 > 0, so the set lies in the domain of Ψ, and Ψ^*ĝ = ǧ carries
  the bound.
- t_1 = max(T′, 1) with T′ from [[cor:s27-rate]] (c), and the rate t_*^(−2−ε_t) is the corollary's last clause.

### 2. Consistency with chapters 00, 01, 03, 61, 62 and 90

- The restatements are at 00:30, 01:66, 01:183, 03:338–340, 61:82–83, 62:17, 62:344, 62:586 and 90:126–131. Each says
  "the development of g_λ's own data settles", or cites the threshold and the class. All remain true under both parts
  of the new (3).
- No other chapter has "maximal vacuum development" or "maximal development". The only other occurrence of "maximal
  globally hyperbolic development" is the unrelated [CTG23] quotation at 95:488.
- No proof in any chapter uses item (3). Inside chapter 63 it is used only in its own proof.

### 3. The crosswalk

- crosswalk/63-own-data.tsv has 124 data rows with 4 columns each.
- Its label column equals, in order, the 124 labels defined in chapter 63. The new row lem:own-maximal comes last,
  after eq:own-transfer, as in the chapter.
- The thm:own-data note records the restatement.

### 4. The contract

- **Line length.** At most 121 characters per line in chapter 63 and chapter 95, both in the source and after label
  resolution. I resolved the labels in memory with the assembler's own number and resolve functions and wrote nothing.
- **Wrapped lines.** None of the new or changed lines (63:3–24, 59–65, 1872–1974, 2017–2026; 95:307–352) starts with
  "+ ", "- ", "* ", "> ", "#", "=" or "|".
- **Backslashes.** There are none.
- **Language.** There is no file, program, code or AI language in the new text.
- **Labels after resolution.** lem:own-maximal is Lemma 44.51, thm:own-data is Theorem 44.1 and thm:std-sbierski is
  Theorem A.14.
- **Check outputs**, run from the paper directory:
  - `python3 lint.py --chapters` → `chapters: 62 file(s), 4585 label(s) defined, 0 hit(s)`
  - `python3 assemble.py --check` → `labels 4585, computations cited 0, problems 0`

I edited no repository file and ran the assembler only with --check.
