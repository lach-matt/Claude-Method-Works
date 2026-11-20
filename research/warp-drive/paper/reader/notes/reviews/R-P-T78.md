# R-P-T78: independent reading of proofs/P-T78.md

File read: `research/warp-drive/paper/reader/proofs/P-T78.md`, md5 b2bff29e39613e28fc605a894c37c63b, 609 lines (608
newlines). Chapters as they stand now, with P-LB already merged into chapter 71 (its section sec:ec-lb-proved at line
1544, its rem:ec-point-outside at lines 49–68, its text 6 in rem:ec-not-evaluated, its text 10 in sec:scope-constants,
and its crosswalk notes).

**Verdict: NOT CONFIRMED: 0 Major, 4 minor, 5 nits.** The mathematics is correct. I re-derived it line by line and
checked it with computer algebra. The findings are about one overview sentence, one pointer, and the placement against
P-LB, which has since been merged.

## Findings

### 1. minor: the overview points to a lemma that will not be in this section (lines 11–13)

Current text:

    Λ_tf. [[lem:tf-lin-reduction]] at the end of the section reduces the kernel of the transition face operator of the
    linearised gauge-fixed operator L_b of [[ch:s15]] to that of □̄^Υ, which gives [[prop:iii-f1-3-3]] on the same set of
    gauge parameters.

What is wrong: Placement item 1 (lines 261–262) says the heading "The linearised gauge-fixed operator at the transition
face" is not inserted, and item 4 puts lem:tf-lin-reduction into ch:s15 before prop:iii-f1-3-3. So after the merge,
"at the end of the section" points at nothing. Also, prop:iii-f1-3-3 needs e_Υ > 0 (z > 0), so its parameter set is
not quite "the same set": e_Υ = 0 is in the set of this section but not in that of prop:iii-f1-3-3.

Replacement (three lines; the line before ends "the factor", unchanged):

    Λ_tf. In [[ch:s15]], [[lem:tf-lin-reduction]] reduces the kernel of the transition face operator of the linearised
    gauge-fixed operator L_b to that of □̄^Υ, which gives [[prop:iii-f1-3-3]] on the same set of gauge parameters with
    e_Υ > 0.

### 2. minor: the overview claims more than the proposition proves (lines 3–5)

Current text:

    This section proves part (a) of [[lem:iii-d-7-1]]: for every gauge parameter with 0 ≤ e_Υ ≤ ½ and 0 < γ_Υ ≤ ¼, and
    more generally wherever the number Λ_tf(γ_Υ, e_Υ) of [[eq:tf-lambda]] is less than 1, the family σ ↦ (□^Υ_b)^(σ) is
    tf-admissible with every weight in its indicial gap. At (γ_Υ, e_Υ) = (1/100, 1/100), Λ_tf < 1.0111·10⁻⁴. The proof is

What is wrong: "wherever Λ_tf < 1" drops three of the hypotheses of prop:tf-gauge-explicit: γ_Υ > 0, 0 ≤ e_Υ < 1 and
z ≤ ½. Two counterexamples to the sentence as written:

- Λ_tf is even in γ_Υ, so Λ_tf(−1/100, 1/100) = 250248044601/2475062500000000 < 1. But γ_Υ < 0 is exactly the case
  the proof does not cover (rem:tf-sign).
- At (γ_Υ, e_Υ) = (15, 1/1000), Λ_tf ≈ 0.812 < 1, while z = 0.9 > ½. That point is outside lem:iii-d-4-1, so the
  indicial gap is not even described there.

Replacement (four lines; the next line, "not a perturbation from γ_Υ = 0. …", is unchanged):

    This section proves part (a) of [[lem:iii-d-7-1]]: for every gauge parameter with 0 ≤ e_Υ ≤ ½ and 0 < γ_Υ ≤ ¼, and
    more generally wherever γ_Υ > 0, 0 ≤ e_Υ < 1, 4e_Υγ_Υ² ≤ ½ and the number Λ_tf(γ_Υ, e_Υ) of [[eq:tf-lambda]] is less
    than 1, the family σ ↦ (□^Υ_b)^(σ) is tf-admissible with every weight in its indicial gap. At
    (γ_Υ, e_Υ) = (1/100, 1/100), Λ_tf < 1.0111·10⁻⁴. The proof is

