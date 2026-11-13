## The linear solution in harmonic gauge, II: the rate {#ch:harmonic-rate}

[[ch:harmonic-structure]] gave every perturbation in the class a representative ġ_H that is in harmonic gauge on all
of N⁺, induces the given data exactly, and settles on compact sets to ṁK* + c_∞ℒ_(W*)g at the rate t_*^(−1/2)
([[cor:gd-r4-4]]). This chapter determines the rate. Two parts of ġ_H behave differently.

The spherically symmetric part is ṁK* + ℒ_(Z′_0)g exactly, with □Z′_0 = 0 ([[prop:gd-r7-5]]), so its rate is that of a
homogeneous solution of the 1-form wave operator, and is set by the decay of its Cauchy data at spatial infinity. We
carry the forward solution of □ to K⁺-weights in (1, 2) ([[thm:gd-r6-4]], [[thm:gd-r6-5]]) and, for forcing terms of
zero total horizon charge, past that window to (2, 3) ([[thm:gd-r7-1]]). A homogeneous solution with data of order
p ∈ (½, 3/2) at spatial infinity then settles at t_*^(−α) for every α < p ([[cor:gd-r7-6]]), and one with data of
compact support settles with an exact t_*^(−2) term, which an explicit solution of charge 4π² exhibits: the
switched-on Coulomb field of flat 4 + 1 placed on Tangherlini ([[lem:gd-r7-2]], [[thm:gd-r7-3]], [[cor:gd-r7-4]]). In
the class the order is p_0 > ½ + 2γ_Υ, and p_0 = 1 for data that differ from a change of mass only on a ball
([[cor:gd-r7-7]]).

The part with l ≥ 2 sees no zero-energy state. On the 1-forms with no part of degree l ≤ 1 the zero-energy operator of
□ has the indicial gap (−1, 3), no kernel and no cokernel at the weights of that gap, and an admissible transition face,
so the low-energy theory of [[ch:s03]] holds there without augmentation, at negative weights too ([[cor:gd-r8-9]]).
The forward solution then decays as fast as the forcing term allows ([[thm:gd-r8-10]]), and the part with l ≥ 2 of
ġ_H settles at t_*^(−3/2−κ) for every κ < δ_♯ ([[cor:gd-r8-11]]), δ_♯ = (1 − e_Υ)γ_Υ being the margin by which the
constraint damping makes the gauge forcing term decay along the forward cone ([[prop:gd-r3-2]]).

Together ([[thm:harmonic-rate]]): ġ_H settles to ṁK* + cℒ_(W*)g at t_*^(−min(p_0,3/2)+ε) for every ε > 0, at
t_*^(−1+ε) when the data differ from a change of mass only on a ball, and at t_*^(−3/2−κ), κ < δ_♯, for data of compact
support, whose spherically symmetric part then carries the exact term (m₀c/2)t_*^(−2)ℒ_(W*)g. The constant c is the
limit of the horizon charge of Z′_0 over that of W*, corrected by the Killing part of the data of Z′_0.

### Setting {#sec:hr-setting}

Everything of [[sec:hg-setting]] and [[sec:hg-positive]] is kept: g = g_(b₀) of mass m₀, r_h = m₀^(1/2), the ingoing
chart, the class, K = r⁻²dv², K_V, the linear solution ġ, its mass change ṁ, h = ġ − ṁK_V and w = α − 2 > 2 + ε_t; □
on 1-forms and □_0 on functions; W*, the horizon functional ℓ of [[eq:hg-ell]] and the horizon charge Q of
[[eq:hg-charge]]; W**, W**_H and K* of [[prop:np-10-2]]; P̂, P̃, f_*, φ_* and the spaces of [[sec:hg-augmented]]; the
cut-offs χ_K and χ^H_K of [[sec:hg-setting]], and the cone cut-off χ′ and the constant T_1 of [[sec:hg-source]]; the
forcing term F_Y of [[eq:gd-r3-2]] and J_h of [[eq:gd-r2-3]]; and M′, its faces I, ι = ι⁺ ∪ ι⁻ and K = K⁺ ∪ K⁻, the
spaces H^(k,(w_I,w_ι,w_K))_b(M′), X^±_(sc-b) with its faces scf, tf, zf, and the dictionary of [[sec:hg-positive]],
by which a conormal function whose pointwise orders exceed the weights lies in the space.

