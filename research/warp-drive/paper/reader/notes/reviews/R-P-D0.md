# R-P-D0: independent reading of proofs/P-D0.md

File read: research/warp-drive/paper/reader/proofs/P-D0.md, md5 5f41b63ff6507be43e6c87b5f286c008, 871 lines, every line,
every proof in full. Writer's report: notes/reports/P-D0.md. Nothing in the repository was edited or committed.

HEAD at the time of the scratch merge: 2b9cb2ea ("Retire P-TR.md: sec:tr ... merged into chapter 71"). Chapter 71 at HEAD
has md5 bb53f3e845095a3cd821bf51f8c12414. That is not the edafc288 text (ef108525…) the file quotes, because P-TR's
merge added lines near the opening, at 1818, at 5488 and appended sec:tr.

Scratch merge: git archive of HEAD in scratchpad/rpd0/. Scripts: scratchpad/reader/tools/ (merge_pd0.py, zroots.py,
muflat.py, chain.py, fixes.py).

## 1. Placement (HEAD 2b9cb2ea, P-TR merged)

- **Old texts.** All 13 occur exactly once in chapter 71 at HEAD, as whole lines, and none overlap.
  - Each sits at its edafc288 line number + 13. P-TR inserted 6 + 5 + 2 lines before 2406.
  - Hits: T5 2419, T13 2583, T6 2606, T7 2627, T8 2633, T9 2648, T10 2669, T11 2675, T12 2685, T1 2911, T2 3632,
    T3 3715, T4 3770.
  - P-TR touched none of them, so the texts are still valid after its merge.
- **Checks after applying T1–T13:**
  - `lint.py --chapters`: 62 files, 4965 labels, 0 hits.
  - `assemble.py --check`: 4965 labels, 0 problems.
  - The required one-liner prints `[] 0`.
  - No assembled line is longer than 121 characters.
  - No new line starts with a Markdown marker.
  - No backticks, file names or process words. "Now take ℰ_ind := ℰ^φ_ind" is mathematical usage.
- **Crosswalk.**
  - I inserted the 9 rows of §7 after thm:is-d0.
  - Every chapter-71 label then has exactly one row, in label order, with 4 fields each.
  - The checks above still pass.
  - Two nits, n5 and part of m4, are below.

## 2. Verification of the three claims

### (1) prop:is-cb-normal and rem:is-cb-open: correct

- **Equivariance under all of O(4).** lem:iii-e1-2-1 is stated for O ∈ O(4): Pf(OAOᵀ) = det O·Pf(A), and Pf² enters.
  - c_Υ, c_(Υ,H), t_* and E_Υ are radial or φ_O-invariant.
  - The s0 indicial solution at 2 + 𝔡₀ is ρ^(2+𝔡₀)(a dt_* + b d|x|), which φ_O fixes.
  - The inverse of (□^Υ_b)^(0) is unique, so it intertwines.
- **The normal form.** Checked entry by entry:
  - The torus kills the off-diagonal block. Take θ₁ = π.
  - P J₁₂ Pᵀ = J₃₄, which gives 𝔠₂(a₁,a₂) = 𝔠₁(a₂,a₁).
  - Q₁ = diag(1,−1,1,1) flips J₁₂ and fixes J₃₄, so 𝔠 is odd in a₁.
  - Q₂ = diag(1,1,1,−1) fixes J₁₂ and flips J₃₄, so 𝔠 is even in a₂.
  - c(J₁₂) = −tr(XJ₁₂) = 2𝔠₁.
- **The equivalence.** It follows from ⟨X_b, X_b⟩ = c_b(X_b) and ‖A‖ = max(|a₁|,|a₂|) (sec:iii-b-3-1).
- **rem:is-cb-open's facts:**
  - (AP3) includes σ = 0 (rem:ec-point-outside).
  - def:ec-point does not fix γ_(Υ,H), ζ_∞ or χ.
  - The first-order derivation is right: □₀ω₁ = −(η₁ + □₁ω₀), s0 part. Two nits, n2 and n3, concern its wording.

### (2) The offset 𝔡₀ dropped by recording relative to order 1: confirmed

I redid the audit myself.