### 3. minor: placement item 8 (rem:ec-point-outside, lines 494–520) cannot be applied; a combined text is given

What is wrong: item 8's old text (lines 496–504) occurs 0 times in chapter 71. P-LB's text 3 has replaced it: the
remark is now lines 49–68 of `chapters/71-explicit-constants.md`.

Can the two texts be combined? Yes. They agree in substance, and each adds something the other lacks:

- P-LB adds: the point lies outside through h; γ_(Υ,H) is not fixed and no number depends on it; the closing sentence
  on the lower bound at every point of the proved set.
- P-T78 adds: tf-admissibility holds at the point; the gauge half is undecided only through ε_1; 𝖹_exc is a separate
  condition.

One sentence of P-LB's text becomes false after P-T78 and must go. It is "the parameters γ_Υ and e_Υ are required in
[[thm:vi-c-2-1]] to lie below thresholds whose existence is proved and whose values are not determined, and (γ_Υ, e_Υ)
= (1/100, 1/100) is not shown to lie below them". The tf conditions are now explicit and hold at the point.

Proposed item 8. The old text is the whole current remark, chapter 71 lines 49–68 (P-LB's "New, the seventeen lines",
as merged). The new text has 21 lines, each at most 121 characters, also after label resolution:

    **Remark {#rem:ec-point-outside}** (The computational point and the proved set.) The computational point lies outside
    the set on which [[thm:settling]] is proved, and it lies outside through h. [[thm:settling]] takes h in the set 𝖧 of
    [[eq:iv4-0-1]], whose supremum h_* = min(10⁻⁶, h_0, h_tf) is at most 10⁻⁶ whatever the values of h_0 and h_tf, and
    𝖧 ⊂ (0, h_*); so h = 10⁻⁶ is not in 𝖧 ([[rem:s14-eps-ind-scope]]). Whether the gauge half of the point lies in the
    proved set is not decided. Of the conditions that [[thm:vi-c-2-1]] places on γ_Υ and e_Υ, the tf-admissibility of
    [[lem:iii-d-7-1]] and [[prop:iii-f1-3-3]] holds for every e_Υ ∈ (0, ½] and γ_Υ ∈ (0, ¼] and every h ∈ 𝖧
    ([[prop:tf-gauge-explicit]], [[lem:tf-lin-reduction]]; at (γ_Υ, e_Υ) = (1/100, 1/100) the factor of [[eq:tf-lambda]] is
    below 1.0111·10⁻⁴), and the caps 3/8, ½s_C and ¼ of row u4 of [[sec:vi-c-1]] hold there; the exclusion z_Υ ∉ 𝖹_exc
    of row u5 is a separate condition. The threshold ε_1 of [[prop:iii-d1-4-1]] for γ_Υ and e_Υ depends on the parameter
    γ_(Υ,H) ∈ (0, ε_0] of the horizon modification (row u2 of [[sec:vi-c-1]]); ε_0 and ε_1 are proved to exist, their
    values are not determined, and whether (γ_Υ, e_Υ) = (1/100, 1/100) lies below ε_1 for some such γ_(Υ,H) is not
    decided. [[def:ec-point]] does not fix γ_(Υ,H), and no number of this chapter depends on it: the horizon thresholds
    that enter do not involve it ([[lem:iii-d-5-1]], and [[lem:iii-f2-1-1]], where y = 0 for the 1-form
    c_(Υ,H) = −½χ dr), and the indicial roots of (□^Υ_b)^(0), which fix ℳ and ε_Υ, do not depend on the horizon
    modification ([[sec:iii-d2-1]]). So the computational point is a point at which the formulas of the proof can be
    evaluated, not one at which the hypotheses of [[thm:settling]] are shown to hold. Every number of this chapter that
    depends on the point is stated at it. For h ∈ 𝖧 the theorems use only 0 < ε_ind(h) ≤ δ_50 ([[prop:np-10-52]] (iii)),
    and the lower bound of [[thm:loss-d]] uses besides only ε_Υ < 1.46214·10⁻¹⁰, which holds at every h, ε_Υ being fixed
    by (γ_Υ, e_Υ) ([[lem:ec-gauge-gap]], [[prop:ec-rounds]]). At every point of the proved set a lower bound for d holds
    as an explicit function of z = 4e_Υγ_Υ² and h, with no threshold evaluated, through bounds for ε_Υ and ε_ind(h) that
    hold at every such point ([[lem:ec-lb-gauge]], [[lem:ec-lb-ind]], [[thm:ec-lb-proved]]).

Crosswalk: append to the existing note of rem:ec-point-outside, which already carries P-LB's note, the text "; the tf
conditions hold at the point (prop:tf-gauge-explicit, lem:tf-lin-reduction), the gauge half is undecided only through
ε_1, 𝖹_exc a separate condition (P-T78 text 8)".

I checked the facts in the combined text:

- "every h ∈ 𝖧": prop:iii-f1-3-3 needs (C1), which holds at every h ∈ (0, 10⁻⁶] (lem:iv4-1-3 (a)). Its Step 4 needs
  thm:iii-e-1-1 (4), and 𝖧 ⊂ (0, h_tf).
- The caps hold at the point: 1/100 < 3/8, 1/100 < ¼, and ½s_C > 50.

### 4. minor: missing placement item for rem:ec-lb-conditions (chapter 71, lines 1779–1780)

This remark came from P-LB and is now in chapter 71. It still names ε_L and γ_1. After items 6 and 7 of P-T78, no
chapter defines either symbol. A grep of `chapters/` for ε_L and for γ_1 used as a threshold finds:

- rows u3 and u4 and step (2) of thm:vi-c-2-1, which items 6 and 7 replace;
- this line.

The γ_1 at chapter 32, lines 1066–1102, is a different symbol: a local constant of the proof of prop:iii-d1-4-1.

Current text, chapter 71 lines 1779–1780:

    It uses none of the thresholds that define the proved set: not h < h_0, h < h_tf or h ∉ 𝖹; not γ_(Υ,H) ≤ ε_0, nor the
    bounds ε_1, ε_L and γ_1 on e_Υ and γ_Υ; not z ∉ 𝖹_exc; not (C2), (C3) or (C5), nor (C4) beyond the existence of ε_ind;

Proposed new item (8b). The first line is unchanged; the second line becomes:

    bounds of rows u3 and u4 on e_Υ and γ_Υ; not z ∉ 𝖹_exc; not (C2), (C3) or (C5), nor (C4) beyond the existence of ε_ind;

This is true. The proof of thm:ec-lb-proved uses z ∈ (0, ½] (row u5) and none of ε_1, ½, 3/8, ½s_C or ¼. Crosswalk:
append to the note of rem:ec-lb-conditions the text "; ε_L and γ_1 replaced by the bounds of rows u3–u4 (P-T78 text
8b)". Add the same entry to the list "Notes for existing rows" (lines 603–608).

