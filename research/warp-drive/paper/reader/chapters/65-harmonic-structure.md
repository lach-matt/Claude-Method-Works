## The linear solution in harmonic gauge, I: structure, the horizon charge and decay modulo W* {#ch:harmonic-structure}

[[ch:rw-gauge]] determined the gauge vector that carries the linear solution of [[cor:viii-2-3]] to a
Regge–Wheeler-type gauge. This chapter and the next do the same for the harmonic gauge Υ̇⁰(ġ) = 0 of [[sec:ix-0]], in
which the linearised vacuum equation is the Lichnerowicz wave equation; in four dimensions the passage is Hung's
[Hun19]. In the class the harmonic-gauge solutions with the data of ġ are ġ_RW + ṁℒ_(W**_H)g + ℒ_(Z′)g, where □Z′ is
a forcing term with no spherically symmetric part and the spherically symmetric part of Z′ is free ([[prop:gd-2-1]]). The
structure of the passage is explicit ([[prop:np-10-2]]): the tensor part is in harmonic gauge already, each scalar
mode of the gauge vector solves three coupled 1 + 1 wave equations with the master field as source, and the
spherically symmetric sector has two solutions that do not decay, the stationary 1-form W* and a gauge-fixed mass
change K* that grows linearly in the ingoing time v, with a coefficient ½ that regularity at the horizon forces. A
conserved horizon charge ([[lem:gd-2-2]]) shows that the growth cannot be avoided: when the mass changes, no
harmonic-gauge solution settles to a change of mass near the horizon at an integrable rate ([[thm:gd-2-3]]).

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
O(2) × O(2); K̄ := r⁻²dv² and K_V = K̄ + ℒ_Vg, with ℒ_Vg = 0 on {r ≤ 2R₁} ([[eq:gd-0-1]]); the linear solution ġ
of [[cor:viii-2-3]], its mass change ṁ, h := ġ − ṁK_V and w := α − 2 > 2 + ε_t, α that of [[thm:viii-2-2]] (4); the
seminorms |·|_k, the bound [[eq:gd-0-2]], and the l = 0 part of a class tensor ([[sec:rw-spheres]]); the covariant
derivative D of the orbit metric, and D̂, Δ̂ on (S³, γ), with dω the measure of γ and |S³| = 2π²; and the
representative ġ_RW = ġ + ℒ_(X_RW)g of [[thm:rw-settling]]. We put

    e := ġ_RW − ṁK_V,

so that e_0 = 0 ([[thm:rw-settling]] (a)). The domains are those of [[sec:ix-0]]: U^♯, Σ° and N⁺ = M°_♭ ∩ {t_IVP ≥ 0},
with Ω^♯ := D_(U^♯)(Σ°) and Ω^♯ ∩ {t_IVP ≥ 0} = N⁺ ([[lem:ix-1-2]]); "smooth up to Σ°" is as there. (Dyn) holds at
b₀ for every operator with principal symbol G Id ([[thm:vi-a-6-1]]), so the results of [[ch:s13]] stated under it
apply to □ below. The curvature is written with [∇_α, ∇_β]ω_λ = −R^σ_(λαβ)ω_σ and Ric_(λβ) = R^σ_(λσβ).