- **Searches.** I grepped all 62 chapters, not only 32–46, 38a, 65 and 71, for:
  - the labels prop:iii-f3-2-2, eq:iii-f3-2-1/2/3, eq:iii-f3-4-2, prop:iii-f3-4-1, rem:iii-f3-2-3, lem:iii-f3-2-1,
    eq:iii-i7-1-1, sec:iii-i7-1 and lem:iii-i11-1-1;
  - the objects ω̇, ġ^Υ_b(0, ġ_b(0, ġ(0, ġ_b(ḃ, ġ(ḃ, 𝒢 and ℰ_ind.
- **Each hit was read in context** and mapped to its result.
  - Chapters 08, 20, 30 and 33 use the symbols with other meanings, or the ungauged ġ_b ∈ |x|⁻³C^∞.
  - Chapter 46 (1899, 1924, 2084) uses them only for parameters and naturality.
  - Chapter 66:92 concerns W*, not ġ.
  - Chapter 36's ℰ_ind (lem:iii-g4-4-3) collects the corrections of the table states, the s1 states and the v1 states.
    It holds with ℰ^φ_ind by lem:is-flat-memberships (a).
  - Chapter 41's 1285 and 1745 and chapter 37's prop:iii-f3-4-1 citations use the nullspace and cokernel, not index
    sets. 41:327 concerns h_s1.
  - 41:1240–1760 (stationary solutions, K⁺ formal solutions) uses 𝒢_* (conormal order > −3).
  - In u_exp and h_rem, ġ appears only with conormal coefficients ḃ_rem and b_rem.
  - The only parameter-dependent profiles in rows are h_(b,v1)(V) = ½ġ^Υ_b(0, [A(b), A_V]). These are spin changes in
    im ad_(A(b)) (rem:iii-f3-2-3, rem:iii-i15-1-2, 44:480).
  - At such spin changes c_b vanishes, and so do the terms at 2 + 𝔡₀ + ℕ₀, for every b. So ∂_b of them has none either.
- **Result.** Every use of the memberships of ω̇_b(0, ·) and ġ^Υ_b(0, ·) is of kind (i) 𝒢, (ii) ℰ_col or (iii) weights
  and leading terms. None enters a formal solution, tower or row.
  - The device is also robust: (3,0) ∪ (3 + (ℰ^φ ∪ ℰ_(𝔡₀))) ⊂ (2,0) ∪ (2 + ℰ^φ).
  - So wherever ġ^Υ_b(0, ·) is used with its index set, its exponents are 2 plus one element of ℰ^φ.
  - That is a sum of increments of Λ^φ. For example, 3 + 𝔡₀ = 1 + 1 + (1 + 𝔡₀).
  - Hence no use can need 𝔡₀ as an increment.
- **The index-set facts:**
  - The count giving (𝔡₀ + j, ≤ j) for ω̇_b(0, ·), using eq:is-l1, F = (2,0), and that no other root ≡ 𝔡₀ mod 1.
  - (1 + 𝔡₀ + j, j) ∈ ℰ^φ from ω̇_b(1, 0).
  - 𝔡₀ ∉ π_1(ℰ^φ ∪ ℰ^(ι,φ)): inheritance along towers shifts offsets by 0 or by positive integers. The boosts and the
    s1 tower are odd. The rotation corrections' 𝔡₀-terms vanish.
  - ℰ^φ ∪ ℰ_(𝔡₀) ⊂ ℰ_ind, by monotonicity of eq:is-l1 and lem:is-count (b).
  - The increments below 3/2 (the "among" list).
  - Λ^φ ⊂ Λ.
  - k̄_0 = 3, l_* = 50, η_0 = 𝔡₁ and J_* = 15,000,015 remain admissible.
- **Weights and leading terms.** Recording relative to order 1 changes no weight or leading-term statement used
  elsewhere, because eq:is-flat-memb keeps the forms at 2 and 3 alongside:
  - ω̇_b(0, Ȧ) has weight 2 and ġ^Υ_b(0, Ȧ) weight 3, with leading terms free of logarithms;
  - the next exponents are at 2 + 𝔡₁ and 3 + 𝔡₁;
  - D ∈ 𝒜^ϵ in rem:iii-f3-2-3, ω′_π ∈ 𝒜^(β−1), and the excesses in lem:iii-f4-3-1 all hold.
- **thm:is-d0 remains true as stated.**
  - (c) says "serving in every membership of [[sec:uc-index-sets]]". That includes prop:iii-f3-2-2 (1) in its
    order-2 form, so the "only if" is right.
  - The file neither changes the statement nor adds a remark at it.
  - The qualification appears only in T1, T2, T5 and thm:is-flat-serves. See m1.
- **One defect in the audit lemma itself.** Its list of results is not complete. See m2.

### (3) The new choice: every number reproduced exactly

- **Roots and μ♭_Z.** I computed certified roots of 𝒫_0 and 𝒫_1, …, 𝒫_1000 (sec:tab-a-sextic coefficients) with
  python-flint acb, at 400 to 600 bits.
  - Z₃ has 2629 elements: 1269 real and 1360 non-real.
  - The least excess (⌊y/𝔡₁⌋ + 1)𝔡₁ − y is at l = 700, the non-real pair: y = 0.13139821983003038063225337…,
    n = 394194.
  - μ♭_Z = 3.5481255635325687308289445552938993361072669955876·10⁻¹⁰ (50 digits), inside
    (3.548125563, 3.548125564)·10⁻¹⁰.
  - The runner-up is 4.24068·10⁻¹⁰ (l = 869, real), above 4.2406·10⁻¹⁰.
  - μ♭ = λ_♯ + 4470304𝔡₁ − 3 = 5.019136·10⁻⁸. The next target is 1.388886·10⁻⁷, above 1.3888·10⁻⁷.
- **Counts.**
  - Σ_(Z₃)(n⁺ + 1) = 3,623,813,354. Over the non-real elements it is 1,227,124,256.
  - The ℬ♭ sums are 56,436,656 without, and 59,377,257 with, the two δ terms.
  - Hence 1,283,560,912 ≤ N_Λ ≤ 3,683,190,611.
- **The chain.** I coded prop:uc-dependence in exact rationals.
  - **Today's inputs** (ε_K = 1.6747·10⁻¹⁷, ε_+ = 1.67478·10⁻¹⁷, N̄_Λ = 909,507,124,095,312, D_e = 1.23382·10²⁷)
    reproduce exactly D_acc, D_NM, 21D_NM + 6, N_ι, C_* and D′_* of thm:uc-integer, prop:cs-cstar and
    rem:uc-small-reading. Hence d_NM < 7.57245·10⁵⁵.
  - **P-D0's inputs** (ε_K = 999/10¹⁶, ε_+ = 9995/10¹⁷, k̄_0 = 3, J_* = 15,000,015, l_* = 50, J′ = 765,000,816)
    reproduce every entry of the file's §4 table digit for digit:
    - L_< = 10,030,060,100,150 and L_> = R_b = 10,030,060,100,152;
    - N_ι = 2,274,483,427,581,842,436,178,649,809,456;
    - k̄_max = 58,991,214,228,154,724,547 and d̄_Φ = 4,780,982,197,210;
    - C_lev, I_base, R_base, T_12, C_* and D′_*;
    - D_acc = 45,626,410,950,904,844,471,104,575,139,346,875,130,945,114 < 4.56265·10⁴³;
    - D_NM = 91,252,821,901,800,591,008,473,304,551,381,395,888,219,703 < 9.12529·10⁴³;
    - 21D_NM + 6 < 1.91631·10⁴⁵ and 22D_NM + 345 < 2.00757·10⁴⁵.
  - F_1 = 2.0683343797703·10²³ ≤ D_e = 2.06834·10²³.
  - Δβ_0 = 9.97002999·10⁻¹⁴ exactly, and ε′_0 = 2.5·10⁻¹⁷ < 0.001ε_K.
  - 3R > 2.05384·10²³, and D_e/(3R) = 1.00706 < 1.0071.
- **N̄_Λ.** 77,112,616,084 is the least N̄_Λ with 4k̄_max + 24 > I_base + 22,119 (bisection, monotone in N̄_Λ).
  - At the proved count the ratio is 0.0478, so it fails "by a factor 21".
  - This N̄_Λ equals N₁ of thm:tr-transfer (iii) at this ε_K: 3,060,003,264·N₁ > I_base + 22,083 first holds there.
- **K ≤ 22D_NM + 345** survives: it needs J ≤ 8, and J ≤ 4(ℓ_I − ℓ♭_I) + 1 < 9 depends only on ℓ_I < 3.5.
- **The file's two labelled estimates** reproduce: 2.08·10⁴¹ and 1.49·10³⁸.

## 3. Findings

### Major

None.

### minor

**m1. thm:is-d0 (title and (c)), chapter 71 at HEAD lines 3670–3682, is unchanged and now reads as contradicting
thm:is-flat-serves.**

- After T3 the paper states two things:
  - thm:is-d0 "(When ℰ_ind can omit 𝔡₀.)": an index set omitting 𝔡₀ that serves "in every membership of
    sec:uc-index-sets" exists iff c_b ≡ 0;
  - thm:is-flat-serves: ℰ^φ_ind, which omits 𝔡₀, "may be taken for ℰ_ind in sec:uc-index-sets" whatever c_b is.
- Both are true. The difference lies in the clause "being read in the forms [[eq:is-flat-memb]]", which only
  thm:is-flat-serves and T1 state.
- The file asserts that thm:is-d0's "if and only if" concerns the order-2 form (its §3.3), but puts this nowhere in
  thm:is-d0.
- A reader meets the title before the resolution.
- **Replacement** (two whole-line texts of chapter 71 at HEAD; checked in the scratch merge):

Old:
```old
**Theorem {#thm:is-d0}** (When ℰ_ind can omit 𝔡₀.) (a) For ℰ_ind as constructed, 𝔡₀ ∈ π_1ℰ_ind
([[cor:uc-two-offsets]] (b)), at every b.
```
New:
```new
**Theorem {#thm:is-d0}** (When ℰ_ind can omit 𝔡₀ with the memberships as stated.) (a) For ℰ_ind as constructed,
𝔡₀ ∈ π_1ℰ_ind ([[cor:uc-two-offsets]] (b)), at every b.
```
Old:
```old
and at every b with A = 0, and c_(m,OAOᵀ)(OȦOᵀ) = c_(m,A)(Ȧ) for O ∈ SO(4). This paper does not determine c_b at a
rotating b.
```
New:
```new
and at every b with A = 0, and c_(m,OAOᵀ)(OȦOᵀ) = c_(m,A)(Ȧ) for O ∈ SO(4). This paper does not determine c_b at a
rotating b. With the memberships of ω̇_b(0, ·) and ġ^Υ_b(0, ·) read relative to the order 1, index sets that omit 𝔡₀
serve whatever c_b is ([[thm:is-flat-serves]]).
```
Append to the crosswalk note of thm:is-d0: "P-D0 review: title qualified; last sentence of (c) points to
thm:is-flat-serves".

**m2. lem:is-flat-uses (T3), the list of results: it omits lem:iii-i7-4-1.**

- 40:532, in the proof of lem:iii-i7-4-1 (b), cites [[eq:iii-i7-1-1]] for "ι⁺-order 2 for the first two terms"
  (χ_K ġ_b(ḃ_j), χ_K h_b(Ṡ⁽⁰⁾_j)).
- That use is of kind (i): 𝒢 = (2,0) ∪ … gives the order 2. So the theorem stands, and the proof's sentence "the
  results that use [[eq:iii-i7-1-1]] use (i)" already covers it.
- But the lemma's list reads as exhaustive.
- I found no other direct citation outside the list. Other results reach ġ only through lem:iii-i7-2-2's conclusion
  h_tot ∈ 𝒜^𝒢, which is listed.
- **Replacement** (whole lines in T3's new text):

Old:
```old
[[lem:iii-i7-2-2]], [[sec:iii-i15-2-8]], [[def:iii-i14-1-2]], [[lem:iii-i14-2-4]], [[lem:iii-j-2-1]], [[prop:iii-j3-5-2]]
and [[lem:gd-r3-5]]; and they are used there only through the following statements, each of which holds with
ℰ^φ_ind in place of ℰ_ind when ω̇_b(0, ·) and ġ^Υ_b(0, ·) are taken in the forms [[eq:is-flat-memb]]:
```
New:
```new
[[lem:iii-i7-2-2]], [[lem:iii-i7-4-1]], [[sec:iii-i15-2-8]], [[def:iii-i14-1-2]], [[lem:iii-i14-2-4]], [[lem:iii-j-2-1]],
[[prop:iii-j3-5-2]] and [[lem:gd-r3-5]]; and they are used there only through the following statements, each of which
holds with ℰ^φ_ind in place of ℰ_ind when ω̇_b(0, ·) and ġ^Υ_b(0, ·) are taken in the forms [[eq:is-flat-memb]]:
```
The crosswalk note of lem:is-flat-uses should then name lem:iii-i7-4-1.

**m3. Merged on HEAD, T6 makes thm:tr-transfer (iii) ambiguous. To be fixed with the merge, or by the chain step before
any check.**

- thm:tr-transfer (HEAD 5573) says "Take … the index sets as constructed", and (iii) then uses "the choice of
  [[def:uc-choice]] with these ε_K and ε_+".
- After T6, def:uc-choice prescribes ℰ_ind := ℰ^φ_ind. (iii) then names two different index sets.
- With ℰ^φ, the paper does not prove (iii): thm:is-flat-serves is stated at the computational point, not at h.
- With the index sets as constructed, (iii) is true as before. Its proof, sec:tr-proof (iii), already replaces (G) by
  prop:tr-lambda (b).
- **Minimal replacement**, which keeps (iii) true (checked in the scratch merge):

Old:
```old
for any ε_K, ε_+ with 0 < ε_K < ε_+ < μ(h), the choice of [[def:uc-choice]] with these ε_K and ε_+, and that
of [[def:cs-choices]], is admissible, and d_acc ≤ d_R ≤ D_acc, d_NM ≤ D_NM and N_NM ≤ 21D_NM + 6, with D_acc and D_NM of
```
New:
```new
for any ε_K, ε_+ with 0 < ε_K < ε_+ < μ(h), the choice of [[def:uc-choice]] with these ε_K and ε_+ and with the
index sets as constructed, and that of [[def:cs-choices]], is admissible, and d_acc ≤ d_R ≤ D_acc, d_NM ≤ D_NM and
N_NM ≤ 21D_NM + 6, with D_acc and D_NM of
```
What in sec:tr would need revising once 𝔡₀ is dropped there too (not drafted; it needs a proof at h):

- **thm:tr-transfer (iii) for ℰ^φ.**
  - The gap would become μ♭(h) := min({μ♭} ∪ {(⌊y_ι/𝔡₁⌋ + 1)𝔡₁ − y_ι : ι ∈ Z₃(h)}), with μ♭(h) ≥ μ(h) since Λ^φ ⊂ Λ.
  - The count would become linear in the y_ι: N_Λ ≤ 59,377,257 + Σ_(ι∈Z₃(h))(⌊(y_ι + ε_+)/𝔡₁⌋ + 1).
  - This needs thm:is-flat-serves at h. Its index-set part concerns □^Υ_b, which does not involve h, and the physical
    states, whose offsets are ≥ 1. So the extension is plausible but is not stated or proved.
- **prop:tr-lambda.**
  - (a) "the increments of real part below 1 are 𝔡₀ and 𝔡₁" becomes 𝔡₁ alone for Λ^φ.
  - (b) "(G) iff ε_K < μ(h)" stays true for the Λ built from the index sets as constructed. For Λ^φ it would read
    "iff ε_K < μ♭(h)".
  - (c) needs the linear count.
- **thm:tr-transfer (ii), prop:tr-mu-small, and the sentences built on them** (chapter 71 opening lines 30–37,
  rem:ec-lb-unbounded's last sentence, 03-theorems:365 "lower bounds that are unbounded near some γ_C", 90-scope:81–83
  "d > 2.0517 × 10¹⁰/μ(h)").
  - These are lower bounds for the index sets as constructed only.
  - prop:tr-mu-small's w_* = 356327𝔡₀ + 1116082𝔡₁ uses 𝔡₀ as an increment, so its "every admissible choice of the
    weights gives d_NM > D" does not transfer to Λ^φ.
  - Each must carry "for the index sets as the proofs construct them" once the paper's choice takes ℰ^φ_ind.
- **The sec:tr opening.** "(e) … fix the gap of (G) and the count N_Λ ([[prop:is-lambda]], [[thm:is-gap]],
  [[prop:is-count]])" and "the gap of (G) becomes the least excess μ(h)" describe the as-constructed route. At h = 10⁻⁶
  the proof of thm:uc-integer now goes through cor:is-flat.
- **sec:tr-proof (iii).** Its list of h-independent statements ("[[thm:is-d0]] … concern numbers fixed by (γ_Υ, e_Υ)")
  would need def:is-flat-set through thm:is-flat-serves. cor:is-flat is h-dependent through Z₃.
- **rem:tr-scope.** "its bound is a number only once μ(h) is known", and "N̄(10⁻⁶) ≤ 909,507,124,095,312".

**m4. The list in the file's §4 of sites left to the chain's evaluation step is incomplete at HEAD.**

- P-D0 was drafted at edafc288, before P-TR. I mapped every occurrence of an old-choice value in the merged chapter
  to its result.
- Besides the file's list, the step must also change the following.
  - **False at the new choice:**
    - rem:uc-missing (HEAD 2886–2887): "L_> = 59,831,791,007,643,520 … C_lev < 6.32812·10³⁸";
    - sec:cs-small opening (HEAD 4927): R_base = 1,407,588,774,438,516,741,176,899. The new value is
      235,964,856,912,243,213,643.
  - **True but stale, should be updated with the integers:**
    - sec:cs opening (HEAD 4391): "6N_ι + 5.13·10³¹", "C_* < 1.89844·10³⁹";
    - rem:cs-sharpness (HEAD 4900–4917): 5.13·10³¹, 5.129·10³¹, 1.9·10³⁹;
    - prop:tr-fail (HEAD 6175): "exceeds 7.5755·10⁵⁵, and so the bounds … of [[thm:uc-integer]]";
    - the paragraph after prop:tr-mu-small (HEAD 6211): "exceeds 7.57245·10⁵⁵ for h ≤ 6.46·10⁻²⁹". With
      D_NM < 9.12529·10⁴³ the threshold becomes h ≲ 5.9·10⁻²³, the same change as in rem:ec-lb-unbounded.
  - **The sec:tr statements of m3:** the opening, thm:tr-transfer, rem:tr-scope and sec:tr-proof (iii). Also the
    P-TR sentences in the chapter-71 opening, 03-theorems:360–367 and 90-scope:81–87.
  - **Crosswalk notes for eq:uc-choice (row 119) and eq:uc-deltas (row 121).** T6 and T7 change these displays. The
    eq:uc-deltas note still records Δβ_0 = 1.6713522747·10⁻¹⁷.
- **Not stale, no change needed:** cor:is-lower, thm:is-gap, lem:is-gap-z, prop:is-count, rem:gap-sums (line 181),
  cor:uc-two-offsets, and the "as constructed" sentences in sec:sp. They are all about the index sets as constructed.
- **Repairability.** None of the merged state's contradictions is beyond that step. Each is a stale value or a missing
  "for the index sets as constructed".
  - thm:uc-integer's "with the index sets as constructed" plus def:uc-choice's ε_K = 9.99·10⁻¹⁴ is inconsistent
    until the step runs: that ε_K is not admissible for the sets as constructed.
  - lem:uc-lambda (T12) cites R_b = 10,030,060,100,152 from [[eq:uc-levels]], while prop:uc-explicit still prints
    59,831,791,007,643,520.
  - The file flags both as the step's.

What the chain's evaluation step must change, in full:

- **Chapter 71:**
  - the opening, lines 18–45 (bounds, and the transfer sentence qualified);
  - thm:loss-d's last sentence and closing;
  - rem:ec-lb-unbounded (7.57245·10⁵⁵ and 6.46·10⁻²⁹);
  - rem:ec-upper-point and rem:ec-upper-open;
  - sec:uc-close;
  - prop:uc-explicit, including its proof's inequalities such as (1 + Δβ_0/2)² < 1 + 2·10⁻¹⁷, which fail at the new
    Δβ_0;
  - lem:uc-n-iota, lem:cs-levels, lem:cs-iterations, lem:cs-rest, prop:cs-cstar and lem:cs-sharp;
  - sec:cs opening, sec:cs-small opening (R_base) and rem:cs-sharpness;
  - lem:uc-small-orders, rem:uc-small-reading and prop:uc-d-small;
  - thm:uc-integer: "of [[def:uc-choice]]", eq:uc-lower qualified, "3R > 2.0538·10²³, D_e < 1.0071 · 3R";
  - rem:uc-missing;
  - prop:uc-data-order (d);
  - sec:tr per m3, prop:tr-fail, and the paragraph after prop:tr-mu-small.
- **Other chapters:** 00-front:37, 01-introduction:155–156, 03-theorems:318–319 and 360–367, 90-scope:73–87.
- **Crosswalk notes:** eq:uc-choice and eq:uc-deltas.

### nit

**n1. cor:is-flat proof (T3, reprinted verbatim from the old text): "the sums with and without … give 56,436,656 and
59,377,257" has the order reversed.**

- Recomputed: without the two δ terms 56,436,656; with them 59,377,257.
- The lower bound uses the first and the upper bound the second, as the proof's last line does.

Old:
```old
are pairwise disjoint by [[lem:is-offsets]] (c); the sums with and without λ_♯ + 1 + δ′₁ and λ_♯ + 1 + δ₂ give
```
New:
```new
are pairwise disjoint by [[lem:is-offsets]] (c); the sums without and with λ_♯ + 1 + δ′₁ and λ_♯ + 1 + δ₂ give
```

**n2 and n3. rem:is-cb-open (T3), the description of the deciding problems.**

- n2: The first-order expansion mixes b₀ = (m₀, 0) with (m, a₁J₁₂). The zeroth-order terms cancel only at m = m₀.
- n3: "(the indicial matrix [[eq:s13-nsl]] at κ = 0, with the terms of c_Υ and c_(Υ,H))" describes a radial boundary
  value problem on {r > r_h} through the model's indicial matrix at infinity. The problem is the scalar type 0 part of
  (□^Υ_(b₀))^(0); N_s0 is only its normal operator.
- **One replacement for both** (whole lines; the last line is exactly 121 characters):

Old:
```old
ω̇_(b₀)(0, J₁₂) solves ([[prop:iii-f3-2-2]] (4)), and a problem of scalar type 0 for (□^Υ_(b₀))^(0) (the indicial matrix
[[eq:s13-nsl]] at κ = 0, with the terms of c_Υ and c_(Υ,H)) whose right side is minus the scalar type 0 part of the
terms of first order in a₁ of η_((m,a₁J₁₂))(0, J₁₂) + (□^Υ_((m,a₁J₁₂)))^(0)ω̇_(b₀)(0, J₁₂); the coefficient of ρ^(2+𝔡₀)
```
New:
```new
ω̇_(b₀)(0, J₁₂) solves ([[prop:iii-f3-2-2]] (4)), and a problem of scalar type 0 for (□^Υ_(b₀))^(0), two equations of
second order whose indicial matrix at infinity is N_s0 (the upper left block of [[eq:s13-nsl]] at κ = 0), with right
side minus the scalar type 0 part of the
terms of first order in a₁ of η_((m₀,a₁J₁₂))(0, J₁₂) + (□^Υ_((m₀,a₁J₁₂)))^(0)ω̇_(b₀)(0, J₁₂); the coefficient of ρ^(2+𝔡₀)
```

**n4. rem:uc-offset-d0 (T5): "these terms need the offset 1 + 𝔡₀ only".** They need the offsets 1 + 𝔡₀ + j, with
logarithmic order at most j.

Old:
```old
relative to the order 1, as the terms of ω̇_b(1, 0) at the same root are, these terms need the offset 1 + 𝔡₀ only, and
the index sets ℰ^φ_ind and ℰ^(ι,φ)_ind obtained so omit 𝔡₀ and serve whatever c_b is ([[thm:is-flat-serves]]). With them
(G) holds for every ε_K < μ♭_Z, where μ♭_Z > ε_Υ ([[cor:is-flat]]).
```
New:
```new
relative to the order 1, as the terms of ω̇_b(1, 0) at the same root are, these terms need only the offsets
1 + 𝔡₀ + ℕ₀, and the index sets ℰ^φ_ind and ℰ^(ι,φ)_ind obtained so omit 𝔡₀ and serve whatever c_b is
([[thm:is-flat-serves]]). With them (G) holds for every ε_K < μ♭_Z, where μ♭_Z > ε_Υ ([[cor:is-flat]]).
```

**n5. Crosswalk (§7): the nine new rows give the source as "paper/reader/proofs/P-D0.md:356", without the commit.**

- All 245 existing proof-file sources carry one (for example "P-TR.md@183ef6fc:61"), since proof files are retired
  after merging.
- Use "paper/reader/proofs/P-D0.md@ace76b95:<line>". P-D0.md is unchanged since ace76b95. With that change the rows
  pass completeness and order in the scratch merge.

**n6. File only, not chapter text.**

- §5 says 𝔠 occurs "only in chapters 46, 63, 64 and 82". It also occurs in 87, unrelated.
- The old-text line numbers in §6 are those of edafc288. They are +13 at HEAD; the texts are unique, so this is
  harmless.

## 4. Overclaim check (P-D0's 13 texts, sentence by sentence)

- **No sentence states more than is proved,** apart from m1's title and the ambiguity m3 creates outside the 13 texts.
  The points below are the ones I checked specifically.
- **Accurate.** rem:is-cb-open's "do [enter them]" means "enter their construction". It is not a claim that c_b
  varies with γ_(Υ,H), ζ_∞ and χ.
- **Accurate.** "which no finite set of values decides" is a statement about what values can show, not a theorem.
- **The numerical observation is kept out.** The file's §2.2 observation, the 20-digit horizon pairing −4π²ṁ, appears
  in no text and is labelled guidance.
- **T1 and T4** say "this paper does not determine [c_b] at a rotating b" and "no bound of this chapter uses" it. Both
  are true after T3.
- **The new choice is justified as it stands:**
  - T8 uses cor:is-flat for (G) and (G⁺).
  - T12 justifies taking N̄_Λ above the proved count by the hypothesis of prop:uc-dependence, and N̄_Λ ≥ N_Λ is all
    that lem:uc-lambda (c) needs.
  - lem:uc-gaps (T10, T11) covers both families of index sets.

Verdict: CONFIRMED

## Confirmation (P-D0 at 1265f3bd480c2df7bf0300e8a43d4c4f, 948 lines; commit 5d862c93)

What was checked:

- **The diff against the reviewed version.** I compared it with 5f41b63f, as held at ace76b95. Every change answers a
  finding of this review or updates placement and bookkeeping:
  - the header and revision note;
  - §2.3 now uses m₀;
  - §3.2 adds the row 40:532, lem:iii-i7-4-1 (b), of kind (i);
  - §3.3 describes T14–T16;
  - §4's site list is replaced by a pointer to the chain step, which carries m4's list;
  - §5 adds chapter 87 and T14–T16;
  - §6 has HEAD line numbers and new T14, T15 and T16;
  - §7 has "@ace76b95" sources and the added notes for eq:uc-choice, eq:uc-deltas, thm:is-d0 and thm:tr-transfer;
  - §8 has the new checks.

  No other text changed.
- **The scratch merge.** I made a fresh git archive of HEAD, now 768e6e52. Chapter 71 there is still
  bb53f3e845095a3cd821bf51f8c12414, the same as at 99e16794.
  - All 16 old texts occur exactly once, as whole lines, at the stated lines, and none overlap: T5 2419, T13 2583,
    T6 2606, T7 2627, T8 2633, T9 2648, T10 2669, T11 2675, T12 2685, T1 2911, T2 3632, T14 3670, T15 3681, T3 3715,
    T4 3770, T16 5587.
  - T3's new text has 234 lines as stated.
- **Each change is my text.** The merged chapter 71 is byte-identical (md5 1b1056fa…) to my earlier scratch chapter:
  T1–T13 of 5f41b63f plus exactly the seven replacement blocks of this review (m1 as T14 and T15, m2, m3 as T16, n1,
  n2 and n3, n4).
- **Checks at HEAD 768e6e52 with T1–T16 applied:**
  - `lint.py --chapters`: 62 files, 5088 labels, 0 hits.
  - `assemble.py --check`: 0 problems.
  - The required one-liner prints `[] 0`.
  - No assembled line is longer than 121 characters.
- **Crosswalk.**
  - The nine rows of §7, inserted after thm:is-d0, give every chapter-71 label exactly one row, in order, with four
    fields each.
  - The ace76b95 line numbers (356 … 516) and the revised ones (405, 410, 444, 461, 470, 472, 480, 526, 566) both point
    at the right labels.
  - 5d862c93 holds 1265f3bd.
- **Numbers.** No mathematical text or number in T1–T13 changed apart from the reviewed blocks. §1–§3 of this review
  therefore stand unchanged: μ♭_Z, N_Λ, N̄_Λ, D_acc, D_NM and K.

One recommendation for the merger. This is a nit and does not block.

- Two of the cited sources differ from what will be merged: at ace76b95, rem:is-cb-open and lem:is-flat-uses do not
  yet contain n2, n3 and m2.
- So cite "paper/reader/proofs/P-D0.md@5d862c93:<line>", with the revised lines that §7 gives.
- §7 already offers this choice.

Nothing remains open. Verdict: CONFIRMED