### 5. nit: stale line numbers in the placement after the P-LB merge

- Item 9: the old text is at chapter 71 lines 4961–4963, not 4691–4693. It occurs exactly once. The new text is
  compatible with P-LB's text 6, which begins on the following line ("this chapter does only at a point outside …").
- Item 10: the old text is at chapter 90 lines 83–84, not 79–80. It occurs exactly once. It does not overlap P-LB's
  text 10, which is at lines 66–71.
- Item 8: see finding 3.

Replacement: in line 522, "(lines 4691–4693)" becomes "(lines 4961–4963)". In line 535, "(lines 79–80)" becomes
"(lines 83–84)".

### 6. nit: row u4's threshold entry (new text, lines 473–474)

Current text:

    [[eq:iii-i9-1-1]]). With e_Υ ≤ ½ this gives z_Υ ≤ ⅛ and Λ_tf(γ_Υ, e_Υ) ≤ 41/64 ([[eq:tf-lambda]]). Threshold: ε_1 on
    u2–u3.

What is wrong: ε_1 depends on u2 only (prop:iii-d1-4-1; row u3 says "Threshold: ε_1 on u2"), not on u3. Also, the cap
½s_C depends on c1–c2 (s_C = (1 − e_C)(1 − v_C)γ_C). The old entry "γ_1 on c1–c3" covered that dependence, and the new
entry drops it. The cap never binds (s_C > 100), but the entry records dependence.

