# Report P-D0: c_b, the free choices, and the offset 𝔡₀

Proof file: research/warp-drive/paper/reader/proofs/P-D0.md (871 lines, md5 5f41b63ff6507be43e6c87b5f286c008).
Old texts are from HEAD edafc288: chapter 71 md5 ef1085259abb5d8008f7300656235055 (unchanged since ebc73adf). Nothing
else in the repository was edited, and nothing was committed.

## Outcome, stated plainly

- **c_b at a rotating b: (d), undecidable by the paper's means.**
- **𝔡₀: dropped in full, by another route, whatever c_b is.**
- **At h = 10⁻⁶, with nothing else moved:**
  - (G) holds exactly for ε_K < μ♭_Z, with 3.548125563·10⁻¹⁰ < μ♭_Z < 3.548125564·10⁻¹⁰. This is above ε_Υ, so (G)
    costs nothing.
  - N_Λ ≤ 3,683,190,611, against 909,507,124,095,312 now.
  - The merged prop:uc-dependence gives **d_NM < 9.12529·10⁴³** (now 7.57245·10⁵⁵), N_NM < 1.91631·10⁴⁵ and
    K < 2.00757·10⁴⁵.
- **For S-HPT: do not move h.** By that report's own sequence, h stays when 𝔡₀ is dropped.

## (d): the argument in brief

**Proved (new prop:is-cb-normal).**
- Write c_b(W) = −tr(X_b W). Then X_b ∈ ker ad_A, and X is O(4)-equivariant, reflections included.
- The torus of A puts X in span{J₁₂, J₃₄}. The plane exchange and the reflections diag(1,−1,1,1) and diag(1,1,1,−1) give
  X_((m,a₁J₁₂+a₂J₃₄)) = 𝔠(m,a₁,a₂)J₁₂ + 𝔠(m,a₂,a₁)J₃₄, with 𝔠 odd in a₁ and even in a₂.
- So "c_b = 0 near b₀" is one identity, 𝔠 ≡ 0. P-UB1's φ± are a single function.

**Not decidable.**
- 𝔠 comes from the global inverse of (□^Υ_b)^(0). It depends on γ_(Υ,H) and on the free radial functions ζ_∞ and χ.
- At the computational point, invertibility of that operator is part of (AP3), which the paper leaves undecided.
- No finite computation of values shows 𝔠 ≡ 0.
- One certified non-zero value would show c_b ≢ 0 for the data at which it is taken.
- **Computation that would decide it:**
  - Two radial boundary value problems on r > r_h at explicit ζ_∞, χ, γ_(Υ,H):
    - the vector type 1 ODE for ω̇_(b₀)(0, J₁₂);
    - the scalar type 0 2×2 system with the first-order source.
  - Then read the coefficient of ρ^(2+𝔡₀).
  - This needs a certified integration of a few thousand steps plus asymptotic matching.
  - (AP3) at those data comes first, and it is the larger task.

