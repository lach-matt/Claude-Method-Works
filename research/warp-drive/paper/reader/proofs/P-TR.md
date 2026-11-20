### The bounds at other values of h {#sec:tr}

[[thm:uc-integer]] bounds d at the computational point, whose damping value h = 10⁻⁶ is not in the set 𝖧 of
[[eq:iv4-0-1]] ([[rem:ec-point-outside]]). This section keeps the gauge parameters (γ_Υ, e_Υ) = (1/100, 1/100) and lets
h run through [h₁, 10⁻⁶), h₁ := 4.76·10⁻¹¹. In this chapter h enters through four inputs only: (a) the number ε_ind(h)
of [[prop:np-10-52]] (iii), through ε_g = min(ε_Υ, ε_ind) and the constants of [[eq:iii-i9-1-1]]
([[lem:uc-admissible]]); (b) the exponents of ℰ^ι_ind that come from the roots of □^C ([[prop:is-iota]],
[[prop:is-logs]]); (c) the simplicity of the indicial roots of L̂_b(0) on the strip −101 ≤ Re ≤ 5 ([[prop:is-mult]]);
(d) the singular roots of real part at most 4 and the orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5
([[lem:sp-roots]], [[thm:sp-spectrum]], [[cor:sp-lstar]]). The forward loss and its orders hold for every γ_C
([[lem:fwd-orders]]), and so do [[lem:ec-theta-in-zero]], [[prop:uc-ltf]], [[prop:uc-dbg]] and the choices of
[[def:cs-choices]]; every other number of the chapter is fixed by (γ_Υ, e_Υ), by (v_C, e_C) or by the choices of
[[def:uc-choice]].

We locate the roots of the polynomials P_l, C and p_(v) of [[prop:np-10-12]] uniformly for 0 < h ≤ 10⁻⁶, as functions
of two parameters: h and y := e_Cκ, which fixes the degree ([[sec:tr-roots]]). This gives the four inputs at every
h ∈ 𝖧 ∩ [h₁, 10⁻⁶) outside a set 𝖩 ([[def:tr-exceptional]]), and [[thm:uc-integer]] holds there with the same numbers
([[thm:tr-transfer]]). The set 𝖩 is the price of moving h: as h varies, the roots of real part at least 5/2 cross the
integers, at finitely many values of h for each degree, and near such a value ε_ind(h) tends to 0. 𝖩 is a finite union
of intervals of total length below 1.7·10⁻¹¹ ([[prop:tr-measure]]), and it cannot be dropped: near a crossing every
admissible choice of the weights gives d_acc > D_acc ([[prop:tr-fail]]). The lower end h₁ is fixed by the root of P_2
near 2, which lies less than 153600h² below 2 + 40h/13: below 13ε_Υ/40 = 4.7512…·10⁻¹¹ no h satisfies the
hypothesis.

*Setting.* Throughout this section e := e_C = 1/102400 and v := v_C = 1/2; h ∈ (0, 10⁻⁶] and ϖ := h/e = 102400h, so
0 < ϖ ≤ 0.1024; for l ≥ 1, κ := l(l + 2), x := hκ and y := eκ, so that x = ϖy and y depends on l alone; P_l,
P_0 = −(ι − 2)C and p_(v) are the polynomials of [[prop:np-10-12]] at (v, e, h); ε_Υ := 1.4619·10⁻¹⁰ is the value of
[[def:uc-choice]], and h₁ := 4.76·10⁻¹¹. The roots of C, P_l and p_(v) give the entries ι − 1 of the lists of
[[prop:np-10-52]], and such an entry has modulus at most 50 exactly when |ι − 1| ≤ 50.