Replacement for the second line: "u2; ½s_C on c1–c2." (the first line is unchanged).

### 7. nit: notation in the new section (line 87, and in passing elsewhere)

Line 15 renames the variable x̂ of tf° to x and sets x̂ := x/r. Line 87 then uses x̂ in the old sense:

    therefore the spectral family of □̄^Υ written in x̂ = x: reading w as a stationary 1-form on the Minkowski model,

Replacement:

    therefore the spectral family of □̄^Υ written in x: reading w as a stationary 1-form on the Minkowski model,

The following are optional, for the same reason:

- r̂ and e^(iσ̂r̂) in lines 7–8 and 190–191, where the Notation paragraph has r.
- Δ for the Euclidean Laplacian. prop:np-10-20 writes Δ_e for it, and prop:i-c-5-3 uses Δ for the Laplacian of 𝕊³.
- S̄ for both the endomorphism and the threshold in lines 126–127.
- N_1 for the given operator in prop:tf-gauge-explicit (b), but for the flat 1-form operator in lem:tf-lin-reduction.

None of these changes the mathematics.

### 8. nit: the new proof of lem:iii-d-7-1 leaves (a) at γ_Υ = 0 implicit (lines 301–303)

Current text:

    standard inner product, H_0 = Id: by [[prop:i-c-5-3]] it is tf-admissible with every weight in (0, 2).
    *(a): γ_Υ > 0.* This is [[prop:tf-gauge-explicit]] (b): for e_Υ ∈ [0, ½] and γ_Υ ∈ (0, ¼], z = 4e_Υγ_Υ² ≤ ⅛ and
    Λ_tf(γ_Υ, e_Υ) ≤ 41/64 < 1 ([[eq:tf-lambda]]). *(b): small |γ_Υ|.*

What is wrong: (a) includes γ_Υ = 0. That case is the paragraph "At γ_Υ = 0" (z = 0, gap (0, 2)), but the text does
not say so.

Replacement (three lines, at most 115 characters):

    standard inner product, H_0 = Id: by [[prop:i-c-5-3]] it is tf-admissible with every weight in (0, 2), which is (a)
    at γ_Υ = 0, where z = 0. *(a): γ_Υ > 0.* This is [[prop:tf-gauge-explicit]] (b): for e_Υ ∈ [0, ½] and γ_Υ ∈ (0, ¼],
    z = 4e_Υγ_Υ² ≤ ⅛ and Λ_tf(γ_Υ, e_Υ) ≤ 41/64 < 1 ([[eq:tf-lambda]]). *(b): small |γ_Υ|.*

If adopted, item 2's note on line 290 ("the first four lines of the proof and its last fourteen lines … are
unchanged") still holds.

### 9. nit: vestigial wording left by the removal of P̂′ (item 11)

After item 5, the operator with parameters (0, γ_Υ) is used nowhere. Two places keep wording that referred to it or
to smallness.

(a) Chapter 34 line 561 still lists it. Current text:

    (γ_C, γ_Υ) replaced by (τγ_C, τγ_Υ), τ ∈ [0, 1], or by (0, γ_Υ), which satisfy (H1)–(H2) by the proof of

Optional replacement:

    (γ_C, γ_Υ) replaced by (τγ_C, τγ_Υ), τ ∈ [0, 1], which satisfy (H1)–(H2) by the proof of

(b) Chapter 35 line 54 reads "γ_Υ is small as in [[prop:iii-f1-3-3]]", but that proposition no longer asks γ_Υ to be
small. Optional replacement: "γ_Υ is as in [[prop:iii-f1-3-3]]". Item 11 is right that both texts stay true as
written.

