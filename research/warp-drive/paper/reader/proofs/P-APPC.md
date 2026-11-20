## Appendix C. The certified approximant {#app:approximant}

This appendix defines the explicit metric ĝ that serves as the background of the continuation argument of
[[sec:tl5-beyond]], fixes the format in which its coefficients are printed in the part "Tables of the approximant"
after the references, states and proves the procedure by which its residual is bounded from the printed numbers alone,
and records the bounds obtained. A reader who has the printed integers, the formulas of [[ch:ten-l5]] and of this
appendix, and any arithmetic of intervals with exact rational end points can repeat every step.

The metric is defined at each seed of [[def:tl5-seeds]] on one of two regions,

    D_A := [−10, −2] × [1/2, 7/2],      D* := [−10, −11/10] × [1/2, 7/2],                              {#eq:appc-regions}

in the coordinates (u, v), times S³. The four cases are named by the seed and the region: (1, D_A), (2, D_A), (2, D*) and
(1, D*). Everything below is stated for a case; the seed enters only through the printed integers and the targets.

### The printed approximant {#sec:appc-definition}

We use the chart of [[def:tl5-chart]] in the u-direction, ξ := arsinh((u + 1)/a) with a = 1/500, and v itself. The
region D_A is [ξ₀, ξ_A] × [1/2, 7/2] in (ξ, v), with ξ₀ := −arsinh 4500 and ξ_A := −arsinh 500, and D* is
[ξ₀, ξ*] × [1/2, 7/2] with ξ* := −arsinh 50; here ξ₀ = −9.10498…, ξ_A = −6.90776… and ξ* = −4.60527….

**Definition {#def:appc-layout}** (Elements.) A layout consists of integers n_ξ, n_v ≥ 1, rational numbers
c₁ < … < c_(n_ξ−1) and d > 0 (the breakpoints in ξ and the half-width of their transitions), rational numbers
c′₁ < … < c′_(n_v−1) and d′ > 0 (the same in v), and for every i ≤ n_ξ and j ≤ n_v rational numbers m_i, h_i, m′_j,
h′_j > 0. Element (i, j) is the box

    B_ij := [m_i − h_i, m_i + h_i] × [m′_j − h′_j, m′_j + h′_j]   in (ξ, v),
    t := (ξ − m_i)/h_i,   σ := (v − m′_j)/h′_j,                                                        {#eq:appc-element}

so that (t, σ) ∈ [−1, 1]² on B_ij. With c₀ − d := ξ₀ and c_(n_ξ) + d the upper end of the region in ξ, and likewise
c′₀ − d′ := 1/2 and c′_(n_v) + d′ := 7/2, the use interval of the element is

    U_ij := [c_(i−1) − d, c_i + d] × [c′_(j−1) − d′, c′_j + d′].

The layout is admissible if c_i + d < c_(i+1) − d and c′_j + d′ < c′_(j+1) − d′ for all i and j, and if U_ij lies in
[m_i − (9/10)h_i, m_i + (9/10)h_i] × [m′_j − (9/10)h′_j, m′_j + (9/10)h′_j] for every element.

So each element is used only on the inner nine tenths of its box in t and σ.

**Definition {#def:appc-layouts}** (The four layouts.) In every case n_v = 2, c′₁ = 2, d′ = 3/80, and the v-boxes are
[829/2000, 21231/10000] and [18769/10000, 7171/2000] (m′ = 793/625 and 1707/625, h′ = 8543/10000). The ξ-parameters
are:

    case        n_ξ   breakpoints c_i     d        ξ-boxes [m_i − h_i, m_i + h_i]
    (1, D_A)    2     −801/100            11/200   [−9169/1000, −7891/1000], [−813/100, −3421/500]
    (2, D_A)    2     −801/100            11/200   [−9169/1000, −7891/1000], [−813/100, −3421/500]
    (2, D*)     2     −343/50             14/125   [−2309/250, −827/125], [−1421/200, −4473/1000]
    (1, D*)     3     −761/100, −611/100  3/40     [−9193/1000, −7447/1000], [−7777/1000, −5943/1000],
                                                   [−6273/1000, −4517/1000]

In u the ξ-boxes of D_A are [−10.595, −3.673] and [−4.395, −1.936] to three decimals; those of the second seed on D*
are [−11.260, −1.747] and [−2.218, −1.088], and those of the first seed on D* are [−10.828, −2.715],
[−3.385, −1.381] and [−1.530, −1.092]. The boxes extend beyond the region by at most one twentieth of their length on
each side, and the approximant is only required to be small in the region. Each layout is admissible, as the numbers
show.

**Definition {#def:appc-pou}** (The partition of unity.) Let

    Φ(s) := 0 for s ≤ 0,   Φ(s) := e^(−1/s)/(e^(−1/s) + e^(−1/(1−s))) for 0 < s < 1,   Φ(s) := 1 for s ≥ 1,

and for a layout put Φ_i(ξ) := Φ((ξ − c_i + d)/(2d)) for 1 ≤ i ≤ n_ξ − 1, Φ₀ := 1 and Φ_(n_ξ) := 0, and

    χ_i := Φ_(i−1) − Φ_i  (1 ≤ i ≤ n_ξ),      ψ_j := Φ′_(j−1) − Φ′_j  (1 ≤ j ≤ n_v),                   {#eq:appc-pou}

where Φ′_j(v) := Φ((v − c′_j + d′)/(2d′)), Φ′₀ := 1 and Φ′_(n_v) := 0.

**Lemma {#lem:appc-pou}** (Properties of the partition.) (a) Φ is smooth on ℝ, 0 ≤ Φ ≤ 1, Φ(s) + Φ(1 − s) = 1, and
sup |Φ^(k)| ≤ φ_k with (φ₀, …, φ₆) = (1, 2, 9.853, 111.3, 2345, 8.527 × 10⁴, 7.565 × 10⁶). (b) For an admissible
layout the χ_i and ψ_j are smooth, nonnegative, Σ_i χ_i = 1 and Σ_j ψ_j = 1; χ_i vanishes outside [c_(i−1) − d,
c_i + d], equals 1 on [c_(i−1) + d, c_i − d], and on [c_i − d, c_i + d] the only nonzero ones are χ_i = 1 − Φ_i and
χ_(i+1) = Φ_i. The same holds for the ψ_j.

*Proof.* (a) e^(−1/s) is smooth on ℝ when extended by 0 for s ≤ 0, with all derivatives vanishing at 0; the
denominator is positive on ℝ since the two terms do not vanish together; so Φ is smooth, and the stated values outside
(0, 1) agree with the formula's limits. The symmetry is immediate from the formula. For the bounds, by the symmetry it
suffices to take s ∈ (0, 1/2]. On [1/100, 1/2], cover the interval by 20,000 equal closed intervals and enclose the
Taylor coefficients of order at most 6 of Φ on each by the rules of [[def:tl5-jets]] (series of order 6), the
exponential and the reciprocal being applied to series whose constant term is an interval; the largest end points,
times k!, are at most φ_k. On (0, 1/100] use Cauchy's estimate on the disc |z − s| ≤ s/2: there Re(1/z) ≥ 2/(3s),
since inversion maps the disc onto the disc with diameter [2/(3s), 2/s], and Re(1/(1 − z)) ≤ 1/(1 − 3s/2),
so |Φ(z)| ≤ e^(−2/(3s))/(e^(−1/(1−3/200)) − e^(−2/(3s))) and |Φ^(k)(s)| ≤ k!(2/s)^k sup |Φ|, which at s = 1/100 is far
below φ_k and increases in s on (0, 1/100]. (b) The Φ_i are nonincreasing in i at each point, because the transitions
are disjoint by admissibility, and the sums telescope. The supports follow from those of the Φ_i. ∎

**Definition {#def:appc-approximant}** (The printed approximant.) For each element (i, j) and each F ∈ {R, m, n, W, s}
the tables give an integer p = p_(ij,F) and integers z_abk = z^(ij,F)_abk for (a, b, k) in a finite set I_(ij,F) of
triples of nonnegative integers. Put

    G^F_ij(t, σ, x) := Σ_((a,b,k) ∈ I_(ij,F)) z_abk 10^(−p) T_a(t) T_b(σ) T_k(x)                        {#eq:appc-fields}

with t and σ the variables of [[eq:appc-element]] on B_ij, and

    R := R_s + (v − 1/2)^κ Σ_ij χ_i ψ_j G^R_ij,      W := W_s + (v − 1/2)^κ Σ_ij χ_i ψ_j G^W_ij,
    F := (v − 1/2)^κ Σ_ij χ_i ψ_j G^F_ij   (F ∈ {m, n, s}),                                            {#eq:appc-seedform}

where R_s and W_s are the seed's R and W of [[lem:tl5-seed]] and κ = 4 is the order of contact with the seed on N₀
([[rem:appc-contact]]). The approximant ĝ of the case is the metric
[[eq:tl5-metric]] with these fields, P := (2(1 + x)m − (1 − x)n)/3, Q := (2(1 − x)n − (1 + x)m)/3 and b = (1 − x²)s.

Each term of the sum is defined where χ_iψ_j ≠ 0, which is inside B_ij by [[lem:appc-pou]] (b), so the fields are
defined on the region and on a neighbourhood of it in the union of the boxes.

**Lemma {#lem:appc-approximant}** (Properties of ĝ.) Let ĝ be the printed approximant of a case, and suppose R > 0 on
an open set 𝒪 ⊂ ⋃ B_ij containing the region. Then:

(a) ĝ is a smooth Lorentzian metric of the class on 𝒪 × S³, in double-null form, invariant under the T² action and
under the reflections φ1 ↦ −φ1 and φ2 ↦ −φ2;

(b) on N₀ = {v = 1/2}, each of the five fields and its partial derivatives of all orders in u and x, and of order at
most κ − 1 in v, take the values of the seed: R − R_s, W − W_s, m, n and s vanish to order κ at v = 1/2;

(c) the coefficients are exact rational numbers, and ĝ and all its derivatives are given by finitely many arithmetic
operations, exponentials and the seed's R_s from these numbers.

*Proof.* (a) The fields are smooth on 𝒪, since the seed's are ([[lem:tl5-seed]] (b)), the polynomials are, and so
are χ_i, ψ_j and the chart. The metric of the class with smooth fields and R > 0 is smooth on 𝒪 × S³, axes included,
because 2P + Q = (1 + x)m and P + 2Q = (1 − x)n vanish at x = −1 and x = 1 and b = (1 − x²)s
([[pending:lem-tl5-cip-axis]]); its form is the double-null form, and the invariances hold for every metric of the
class. (b) Each correction is (v − 1/2)^κ times a smooth function, and m, n, s vanish for the seed. (c) is the
definition. ∎

The form [[eq:appc-seedform]] makes the agreement with the seed's (κ − 1)-jet on N₀ exact, whatever the printed integers.

**Remark {#rem:appc-contact}** (The order of contact on N₀.) The integer κ ≥ 1 is a parameter of the definition: for
every κ the approximant agrees with the seed on N₀ to order κ − 1 in v, whatever the printed integers. The tables are
printed for κ = 4. A contact of higher order with a metric other than the seed, as a hypothesis on N₀ may require,
needs a reference part in place of R_s, W_s and the zero functions in [[eq:appc-seedform]] that carries that metric's
v-derivatives on N₀ of the orders between 4 and κ − 1.

### The format of the tables and their checks {#sec:appc-format}

The tables of a case consist of one block for each element (i, j), taken in the order of i and then j, and each field
in the order R, m, n, W, s. A block begins with two header lines:

    element (i, j): ξ in [m_i − h_i, m_i + h_i], v in [m′_j − h′_j, m′_j + h′_j]; field F; p = p; rows r; entries e;
    S1 = S₁,  S2 = S₂,  S0 = S₀

where r is the number of rows, e the number of printed integers, and S₁, S₂, S₀ are the integers

    S₁ := Σ z_abk = 10^p G(1, 1, 1),      S₂ := Σ (−1)^(a+b+k) z_abk = 10^p G(−1, −1, −1),
    S₀ := Σ_(a, b, k even) (−1)^((a+b+k)/2) z_abk = 10^p G(0, 0, 0),                                      {#eq:appc-sums}

the identities holding because T_n(1) = 1, T_n(−1) = (−1)^n and T_n(0) = cos(nπ/2). Then come the rows. Row (a, b)
lists z_ab0, z_ab1, …, z_abK in order of k, where K = K(a, b) is the largest k with (a, b, k) ∈ I and z_abK ≠ 0;
the entries with k ≤ K that are not in I are printed as 0, rows without a nonzero entry are omitted, and the rows come
in the order of a and then b. So I is determined by the row labels and the row lengths. A row begins with its label
"(a,b)", padded to eight characters; when it does not fit on one line of 121 characters it continues on lines
beginning with "+". An entry is a decimal integer without leading zeros, preceded by "−" when negative. Every line
ends with " |cc", where cc, two digits, is the check of the line:

    cc := (Σ_m m z_m) mod 97,                                                                        {#eq:appc-linecheck}

the sum over the integers z₁, z₂, … printed on that line, in order.

**Lemma {#lem:appc-checks}** (What the checks detect.) (a) If one digit of one entry of a line is changed, or two
adjacent digits of one entry are interchanged, the line check fails. (b) If the sign of one entry z of a line is
changed, the line check fails unless 97 divides z. (c) If two entries z_m, z_m′ of a line are interchanged, the line
check fails unless z_m ≡ z_m′ (mod 97). (d) An error that leaves every line check valid changes S₁, S₂ or S₀ unless
the printed field takes the same values at the three points (1, 1, 1), (−1, −1, −1) and (0, 0, 0) as the correct one,
and a misplaced or omitted line changes the entry count.

*Proof.* A line holds at most 30 entries, so 1 ≤ m ≤ 30 < 97. (a) Changing the digit of weight 10^r of z_m by
δ ∈ {±1, …, ±9} changes the sum by mδ10^r, and interchanging the digits d, d′ of weights 10^(r+1), 10^r changes z_m by
9(d − d′)10^r; since 97 is prime and divides none of m, δ, 9(d − d′) ≠ 0 and 10^r, neither change is 0 mod 97. (b) The
change is −2mz, and 97 ∤ 2m. (c) The change is (m − m′)(z_m′ − z_m) and 97 ∤ m − m′. (d) is [[eq:appc-sums]]. ∎

Within a row the entries decrease in size roughly geometrically in k, so the number of digits falls roughly linearly
along a row; a long entry where short ones are expected is a transcription error that the eye catches without
arithmetic.

### The residual in a form regular at the axes {#sec:appc-regular}

The formula of [[sec:tl5-formula]] contains 1/(1 + x), 1/(1 − x), x/w and (1 + x²)/w² with w = (1 + x)(1 − x), and the
factor μ = e^(−ζ) = 2√w e^S/R ([[eq:tl5-derivatives]]); the components are bounded at the axes, but the individual
terms are not. An enclosure that reaches x = ±1 needs the cancellations made explicit. We write them out.

For ψ ∈ {ζ, A, B} and every index a ∈ {u, v, x, uu, uv, vv, ux, vx, xx} let ψ°_a be ψ_a of [[eq:tl5-derivatives]] with
the terms x/w, 1/(2(1 + x)), −1/(2(1 − x)), (1 + x²)/w², −1/(2(1 + x)²) and −1/(2(1 − x)²) omitted:

    ζ°_a := ℓ_a − S_a,   A°_a := ℓ_a + P_a,   B°_a := ℓ_a + Q_a     (ℓ_a or ℓ_ab as in [[eq:tl5-derivatives]]).

So ψ_a = ψ°_a for a ≠ x, xx. Put

    ζ̌ := wζ°_x + x,   Ǎ := wA°_x + (1 − x)/2,   B̌ := wB°_x − (1 + x)/2,
    ζ̌₂ := w²ζ°_xx + 1 + x²,   Ǎ₂ := w²A°_xx − (1 − x)²/2,   B̌₂ := w²B°_xx − (1 + x)²/2,              {#eq:appc-checked}

which are wψ_x and w²ψ_xx, and

    μ̂ := 2e^S/R,   τ̂ := R s_v/(8e^S Ω²),   η̂ := μ̂ W_x,   λ := ℓ_x + 2S_x,
    α₁ := (1 + x)A°_x + 1/2,   β₁ := (1 − x)B°_x − 1/2,                                                  {#eq:appc-hat}

so that μ = √w μ̂, τ = √w τ̂ and η = √w η̂. Define further

    Σ_EE := w(A°_xx + B°_xx + A°_xA°_x + B°_xB°_x − ζ°_x(A°_x + B°_x)) + (1 − 2x)A°_x − (1 + 2x)B°_x + xζ°_x − 1/2,
    Σ₁₁ := w(A°_xx + A°_x λ) − 2xA°_x + ((1 − x)/2)λ − 1/2,
    Σ₂₂ := w(B°_xx + B°_x λ) − 2xB°_x − ((1 + x)/2)λ − 1/2,
    Θ_A := w(A°_x(A°_x − ζ°_x) + A°_xx) + ((1 − x)/2)(A°_x − ζ°_x) + ((1 − 3x)/2)A°_x − 1/4,
    Θ_B := w(B°_x(B°_x − ζ°_x) + B°_xx) − ((1 + x)/2)(B°_x − ζ°_x) − ((1 + 3x)/2)B°_x − 1/4.          {#eq:appc-sigma}

**Lemma {#lem:appc-regular}** (The residual regular at the axes.) For every metric of the class with C² fields and
R > 0, at every point with |x| < 1, the eight components of [[eq:tl5-components]] are

    f_ll = ρ N(L, L),   f_ln = ρ N(L, Y)/(2Ω²),   f_nn = ρ N(Y, Y)/(4Ω⁴),
    f_lx = ρ √w (−L̂η + L̂τ + 2kτ̂ − Σ_LE),   f_nx = ρ √w (−Ŷη − Ŷτ − 2k̲τ̂ − Σ_YE)/(2Ω²),
    f_xx = ρ (Ric(E, E) − h°_A − h°_B − μ̂²Σ_EE),
    f_11 = −ρ (□°A + ⟨dA, dA⟩° + ⟨dA, dB⟩° + μ̂²Σ₁₁),   f_22 = −ρ (□°B + ⟨dB, dB⟩° + ⟨dA, dB⟩° + μ̂²Σ₂₂),
                                                                                                       {#eq:appc-regular}

where N(X, Z) := Ric(X, Z) − M_A(X, Z) − M_B(X, Z) for XZ ∈ {LL, YY, LY}, and all quantities are the following
polynomials in x, in the values and first and second derivatives of R, m, n, W, s, and in 1/R, e^(±S) and 1/Ω²:

    Y(ζ) := ζ°_u + sζ̌,   ω := W_v,   ω̲ := W_u + bW_x,   k := ζ°_v,   k̲ := ζ°_u + sζ̌ + b_x,
    L(k̲) := ζ°_uv + s_vζ̌ + bζ°_vx + b_vx,   Y(k) := ζ°_uv + bζ°_vx,   L(ω̲) := W_uv + b_vW_x + bW_vx,
    Y(k̲) := ζ°_uu + s_uζ̌ + 2bζ°_ux + b_ux + s b_x ζ̌ + s²ζ̌₂ + b b_xx,
    L̂η := μ̂(W_vx − ζ°_vW_x),   Ŷη := μ̂(W_ux + bW_xx − Y(ζ)W_x),   E(η) := μ̂²(wW_xx − ζ̌W_x),
    L̂τ := τ̂(ζ°_v − 2ω) + R s_vv/(8e^S Ω²),   Ŷτ := τ̂(Y(ζ) − 2ω̲) + R (s_uv + s(ws_vx − 2xs_v))/(8e^S Ω²),
    E(τ) := μ̂τ̂(ζ̌ − 2wW_x) + b_vx/(4Ω²),
    Ric(L, L) := −ζ°_vv + 2ωk − kk,   Ric(Y, Y) := −Y(k̲) + 2ω̲k̲ − k̲k̲,
    Ric(L, Y) := −L(k̲) − 2L(ω̲) − kk̲ + Ω²(2E(η) + 2E(τ) + w(4η̂η̂ + 8η̂τ̂ − 4τ̂τ̂)),
    Ric(E, E) := −2E(η) − 2w(η̂η̂ + τ̂τ̂) + (L(k̲) + Y(k) + 2kk̲)/(2Ω²),

and, for ψ ∈ {A, B} with ψ̌ and ψ̌₂ from [[eq:appc-checked]],

    ψ_L := ψ°_v,   ψ_Y := ψ°_u + sψ̌,   L(ψ_Y) := ψ°_uv + s_vψ̌ + bψ°_vx,
    Y(ψ_Y) := ψ°_uu + s_uψ̌ + 2bψ°_ux + s b_x ψ̌ + s²ψ̌₂,   h_ψ(L, Y) := L(ψ_Y) − 2Ω²(η̂ + τ̂)μ̂ψ̌,
    M_ψ(L, L) := ψ°_vv − 2ωψ_L + ψ_Lψ_L,   M_ψ(Y, Y) := Y(ψ_Y) − 2ω̲ψ_Y + ψ_Yψ_Y,
    M_ψ(L, Y) := h_ψ(L, Y) + ψ_Lψ_Y,   h°_ψ := −(k̲ψ_L + kψ_Y)/(2Ω²),
    □°ψ := −h_ψ(L, Y)/Ω² + h°_ψ,   ⟨dψ, dχ⟩° := −(ψ_Lχ_Y + ψ_Yχ_L)/(2Ω²),
    Σ_LE := μ̂(A°_vx + B°_vx + α₁m_v + β₁n_v) − (η̂ + τ̂)(A°_v + B°_v),
    Σ_YE := μ̂(A°_ux + B°_ux + α₁m_u + β₁n_u + s(Θ_A + Θ_B)) − (η̂ − τ̂)(A_Y + B_Y).

In particular every f_ab, and f_lx/√w and f_nx/√w, extends continuously to x = ±1, by these expressions; the only
divisions in them are by R, Ω², e^S and the integers 2, 3, 4 and 8.

*Proof.* Write ψ = ψ° + σ_ψ with σ_ζ := −(1/2) log(4w), σ_A := (1/2) log((1 + x)/2) and σ_B := (1/2) log((1 − x)/2),
which depend on x alone. Their derivatives are σ′_ζ = x/w, σ″_ζ = (1 + x²)/w², σ′_A = 1/(2(1 + x)),
σ″_A = −1/(2(1 + x)²), σ′_B = −1/(2(1 − x)) and σ″_B = −1/(2(1 − x)²), the omitted terms above; so ψ_x = ψ°_x + σ′_ψ,
ψ_xx = ψ°_xx + σ″_ψ, and [[eq:appc-checked]] states wσ′_ζ = x, wσ′_A = (1 − x)/2, wσ′_B = −(1 + x)/2, w²σ″_ζ = 1 + x²,
w²σ″_A = −(1 − x)²/2 and w²σ″_B = −(1 + x)²/2. Six further identities are checked by putting each over the common
denominator 4w and expanding: with σ′_A + σ′_B − σ′_ζ = −2x/w,

    w(σ″_A + σ′_A(σ′_A + σ′_B − σ′_ζ)) = −1/2 = w(σ″_B + σ′_B(σ′_A + σ′_B − σ′_ζ)),
    w(σ″_A + σ″_B + σ′_Aσ′_A + σ′_Bσ′_B − σ′_ζ(σ′_A + σ′_B)) = −1/2,
    w(σ″_A + σ′_A(σ′_A − σ′_ζ)) = −1/4 = w(σ″_B + σ′_B(σ′_B − σ′_ζ)),
    (1 + x)σ′_A = 1/2,   (1 − x)σ′_B = −1/2.                                                            {#eq:appc-sing}

For instance the first reads −(1 − x)/(2(1 + x)) − x/(1 + x) = −1/2. Finally, by the definitions of S, P and Q,
A°_a − ζ°_a = P_a + S_a = (2P + Q)_a = ((1 + x)m)_a and B°_a − ζ°_a = ((1 − x)n)_a, so that

    A°_v − ζ°_v = (1 + x)m_v,   B°_v − ζ°_v = (1 − x)n_v,   A°_u − ζ°_u = (1 + x)m_u,   B°_u − ζ°_u = (1 − x)n_u.

Take the chapter's formula ([[eq:tl5-components]], [[eq:tl5-derivatives]], [[eq:tl5-frame-derivatives]] and the
lines after it) term by term. A first derivative ψ_x occurs multiplied by b, b_u, b_v or b·b_x, which carry the factor
w, so bψ_x = sψ̌, b_uψ_x = s_uψ̌, b_vψ_x = s_vψ̌ and b b_xψ_x = s b_xψ̌; ψ_xx occurs only as b²ψ_xx = s²ψ̌₂, and in
the factors E(ψ_E) = μ²(ψ_xx − ζ_xψ_x), μ²ψ_x and μ ψ_x treated below. With μ = √w μ̂, ϑ = e^(ζ−2W)/4 = 1/(4√w μ̂Ω²)
and b_v = ws_v one has τ = ϑb_v = √w τ̂, η = μW_x = √w η̂, and ϑb_vv, ϑ(b_uv + bb_vx) and μ(τ(ζ_x − 2W_x) + ϑb_vx)
equal √w R s_vv/(8e^S Ω²), √w R(s_uv + s(ws_vx − 2xs_v))/(8e^SΩ²) and E(τ) as defined. This gives every quantity
of [[eq:tl5-ricci3]] in the stated form: L(η) = √w L̂η, Y(η) = √w Ŷη, L(τ) = √w L̂τ, Y(τ) = √w Ŷτ, and E(η), E(τ),
η², ητ, τ² = w(·) as written, so that Ric[g3](L, E) = √w(−L̂η + L̂τ + 2kτ̂) and Ric[g3](Y, E) = √w(−Ŷη − Ŷτ − 2k̲τ̂).

It remains to treat the terms with ψ_E = μψ_x and with E(ψ_E) in M_ψ and ⟨dψ, dχ⟩. In h_ψ(L, Y) the term
2Ω²(η + τ)ψ_E = 2Ω²(η̂ + τ̂)μ̂ wψ_x = 2Ω²(η̂ + τ̂)μ̂ψ̌. The terms μ²ψ_xχ_x of M_ψ(E, E), □ψ and ⟨dψ, dχ⟩ combine with
μ²(ψ_xx − ζ_xψ_x) as follows. In N(E, E) they give −μ̂²w(A_xx + B_xx + A_xA_x + B_xB_x − ζ_x(A_x + B_x)); in f_11
they give −μ̂²w(A_xx + A_x(A_x + B_x − ζ_x)), and in f_22 the same with A and B interchanged, where
A_x + B_x − ζ_x = λ + σ′_A + σ′_B − σ′_ζ because A° + B° − ζ° = log R + 2S. Expanding each with ψ_x = ψ°_x + σ′_ψ
and ψ_xx = ψ°_xx + σ″_ψ, the products of two regular parts and the terms ψ°_x · wσ′_χ are polynomials, and the purely
singular parts are the left sides of [[eq:appc-sing]]; collecting gives w times these brackets equal to Σ_EE, Σ₁₁ and
Σ₂₂. For example w(A_xx + A_x(A_x + B_x − ζ_x)) = w(A°_xx + A°_xλ) + A°_x · w(−2x/w) + wσ′_A λ + w(σ″_A +
σ′_A(−2x/w)) = Σ₁₁ by the first identity of [[eq:appc-sing]]. Next, M_A(L, E) + M_B(L, E) = Σ_ψ (L(ψ_E) −
(η + τ)ψ_L + ψ_Lψ_E) = √w Σ_ψ (μ̂(ψ°_vx + ψ_x(ψ°_v − ζ°_v)) − (η̂ + τ̂)ψ°_v), and with the last display and the fifth and
sixth identities of [[eq:appc-sing]], ψ_x(ψ°_v − ζ°_v) is α₁m_v for ψ = A and β₁n_v for ψ = B; this is √w Σ_LE.
Likewise M_A(Y, E) + M_B(Y, E) = √w Σ_ψ (μ̂(ψ°_ux + bψ_xx + ψ_x(ψ_Y − Y(ζ))) − (η̂ − τ̂)ψ_Y), and with
ψ_Y − Y(ζ) = (ψ°_u − ζ°_u) + s(ψ̌ − ζ̌) one gets μ̂(ψ°_ux + ψ_x(ψ°_u − ζ°_u)) + μ̂ s w(ψ_xx + ψ_x(ψ_x − ζ_x)), where
the first is μ̂(A°_ux + α₁m_u) or μ̂(B°_ux + β₁n_u) and the second is μ̂sΘ_ψ by the third and fourth identities of
[[eq:appc-sing]]; this is √w Σ_YE. Substituting in [[eq:tl5-components]], with l = L, n̂ = Y/(2Ω²) and e_x = E,
gives [[eq:appc-regular]]. Every quantity in it is a polynomial in x and the jets, divided at most by R, Ω², e^S and
the integers named, so it is defined and continuous at x = ±1; since the left sides are continuous on the metric's
domain, axes included, the identities extend to x = ±1. ∎

So f_lx and f_nx vanish at the axes like √(1 − x²), and |f_ab| ≤ |f̃_ab| for the regular parts f̃_lx := f_lx/√w,
f̃_nx := f_nx/√w and f̃_ab := f_ab otherwise. The certification below bounds the f̃_ab.

### Certification {#sec:appc-certification}

The residual is bounded on each element's use interval in two steps: the residual of the element's own polynomial
approximant, by interpolation in ball arithmetic and an analyticity bound on a polyellipse
([[prop:appc-element-bound]]); and the effect of the partition of unity on the overlaps, by a perturbation bound
([[prop:appc-overlap]]). Every number used is either exact or an interval that contains the exact value, formed by the
rules of [[def:tl5-jets]] (real intervals) and the same rules for complex rectangles; the exponential, logarithm,
sine, cosine and square root of an interval are enclosed by their power series with an explicit tail bound, in any
of the standard ways.

#### Exact operations on the printed coefficients {#sec:appc-exact}

The coefficients z 10^(−p) are rational. Derivatives in t, σ and x of a field [[eq:appc-fields]] have rational
Chebyshev coefficients, obtained by [[eq:tl5-cheb-derivative]] ([[lem:tl5-chebyshev]]).

**Lemma {#lem:appc-reexpand}** (Affine change of variable.) Let c and h ≠ 0 be rational. There are rational numbers
A_jk, 0 ≤ k ≤ j, with T_j(c + hτ) = Σ_k A_jk T_k(τ) for all τ; they are given by A₀₀ = 1, (A₁₀, A₁₁) = (c, h) and
T_(j+1)(c + hτ) = 2c T_j(c + hτ) + 2h τT_j(c + hτ) − T_(j−1)(c + hτ), with τT_k = (T_(k+1) + T_(|k−1|))/2.

*Proof.* The recurrence T_(j+1)(y) = 2yT_j(y) − T_(j−1)(y) at y = c + hτ and the product formula
2T_1T_k = T_(k+1) + T_(|k−1|) give the stated recursion; it involves only rational operations. ∎

So the polynomial G^F_ij restricted to a sub-box [t_c − t_h, t_c + t_h] × [σ_c − σ_h, σ_c + σ_h] × [−1, 1] has exact
rational Chebyshev coefficients in the variables τ₁ := (t − t_c)/t_h, τ₂ := (σ − σ_c)/σ_h and τ₃ := x.

#### The seed in complex arithmetic {#sec:appc-seed}

On u < −1 the seed's radius solves G(R) = H(u, v), where

    G(R) := 2R + log((R − 1)/(R + 1)),      H(u, v) := v − 2u + log((u + 1)/(u − 1)),                  {#eq:appc-seed-eq}

by [[eq:tl5-seed-radius]] after taking logarithms; and by [[lem:tl5-seed]] (b) and the chain rule, with f(r) = 1 − r⁻²
and g(u) := f(−u) = 1 − u⁻²,

    ∂_vR_s = f/2,   ∂_uR_s = −f/g,   ∂_v²R_s = f′∂_vR_s/2,   ∂_u∂_vR_s = f′∂_uR_s/2,
    ∂_u²R_s = −f′∂_uR_s/g + fg′/g²,   Ω_s² = e^(2W_s) = f/(2g),   ∂_vW_s = f′∂_vR_s/(2f),
    ∂_uW_s = (f′∂_uR_s/f − g′/g)/2,                                                                  {#eq:appc-seed-jets}

and the second derivatives of W_s by differentiating the last two once more; here f = f(R_s), f′ = 2R_s⁻³,
g′ = 2u⁻³. In [[eq:appc-seedform]] W enters the residual only through its derivatives and through
Ω² = Ω_s² e^(2(v−1/2)⁴ Σχψ G^W).

**Lemma {#lem:appc-seed-holo}** (The inverse of G.) On the half plane {Re R > 3/2}, G is holomorphic and injective, and
G′ = 2 + 2/(R² − 1) does not vanish; so G has a holomorphic inverse on G({Re R > 3/2}).

*Proof.* There |R| > 3/2, hence |R² − 1| ≥ |R|² − 1 > 5/4 and Re G′ ≥ 2 − 2/|R² − 1| > 2/5. Also (R − 1)/(R + 1) has
positive real part, since its real part is (|R|² − 1)/|R + 1|², so the principal logarithm is holomorphic. If
G(R₁) = G(R₂) with R₁ ≠ R₂ in the convex half plane, then 0 = (R₂ − R₁)∫₀¹ G′(R₁ + θ(R₂ − R₁)) dθ, whose real part is
positive; so G is injective, and its inverse is holomorphic since G′ ≠ 0. ∎

**Lemma {#lem:appc-newton}** (One step of interval Newton.) Let X be a closed rectangle in {Re R > 3/2}, r_c ∈ X,
𝐇 a closed rectangle, and Q a closed rectangle containing G′(X), with 0 ∉ Q. If

    N := r_c − (G(r_c) − 𝐇)/Q ⊂ X

in rectangle arithmetic, then for every H₀ ∈ 𝐇 the equation G(R) = H₀ has exactly one solution in {Re R > 3/2}, and it
lies in N.

*Proof.* For r ∈ X put q(r) := ∫₀¹ G′(r_c + θ(r − r_c)) dθ, which lies in the closed convex hull of G′(X), hence in
Q. The map r ↦ r_c − (G(r_c) − H₀)/q(r) is continuous on X and takes values in N ⊂ X, so by Brouwer's theorem it has a
fixed point r*, and q(r*)(r* − r_c) = H₀ − G(r_c) says G(r*) = H₀. Uniqueness is [[lem:tl5-seed]] (a) on the reals and
[[lem:appc-seed-holo]] in the half plane. ∎

#### The residual of one polynomial approximant on a box {#sec:appc-box}

Fix an element (i, j) and a sub-box 𝔅 = [t_c − t_h, t_c + t_h] × [σ_c − σ_h, σ_c + σ_h] × [−1, 1] of [−1, 1]³ in
(t, σ, x), with rational centre and half-widths; in this appendix 𝔅 is the element's use interval U_ij, rounded
outward to multiples of 1/1000, in (t, σ). Let F_ij be the fields [[eq:appc-seedform]] with χ_iψ_j replaced by 1 and
all other terms by 0, and let g_ab(τ) := f̃_ab(F_ij) at (t, σ, x) = (t_c + t_hτ₁, σ_c + σ_hτ₂, τ₃), for τ ∈ [−1, 1]³.
The polynomial parts of F_ij are Q^F := (v − 1/2)⁴G^F_ij; since v − 1/2 = α + βτ₂ with rational α, β, they are
polynomials in τ whose Chebyshev coefficients are exact rationals, by [[lem:appc-reexpand]] and four multiplications by
α + βτ₂ (with τ₂T_k = (T_(k+1) + T_(|k−1|))/2).

For ρ > 1 let E_ρ be the closed region bounded by the ellipse {(ω + ω⁻¹)/2 : |ω| = ρ}, as in [[lem:cone-ellipse]],
and for ρ = (ρ₁, ρ₂, ρ₃) let ℰ_ρ := E_ρ₁ × E_ρ₂ × E_ρ₃ ⊂ ℂ³ and ∂₀ℰ_ρ := ∂E_ρ₁ × ∂E_ρ₂ × ∂E_ρ₃ its distinguished
boundary.

On E_ρ every Chebyshev polynomial satisfies |T_n(τ)| ≤ ρ^n, since τ = (ω + ω⁻¹)/2 with 1 ≤ |ω| ≤ ρ and
T_n(τ) = (ω^n + ω^(−n))/2. Hence a polynomial Σ c_ijk T_i(τ₁)T_j(τ₂)T_k(τ₃) is bounded on ℰ_ρ by its weighted
coefficient sum Σ |c_ijk| ρ₁^i ρ₂^j ρ₃^k, and so is each derivative, with the coefficients of [[eq:tl5-cheb-derivative]].

**Lemma {#lem:appc-analytic}** (Analyticity on a polyellipse.) Suppose that: (i) on a covering of E_ρ₁ by closed
rectangles, the enclosures of cosh ξ, of Re((u + 1)/(u − 1)) and of Re u + 1, with ξ = m_i + h_i(t_c + t_hτ₁) and
u = −1 + a sinh ξ, are respectively of positive real part, positive and negative; (ii) a rectangle in ℂ that contains
H(u, v) for all τ₁ ∈ E_ρ₁, τ₂ ∈ E_ρ₂ (with v = m′_j + h′_j(σ_c + σ_hτ₂)) is covered by rectangles 𝐇 on each of which
[[lem:appc-newton]] applies, the least real part of the enclosures N so obtained being r_s; (iii) r_s exceeds the
weighted coefficient sum q_R of Q^R. Then every g_ab extends holomorphically to a neighbourhood of ℰ_ρ, and there
Re R ≥ r_s − q_R > 0.

*Proof.* By (i), ξ and u are holomorphic in τ₁, cosh ξ ≠ 0 (so dt/du and its derivative are holomorphic), u ∉ [−1, 1]
and the logarithm in H is holomorphic; so H is holomorphic on E_ρ₁ × E_ρ₂. By (ii) and [[lem:appc-newton]] every value
of H there is G(R) for a unique R with Re R > 3/2, so R_s = G⁻¹ ∘ H is holomorphic by [[lem:appc-seed-holo]], with
Re R_s ≥ r_s, hence f(R_s) ≠ 0; and g(u) ≠ 0. So the seed's jets [[eq:appc-seed-jets]] are holomorphic. The
polynomial parts are entire, and so are e^S and Ω²/Ω_s². Since |Q^R| ≤ q_R, Re R ≥ r_s − q_R > 0 by (iii). Hence 1/R,
1/e^S and 1/Ω² are holomorphic, and by [[lem:appc-regular]] so is every g_ab. ∎

**Lemma {#lem:appc-majorant}** (The bound M.) Under the hypotheses of [[lem:appc-analytic]], replace in
[[eq:appc-regular]] every quantity by an upper bound of its modulus on ℰ_ρ, and every operation by the bound of its
result: a ± b by |a| + |b|, ab by |a||b|, and a/b, for b ∈ {R, Ω², e^S, μ̂} and integers, by |a| divided by a lower
bound of |b|. The inputs are: the weighted coefficient sums of Q^F and of its derivatives, multiplied by the bounds of
the chart factors dt/du and d²t/du² on a covering of E_ρ₁ ([[eq:tl5-chain]], with the element's h_i) and by 1/t_h,
1/(h′_jσ_h); the bounds of [[eq:appc-seed-jets]] obtained from r_s ≤ |R_s| ≤ (|H| + 2.35)/2 and from the bounds of |u| on
the covering of (i); (ρ₃ + ρ₃⁻¹)/2 for |x|; e^(±s_S) for e^(±S), with s_S the bound of |S|; and
Ω_s² e^(±2q_W) for Ω². The result, times the bound of ρ = R⁴/√72, is a number M ≥ max_ab sup_(ℰ_ρ) |g_ab|.

*Proof.* Each replacement is the triangle inequality or multiplicativity of the modulus, and every input bounds the
modulus of the quantity it replaces, on all of ℰ_ρ. For |R_s|: the map R ↦ (R − 1)/(R + 1) sends {Re R > 3/2} into
the disc with diameter [1/5, 1], so |log((R − 1)/(R + 1))| ≤ log 5 + arcsin(2/3) < 2.35 there, and
2R_s = H − log((R_s − 1)/(R_s + 1)) gives |R_s| ≤ (|H| + 2.35)/2. ∎

**Lemma {#lem:appc-coefficients}** (Coefficients and interpolation.) Let g be holomorphic on a neighbourhood of ℰ_ρ
with |g| ≤ M there, and let g = Σ a_ijk T_i(τ₁)T_j(τ₂)T_k(τ₃) be its Chebyshev expansion on [−1, 1]³.
Then |a_ijk| ≤ 8Mρ₁^(−i)ρ₂^(−j)ρ₃^(−k). For N = (N₁, N₂, N₃) let p be the polynomial of degree at most N_d in τ_d that
interpolates g at the points (cos(πl₁/N₁), cos(πl₂/N₂), cos(πl₃/N₃)), 0 ≤ l_d ≤ N_d. Then for every multi-index
α = (α₁, α₂, α₃),

    sup_([−1,1]³) |∂^α (g − p)| ≤ E_α := 16M Σ_(d=1..3) S^(>N_d)_d(α_d) ∏_(d′≠d) S_(d′)(α_(d′)),        {#eq:appc-ealpha}

where S_d(l) := Σ_(n≥0) ρ_d^(−n) T_n^(l)(1) and S^(>N)_d(l) := Σ_(n>N) ρ_d^(−n) T_n^(l)(1), with T_n^(l)(1) as in
[[lem:tl5-rounding]].

*Proof.* In one variable, with τ = (z + z⁻¹)/2, the function z ↦ g((z + z⁻¹)/2) is holomorphic on the annulus
ρ⁻¹ ≤ |z| ≤ ρ, and a_n = (1/(πi)) ∮_(|z|=1) g((z + z⁻¹)/2) z^(−n−1) dz for n ≥ 1 (half that for n = 0). Moving the
contour to |z| = ρ gives |a_n| ≤ 2Mρ^(−n). Applied in each variable in turn, with the other two fixed in their
ellipses, this gives the first claim, the factor 8 = 2³ being an upper bound for every (i, j, k). The series converges
absolutely and uniformly on [−1, 1]³ with all its derivatives. At the points cos(πl/N), T_n takes the value of T_(n′),
n′ ∈ [0, N] with n′ ≡ ±n (mod 2N), since cos(nπl/N) depends on n only through that class; so the interpolant of each
T_iT_jT_k is T_(i′)T_(j′)T_(k′), and p = Σ a_ijk T_(i′)T_(j′)T_(k′), with i′ = i when i ≤ N₁ and likewise. Hence
g − p = Σ over the triples with i > N₁ or j > N₂ or k > N₃ of a_ijk (T_iT_jT_k − T_(i′)T_(j′)T_(k′)). By
[[lem:tl5-rounding]], |T_n^(l)| ≤ T_n^(l)(1) on [−1, 1], and T_n^(l)(1) is nondecreasing in n, while n′ ≤ n; so each
difference has its α-derivative bounded by 2∏_d T^(α_d)(1) at the larger indices. Summing over the union of the three
sets {i > N₁}, {j > N₂}, {k > N₃} gives [[eq:appc-ealpha]]. ∎

The sums S are explicit: T_n^(l)(1) ≤ n^(2l)/(1 · 3 ⋯ (2l − 1)), and the tail of Σ n^(2l)ρ^(−n) beyond n₀ is at most
n₀^(2l)ρ^(−n₀)/(1 − ((n₀ + 1)/n₀)^(2l)/ρ) when the denominator is positive.

**Proposition {#prop:appc-element-bound}** (The element's own residual.) Under the hypotheses of
[[lem:appc-analytic]], let M be as in [[lem:appc-majorant]], let c^(ab)_ijk be the Chebyshev coefficients of the
interpolant p_ab of [[lem:appc-coefficients]], and c^(ab,α) those of ∂^αp_ab ([[lem:tl5-chebyshev]]). Then for every
ab and every α,

    sup_𝔅 |∂_t^(α₁)∂_σ^(α₂)∂_x^(α₃) f̃_ab(F_ij)| ≤ (Σ_ijk |c^(ab,α)_ijk| + E_α)/(t_h^(α₁) σ_h^(α₂)).
                                                                                                 {#eq:appc-element-bound}

The coefficients c^(ab) are the exact discrete transform of the values at the nodes,
c_ijk = (2/N₁)(2/N₂)(2/N₃) Σ″ g(τ_l) T_i(τ_l₁)T_j(τ_l₂)T_k(τ_l₃) with the end terms of each sum and the coefficients of
index 0 and N_d halved; with the values enclosed in intervals they are enclosed in intervals.

*Proof.* |∂^αp| ≤ Σ|c^(α)| on [−1, 1]³ since |T_n| ≤ 1, and [[lem:appc-coefficients]] bounds ∂^α(g − p); the
chain rule for τ₁ = (t − t_c)/t_h and τ₂ = (σ − σ_c)/σ_h gives the division. The transform is the inverse of the
evaluation at the Chebyshev–Lobatto points, which is the standard identity for interpolation at those points. ∎

The values g_ab(τ_l) at the nodes are obtained from the 2-jets of the fields there, which by [[lem:appc-reexpand]] and
[[eq:tl5-cheb-derivative]] are exact rational combinations of the printed integers evaluated at the nodes, the seed's
jets by [[lem:appc-newton]] and [[eq:appc-seed-jets]], and the chart's derivatives by [[eq:tl5-chain]] with the
element's h_i in place of h_ξ; then [[eq:appc-regular]] is evaluated by the rules for intervals.

#### The overlaps {#sec:appc-overlaps}

On U_ij the fields [[eq:appc-seedform]] differ from those of F_ij by

    δF := (v − 1/2)⁴ Σ_((i′,j′) ≠ (i,j)) χ_(i′)ψ_(j′) (G^F_(i′j′) − G^F_ij),                             {#eq:appc-delta}

because Σχ_(i′)ψ_(j′) = 1 ([[lem:appc-pou]] (b)), and by [[lem:appc-pou]] (b) the sum has at most three nonzero terms,
all on the transition strips of width 2d in ξ or 2d′ in v.

**Lemma {#lem:appc-lipschitz}** (A perturbation bound.) Let 𝒥 ⊂ ℝ^50 be a convex set of 2-jets of the five fields at
a point (values and the nine derivatives of order one and two), on which R, Ω² and e^S are bounded below by positive
numbers, and let E be one of the expressions of [[eq:appc-regular]] (with f_lx, f_nx divided by √w), a polynomial in x
and the jets over a monomial in R, Ω² and e^S. Then for J, J + δJ ∈ 𝒥,

    |E(J + δJ) − E(J)| ≤ Σ_(q=1..50) L_q |δJ_q|,      L_q := sup_(𝒥) |∂E/∂J_q|.

The same holds with 2-jets replaced by (K + 2)-jets and E by any derivative of order at most K of a component in
(t, σ, x), which is again a polynomial in x and the (K + 2)-jets over a monomial in R, Ω² and e^S.

*Proof.* The mean value theorem on the segment from J to J + δJ, which lies in 𝒥. ∎

**Proposition {#prop:appc-overlap}** (The blended residual.) On U_ij, sup |f̃_ab(ĝ)| ≤ sup_𝔅 |f̃_ab(F_ij)| + Λ_ab,
where Λ_ab := Σ_q L_q D_q, D_q is an upper bound on U_ij of the q-th component of the 2-jet of δF, and the L_q are
taken over the convex hull of the 2-jets of F_ij + θδF, 0 ≤ θ ≤ 1, on U_ij. The D_q are bounded by Leibniz's rule from
the bounds φ_k of [[lem:appc-pou]] (a) for the derivatives of χ_(i′) and ψ_(j′) (with the factors (1/(2d))^k and
(1/(2d′))^k of the chain rule), the derivatives of (v − 1/2)⁴, and the sums of the absolute values of the Chebyshev
coefficients of the derivatives of G^F_(i′j′) − G^F_ij on the strips, which are exact by [[lem:appc-reexpand]] (both
polynomials re-expanded in the variables of the strip). The same holds for the derivatives of order at most K, with
(K + 2)-jets.

*Proof.* [[lem:appc-lipschitz]] with J the jet of F_ij and δJ that of δF, at each point of U_ij. ∎

Away from the strips δF = 0 and Λ_ab = 0. On the strips Λ_ab is small because G_(i′j′) − G_ij is: both approximate the
same field to the accuracy of the tables, and the derivatives of the blend, of size φ_k(2d)^(−k), multiply this
difference.

#### The bound in the norm of the continuation argument {#sec:appc-norm}

The certificate of an element is the family of numbers

    B^(ab)_(ij,α) ≥ sup_(U_ij) |∂_t^(α₁)∂_σ^(α₂)∂_x^(α₃) f̃_ab(ĝ)|,   |α| ≤ K,                     {#eq:appc-certificate}

given by [[prop:appc-element-bound]] and [[prop:appc-overlap]], printed rounded upward, where K is the number of
derivatives of the residual that the norm of the continuation argument contains (K = N for a level-N norm). They bound
every quantity that argument uses: the derivatives in (u, v, x) follow by [[eq:tl5-chain]] with the element's chart, and the
Lie derivatives of Ric(ĝ) along the commutation fields of the level-K estimate, weighted by μ^(|I|/2), are explicit
combinations of these derivatives, of f_ab themselves and of the fields' jets, as [[pending:lem-tl5-f3-residual]] states.
With the weight φ of the weighted norm, whose rates are those of [[pending:lem-tl5-l7-rates]], the target of element
(i, j) is

    f_ij := f e^(φ_ij/2),   φ_ij := min over U_ij of φ,                                                 {#eq:appc-target}

where f is the target of the case ([[sec:appc-outcomes]]); since e^(−φ/2) ≤ e^(−φ_ij/2) on U_ij, a pointwise bound f_ij
on U_ij for every element gives the weighted norm of the residual at most the bound that f gives with φ ≡ 0 on the
whole region.

### Certified outcomes {#sec:appc-outcomes}

The target f of a case is one tenth of the pointwise residual bound its closing needs; the allocated targets f_ij are
[[eq:appc-target]]; B_ij is the largest of the weighted certificates [[eq:appc-certificate]] of element (i, j).

    case        f            elements   B_ij against f_ij
    (1, D_A)    10^(−17.5)   2 × 2      [[pending:computational-appc-1a]]
    (2, D_A)    10^(−16.6)   2 × 2      [[pending:computational-appc-2a]]
    (2, D*)     10^(−20.1)   2 × 2      [[pending:computational-appc-2d]]
    (1, D*)     10^(−22.9)   3 × 2      [[pending:computational-appc-1d]]

For each element the tables also print the parameters of its certificate: the box 𝔅, ρ, N, the coverings of
[[lem:appc-analytic]] (i) and (ii), the numbers r_s, q_R and M, and the numbers B^(ab)_(ij,α).

### Specimen of the tables {#sec:appc-specimen}

The first lines of one block, in the format of [[sec:appc-format]]; the numbers are a specimen of the format and not
entries of the tables [[pending:computational-appc-specimen]].

    element (2,2): ξ in [−813/100, −3421/500], v in [18769/10000, 7171/2000]; field m; p = 13; rows 305; entries 4181;
    S1 = −966855768,  S2 = 35253466018,  S0 = −5112442949
    (0,0)    14633957741 −1314838470 50373968 5579401 −84957653 4844995 1048812 279577 −33967 −8255 −16537 2612 3135 |00
    +        −1104 −888 27 |14
    (0,1)    −28947799952 2821862661 320568279 −54824254 148686095 −7663444 −3560595 −135643 −42406 27333 14863 −959 |93
    +        −6441 2862 528 −69 |09
    (0,2)    21639759297 −1437057815 −1655421165 155526380 −127505282 10081040 3551495 37705 −191745 20855 −31231 |20
    +        2213 3487 −1326 74 −81 |56
    (0,3)    −9756542251 −135736511 1901753838 −149586896 15155271 −5838885 −4572416 −87815 269110 −65077 −3761 8592 |62

### Placement

This part and the crosswalk rows below are instructions for merging; they are not appendix text.

*1. Where the appendix goes.* The sections above, from "## Appendix C. The certified approximant {#app:approximant}"
through [[sec:appc-specimen]], form a new appendix file placed after Appendix B ([[app:tables]]) and before the
references. The tables themselves form a separate final part, "Tables of the approximant", after the references,
paginated on; its blocks are in the format of [[sec:appc-format]], one case after another, the case (2, D*) first, then
(1, D_A); the case (1, D*) replaces (1, D_A) once its closing is shown. The specimen section is replaced by the first
block of the first table when the tables are certified.

*2. Pending items.* [[pending:lem-tl5-cip-axis]] is the axis lemma of the characteristic problem (smoothness of a
metric of the class with smooth fields). [[pending:lem-tl5-f3-residual]] is the statement of the level-N estimate that
names the residual norm; [[sec:appc-norm]] must be completed with its exact combination once it is written.
[[pending:lem-tl5-l7-rates]] is the certified rates lemma. The four outcome rows and the specimen are computational
items: no coefficients have been certified.

*3. Other texts.* [[sec:tl5-residuals]] is unchanged. [[rem:tl5-beyond]] and the closing remarks of [[sec:tl5-beyond]]
will cite [[app:approximant]] when the continuation theorem is stated; that change belongs to the file that states it.

### Crosswalk rows

Rows for the crosswalk of the new appendix, in its four columns, separated by tabs, in order:

    app:approximant	paper/reader/proofs/P-APPC.md:1	P-APPC, appendix	new Appendix C (author's decision 2026-11-20); S-APP 4.1, 5
    eq:appc-regions	paper/reader/proofs/P-APPC.md:11	P-APPC, display	D_A and D*
    sec:appc-definition	paper/reader/proofs/P-APPC.md:16	P-APPC, section	new
    def:appc-layout	paper/reader/proofs/P-APPC.md:22	P-APPC, Definition	elements, use intervals, inner nine tenths (S-APP 3b)
    eq:appc-element	paper/reader/proofs/P-APPC.md:28	P-APPC, display	element variables
    def:appc-layouts	paper/reader/proofs/P-APPC.md:40	P-APPC, Definition	the four layouts (rational)
    def:appc-pou	paper/reader/proofs/P-APPC.md:57	P-APPC, Definition	partition of unity from Phi
    eq:appc-pou	paper/reader/proofs/P-APPC.md:63	P-APPC, display	chi_i, psi_j
    lem:appc-pou	paper/reader/proofs/P-APPC.md:67	P-APPC, Lemma	Phi smooth, symmetric, derivative bounds phi_k (ball covering + Cauchy)
    def:appc-approximant	paper/reader/proofs/P-APPC.md:85	P-APPC, Definition	seed form F = F_seed + (v-1/2)^4 sum chi psi G (S-APP 3e)
    eq:appc-fields	paper/reader/proofs/P-APPC.md:89	P-APPC, display	printed polynomials
    eq:appc-seedform	paper/reader/proofs/P-APPC.md:94	P-APPC, display	the five fields
    lem:appc-approximant	paper/reader/proofs/P-APPC.md:102	P-APPC, Lemma	smooth, class, invariances, 3-jet of the seed on N0 exact (G0b L1.1)
    sec:appc-format	paper/reader/proofs/P-APPC.md:123	P-APPC, section	new; S-APP 4.2-4.3
    eq:appc-sums	paper/reader/proofs/P-APPC.md:134	P-APPC, display	block checks S1, S2, S0
    eq:appc-linecheck	paper/reader/proofs/P-APPC.md:144	P-APPC, display	line check mod 97
    lem:appc-checks	paper/reader/proofs/P-APPC.md:148	P-APPC, Lemma	detection properties
    sec:appc-regular	paper/reader/proofs/P-APPC.md:164	P-APPC, section	new; S-APP 5 item 3 prerequisite
    eq:appc-checked	paper/reader/proofs/P-APPC.md:178	P-APPC, display	w psi_x, w^2 psi_xx regular
    eq:appc-hat	paper/reader/proofs/P-APPC.md:183	P-APPC, display	muhat, tauhat, etahat, lambda, alpha1, beta1
    eq:appc-sigma	paper/reader/proofs/P-APPC.md:191	P-APPC, display	Sigma_EE, Sigma_11, Sigma_22, Theta_A, Theta_B
    lem:appc-regular	paper/reader/proofs/P-APPC.md:193	P-APPC, Lemma	axis-regular residual; verified identical to the chapter's formula
    eq:appc-regular	paper/reader/proofs/P-APPC.md:200	P-APPC, display	the eight components
    eq:appc-sing	paper/reader/proofs/P-APPC.md:238	P-APPC, display	singular identities
    sec:appc-certification	paper/reader/proofs/P-APPC.md:276	P-APPC, section	new; S-APP 5 method B, overlaps
    sec:appc-exact	paper/reader/proofs/P-APPC.md:286	P-APPC, section	new
    lem:appc-reexpand	paper/reader/proofs/P-APPC.md:291	P-APPC, Lemma	exact affine re-expansion
    sec:appc-seed	paper/reader/proofs/P-APPC.md:301	P-APPC, section	new
    eq:appc-seed-eq	paper/reader/proofs/P-APPC.md:305	P-APPC, display	G(R) = H(u, v)
    eq:appc-seed-jets	paper/reader/proofs/P-APPC.md:312	P-APPC, display	seed jets, Omega_s^2 without a logarithm
    lem:appc-seed-holo	paper/reader/proofs/P-APPC.md:318	P-APPC, Lemma	G injective on Re R > 3/2
    lem:appc-newton	paper/reader/proofs/P-APPC.md:326	P-APPC, Lemma	interval Newton (Brouwer)
    sec:appc-box	paper/reader/proofs/P-APPC.md:339	P-APPC, section	new
    lem:appc-analytic	paper/reader/proofs/P-APPC.md:357	P-APPC, Lemma	holomorphy on the polyellipse; pluriharmonic minimum of Re R
    lem:appc-majorant	paper/reader/proofs/P-APPC.md:372	P-APPC, Lemma	new
    lem:appc-coefficients	paper/reader/proofs/P-APPC.md:386	P-APPC, Lemma	coefficient bound, Lobatto aliasing, E_alpha
    eq:appc-ealpha	paper/reader/proofs/P-APPC.md:392	P-APPC, display	interpolation error of derivatives
    prop:appc-element-bound	paper/reader/proofs/P-APPC.md:412	P-APPC, Proposition	element's own residual and derivatives on its box
    eq:appc-element-bound	paper/reader/proofs/P-APPC.md:418	P-APPC, display	the bound
    sec:appc-overlaps	paper/reader/proofs/P-APPC.md:433	P-APPC, section	new; S-APP risk 5
    eq:appc-delta	paper/reader/proofs/P-APPC.md:437	P-APPC, display	blend minus element
    lem:appc-lipschitz	paper/reader/proofs/P-APPC.md:442	P-APPC, Lemma	mean value bound in the jets
    prop:appc-overlap	paper/reader/proofs/P-APPC.md:454	P-APPC, Proposition	blended residual on the use interval
    sec:appc-norm	paper/reader/proofs/P-APPC.md:469	P-APPC, section	interface to the level-N estimate (pending its exact source term)
    eq:appc-certificate	paper/reader/proofs/P-APPC.md:473	P-APPC, display	certificate numbers B per element, |alpha| <= 3
    eq:appc-target	paper/reader/proofs/P-APPC.md:482	P-APPC, display	allocation f e^(phi_min/2) (S-APP 3g)
    sec:appc-outcomes	paper/reader/proofs/P-APPC.md:487	P-APPC, section	new; all rows pending
    sec:appc-specimen	paper/reader/proofs/P-APPC.md:501	P-APPC, section	format specimen, to be replaced
