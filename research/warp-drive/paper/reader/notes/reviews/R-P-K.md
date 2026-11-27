# R-P-K: independent reading of proofs/P-K.md (md5 6c7eb17393ce45f0f67b0d52cbd36773)

**Verdict: NOT CONFIRMED.** I found no Major issue: the count k′_k = 282 + L_P, d_0 = 309, d_1 = 22d + 291 + L_P,
K = d_1 + 14 is right for k ≥ 1, and every numerical bound recomputes exactly. I found six minor issues and twelve nits.
The minor issues are: a gap at k = 0 and three missing ranges of n; a clash of the symbol a; a hypothesis on the lowering
in Step 1 that is never needed; placement texts that overstate how L_P depends on the parameters or where the count
applies; and one wrong phrase in the remark. Each has an exact replacement below.

Line numbers are those of proofs/P-K.md. "Resolved" means after the assembler resolves the labels. I checked every
proposed replacement below against the same rules: at most 121 characters before and after resolution, no forbidden
start of a wrapped line, and no hit of the lint patterns.

## Answers to the writer's six questions

- **(a) The jet argument (Step 1, data loss p + 1): correct.** The data of Rh are Rh|_Σ (jet of order p) and
  rℒ(Rh)|_Σ (jet of order p + 1). The jet of order q is polynomial in the derivatives along Σ of h₀ up to order q and of
  h₁ up to order q − 1. So data of Rh at the order j + 4 need (h₀, h₁) at the order j + 5 + p, below the order j + 6 + p
  at which the forcing reads h. One clarity nit (N6).
- **(b) The Taylor argument (pull-back costs 2 in ℬ): correct** for the two classes: no logarithms, z ≥ 2, and
  z + 2 ≥ 4 > ℓ₀. c_1 is a coefficient in H^(j−1). c_2, with j − 2 b-derivatives, lies in the remainder H^(j−2,ℓ₀)_b.
  One nit (N2).
- **(c) The loss 1 in prop:iii-c2-4-1: correct.** In the proof of prop:iii-c2-4-1, h̃₁ is algebraic in k̃ and in
  ∇^(g₀) − ∇^(g_(b₀)), which is linear in the first derivatives of γ̃. An x-derivative is r⁻¹ times a b-derivative, so
  h̊_1 = rh̃₁ at the order n reads γ̃ at the order n + 1 and k̃ at the order n.
- **(d) The counts in (S, S⁰): correct for n ≥ 4, but the lemma states them for n ≥ 1** (finding 2). The tame estimate
  eq:iv2-2-3 at the order n reads F₁ and the data at the orders n + 4 and 8, and h at the orders n + 7 and 10.
- **(e) d is the same in the half-integer class: correct.** prop:own-same-index-sets gives ℰ^((m))(ℰ_0^½) =
  ℰ^((m))(ℰ_0^ℤ) as index sets, logarithmic orders included. With the weights of thm:own-half-settling, ℰ^C_I, Λ, ε_+,
  ε_K and α are therefore the same. The d's of lem:iii-k-2-2, lem:iii-k-2-3 and prop:iii-j2-4-3 are built on Ω_*, away
  from I₀, from these alone. The data enter only through constants (lem:iii-k-2-2 (c), eq:s27-rinv). This agrees with
  rem:half-class-changes in chapter 62 and with rem:own-half-changes (b).
- **Lowering below 1/6 in Step 1.** The lowering is the proof's own free choice, so the hypothesis is a legitimate
  reading of the paper's wording. Re π₁ℰ₀ is discrete, so any bound can be met. But no lowering is ever needed in the two
  classes, so the hypothesis should be removed rather than stated (finding 1).

## Findings

### 1. minor — the lowering hypothesis is unnecessary (lines 40–41, 85–88, 174)