## What I checked and found correct

### lem:tf-gauge-modes (lines 75–103)

I re-derived it from the definitions:

- □̄^Υ = 2(δ̄ + Ē)Ḡδ̄* (sec:iii-d-2), with Ē h = −γ(2ι_(ḡ⁻¹c̄)h − (2/3)(1 − e)c̄ tr h), c̄ = r⁻¹dt̄ and ḡ⁻¹c̄ = −r⁻¹∂_t̄.
- ĒḠh = −γ(2ι_(ḡ⁻¹c̄)h − e c̄ tr h), checked symbolically.
- δ̄* is the positive symmetric gradient, which is consistent with a = −½ρDω_0 in the proof of lem:iii-d-3-1.
- □̄ = ∂_t̄² + Δ componentwise (prop:np-10-20 (i)).

In sympy I applied □̄^Υ to e^(−iσt̄)(φ dt̄ + Σ ω_i dx^i) with general functions φ, ω_i of x. The result is
e^(−iσt̄)(F_0, F_i) with eq:tf-modes exactly, all coefficients and signs included.

The identification N_tf(σ̂)w = e^(iσ̂t_*)□̄^Υ(e^(−iσ̂t_*)w) holds for these reasons:

- eq:i-c-4-1 and the exact form eq:iii-d-2-1 apply, since ρ⁻²(□̄^Υ)^(0) is dilation invariant and S_0 = S̄ by
  lem:iii-d-2-1 (3).
- e^(iσ̂t_*)e^(−iσ̂t̄) = e^(−iσ̂r).
- The convention matches prop:i-c-5-3 and prop:np-10-20: N_tf = e^(−iσ̂r)(Δ − σ̂²)e^(iσ̂r) at γ_Υ = 0.

As a cross-check, the σ̂-linear part of e^(−iσ̂r)F gives, in the frame (dt̄, dx^i):

- (S_0 w)_0 = γ((2 − e)w_0 − e x̂·w);
- (S_0 w)_i = γ(w_i − x̂_i w_0).

The spectrum of this S_0 is {2γ, γ(1 − e), γ, γ, γ}, that of S̄ in lem:iii-d-3-1.

### Decay (lines 125–137)

- (H2) defines S̄ := inf min Re spec S. For e ∈ [0, 1) and γ > 0 this is γ min(1 − e, 1) = λ > 0.
- thm:i-c-4-3 (5) gives w ∈ 𝒜^(3/2+λ−ϵ,−β′) in each setting of (1)–(2), so for every θ ∈ [0, π], including θ = 0
  and θ = π.
- The identity r∂_j = x̂_j r∂_r + Σ_k x̂_k(x_k∂_j − x_j∂_k) is right.
- The frame change between (dt_*, dx^i) and (dt̄, dx^i) is homogeneous of degree 0.
- The bounds with a = λ/2, b = ¼ and constant 2C follow, using |e^(iσ̂r)| = e^(−r sin θ) ≤ 1 and
  ∇e^(iσ̂r) = iσ̂x̂e^(iσ̂r).
- So the boundary terms of Green's formula vanish at R → ∞ for every θ, the oscillating factor at θ = 0, π included.

### lem:tf-damped-helmholtz (lines 23–73)

I checked every step in full:

- finiteness of ‖v‖_+ and ‖∇v‖_+;
- Green's formula with the outward normals;
- the four boundary bounds 2π²C²R^(−2a), 2π²C²ε^(2−2b), 2π²C²R^(−1−2a) and 2π²C²ε^(1−2b);
- the imaginary part after multiplying by σ̄: σ̄σ² = σ, giving −sin θ(P + Q) − 2cN;
- the passage to the limit by integrability of f v̄;
- ∇(v̄r⁻¹) = r⁻¹∇v̄ − r⁻²v̄x̂;
- the polar integration by parts giving ½[t∫|v(tω)|²dω] − ½E_A;
- Re(−σ²) = −cos 2θ and Re(−2iσc) = 2c sin θ;
- the Cauchy–Schwarz split (f r^(1/2))(v̄ r^(−3/2)), with E_A finite on each annulus.

