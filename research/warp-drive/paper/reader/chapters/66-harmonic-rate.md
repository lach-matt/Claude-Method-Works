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

### Past the window: forcing terms of zero total charge {#sec:hr-past}

The cap γ_+ < 2 of [[thm:gd-r6-4]] is the column at order 0 in σ. A forcing term of zero total charge needs no column
there, and the column enters only at order 1, at the weight γ_+ − 2; so the window extends to K⁺-weights in (2, 3).
An explicit solution of charge 4π² then gives the t_*^(−2) term of every forcing term with enough decay at ℐ⁺.

**Theorem {#thm:gd-r7-1}** (Past the window, for forcing terms of zero total charge.) Let α_K ∈ (2, 3),
γ_+ ∈ (α_K, 3), ε_1 ∈ (0, 3 − γ_+), w_I ≥ γ_+ + 1 + ε_1 and

    f ∈ H^(∞,(w_I,γ_++2,α_K))_b(Ω_*; T*)^(•,−),        ∫ℓ(f) dv = 0,                                  {#eq:gd-r7-1}

with plain weights, and let u be the forward solution of □u = f. Then for every ε ∈ (0, ε_1/3]:

(i) u = u′ + u_sing with u′ ∈ H^(∞,(3/2−3ε,γ_+,α_K))_b(M′);

(ii) u_sing = β(t_*, r)W* with ∂_(t_*)β(·, r) = (∂_tχ^H_K)(·, r) ∗ B and
β(·, r) − β(·, r′) = (χ^H_K(·, r) − χ^H_K(·, r′)) ∗ B, where B ∈ H^(k,α_K)_b(ℝ) and ∫B = 0;

(iii) on {r_♭ < r ≤ R′, t_* ≥ 8 max(R′, 1)}, with every number of derivatives in x and t_*,
|u − c_f(t_*)W*| ≤ C t_*^(−α_K)‖f‖.

The dependence on k is that of [[thm:gd-r6-4]].

*Proof.* The proof of [[thm:gd-r6-4]], with the following changes.

*Step 2.* [[lem:iii-i2-4-1]] at (w_I, γ_+ + 2, α_K), α_K ∈ (2, 3) not an integer, gives u_hi ∈ H^(∞,(3/2−ε,N,N))_b; its
conditions are w_I − 1 ≥ 3/2 and w_I ≥ γ_+ + 1 + ε_1. [[prop:ii-g1-3-3]] (1) at β_K = α_K, with ε_PP := min(ε, ε_1)
for its ε, gives

    f̂|_(±(0,c]) ∈ H^(∞,(5/2−ε,γ_++1,((0,0),(1,0),α_K−1)))_b(X^±_(sc-b)),

with the Taylor terms of orders 0 and 1: their coefficients are f̂(0) = ∫f dt_* ∈ H^(∞,γ_++1)_b(X) and
f̂_1 := i∫t_*f dt_* ∈ ⟨x⟩H^(∞,γ_++1)_b(X) ⊂ H^(∞,γ_+)_b(X), each the same for both signs. The density step is that of
[[thm:gd-r6-4]].

*Step 3.1′ (zero energy at order 0, without the column).* Put β_tf := γ_+ − 1 ∈ (1, 2). At the b-weight β_tf, which
lies in the interval (0, 2) on which P̂ satisfies (G) ([[sec:iii-d1-1]]), P̂(0): 𝒳_0 → 𝒴_0 has kernel span{W*} and
range ker ℓ ([[lem:iii-d1-2-1]] (2)–(3); by [[thm:i-c-3-1]] (3)–(4), kernels and annihilators of ranges do not depend
on the weight within the gap). f̂(0) ∈ 𝒴_0, its μ_b-weight being β_tf + 2, and ℓ(f̂(0)) = ∫ℓ(f) dv = 0. So there is a
unique û_0 ∈ H^(∞,β_tf)_b(X) with P̂(0)û_0 = f̂(0) and ⟨û_0, φ_*⟩_h = 0 (the argument at every regularity s > 5/2). The
column is not used.

*Step 3.1″ (order 1).* Put g_1 := f̂_1 + iL_1û_0 ∈ H^(∞,β_tf+1)_b(X) (L_1 ∈ ρDiff¹_b). [[prop:gd-r2-3]] at the weight
α + 2 := β_tf − 1 = γ_+ − 2 ∈ (0, 1), where 𝒴_0 has the μ_b-weight γ_+ < 3 and so contains g_1 and the column, gives
(û_1, b_1) := P̃(0)⁻¹(g_1, 0), with û_1 ∈ H^(∞,β_tf−1)_b(X), ⟨û_1, φ_*⟩_h = 0 and b_1 = ℓ(g_1)/4π².

*The remainder.* With P̂(σ) = P̂(0) − iσL_1 − σ²L_2, P̂(0)û_0 = f̂(0) and P̂(0)û_1 + b_1f̂_*(0) = g_1, expanding gives,
for 0 < |σ| ≤ c, P̃(σ)(χ_zf(û_0 + σû_1), σb_1) = (f̂(σ) − f̂_2(σ), 0), where

    f̂_2 := (f̂ − χ_zf(f̂(0) + σf̂_1)) − [P̂(0), χ_zf](û_0 + σû_1) + iσ[L_1, χ_zf]û_0 + σ²L_2χ_zfû_0
             + iσ²L_1χ_zfû_1 + σ³L_2χ_zfû_1 − σb_1(f̂_*(σ) − χ_zf f̂_*(0));

the row vanishes, as ⟨û_0, φ_*⟩_h = ⟨û_1, φ_*⟩_h = 0. The terms lie, in order: in H^(∞,(5/2−ε,γ_++1,α_K−1))_b
(Step 2); in H^(∞,(∞,γ_++1,∞))_b ([[lem:iii-i3-1-1]] (b) with p = 2, at a = β_tf, and at a = β_tf − 1 with the factor
σ, which has tf-order 1 on supp dχ_zf); in the same space ([[lem:iii-i3-1-1]] (b) with p = 1, and one factor σ); in
H^(∞,(∞,β_tf+4,γ_zf))_b ([[lem:iii-i3-1-1]] (a) with p = j = 2); in H^(∞,(∞,β_tf+2,γ_zf))_b ([[lem:iii-i3-1-1]] (a)
at a = β_tf − 1 with p = 1, j = 2, and (b) for the commutator [L_1, χ_zf]); in H^(∞,(∞,β_tf+4,γ_zf))_b
([[lem:iii-i3-1-1]] (a) with p = 2, j = 3), for every γ_zf < 2; and in H^(∞,(N,4−ε,2−ε))_b ([[lem:gd-r6-2]] (b) and
one factor σ, |σ| = ρ_tfρ_zf). As α_K − 1 < 2 − ε and β_tf + 2 = γ_+ + 1 ≤ 4 − ε (by ε ≤ ε_1/3 < 3 − γ_+),

    f̂_2|_(±(0,c]) ∈ H^(∞,(5/2−ε,γ_++1,α_K−1))_b(X^±_(sc-b)).

*Step 3.2.* [[lem:iii-i2-4-2]] with P̃, whose β_zf is free and enters by division by |σ|^(β_zf), at
β_scf := 3/2 − ε, β_tf and β_zf := α_K − 1, with the window β_tf − β_zf = γ_+ − α_K ∈ (0, 1) ([[thm:gd-r2-4]] there),
gives (û′, b̂′) := P̃(σ)⁻¹(f̂_2, 0) with û′ ∈ H^(∞,(3/2−2ε,β_tf,α_K−1))_b and
b̂′ ∈ H^(∞,α_K−1)_b(±(0, c], |dσ/σ|). So û_(reg,1) = χ_zf(û_0 + σû_1) + û′ and b̂_1 = σb_1 + b̂′.
[[prop:ii-g1-3-5]] (1) at β_K = α_K applies with the two Taylor terms: their coefficients û_0 and û_1 are the same for
both signs, and v_0 = û_0 and v_1 = ⟨x⟩⁻¹û_1 lie in H^(∞,γ_+−1)_b(X), the tf-weight β_ι − 1 that it asks
(β_ι = γ_+). It gives u_reg ∈ H^(∞,(3/2−3ε,γ_+,α_K))_b(M′), as γ_+ > 3/2. With Step 2 this is (i).

*Step 3.4.* B := ℱ⁻¹(χb̂_1). The pair (χb̂_1|_(σ<0), χb̂_1|_(σ>0)) lies in X^(k,α_K−1) of [[def:ii-g1-2-7]], with the
polynomial part b_1σ, of degree 1 < α_K − 1, the same for both signs. [[prop:ii-g1-2-8]] (2) at β = α_K ∈ (2, 3)
gives B ∈ H^(k,α_K)_b(ℝ), and ∫B = (χb̂_1)(0) = 0. The identities of (ii) are those of [[thm:gd-r2-5]] (ii).

*(iii)* is the proof of [[thm:gd-r6-5]], with (i)–(ii): |B(t)| ≤ C⟨t⟩^(−α_K)‖f‖ by [[lem:gd-r2-6]], the convolutions
sample B on [t_*/2, t_*], and u′ = O(t_*^(−α_K)) with its b-derivatives by b-Sobolev embedding near K⁺; so
|Q[u′]| ≤ Ct_*^(−α_K)‖f‖ and 4π²β(t_*, r_h) = 4π²c_f + O(t_*^(−α_K)). No integration with a moment condition is
needed, and no statement at K⁺ is made for u_sing itself. ∎

The caps here are γ_+ < 3, which the column at order 1 needs (û_0 is of order r⁻², and 𝒴_0 must contain f̂_*(0) at
the μ_b-weight γ_+), and α_K < 3, where the Taylor term of order 2 enters.

**Lemma {#lem:gd-r7-2}** (An explicit solution of charge 4π².) For w > 0 and r > 0 put

    𝔨(w, r) := r⁻²((w + r)(w(w + 2r))^(−1/2) − 1),        𝔨(w, r) := 0  for w < 0,                     {#eq:hr-kernel}

so that a_0(t, r) := r⁻²H(t − r) + 𝔨(t − r, r) = tr⁻²(t² − r²)^(−1/2)H(t − r), H the Heaviside function. Let
R_T ≥ 3R₁, let h ∈ C^∞([r_♭, ∞)) equal −2r for r ≤ R_T and −2r_*(r) for r ≥ 2R_T, r_* of [[sec:iii-b-4]], and put
T := v + h(r). On {r ≥ 2R_T}, v = x¹ + 2r_*, so T = x¹ = t − |x| ([[eq:iii-b-4-1]]); near infinity
t_* = x¹ + C′ − 8m₀|x|⁻¹ ([[eq:iii-b-3-6]]); and on {r ≤ 2R_T}, t_* − v and T − v are functions of r. So |T − t_*| is
bounded on {r ≥ r_♭}. Fix T_2 so large that {T ≥ T_2} ⊂ {t^♭_* ≥ T̂}, and χ_on ∈ C^∞(ℝ) equal to 0 on (−∞, T_2] and to
1 on [T_2 + 1, ∞). Put

    𝔞(T, r) := ∫χ_on′(s)𝔨(T − s, r) ds,        u_ex := χ_on(T)W* + 𝔞(T, r) dψ,        f_ex := □u_ex.

Then:

(a) u_ex is smooth on {r ≥ r_♭}, spherically symmetric, and vanishes on {T < T_2}. At m₀ = 0 it is a dt, with
a(T, r) := χ_on(T)r⁻² + 𝔞(T, r) = ∫χ_on′(s)a_0(t − s, r) ds: the flat field of a charge switched on along χ_on.

(b) f_ex has ℐ⁺-order 4, ι⁺-order 6 and K⁺-order 3, with b-regularity, and vanishes on {t^♭_* < T̂}. So it lies in the
space of [[eq:gd-r7-1]], the condition on the charge aside, for every α_K < 3, γ_+ < 3 and w_I < 4, and in
[[eq:gd-r6-1]] for every α_K < 2.

(c) At r = r_h, with ∂_r at fixed v, Q[u_ex](v) = 4π²(χ_on(T) − r_h∂_r(χ_on(T))) − 4π²r_h³∂_r𝔞. So
Q[u_ex] = 4π² + O(t_*^(−3)) at late times, and the total charge of f_ex is 4π².

(d) On compact r-sets at late times, with every derivative, u_ex − W* = 𝔞 dψ = ½t_*^(−2)dψ + O(t_*^(−3)).

*Proof.* *The flat field.* In the variables (t, r), for t > r > 0, a_0 = tr⁻²(t² − r²)^(−1/2) solves the radial wave
equation of ℝ^(1+4):

    (∂_t² − ∂_r² − (3/r)∂_r)a_0 = 0.

Indeed b_0 := ∂_ta_0 = −s^(−3/2), s := t² − r², and ∂_t²b_0 = 3s^(−5/2) − 15t²s^(−7/2), ∂_rb_0 = −3rs^(−5/2),
∂_r²b_0 = −3s^(−5/2) − 15r²s^(−7/2), so (∂_t² − ∂_r² − (3/r)∂_r)b_0 = 15s^(−5/2) − 15(t² − r²)s^(−7/2) = 0. The
operator has coefficients independent of t, so the left side for a_0 is a function of r alone. As t → ∞ at fixed r,
a_0 = r⁻²(1 − r²/t²)^(−1/2) tends to r⁻² with its r-derivatives while its t-derivatives tend to 0, and
(∂_r² + (3/r)∂_r)r⁻² = 0; so that function vanishes. In the variables (w, r) := (t − r, r) the operator is

    P := 2∂_w∂_r − ∂_r² − (3/r)∂_r + (3/r)∂_w,

as ∂_t = ∂_w and ∂_r|_t = ∂_r|_w − ∂_w; so Pa_0 = 0 on {w > 0}. Near w = 0, a_0 = w^(−1/2)g(w, r), with
g(w, r) := (w + r)r⁻²(w + 2r)^(−1/2) smooth on [0, ∞) × (0, ∞) and g(0, r) = 2^(−1/2)r^(−3/2); as
(2∂_r + 3/r)r^(−3/2) = 0, 𝔟 := (2∂_r + 3/r)a_0 = w^(−1/2)(2∂_r + 3/r)g is O(w^(1/2)) as w → 0+, locally uniformly in
r. Now a(T, r) = ∫_0^∞ χ_on′(T − w)a_0(w, r) dw, as χ_on(T) = ∫_0^∞ χ_on′(T − w)
dw. The r-derivatives of a_0 are w^(−1/2)
times functions smooth up to w = 0, so they are locally integrable, uniformly for r in compact subsets of (0, ∞); hence
a is smooth on {r > 0}, and we may differentiate under the integral, the T-derivatives falling on χ_on′. As
χ_on″(T − w) = −∂_w(χ_on′(T − w)), an integration by parts on [ε, ∞) gives

    Pa(T, r) = lim_(ε→0) (χ_on′(T − ε)𝔟(ε, r) + ∫_ε^∞ χ_on′(T − w)(Pa_0)(w, r) dw) = 0,                    {#eq:hr-flat}

since Pa_0 = ∂_w𝔟 − (∂_r² + (3/r)∂_r)a_0 = 0 on {w > 0} and 𝔟(ε, r) → 0.

*(a)* 𝔨(·, r) = a_0(·, r) − r⁻²H is smooth on {w > 0} and vanishes on {w < 0}, with the integrable singularity
w^(−1/2)g(0, r) at w = 0+, and its r-derivatives behave alike; so 𝔞 is smooth on {r > 0}, as a is. T, W* and dψ are
smooth on {r ≥ r_♭}, r_♭ > 0. χ_on(T) and 𝔞 vanish on {T < T_2}, as χ_on′(T − w)𝔨(w, r) ≠ 0 needs w > 0 and T − w ≥ T_2.
Everything is spherically symmetric. At m₀ = 0, r_h = 0, v = t + r and T = t − r; W* = r⁻²dv − r⁻²dr = r⁻²dt and,
as F′ = −1, dψ = dv − dr = dt; so u_ex = a dt.

*(b) Near infinity.* On {r ≥ 2R_T}, dv = dT + 2f⁻¹dr, so g = −f dT² − 2 dT dr + r²γ, and

    W* = r⁻²dT + dr/(r(r − r_h)),        dψ = dT + p(r) dr,        p(r) := 1 + m₀/(r(r − r_h)).

For a spherically symmetric 1-form Y = A dT + B dr, the calculation of the proof of [[lem:gd-r2-9]], with g^(TT) = 0,
g^(Tr) = −1 and g^(rr) = f, gives, for φ := δY and q := r³(dY)_(Tr),

    φ = ∂_TB + r⁻³∂_r(r³(A − fB)),        q = r³(∂_TB − ∂_rA),
    (□Y)_T = ∂_Tφ + r⁻³(f∂_rq − ∂_Tq),        (□Y)_r = ∂_rφ + r⁻³∂_rq,

and no angular components. For Y = u_ex, with χ := χ_on(T),

    φ = χ′/(r(r − r_h)) + p ∂_T𝔞 − r_h³r⁻³∂_r𝔞,        q = 2χ + r²χ′/(r − r_h) + r³p ∂_T𝔞 − r³∂_r𝔞,

and substituting gives, for all functions χ of T and 𝔞 of (T, r), with a := χr⁻² + 𝔞,

    f_ex = (Pa) dψ + R_T dT + R_r dr,                                                                    {#eq:hr-far}
    R_T = m₀r⁻²∂_r²𝔞 + 3m₀r⁻³∂_r𝔞 − 2m₀r⁻³p ∂_T𝔞 − 2m₀r⁻⁴(r − r_h)⁻¹χ′,
    R_r = m₀r⁻²p ∂_r²𝔞 + 3m₀(r² + rr_h − r_h²)r⁻⁴(r − r_h)⁻¹∂_r𝔞 − 2m₀(2r − r_h)r⁻²(r − r_h)⁻²∂_T𝔞
          − r_h(3r² − 2rr_h + r_h²)r⁻⁴(r − r_h)⁻²χ′,

with Pa = 2∂_T∂_ra − ∂_r²a − (3/r)∂_ra + (3/r)∂_Ta. By [[eq:hr-flat]], Pa = 0, so f_ex = R_T dT + R_r dr there: every
term carries a factor m₀ or r_h, and no term has χ or 𝔞 undifferentiated.

*Orders at ℐ⁺.* 𝔨(w, r) = r⁻²𝔨_0(w/r) with 𝔨_0(ϱ) := (1 + ϱ)(ϱ(2 + ϱ))^(−1/2) − 1, and for 0 < ϱ < 2,
𝔨_0(ϱ) = (2ϱ)^(−1/2)Σ_(j≥0) c_jϱ^j − 1 with a convergent series, c_0 = 1. On the support of χ_on′(T − w),
0 < w ≤ T − T_2; so for T in a bounded set and r large, with every derivative,

    𝔞 = −χ_on(T)r⁻² + 2^(−1/2)Σ_(j≥0) c_j r^(−3/2−j)F_j(T),        F_j(T) := ∫_0^∞ χ_on′(T − w)w^(j−½) dw,

each F_j smooth. Hence ∂_T𝔞 = O(r^(−3/2)), ∂_r𝔞 = O(r^(−5/2)) and ∂_r²𝔞 = O(r^(−7/2)), and T∂_T and r∂_r preserve these
forms. In [[eq:hr-far]] the coefficients of ∂_r²𝔞 are O(r⁻²) and those of ∂_r𝔞 and ∂_T𝔞 are O(r⁻³); so these terms
have ℐ⁺-order at least 9/2. The χ_on′ terms are −2m₀r⁻⁵χ_on′(1 + O(r⁻¹)) and −3r_hr⁻⁴χ_on′(1 + O(r⁻¹)), of order 4,
supported in the slab {T_2 ≤ T ≤ T_2 + 1}. dT and dr are smooth combinations of the Cartesian frame there.

*Orders at ι⁺.* For T ≥ T_2 + 1, χ_on = 1, and f_ex = Σ_m c_m(r)D_m𝔞 on {r ≥ 2R_T}, with D_m ∈ {∂_T, ∂_r, ∂_r²}; by
[[eq:hr-far]] the coefficients have the leading powers r^(−p_m), p_m = 3, 3, 2, in both components, and their other
terms carry further powers of r⁻¹. D_m𝔞 = ∫χ_on′(s)(D_m𝔨)(T − s, r) ds, and with ϱ := w/r,

    ∂_w𝔨 = r⁻³𝔨_0′(ϱ),        ∂_r𝔨 = −r⁻³(2𝔨_0 + ϱ𝔨_0′)(ϱ),        ∂_r²𝔨 = r⁻⁴(6𝔨_0 + 6ϱ𝔨_0′ + ϱ²𝔨_0″)(ϱ):

D_m𝔨 = r^(−d_m)𝔨_m(ϱ) with d_m = 3, 3, 4. As ϱ → 0, by the series above, 𝔨_m(ϱ) = ϱ^(a_m)(𝔨_m⁰ + O(ϱ^(1/2))) with
(a_m) = (−3/2, −1/2, −1/2), and as ϱ → ∞, from 𝔨_0(ϱ) = ½ϱ⁻² − ϱ⁻³ + (15/8)ϱ⁻⁴ + O(ϱ⁻⁵), 𝔨_m(ϱ) = ϱ^(−b_m)(𝔨_m^∞ +
O(ϱ⁻¹)) with (b_m) = (3, 3, 4); both expansions are conormal, ϱ∂_ϱ preserving them. Near ι⁺ ∩ ℐ⁺, with ρ_+ ∼ T⁻¹ and
ρ_I ∼ ϱ = T/r, a term c_mD_m𝔨 is ρ_+^(p_m+d_m)ρ_I^(p_m+d_m+a_m) times a bounded conormal function; near ι⁺ ∩ K⁺, with
ρ_+ ∼ r⁻¹ and ρ_K ∼ ϱ⁻¹, it is ρ_+^(p_m+d_m)ρ_K^(b_m) times one. Here p_m + d_m = 6, p_m + d_m + a_m ≥ 9/2 and b_m ≥ 3.
The lower terms of c_m raise the orders, r∂_r and ϱ∂_ϱ preserve the forms, and the convolution with χ_on′ shifts T by
at most T_2 + 1. So f_ex has ι⁺-order 6, with ℐ⁺-order 9/2 and K⁺-order 3 at the corners.

*Near compact sets.* At late times χ_on(T) = 1 on {r ≤ 2R_T}, so u_ex = W* + 𝔞 dψ there and, as □W* = □dψ = 0 and
□ = −∇^α∇_α on 1-forms,

    f_ex = (□_0𝔞) dψ − 2∇_(∇𝔞) dψ,

every term carrying a derivative of 𝔞. From 𝔨_0(ϱ) = ½ϱ⁻² − ϱ⁻³ + O(ϱ⁻⁴), uniformly for r in compact sets,
𝔨 = ½w⁻² − rw⁻³ + O(w⁻⁴), ∂_w𝔨 = −w⁻³ + O(w⁻⁴), ∂_r𝔨 = −w⁻³ + O(w⁻⁴), and the second derivatives are O(w⁻⁴), each
w∂_w preserving the bounds. T − v is a function of r, so the derivatives of 𝔞 in (v, r) are O(T⁻³) there, with
b-regularity: f_ex has K⁺-order 3. The slab {T_2 ≤ T ≤ T_2 + 1} ∩ {r ≤ 2R_T} is compact.

f_ex is smooth and vanishes on {T < T_2}, which contains {t^♭_* < T̂}. With these orders the criterion of
[[sec:hg-positive]] gives the memberships.

*(c)* By [[eq:hr-charges]], Q[χ_on(T)W*] = 4π²(χ_on(T) − r_h∂_r(χ_on(T))) and Q[𝔞 dψ] = −4π²r_h³∂_r𝔞 at r = r_h, with ∂_r
at fixed v. As r_h < R_T, T = v − 2r near the horizon, so ∂_r(χ_on(T)) = −2χ_on′(T) vanishes at late times, and
∂_r𝔞|_v = ∂_r𝔞|_T − 2∂_T𝔞 = O(T⁻³). So Q[u_ex] = 4π² + O(t_*^(−3)). As u_ex = 0 for T < T_2, [[eq:gd-2-1]] gives
∫ℓ(f_ex) dv = lim_(v→∞) Q[u_ex](v) = 4π².

*(d)* On compact r-sets, 𝔨(w, r) = ½w⁻² + O(w⁻³) uniformly, with every derivative, and ∫χ_on′ = 1; so
𝔞 = ½T⁻² + O(T⁻³), and T − t_* is bounded there. ∎

The coefficient ½ is that of the flat field: at m₀ = 0 and fixed r, a_0 = r⁻²(1 − r²/t²)^(−1/2) = r⁻² + ½t⁻² + O(t⁻⁴),
and a_0 → r⁻² = 4π²G as t → ∞, G = (4π²|x|²)⁻¹ the Green function of −Δ on ℝ⁴. So a_0 is the field of the charge
4π²δ_0 switched on at t = 0, which in 4 + 1 dimensions approaches its static value at the rate t⁻².

**Theorem {#thm:gd-r7-3}** (The t_*^(−2) term.) Let f satisfy [[eq:gd-r7-1]] without the condition ∫ℓ(f) dv = 0, with
γ_+ < 3 and w_I < 4 (lowering weights is free), let c_0 := (4π²)⁻¹∫ℓ(f) dv, and let u be the forward solution of
□u = f. Then on each {r_♭ < r ≤ R′, t_* ≥ T′}, with every number of derivatives in x and t_*,

    u − c_f(t_*)W* = (c_0/2) t_*^(−2) dψ + O(t_*^(−α_K)),        dψ = m₀W* − (∂_v)^♭.                    {#eq:gd-r7-2}

*Proof.* f′ := f − c_0f_ex lies in the space of [[eq:gd-r7-1]] ([[lem:gd-r7-2]] (b)) and has zero total charge
([[lem:gd-r7-2]] (c)). u − c_0u_ex is smooth, vanishes on {t^♭_* < 1} (u_ex vanishes on {t^♭_* < T̂}), and solves
□(u − c_0u_ex) = f′; so it is the forward solution of f′ ([[prop:ii-e-3-4]]). [[thm:gd-r7-1]] (iii) gives
u − c_0u_ex − c_(f′)(t_*)W* = O(t_*^(−α_K)). By [[eq:gd-2-1]], at v = v_h(t_*),
4π²c_(f′) = Q[u] − c_0Q[u_ex] = 4π²c_f − c_0Q[u_ex], and Q[u_ex] = 4π² + O(t_*^(−3)) ([[lem:gd-r7-2]] (c)). So
u = c_fW* + c_0(u_ex − W*) + O(t_*^(−α_K)), and [[lem:gd-r7-2]] (d) gives [[eq:gd-r7-2]], as α_K < 3. ∎

**Corollary {#cor:gd-r7-4}** (Gauge vectors with compactly supported data.) Let Y be a smooth 1-form on N⁺, smooth up
to Σ°, with □Y = 0, whose Cauchy data on Σ° have compact support, and let c := Q[Y]/4π². For every ε > 0, on each
{r_♭ < r ≤ R′, t_* ≥ T′} and with every number of derivatives,

    Y − cW* = (c/2) t_*^(−2) dψ + O(t_*^(−3+ε)),
    ℒ_Yg − cℒ_(W*)g = (m₀c/2) t_*^(−2) ℒ_(W*)g + O(t_*^(−3+ε)).                                          {#eq:gd-r7-3}

The second term is not o(t_*^(−2)) when c ≠ 0: ℒ_(W*)g ≠ 0, and (ℒ_(W*)g)_(vr) = −(7/24)r_h⁻³ at r = 2r_h.

*Proof.* The cut-off of the proof of [[cor:gd-r6-6]], with its translation, gives U = Y on compact r-sets at late times,
U the forward solution of a smooth forcing term with compact support in spacetime; that forcing term lies in
[[eq:gd-r7-1]] (without the condition on the charge) for every α_K < 3, γ_+ < 3 and w_I < 4, and its running charge is
constant, c_F = Q[U]/4π² = c, once the cut-off vanishes near the horizon. [[thm:gd-r7-3]] with α_K := 3 − ε gives the
first identity. For the second, ℒ_(φ dψ)g = φℒ_(dψ)g + 2dφ ⊗_s dψ and ℒ_(dψ)g = m₀ℒ_(W*)g; with φ := (c/2)t_*^(−2),
dφ = O(t_*^(−3)). For the value: (ℒ_(W*)g)_(vr) = ∂_rW*_v + ∂_vW*_r − 2Γ^μ_(vr)W*_μ, and in the ingoing chart
Γ^v_(vr) = 0 and Γ^r_(vr) = −f′/2; so (ℒ_(W*)g)_(vr) = −2r⁻³ − f′/(r(r + r_h)), f′ = 2m₀r⁻³, which is
−¼r_h⁻³ − (1/24)r_h⁻³ at r = 2r_h. ∎

**Corollary {#cor:hr-compact-rates}** (The rates of [[ch:harmonic-structure]] for gauge vectors with compactly
supported data.) Let ε > 0; on each {r_♭ < r ≤ R′, t_* ≥ T′}, with every number of derivatives:

(a) for Y as in [[cor:gd-r4-6]], Y − (Q[Y]/4π²)W* = (Q[Y]/8π²)t_*^(−2)dψ + O(t_*^(−3+ε));

(b) in [[prop:gd-r2-13]] (b), with c = Q[Z′_0]/4π²,

    (ġ_H)_0 = ṁK* + cℒ_(W*)g + (m₀c/2)t_*^(−2)ℒ_(W*)g + O(t_*^(−3+ε));

(c) in the last clause of [[cor:gd-r4-4]], ℒ_(Y_h)g − (Q[Y_h]/4π²)ℒ_(W*)g = (m₀Q[Y_h]/8π²)t_*^(−2)ℒ_(W*)g +
O(t_*^(−3+ε)); so ġ_H + ℒ_(Y_h)g settles to ṁK* + (c_∞ + Q[Y_h]/4π²)ℒ_(W*)g at the rate of ġ_H, for the
representative of [[cor:gd-r4-4]] that of [[thm:harmonic-rate]], and for that of [[thm:gd-r3-4]] that of
[[cor:gd-r5-3]].

*Proof.* (a) and (c) are [[cor:gd-r7-4]] for Y and Y_h. (b): (ġ_H)_0 = ṁK* + ℒ_(Z′_0)g exactly
([[prop:gd-r2-13]] (a)), and [[cor:gd-r7-4]] applies to Z′_0. ∎

### The spherically symmetric part {#sec:hr-l0}

The l = 0 part of a class tensor or 1-form is its SO(4)-average ([[sec:hg-setting]]); Υ̇⁰, □ and X ↦ ℒ_Xg commute
with it, the rotations being isometries of g. Recall X_RW and Y[h_0] of [[thm:rw-settling]], with
h_0 := (ġ − ṁK_V)_0 = ℒ_(Y[h_0])g ([[thm:rw-settling]] (a)) and X_(RW,0) = −Y[h_0]^♭.

**Lemma {#lem:gd-r6-8}** (The spherically symmetric part of the gauge forcing term.) On N⁺ the l = 0 part of F_Y is

    F_(Y,0) = □(X_(RW,0) + ṁ(1 − χ_K)W**_H),        so        J_(h,0) = □X_(RW,0)  on {χ_K = 1}.

*Proof.* F_Y = Υ̇⁰(ġ) − ṁ□(χ_KW**_H) on N⁺ ([[eq:gd-r3-2]]), ġ = ġ_RW − ℒ_(X_RW)g and (ġ_RW)_0 = ṁK_V
([[thm:rw-settling]] (a)). Averaging, Υ̇⁰(ġ)_0 = ṁΥ̇⁰(K_V) + □X_(RW,0) = ṁ□W**_H + □X_(RW,0), so
F_(Y,0) = □X_(RW,0) + ṁ□((1 − χ_K)W**_H). On {χ_K = 1}, F_Y = J_h ([[sec:hg-late]]). ∎

On the cone the spherically symmetric gauge forcing term is therefore □ of a radial 1-form, and X_(RW,0) =
O(t_*^(−(w−1)+ε′)) on compact sets ([[thm:rw-settling]] (c)). The next proposition shows that this part never reaches
the l = 0 part of the representative.

**Proposition {#prop:gd-r7-5}** (The spherically symmetric part is homogeneous.) Let ġ_H = ġ + ℒ_Zg be the
representative of [[cor:gd-r4-4]], Z = ṁχ_KW**_H + Z_1, let Y_0 := Y[h_0]^♭ = −X_(RW,0), and put
Z′_0 := Z_0 + Y_0 − ṁW**_H. Then on N⁺

    (ġ_H)_0 = ṁK* + ℒ_(Z′_0)g,        □Z′_0 = 0,        Z′_0 = Y_0 − ṁW**_H  near Σ°.                    {#eq:gd-r7-4}

For ġ_H + ℒ_(Y_h)g, the clause of [[cor:gd-r4-4]], the same holds with Z′_0 + Y_(h,0) in place of Z′_0.

*Proof.* ġ_0 = ṁK_V + h_0 = ṁK_V + ℒ_(Y_0)g, and averaging commutes with X ↦ ℒ_Xg; so
(ġ_H)_0 = ṁK_V + ℒ_(Y_0+Z_0)g = ṁK* + ℒ_(Z′_0)g, as K* = K_V + ℒ_(W**_H)g ([[prop:np-10-2]] (iv) (c)). Υ̇⁰(ġ_H) = 0
on N⁺ ([[cor:gd-r4-4]]), Υ̇⁰(K*) = 0 and Υ̇⁰(ℒ_Xg) = −□X; so □Z′_0 = −Υ̇⁰((ġ_H)_0) + ṁΥ̇⁰(K*) = 0. Near Σ°,
χ_K = 0 and Z_1 = 0 (the proof of [[cor:gd-r4-4]]), so Z = 0 there. For Y_h, □Y_h = 0 and (ℒ_(Y_h)g)_0 = ℒ_(Y_(h,0))g. ∎

The l = 0 part of Z_1 is −Y_0 + ṁ(1 − χ_K)W**_H + Z′_0: its slow piece −Y_0 cancels against the term ℒ_(Y_0)g of ġ,
and the l = 0 rate of ġ_H is the rate of Z′_0, a solution of □Z′_0 = 0 whose Cauchy data on Σ° are those of
Y_0 − ṁW**_H, fixed by the spherically symmetric part of the initial data. This is the statement
[[prop:gd-2-1]] (c) for this representative.

**Definition {#def:hr-order}** (Data of order p.) Let n be the future unit normal of Σ^IVP. A 1-form Y on N⁺, smooth up
to Σ°, has *data of order p at spatial infinity* if there is a constant c′ such that, near infinity on Σ^IVP, the
Cartesian components of Y − c′(∂_t)^♭ and of ∇_n(Y − c′(∂_t)^♭) are conormal of orders p and p + 1 in |x|⁻¹. c′ is its
*Killing multiple*; it is unique when p > 0. Data that have compact support up to such a multiple have every order.

(∂_t)^♭ = (∂_v)^♭ is the Killing form, with □(∂_t)^♭ = 0, ℒ_((∂_t)^♭)g = 0 and Q[(∂_t)^♭] = 4π²m₀ ([[lem:gd-2-2]] (b)).

**Corollary {#cor:gd-r7-6}** (Homogeneous solutions with data of order p.) Let □Y = 0 on N⁺, with Y smooth up to Σ° and
data of order p ∈ (½, 3/2), with Killing multiple c′. Then Q[Y] is constant, and for every α_K < p with α_K ≠ 1, on
each {r_♭ < r ≤ R′, t_* ≥ T′} and with every number of derivatives,

    |Y − c′(∂_t)^♭ − cW*| ≤ C t_*^(−α_K),        |ℒ_Yg − cℒ_(W*)g| ≤ C t_*^(−α_K),        c := (Q[Y] − 4π²m₀c′)/4π².

*Proof.* Q[Y] is constant by [[eq:gd-2-1]]. Subtract c′(∂_t)^♭, a solution with Q[(∂_t)^♭] = 4π²m₀ and
ℒ_((∂_t)^♭)g = 0; so we may take c′ = 0, and then c = Q[Y]/4π². It suffices to take α_K ∈ [½, p) ∖ {1}. Put
δ := (p − α_K)/5 and

    γ_+ := α_K + δ,   b_+ := α_K + 2δ,   b_I := α_K + 3δ,   p_slab := α_K + 4δ,   β := b_+ − ½,
    α_I := p_slab − 3/2,

so that α_K < γ_+ < b_+ < b_I < p_slab < p < 3/2, β ∈ (0, 1) and α_I < 0. Let τ′ := t_IVP/|x|, as in step (2) of the
proof of [[thm:gd-r4-3]], χ_d ∈ C_c^∞((−1/16, 1/16)) equal to 1 near 0, and Y_d := χ_d(τ′)(y_0 + t_IVP y_1) near
infinity, (y_0, y_1) the data of Y (y_1 the t_IVP-derivative), extended to a smooth 1-form near Σ^IVP with the data of
Y on Σ°. τ′ is a b-time function at I₀ for every weight ([[lem:gd-r4-1]] (d)), so □Y_d is conormal of I₀-order p + 2,
and near infinity it is supported in {|τ′| ≤ 1/16}, away from ℐ⁺.

(1) *The initial slab.* Y − Y_d has vanishing data and solves □(Y − Y_d) = −□Y_d. As ρ_Iρ^(−7/2) = ρ₀^(−7/2)ρ_I^(−5/2)
([[eq:iv2-0-2]]), ρ_Iρ^(−7/2)□Y_d lies in H^(m,(a₀,2α_I))_b for every m, every a₀ < p − 3/2 and every α_I. Fix
a₀ ∈ (α_I, p − 3/2), possible as p_slab < p. [[prop:gd-r4-2]], with α_I < min(a₀, 0), and b-Sobolev embedding as in
step (4) of the proof of [[thm:gd-r4-3]], give the Cartesian components of Y and all their b-derivatives the
ℐ⁺-order α_I + 3/2 = p_slab on N⁺ ∩ {2 ≤ t^♭_* ≤ 3}, Y_d vanishing near ℐ⁺.

(2) *The forward solution.* With χ of [[lem:gd-r3-5]], χ(t^♭_*)Y solves □(χ(t^♭_*)Y) = [□, χ(t^♭_*)]Y, a forcing
term supported in {2 ≤ t^♭_* ≤ 3}, meeting ∂M only at ℐ⁺, of ℐ⁺-order p_slab + 1 (the proof of [[prop:gd-r3-6]]).
With b_+ = β + ½ and b_I ∈ (b_+, p_slab) it lies in the space of [[lem:gd-r3-5]], whose conditions b_+ < b_I < 3/2 hold
for □, which is 1-admissible with sf-weight b_+ − 5/2 ([[thm:gd-r2-5]] (iii), b_+ − ½ = β ∈ (0, 1)). So
χ(t^♭_*)Y is its forward solution ([[thm:ii-f1-1-1]]; uniqueness as in the proof of [[prop:gd-r3-6]]), and
[[cor:ii-f1-1-2]] gives χ(t^♭_*)Y ∈ H^(k,(b_I,b_+,−1/2))_b(Ω_*, μ_b) for every k.

(3) *The cone.* χ′Y is the forward solution of [□, χ′]Y. On the cone part {t_*/40 ≤ r ≤ t_*/20} of supp dχ′,
[□, χ′] ∈ ρ_+²Diff¹_b (the proof of [[thm:gd-r3-4]] (iii)), and that cone stays away from K⁺ and ℐ⁺; the rest of
supp dχ′ is compact. So [□, χ′]Y ∈ H^(∞,(N,b_++2,N))_b for every N. If α_K < 1, it lies in [[eq:gd-r5-1]] with
γ_+ ∈ (α_K, 3/2) and α_K ∈ [½, 1), as γ_+ < b_+; if α_K ∈ (1, 2), it lies in [[eq:gd-r6-1]] with γ_+ ∈ (α_K, 2),
for any ε_1, the forcing term vanishing near ℐ⁺. [[thm:gd-r5-2]], resp. [[thm:gd-r6-5]], gives
|χ′Y − c_f(t_*)W*| ≤ Ct_*^(−α_K). At late times dχ′ = 0 near the horizon, so ℓ of the forcing term vanishes for large v
and c_f = Q[χ′Y]/4π² = Q[Y]/4π², constant. On compact r-sets at late times χ′Y = Y. The metric part:
ℒ_Yg − cℒ_(W*)g = ℒ_(Y−cW*)g, bounded by the derivatives of Y − cW*. ∎

At p = ½ the chain α_K < γ_+ < b_+ < b_I < p_slab < p is empty; for p ≥ 3/2 it stops at 3/2, the a priori ι⁺-weight
b_+ < 3/2 of the forward solution on the slab. For data of compact support [[cor:gd-r7-4]] is better.

**Corollary {#cor:gd-r7-7}** (The spherically symmetric rate.) Let ġ_H be the representative of [[cor:gd-r4-4]] for
data (γ̇, k̇) in the class of [[cor:viii-2-3]], let q := min(min Re ℰ_0, ℓ_0, 2), so that q > 3/2 + 2γ_Υ
([[sec:iii-k-0]]: min Re ℰ_0 > 3/2 + 2γ_Υ and ℓ_0 > 3; and γ_Υ < ¼), and let c′ be the Killing multiple of the data of
Z′_0 ([[eq:gd-r7-4]]) and c := (Q[Z′_0] − 4π²m₀c′)/4π².

(a) Z′_0 has data of order p for every p < q − 1. Let p_0 be the supremum of the orders of its data; so
p_0 ≥ q − 1 > ½ + 2γ_Υ > ½ + δ_♯. Then (ġ_H)_0 − ṁK* − cℒ_(W*)g = O(t_*^(−α)) on compact sets, with every derivative,
for every α < min(p_0, 3/2) with α ≠ 1. In particular the spherically symmetric part of every perturbation in the class
settles faster than t_*^(−1/2−δ_♯).

(b) Suppose that outside a ball (γ̇, k̇) are ṁ times the data of K_V, as for the data of [[thm:settling]], glued to
exact Tangherlini data beyond a ball ([[ch:after-shell]]). Then Z′_0 = ṁZ^(K) + Z_c + c″(∂_t)^♭, where Z_c solves
□Z_c = 0 with data of compact support, c″ is a constant, and Z^(K) is one solution of □Z^(K) = 0, independent of the
perturbation, with data of order exactly 1. So (ġ_H)_0 − ṁK* − cℒ_(W*)g = O(t_*^(−1+ε)) for every ε > 0. If ṁ = 0, as
for data with compact support, then

    (ġ_H)_0 − cℒ_(W*)g = (m₀c/2) t_*^(−2) ℒ_(W*)g + O(t_*^(−3+ε)).

*Proof.* (a) Near Σ°, Z′_0 = Y_0 − ṁW**_H ([[eq:gd-r7-4]]). Y_0 = ζ(∂_v)^♭ + rH_L dv, with d ζ = 𝔷 algebraic in h_0
and the first derivatives of H_L ([[lem:gd-1-4]] (b)). In the class S′ = 0 ([[cor:viii-2-3]]), so ġ = ḣ near Σ°
([[thm:viii-2-2]] (2)), whose data ḣ_0 and ḣ_1 = rℒ_(∂_(t_IVP))ḣ lie in H^(∞,(ℰ_0,ℓ_0))_b(Σ^IVP)
([[lem:viii-1-1]]); and K_V ∈ |x|⁻²C^∞ is stationary ([[eq:iii-b-3-7]]). So along Σ^IVP near infinity the components
of h_0 and of its normal derivative are conormal of every order below q, resp. q + 1. Hence 𝔷 is conormal of every order
below q and rH_L of every order below q − 1; ζ has a limit ζ_∞ at infinity along Σ^IVP, with ζ − ζ_∞ of every order
below q − 1; and ∇Y_0 is of every order below q. So Y_0 has data of every order below q − 1,
with Killing multiple ζ_∞. W**_H has data of order 1 with no Killing part: near infinity on Σ^IVP = {t = C″}
([[lem:iii-b-3-9]]), v = |x| + O(1); from [[eq:np-10-2]], A = 1/(2r) + O(r⁻²) and B = −1/(4r) + O(r⁻² log r);
dv = dt + ((2 − f)/f)d|x| ([[eq:iii-b-4-2]]) and W* = r⁻²dt + O(r⁻³)d|x|; and V = −(∂_mT_m)∂_t ([[eq:gd-0-1]]) with
T_m(|x|) = 2|x| − 2r_*, so ∂_mT_m = 2/|x| + O(|x|⁻³) and V^♭ = (2/|x|)dt + O(|x|⁻³). So

    W**_H = −dt/|x| + d|x|/(4|x|) + O(|x|⁻² log|x|),        ∂_tW**_H = ½W* = O(|x|⁻²),

with conormal components (A and B are analytic in r with logarithmic terms at infinity). As q − 1 ≤ 1, Z′_0 has data of
every order below q − 1, with Killing multiple c′ = ζ_∞; and q − 1 > ½ + 2γ_Υ ≥ ½ + 2δ_♯. [[cor:gd-r7-6]] for Z′_0,
at every p < min(p_0, 3/2), with [[eq:gd-r7-4]], gives the rate.

(b) The data (ḣ_0, ḣ_1) of [[lem:viii-1-1]] are determined at each point by linear algebraic equations in (γ̇, k̇) and
finitely many of their derivatives; so outside a ball they are ṁ times those of the initial solution ḣ^(K) of
[[prop:viii-1-2]] for the data of K_V, and ḣ − ṁḣ^(K) has data of compact support. It solves L^♮(ḣ − ṁḣ^(K)) = 0, an
equation whose principal part is ½□_g ⊗ id; so it vanishes on the Cauchy development ℰ, in the interior of 𝒟, of the
part of Σ° outside a large ball ([[thm:std-bgp-development]], [[thm:std-bgp-cauchy]] (3)). ḣ^(K) induces the data of
K_V ([[lem:viii-1-1]] (1)), so k := ḣ^(K) − K_V induces zero data, with DRic(k) = 0. By [[thm:ix-2-2]] and Step 1 of
its proof (with Z = 0 and U := U^♯ ∩ {t_IVP < 1}, so that Ω′_+ ⊂ 𝒟), k = ℒ_(Y_K)g near Σ°, with Y_K = 0 on Σ° and
∇_nY_K^♭ = k(n, ·) + ½k(n, n)n^♭ = −K_V(n, ·) − ½K_V(n, n)n^♭ there, as ḣ^(K)(n, ·) = 0 on Σ^IVP
([[lem:viii-1-1]]); averaging over SO(4), we take Y_K spherically symmetric. Near infinity on Σ^IVP,
K_V = |x|⁻²(dt − d|x|)² ([[sec:hg-exterior]]), so ∇_nY_K is conormal of order 2: Y_K has data of order 1 and no Killing
part. On ℰ, h_0 = (ḣ − ṁK_V)_0 = ṁk = ℒ_(ṁY_K)g, so ℒ_(Y_0−ṁY_K)g = 0: Y_0 − ṁY_K is a spherically symmetric Killing
field on ℰ, whose orbit space is connected, so it equals c″(∂_v)^♭ ([[lem:gd-1-4]] (c)). Let Z^(K) be the solution of
□Z^(K) = 0 on N⁺ with the data of Y_K − W**_H on Σ° ([[lem:ix-1-1]], [[lem:gd-r3-1]]); its data have order 1, and
exactly 1, as the term −dt/|x| + d|x|/(4|x|) of W**_H is removed neither by a multiple of (∂_t)^♭, of order 0, nor by
anything of order above 1. Then Z_c := Z′_0 − ṁZ^(K) − c″(∂_t)^♭ solves □Z_c = 0, with data of compact support.
[[cor:gd-r7-6]] for Z^(K) at every p < 1 and [[cor:gd-r7-4]] for Z_c give the rate t_*^(−1+ε), the Killing part
dropping out of the metric. If ṁ = 0: then Z′_0 = Y_0 near Σ°, h_0 vanishes outside the domain of influence of a ball,
so 𝔷 = 0 there and Y_0 = ζ_∞(∂_v)^♭ near infinity on Σ°; [[cor:gd-r7-4]] applied to Z′_0 − ζ_∞(∂_t)^♭ gives the last
display, with c = (Q[Z′_0] − 4π²m₀ζ_∞)/4π². For data with compact support, ġ_0 = 0 near Σ° outside a ball, and
δm[ġ_0] = ṁδm[K_V] + δm[h_0] = ṁ ([[lem:gd-1-4]] (a), [[thm:rw-settling]] (a)) is constant on the simply connected
orbit space of the interior of N⁺ ([[lem:gd-1-4]] (b)); so ṁ = 0. ∎

### The 1-forms with no part of degree l ≤ 1 {#sec:hr-subspace}

On all 1-forms the window of [[thm:gd-r6-4]] cannot be lowered: the indicial root 0 of the l = 0 forms bounds it from
below, and at negative weights the zero-energy kernel contains W* and (∂_v)^♭. On the 1-forms with no part of degree
l ≤ 1 neither obstruction occurs. This section proves the low-energy hypotheses (G), (Z) and (TF) of [[sec:i-c-1-2]] on
that subspace, at every b-weight of (−1, 3).

*Setting.* As in [[sec:iii-d1-1]] at 𝗉_0: P̂(σ) is the spectral family of □ = dδ + δd at b₀, with (H1)–(H5),
ϑ_ℋ = 1, index 0 at σ ≠ 0, and P̂(σ) invertible for every σ ≠ 0 with Im σ ≥ 0 ([[prop:iii-d-6-2]]); the spaces 𝒳_0,
𝒴_0 and 𝒳^*_0 of [[eq:i-c-3-1]], 𝒳_σ and 𝒴_σ of [[eq:i-c-6-4]], the tf spaces of [[sec:i-c-4-3]], a constant
s > 5/2, and the frame dt_*, dx¹, …, dx⁴ of [[ch:s01]], the *Cartesian frame*. On stationary 1-forms P̂(0) = □,
computed in the ingoing chart, as t_* − v is a function of r. A 1-form on {r = c} decomposes into its dt_* and dr
components and its angular part, and by [[lem:iii-a1-1-6]] a 1-form is a sum of *scalar types of degree l*,
aS dt_* + bS dr + c dS with S ∈ 𝒮_l, l ≥ 0, and *vector types of degree l*, ψY with Y ∈ 𝒱_l, l ≥ 1, the coefficients
functions of r (of (t_*, r) on spacetime).

**Definition {#def:gd-r8-1}** (The projections.) O(4) acts on X by x ↦ gx, isometries of g that fix t, r and t_*, and on
1-forms by T_gu := (g⁻¹)^*u; in the Cartesian frame (T_gu)(x) = A_gu(g⁻¹x) with the constant orthogonal matrix
A_g = diag(1, g). For an irreducible representation τ of SO(4) with character χ_τ put

    P_τ := dim τ ∫_(SO(4)) χ̄_τ(g) T_g dg        (Haar probability measure).

Let τ_0 be the trivial representation, τ_1 the standard one on ℂ⁴, and τ_± those on the self-dual and anti-self-dual
2-forms Λ²_±ℂ⁴, so that Λ²ℂ⁴ = τ_+ ⊕ τ_−. Put

    Π_(≥2) := 1 − P_(τ_0) − P_(τ_1) − P_(τ_+) − P_(τ_−),        Π_0 := P_(τ_0),        Π_G := ∫_G T_g dg,
    Π_cl := Π_G(1 − Π_0),

G = O(2) × O(2) the group of the class. Π_0 is the SO(4)-average, the l = 0 part of [[sec:hg-setting]]. Below Π is
either Π_(≥2) or Π_cl, and h is an O(4)-invariant fibre inner product equal to the identity in the Cartesian frame at
∂X (average any admissible choice over O(4)).

**Lemma {#lem:gd-r8-2}** (The projections.)

(a) Π is a projection; it commutes with P̂(σ), P̂(σ)^(*h), multiplication by functions of r, ρ∂_ρ, the dilations S_ς of
[[sec:i-c-6]], N(P⁽⁰⁾), I(ι), N_tf(σ̂) and its adjoint, and the Mellin transform of [[sec:i-c-2-3]]; and Π^(*h) = Π.

(b) Π and 1 − Π are bounded, uniformly in ς, on every space of [[ch:s01]] and [[ch:s03]] (H̄^s, Ḣ^s, H^s_(b,c),
H̄^(s,a)_b, 𝒳_0, 𝒴_0, 𝒳^*_0, the scattering spaces with the decay orders of [[sec:i-c-4-3]] and [[sec:i-c-6-1]], the
spaces of [[def:i-c-4-1]] and [[def:i-c-6-1]], 𝒳_σ, 𝒴_σ, 𝒳^*_σ and the tf spaces), so ran Π is closed in each. On M′,
Π is bounded on every H^(k,(w_I,w_ι,w_K))_b and commutes with □, with the cut-offs that are functions of (t_*, r), and
with the forward solution operator of [[thm:ii-f1-1-1]].

(c) ℓ ∘ Π = 0.

(d) For u ∈ ran Π, every component of u in the Cartesian frame has zero mean on every sphere {r = c}.

(e) ran Π_(≥2) lies in the closed span of the scalar and vector types of degrees l ≥ 2. ran Π_cl is the space of class
1-forms with no l = 0 part, and lies in the closed span of the scalar types of even degrees l ≥ 2.

*Proof.* (a) Each T_g, g ∈ O(4), commutes with the operators listed: g is an isometry of g fixing t_* and r, it
preserves |dx| and the Laplacian of 𝕊³, and h is invariant; the restrictions to ρ = 0, the Mellin transform in ρ and
the conjugation by e^(iσ̂r̂) that define N(P⁽⁰⁾), I(ι) and N_tf commute with maps that fix ρ and r̂. The averages
inherit this, a bounded operator commuting with a Bochner integral. P_τP_σ = δ_(τσ)P_τ is the orthogonality of the
characters of a compact group, for every strongly continuous representation; so Π_(≥2), one minus four mutually
orthogonal P_τ, is a projection. Conjugation by g ∈ O(4) maps P_τ to P_(τ^g), τ^g(h) := τ(g⁻¹hg); τ_0 and τ_1 are
invariant under it, and τ_+, τ_− are exchanged when det g = −1; so every T_g, g ∈ O(4), commutes with Π_(≥2) and with
Π_0. Hence Π_G commutes with Π_0, and Π_cl is a projection. T_g^(*h) = T_(g⁻¹), χ_τ(g⁻¹) = χ̄_τ(g) and the Haar measures
are inversion-invariant, so P_τ^(*h) = P_τ, Π_G^(*h) = Π_G, and Π^(*h) = Π.

(b) Let E be one of the spaces listed. On the b-Sobolev spaces the weights are functions of |x|, or of (t_*, r) on M′,
and T_g is an isometry. On the scattering spaces with variable decay order the norm is ‖Au‖ + ‖u‖_(−N) for an elliptic
A of that order; T_g⁻¹AT_g is elliptic of the same order, which is a function of ξ and |η|², hence rotation- and
reflection-invariant ([[sec:i-c-4-3]]), and it depends continuously on g in the calculus; as O(4) is compact,
C_E := sup_g‖T_g‖_(E→E) < ∞. With this uniform bound, the density of C_c^∞ (or of Schwartz sections) gives the strong
continuity of g ↦ T_gu on E by an ε/3 argument. For a graph-norm space 𝒳 = {u ∈ H : Pu ∈ Y},
‖u‖_𝒳 = ‖u‖_H + ‖Pu‖_Y, with H and Y base spaces and P commuting with every T_g (by (a)), T_g𝒳 ⊂ 𝒳 with
‖T_g‖_𝒳 ≤ max(C_H, C_Y), and ‖T_gu − u‖_𝒳 = ‖T_gu − u‖_H + ‖T_g(Pu) − Pu‖_Y → 0 as g → e; this covers 𝒳_0, 𝒳_σ,
𝒳^*_0, 𝒳^*_σ and the tf domains. So each average is a Bochner integral of a continuous bounded E-valued function, with
‖P_τ‖ ≤ (dim τ)²C_E, ‖Π_G‖ ≤ C_E, ‖Π_(≥2)‖ ≤ 1 + (1 + 16 + 9 + 9)C_E and ‖Π_cl‖ ≤ C_E(1 + C_E); and S_ς commutes with
every T_g, so the bounds are uniform in ς. On M′ the weights are functions of (t_*, r), □ is natural under isometries,
and the forward solution is unique with an O(4)-invariant support condition, so it commutes with each T_g.

(c) ℓ(u) = r_h³∫_(𝕊³) u(∂_(t_*))|_(r=r_h) dω, and ∂_(t_*) and dω are O(4)-invariant; so ℓ = ℓ ∘ Π_0. Π_0Π_(≥2) = 0 by the
orthogonality of characters, and Π_0Π_cl = Π_GΠ_0(1 − Π_0) = 0.

(d) For Π_(≥2): the map u ↦ (∫_(𝕊³) u_μ(cω) dω)_μ, the means of the components in the Cartesian frame, is
SO(4)-equivariant into ℂ ⊕ ℂ⁴, on which SO(4) acts by τ_0 ⊕ τ_1; by Schur's lemma it commutes the projections P_τ with
their counterparts on ℂ ⊕ ℂ⁴, and so vanishes on ran Π_(≥2). For Π_cl: G contains each reflection x_i ↦ −x_i, so the
spatial Cartesian components of a class 1-form are odd under it and have zero mean, and the mean of its time component
is the time component of its l = 0 part, which vanishes on ran Π_cl.

(e) The projections onto a type and a degree commute with every T_g, g ∈ O(4), as the isometries of 𝕊³ commute with
d, δ and the Laplacian and preserve 𝒮_l and 𝒱_l; so Π maps each type and degree into itself. The scalar type of degree
0 is SO(4)-invariant, so it lies in ran P_(τ_0). On the scalar type of degree 1, SO(4) acts through 𝒮_1, the
restrictions of the linear functions ⟨a, x⟩/r ([[lem:iii-a1-1-4]] (1)), by a ↦ ga, that is by τ_1. On 𝒱_1, the duals
of the Killing fields Ω_A, A ∈ 𝔰𝔬(4) ([[lem:iii-a1-1-4]] (2)), it acts by T_gΩ_A^♭ = Ω_(gAg⁻¹)^♭, the adjoint
representation 𝔰𝔬(4) ≅ Λ²ℂ⁴ = τ_+ ⊕ τ_−. So Π_(≥2) vanishes on the types of degree ≤ 1, and the first claim follows from
[[lem:iii-a1-1-6]]. Π_G is the identity on class 1-forms and Π_cl u = u − Π_0u for them; a 1-form u with Π_cl u = u is
G-invariant and has Π_0u = Π_GΠ_0(1 − Π_0)u = 0. The class 1-forms are sums over even l of scalar types
([[lem:gd-1-2]] (a), (c)), and those with no l = 0 part have l ≥ 2. ∎

**Lemma {#lem:gd-r8-3}** ((G) on the subspace.)

(a) (*The radial systems.*) Let κ := l(l + 2). On ω = aS dv + bS dr + c dS, S ∈ 𝒮_l, a, b, c functions of r,
P̂(0)ω = E_vS dv + E_rS dr + E_θ dS with

    r³E_v = −[r(r² − m₀)a″ + 3(r² − m₀)a′ − κra],
    r⁴E_r = −[r²(r² − m₀)b″ + (3r³ + m₀r)b′ − (κr² + 3r² − 3m₀)b + 2κrc − 3r²a],
    r³E_θ = −[r(r² − m₀)c″ + (r² + m₀)c′ − κrc + 2r²a + 2(r² − m₀)b],                                    {#eq:gd-r8-1}

and δω = −r⁻³[(r³a)′ + (r³fb)′ − κrc]S. On ω = ψY, Y ∈ 𝒱_l, ψ a function of r and Λ_l := (l + 1)²,
P̂(0)ω = −r⁻²[r(rfψ′)′ − Λ_lψ]Y. The types do not couple.

(b) (*The roots.*) In the Cartesian frame the indicial roots of the scalar type of degree l are
{−l − 1, −l, 1 − l, l + 1, l + 2, l + 3}, and those of the vector type of degree l are {−l, l + 2}.

(c) (*The gap.*) Let Π_∂ be the action of Π on C^∞(𝕊³; ℂ⁵), and spec^Π_b := {ι : ker I(ι) ∩ ran Π_∂ ≠ 0}. Then
spec^Π_b ⊂ (−∞, −1] ∪ [3, ∞), so (−1, 3) is an indicial gap of the restricted operator, for both projections and
uniformly in l: every scalar root of degree l ≥ 2 is ≤ 1 − l ≤ −1 or ≥ l + 1 ≥ 3, and every vector root of degree
l ≥ 2 is ≤ −l ≤ −2 or ≥ l + 2 ≥ 4. The ends −1 and 3 are roots of the scalar type of degree 2. On all 1-forms the roots
0 (of degree 0 and of the scalar type of degree 1) and 2 lie in (−1, 3), and the gaps there are (−1, 0), (0, 2) and
(2, 3).

*Proof.* (a) In the ingoing chart |det g|^(1/2) = r³γ^(1/2), g^(vv) = 0, g^(vr) = 1, g^(rr) = f, g^(ij) = r⁻²γ^(ij), and
Δ̂S = −κS. So ω^v = bS, ω^r = (a + fb)S, ω^i = r⁻²cγ^(ij)∂_jS, and δω = −|det g|^(−1/2)∂_μ(|det g|^(1/2)ω^μ) is the
stated formula; write δω = 𝒹S. For F := dω, F_(vr) = −a′S, F_(vi) = −a∂_iS, F_(ri) = e∂_iS with e := c′ − b, and
F_(ij) = 0; raising, F^(vr) = a′S, F^(vi) = r⁻²eγ^(ij)∂_jS and F^(ri) = r⁻²(fe − a)γ^(ij)∂_jS. With
(δF)^ν = −|det g|^(−1/2)∂_μ(|det g|^(1/2)F^(μν)),

    (δF)^v = (r⁻³(r³a′)′ − κr⁻²e)S,    (δF)^r = κr⁻²(a − fe)S,    (δF)^i = −r⁻³(r(fe − a))′γ^(ij)∂_jS,

and lowering with g_(vv) = −f, g_(vr) = 1, g_(ij) = r²γ_(ij) gives (δF)_v = (−fr⁻³(r³a′)′ + κr⁻²a)S,
(δF)_r = (r⁻³(r³a′)′ − κr⁻²e)S and (δF)_i = r⁻¹(r(a − fe))′∂_iS. As P̂(0)ω = dδω + δdω on stationary ω,
E_v = −fr⁻³(r³a′)′ + κr⁻²a, E_r = 𝒹′ + r⁻³(r³a′)′ − κr⁻²e and E_θ = 𝒹 + r⁻¹(r(a − fe))′, which with r³f = r(r² − m₀)
multiply out to [[eq:gd-r8-1]]. For ψY, δ(ψY) = r⁻²ψδ̸Y = 0, d(ψY) has the components ψ′Y_i and ψ(d̸Y)_(ij), and the
same calculation gives (δd(ψY))_v = (δd(ψY))_r = 0 and the stated angular part, with δ̸d̸Y = Λ_lY
([[lem:iii-a1-1-4]] (2)). Each formula maps a type and degree to itself.

(b) This is [[lem:iii-d-4-1]] at z = 0, the parameter value γ_Υ = 0 at which the operator there is □: its roots of type
sl are 1 − (l + 2), 1 − (l + 1), 1 − l, l + 1, l + 2, l + 3, those of type vl are −l and l + 2, and those of type s0 are
−1, 0, 2, 3. (They are the roots −m and m + 2 of the Cartesian components of degree m ∈ {l − 1, l, l + 1}, resp. m = l,
under the flat Laplacian, [[lem:iii-a1-2-3]].)

(c) I(ι) commutes with the rotations and with Π_∂ ([[lem:gd-r8-2]] (a)), and preserves each type and degree, on which it
is the indicial family of that type. By [[lem:gd-r8-2]] (e), an element of ker I(ι) ∩ ran Π_∂ is a sum of components of
types of degree l ≥ 2 (for Π_cl: scalar, of even degree), each in ker I(ι); so ι is a root of such a type, and (b)
gives the bounds. On all 1-forms the roots of types s0 and s1 are {−1, 0, 2, 3} and {−2, −1, 0, 2, 3, 4}, and of type v1
{−1, 3}. ∎

**Lemma {#lem:gd-r8-4}** (No kernel at negative weights.) Let β ∈ (−1, 0) and let u be a stationary 1-form on X, smooth
up to ∂_♯X (so across the horizon), in 𝒜^β near ∂X (conormal, |u| = O(r^(−β)) in the Cartesian frame, with all its
b-derivatives), with P̂(0)u = 0, whose expansion in types and degrees ([[lem:iii-a1-1-6]]) has no component of degree
l ≤ 1 (for instance u ∈ ran Π, by [[lem:gd-r8-2]] (e)). Then u = 0.

*Proof.* We follow the proof of [[lem:iii-d1-2-1]] (2), with the growth at infinity excluded mode by mode. Expand u in
types and degrees ([[lem:iii-a1-1-6]]; the projections act in the angles and preserve smoothness at r_h in the ingoing
chart and the conormal bounds); only degrees l ≥ 2 occur. Let κ := l(l + 2) and ρ := 1/r.

*(a) The divergence.* φ := δu is smooth, stationary and in 𝒜^(β+1) near infinity, and δdφ = δ(P̂(0)u) = 0, as
δ□ = δdδ = □_0δ. Its degree-l component solves (r³fφ_l′)′ = κrφ_l. At r = ∞ this equation has a regular singular point
with the indicial roots ρ^(l+2) and ρ^(−l) (the proof of [[lem:iii-d1-2-1]] (2) (c)); φ_l = O(r^(−β−1)) with
β + 1 > 0 excludes ρ^(−l) for every l ≥ 0, so φ_l = O(r^(−l−2)) and φ_l′ = O(r^(−l−3)). On [r_1, R] ⊂ (r_h, ∞),
[r³fφ_l′φ̄_l]_(r_1)^R = ∫_(r_1)^R (r³f|φ_l′|² + κr|φ_l|²) dr, and the bracket tends to 0 as r_1 → r_h (f → 0) and as
R → ∞. So φ_l = 0: δu = 0 on {r > r_h}.

*(b) The field.* F := du ∈ 𝒜^(β+1) has δF = P̂(0)u − dδu = 0 on {r > r_h}. *Vector type.* A component r^(−1/2)Φ(r)Y,
Y ∈ 𝒱_l, of u has −Φ_** + V_1Φ = 0 with V_1 > 0 ([[prop:np-10-16]] (iii), (v) at σ = 0, Λ = (l + 1)² ≥ 9). Φ is smooth
in r at r_h, and Φ = O(r^(3/2−β)), as |Y| is r⁻¹ in the Euclidean metric. The equation has a regular singular point at
r = ∞, where r^(−1/2)Φ grows like r^(l+1) or decays like r^(−l−1), as V_1 = ((l + 1)² − ¼)r⁻² + O(r⁻⁴); as
l + 1 > 1 − β, the first is excluded, so
Φ = O(r^(−l−1/2)) and Φ_* = fΦ′ = O(r^(−l−3/2)). The energy identity of the proof of [[lem:iii-d1-2-1]] (2),
∫(|Φ_*|² + V_1|Φ|²) dr_* = [Φ_*Φ̄], whose end terms vanish, gives Φ = 0. *Scalar type.* With W := r³F_tr,
R[W] = (r²M_t)′ = 0 (M = δdu = 0), and Φ := r^(−1/2)W solves −Φ_** + V_2Φ = 0 with V_2 > 0 for κ ≥ 3
([[prop:np-10-16]] (iv)–(v)). F_tr = F_vr is smooth at r_h, and W = O(r^(2−β)). R[W] = 0 has a regular singular
point at r = ∞, with the indicial roots W ∼ r^(l+2) and W ∼ r^(−l); as l + 2 > 2 − β, W = O(r^(−l)), so
Φ = O(r^(−l−1/2)), Φ_* = O(r^(−l−3/2)), and the energy identity gives Φ = 0. So F_tr = 0, and with M = 0
[[prop:np-10-16]] (iv) gives a = b = 0 for the gauge-invariant pair there: each scalar component of u is d(c_lS) on
{r > r_h}, for a function c_l of r.

*(c) The gauge.* So u = Σ_(l≥2) d(c_lS_l) on {r > r_h}, and δu = 0 gives (r³fc_l′)′ = κrc_l. c_l dS has size |c_l|/r
in the Cartesian frame, so c_l = O(r^(1−β)). At r = ∞ the indicial roots are r^l and r^(−l−2), and r^l is excluded as
l > 1 − β, which holds for l ≥ 2 as β > −1. So c_l = O(r^(−l−2)), and the energy identity of (a) gives c_l = 0. So
u = 0 on {r > r_h}.

*(d) Inside the horizon.* u is smooth across r_h, in ker P̂(0), and vanishes on {r > r_h}; part (d) of the proof of
[[prop:iii-d-6-2]], which uses only these properties (at σ = 0, as in [[lem:iii-d1-2-1]] (2) (d)), gives u = 0 on
{r_♭ < r < r_h}. ∎

At degree l = 1, (c) fails: the solution r^l of the gauge equation is admitted by the weights of (−1, 0). The four
1-forms d(φ_1S), S ∈ 𝒮_1, lie in the kernel on all 1-forms at those weights, φ_1 being the solution of
(r³fφ′)′ = 3rφ that is smooth at r_h (where the equation has the double indicial root 0); it cannot decay, by the energy
identity of (a), so it grows like r. At degree 0, W* and (∂_v)^♭ lie in the kernel.

**Lemma {#lem:hr-split}** (Fredholm operators and commuting projections.) Let T : X → Y be a bounded Fredholm operator
between Banach spaces, and Π_X, Π_Y bounded projections with TΠ_X = Π_YT. Then T_1 := T|_(ran Π_X) : ran Π_X → ran Π_Y
and T_2 := T|_(ker Π_X) : ker Π_X → ker Π_Y are Fredholm, ind T = ind T_1 + ind T_2, ker T_1 = ker T ∩ ran Π_X and
ran T_1 = ran T ∩ ran Π_Y.

*Proof.* X = X_1 ⊕ X_2 and Y = Y_1 ⊕ Y_2 with X_1 = ran Π_X, X_2 = ker Π_X and likewise for Y, closed and complementary.
T maps X_i into Y_i, as TΠ_X = Π_YT; so T = T_1 ⊕ T_2 and ker T = ker T_1 ⊕ ker T_2, both finite-dimensional. If
y ∈ ran T ∩ Y_1, y = T_1x_1 + T_2x_2 with T_2x_2 ∈ Y_2, so T_2x_2 = 0 and y = T_1x_1: ran T_1 = ran T ∩ Y_1, which is
closed, and likewise ran T_2. Y_i/ran T_i → Y/ran T is injective, and Y/ran T ≅ Y_1/ran T_1 ⊕ Y_2/ran T_2; so the
cokernels are finite-dimensional and the indices add. ∎

**Proposition {#prop:gd-r8-5}** ((Z) on the subspace.) For every α with α + 2 ∈ (−1, 0) ∪ (0, 2),
P̂(0) : 𝒳_0 ∩ ran Π → 𝒴_0 ∩ ran Π is invertible, at every regularity s > 5/2. By [[thm:gd-r8-7]] (b) the same holds at
every α with α + 2 ∈ (−1, 3).

*Proof.* *Fredholm.* α + 2 lies in a gap of the full bundle, (−1, 0) or (0, 2) ([[lem:gd-r8-3]] (c)), so
[[thm:i-c-3-1]] (1) makes P̂(0) : 𝒳_0 → 𝒴_0 Fredholm. Π is bounded on 𝒴_0, and on 𝒳_0 with its graph norm, as
‖Πu‖ + ‖P̂(0)Πu‖ = ‖Πu‖ + ‖ΠP̂(0)u‖ ≤ C(‖u‖ + ‖P̂(0)u‖); and it commutes with P̂(0) ([[lem:gd-r8-2]]). By
[[lem:hr-split]] the restriction is Fredholm, with ker = ker P̂(0) ∩ ran Π.

*Kernel.* At α + 2 ∈ (0, 2) the kernel is span{W*} ([[lem:iii-d1-2-1]] (2)), and ΠW* = 0, W* being SO(4)-invariant. At
α + 2 ∈ (−1, 0), a kernel element is smooth up to ∂_♯X and lies in 𝒜^(α+2) near ∂X ([[thm:i-c-3-1]] (2) at the gap
(−1, 0), [[lem:i-c-2-9]] (c)), so [[lem:gd-r8-4]] with β = α + 2 applies, by [[lem:gd-r8-2]] (e).

*Cokernel.* Let w be a bounded functional on 𝒴_0 ∩ ran Π that annihilates the restricted range, and v := w ∘ Π on
𝒴_0, so that v ∘ Π = v. v annihilates P̂(0)𝒳_0, as ΠP̂(0) = P̂(0)Π. At α + 2 ∈ (0, 2), v = cℓ ([[lem:iii-d1-2-1]] (3)),
and v = v ∘ Π = cℓ ∘ Π = 0 ([[lem:gd-r8-2]] (c)); so w = 0. At α + 2 ∈ (−1, 0): fix α′ with α′ + 2 ∈ (0, 2).
𝒳_0(α′) ⊂ 𝒳_0(α) and 𝒴_0(α′) ↪ 𝒴_0(α) continuously, so v|_(𝒴_0(α′)) annihilates P̂(0)𝒳_0(α′), hence equals cℓ there,
and so vanishes there, as v = v ∘ Π; so w vanishes on 𝒴_0(α′) ∩ ran Π. This is dense in 𝒴_0(α) ∩ ran Π: if d_n → y in
𝒴_0(α) with d_n smooth and vanishing for large r ([[lem:i-c-2-2]] (d)), then Πd_n → Πy = y, and Πd_n is again smooth and
vanishes for large r, so lies in 𝒴_0(α′).

*Invertibility.* Kernel and cokernel are trivial at each s > 5/2 by the same arguments ([[lem:iii-d1-2-1]] holds at each
such s, [[sec:iii-d1-1]]), and the inverse is bounded by the open mapping theorem. ∎

**Proposition {#prop:gd-r8-6}** ((TF) on the subspace.) Let β ∈ (−1, 0) ∪ (0, 2). Then [[def:i-c-5-1]] holds on ran Π
with the weight β: (i) β lies in the gap (−1, 3) of spec^Π_b; (ii) N_tf(e^(iθ)) is injective on 𝒳_(tf,θ) ∩ ran Π for
every θ ∈ [0, π]; (iii) N_tf(1)^(*h) is injective on 𝒳^*_(tf,0) ∩ ran Π. By [[thm:gd-r8-7]] (b) the same holds for every
β ∈ (−1, 3).

*Proof.* (i) is [[lem:gd-r8-3]] (c). The transition-face data of P̂ are those of the model: in the Cartesian frame
S_0 = 0, N(P⁽⁰⁾) = (−(ρ∂_ρ)² + 2ρ∂_ρ + Δ_(𝕊³))Id and H_0 = Id (the proof of [[lem:iii-d-7-1]] at γ_Υ = 0). So
N_tf(σ̂) = e^(−iσ̂r̂)(Δ_e − σ̂²)e^(iσ̂r̂) on each component (the proof of [[prop:i-c-5-3]]), and on the part of degree
ℓ in ω each component solves the equation of [[lem:i-c-5-4]] (a). Π commutes with N_tf and with the projections Π_ℓ of the
proof of [[prop:i-c-5-3]], and on ran Π every component has degrees ℓ ≥ 1 only ([[lem:gd-r8-2]] (d)).

(ii) The argument of (ii) in the proof of [[prop:i-c-5-3]], with [[thm:i-c-4-3]] (5) applied at the gap of the full
bundle that contains β, (−1, 0) or (0, 2) (its part at sctf uses no gap): a kernel element lies in
𝒜^(3/2−ε,−β′)(tf) for every β′ in that gap, so its components are O(r̂^(−β′)) at ztf with β′ < 2. In each component and
degree ℓ ≥ 1 one Hankel coefficient remains, of size at least cr̂^(−2−ℓ) at ztf ([[lem:i-c-5-4]] (d)) unless it
vanishes; as 2 + ℓ > β′, it vanishes.

(iii) The argument of (iii) in the proof of [[prop:i-c-5-3]]: at sctf the coefficients a_(1m) vanish, by the same
argument, which uses no gap; at ztf the remaining term has size at least cr̂^(−2−ℓ), while 𝒳^*_(tf,0) has the b-weight
−q there, q = 2 − β, so it would need ∫_0 r̂^(2(q−2−ℓ)) dr̂/r̂ < ∞, that is q > 2 + ℓ ≥ 3, which is false as β > −1. ∎

The argument of (iii) uses ℓ ≥ 1: at ℓ = 0 its condition at ztf, q > 2, holds for every β < 0.

Write P_Π(σ) for P̂(σ) on the spaces of [[ch:s03]] intersected with ran Π, and its adjoint on the dual spaces
intersected with ran Π (Π^(*h) = Π), and read (G) for spec^Π_b and [[def:i-c-5-1]] on ran Π, as in [[prop:gd-r8-6]].

**Lemma {#lem:gd-r8-8}** (The Mellin families on the subspace.) Let J be one of the Mellin families of [[ch:s03]]: I(ι)
(the end at infinity), I(−ι) (at ztf, [[sec:i-c-4-1]]), I^♯(ι) of [[eq:i-c-3-5]], and the adjoint family of ztf,
H_0⁻¹I(ῑ + 2)^†H_0. Each commutes with Π_∂. Put spec^Π_J := {ι : ker J(ι) ∩ ran Π_∂ ≠ 0}. Then [[lem:i-c-2-4]] (a)–(c)
hold for J restricted to ran Π_∂, with spec^Π_J in place of spec_J, and [[lem:i-c-2-6]] and [[lem:i-c-2-7]] hold for
every v with Πv = v, with spec_J replaced by spec^Π_J.

*Proof.* H_0 = Id is invariant, so the families commute with Π_∂ ([[lem:gd-r8-2]] (a)). Fix m and put
E_m := ran Π_∂ ∩ H^m(𝕊³; ℂ⁵), closed in H^m as Π_∂ is bounded there ([[lem:gd-r8-2]] (b)).

1. The proof of [[lem:i-c-2-4]] (b) writes J(ι) = (1 + Δ)(Id + F(ι)) on H^m, with F(ι) compact and analytic in ι.
   Π_∂ commutes with J(ι) and with 1 + Δ (the rotations commute with the Laplacian), so with
   F(ι) = (1 + Δ)⁻¹J(ι) − Id, and F(ι)E_m ⊂ E_m.
2. The restriction of a compact operator to a closed invariant subspace is compact: the image of the unit ball of E_m
   lies in that of H^m, which is relatively compact, and in the closed set E_m.
3. 1 + Δ maps E_m injectively onto E_(m−2): for y ∈ E_(m−2), x := (1 + Δ)⁻¹y = (1 + Δ)⁻¹Π_∂y = Π_∂(1 + Δ)⁻¹y ∈ E_m.
   So it is an isomorphism, by the open mapping theorem.
4. So J(ι)|_(E_m) = (1 + Δ)|_(E_m) ∘ (Id + F(ι)|_(E_m)), and the second factor is Fredholm of index 0 (Riesz–Schauder),
   so the product is Fredholm of index 0 from E_m to E_(m−2).
5. The restricted family is analytic in ι, and invertible wherever J(ι) is invertible on H^m, as J(ι)⁻¹ commutes with
   Π_∂ and so maps E_(m−2) into E_m; such ι exist ([[lem:i-c-2-4]] (a)). So [[thm:std-analytic-fredholm]] applies on
   these Hilbert spaces: the restricted inverse is meromorphic, and its poles are where the restriction is not
   invertible, which, at index 0, is where it has a kernel, that is spec^Π_J.

[[lem:i-c-2-4]] (a) holds for the restriction because the Neumann series of its proof stays in E_m, and (c) follows as
there. In [[lem:i-c-2-6]] and [[lem:i-c-2-7]] the Mellin transform of v = Πv takes values in ran Π_∂, the cut-offs are
functions of t, N(L) commutes with Π, and the proofs use J(ι)⁻¹ only on ℳv and ℳ(N(L)χv), both in ran Π_∂, where the
restricted inverse replaces it. ∎

**Theorem {#thm:gd-r8-7}** (The low-energy theory on the subspace.) Let Π ∈ {Π_(≥2), Π_cl}.

(a) For every α with α + 2 ∈ (−1, 0) ∪ (0, 2), [[thm:i-c-3-1]], [[thm:i-c-4-3]] (at every q with −q + 2 in the same gap
of the full bundle), [[cor:i-c-5-2]] (a)–(b) and [[thm:i-c-6-4]] (1), (3) and (4) with m_1 = m_2 = 0 hold for P_Π,
with (Z) given by [[prop:gd-r8-5]] and (TF) by [[prop:gd-r8-6]].

(b) The same holds for every α with α + 2 ∈ (−1, 3), 0 included, and [[prop:gd-r8-5]] and [[prop:gd-r8-6]] hold there.

*Proof.* (a) *Restriction.* Every estimate of [[ch:s03]] for P̂(σ), its adjoint, N_tf and its adjoint
([[eq:i-c-3-2]]–[[eq:i-c-3-3]], [[eq:i-c-4-3]]–[[eq:i-c-4-5]], [[eq:i-c-6-3]] and those of [[thm:i-a-7-2]]) holds for
every element of its space at the weights where it is proved, so for the elements of ran Π; at the weights of (a),
α + 2 and −q + 2 lie in gaps of the full bundle, where (G) holds for P̂. Fredholm properties pass to the restrictions
([[lem:hr-split]]), and the annihilator of a restricted range is the part in ran Π of the full one: if v ∈ ran Π
annihilates P_Π(𝒳 ∩ ran Π), it annihilates P̂𝒳, as ⟨P̂u, v⟩ = ⟨ΠP̂u, v⟩ = ⟨P̂Πu, v⟩. The statements on the regularity
of kernels ([[thm:i-c-3-1]] (2), [[thm:i-c-4-3]] (5)) restrict. [[thm:i-c-3-1]] (4) for P_Π is [[prop:gd-r8-5]].
[[cor:i-c-5-2]] (a): by [[prop:gd-r8-6]] (ii)–(iii) and [[thm:i-c-4-3]] (3) restricted, the restricted N_tf(1) has index
0, the index is constant in θ (the local constancy argument of [[thm:i-c-4-3]] (3) runs with its finite-rank
augmentations chosen in ran Π, which is possible as ΠC_c^∞(tf°) ⊂ C_c^∞(tf°) is dense in each restricted space), and
(ii) gives invertibility. [[cor:i-c-5-2]] (b): the contradiction argument stays in ran Π, which is closed in
H^(−N,(−N,−N))_(sc,b). [[thm:i-c-6-4]] (1): Step 1 inverts P_Π(0) at the regularity s + k ([[prop:gd-r8-5]] at that
regularity) on χ_zf u ∈ ran Π (χ_zf is a function of ρ); Step 2 applies [[eq:i-c-5-1]] to S_ς(χ_tf u) ∈ ran Π at the
weight shifted by η ∈ (0, 1], η so small that α + 2 + η lies in the same gap of the full bundle ([[cor:i-c-5-2]] (b)
restricted); [[lem:i-c-6-2]], [[lem:i-c-6-3]] and [[thm:i-a-7-2]] (4) are estimates for all u. [[thm:i-c-6-4]] (3):
P̂(σ) is invertible for σ ≠ 0, Im σ ≥ 0 ([[prop:iii-d-6-2]]), and commutes with Π, so P_Π(σ) is. [[thm:i-c-6-4]] (4):
its proof, with P̂(σ)⁻¹ restricted to ran Π, whose differentiability is [[thm:i-a-7-2]] (6) restricted, and (1) at the
regularities s + i ([[prop:gd-r8-5]] at each).

(b) *Transposition.* Every use of the gap in the proofs of [[thm:i-c-3-1]], [[thm:i-c-4-3]],
[[cor:i-c-5-2]] and [[thm:i-c-6-4]] is one of [[lem:i-c-2-4]], [[lem:i-c-2-6]] and [[lem:i-c-2-7]] applied to an
element of ran Π: [[lem:i-c-2-6]] at c = α + 2 to χ̃_∂u and at c = −α to the v of the adjoint ([[sec:i-c-3-1]]);
[[lem:i-c-2-7]] for kernels and annihilators ([[sec:i-c-3-2]]–[[sec:i-c-3-3]]); [[lem:i-c-2-6]]–[[lem:i-c-2-7]] at
ztf ([[sec:i-c-4-4]]); and the choice of η in Step 2 of the proof of [[thm:i-c-6-4]], now inside (−1, 3). By
[[lem:gd-r8-8]] these hold on ran Π with (G) read for spec^Π_b, at every weight of (−1, 3) ([[lem:gd-r8-3]] (c)); so the
proofs run on ran Π. [[thm:i-c-3-1]] (3)–(4) restricted carries the invertibility of [[prop:gd-r8-5]] from one weight
to every weight of (−1, 3); [[thm:i-c-4-3]] (5) restricted gives [[prop:gd-r8-6]] (ii) by the same argument at every
β ∈ (−1, 3), now with β′ < 3 ≤ 2 + ℓ; (iii) uses no gap; and [[cor:i-c-5-2]] (c) restricted gives (TF) at every weight
of the gap. ∎

Part (a) is all that is used below: [[thm:gd-r8-10]] works at weights in (−1, 0).

**Corollary {#cor:gd-r8-9}** (The low-energy hypotheses on the subspace.) For P̂(σ) restricted to ran Π_cl (the class
1-forms with no l = 0 part) or to ran Π_(≥2), (G), (Z) and (TF) of [[sec:i-c-1-2]] hold at every b-weight
α + 2 ∈ (−1, 3), in particular at every α + 2 ∈ (−1, 0]. [[thm:i-c-6-4]] (4) holds there for P_Π, and so do
[[prop:ii-g1-4-7]] and [[lem:iii-i2-4-2]], with β_tf − β_zf = α + 2 and with û = P_Π(σ)⁻¹f̂ in place of
(û, b̂, Ŝ): no augmentation is needed.

*Proof.* [[lem:gd-r8-3]] (c), [[prop:gd-r8-5]], [[prop:gd-r8-6]] and [[thm:gd-r8-7]]. The proof of
[[prop:ii-g1-4-7]] uses of the operator only [[thm:i-c-6-4]] (4) with m_1 = m_2 = 0 and (5), and [[lem:ii-g1-4-1]],
which involves no operator; the proof of [[lem:iii-i2-4-2]] is that proof with the augmented estimates of [[ch:s18]] in
place of those of [[ch:s03]], which are no longer needed. ∎

### The rate of the representative {#sec:hr-rate}

The first improvement uses only [[thm:gd-r5-2]]: the forcing term of the gauge vector on the cone has the ι⁺-order
5/2 + δ_♯ less any η > 0 ([[prop:gd-r3-2]]), and the window γ_+ − α_K ∈ (0, 1) of [[thm:gd-r5-1]] turns it into the
rate t_*^(−1/2−κ), κ < δ_♯. Its construction serves the part with l ≥ 2 below.

**Corollary {#cor:gd-r5-3}** (The harmonic gauge at t_*^(−1/2−κ).) For every κ ∈ (0, δ_♯) there is C_κ, bounded by
finitely many norms of the data, such that on each {r_♭ < r ≤ R′, t_* ≥ T′}, with every number of derivatives,

    |ġ_H − ṁK* − c_∞ℒ_(W*)g| ≤ C_κ t_*^(−1/2−κ),                                                          {#eq:gd-r5-3}

for ġ_H of [[cor:gd-r4-4]] (on all of N⁺) and of [[thm:gd-r3-4]] (on the late region), each with its c_∞.

*Proof.* Fix κ and put

    β := ½(κ + δ_♯),    η := ½(δ_♯ − β),    b_+ := ½ + β,    γ_+ := ½ + ½(κ + β),    α_K := ½ + κ.

Then κ < β < δ_♯ < ¼, and: α_K ∈ [½, 1); γ_+ − α_K = ¼(δ_♯ − κ) > 0 and γ_+ < 3/2; γ_+ + 2 < 5/2 + δ_♯ − η, as
δ_♯ − η = ½(δ_♯ + β) > ½(κ + β); and γ_+ < b_+, as b_+ − γ_+ = ½(β − κ) > 0.

*The full solution.* For [[cor:gd-r4-4]]: with [[thm:gd-r4-3]] at this β (some p ∈ (½ + β, min(3/2, q_ḣ − 1))) and
b_I ∈ (b_+, p), Y := χ(t^♭_*)Z_1 is the forward solution on Ω_* of χ(t^♭_*)F_Y + [□, χ(t^♭_*)]Z_1, a forcing term in
the space of [[lem:gd-r3-5]] (the proof of [[prop:gd-r3-6]]); and [[cor:ii-f1-1-2]] gives
Y ∈ H^(k,(b_I,b_+,−1/2))_b(Ω_*, μ_b) for every k. For [[thm:gd-r3-4]], Y is its own forward solution, with the same
weights ([[lem:gd-r3-5]]).

*Cone localisation.* χ′Y is the forward solution of f := χ′J_h + [□, χ′]Y (the proof of [[thm:gd-r3-4]] (iii)). f
vanishes near ℐ⁺, as supp χ′ ⊂ {r ≤ t_*/20}, so [[eq:gd-r5-1]] holds with every w_I. On supp χ′ ⊂ {χ_K = 1}, χ′J_h is
conormal of ι⁺-order ϰ_♯ + 1 − η = 5/2 + δ_♯ − η and of K⁺-order α − 2 − η = w − η > 2 + ε_t − η > 1
([[prop:gd-r3-2]] and its proof, [[sec:hg-setting]]); so it lies in [[eq:gd-r5-1]], as γ_+ + 2 < 5/2 + δ_♯ − η and
α_K < 1. On the cone part {1/40 ≤ r/t_* ≤ 1/20} of supp dχ′, [□, χ′] ∈ ρ_+²Diff¹_b, and that cone stays away from K⁺
and ℐ⁺; the rest of supp dχ′ is compact. So [□, χ′]Y ∈ H^(∞,(N,b_++2,N))_b for every N, in [[eq:gd-r5-1]] as
γ_+ < b_+.

*The rate.* [[thm:gd-r5-2]] gives |χ′Y − c_f(t_*)W*| ≤ Ct_*^(−1/2−κ), with every derivative. For large t_*, χ′ = 1 near
the horizon, and ℓ(f) = ℓ(J_h) = ℓ(Υ̇⁰(h)) = O(v^(−w+ε′)) ([[thm:gd-2-3]]), so c_f − c_∞ = O(t_*^(−(w−1)+ε′)), w − 1 > 1.
On compact r-sets at late times χ′ = χ(t^♭_*) = χ_K = 1, so Z_1 = χ′Y (for [[thm:gd-r3-4]], Y = χ′Y), and
ġ_H − ṁK* − c_∞ℒ_(W*)g = h + ℒ_(Z_1−c_∞W*)g as K* = K_V + ℒ_(W**_H)g, with |h|_k = O(t_*^(−w+ε′)) ([[eq:gd-0-2]]). ∎

For the representative of [[cor:gd-r4-4]] this is improved below: its spherically symmetric part is that of a
homogeneous solution ([[cor:gd-r7-7]]), and its part with l ≥ 2 sees no zero-energy state.

**Theorem {#thm:gd-r8-10}** ([[thm:gd-r6-4]] on the subspace, with the window in (−1, 0).) Let Π ∈ {Π_(≥2), Π_cl},
α_K ∈ (1, 2), γ_+ ∈ (max(½, α_K − 1), 1), ε_1 ∈ (0, ½), w_I ≥ max(5/2, γ_+ + 1 + ε_1), let
f ∈ H^(∞,(w_I,γ_++2,α_K))_b(Ω_*; T*)^(•,−) with plain weights and Πf = f, and let u be the forward solution of □u = f.
Then Πu = u, and for every small ε > 0

    u ∈ H^(∞,(γ_+−3ε,γ_+,α_K))_b(M′),     |u| ≤ C t_*^(−α_K)‖f‖  on {r_♭ < r ≤ R′, t_* ≥ 8 max(R′, 1)},  {#eq:gd-r8-2}

with every number of derivatives in x and t_*, ‖f‖ a norm of f in that space at an order k + ℓ. There is no singular
part and no W*.

*Proof.* Πu = u by [[lem:gd-r8-2]] (b). We follow the proof of [[thm:gd-r6-4]].

*The decomposition.* For f with Πf = f, (û_(reg,1), b̂_1) := P̃(σ)⁻¹(f̂, 0) has b̂_1 = 0 and
û_(reg,1) = P_Π(σ)⁻¹f̂ for 0 < |σ| ≤ c: Π_0 commutes with P̂(σ), fixes the column f̂_*(σ), the transform of the
SO(4)-invariant [□, χ^H_K]W*, and the row, φ_* and h being SO(4)-invariant, and kills f̂ (Π_0Π = 0); so
P̃(σ)(Π_0û_(reg,1), b̂_1) = (Π_0f̂, ⟨û_(reg,1), φ_*⟩_h) = (0, 0), whence Π_0û_(reg,1) = 0, b̂_1 = 0, and
P̂(σ)û_(reg,1) = f̂. So u_sing = 0 and u = u_hi + u_reg, with c at most the constant c_k of [[cor:gd-r8-9]] at the
weight below.

*Step 2* is that of [[thm:gd-r6-4]]: [[lem:iii-i2-4-1]] at (w_I, γ_+ + 2, α_K), whose conditions are w_I − 1 ≥ 3/2 and
w_I ≥ γ_+ + 1 + ε_1 (as α_K > 1 − ε_1), gives u_hi ∈ H^(∞,(3/2−ε,N,N))_b; and [[prop:ii-g1-3-3]] (1) with ε_PP gives
f̂|_(±(0,c]) ∈ H^(∞,(min(w_I,γ_++2)−ε,γ_++1,((0,0),α_K−1)))_b, with f̂(0) = ∫f dt_* ∈ H^(∞,γ_++1)_b(X) ∩ ran Π. The
density step takes b_+ := ½(½ + γ_+) ∈ (½, γ_+) and b_I := ½(b_+ + 3/2) in [[cor:ii-f1-1-2]]: ½ < b_+ < b_I < 3/2, b_+ ≤ γ_+,
b_I + 1 < 5/2 ≤ w_I and α_K ≥ ½, and b_+ − ½ ∈ (0, 1).

*Step 3.1 (zero energy, without the column).* At α := γ_+ − 3, α + 2 = γ_+ − 1 ∈ (−1, 0), and 𝒴_0 has the μ_b-weight
γ_+ + 1, so f̂(0) ∈ 𝒴_0 ∩ ran Π and û_0 := P_Π(0)⁻¹f̂(0) ∈ H^(∞,γ_+−1)_b(X) ([[prop:gd-r8-5]] at every regularity). With

    f̂_2 := (f̂ − χ_zf f̂(0)) − [P̂(0), χ_zf]û_0 − (P̂(σ) − P̂(0))(χ_zfû_0),

P̂(σ)(χ_zfû_0) = f̂ − f̂_2, and f̂_2 lies in H^(∞,(min(w_I,γ_++2)−ε,γ_++1,α_K−1))_b by [[lem:iii-i3-1-1]] (b) and
[[lem:gd-r6-2]] (a) at a = γ_+ − 1, as α_K − 1 < 1. The column term of [[thm:gd-r6-4]] is absent.

*Step 3.2.* [[cor:gd-r8-9]] ([[lem:iii-i2-4-2]] for P_Π) applies at β_scf := 3/2 − ε, β_tf := γ_+ − 1,
β_zf := α_K − 1, with the window β_tf − β_zf = γ_+ − α_K ∈ (−1, 0); its forcing space asks the scf-weight
5/2 − ε ≤ min(w_I, γ_+ + 2) − ε, which is γ_+ ≥ ½. So û_(reg,1) = χ_zfû_0 + P_Π(σ)⁻¹f̂_2 lies in
H^(∞,(3/2−2ε,γ_+−1,((0,0),α_K−1)))_b with zf-coefficient û_0, the same for both signs. [[prop:ii-g1-3-5]] (1) at
β_K = α_K ∈ (1, 2), with that one Taylor coefficient, v_0 = û_0 ∈ H^(∞,β_ι−1)_b(X), β_ι = γ_+, gives
u_reg ∈ H^(∞,(γ_+−ε,γ_+,α_K))_b(M′), as γ_+ < 3/2 − 2ε.

*The rate.* u = u_hi + u_reg ∈ H^(∞,(γ_+−3ε,γ_+,α_K))_b(M′), and b-Sobolev embedding near K⁺, where ρ_K is comparable
to t_*⁻¹ on compact r-sets, gives [[eq:gd-r8-2]], as in the proof of [[thm:gd-r6-5]] without u_sing. ∎

Where [[thm:gd-r6-4]] needs γ_+ > α_K, the lower end 0 of the window being the indicial root of W* and of the
constants, here γ_+ − α_K > −1 suffices.

The *part with l ≥ 2* of a class tensor or 1-form k is k_(≥2) := k − k_0; class tensors and 1-forms carry only l = 0
and even l ≥ 2 ([[lem:gd-1-2]]), and for a class 1-form Z, (ℒ_Zg)_(≥2) = ℒ_(Z_(≥2))g, as X ↦ ℒ_Xg commutes with the
SO(4)-average. For class 1-forms, Z_(≥2) = Π_cl Z.

**Corollary {#cor:gd-r8-11}** (The part with l ≥ 2.) Let ġ_H be the representative of [[cor:gd-r4-4]]. For every
α < 3/2 + δ_♯, on each {r_♭ < r ≤ R′, t_* ≥ T′} and with every number of derivatives, (ġ_H)_(≥2) = O(t_*^(−α)), the
constant bounded by finitely many norms of the data.

*Proof.* It suffices to take α = α_K ∈ (1, 3/2 + δ_♯). Choose

    γ_+ ∈ (max(½, α_K − 1), ½ + δ_♯),        β ∈ (γ_+ − ½, δ_♯),        η ∈ (0, ½ + δ_♯ − γ_+),

possible as α_K − 1 < ½ + δ_♯; then γ_+ < ¾ < 1 and β > 0. As in the proof of [[cor:gd-r5-3]] at this β, with
[[thm:gd-r4-3]] (some p ∈ (½ + β, min(3/2, q_ḣ − 1)), which is nonempty as q_ḣ − 1 > ½ + 2γ_Υ), b_+ := ½ + β and
b_I ∈ (b_+, p): Y := χ(t^♭_*)Z_1 ∈ H^(k,(b_I,b_+,−1/2))_b(Ω_*, μ_b), and χ′Y is the forward solution of
f := χ′J_h + [□, χ′]Y. Put f_(≥2) := Π_cl f; its forward solution is Π_cl(χ′Y) ([[lem:gd-r8-2]] (b)). f vanishes near
ℐ⁺, so every w_I is allowed. χ′J_h has ι⁺-order 5/2 + δ_♯ − η > γ_+ + 2 and K⁺-order w − η > 2 + ε_t − η > α_K
([[prop:gd-r3-2]]; η < δ_♯ < ¼); [□, χ′]Y ∈ H^(∞,(N,b_++2,N))_b with b_+ > γ_+; and Π_cl preserves these classes
([[lem:gd-r8-2]] (b)). So f_(≥2) satisfies the hypotheses of [[thm:gd-r8-10]] with Π = Π_cl, which gives
Π_cl(χ′Y) = O(t_*^(−α_K)) on compact sets, with every derivative. At late times on compact sets χ′ = χ(t^♭_*) = χ_K = 1,
so Z_(1,≥2) = Π_cl(χ′Y), and (ġ_H)_(≥2) = h_(≥2) + ℒ_(Z_(1,≥2))g, as ṁK_V and ℒ_(W**_H)g have no part with l ≥ 2; and
|h|_k = O(t_*^(−w+ε′)) ([[eq:gd-0-2]]). ∎

**Theorem {#thm:harmonic-rate}** (The harmonic-gauge representative and its rate.) Let (γ̇, k̇) be data in the class of
[[cor:viii-2-3]], ġ its linear solution and ṁ its mass change, and let ġ_H = ġ + ℒ_Zg be the representative of
[[cor:gd-r4-4]]: G-invariant, DRic(ġ_H) = 0 and Υ̇⁰(ġ_H) = 0 on all of N⁺, and ġ_H = ġ near Σ°, so that ġ_H induces
(γ̇, k̇) exactly. Let Z′_0 be the 1-form of [[eq:gd-r7-4]], with □Z′_0 = 0, c′ the Killing multiple of its data, p_0 the
supremum of the orders of its data ([[def:hr-order]]), and

    c := (Q[Z′_0] − 4π²m₀c′)/4π².

On each {r_♭ < r ≤ R′, t_* ≥ T′}, with every number of derivatives:

(a) ġ_H − ṁK* − cℒ_(W*)g = O(t_*^(−α)) for every α < min(p_0, 3/2), where p_0 ≥ q − 1 > ½ + 2γ_Υ, q of
[[cor:gd-r7-7]]. As γ_Υ ≥ δ_♯, this is faster than t_*^(−1/2−δ_♯) for every perturbation in the class.

(b) If outside a ball (γ̇, k̇) are ṁ times the data of K_V, as for the data of [[thm:settling]], then
ġ_H − ṁK* − cℒ_(W*)g = O(t_*^(−1+ε)) for every ε > 0.

(c) For data with compact support, ṁ = 0 and ġ_H − cℒ_(W*)g = O(t_*^(−3/2−κ)) for every κ < δ_♯, and the spherically
symmetric part is

    (ġ_H)_0 = cℒ_(W*)g + (m₀c/2) t_*^(−2) ℒ_(W*)g + O(t_*^(−3+ε))        for every ε > 0.

In every case the part with l ≥ 2 is O(t_*^(−3/2−κ)) for every κ < δ_♯. K* = K + ℒ_(W**)g is the gauge-fixed mass
change of [[prop:np-10-2]] (iv) (c), smooth across the horizon, with K* − (v/2)ℒ_(W*)g stationary: ṁK* grows linearly
in v.

*Proof.* In the class, ġ_H − ṁK* − cℒ_(W*)g = ((ġ_H)_0 − ṁK* − cℒ_(W*)g) + (ġ_H)_(≥2), as K* and ℒ_(W*)g are
spherically symmetric. The first term is [[cor:gd-r7-7]] (a), (b) and its last display; the case α = 1 of (a) follows
from a slightly larger α when min(p_0, 3/2) > 1. The second is [[cor:gd-r8-11]], whose exponent 3/2 + δ_♯ exceeds 3/2
and 1 and is below 2: so in (c) the rate of the sum is that of the part with l ≥ 2. ∎

On each {r_♭ < r ≤ R′}, t_* − v and t_* − t are bounded, so the rates hold with v or t in place of t_*. Without decay of
the data of Z′_0 the growth ṁK* can be traded for a stationary term that does not decay at infinity
([[prop:gd-r2-13]] (c)).