Current (40–41):

    [[thm:vi-c-2-1]], with ℰ_0 of [[eq:vii-0-1]] or of [[eq:half-class]], and let each lowering of α₀ in Step 1 of the
    proof of [[thm:iii-c1-3-1]] be less than 1/6. Uniformly for |S| + |S⁰| ≤ σ_0, and for n as stated:

Current (85–88):

    (iii) *The number of steps.* ℓ^♭_0 = 3/2 + ½(1 − e_Υ)γ_Υ lies in (3/2, 13/8), as 0 < e_Υ < 1 and γ_Υ < ¼. A step raises
    the weight by more than 5/6 unless it reaches ℓ₀, the lowering being less than 1/6; so after two steps the weight
    exceeds 3/2 + 5/3, and the third step reaches ℓ₀ < 4, which is not lowered, as ℓ₀ ∉ Re π₁ℰ₀. At the first step
    α₁ ≤ ℓ^♭_0 + 1 < 3, at the second α₁ < ℓ^♭_0 + 2 < 4, and at the third α₁ = ℓ₀ < 4. ℰ_0 of [[eq:vii-0-1]] has the

Current (174):

    as in [[thm:vi-c-2-1]], with the lowerings of [[lem:uc-data-losses]], let d be the loss with which [[thm:iii-k-3-2]]

What is wrong: Step 1 lowers α₀ only "if needed", that is, only if α₁ = min(α₀ + 1, ℓ₀) ∈ Re π₁ℰ₀. In both classes
Re π₁ℰ₀ ⊂ ½ℤ. Step 1 starts at α₀ = ℓ^♭_0 ∈ (3/2, 13/8). Its candidates are therefore ℓ^♭_0 + 1 ∈ (5/2, 21/8),
ℓ^♭_0 + 2 ∈ (7/2, 29/8) and ℓ₀ ∉ Re π₁ℰ₀, and none of them is in Re π₁ℰ₀. So no lowering ever occurs. As written,
the lemma (and through "with the lowerings of", the proposition) places a condition on the proof of a theorem of
chapter 45. The condition is harmless, but the text never shows that the paper allows it.

Proposed (40–41):

    [[thm:vi-c-2-1]], with ℰ_0 of [[eq:vii-0-1]] or of [[eq:half-class]]. Uniformly for |S| + |S⁰| ≤ σ_0, and for n
    as stated:

Proposed (85–88; the line that follows stays, refill):

    (iii) *The number of steps.* ℓ^♭_0 = 3/2 + ½(1 − e_Υ)γ_Υ lies in (3/2, 13/8), as 0 < e_Υ < 1 and γ_Υ < ¼. In both
    classes Re π₁ℰ₀ ⊂ ½ℤ, while ℓ^♭_0 + 1 ∈ (5/2, 21/8) and ℓ^♭_0 + 2 ∈ (7/2, 29/8) are not in ½ℤ, and ℓ₀ ∉ Re π₁ℰ₀; so
    Step 1 never lowers α₀. Its first step gives α₁ = ℓ^♭_0 + 1 < 3, its second α₁ = min(ℓ^♭_0 + 2, ℓ₀) < 4, and, if
    ℓ^♭_0 + 2 < ℓ₀, a third gives α₁ = ℓ₀ < 4, as ℓ^♭_0 + 3 > 4 > ℓ₀. ℰ_0 of [[eq:vii-0-1]] has the

Proposed (174, refill the paragraph):

    as in [[thm:vi-c-2-1]], let d be the loss with which [[thm:iii-k-3-2]]

The counts p ≤ 1, 2, 2 and p ≤ 2, 4, 4 (lines 89–90) and L_0 ≤ 23, 28 then stand unchanged. This also makes Step 1's
weights the same in the two classes, as prop:own-same-index-sets asks. The writer's report (§4, item 2) should then drop
the lowering from what is "bounded, not fixed".

### 2. minor — k′_0 is not 282 + L_P, and three ranges of n are missing (lines 50, 56, 62, 92, 121–122, 164, 178, 217, 236–237; placement 4)