Both inequalities are right as stated, with c > 0 and b < ½ used where claimed. A numerical test on three test
functions, at θ ∈ {0, 0.7, π/2, 2.5, π} and c ∈ {0.05, 1.3}, agrees.

### The chaining into Λ_tf (lines 139–155)

- ‖f_i‖_−² = 4γ²‖∂_iφ‖_+².
- |Σ_j ∂_jω_j|² ≤ 4Σ_j|∇ω_j|².
- Ω ≤ (1 + 2γ²)Φ, using c = γ.
- Φ ≤ (4e²(2 − e)⁻² + 8γ²e²)Ω, using c = γ(2 − e) > 0.
- Hence Φ ≤ Λ_tf Φ. Then Φ = 0, φ = 0 (it decays), f_i = 0, and ω_i = 0 by eq:tf-dh-zero.

### Condition (iii) (lines 157–179)

- (i) holds: weight 1 ∈ (0, 2) lies in the gap for 4eτ²γ² ≤ ½.
- P̂_0 = □̄ is tf-admissible (prop:i-c-5-3).
- Common orders for the continuous family exist (lem:iii-f1-3-2). This is a forward reference to ch:s15, and it is not
  circular.
- S̄ and γM_E are linear in γ (M_E does not involve γ).
- V is bounded H → 𝒴. Near ztf with the convention H_(b,c) ≈ ϱ^c L²(μ_b) (def:i-c-2-1, lem:i-c-2-2 (b)):
  H^s_(b,−1) → H^s_(b,−2) ⊂ H^(s−2)_(b,−3). Near sctf: a gain of one order of decay.
- 𝒳 is independent of τ, and the index is constant.
- N_0 is invertible (cor:i-c-5-2 (a)), so N_1 is injective and onto, and the annihilator is trivial by thm:i-c-4-3 (3).
- lem:iii-d-7-1 (a) cites prop:tf-gauge-explicit, which follows it. This is not circular: the proposition's (b) uses
  only the γ_Υ = 0 part and the boundedness of that proof.

### lem:tf-lin-reduction (lines 198–248)

- The gap (0, β_+), β_+ > 1, and u_0 ∈ H^∞_(b,−2β′) near ztf.
- (D Ric)^(σ̂)u_0 = 0 and (δ̄Ḡ)^(σ̂)u_0 = −ξ_0, from η_0 = 0 and the composition of spectral families. η_0 = 0 is a
  hypothesis of the lemma; in prop:iii-f1-3-3 it is proved by Steps 2–4, which are unchanged. Nothing assumes it.
- ξ_0 = ρ̂Bu_0 ∈ 𝒴 of the flat 1-form operator at q = 3/2, near ztf (H_(b,−1−2β′) ⊂ H_(b,−5/2)) and near sctf.
- The flat inverse exists by prop:i-c-5-3 and cor:i-c-5-2 (a).
- N_1 = 2(δ̄Ḡ)^(σ̂)(δ̄*)^(σ̂) (proof of lem:iii-f1-2-1).
- h_0 is in harmonic gauge, and (D Ric)^(σ̂)h_0 = 0 by D Ric ∘ δ̄* = 0.
- □̄ = 2D Ric + 2δ̄*δ̄Ḡ on Minkowski space (eq:iii-f-1-2 with R = 0).
- (δ̄*)^(σ̂) = ρ̂B_1 + σ̂B_0 with B_0 = −i dt_* ⊗_s ·.
- h_0 ∈ H_(sc,b)^(s−1,(𝗋+α_+,1/2)), that is weight 3/2 ∈ (0, 2). The kernel is independent of s, and the flat tensor
  operator is tf-admissible, so h_0 = 0.
- Finally N_tf((□^Υ_b)^(·))ω_0 = −2ξ_0 + 2ξ_0 = 0, and ω_0 is in the space at the weight ½ ∈ (0, ι^Υ_(s1,2)).
- The new prop:iii-f1-3-3 supplies everything the lemma needs: its (i) gives the common orders, Step 5 gives the
  hypotheses, and its parameter conditions satisfy those of prop:tf-gauge-explicit.