*The gauge condition.* We write Υ̇⁰(k) = −δGk for the linearised gauge 1-form ([[sec:ix-0]]). A symmetric 2-tensor k is
in harmonic gauge if Υ̇⁰(k) = 0, and [[eq:hg-box]] reads Υ̇⁰(ℒ_Xg) = −□X. By [[prop:np-10-2]] (iv) (b)–(c),
Υ̇⁰(K_V) = □W**_H and Υ̇⁰(K*) = 0.

*The form dψ.* dψ = m₀W* − (∂_v)^♭, ψ = v + F, is the closed 1-form of [[lem:gd-r2-9]]: □dψ = d□_0ψ = 0, and
ℒ_(dψ)g = m₀ℒ_(W*)g, as (∂_v)^♭ is Killing. dψ is stationary and bounded, and does not decay at infinity.

*Charges.* For a 1-form f on Ω_* in the class of [[eq:gd-r5-1]], ∫ℓ(f) dv = ℓ(f̂(0)), f̂(0) = ∫f dt_*, as t_* − v is a
function of r near r_h; we call it the *total charge* of f. c_f(t_*) := (4π²)⁻¹∫_(−∞)^(v_h(t_*)) ℓ(f) dv is its running
charge ([[eq:gd-r2-2]]), and for the forward solution u of □u = f, Q[u](v_h(t_*)) = 4π²c_f(t_*) by [[eq:gd-2-1]].