*Operators.* As in [[sec:ix-0]]: (δk)_μ = −∇^αk_αμ, Gk = k − ½g tr_g k, δ* the symmetrised covariant derivative, and
Υ̇⁰ the derivative at (g, g) in the first argument of Υ⁰, for which Υ̇⁰(k) = −δGk ([[lem:iii-b-6-3]]); −Υ̇⁰(k) is the
linearised harmonic gauge 1-form. We identify vector fields and 1-forms by g and write ℒ_Xg for ℒ_(X^♯)g, so that
ℒ_Xg = 2δ*X. Put

    □ := 2δGδ*   on 1-forms,        so that   Υ̇⁰(ℒ_Xg) = −□X.                                           {#eq:hg-box}

At the Ricci-flat g, □ = −∇^α∇_α ([[lem:ix-2-1]] (a)) = dδ + δd ([[sec:iii-d-1]]), and on functions we write
□_0 := δd = −∇^α∇_α. A symmetric 2-tensor k is in *harmonic gauge* if Υ̇⁰(k) = 0. For 1-forms a, b put
a ⊗_s b := ½(a ⊗ b + b ⊗ a); then ℒ_(cX)g = cℒ_Xg + 2 dc ⊗_s X for a function c. The *l = 0 part* X_0 of a 1-form X
is its average over SO(4); d, δ, □ and Υ̇⁰ commute with this average, the rotations being isometries of g.

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
{|x| < t/10, t > T′_♭}. The cut-off χ_K of [[eq:iii-h-1-2]] is a different function; as in [[sec:iii-i4-1]] we write it
χ^H_K(t_*, x) := χ_+(t_*)χ_c(|x|/t_*), and it builds the augmentation of [[sec:hg-augmented]].

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

    DRic(h) = −½(∇^α∇_αh_μν + 2R_μ^λ_ν^σ h_λσ) + (δ*Υ̇⁰(h))_μν.

So under Υ̇⁰(h) = 0 the linearised vacuum equation DRic(h) = 0 is the Lichnerowicz equation
∇^α∇_αh_μν + 2R_μ^λ_ν^σ h_λσ = 0; and h + ℒ_Xg is in harmonic gauge exactly when □X = Υ̇⁰(h).

(ii) (*The tensor part.*) For a class tensor h, the tensor h^TT whose only components are the angular block h^TT of
[[sec:rw-spheres]] (γ-trace-free and divergence-free on each sphere, [[lem:gd-1-2]] (c)) satisfies Υ̇⁰(h^TT) = 0: the
tensor part is in harmonic gauge as it stands.

(iii) (*The scalar modes.*) Every class 1-form X is, on each sphere, a sum over even l of X_a^(l)S_l dy^a + η_l dS_l,
S_l := P_(l/2)(cos 2ϑ), with X_a^(l) and η_l functions on the orbit space. For each l, □ maps the class 1-forms X_aS_l
dy^a + η dS_l to class 1-forms of the same kind, and □X = J is, for (X_v, X_r, η), a system of three equations on the
orbit space with coefficients depending on r, m₀ and l only, each with principal part −g^(ab)∂_a∂_b
(in the static chart f⁻¹∂_t² − f∂_r²), coupled at first order. For the scalar mode h_S = F_abS_l dy^ady^b + 2r²FS_lγ of
[[prop:np-10-1]] (ii), the forcing term Υ̇⁰(h_S) is of the same kind and linear in F, F_ab and their first derivatives;
by [[eq:np-10-1]] it is linear in the master field Φ of the mode and its derivatives of order at most three.

(iv) (*The spherically symmetric sector.*) By [[lem:gd-r2-9]], W* spans the stationary spherically symmetric solutions
of □W = 0 on {r > r_h} that extend smoothly across the future horizon and decay. Put

    W** := (v/2)W* + A dv + B dr,        W**_H := W** − V^♭,
    A := (r_h² + 2r² log((r + r_h)/r))/(4r_hr²),
    B := 𝔑(r)/(4rr_h(r² − r_h²)),
    𝔑(r) := r²r_h − 3rr_h² + 2r_h³ + 2r³ log r + 2(r_h³ − r³) log(r + r_h) − 2r_h³ log r_h,                {#eq:np-10-2}

with V of [[eq:gd-0-1]]. Then:

(a) A and B are real-analytic on {r > 0}, the numerator of B vanishing at r = r_h; rA → ½ and rB → −¼ as r → ∞.

(b) δW** = 0 and r³(dW**)_(vr) = v + r_h/2. Hence □W** = r⁻³dv = Υ̇⁰(K̄) and □W**_H = Υ̇⁰(K_V).

(c) K* := K_V + ℒ_(W**_H)g = K̄ + ℒ_(W**)g is smooth across the horizon, Υ̇⁰(K*) = 0, δm[K*] = 1 (the linearised
mass of [[lem:gd-1-4]] (a)), and

    K* − (v/2)ℒ_(W*)g = K̄ + dv ⊗_s W* + ℒ_(A dv + B dr)g                                                {#eq:np-10-2-k}

is stationary and smooth across the horizon, with ℒ_(W*)g ≠ 0. So the gauge-fixed mass change K* grows linearly in v.

(d) (*The coefficient ½.*) If c is a constant, U a stationary 1-form smooth near the horizon sphere, and
□(cvW* + U) = Υ̇⁰(K̄) near the horizon sphere, then c = ½.

*Proof.* (i) By [[eq:ix-0-1]] and [[lem:ix-2-1]] (a),
2(DRic − δ*Υ̇⁰)(k) = 2L⁰k = −∇^α∇_αk + ([∇^λ, ∇_μ]k_λν + [∇^λ, ∇_ν]k_λμ)_(μν). With the convention of
[[sec:hg-setting]], [∇^λ, ∇_μ]k_λν = g^(λα)[∇_α, ∇_μ]k_λν = Ric^σ_μ k_σν − R_(σνλμ)k^(λσ), and the Ricci term
vanishes. The pair symmetry R_(σμλν) = R_(λνσμ) and the symmetry of k give R_(σμλν)k^(λσ) = R_(σνλμ)k^(λσ), so the
bracket is −2R_(σνλμ)k^(λσ) = −2R_μ^λ_ν^σ k_λσ. The last claim is Υ̇⁰(ℒ_Xg) = −□X ([[eq:hg-box]]).

(ii) For g = g_ab dy^ady^b + r²γ the only Christoffel symbols mixing the factors are Γ^a_ij = −rD^ar γ_ij and
Γ^i_aj = (∂_ar/r)δ^i_j (the proof of [[lem:gd-1-3]]). Write k := h^TT. Its trace vanishes, so −Υ̇⁰(k) = δk. For an
orbit index b, ∇^μk_μb = g^(ij)∇_ik_jb = −g^(ij)Γ^l_ib k_jl = −(∂_br/r)g^(jl)k_jl = 0, the other terms containing a
vanishing component of k. For an angular index j, ∇^μk_μj = g^(ac)∇_ck_aj + g^(il)∇_lk_ij; every Christoffel term in
these contains a vanishing orbit or mixed component of k, so ∇^μk_μj = r⁻²D̂^ik_ij = 0.

(iii) The expansion is [[lem:gd-1-2]] (a) and (c): on each sphere the dz^i-part of a class 1-form is exact, X_ϑdϑ = dη,
and class functions expand in the S_l. Let L_1, …, L_6 be the Lie derivatives along the rotation fields Ω_i of
[[lem:rwg-a]], extended to spacetime as rotations of x, and C := Σ_i L_i². They generate isometries of g, so C commutes
with □ and with Υ̇⁰. As the Ω_i are tangent to the spheres and the y^a are invariant, L_i(S dy^a) = (Ω_iS)dy^a and
L_i(η dS) = η d(Ω_iS); by [[lem:rwg-a]], Σ_iΩ_i² = Δ̂, so C(S_l dy^a) = −k_l²S_l dy^a and C(η dS_l) = −k_l²η dS_l,
k_l² = l(l + 2). These eigenvalues are distinct for distinct l. □ preserves the class (G acts by isometries) and commutes
with C, so it maps the mode-l part of a class 1-form, the −k_l²-eigenspace of C in the class, into itself. Writing
□(X_aS_l dy^a + η dS_l) = J_aS_l dy^a + ζ dS_l, the coefficients of the linear differential operator (X_a, η) ↦ (J_a, ζ)
at a point y are those of □ at (y, ϑ) divided by S_l(ϑ) or S_l′(ϑ), for any ϑ where these do not vanish, so they depend
on r (through g), m₀ and l only. In the chart (y, ϑ, φ1, φ2), □ = −g^(μν)∂_μ∂_ν + (first order) on each component
([[lem:ix-2-1]] (a)); on X_aS_l dy^a + ηS_l′dϑ the second derivatives in y give −g^(ab)∂_a∂_bX_c S_l and −g^(ab)∂_a∂_bη
S_l′, and those that fall on S_l are of lower order in y. So each equation has principal part −g^(ab)∂_a∂_b, and in the
static chart −g^(ab)∂_a∂_b = f⁻¹∂_t² − f∂_r² + (first order). For h_S, C acts on its components as on those of a 1-form
of mode l (C(S_l k_ab) = −k_l²S_l k_ab and C(S_lγ) = −k_l²S_lγ, γ being invariant), and C commutes with Υ̇⁰; so Υ̇⁰(h_S)
is a class 1-form of mode l. Υ̇⁰ is a first-order operator, so Υ̇⁰(h_S) is linear in F, F_ab and their first derivatives,
and these are linear in Φ and its derivatives of order at most two by [[eq:np-10-1]].

(iv) The first sentence is [[lem:gd-r2-9]].

(a) log r, log(r + r_h) and the denominators r and r + r_h are analytic on {r > 0}. The numerator 𝔑(r) of B is analytic
there, and 𝔑(r_h) = r_h³ − 3r_h³ + 2r_h³ + 2r_h³ log r_h − 2r_h³ log r_h = 0; so 𝔑(r)/(r − r_h) is analytic, and so is
B = 𝔑(r)/((r − r_h) · 4rr_h(r + r_h)). As r → ∞, A = r_h/(4r²) + log(1 + r_h/r)/(2r_h) = 1/(2r) + O(r⁻²); and the
identity for r³(A + fB) in (b), with r³f = r(r² − m₀) and r³A = r²/2 + O(r), gives r³fB = −r²/4 + O(r log r), so
rB → −¼.

(b) We use [[lem:gd-r2-9]]. For the part (v/2)W*, with a = v/(2r²) and b = −v/(2r(r + r_h)): a + fb = vr_h/(2r³), so
φ = 1/(2r(r + r_h)), and q = r³(−1/(2r(r + r_h)) + vr⁻³) = v − r²/(2(r + r_h)). For U := A dv + B dr: from the
definitions,

    r³(A + fB) = (r − r_h)²/4 + r_h²/4 + (r_h²/2) log(1 + r/r_h),       −r³A′ = r_h/2 + r²/(2(r + r_h)),

as A′ = −r_h/(2r³) − 1/(2r(r + r_h)) and, for the first, r³A = rr_h/4 + (r³/(2r_h))(log(r + r_h) − log r) and
r³fB = r(r² − r_h²)B = 𝔑(r)/(4r_h). The derivative of the first identity is (r − r_h)/2 + r_h²/(2(r + r_h)) =
r²/(2(r + r_h)). So U has φ = −1/(2r(r + r_h)) and q = r_h/2 + r²/(2(r + r_h)), and W** has φ = 0, q = v + r_h/2.
[[eq:gd-r2-9]] gives (□W**)_v = r⁻³ and (□W**)_r = 0. Next, tr_g K̄ = g^(vv)r⁻² = 0, so
Υ̇⁰(K̄)_ν = ∇^μ(r⁻²(dv)_μ(dv)_ν), where (dv)^♯ = ∂_r. ∇^μ(r⁻²(dv)_μ) = r⁻³∂_r(r³r⁻²) = r⁻³, and ∇_(∂_r)dv = 0, as
Γ^v_(rν) = g^(vσ)Γ_(σ,rν) = Γ_(r,rν) = 0 (in the chart the only nonzero lowered symbols of the orbit metric are
Γ_(r,vv) = f′/2 and Γ_(v,vr) = −f′/2, and those mixing the factors have an angular index). So Υ̇⁰(K̄) = r⁻³dv. By
[[eq:gd-0-1]] and [[eq:hg-box]], Υ̇⁰(K_V) = Υ̇⁰(K̄) − □V^♭, so □W**_H = Υ̇⁰(K̄) − □V^♭ = Υ̇⁰(K_V).

(c) ℒ_Vg = ℒ_(V^♭)g, so K* = K̄ + ℒ_Vg + ℒ_(W**)g − ℒ_(V^♭)g = K̄ + ℒ_(W**)g. K̄ and W** are smooth across the horizon
(by (a)), so K* is. Υ̇⁰(K*) = Υ̇⁰(K̄) − □W** = 0 by (b). W** is spherically symmetric, so δm[ℒ_(W**)g] = 0 and
δm[K*] = δm[K̄] = 1 ([[lem:gd-1-4]] (a)). With ℒ_(cX)g = cℒ_Xg + 2dc ⊗_s X, ℒ_((v/2)W*)g = (v/2)ℒ_(W*)g + dv ⊗_s W*,
which gives [[eq:np-10-2-k]]; its right side has stationary coefficients, smooth across the horizon. W* is not a multiple
of (∂_v)^♭, so by [[lem:gd-1-4]] (c) it is not Killing, and ℒ_(W*)g ≠ 0.

(d) □(cvW* + U) = c[□, v]W* + cv□W* + □U = c[□, v]W* + □U, a stationary 1-form. By [[lem:iii-d1-2-1]] (1),
ℓ(□U) = 0, and by the proof of [[lem:iii-d1-3-1]] (1), ℓ([□, v]W*) = 4π². ℓ(Υ̇⁰(K̄)) = ℓ(r⁻³dv) = r_h³ · r_h⁻³ · 2π² =
2π². So 4π²c = 2π². ∎

By (d), among the gauge vectors cvW* + U with U stationary and smooth at the horizon, only c = ½ solves
□W = Υ̇⁰(K̄): the coefficient ½ of W** is the one that regularity at the horizon allows.

### The horizon charge {#sec:hg-charge}

**Lemma {#lem:gd-2-2}** (The horizon charge.) (a) For every 1-form X, at r = r_h, with F := dX,

    r³(□X)_v = ∂_v[r³(δX + F_(vr))] − r(γ^(1/2))⁻¹∂_i(γ^(1/2)γ^(ij)F_(jv)),

γ^(1/2) the density of γ in the coordinates z^i of the sphere; for a class 1-form the last term is
−(r/(cs))∂_ϑ(cs F_(ϑv)). Integrating over S³,

    (d/dv) Q[X] = ℓ(□X).                                                                                 {#eq:gd-2-1}

Q[X] depends only on the l = 0 part X_0 of X: Q[X] = Q[X_0].

(b) δW* = 0, (dW*)_(vr) = 2r⁻³ and Q[W*] = 4π². The Killing form (∂_v)^♭ = −f dv + dr has Q[(∂_v)^♭] = 4π²m₀, and
(∂_v)^♭ − m₀W* is closed. ℓ([□, v]W*) = 4π². ℓ(Υ̇⁰(K̄)) = 2π², and ℓ(Υ̇⁰(K_V)) = 2π². Q[W**](v) = 2π²(v + r_h/2),
so (d/dv)Q[W**] = 2π².

[[eq:gd-2-1]] is the time-dependent form of [[lem:iii-d1-2-1]] (1): ℓ annihilates □ of every stationary 1-form smooth
at the horizon (the case ∂_v = 0 of [[eq:gd-2-1]]). By [[lem:iii-d1-2-1]] (3), ℓ moreover spans the annihilator of the
range at zero energy.

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
proof of [[lem:iii-d1-3-1]] (1). Υ̇⁰(K̄) = r⁻³dv ([[prop:np-10-2]] (iv) (b)), so ℓ(Υ̇⁰(K̄)) = r_h³ · r_h⁻³ · 2π² = 2π²;
and K_V = K̄ near the horizon ([[eq:gd-0-1]]). By [[prop:np-10-2]] (iv) (b), W** has φ = 0 and q = v + r_h/2, and
[[lem:gd-r2-9]] gives Q[W**] = 2π²(v + r_h/2). ∎

### The harmonic-gauge solutions and the forced growth {#sec:hg-solutions}

**Lemma {#lem:gd-r3-1}** (Uniqueness on N⁺.) Let d be a 1-form on N⁺, smooth up to Σ°, with □d = 0 on N⁺ and
vanishing Cauchy data on Σ°. Then d = 0. In particular, if F_1, F_2 are smooth 1-forms on Ω^♯ that agree on N⁺, and
Z̃_1, Z̃_2 solve □Z̃_i = F_i on Ω^♯ with the same Cauchy data on Σ°, then Z̃_1 = Z̃_2 on N⁺.

*Proof.* By [[lem:ix-2-1]] (a), □ has principal part −g^(αβ)∂_α∂_β ⊗ id, and dt_IVP is timelike ([[sec:ix-0]]), so Σ° is
noncharacteristic for □. Step 3 of the proof of [[thm:ix-2-2]] uses of its operator only this. In coordinates (t_IVP, y)
near a point of Σ°, d = 0 and ∂_(t_IVP)d = 0 on Σ°; if ∂^j_(t_IVP)d = 0 on Σ° for j < m, some m ≥ 2, apply
∂^(m−2)_(t_IVP) to □d = 0 and restrict to Σ°: every term but −g⁻¹(dt_IVP, dt_IVP)∂^m_(t_IVP)d is a derivative of d of
order below m, or of order m with at most m − 1 derivatives in t_IVP, so it vanishes, and ∂^m_(t_IVP)d = 0. So d vanishes
to infinite order along Σ°, and its extension d̃ by 0 to Ω^♯ ∩ {t_IVP < 0} is smooth on Ω^♯, with □d̃ = 0 and vanishing
data on Σ°. Ω^♯ is globally hyperbolic on each component, with Cauchy hypersurface Σ° ([[lem:ix-1-2]]), and □ = 2δGδ* is
normally hyperbolic ([[sec:ix-0]]), so [[thm:std-bgp-cauchy]] (3) on each component gives d̃ = 0. For the second claim
apply the first to d := (Z̃_1 − Z̃_2)|_(N⁺). ∎

**Proposition {#prop:gd-2-1}** (The harmonic-gauge solutions.)

(a) For every 1-form Z′ on N⁺, smooth up to Σ°, with □Z′ = Υ̇⁰(e) on N⁺,

    ġ_H := ġ_RW + ṁℒ_(W**_H)g + ℒ_(Z′)g                                                                   {#eq:gd-2-gh}

is a linearised vacuum solution on N⁺, smooth up to Σ°, in harmonic gauge, inducing (γ̇, k̇) up to the data of a
linearised diffeomorphism. For all smooth Cauchy data on Σ° such a Z′ exists, and it is determined on N⁺ by its data;
for G-invariant data it is G-invariant.

(b) Let U ⊂ U^♯ be open and G-invariant, Ω′_+ := D_U(Σ_U) ∩ {t_IVP ≥ 0}, and let ġ′ be a G-invariant linearised vacuum
solution on Ω′_+, smooth up to Σ_U, in harmonic gauge, inducing (γ̇, k̇) plus the data of ℒ_Zg for a vector field Z
near Σ_U, smooth up to Σ_U. Then ġ′ = ġ_RW + ṁℒ_(W**_H)g + ℒ_(Z′)g on Ω′_+ for a G-invariant 1-form Z′ with
□Z′ = Υ̇⁰(e).

(c) (*The forcing term has no l = 0 part.*) Υ̇⁰(e)_0 = 0. So the l = 0 part Z′_0 of Z′ solves □Z′_0 = 0, and
Z′_(≥2) := Z′ − Z′_0 solves □Z′_(≥2) = J := Υ̇⁰(e), with, for every k, R′ and ε′ > 0,

    |J|_k ≤ C‖(γ̇, k̇)‖_(H^(k₁(k+3))) t_*^(−w+ε′)     on {r_♭ < r ≤ R′, t_* ≥ T′},

a loss of three derivatives.

(d) (*Non-uniqueness.*) □W* = 0, so Z′ ↦ Z′ + cW* preserves (a): ġ_H + cℒ_(W*)g is again a harmonic-gauge solution with
the same data up to a linearised diffeomorphism. A decay statement in harmonic gauge therefore concerns a chosen Z′,
the freedom being the solutions of □Y = 0 (more than the multiples of W* when the data of Y do not decay:
[[prop:gd-r2-13]] (c)).

*Proof.* (a) DRic(ġ_RW) = 0 ([[thm:rw-settling]] (a)) and DRic(ℒ_Xg) = 0 ([[lem:ix-2-1]] (b)). By
[[prop:np-10-2]] (iv) (b) and [[eq:hg-box]], Υ̇⁰(ġ_H) = ṁΥ̇⁰(K_V) + Υ̇⁰(e) − ṁ□W**_H − □Z′ = ṁΥ̇⁰(K_V) + Υ̇⁰(e) −
ṁΥ̇⁰(K_V) − Υ̇⁰(e) = 0. ġ_RW induces (γ̇, k̇) plus the data of ℒ_(X_RW)g ([[thm:rw-settling]] (a)), and W**_H and Z′ are
smooth up to Σ°. *Existence.* e is given on N⁺ only, smooth up to Σ°. As in Step 1 of the proof of [[thm:ix-2-2]], Υ̇⁰(e)
extends to a smooth 1-form F on Ω^♯: it extends to an open neighbourhood of N⁺ ([[sec:ix-0]]), and a smooth function
equal to 1 on N⁺ and supported in that neighbourhood extends it by 0 beyond. By [[lem:ix-1-1]] on Ω^♯
(globally hyperbolic on each component with Cauchy hypersurface Σ°, [[lem:ix-1-2]]), with the normally hyperbolic
operator □ ([[sec:ix-0]]), □Z̃ = F has a smooth solution on Ω^♯ with any given smooth data on Σ°, and Z′ := Z̃|_(N⁺) is
smooth up to Σ°. By [[lem:gd-r3-1]], Z′ does not depend on the extension, and two solutions on N⁺ with the same data
agree. *Invariance.* G preserves t_IVP and |x|, so N⁺, Ω^♯ and Σ°; Υ̇⁰(e) is G-invariant, and □ commutes with the action
of G. For σ ∈ G, σ*Z′ solves □(σ*Z′) = Υ̇⁰(e) on N⁺ with the data σ* of those of Z′; for G-invariant data, σ*Z′ = Z′ by
uniqueness.

(b) By [[cor:ix-2-3]] and [[rem:ix-2-4]] (c), ġ′ = ġ + ℒ_(X′)g on Ω′_+ ⊂ N⁺ with X′ G-invariant and smooth up to
Σ_U; and ġ_RW = ġ + ℒ_(X_RW)g. So ġ′ − ġ_RW = ℒ_Yg with Y := X′ − X_RW, G-invariant. Υ̇⁰(ġ′) = 0 reads
Υ̇⁰(e) + ṁΥ̇⁰(K_V) − □Y = 0, that is □(Y − ṁW**_H) = Υ̇⁰(e) by [[prop:np-10-2]] (iv) (b). Put Z′ := Y − ṁW**_H.

(c) Υ̇⁰ commutes with the SO(4)-average, and e_0 = 0, so Υ̇⁰(e)_0 = 0; □ commutes with it too, so □Z′_0 = (□Z′)_0 = 0.
Υ̇⁰(e) is first order in e, so |Υ̇⁰(e)|_k ≤ C|e|_(k+1), and [[thm:rw-settling]] (b) bounds |e|_(k+1).

(d) □W* = 0 ([[sec:hg-setting]]), and ℒ_(cW*)g = cℒ_(W*)g is a linearised diffeomorphism. ∎

**Theorem {#thm:gd-2-3}** (The forced linear growth.) Let ġ_H = ġ + ℒ_Zg be a harmonic-gauge solution of
[[prop:gd-2-1]] (a), Z = X_RW + ṁW**_H + Z′ G-invariant. Then on the horizon, for v ≥ v_0 with t_* ≥ T′ there,

    Q[Z](v) = Q[Z](v_0) + 2π²ṁ(v − v_0) + ∫_(v_0)^v ℓ(Υ̇⁰(h))(v′) dv′,        |ℓ(Υ̇⁰(h))(v)| ≤ Cv^(−w+ε′),

and Q[Z − ṁW**_H](v) converges as v → ∞. Consequently, if ṁ ≠ 0, no harmonic-gauge solution settles to ṁK_V near
the horizon at an integrable rate: there are no δ, ε > 0 for which (ġ_H − ṁK_V)_0 and its first derivatives are
O(t_*^(−1−δ)) on {|r − r_h| ≤ ε}.

*Proof.* □Z = −Υ̇⁰(ℒ_Zg) = Υ̇⁰(ġ) = ṁΥ̇⁰(K_V) + Υ̇⁰(h), as Υ̇⁰(ġ_H) = 0, and ℓ(Υ̇⁰(K_V)) = 2π² ([[lem:gd-2-2]] (b)).
ℓ(Υ̇⁰(h)) involves h and its first derivatives at r_h, bounded by [[eq:gd-0-2]], with |t_* − v| ≤ C near r_h.
Integrating [[eq:gd-2-1]] gives the identity. Near the horizon V is a constant multiple of the Killing field ∂_t
([[eq:gd-0-1]]), so there □V^♭ = −Υ̇⁰(ℒ_Vg) = 0 and Q[V^♭] is constant by [[eq:gd-2-1]]; and (d/dv)Q[W**] = 2π²
([[lem:gd-2-2]] (b)). So (d/dv)Q[ṁW**_H] = 2π²ṁ, and Q[Z − ṁW**_H] has the integrable derivative ℓ(Υ̇⁰(h)) and
converges.

Suppose ṁ ≠ 0 and (ġ_H − ṁK_V)_0 is O(t_*^(−1−δ)), with its first derivatives, on {|r − r_h| ≤ ε}, ε small. Averaging
ġ_H = ṁK_V + h + ℒ_Zg, ℒ_(Z_0)g = (ġ_H − ṁK_V)_0 − h_0, which with [[eq:gd-0-2]] is O(t_*^(−min(1+δ,w−ε′))) there,
with first derivatives. It is a spherically symmetric linearised vacuum solution with δm[ℒ_(Z_0)g] = 0
([[lem:gd-1-4]] (a)). Apply [[lem:gd-1-4]] (b) on the simply connected set {|r − r_h| < ε, v > v_1} of the orbit
space: ℒ_(Z_0)g = ℒ_(Y)g with Y = ζ∂_v + rH_L∂_r, where H_L and dζ = 𝔷 are algebraic in ℒ_(Z_0)g and its first
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
s > 5/2 (the threshold of the density argument in [[lem:iii-d1-2-1]] (3)), an SO(4)-invariant fibre inner product on
the bundle E of [[sec:iii-d-1]], which, as in [[thm:iii-h-4-1]], enters only as the index h of the L² pairing ⟨·, ·⟩_h
on X (the index is not the tensor h of [[sec:hg-setting]]), and an SO(4)-invariant φ_* ∈ C_c^∞(X°; E) with
⟨W*, φ_*⟩_h = 1 (average any choice over SO(4); W* is SO(4)-invariant).
The spaces 𝒳_σ, 𝒴_σ, 𝒳_0 = {u ∈ H̄_b^(s,α) : P̂(0)u ∈ 𝒴_0} and 𝒴_0 = H̄_b^(s−1,α+2) are those of [[sec:iii-h-1]] and
[[prop:iii-h-3-2]] for P̂. The state is W*: smooth on X, W* ∈ 𝒜², and □W* = 0.

**Definition {#def:gd-r2-1}** (The augmented operator.) Put

    f_* := □(χ^H_KW*) = [□, χ^H_K]W*,      f̂_*(σ) := ∫ e^(iσt_*)f_* dt_*,      ĝ_*(σ) := iσ⁻¹Ψ(σ, ·)W*,

with Ψ of [[lem:iii-h-2-5]], and, for (u, c) with u a section over X and c ∈ ℂ,

    P̃(σ)(u, c) := (P̂(σ)u + cf̂_*(σ), ⟨u, φ_*⟩_h).

**Lemma {#lem:gd-r2-2}** ([[lem:iii-h-2-2]]–[[lem:iii-h-2-5]] at □.)
(a) f_* vanishes outside {1 ≤ t_* ≤ 2, |x| ≤ t_*/2} ∪ {t_* ≥ 2, t_*/4 ≤ |x| ≤ t_*/2}, and its part f_∞ at r ≥ 1
obeys [[eq:iii-h-2-1]]: |(t_*∂_(t_*))^j(r∂_r)^a∂_ω^β f_∞| ≤ Cr⁻⁴.
(b) f̂_*(0) = L_1W* + L_0z_* with z_* := −κ(r)W*, κ of [[lem:iii-h-2-3]]; so z_* ∈ 𝒜¹ and f̂_*(0) ∈ 𝒜³.
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
P̃(0)(u, c) = 0. By [[lem:gd-r2-2]] (b), P̂(0)(u + cz_*) + cL_1W* = 0, and u + cz_* ∈ 𝒳_0, as 𝒜¹ ⊂ H̄_b^(∞,α) for
α < −1.
Apply ℓ. ℓ ∘ P̂(0) = 0 on 𝒳_0 ([[lem:iii-d1-2-1]] (1), with the density argument of its (3)); and
ℓ(L_1W*) = ℓ([□, t_*]W*) = 4π² ([[lem:iii-d1-3-1]] (1)). So 4π²c = 0, c = 0, u ∈ span{W*} ([[lem:iii-d1-2-1]] (2)),
and ⟨u, φ_*⟩_h = 0 gives u = 0. ∎

The block-triangular 11 × 11 pairing matrix of [[prop:iii-h-3-2]] is here the 1 × 1 matrix (4π²). The time cut-off is
what makes it nonzero: ℓ annihilates the stationary column P̂(0)(κW*) for every stationary κ smooth at the horizon
([[lem:iii-d1-2-1]] (1)), and an augmentation by such a column is not invertible at zero energy: ℓ vanishes on the
first component of its range ([[lem:iii-d1-2-1]] (1), with the density argument of its (3)), but not on 𝒴_0, as
ℓ(L_1W*) = 4π² ([[lem:iii-d1-3-1]] (1)).

**Theorem {#thm:gd-r2-4}** (Uniform low-energy estimates for P̃.) There are c_k > 0 and C_k such that for σ ∈ Σ_0
with |σ| ≤ c_k, P̃(σ) : 𝒳_σ ⊕ ℂ → 𝒴_σ ⊕ ℂ is invertible with the estimate [[eq:iii-h-4-5]] (with |c| in place
of |ḃ| + |S|); [[thm:iii-h-4-1]] (3) holds for P̃ on Σ_0 ∩ ℝ; and, with (u, c) := P̃(σ)⁻¹(f, 0) for 0 < |σ| ≤ c_0,

    P̂(σ)⁻¹f = u + c ĝ_*(σ).                                                                              {#eq:gd-r2-1}

*Proof.* [[thm:iii-h-4-1]] is stated for every family P̂ with (H1)–(H4), (G), (TF) and index 0 at σ ≠ 0, which the
setting gives, and columns with (A1)–(A4), which [[lem:gd-r2-2]] (b)–(c) give with ϵ_0 = ¼(1 − (α + 2)) exactly as in
the proof of [[cor:iii-h-4-2]]; its (Z_𝒫) is [[prop:gd-r2-3]]. P̂(σ) is invertible for every σ ≠ 0 with Im σ ≥ 0
([[prop:iii-d-6-1]], [[prop:iii-d-6-2]]), so no scaling argument is needed at small σ, and [[eq:gd-r2-1]] follows
from [[lem:gd-r2-2]] (d) as [[eq:iii-h-4-6]] follows in the proof of [[cor:iii-h-4-3]]. ∎

### □ is 1-admissible {#sec:hg-admissible}

𝒪_c(□) denotes the class of orders of [[def:iii-h1-1-1]] with □ in place of L_b and the K⁺-weight −1 in place of
−2: the t_*-translation-invariant orders 𝗌 that are stationary-□-admissible with weights α_sf, −1 and margin 1
([[def:ii-c-2-4]]) and satisfy (C1)–(C3) there. The spaces H^((𝗌;k),(β,γ))_(3b;b), on Ω, M_0 and Ω_−, are those of
[[sec:iii-h1-1]], with r_0 = r_♭.

**Theorem {#thm:gd-r2-5}** (□ is 1-admissible; [[thm:iii-h1-1-3]] at □.) Let α_sf + 2 ∈ (0, 1), k ∈ ℕ_0,
𝗌 ∈ 𝒪_c(□) and f ∈ H^((𝗌;k),(α_sf+2,0))_(3b;b)(Ω)^(•,−), with norm ‖f‖. The forward solution u of □u = f satisfies,
with C independent of f:

(i) u = u′ + u_sing with ‖u′‖_(H^((𝗌;k),(α_sf,0))_(3b;b)(M_0)) ≤ C‖f‖;

(ii) u_sing = β(t_*, r)W*, where for one function B on ℝ with Σ_(j≤k)‖(t∂_t)^jB‖_(L²(ℝ)) ≤ C‖f‖,

    ∂_(t_*)β(·, r) = (∂_tχ^H_K)(·, r) ∗ B,        β(·, r) − β(·, r′) = (χ^H_K(·, r) − χ^H_K(·, r′)) ∗ B,

∗ the convolution in t_*;

(iii) ‖u‖_(H^((𝗌−1;k),(α_sf,−1))_(3b;b)(Ω)^(•,−)) ≤ C‖f‖.

So □ is 1-admissible with sf-weight α_sf, sf-loss 0 and margin 1 at b₀, in the relaxed form of [[def:ii-c-2-7]], for
orders in 𝒪_c(□) and every k: (1) of [[def:ii-c-2-7]] holds by [[lem:iii-d-5-2]] at γ_Υ = 0, (2) by
[[lem:iii-d-7-1]] (whose gap is (0, 2) when e_Υγ_Υ² = 0) at the weight α_sf + 2 ∈ (0, 1), and (3) by (iii).

*Proof.* We follow [[sec:iii-h1-2]]–[[sec:iii-h1-7]] with L_b replaced by □ and L̃_b by P̃ ([[thm:gd-r2-4]]); the eleven
states reduce to W*, of weight 2, with no generalised state, and the two integrations of [[sec:iii-h1-7]] (iv)–(v)
reduce to one. What these sections take from L_b holds for □ as follows.

- [[lem:iii-h1-1-2]] (*orders*). With the K⁺-weight −1 and margin 1, [[def:ii-c-2-4]] (5)–(6) give
  𝗌 + α_sf + 1 > ½(−1 + ϑ_in) + 1 at the incoming radial set and 𝗌 + α_sf + 1 < ½(−1 + ϑ_out) − 1 ≤ −3/2 + S̄ at the
  outgoing one, inside the interval that [[lem:iii-h1-1-2]] (a) needs; and (4) gives s_c > 3/2 + ϑ_ℋ = 5/2
  ([[lem:iii-d-5-1]]).
- [[lem:iii-h1-2-1]]: high energies ([[thm:i-b-1-3]] (3), [[prop:iii-d-6-1]]), invertibility at every σ ≠ 0 with
  Im σ ≥ 0 ([[prop:iii-d-6-2]]), and uniqueness of forward solutions ([[prop:ii-e-3-4]]).
- [[lem:iii-h1-3-1]]: [[thm:i-b-1-3]] (5) with δ_Γ(0) < 1/(2(k + 1)); [[lem:iii-d-5-2]] gives δ_Γ(0) as small as
  wished at b₀, so b₀ ∈ ℬ_k for every k, as [[prop:iii-f-4-1]] gives for L_b.
- [[lem:iii-h1-4-1]]–[[lem:iii-h1-4-2]]: [[thm:gd-r2-4]].
- [[lem:iii-h1-5-1]], for the one state, of weight q = 2: ∂_(t_*)u_sing ∈ H^((p;k),(α_sf+1,0))_(3b;b)(M_0) for every
  p, the sf-weight α_sf + 1 being negative, as the proof of that lemma requires.
- [[sec:iii-h1-7]]: (i) as there, with u′ := u_hi + u_reg; (ii) u_sing = −u′ on Ω_−; then [[lem:iii-h1-6-2]] once,
  for u_sing, with the order 𝗌 − 1 and the lemma's two weight parameters (its β and ℓ) equal to α_sf + 1 and 1: the
  data of weights (α_sf, 0) ⊂ (α_sf, −1) on Ω_− and ∂_(t_*)u_sing of weights (α_sf + 1, 0) give
  u_sing ∈ H^((𝗌−1;k),(α_sf,−1))_(3b;b)(M_0). With (i) this is (iii).

For (ii): by the proof of [[lem:iii-h1-5-1]], ℱ(∂_(t_*)u_sing) = χ(|σ|)Ψb̂_1W* on ℝ, where Ψ(·, r) is the Fourier
transform of ∂_tχ^H_K(·, r) ([[lem:iii-h-2-5]]). B := ℱ⁻¹(χb̂_1) is bounded as stated by [[lem:iii-h1-4-2]] and
Plancherel's theorem, as ℱ(t∂_tB) = −(1 + σ∂_σ)ℱB. The first identity is then the convolution theorem. For the second,
χ_(r,r′) := χ^H_K(·, r) − χ^H_K(·, r′) lies in C_c^∞([1, max(2, 4r, 4r′)]) (both functions vanish for t_* ≤ 1 and equal 1
for t_* ≥ max(2, 4r, 4r′)), so β(·, r) − β(·, r′) − χ_(r,r′) ∗ B has zero t_*-derivative; it is square integrable as
t_* → −∞, where u_sing = −u′, so it vanishes. (i) and (ii) extend to general f by density, u′ and B by continuity. ∎

**Remark {#rem:gd-orders}** (The orders used with □.) [[thm:ii-f1-1-1]], in the relaxed form of [[rem:ii-f1-7-1]],
is applied to □ below with the orders of [[prop:ii-c-5-1]] built for □. They lie in 𝒪_c(□): the proof of
[[lem:iii-i-5-1]] uses the construction of [[prop:ii-c-5-1]] and the Hamilton flow of G_0, and of the operator only the
constants s_in and s_out, which it does not constrain.

### Decay modulo W*: the coefficient is the horizon charge {#sec:hg-modulo}

**Lemma {#lem:gd-r2-6}** (Sobolev embedding on an interval, rescaled.) If H is a Hilbert space and w, t∂_tw ∈
L²([T/2, 4T]; H), T > 0, then

    sup_([T,2T]) ‖w(t)‖²_H ≤ C T⁻¹ ∫_(T/2)^(4T) (‖w‖²_H + ‖t∂_tw‖²_H) dt,

with C absolute.

*Proof.* Put W(s) := w(Ts) for s ∈ [½, 4]. Then W′(s) = T w′(Ts) = (t∂_tw)(Ts)/s, so ∫_(1/2)^4 (‖W‖² + ‖W′‖²) ds ≤
4T⁻¹∫_(T/2)^(4T)(‖w‖² + ‖t∂_tw‖²) dt. For s, s′ ∈ [½, 4], ‖W(s)‖ ≤ ‖W(s′)‖ + ∫_(1/2)^4‖W′‖; averaging over s′ and
using Cauchy–Schwarz, sup ‖W‖² ≤ 2(2/7 + 7/2)∫_(1/2)^4(‖W‖² + ‖W′‖²) ds. ∎

**Theorem {#thm:gd-r2-7}** (Decay modulo W*.) Let k ≥ 1, j ≥ 0, R′ > r_♭, and 𝗌 ∈ 𝒪_c(□) with 𝗌 ≥ j + 3 over
{r ≤ R′ + 1} (such orders exist: [[def:ii-c-2-4]] bounds 𝗌 above only near the outgoing radial set, which lies over
sf, and the monotonicity runs towards it). Let f ∈ H^((𝗌;k),(α_sf+2,0))_(3b;b)(Ω)^(•,−), u the forward solution of
□u = f, and v_h(t_*) the value of v at (t_*, r_h). On {r_♭ < r ≤ R′, t_* ≥ 4 max(R′, 1)}, with j derivatives in x and
k − 1 derivatives ∂_(t_*),

    |u − c_f(t_*)W*| ≤ C t_*^(−1/2)‖f‖,        c_f(t_*) := (4π²)⁻¹ ∫_(−∞)^(v_h(t_*)) ℓ(f)(v′) dv′.          {#eq:gd-r2-2}

In particular: (a) if f has no l = 0 part, ℓ(f) = 0 and u = O(t_*^(−1/2)); (b) if ∫_v^∞|ℓ(f)| ≤ C′v^(−κ), then
u = c_∞W* + O(t_*^(−min(1/2,κ))), c_∞ := (4π²)⁻¹∫ℓ(f).

*Proof.* (1) Q[u](v) = 4π²c_f(t_*) at v = v_h(t_*): this is [[eq:gd-2-1]] (which holds for every 1-form) with
□u = f, as u = 0 for t_* < 1.

(2) For a function β(t_*, r), β(t_*, r)W* is a 1-form a dv + b dr with a = βr⁻² and b = −β/(r(r + r_h)), β written
in (v, r) near the horizon (t_* − v is a function of r there). By [[lem:gd-r2-9]], using W*^v = W*_r and
W*^r = r_hr⁻³, φ = δ(βW*) = −W*^μ∂_μβ = ∂_vβ/(r(r + r_h)) − r_hr⁻³∂_rβ and
q = r³(∂_vβW*_r − ∂_rβW*_v) + 2β; at r_h, r_h³φ + q = 2β − 2r_h∂_rβ, so

    Q[βW*] = 4π²(β − r_h∂_rβ)|_(r=r_h),     ∂_r at fixed v.

By [[thm:gd-r2-5]] (ii), ∂_rβ|_v = ∂_rβ|_(t_*) + (∂_rt_*)|_v∂_(t_*)β is the convolution of B with a kernel in C_c^∞
(∂_rχ^H_K and ∂_tχ^H_K at r near r_h), and |B(t)| ≤ Ct^(−1/2)‖f‖ for t ≥ 1 by [[lem:gd-r2-6]] with H = ℂ.

(3) Q[u′] involves u′ and its first derivatives on the horizon sphere, so |Q[u′](v)| ≤ C‖u′(t_*)‖_(H²(𝒰_h)), 𝒰_h a
compact neighbourhood of the horizon sphere in X, by the trace theorem. By [[thm:gd-r2-5]] (i), whose norm on compact
r-sets controls t∂_t and 𝗌 ≥ 2 derivatives in L²(dt dx), and [[lem:gd-r2-6]], ‖u′(t_*)‖_(H²(𝒰_h)) ≤ Ct_*^(−1/2)‖f‖.

(4) Hence 4π²β(t_*, r_h) = Q[u] − Q[u′] + 4π²r_h∂_rβ = 4π²c_f + O(t_*^(−1/2)‖f‖), and for r_♭ < r ≤ R′,
β(t_*, r) = β(t_*, r_h) + (χ_(r,r_h) ∗ B)(t_*) = c_f + O(t_*^(−1/2)‖f‖), with χ_(r,r′) as in the proof of
[[thm:gd-r2-5]].

(5) u − c_fW* = u′ + (β − c_f)W*. The first term is bounded by [[thm:gd-r2-5]] (i) and [[lem:gd-r2-6]] in H^(j+3) ⊂ C^j
on compact subsets of X. For the second, ∂^i_(t_*)(β − c_f) = (∂^i_tχ^H_K) ∗ B − ∂^(i−1)_(t_*)ℓ(f)/(4π²) for i ≥ 1, as
dv_h/dt_* = 1; the first term is bounded by the supremum of |B| over a window of bounded length, and the second by
[[lem:gd-r2-6]] applied to ℓ(f), whose (t∂_t)^i are square integrable for i ≤ k. The r-derivatives of β are convolutions
of B with kernels in C_c^∞. The kernels ∂_tχ^H_K, ∂_rχ^H_K and χ_(r,r_h) are supported in [1, 4 max(R′, 1)]. For t_* ≥ 8
max(R′, 1) the convolutions sample B on [t_*/2, t_*], where [[lem:gd-r2-6]] gives O(t_*^(−1/2)‖f‖). On the bounded range
4 max(R′, 1) ≤ t_* ≤ 8 max(R′, 1), B = ℱ⁻¹(χb̂_1) is bounded, |B| ≤ ‖χb̂_1‖_(L¹) ≤ C‖f‖, and C‖f‖ ≤ C′t_*^(−1/2)‖f‖
there.

For general f, both sides of [[eq:gd-r2-2]] depend continuously on f on bounded time intervals
([[thm:gd-r2-5]] (iii); ℓ(f) ∈ L²_loc), and C_c^∞(Ω°) is dense. (a): ℓ(f) depends only on the l = 0 part of f, by the
argument of [[lem:gd-2-2]] (a). (b): |c_f − c_∞| ≤ C′v_h^(−κ)/(4π²). ∎

c_f need not converge, ℓ(f) being only square integrable; c_fW* is then the growth that the K⁺-weight −1 of
[[thm:gd-r2-5]] (iii) allows, and all of it is along W*.

### The forcing term near K⁺ {#sec:hg-source}

The gauge modifications Υ⁰, Υ^(E_Υ), E^Υ and c_Υ are those of [[def:iii-b-6-1]], and Υ̇, ϑ_tot, p⃗′, q′ and h′ those of
[[sec:viii-0]] and [[thm:viii-2-2]].

**Lemma {#lem:gd-r2-10}** (The gauge identity.) For every symmetric 2-tensor k,
Υ̇⁰(k) = (d/dε)Υ⁰(g + εk, g)|_(ε=0) = −δGk. Hence Υ̇ := D_1Υ^(E_Υ)(g, g) = Υ̇⁰ − E^Υ_gG_g and
D_2Υ^(E_Υ)(g, g) = −Υ̇. In the class, on Ω_*, with ġ_(p⃗′) of [[thm:viii-2-2]] (5),

    Υ̇⁰(ġ − ġ_(p⃗′)) = E^Υ_gG_g(ġ − ġ_(p⃗′)) + Dϑ_tot(p⃗′),     ġ_(p⃗′) = χ_KṁK_V,

and so

    J_h := Υ̇⁰(h) = E^Υ_gG_gh + Dϑ_tot(p⃗′)     on {χ_K = 1},     h = ġ − ṁK_V.                            {#eq:gd-r2-3}

No derivative of h enters J_h, and E^Υ_(g,∞) carries the factor |x|⁻¹ of c_Υ = |x|⁻¹dt.

*Proof.* By [[eq:iii-b-6-3]], Υ⁰(g′, g)_μ = g′_μκg′^(ατ)(Γ(g′)^κ_ατ − Γ(g)^κ_ατ), and the difference vanishes at
g′ = g; so the derivative is g_μκg^(ατ)Γ̇^κ_ατ with Γ̇^κ_ατ = ½g^(κλ)(∇_αk_λτ + ∇_τk_λα − ∇_λk_ατ) (the proof of
[[lem:ix-2-1]] (a)), that is ∇^αk_αμ − ½∇_μ tr_g k = −(δGk)_μ, as in [[sec:ix-0]]. The term
−E^Υ_(g_0)G_(g_0)(g′ − g_0) of Υ^(E_Υ)(g′, g_0) has the derivative −E^Υ_gG_g in g′ at (g, g).
Υ^(E_Υ)(g_0, g_0) = 0 for every metric g_0 ([[sec:viii-0]]), so (D_1 + D_2)Υ^(E_Υ)(g, g) = 0. [[thm:viii-2-2]] (5)
then reads Υ̇(ġ − ġ_(p⃗′)) − Dϑ_tot(p⃗′) = 0 on Ω_*, where ġ_(p⃗′) = D_0g_(p⃗)(U′) and
g_(p⃗) = (1 − χ_K)φ*_(−S,−S⁰)g + χ_Kg_b is the translated background of [[sec:viii-0]]. Differentiating at p⃗ = 0,
ġ_(p⃗′) = (1 − χ_K)(ġ_(S′) + ġ⁰_(S⁰′)) + χ_K∂_bg_b(ḃ) ([[eq:viii-0-2]] and the identity after it). In the class
S′ = S⁰′ = 0 and ḃ = (ṁ, 0) ([[cor:viii-2-3]]), so ġ_(S′) = ġ⁰_(S⁰′) = 0, and ġ_(p⃗′) = χ_KṁK_V, as
∂_mg_((m,0))|_(m=m₀) = K_V ([[sec:rw-setting]]). Where χ_K = 1, ġ − ġ_(p⃗′) = h. ∎

**Lemma {#lem:gd-r2-11}** (Forcing terms in a cone.) Let F be smooth, supported in {t_* ≥ 2, r ≤ t_*/4},
with |(t_*∂_(t_*))^i(r∂_r)^j∂^m_ωF| ≤ Cr^(−a_ι)(r/t_*)^(b_K) on {r ≥ 1} and ≤ Ct_*^(−b_K) on {r ≤ 1}, for all i, j and
multi-indices m. If b_K > ½ and a_ι > a + 5/2, then F ∈ H^((𝗌;k),(a,0))_(3b;b)(Ω)^(•,−) for every 𝗌 and k.

*Proof.* On the cone, r∂_(t_*) = (r/t_*)t_*∂_(t_*) and r∂_x are b-vector fields with coefficients bounded with all
their b-derivatives, so b-regularity gives every 3b-order. There ρ_sf = r⁻¹, and the K⁺-weight of the space is 0.
With |dt_* dx| = r³dt_* dr dω, the square of the norm is bounded by C∫_1^∞∫_(4r)^∞ r^(2a−2a_ι)(r/t)^(2b_K)r³ dt dr.
For b_K > ½ the t-integral is 4^(1−2b_K)r/(2b_K − 1), and the r-integral of r^(2a−2a_ι+4) converges if and only if
a_ι > a + 5/2. On {r ≤ 1}, t_*^(−b_K) is square integrable on [2, ∞) as b_K > ½. ∎

*Orders.* For a tensor u on {χ_K = 1, t_* ≥ T_0} we say that u has *ι⁺-order* A and *K⁺-order* B if its components
in the frame dt_*, dx satisfy |(t_*∂_(t_*))^i(r∂_r)^j∂^m_ωu| ≤ Cr^(−A)(r/t_*)^B on {r ≥ 1} and ≤ Ct_*^(−B) on
{r ≤ 1}, for all i, j and m. Near ι⁺ ∩ K⁺, with ρ_+ = 1/r and ρ_K = r/t_*, the bound is ρ_+^Aρ_K^B. A product
a(t_*)P(x), with |(t∂_t)^ia| ≤ Ct^(−c) and P of spatial order m (|(r∂_r)^j∂^n_ωP| ≤ Cr^(−m) for r ≥ 1), has
ι⁺-order c + m and K⁺-order c, as t_*^(−c)r^(−m) = r^(−(c+m))(r/t_*)^c; a factor that is a power of log t_* costs an
arbitrarily small amount of either order.

*The cone cut-off.* Fix T_1 ≥ max(T′_♭, 2) and put χ′ := χ_+(t_*/T_1)χ_c(10r/t_*), χ_+ and χ_c as in
[[eq:iii-h-1-2]]. As t ≥ t_IVP ≥ t_* ([[lem:iii-b-3-7]] (b), [[sec:iii-k-0]]),

    supp χ′ ⊂ {t_* ≥ T_1, r ≤ t_*/20} ⊂ {|x| < t/10, t > T′_♭} ⊂ int{χ_K = 1},

and χ′ = 1 on {t_* ≥ 2T_1, r ≤ t_*/40}; also supp χ′ ⊂ {t_* ≥ 2, r ≤ t_*/4}, as [[lem:gd-r2-11]] asks.

Let ϰ_♯ := 3/2 + (1 − e_Υ)γ_Υ ([[eq:iii-g3-0-1]]) and δ_♯ := ϰ_♯ − 3/2 = (1 − e_Υ)γ_Υ > 0, the margin by which the
constraint damping makes the gauge forcing term decay along the forward cone.

**Proposition {#prop:gd-r3-2}** (The orders of the forcing term near K⁺.) For every β ∈ (0, δ_♯) and η ∈ (0, δ_♯ − β),
on {χ_K = 1, t_* ≥ T_0}:

- h = h_(b₀,rem)(q′) + h′ has ι⁺-order ϰ_♯ − η > 3/2 + β and K⁺-order w − η > ½;
- Dϑ_tot(p⃗′) has ι⁺-order ϰ_♯ + 1 − η > 5/2 + β and K⁺-order above ϰ_♯ + 3;
- J_h of [[eq:gd-r2-3]] has ι⁺-order ϰ_♯ + 1 − η > 5/2 + β and K⁺-order w − η > ½.

Each bound is by finitely many seminorms of U′, so ([[thm:viii-2-2]] (6)) of the data.

*Proof.* *h′.* By [[thm:viii-2-2]] (3), h′ ∈ 𝒳^∞_(J,ex) = H^(∞,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_+,3+ε_+),α)_b ([[def:iii-j3-1-1]]): a
partial expansion at ι⁺ with exponents in ℰ_+ up to the weight 3 + ε_+, whose coefficients and remainder have the
K⁺-weight α = w + 2 (α that of [[thm:viii-2-2]] (4)), and K⁺-weight w + 2 elsewhere near K⁺. ℰ_+ ⊂ {Re ≥ ϰ_♯} by (H1)
of [[sec:iii-i9-1]]. By b-Sobolev embedding for the unweighted b-density ([[lem:ii-a-8-8]]), h′ and its b-derivatives
are O(ρ_+^(ϰ_♯−η)ρ_K^(w+2−η)) near ι⁺ ∩ K⁺, O(ρ_+^(ϰ_♯−η)) near (ι⁺)° and O(t_*^(−w−2+η)) near K⁺, for every
η > 0, the logarithms costing η; and t_*∂_(t_*), r∂_r, ∂_ω span the b-vector fields there. So h′ has ι⁺-order
ϰ_♯ − η and K⁺-order w + 2 − η.

*h_(b₀,rem)(q′).* By [[lem:iii-i14-2-2]] (a) it has K⁺-order w − η for every η > 0 and, at ι⁺, a partial expansion of
plain weight at least ϰ_♯; by [[eq:iii-i14-1-2]] it is a finite sum of products a(t_*)P(x) with stationary P. For a
product, the K⁺-rate c and the ι⁺-order c + m of the orders paragraph are those two numbers, so each product has the
joint orders (ϰ_♯ − η, w − η).

*Dϑ_tot(p⃗′).* ϑ_tot(p⃗) = ϑ_(tot,2)(p⃗_(≤0)) + Σ_ν ϑ_(ν,♯)(W_ν), summed over the rows ν = (τ, ϰ, k) of
[[sec:iii-i9-1]] (τ the type of the row and (ϰ, k) an element of its index set: ι⁺-exponent ϰ, logarithmic power k)
and the rotation rows of [[def:iii-i14-1-3]] ([[def:iii-i9-2-3]]). The terms of ϑ_(tot,2) carry a factor dχ_K
([[def:iii-i4-2-1]], [[def:iii-i7-2-1]]) and vanish on {χ_K = 1}, where dχ_K = 0 (χ_K takes values in [0, 1]). Where
χ_K = 1 a row term is ϑ_(ν,♯)(W) = ½□^Υ_(b₀)ω_ν(W) ([[lem:iii-i9-2-2]] (d)), which by [[eq:iii-i9-2-2]] is

    ½[a^((K_τ+1))(A_1ω̆^(K_τ)_τ + A_2ω̆^(K_τ−1)_τ) + a^((K_τ+2))A_2ω̆^(K_τ)_τ],

with ω̆^i_τ ∈ 𝒜^((ς_τ−i,0)+ℱ) ([[eq:iii-i9-2-1]]), a^((i)) of rate e_ν + i, e_ν = ϰ − 1 − ς_τ (the proof of
[[lem:iii-i9-2-2]] (b); for s0 the rate is ϰ − 1 + i), and A_1, A_2 the coefficients of ∂_(t_*) and ∂²_(t_*) in
□^Υ_(b₀). By [[lem:iii-d-2-1]] (2)–(3), with the E_Υ-term of □^Υ, A_1 = −2ρ(ρ∂_ρ − 3/2 − S̄) + Q_(b₀) ∈ ρDiff¹_b and A_2
= −g^(00) ∈ ρ²C^∞ near ∂X: they gain one and two spatial orders. So the first product has rate c = e_ν + K_τ + 1 and
spatial order ς_τ − K_τ + 1, hence ι⁺-order ϰ + 1 and K⁺-order e_ν + K_τ + 1, which is κ_ν of [[lem:iii-i9-2-2]] (d);
the other two have ι⁺-order ϰ + 3 and K⁺-orders κ_ν and κ_ν + 1. The ℱ-shifts only raise orders (min Re ℰ_ind > 0).
Every row has Re ϰ ≥ ϰ_♯ ([[eq:iii-i9-1-2]]; the rotation rows have (ϰ, k) in ℳ_rot = ℳ ∪ (ℰ_♯ ∩ {Re = 2}) of
[[def:iii-i14-1-1]], and ϰ_♯ < 2), and κ_ν > ϰ_♯ + 3 ([[lem:iii-i9-2-2]] (d)). Dϑ_tot(p⃗′) is linear in p⃗′, with
seminorms O(|p⃗′|) ([[lem:iii-i9-2-2]]).

*J_h.* By [[eq:gd-r2-3]], J_h = E^Υ_gG_gh + Dϑ_tot(p⃗′). On {χ_K = 1} near K⁺ and ι⁺, |x| ≥ 3R₁ or |x| is bounded;
E^Υ_(g,H) is compactly supported in space, and E^Υ_(g,∞) is |x|⁻¹ times coefficients smooth on X̄, which gains one
ι⁺-order and no K⁺-order. So J_h has ι⁺-order min(ϰ_♯ − η + 1, ϰ_♯ + 1 − η) and K⁺-order w − η.

*The inequalities.* η < δ_♯ − β gives ϰ_♯ − η > 3/2 + β; and w > 2 ([[sec:hg-setting]]), so w − η > ½ for
η < δ_♯ < ¼ (0 < e_Υ < 1 and 0 < γ_Υ < ¼, [[eq:iii-c-1-1]]). ∎

### The harmonic gauge on the late region {#sec:hg-late}

On Ω_*, in the class, [[lem:gd-r2-10]] gives

    Υ̇⁰(ġ) = E^ΥG(ġ − χ_KṁK_V) + Dϑ_tot(p⃗′) + ṁΥ̇⁰(χ_KK_V).                                              {#eq:gd-r3-1}

With □W**_H = Υ̇⁰(K_V) ([[prop:np-10-2]] (iv) (b)) put, on N⁺,

    F_Y := Υ̇⁰(ġ) − ṁ□(χ_KW**_H),

so that on Ω_*

    F_Y = E^ΥG(ġ − χ_KṁK_V) + Dϑ_tot(p⃗′) + ṁ([Υ̇⁰, χ_K]K_V − [□, χ_K]W**_H).                              {#eq:gd-r3-2}

So F_Y = J_h on {χ_K = 1}. On {χ_K = 0}, F_Y = E^ΥGġ: the row terms are supported in supp χ_K ([[lem:iii-i9-2-2]] (c))
and the terms of ϑ_(tot,2) carry dχ_K. In particular F_Y = E^ΥGġ near ℐ⁺, as supp χ_K ⊂ {|x| < t/2}
([[sec:iii-b-5]]). The commutator terms live on supp dχ_K, which meets ∂M only in a compact subset of (ι⁺)°.

**Lemma {#lem:gd-r3-5}** (The forcing term in the class of [[thm:ii-f1-1-1]].) Let β ∈ (0, δ_♯), b_+ := β + ½,
b_I ∈ (b_+, 3/2), and χ ∈ C^∞(ℝ) equal to 0 on (−∞, 2] and to 1 on [3, ∞). Then for P_0 = □ the conditions
[[eq:ii-f1-1-3]] hold in the form of [[cor:ii-f1-1-2]], b_I < 3/2 + S̄ and b_+ < b_I, and χ(t^♭_*)F_Y lies in
H^(∞,(b_I+1,b_++2,1/2))_b(Ω_*, μ_b)^(•,−), the space of [[eq:ii-f1-1-4]] in that form.

*Proof.* *The conditions.* S̄ = 0 for □ ([[lem:iii-d-3-1]] at γ_Υ = 0), so they read b_I < 3/2 and b_+ < b_I. *Weights.*
A conormal tensor whose pointwise orders at ℐ⁺, ι⁺ and K⁺ exceed b_I + 1, b_+ + 2 and ½ lies in the space, the density
μ_b being a b-density. *ℐ⁺.* There F_Y = E^ΥGġ, with E^Υ_(g,∞)k = −γ_Υ(2ι_(g⁻¹c_Υ)k − (2/3)(1 − e_Υ)c_Υ tr_g k) and c_Υ
= |x|⁻¹dt. The vector g⁻¹c_Υ has no angular component, and the other term is a trace; G_gġ differs from ġ by a multiple
of g tr_gġ. So E^ΥGġ does not involve the trace-free angular part π̸₀ġ of [[sec:iii-c-3]]. Near ℐ⁺, ġ has the classes of
[[eq:iii-c-3-3]] slot by slot (h′ ∈ 𝒳^∞_(J,ex) by [[def:iii-j3-1-1]], χ_−ḣ by [[prop:viii-1-2]] (2), the terms with χ_K
vanishing there), with the exponents of [[eq:iii-c-3-2]]: above 3/2 + 2γ_Υ for π_C, ϰ_♯ for π₀₁, 3/2 + γ_Υ for π_(1/),
ϰ_♯ and 3/2 + 2γ_Υ for π₁₁, and 3/2 for π̸₀, the radiation field. Without π̸₀ the least is ϰ_♯, as e_Υ ≥ 0, and |x|⁻¹
adds one: the ℐ⁺-order is ϰ_♯ + 1 − η > 5/2 > b_I + 1. *ι⁺.* On {χ_K = 1} the order is ϰ_♯ + 1 − η ([[prop:gd-r3-2]]).
Elsewhere near ι⁺: ġ − χ_KṁK_V = h′ + h_rem(q′) + Dh_tot(p⃗′) has ι⁺-order ϰ_♯ − η, as the terms of h_tot lie in 𝒜^𝒢,
𝒜^(𝒢+1) ([[lem:iii-i7-2-2]], 𝒢 = (2, 0) ∪ (2 + ℰ_ind), [[eq:iii-i7-1-1]]) and 𝒜^((ϰ,k)+ℱ) ([[lem:iii-i9-2-2]] (b)), so
E^ΥG of it has ι⁺-order ϰ_♯ + 1 − η; Dϑ_tot(p⃗′) has min(3, ϰ_♯ + 1) − η ([[eq:iii-i7-2-1]], [[lem:iii-i9-2-2]] (b));
[Υ̇⁰, χ_K]K_V has order 3, as dχ_K ∈ ρ_+C^∞ and K_V is stationary in |x|⁻²C^∞(X̄); [□, χ_K] = (□_0χ_K) − 2∇_(∇χ_K) gains
two orders near (ι⁺)°, as ∂χ_K ∈ ρ_+C^∞ there ([[sec:iii-i4-1]]) and Cartesian derivatives map ρ_+^aC^∞ into
ρ_+^(a+1)C^∞, and W**_H has order 1 on (ι⁺)°, as |rA|, |rB| and |r∂_mT_m| are bounded and r(v/2)|W*| ≤ C t_*r⁻¹ is
bounded there; so [□, χ_K]W**_H has order 3. Every one of these exceeds b_+ + 2 = β + 5/2. *K⁺.* On {χ_K = 1}, w − η > ½;
supp dχ_K and {χ_K < 1} stay away from K⁺. *Support.* χ(t^♭_*)F_Y vanishes on {t^♭_* < 2}. ∎

Without the term ṁ□(χ_KW**_H) the forcing term near K⁺ would be J_h + ṁΥ̇⁰(K_V), and Υ̇⁰(K_V) = r⁻³dv near the
horizon is stationary and nonzero, of K⁺-order 0, below the ½ of the space. That is why the mass change is carried
explicitly by W**.

**Theorem {#thm:gd-r3-4}** (The harmonic gauge on the late region.) Let β, b_+, b_I and χ be as in [[lem:gd-r3-5]].
□ is 1-admissible with sf-weight α_+ := β − 2 and sf-loss 0 ([[thm:gd-r2-5]] (iii), α_+ + 2 = β ∈ (0, 1)), in the
relaxed form of [[rem:ii-f1-7-1]], with the orders of [[rem:gd-orders]]. Let Y be the forward solution on Ω_* of
□Y = χ(t^♭_*)F_Y ([[thm:ii-f1-1-1]] at P = P_0 = □), extended by 0 to N⁺, and put

    Z := ṁχ_KW**_H + Y,        ġ_H := ġ + ℒ_Zg   on N⁺.

(i) ġ_H is G-invariant, DRic(ġ_H) = 0, and ġ_H = ġ on N⁺ ∩ {t^♭_* < 2}; so it induces (γ̇, k̇) exactly.

(ii) Υ̇⁰(ġ_H) = (1 − χ(t^♭_*))χ^♮_0E^ΥGġ, with χ^♮_0 of [[lem:iii-k-1-1]]. So ġ_H is in harmonic gauge on
N⁺ ∩ {t^♭_* ≥ 3}, out to ℐ⁺, and near Σ°, where χ^♮_0 = 0.

(iii) On each {r_♭ < r ≤ R′, t_* ≥ T′}, with the derivatives of [[eq:gd-r2-2]],

    |ġ_H − ṁK* − c_∞ℒ_(W*)g| ≤ Ct_*^(−1/2),        c_∞ := (4π²)⁻¹ ∫ ℓ(χ′J_h + [□, χ′]Y) dv,

a horizon charge, χ′ the cone cut-off of [[sec:hg-source]].

*Proof.* (i) χ_K = 0 on {t^♭_* < T_K} ⊃ {t^♭_* < 10}, and Y = 0 on {t^♭_* < 2}; ġ induces (γ̇, k̇)
([[cor:viii-2-3]]). DRic(ℒ_Zg) = 0 ([[lem:ix-2-1]] (b)). *G-invariance.* ġ, χ_K, χ(t^♭_*) and W**_H, and so F_Y, are
G-invariant, and □ commutes with the action of G; so σ_*Y is again a forward solution of □Y = χ(t^♭_*)F_Y, and
σ_*Y = Y by the uniqueness of forward solutions ([[thm:ii-f1-1-1]]). Hence Z and ġ_H are G-invariant.

(ii) By [[eq:hg-box]] and the definition of F_Y, Υ̇⁰(ġ_H) = Υ̇⁰(ġ) − ṁ□(χ_KW**_H) − χ(t^♭_*)F_Y =
(1 − χ(t^♭_*))(Υ̇⁰(ġ) − ṁ□(χ_KW**_H)), and χ_K = 0 where χ(t^♭_*) < 1. There N⁺ ∩ {t^♭_* < 3} lies in 𝒟′
([[sec:viii-0]]: T̂ + 7/4 ≥ 15/4, and N⁺ ⊂ N_ν = Ω_* ∪ 𝒟, [[lem:s29-g-on-n]]). On 𝒟′, Υ̇^♮(ġ) = 0 by
[[thm:viii-2-2]] (5), as S′ = S⁰′ = 0 in the class ([[cor:viii-2-3]]), so that ġ_(S′) = ġ⁰_(S⁰′) = 0; and the
argument of [[lem:gd-r2-10]] with χ^♮_0E_Υ in place of E_Υ gives Υ̇^♮ = Υ̇⁰ − χ^♮_0E^ΥG. So Υ̇⁰(ġ) = χ^♮_0E^ΥGġ
there. χ^♮_0 = 0 near Σ° ([[lem:iii-k-1-1]] (d)).

(iii) *Cone localisation.* supp χ′ ⊂ {t^♭_* ≥ T_K} ∩ {χ_K = 1}, so χ(t^♭_*) = 1 and F_Y = J_h there, and χ′Y is the
forward solution of □(χ′Y) = χ′J_h + [□, χ′]Y. The first term lies in the class of [[thm:gd-r2-5]] with α_sf + 2 = β, by
[[prop:gd-r3-2]] and [[lem:gd-r2-11]] (ι⁺-order ϰ_♯ + 1 − η > β + 5/2, K⁺-order above ½). The second is supported in supp
dχ′, a compact set together with the cone {T_1 ≤ t_*, t_*/40 ≤ r ≤ t_*/20} in (ι⁺)°; there Y ∈ H^(k,(b_I−2,α_+,−1))_b by
[[thm:ii-f1-1-1]] (ℵ = 1, sf-loss 0; its ℐ⁺-weight is b_I − 2 by [[eq:ii-f1-1-6]]), and
[□, χ′] = (□_0χ′) − 2∇_(∇χ′) ∈ ρ_+²Diff¹_b on the cone, χ′ being homogeneous of degree 0 for t_* ≥ 2T_1; so the second
term has sf-weight α_+ + 2 = β, the class of [[thm:gd-r2-5]] (b-regularity gives every 3b-order on the cone, as in the
proof of [[lem:gd-r2-11]]). [[thm:gd-r2-7]] gives |χ′Y − c(t_*)W*| ≤ Ct_*^(−1/2) with one more derivative,
c(t_*) := (4π²)⁻¹∫^(v_h(t_*))ℓ of the forcing term. For t_* ≥ max(2T_1, 40r_h), χ′ = 1 on compact r-sets near the horizon
and dχ′ = 0 there, so the integrand is ℓ(J_h) = ℓ(Υ̇⁰(h)), which is O(v^(−w+ε′)) ([[thm:gd-2-3]]); so c(t_*) → c_∞, with
c − c_∞ and dc/dt_* of order t_*^(−(w−1)+ε′) and t_*^(−w+ε′). *The conclusion.* On compact r-sets at late times, Y = χ′Y
and χ_K = 1, so ġ_H = ṁK_V + h + ṁℒ_(W**_H)g + ℒ_Yg = ṁK* + h + ℒ_Yg, and with ℒ_(cW*)g = cℒ_(W*)g + 2dc ⊗_s W*,

    ġ_H − ṁK* − c_∞ℒ_(W*)g = h + ℒ_(Y−cW*)g + (c − c_∞)ℒ_(W*)g + 2dc ⊗_s W*.

The first term is O(t_*^(−w+ε′)) ([[eq:gd-0-2]]), the second O(t_*^(−1/2)), and the last two O(t_*^(−(w−1)+ε′)); as
w − 1 > 1, the sum is O(t_*^(−1/2)), with the derivatives of [[eq:gd-r2-2]]. ∎

So the representative is in harmonic gauge everywhere but on a region bounded in t^♭_*, where it is [[thm:viii-2-2]]'s
own solution, in the generalised harmonic gauge Υ̇^♮ = 0. The next proposition reduces harmonic gauge on all of N⁺ to
one estimate on that region.

**Proposition {#prop:gd-r3-6}** (Harmonic gauge down to Σ°, given an order on the initial slab.) Let Z_1 be the
1-form on N⁺, smooth up to Σ°, with □Z_1 = F_Y on N⁺ and vanishing Cauchy data on Σ° ([[lem:ix-1-1]] on Ω^♯, with
F_Y extended across Σ° as in the proof of [[prop:gd-2-1]] (a); unique by [[lem:gd-r3-1]]). Suppose that for some
β ∈ (0, δ_♯) and p > ½ + β the Cartesian components of Z_1 and all their b-derivatives are O(ρ_I^p) near ℐ⁺ on
N⁺ ∩ {2 ≤ t^♭_* ≤ 3}. Then with Z := ṁχ_KW**_H + Z_1, ġ_H := ġ + ℒ_Zg is in harmonic gauge on all of N⁺, induces
(γ̇, k̇) exactly, and satisfies [[thm:gd-r3-4]] (iii) with Z_1 in place of Y.

*Proof.* □Z = ṁ□(χ_KW**_H) + F_Y = Υ̇⁰(ġ) on N⁺, so Υ̇⁰(ġ_H) = Υ̇⁰(ġ) − □Z = 0. Z_1 = 0 and ∇_nZ_1 = 0 on Σ°,
so ℒ_(Z_1)g induces zero data ([[lem:ix-2-1]] (f)), and χ_K = 0 near Σ°; so ġ_H induces the data of ġ. χ(t^♭_*)Z_1
and the forward solution of □u = χ(t^♭_*)F_Y + [□, χ(t^♭_*)]Z_1 on Ω_* are smooth, vanish on {t^♭_* < 2} and solve
the same equation; each {t^♭_* ≤ T} is closed under past causal curves (dt^♭_* is past timelike, [[sec:iii-k-0]]), so
they agree there for every T ([[lem:ii-f-1-3]]). The first term is that of [[lem:gd-r3-5]]. The second is supported
in {2 ≤ t^♭_* ≤ 3}, bounded in t_*, and meets ∂M only at ℐ⁺. Near ℐ⁺, t^♭_* = t_*(1 − (t_*/r)^(1/2))
([[lem:ii-c-3-2]] (a), with the exponent ½), smooth in x_I and equal to t_* at ℐ⁺. With dχ/ds the derivative of χ,
the commutator [□, χ(t^♭_*)] = (□_0χ(t^♭_*)) − 2(dχ/ds)(t^♭_*)∇_(∇t^♭_*) gains one order at ℐ⁺: in the coordinates
(t_*, r, ω) on a bounded t_*-range, g⁻¹ = ḡ⁻¹ + O(r⁻²) with ḡ⁻¹(dt_*, ·) = −∂_r ([[lem:iii-d-2-1]] (3) and its
proof), dt^♭_* = (1 − (3/2)(t_*/r)^(1/2))dt_* + O(r^(−3/2))dr, the connection coefficients in the Cartesian frame
are O(r⁻¹), and □_0t^♭_* = O(r⁻¹); so for Z_1 = O(ρ_I^p), whose r∂_r- and ∂_(t_*)-derivatives are O(ρ_I^p), the
commutator term is O(ρ_I^(p+1)) with its b-derivatives. Choosing b_I ∈ (b_+, min(p, 3/2)) in [[lem:gd-r3-5]], it lies
in the space there. So χ(t^♭_*)Z_1 is the forward solution of a forcing term in that space, and the proof of
[[thm:gd-r3-4]] (iii) applies to it; at late times χ(t^♭_*)Z_1 = Z_1. ∎

### The 1-form wave operator near spatial and null infinity {#sec:hg-exterior}

The hypothesis of [[prop:gd-r3-6]] concerns the region near I₀ ∪ ℐ⁺, where the exterior theory of
[[sec:iv-0]]–[[sec:iv-4]], [[sec:iv1-0]]–[[sec:iv2-4]] and [[sec:iv3-0]]–[[sec:iv3-2]] is written for the linearised
gauge-fixed Einstein operator. It carries over to □: in Cartesian components □ is the scalar wave operator on each
component plus a coupling that decays like |x|⁻³.

*Setting.* On {|x| ≥ 3R₁}, in the coordinates (t, x) of [[sec:iii-b-3]], g = η + m₀|x|⁻²𝔩 ⊗ 𝔩 with
𝔩 := dt − d|x| ([[lem:iii-b-3-5]] (b)), a Kerr–Schild metric with the η-null form 𝔩, so det g = −1. The chart of
[[sec:iv-0]] is used: ρ₀, ρ_I, ρ = ρ₀ρ_I = |x|⁻¹, x_I = ρ_I^(1/2), X₀ and X_I, with M_♯ and the edge-b structures there.
1-forms are written in the Cartesian frame dt, dx^i (i = 1, …, 4), the fixed smooth frame of the spaces of
[[ch:s05]]; the frames (dt, dr, r dω) and that of [[sec:iii-c-1]] differ from it by smooth bounded functions of x/|x|,
so the weighted b-spaces and the pointwise orders do not depend on the frame. □_0 is the scalar wave operator, and

    L_□ := ρ_Iρ^(−7/2) □ ρ^(3/2)     on Cartesian components,                                            {#eq:gd-r4-1}

the conjugation of [[eq:iv-2-1]] applied componentwise; L is the scalar operator of [[eq:iv-2-1]].

**Lemma {#lem:gd-r4-1}** (The operator and its indicial data.)

(a) For every 1-form Z, (□Z)_c = □_0Z_c + C_c^(νb)∂_bZ_ν + D_c^νZ_ν, with C and D stationary, C = Σ_(k≥1)m₀^kC_k
and D = Σ_(k≥1)m₀^kD_k finite sums, C_k and D_k homogeneous in x of degrees −1 − 2k and −2 − 2k (so O(|x|⁻³) and
O(|x|⁻⁴) with every derivative), and C_1 ≠ 0. There is no second-order coupling.

(b) L_□ = L ⊗ Id + E with E ∈ ρ₀²x_I⁴C^∞(M_♯)Diff¹_(e,b)(M_♯). So [[eq:iv-2-2]] holds for L_□ with
L̃_□ := L̃ ⊗ Id + E ∈ x_IDiff²_(e,b); [[eq:iv1-1-1]] holds for L_□ with Ā = 0 and without the terms of h; and the
commutators of L_□ with X₀, X_I and the rotation fields, acting on each Cartesian component, lie in
x_IDiff^(1;1)_(e,b;b) (as [[eq:iv-2-3]] for L).

(c) (*At ℐ⁺.*) For a, ι ∈ ℂ and every constant Cartesian covector ξ,
L_□(ρ₀^aρ_I^ι ξ) = −2ι(a − ι)ρ₀^aρ_I^ι ξ + o(ρ_I^(Re ι)) at fixed ρ₀ and ω. The indicial roots are ι = 0, a radiation
field (Z = ρ^(3/2)u of ℐ⁺-order 3/2 in every Cartesian component), and ι = a.

(d) (*At I₀.*) In (τ, ρ) := (t/|x|, |x|⁻¹), ρ^(−2−α)□_0(ρ^αv(τ)) → (1 − τ²)v″ + (1 − 2α)τv′ + α(2 − α)v as ρ → 0,
the coefficient of v″ not depending on α; the coupling of (a) is O(ρ²) relative to this and does not enter. So τ is a
b-time function on {|τ| < 1} for every weight: there is no indicial restriction at I₀.

(e) (*The multiplier.*) With Ā = 0, the identity [[eq:iv-3-3]] holds on each Cartesian component, and its coefficients
−4α_I, 4κ(α₀ − α_I) and c_A = 1 + 2(α₀ − α_I) + κ(1 − 2α_I) are positive for every κ > 0 if and only if
α_I < min(α₀, 0).

*Proof.* (a) As g − η = m₀H𝔩 ⊗ 𝔩 with H := |x|⁻² and 𝔩 η-null, g⁻¹ = η⁻¹ − m₀H𝔩^♯ ⊗ 𝔩^♯ exactly (𝔩^♯ := η⁻¹𝔩):
(η + m₀H𝔩 ⊗ 𝔩)(η⁻¹ − m₀H𝔩^♯ ⊗ 𝔩^♯) = I − m₀²H²η⁻¹(𝔩, 𝔩)𝔩 ⊗ 𝔩^♯ = I. The coefficients of 𝔩 are homogeneous of degree 0
in x and stationary, so ∂(H𝔩 ⊗ 𝔩) is homogeneous of degree −3, and the Christoffel symbols are Γ = m₀Γ_1 + m₀²Γ_2,
with Γ_1 = ½η⁻¹∂(H𝔩 ⊗ 𝔩)-terms of degree −3 and Γ_2 = −½H𝔩^♯ ⊗ 𝔩^♯ · ∂(H𝔩 ⊗ 𝔩)-terms of degree −5. On the Ricci-flat
g, □ = −∇^α∇_α; written out, −∇^α∇_αZ_c = −g^(ab)(∂_a∂_bZ_c − Γ^d_(ab)∂_dZ_c) + 2g^(ab)Γ^ν_(ac)∂_bZ_ν + (terms in ∂Γ
and ΓΓ)Z, and the first bracket is □_0Z_c. So C^(νb)_c = 2g^(ab)Γ^ν_(ac) and D is a sum of products g⁻¹∂Γ and
g⁻¹ΓΓ; expanding g⁻¹ = η⁻¹ − m₀H𝔩^♯ ⊗ 𝔩^♯ gives the stated sums and degrees, and no second-order term other than
□_0's. C_1 = 2η^(ab)(Γ_1)^ν_(ac): its component with ν = b = t and c the index of x^1 is −2(Γ_1)^t_(t1), and
(Γ_1)^t_(t1) = ½η^(tt)∂_1(H𝔩_t𝔩_t) = −½∂_1H (𝔩_t = 1, ∂_tH = 0), so the component is ∂_1H = −2x^1|x|⁻⁴ ≠ 0.

(b) By [[lem:iv1-1-1]], ∂_t, ∂_(x^i) ∈ ρ₀𝒱_(e,b) and |x|⁻¹∂_ω ∈ ρ₀x_I𝒱_(e,b). A coefficient homogeneous of degree −d in
x is ρ^d times a smooth function of x/|x|, and ρ = ρ₀x_I². The prefactor is ρ_Iρ^(−2) = ρ₀^(−2)x_I^(−2), and the
conjugation adds (3/2)∂_b log ρ, of degree −1. So C∂(ρ^(3/2)u) contributes ρ₀^(−2)x_I^(−2) · ρ₀³x_I⁶ · ρ₀𝒱_(e,b) ⊂
ρ₀²x_I⁴Diff¹_(e,b) and ρ₀^(−2)x_I^(−2) · ρ₀³x_I⁶ · ρ₀x_I² ⊂ ρ₀²x_I⁶C^∞; D contributes ρ₀²x_I⁶C^∞; the higher powers of
m₀ more decay. L ⊗ Id is the conjugated □_0 on each component ([[eq:iv-2-1]]). As 𝒱_(e,b) is a Lie algebra and
differentiation along it preserves ρ₀^(ℓ₀)x_I^(ℓ_I)C^∞ ([[rem:iv-1-3]]), [E, X] ∈ ρ₀²x_I⁴Diff¹_(e,b) for
X ∈ {X₀, X_I, rotations}, and with [[eq:iv-2-3]] for L this gives the commutators. The other claims are restatements:
E ∈ x_IDiff²_(e,b), and its first-order part replaces the matrix Ā of [[eq:iv1-1-1]] by 0.

(c) By [[eq:iv-2-2]], L = −2X_I(X₀ − X_I) + x_I²(Δ̸ + ¾) + L̃ with L̃ ∈ x_IDiff²_(e,b). As X₀ρ₀^a = aρ₀^a and
X_Iρ_I^ι = ιρ_I^ι, −2X_I(X₀ − X_I)(ρ₀^aρ_I^ι) = −2ι(a − ι)ρ₀^aρ_I^ι; the other terms of L, and E by (b), are
O(x_I|ρ_I^ι|) = o(ρ_I^(Re ι)). The roots of −2ι(a − ι) are 0 and a, and Z = ρ^(3/2)u with u of ℐ⁺-order 0 has order 3/2.

(d) For η, □_0 = ∂_t² − ∂_r² − 3r⁻¹∂_r − r⁻²Δ̂ on functions. With ρ = 1/r and τ = t/r, ∂_tρ = 0, ∂_tτ = ρ, ∂_rρ = −ρ²
and ∂_rτ = −τρ; so for u = ρ^αv(τ), ∂_t²u = ρ^(α+2)v″, ∂_ru = −ρ^(α+1)(αv + τv′) and
∂_r²u = ρ^(α+2)((α + 1)(αv + τv′) + (α + 1)τv′ + τ²v″). Hence □_0u = ρ^(α+2)((1 − τ²)v″ + (1 − 2α)τv′ + α(2 − α)v)
exactly for η. For g, g⁻¹ − η⁻¹ = O(ρ²) and Γ = O(ρ³) with all derivatives, and the derivatives of u of order one and
two are O(ρ^(α+1)) and O(ρ^(α+2)); so the corrections, and the coupling terms C∂Z = O(ρ³ · ρ^(α+1)) and
DZ = O(ρ⁴ · ρ^α), are O(ρ^(α+4)), two orders below.

(e) [[eq:iv-3-3]] is an identity for the leading part L₀ = −2X_I(X₀ − X_I) + ρ_I(Δ̸ + ¾) of [[eq:iv-2-2]], which acts
on each Cartesian component of L_□ by (b). Its coefficients are 4|α_I| (written for α_I < 0), 4κ(α₀ − α_I) and c_A. If
α_I < min(α₀, 0), then −4α_I > 0, 4κ(α₀ − α_I) > 0 and c_A > 1 + κ > 0; conversely positivity of the first two for
some κ > 0 needs α_I < 0 and α₀ > α_I. ∎

**Proposition {#prop:gd-r4-2}** (The exterior estimate for □.) Let 𝒟, Ω_(ext,r_1), 𝒦, 𝒮,
Ω^♮ := Ω_(ext,r_1) ∪ 𝒮, ρ′₀ and ρ′_I be those of [[sec:iii-k-0]], the proof of [[prop:iii-k-1-2]] and
[[sec:iv3-0]]–[[sec:iv3-2]], at S = 0, and 𝒟⁺ := 𝒟 ∩ {t_IVP ≥ 0}, 𝒦⁺ := 𝒦 ∩ {t_IVP ≥ 0} those of
[[lem:s27-cover]] (e); put τ′ := t_IVP/|x|. Let a₀ ∈ ℝ, α_I < min(a₀, 0) and m ∈ ℕ_0; let c_1 ∈ (0, c_♮], with c_♮
the constant fixed in [[sec:iv3-1]], be so small that 2 of the proof holds on {ρ′_I < c_1} for these weights, and put
Ω^♮_(c_1) := Ω^♮ ∩ {ρ′_I < c_1}. Let F be a smooth 1-form on 𝒟⁺ with
f_♭ := ρ_Iρ^(−7/2)F ∈ H^(m+4,(a₀,2α_I))_b over Ω^♮ near infinity (in the translated chart over 𝒮) and
F ∈ H^(m+4)(𝒦⁺). Then the solution Z of □Z = F on 𝒟⁺ with vanishing Cauchy data on Σ^IVP lies in H^(m+1)(𝒦⁺), and
u := ρ^(−3/2)Z satisfies

    ‖u‖_(H^(m+1,a₀)_b(Ω^♮∩{ρ′_I>c_1/2})) + ‖u‖_(H^((1;m),(a₀,2α_I))_(e,b;b)(Ω^♮_(c_1)))
        ≤ C(‖f_♭‖_(H^(m+4,(a₀,2α_I))_b) + ‖F‖_(H^(m+4)(𝒦⁺))).                                        {#eq:gd-r4-2}

(The loss of four derivatives is the d of [[thm:iv2-2-4]]. Compactly supported F is allowed.)

*Proof.* We follow [[prop:iv-3-1]], [[prop:iv-4-1]], [[prop:iv1-2-2]], [[lem:iv2-2-2]], [[lem:iv2-2-3]],
[[thm:iv2-2-4]] and [[thm:iv3-2-1]] with L_□ in place of the linearised operator; what each takes from it holds for
□ as follows.

1. *The operator.* Every use of the form [[eq:iv1-1-1]] is met by [[lem:gd-r4-1]] (b) with Ā = 0, the coefficients ã_i
   of [[eq:iv2-0-4]] equal to 0, and so with no tame terms. The rotations act on each Cartesian component as
   derivations, and no equivariance is needed for them to act on the components.
2. *Near ℐ⁺: [[prop:iv1-2-2]] at □.* The multiplier is W = w²V, V = X₀ − (1 + κ)X_I, with the Euclidean fibre inner
   product on Cartesian components ([[lem:iv1-2-1]] is not needed, Ā = 0 being diagonal). Write
   2 Re⟨wL_□u, wVu⟩ = 2 Re⟨w(L ⊗ Id)u, wVu⟩ + 2 Re⟨wEu, wVu⟩. The first term is the identity of the proof of
   [[prop:iv-3-1]] in each component: ⟨Qu, u⟩ + ℬ_fin with ℬ_fin ≥ 0 (the energy current of □_0 ⊗ Id is the sum of the
   components' currents) and ⟨Qu, u⟩ ≥ c_0‖wu‖²_(H¹_(e,b)) − Cc‖wu‖²_(H¹_(e,b)) on {x_I < c}, with c_0 > 0 by
   [[lem:gd-r4-1]] (e) and independent of c, after the Poincaré inequality of that proof in each component. The second
   term is at most Cc²‖wu‖²_(H¹_(e,b)) on {x_I < c}, as E carries ρ₀²x_I⁴ with ρ₀ ≤ 1 and V ∈ 𝒱_(e,b); it is absorbed
   for c small, as Q − Q̄ is there. Higher b-regularity follows by the same induction, with the commutators of
   [[lem:gd-r4-1]] (b).
3. *Near the interior of I₀: [[prop:iv-4-1]] and [[lem:iv2-2-2]] at □.* There ρ_I ≥ δ, the eb- and b-structures agree,
   L_□ ∈ Diff²_b with principal symbol ρ_IG_b ⊗ Id up to O(ρ), and E ∈ ρ₀²Diff¹_b is a bounded first-order b-operator,
   absorbed by the exponential weight in τ (or τ′) as the first-order terms of the system are absorbed there; τ′ is a
   b-time function for every weight ([[lem:gd-r4-1]] (d)). [[lem:iv2-2-2]] at □, with zero data and the forcing term F
   (which it does not ask to vanish near Σ^IVP), gives Z on the region of [[lem:iv2-2-2]].
4. *The gluing: Steps 1–3 of the proof of [[thm:iv2-2-4]] and [[lem:iv2-2-3]] at □*, with 2 and 3: the cut-off
   χ̂_N(τ′) of Step 2, whose commutator lives where ρ_I ≥ ½, so that every ℐ⁺-weight is met there; then
   [[lem:iv2-2-3]], away from ℐ⁺ by 3, and near ℐ⁺ the forward problem for u − χ_cu_1, the first-order b-commutator
   [L_□, χ_c] being supported in {c/4 ≤ ρ_I ≤ c/2}, by 2.
5. *The slab: [[thm:iv3-2-1]] at □.* Of its three changes, the gauge cut-off is absent for □; the background is g
   itself (S = 0), for which [[lem:iv3-0-1]] is the form of g − η of [[lem:iii-c-3-5]], and [[lem:gd-r4-1]] holds in the
   translated chart, g being stationary; and the regions, whose curves ([[lem:iv3-1-1]]) are statements about g, t^♭_*,
   t_IVP and ρ′_I alone, are unchanged. The compact parts (𝒦, and 𝒮 ∩ {ρ′_I ≥ c_1/4}) use the energy estimates for a
   linear wave equation with principal symbol g⁻¹(ζ, ζ) Id ([[lem:ix-2-1]] (a)) on compact domains of dependence; on
   Ω^♮_(c_1), 2 applies with Σ_in = {ρ′_I = c_1} and Σ_fin = {t^♭_* = T̂ + 3}, spacelike for g. Uniqueness on each
   region is [[lem:ii-f-1-3]].
6. *What is not used.* The recovery of the sharp weight at ℐ⁺, Steps 4–6 of the proof of [[thm:iv2-2-4]], integrates
   each slot along X_I and X₀ − X_I; with Ā = 0 every Cartesian component would be integrated as slot 6 is there. Only
   the estimate [[eq:gd-r4-2]] is needed below. ∎

**Theorem {#thm:gd-r4-3}** (The order of the gauge vector on the initial slab.) Let q_ḣ := min(min Re ℰ_0, ℓ_0), so
that q_ḣ > 3/2 + 2γ_Υ (min Re ℰ_0 > 3/2 + 2γ_Υ and ℓ_0 > 3, [[sec:iii-k-0]]). For every β ∈ (0, δ_♯) and every p with

    ½ + β < p < min(3/2, q_ḣ − 1),

the Cartesian components of Z_1 of [[prop:gd-r3-6]] and all their b-derivatives are O(ρ_I^p) near ℐ⁺ on
N⁺ ∩ {2 ≤ t^♭_* ≤ 3}, with constants bounded by finitely many norms of the data. The interval is not empty:
q_ḣ − 1 > ½ + 2γ_Υ ≥ ½ + 2δ_♯. With the weight ℓ^♭_0 = 3/2 + ½δ_♯ of [[thm:iii-c1-3-1]] in place of q_ḣ the same holds
for β ∈ (0, ½δ_♯).

*Proof.* (1) *The forcing term on the past of the slab.* In the class S′ = S⁰′ = 0 ([[cor:viii-2-3]]), so
ġ_(S′) = ġ⁰_(S⁰′) = 0, ġ = ḣ on 𝒟′ ([[thm:viii-2-2]] (2)) and Υ̇^♮(ġ) = 0 there ([[thm:viii-2-2]] (5)). As
Υ̇^♮ = Υ̇⁰ − χ^♮_0E^ΥG (the proof of [[thm:gd-r3-4]] (ii)) and χ_K = 0 on {t^♭_* < T_K} with
T_K = max(10, T_ι + 2) ≥ T̂ + 4 ([[sec:iii-k-0]]), F_Y = χ^♮_0E^ΥGḣ on N⁺ ∩ {t^♭_* < T̂ + 7/4}, which contains
{t^♭_* ≤ 7/2} as T̂ ≥ 2. Let χ_3 ∈ C^∞(ℝ) equal 1 on (−∞, 3] and 0 on [7/2, ∞), and F_3 := χ_3(t^♭_*)F_Y, a smooth
1-form on 𝒟⁺. As dt^♭_* is past timelike ([[sec:iii-k-0]]), N⁺ ∩ {t^♭_* ≤ 3} is closed under past causal curves in
N⁺; so the solution Z_3 of □Z_3 = F_3 on 𝒟⁺ with vanishing data equals Z_1 there ([[lem:ii-f-1-3]]; the extension
across Σ° is immaterial by [[lem:gd-r3-1]]).

(2) *Support.* Near infinity on {τ′ < ⅛}, t_IVP < r/8 and t_* = t_IVP − F_s(r) ≤ r/8 − r/4 < 0 for r ≥ R_6, where
F_s(r) := t_IVP − t_* is the function of [[eq:s27-f]], so χ_♮(t_*) = 0, and χ_0 = 0 as χ̌_0(t_IVP/r) = 1; so χ^♮_0 = 0
([[eq:iii-k-1-1]]). And χ^♮_0 = 0 near Σ^IVP ([[lem:iii-k-1-1]] (d)). So F_3 vanishes near Σ^IVP and, near infinity, on
{τ′ < ⅛}. [[prop:gd-r4-2]] does not ask this, but it places the I₀-tail of F_3 in {τ′ ≥ ⅛}, the region of
[[lem:iv2-2-3]].

(3) *Weights.* On Ω_(ext,r_1) and 𝒮, ḣ ∈ H^(∞,(ℰ_0,ℓ_0),⟨ℰ^C_I⟩,ℓ_I)_b ([[prop:viii-1-2]] (2) and its proof): conormal
with order q_ḣ − η at I₀ for every η > 0 and, at ℐ⁺, with the exponents of [[eq:iii-c-3-2]] slot by slot, above ℓ^♭_I
in every slot but π̸₀, which has 3/2. E^Υ_(g,∞) is |x|⁻¹ times coefficients smooth on M ([[def:iii-b-6-1]]) and does not
see π̸₀ (the proof of [[lem:gd-r3-5]]); χ^♮_0 and χ_3(t^♭_*) are smooth on M near infinity ([[lem:iii-k-1-1]] (a);
t^♭_* is smooth near ℐ⁺, [[sec:iii-k-0]]). So F_3 has I₀-order q_ḣ + 1 − η and ℐ⁺-order ℓ^♭_I + 1, and
f_♭ := ρ_Iρ^(−7/2)F_3 ∈ H^(m,(a₀,2α_I))_b for every m, every a₀ < q_ḣ − 5/2 and every α_I < ℓ^♭_I − 3/2, as
ρ_Iρ^(−7/2) = ρ₀^(−7/2)ρ_I^(−5/2) ([[eq:iv2-0-2]]).

(4) *The estimate.* Fix a₀ < q_ḣ − 5/2 with p − 3/2 < a₀, and put α_I := p − 3/2; then α_I < min(a₀, 0) and
α_I < ℓ^♭_I − 3/2 (p < 3/2 < ℓ^♭_I), and [[prop:gd-r4-2]] gives u = ρ^(−3/2)Z_3 ∈ H^((1;m),(a₀,2α_I))_(e,b;b)(Ω^♮_(c_1))
for every m. By b-Sobolev embedding ([[eq:iv-0-1]]), V^ju = O(ρ₀^(a₀)ρ_I^(α_I)) for b-vector fields V and j ≤ m − 3; as
Vρ^(3/2) ∈ ℂρ^(3/2) for V ∈ {X₀, X_I, rotations}, V^jZ_3 = O(ρ₀^(3/2+a₀)ρ_I^p). On the slab ρ₀ is bounded above and below
([[sec:iv3-0]]), and away from ℐ⁺ there is nothing to show. The three conditions are: α_I > β − 1, that is p > ½ + β;
α_I < a₀, possible for some a₀ < q_ḣ − 5/2 exactly when p < q_ḣ − 1; and α_I < 0, that is p < 3/2. ∎

**Remark {#rem:gd-r4-bounds}** (Where the two bounds on p come from.) This remark is a heuristic about the method,
and no proof uses it. The bound p < 3/2 is the condition α_I < 0 of the multiplier ([[lem:gd-r4-1]] (e)), whose
threshold α_I = 0 is the indicial root ι = 0 of [[lem:gd-r4-1]] (c), the radiation field, of ℐ⁺-order exactly 3/2;
it is not shown here whether Z_1 attains that order, the recovery of the sharp ℐ⁺-weight not being carried out for
□ (item 6 of the proof of [[prop:gd-r4-2]]). The bound p < q_ḣ − 1 is the condition α_I < a₀ of [[prop:gd-r4-2]],
which the multiplier needs at the corner I₀ ∩ ℐ⁺ ([[lem:gd-r4-1]] (e)); it ties the ℐ⁺-order to the I₀-order of the
forcing term, which is one above that of ḣ through the factor |x|⁻¹ of c_Υ (step (3) of the proof of
[[thm:gd-r4-3]]). Without that factor the same argument would give only p < q_ḣ − 2, which leaves no p > ½ + β when
q_ḣ ≤ 5/2 + β.

**Corollary {#cor:gd-r4-6}** (Homogeneous solutions with data of compact support on Σ°.) Let Y be a 1-form on N⁺,
smooth up to Σ°, with □Y = 0, whose Cauchy data on Σ° have compact support. Then Q[Y] is constant, and on each
{r_♭ < r ≤ R′, t_* ≥ T′}, |Y − (Q[Y]/4π²)W*| ≤ Ct_*^(−1/2) with the derivatives of [[eq:gd-r2-2]]. Near ℐ⁺ on
N⁺ ∩ {t^♭_* ≤ T̂ + 3} the Cartesian components of Y and all their b-derivatives are O(ρ_I^p) for every p < 3/2.

*Proof.* Q[Y] is constant by [[eq:gd-2-1]]. (1) *ℐ⁺.* Let Y_c be a smooth 1-form on N⁺ of compact support with Y's Cauchy
data on Σ°. Then Y − Y_c has vanishing data and □(Y − Y_c) = −□Y_c, which has compact support; so ρ_Iρ^(−7/2)□Y_c lies in
every weighted space, and [[prop:gd-r4-2]] applies with every a₀. With a₀ > 0 and α_I = p − 3/2 < 0, the b-Sobolev
embedding of step (4) of the proof of [[thm:gd-r4-3]] gives the order p; Y_c vanishes near infinity. (2) *The slab.* With
χ of [[lem:gd-r3-5]], χ(t^♭_*)Y solves □(χ(t^♭_*)Y) = [□, χ(t^♭_*)]Y, supported in {2 ≤ t^♭_* ≤ 3} and meeting ∂M only at
ℐ⁺, of ℐ⁺-order p + 1 (the proof of [[prop:gd-r3-6]]). Fix β ∈ (0, 1) and p ∈ (½ + β, 3/2), and put b_+ := β + ½ and
b_I ∈ (b_+, p). This forcing term lies in H^(∞,(b_I+1,b_++2,1/2))_b(Ω_*, μ_b)^(•,−), the space of [[eq:ii-f1-1-4]] in the
form of [[cor:ii-f1-1-2]], whose conditions b_I < 3/2 + S̄ and b_+ < b_I hold for □ (S̄ = 0, [[lem:iii-d-3-1]] at
γ_Υ = 0); □ is 1-admissible with sf-weight b_+ − 5/2 = β − 2 ([[thm:gd-r2-5]] (iii), as β ∈ (0, 1)), and
[[thm:ii-f1-1-1]] gives its forward solution, which is χ(t^♭_*)Y by the uniqueness argument of the proof of
[[prop:gd-r3-6]]. (3) *Late times.* As in the proof of [[thm:gd-r3-4]] (iii): χ′Y solves □(χ′Y) = [□, χ′]Y, a forcing
term supported in supp dχ′ and in the class of [[thm:gd-r2-5]]; [[thm:gd-r2-7]] gives |χ′Y − c(t_*)W*| ≤ Ct_*^(−1/2), and
for large t_*, dχ′ = 0 near the horizon, so c is constant there, equal to Q[χ′Y]/4π² = Q[Y]/4π²
([[eq:gd-2-1]] and □Y = 0). ∎

The data must be taken on Σ°: a slice {t_* = t_0} reaches ℐ⁺, outgoing null rays from a compact set reach ℐ⁺ after a
bounded increment of t_*, and in 4 + 1 dimensions there is no Huygens principle, so a solution with data of compact
support on such a slice does not vanish near ℐ⁺ on later slices. Step (1) supplies the estimate at ℐ⁺ that the slab
needs.

**Corollary {#cor:gd-r4-4}** (The harmonic gauge on all of N⁺.) With Z_1 of [[prop:gd-r3-6]], Z := ṁχ_KW**_H + Z_1 and
ġ_H := ġ + ℒ_Zg on N⁺: ġ_H is G-invariant, DRic(ġ_H) = 0, Υ̇⁰(ġ_H) = 0 on all of N⁺, ġ_H = ġ on a neighbourhood of Σ°
(so ġ_H induces (γ̇, k̇) exactly), and on each {r_♭ < r ≤ R′, t_* ≥ T′}, with the derivatives of [[eq:gd-r2-2]],

    |ġ_H − ṁK* − c_∞ℒ_(W*)g| ≤ Ct_*^(−1/2),        c_∞ := (4π²)⁻¹ ∫ ℓ(χ′J_h + [□, χ′]Z_1) dv,

the limit of a horizon charge. For a 1-form Y_h on N⁺, smooth up to Σ°, with □Y_h = 0 and Cauchy data of compact
support on Σ°, ġ_H + ℒ_(Y_h)g has the properties above with three changes: c_∞ + Q[Y_h]/4π² replaces c_∞; where
ġ_H equals ġ it equals ġ + ℒ_(Y_h)g, so it induces (γ̇, k̇) plus the data of ℒ_(Y_h)g; and it is G-invariant when Y_h
is. With the same three changes, (i)–(iii) of [[thm:gd-r3-4]] hold for that theorem's representative plus ℒ_(Y_h)g.

*Proof.* [[prop:gd-r3-6]], whose hypothesis is [[thm:gd-r4-3]]. Z_1 is G-invariant by the argument of
[[prop:gd-2-1]] (a). *Near Σ°.* χ_K = 0 there, and F_Y = χ^♮_0E^ΥGḣ (step (1) of the proof of [[thm:gd-r4-3]])
vanishes on V ∩ N⁺ for a neighbourhood V of Σ° in U^♯ ([[lem:iii-k-1-1]] (d)); so Z_1, with vanishing data, vanishes
on D_V(Σ°) ∩ {t_IVP ≥ 0} by the argument of [[lem:gd-r3-1]] on D_V(Σ°) ([[lem:ix-1-2]]). The clause on Y_h is
[[cor:gd-r4-6]], ℒ_(Y_h)g being linear in Y_h, and DRic(ℒ_(Y_h)g) = 0, Υ̇⁰(ℒ_(Y_h)g) = −□Y_h = 0; ℒ_(Y_h)g is
G-invariant when Y_h is. ∎

So every perturbation in the class has a representative in harmonic gauge on all of N⁺ that induces the given data
exactly, and its settling on compact sets is determined up to the constant c_∞: the explicit ṁK*, growing linearly
in v, plus the stationary c_∞ℒ_(W*)g, plus a decaying remainder.

### The spherically symmetric sector {#sec:hg-l0}

**Proposition {#prop:gd-r2-13}** (The spherically symmetric sector in harmonic gauge.) Let ġ_H be a harmonic-gauge
solution of [[prop:gd-2-1]] (a), with gauge vector Z′.

(a) (*Exact form.*) (ġ_H)_0 = ṁK* + ℒ_(Z′_0)g, where Z′_0 is the l = 0 part of Z′, □Z′_0 = 0, and K* is the mass
change of [[prop:np-10-2]] (iv) (c): smooth across the horizon, Υ̇⁰(K*) = 0, δm[K*] = 1, and K* − (v/2)ℒ_(W*)g
stationary. The choice Z′_0 = 0 is allowed, and then (ġ_H)_0 = ṁK* identically.

(b) (*Decaying gauge data.*) If Z′_0 has Cauchy data of compact support on Σ°, then on each
{r_♭ < r ≤ R′, t_* ≥ T′}, with the derivatives of [[eq:gd-r2-2]],

    (ġ_H)_0 = ṁK* + cℒ_(W*)g + O(t_*^(−1/2)),        c = Q[Z′_0]/4π².

When ṁ ≠ 0 this grows linearly in v, and it is not the sum of a stationary tensor smooth at r_h and a term o(1).

(c) (*Non-decaying gauge data.*) Let F be as in [[lem:gd-r2-9]], ψ = v + F, and

    Ξ := ψ² + K_Ξ(r),        K_Ξ′ := (r⁴/2 + r²r_h² − (3/2)r_h⁴ + 2r_h⁴ log(r/r_h))/(r(r² − r_h²)).

Then □_0Ξ = 0, dΞ is smooth across r_h, and S := K* − (4m₀)⁻¹ℒ_(dΞ)g is stationary, smooth across the horizon, with
Υ̇⁰(S) = 0 and δm[S] = 1; but S_vv → −1/m₀ as r → ∞. So ṁS is the l = 0 part of a harmonic-gauge solution, with
Z′_0 = −(ṁ/(4m₀))dΞ: stationary near the horizon, not decaying at infinity, and with a gauge vector that grows in v and
in r. The growth of the horizon charge ([[thm:gd-2-3]]) is then carried by (ṁ/(2m₀))v(∂_v)^♭, a linearly growing time
translation, whose Lie derivative is stationary.

*Proof.* (a) (ġ_RW)_0 = ṁK_V ([[thm:rw-settling]] (a)), W**_H is spherically symmetric, and □Z′_0 = 0 by
[[prop:gd-2-1]] (c); ṁK_V + ṁℒ_(W**_H)g = ṁK* by [[prop:np-10-2]] (iv) (c), which gives the properties of K*.

(b) Z′_0 is smooth up to Σ°, with □Z′_0 = 0, so [[cor:gd-r4-6]] applies; ℒ_(Z′_0)g − cℒ_(W*)g = ℒ_(Z′_0−cW*)g is
bounded by the derivatives of Z′_0 − cW*. By [[eq:np-10-2-k]], ṁK* = (ṁv/2)ℒ_(W*)g + (stationary), with
ℒ_(W*)g ≠ 0.

(c) By [[lem:gd-r2-9]], dψ = m₀W* − (∂_v)^♭ and □_0ψ = 0. So □_0(ψ²) = 2ψ□_0ψ − 2g⁻¹(dψ, dψ) = −2g⁻¹(dψ, dψ), and,
with dψ = dv + F′dr and P := −F′ = (r² + rr_h + r_h²)/(r(r + r_h)), for which fP = (r³ − r_h³)/r³,

    g⁻¹(dψ, dψ) = 2F′ + fF′² = P(fP − 2) = −P(r³ + r_h³)/r³ = −(r⁴ + r²r_h² + r_h⁴)/r⁴.

For a function of r, □_0K_Ξ = −r⁻³(r³fK_Ξ′)′, and r³fK_Ξ′ = r⁴/2 + r²r_h² − (3/2)r_h⁴ + 2r_h⁴ log(r/r_h), whose
derivative is 2(r⁴ + r²r_h² + r_h⁴)/r. So □_0Ξ = 2(r⁴ + r²r_h² + r_h⁴)/r⁴ − 2(r⁴ + r²r_h² + r_h⁴)/r⁴ = 0.
dΞ = 2ψdψ + K_Ξ′dr: ψ and dψ are smooth on {r > 0}, and the numerator of K_Ξ′ vanishes at r = r_h
(r_h⁴/2 + r_h⁴ − (3/2)r_h⁴ = 0), so K_Ξ′ is analytic on {r > 0}. *Stationarity.* ℒ_(dΞ)g = 2∇dΞ =
4dψ ⊗ dψ + 4ψ∇dψ + 2∇(K_Ξ′dr), and ∇dψ = ½ℒ_(dψ)g = ½m₀ℒ_(W*)g, (∂_v)^♭ being Killing. So

    (4m₀)⁻¹ℒ_(dΞ)g = m₀⁻¹dψ ⊗ dψ + ((v + F)/2)ℒ_(W*)g + (2m₀)⁻¹∇(K_Ξ′dr),

and by [[eq:np-10-2-k]] the terms (v/2)ℒ_(W*)g cancel in S, which is therefore stationary and smooth across the horizon.
Υ̇⁰(S) = Υ̇⁰(K*) + (4m₀)⁻¹□dΞ = (4m₀)⁻¹d□_0Ξ = 0, as □ = dδ + δd commutes with d. δm[ℒ_(dΞ)g] = 0, dΞ being spherically
symmetric ([[lem:gd-1-4]] (a)), so δm[S] = 1. *S_vv.* For Y = a dv + b dr, (ℒ_Yg)_vv = 2∂_va − f′a − ff′b (the
symbols Γ^v_(vv) = f′/2 and Γ^r_(vv) = ff′/2). The v-dependent terms of S_vv cancel, S being stationary. As r → ∞,
f′ = 2m₀r⁻³, rA → ½, rB → −¼, F = −r + O(1), 1 + fF′ = r_h³r⁻³ and K_Ξ′ = r/2 + O(r⁻¹); so the stationary part of
(ℒ_(W**)g)_vv is r⁻² + O(r⁻⁴), that of (ℒ_(dΞ)g)_vv = 4 − 2f′ψ(1 + fF′) − ff′K_Ξ′ is 4 + O(r⁻²), and
S_vv = K̄_vv + (ℒ_(W**)g)_vv − (4m₀)⁻¹(ℒ_(dΞ)g)_vv = −1/m₀ + O(r⁻²). *The gauge vector.* By [[prop:gd-2-1]] (a), a
harmonic-gauge solution with Z′_0 = −(ṁ/(4m₀))dΞ exists, and its l = 0 part is ṁK* − (ṁ/(4m₀))ℒ_(dΞ)g = ṁS. The
growing part of −(ṁ/(4m₀))dΞ = −(ṁ/(2m₀))ψdψ − (ṁ/(4m₀))K_Ξ′dr is −(ṁ/2)vW* + (ṁ/(2m₀))v(∂_v)^♭. The first
cancels the growing part (ṁ/2)vW* of ṁW**; Q[dΞ] = 0, as δdΞ = □_0Ξ = 0 and d dΞ = 0; and by the argument in the
proof of [[thm:gd-2-3]], Q[(ṁ/(2m₀))v(∂_v)^♭] = 2π²ṁv, while ℒ_(v(∂_v)^♭)g = 2dv ⊗_s (∂_v)^♭ is stationary. ∎

So the growth of the spherically symmetric part is forced for perturbations whose gauge vector has decaying data, and
only for them; a statement of the final state in harmonic gauge carries that class.

### The forward solution at positive K⁺-weight {#sec:hg-positive}

The rate t_*^(−1/2) of [[thm:gd-r2-7]] is what square integrability in time gives. For forcing terms with more decay
at K⁺ the forward solution of □ improves, by the argument of [[prop:iii-i2-5-1]], which is shorter at □: □ is its own
stationary model, it has one zero-energy state W* ∈ 𝒜² with no generalised partner, and the forcing terms below have
ℐ⁺-weight at least 5/2.

*Setting.* X = {r ≥ r_♭}, and M′, its faces I, ι = ι⁺ ∪ ι⁻ and K = K⁺ ∪ K⁻, the spaces H^(k,(w_I,w_ι,w_K))_b(M′) for the
b-density |dt_*/⟨t_*⟩|μ_b, μ_b = |dx|/⟨x⟩⁴, which on Ω_* are those of [[cor:ii-f1-1-2]], and X^±_(sc-b) with its faces
scf, tf, zf, are those of [[sec:iii-i2-1]]. P̂ and P̃ are those of [[sec:hg-augmented]].

*The dictionary.* Near ι⁺ ∩ K⁺, with ρ_+ = 1/r and ρ_K = r/t_*, one has t_* = 1/(ρ_+ρ_K) and r = 1/ρ_+, so the
density |dt_* dx| = ρ_+^(−5)ρ_K^(−1)|(dρ_+/ρ_+)(dρ_K/ρ_K)dω| and L²(|dt_* dx|) = ρ_+^(5/2)ρ_K^(1/2)L²_b. So a 3b-weight
(β_sf, β_K) of [[sec:iii-h1-1]] is the b-weight (β_sf + 5/2, β_K + ½), as [[cor:ii-f1-1-2]] records. The forcing class
H^((𝗌;k),(α_sf+2,0))_(3b;b) of [[thm:gd-r2-5]] is the b-class (γ_+ + 2, ½) with γ_+ := α_sf + 5/2, its window
α_sf + 2 ∈ (0, 1) is γ_+ − ½ ∈ (0, 1), and the K⁺-weight −1 of its solution is the b-weight −½. A conormal function
O(ρ_+^Aρ_K^B) lies in ρ_+^(w_ι)ρ_K^(w_K)L²_b near the corner if A > w_ι and B > w_K, and b-Sobolev embedding returns to
pointwise bounds; on compact r-sets ρ_K is comparable to t_*⁻¹, so the b-weight α_K at K⁺ is the rate t_*^(−α_K).

*The window.* On Cartesian components P̂(0) is −Δ up to ρ²-relative terms ([[lem:gd-r4-1]] (a)), with indicial roots
−l and l + 2 on r^(−q)Y_l (l the degree of the spherical harmonic Y_l); a weight α of [[sec:iii-h-1]] is the
μ_b-weight α + 2, and the root-free interval around it is (0, 2), the gap of [[sec:hg-augmented]]. The column f̂_*(0)
∈ 𝒜³ lies in 𝒴_0, of μ_b-weight α + 4, if and only if α + 2 < 1. So the window at □ is α + 2 ∈ (0, 1). At ℐ⁺ the
outgoing root is 3/2 ([[lem:gd-r4-1]] (c)), the cap 3/2 + S̄ of [[cor:ii-g1-4-5]] with S̄ = 0.

**Theorem {#thm:gd-r5-1}** ([[thm:gd-r2-5]] at positive K⁺-weight.) Let α_K ∈ [½, 1), γ_+ ∈ (α_K, 3/2),
w_I ≥ max(5/2, γ_+ + 2 − α_K) and

    f ∈ H^(∞,(w_I,γ_++2,α_K))_b(Ω_*; T*)^(•,−),                                                          {#eq:gd-r5-1}

and let u be the forward solution of □u = f ([[thm:ii-f1-1-1]] at P = P_0 = □). Then γ_+ − α_K ∈ (0, 1), and for every
ϵ ∈ (0, (3/2 − γ_+)/5]:

(i) u = u′ + u_sing with u′ ∈ H^(∞,(γ_+−ϵ,γ_+,α_K))_b(M′);

(ii) u_sing = β(t_*, r)W*, where for one B ∈ H^(∞,α_K)_b(ℝ) ([[def:ii-g1-2-1]]: ⟨t⟩^(α_K−½)∂_t^p(t∂_t)^qB ∈ L²(dt)),
∂_(t_*)β(·, r) = (∂_tχ^H_K)(·, r) ∗ B and β(·, r) − β(·, r′) = (χ^H_K(·, r) − χ^H_K(·, r′)) ∗ B;

(iii) u_sing, and so u, lies in H^(∞,(γ_+−ϵ,γ_+−ϵ,α_K−1))_b: one order is lost at K⁺ and none at ι⁺.

At each order k the norms are bounded by C_k times the norm of f in [[eq:gd-r5-1]] at an order k + k′, k′ independent of
k; u′, u_sing and B depend on k through the constant c of [[sec:iii-i2-4]], and u does not. At α_K = ½, for b-regular
forcing terms, (i)–(iii) are [[thm:gd-r2-5]] (i)–(iii) in the b-form of the dictionary.

*Proof.* We follow the proof of [[prop:iii-i2-5-1]] with the following changes.

1. *The operator.* There, L is a perturbation of L_b, removed by Step 1 and the iteration. Here L = L_b = □: Step 0,
   Step 1, the iteration and the continuity in (S, h) are void. P̂(σ) is invertible for real σ ≠ 0
   ([[prop:iii-d-6-2]]), and P̃(σ) for 0 < |σ| ≤ c_k ([[thm:gd-r2-4]]). The window is the one above.
2. [[lem:iii-i2-2-1]] and [[lem:iii-i2-3-1]] involve no operator, and hold as stated.
3. *The decomposition* ([[sec:iii-i2-4]]). For f ∈ C_c^∞(Ω_*°), the proof of [[thm:gd-r2-5]] gives
   u = u_hi + u_reg + u_sing with ℱu_hi = (1 − χ(|σ|))P̂(σ)⁻¹f̂, ℱu_reg = χ(|σ|)û_(reg,1),
   (û_(reg,1), b̂_1) := P̃(σ)⁻¹(f̂, 0) and ℱ(∂_(t_*)u_sing) = χ(|σ|)G_1(σ)(b̂_1), G_1(σ)b := Ψ(σ, ·)bW*: the first member
   of [[eq:iii-i2-4-1]], with no second (there is no generalised state). c is chosen as in [[sec:iii-i2-4]], with the
   constants of [[thm:gd-r2-4]]. For the density argument, the forward solution map of [[thm:ii-f1-1-1]] at
   P = P_0 = □ (with [[rem:ii-f1-7-1]] and the orders of [[rem:gd-orders]]) is continuous from the space of
   [[cor:ii-f1-1-2]] with b_+ := ½(½ + γ_+) and b_I := ½(b_+ + 3/2), which contains [[eq:gd-r5-1]]: ½ < b_+ < b_I < 3/2,
   b_+ ≤ γ_+, b_I + 1 < 5/2 ≤ w_I and α_K ≥ ½; and □ is 1-admissible with sf-weight b_+ − 5/2 by [[thm:gd-r2-5]]
   (iii), as b_+ − ½ ∈ (0, 1). The extension across {r = r_♭} is that of [[sec:iii-i2-4]].
4. *High and bounded frequencies: [[lem:iii-i2-4-1]].* Its inputs are [[cor:ii-g1-4-5]], with the hypotheses of
   [[ch:s02]] for □ (the proof of [[prop:iii-d-6-1]] gives them on a compact set of parameters), [[cor:ii-g1-4-2]], with
   the hypotheses of [[ch:s01]] ([[sec:hg-augmented]]), invertibility on the compact frequency set J
   ([[prop:iii-d-6-1]], [[prop:iii-d-6-2]]), and S̄ = 0. Its weight conditions at
   (β^f_I + 1, β_ι + 2, β_K) = (w_I, γ_+ + 2, α_K) are α_K ∈ (0, 1), β^f_I = w_I − 1 ≥ 3/2 and
   w_I ≥ γ_+ + 2 − min(α_K, 1 − ϵ_1), which holds with ϵ_1 := 1 − α_K. So u_hi ∈ H^(∞,(3/2−ϵ,𝔪,𝔪))_b(M′) for every 𝔪.
5. *The transform of f.* The condition of [[prop:ii-g1-3-3]] (1) at the weights (w_I, γ_+ + 2, α_K) is
   w_I ≥ γ_+ + 2 − min(α_K, 1 − ϵ), and it holds: if α_K ≤ 1 − ϵ it is the hypothesis w_I ≥ γ_+ + 2 − α_K; otherwise it
   reads w_I ≥ γ_+ + 1 + ϵ, and γ_+ + 1 + ϵ ≤ γ_+ + 1 + (3/2 − γ_+)/5 = 13/10 + (4/5)γ_+ < 5/2 ≤ w_I, as γ_+ < 3/2. So
   [[prop:ii-g1-3-3]] (1) gives f̂|_(±(0,1]) ∈ H^(∞,(min(w_I,γ_++2)−ϵ,γ_++1,α_K−1))_b(X^±_(sc-b)), the zf index set
   (0, 0) dropping as α_K − 1 < 0.
6. *Low frequencies: [[lem:iii-i2-4-2]]* with P̃ in place of L̃_b; its proof is that of [[prop:ii-g1-4-7]] with
   [[thm:iii-h-4-1]] (3) and the estimate of [[thm:gd-r2-4]], with the outgoing order β_scf − 2 − ϵ/2 below
   −½ + S̄ = −½. With β_scf := 3/2 − ϵ, β_tf := γ_+ − 1 and β_zf := α_K − 1, so that β_tf − β_zf = γ_+ − α_K ∈ (0, 1),
   and f̂ in the space of its right side (5/2 − ϵ ≤ min(w_I, γ_+ + 2) − ϵ):
   û_(reg,1) ∈ H^(∞,(3/2−2ϵ,γ_+−1,α_K−1))_b and b̂_1 ∈ H^(∞,α_K−1)_b(±(0, c], |dσ/σ|).
7. *The regular part.* [[prop:ii-g1-3-5]] (1) at the K-weight α_K ∈ (0, 1), with a void Taylor condition, gives
   u_reg ∈ H^(∞,(γ_+−ϵ,γ_+,α_K))_b(M′). With 4 this is (i), u′ := u_hi + u_reg, as γ_+ < 3/2 − 2ϵ.
8. *The cut-off state: [[lem:iii-i2-4-3]]* with the one state W* ∈ 𝒜² (q_1 = 2) and Ψ of [[lem:iii-h-2-5]], which does
   not depend on the operator: χG_1(b̂_1) ∈ H^(∞,(𝔪,α_K+1−ϵ,α_K−1))_b(X^±_(sc-b)).
9. *The singular part: one integration.* [[lem:iii-i2-3-1]] is applied once, to u_sing, with β_I := γ_+ − ϵ,
   β_ι := γ_+ and β_K := α_K − 1 ∈ [−½, 0). Its hypotheses: β_ι > β_I; β_K < 0 < β_ι − β_I; β_K ∈ (−1, 1) ∖ {0};
   ℱ(∂_(t_*)u_sing) = χG_1(b̂_1) is 8, whose tf-weight α_K + 1 − ϵ is at least γ_+ (as ϵ ≤ 3/2 − γ_+ and
   α_K + 1 ≥ 3/2) and whose zf-weight β_K < 0 carries no index term; on {t_* < −r}, u = 0, so
   u_sing = −(u_hi + u_reg) there, of weights at least (∞, β_ι, β_K) by 4 and 7; and ℱ(∂_(t_*)u_sing) is χ(|σ|) times
   the boundary value from Im σ > 0 of Ψb̂_1W* (the proof of [[thm:gd-r2-5]]), so ℱu_sing is supported in
   supp χ(|·|) ∪ {0}, a compact subset of (−c, c), c ≤ ½. [[lem:iii-i2-3-1]] gives
   u_sing ∈ H^(∞,γ_+−ϵ,γ_+−ϵ,((0,0),α_K−1))_b(M′), the term (0, 0) lying above the weight α_K − 1 < 0: this is (iii).
   At □ the second integration of [[prop:iii-i2-5-1]], which is needed there for the generalised state, does not occur.
10. *(ii).* B := ℱ⁻¹(χb̂_1). By 6, the pair (χb̂_1|_(σ<0), χb̂_1|_(σ>0)) lies in the space X^(k,α_K−1) of
   [[def:ii-g1-2-7]] with no polynomial part (α_K − 1 < 0), and [[prop:ii-g1-2-8]] (2) at the weight α_K ∈ (0, 1) gives
   B ∈ H^(k,α_K)_b(ℝ). The identities are those of [[thm:gd-r2-5]] (ii), proved there from
   ℱ(∂_(t_*)u_sing) = χΨb̂_1W* without a weight.
11. *What is not used.* The formal solutions at ℐ⁺ (Step 2a of the proof of [[prop:iii-i2-5-1]]) are not needed, as
   w_I ≥ 5/2; a forcing term that reaches ℐ⁺ with a lower order is first localised to a cone, as in the proof of
   [[thm:gd-r3-4]]. The expansion at ℐ⁺ (Step 3 there) is not carried: (iii) states the plain weight γ_+ − ϵ. ∎

**Theorem {#thm:gd-r5-2}** ([[thm:gd-r2-7]] at K⁺-weight α_K.) Let f and u be as in [[thm:gd-r5-1]] and R′ > r_♭. On
{r_♭ < r ≤ R′, t_* ≥ 8 max(R′, 1)}, with any number of derivatives in x and t_* (the constant depending on the number),

    |u − c_f(t_*)W*| ≤ C t_*^(−α_K)‖f‖,                                                                   {#eq:gd-r5-2}

with c_f of [[eq:gd-r2-2]] and ‖f‖ a norm of [[eq:gd-r5-1]]. In particular: (a) if ℓ(f) = 0, u = O(t_*^(−α_K)); (b) if
∫_v^∞|ℓ(f)| ≤ C′v^(−κ′), then u = c_∞W* + O(t_*^(−min(α_K,κ′))).

*Proof.* The steps (1)–(5) of the proof of [[thm:gd-r2-7]], with three replacements. In (2): |B(t)| ≤ C⟨t⟩^(−α_K)‖f‖, by
[[lem:gd-r2-6]] with H = ℂ on [T/2, 4T], as ⟨t⟩^(α_K−½)B and ⟨t⟩^(α_K−½)t∂_tB in L²(dt) give
∫_(T/2)^(4T)(|B|² + |t∂_tB|²) dt ≤ CT^(1−2α_K); the kernels ∂_rχ^H_K, ∂_tχ^H_K and χ_(r,r_h) are supported in
[1, 4 max(R′, 1)], so for t_* ≥ 8 max(R′, 1) the convolutions sample B on [t_*/2, t_*] and are O(t_*^(−α_K)).
In (3): |Q[u′](v)| ≤ C‖u′(t_*)‖_(C¹(𝒰_h)) ≤ Ct_*^(−α_K)‖f‖, by b-Sobolev embedding of [[thm:gd-r5-1]] (i) near K⁺.
In (5): u′ = O(t_*^(−α_K)) the same way, with its b-derivatives t_*∂_(t_*) and ∂_x; ∂_(t_*)β = ∂_tχ^H_K ∗ B, and
∂_(t_*)c_f = ℓ(f)/(4π²) is O(t_*^(−α_K)) by b-Sobolev embedding of f near K⁺. Density as in [[thm:gd-r2-7]], by the
bounds of [[thm:gd-r5-1]]. ∎

At α_K = ½ this is the bound of [[thm:gd-r2-7]], for b-regular forcing terms. In [[ch:harmonic-rate]] this theorem
gives the faster rates of [[thm:gd-r3-4]] (iii) and [[cor:gd-r4-4]] ([[cor:gd-r5-3]]); its extension to K⁺-weights in
(1, 2), and past that window to (2, 3) for forcing terms of zero total charge, gives those of the gauge vectors of
[[cor:gd-r4-6]], of [[prop:gd-r2-13]] (b) and of the Y_h clauses ([[cor:gd-r6-6]], [[cor:gd-r7-4]],
[[cor:hr-compact-rates]]), and the rate t_*^(−min(p_0,3/2)+ε), for every ε > 0, of the representative of
[[cor:gd-r4-4]], p_0 being the supremum of the orders at spatial infinity of the data of its Z′_0
([[prop:gd-r2-13]] (a), [[thm:harmonic-rate]]).