- The index argument in (iii) uses no smallness of γ_Υ.

### Numbers (exact, with fractions)

- Λ_tf(1/100, 1/100) = (5001/5000)(4/39601 + 1/12500000) = 250248044601/2475062500000000.
- The intermediate sum is 50039601/495012500000.
- 24750625·10111 = 250253569375 > 250248044601, so Λ_tf < 1.0111·10⁻⁴ (≈ 1.01108·10⁻⁴).
- On the box: d/de(4e²(2 − e)⁻²) = 16e(2 − e)⁻³; Λ_tf(¼, ½) = 41/64 exactly; Λ_tf increases in both variables; and
  z ≤ ⅛.

### Thresholds at every use

grep ε_L, γ_1, lem:iii-d-7-1 and prop:iii-f1-3-3 over `chapters/`:

- Rows u3 and u4 and step (2) of thm:vi-c-2-1 are the uses of ε_L and γ_1. Items 6 and 7 replace all of them, and the
  new texts are correct:
  - e_Υ ∈ (0, min(ε_1, ½)] is closed, as prop:iii-d1-4-1 allows e_Υ ∈ [0, ϵ_1];
  - z_Υ ≤ ⅛;
  - the proof of thm:vi-c-2-1 stands.
- The remaining use is chapter 71 line 1780 (finding 4).
- lem:iii-d-7-1 is used in four further places:
  - ch32:827, sec:iii-d1-1 (TF) on a compact neighbourhood 𝒦 of 𝗉_0 where γ_Υ may be negative, and through it
    prop:iii-d1-4-1 Step 1 (line 1064). Part (b) covers both, as item 11 says.
  - ch65:448 and ch66:911, at γ_Υ = 0, covered by (a) and by the unchanged γ_Υ = 0 paragraph.
  - ch34:674, inside Step 6, which item 5 removes.
- prop:iii-f1-3-3 is used in about twenty places. All of them stay true under the new statement:
  - ch34:1127 and ch35:939 and 1423 cite "the parameters of prop:iii-f1-3-3";
  - ch46:93 says "small enough for … the tf-admissibility";
  - ch71:1936 and 2397–2401 concern s, not γ_Υ.
- Nothing outside prop:iii-f1-3-3 cites its Step 6 or P̂′.

### Placement texts

Items 2, 5, 6, 7, 9 and 10 each have an old text that occurs exactly once (item 8: see finding 3):

- item 2 at ch32:780;
- item 5 at ch34:635;
- item 6 at ch46:1729;
- item 7 at ch46:1791;
- item 9 at ch71:4961;
- item 10 at ch90:83.

The diffs confirm the descriptions in items 2 and 5:

- item 2: only proof line 5 changes; the first four lines and the last fourteen lines are unchanged;
- item 5: statement, (i), Steps 5–6 → Step 5, and the sentence at lines 682–684.

The insertion points are right: item 1 between ch32:802 and ch32:804; item 4 between ch34:633 and ch34:635. The eleven
labels of item 1 and lem:tf-lin-reduction are defined nowhere else. All twelve crosswalk rows point to the right lines
of P-T78.

### Typography

- Every line of P-T78 is at most 121 characters, also after label resolution with the current numbering and worst-case
  numbers for the new labels.
- No wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|".
- All labels are lowercase, and every reference resolves to a defined or new label.
- `lint.py` on lines 1–248 together with all new placement texts gives no hit except references undefined in the
  isolated file.
- The replacement texts proposed above satisfy the same rules.

Scratch checks are in
`/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpt78/`:

- `modes.py`: sympy check of eq:tf-modes and of the ĒḠ identity;
- `lam.py`: exact Λ_tf values and the box bounds;
- `dh.py`: numerical test of the two inequalities;
- `typo.py`: line lengths, wrapped-line starts and labels;
- `occ.py`: occurrences of the old texts;
- `proposals.md`: length checks of the replacement texts.