**Lemma {#lem:hr-charges}** (Two horizon charges.) For functions β and φ of (v, r) near the horizon, with ∂_r taken at
fixed v,

    Q[βW*] = 4π²(β − r_h∂_rβ)|_(r=r_h),        Q[φ dψ] = −4π²r_h³∂_rφ|_(r=r_h).                          {#eq:hr-charges}

*Proof.* The first is step (2) of the proof of [[thm:gd-r2-7]]. For the second, δ(φ dψ) = φ δdψ − g⁻¹(dφ, dψ) =
−g⁻¹(dφ, dψ), as δdψ = □_0ψ = 0. With dψ = dv + F′dr, g^(vv) = 0, g^(vr) = 1 and g^(rr) = f,
g⁻¹(dφ, dψ) = F′∂_vφ + (1 + fF′)∂_rφ, and 1 + fF′ = r_h³r⁻³, as fF′ = −(r − r_h)(r² + rr_h + r_h²)r⁻³. Also
d(φ dψ) = dφ ∧ dψ has the component (d(φ dψ))_(vr) = F′∂_vφ − ∂_rφ. So δ(φ dψ) + (d(φ dψ))_(vr) = −(1 + r_h³r⁻³)∂_rφ,
which is −2∂_rφ at r = r_h, and [[eq:hg-charge]] gives Q[φ dψ] = r_h³ · 2π² · (−2∂_rφ). ∎

### The forward solution at K⁺-weights in (1, 2) {#sec:hr-window}

Above the K⁺-weight 1 the transform of a forcing term has a Taylor term at zero frequency, f̂(0) = ∫f dt_*. The
augmented zero-energy operator inverts it at the weight α + 2 = γ_+ − 1, which lies in its window (0, 1) as long as
γ_+ < 2, and one integration in t_* recovers the solution. The spaces X^±_(sc-b), the cut-off χ_zf = χ_1(|σ|⟨x⟩) and
the constant c ≤ 1/(8√5) are those of [[sec:iii-i3-1]], c being also so small that χ_zf = 1 on supp φ_*.
[[lem:iii-i3-1-1]] involves no operator and holds as stated. Its two companions at □ are the following.

**Lemma {#lem:gd-r6-2}** ([[lem:iii-i3-1-2]] at □.) For u_0 ∈ H^(∞,a)_b(X) and |σ| ≤ c:

(a) (P̂(σ) − P̂(0))(χ_zf u_0) ∈ H^(∞,(∞,a+2,γ_zf))_b for every γ_zf < 1;

(b) f̂_*(σ) − χ_zf f̂_*(0) ∈ H^(∞,(N,3−ε,1−ε))_b(X^±_(sc-b)) for every N and ε > 0, and f̂_*(0) ∈ 𝒜³.

*Proof.* (a) P̂(σ) − P̂(0) = −iσL_1 − σ²L_2, with L_1 ∈ ρDiff¹_b and L_2 ∈ ρ²C^∞ near ∂X and with coefficients smooth
on compact sets ([[sec:hg-augmented]]); the proof of [[lem:iii-i3-1-2]] (a) uses of the operator only this. (b) By
[[lem:gd-r2-2]] (c), [[lem:iii-h-2-4]] (a) holds for f̂_*: f̂_* = f̂_c + f̂_∞, with f̂_c entire in σ and supported in
{r ≤ 2}, and f̂_∞ = r⁻³G(σr, x) on {r ≥ 1}, G entire and rapidly decreasing for Im ζ ≥ 0. The proof of
[[lem:iii-i3-1-2]] (b) uses only this. f̂_*(0) ∈ 𝒜³ is [[lem:gd-r2-2]] (b). ∎

**Lemma {#lem:gd-r6-3}** ([[lem:iii-i3-1-3]] at □.) Put G_1(σ)b := Ψ(σ, ·)bW* for b ∈ ℂ, with Ψ of
[[lem:iii-h-2-5]], and let χ be the cut-off of [[sec:iii-i2-4]]. For b_0 ∈ ℂ,
χ(|σ|)G_1(σ)(b_0) − χ_zf b_0W* ∈ H^(∞,(N,2−ε,1−ε))_b for every N and ε > 0, and W* ∈ H^(∞,2−ε)_b(X).

*Proof.* The proof of [[lem:iii-i3-1-3]] for G_1 alone, with the state W* ∈ 𝒜² ([[sec:hg-setting]]) in place of
ġ_b(ḃ_0): for r ≥ 1, Ψ = Φ(σr) with Φ(0) = 1 ([[lem:iii-h-2-5]] (b)), so G_1(b_0) − χ_zf b_0W* =
(Φ(ζ) − χ_1(|σ|⟨x⟩))b_0W*, ζ = σr, is O(min(|ζ|, 1)⟨ζ⟩^(−N)) times a state in 𝒜²; and the Fubini count of the proof of
[[lem:iii-i3-1-2]] (b), with ⟨x⟩⁻² in place of ⟨x⟩⁻³, gives the tf-weight 2 − ε. There is no generalised state. ∎

**Theorem {#thm:gd-r6-4}** (The forward solution at K⁺-weights in (1, 2).) Let α_K ∈ (1, 2), γ_+ ∈ (α_K, 2),
ε_1 ∈ (0, ½), w_I ≥ max(5/2, γ_+ + 1 + ε_1) and

    f ∈ H^(∞,(w_I,γ_++2,α_K))_b(Ω_*; T*)^(•,−),                                                            {#eq:gd-r6-1}

with plain weights (no expansion at ℐ⁺), and let u be the forward solution of □u = f ([[thm:ii-f1-1-1]] at
P = P_0 = □). Then for every ε ∈ (0, (2 − γ_+)/5]:

(i) u = u′ + u_sing with u′ ∈ H^(∞,(min(3/2,γ_+)−3ε,γ_+,α_K))_b(M′);

(ii) u_sing = β(t_*, r)W*, where ∂_(t_*)β(·, r) = (∂_tχ^H_K)(·, r) ∗ B and
β(·, r) − β(·, r′) = (χ^H_K(·, r) − χ^H_K(·, r′)) ∗ B for one B ∈ H^(k,α_K)_b(ℝ) ([[def:ii-g1-2-1]]), ∗ the
convolution in t_*, and ∫B = c_0 := (4π²)⁻¹∫ℓ(f) dv;

(iii) u − c_0χ^H_KW* ∈ H^(∞,(min(3/2,1+γ_+−α_K)−3ε,γ_+−2ε,α_K−1))_b(M′): at K⁺, u is c_0W* plus a term of weight
α_K − 1 > 0.

At each order k the norms are bounded by C_k times the norm of f in [[eq:gd-r6-1]] at an order k + ℓ, with ℓ
independent of k. u′, u_sing and B depend on k through the constant c of [[sec:iii-i2-4]]; u and c_0 do not.

*Proof.* We follow the proof of [[prop:iii-i3-2-1]], with L_b replaced by □ and L̃_b by P̃. Its Step 0 removes L − L_b
and is void, as L = L_b = □. Its Step 1 removes the terms of the forcing term at ℐ⁺; [[eq:gd-r6-1]] has none, so
u^♭ = u and f^♭ = f.

*Step 2 (the decomposition).* u = u_hi + u_reg + u_sing as in step 3 of the proof of [[thm:gd-r5-1]], with
ℱu_hi = (1 − χ(|σ|))P̂(σ)⁻¹f̂, ℱu_reg = χ(|σ|)û_(reg,1), (û_(reg,1), b̂_1) := P̃(σ)⁻¹(f̂, 0) and
ℱ(∂_(t_*)u_sing) = χ(|σ|)G_1(σ)(b̂_1). [[lem:iii-i2-4-1]] applies with (β^f_I + 1, β_ι + 2, β_K) =
(w_I, γ_+ + 2, α_K): β_K ∈ (1, 2) is not an integer, β^f_I = w_I − 1 ≥ 3/2, and β^f_I + 1 ≥ β_ι + 2 −
min(β_K, 1 − ε_1) reads w_I ≥ γ_+ + 1 + ε_1, as α_K > 1 − ε_1; its inputs at □ are those of step 4 of the proof of
[[thm:gd-r5-1]]. So u_hi ∈ H^(∞,(3/2−ε,N,N))_b(M′) for every N. Put ε_PP := min(ε, ε_1). [[prop:ii-g1-3-3]] (1) with
β_K = α_K and with ε_PP for its ε, whose condition w_I ≥ γ_+ + 2 − min(α_K, 1 − ε_PP) = γ_+ + 1 + ε_PP holds, gives

    f̂|_(±(0,c]) ∈ H^(∞,(5/2−ε,γ_++1,((0,0),α_K−1)))_b(X^±_(sc-b)),                                       {#eq:hr-fhat}

as min(w_I, γ_+ + 2) − ε_PP ≥ 5/2 − ε, with the zf-coefficient f̂(0) = ∫f dt_* ∈ H^(∞,γ_++1)_b(X), the same for both
signs (f(·, x) is integrable, its K⁺-weight being α_K > 1). For the density argument of step 3 of the proof of
[[thm:gd-r5-1]], the forward solution map is continuous from the space of [[cor:ii-f1-1-2]] with b_+ := 1 and
b_I := 5/4, which contains [[eq:gd-r6-1]]: ½ < b_+ < b_I < 3/2, b_+ ≤ γ_+, b_I + 1 ≤ w_I and α_K ≥ ½; and □ is
1-admissible with sf-weight b_+ − 5/2 by [[thm:gd-r2-5]] (iii), as b_+ − ½ ∈ (0, 1).

*Step 3.1 (zero energy).* At the weight α := γ_+ − 3, α + 2 = γ_+ − 1 ∈ (0, 1), and 𝒴_0 has the μ_b-weight
α + 4 = γ_+ + 1, so f̂(0) ∈ 𝒴_0; the column f̂_*(0) ∈ 𝒜³ lies in 𝒴_0, as γ_+ + 1 < 3. By [[prop:gd-r2-3]], at every
regularity, put

    (û_0, c_0) := P̃(0)⁻¹(f̂(0), 0),        û_0 ∈ H^(∞,γ_+−1)_b(X).

Apply ℓ to P̂(0)û_0 + c_0f̂_*(0) = f̂(0): ℓ ∘ P̂(0) = 0 on 𝒳_0, and ℓ(f̂_*(0)) = ℓ(L_1W*) = 4π² (the proof of
[[prop:gd-r2-3]]); so c_0 = ℓ(f̂(0))/4π² = (4π²)⁻¹∫ℓ(f) dv. For 0 < |σ| ≤ c, P̃(σ)(χ_zfû_0, c_0) =
(f̂(σ) − f̂_2(σ), 0), with

    f̂_2 := (f̂ − χ_zf f̂(0)) − [P̂(0), χ_zf]û_0 − (P̂(σ) − P̂(0))(χ_zfû_0) − c_0(f̂_*(σ) − χ_zf f̂_*(0)):

the row ⟨·, φ_*⟩_h does not depend on σ, ⟨χ_zfû_0, φ_*⟩_h = ⟨û_0, φ_*⟩_h = 0, and χ_zfû_0 ∈ 𝒳_σ for σ ≠ 0, having
compact support in x. The four terms lie in H^(∞,(5/2−ε,γ_++1,α_K−1))_b ([[eq:hr-fhat]] and the definition of the
space), H^(∞,(∞,γ_++1,∞))_b ([[lem:iii-i3-1-1]] (b) with p = 2, P̂(0) ∈ ρ²Diff²_b, a = γ_+ − 1),
H^(∞,(∞,γ_++1,γ_zf))_b for every γ_zf < 1 ([[lem:gd-r6-2]] (a) at a = γ_+ − 1), and H^(∞,(N,3−ε,1−ε))_b
([[lem:gd-r6-2]] (b)). As γ_+ + 1 ≤ 3 − ε and α_K − 1 < 1 − ε (both by ε ≤ (2 − γ_+)/5 and α_K < γ_+),

    f̂_2|_(±(0,c]) ∈ H^(∞,(5/2−ε,γ_++1,α_K−1))_b(X^±_(sc-b)).

*Step 3.2 (the regular part).* (û_(reg,1), b̂_1) = (χ_zfû_0, c_0) + P̃(σ)⁻¹(f̂_2, 0). [[lem:iii-i2-4-2]], with P̃ in
place of L̃_b as in step 6 of the proof of [[thm:gd-r5-1]], applies with β_scf := 3/2 − ε, β_tf := γ_+ − 1,
β_zf := α_K − 1 and the window β_tf − β_zf = γ_+ − α_K ∈ (0, 1) ([[thm:gd-r2-4]] at that weight). It gives

    û_(reg,1) ∈ H^(∞,(3/2−2ε,γ_+−1,((0,0),α_K−1)))_b,        b̂_1 ∈ H^(∞,((0,0),α_K−1))_b(±(0, c], |dσ/σ|),

with the coefficients û_0 and c_0 at σ = 0, the same for both signs. [[prop:ii-g1-3-5]] (1) with β_K = α_K ∈ (1, 2),
applied to χ(|σ|)û_(reg,1) (supported where the cut-off of that proposition is 1, as c ≤ ½), with its one Taylor
coefficient û_0 ∈ H^(∞,γ_+−1)_b(X), of order 0 < α_K − 1, gives u_reg ∈ H^(∞,(min(3/2,γ_+)−3ε,γ_+,α_K))_b(M′). With
Step 2 this is (i), with u′ := u_hi + u_reg.

*Step 3.3 (the singular part: one integration).* By [[lem:gd-r6-3]] for c_0, and by [[lem:iii-i2-4-3]] with a = α_K − 1
for b̂_1 − c_0 (with the one state W* ∈ 𝒜², as in step 8 of the proof of [[thm:gd-r5-1]]), whose tf-weight α_K + 1 − ε
exceeds 2 − ε,

    ℱ(∂_(t_*)u_sing) = χ(|σ|)G_1(σ)(b̂_1) ∈ H^(∞,(N,2−ε,((0,0),α_K−1)))_b,

with zf-coefficient c_0W*, the same for both signs. [[lem:iii-i2-3-1]] applies once, to u_sing, with
β_I := 1 + γ_+ − α_K, β_ι := γ_+ and β_K := α_K − 1 ∈ (0, 1). Its hypotheses hold: β_ι > β_I, as α_K > 1;
β_K = β_ι − β_I; β_K ∈ (−1, 1) ∖ {0}; the zf-restrictions of the two signs agree; the tf-weight 2 − ε is at least γ_+,
as ε ≤ 2 − γ_+; on Ω_<, u_sing = −(u_hi + u_reg), since u = 0 for t_* < 1, with weights at least (∞, γ_+, α_K); and
ℱu_sing is supported in supp χ(|·|) ∪ {0}, a compact subset of (−c, c) with c ≤ ½ (step 9 of the proof of
[[thm:gd-r5-1]]). So

    u_sing ∈ H^(∞,(1+γ_+−α_K,γ_+−ε,((0,0),α_K−1)))_b(M′).

Its (0, 0)-coefficient at K⁺ is lim_(t_*→∞) u_sing = ∫∂_(t_*)u_sing dt_* = ℱ(∂_(t_*)u_sing)(0) = c_0W*, as
∂_(t_*)u_sing(·, x) is integrable, its K⁺-weight being α_K > 1. Near K⁺, χ^H_K = 1; near ℐ⁺, χ^H_K = 0; and
χ^H_KW* has the ι⁺-weight 2 − ε, W* ∈ 𝒜² being stationary. So u_sing − c_0χ^H_KW* has the weights
(1 + γ_+ − α_K, γ_+ − ε, α_K − 1), as γ_+ < 2; with (i) this is (iii), as 1 + γ_+ − α_K < γ_+.

*Step 3.4 (the coefficient B).* B := ℱ⁻¹(χb̂_1). The pair (χb̂_1|_(σ<0), χb̂_1|_(σ>0)) lies in X^(k,α_K−1) of
[[def:ii-g1-2-7]], with polynomial part the constant c_0, of degree 0 < α_K − 1, the same for both signs.
[[prop:ii-g1-2-8]] (2) with β = α_K ∈ (1, 2) gives B ∈ H^(k,α_K)_b(ℝ), and ∫B = (χb̂_1)(0) = c_0. The identities of (ii)
are those of [[thm:gd-r2-5]] (ii), proved there from ℱ(∂_(t_*)u_sing) = χΨb̂_1W* without a weight. The dependence on k
is that of [[thm:gd-r5-1]]. ∎

The expansion at ℐ⁺, Step 4 of the proof of [[prop:iii-i3-2-1]], is not needed for (i)–(iii). There is one state and
no generalised partner, so one integration in t_* suffices, and the term at K⁺ is the constant c_0W*. The ι⁺-weight
γ_+ may exceed 3/2; the cap γ_+ < 2 is the zero-energy inversion of Step 3.1, which needs the column f̂_*(0) ∈ 𝒜³ to
lie in 𝒴_0 at the μ_b-weight γ_+ + 1.

**Theorem {#thm:gd-r6-5}** (The rate at K⁺-weights in (1, 2).) Let f and u be as in [[thm:gd-r6-4]] and R′ > r_♭. On
{r_♭ < r ≤ R′, t_* ≥ 8 max(R′, 1)}, with every number of derivatives in x and t_* (the constant depending on the
number),

    |u − c_f(t_*)W*| ≤ C t_*^(−α_K)‖f‖,                                                                   {#eq:gd-r6-2}

with ‖f‖ a norm of [[eq:gd-r6-1]]. In particular, if ℓ(f) vanishes for large v, then u = c_∞W* + O(t_*^(−α_K)),
c_∞ := (4π²)⁻¹∫ℓ(f) dv.

*Proof.* The proof of [[thm:gd-r5-2]], with [[thm:gd-r6-4]] (i)–(ii) in place of [[thm:gd-r5-1]] (i)–(ii).
|B(t)| ≤ C⟨t⟩^(−α_K)‖f‖ by [[lem:gd-r2-6]] on [T/2, 4T], as ⟨t⟩^(α_K−½)B and ⟨t⟩^(α_K−½)t∂_tB lie in L²(dt); the
kernels ∂_rχ^H_K, ∂_tχ^H_K and χ^H_K(·, r) − χ^H_K(·, r′) are supported in [1, 4 max(R′, 1)], so for
t_* ≥ 8 max(R′, 1) the convolutions sample B on [t_*/2, t_*]. u′ = O(t_*^(−α_K)) with its b-derivatives, by b-Sobolev
embedding near K⁺, where ρ_K is comparable to t_*⁻¹ on compact r-sets; so |Q[u′]| ≤ Ct_*^(−α_K)‖f‖, and
4π²β(t_*, r_h) = 4π²c_f + O(t_*^(−α_K)) as in step (4) of the proof of [[thm:gd-r2-7]]. ∂_(t_*)c_f = ℓ(f)/(4π²) is
O(t_*^(−α_K)) by b-Sobolev embedding of f near K⁺. ∎

### Gauge vectors with compactly supported data {#sec:hr-compact}

**Corollary {#cor:gd-r6-6}** (The rate t_*^(−2+ε).) Let Y be a smooth 1-form on N⁺, smooth up to Σ°, with □Y = 0,
whose Cauchy data on Σ° have compact support. Then Q[Y] is constant, and for every ε > 0, on each
{r_♭ < r ≤ R′, t_* ≥ T′} and with every number of derivatives,

    |Y − (Q[Y]/4π²)W*| ≤ C_ε t_*^(−2+ε).                                                                  {#eq:gd-r6-3}

*Proof.* Q[Y] is constant by [[eq:gd-2-1]].

(1) *The cut-off.* Let 𝒦_Y ⊂ Σ° be the support of the data. Ω^♯ is globally hyperbolic on each component, with Cauchy
hypersurface Σ° ([[lem:ix-1-2]]), and □ is normally hyperbolic ([[lem:ix-2-1]] (a)); so [[thm:std-bgp-cauchy]] (5)
gives a smooth solution on Ω^♯ with the data of Y, supported in J(𝒦_Y), and by [[lem:ix-1-1]] and [[lem:gd-r3-1]] Y is
its restriction to N⁺. So Y vanishes on N⁺ ∖ J⁺(𝒦_Y), a relatively open set containing Σ° ∖ 𝒦_Y. Take
χ_Y ∈ C_c^∞(M°_♭) equal to 1 on a neighbourhood of 𝒦_Y. Then U := (1 − χ_Y)Y vanishes on a neighbourhood of Σ° in N⁺:
near 𝒦_Y because χ_Y = 1, elsewhere because Y = 0. So F := □U = −[□, χ_Y]Y is smooth, supported in a compact subset of
N⁺, and vanishes near Σ°.

(2) *The forward problem.* Let T_a := min t_* on supp F. For p ∈ N⁺ with t_*(p) < T_a, the past of p in N⁺ lies in
{t_* < T_a}, dt_* being timelike ([[lem:iii-b-3-7]] (a)), and there □U = 0; U vanishes near Σ°, so U(p) = 0
([[lem:ix-1-1]] on Ω^♯, [[lem:gd-r3-1]]). Extended by 0 across Σ°, U is smooth on M°_♭, vanishes on {t_* < T_a},
and solves □U = F. Let T̂ = 2/C_♭ be the constant of [[sec:viii-0]]. g being stationary, the translate
U_T of U by T̂ − T_a in t_* solves □U_T = F_T, F_T the translate of F, and vanishes on {t_* < T̂}, which contains
{t^♭_* < 2} as C_♭t_* ≤ t^♭_* ([[lem:ii-c-3-2]] (b)). So U_T is the forward solution on Ω_* of □U_T = F_T
([[prop:ii-e-3-4]]), and F_T, smooth with compact support, lies in [[eq:gd-r6-1]] for every α_K < 2, γ_+ < 2 and w_I.

(3) *The rate.* On compact r-sets at late times χ_Y = 0, so Y = U. [[thm:gd-r6-5]] with α_K := 2 − ε and
γ_+ ∈ (α_K, 2), translated back, gives |U − c_F(t_*)W*| ≤ Ct_*^(−2+ε). Once χ_Y = 0 near the horizon,
c_F(t_*) = Q[U]/4π² = Q[Y]/4π², by [[eq:gd-2-1]] and U = 0 for t_* < T_a. ∎

The cut-off has compact support in spacetime, and this is what gives the rate: a cut-off in a cone, as in the proof of
[[cor:gd-r4-6]], produces a forcing term whose ι⁺-weight is that of the forward solution of [[thm:ii-f1-1-1]], below
3/2. The cut-off is admissible because Y vanishes near Σ° off the domain of influence of its data.