Current (178): `(a) [[prop:iii-k-1-2]] holds with d_0 := 309, and its part (3) holds with k′_k := 282 + L_P for every k.`

Current (217): `*k′_k.* Fix k ≥ 0, and put m := k + 2 and n := m + L_P; then n ≥ 9, as L_P ≥ L_0 ≥ 7. By (iii) and (iv) of`

Current (121–122):

    (iv) The bound for J is part of Step 2 of the proof of [[thm:iii-c1-3-1]]. In one repetition the right side f̃ of
    [[eq:iii-c1-3-5]] at the order j reads h at the order j + 2: R̃_b ∈ ρ₀²ρ_I²C^∞Diff²_b, and the second term is a

What is wrong:

- **(iv) needs n ≥ 3.** The quadratic part of f̃ is bounded by lem:iii-c-2-1, which asks the order of a product to
  exceed d/2 = 5/2 (𝒟⁺ has dimension 5). At an order j ≤ 2 it gives f̃ only through the order 3, so it reads h at the
  order 5, not j + 2. In the proof of (a), the last repetition of Step 2 runs at j = m = k + 2. At k = 0 this is j = 2.
  There the count gives the data order 283 + L_P, so k′_0 = 283 + L_P, not 282 + L_P.
- **(vi) needs n ≥ 4.** eq:iv2-2-3 at the order n reads N(F₁, ∂(h⁰, h¹); 8), that is the data at the order 8 and F₁ at
  the order 8, hence h at the order 10. Its constant asks h small in 𝒜^10. Both are within n + 4 and n + 7 only for
  n ≥ 4. The lemma states (vi) for n ≥ 1.
- **(iii) needs n ≥ 1** (line 92 takes j ≥ 0). thm:iv3-2-1 is stated for k ≥ 1, and its order 0 comes from its order 1.

None of this touches d_1 or K. The proof uses (iii) at n ≥ 4, (iv) at n ≥ 2 and (vi) at n ≥ 9. The paper uses (3) only
at the orders j + 3 and k + 3 ≥ 3: eq:s27-theta, lem:iii-k-2-2 (d), lem:iii-k-2-3, the proof of thm:iii-k-3-2 and
prop:ec-delta-cap. I grepped every use of k′ in chapter 46. But "for every k" and placement 4's "a constant serves" are
not proved at k = 0.

Proposed (50, first line of (iii)):

    (iii) (the expansion at I₀, n ≥ 1) Step 1 has at most three steps, L_0 ≤ 23, and L_0 ≤ 28 for ℰ_0^½; the triple

Proposed (56–57):

    (iv) (the expansion at ℐ⁺, n ≥ 3) J ≤ 4(ℓ_I − ℓ^♭_I) + 1, and the triple in H^(n+2J,(ℰ_0,ℓ_0),(−,ℓ^♭_I))_b(𝒟⁺)
    controls it in ℬ^n;

Proposed (62):

    (vi) (the derivatives in (S, S⁰)) for n ≥ 4, h_(S,S⁰) in 𝒜^(n+7) and ∂(h⁰, h¹) in 𝒜^(n+4)_Σ control ∂h_(S,S⁰) in 𝒜^n;

Proposed (92): replace "and let j ≥ 0." by "and let j ≥ 1.".

Proposed (121–122, refill):

    (iv) The bound for J is part of Step 2 of the proof of [[thm:iii-c1-3-1]]. In one repetition the right side f̃ of
    [[eq:iii-c1-3-5]] at an order j ≥ 3 reads h at the order j + 2 ([[lem:iii-c-2-1]] asks the order of a product above
    5/2): R̃_b ∈ ρ₀²ρ_I²C^∞Diff²_b, and the second term is a

Proposed (164, the sentence after the display):

    with C uniform for h small in 𝒜^10 and for |S| + |S⁰| small; for n ≥ 4 the orders 8 and 10 are at most n + 4 and n + 7.

