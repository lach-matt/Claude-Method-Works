## Gluing to the Myers–Perry family, and gluing in the symmetry class {#ch:s28}

This chapter proves [CD03, Theorem 8.1] in space dimension 4 for vacuum initial data whose Poincaré charges lie near
those of five-dimensional Schwarzschild–Tangherlini. Smooth vacuum data on ℝ⁴ ∖ B that decay at a rate α ∈ (3/2, 2] are
glued, on an annulus Γ(R, 4R), to the data of a translated, rotated and boosted Myers–Perry metric, which they equal for
|x| ≥ 4R ([[thm:v-3-1]]). [CD03, Theorem 8.1, p. 35] is stated for three-dimensional data, and [CD03, Remark 8.2, p. 36]
names what is missing in higher dimensions: "The argument below carries over to any dimension, the only element missing
is an equivalent of Proposition F.1 for the family of translated, rotated, and boosted Myers-Perry metrics." Near
Tangherlini, which is the case needed here, this equivalent is [[prop:v-2-3]] and [[cor:v-2-4]]. The proof follows
[CD03, Section 8.1], with three changes in dimension 4 + 1. First, the charges are defined and estimated directly from a
linear flux identity ([[sec:v-1]]); this replaces [CD03, Appendix E] and needs no parity condition, since
2α > n − 1 = 3. Second, the exponentially weighted spaces of [CD03, Theorem 5.9] are used from the start, so the glued
data are smooth. Third, the powers of R are those of space dimension 4: R⁻² for the energy and the momentum, R⁻³ for
the angular momentum and the centre of mass. Every result of [CD03] used here holds in every space dimension n ≥ 2
([CD03, p. 4]); each is stated exactly, here or in [[app:standard-results]]. [CD03, Lemma 3.18] is proved again
([[lem:v-3-3]]), and the continuity in the parameter that [CD03, Theorem 3.19] needs is proved as [[lem:v-3-2]].

[[sec:vii-2]] runs the construction in the symmetry class of [[sec:class]], G = O(2) × O(2), on the initial surface
Σ^IVP of [[sec:iii-b-3-3]] and with the Tangherlini data on that surface as the family ([[prop:vii-2-2]]). The
obstruction is then one-dimensional and is matched by the mass alone, and the flux identity bounds the change of mass
by the size of the data's deviation on the annulus. [[cor:vii-2-3]] applies it to the data of the solution g_λ after
the shell; these are the data of item (i) of [[thm:settling]], proved in [[ch:settling-proof]].

The continuity lemma [[lem:v-3-2]] is stated on a general compact manifold with boundary and for a general smooth
background, with every hypothesis explicit ([[sec:s28-solvability]]), and is then applied to the flat annulus.
[[ch:localised-data]] applies it to other data.

*The inner radius.* Nothing in this chapter reaches the inner region of the spacetime of [[sec:iii-b-2]]. [[sec:v-2]]
uses the Myers–Perry family on {|x| ≥ 50R₁} only, and [[sec:vii-2]] takes data on Σ^IVP ∩ {r_♭ ≤ |x| ≤ 3R} and changes
them only on {R ≤ |x| ≤ 4R}. So every result holds for every inner radius r_♭ ∈ (0, ½R₁] of [[sec:iii-b-2]].

*Notation.* n = 4 is the space dimension, except in [[sec:s28-solvability]], where n is general. As in [CD03], K denotes
the second fundamental form of an initial data set, and N a lapse or the function in a pair (Y, N); neither the
approximant's order nor its number of stages occurs in this chapter. The mass parameter of the Myers–Perry family is m,
as in [[ch:s11]]; b₀ = (m₀, 0) and R₁ = m₀^(1/2). 𝔎 is the space of Killing initial data of flat space ([[eq:v-0-4]]). A
pair (K, g) in the argument of a map of [CD03] is written u = (K, g). π_(g′) and π₀ always denote projections, and the
number π occurs only in the charges.

### Initial data and the Killing initial data of flat space {#sec:v-0}

