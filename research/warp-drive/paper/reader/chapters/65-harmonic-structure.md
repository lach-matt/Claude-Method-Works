## The linear solution in harmonic gauge, I: structure, the horizon charge and decay modulo W* {#ch:harmonic-structure}

[[ch:rw-gauge]] determined the gauge vector that carries the linear solution of [[cor:viii-2-3]] to a
Regge–Wheeler-type gauge. This chapter and the next do the same for the harmonic gauge Θ(ġ) = 0, in which the
linearised vacuum equation is the Lichnerowicz wave equation; in four dimensions the passage is Hung's [Hun19]. In
the class the harmonic-gauge solutions with the data of ġ are ġ_RW + ṁℒ_(W**_H)g + ℒ_(Z′)g, where □Z′ is a forcing
term with no spherically symmetric part and the spherically symmetric part of Z′ is free ([[prop:gd-2-1]]). The
structure of the
passage is explicit ([[prop:np-10-2]]): the tensor part is in harmonic gauge already, each scalar mode of the gauge
vector solves three coupled 1 + 1 wave equations with the master field as source, and the spherically symmetric sector
has two solutions that do not decay, the stationary 1-form W* and a gauge-fixed mass change K* that grows linearly in
the ingoing time v, with a coefficient ½ that regularity at the horizon forces. A conserved horizon charge
([[lem:gd-2-2]]) shows that the growth cannot be avoided: when the mass changes, no harmonic-gauge solution settles
to a change of mass near the horizon at an integrable rate ([[thm:gd-2-3]]).

The decay of the gauge vector modulo W* rests on the 1-form wave operator □ at zero energy, where its kernel is
spanned by W* and the annihilator of its range by the horizon functional ℓ ([[lem:iii-d1-2-1]]). Augmenting the
spectral family by one cut-off state, whose pairing with ℓ is 4π² ([[prop:gd-r2-3]]), the analysis of [[ch:s18]]
carries over with one state in place of eleven: □ is 1-admissible with sf-loss 0 ([[thm:gd-r2-5]]), and the forward
solution of □u = f is c_fW* + O(t_*^(−1/2)) on compact sets, where 4π²c_f is the horizon charge that f has injected
([[thm:gd-r2-7]]). The forcing term of the gauge vector of [[thm:viii-2-2]]'s solution is algebraic in h near K⁺
([[lem:gd-r2-10]]), with the ι⁺-decay that the constraint damping gives ([[prop:gd-r3-2]]), and near ℐ⁺ it does not
see the radiation field ([[lem:gd-r3-5]]). With an estimate for □ near spatial and null infinity ([[prop:gd-r4-2]],
[[thm:gd-r4-3]]), every perturbation in the class has a representative that is in harmonic gauge on all of N⁺,
induces the given data exactly, and settles on compact sets to ṁK* + c_∞ℒ_(W*)g at the rate t_*^(−1/2)
([[cor:gd-r4-4]]); its spherically symmetric part is exactly ṁK* + ℒ_(Z′_0)g with □Z′_0 = 0 ([[prop:gd-r2-13]]). The
forward solution of □ improves at positive K⁺-weight ([[thm:gd-r5-1]], [[thm:gd-r5-2]]); the rates that follow from
this, and the representative's rate, are in [[ch:harmonic-rate]].

### Setting {#sec:hg-setting}

Everything of [[sec:rw-setting]] is kept: g = g_(b₀), the Schwarzschild–Tangherlini metric of mass m₀, in the ingoing
chart g = −f dv² + 2 dv dr + r²γ on {r ≥ r_♭} ([[eq:rw-ingoing]]), f = 1 − m₀/r², r_h = m₀^(1/2); the class, G =
O(2) × O(2); K := r⁻²dv² and K_V = K + ℒ_Vg, with ℒ_Vg = 0 on {r ≤ 2R₁} ([[eq:gd-0-1]]); the linear solution ġ of
[[cor:viii-2-3]], its mass change ṁ, h := ġ − ṁK_V and w := α − 2 > 2 + ε_t; the seminorms |·|_k, the bound
[[eq:gd-0-2]], and the l = 0 part of a class tensor ([[sec:rw-spheres]]); the operators D, □ on the orbit space
and D̂, Δ̂ on (S³, γ), with dω the measure of γ and |S³| = 2π²; and the representative ġ_RW = ġ + ℒ_(X_RW)g of
[[thm:rw-settling]]. We put

    e := ġ_RW − ṁK_V,

so that e_0 = 0 ([[thm:rw-settling]] (a)). The domains are those of [[sec:ix-0]]: U^♯, Σ° and N⁺ = M°_♭ ∩ {t_IVP ≥ 0},
with Ω^♯ := D_(U^♯)(Σ°) and Ω^♯ ∩ {t_IVP ≥ 0} = N⁺ ([[lem:ix-1-2]]); "smooth up to Σ°" is as there. (Dyn) holds at
b₀ for every operator with principal symbol G Id ([[thm:vi-a-6-1]]), so the results of [[ch:s13]] stated under it
apply to □ below. The curvature is written with [∇_α, ∇_β]ω_λ = −R^σ_(λαβ)ω_σ and Ric_(λβ) = R^σ_(λσβ).