Proposed (178):

    (a) [[prop:iii-k-1-2]] holds with d_0 := 309, and its part (3) holds with k′_k := 282 + L_P for every k ≥ 1, and at
    k = 0 with k′_0 := 283 + L_P.

Proposed (217):

    *k′_k.* Fix k ≥ 1, and put m := k + 2 and n := m + L_P; then m ≥ 3, as (iv) asks, and n ≥ 10, as L_P ≥ L_0 ≥ 7. By

Proposed (236–237, replacing "‖(γ̃, k̃)‖_(k+k′_k) ≤ s, … as (3) asks."):

    ‖(γ̃, k̃)‖_(k+k′_k) ≤ s, which is finite for s ≤ s_k and tends to 0 with s. At k = 0 the left side of (3) at the order 2
    is at most that at the order 3, so (3) holds with k′_0 := 1 + k′_1 = 283 + L_P. For k ≥ 1, where the proofs use (3)
    (at the orders j + 3 of [[eq:s27-theta]] and k + 3 of [[lem:iii-k-2-2]] (d)), k′_k is constant, so non-decreasing.

Proposed placement 4 (new text; this also covers finding 5):

    uses it). We take k′_k non-decreasing in k ≥ 1, the orders at which (3) is used; in the classes of [[eq:vii-0-1]] and
    [[eq:half-class]] a constant serves there ([[prop:uc-data-order]]).

An alternative keeps "for every k" and placement 4's "a constant serves" as they are. It takes m := k + 3 throughout,
so that k′_k := 283 + L_P for every k. All the printed integers then rise by 1: 291 → 292, 305 → 306, 348 → 349,
344 → 345, 330 → 331, 347 → 348, 335 → 336, 339 → 340, and the last digit of the three long integers rises by 1. I
checked that every decimal bound (3.45745·10⁵¹, 5.7624·10⁵⁰, 1.15248·10⁵¹, 4.78156·10¹⁰³, 1.0078·10⁵¹) survives that
change. Crosswalk row 3 should then read "k′_k = 282 + L_P (k ≥ 1)" or "283 + L_P".

### 3. minor — the symbol a is used for two different things (lines 14, 45–46, 213, 225–226, 230, 233–234)

Current (14): `of [[eq:half-class]]. Put a := 132 = 153 − 21: the data of [[thm:iv3-2-2]] and of [[thm:iv2-3-1]] at the order 153 + k`

What is wrong: the same proposition also uses a for the weight a ∈ (ℓ0 − 1, 3) of thm:own-data. It appears in the
statement (c), in eq:uc-kstar-own, in K*(a, M, k1), in (d) and in the proof of (c). Line 233 has "L_0 ≤ 28 < a + 9",
with a = 132, and line 259 has "a > ℓ0 − 1 > 2", with a the weight.

Proposed (14):

    of [[eq:half-class]]. Put L_F := 132 = 153 − 21: the data of [[thm:iv3-2-2]] and of [[thm:iv2-3-1]] at the order 153 + k

and replace a by L_F at its other uses: line 45 "max(n, 21) + L_F", line 46 "max(n, 21) + L_F", line 213
"𝒜^(155+L_F)_Σ", line 225 "𝒜^(n+13+L_F)_Σ" and "𝒜^(n+15+L_F)(𝒪_𝒟)", line 226 "𝒜^(n+15+2L_F)_Σ" and
"𝒜^(n+15+L_F)(𝒪_𝒟)", line 230 "ℬ^(n+6+L_0+L_F)_Σ", line 233 "L_0 ≤ 28 < L_F + 9, n + 6 + L_0 + L_F < n + 15 + 2L_F" and
"ℬ^(n+15+2L_F)_Σ", and line 234 "n + 16 + 2L_F". Refill where lines lengthen. L_F occurs in no chapter.

### 4. minor — "fixed by ℓ0 and ℓ_I" contradicts the remark (placements 2, 3, 8)

