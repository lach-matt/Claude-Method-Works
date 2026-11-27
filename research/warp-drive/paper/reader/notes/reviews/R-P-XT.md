# R-P-XT: review of proofs/P-XT.md (md5 a9e3d28426e8bd4103ac04fcd94789b2, 525 lines)

Reader: independent, adversarial, line by line. Every line of P-XT.md was read, every proof in full. I also read the
chapter-87 text the subsection rests on, in full: sec:tl5-wg (87:1947–2757), sec:tl5-cip (87:1159–1946), the seed
(87:496–582) and the data cone (87:83–203, 433–494). Chapter 87 at HEAD is byte-identical to the writer's base edafc288
(md5 eeaa48e1…; `git diff edafc288 HEAD` does not touch it), so the placement line numbers hold. No repository file was
edited.

## Summary

The mathematics holds. Every lemma, the theorem, the definition and lemma of ĝ_♮, the corollary and the proposition are
correct as stated, and every number printed in the chapter text is a valid bound. One printed intermediate chain in
lem:tl5-xt-rx is wrong (m1). The main problem is scope: three sentences of chapter text, the subsection's opening and
the two one-sentence edits, say that (X) and (T) "hold at the first stage" and that for any other background they "are"
explicit inequalities. What is proved is narrower: cor:tl5-xt-data needs u* < −1, and thm:tl5-xt needs the seed's
1-jet on N₀⁺ and gives only sufficient conditions (M1). The remark also asserts things that are not proved (m2). Two
small gaps in proofs (m3, m4) and eight nits complete the list.

Findings: 1 Major, 4 minor, 8 nits on the chapter text, and 4 notes on material that is not chapter text.

## Checks run

- Scratch merge on `git archive HEAD` (…/scratchpad/rpxt/tree). The subsection was inserted after 87:2757 with one blank
  line before and one after. Items 2 and 3 were applied: each old text occurs exactly once as whole lines (at 2151 and
  2500; 2502 after item 2). The 21 rows went into crosswalk/87-ten-l5.tsv after cor:tl5-wg-data-first-stage, with
  PENDING set to a commit id. Results: `lint.py --chapters`: 62 files, 4977 labels, 0 hits. `assemble.py --check`:
  labels 4977, problems 0. The assembled one-liner prints `[] 0`. After labels resolve the longest line in the
  subsection is 121 characters; source lines are ≤ 121; no wrapped line starts with a marker; there is no backtick and
  no stray bold. The 21 crosswalk rows have four columns each, are in chapter order, and each @PENDING:N is the line of
  its label in P-XT.md (all 21 checked).
- With every replacement text below applied (…/scratchpad/rpxt/fix/apply.py → P-XT.reviewed.md, diff
  P-XT.review.diff), the same three checks give 0 hits, problems 0 and `[] 0`, with the longest assembled line at 121.
  The crosswalk N values move with these edits and need recomputing.