*Operators.* As in [[sec:ix-0]]: (δk)_μ = −∇^αk_αμ, Gk = k − ½g tr_g k, δ* the symmetrised covariant derivative and
Θ(k) := δGk. We identify vector fields and 1-forms by g and write ℒ_Xg for ℒ_(X^♯)g, so that ℒ_Xg = 2δ*X. Put

    □ := 2δGδ*   on 1-forms,        so that   Θ(ℒ_Xg) = □X.                                              {#eq:hg-box}

At the Ricci-flat g, □ = −∇^α∇_α ([[lem:ix-2-1]] (a)) = dδ + δd ([[sec:iii-d-1]]), and on functions we write
□_0 := δd = −∇^α∇_α. A symmetric 2-tensor k is in *harmonic gauge* if Θ(k) = 0. For 1-forms a, b put
a ⊗_s b := ½(a ⊗ b + b ⊗ a); then ℒ_(cX)g = cℒ_Xg + 2 dc ⊗_s X for a function c. The *l = 0 part* X_0 of a 1-form X
is its average over SO(4); d, δ, □ and Θ commute with this average, the rotations being isometries of g.

*The 1-form W* and the horizon functional.* Let

    W* := r⁻²dv − dr/(r(r + r_h)) = r⁻²dt + r_hr⁻³f⁻¹dr

([[eq:iii-d1-2-1]]): smooth on {r > 0} in the ingoing chart, W* ∈ 𝒜², δW* = 0, dW* = 2r⁻³dv ∧ dr and □W* = 0
([[sec:iii-d1-2]]). For a 1-form J defined near the horizon sphere put

    ℓ(J)(v) := r_h³ ∫_(S³) J(∂_v)|_((v,r_h)) dω,                                                        {#eq:hg-ell}

which for stationary J is the horizon functional [[eq:iii-d1-1-1]]: at r = r_h, ∂_(t_*) = ∂_v at fixed x, as t_* − v is
a function of r. For a 1-form X near the horizon sphere the *horizon charge* is

    Q[X](v) := r_h³ ∫_(S³) (δX + (dX)_(vr))|_((v,r_h)) dω.                                             {#eq:hg-charge}

*Cut-offs.* χ_K denotes the cut-off of [[sec:iii-b-5]] with the threshold of [[sec:iii-k-0]], as in [[thm:viii-2-2]]:
χ_K = 0 on {t^♭_* < T_K}, supp χ^♭_K ⊂ int{χ_K = 1}, and there is T′_♭ ≥ 60R₁ with χ^♭_K = 1 on
{|x| < t/10, t > T′_♭}. The cut-off χ_K of [[eq:iii-h-1-2]] is a different function; we write it
χ_aug(t_*, x) := χ_+(t_*)χ_c(|x|/t_*), and it builds the augmentation of [[sec:hg-augmented]].

### The structure in the class {#sec:hg-structure}

**Lemma {#lem:gd-r2-9}** (Spherically symmetric 1-forms.) For Y = a dv + b dr, with a, b functions of (v, r), put
φ := δY and q := r³(dY)_(vr). Then

    φ = −∂_vb − r⁻³∂_r(r³(a + fb)),        q = r³(∂_vb − ∂_ra),
    (□Y)_v = ∂_vφ + r⁻³(∂_vq + f∂_rq),        (□Y)_r = ∂_rφ − r⁻³∂_rq,                                  {#eq:gd-r2-9}

and the angular components of □Y vanish. So □Y = 0 if and only if ∂_rq = r³∂_rφ and ∂_vq = −r³(∂_vφ + f∂_rφ);
the integrability condition of this pair is □_0φ = 0, the l = 0 scalar wave equation, and q is then fixed by φ up to a
constant. Moreover Q[Y] = 2π²(r_h³φ + q)|_(r=r_h). The stationary solutions of □Y = 0 of this form on {r > r_h} that
extend smoothly across the future horizon and are bounded form span{W*, (∂_v)^♭}, where (∂_v)^♭ = −f dv + dr; their
(φ, q) are (0, 2) and (0, 2m₀); the combination dψ := m₀W* − (∂_v)^♭ has (φ, q) = (0, 0), with ψ = v + F,
F′ = −(r² + rr_h + r_h²)/(r(r + r_h)) and □_0ψ = 0; and only the multiples of W* decay.

*Proof.* In the chart (v, r, ϑ, φ1, φ2), |det g|^(1/2) = r³cs (c := cos ϑ, s := sin ϑ), g^(vv) = 0, g^(vr) = 1 and
g^(rr) = f, so Y^v = b and Y^r = a + fb, and δY = −|det g|^(−1/2)∂_μ(|det g|^(1/2)Y^μ) is the formula for φ. dY =
(∂_vb − ∂_ra)dv ∧ dr gives q. □Y = dδY + δdY, and dδY = ∂_vφ dv + ∂_rφ dr. For the 2-form F := dY,
(δF)^ν = −|det g|^(−1/2)∂_μ(|det g|^(1/2)F^(μν)), and F^(vr) = g^(vr)g^(rv)F_(rv) = −F_(vr) = −qr⁻³ is its only
nonzero component up to sign; so (δF)^v = −r⁻³∂_rq and (δF)^r = r⁻³∂_vq, and lowering with g_(vv) = −f, g_(vr) = 1
gives (δF)_v = r⁻³(∂_vq + f∂_rq), (δF)_r = −r⁻³∂_rq, and no angular component. Equating the two expressions of
∂_v∂_rq, the integrability condition is ∂_v(r³∂_rφ) + ∂_r(r³(∂_vφ + f∂_rφ)) = 0, that is −r³□_0φ = 0, since for a
function of (v, r), □_0φ = −r⁻³(∂_v(r³∂_rφ) + ∂_r(r³(∂_vφ + f∂_rφ))). For Q, δY + (dY)_(vr) = φ + qr⁻³ is constant on
the sphere, so Q[Y] = r_h³ · 2π²(φ + qr_h⁻³).

By [[prop:np-10-15]] (iii) the stationary solutions on {r > r_h} are A dt + B dr with A = a_0 + a_2r⁻² and
B = b_3r⁻³f⁻¹ + b_1rf⁻¹. Boundedness forces b_1 = 0. In the ingoing chart, dt = dv − f⁻¹dr, so the form is
A dv + (B − Af⁻¹)dr, and B − Af⁻¹ = (b_3r⁻³ − a_0 − a_2r⁻²)f⁻¹ extends smoothly across r = r_h, where f has a simple
zero, if and only if b_3 = r_h³(a_0 + a_2r_h⁻²). This leaves a two-dimensional space: a_0 = 0, a_2 = 1 gives W*, and
a_0 = 1, a_2 = 0 gives dt + r_h³r⁻³f⁻¹dr, which equals m₀W* − (∂_v)^♭ as (∂_v)^♭ = (∂_t)^♭ = −f dt = −dt + m₀r⁻²dt.
A solution decays only if a_0 = 0. For W*, a = r⁻² and b = −1/(r(r + r_h)), so a + fb = r⁻² − (r − r_h)r⁻³ =
r_hr⁻³, φ = 0 and q = r³ · 2r⁻³ = 2. For (∂_v)^♭, a = −f and b = 1, so a + fb = 0, φ = 0 and q = r³f′ = 2m₀. So dψ
has (φ, q) = (0, 0). Its components are m₀r⁻² + f = 1 and −m₀/(r(r + r_h)) − 1 = F′, so dψ = d(v + F); and
□_0ψ = δdψ = m₀δW* − δ(∂_v)^♭ = 0, the divergence of a Killing field vanishing. ∎

**Proposition {#prop:np-10-2}** (The passage to harmonic gauge in the class.)

(i) (*The Lichnerowicz equation.*) For every symmetric 2-tensor h,

    DRic(h) = −½(∇^α∇_αh_μν + 2R_μ^λ_ν^σ h_λσ) − (δ*Θ(h))_μν.

So under Θ(h) = 0 the linearised vacuum equation DRic(h) = 0 is the Lichnerowicz equation
∇^α∇_αh_μν + 2R_μ^λ_ν^σ h_λσ = 0; and h + ℒ_Xg is in harmonic gauge exactly when □X = −Θ(h).

(ii) (*The tensor part.*) For a class tensor h, the tensor h^TT whose only components are the angular block h^TT of
[[sec:rw-spheres]] (γ-trace-free and divergence-free on each sphere, [[lem:gd-1-2]] (c)) satisfies Θ(h^TT) = 0: the
tensor part is in harmonic gauge as it stands.

(iii) (*The scalar modes.*) Every class 1-form X is, on each sphere, a sum over even l of X_a^(l)S_l dy^a + η_l dS_l,
S_l := P_(l/2)(cos 2ϑ), with X_a^(l) and η_l functions on the orbit space. For each l, □ maps the class 1-forms
X_aS_l dy^a + η dS_l to class 1-forms of the same kind, and □X = J is, for (X_v, X_r, η), a system of three equations
on the orbit space with coefficients depending on r, m₀ and l only, each with principal part −g^(ab)∂_a∂_b (in the
static chart f⁻¹∂_t² − f∂_r²), coupled at first order. For the scalar mode h_S = F_abS_l dy^ady^b + 2r²FS_lγ of
[[prop:np-10-1]] (ii), the forcing term −Θ(h_S) is of the same kind and linear in F, F_ab and their first derivatives; by
[[eq:np-10-1]] it is linear in the master field Φ of the mode and its derivatives of order at most three.

(iv) (*The spherically symmetric sector.*) By [[lem:gd-r2-9]], W* spans the stationary spherically symmetric solutions
of □W = 0 on {r > r_h} that extend smoothly across the future horizon and decay. Put

    W** := (v/2)W* + A dv + B dr,        W**_H := W** − V^♭,
    A := (r_h² + 2r² log((r + r_h)/r))/(4r_hr²),
    B := N(r)/(4rr_h(r² − r_h²)),
    N(r) := r²r_h − 3rr_h² + 2r_h³ + 2r³ log r + 2(r_h³ − r³) log(r + r_h) − 2r_h³ log r_h,                {#eq:np-10-2}

with V of [[eq:gd-0-1]]. Then:

(a) A and B are real-analytic on {r > 0}, the numerator of B vanishing at r = r_h; rA → ½ and rB → −¼ as r → ∞.

(b) δW** = 0 and r³(dW**)_(vr) = v + r_h/2. Hence □W** = r⁻³dv = −Θ(K) and □W**_H = −Θ(K_V).

(c) K* := K_V + ℒ_(W**_H)g = K + ℒ_(W**)g is smooth across the horizon, Θ(K*) = 0, δm[K*] = 1 (the linearised mass
of [[lem:gd-1-4]] (a)), and

    K* − (v/2)ℒ_(W*)g = K + dv ⊗_s W* + ℒ_(A dv + B dr)g                                                {#eq:np-10-2-k}

is stationary and smooth across the horizon, with ℒ_(W*)g ≠ 0. So the gauge-fixed mass change K* grows linearly in v.

(d) (*The coefficient ½.*) If c is a constant, U a stationary 1-form smooth near the horizon sphere, and
□(cvW* + U) = −Θ(K) near the horizon sphere, then c = ½.

*Proof.* (i) [[lem:ix-2-1]] (a) gives 2(DRic + δ*Θ)(k) = −∇^α∇_αk + ([∇^λ, ∇_μ]k_λν + [∇^λ, ∇_ν]k_λμ)_(μν).
With the convention of [[sec:hg-setting]], [∇^λ, ∇_μ]k_λν = g^(λα)[∇_α, ∇_μ]k_λν = Ric^σ_μ k_σν − R_(σνλμ)k^(λσ),
and the Ricci term vanishes. The pair symmetry R_(σμλν) = R_(λνσμ) and the symmetry of k give
R_(σμλν)k^(λσ) = R_(σνλμ)k^(λσ), so the bracket is −2R_(σνλμ)k^(λσ) = −2R_μ^λ_ν^σ k_λσ. The last claim is
Θ(ℒ_Xg) = □X ([[eq:hg-box]]).

(ii) For g = g_ab dy^ady^b + r²γ the only Christoffel symbols mixing the factors are Γ^a_ij = −rD^ar γ_ij and
Γ^i_aj = (∂_ar/r)δ^i_j (the proof of [[lem:gd-1-3]]). Write k := h^TT. Its trace vanishes, so Θ(k) = δk. For an
orbit index b, ∇^μk_μb = g^(ij)∇_ik_jb = −g^(ij)Γ^l_ib k_jl = −(∂_br/r)g^(jl)k_jl = 0, the other terms containing a
vanishing component of k. For an angular index j, ∇^μk_μj = g^(ac)∇_ck_aj + g^(il)∇_lk_ij; every Christoffel term in
these contains a vanishing orbit or mixed component of k, so ∇^μk_μj = r⁻²D̂^ik_ij = 0.

(iii) The expansion is [[lem:gd-1-2]] (a) and (c): on each sphere the dz^i-part of a class 1-form is exact, X_ϑdϑ =
dη, and class functions expand in the S_l. Let L_1, …, L_6 be the Lie derivatives along the rotation fields Ω_i of
[[lem:rwg-a]], extended to spacetime as rotations of x, and C := Σ_i L_i². They generate isometries of g, so C
commutes with □ and with Θ. As the Ω_i are tangent to the spheres and the y^a are invariant, L_i(S dy^a) =
(Ω_iS)dy^a and L_i(η dS) = η d(Ω_iS); by [[lem:rwg-a]], Σ_iΩ_i² = Δ̂, so C(S_l dy^a) = −k_l²S_l dy^a and
C(η dS_l) = −k_l²η dS_l, k_l² = l(l + 2). These eigenvalues are distinct for distinct l. □ preserves the class (G acts by
isometries) and commutes with C, so it maps the mode-l part of a class 1-form, the −k_l²-eigenspace of C in the class,
into itself. Writing □(X_aS_l dy^a + η dS_l) = J_aS_l dy^a + ζ dS_l, the coefficients of the linear differential
operator (X_a, η) ↦ (J_a, ζ) at a point y are those of □ at (y, ϑ) divided by S_l(ϑ) or S_l′(ϑ), for any ϑ where these
do not vanish, so they depend on r (through g), m₀ and l only. In the chart (y, ϑ, φ1, φ2), □ = −g^(μν)∂_μ∂_ν + (first
order) on each component ([[lem:ix-2-1]] (a)); on X_aS_l dy^a + ηS_l′dϑ the second derivatives in y give
−g^(ab)∂_a∂_bX_c S_l and −g^(ab)∂_a∂_bη S_l′, and those that fall on S_l are of lower order in y. So each equation has
principal part −g^(ab)∂_a∂_b, and in the static chart −g^(ab)∂_a∂_b = f⁻¹∂_t² − f∂_r² + (first order). For h_S, C acts
on its components as on those of a 1-form of mode l (C(S_l k_ab) = −k_l²S_l k_ab and C(S_lγ) = −k_l²S_lγ, γ being
invariant), and C commutes with Θ; so −Θ(h_S) is a class 1-form of mode l. Θ is a first-order operator, so −Θ(h_S) is
linear in F, F_ab and their first derivatives, and these are linear in Φ and its derivatives of order at most two by
[[eq:np-10-1]].

(iv) The first sentence is [[lem:gd-r2-9]].

(a) log r, log(r + r_h) and the denominators r and r + r_h are analytic on {r > 0}. The numerator N(r) of B is analytic
there, and N(r_h) = r_h³ − 3r_h³ + 2r_h³ + 2r_h³ log r_h − 2r_h³ log r_h = 0; so N(r)/(r − r_h) is analytic, and so is
B = N(r)/((r − r_h) · 4rr_h(r + r_h)). As r → ∞, A = r_h/(4r²) + log(1 + r_h/r)/(2r_h) = 1/(2r) + O(r⁻²); and the
identity for r³(A + fB) in (b), with r³f = r(r² − m₀) and r³A = r²/2 + O(r), gives r³fB = −r²/4 + O(r log r), so
rB → −¼.

(b) We use [[lem:gd-r2-9]]. For the part (v/2)W*, with a = v/(2r²) and b = −v/(2r(r + r_h)): a + fb = vr_h/(2r³), so
φ = 1/(2r(r + r_h)), and q = r³(−1/(2r(r + r_h)) + vr⁻³) = v − r²/(2(r + r_h)). For U := A dv + B dr: from the
definitions,

    r³(A + fB) = (r − r_h)²/4 + r_h²/4 + (r_h²/2) log(1 + r/r_h),       −r³A′ = r_h/2 + r²/(2(r + r_h)),

as A′ = −r_h/(2r³) − 1/(2r(r + r_h)) and, for the first, r³A = rr_h/4 + (r³/(2r_h))(log(r + r_h) − log r) and
r³fB = r(r² − r_h²)B = N(r)/(4r_h). The derivative of the first identity is (r − r_h)/2 + r_h²/(2(r + r_h)) =
r²/(2(r + r_h)). So U has φ = −1/(2r(r + r_h)) and q = r_h/2 + r²/(2(r + r_h)), and W** has φ = 0, q = v + r_h/2.
[[eq:gd-r2-9]] gives (□W**)_v = r⁻³ and (□W**)_r = 0. Next, tr_g K = g^(vv)r⁻² = 0, so Θ(K)_ν = −∇^μ(r⁻²ℓ_μℓ_ν)
with ℓ := dv, ℓ^♯ = ∂_r. ∇^μ(r⁻²ℓ_μ) = r⁻³∂_r(r³r⁻²) = r⁻³, and ∇_(∂_r)dv = 0, as Γ^v_(rν) = g^(vσ)Γ_(σ,rν) =
Γ_(r,rν) = 0 (in the chart the only nonzero lowered symbols of the orbit metric are Γ_(r,vv) = f′/2 and
Γ_(v,vr) = −f′/2, and those mixing the factors have an angular index). So Θ(K) = −r⁻³dv. By [[eq:gd-0-1]] and
[[eq:hg-box]], Θ(K_V) = Θ(K) + □V^♭, so □W**_H = −Θ(K) − □V^♭ = −Θ(K_V).

(c) ℒ_Vg = ℒ_(V^♭)g, so K* = K + ℒ_Vg + ℒ_(W**)g − ℒ_(V^♭)g = K + ℒ_(W**)g. K and W** are smooth across the horizon
(by (a)), so K* is. Θ(K*) = Θ(K) + □W** = 0 by (b). W** is spherically symmetric, so δm[ℒ_(W**)g] = 0 and δm[K*] =
δm[K] = 1 ([[lem:gd-1-4]] (a)). With ℒ_(cX)g = cℒ_Xg + 2dc ⊗_s X, ℒ_((v/2)W*)g = (v/2)ℒ_(W*)g + dv ⊗_s W*, which
gives [[eq:np-10-2-k]]; its right side has stationary coefficients, smooth across the horizon. W* is not a multiple of
(∂_v)^♭, so by [[lem:gd-1-4]] (c) it is not Killing, and ℒ_(W*)g ≠ 0.

(d) □(cvW* + U) = c[□, v]W* + cv□W* + □U = c[□, v]W* + □U, a stationary 1-form. By [[lem:iii-d1-2-1]] (1),
ℓ(□U) = 0, and by the proof of [[lem:iii-d1-3-1]] (1), ℓ([□, v]W*) = 4π². ℓ(−Θ(K)) = ℓ(r⁻³dv) = r_h³ · r_h⁻³ · 2π² =
2π². So 4π²c = 2π². ∎

By (d), the gauge-fixed mass change built from the static time with the coefficient 1, or from any gauge vector
vW* + U with U stationary, is not smooth across the horizon. The coefficient ½ of W** is the one regularity allows.

### The horizon charge {#sec:hg-charge}

**Lemma {#lem:gd-2-2}** (The horizon charge.) (a) For every 1-form X, at r = r_h, with F := dX,

    r³(□X)_v = ∂_v[r³(δX + F_(vr))] − r(γ^(1/2))⁻¹∂_i(γ^(1/2)γ^(ij)F_(jv)),

γ^(1/2) the density of γ in the coordinates z^i of the sphere; for a class 1-form the last term is
−(r/(cs))∂_ϑ(cs F_(ϑv)). Integrating over S³,

    (d/dv) Q[X] = ℓ(□X).                                                                                 {#eq:gd-2-1}

Q[X] depends only on the l = 0 part X_0 of X: Q[X] = Q[X_0].

(b) δW* = 0, (dW*)_(vr) = 2r⁻³ and Q[W*] = 4π². The Killing form (∂_v)^♭ = −f dv + dr has Q[(∂_v)^♭] = 4π²m₀, and
(∂_v)^♭ − m₀W* is closed. ℓ([□, v]W*) = 4π². ℓ(Θ(K)) = −2π², and ℓ(Θ(K_V)) = −2π². Q[W**](v) = 2π²(v + r_h/2),
so (d/dv)Q[W**] = 2π².

[[eq:gd-2-1]] is the time-dependent form of [[lem:iii-d1-2-1]] (1) and (3): ℓ annihilates □ of every stationary 1-form
smooth at the horizon (the case ∂_v = 0 of [[eq:gd-2-1]]), and spans the annihilator of the range at zero energy.

*Proof.* (a) □X = dδX + δF, and (dδX)_v = ∂_v(δX). For the 2-form F, (δF)^ν = −|det g|^(−1/2)∂_μ(|det g|^(1/2)F^(μν))
with |det g|^(1/2) = r³γ^(1/2), and (δF)_v = g_(vv)(δF)^v + g_(vr)(δF)^r = −f(δF)^v + (δF)^r. At r = r_h, f = 0, so
(δF)_v = (δF)^r. Here F^(vr) = g^(vr)g^(rv)F_(rv) = −F_(vr) (g^(vv) = 0), F^(rr) = 0, and
F^(ir) = r⁻²γ^(ij)(F_(jv) + fF_(jr)). So at r = r_h, where f = 0 and ∂_i, ∂_v do not act on f,

    (δF)_v = −(r³γ^(1/2))⁻¹(−r³γ^(1/2)∂_vF_(vr) + r∂_i(γ^(1/2)γ^(ij)F_(jv)))
           = ∂_vF_(vr) − r⁻²(γ^(1/2))⁻¹∂_i(γ^(1/2)γ^(ij)F_(jv)),

and multiplying by r³ gives the formula. In the class the only angular component of F with index v is F_(ϑv), and
γ^(1/2) = cs, γ^(ϑϑ) = 1. The divergence on S³ integrates to zero, which gives [[eq:gd-2-1]]. As d, δ commute with the
SO(4)-average and dω is invariant, ∫_(S³)(δX + F_(vr)) dω = ∫_(S³)(δX_0 + (dX_0)_(vr)) dω.

(b) δW* = 0 and dW* = 2r⁻³dv ∧ dr ([[sec:hg-setting]]), so Q[W*] = r_h³ · 2π² · 2r_h⁻³ = 4π². For (∂_v)^♭,
[[lem:gd-r2-9]] gives (φ, q) = (0, 2m₀), so Q = 4π²m₀, and (∂_v)^♭ − m₀W* = −dψ is closed. ℓ([□, v]W*) = 4π² is the
proof of [[lem:iii-d1-3-1]] (1). Θ(K) = −r⁻³dv ([[prop:np-10-2]] (iv) (b)), so ℓ(Θ(K)) = −r_h³ · r_h⁻³ · 2π² = −2π²; and
K_V = K near the horizon ([[eq:gd-0-1]]). By [[prop:np-10-2]] (iv) (b), W** has φ = 0 and q = v + r_h/2, and
[[lem:gd-r2-9]] gives Q[W**] = 2π²(v + r_h/2). ∎

### The harmonic-gauge solutions and the forced growth {#sec:hg-solutions}

**Lemma {#lem:gd-r3-1}** (Uniqueness on N⁺.) Let d be a 1-form on N⁺, smooth up to Σ°, with □d = 0 on N⁺ and
vanishing Cauchy data on Σ°. Then d = 0. In particular, if F_1, F_2 are smooth 1-forms on Ω^♯ that agree on N⁺, and
Z̃_1, Z̃_2 solve □Z̃_i = F_i on Ω^♯ with the same Cauchy data on Σ°, then Z̃_1 = Z̃_2 on N⁺.

*Proof.* By [[lem:ix-2-1]] (a), □ has principal part −g^(αβ)∂_α∂_β ⊗ id, and dt_IVP is timelike ([[sec:ix-0]]), so Σ°
is noncharacteristic for □. Step 3 of the proof of [[thm:ix-2-2]] uses of its operator only this. In coordinates
(t_IVP, y) near a point of Σ°, d = 0 and ∂_(t_IVP)d = 0 on Σ°; if ∂^j_(t_IVP)d = 0 on Σ° for j < m, some m ≥ 2, apply
∂^(m−2)_(t_IVP) to □d = 0 and restrict to Σ°: every term but −g⁻¹(dt_IVP, dt_IVP)∂^m_(t_IVP)d is a derivative of d
of order below m, or of order m with at most m − 1 derivatives in t_IVP, so it vanishes, and ∂^m_(t_IVP)d = 0. So d
vanishes to infinite order along Σ°, and its extension d̃ by 0 to Ω^♯ ∩ {t_IVP < 0} is smooth on Ω^♯, with □d̃ = 0
and vanishing data on Σ°. Ω^♯ is globally hyperbolic on each component, with Cauchy hypersurface Σ° ([[lem:ix-1-2]]),
and ±□ is normally hyperbolic, so [[thm:std-bgp-cauchy]] (3) on each component gives d̃ = 0. For the second claim
apply the first to d := (Z̃_1 − Z̃_2)|_(N⁺). ∎

**Proposition {#prop:gd-2-1}** (The harmonic-gauge solutions.)

(a) For every 1-form Z′ on N⁺, smooth up to Σ°, with □Z′ = −Θ(e) on N⁺,

    ġ_H := ġ_RW + ṁℒ_(W**_H)g + ℒ_(Z′)g                                                                   {#eq:gd-2-gh}

is a linearised vacuum solution on N⁺, smooth up to Σ°, in harmonic gauge, inducing (γ̇, k̇) up to the data of a
linearised diffeomorphism. For all smooth Cauchy data on Σ° such a Z′ exists, and it is determined on N⁺ by its data;
for G-invariant data it is G-invariant.

(b) Let U ⊂ U^♯ be open and G-invariant, Ω′_+ := D_U(Σ_U) ∩ {t_IVP ≥ 0}, and let ġ′ be a G-invariant linearised vacuum
solution on Ω′_+, smooth up to Σ_U, in harmonic gauge, inducing (γ̇, k̇) plus the data of ℒ_Zg for a vector field Z
near Σ_U, smooth up to Σ_U. Then ġ′ = ġ_RW + ṁℒ_(W**_H)g + ℒ_(Z′)g on Ω′_+ for a G-invariant 1-form Z′ with
□Z′ = −Θ(e).

(c) (*The forcing term has no l = 0 part.*) Θ(e)_0 = 0. So the l = 0 part Z′_0 of Z′ solves □Z′_0 = 0, and
Z′_(≥2) := Z′ − Z′_0 solves □Z′_(≥2) = J := −Θ(e), with, for every k, R′ and ε′ > 0,

    |J|_k ≤ C‖(γ̇, k̇)‖_(H^(k₁(k+3))) t_*^(−w+ε′)     on {r_♭ < r ≤ R′, t_* ≥ T′},

a loss of three derivatives.

(d) (*Non-uniqueness.*) □W* = 0, so Z′ ↦ Z′ + cW* preserves (a): ġ_H + cℒ_(W*)g is again a harmonic-gauge solution with
the same data up to a linearised diffeomorphism. A decay statement in harmonic gauge therefore concerns a chosen Z′,
the freedom being the solutions of □Y = 0 (more than the multiples of W* when the data of Y do not decay:
[[prop:gd-r2-13]] (c)).

*Proof.* (a) DRic(ġ_RW) = 0 ([[thm:rw-settling]] (a)) and DRic(ℒ_Xg) = 0 ([[lem:ix-2-1]] (b)). By [[prop:np-10-2]]
(iv) (b), Θ(ġ_H) = ṁΘ(K_V) + Θ(e) + ṁ□W**_H + □Z′ = ṁΘ(K_V) + Θ(e) − ṁΘ(K_V) − Θ(e) = 0. ġ_RW induces (γ̇, k̇)
plus the data of ℒ_(X_RW)g ([[thm:rw-settling]] (a)), and W**_H and Z′ are smooth up to Σ°. *Existence.* e is given
on N⁺ only, smooth up to Σ°. As in Step 1 of the proof of [[thm:ix-2-2]], −Θ(e) extends to a smooth 1-form F on Ω^♯:
it extends to an open neighbourhood of N⁺ ([[sec:ix-0]]), and a smooth function equal to 1 on N⁺ and supported in
that neighbourhood extends it by 0 beyond. By [[lem:ix-1-1]] on Ω^♯ (globally hyperbolic on each component with Cauchy
hypersurface Σ°, [[lem:ix-1-2]]), with the operator ±□ ([[lem:ix-2-1]] (a)), □Z̃ = F has a smooth solution on Ω^♯
with any given smooth data on Σ°, and Z′ := Z̃|_(N⁺) is smooth up to Σ°. By [[lem:gd-r3-1]], Z′ does not depend on the
extension, and two solutions on N⁺ with the same data agree. *Invariance.* G preserves t_IVP and |x|, so N⁺, Ω^♯ and
Σ°; Θ(e) is G-invariant, and □ commutes with the action of G. For σ ∈ G, σ*Z′ solves □(σ*Z′) = −Θ(e) on N⁺ with the
data σ* of those of Z′; for G-invariant data, σ*Z′ = Z′ by uniqueness.

(b) By [[cor:ix-2-3]] and [[rem:ix-2-4]] (c), ġ′ = ġ + ℒ_(X′)g on Ω′_+ ⊂ N⁺ with X′ G-invariant and smooth up to
Σ_U; and ġ_RW = ġ + ℒ_(X_RW)g. So ġ′ − ġ_RW = ℒ_Yg with Y := X′ − X_RW, G-invariant. Θ(ġ′) = 0 reads
Θ(e) + ṁΘ(K_V) + □Y = 0, that is □(Y − ṁW**_H) = −Θ(e) by [[prop:np-10-2]] (iv) (b). Put Z′ := Y − ṁW**_H.

(c) Θ commutes with the SO(4)-average, and e_0 = 0, so Θ(e)_0 = 0; □ commutes with it too, so □Z′_0 = (□Z′)_0 = 0.
Θ(e) is first order in e, so |Θ(e)|_k ≤ C|e|_(k+1), and [[thm:rw-settling]] (b) bounds |e|_(k+1).

(d) □W* = 0 ([[sec:hg-setting]]), and ℒ_(cW*)g = cℒ_(W*)g is a linearised diffeomorphism. ∎

**Theorem {#thm:gd-2-3}** (The forced linear growth.) Let ġ_H = ġ + ℒ_Zg be a harmonic-gauge solution of
[[prop:gd-2-1]] (a), Z = X_RW + ṁW**_H + Z′ G-invariant. Then on the horizon, for v ≥ v_0 with t_* ≥ T′ there,

    Q[Z](v) = Q[Z](v_0) + 2π²ṁ(v − v_0) − ∫_(v_0)^v ℓ(Θ(h))(v′) dv′,        |ℓ(Θ(h))(v)| ≤ Cv^(−w+ε′),

and Q[Z − ṁW**_H](v) converges as v → ∞. Consequently, if ṁ ≠ 0, no harmonic-gauge solution settles to ṁK_V near
the horizon at an integrable rate: there are no δ, ε > 0 for which (ġ_H − ṁK_V)_0 and its first derivatives are
O(t_*^(−1−δ)) on {|r − r_h| ≤ ε}.

*Proof.* □Z = Θ(ℒ_Zg) = −Θ(ġ) = −ṁΘ(K_V) − Θ(h), as Θ(ġ_H) = 0, and ℓ(Θ(K_V)) = −2π² ([[lem:gd-2-2]] (b)).
ℓ(Θ(h)) involves h and its first derivatives at r_h, bounded by [[eq:gd-0-2]], with |t_* − v| ≤ C near r_h.
Integrating [[eq:gd-2-1]] gives the identity. Near the horizon V is a constant multiple of the Killing field ∂_t
([[eq:gd-0-1]]), so there □V^♭ = Θ(ℒ_Vg) = 0 and Q[V^♭] is constant by [[eq:gd-2-1]]; and (d/dv)Q[W**] = 2π²
([[lem:gd-2-2]] (b)). So (d/dv)Q[ṁW**_H] = 2π²ṁ, and Q[Z − ṁW**_H] has the integrable derivative −ℓ(Θ(h)) and
converges.

Suppose ṁ ≠ 0 and (ġ_H − ṁK_V)_0 is O(t_*^(−1−δ)), with its first derivatives, on {|r − r_h| ≤ ε}, ε small. Averaging
ġ_H = ṁK_V + h + ℒ_Zg, ℒ_(Z_0)g = (ġ_H − ṁK_V)_0 − h_0, which with [[eq:gd-0-2]] is O(t_*^(−min(1+δ,w−ε′))) there,
with first derivatives. It is a spherically symmetric linearised vacuum solution with δm[ℒ_(Z_0)g] = 0
([[lem:gd-1-4]] (a)). Apply [[lem:gd-1-4]] (b) on the simply connected set {|r − r_h| < ε, v > v_1} of the orbit
space: ℒ_(Z_0)g = ℒ_(Y)g with Y = ζ∂_v + rH_L∂_r, where H_L and dζ = ω are algebraic in ℒ_(Z_0)g and its first
derivatives, so integrable in v; hence ζ(v, r_h) converges as v → ∞, and H_L and its first derivatives tend to 0. By
[[lem:gd-1-4]] (c), Z_0 − Y^♭ = c′(∂_v)^♭ for a constant c′. Now ζ(∂_v)^♭ has δ(ζ(∂_v)^♭) = −∂_vζ and
(d(ζ(∂_v)^♭))_(vr) = ∂_vζ + f∂_rζ + ζf′, so at r_h, where f = 0 and f′ = 2/r_h, Q[ζ(∂_v)^♭] = 4π²m₀ζ(v, r_h). And
(rH_L∂_r)^♭ = rH_L dv, whose charge involves H_L and its first derivatives and tends to 0. So Q[Z] = Q[Z_0]
([[lem:gd-2-2]] (a)) converges as v → ∞, against the growth 2π²ṁv of the identity. ∎

In terms of the gauge vector the statement is exact: its horizon charge grows as 2π²ṁv. At the level of the metric,
[[prop:gd-r2-13]] makes the growth precise for the spherically symmetric part of the representatives.

### The augmented zero-energy operator {#sec:hg-augmented}

This section and the next two carry [[ch:s18]] over from the linearised gauge-fixed Einstein operator to the 1-form
wave operator □ at b₀, with W* as the only zero-energy state.

*Setting.* P̂(σ) is the spectral family of □ at b₀, the parameter 𝗉_0 of [[sec:iii-d1-1]]. By [[sec:iii-d1-1]],
P̂ satisfies (H1)–(H5) with ϑ_ℋ = 1, (G) for every weight α with α + 2 ∈ (0, 2), and (TF), and has index 0 at σ ≠ 0.
By [[lem:iii-d-2-1]], □ = L_0 + L_1∂_(t_*) + L_2∂²_(t_*) with stationary L_j, where L_0 = P̂(0), L_1 = [□, t_*] on
stationary 1-forms, L_2 = −g^(00) with g^(00) := g⁻¹(dt_*, dt_*), and near ∂X, L_0 ∈ ρ²Diff²_b, L_1 ∈ ρDiff¹_b and
L_2 ∈ ρ²C^∞, the form [[sec:iii-h-1]] uses for L_b; and S̄ = 0, as the spectrum of S̄ is γ_Υ(1 − e_Υ), 2γ_Υ, γ_Υ
([[lem:iii-d-3-1]]) and γ_Υ = 0 for □. Fix a weight α with α + 2 ∈ (0, 1) ([[eq:iii-h-1-1]]), a constant regularity
s > 5/2 (the threshold of the density argument in [[lem:iii-d1-2-1]] (3)), an SO(4)-invariant fibre inner product h,
and an SO(4)-invariant φ ∈ C_c^∞(X°; E) with ⟨W*, φ⟩_h = 1 (average any choice over SO(4); W* is SO(4)-invariant).
The spaces 𝒳_σ, 𝒴_σ, 𝒳_0 = {u ∈ H̄_b^(s,α) : P̂(0)u ∈ 𝒴_0} and 𝒴_0 = H̄_b^(s−1,α+2) are those of [[sec:iii-h-1]] and
[[prop:iii-h-3-2]] for P̂. The state is W*: smooth on X, W* ∈ 𝒜², and □W* = 0.

**Definition {#def:gd-r2-1}** (The augmented operator.) Put

    f_* := □(χ_augW*) = [□, χ_aug]W*,      f̂_*(σ) := ∫ e^(iσt_*)f_* dt_*,      ĝ_*(σ) := iσ⁻¹Ψ(σ, ·)W*,

with Ψ of [[lem:iii-h-2-5]], and, for (u, c) with u a section over X and c ∈ ℂ,

    P̃(σ)(u, c) := (P̂(σ)u + cf̂_*(σ), ⟨u, φ⟩_h).

**Lemma {#lem:gd-r2-2}** ([[lem:iii-h-2-2]]–[[lem:iii-h-2-5]] at □.)
(a) f_* vanishes outside {1 ≤ t_* ≤ 2, |x| ≤ t_*/2} ∪ {t_* ≥ 2, t_*/4 ≤ |x| ≤ t_*/2}, and its part f_∞ at r ≥ 1
obeys [[eq:iii-h-2-1]]: |(t_*∂_(t_*))^j(r∂_r)^a∂_ω^β f_∞| ≤ Cr⁻⁴.
(b) f̂_*(0) = L_1W* + L_0w with w := −κ(r)W*, κ of [[lem:iii-h-2-3]]; so w ∈ 𝒜¹ and f̂_*(0) ∈ 𝒜³.
(c) [[lem:iii-h-2-4]] (a)–(d) hold for f̂_*.
(d) For σ ≠ 0 with Im σ ≥ 0, ĝ_*(σ) ∈ 𝒳_σ and P̂(σ)ĝ_*(σ) = f̂_*(σ).

*Proof.* The proofs of [[lem:iii-h-2-2]]–[[lem:iii-h-2-5]] use, of the state ġ(1, 0) and the operator L_b, only that
L_bġ = L_0ġ = 0, that ġ is stationary, smooth on X and in 𝒜², and that L_0 ∈ ρ²Diff²_b, L_1 ∈ ρDiff¹_b and
L_2 ∈ ρ²C^∞ near ∂X with stationary coefficients, smooth on compact subsets of X. At □ these are □W* = 0, W* ∈ 𝒜²
smooth and stationary, and the structure above. So (a) is [[lem:iii-h-2-2]] with h = W* (|W*| ≤ Cr⁻² with its
b-derivatives on the cone, ∂_(t_*)W* = 0); (b) is [[eq:iii-h-2-2]] for ḃ = (1, 0); (c) is [[lem:iii-h-2-4]]; and (d)
is [[lem:iii-h-2-5]] (a)–(c). The generalised states h^(≤1)(S) of [[ch:s18]] do not occur. ∎

**Proposition {#prop:gd-r2-3}** (The augmented zero-energy operator is invertible.) P̃(0) : 𝒳_0 ⊕ ℂ → 𝒴_0 ⊕ ℂ is
invertible.

*Proof.* *Index 0.* P̃(0) is a finite-rank perturbation of P̂(0) ⊕ 0, and P̂(0) : 𝒳_0 → 𝒴_0 has index 0
([[cor:i-c-6-6]], as in the proof of [[lem:iii-d1-2-1]] (3)); f̂_*(0) ∈ 𝒜³ ⊂ 𝒴_0, as α + 2 < 1. *Injectivity.* Let
P̃(0)(u, c) = 0. By [[lem:gd-r2-2]] (b), P̂(0)(u + cw) + cL_1W* = 0, and u + cw ∈ 𝒳_0, as 𝒜¹ ⊂ H̄_b^(∞,α) for α < −1.
Apply ℓ. ℓ ∘ P̂(0) = 0 on 𝒳_0 ([[lem:iii-d1-2-1]] (1), with the density argument of its (3)); and
ℓ(L_1W*) = ℓ([□, t_*]W*) = 4π² ([[lem:iii-d1-3-1]] (1)). So 4π²c = 0, c = 0, u ∈ span{W*} ([[lem:iii-d1-2-1]] (2)),
and ⟨u, φ⟩_h = 0 gives u = 0. ∎

The block-triangular 11 × 11 pairing matrix of [[prop:iii-h-3-2]] is here the 1 × 1 matrix (4π²). The time cut-off is
what makes it nonzero: ℓ annihilates the stationary column P̂(0)(κW*) for every stationary κ smooth at the horizon
([[lem:iii-d1-2-1]] (1)), and an augmentation by such a column is not injective at zero energy.

**Theorem {#thm:gd-r2-4}** (Uniform low-energy estimates for P̃.) There are c_k > 0 and C_k such that for σ ∈ Σ_0 with
|σ| ≤ c_k, P̃(σ) : 𝒳_σ ⊕ ℂ → 𝒴_σ ⊕ ℂ is invertible with the estimate [[eq:iii-h-4-5]] (with |c| in place of
|ḃ| + |S|); [[thm:iii-h-4-1]] (3) holds for P̃ on Σ_0 ∩ ℝ; and, with (u, c) := P̃(σ)⁻¹(f, 0) for 0 < |σ| ≤ c_0,

    P̂(σ)⁻¹f = u + c ĝ_*(σ).                                                                              {#eq:gd-r2-1}

*Proof.* [[thm:iii-h-4-1]] is stated for every family P̂ with (H1)–(H4), (G), (TF) and index 0 at σ ≠ 0, which the
setting gives, and columns with (A1)–(A4), which [[lem:gd-r2-2]] (b)–(c) give with ϵ_0 = ¼(1 − (α + 2)) exactly as in
the proof of [[cor:iii-h-4-2]]; its (Z_𝒫) is [[prop:gd-r2-3]]. P̂(σ) is invertible for every σ ≠ 0 with Im σ ≥ 0
([[prop:iii-d-6-1]], [[prop:iii-d-6-2]]), so no scaling argument is needed at small σ, and [[eq:gd-r2-1]] follows
from [[lem:gd-r2-2]] (d) as [[eq:iii-h-4-6]] follows in the proof of [[cor:iii-h-4-3]]. ∎