Current (placement 2, lines 333–334):

    [[thm:iii-k-4-3]] is 22d + 291 + L_P and the order of the approximant of [[thm:settling]] is K = d_1 + 14, L_P ≤ 43
    being a number of derivatives fixed by ℓ_0 and ℓ_I; at that point K is at most an integer below 3.45745 × 10⁵¹

Current (placement 3, lines 345–346):

    the orders that [[prop:uc-data-order]] counts, d_1 = 22d + 291 + L_P and K = 22d + 305 + L_P, where L_P ≤ 43 is a number
    of derivatives fixed by ℓ0 and ℓ_I. d is not evaluated on the set where [[thm:settling]] is proved; at the

Current (placement 8, lines 402–403):

    of the approximant of [[thm:settling]] is K = d_1 + 14 = 22d + 305 + L_P, with L_P ≤ 43 a number of derivatives fixed
    by ℓ0 and ℓ_I, so that at that point K is at most an integer below 3.45745 × 10⁵¹ ([[prop:uc-data-order]]). The

What is wrong: L_0 depends on ℓ^♭_0, that is on the gauge parameters (γ_Υ, e_Υ): whether ℓ^♭_0 + 2 < ℓ₀ decides between
two and three steps. J depends on ℓ^♭_I and on the ν chosen in Step 2. rem:uc-data-order-limits itself says L_0 and J
"are bounded, not fixed". Placements 5–7 already use the right phrase, "an explicit number of derivatives". In
placement 2, "at that point" also refers back past a sentence about other formulas, to "That parameter point".

Proposed (placement 2, lines 2–3 of the new text):

    [[thm:iii-k-4-3]] is 22d + 291 + L_P and the order of the approximant of [[thm:settling]] is K = d_1 + 14, L_P ≤ 43
    being an explicit number of derivatives; at the computational point K is at most an integer below 3.45745 × 10⁵¹

Proposed (placement 3, lines 2–3 of the added text):

    the orders that [[prop:uc-data-order]] counts, d_1 = 22d + 291 + L_P and K = 22d + 305 + L_P, where L_P ≤ 43 is an
    explicit number of derivatives. d is not evaluated on the set where [[thm:settling]] is proved; at the

Proposed (placement 8, lines 2–3 of the new text):

    of the approximant of [[thm:settling]] is K = d_1 + 14 = 22d + 305 + L_P, with L_P ≤ 43 an explicit number of
    derivatives, so that at that point K is at most an integer below 3.45745 × 10⁵¹ ([[prop:uc-data-order]]). The

### 5. minor — placements 4 and 5 state the count where chapter 46 allows a general data class (lines 356, 364–365)

Current (placement 5 new text):

    d_1 := max(d_0, N_NM + k″), with d_0 of [[prop:iii-k-1-2]] ([[prop:uc-data-order]] evaluates d_0 and k′_k, which gives
    d_1 = 22d + 291 + L_P, L_P ≤ 48 an explicit number of derivatives). By [[lem:iii-k-2-2]] (d),

What is wrong: thm:iii-k-3-2 and prop:iii-k-1-2 hold for every ℰ_0, ℓ_0 of row d1 (sec:iii-k-0), which allows ℓ_0 > 4
and other index sets. lem:uc-data-losses is proved only for eq:vii-0-1 and eq:half-class: it uses z ≥ 2, ℓ₀ < 4 and no
logarithms. For a general class of row d1, "L_P ≤ 48" is false. Placement 4 needs the same restriction; it is included
in the replacement under finding 2.

Proposed (placement 5 new text):

    d_1 := max(d_0, N_NM + k″), with d_0 of [[prop:iii-k-1-2]] ([[prop:uc-data-order]] evaluates d_0 and k′_k in the classes
    of [[eq:vii-0-1]] and [[eq:half-class]], which gives there d_1 = 22d + 291 + L_P, L_P ≤ 48 an explicit number of
    derivatives). By [[lem:iii-k-2-2]] (d),

### 6. minor — "an additive term of at most 48 derivatives" is wrong (lines 302–303)