**Definition {#def:tr-exceptional}** (The condition (H_ε) and the set 𝖩.) Let 0 < h ≤ 10⁻⁶.

(a) h satisfies *(H_ε)* if every root ι of C, of P_l (l ≥ 1) and of p_(v) (l ≥ 1) with |ι − 1| ≤ 50 has
dist(Re ι, ℤ) ≥ ε_Υ, except the root 2 of P_0 and of P_1 and the root 3 of p_(v) at l = 1.

(b) For y ≥ 3/20 (that is, l ≥ 123), ι_B(l, h) is the root of P_l with |ι − 2 − x| < 1/100; for y ≥ 1/5 (that is,
l ≥ 143), ι_P(l, h) is the root of P_l with Re ι > 19/10 and Im ι > 0, and b(l, h) := ¼(24y − (2 + x)² − 16x)^(1/2);
ι_v(l, h) is the larger root of p_(v). Each is well defined and depends continuously on h ([[lem:tr-large]],
[[lem:tr-c-v]]).

(c) 𝖩 is the set of h ∈ [h₁, 10⁻⁶] for which there are l and an integer n with 3 ≤ n ≤ 51 such that
|ι_B(l, h) − n| < ε_Υ, or b(l, h) ≤ 50.2 and |Re ι_P(l, h) − n| < ε_Υ, or n ≥ 4 and |ι_v(l, h) − n| < ε_Υ.

**Theorem {#thm:tr-transfer}** (The bounds of [[thm:uc-integer]] at other values of h.) Let h ∈ 𝖧 with
h₁ ≤ h < 10⁻⁶ and h ∉ 𝖩, and suppose that, with this h, the gauge parameters e_Υ = γ_Υ = 1/100 meet the conditions that
[[thm:vi-c-2-1]] places on them, for some γ_(Υ,H). Take (v_C, e_C) of [[eq:iv4-0-1]], the index sets as constructed,
and the choices of [[def:uc-choice]] and [[def:cs-choices]]. Then:

(i) (*the inputs*) ε_Υ ≤ ε_ind(h) ≤ min(δ_50, ι₂ − 2), where ι₂ is the root of P_2 with
(40/13 − 153600h)h < ι₂ − 2 < 40h/13; the exponents of ℰ^ι_ind of real part at most 5 are those of ℰ_ind, the integers
1, …, 5 and numbers of real part greater than 3, none an integer; every indicial root of L̂_b(0) of real part in
[−101, 5] is simple; and every pole of N_ι⁺(L̄, ·)⁻¹ of real part at most 5 is simple ([[prop:tr-eps]],
[[prop:tr-inputs]]);

(ii) (*the bounds*) every statement of [[thm:uc-integer]] holds at (h, 1/100, 1/100) with the same numbers:
c_* < C_* = 6.4368·10³⁵; d_acc ≤ d_R ≤ D_acc and d_NM ≤ D_acc < 1.57157·10⁵⁰; N_NM ≤ 21D_acc + 6 < 3.30029·10⁵¹;
d_Ψ, d_FM ≤ 1,038,326,399,999,948; d_acc, d_R < 2.6193·10⁴⁹ and d_NM < 5.2386·10⁴⁹; at a level β ∈ (3, α],
1 + n_ι ≤ c(β) ≤ C_lev; and d_NM ≥ d_acc > 1.2497·10²⁴, N_NM > 2.624·10²⁵ for every admissible choice of the
weights, with 3R > 1.2498·10²⁴ at the choice of [[def:uc-choice]].

The lower bounds of (ii) hold at every h ∈ 𝖧 at which (1/100, 1/100) meets those conditions, whether or not h ∉ 𝖩 and
h ≥ h₁ ([[prop:ec-rounds]], [[cor:uc-two-offsets]]).

**Remark {#rem:tr-scope}** (What the theorem assumes.) [[thm:tr-transfer]] is conditional, and its hypothesis may be
empty. It needs an h ∈ 𝖧 with h ≥ h₁, and the supremum h_* = min(10⁻⁶, h_0, h_tf) of 𝖧 is not determined, h_0 and h_tf
being thresholds whose existence is proved and whose values are not ([[rem:ec-point-outside]]); if h_* ≤ h₁, no h
qualifies. It needs also that (1/100, 1/100) lie below the gauge thresholds of [[thm:vi-c-2-1]] at that h, which this
paper does not decide. The other restrictions are proved to be needed. Below 13ε_Υ/40 = 4.7512…·10⁻¹¹ the root ι₂
gives ε_ind(h) < ε_Υ, so ε_g = ε_ind(h) < ε_Υ and the counts of [[prop:uc-explicit]] that use ε_g change; h₁ lies
within 0.19 % of that value. On 𝖩 the condition (H_ε) can fail, and where ε_ind(h) < 1.38·10⁻²⁵ the bound fails for
every admissible choice ([[prop:tr-fail]]). What the theorem gives is therefore: if the parameter point
(h, 1/100, 1/100) is admissible, h ≥ h₁ and h ∉ 𝖩, the bounds computed at h = 10⁻⁶ are bounds at h.

#### The sextic in two parameters {#sec:tr-split}

**Lemma {#lem:tr-split}** (The sextic and its derivative in h.) Let l ≥ 1 and 0 < h ≤ 10⁻⁶, put
𝒬(ι) := 2ι² − (3x + 10)ι + (4 + x)(3 + x) + (3 − 2ϖ)y and U := (2 + x − ι)𝒬. Then

    P_l = U + eF,     F := F₁ + hF₂ + h²F₃,                                                                {#eq:tr-split}

    F₁ := 5ι³ − 20ι² + 5ι + 30 + x(−9ι² + 15ι − 3) + x²(ι − 1)
          + ϖ(−5ι⁴ + 33ι³ − 71ι² + 45ι + 10 + x(8ι³ − 32ι² + 33ι + 1) + x²(−3ι² + 6ι − 2)),
    F₂ := 6ι⁴ − 19ι³ + 6ι² + 21ι − 10 + x(−2ι³ + 4ι² − ι − 1)
          + ϖ(−4ι⁵ + 25ι⁴ − 49ι³ + 21ι² + 21ι − 6 + x(3ι⁴ − 12ι³ + 12ι² − 3)),
    F₃ := −ι(ι − 2)(ι − 1)²(ι + 1)(ϖι − 3ϖ − 1).

With F₁, F₂, F₃ read as polynomials in (ι, x, ϖ) and h = eϖ, the derivative of P_l in h at fixed l is

    ∂_hP_l = κ(𝒬 + (2 + x − ι)(5 + 2x − 3ι) + e∂_xF) + F^ϖ,
    F^ϖ := ∂_ϖF₁ + eF₂ + h∂_ϖF₂ + 2ehF₃ + h²∂_ϖF₃.                                                        {#eq:tr-dh}

Further, with a := (3x + 10)/4 and Δ := (2 + x)² + 16x − 24y,

    𝒬(ι) = 2(ι − a)² − Δ/8,     𝒬(2 + x + s) = 3(1 − ϖ)y + (x − 2)s + 2s²,     F(2 + x) = −x g_B,
    g_B := 24 + 10x + 3x² − 6ϖx − 3ϖx² + h(ϖx⁴ + 3ϖx³ − 3ϖx² − 7ϖx + 6ϖ − 4x³ − 21x² − 27x − 6)
           + h²(x + 1)²(x + 2)(x + 3)(ϖx − ϖ − 1),                                                     {#eq:tr-gb}

and F₁(a + s) = A₀ + A₁s + A₂s² + A₃s³ + A₄s⁴ with

    A₀ := −35/8 − 363x/16 − 357x²/32 − 141x³/64 + ϖ(−15/16 + 91x/16 + 85x²/16 + 117x³/64 + 27x⁴/256),
    A₁ := −5/4 − 15x/4 − 65x²/16 + ϖ(−15/4 + 13x/2 + 69x²/16 + 9x³/16),
    A₂ := 35/2 + 9x/4 − ϖ(11 + 41x/4 + 15x²/8),     A₃ := 5 − ϖ(17 + 7x),     A₄ := −5ϖ.               {#eq:tr-aj}

*Proof.* [[lem:s14-sextic-split]] (i) and its proof give P_l = U + hW, W = R₁ + hR₂ + h²R₃, as identities in
(ι, x, h, ε₀) with e = ε₀h, the polynomials R₁, R₂, R₃ of [[sec:tab-a-split]] being of degree at most 1 in ε₀. At a
given h take ε₀ := e/h = 1/ϖ. The 𝒬 of that lemma is 2ι² − (3x + 10)ι + x² + (5 + 3ε₀)x + 12, which is ours, as
x² + 5x + 12 + 3x/ϖ = (4 + x)(3 + x) + (3/ϖ − 2)x and x/ϖ = y. As h = eϖ, hW = e(ϖR₁ + hϖR₂ + h²ϖR₃), and
multiplying R₁, R₂ and R₃ = ι(ι − 2)(ι − 1)²(ι + 1)(ε₀ + 3 − ι) by ϖ gives F₁, F₂ and F₃.

For [[eq:tr-dh]], P_l(ι) = Φ(ι, hκ, h/e) with Φ(ι, x, ϖ) := U + eF, F evaluated at h = eϖ; so
∂_hP_l = κ∂_xΦ + e⁻¹∂_ϖΦ. Here ∂_x𝒬 = −3ι + 7 + 2x + (3 − 2ϖ)/ϖ, since (3 − 2ϖ)y = (3 − 2ϖ)x/ϖ, and
∂_ϖ𝒬 = −3x/ϖ²; with x/(eϖ²) = κ/ϖ,

    κ∂_xU + e⁻¹∂_ϖU = κ𝒬 + (2 + x − ι)(κ(−3ι + 7 + 2x + 3/ϖ − 2) − 3κ/ϖ) = κ(𝒬 + (2 + x − ι)(5 + 2x − 3ι)),

and κ∂_x(eF) + e⁻¹∂_ϖ(eF) = κe∂_xF + F^ϖ, the term eF₂ + 2ehF₃ coming from ∂_ϖh = e. The identities [[eq:tr-gb]] and
[[eq:tr-aj]] are the substitutions ι = 2 + x and ι = a + s, multiplied out; 𝒬(2 + x) = −x + (3 − 2ϖ)y = 3(1 − ϖ)y, and
𝒬′(2 + x) = 4(2 + x) − 3x − 10 = x − 2. ∎

*Majorants.* For a polynomial g in ι, x, ϖ and h (and e) we write ḡ(R, X) for the polynomial obtained by replacing every
coefficient by its absolute value, ϖ by 0.1024, h by 10⁻⁶ and e by 1/102400, |ι| by R and x by X. Then
|g(ι, x, ϖ, h)| ≤ ḡ(R, X) whenever |ι| ≤ R, 0 ≤ x ≤ X, 0 < ϖ ≤ 0.1024 and 0 < h ≤ 10⁻⁶, and ḡ increases in R and X
([[lem:s14-majorant]]). We use F̄₂, F̄₃, F̄_ι := (∂_ιF)‾, F̄_x := (∂_xF)‾, F̄^ϖ := (F^ϖ)‾ and ḡ_B(X); and Ā_j(X, ϖ̄)
for A_j with its coefficients replaced by their absolute values, x by X and ϖ by ϖ̄. Where a smaller bound ϖ̄ for ϖ
is known, it replaces 0.1024.

#### The roots, uniformly in h {#sec:tr-roots}

**Lemma {#lem:tr-c-v}** (The scalar type 0 and the vector type.) Let 0 < h ≤ 10⁻⁶.

(a) The root ι₁ > 2 of C satisfies 2 + 7·10⁻⁵ < ι₁ < 5/2; the other two roots of C have real part below −100.

(b) Let l ≥ 1. The roots of p_(v) are real; the smaller is below −100, and the larger, ι_v(l, h), equals 3 at l = 1
and increases with l. For l ≥ 2, ι_v(l, h) − 3 ≥ h(κ − 3)/(1 + 2h(ι_v(l, h) − 1)), and ι_v(2, h), ι_v(3, h) ∈ (3, 4).
For an integer n ≥ 4, ι_v(l, h) = n exactly when h = (n − 3)/((l + 1)² − (n − 1)²). Finally

    ∂_hι_v(l, h) = ((l + 1)² − (ι_v(l, h) − 1)²)/(1 + 2h(ι_v(l, h) − 1)).                               {#eq:tr-vslope}

*Proof.* (a) As in the proof of [[prop:np-10-54]], C = C₀ + C_h with C₀ = (5e − 2)ι + 5e + 4 and
C_h = 3h(1 + 2ι − ι²) + h²ι(3 + 2ι − ι²) + ehι(ι + 1), C has exactly one root in (2, ∞) with C(2) > 0, and its other
two roots have real part below −100. At ι = 2 + 7·10⁻⁵, C₀ = 15e − (2 − 5e)·7·10⁻⁵ > 1.4648·10⁻⁴ − 1.4·10⁻⁴ > 0 and
C_h > 0, as 1 + 2ι − ι² = 2 − (ι − 1)² and 3 + 2ι − ι² = 4 − (ι − 1)² are positive there. At ι = 5/2,
C₀ = 35e/2 − 1 < 0 and C_h = −3h/4 + 35h²/8 + 35eh/4 < 0. So ι₁ lies between the two points.

(b) At v = 1/2, −h⁻¹p_(v)(ι) = f(ι)/h with f(ι) := hι² − (2h − 1)ι − hκ − 3, and the roots are real by
[[lem:s14-small-h]] (c); the smaller is below −100 by [[prop:np-10-54]] (i). f(3) = h(3 − κ), which is 0 at l = 1
and negative for l ≥ 2, and f′(ι) = 1 + 2h(ι − 1) > 0 for ι ≥ 1; f decreases in κ, so ι_v increases with l. For
l ≥ 2 the mean value theorem gives ι_v − 3 = h(κ − 3)/f′(ξ) for some ξ ∈ (3, ι_v), and f′(ξ) ≤ 1 + 2h(ι_v − 1).
f(4) = 1 + 8h − hκ is 1 at l = 2 and 1 − 7h > 0 at l = 3, so ι_v(2, h), ι_v(3, h) < 4. f(n) = h(n² − 2n − κ) + n − 3
vanishes exactly at the stated h, as n² − 2n − κ = (n − 1)² − (l + 1)². Differentiating f(ι_v) = 0 in h,
(ι_v² − 2ι_v − κ) + f′(ι_v)∂_hι_v = 0, which is [[eq:tr-vslope]]. ∎

**Lemma {#lem:tr-small}** (The degrees with y ≤ 3/20.) Let 0 < h ≤ 10⁻⁶ and 1 ≤ l ≤ 122, so that y ≤ 3/20 and
x ≤ 0.01536. The three roots of P_l of real part greater than 19/10 are real, simple and lie in (2, 3):

(a) for l = 1 they are 2 and one root in each of (2 + y, a) and (a, 3 − y/2);

(b) for l = 2 they lie one in each of (2 + (40/13 − 3ϖ/2)h, 2 + 40h/13), (2 + y, a) and (a, 3 − y/2);

(c) for 3 ≤ l ≤ 122 they lie one in each of (2 + 3.1h, 2 + y), (2 + y, a) and (a, 3 − y/2).

In particular the root of P_2 nearest 2, ι₂, satisfies (40/13 − 153600h)h < ι₂ − 2 < 40h/13.

*Proof.* By [[prop:np-10-54]] (i), P_l has exactly three roots of real part greater than 19/10, counted with
multiplicity. As P_l has real coefficients, three sign changes on (2, 3) at points of three disjoint intervals give
three real roots there, one in each interval, simple, and no other root of real part above 19/10. We use the
decomposition [[eq:tr-split]] at the points 2 + y, a, 3 − y/2, and at one point near 2. Note that
2 + 3.1h < 2 + y < a < 3 − y/2, as 3.1h ≤ 3.1·10⁻⁶ < 3e ≤ y, a − 2 ≥ 1/2 and 3x/4 + y/2 < 1/2.

*At 2 + y.* Substituting into [[eq:tr-split]], U(2 + y) = −y²(1 − ϖ)²(1 + (2 − ϖ)y) < 0, and

    F₁(2 + y)/y = −15 + 10y + 5y² − ϖ(12 + 14y + 16y² + 5y³) + ϖ²(3 + 2y + 17y² + 8y³) − ϖ³(2y + 6y² + 3y³).

For y ≤ 3/20 and ϖ ≤ 0.1024 its positive terms add to at most 1.652; and (F₂ + hF₃)(2 + y)/y, a polynomial in
(y, ϖ, h) as F₂(2, x, ϖ) = −3x(1 + ϖ) and F₃ has the factor ι − 2, has majorant at most 15.8 there. So
F(2 + y)/y < −15 + 1.652 + 15.8·10⁻⁶ < 0, and P_l(2 + y) = U(2 + y) + eF(2 + y) < 0.

*At a.* U(a) = (2 − x)Δ/32 by [[eq:tr-split]] and 𝒬(a) = −Δ/8, with Δ = 4 + 20x + x² − 24y ≥ 4 − 24·(3/20) = 0.4; so
U(a) ≥ 1.9846·0.4/32 > 0.0248. And |F(a)| ≤ Ā₀(0.01536, 0.1024) + 10⁻⁶F̄₂(2.512, 0.01536) + 10⁻¹²F̄₃(2.512)
≤ 4.832 + 0.0009, as a ≤ 2.5116. So e|F(a)| < 4.8·10⁻⁵ and P_l(a) > 0.

*At 3 − y/2.* U(3 − y/2) = (y/4)(y + 2ϖy − 2)(4 − 8ϖ + y + 3ϖy + 2ϖ²y), whose second factor is at most
−2 + 0.15·1.2048 < −1.8192 and whose third is at least 4 − 0.8192; so U(3 − y/2) ≤ −1.4466y. Further

    F₁(3 − y/2) = −8ϖ − y(10 + 24ϖ − 28ϖ²) + y²(25/4 + 17ϖ/2 − 53ϖ²/2 − 11ϖ³)
                  + y³(−5/8 + 9ϖ/8 + 19ϖ²/2 + 6ϖ³) − y⁴(5ϖ/16 + ϖ² + 3ϖ³/4),

so |F₁(3 − y/2)| ≤ 8ϖ + 13.89y, and h|F₂| + h²|F₃| ≤ 10⁻⁶F̄₂(3, 0.01536) + 10⁻¹²F̄₃(3) < 0.0016 there. Hence
e|F(3 − y/2)| ≤ 8h + 1.357·10⁻⁴y + 1.6·10⁻⁸, which is below 1.4466y, as y ≥ 3e > 2.9297·10⁻⁵ gives
(1.4466 − 1.357·10⁻⁴)y > 4.23·10⁻⁵ > 8·10⁻⁶ + 1.6·10⁻⁸. So P_l(3 − y/2) < 0.

*Near 2.* (a) P_1(2) = 0 ([[prop:np-10-12]] (iii)); with the signs −, +, − at 2 + y, a, 3 − y/2 this gives the three
roots. (b) At l = 2, κ = 8, put ι = 2 + τh. Substituting into [[eq:tr-split]] with x = 8h and dividing by he = ϖe²,

    P_2(2 + τh) = he(120 − 39τ + ϖ(2τ² − 11τ − 40) + hQ(τ, ϖ, h)),
    Q := 40 − 159τ + 10τ² + ϖ(360 − 251τ + 47τ² − 2τ³) + h(5τ³ − 36τ² − 2τ + ϖ(−7τ³ + 135τ² − 378τ))
         + h²(29τ³ − 47τ² + ϖ(−5τ⁴ + 55τ³ − 85τ²)) + h³(6τ⁴ + τ³ + ϖ(−15τ⁴ + 96τ³))
         + h⁴(7τ⁴ + ϖ(−4τ⁵ + 14τ⁴)) + h⁵(τ⁵ − 6ϖτ⁵) − ϖh⁶τ⁶,                                            {#eq:tr-p2}

and for 0 ≤ τ ≤ 3.1, |Q| ≤ 798, so e|Q| < 0.008. With f(τ) := 2τ² − 11τ − 40, f(40/13) = −9280/169 < −54.91. At
τ = 40/13, 120 − 39τ = 0 and P_2(2 + τh) ≤ ϖhe(−54.91 + 0.008) < 0. At τ₀ := 40/13 − 3ϖ/2, 120 − 39τ₀ = 117ϖ/2 and
f(τ₀) = −9280/169 − (3ϖ/2)(17/13) + 9ϖ²/2 > −54.912 − 1.9616ϖ, so P_2(2 + τ₀h) ≥ ϖhe(58.5 − 54.912 − 0.2009 −
0.008) > 0. With the signs −, +, − at 2 + y, a, 3 − y/2 this gives the three roots, and the last claim, as
(3ϖ/2)h = 153600h². (c) For 3 ≤ l ≤ 122, κ ≥ 15. Put t := 3.1h. As x − 2t = h(κ − 6.2) > 0,
𝒬(2 + t) = (x − 2t)(1 + x − t) + (3 − 2ϖ)y ≥ 2.7952y, and U(2 + t) = (x − t)𝒬(2 + t) ≥ 2.7952heκ(κ − 3.1). By
[[eq:tr-split]], F(2) = −x(9 − x − 3ϖ + 2ϖx + 3h + 3ϖh), so |F(2)| ≤ 9.326x, and |∂_ιF| ≤ 15.64 on [2, 2 + t], by the
majorant of ∂_ιF(2 + t′, x, ϖ, h) in t′ ≤ 3.1·10⁻⁶ and x ≤ 0.01536. So e|F(2 + t)| ≤ he(9.326κ + 48.49), and
2.7952κ(κ − 3.1) − 9.326κ − 48.49 is 310.56… at κ = 15 and increases for κ ≥ 15. So P_l(2 + t) > 0; with the signs
at 2 + y, a and 3 − y/2 this gives the three roots. ∎

**Lemma {#lem:tr-large}** (The degrees with y ≥ 3/20.) Let 0 < h ≤ 10⁻⁶ and l ≥ 123, so that y ≥ 3/20, and let
x ≤ 70 in (a)–(c).

(a) P_l has exactly one root with |ι − 2 − x| < 1/100; it is real, it is ι_B(l, h), and if x ≤ 1/2 it lies in
(2 + x/2, 2 + 3x/2).

(b) If y ≤ 1/5, so that x ≤ 0.02048, P_l has exactly two roots in |ι − a| < 2/5, and the three roots of P_l of real
part greater than 19/10 are ι_B(l, h) and these two, whose real parts lie in (2.1, 2.92).

(c) If y ≥ 1/5, put ζ := a + ib with b := b(l, h) = ¼(−Δ)^(1/2), and ϱ := 1/20 for x ≤ 20, ϱ := 1/5 for x > 20.
Then b ≥ 0.1561, and P_l has exactly one root in |ι − ζ| < ϱ if b ≤ 56, and exactly one in |ι − ζ| < b/10 if b ≥ 56;
this root is ι_P(l, h), its conjugate is the only root in the conjugate disc, and the three roots of P_l of real part
greater than 19/10 are ι_B(l, h), ι_P(l, h) and its conjugate. If |ι_P(l, h) − 1| ≤ 50, then b ≤ 50.2.

(d) If x ≥ 70, no root of P_l satisfies |ι − 1| ≤ 50.

*Proof.* (a) By [[eq:tr-split]], 𝒬(2 + x + s) = 3(1 − ϖ)y + (x − 2)s + 2s², and 3(1 − ϖ)y ≥ max(0.40392, 26.296875x),
since y ≥ 3/20, ϖ ≤ 0.1024 and (1 − ϖ)y = x(1/ϖ − 1) ≥ 8.765625x. On |s| = r ≤ 1/4, |U| = r|𝒬|, and U has the
single root 2 + x in |s| < r: the roots of 𝒬 lie at distance (3(1 − ϖ)y/2)^(1/2) ≥ 0.449 from 2 + x if they are
non-real, and at distance (2 − x)/4 − Δ^(1/2)/4 > 0.27 if they are real, as then x ≤ 0.0187 and Δ ≤ 0.78. By Rouché's
theorem it suffices that e|F| < r|𝒬| on |s| = r; then P_l has exactly one root there, simple, and real, as P_l has real
coefficients and the disc is symmetric about ℝ. On |s| = r, |F(2 + x + s)| ≤ x|g_B| + rF̄_ι(2 + x + r, x) by
[[eq:tr-gb]] and the mean value theorem. For r = x/2 and x ≤ 1/2: |𝒬| ≥ 3(1 − ϖ)y − x ≥ max(0.40392 − x, 25.296875x)
≥ 0.3885, so |U| ≥ 0.194x, while e|F| ≤ ex(ḡ_B(1/2) + F̄_ι(11/4, 1/2)/2) ≤ ex(30.14 + 222.7) < 0.0025x. For
r = 1/100 and x ≤ 70 the following table gives, on each interval [x_a, x_b], an upper bound for
e(x_bḡ_B(x_b) + F̄_ι(2.01 + x_b, x_b)/100) and a lower bound for (max(0.40392, 26.296875x_a) − m/100 − 0.0002)/100,
m := max(|x_a − 2|, |x_b − 2|), which bound e|F| and r|𝒬| from above and below:

| [x_a, x_b] | ḡ_B(x_b) ≤ | F̄_ι(2.01 + x_b, x_b) ≤ | e|F| ≤ | r|𝒬| ≥ |
|---|---|---|---|---|
| [0, 1/2] | 30.14 | 385.8 | 1.849·10⁻⁴ | 3.836·10⁻³ |
| [1/2, 5] | 159.8 | 4038 | 8.195·10⁻³ | 0.1311 |
| [5, 20] | 1560 | 76270 | 0.312 | 1.313 |
| [20, 40] | 5741 | 457900 | 2.288 | 5.255 |
| [40, 55] | 10620 | 1.093·10⁶ | 5.808 | 10.51 |
| [55, 70] | 16980 | 2.141·10⁶ | 11.82 | 14.45 |

In every row the fourth entry is below the fifth.

(b) Here x = ϖy ≤ 0.02048 and Δ = 4 + 20x + x² − 24y lies in [−0.8, 0.81], so the roots of 𝒬 lie within 0.225 of a,
while |2 + x − a| = (2 − x)/4 ≥ 0.4948. On |ι − a| = 2/5, |U| ≥ 0.09488·2·0.175² > 0.00581. There |ι| ≤ 2.9155, and
by [[eq:tr-aj]], |F| ≤ Σ_j Ā_j(0.02048, 0.1024)(2/5)^j + 10⁻⁶F̄₂(2.9155, 0.02048) + 10⁻¹²F̄₃(2.9155), with
Ā₀, …, Ā₄ ≤ 4.9526, 1.7264, 18.695, 6.7555, 0.512; so |F| ≤ 9.081 and e|F| < 9·10⁻⁵ < |U|. By Rouché's theorem P_l
has as many roots in |ι − a| < 2/5 as U, namely the two roots of 𝒬. The disc of (a) with r = x/2 is disjoint from
this one, so these are three roots of real part greater than 2, all of them ([[prop:np-10-54]] (i)), and
a ± 2/5 ⊂ (2.1, 2.92) as 2.5 ≤ a ≤ 2.5154.

(c) As y = x/ϖ ≥ max(1/5, x/0.1024), 16b² = 24y − (2 + x)² − 16x ≥ max(4.8 − (2 + x)² − 16x, 214.375x − 4 − x²);
the first bound decreases and the second increases in x, and they agree at x = 0.02048, where both exceed 0.3899; so
b ≥ 0.1561, and b ≥ 2.536, 8.073, 15.579, 21.82 for x ≥ 1/2, 5, 20, 45. By [[eq:tr-split]] U = (ι − ζ)V with
V := 2(2 + x − ι)(ι − ζ̄), and d := |2 + x − ζ| = (b² + (x − 2)²/16)^(1/2) ≥ b. On |ι − ζ| = r < b,
|U| ≥ 2r(d − r)(2b − r) ≥ 2r(b − r)(2b − r), and U has the single root ζ inside. On that circle |ι − a| ≤ b + r, so by
[[eq:tr-aj]] |F| ≤ Σ_j Ā_j(x, ϖ̄)(b + r)^j + 10⁻⁶F̄₂(a + b + r, x) + 10⁻¹²F̄₃(a + b + r), where ϖ̄ bounds ϖ: ϖ ≤ 0.1024,
ϖ = x/y ≤ 5x, and ϖ ≤ 3x/(2b²), as b² ≤ 3y/2. For b ≤ 56 the following table covers the possible (x, b) by boxes
[x_a, x_b] × [b_a, b_b], each with r = ϱ; in each, N bounds e|F| (from the values at x_b and b_b, with
ϖ̄ := min(0.1024, 5x_b, 3x_b/(2b_a²))) and D := 2ϱ(b_a − ϱ)(2b_a − ϱ) bounds |U| from below; the last column is used in
[[lem:tr-slopes]]:

| [x_a, x_b] | [b_a, b_b] | ϱ | ϖ̄ | N ≤ | D ≥ | dev ≤ |
|---|---|---|---|---|---|---|
| [0, 0.02048] | [0.156, 0.6] | 1/20 | 0.1024 | 1.555·10⁻⁴ | 2.777·10⁻³ | — |
| [0, 0.02048] | [0.6, 2.5] | 1/20 | 0.0854 | 2.488·10⁻³ | 0.06325 | — |
| [0, 0.02048] | [2.5, 10] | 1/20 | 4.92·10⁻³ | 0.0704 | 1.212 | — |
| [0, 0.02048] | [10, 40] | 1/20 | 3.08·10⁻⁴ | 3.455 | 19.85 | — |
| [0, 0.02048] | [40, 56] | 1/20 | 1.92·10⁻⁵ | 9.151 | 319.4 | — |
| [0.02048, 1/2] | [0.156, 0.6] | 1/20 | 0.1024 | 3.242·10⁻⁴ | 2.777·10⁻³ | — |
| [0.02048, 1/2] | [0.6, 2.5] | 1/20 | 0.1024 | 2.965·10⁻³ | 0.06325 | — |
| [0.02048, 1/2] | [2.5, 10] | 1/20 | 0.1024 | 0.1422 | 1.212 | — |
| [0.02048, 1/2] | [10, 40] | 1/20 | 7.5·10⁻³ | 4.472 | 19.85 | — |
| [0.02048, 1/2] | [40, 56] | 1/20 | 4.69·10⁻⁴ | 9.419 | 319.4 | — |
| [1/2, 5] | [2.53, 3.2] | 1/20 | 0.1024 | 0.01972 | 1.242 | 0.2153 |
| [1/2, 5] | [3.2, 5] | 1/20 | 0.1024 | 0.04029 | 2.0 | 0.2146 |
| [1/2, 5] | [5, 10] | 1/20 | 0.1024 | 0.2139 | 4.925 | 0.1888 |
| [1/2, 5] | [10, 20] | 1/20 | 0.075 | 1.472 | 19.85 | 0.1005 |
| [1/2, 5] | [20, 40] | 1/20 | 0.0188 | 6.644 | 79.7 | 0.0795 |
| [1/2, 5] | [40, 56] | 1/20 | 4.69·10⁻³ | 12.26 | 319.4 | 0.0413 |
| [5, 20] | [8.07, 16] | 1/20 | 0.1024 | 2.212 | 12.9 | 0.1374 |
| [5, 20] | [16, 32] | 1/20 | 0.1024 | 14.67 | 50.96 | 0.0704 |
| [5, 20] | [32, 56] | 1/20 | 0.0293 | 34.69 | 204.3 | 0.0358 |
| [20, 45] | [15.57, 31] | 1/5 | 0.1024 | 28.84 | 190.2 | 0.2923 |
| [20, 45] | [31, 56] | 1/5 | 0.0703 | 105.9 | 761.3 | 0.1148 |
| [45, 70] | [21.81, 43] | 1/5 | 0.1024 | 112.9 | 375.3 | 0.2363 |
| [45, 70] | [43, 56] | 1/5 | 0.0568 | 136.6 | 1468 | 0.0568 |

In every row N < D. For b ≥ 56 take r = b/10: then |U| ≥ 2(b/10)(0.9b)(1.9b) = 0.342b³, and with ϖ ≤ 105/b²,
h = eϖ ≤ 105e/b², b + r = 1.1b and a + b + r ≤ 2.1b (a ≤ 55 ≤ b), the bound for |F| is a sum of terms c_kb^k with
c_k ≥ 0 and k ≤ 3; replacing b^k by b³56^(k−3) gives |F| ≤ 68.77b³, so e|F| < 6.8·10⁻⁴b³ < |U|. In both cases
Rouché's theorem gives exactly one root in the disc. The disc lies in Im ι > 0, as r < b, and is disjoint from the
disc of (a), as d − r > 1/100; by symmetry its conjugate holds exactly one root; so, with ι_B(l, h), these are the
three roots of real part greater than 19/10 ([[prop:np-10-54]] (i)), and the root in the upper disc is ι_P(l, h).
Finally |ι_P − 1| ≥ Im ι_P > b − r, which exceeds 50 if b > 50.2 (r ≤ 1/5 for b ≤ 56, r = b/10 for b ≥ 56).

(d) For |ι − 1| ≤ 50, |ι| ≤ 51 and Re ι ≤ 51, so |2 + x − ι| ≥ x − 49. The roots of 𝒬 are non-real for x ≤ 214.35,
as Δ < 0 there (24y ≥ 234.375x and x² − 214.375x + 4 < 0), with real part a; for larger x they have real part a or
are real and at least a − (2 + x)/4 = x/2 + 2, as Δ < (2 + x)². So |𝒬(ι)| ≥ 2m², with m := (3x − 194)/4 ≥ x/17.5 for
70 ≤ x ≤ 214.35 and m := x/2 − 49 ≥ 0.2714x beyond, and |U| ≥ 2(x − 49)m² ≥ 0.001959x³ for x ≥ 70. On the other side
|F| ≤ F̄(51, x) = c₀ + c₁x + c₂x² with c₀ < 4,646,946, c₁ < 141,543, c₂ < 882.57, so for x ≥ 70,
e|F| ≤ ex²(c₀/4900 + c₁/70 + c₂) < 0.0377x² < 0.001959·70x² ≤ |U|. So P_l = U + eF has no zero with
|ι − 1| ≤ 50. ∎

**Lemma {#lem:tr-slopes}** (The roots move fast at the integers.) Let l be fixed and let the derivatives be in h.

(a) If y ≥ 3/20 and 0.98 ≤ x ≤ 49.02, then ∂_hι_B(l, h) ≥ 0.98κ.

(b) If y ≥ 1/5, 1/2 ≤ x ≤ 70 and b ≤ 56, then ∂_h Re ι_P(l, h) ≥ (2/5)κ.

(c) If l ≥ 999 and |ι_v(l, h) − n| ≤ 10⁻⁴ for an integer n ≤ 51, then ∂_hι_v(l, h) ≥ 0.99κ.

*Proof.* The roots concerned are simple ([[lem:tr-large]]), so ∂_hι = −∂_hP_l/∂_ιP_l, with ∂_hP_l of [[eq:tr-dh]] and,
by [[eq:tr-split]], ∂_ιP_l = −𝒬 + (2 + x − ι)𝒬′ + e∂_ιF. In the bounds below κ = x/h ≥ 10⁶x.

(a) Put s := ι_B − 2 − x, so |s| < 1/100. Then (2 + x − ι)(5 + 2x − 3ι) = s(1 + x + 3s), 𝒬′(ι_B) = x − 2 + 4s, and

    ∂_hι_B = κ(𝒬 + s(1 + x + 3s) + e∂_xF + F^ϖ/κ)/(𝒬 + s𝒬′ − e∂_ιF)     at ι = ι_B,

with 𝒬(ι_B) = 3(1 − ϖ)y + (x − 2)s + 2s² ≥ 26.296875x − |x − 2|/100 − 0.0002. With A := (1 + x + 0.03)/100 +
eF̄_x + 10⁻⁶F̄^ϖ/x and B := (|x − 2| + 0.04)/100 + eF̄_ι, the majorants at (2.01 + x, x), the quotient is at least
(𝒬 − A)/(𝒬 + B). On the intervals [0.98, 2], [2, 5], [5, 10], [10, 20], [20, 35], [35, 49.02], evaluating 𝒬 from
below at the left end and A, B from above at the right end gives 𝒬 ≥ 25.76, 52.56, 131.4, 262.7, 525.6, 919.9,
A ≤ 0.04152, 0.1004, 0.2386, 0.8528, 2.878, 5.997 and B ≤ 0.02129, 0.06983, 0.231, 0.9253, 3.46, 8.242, so the
quotient is at least 0.9975, 0.9967, 0.9964, 0.9932, 0.988, 0.9846.

(b) Put s := ι_P − ζ, |s| < r with r = ϱ of [[lem:tr-large]] (c), A₂ := 2 + x − ζ, so |A₂| = d, and
c₀ := −(10 + x)/4 − 3ib. As 𝒬 = 2(ι − ζ)(ι − ζ̄) and 4a = 3x + 10, 𝒬(ι_P) = 2s(s + 2ib), 𝒬′(ι_P) = 4ib + 4s and
5 + 2x − 3ι_P = c₀ − 3s. So, at ι = ι_P,

    ∂_hP_l/κ = A₂c₀ + δN,     δN := 2s(s + 2ib) − 3A₂s − c₀s + 3s² + e∂_xF + F^ϖ/κ,
    ∂_ιP_l = 4ibA₂ + δD,      δD := −2s(s + 2ib) + 4A₂s − 4ibs − 4s² + e∂_ιF,

and −A₂c₀/(4ibA₂) = 3/4 − i(10 + x)/(16b) has real part 3/4. Hence

    |∂_hι_P/κ − 3/4 + i(10 + x)/(16b)| ≤ (|δN| + (|c₀|/(4b))|δD|)/(4bd − |δD|),

with |δN| ≤ 2r(r + 2b) + 3dr + r|c₀| + 3r² + eF̄_x + 10⁻⁶F̄^ϖ/x, |δD| ≤ 2r(r + 2b) + 4dr + 4br + 4r² + eF̄_ι,
|c₀| ≤ (10 + x)/4 + 3b, d ≤ b + |x − 2|/4 and d ≥ b, the majorants at (a + b + r, x). Evaluated on the boxes of the
table of [[lem:tr-large]] with x_a ≥ 1/2 (b_b and x_b where the bound increases, b_a and x_a where it decreases), the
right side is at most the last column there, at most 0.2923; so ∂_h Re ι_P ≥ (3/4 − 0.2923)κ > (2/5)κ.

(c) By [[eq:tr-vslope]], with ι_v − 1 ≤ 50.0001 and h ≤ 10⁻⁶, ∂_hι_v ≥ ((l + 1)² − 2501)/1.0001, and
(l + 1)² = κ + 1 ≥ 999·1001 + 1, for which this is at least 0.99κ. ∎

#### The four inputs {#sec:tr-inputs}

**Proposition {#prop:tr-eps}** (The number ε_ind(h).) (a) For every h ∈ (0, 10⁻⁶], ε_ind(h) ≤ min(δ_50, ι₂ − 2) with
ι₂ of [[lem:tr-small]], and ι₂ − 2 < 40h/13.

(b) Every h ∈ [h₁, 10⁻⁶] ∖ 𝖩 satisfies (H_ε), and then ε_ind(h) ≥ ε_Υ.

(c) No h ≤ 13ε_Υ/40 satisfies (H_ε), and at every such h, ε_ind(h) < ε_Υ.

*Proof.* (a) ε_ind(h) ≤ δ_50 is [[prop:np-10-52]] (iii). The entry ι₂ − 1 of ℛ^sc_2 has modulus below 50 and distance
ι₂ − 2 ∈ (0, 40h/13) from ℤ ([[lem:tr-small]] (b)), which bounds the infimum.

(b) Let h ∈ [h₁, 10⁻⁶] ∖ 𝖩 and let ι be a root as in [[def:tr-exceptional]] (a). If ι is a root of C, then ι = ι₁, as
the other roots have |ι − 1| > 101, and 2 + 7·10⁻⁵ < ι₁ < 5/2 ([[lem:tr-c-v]] (a)). If ι is a root of p_(v), then
ι = ι_v(l, h) with l ≥ 2, the smaller root being below −100; ι_v(l, h) − 3 ≥ ι_v(2, h) − 3 ≥ 5h/(1 + 6h) > 4.99h₁ >
ε_Υ, and as h ∉ 𝖩, ι_v is not within ε_Υ of an integer n with 4 ≤ n ≤ 51, while |ι − 1| ≤ 50 gives ι ≤ 51. Let ι be
a root of P_l; then Re ι > 19/10 ([[prop:np-10-54]] (i)). For l ≤ 122, [[lem:tr-small]] places ι in (2, 3) at
distance more than min((40/13 − 153600h)h, 3.1h, 3e, 3e/2) from 2 and 3, apart from ι = 2 at l = 1; as h ↦ (40/13 −
153600h)h increases on (0, 10⁻⁶] and is 1.46461…·10⁻¹⁰ at h₁, and 3.1h₁ = 1.4756·10⁻¹⁰, this is at least ε_Υ. For
123 ≤ l ≤ 142 (3/20 ≤ y ≤ 1/5), [[lem:tr-large]] (a), (b) give ι = ι_B ∈ (2 + x/2, 2.031), with
x/2 = hκ/2 ≥ 7687h > ε_Υ, or Re ι ∈ (2.1, 2.92). For l ≥ 143 and x ≤ 70: if ι = ι_B and x ≤ 1/2, ι ∈ (2 + x/2, 2.75)
with x/2 ≥ 10240h > ε_Υ; if ι = ι_B and x > 1/2, ι is real and within ε_Υ of an integer only if that integer n lies in
[3, 51] (as |ι − 1| ≤ 50), which h ∉ 𝖩 excludes; if ι = ι_P or its conjugate, then b ≤ 50.2 by [[lem:tr-large]] (c),
Re ι ∈ (a − 1/5, a + 1/5) ⊂ (2.3, 51.2), and Re ι lies within ε_Υ of an integer only if that integer lies in [3, 51],
which h ∉ 𝖩 excludes. For x > 70 no such root exists ([[lem:tr-large]] (d)). So (H_ε) holds. Then every non-integer
entry of modulus at most 50 that depends on h has distance at least ε_Υ from ℤ, the h-independent ones have distance at
least δ_50 > ε_Υ ([[prop:np-10-52]] (iii)), and the only h-dependent integer entries are the excepted ones; so
ε_ind(h) ≥ ε_Υ.

(c) For h ≤ 13ε_Υ/40, ι₂ − 2 < 40h/13 ≤ ε_Υ, so ι₂ violates (H_ε) and ε_ind(h) < ε_Υ by (a). ∎

**Proposition {#prop:tr-inputs}** (The other three inputs.) Let h ∈ 𝖧 with h₁ ≤ h < 10⁻⁶ satisfy (H_ε). Then:

(a) (*[[prop:is-iota]] at h*) the exponents of ℰ^ι_ind of real part at most 5, as constructed, are those of ℰ_ind, the
integers 1, …, 5 and the numbers ι + 1 + j of real part at most 5, ι a root of C (ι > 2), of P_l (l ≥ 1, Re ι > 19/10,
ι ≠ 2) or of p_(v) (l ≥ 2, the larger root) at (v, e, h), j ∈ ℕ₀; each such ι has real part greater than 2, none of
real part at most 6 is an integer, and the real ones of real part at most 6 have distance at least ε_Υ from ℤ. The
logarithmic orders of ℰ^ι_ind are at most 3 at real part at most 3/2 and at most 50 at real part at most 5;

(b) (*[[prop:is-mult]] at h*) every indicial root of L̂_b(0) has multiplicity at most 7, and every one of real part in
[−101, 5] is simple at each type and degree at which it occurs;

(c) (*[[lem:sp-roots]] and [[thm:sp-spectrum]] (b) at h*) the sets 𝒮_τ of [[lem:sp-roots]] are 𝒮_s0 = {2, 3 + 𝔡₀,
ι₁ − 1, 4}; 𝒮_s1 = {3, 3 + 𝔡₁, ι − 1, ι′ − 1}, ι, ι′ the roots of P_1 in (2 + 3e, a) and (a, 3 − 3e/2);
𝒮_s2 = {4} ∪ {ι − 1 : P_2(ι) = 0, Re ι > 2}, three numbers in (1, 2); 𝒮_sl = {ι − 1 : P_l(ι) = 0, 2 < Re ι ≤ 5} for
l ≥ 3; 𝒮_v1 = {3, 4}; 𝒮_v2 = {4, ι_v(2, h) − 1}; 𝒮_vl = {ι_v(l, h) − 1} if ι_v(l, h) ≤ 5 and ∅ otherwise (l ≥ 3);
𝒮_t2 = {4} and 𝒮_tl = ∅ (l ≥ 3). Every element of 𝒮_τ is a simple root of type τ, and two distinct elements of one
𝒮_τ differ by an integer only for {2, 4} ⊂ 𝒮_s0 and {3, 4} ⊂ 𝒮_v1. Every pole of N_sf(·)⁻¹ and of N_ι⁺(L̄, ·)⁻¹ of
real part at most 5 is simple, and the order m_ι of [[thm:sp-spectrum]] (b) is at most 1 on {Re ϰ ≤ 5};

(d) [[cor:sp-lstar]] (a)–(c) hold at h: l_* = 50 is admissible, K_ι(ϰ) ≤ 2 for ϰ ∈ Σ, and each raise of a logarithmic
order by a pole order of N_ι⁺(L̄, ·)⁻¹ at real part at most 5 is at most 1.

*Proof.* (a) The proof of [[prop:is-iota]] gives the list at every h: it uses the index sets of [[sec:is-ind]], which
are fixed by the gauge parameters, and [[prop:iii-f4-5-1]] and [[prop:iii-f1-2-3]], which hold at every h for which
(C1) holds, as it does on (0, 10⁻⁶] by [[prop:np-10-54]]. Re ι > 2 is [[prop:np-10-54]] (ii). A root ι of real part at
most 6 that is an integer, or real at distance less than ε_Υ from ℤ, satisfies |ι − 1| ≤ 5 and is none of the excepted
roots, so (H_ε) excludes it. The bound 3 at real part at most 3/2 is that of the proof of [[prop:is-logs]] (c), which
does not involve h, as every exponent ι + 1 + j has real part above 3. For the bound 50, the proof of
[[prop:is-logs]] (c) bounds the order at a real exponent w of u_b of real part at most 3 by 3·16 + 3 − 1 from the three
terms w, w − 1, w − 2, each term of F having order at most 15 and each term of E(α) order 0; this uses only the
simplicity of the real roots of L̂_b(0) of real part at most 3, which (b) gives, and that the integer roots of L̂_b(0)
in [0, 3] are 0, 2, 3, which holds as no root of □^C with |ι − 1| ≤ 50 is an integer other than the excepted ones. At a
non-real exponent no term of F, all of whose exponents are real, enters, and the order is at most 1.

(b) The bound 7 is the first part of the proof of [[prop:is-mult]], which uses (C1) only. On the strip the entries of
each type are −l, l + 2, the roots of (□^Υ_b)^(0) plus 1 and the roots of □^C minus 1, less those of D, and those from
□^Υ_b and the integers are distinct within each type ([[prop:iii-f1-2-3]]). The entries from □^C on the strip are the
ι − 1 with Re ι ≤ 6, the other roots of C, P_l and p_(v) having real part below −100. Each such ι is simple in its
polynomial, as h ∉ 𝖹₁ ([[lem:iv4-1-3]] (b)). Such an ι − 1 is not an integer entry: a non-real one is not real, and a
real one has |ι − 1| ≤ 5 and is not an integer by (H_ε). It is not an entry from □^Υ_b of its type and degree: those
are real, and in (1, 5] they are, at scalar type l, l + 2 + d₂(l) for l ≤ 2 and l + 3 + d₁(l) for l = 1, and at
vector type l, l + 2 for l ≤ 3 and l + 3 for l ≤ 2 ([[lem:is-roots]] (a)); the entries from □^C of real part in (1, 5]
are, at scalar type l ≤ 2, the ι − 1 with ι in (2, 3) ([[lem:tr-small]]), and at vector type l = 2, 3 the numbers
ι_v(l, h) − 1 ∈ (2, 3) ([[lem:tr-c-v]] (b)), none of which equals one of those. At scalar type 0 the entry ι₁ − 1 lies
in (1, 3/2), where that type has no other entry. With the poles, as in the proof of [[prop:is-mult]], this gives (b).

(c) The lists are those of the proof of [[lem:sp-roots]] (a), which does not use h, with the roots located by
[[lem:tr-c-v]] and [[lem:tr-small]]; at l ≥ 3 the condition Re ι ≤ 5 selects the roots. Simplicity is (b). For the
differences: at s0, 𝔡₀ < 1.34·10⁻⁶ ([[lem:is-roots]] (b)), so 3 − ι₁ ∈ (1/2, 1 − 7·10⁻⁵),
4 + 𝔡₀ − ι₁ ∈ (3/2 + 𝔡₀, 2 − 7·10⁻⁵ + 𝔡₀) and 5 − ι₁ ∈ (5/2, 3 − 7·10⁻⁵) contain no integer, nor do 1 ± 𝔡₀. At s1,
ι − 1, ι′ − 1 are distinct points of (1 + 3e, 2 − 3e/2), and 3 − (ι − 1) ∈ (1 + 3e/2, 2 − 3e) and
(3 + 𝔡₁) − (ι − 1) ∈ (1 + 3e/2 + 𝔡₁, 2 + 𝔡₁ − 3e) ⊂ (1, 2), as 𝔡₁ < 3.4·10⁻⁷ < 3e, and likewise for ι′; and
(3 + 𝔡₁) − 3 = 𝔡₁. At s2 the three numbers lie in (1, 2) and are distinct, and 4 − (ι − 1) ∈ (2, 3). At sl, l ≥ 3: for
l ≤ 122 the roots of real part above 2 lie in (2, 3) ([[lem:tr-small]]); for 123 ≤ l ≤ 142 they are ι_B ∈ (2, 2.031)
and two of real part in (2.1, 2.92) ([[lem:tr-large]] (b)), so two real ones differ by less than 1 and a non-real one
differs from each other root by a non-real number; for l ≥ 143 and x ≤ 70 only ι_B is real; for x > 70 no root with
|ι − 1| ≤ 50 exists, so a real root of real part at least 2 exceeds 51, and those of real part at most 5 are non-real,
simple and at most one conjugate pair, as in the proof of [[lem:sp-roots]] (c). At v2, 4 − (ι_v(2, h) − 1) ∈ (1, 2).
So the proof of [[thm:sp-spectrum]] (b) applies: by [[thm:sp-reduction]] (b), [[lem:sp-two-roots]] (c), whose
conditions at s0 and v1 are those just stated, and [[lem:sp-block]], N_sf(·)⁻¹ has at most simple poles on
{Re ϰ ≤ 5}; and as N_ι⁺(L̄, ϰ)⁻¹f = R^(−ϰ)N_sf(ϰ)⁻¹(R^(2+ϰ)f) with R^(2+ϰ)f holomorphic ([[prop:sp-visible]], proof),
the poles of N_ι⁺(L̄, ·)⁻¹ have order at most that of N_sf(·)⁻¹, and m_ι, the order of the pole on Ċ^∞(ι⁺)
([[lem:iii-g1-4-2]] (b)), is at most 1.

(d) The proof of [[cor:sp-lstar]] (a)–(c) uses of the poles only that their orders are at most 1, of the index sets
the bounds of [[prop:is-logs]], which (a) gives, and M ≤ 7, which (b) gives; with these it holds at h. ∎

At h ∈ 𝖹_Q, the countable set of h at which some root of P_l or p_(v) lies in {5/2, 7/2, 9/2} + σ_Υ, the visibility
statement of [[thm:sp-spectrum]] (a), spec_ι⁺(L̄) ∩ {Re ≤ 5} = 𝒫 ∩ {Re ≤ 5}, is not shown by [[lem:sp-exceptional]];
no bound uses it, as (c) gives the orders from above at every h.

#### Proof of the transfer {#sec:tr-proof}

*Proof of [[thm:tr-transfer]].* (i) is [[prop:tr-eps]] (a), (b) and [[prop:tr-inputs]].

(ii) We go through the statements of [[sec:ec-gap-sums]]–[[sec:cs-small]] that the proof of [[thm:uc-integer]] and of
[[prop:uc-d-small]] uses, and show that each holds at (h, 1/100, 1/100) with the same numbers. [[prop:gap-sums]],
[[lem:ec-gauge-gap]], [[prop:is-ind]], [[prop:is-ci-pp]], [[thm:is-gap]], [[thm:is-d0]], [[cor:is-flat]] and
[[lem:uc-two-offsets]] concern numbers fixed by (γ_Υ, e_Υ). [[prop:is-lambda]] and [[prop:is-count]] use of ℰ^ι_ind
only its exponents of real part below 3/2 and its least real part, and by [[prop:tr-inputs]] (a) these are those of
ℰ_ind and 1; so N_Λ, k̄_0, J_* and η_0 = 𝔡₁ are unchanged, and so are [[lem:uc-gaps]], [[lem:uc-lambda]] and
[[lem:uc-n-iota]]. [[cor:sp-lstar]] holds by [[prop:tr-inputs]] (d), so l_* = 50 and K_ι ≤ 2. In
[[lem:uc-admissible]], ε_ind(h) ≥ ε_Υ ([[prop:tr-eps]] (b)) allows ε_ind := min(1, ε_ind(h)) ≥ ε_Υ, so ε_g = ε_Υ as at
the computational point, and the constants of [[eq:iii-i9-1-1]] ask 0 < ε_K < ε_+ < min(δ_♯, ε_ind), which
1.6416·10⁻¹⁴ < 1.64160217·10⁻¹⁴ < ε_Υ ≤ ε_ind meets; every other step of that proof uses the index sets, (G) and
choices that do not involve h. So [[eq:uc-deltas]] holds with Δτ_0 = 0.999ε_Υ, and [[prop:uc-explicit]], [[lem:uc-dr]]
and [[lem:uc-phi-loss]] give the same numbers. In [[sec:cs]] the charges are closed forms in the weights, the counts
of [[lem:uc-lambda]] and [[lem:uc-n-iota]], the forward loss, which holds for every γ_C ([[lem:fwd-orders]]), ℓ_tf = 1
([[prop:uc-ltf]]), d_BG = 11 ([[prop:uc-dbg]]) and the free choices of [[def:cs-choices]], of which (a) uses
ϑ_ℋ < ϑ_L + δ with ϑ_L = max(0, 2 − 2a_vγ_Cr_h) < 2 at every γ_C, and (f) the interval (2, 2 + ε_g − 2ε) with
ε_g = ε_Υ; the step of the proof of [[lem:cs-elem]] that uses ε_ind uses ε_ind > ε_K, which holds. So [[prop:cs-cstar]],
[[lem:cs-sharp]] and [[lem:cs-levels]] hold with the same numbers, and so do [[lem:uc-small-orders]] and
[[prop:uc-d-small]], whose orders are fixed by the same counts. The proof of [[thm:uc-integer]] then runs unchanged.
The lower bounds are those of [[prop:ec-rounds]] and [[cor:uc-two-offsets]], which use only ε_K < ε_Υ < 1.46214·10⁻¹⁰
and ε_ind(h) ≤ δ_50 and hold at every h ∈ 𝖧 at which the gauge point is admissible. ∎

#### The exceptional set {#sec:tr-exceptional}

**Proposition {#prop:tr-measure}** (The size of 𝖩.) 𝖩 is a union of finitely many intervals, and its total length is
below 1.698·10⁻¹¹, less than 1.7·10⁻⁵ times the length of [h₁, 10⁻⁶].

*Proof.* For fixed l and n, write 𝖩_B(l, n), 𝖩_P(l, n) and 𝖩_v(l, n) for the three parts of the set of
[[def:tr-exceptional]] (c).

*𝖩_B.* If |ι_B(l, h) − n| < ε_Υ, then |x − (n − 2)| < 0.0101 by [[lem:tr-large]] (a), so 0.98 ≤ x ≤ 49.02 and
κ > (n − 2.0101)·10⁶. The h with |hκ − (n − 2)| ≤ 0.0101 form an interval I, ι_B(l, ·) is continuous there with
∂_hι_B ≥ 0.98κ ([[lem:tr-slopes]] (a)), and outside I, |ι_B − n| > 0.0001 > ε_Υ. So 𝖩_B(l, n) is an interval of length
below 2ε_Υ/(0.98κ). The least l with l(l + 2) > (n − 2.0101)·10⁶ is L_n ≥ 1000(n − 2.0101)^(1/2) − 1 ≥ 994, and
Σ_(l≥L) 1/(l(l + 2)) < 1/L. So the total length of 𝖩_B is below (2ε_Υ/0.98)·1.0011·10⁻³·Σ_(n=3)^(51) (n − 2.0101)^(−1/2),
and the sum is at most 0.9899^(−1/2) + 2(48.9899^(1/2) − 0.9899^(1/2)) < 13.014; so it is below 0.02659ε_Υ.

*𝖩_P.* On {b ≤ 50.2}, which is an interval of h as b² = (24y − (2 + x)² − 16x)/16 decreases in h at fixed l, Re ι_P
lies within ϱ of a ([[lem:tr-large]] (c)); so |Re ι_P − n| < ε_Υ forces |x − x_n| < (4/3)(ϱ + ε_Υ), with
x_n := (4n − 10)/3 ≥ 2/3, whence 1/2 < x ≤ 70 (ϱ = 1/20 for x ≤ 20) and κ ≥ (4n/3 − 3.6001)·10⁶ (ϱ ≤ 1/5). There ∂_h Re ι_P ≥ (2/5)κ ([[lem:tr-slopes]] (b)), so 𝖩_P(l, n) is an
interval of length below 5ε_Υ/κ, and the least l is at least 1000(4n/3 − 3.6001)^(1/2) − 1 ≥ 631. As
Σ_(n=3)^(51)(4n/3 − 3.6001)^(−1/2) ≤ 0.3999^(−1/2) + (3/2)(64.3999^(1/2) − 0.3999^(1/2)) < 12.671, the total length of 𝖩_P is
below 5ε_Υ·1.0016·10⁻³·12.671 < 0.06346ε_Υ.

*𝖩_v.* ι_v(l, ·) increases in h, and |ι_v(l, h) − n| < ε_Υ for some h ≤ 10⁻⁶ forces ι_v(l, 10⁻⁶) > n − ε_Υ, that is
(l + 1)² > (n − 1)² + 10⁶(n − 3) − 10⁻⁴ by the closed form of [[lem:s14-vector-distance]], so l ≥ 1000(n − 3)^(1/2) − 1
≥ 999. By [[lem:tr-slopes]] (c), 𝖩_v(l, n) is an interval of length below 2ε_Υ/(0.99κ), and as
Σ_(n=4)^(51)(n − 3)^(−1/2) ≤ 1 + 2(48^(1/2) − 1) < 12.857, the total length of 𝖩_v is below
(2ε_Υ/0.99)·1.0011·10⁻³·12.857 < 0.02601ε_Υ.

Only finitely many l occur, as κ ≤ 70/h₁ in each case. The total length is below (0.02659 + 0.06346 + 0.02601)ε_Υ <
0.1161ε_Υ < 1.698·10⁻¹¹. ∎

**Proposition {#prop:tr-fail}** (The bound fails near a crossing.) Let h ∈ 𝖧, and suppose that, with this h, (1/100,
1/100) meets the conditions of [[thm:vi-c-2-1]]. If ε_ind(h) < 1.38·10⁻²⁵, every admissible choice of the weights at
(h, 1/100, 1/100) gives d_NM ≥ d_acc > D_acc, with D_acc of [[thm:uc-integer]]. Let h_c := 1/1001992 = 9.98012…·10⁻⁷;
then h_c ∈ 𝖩, ι_v(1000, h_c) = 4, and ε_ind(h) < 1.38·10⁻²⁵ for 0 < |h − h_c| < 1.377·10⁻³¹. So if h_* > h_c, there are
points of 𝖧 arbitrarily close to h_c with ε_ind(h) < 1.38·10⁻²⁵, and [[thm:tr-transfer]] (ii) fails at each of them
at which the gauge point is admissible.

*Proof.* The proof of [[prop:ec-rounds]] uses of its number δ̂ only that ε_g ≤ δ̂, ε_K < δ̂ and 5δ̂ + δ̄ < 2.1·10⁻⁸.
As ε_K < ε_+ < ε_ind ≤ ε_ind(h) and ε_g ≤ ε_ind, it applies with δ̂ := ε_ind(h), and gives
R > (1 − 5δ̂ − δ̄)/δ̂²; so by [[thm:loss-d]] (ii), d_NM ≥ d_acc ≥ 3R > 3(1 − 2.1·10⁻⁸)/(1.38·10⁻²⁵)² > 1.5752·10⁵⁰ >
D_acc. At l = 1000, κ = 1002000 and (n − 3)/((l + 1)² − (n − 1)²) = 1/1001992 at n = 4, so ι_v(1000, h_c) = 4
([[lem:tr-c-v]] (b)) and h_c ∈ 𝖩_v(1000, 4). By [[eq:tr-vslope]], 0 < ∂_hι_v ≤ (l + 1)² = 1002001, so for
0 < |h − h_c| < 1.377·10⁻³¹, 0 < |ι_v(1000, h) − 4| < 1.38·10⁻²⁵, and the entry ι_v − 1 of ℛ^v_1000, of modulus below
50 and not an integer, bounds ε_ind(h). If h_* > h_c, 𝖧 contains all but countably many points of
(h_c − 1.377·10⁻³¹, h_c + 1.377·10⁻³¹) ∩ (0, h_*). ∎

The same holds near every point of 𝖩 at which some ι_B, Re ι_P or ι_v equals an integer n ∈ [3, 51]; the number
1.38·10⁻²⁵ and the bound of [[thm:loss-d]] (ii) make the threshold explicit. For h < 13ε_Υ/40 the condition (H_ε) fails
at every h, through ι₂, and ε_g = ε_ind(h) < 40h/13; the quantities of [[prop:uc-explicit]] that use ε_g then change,
and by the argument just given d_acc > 3(13/40)²(1 − 2.1·10⁻⁸)/h², which exceeds D_acc for h < 4.5·10⁻²⁶.

### Placement

Each item names the place, the old text and the new text. Old and new texts are given as the lines of the chapter
source, unindented, each preceded by a line ending "Old:" or "New:". Line numbers are those of the current chapter
sources and serve only to find the place.

*1. Where the section goes.* The section above, from its heading through the paragraph after [[prop:tr-fail]], is
inserted in [[ch:explicit-constants]] immediately before the heading of [[sec:ec-linear]], "The first constants of the
linear theory" (after the section sec:uc-data-order, if that section has been inserted before it), with one blank
line before and one after. It defines sec:tr, def:tr-exceptional, thm:tr-transfer, rem:tr-scope, sec:tr-split,
lem:tr-split, eq:tr-split, eq:tr-dh, eq:tr-gb, eq:tr-aj, sec:tr-roots, lem:tr-c-v, eq:tr-vslope, lem:tr-small,
eq:tr-p2, lem:tr-large, lem:tr-slopes, sec:tr-inputs, prop:tr-eps, prop:tr-inputs, sec:tr-proof, sec:tr-exceptional,
prop:tr-measure and prop:tr-fail, none of which is defined elsewhere. Its two tables are of the size of those of
[[lem:ec-gauge-gap]] and [[prop:gap-sums]] and stay in the text. No number already printed in any chapter changes.

*2. [[ch:explicit-constants]], its opening paragraph (lines 22–25).* Old:

products ([[def:uc-choice]], [[def:cs-choices]]), d_acc and d_NM, the latter the d of [[thm:iii-k-3-2]], at least the
orders at which its lemmas ask U small ([[prop:uc-d-small]]), are at most an integer below 1.57157 × 10⁵⁰, and N_NM at
most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter point lies outside the set on which [[thm:settling]]
is proved ([[rem:ec-point-outside]]), and the bounds bound what this proof's choices produce, not the optimal loss. The

New:

products ([[def:uc-choice]], [[def:cs-choices]]), d_acc and d_NM, the latter the d of [[thm:iii-k-3-2]], at least the
orders at which its lemmas ask U small ([[prop:uc-d-small]]), are at most an integer below 1.57157 × 10⁵⁰, and N_NM at
most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter point lies outside the set on which [[thm:settling]]
is proved ([[rem:ec-point-outside]]), and the bounds bound what this proof's choices produce, not the optimal loss. The
same bounds hold at every h ∈ 𝖧 ∩ [4.76·10⁻¹¹, 10⁻⁶) outside an explicit set of total length below 1.7·10⁻¹¹, if
(γ_Υ, e_Υ) = (1/100, 1/100) is admissible at that h, and they fail near the excluded values of h ([[thm:tr-transfer]],
[[prop:tr-fail]]); whether such an h exists is not decided ([[rem:tr-scope]]). The

*3. [[rem:ec-point-outside]], its last sentence (lines 55–57).* Old:

at it. For h ∈ 𝖧 the theorems use only 0 < ε_ind(h) ≤ δ_50 ([[prop:np-10-52]] (iii)), and the lower bound of
[[thm:loss-d]] uses besides only ε_Υ < 1.46214·10⁻¹⁰, which holds at every h, ε_Υ being fixed by (γ_Υ, e_Υ)
([[lem:ec-gauge-gap]], [[prop:ec-rounds]]).

New:

at it. For h ∈ 𝖧 the theorems use only 0 < ε_ind(h) ≤ δ_50 ([[prop:np-10-52]] (iii)), and the lower bound of
[[thm:loss-d]] uses besides only ε_Υ < 1.46214·10⁻¹⁰, which holds at every h, ε_Υ being fixed by (γ_Υ, e_Υ)
([[lem:ec-gauge-gap]], [[prop:ec-rounds]]). [[thm:tr-transfer]] moves the upper bounds to h ∈ 𝖧 ∩ [h₁, 10⁻⁶),
h₁ = 4.76·10⁻¹¹, outside a set 𝖩 of total length below 1.7·10⁻¹¹, under the same condition on (γ_Υ, e_Υ); for every
h ∈ (0, 10⁻⁶], ε_ind(h) < 40h/13 ([[prop:tr-eps]]).

*4. [[ch:theorems]], the list of further results (lines 353–354).* Old:

  parameter point that lies outside the proved set ([[thm:loss-d]]) and, there, explicit upper bounds for d and N_NM
  at one admissible choice of the weights, orders and inner products ([[thm:uc-integer]]); through the lower bounds,

New:

  parameter point that lies outside the proved set ([[thm:loss-d]]) and, there, explicit upper bounds for d and N_NM
  at one admissible choice of the weights, orders and inner products ([[thm:uc-integer]]), which hold at the same
  gauge parameters for h ∈ 𝖧 ∩ [4.76·10⁻¹¹, 10⁻⁶) outside a set of length below 1.7·10⁻¹¹ if those gauge parameters
  are admissible there, a condition not decided ([[thm:tr-transfer]]); through the lower bounds,

*5. [[ch:scope]], [[sec:scope-constants]] (line 74; the item that inserts the order of the approximant after line 72
leaves this line as it is).* Old:

[[thm:settling]] is proved ([[rem:ec-point-outside]]). No result of [[ch:explicit-constants]] is used in the proof of any

New (the paragraph may be refilled):

[[thm:settling]] is proved ([[rem:ec-point-outside]]). The upper bounds hold with the same numbers at the points
(h, 1/100, 1/100) with h ∈ 𝖧 ∩ [4.76·10⁻¹¹, 10⁻⁶) outside a set 𝖩 of total length below 1.7·10⁻¹¹, provided the
gauge values 1/100 are admissible at h; this conditional statement may be empty, as h_* and the gauge thresholds are not
determined, and near the points of 𝖩 the bounds fail ([[thm:tr-transfer]], [[rem:tr-scope]], [[prop:tr-fail]]). No
result of [[ch:explicit-constants]] is used in the proof of any

*6. Unchanged.* [[def:ec-point]], [[thm:uc-integer]] and every statement at the computational point keep their texts
and numbers; [[cor:s14-eps-ind-point]] and [[rem:s14-eps-ind-scope]] stand, h = 10⁻⁶ being the point at which the
enclosures of [[ch:s14]] are made. No result of the new section is used outside [[ch:explicit-constants]].

### Crosswalk rows

New rows for the crosswalk table of [[ch:explicit-constants]], one per label, each given as its four fields (label;
location in this file; name; note), to be written with tab separators:

Row 1. sec:tr; paper/reader/proofs/P-TR.md:1; transfer proof P-TR, section heading; new section, inserted before
sec:ec-linear.

Row 2. def:tr-exceptional; paper/reader/proofs/P-TR.md:LDEF; transfer proof P-TR, Definition (The condition (H_ε) and
the set 𝖩.); new: (H_ε) is dist ≥ ε_Υ for all h-dependent roots with |ι − 1| ≤ 50; 𝖩 the crossings of ι_B, Re ι_P,
ι_v with n ∈ [3, 51] within ε_Υ.

Row 3. thm:tr-transfer; paper/reader/proofs/P-TR.md:LTHM; transfer proof P-TR, Theorem (The bounds of thm:uc-integer
at other values of h.); new conditional transfer: h ∈ 𝖧 ∩ [4.76·10⁻¹¹, 10⁻⁶) ∖ 𝖩, gauge point admissible, all
numbers of thm:uc-integer unchanged.

Row 4. rem:tr-scope; paper/reader/proofs/P-TR.md:LREM; transfer proof P-TR, Remark (What the theorem assumes.); the
hypothesis may be empty (h_* unknown, gauge thresholds undecided); 13ε_Υ/40 the least h for (H_ε).

Row 5. sec:tr-split; paper/reader/proofs/P-TR.md:LSPLIT; transfer proof P-TR, subsection heading; new.

Row 6. lem:tr-split; paper/reader/proofs/P-TR.md:LLSPLIT; transfer proof P-TR, Lemma (The sextic and its derivative
in h.); P_l = U + eF from lem:s14-sextic-split at ε₀ = e/h, F_k = ϖR_k; ∂_hP_l at fixed l; F(2 + x) and F₁(a + s).

Row 7. eq:tr-split; paper/reader/proofs/P-TR.md:LEQ1; transfer proof P-TR, display; P_l = U + eF.

Row 8. eq:tr-dh; paper/reader/proofs/P-TR.md:LEQ2; transfer proof P-TR, display; the h-derivative of P_l.

Row 9. eq:tr-gb; paper/reader/proofs/P-TR.md:LEQ3; transfer proof P-TR, display; 𝒬 and F at 2 + x.

Row 10. eq:tr-aj; paper/reader/proofs/P-TR.md:LEQ4; transfer proof P-TR, display; F₁ expanded about a.

Row 11. sec:tr-roots; paper/reader/proofs/P-TR.md:LROOTS; transfer proof P-TR, subsection heading; new.

Row 12. lem:tr-c-v; paper/reader/proofs/P-TR.md:LCV; transfer proof P-TR, Lemma (The scalar type 0 and the vector
type.); ι₁ ∈ (2 + 7·10⁻⁵, 5/2) and ι_v at every h ∈ (0, 10⁻⁶], with its crossings and slope.

Row 13. eq:tr-vslope; paper/reader/proofs/P-TR.md:LEQ5; transfer proof P-TR, display; ∂_hι_v.

Row 14. lem:tr-small; paper/reader/proofs/P-TR.md:LSMALL; transfer proof P-TR, Lemma (The degrees with y ≤ 3/20.);
two-parameter form of lem:s14-sextic-small for l ≤ 122 and every h ∈ (0, 10⁻⁶]; ι₂ − 2 ∈ ((40/13 − 153600h)h,
40h/13).

Row 15. eq:tr-p2; paper/reader/proofs/P-TR.md:LEQ6; transfer proof P-TR, display; P_2(2 + τh).

Row 16. lem:tr-large; paper/reader/proofs/P-TR.md:LLARGE; transfer proof P-TR, Lemma (The degrees with y ≥ 3/20.);
two-parameter form of lem:s14-sextic-large and lem:s14-sextic-count (b): Rouché discs about 2 + x, a and ζ, with two
tables.

Row 17. lem:tr-slopes; paper/reader/proofs/P-TR.md:LSLOPES; transfer proof P-TR, Lemma (The roots move fast at the
integers.); ∂_hι_B ≥ 0.98κ, ∂_h Re ι_P ≥ 2κ/5, ∂_hι_v ≥ 0.99κ.

Row 18. sec:tr-inputs; paper/reader/proofs/P-TR.md:LINPUTS; transfer proof P-TR, subsection heading; new.

Row 19. prop:tr-eps; paper/reader/proofs/P-TR.md:LEPS; transfer proof P-TR, Proposition (The number ε_ind(h).);
ε_ind(h) < min(δ_50, 40h/13) for every h; (H_ε) off 𝖩 on [h₁, 10⁻⁶]; none below 13ε_Υ/40.

Row 20. prop:tr-inputs; paper/reader/proofs/P-TR.md:LINP; transfer proof P-TR, Proposition (The other three inputs.);
prop:is-iota, prop:is-logs (c), prop:is-mult, lem:sp-roots, thm:sp-spectrum (b) and cor:sp-lstar at h.

Row 21. sec:tr-proof; paper/reader/proofs/P-TR.md:LPROOF; transfer proof P-TR, subsection heading; new.

Row 22. sec:tr-exceptional; paper/reader/proofs/P-TR.md:LEXC; transfer proof P-TR, subsection heading; new.

Row 23. prop:tr-measure; paper/reader/proofs/P-TR.md:LMEAS; transfer proof P-TR, Proposition (The size of 𝖩.);
total length below 1.7·10⁻¹¹.

Row 24. prop:tr-fail; paper/reader/proofs/P-TR.md:LFAIL; transfer proof P-TR, Proposition (The bound fails near a
crossing.); d_acc > D_acc when ε_ind(h) < 1.38·10⁻²⁵; h_c = 1/1001992.

Notes for existing rows: ch:explicit-constants (opening states the transfer, text 2); rem:ec-point-outside (text 3); in
the crosswalk table of [[ch:theorems]], the list of further results (text 4); in that of [[ch:scope]], the paragraph on
the constants (text 5).