ℝ⁴ carries Cartesian coordinates x, with r = |x|, x̂ = x/r, S_ϱ := {r = ϱ} with outward unit normal ν = x̂ and
Euclidean area element dS, and Γ(a, b) := {a < r < b}. Indices are raised and traced with δ unless a metric is named.
An *initial data set* is a pair (g, K) of a Riemannian metric and a symmetric 2-tensor. Its constraint map is
[[thm:std-cd-constraints]] ([CD03, (2.1), p. 4]),

    J(K, g)_i := 2(−∇^j K_ij + ∇_i tr_g K),     ρ(K, g) := R(g) − |K|²_g + (tr_g K)²,                      {#eq:v-0-1}

"the general relativistic constraint equations whatever the space-dimension n" ([CD03, p. 4]). The data are *vacuum*
where J = 0 and ρ = 0; this condition is invariant under K ↦ −K. For a Lorentzian metric
𝔤 = −N²dt² + g_ij(dxⁱ + βⁱdt)(dxʲ + βʲdt) the data on {t = 0} are g and

    K_ij := (1/(2N))(∂_t g_ij − D_iβ_j − D_jβ_i),                                                          {#eq:v-0-2}

where D is the connection of g and β_i = 𝔤_0i; the Gauss–Codazzi equations make them vacuum when 𝔤 is Ricci-flat.

*Decay.* For α > 0, an integer j ≥ 1 and data on {r > R₀}, put

    |||(g, K)|||_(α,j) := sup_(r>R₀) ( Σ_(|γ|≤j) r^(α+|γ|)|∂^γ(g − δ)| + Σ_(|γ|≤j−1) r^(α+1+|γ|)|∂^γK| ),
                                                                                                          {#eq:v-0-3}

the components taken in Cartesian coordinates. This is the r^(−α)W^(j,∞)_r-asymptotic flatness of g, with
K ∈ r^(−α−1)W^(j−1,∞)_r, of [CD03, Section 7, (7.1)], at j = k + 4, k the order of the proof of [[thm:v-3-1]].

*The Killing initial data of flat space.* Let 𝔎 be the space of pairs X = (Y, N) with Y a Killing field of (ℝ⁴, δ)
and N an affine function, and fix the basis

    e₀ := (0, 1),     e_l := (∂_l, 0),     e_ab := (W_ab x, 0),     e′_l := (0, x^l),                         {#eq:v-0-4}

for 1 ≤ l ≤ 4 and 1 ≤ a < b ≤ 4, with W_ab := E_ab − E_ba and E_ab the matrix units (W_ab is the generator J_ab of
[[sec:iii-b-3-1]]). So dim 𝔎 = 1 + 4 + 6 + 4 = 15 = (n + 1)(n + 2)/2. Each basis element X = (Y, N) is homogeneous of a
degree d(X), meaning that N(cx) = c^(d(X))N(x) and Yⁱ(cx) = c^(d(X))Yⁱ(x) for c > 0: the degree is 0 for e₀, e_l and
1 for e_ab, e′_l. The group O(4) acts on 𝔎 by push-forward under x ↦ Ox. As O(4)-representations, the four groups in
[[eq:v-0-4]] are the trivial representation, the standard ℝ⁴, Λ²ℝ⁴ (with W ↦ OWOᵀ) and ℝ⁴.

We use the formal adjoint of the linearised constraint map in the form [CD03, (2.4), p. 5]: with P the linearisation
of (J, ρ) at (K, g) ([[thm:std-cd-constraints]]), "the formal L²-adjoint of P takes the form

    P*(Y, N) = ( 2(∇_(iY_j) − ∇^lY_l g_ij − K_ij N + tr K N g_ij),
                 ∇^lY_l K_ij − 2K^l_(i∇_j)Y_l + K^q_l∇_qY^l g_ij − ΔN g_ij + ∇_i∇_jN
                   + (∇^pK_lp g_ij − ∇_lK_ij)Y^l − N Ric(g)_ij + 2NK^l_iK_jl − 2N(tr K)K_ij )."

### Killing initial data, the flux identity and the charges {#sec:v-1}

**Lemma {#lem:v-1-1}** (The Killing initial data.) Let 𝒪 ⊂ ℝ⁴ be open and connected. A smooth pair (Y, N) on 𝒪
satisfies P*_((0,δ))(Y, N) = 0 if and only if it is the restriction of an element of 𝔎.

*Proof.* At K = 0, g = δ, [CD03, (2.4)] gives P*(Y, N) = (2(∂_(iY_j) − (div Y)δ_ij), −ΔN δ_ij + ∂_i∂_jN). The trace of
the first component is 2(1 − n) div Y, so div Y = 0 and ∂_(iY_j) = 0. The trace of the second is (1 − n)ΔN, so ΔN = 0
and ∂_i∂_jN = 0, and N is affine on the connected 𝒪. For a Killing field, ∂_iY_j is antisymmetric, so
∂_k∂_iY_j = −∂_k∂_jY_i = −∂_j∂_kY_i = ∂_j∂_iY_k = ∂_i∂_jY_k = −∂_i∂_kY_j = −∂_k∂_iY_j, which therefore vanishes. So Y is
affine with antisymmetric linear part. The converse is immediate. ∎

**Lemma {#lem:v-1-2}** (The flux identity.) Let X = (Y, N) ∈ 𝔎, let 𝒪 ⊂ ℝ⁴ be a bounded open set with smooth
boundary, and let (g, K) be data on cl 𝒪 with h := g − δ, |h| ≤ ½. Then

    ∫_𝒪 (YⁱJ_i + Nρ)(K, g) dμ_g = ∮_(∂𝒪) 𝔟_X(h, K) + ∫_𝒪 q_X dx,                                           {#eq:v-1-1}

    𝔟_X(h, K) := [N(∂_jh_ij − ∂_i tr h) − (∂_jN h_ij − ∂_iN tr h) − 2(YʲK_ij − Y_i tr K)] νⁱ dS,

where ν and dS are Euclidean, and q_X is a smooth function of (N, Y, h, ∂h, ∂²h, K, ∂K), linear in (N, Y), with

    |q_X| ≤ C(|N| + |Y|)(|h||∂²h| + |∂h|² + |h||∂K| + |∂h||K| + |K|²).                                     {#eq:v-1-2}

*Proof.* Write R(g) = g^ij(∂_kΓ^k_ij − ∂_jΓ^k_ki) + g^ij(Γ^k_klΓ^l_ij − Γ^k_jlΓ^l_ik), with Γ = ½g⁻¹∂h and
g⁻¹ = δ + O(|h|). Then R(g) = ∂_i∂_jh_ij − Δ tr h + ρ₂, where ρ₂ is a sum of terms (g⁻¹ − δ)∂²h, ∂(g⁻¹)∂h and
g⁻¹g⁻¹∂h ∂h. So |ρ₂| ≤ C(|h||∂²h| + |∂h|²), and the K-terms of ρ are bounded by C|K|². Likewise
J_i = −2(∂_jK_ij − ∂_i tr K) + J_(2,i) with |J₂| ≤ C(|h||∂K| + |∂h||K|), and dμ_g = (1 + O(|h|)) dx. So

    q_X := (YⁱJ_i + Nρ)(det g)^(1/2) − (−2Yⁱ(∂_jK_ij − ∂_i tr K) + N(∂_i∂_jh_ij − Δ tr h))

satisfies [[eq:v-1-2]]. For the linear part, integrate by parts:

    ∫_𝒪 N(∂_i∂_jh_ij − Δ tr h) = ∮ [N(∂_jh_ij − ∂_i tr h) − (∂_jN h_ij − ∂_iN tr h)]νⁱ
                                 + ∫ (∂_i∂_jN h_ij − ΔN tr h),

    ∫_𝒪 Yⁱ(∂_jK_ij − ∂_i tr K) = ∮ (YʲK_ij − Y_i tr K)νⁱ − ∫ (∂_jY_i K_ij − div Y tr K).

The last integrals vanish, because ∂∂N = 0, ∂_jY_i is antisymmetric, K is symmetric and div Y = 0. ∎

[[eq:v-1-1]] is the identity of [CD03, (E.15)–(E.16) and (E.27), Appendix E] in linear form; it is all that is used.

**Proposition {#prop:v-1-3}** (The charges.) Let (g, K) be vacuum data on {r > R₀} with |||(g, K)|||_(α,2) < ∞,
α > 3/2, and |g − δ| ≤ ½. For X in the basis [[eq:v-0-4]], of degree d, the limit

    𝔔_X(g, K) := lim_(ϱ→∞) ∮_(S_ϱ) 𝔟_X(g − δ, K)

exists, and

    |𝔔_X(g, K) − ∮_(S_ϱ) 𝔟_X(g − δ, K)| ≤ C |||(g, K)|||²_(α,2) ϱ^(2+d−2α)     (ϱ > R₀),                     {#eq:v-1-3}

with C depending only on α and R₀. Moreover:

(a) 𝔔_X is continuous on such data for the norm |||·|||_(α,2);

(b) for O ∈ O(4), 𝔔_X(O*(g, K)) = 𝔔_(O·X)(g, K), where O·X is the push-forward of X by x ↦ Ox.

*Proof.* Apply [[eq:v-1-1]] on Γ(ϱ₁, ϱ₂), R₀ < ϱ₁ < ϱ₂, where J = ρ = 0:

    ∮_(S_(ϱ₂)) 𝔟_X − ∮_(S_(ϱ₁)) 𝔟_X = −∫_(Γ(ϱ₁,ϱ₂)) q_X dx.

By [[eq:v-0-3]] every term of [[eq:v-1-2]] is at most |||·|||² r^(−2α−2), and |N| + |Y| ≤ C(1 + r)^d. So the right side
is at most C|||·|||² ∫_(ϱ₁)^∞ r^(d−2α−2) r³ dr = C′|||·|||² ϱ₁^(2+d−2α), and 2 + d − 2α ≤ 3 − 2α < 0. So the flux is
Cauchy as ϱ → ∞, and [[eq:v-1-3]] follows. (a): for two such data sets,
|𝔔_X(1) − 𝔔_X(2)| ≤ |∮_(S_ϱ) 𝔟_X(h₁ − h₂, K₁ − K₂)| + Cϱ^(2+d−2α). Choose ϱ large, then the data close in C¹ on S_ϱ.
(b): 𝔟_X is built from δ, the radial normal and X, so a change of variables gives
∮_(S_ϱ) 𝔟_X(O*h, O*K) = ∮_(S_ϱ) 𝔟_(O·X)(h, K), and S_ϱ is invariant. ∎

The normalisation is that of a linear flux. In ADM units (Newton's constant equal to one) the energy is 𝔔_(e₀)/16π and
the momentum −𝔔_(e_l)/16π, as −2(K − (tr K)δ) is −2 times the momentum density, and similarly for the others. Only 𝔔
is used below.

**Lemma {#lem:v-1-4}** (Scaling.) For R > 0 and data (g, K) on Γ(R, 4R), define 𝒮_R(g, K) on Γ(1, 4) by
(𝒮_Rg)_ij(y) := g_ij(Ry) and (𝒮_RK)_ij(y) := R K_ij(Ry). Then (J, ρ)(𝒮_R(K, g))(y) = R²(J, ρ)(K, g)(Ry)
componentwise, and for X ∈ 𝔎 homogeneous of degree d,

    ∫_(Γ(1,4)) (YⁱJ_i + Nρ)(𝒮_R(K, g)) dμ_(𝒮_Rg) = R^(−2−d) ∫_(Γ(R,4R)) (YⁱJ_i + Nρ)(K, g) dμ_g.            {#eq:v-1-4}

*Proof.* With D_R(y) := Ry, 𝒮_Rg = R⁻²D_R*g and 𝒮_RK = R⁻¹D_R*K. The constraint map is natural under
diffeomorphisms. It satisfies ρ(c⁻¹K, c⁻²g) = c²ρ(K, g) and J(c⁻¹K, c⁻²g) = cJ(K, g), as g⁻¹ scales by c² and ∇ is
unchanged. As (D_R*J)_i(y) = RJ_i(Ry), both components scale by R². In [[eq:v-1-4]] the left integrand at y is
R²(Yⁱ(y)J_i(Ry) + N(y)ρ(Ry))(det g(Ry))^(1/2), with Yⁱ(y) = R^(−d)Yⁱ(Ry) and N(y) = R^(−d)N(Ry), and dy = R⁻⁴dx. ∎

### The Myers–Perry family and its charge map near Tangherlini {#sec:v-2}

**Definition {#def:v-2-1}** For p = (m, A, w, c) with |m − m₀| < ½m₀, A ∈ 𝔰𝔬(4), w, c ∈ ℝ⁴ and ‖A‖, |w|, |c| < ε_P,
where ‖A‖ is the operator norm and ε_P ∈ (0, R₁] is fixed small below ([[lem:v-2-2]]), put:

- g^KS_(m,A), the Myers–Perry metric in Kerr–Schild form ([[def:iii-b-3-2]]), on ℝ_t × {|x| ≥ 50R₁};
- Λ_w := exp(Σ_k w_kB_k), where B_k is the linear map of ℝ^(1+4) whose vector field is the boost
  Z_k := x^k∂_t + t∂_k;
- 𝒫_p(y) := Λ_w y + (0, c) and 𝔤_p := 𝒫_p*g^KS_(m,A);
- (g_p, K_p), the data [[eq:v-0-2]] of 𝔤_p on {y⁰ = 0} ∩ {|y| > R_P}, with R_P := 100R₁ (not the gluing radius of
  [[thm:v-3-1]]).

Write p₀ := (m₀, 0, 0, 0). Writing A = Σ_(a<b) A_ab W_ab fixes the coordinates A_ab on 𝔰𝔬(4).

g^KS_(m,A) is defined, smooth in (x, m, A), Lorentzian and Ricci-flat on ℝ_t × {|x| ≥ 50R₁} for ‖A‖ < R₁. Indeed
−½ tr(A²) ≤ 2‖A‖² < 2R₁² < |x|², so r_A is defined there ([[lem:iii-b-3-1]] (b)), and
r_A² ≥ |x|² − ‖A‖² > 3‖A‖², so that ‖A‖²(r_A² + ‖A‖²) < (r_A²/3)(4r_A²/3) < r_A⁴, which is the condition of
[[lem:iii-b-3-3]] (c). The rest is the proof of [[lem:s11-ks-domain]] and [[prop:iii-b-3-4]].

**Lemma {#lem:v-2-2}** (The family's data.) For ε_P small: (g_p, K_p) are smooth vacuum data on {|y| > R_P}, smooth in
(p, y); for every j, |||(g_p, K_p)|||_(2,j) ≤ C_j; and every p-derivative of (g_p − δ, K_p) obeys the bounds of
[[eq:v-0-3]] with α = 2, uniformly in p.

*Proof.* g^KS_(m,A) − η = H_(m,A) k_A ⊗ k_A with H_(m,A) ∈ |x|⁻²C^∞(X̄) and k_A − dt = ℓ_A ∈ C^∞(X̄), smoothly in
(m, A): by [[lem:iii-b-3-1]] (b), r_A ∈ |x|(1 + |x|⁻²C^∞(X̄)), and by the proof of [[prop:iii-b-3-6]],
H_(m,A) ∈ m|x|⁻²(1 + |x|⁻²C^∞(X̄)) and the coefficient vector of ℓ_A lies in x̂ + |x|⁻¹Ax̂ + |x|⁻²C^∞(X̄) (with
Π = r_A⁴(1 + O(r_A⁻²)) and F_A = 1 + O(|x|⁻²)). So 𝔤 − η, 𝔤 := g^KS_(m,A), is independent of t and a classical symbol
of order −2 in x: |∂_x^γ(𝔤 − η)| ≤ C|x|^(−2−|γ|). 𝒫_p is affine with linear part near the identity. On {y⁰ = 0} the point
𝒫_p(0, y) has |x| ≥ ½|y| and |t| ≤ 2|w||y|, so 𝔤_p − η = 𝒫_p*(𝔤 − η) obeys the same symbol bounds on
{|y⁰| ≤ ½|y|}, smoothly in p together with all p-derivatives. There |𝔤_p − η| ≤ Cm₀R_P⁻² is small, so {y⁰ = 0} is
spacelike, N is bounded below, and [[eq:v-0-2]] expresses (g_p, K_p) as smooth functions of (𝔤_p, ∂𝔤_p) on the slice,
vanishing at (η, 0). This gives the bounds. 𝔤_p is Ricci-flat ([[prop:iii-b-3-4]]), so the data are vacuum. ∎

**Proposition {#prop:v-2-3}** (The charge map near Tangherlini; the equivalent of [CD03, Proposition F.1].) The map

    𝔮 : p ↦ (𝔔_X(g_p, K_p))_X ∈ ℝ¹⁵

(X ranging over the basis [[eq:v-0-4]]) is C¹. At every p = (m, 0, 0, 0) with |m − m₀| < ½m₀, in particular at p₀,
𝔮(p) = (6π²m, 0, …, 0) and D𝔮(p) is invertible, with the values below for m in place of m₀. In the bases [[eq:v-0-4]]
and (m, w_k, A_ab, c_k) it is block lower triangular, with diagonal blocks

    ∂𝔔_(e₀)/∂m = 6π²,     (∂𝔔_(e_l)/∂w_k) = −6π²m₀I₄,     (∂𝔔_(e_ab)/∂A_(a′b′)) = −4π²m₀I₆,
    (∂𝔔_(e′_l)/∂c_k) = −6π²m₀I₄.                                                                           {#eq:v-2-1}

The block (∂𝔔_(e′_l)/∂w_k) is not needed, the other blocks off the diagonal vanish, and
det D𝔮(p) = 6π²(6π²m)⁸(4π²m)⁶.

*Proof.* *C¹.* For fixed ϱ, f_ϱ(p) := ∮_(S_ϱ) 𝔟_X(g_p − δ, K_p) is C¹, with
∂_pf_ϱ = ∮_(S_ϱ) 𝔟_X(∂_pg_p, ∂_pK_p), since 𝔟_X is linear. Differentiate in p the identity of the proof of
[[prop:v-1-3]], which holds for every p. The difference of ∂_pf_ϱ at ϱ₂ and ϱ₁ is then −∫ ∂_p[q_X(g_p, K_p)] dx. As q_X
vanishes to second order in the jets, |∂_p[q_X]| ≤ C(1 + r)^d |jet(g_p − δ, K_p)| |jet ∂_p(g_p, K_p)| ≤ Cr^(d−6) by
[[lem:v-2-2]]. So ∂_pf_ϱ converges uniformly in p, at the rate ϱ^(d−2), and 𝔮 is C¹ with
D𝔮(p) = lim_ϱ ∮_(S_ϱ) 𝔟_X(∂_p(g_p, K_p)).

*Equivariance.* For O ∈ O(4) let Õ(t, x) := (t, Ox). By [[lem:iii-b-3-1]], r_A(Ox) = r_(OᵀAO)(x), since |Ox| = |x|,
|AOx| = |OᵀAOx| and tr A², det A are invariant under conjugation. The other ingredients of [[def:iii-b-3-2]] are
covariant in the same way, so Õ*g^KS_(m,A) = g^KS_(m,OᵀAO). Also 𝒫_p ∘ Õ = Õ ∘ 𝒫_(p·O) with
p·O := (m, OᵀAO, Oᵀw, Oᵀc), and Õ preserves {y⁰ = 0}. So (g_(p·O), K_(p·O)) = O*(g_p, K_p), and [[prop:v-1-3]] (b)
gives 𝔔_X(g_(p·O), K_(p·O)) = 𝔔_(O·X)(g_p, K_p). Fix m with |m − m₀| < ½m₀ and put p_m := (m, 0, 0, 0). As
p_m·O = p_m, D𝔮(p_m) intertwines the representations

    ℝ ⊕ Λ² ⊕ ℝ⁴ ⊕ ℝ⁴  (m, A, w, c)   ⟶   ℝ ⊕ ℝ⁴ ⊕ Λ² ⊕ ℝ⁴  (𝔔_(e₀), 𝔔_(e_l), 𝔔_(e_ab), 𝔔_(e′_l)),

the charges being linear functionals on 𝔎, whose representation is self-dual. The trivial representation, the
standard ℝ⁴ and Λ²ℝ⁴ of O(4) are real irreducible and pairwise non-isomorphic (dimensions 1, 4, 6), each with commutant
ℝ. For ℝ⁴ this holds already for SO(4). Λ² is the sum of the self-dual and anti-self-dual parts, each irreducible of
dimension 3 under SO(4) (acting through SO(3) × SO(3)); a reflection exchanges them, so no proper nonzero subspace is
O(4)-invariant. An SO(4)-equivariant endomorphism of Λ² is a ⊕ b on the two parts, and commuting with a reflection
forces a = b. By Schur's lemma D𝔮(p_m) is: a scalar c_E from m to 𝔔_(e₀); a scalar c_J times I₆ from A to (𝔔_(e_ab));
on the two copies of ℝ⁴, a matrix (a₁₁ a₁₂; a₂₁ a₂₂) ⊗ I₄ from (w, c) to (𝔔_(e_l), 𝔔_(e′_l)); and zero elsewhere.
Likewise 𝔮(p_m) is O(4)-invariant, so only its trivial component 𝔔_(e₀) can be nonzero.

*The base.* On {t = 0}, g^KS_(m,0) = η + H(dt + dr)² with H = mr⁻² ([[prop:iii-b-3-4]]) has h₀ = H x̂ ⊗ x̂ exactly,
β₀ = H x̂, 𝔤₀₀ = −1 + H and N₀ = (1 + H)^(−1/2). Its second fundamental form K₀ = −N₀⁻¹D_(iβ_j) is O(mr⁻³) with
∂K₀ = O(mr⁻⁴). It is invariant under O(4), so K₀ = a(r) x̂ ⊗ x̂ + b(r)(δ − x̂ ⊗ x̂).

*c_E.* ∂_m h₀ = r⁻² x̂ ⊗ x̂, h_ij = m x_ix_j r⁻⁴. So ∂_jh_ij = m(n + 1 − 4)x_i r⁻⁴ = m x_i r⁻⁴ and
∂_i tr h = −2m x_i r⁻⁴, and 𝔟_(e₀) = 3m r⁻³ dS. Integrating over S_ϱ, of area 2π²ϱ³, gives 6π²m at every radius:
𝔔_(e₀)(g_((m,0,0,0)), K_((m,0,0,0))) = 6π²m and c_E = 6π². (In ADM units this is 3πm/8, the mass of
five-dimensional Tangherlini.)

*a₂₂ and a₁₂.* The translation in c_k changes the data to (h₀, K₀)(y + c), with derivative ∂_k(h₀, K₀). For
e′_l = (0, x^l): x^l∂_k(∂_jh_ij − ∂_i tr h)νⁱ = 3m x^l∂_k(x_i r⁻⁴)x̂_i = −9m x^lx_k r⁻⁵, and
−(δ_lj∂_kh_ij − δ_li∂_k tr h)νⁱ = −m(δ_lk r⁻³ − x_kx_l r⁻⁵). With ∫_(𝕊³) ω_kω_l = (π²/2)δ_kl the flux is
−(9/2)π²m δ_lk − (3/2)π²m δ_lk, so a₂₂ = −6π²m at every radius. For e_l the flux of ∂_kK₀ = O(r⁻⁴) is O(ϱ⁻¹), so
a₁₂ = 0.

*a₁₁.* ∂_(w_k)𝔤_p|_(p_m) = ℒ_(Z_k)𝔤 for 𝔤 := g^KS_(m,0). As ℒ_(Z_k)η = 0 and Z_k(H) = t∂_kH,
ℒ_(Z_k)(H k₀ ⊗ k₀) = t∂_kH k₀ ⊗ k₀ + H(ℒ_(Z_k)k₀ ⊗ k₀ + k₀ ⊗ ℒ_(Z_k)k₀), with k₀ = dt + dr, the 1-form k_A of
[[def:iii-b-3-2]] at A = 0, and ℒ_(Z_k)k₀ = d(x^k + t x̂_k) = dx^k + x̂_k dt + t dx̂_k. At t = 0 this gives

    δ𝔤₀₀ = 2H x̂_k,     δβ_i = H(x̂_kx̂_i + δ_ik),     δg_ij = H(δ_ik x̂_j + x̂_iδ_jk),
    ∂_tδg_ij = ∂_kH x̂_ix̂_j + H(∂_ix̂_k x̂_j + x̂_i ∂_jx̂_k).

Linearising [[eq:v-0-2]], δK = −(δN/N₀)K₀ + (1/(2N₀))(∂_tδg − 2δ(D_(iβ_j))). Since δN = O(r⁻²), N₀ − 1 = O(r⁻²),
Γ₀δβ = O(r⁻⁵) and δΓ β₀ = O(r⁻⁵), this is δK_ij = ½(∂_tδg_ij − ∂_iδβ_j − ∂_jδβ_i) + O(r⁻⁵). The terms H∂x̂_k cancel.
With ∂_iH = −2Hx̂_i/r and ∂_ix̂_j = (δ_ij − x̂_ix̂_j)/r,

    δK_ij = (H/r)(2x̂_ix̂_jx̂_k + x̂_iδ_jk + x̂_jδ_ik − x̂_kδ_ij) + O(r⁻⁵),
    tr δK = (H/r)(4 − n)x̂_k + O(r⁻⁵) = O(r⁻⁵).

For e_l, 𝔟 = −2(δK_lj x̂_j − x̂_l tr δK) dS = −2mr⁻³(2x̂_lx̂_k + δ_lk) dS + O(r⁻⁵) dS, whose integral tends to
−2m(π² + 2π²)δ_lk. So a₁₁ = −6π²m; in ADM units the momentum per unit rapidity is the energy.

*c_J.* At A = 0, r_A = |x| + O(|A|²) and H_(m,A) = H + O(|A|²), as Π, F_A, tr A² and det A are even in A; and
ℓ_A = (r²I − A²)⁻¹(rI + A)x · dx = x̂ · dx + r⁻²(Ax) · dx + O(|A|²) ([[lem:iii-b-3-1]] (a): 𝖬/Π = (r²I − A²)⁻¹). So
the derivative in the direction A = W_ab is δ𝔤 = H(k₀ ⊗ ξ_A + ξ_A ⊗ k₀), ξ_A := r⁻²(Ax) · dx, ξ_A(x̂) = 0. Then
δ𝔤₀₀ = 0, δβ = Hξ_A = mr⁻⁴(Ax) · dx, δg = H(x̂ ⊗ ξ_A + ξ_A ⊗ x̂) and ∂_tδg = 0. Further
δ(N²) = −δ𝔤₀₀ + 2β₀ⁱδβ_i − β₀ⁱβ₀ʲδg_ij = 0, as β₀ ∥ x̂ ⊥ ξ_A. The remaining terms other than ∂δβ are O(r⁻⁶), so

    δK_ij = −∂_(iδβ_j) + O(r⁻⁶) = 2mr⁻⁶(x_i(Ax)_j + x_j(Ax)_i) + O(r⁻⁶),     tr δK = O(r⁻⁶).

For e_(a′b′) = (W′x, 0) with W′ := W_(a′b′), as (W′x) · x̂ = 0, 𝔟 = −2δK(W′x, x̂) dS =
−4mr⁻⁵(Ax) · (W′x) dS + O(r⁻⁵) dS. On S_ϱ, (Ax) · (W′x) = ϱ²(Aω) · (W′ω) and dS = ϱ³dω, so the integral tends to
−4m∫_(𝕊³) ωᵀAᵀW′ω dω = −2π²m tr(AᵀW′), using ∫ ω_iω_j = (π²/2)δ_ij. As tr(W_abᵀW_(a′b′)) = 2δ_aa′δ_bb′,
c_J = −4π²m; in ADM units the angular momentum is (πm/4)A_ab, two thirds of the mass per unit spin.

So D𝔮(p_m) is as stated, with m in place of m₀: c_E = 6π², a₁₁ = a₂₂ = −6π²m, a₁₂ = 0 and c_J = −4π²m. Its determinant
is c_E (a₁₁a₂₂ − a₁₂a₂₁)⁴ c_J⁶ = 6π²(6π²m)⁸(4π²m)⁶ ≠ 0. ∎

**Corollary {#cor:v-2-4}** There are neighbourhoods U of p₀ and V of 𝔮(p₀) such that 𝔮 : U → V is a C¹
diffeomorphism (inverse function theorem). For Q ∈ V write p(Q) := 𝔮|_U⁻¹(Q); then p(Q) is continuous and the data
(g_(p(Q)), K_(p(Q))) have charge vector exactly Q.

**Remark {#rem:s28-jacobian}** (Numerical observation.) Numerical quadrature on 𝕊³ of the charge fluxes of the fifteen
linearisations of the family at p₀, at a large radius, gives the 225 entries of D𝔮(p₀) as in [[prop:v-2-3]], and gives
the block (∂𝔔_(e′_l)/∂w_k) zero to the accuracy of the quadrature. No proof uses this.

[[prop:v-2-3]] is proved near Tangherlini only, which is the case the gluing needs; the global form of the equivalent
of [CD03, Proposition F.1] for the Myers–Perry family is not used. In ADM units its values are: energy 3πm/8, momentum
per unit rapidity equal to the energy, angular momentum πm/4 per unit spin, centre of mass shifted by the translation.

### The gluing {#sec:v-3}

#### The solvability statement and its continuity in the background {#sec:s28-solvability}

The gluing solves the constraint equations on a compact annulus by [CD03, Theorem 5.9]. This subsection states what is
used of it, on a general compact manifold with boundary, and proves the continuity in the background that the gluing
needs ([[lem:v-3-2]]). Besides [[thm:std-cd-isomorphism]], [[thm:std-cd-bijective]], [[thm:std-cd-uniform-inverse]]
and [[thm:std-cd-exponential]] we use the following statements of [CD03], which hold for every n ≥ 2.

- [CD03, (A.1), p. 58]: for smooth positive functions φ, ψ, H^k_(φ,ψ)(g) is "the space of H^k_loc functions or tensor
  fields such that the norm ‖u‖_(H^k_(φ,ψ)(g)) := (∫_M (Σ_(i=0)^k φ^(2i)|∇^(i)u|²_g)ψ² dμ_g)^(1/2) is finite";
  H̊^k_(φ,ψ) is "the closure in H^k_(φ,ψ) of the space of H^k functions or tensors which are compactly (up to a
  negligible set) supported in M"; L²_ψ := H̊⁰_(1,ψ); and W^(k,∞)_φ := {u ∈ W^(k,∞)_loc : φⁱ|∇^(i)u|_g ∈ L^∞}.
- [CD03, (2.9), p. 7]: "We define a map Φ by Φ(x, y) := (φx, φ²y)."
- [CD03, Lemma 2.6, p. 7]: "Let k ∈ ℤ. Suppose that g ∈ W^(k+3,∞)_loc and that Ric(g) ∈ φ⁻²W^(k+2,∞)_φ,
  K ∈ φ⁻¹W^(k+3,∞)_φ. If (A.2) holds with 0 ≤ i ≤ k + 2, then the linear operators
  ΦP* : H̊^(k+3)_(φ,ψ) × H̊^(k+4)_(φ,ψ) ⟶ H̊^(k+2)_(φ,ψ) × H̊^(k+2)_(φ,ψ), k ≥ −2,
  ψ⁻²PΦψ² : H̊^(k+2)_(φ,ψ) × H̊^(k+2)_(φ,ψ) ⟶ H̊^(k+1)_(φ,ψ) × H̊^k_(φ,ψ), k ≥ 0, are well defined, and bounded."
- [CD03, Proposition 3.3, p. 11]: "Under the hypotheses of Lemma 2.8 with (K, g) = (K₀, g₀), let 𝒦₀ be kernel of
  ΦP*₀ : H̊¹_(φ,ψ)(g₀) × H̊²_(φ,ψ)(g₀) ⟶ L²_ψ(g₀) × L²_ψ(g₀), and let 𝒦₀^(⊥g₀) be its L²_ψ(g₀) ⊕ L²_ψ(g₀)-orthogonal.
  …"; and, on the same page, "We denote by π_(𝒦₀^(⊥g)) the L²_ψ(g) projection onto 𝒦₀^(⊥g).", where 𝒦₀^(⊥g) is the
  L²_ψ(g) ⊕ L²_ψ(g)-orthogonal of 𝒦₀, g being the current metric. [[thm:std-cd-isomorphism]], [[thm:std-cd-bijective]]
  and the equation (5.11) of [[thm:std-cd-exponential]] are stated for this projection, on the space 𝒦₀^(⊥g), which
  moves with g.
- [CD03, (3.9), p. 13]: "L_(φ,ψ) := ψ⁻²PΦψ²ΦP*."
- [CD03, Definition 5.3, p. 22]: "Let k ∈ ℕ and let 𝒲 be a space of symmetric tensors on M. We shall say that g has an
  (𝒲, k)–behavior at ∂M if there exists a metric g_M̄ on M̄ of class C^k(M̄) such that g − g_M̄ ∈ 𝒲."

In [CD03] indices are raised and lowered with the current metric g: P* at (K, g) lowers the index of Y with g, and the
1-form J is paired with a vector field, or projected, with its index raised by g ([CD03, (8.6)] pairs the residual with
the Killing initial data in this way). We do the same.

*Setting.* Let 𝒜 be a compact manifold with boundary, of dimension n ≥ 2, and let u₀ = (K₀, g₀) be a symmetric
2-tensor and a Riemannian metric on 𝒜, both smooth up to ∂𝒜. Let x ∈ C^∞(𝒜) be a defining function of ∂𝒜 with
0 < x ≤ 1 on the interior 𝒜° that equals the g₀-distance to ∂𝒜 near ∂𝒜. Fix s > 0 and an integer k > n/2. The weighted
spaces are those of [CD03, (A.1)] on 𝒜, with φ := x², and we write ψ := e^(−s/x). For ε ∈ (0, ½] let 𝒩_ε be the set of
pairs u′ = (K′, g′) with

    ‖(K′ − K₀, g′ − g₀)‖_(x⁻²W^(k+3,∞)_(x²)(g₀) × W^(k+4,∞)_(x²)(g₀)) < ε;

in particular |g′ − g₀|_(g₀) < ε on 𝒜. The unknowns are pairs z = (Y, N) of a vector field and a function on 𝒜°. For
u′ ∈ 𝒩_ε their L²_ψ(g′) product is

    ⟨(Y, N), (Z, M)⟩_(L²_ψ(g′)) := ∫_𝒜 (g′(Y, Z) + NM) ψ² dμ_(g′),

and ♯_(g′)(V, f) := (g′⁻¹V, f) turns a pair of a 1-form and a function, such as a value of (J, ρ), into such a pair,
by raising the index with g′; ♭_(g′) := ♯_(g′)⁻¹. Let 𝒦₀ be the kernel of ΦP*_(u₀) on H̊¹_(x²,ψ)(g₀) × H̊²_(x²,ψ)(g₀),
as in [CD03, Proposition 3.3], with Φ(a, b) := (x²a, x⁴b). For u′ ∈ 𝒩_ε let 𝒦₀^(⊥g′) be the L²_ψ(g′)-orthogonal of
𝒦₀, and π_(g′) the L²_ψ(g′)-orthogonal projection onto 𝒦₀^(⊥g′), as on [CD03, p. 11]; put π₀ := π_(g₀). Put

    𝒴_(g′) := 𝒦₀^(⊥g′) ∩ (H̊^(k+3)_(x²,ψ) × H̊^(k+4)_(x²,ψ)),     𝒵̃ := H̊^(k+1)_(x²,ψ) × H̊^k_(x²,ψ),
    𝒵_(g′) := 𝒦₀^(⊥g′) ∩ 𝒵̃,     𝒴 := 𝒴_(g₀),     𝒵 := 𝒵_(g₀),
    𝒮 := H^(k+1)_(x²,e^(s/x)) × H^k_(x²,e^(s/x)),     𝒳 := x²H^(k+2)_(x²,e^(s/x)) × x⁴H^(k+2)_(x²,e^(s/x)),

the spaces of the unknowns, of the projected sources, of the sources (δJ, δρ) and of the solutions (δK, δg).

*The spaces.* All of them are built with g₀. For u′ ∈ 𝒩_ε the spaces built with g′ are the same, with norms equivalent
to these by constants independent of u′. Indeed, the difference D of the Levi-Civita connections of g′ and g₀ is a
tensor with x^(2i+2)|∇^(i)D|_(g₀) ≤ Cε for i ≤ k + 3; so φⁱ∇′^(i)u − φⁱ∇^(i)u is a sum of contractions of products of
factors φ^(j+1)∇^(j)D with one factor φ^l∇^(l)u, l < i; and |·|_(g′), dμ_(g′) are comparable to |·|_(g₀), dμ_(g₀)
(compare [CD03, (A.4)]). So the statements of [CD03], made in the spaces built with the current metric, hold in these.
Two further facts are used. First, multiplication by ψ² maps H^j_(x²,ψ) onto H^j_(x²,ψ⁻¹), with equivalent norms, as
φⁱψ^(∓2)∇^(i)(ψ^(±2)) is bounded for every i, each derivative of e^(±2s/x) bringing a factor of order x⁻²; so
e^(2s/x) = ψ⁻² maps 𝒮 isomorphically onto H^(k+1)_(x²,ψ) × H^k_(x²,ψ). Second, for φ = x² the closure H̊^j_(x²,ψ′) is
all of H^j_(x²,ψ′), for every positive weight ψ′. Let χ₁ ∈ C^∞(ℝ) vanish on (−∞, 1] and equal 1 on [2, ∞). For
u ∈ H^j_(x²,ψ′), χ₁(x/δ)u has compact support in 𝒜°, where the weights are bounded above and below, so it lies in H^j
there. It tends to u in H^j_(x²,ψ′) as δ → 0: the derivatives of the cut-off live on {δ ≤ x ≤ 2δ}, where
x^(2i)|∇^(i)(χ₁(x/δ))| ≤ C_iδⁱ, and the integrals of the weighted derivatives of u over {x ≤ 2δ} tend to zero. Hence
e^(2s/x) maps 𝒮 isomorphically onto 𝒵̃, and a pair smooth up to ∂𝒜 lies in H̊^j_(x²,ψ) for every j, its weighted
derivatives being bounded and ψ² integrable.

For u′ ∈ 𝒩_ε and z ∈ 𝒴 put ι_(u′) := π_(g′)|_𝒴 and

    T_(u′)z := e^(−2s/x)Φ²P*_(u′)ι_(u′)z,     Ψ(u′, z) := π₀♯_(g′)e^(2s/x){(J, ρ)(u′ + T_(u′)z) − (J, ρ)(u′)},
                                                                                                          {#eq:s28-psi}

with P*_(u′) the operator [CD03, (2.4)] at u′. So T_(u′)z is a field of the form e^(−2s/x)Φ²P*_(u′)(Y, N) in which
[CD03, Theorem 5.9] gives its solutions, with (Y, N) := ι_(u′)z ∈ 𝒴_(g′) ([[lem:s28-setting]] (e)). The one further
hypothesis is:

(Fin) 𝒦₀ is finite-dimensional, with a basis (e_i)_(i∈I) of pairs smooth on 𝒜.

**Lemma {#lem:s28-setting}** (The solvability statement.) In the setting above, with (Fin):

(a) The hypotheses of [[thm:std-cd-exponential]] ([CD03, Theorem 5.9]) hold for g₀, K₀ and x. So there is ε > 0 such
that for u′ ∈ 𝒩_ε and every (δJ, δρ) ∈ 𝒮 of norm < ε there is (Y, N) ∈ 𝒴_(g′) for which
(δK, δg) := e^(−2s/x)Φ²P*_(u′)(Y, N) ∈ 𝒳 is close to zero and solves

    π_(g′)♯_(g′)e^(2s/x){(J, ρ)(K′ + δK, g′ + δg) − (J, ρ)(K′, g′)} = π_(g′)♯_(g′)e^(2s/x)(δJ, δρ),
                                                                                                          {#eq:v-3-1}

which is [CD03, (5.11)] at (K, g) = u′. For z ∈ 𝒴 and (δK, δg) := T_(u′)z, [[eq:v-3-1]] holds if and only if

    Ψ(u′, z) = δf,     δf := π₀♯_(g′)e^(2s/x)(δJ, δρ) ∈ 𝒵;

and each (Y, N) ∈ 𝒴_(g′) is ι_(u′)z for exactly one z ∈ 𝒴, namely z = π₀(Y, N).

(b) Diminishing ε: if u′ ∈ 𝒩_ε is smooth on 𝒜, and (δJ, δρ) ∈ 𝒮 is smooth with compact support in 𝒜° and has norm less
than ε also in the norm of [CD03, Proposition 5.10] with t := s, then the solution (δK, δg) of (a) is smooth on 𝒜 and
extends smoothly by zero across ∂𝒜. If the support of (δJ, δρ) lies in a fixed compact set Ω_c ⊂ 𝒜°, that norm is at
most C(Ω_c)‖(δJ, δρ)‖_(C^(k+2)(𝒜)), with C(Ω_c) independent of u′ ∈ 𝒩_ε.

(c) 𝒳 ⊂ C²(𝒜), with ‖(δK, δg)‖_(C²(𝒜)) ≤ C‖(δK, δg)‖_𝒳.

(d) D_zΨ(u′, 0) = π₀L_(u′)ι_(u′), with L_(u′) := ♯_(g′)ψ⁻²P_(u′)Φψ²ΦP*_(u′), the operator L_(φ,ψ) of [CD03, (3.9)] at
u′. Diminishing ε, for every u′ ∈ 𝒩_ε, π_(g′)L_(u′) is an isomorphism 𝒴_(g′) → 𝒵_(g′) ([[thm:std-cd-isomorphism]]),
and D_zΨ(u′, 0) is an isomorphism 𝒴 → 𝒵 whose inverse has norm at most a constant C₁ independent of u′.

(e) For u′ ∈ 𝒩_ε let A_(g′) be the matrix (A_(g′))_(ij) := ⟨e_i, e_j⟩_(L²_ψ(g′)); it is symmetric and positive
definite, and

    π_(g′)v = v − Σ_(i,j∈I) (A_(g′)⁻¹)_(ij) ⟨v, e_j⟩_(L²_ψ(g′)) e_i.                                 {#eq:s28-projection}

The kernel of π_(g′) is 𝒦₀, and π₀π_(g′) = π₀, π_(g′)π₀ = π_(g′). π_(g′) maps 𝒵̃ and H̊^(k+3)_(x²,ψ) × H̊^(k+4)_(x²,ψ)
into themselves, and on each ‖π_(g′) − π_(g″)‖ ≤ C‖g′ − g″‖_(W^(k+4,∞)_(x²)(g₀)) for u′, u″ ∈ 𝒩_ε. The maps
ι_(u′) : 𝒴 → 𝒴_(g′) and π₀|_(𝒵_(g′)) : 𝒵_(g′) → 𝒵 are isomorphisms, with inverses π₀|_(𝒴_(g′)) and π_(g′)|_𝒵. These
four maps, and ♯_(g′) on 𝒵̃, have norms at most a constant independent of u′, and
‖♯_(g′) − ♯_(g″)‖_(𝒵̃→𝒵̃) ≤ C‖g′ − g″‖_(W^(k+4,∞)_(x²)(g₀)).

*Proof.* We prove (e) first.

(e) 𝒦₀ is finite-dimensional, hence closed, and the e_i lie in L²_ψ, being smooth up to ∂𝒜. A_(g′) is the Gram matrix
of the linearly independent e_i for the inner product of L²_ψ(g′), hence symmetric and positive definite. Let w be the
right side of [[eq:s28-projection]]. Then v − w ∈ 𝒦₀, and, all products being those of L²_ψ(g′),
⟨w, e_l⟩ = ⟨v, e_l⟩ − Σ_(i,j)(A_(g′))_(li)(A_(g′)⁻¹)_(ij)⟨v, e_j⟩ = 0 for every l. So w ∈ 𝒦₀^(⊥g′); as v − w lies in
𝒦₀, which is the L²_ψ(g′)-orthogonal of 𝒦₀^(⊥g′), w = π_(g′)v. By the formula, π_(g′)v = 0 only if v ∈ 𝒦₀; and for
v = e_l the sum is Σ_(i,j)(A_(g′)⁻¹)_(ij)(A_(g′))_(jl)e_i = e_l, so π_(g′)e_l = 0. Hence π_(g′)v = v − k with k ∈ 𝒦₀,
and π₀π_(g′)v = π₀v − π₀k = π₀v; likewise π_(g′)π₀ = π_(g′). The e_i lie in 𝒵̃ and in
H̊^(k+3)_(x²,ψ) × H̊^(k+4)_(x²,ψ) (*The spaces*), and |⟨v, e_j⟩_(L²_ψ(g′))| ≤ C‖v‖_(L²_ψ(g₀)), which is at most C times
either norm of v; so π_(g′) maps both spaces into themselves, with norm bounded independently of u′, as A_(g′) is within
Cε of A_(g₀). The integrand of ⟨v, e_j⟩_(L²_ψ(g′)) is a smooth function of the values of g′ times a bilinear expression
in v and e_j, so |⟨v, e_j⟩_(L²_ψ(g′)) − ⟨v, e_j⟩_(L²_ψ(g″))| ≤ C sup_𝒜|g′ − g″|_(g₀)‖v‖_(L²_ψ(g₀)); the same holds for
A_(g′) − A_(g″), hence for A_(g′)⁻¹ − A_(g″)⁻¹, and this gives the bound on π_(g′) − π_(g″), sup_𝒜|g′ − g″|_(g₀) being at
most the norm of W^(k+4,∞)_(x²)(g₀). For z ∈ 𝒴, ι_(u′)z lies in H̊^(k+3)_(x²,ψ) × H̊^(k+4)_(x²,ψ) and in 𝒦₀^(⊥g′), so in
𝒴_(g′); likewise π₀y ∈ 𝒴 for y ∈ 𝒴_(g′); and π₀ι_(u′)z = π₀π_(g′)z = π₀z = z, ι_(u′)π₀y = π_(g′)π₀y = π_(g′)y = y. The
same argument applies to π₀|_(𝒵_(g′)) and π_(g′)|_𝒵. Finally, ♯_(g′) multiplies the 1-form by g′⁻¹, and for
i ≤ k + 4, x^(2i)|∇^(i)(g′⁻¹ − g₀⁻¹)|_(g₀) ≤ Cε and x^(2i)|∇^(i)(g′⁻¹ − g″⁻¹)|_(g₀) ≤ C‖g′ − g″‖_(W^(k+4,∞)_(x²)(g₀));
by the Leibniz rule, multiplication by a tensor with bounded x^(2i)|∇^(i)·|_(g₀), i ≤ k + 1, is bounded on H̊^j_(x²,ψ),
j ≤ k + 1, by a multiple of these bounds.

(a) A metric smooth on 𝒜 has the (W^(k+4,∞)_(x²), k + 4)- and the (C^(k+4,α)_(x²,1), k + 5)-behaviour at ∂𝒜 of
[CD03, Definition 5.3], with g_M̄ := g₀. (5.10a) holds as Ric(g₀) is bounded on 𝒜, (5.10b) as ∇∇x is bounded near ∂𝒜,
and (5.10c) as K₀ and its derivatives are bounded. The ε and the solution are those of [[thm:std-cd-exponential]]. Its
(Y, N)-spaces are those of [[thm:std-cd-bijective]] with ψ = e^(−s/x), as its solution
(δK, δg) = e^(−2s/x)Φ²P*(Y, N) = ψ²Φ²P*(Y, N) shows (*The spaces*). [CD03, Theorem 5.9] is obtained from
[[thm:std-cd-bijective]] ([CD03, p. 26]), whose map (3.13) is defined on
𝒦₀^(⊥g′) ∩ (H̊^(k+3)_(x²,ψ) × H̊^(k+4)_(x²,ψ)) = 𝒴_(g′); so (Y, N) ∈ 𝒴_(g′). [CD03, (5.11)] at u′ is [[eq:v-3-1]], the
index of J being raised with g′, as in [CD03]. By (e), the kernels of π_(g′) and of π₀ are both 𝒦₀. So [[eq:v-3-1]]
says

    ♯_(g′)e^(2s/x){(J, ρ)(u′ + (δK, δg)) − (J, ρ)(u′) − (δJ, δρ)} ∈ 𝒦₀,

and for (δK, δg) = T_(u′)z so does Ψ(u′, z) = δf. δf lies in 𝒵, as e^(2s/x)(δJ, δρ) ∈ 𝒵̃ (*The spaces*) and by (e).
The last assertion is part of (e). "Close to zero" is the conclusion of [CD03, Theorem 5.9]; we use it in the form:
for every r > 0, diminishing ε, the solution has ‖(δK, δg)‖_𝒳 < r. [CD03] applies its existence theorems in this form,
with the solution bounded by a multiple of the norm of (δJ, δρ) ([CD03, (8.5)]), and [[lem:v-3-2]] (c) proves that
bound for the solution it constructs.

(b) As k > n/2 is an integer, k ≥ k₀ := ⌊n/2⌋ + 1. The metric g₀ has the (C^(k+4,α)_(x²,1), k + 5)-behaviour and (5.10)
holds, by (a). As u′ is smooth on 𝒜, it lies in x⁻²C^(k+3,α)_(x²,1)(g₀) × C^(k+4,α)_(x²,1)(g₀), and the norm of 𝒩_ε
bounds the norm ‖(K′ − K₀, g′ − g₀)‖_(x⁻²W^(k₀+3,∞)_(x²)(g₀) × W^(k₀+4,∞)_(x²)(g₀)) of [CD03, Proposition 5.10], as
k₀ ≤ k. The condition of [CD03, Proposition 5.10] on (δJ, δρ), with t := s > 0, is assumed. So, ε being at most the ε
of [CD03, Proposition 5.10], the hypotheses of [CD03, Proposition 5.10] hold. A smooth pair with compact support in 𝒜°
lies in C^∞_(x²,e^(s/x))(g′), x being bounded below on its support, and u′ ∈ C^∞(𝒜) × C^∞(𝒜); so
[CD03, Corollary 5.11] ([[thm:std-cd-exponential]]) applies to the solution of (a). For the bound: on a neighbourhood
of Ω_c, x is bounded below, so the weights x², x⁻ⁿ and e^(s/x) are bounded above and below there, and the norm of
[CD03, Proposition 5.10] of a pair supported in Ω_c is at most C(Ω_c) times its C^(k₀+2) × C^(k₀+1)-norm, the covariant
derivatives being those of g′. These are at most C(Ω_c)‖(δJ, δρ)‖_(C^(k+2)(𝒜)), as k₀ ≤ k and the derivatives of g′ of
order at most k + 4 are bounded on Ω_c uniformly for u′ ∈ 𝒩_ε.

(c) x^(−4j)e^(−2s/x) is bounded on 𝒜°, so H^(k+2)_(x²,e^(s/x)) ⊂ H^(k+2)(𝒜), and H^(k+2)(𝒜) ⊂ C²(𝒜) by Sobolev's
inequality, as k + 2 > n/2 + 2; the factors x² and x⁴ are bounded.

(d) D_zΨ(u′, 0)z = π₀♯_(g′)e^(2s/x)P_(u′)(T_(u′)z) = π₀♯_(g′)ψ⁻²P_(u′)ψ²Φ²P*_(u′)ι_(u′)z = π₀L_(u′)ι_(u′)z, as Φ and
ψ² commute. The hypotheses of [[thm:std-cd-isomorphism]] hold at u₀, with φ = x² and ψ = e^(−s/x):

- g₀ ∈ W^(k+4,∞)_loc, Ric(g₀) ∈ φ⁻²W^(k+2,∞)_φ(g₀) and K₀ ∈ φ⁻¹W^(k+3,∞)_φ(g₀), as g₀ and K₀ are smooth up to ∂𝒜 and
  x ≤ 1;
- (A.2) holds for every i: φ^(i−1)∇^(i)φ is a polynomial in x and the derivatives of x, and ψ⁻¹∇^(i)ψ is a sum of
  products of derivatives of s/x of total size at most Cx^(−2i), which φⁱ = x^(2i) compensates;
- the scaling property holds by [CD03, Lemma B.1] and the argument after it, [CD03, pp. 61–62], which treats φ = x²
  with the weights e^(±s/x) (see [CD03, p. 25]);
- inequality (3.4) holds for (Y, N) supported in a neighbourhood of ∂𝒜, whose complement is compact: there it is (5.12)
  and the display after it, [CD03, p. 26], obtained from [CD03, Corollary D.5 and Proposition C.4], with
  [CD03, Lemma 4.3], as (𝒜°, g₀, K₀, x) satisfies the asymptotic condition b) of [CD03, Definition 4.1] with
  U_i := {x > 1/i}, K₀, ∇K₀ and Ric(g₀) being bounded.

So, diminishing ε, for every u′ ∈ 𝒩_ε the map π_(g′)L_(u′) is an isomorphism 𝒴_(g′) → 𝒵_(g′) whose inverse has norm
bounded independently of u′; these are the spaces of [[thm:std-cd-isomorphism]] at (K, g) = u′ (*The spaces*), and the
closeness there is in the norm of 𝒩_ε, as φ⁻¹ = x⁻². By (e), π₀ = π₀π_(g′), so

    D_zΨ(u′, 0) = (π₀|_(𝒵_(g′)))(π_(g′)L_(u′))ι_(u′),

a composition of three isomorphisms whose inverses have norms bounded independently of u′, by (e); its inverse is
π₀|_(𝒴_(g′))(π_(g′)L_(u′))⁻¹π_(g′)|_𝒵, of norm at most some C₁. ∎

**Lemma {#lem:v-3-2}** (Continuity in the background.) In the setting above, with (Fin), let ε and C₁ be as in
[[lem:s28-setting]]. There are ε_c ∈ (0, ε] and r_c > 0 such that, with B the ball of radius r_c about zero in 𝒴:

(a) for u′ ∈ 𝒩_(ε_c) and z₁, z₂ ∈ B,

    ‖Ψ(u′, z₁) − Ψ(u′, z₂)‖_𝒵 ≥ (2C₁)⁻¹‖z₁ − z₂‖_𝒴;                                                       {#eq:s28-lower}

in particular [[eq:v-3-1]] has at most one solution (δK, δg) = T_(u′)z with z ∈ B;

(b) if z ∈ B solves [[eq:v-3-1]] for (u′, (δJ, δρ)) and z̃ ∈ B for (ũ′, (δJ̃, δρ̃)), with u′, ũ′ ∈ 𝒩_(ε_c), then

    ‖z̃ − z‖_𝒴 ≤ 2C₁(‖δf̃ − δf‖_𝒵 + ‖Ψ(u′, z) − Ψ(ũ′, z)‖_𝒵),     δf̃ := π₀♯_(g̃′)e^(2s/x)(δJ̃, δρ̃),
                                                                                                          {#eq:s28-cont}

with δf as in [[lem:s28-setting]] (a); both terms on the right tend to zero as (ũ′, (δJ̃, δρ̃)) tends to
(u′, (δJ, δρ)) in 𝒩_(ε_c) × 𝒮. So the solution with z ∈ B is unique and depends continuously on the background u′ and
the right side (δJ, δρ), and so does (δK, δg) = T_(u′)z in 𝒳;

(c) there are ε_s > 0 and C₅ such that for u′ ∈ 𝒩_(ε_c) and ‖(δJ, δρ)‖_𝒮 < ε_s, [[eq:v-3-1]] has a solution
(δK, δg) = T_(u′)z with z ∈ B, and ‖z‖_𝒴 + ‖(δK, δg)‖_𝒳 ≤ C₅‖(δJ, δρ)‖_𝒮. Diminishing ε_s, it is the solution of
[[lem:s28-setting]] (a), so (b) of that lemma applies to it.

*Proof.* (a) By [[lem:s28-setting]] (d), D_zΨ(u′, 0) is an isomorphism with inverse of norm at most C₁, independently of
u′. T_(u′) is bounded from 𝒴 to 𝒳, continuously in u′ in operator norm: so is e^(−2s/x)Φ²P*_(u′), its coefficients
being polynomial in the 2-jet of u′ and in g′⁻¹, and so is ι_(u′), by [[lem:s28-setting]] (e). The constraint map is a
polynomial in the 2-jet of the data, with coefficients rational in the metric. The spaces H^(k+2)_(x²,e^(s/x)), with
k + 2 > n/2 + 1, embed in C¹(𝒜), and they are stable under products with each other and with W^(k+2,∞)_(x²)(𝒜), by
Sobolev's inequality on the balls B_p of centre p and radius x(p)²/2, on which x and e^(s/x) are comparable to their
values at p ([CD03, Appendix B, (B.2)–(B.3), pp. 61–62]). The space W^(k+2,∞)_(x²)(𝒜) contains C^(k+2)(𝒜) and the
coefficients built from u′ ∈ 𝒩_ε, each K′ and each Christoffel symbol of g′ entering with a factor x² supplied by the
factors x² and x⁴ of 𝒳, as in [CD03, Lemma 2.6]. So (u′, δu) ↦ (J, ρ)(u′ + δu) − (J, ρ)(u′) is C² from a neighbourhood
of zero in 𝒳 into 𝒮, with derivatives continuous in u′ and bounded uniformly. With
D_zΨ(u′, z) = π₀♯_(g′)e^(2s/x)D(J, ρ)(u′ + T_(u′)z)T_(u′), and e^(2s/x) : 𝒮 → 𝒵̃ bounded (*The spaces*), this gives a
constant C₃, independent of u′ ∈ 𝒩_ε for ε small (it includes the factors ‖π₀‖, ‖♯_(g′)‖ and ‖T_(u′)‖², bounded
uniformly), with

    ‖D_zΨ(u′, z₁) − D_zΨ(u′, z₂)‖ ≤ C₃‖z₁ − z₂‖

for z₁, z₂ in a ball about zero; this is hypothesis 3 of [[thm:std-cd-uniform-inverse]], for the variable z. Take r_c
at most the radius of that ball and at most (2C₁C₃)⁻¹. For z₁, z₂ ∈ B, with z_θ := z₂ + θ(z₁ − z₂),

    Ψ(u′, z₁) − Ψ(u′, z₂) = D_zΨ(u′, 0)(z₁ − z₂) + ∫₀¹ (D_zΨ(u′, z_θ) − D_zΨ(u′, 0)) dθ (z₁ − z₂),

and ‖z_θ‖ ≤ max(‖z₁‖, ‖z₂‖), so

    ‖Ψ(u′, z₁) − Ψ(u′, z₂)‖ ≥ ‖D_zΨ(u′, 0)(z₁ − z₂)‖ − C₃ max(‖z₁‖, ‖z₂‖)‖z₁ − z₂‖ ≥ (2C₁)⁻¹‖z₁ − z₂‖.

By [[lem:s28-setting]] (a), (δK, δg) = T_(u′)z solves [[eq:v-3-1]] exactly when Ψ(u′, z) = δf; so two solutions with
z ∈ B have the same z.

(b) Ψ(ũ′, z̃) = δf̃ and Ψ(u′, z) = δf ([[lem:s28-setting]] (a)), so by (a) at ũ′,

    ‖z̃ − z‖ ≤ 2C₁‖Ψ(ũ′, z̃) − Ψ(ũ′, z)‖ ≤ 2C₁(‖δf̃ − δf‖ + ‖Ψ(u′, z) − Ψ(ũ′, z)‖).

At fixed z, u′ ↦ T_(u′)z is continuous, the constraint map is continuous in the background and the datum by the same
product estimates, and ♯_(g′) is continuous in g′ ([[lem:s28-setting]] (e)); so the last term tends to zero as ũ′ → u′.
As e^(2s/x) : 𝒮 → 𝒵̃ and π₀ are bounded and ♯_(g′) is continuous in g′, δf̃ → δf as
(ũ′, (δJ̃, δρ̃)) → (u′, (δJ, δρ)). The continuity of T_(u′)z in 𝒳 follows from that of z and of T_(u′).

(c) Apply [[thm:std-cd-uniform-inverse]] with A := 𝒩_(ε_c), V_(u′) := 𝒴, W_(u′) := 𝒵, r := r_c and
f_(u′) := Ψ(u′, ·) on B. Hypothesis 1 holds by [[lem:s28-setting]] (d), the inverse of D_zΨ(u′, 0) being a right
inverse of norm at most C₁. Hypothesis 3 is the bound with C₃ in the proof of (a). Hypothesis 2 follows from it: for
v, v + h ∈ B, B being convex,

    f_(u′)(v + h) − f_(u′)(v) − Df_(u′)(v)h = ∫₀¹ (Df_(u′)(v + θh) − Df_(u′)(v))h dθ,

of norm at most C₃‖h‖²/2. So there are ε_G and C_G such that for u′ ∈ 𝒩_(ε_c) and δf ∈ 𝒵 with ‖δf‖_𝒵 < ε_G there is
z ∈ B with Ψ(u′, z) − Ψ(u′, 0) = δf and ‖z‖_𝒴 ≤ C_G‖δf‖_𝒵; and Ψ(u′, 0) = 0. Take δf := π₀♯_(g′)e^(2s/x)(δJ, δρ). By
[[lem:s28-setting]] (e) and *The spaces*, ‖δf‖_𝒵 ≤ C₆‖(δJ, δρ)‖_𝒮 with C₆ independent of u′. For
‖(δJ, δρ)‖_𝒮 < ε_G/C₆ this gives z ∈ B with Ψ(u′, z) = δf, that is, by [[lem:s28-setting]] (a), a solution
(δK, δg) = T_(u′)z of [[eq:v-3-1]], with ‖z‖_𝒴 ≤ C_GC₆‖(δJ, δρ)‖_𝒮 and ‖(δK, δg)‖_𝒳 ≤ ‖T_(u′)‖‖z‖_𝒴, ‖T_(u′)‖ being
bounded uniformly.

Now let (δK′, δg′) = e^(−2s/x)Φ²P*_(u′)(Y, N), (Y, N) ∈ 𝒴_(g′), be the solution of [[lem:s28-setting]] (a), and
z′ := π₀(Y, N), so that (δK′, δg′) = T_(u′)z′ and Ψ(u′, z′) = δf ([[lem:s28-setting]] (a)). As
D_zΨ(u′, 0) = π₀♯_(g′)e^(2s/x)D(J, ρ)(u′)T_(u′), the inverse bound of [[lem:s28-setting]] (d) and the uniform bound on
the derivative of the constraint map in the proof of (a) give a constant C₄, independent of u′, with

    ‖z′‖_𝒴 ≤ C₁‖D_zΨ(u′, 0)z′‖_𝒵 ≤ C₁C₄‖T_(u′)z′‖_𝒳.

Diminishing ε_s, and with it the ε of [[lem:s28-setting]] (a), the solution of [[lem:s28-setting]] (a) has
‖T_(u′)z′‖_𝒳 < r_c/(C₁C₄), in the form in which that lemma uses "close to zero". Then z′ ∈ B, and z′ = z by (a). ∎

**Lemma {#lem:v-3-3}** ([CD03, Lemma 3.18, p. 19].) Let U′, V′ ⊂ ℝ^D be open, f : U′ → V′ a homeomorphism, and
f_R : U′ → ℝ^D, R ≥ R′, continuous maps with f_R → f uniformly on U′ as R → ∞. For every y ∈ V′ and every R large
there is v_R ∈ U′ with f_R(v_R) = y. If the closed ball B̄(y, r′) lies in V′, v_R can be taken in f⁻¹(B̄(y, r′)).

*Proof.* u_R := Id − f_R ∘ f⁻¹ tends to 0 uniformly on B̄(y, r′). Once max over B̄(y, r′) of |u_R| is at most r′, the
map z ↦ y + u_R(z) is continuous from B̄(y, r′) to itself and has a fixed point y_R by Brouwer's fixed point theorem.
Then v_R := f⁻¹(y_R) satisfies f_R(v_R) = y_R − u_R(y_R) = y. ∎

#### The gluing theorem {#sec:s28-gluing-theorem}

**Theorem {#thm:v-3-1}** ([CD03, Theorem 8.1 and Remark 8.4] in space dimension 4.) Let (g, K) be smooth vacuum data
on {r > R₀} ⊂ ℝ⁴ with |||(g, K)|||_(α,7) < ∞ for some α ∈ (3/2, 2], and with charge vector
𝔔⁰ := (𝔔_X(g, K))_X ∈ V. There is R_gl such that for every R ≥ R_gl there are p_R ∈ U and smooth vacuum data
(ĝ_R, K̂_R) on {r > R₀} that equal (g, K) on {r ≤ R} and (g_(p_R), K_(p_R)) on {r ≥ 4R}. Moreover 𝔮(p_R) → 𝔔⁰ as
R → ∞.

*Proof.* Enlarging R₀, |g − δ| ≤ ½ on {r > R₀}; this is assumed below. Fix k := 3, the least integer above n/2. The
proof has five steps.

*Step 1: the solvability statement on the annulus.* Apply [[sec:s28-solvability]] with 𝒜 := Γ̄(1, 4), a compact
manifold with boundary, n = 4, x ∈ C^∞(𝒜) a radial defining function of ∂𝒜 (a function of r) with 0 < x ≤ 1 in the
interior that equals the Euclidean distance to ∂𝒜 near it, u₀ := (0, δ), s := 1 and k = 3. Such an x exists, the
distance min(r − 1, 4 − r) being radial: take x := h(r) with h smooth, 0 < h ≤ 1 on (1, 4), h(r) = r − 1 near 1 and
h(r) = 4 − r near 4. Hypothesis (Fin) holds: 𝒦₀ is the restriction of 𝔎 to 𝒜, with the basis [[eq:v-0-4]]. Indeed, the
fifteen elements of 𝔎 are polynomials, bounded with all derivatives on 𝒜, and ψ² is integrable, so they lie in
H̊¹_(x²,ψ) × H̊²_(x²,ψ) (*The spaces* in [[sec:s28-solvability]]), and P*_((0,δ)) annihilates them ([[lem:v-1-1]]); and
an element of the kernel of ΦP*_((0,δ)) is
annihilated by P*_((0,δ)), Φ being multiplication by positive functions, so it is smooth in 𝒜° by interior regularity
and is one of them by [[lem:v-1-1]], 𝒜° being connected. The elements of 𝔎 are polynomials, linearly independent on
every open set. A pair (K′, g′) with ‖K′‖_(C^(k+3)(𝒜)) + ‖g′ − δ‖_(C^(k+4)(𝒜)) < ε lies in 𝒩_(Cε), as x ≤ 1, C
depending only on x. So [[lem:s28-setting]] and [[lem:v-3-2]] apply: for such (K′, g′), ε small, and (δJ, δρ) ∈ 𝒮 of
small norm, [[eq:v-3-1]] has a solution (δK, δg) = T_(u′)z, u′ := (K′, g′), with z ∈ B, unique there, continuous in
(u′, (δJ, δρ)), with ‖(δK, δg)‖_(C²(𝒜)) ≤ C‖(δJ, δρ)‖_𝒮 ([[lem:v-3-2]] (c), [[lem:s28-setting]] (c)); and when
(K′, g′) ∈ C^∞(𝒜) and (δJ, δρ) ∈ C^∞_c(𝒜°) is supported in Γ̄(2, 3) with C^(k+2)(𝒜)-norm small enough, (δK, δg) ∈ C^∞(𝒜)
and extends smoothly by zero across ∂𝒜 ([[lem:v-3-2]] (c), and [[lem:s28-setting]] (b) with Ω_c := Γ̄(2, 3)).

*Step 2: the approximate data.* Fix a radial χ ∈ C^∞(ℝ⁴) with 0 ≤ χ ≤ 1, χ = 1 for r ≤ 2 and χ = 0 for r ≥ 3. Let
B̄ ⊂ V be a closed ball about 𝔔⁰. For R ≥ max(2R₀, R_P) and Q ∈ B̄ put

    u_(Q,R) = (K_(Q,R), g_(Q,R)) := χ 𝒮_R(K, g) + (1 − χ) 𝒮_R(K_(p(Q)), g_(p(Q)))     on 𝒜.

Then:

(a) ‖K_(Q,R)‖_(C^(k+3)(𝒜)) + ‖g_(Q,R) − δ‖_(C^(k+4)(𝒜)) ≤ CR^(−α), uniformly for Q ∈ B̄, and Q ↦ u_(Q,R) is continuous
into C^(k+3) × C^(k+4)(𝒜). Indeed |∂^γ_y(𝒮_Rg − δ)(y)| = R^(|γ|)|∂^γ(g − δ)(Ry)| ≤ CR^(−α) and
|∂^γ𝒮_RK| ≤ CR^(−α) for |γ| ≤ k + 4 = 7 (resp. 6). The member's data obey the same bounds with α replaced by 2 ≥ α,
uniformly in p, and depend smoothly on p ([[lem:v-2-2]]), and p(Q) is continuous ([[cor:v-2-4]]).

(b) (J, ρ)(u_(Q,R)) is supported in Γ̄(2, 3), with C^(k+2)-norm at most CR^(−α). On Γ(1, 2) and Γ(3, 4) the data are
rescaled vacuum data, hence vacuum by [[lem:v-1-4]]. The constraint map is a smooth function of the 2-jet vanishing
at (0, δ).

By (b), (δJ, δρ) := −(J, ρ)(u_(Q,R)) is smooth and supported in Γ̄(2, 3) ⊂ 𝒜°, where x is bounded below, so its
weighted norms are at most C‖·‖_(C^(k+1)) ≤ CR^(−α); and its C^(k+2)-norm, which bounds the norm of
[CD03, Proposition 5.10] ([[lem:s28-setting]] (b) with Ω_c := Γ̄(2, 3)), is at most CR^(−α) by (b). Let R_ε be such
that these bounds, and the bound of (a), are below the thresholds of Step 1 for R ≥ R_ε. For R ≥ R_ε, Step 1 gives a
smooth δu_(Q,R) on 𝒜 that extends by zero, with ‖δu_(Q,R)‖_(C²(𝒜)) ≤ CR^(−α), continuous in Q. Put
û_(Q,R) := u_(Q,R) + δu_(Q,R); by [[eq:v-3-1]], with g′ := g_(Q,R), π_(g′)♯_(g′)e^(2s/x)(J, ρ)(û_(Q,R)) = 0.

*Step 3: the obstruction is a pairing.* By [[lem:s28-setting]] (e), the kernel of π_(g′), g′ := g_(Q,R), is 𝒦₀. So
♯_(g′)e^(2s/x)(J, ρ)(û_(Q,R)) ∈ 𝒦₀, that is, on 𝒜°,

    (J, ρ)(û_(Q,R)) = e^(−2s/x) ♭_(g′) Σ_i κ_i e_i     for some κ ∈ ℝ¹⁵,

the e_i = (Y_i, N_i) being the basis [[eq:v-0-4]]: in Cartesian components J_a = e^(−2s/x) Σ_i κ_i g′_(ab)Y_iᵇ and
ρ = e^(−2s/x) Σ_i κ_iN_i. Let

    F_R(Q)_j := ∫_𝒜 (Y_jᵃJ_a + N_jρ)(û_(Q,R)) dμ_(ĝ_(Q,R)),

ĝ_(Q,R) the metric of û_(Q,R). Then F_R(Q) = 𝒢′κ with 𝒢′_(ji) := ∫_𝒜 (g′(Y_j, Y_i) + N_jN_i) e^(−2s/x) dμ_(ĝ). As in
[CD03, (8.6)], F_R pairs the residual with the Killing initial data themselves. As g′, ĝ → δ in C⁰(𝒜) uniformly on B̄,
𝒢′ → 𝒢, 𝒢_(ji) := ∫_𝒜 (Y_j · Y_i + N_jN_i) e^(−2s/x) dx, the Gram matrix, for a positive measure, of functions that are
linearly independent on every open set. So 𝒢 is positive definite, and there is R_𝒢 such that 𝒢′ is invertible for
R ≥ R_𝒢 and Q ∈ B̄. Then (J, ρ)(û_(Q,R)) = 0 if and only if κ = 0, if and only if F_R(Q) = 0. F_R is continuous on B̄,
its integrand depending continuously on û_(Q,R) in C²(𝒜).

*Step 4: the pairing's asymptotics.* Let 𝔵 = (K̂, ĝ) := 𝒮_R⁻¹û_(Q,R) on Γ(R, 4R). By [[lem:v-1-4]] and then
[[eq:v-1-1]],

    F_R(Q)_j = R^(−2−d_j) [ ∮_(S_(4R)) 𝔟_(e_j)(𝔵) − ∮_(S_R) 𝔟_(e_j)(𝔵) + ∫_(Γ(R,4R)) q_(e_j)(𝔵) dx ],     d_j := d(e_j).

Near S_(4R), 𝔵 is the member's data with all derivatives, since χ = 0 for r ≥ 3 and δu_(Q,R) vanishes to infinite
order at ∂𝒜. So [[eq:v-1-3]] with α = 2 and [[cor:v-2-4]] give ∮_(S_(4R)) 𝔟_(e_j) = Q_j + O(R^(d_j−2)), uniformly on B̄.
Near S_R, 𝔵 = (g, K), so ∮_(S_R) 𝔟_(e_j) = 𝔔⁰_j + O(R^(2+d_j−2α)). On Γ(R, 4R), unscaling the bounds of Step 2 gives
|∂^γ(ĝ − δ)| ≤ CR^(−α−|γ|) (|γ| ≤ 2) and |∂^γK̂| ≤ CR^(−α−1−|γ|) (|γ| ≤ 1). With [[eq:v-1-2]] and |e_j| ≤ CR^(d_j),
∫|q_(e_j)| ≤ CR^(d_j)R^(−2α−2)R⁴. As α ≤ 2, d_j − 2 ≤ 2 + d_j − 2α, so

    F̂_R(Q) := (R^(2+d_j)F_R(Q)_j)_j = Q − 𝔔⁰ + O(R^(3−2α))     uniformly on B̄,                              {#eq:v-3-2}

and 3 − 2α < 0. (The power R^(−2−d_j) is R^(−(n−2)−d_j) at n = 4; [CD03, (8.7)] prints R⁻¹ for every charge at n = 3.)

*Step 5: conclusion.* Apply [[lem:v-3-3]] with U′ the interior of B̄, f(Q) := Q − 𝔔⁰, f_R := F̂_R for
R ≥ R′ := max(2R₀, R_P, R_ε, R_𝒢), and y = 0. For every r′ > 0 below the radius of B̄ there is R(r′) ≥ R′ such that for
R ≥ R(r′) some Q_R with |Q_R − 𝔔⁰| ≤ r′ has F̂_R(Q_R) = 0; put R_gl := R(r′₀) for one such r′₀. Then F_R(Q_R) = 0 and,
by Step 3, as R ≥ R_𝒢, (J, ρ)(û_(Q_R,R)) = 0. Put p_R := p(Q_R), and let (ĝ_R, K̂_R) be (g, K) on {R₀ < r ≤ R}, 𝒮_R⁻¹û_(Q_R,R) on
Γ(R, 4R) and (g_(p_R), K_(p_R)) on {r ≥ 4R}. These are smooth, as χ is constant near ∂𝒜 and δu extends smoothly by
zero. They are vacuum everywhere, and ĝ_R is Riemannian, being C⁰-close to δ on Γ(R, 4R). Finally 𝔮(p_R) = Q_R.
Choose Q_R for an admissible r′ = r′(R) ≤ 2 inf{r′ : R ≥ R(r′)} + R⁻¹, which exists as R ≥ R(r′₀), and tends to 0 as
R → ∞, since every r′ > 0 is admissible once R ≥ R(r′). Then 𝔮(p_R) → 𝔔⁰. ∎

**Remark {#rem:v-3-4}** (What the settling theorem takes from [[thm:v-3-1]].) The data (ĝ_R, K̂_R) equal, for
r ≥ 4R, the data that 𝔤_(p_R) = 𝒫_(p_R)*g^KS_(m,A) induces on {y⁰ = 0}. By uniqueness for the vacuum Cauchy problem,
their development contains the domain of dependence of {r > 4R} in 𝔤_(p_R): a Poincaré transform of a Myers–Perry
metric with parameters near b₀. The proof of [[thm:settling]] uses only the proof of [[thm:v-3-1]], in the class form
[[prop:vii-2-2]], with Tangherlini members on Σ^IVP. The members of [[def:v-2-1]] lie on the slices {y⁰ = 0} of
Kerr–Schild time, and there the second fundamental form differs from the one induced on Σ^IVP by
∇²f + |x|⁻⁴C^∞(X̄), with f the height function of the graph Σ^IVP = {t_KS = f(|x|)} far out
([[pending:after-shell-mp-data-on-sigma-ivp]]). So the glued data of [[thm:v-3-1]] are not small in the data class
[[eq:vii-0-1]] of [[thm:iii-k-4-3]] at any R. Gluing a decaying perturbation with smallness in that class takes the
members on Σ^IVP ([[ch:after-shell]]).

**Remark {#rem:s28-cd03}** ([CD03, Section 8.1] in space dimension 4.) [CD03, (8.1)] asks the parity condition (E.9)
so that the angular momentum and the centre of mass converge and so that the errors of [CD03, (8.6)] lie below the main
terms. In space dimension 4 with α > 3/2 both follow from the decay alone, since 2α > n − 1 = 3 ([[prop:v-1-3]],
[[eq:v-3-2]]). The members of [[def:v-2-1]] are taken in Kerr–Schild form, where the shift is odd and of the same order
r⁻² as the metric, which (E.9) would exclude. The convergence rate of [CD03, (8.3)] is β = min(α, n − 2), printed as
min(α, 1), and the power of R in [CD03, (8.7)] is R^(−(n−2)−d). [CD03, Theorem 5.6] states s ≥ n − 2 where its proof
uses s ≥ n − 1, and [CD03, (8.5)] applies it with s = t − 1 where its solution space requires s = t + n − 2; the
exponentially weighted spaces of [CD03, Theorem 5.9], which [CD03] uses for smooth data, avoid both. [CD03, Theorem
3.19] applies [CD03, Lemma 3.18] to the maps of [CD03, (3.29)], which must be continuous in Q; this is
[[lem:v-3-2]]. Finally the projection of [CD03] is orthogonal in L²_ψ of the current metric, so the obstruction it
leaves is 𝒞_(g′)⁻¹𝒦₀ ([[lem:s28-setting]] (e)), and Step 3 pairs with these converted Killing initial data, whose Gram
matrix tends to the flat one.

### Gluing in the symmetry class {#sec:vii-2}

In this section b₀ = (m₀, 0), Σ^IVP is the hypersurface of [[sec:iii-b-3-3]], identified with X = cl{|x| ≥ r_♭} by
(t, x) ↦ x, and G = O(2) × O(2) acts on ℝ⁴ as in [[sec:class]] and on spacetime by (t, x) ↦ (t, Ox), O ∈ G ⊂ O(4).
Every element of O(4), acting so, is an isometry of every g^KS_(m,0) and fixes every function of (t, |x|). The fixed
spaces are (ℝ⁴)^G = 0 and 𝔰𝔬(4)^G = 0: the torus T² ⊂ G fixes in ℝ⁴ only 0, and in 𝔰𝔬(4) exactly span(W₁₂, W₃₄),
while x₂ ↦ −x₂ reverses W₁₂ and x₄ ↦ −x₄ reverses W₃₄. So 𝔎^G = span(e₀).

For |x| ≥ R₃, Σ^IVP = {t = C″} ([[lem:iii-b-3-7]] (b)), that is {t_KS = f(|x|)} with f := C″ − T_(m₀)(|x|) in the
Kerr–Schild time t_KS = t − T_(m₀)(|x|) of [[eq:iii-b-3-3]]. For m ∈ I_m := [¾m₀, (5/4)m₀], let (γ^m, k^m) be the data
that g^KS_(m,0) induces on this graph over {|x| > R₃}, as tensors on {|x| > R₃}. At m = m₀ they are (γ_(b₀), k_(b₀)) of
[[lem:iii-b-3-9]].

**Lemma {#lem:vii-2-1}** (Tangherlini on Σ^IVP.) (a) γ^m − δ ∈ |x|⁻²C^∞(X̄) and k^m ∈ |x|⁻³C^∞(X̄) on the
compactified {|x| > R₃}, smoothly in m ∈ I_m, and γ^m − γ_(b₀), k^m − k_(b₀) have seminorms O(|m − m₀|). In particular
|||(γ^m, k^m)|||_(2,j) ([[eq:v-0-3]]) is bounded for every j, uniformly in m. (b) (γ^m, k^m) are vacuum and
O(4)-invariant. (c) Their charges ([[prop:v-1-3]]) are 𝔔_(e₀) = 6π²m and 𝔔_X = 0 for X in the other three groups of
[[eq:v-0-4]].

*Proof.* (a) g^KS_(m,0) − η = (m/r²) ℓ ⊗ ℓ with ℓ = dt_KS + x̂ · dx, independent of t_KS and a classical symbol of order
−2 in x, smoothly in m, and f′ ∈ |x|⁻²C^∞ near infinity ([[lem:iii-b-3-5]] (a)). The induced metric
g_ij + 2g_(t(i)∂_(j)f + g_tt∂_if∂_jf and the second fundamental form ([[eq:v-0-2]] for the graph) are smooth functions
of the components of g^KS_(m,0) at (f(x), x), which do not depend on the first argument, and of (∂f, ∂²f). They equal
(δ, 0) at g = η, f constant. This gives the symbol classes, and the m-derivatives are symbols of the same orders.
(b) g^KS_(m,0) is Ricci-flat ([[prop:iii-b-3-4]]), and O(4) acts by its isometries, preserving the graph. (c) The
charges are limits of the fluxes ∮_(S_ϱ) 𝔟_X of [[eq:v-1-1]]. The flux integrand is natural for the Euclidean
structure, so on O(4)-invariant data X ↦ 𝔔_X is an O(4)-invariant linear form on 𝔎. It therefore vanishes on the
summands ℝ⁴, Λ²ℝ⁴, ℝ⁴, which are irreducible and nontrivial. 𝔟_(e₀) = (∂_jh_ij − ∂_i tr h)νⁱdS involves only
h = γ − δ. On the graph, γ^m_ij differs from the metric induced on {t_KS = 0} by 2g_(t(i)∂_(j)f + g_tt∂_if∂_jf = O(r⁻⁴),
with first derivatives O(r⁻⁵), as g_ti = (m/r²)x̂_i. So the two fluxes over S_ϱ differ by O(ϱ⁻²), and 𝔔_(e₀) is that of
{t_KS = 0}, which is 6π²m by the part *c_E* of the proof of [[prop:v-2-3]], at p = (m, 0, 0, 0). ∎

**Proposition {#prop:vii-2-2}** (Gluing in the class; [CD03, Theorem 8.1] with G.) Fix k ≥ 3, the order of the
gluing. There are R_gl, ζ₀ and C such that for R ≥ max(R_gl, R₃) the following holds. Let (g, K) be G-invariant
smooth vacuum data on Σ^IVP ∩ {r_♭ ≤ r ≤ 3R} with

    ζ := sup_(R≤r≤3R) ( Σ_(|β|≤k+4) r^(2+|β|)|∂^β(g − γ^(m₀))| + Σ_(|β|≤k+3) r^(3+|β|)|∂^β(K − k^(m₀))| ) ≤ ζ₀.
                                                                                                          {#eq:vii-2-1}

Then there are m with |m − m₀| ≤ Cζ, and G-invariant smooth vacuum data (ĝ, K̂) on Σ^IVP, equal to (g, K) on {r ≤ R}
and to (γ^m, k^m) on {r ≥ 4R}, with

    sup_(R≤r≤4R) ( Σ_(|β|≤k−1) r^(2+|β|)|∂^β(ĝ − γ^(m₀))| + Σ_(|β|≤k−2) r^(3+|β|)|∂^β(K̂ − k^(m₀))| ) ≤ Cζ.
                                                                                                          {#eq:vii-2-2}

*Proof.* The proof of [[thm:v-3-1]], with k in place of 3 ([[sec:s28-solvability]] allows any integer k > n/2), and
seven changes.

(1) *The data used.* Steps 2–5 use (g, K) only on Γ(R, 3R) (in Step 2, χ = 0 for r ≥ 3), and through 𝔔⁰ in Step 4.
Replace 𝔔⁰ by the fluxes 𝔔⁰_R := (∮_(S_R) 𝔟_(e_j)(g − δ, K))_j; Step 4's term at S_R is then exactly 𝔔⁰_R.

(2) *The family.* Replace the members by (γ^m, k^m), m ∈ I_m. [[lem:vii-2-1]] (a) gives the bounds of Step 2 (a), with
α = 2, and continuity in m. The smallness of Step 1 holds for R ≥ R_gl: the rescaled u_(m,R) is within
C(m₀ + ζ₀)R⁻² of (0, δ).

(3) *Equivariance.* G acts on data on 𝒜 = Γ̄(1, 4) by pull-back, commuting with the rescaling 𝒮_R. For G-invariant
u′ = (K′, g′), the map Ψ(u′, ·) of [[eq:s28-psi]] is G-equivariant. Indeed, the constraint map is natural, x and the
weights e^(±s/x), x² are radial, T_(u′) is natural, and π_(g′) commutes with G, as 𝒦₀ = 𝔎|_𝒜 and the L²_ψ(g′) inner
product are G-invariant. The norms of Step 1 are G-invariant. So the solution of [[eq:v-3-1]] with z in the ball B of
[[lem:v-3-2]] is unique, hence G-invariant when u′ and the right side are, and û_(m,R) := u_(m,R) + δu_(m,R) is
G-invariant.

(4) *A one-dimensional obstruction.* By Step 3, (J, ρ)(û_(m,R)) = e^(−2s/x) Σ_i κ_i 𝒞_(g′)⁻¹e_i, which is G-invariant.
𝒞_(g′) commutes with G, so Σ_i κ_ie_i ∈ 𝔎^G = span(e₀). Hence (J, ρ)(û_(m,R)) = 0 if and only if κ₀ = 0, if and only
if F_R(m)₀ = 𝒢′₀₀κ₀ = 0, where 𝒢′₀₀ > 0 (Step 3).

(5) *A zero.* Step 4 at j = 0 with α = 2 gives G_R(m) := R²F_R(m)₀ = 6π²m − 𝔔⁰_(R,0) + O(R⁻¹), uniformly on I_m. By
[[eq:vii-2-1]] and [[lem:vii-2-1]], 𝔔⁰_(R,0) = 6π²m₀ + O(ζ) + O(R⁻²). So for R large and ζ₀ small,
G_R(¾m₀) < 0 < G_R((5/4)m₀). G_R is continuous (Step 3), so it has a zero m, by the intermediate value theorem in place
of [[lem:v-3-3]].

(6) *The mass bound.* At m the data û are vacuum. [[lem:v-1-2]] with X = e₀ on Γ(R, 4R), unscaled, gives

    ∮_(S_(4R)) 𝔟(γ^m, k^m) − ∮_(S_R) 𝔟(g, K) + ∫_(Γ(R,4R)) q_(e₀)(û) dx = 0.

The same lemma on Γ(4R, ϱ) for (γ^m, k^m), and on Γ(R, ϱ) for (γ^(m₀), k^(m₀)), with ϱ → ∞ ([[lem:vii-2-1]] (c);
|q| ≤ Cr⁻⁶ is integrable), gives ∮_(S_(4R)) 𝔟(γ^m, k^m) = 6π²m + ∫_(r>4R) q(γ^m) and
∮_(S_R) 𝔟(γ^(m₀), k^(m₀)) = 6π²m₀ + ∫_(r>R) q(γ^(m₀)). By [[eq:vii-2-1]], ∮_(S_R) 𝔟(g, K) differs from the latter flux
by at most Cζ. Hence

    6π²(m − m₀) = ∫_(Γ(R,4R)) (q(γ^(m₀)) − q(û)) + ∫_(r>4R) (q(γ^(m₀)) − q(γ^m)) + O(ζ).

Write a := 𝒮_R(g, K) and b := 𝒮_R(γ^m, k^m); both are vacuum, and u_(m,R) = b + χ(a − b). The constraint map is smooth
near flat data and vanishes at b. So the right side of Step 1 has
‖(J, ρ)(u_(m,R))‖_(C^(k+1)) ≤ C‖a − b‖_(C^(k+3) × C^(k+4)) ≤ C(ζ + |m − m₀|)R⁻². By the bound of Step 1, δu_(m,R) is of
the same size in H^(k+2)(𝒜) ⊂ C^(k−1)(𝒜). On 𝒜,
û_(m,R) − 𝒮_R(γ^(m₀), k^(m₀)) = χ(a − 𝒮_R(γ^(m₀), k^(m₀))) + (1 − χ)(b − 𝒮_R(γ^(m₀), k^(m₀))) + δu_(m,R); unscaled,
the difference û − (γ^(m₀), k^(m₀)), û := 𝒮_R⁻¹û_(m,R), has |h| ≤ C(ζ + |m − m₀|)R⁻², with each derivative, and K, a
further factor R⁻¹. Both û and (γ^(m₀), k^(m₀)) have |h| ≤ CR⁻² with the same scaling. q_(e₀) is a smooth function
of (h, ∂h, ∂²h, K, ∂K) vanishing to second order at 0 (the proof of [[lem:v-1-2]]), with the quadratic bound
[[eq:v-1-2]]. So |q(û) − q(γ^(m₀))| ≤ C(ζ + |m − m₀|)R⁻⁶ on
Γ(R, 4R), and |q(γ^m) − q(γ^(m₀))| ≤ C|m − m₀|r⁻⁶. Integrating, 6π²|m − m₀| ≤ C(ζ + |m − m₀|)R⁻² + Cζ, so
|m − m₀| ≤ Cζ for R large.

(7) *The bound [[eq:vii-2-2]] and the conclusion.* û − (γ^(m₀), k^(m₀)) is the sum of χ times the data's deviation,
(1 − χ)(γ^m − γ^(m₀), k^m − k^(m₀)) and δu. These are bounded in the norm of [[eq:vii-2-2]] by ζ, by C|m − m₀| ≤ Cζ
([[lem:vii-2-1]] (a)), and by Cζ (from (6), rescaled). The glued data are smooth, vacuum and Riemannian as in Step 5 of
the proof of [[thm:v-3-1]], and G-invariant by (3). ∎

**Remark {#rem:s28-mass-bound}** (The mass bound.) [[prop:vii-2-2]] adds to the proof of [[thm:v-3-1]] the
equivariance of its Step 1, a one-dimensional obstruction, and the a priori bound |m − m₀| ≤ Cζ from the flux identity.
The bound makes the glued data close to Tangherlini, by a multiple of ζ, at a fixed gluing radius (by O(λ) in
[[cor:vii-2-3]]), which the weighted norm of the data class [[eq:vii-0-1]] of [[thm:iii-k-4-3]] needs: a bump of
relative size R⁻¹ at radius R has, in that norm, size about R^(ℓ_0−3), which grows with R, ℓ_0 ∈ (3, 4) being the weight
of the class.

**Corollary {#cor:vii-2-3}** (The data of item (i) of [[thm:settling]].) Let b₀ = (μ_end, 0), so that m₀ = μ_end. Let
k ≥ 3 and R ≥ max(R_gl, R₃), and let c₀ and Ω′ be as in [[lem:vii-1-2]]. Take J = k + 5 in [[lem:vii-1-1]], and let
(g, K) be the data of g_λ on Σ^IVP ∩ {r_♭ ≤ r ≤ 4R}. Then [[eq:vii-2-1]] holds with ζ ≤ C_Rλ, and for λ small
[[prop:vii-2-2]] gives (γ_λ, k_λ) := (ĝ, K̂) and m_λ := m, with |m_λ − μ_end| ≤ C_Rλ. If k ≥ d_1 + 5, d_1 the order of
[[thm:iii-k-4-3]], then also ‖(γ_λ − γ_(b₀), k_λ − k_(b₀))‖_(d_1) ≤ C_Rλ, in the norm of the data class of
[[thm:iii-k-4-3]] ([[eq:vii-0-1]]).

*Proof.* The data a metric induces on a fixed spacelike slice are smooth functions of its components and their first
derivatives at the slice. By [[lem:vii-1-2]] the slice piece lies in Ω′_+, where the background g0 equals g_(b₀), so by
[[lem:vii-1-1]] the data of g_λ differ from (γ_(b₀), k_(b₀)) = (γ^(μ_end), k^(μ_end)) by Cλ in C^(k+4) there. With the
weights r^(2+|β|) ≤ (3R)^(k+6), ζ ≤ C_Rλ. The data are G-invariant (g_λ and Σ^IVP are, [[lem:vii-1-1]] and
[[lem:vii-1-2]]) and vacuum. For the last claim apply [[lem:vii-0-1]] with R′ = 4R: on {r ≤ 8R} the deviation is
C_Rλ in C^(d_1+3), by [[lem:vii-1-1]], [[eq:vii-2-2]] and [[lem:vii-2-1]] (a), and on {r ≥ 4R} it is
(γ^m − γ_(b₀), k^m − k_(b₀)), whose seminorms are O(|m − μ_end|) = O(λ). ∎