- Arithmetic: independent outward-rounded ball arithmetic (python-flint arb, 200 bits; …/scratchpad/rpxt/num/check*.py,
  written without the writer's scripts). The fields were taken from their chapter definitions: eq:cone-v,
  eq:cone-data, lem:cone-w (W̄), prop:cone-exact and the seed formulas of lem:tl5-seed. Each printed inequality was
  checked as printed, including every printed intermediate value, and also through the unrounded chain. Results:

| claim | value (enclosure) | verdict |
|---|---|---|
| v(10.24756039) < 1/2 < v(10.24756040); v(11.73508635) < 7/2 < v(11.73508636) | 0.4999999997, 0.50000002; 3.49999998, 3.500000002 | holds |
| f(r_s) ≥ 0.9904773, f(r_e) ≤ 0.992739 | 0.99047732, 0.99273848 | holds |
| e₋² ≥ 0.500241, e₊² ≤ 0.501384, e₋ ≥ 0.707277, e₊/e₋ ≤ 1.001142 | 0.50024107, 0.50138307, 0.70727722, 1.00114080 | holds |
| ∂_vW ≤ 1/(2r_s³) ≤ 4.6464·10⁻⁴ | 4.646314·10⁻⁴ | holds |
| (3/2)∂_vR/R ≤ 3f(r_e)/(4r_s) ≤ 0.072657 | 0.07265669 | holds |
| 2ℓ² ≤ 1.1064, 2ℓ ≤ 1.4876, r_e ≤ 11.7351 | 1.1063668, 1.4875260, 11.7350864 | holds |
| X̄ ≤ 0.025895 / 0.011112 | 0.0258946 / 0.0111116 | holds |
| X̄′ ≤ 0.034817 / 0.014940 | 0.0348164 / 0.01493998 | holds |
| printed step "0.0111011/0.999054" (seed 2) | numerator 9.4598e-4 × 11.7351 = 0.01110117 > 0.0111011 | **printed step fails** (m1) |
| printed step "1.27190·10⁻³ × 11.74622 ≤ 0.014940" (seed 2) | 0.014940017 | **printed step fails** (m1) |
| r_s^(−3/2), √2 + 2(2/3)^(3/2), 1/(2√10) | 0.03048381, 2.5028757, 0.15811388 | holds |
| φ̄, 𝔭̄, Θ̄, X̄′/r_s, X̄/r_s², X̄/r_s, Θ̄(…), 𝔣̄, e^(2φ̄/3), ζ̄ (both seeds) | each as printed | holds |
| \|ζ\|_γ ≤ 0.03106 / 0.01924 (unrounded chain: 0.0310529 / 0.0192347) | | holds |
| √2((∂_vW)² + e^(2W)\|ζ\|²)^(1/2) ≤ 0.03111 / 0.01928 | 0.0311099 / 0.0192778 | holds |
| K₁ ≤ 0.1038 / 0.09194 (unrounded chain: 0.1037595 / 0.0919291) | | holds |
| e^(0.3114) ≤ 1.3654, e^(0.27582) ≤ 1.3177; c_R ≤ 1.2006 / 1.1587 | 1.20054 / 1.15860 | holds |
| ε_R ≤ 0.8329 κ_m / 0.8630 κ_m at v* = 7/2 | exact thresholds 1/c_R = 0.832997 / 0.863169 | holds |
| 4.996 (√2(8/7)^(1/2) ≤ 1.511858, √5 + 1/4 ≤ 2.486068) | 4.995813 (unrounded 4.995802) | holds |
| 20.9 (e^0.33 ≤ 1.39097) | 20.8479 | holds |
| 0.495 = f(10)/2; 0.495^(3/2) ≥ 0.3482 (placement remark only) | 0.348263 | holds |
| √2 min Ω̂ ≥ 1.0002 for ĝ_♮ (report only) | 1.000241: min of e^(2W_s) on N⁺ is at S, since ∂_v ln e^(2W_s) = R_s⁻³ and ∂_uR_s < 0 | holds |
| Y₁ ≤ 3e₊ε_R/(√2 r_s) (formula in the text) | 3e₊/(√2 r_s) = 0.1465786 | the formula holds; the report's "= 0.14657 ε_R" is not an upper bound (note N1) |
| prop:tl5-xt-seed, seed 1 at (9/4, 1): v(11.1148) < 9/4 < v(11.1149), r^(−3/2) ≥ 0.0269861, env = (7 + 4√3)/16 ≥ 0.870512, cos(9/4) ≤ −0.628173, −2P ≥ 0.01967 | 0.02698620, 0.8705127, −0.6281736, 0.0196758 (e^(−2P) − 1 ≥ 0.019871) | holds |
| prop:tl5-xt-seed, seed 2 at (2, 1): r ∈ (10.9909, 10.9910), cos(2√10) ≥ 0.999144, φ ≥ 0.0043392, P ≥ 0.00578, e^(−0.01156) ≤ 0.988507, r − R ≤ 0.0025970, r/R ≤ 1.000246, r²/R² ≤ 1.000493, final ≤ −0.01100 | 0.9991444, 0.00433925, 0.00578065, 0.9885066, 0.00259696, 1.0002454, 1.0004921, −0.0110057 | holds |

- Mathematics, each claim redone by hand:
  - lem:tl5-xt-implies holds for every background. It uses k̂(ê₃, ê₃) = k̂(ê₄, ê₄) = 2Ω̂²,
    g_N(ê₃, ê₄) = −2e^(2W), lem:tl5-wg-norms (b) and |e₃| ≥ |du(e₃)|/|du| = √2 Ω̂.
  - lem:tl5-xt-seed-jets (a) holds: lem:tl5-cip-jets (a) with m = 3; the field on N is C³ in v; the seed is the data
    on {u = −10, v ≤ 1/2}.
  - lem:tl5-xt-seed-jets (b) holds, checked as asked. With the derivatives of order ≤ 3 in v equal on N₀⁺, step (i) of
    the proof of lem:tl5-cip-jets at k = 4 gives a homogeneous system for δ∂_v⁴b. Its value on S is 0, since b is C⁴
    on N and 0 for v ≤ 1/2. The fifth line of eq:tl5-cip-ricci contains no ∂_v⁴W after ∂_v³ is applied, because W
    enters only through e^(−2W), ∇̸∇̸W, ∂W and ζ. So step (ii) gives a closed homogeneous system for δ∂_v⁴γ alone along
    the curves u ↦ (u, 1/2, y), on which x is constant. A solution that is nonzero at its point on S is nowhere zero.
    At S, R − r vanishes to order 7, P to order 3 and env⁽⁴⁾(1/2) = 4!(π/3)⁴. This gives
    δ∂_v⁴γ_(φ1φ1) = r_s²(1 + x)∂_v⁴P = (4λπ⁴/81) r_s^(1/2) (1 + x) h (2(1 + x)c₀ − (1 − x)s₀); I recomputed it from
    eq:cone-data. The linear factor has at most one root in (−1, 1). Off that torus, and for −1 < x < 1, the
    development's fourth v-jet differs from the seed's. So ĝ_♮, which carries only the seed's 3-jet, gives G^♯ − ĝ_♮
    to order 2 and no more by lem:tl5-xt-order. It cannot meet a hypothesis of agreement to order N + 1 ≥ 7 on N₀
    through that lemma, as the writer reports.
  - lem:tl5-xt-order (a)–(d) hold: C = (1/2)g′⁻¹(D̂h′ + D̂h′ − D̂h′); jets of Ψ by the step-(i) transport;
    τ(id) = −Υ(g′); Φ = Ψ⁻¹ has the identity's m-jet; (Φ*g′) has the identity's (m − 1)-jet relative to g′.
  - lem:tl5-xt-gauge holds.
    - (a): w = ∂_vŴ e₁ + Ω̂ â^A∂_A and |∇̂_(∂_v)k̂|² = 8|w|².
    - (b): Υ(g)^μ = −|g|^(−1/2)∂_α(|g|^(1/2)g^(αμ)) − g^(αβ)Γ̂^μ_αβ, |g|^(1/2)g^(uμ) = −(det γ)^(1/2)δ^μ_v,
      (det γ)^(1/2) = R³/4. This gives Υ^v = (3e^(−2W)/(2R))∂_u(R′ − R̂) and e^(2W)|Υ| = (3e^W/(√2R))|∂_u(R′ − R̂)|.
    - (c): Frobenius and operator norms, and Minkowski over λ, give |ν| ≤ (3/2)|G||D̂h′|.
  - lem:tl5-xt-rho holds.
    - (a): the trace of the fifth line, including the cancellation of the ∂b terms of e₃γ and ℒ₃χ, and
      trχ̲ = 3∂_uR/R + div_γ b (the b^A∂_A ln det γ₀ term is absorbed by div_γ b); the identity
      (6/R³)∂_v(R²∂_uR) = 6∂_u∂_vR/R + 12∂_uR∂_vR/R².
    - (b): the formula for R̸ in ϰ₁, ϰ₂, ϰ₃ was checked on the round S³ (it gives 6/R²); ∂_uR′ = −f(r_s)/f(10) at S.
  - lem:tl5-xt-rx holds: the rewriting of w with p, q; p′² + q′² = 4/(1 + x²)²; |∂_xw| ≤ (8/9)(A² + B²) ≤ W̄
    (lem:cone-w); and the two integral bounds.
  - lem:tl5-xt-k1 holds: the specialisation of 𝔣 on N₁ (the 1/(2(1 ± x)) terms give (∂_vm − ∂_vn)/2), every bound
    of its proof, and ∂_v(R³ζ_x) = R³𝔣.
  - thm:tl5-xt (a)–(c), def/lem:tl5-xt-natural, cor:tl5-xt-data and prop:tl5-xt-seed hold. In the lemma I checked:
    - the seed is defined on 𝒪̂;
    - positivity of γ̂;
    - D, b_N and λ vanish to order 3 at v = 1/2. For λ this comes from ∂_v(r²ρ_s) = 𝒢_s, from 𝒢 − 𝒢_s vanishing to
      order 2 (𝒢 has at most one derivative in v), and from the decomposition of λ;
    - tr_(γ_N)∂_uγ̂ = 6ρ/R, hence ∂_uR̂ = ρ.
- Citations to the merged chapter-87 results say what they use. thm:tl5-wg-data supplies the definitions of δ, g′, Ψ,
  ξ, ξ′, Y, K, ξ₀, ξ₁, its bounds |ξ| ≤ ξ₀ and |ξ′| ≤ ξ₁, its inverse-metric formula and its conclusion. Its gluing
  clause (g′ = development on 𝒩_δ ∩ 𝒰) is used explicitly in the second paragraph. cor:tl5-wg-data-first-stage is used
  for g_N. sec:tl5-dn is not cited in the text. The exceptions are nits n2 and n8.

## Major

**M1. Scope: "(X) and (T) hold at the first stage" without u* < −1, and "for any other background they are explicit
inequalities".** Places: P-XT 3–5 (the subsection's opening), placement item 2 (new text at 87:2151–2153) and item 3
(new text at 87:2500).

Why. The standing hypotheses (P-XT 12) and cor:tl5-wg-data-first-stage allow every u* < u⁺ < u₀ with
−0.7698 < u₀ < −0.7697. But ĝ_♮ needs u′ ∈ (u*, −1) (def:tl5-xt-natural), so cor:tl5-xt-data is proved for
u* ∈ (−10, −1) only. The restriction is real: for u* ∈ (−1, u₀) the seed is defined at (u, v) only for
v < 2u + ln((1 − u)/(1 + u)), which is about 1.14 at u = −0.9, so the seed does not cover D̄ when v* = 7/2. In
addition, thm:tl5-xt applies only to backgrounds with the seed's values and first derivatives on N₀⁺, and it gives
sufficient conditions ("hold … if"), not equivalent ones. So "states them for every other background as explicit
inequalities", "for any other background they are explicit inequalities" and "shows that they hold at the first stage"
say more than is proved. The mathematics is unaffected; I grade this Major because the chapter text asserts a result
that is not proved.

Replacement (checked in the scratch merge).

P-XT 3–5. Old:

    This subsection shows that the conditions (X) and (T) of [[thm:tl5-wg-data]] hold at the first stage of the problem at
    10 l5 for an explicit background built from the seed and the data ([[cor:tl5-xt-data]]), and states them for every other
    background as explicit inequalities on its departure from the data along N₁ ([[thm:tl5-xt]]). Three facts make this

New:

    This subsection shows that the conditions (X) and (T) of [[thm:tl5-wg-data]] hold at the first stage of the problem at
    10 l5 when u* < −1, for an explicit background built from the seed and the data ([[cor:tl5-xt-data]]), and that for
    every other background with the seed's values and first derivatives on N₀⁺ they follow from explicit inequalities on
    its departure from the data along N₁ ([[thm:tl5-xt]]). Three facts make this

Placement item 2. Replace the last two lines of its "New:" block,

    stage they hold for an explicit background built from the seed and the data ([[cor:tl5-xt-data]]), and for any other
    background they are explicit inequalities on its departure from the data along N₁ ([[thm:tl5-xt]]). By

with

    stage with u* < −1 they hold for an explicit background built from the seed and the data ([[cor:tl5-xt-data]]), and
    for a background with the seed's values and first derivatives on N₀⁺ they follow from explicit inequalities on its
    departure from the data along N₁ ([[thm:tl5-xt]]). By

(the three old lines 2151–2153 then become six).

Placement item 3. Replace the second line of its "New:" block, "they hold at the first stage.", with

    they hold at the first stage when u* < −1, for an explicit background.

## minor

**m1. lem:tl5-xt-rx, seed 2: two printed intermediate values do not dominate (P-XT 236–237).** The numerator is
9.4598·10⁻⁴ × 11.7351 = 0.011101170 > 0.0111011. And 1.27190·10⁻³ × 11.74622 = 0.014940017 > 0.014940. The final bounds
hold: X̄ ≤ 0.0111116 ≤ 0.011112, and X̄′ ≤ 1.4876 × 8.55·10⁻⁴ × 11.746212 = 0.01493998 ≤ 0.014940. But a chain of
outward rounding must hold at every printed step. In the same lines, the citation of 2ℓ² ≤ 1.1064 and 2ℓ ≤ 1.4876 is
moved to the proof of cor:cone-compare, where they appear (nit n4, folded in here). Old (P-XT 234–237):

    most 2ℓ W̄ (r_e + X̄). With 2ℓ² ≤ 1.1064, 2ℓ ≤ 1.4876 and r_e ≤ 11.7351 ([[cor:cone-compare]], [[eq:cone-v]]), at the
    first seed 2ℓ² W̄ ≤ 2.20174 × 10⁻³, X̄ ≤ 0.0258377/0.997798 ≤ 0.025895 and X̄′ ≤ 2.96033 × 10⁻³ × 11.76100 ≤
    0.034817; at the second 2ℓ² W̄ ≤ 9.4598 × 10⁻⁴, X̄ ≤ 0.0111011/0.999054 ≤ 0.011112 and X̄′ ≤ 1.27190 × 10⁻³ × 11.74622
    ≤ 0.014940. ∎

New:

    most 2ℓ W̄ (r_e + X̄). With 2ℓ² ≤ 1.1064, 2ℓ ≤ 1.4876 (the proof of [[cor:cone-compare]]) and r_e ≤ 11.7351
    ([[eq:cone-v]]), at the first seed 2ℓ² W̄ ≤ 2.20174 × 10⁻³, X̄ ≤ 0.0258377/0.997798 ≤ 0.025895 and X̄′ ≤ 2.96033 ×
    10⁻³ × 11.76100 ≤ 0.034817; at the second 2ℓ² W̄ ≤ 9.4598 × 10⁻⁴, X̄ ≤ 0.0111012/0.999054 ≤ 0.011112 and
    X̄′ ≤ 1.271898 × 10⁻³ × 11.746212 ≤ 0.014940. ∎

(0.0111012/0.999054 = 0.0111117 ≤ 0.011112. 1.271898·10⁻³ = 1.4876 × 8.55·10⁻⁴ exactly, and
11.746212 = 11.7351 + 0.011112.)

**m2. rem:tl5-xt-background asserts what is not proved and drops conditions (P-XT 420–429).**
- (i) "so its Ricci tensor there is not small": nothing bounds the Ricci tensor of ĝ_♮ in the strip from below.
- (ii) "needs a small Ricci tensor on all of D̄, and so carries the incoming wave on all of D̄" is a claim about an
  estimate that is not in the merged text, and "and so carries" is not shown.
- (iii) "does not satisfy (T) for κ_m below 0.019 and 0.011" omits v* ≥ 9/4 and v* ≥ 2 from prop:tl5-xt-seed.
- (iv) "(X) and (T) reduce to …" reads as an equivalence; thm:tl5-xt gives sufficient conditions.
- (v) "[[lem:tl5-xt-order]] asks … must then be those of the development" reads as a necessity. The lemma gives one
  sufficient route; G^♯ = (Ψ⁻¹)*g′ has k-jets that also involve ∂_v^(k+1)Ψ, so the necessity is not shown.

Old: lines 422–429, from "seed outside the strip" to "4 are not the seed's.". New (the first two lines of the remark
are kept):

    seed outside the strip |u + 10| < η₁, and across the strip it passes from the data to the seed; nothing here bounds its
    Ricci tensor there. A background for an a priori estimate is to have a small Ricci tensor on all of D̄; by
    [[prop:tl5-xt-seed]] the seed itself does not satisfy (T) for κ_m ≤ 0.01967 at the first seed when v* ≥ 9/4, nor for
    κ_m ≤ 0.01100 at the second when v* ≥ 2. For a background whose values and first derivatives on N₀⁺ are the seed's,
    (X) and (T) follow from [[eq:tl5-xt-condition]] or [[eq:tl5-xt-condition-general]], conditions on N₁ alone. For
    G^♯ − ĝ to vanish with its partial derivatives of order at most k on N₀⁺ by [[lem:tl5-xt-order]], ĝ − g′ is to vanish to
    order k + 1 there; for k ≥ 3, by [[lem:tl5-xt-seed-jets]] (b), this asks that the derivatives in v of ĝ of the orders 4
    to k + 1 at the points of N₀⁺ be those of the development, which at order 4 are not the seed's.

**m3. lem:tl5-xt-gauge (a): the formula for K₁ drops the absolute value without saying why (P-XT 126, 147–148).** K₁ of
thm:tl5-wg-data contains (1/2)|trχ|, and the lemma writes (3/2)∂_vR/R. These are equal only because ∂_vR > 0 on N₁,
and the proof does not say so. Old (P-XT 148):

    trχ = 3∂_vR/R, χ being that of g′, whose leaf metric on N₁ is the data's ([[lem:tl5-leaf-expansion]]).

New:

    trχ = 3∂_vR/R, χ being that of g′, whose leaf metric on N₁ is the data's ([[lem:tl5-leaf-expansion]]); and ∂_vR =
    (f/2) ∂_rR > 0 on N₁ by [[prop:cone-exact]] (a), so (1/2) |trχ| = (3/2) ∂_vR/R.

**m4. lem:tl5-seed (d) is cited for v ≥ 1/2, but it states the values only for 0 ≤ v ≤ 1/2 (P-XT 372, 381–382).**
R_s(−10, v) = r and W_s(−10, v) = W are used on all of N₁. They follow from the proof of (d), where at u = −10 the
seed equation reads v = v(R) for every v and (b) gives e^(2W) = f(R)/(2f(10)). They do not follow from its statement.
Old (P-XT 372–373):

    being 𝒢 computed from the seed's fields, since R_s(−10, v) = r ([[lem:tl5-seed]] (d)); and 𝒢 contains derivatives of W, b
    and γ with at most one derivative in v, so 𝒢 − 𝒢_s vanishes to order 2 at v = 1/2. As r_s² ρ_s(1/2) = −r_s² f(r_s)/f(10),

New:

    being 𝒢 computed from the seed's fields, since R_s(−10, v) = r (the proof of [[lem:tl5-seed]] (d)); and 𝒢 contains
    derivatives of W, b and γ with at most one derivative in v, so 𝒢 − 𝒢_s vanishes to order 2 at v = 1/2. As
    r_s² ρ_s(1/2) = −r_s² f(r_s)/f(10),

and at P-XT 382, "([[lem:tl5-seed]] (d)); and ∂_uγ̂ = ∂_uγ_s + λγ_N." becomes "(the proof of [[lem:tl5-seed]] (d)); and
∂_uγ̂ = ∂_uγ_s + λγ_N." (the line is then 114 characters).

## nits

**n1. thm:tl5-xt (b), proof, case ε_R = 0 (P-XT 318).** The statement claims G^♯ = g_N at every point of N⁺, but the
proof shows it on N₁ only; on N₀⁺ it comes from (a). Old: "ξ₁ = 0, and the formula of [[thm:tl5-wg-data]] gives
G^♯⁻¹ = g_N⁻¹ on N₁." New: "ξ₁ = 0, and the formula of [[thm:tl5-wg-data]] gives G^♯⁻¹ = g_N⁻¹ on N₁; on N₀⁺, G^♯ = g_N
by (a)."

**n2. cor:tl5-xt-data, proof (P-XT 394).** "[[thm:tl5-wg]] applies" also needs g_N to be smooth data in the gauge on N⁺
satisfying the constraints. Old: "[[lem:tl5-xt-order]] (c) with m = 3 gives the order 2. ∎" New:

    [[lem:tl5-xt-order]] (c) with m = 3 gives the order 2. As g_N is smooth data in the gauge on N⁺ satisfying the
    constraints ([[cor:tl5-wg-data-first-stage]]) and ĝ_♮ is a background, [[thm:tl5-wg]] applies. ∎

**n3. Opening paragraph (P-XT 9).** "a multiple of ∂_v whose size is the difference of the transverse derivatives of R"
is imprecise: the coefficient is 3e^(−2W)/(2R) times that difference. Old line 9: "gauge vector of the development is a
multiple of ∂_v whose size is the difference of the transverse derivatives of R". New: "gauge vector of the development
is ∂_v times 3e^(−2W)/(2R) times the difference of the transverse derivatives of R".

**n4.** Folded into m1: 2ℓ² ≤ 1.1064 and 2ℓ ≤ 1.4876 are in the proof of cor:cone-compare, not in its statement.

**n5. lem:tl5-xt-k1 (P-XT 271).** |P + Q| ≤ 2φ/3 needs the Cauchy–Schwarz inequality with h; the crude bound gives
2√2φ/3. Old: "G_x = R² e^(−2(P+Q))/(4(1 − x²)) and |P + Q| = |(1 + x) m + (1 − x) n|/3 ≤ 2φ/3,". New:

    G_x = R² e^(−2(P+Q))/(4(1 − x²)) and |P + Q| = |(1 + x) m + (1 − x) n|/3 ≤ 2φ/3, by the Cauchy–Schwarz inequality
    and h ((1 + x)² + (1 − x)²)^(1/2) = 2,

**n6. thm:tl5-xt (c) (P-XT 300–301).** "for instance the value of the formula of [[lem:tl5-xt-gauge]] (a)" names K₁
itself. New:

    (c) In general, let ε₀ and ε₁ be as in [[lem:tl5-xt-gauge]] (c) and K̄₁ ≥ K₁, for instance K₁ itself, given by the
    formula of [[lem:tl5-xt-gauge]] (a). Then (X) and (T) hold, and G^♯ is data in the wave gauge for g_N, if

**n7. Paragraph after thm:tl5-xt (P-XT 327–328).** "the admissible departure": the conditions are sufficient, so the
departure is the one they admit. New:

    departure of ĝ from the data along N₁ that they admit, and nothing else. Neither condition involves N₀⁺, beyond the
    agreement of ĝ with the seed to first order there.

**n8. Standing notation (P-XT 13–14) omits K₀.** The proof of lem:tl5-xt-order (a) uses K₀ (P-XT 98). Old (P-XT 98):
"of Υ(g′) = g′^(αβ) C_αβ. Then Y₀ = 0, and ξ₀ = Y₀ (u⁺ + 10) e^(K₀(u⁺ + 10)) = 0." New: "of Υ(g′) = g′^(αβ) C_αβ. Then
Y₀ = 0, and ξ₀ = Y₀ (u⁺ + 10) e^(K₀(u⁺ + 10)) = 0, K₀ being that of [[thm:tl5-wg-data]]." (118 characters). This one
is not in apply.py; it was checked for length only.

## Notes on material that is not chapter text (for the coordinator)

- **N1.** Report, item thm:tl5-xt (b): "(= 0.14657 ε_R)". 3e₊/(√2 r_s) = 0.1465786…, so 0.14657 is a truncation, not an
  upper bound; 0.14658 would be one. The chapter text uses only the formula, which is right.
- **N2.** Placement item 6 (i): "for a background of the form 'seed plus (v − 1/2)⁴ times a smooth field' ĝ − g′
  vanishes to order 3 and not to order 4" is false as stated. The fourth v-derivative of such a background is the
  seed's plus 4! times the field's value at v = 1/2, which can be chosen to match the development's. It should read
  "(v − 1/2)⁵", or "a field vanishing to order 4 at v = 1/2".
- **N3.** Placement item 5 lists [[lem:tl5-cip-form]] (b); the subsection cites only (a). Also the item headers say
  "HEAD edafc288". Chapter 87 at the present HEAD is identical, so this is harmless.
- **N4.** Crosswalk notes, which are not published:
  - cor:tl5-xt-data, "unconditional … every kappa", omits u* ∈ (−10, −1); suggested: "…, every u* < −1, …".
  - thm:tl5-xt has "eps_R < 0.8329 kappa_m" where the theorem has ≤.
  - After the fixes, the @PENDING:N line numbers must be recomputed.

Verdict: NOT CONFIRMED

## Confirmation (P-XT.md md5 5fa426c0e7a53e4f7787090732711b2f, 535 lines; HEAD 22033457)

**Diff against my patch output** (P-XT.reviewed.md, c5cf16af). M1, m1–m4 and n1–n7 are in the new file verbatim. The
other differences are these.

- **Opening paragraph (P-XT 3–11), rewrapped.** The word sequence is identical (compared token by token), and every
  line is ≤ 121.
- **n8 (P-XT 99).** "…= 0, K₀ being that of [[thm:tl5-wg-data]]." is as I proposed; the line is 118 characters.
- **Placement header.** It now reads "HEAD 6bf3f7d7; lines 1–2760 are those of edafc288". This is correct. Chapter 87 at
  HEAD (md5 3d01b3e2…, 4170 lines) differs from edafc288 only from line 3049 on: the rewrite of sec:tl5-beyond and the
  merge of sec:tl5-hf. The anchors 87:2151–2153, 2500 and 2757–2759 are unchanged, and I checked them by eye.
- **Placement 5.** It now cites [[lem:tl5-cip-form]] (a) only. Correct.
- **Placement 6 (i), restated.** Checked against lem:tl5-xt-seed-jets (a) and (b); it is correct.
  - A background with the seed's derivatives of order ≤ 4 on N₀⁺, such as seed + (v − 1/2)⁵G, has ĝ − g′ vanishing
    to order 3, by (a). It does not vanish to order 4, because the development's fourth v-derivatives of the leaf
    metric differ from the seed's off at most one torus, by (b). lem:tl5-xt-order then gives G^♯ − ĝ to order 2.
  - For seed + (v − 1/2)⁴G, every partial derivative of order ≤ 4 at v = 1/2 other than ∂_v⁴ is the seed's. The
    derivatives with at most three in v already agree with g′'s by (a). The derivative ∂_v⁴ is the seed's plus 4! G(·, 1/2, ·).
    So "order 4 exactly when G(·, 1/2) is the difference of the fourth derivatives divided by 4!" is right.
  - "Sufficient route; necessity not shown" is right.
  - "With the seed's coefficients" is right for the coefficients of the top jet in the transport equations. The lower
    development jets enter only the inhomogeneous terms. This is not chapter text, and it is fine as it stands.
- **Placement 6 (ii).** It is now stated as sufficiency, with the seed's 1-jet and v* = 7/2. Correct.
- **Report.** The fix-round section has Y₁ ≤ 0.14658 ε_R, which is a valid upper bound (0.1465786). The first section
  of the report still shows the old "= 0.14657"; that is history and harmless.
- **Crosswalk rows.** The notes now carry u* < −1, "≤" and "(sufficient)". All 21 pins match the label lines of the new
  file (checked mechanically), the rows are in chapter order, and each has four columns.

**Scratch merge at HEAD 22033457** (git archive; chapter 87 includes sec:tl5-hf).
- The subsection was inserted after 87:2757 and before the sec:tl5-dn heading at 2759.
- Item 2 applied at 2151, where the old three lines occur exactly once as whole lines; they become six.
- Item 3 applied at 2500, shifted to 2503 by item 2.
- The 21 rows were inserted after cor:tl5-wg-data-first-stage in crosswalk/87-ten-l5.tsv.
- Results: `lint.py --chapters`: 62 files, 5063 labels, 0 hits. `assemble.py --check`: labels 5063, problems 0. The
  assembled one-liner prints `[] 0`. The longest assembled line in the subsection is 121; the edited lines are 111, 114
  and 70. No wrapped line starts with a marker.

**Interaction with the newly merged sec:tl5-hf** (not a finding).
- Placement 4's "no other text changes" still holds. The two new sentences that mention the wave-gauge data stay true
  with sec:tl5-xt merged: 87:3084–3086 ("…gives data in the wave gauge for them under two explicit conditions on the
  background along N⁺") and 87:4160–4161 ("The hypotheses (X) and (T) … are conditions on the background of the same
  kind").
- Merged thm:tl5-hf (a) is now the N₀ data term η₀ < 𝔰₁, not "G^♯ − ĝ to order N + 1". Placement 6 (i)'s reference to
  such a hypothesis is therefore a remark for writers only, and it is consistent with the chapter: it names the data
  term as the alternative.
- Optionally, rem:tl5-xt-background could now name [[thm:tl5-wg]]'s companion [[thm:tl5-hf]] as "the a priori estimate";
  this is not required.

Nothing remains open.

Verdict: CONFIRMED