Current:

    **Remark {#rem:uc-data-order-limits}** (What the count gives and what it does not.) [[prop:uc-data-order]] makes d_1
    and K explicit in d, with an additive term of at most 48 derivatives, and makes the threshold K* of [[thm:own-data]]

What is wrong: d_1 = 22d + 291 + L_P and K = 22d + 305 + L_P, so the additive terms are at most 339 and 353. The number
48 bounds only L_P.

Proposed:

    **Remark {#rem:uc-data-order-limits}** (What the count gives and what it does not.) [[prop:uc-data-order]] makes d_1
    and K explicit in d, with the additive terms 291 + L_P and 305 + L_P, L_P ≤ 48, and makes the threshold K* of

(the line that follows, "[[thm:own-data]] explicit as a quadratic in d_1; …", then begins with "[[thm:own-data]]";
refill).

### Nits

- **N1 (line 75).** "(row d1)" has no reference. Proposed: `tends to 0 with ‖(γ̃, k̃)‖_(n+1), the index sets being
  closed under sums and positive multiples (row d1 of` / `[[sec:vi-c-1]]). The weight and` (refill line 76).
- **N2 (line 147).** "c_0 is u_z composed with Y(0, ·)" omits the factor α(0, ·)^z. Proposed: `α^z u_z(Y) = c_0 + ρ₀c_1
  + ρ₀²c_2(ρ₀, y), where c_0 = α(0, ·)^z u_z(Y(0, ·)), c_1 contains first derivatives of u_z,`
- **N3 (lines 309–310).** rem:ec-not-evaluated does not mention λ_2. Its non-evaluation is stated in the paragraph after
  thm:own-data. Proposed: `whose constants C(q) of [[eq:near-lines]] are not evaluated, and the thresholds λ1, δ and
  λ_2 are not evaluated` / `([[rem:ec-not-evaluated]] and the paragraph after [[thm:own-data]]).`
- **N4 (placements 6, 7).** Chapter 63 changed after the file was written (commit 003371f6 added a line to its opening
  paragraph). The old texts still occur exactly once, but item 6 is now at line 68 (not 67) and item 7 at lines 292–294
  (not 291–293). In item 6, "the four lines that follow it" should be "the three lines that follow it". Lines 69–71
  follow it, ending "[[sec:own-proof]]; its first step checks every use of k_P.".
- **N5 (lines 5–7).** k′_k is not "the order at which (3) reads the data". (3) reads the data at the order k + k′_k.
  Proposed for line 6: `applies [[thm:ii-g-2-1]], N_NM = 21d + 6, d_0 is the regularity of [[prop:iii-k-1-2]], and
  k + k′_k is the order at which` (121 characters, fewer resolved).
- **N6 (line 101).** "the jet of h on Σ^IVP of order at most p + 1 in a direction transversal to Σ^IVP" can be read
  as transversal order only. The count needs total order, as the next sentence assumes. Proposed: `from the jet of h on
  Σ^IVP of order at most p + 1 (its b-derivatives of total order at most p + 1). The equation is`
- **N7 (line 234–235).** The control gives LHS < 1 only for data strictly below s, while ω_k takes ‖·‖ ≤ s, so ω_k(s_k)
  is not covered. Proposed for line 235: `this control at η := 1 halved, and ω_k(s) the supremum of the left side of (3) over
  the parameters and the data with`
- **N8 (line 212).** On domains, H^k is a quotient norm (sec:s27-local), so the sum bound holds only up to a constant.
  Proposed: `order its norm on 𝒪_𝒟 is at most a constant times the sum of its norms on the three parts, which (ii)
  bounds:` (refill).
- **N9 (lines 263–265).** θ_k is used without its definition. Proposed: end the display with "," instead of "." and
  begin line 265 with `with θ_k = (k − 4)/5 as in [[lem:own-e-flux]]. They increase with i, and M + k1 + 1 = 3k1 + 18;
  so` (refill).
- **N10 (placement 10).** lem:viii-2-1 (chapter 48) also names "k′_k as in lem:iii-k-2-2 (d)". It stands, and could be
  listed among the unchanged results.
- **N11 (outside P-K, for the coordinator).** "Section [[sec:…]]" resolves to "Section Section 44.5" and similar, 20
  times in the current PAPER.md, including line 69 of chapter 63, which placement 6 keeps. P-K's own text has no
  instance.
- **N12 (the writer's report, not the proof file).** The Placement section has eight old/new texts (items 2–9), not
  nine. Item 1 is the insertion, and item 10 lists what stays unchanged.

## What I checked and found correct

- **Labels.** All 75 existing labels cited by P-K resolve, each to the result the text says it is: thm:iv3-2-2's last
  clause (153 + k → 21 + k); thm:iv2-3-1; eq:iv2-2-3 (loss 4, tame term ‖h‖_(k+7)N(8)); thm:iv3-2-1 (k ≥ 1, h small in
  H^10); thm:iii-c2-3-1 (k₂ = 308); prop:iii-c2-4-1; (N) of sec:s27-local (r₀ = 4); lem:iii-a-1-3 (converse costs
  |E_(H,≤)|; direct part keeps the order); lem:iii-a-1-2 and lem:iii-a-3-2 (same order k); lem:iii-c-2-1 (k > d/2);
  prop:iii-c-4-4 (Neumann series in Step 1; coefficients of order k − 2); lem:s27-translated-exterior (a)–(c);
  lem:s27-cover (e); the proof of prop:iii-k-1-2 (𝒪, 𝒰′, *Gluing*, *The modulus*, (3), F₁); eq:s27-theta,
  lem:iii-k-2-2 (c), (d), eq:s27-rinv; thm:iii-k-3-2 *Smallness* (d_1 := max(d_0, N_NM + k″)); sec:vii-4, lem:vii-1-1,
  cor:vii-2-3, eq:vii-2-1, eq:vii-2-2, lem:vii-0-1; prop:own-same-index-sets, thm:own-half-settling,
  rem:own-half-changes, lem:own-e-flux and eq:own-kstar; def:ec-point, def:uc-choice (ℓ_I < 3.5), def:cs-choices,
  thm:uc-integer, eq:uc-lower, prop:uc-d-small (b)–(d), lem:uc-small-orders, rem:uc-small-reading, rem:ec-point-outside,
  rem:ec-not-evaluated. The six new labels are defined nowhere else.
- **The count, step by step.** (i) loss 1; (ii) loss 132 above order 21, and the backward clause; per step of Step 1,
  p + 6 for h and p + 5 for the data; per repetition of Step 2, 2; pull-back 2 + l in 𝒜 and 4 + l in ℬ; (vi) +7, +6 and
  +4. The composition gives the triple in 𝒜^n from h at n + 13 and from data at n + 10 (l = 1, 2). h at n + 13 comes from
  (h⁰, h¹) at n + 13 + 132, which come from h_0 on 𝒪_𝒟 at n + 15 + 132, which comes from h̊ at n + 15 + 264. The ℬ route
  needs only h̊ at n + 6 + L_0 + 132 < n + 15 + 264. With (i), the data order is n + 16 + 264 = k + 282 + L_P (k ≥ 1).
- **Completeness.** Every consumer of data derivatives in the proofs of thm:settling and its inputs is accounted for.
  - d_0 = 309: thm:iii-c2-3-1 (308 → 309); thm:iv3-2-2 for every (S, S⁰) (153 → h_0 at 155 → h̊ at 287 → 288); (N),
    H^5 × H^4; and γ̃ in H³_b.
  - N_NM + k″ = 22d + 291 + L_P covers the threshold constants up to order N_NM: the map through Θ_k, the right inverses
    through Θ_(k+d), lem:iii-k-2-2 (d) at 2d + 3, the smallness conditions Θ_0 and Θ_d < ε_0, and the threshold
    ε^G_NM of prop:vii-3-2 and of cor:s27-rate, which run the same estimates.
  - The bounds at every order k (on e_S, e_(S⁰)) enter only C_k with k > N_NM, which the threshold does not read.
  - The gluing takes k = d_1 + 5 (eq:vii-2-2 in C^(k−1), C^(k−2); lem:vii-0-1 in C^(d_1+3)). eq:vii-2-1 asks
    C^(k+4) × C^(k+3) of the data, hence C^(k+5) of g_λ, which lem:vii-1-1 gives at J = k + 5, K = J + 4. So
    K = d_1 + 14 and N = K + 3.
  - I found no consumer that the count misses.
- **Arithmetic** (exact integers and fractions):
  - 22D_acc + 344 is the printed 52-digit integer, < 3.45745·10⁵¹.
  - 22D_b + 344 and 22D_c + 344 are the printed integers, < 5.7624·10⁵⁰ and < 1.15248·10⁵¹.
  - 22 × 1.2497·10²⁴ = 2.74934·10²⁵.
  - ℓ^♭_I = 60099/40000 and 4(7/2 − ℓ^♭_I) + 1 = 89901/10000 < 9, so J ≤ 8. In general the bound is < 11, so J ≤ 10.
  - L_0 ≤ 23 and 28, so L_P ≤ 43, 48, 39 and 44.
  - d_1 = max(309, 22d + 291 + L_P), and the sums 291, 305, 330, 335, 339, 344, 347 and 348.
  - k̄ = 22D_acc + 339, and k̄ + 4 + (4k̄ + 35)(k̄ + 3) = 4k̄² + 48k̄ + 109 = 4.78155893918…·10¹⁰³ < 4.78156·10¹⁰³.
    Also k̄ < 3.4574408669·10⁵¹, k̄² < 11.95389735·10¹⁰², and 48k̄ + 109 < 10⁻⁴⁹k̄².
  - (4/3)(2.74934·10²⁵)² = 1.00785·10⁵¹ > 1.0078·10⁵¹.
- **K\*.** For a ∈ (2, 3) with k1 ≥ 8: s_R = (4k1 + 35)/(7 − 2a); E(k, i) increases in i; X_4 = k1 + 1,
  X_5 > (4k1 + 9/2)/5, X_6 > (3k1 + 4)/5, X_7 > (4k1 + 7)/10 (both cases of a ≶ 5/2), X_8 > (k1 + 2)/5. The four
  polynomial inequalities follow from s_R ≥ (4k1 + 35)/3 and hold for k1 ≥ 8, so K* is the first entry. K* increases
  in a, and the two-sided bound for a ∈ (2, 3) holds.
- **Placements.** All eight old texts occur exactly once in the current chapters. Items 2 and 3 are at ch71:26–27 and
  ch03:311. Items 4 and 5 are at ch46:248 and 1603. Items 6 and 7 are at ch63:68 and 292–294. Items 8 and 9 are at
  ch90:72–73 and 130–131. The insertion anchor ("under both." then "### The first constants of the linear theory") occurs
  once.
- **Simulated merge.** I merged the section and all eight new texts in a scratch copy. `assemble.py --check` reports
  labels 4599 (baseline 4593 + 6) and problems 0. `lint.py --chapters` and `lint.py --paper` report 0 hits. The new
  section has no line over 121 characters, before or after resolution (maximum 121), and no wrapped line starts with
  "+ ", "- ", "* ", "> ", "#", "=" or "|". Labels are lowercase. The new texts read correctly in context. Apart from
  findings 4–5 and N4, they are consistent with the section: d_1, K, K* and L_P bounds agree, and the half-class bound
  L_P ≤ 48 appears where the half class is meant.
- **Crosswalk rows.** All six rows are present. They follow the existing four-field format, and their summaries match
  the section, apart from the k = 0 qualification of finding 2.