**Numerical observation (guidance; in the file's section 2.2, not in the paper).**
- The horizon pairing ℓ_b(2δGġ_b(ṁ, Ȧ)) equals −4π²ṁ to 20 digits, on the exact Myers–Perry metric up to |A| = 0.3.
- So the 1/γ_(Υ,H) term of the Schur complement vanishes. Even small γ_(Υ,H) does not decide c_b at leading order.

## The route that drops 𝔡₀

1. thm:is-d0 (c)'s "if and only if" holds only for the membership written relative to ω̇_b(0, ·)'s own leading order 2.
2. The terms of ω̇_b(0, ·) at 2 + 𝔡₀ + ℕ₀ carry logarithmic order at most j at 𝔡₀ + j. They can be recorded relative to
   order 1, as 1 + 𝔡₀ + ℕ₀.
3. ω̇_b(1, 0) already has those pairs with the same orders: 1 + ℰ_(𝔡₀) ⊂ ℰ^φ_ind.
4. An audit of every citation found that ω̇_b(0, ·) and ġ^Υ_b(0, ·) are used in only three ways:
   - combined with the mass state (𝒢 and (1,0)∪(1+ℰ));
   - through ℰ_col;
   - through their weights and leading terms.

   They never enter a formal solution, a tower or a row, which is where an offset becomes an increment of Λ. The
   paper's v1 terms are h_(b,v1)(V) = ½ġ^Υ_b(0, [A, A_V]), and c_b vanishes on im ad.
5. So ℰ^φ_ind serves unconditionally (thm:is-flat-serves). This is P-UB1's ℰ′_ind, typed by parity.
6. cor:is-flat therefore holds without c_b = 0, and its μ♭_Z and N_Λ apply.
7. The same device cannot remove 𝔡₁: the translation corrections are s1 terms of the formal solutions at ι⁺, and their
   term at ρ^(2+𝔡₁) is a genuine increment.

## Free choices found

| choice | status | does c_b depend on it? |
|---|---|---|
| e_Υ, γ_Υ | fixed at 1/100 | yes |
| γ_(Υ,H) | free | yes |
| ζ_∞ (in c_Υ) | free | yes |
| χ (in c_(Υ,H)) | free | yes |
| trace weight 2/3 | forced | — |
| E_C (γ_C, v_C, e_C; interior of c_C) | | no |
| t_* | | no |
| inversion weight | | no |
| r_0 | | not examined |
| family g_b | fixed | yes |
| basis of states | fixed | — |
| index sets ℰ_ind, ℰ^ι_ind, ℰ_++, ℰ^C_I, ℰ_+ | free while they serve | no; this is the freedom the route uses |
| weights, orders, cut-offs | | no |

## New inputs for the chain (exact)

- ε_K = 9.99·10⁻¹⁴ = 999/10¹⁶.
- ε_+ = 9.995·10⁻¹⁴ = 9995/10¹⁷.
- N̄_Λ = 77,112,616,084.
- Unchanged: k̄_0 = 3, J_* = 15,000,015, l_* = 50, J′ = 765,000,816, ε_Υ = 1.4619·10⁻¹⁰.
- Derived: Δβ_0 = 9.97002999·10⁻¹⁴ exactly; ε′_0 = 2.5·10⁻¹⁷.

**Why N̄_Λ is above the proved count.** The proved bound is N_Λ ≤ 3,683,190,611. N̄_Λ = 77,112,616,084 is the least
integer for which prop:uc-dependence's hypothesis 4k̄_max + 24 > I_base + 22,119 holds; at the proved count it fails by
a factor of 21. The other hypothesis, ε_+ < 10⁻¹³, is what caps ε_K.

**Resulting bound (prop:uc-dependence evaluated exactly; the formulas reproduce today's integers).**
- D_acc < 4.56265·10⁴³.
- D_NM = 91,252,821,901,800,591,008,473,304,551,381,395,888,219,703 < 9.12529·10⁴³.
- 21D_NM + 6 < 1.91631·10⁴⁵.
- 3R > 2.0538·10²³ at the choice.

**What-ifs (estimates, not drafted).**
- If the inequality hypothesis were dropped, N̄_Λ = 3,683,190,611 would give d_NM ≈ 2.08·10⁴¹.
- If ε_+ < 10⁻¹³ were also relaxed, ε_K ≈ 1.4·10⁻¹⁰ would give ≈ 1.49·10³⁸.

## Texts

Thirteen texts, all in chapter 71, disjoint, at HEAD line numbers.

**New results**, inserted after thm:is-d0:
- prop:is-cb-normal;
- rem:is-cb-open;
- def:is-flat-set;
- lem:is-flat-memberships;
- lem:is-flat-uses;
- thm:is-flat-serves.

**cor:is-flat**: its hypothesis is replaced; the rest of the corollary is verbatim.

**The choice**:
- def:uc-choice;
- lem:uc-admissible (three texts);
- lem:uc-gaps (two texts);
- lem:uc-lambda.

**Narrative**:
- thm:uc-reduction (iii);
- the sec:is opening;
- the sec:is-smaller opening;
- rem:is-summary;
- rem:uc-offset-d0.

**Checks.** On a scratch copy:
- lint --chapters: 0 hits;
- assemble --check: 0 problems;
- assemble, then lint --paper: 0 hits.

The file lists crosswalk rows for the 9 new labels.

**Sites left to the chain's evaluation step** (listed in the file's section 4):
- the chapter opening;
- thm:loss-d;
- rem:ec-lb-unbounded;
- rem:ec-upper-point and rem:ec-upper-open;
- sec:uc-close;
- prop:uc-explicit through prop:uc-data-order (d);
- thm:uc-integer: "index sets as constructed" becomes "of def:uc-choice", and eq:uc-lower must be qualified;
- 00-front, 01-introduction, 03-theorems, 90-scope.

## Not proved

- The value of c_b at a rotating b.
- Whether 𝔡₁ can be omitted. The argument above says this route cannot do it.
- Anything at another h.
- That prop:uc-dependence could do without its inequality.

Scratch work (scripts, numeric checks, chain evaluation):
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pd0/

## Revision after the review R-P-D0 (no Major)

Proof file now: research/warp-drive/paper/reader/proofs/P-D0.md, md5 1265f3bd480c2df7bf0300e8a43d4c4f, 948 lines
(was 5f41b63ff6507be43e6c87b5f286c008, 871 lines, as read by the review at ace76b95). Old texts are now from chapter 71
at HEAD 99e16794 (P-TR merged), md5 bb53f3e845095a3cd821bf51f8c12414. HEAD later moved to 598f56ab; chapter 71 has
the same md5 there. Not committed; nothing else in the repository was edited.

Delta:

- m1: new T14 (thm:is-d0 title: "with the memberships as stated") and T15 (one sentence appended to (c), pointing to
  thm:is-flat-serves). These are the review's exact texts. The crosswalk note for thm:is-d0 is added.
- m2: lem:iii-i7-4-1 is added to the list in lem:is-flat-uses (T3) and to the 40:… row of the audit (section 3.2).
  The crosswalk row note for lem:is-flat-uses names it.
- m3: new T16 (thm:tr-transfer (iii): "and with the index sets as constructed"). This is the review's exact text, and
  a crosswalk note is added. The rest of sec:tr for 𝔡₀ dropped at other h is not drafted; it needs a proof at h.
- n1 in T3's verbatim tail: "without and with".
- n2 and n3 in rem:is-cb-open (T3): the review's text. m₀ is now also used in section 2.3.
- n4 in T5: "only the offsets 1 + 𝔡₀ + ℕ₀".
- n5: the crosswalk sources are "P-D0.md@ace76b95:<line>", with the lines of the ace76b95 version. Section 7 also
  gives the labels' lines in this revision: 405, 410, 444, 461, 470, 472, 480, 526, 566.
- n6: chapter 87 is added to the 𝔠 note in section 5.
- m4: the section 4 site list is replaced by a pointer to the chain's evaluation step, with the review's list going to
  that step.
- Crosswalk notes for eq:uc-choice (T6) and eq:uc-deltas (T7) are added to section 7's list of notes.
- Placement: T1–T13 line numbers are +13 at HEAD.

Checks, on a fresh scratch merge of all sixteen texts into HEAD's reader directory:

- lint --chapters: 62 files, 5072 labels, 0 hits.
- assemble --check: 0 problems.
- assemble, then lint --paper (scratch copy only): 0 hits, and no assembled line is over 121 characters.
- With the nine crosswalk rows inserted after thm:is-d0:
  - 280 labels, 280 rows, in chapter order;
  - each row has 4 fields.
- In the real directory, with the file copied in: lint --chapters 0 hits, and assemble --check 0 problems.
