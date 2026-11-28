### The map of the recovery at a point, and the seven fields through it {#sec:tl5-hfk}

This section makes one change, at level four. In the recovery of D̂²h at a point p ([[lem:tl5-hfp-rec]]) the components
of D̂²h in the directions E₀ and f_j are, by the proof of [[lem:tl5-hf-recovery]], the image under the linear map 𝒳_p :
(x_Z)_(Z∈Γ) ↦ (|T|⁻¹ x_T, (Σ_(a<b) c^ab_j x_(K_ab))_j) of the family of the derivatives D̂ℒ_Zh of the seven fields, up
to the terms 𝔷_(Z,A) of that proof. That lemma bounds the image by the operator norm K_rec of 𝒳_p times the Euclidean
norm of the family, and [[lem:tl5-hfp-c1]] bounds this norm for the family Γ. We bound the image itself
([[lem:tl5-hfk-rec]]). The coefficients of 𝒳_p at p are numbers, so the Sobolev inequality of the face applies to the
four fields that 𝒳_p makes of the D̂Ψ_Z, and at each point of the face the sum of the squares of their Lie derivatives
along a word J is at most the sum of |T(p)|⁻² |ℒ^J D̂Ψ_T|² and of the λ_M(p)⁻¹ |ℒ^J D̂Ψ_Z|² of the six rotations, and
likewise with D̂ℒ^J. In the bound of the family that results, two kinds of terms take different factors
([[lem:tl5-hfk-fam]]). The terms whose bounds for the seven fields form a family bounded in the Euclidean norm through
𝒟_g and 𝒥_g, that is the leading terms D̂Ψ_(JZ), the remainders, and the leading term and the terms with 𝔷 and 𝔯_♯ of
the recovery of D̂²Ψ_(JZ), take the factor K_rec(p), as before. The terms with one bound for all seven fields, that is
the nonlinear part and the part with ϱ of the bounds of the D̂²Ψ_(JZ), and the terms on the leaf S_a, take 𝔨_Γ :=
(|T(p)|⁻² + 6λ_M(p)⁻¹)^(1/2) in place of √7 K_rec(p), which is smaller unless |T|⁻¹ = λ_M^(−1/2); and the couplings 𝔄
take the operator norm of their map with its components so weighted. In the recovery at p the terms 𝔷_Z take the same
weights. The change enters the recovery constants with index k, through them C_P^v, C_(P,ϱ)^v and C_(P,0)^v, and so both
𝔰_* and the closing condition ([[def:tl5-hfk-constants]], [[thm:tl5-hfk]]). The closing condition is
[[eq:tl5-hfk-closing]]; every new constant is at most the one it replaces, and the earlier closing conditions remain
valid. The notation is that of [[sec:tl5-hff]].

**Lemma {#lem:tl5-hfk-rec}** (The recovery through the map of the seven fields.) Let p, H, Ψ, 𝔣, 𝔷_Z, ‖𝓡̂‖, ‖𝒞_(·1)‖, 𝔥,
𝔨_♯(𝔥) and 𝔯_♯ be as in [[lem:tl5-hfz-rec]], and let |T|, λ_M and the coefficients c^ab_j (j = 2, 3, 4) be those of
[[def:tl5-hf-frame]] and [[lem:tl5-hf-fields]] (a) at p. For a family x = (x_Z)_(Z∈Γ) of tensors at p of one type let
𝒳_p x be the family (|T|⁻¹ x_T, (Σ_(a<b) c^ab_j x_(K_ab))_(j=2,3,4)), and |𝒳_p x| its Euclidean norm, formed with the
norm |·| of its four members; for a family y = (y_Z)_(Z∈Γ) of numbers put |y|_Γ := (|T|⁻² y_T² + λ_M⁻¹ Σ_(a<b)
y_(K_ab)²)^(1/2); and put

    𝔨_Γ := (|T|⁻² + 6λ_M⁻¹)^(1/2),      𝔷₁^k := 3 |(|D̂Z|)_(Z∈Γ)|_Γ,      𝔷₂^k := 2 |(|D̂²Z|)_(Z∈Γ)|_Γ.

(a) For every family x, |𝒳_p x| ≤ |(|x_Z|)_Z|_Γ ≤ K_rec (Σ_Z |x_Z|²)^(1/2); and 𝔨_Γ ≤ √7 K_rec, 𝔷₁^k ≤ K_rec 𝔷₁′ and
𝔷₂^k ≤ K_rec 𝔷₂′, with 𝔷₁′ and 𝔷₂′ as in [[def:tl5-hfp-constants]].

(b) At p,

    |D̂²Ψ| ≤ 𝔨_♯(𝔥) (|𝒳_p (D̂ℒ_ZΨ)_(Z∈Γ)| + 𝔷₁^k |D̂Ψ| + 𝔷₂^k |Ψ|) + (1 − 𝔥)⁻¹ (|𝔣| + 𝔯_♯ |Ψ|).        {#eq:tl5-hfk-rec}

By (a), the right side of [[eq:tl5-hfk-rec]] is at most that of [[eq:tl5-hfz-rec]] with 𝔷₁′ |D̂Ψ| + 𝔷₂′ |Ψ| in place of
(Σ_Z 𝔷_Z²)^(1/2), the form in which [[lem:tl5-hfp-rec]] uses it.

*Proof.* (a) By [[lem:tl5-hf-fields]] (a), Σ_j |Σ_(a<b) c^ab_j x_(K_ab)|² ≤ λ_M⁻¹ Σ_(a<b) |x_(K_ab)|², the x_(K_ab)
lying in a Euclidean space; this is the first inequality. The second holds as |T|⁻² and λ_M⁻¹ are at most K_rec², and so
do the bounds of 𝔨_Γ, 𝔷₁^k and 𝔷₂^k, as 𝔷₁′ = 3 (Σ_Z |D̂Z|²)^(1/2) and 𝔷₂′ = 2 (Σ_Z |D̂²Z|²)^(1/2).

(b) In the proof of [[lem:tl5-hf-recovery]] the frame directions F_B with B ≠ 1 are E₀ and the f_j, and for every A,
D̂²Ψ(A, 0) = |T|⁻¹ (D̂_A ℒ_TΨ − 𝔷_(T,A)) and D̂²Ψ(A, j) = Σ_(a<b) c^ab_j (D̂_A ℒ_(K_ab)Ψ − 𝔷_(K_ab,A)). For Z ∈ Γ let
u_Z := D̂ℒ_ZΨ and let w_Z be the tensor of rank three with w_Z(F_A, ·, ·) := 𝔷_(Z,A); so |w_Z| ≤ 𝔷_Z by that proof, and,
as |B|² = Σ_A |B(F_A, ·, ·)|² for a tensor B of rank three, the number X of that proof, the sum of the |D̂²Ψ(A, B)|²
over all A and all B ≠ 1, is |𝒳_p (u − w)|². As 𝒳_p is linear, Minkowski's inequality gives X^(1/2) ≤ |𝒳_p u| + |𝒳_p w|,
and by (a) and Minkowski's inequality in the weighted Euclidean norm |·|_Γ, |𝒳_p w| ≤ |(𝔷_Z)_Z|_Γ ≤
3 |(|D̂Z|)_Z|_Γ |D̂Ψ| + 2 |(|D̂²Z|)_Z|_Γ |Ψ| = 𝔷₁^k |D̂Ψ| + 𝔷₂^k |Ψ|. The proof of [[lem:tl5-hfz-rec]] uses the bound of
X only as a number 𝔟 with X^(1/2) ≤ 𝔟, there K_rec ((Σ_Z |D̂ℒ_ZΨ|²)^(1/2) + (Σ_Z 𝔷_Z²)^(1/2)), and gives |D̂²Ψ| ≤ 𝔨_♯(𝔥)
𝔟 + (1 − 𝔥)⁻¹ (|𝔣| + 𝔯_♯ |Ψ|); with 𝔟 := |𝒳_p u| + 𝔷₁^k |D̂Ψ| + 𝔷₂^k |Ψ| this is [[eq:tl5-hfk-rec]]. The last claim
follows from (a), as (Σ_Z 𝔷_Z²)^(1/2) ≤ 𝔷₁′ |D̂Ψ| + 𝔷₂′ |Ψ| by Minkowski's inequality over Z. ∎

**Lemma {#lem:tl5-hfk-fam}** (The seven fields through the map of the recovery.) Let N = 4, let the setting be that of
[[lem:tl5-hfp-rec]], with 𝔰 ≤ 𝔰₁^v on Q(a, b) and the constants with index l, and let 𝒳_p, |·|_Γ and 𝔨_Γ be as in
[[lem:tl5-hfk-rec]], formed with the numbers |T(p)|, λ_M(p) and c^ab_j(p) of the point p. At each point of Σ₁(a, b) let
𝔞_𝔄^k be the operator norm of the map that defines 𝔞_𝔄(Γ) in [[def:tl5-hfp-constants]], the words of Γ having length
one, its components of the pairs (J, T) multiplied by |T(p)|⁻¹ and those of the pairs (J, K_ab) by λ_M(p)^(−1/2). Let
C₁^k(p) be K_rec(p) times the constant C₁^(Γ,l)(p) = C₁^l(Γ)(p) of [[eq:tl5-hfe-constants]] formed with 43^(1/2)
𝔨_Γ/K_rec(p) in place of (43n)^(1/2) = 301^(1/2) and with 𝔞_𝔄^k/K_rec(p) in place of 𝔞_𝔄(Γ), in 𝔩_D(Γ) and 𝔩_J(Γ) at
every point of the face. Then

    |𝒳_p (D̂Ψ_Z(p))_(Z∈Γ)| ≤ μ^(−2) C₁^k ℰ_g(p)^(1/2) + 𝔨_Γ (w C_(1,ϱ)^l ϱ(p) + E₀),                   {#eq:tl5-hfk-fam}

with w and the part E₀ with η₀ as in [[lem:tl5-hfp-c1]] for 𝔚 = Γ. Moreover 𝔞_𝔄^k ≤ K_rec(p) 𝔞_𝔄(Γ) and C₁^k ≤ K_rec(p)
C₁^(Γ,l).

*Proof.* Let A_Z := D̂Ψ_Z for Z ∈ Γ, and let Ã₀ := |T(p)|⁻¹ A_T and Ã_j := Σ_(a<b) c^ab_j(p) A_(K_ab), j = 2, 3, 4,
tensor fields of rank three on Q(a, b) that are combinations of the A_Z with constant coefficients; so
Σ_i |Ã_i(p)|² = |𝒳_p (A_Z(p))_Z|². As the coefficients are numbers, ℒ^J Ã_i and D̂ℒ^J Ã_i are the same combinations of
the ℒ^J A_Z and of the D̂ℒ^J A_Z, and so, by [[lem:tl5-hf-fields]] (a) at p, applied to the tensors at each point,
Σ_i |ℒ^J Ã_i|² ≤ |(|ℒ^J A_Z|)_Z|_Γ² and Σ_i |D̂ℒ^J Ã_i|² ≤ |(|D̂ℒ^J A_Z|)_Z|_Γ² at every point of the face and of S_a,
for every word J. In the proof of [[lem:tl5-hfp-c1]] with 𝔚 = Γ and b = 1, in the form that the proof of [[thm:tl5-hfe]]
gives it, [[eq:tl5-hfe-face]] with r = 3 and 𝔲 = 𝔲₁ is applied to each A_B and added over B ∈ Γ; apply it to each Ã_i
and add over i. By these inequalities the right side is at most that of the proof with every sum over Z ∈ Γ of squares
weighted by |T(p)|⁻² for Z = T and by λ_M(p)⁻¹ for the rotations: with the weights 𝔶_(|J|) and the factor μ⁴, the
Euclidean norm of a family y = (y_(J,Z)) of numbers over the 301 pairs is replaced by the weighted Euclidean norm |y|_Γ
:= (Σ_J |(y_(J,Z))_Z|_Γ²)^(1/2).

That proof bounds these norms at each point by Minkowski's inequality, over bounds for each pair of three kinds. (i)
Bounds that form, over the pairs, a family whose Euclidean norm the proof bounds through 𝒟_g or 𝒥_g: those of the
leading terms D̂Ψ_(JZ), of the remainders R′_(J,Z) and D̂R′_(J,Z), and, in the bound of D̂²Ψ_(JZ) by [[lem:tl5-hfz-rec]]
at the point of the face, of its leading term through the words Z′JZ and of its terms with 𝔷_(Z′) and with 𝔯_♯ |Ψ_(JZ)|.
As |y|_Γ ≤ K_rec(p) (Σ_(J,Z) y_(J,Z)²)^(1/2) by [[lem:tl5-hfk-rec]] (a), each of these parts is at most K_rec(p) times
its bound there. (ii) Bounds u_J that do not depend on Z: the nonlinear part and the part with ϱ of the bound of
D̂²Ψ_(JZ), which multiplied by 𝔬_J are at most 𝔵^z (k₁^D 𝒟_g + (k₁^p − k₁^D + 2) 𝒥_g)/(1 − 𝔵^z) and 𝔬_J P_C, by the
proof of [[lem:tl5-hfp-words]]; and on S_a the bound of ℒ^J A_Z that the step uses for every J. For these |y|_Γ = 𝔨_Γ
(Σ_J u_J²)^(1/2), where the Euclidean norm is √7 (Σ_J u_J²)^(1/2); so their parts are those of the proof with 𝔨_Γ in
place of n^(1/2) = √7, that is with 43^(1/2) 𝔨_Γ in place of (43n)^(1/2) in the nonlinear parts of 𝔩_D(Γ) and 𝔩_J(Γ) and
in y, and with 𝔨_Γ in place of n^(1/2) in the parts with ϱ(p) and η₀ of [[eq:tl5-hfp-family]]. (iii) The terms with 𝔄,
whose family over the pairs, multiplied by 𝔬_J and weighted, has the norm |·|_Γ at most (1 − 𝔰₁^v)⁻¹ 𝔞_𝔄^k 𝒥_g, by the
definition of 𝔞_𝔄^k and Σ_K μ^|K| (|D̂Ψ_K|² + |Ψ_K|²) ≤ 𝒥_g², as in that proof.

So, with K := K_rec(p) and 𝔩_D^k and 𝔩_J^k the functions 𝔩_D(Γ) and 𝔩_J(Γ) formed with 43^(1/2) 𝔨_Γ/K and 𝔞_𝔄^k/K in
place of 301^(1/2) and 𝔞_𝔄(Γ), at each point of the face

    |(𝔶_(|J|)^(1/2) μ² |ℒ^J A_Z|)_(J,Z)|_Γ ≤ K (μ^(1/2) 𝒟_g + ϖ′^(1/2) 𝒥_g),
    |(𝔶_(|J|)^(1/2) μ² |D̂ℒ^J A_Z|)_(J,Z)|_Γ ≤ K (𝔩_D^k 𝒟_g + (𝔩_J^k + (2ϖ′)^(1/2)) 𝒥_g) + 43^(1/2) 𝔨_Γ 𝔗(𝔶) μ² P_ϱ,

in place of the two bounds of that proof, since K 𝔩_D^k = K k₁^D + 43^(1/2) 𝔨_Γ k₁^D 𝔵^z/(1 − 𝔵^z) and K 𝔩_J^k = K
μ^(1/2) (k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) + (1 − 𝔰₁^v)⁻¹ 𝔞_𝔄^k + 43^(1/2) 𝔨_Γ 𝔵^z (k₁^p − k₁^D + 2)/(1 − 𝔵^z). The rest of
that proof uses these bounds only through Minkowski's inequality in L² of the face and the bounds ∫ g 𝒟_g² ≤ sup (g 𝔨₂′)
ℰ_g(p) and ∫ g 𝒥_g² ≤ sup (g 𝔨₂) ℰ_g(p) for functions g ≥ 0, the number K² coming out of the integrals; so it gives its
two bounds with K² times the functions of C₁^(U,l)(Γ)², C₁^(D,l)(Γ)² and C₁^(J,l)(Γ)² so formed, the smaller of which is
C₁^k, and with 𝔨_Γ in place of n^(1/2) in the parts with ϱ(p) and η₀. This is [[eq:tl5-hfk-fam]].

For the last claims, the map defining 𝔞_𝔄^k is that defining 𝔞_𝔄(Γ) followed by the multiplication of its components by
numbers at most K, so 𝔞_𝔄^k ≤ K 𝔞_𝔄(Γ); and 43^(1/2) 𝔨_Γ/K ≤ 301^(1/2) by [[lem:tl5-hfk-rec]] (a). The functions in
C₁^(U,l)(Γ), C₁^(D,l)(Γ) and C₁^(J,l)(Γ) are nondecreasing in (43n)^(1/2) and in 𝔞_𝔄(Γ), whose coefficients k₁^D 𝔵^z/(1
− 𝔵^z), 𝔵^z (k₁^p − k₁^D + 2)/(1 − 𝔵^z) and (1 − 𝔰₁^v)⁻¹ are nonnegative, as k₁^p ≥ k₁^D; so C₁^k ≤ K C₁^(Γ,l). ∎

**Definition {#def:tl5-hfk-constants}** (The constants with index k.) Let N = 4, let the setting be that of
[[def:tl5-hff-constants]] with route (𝔰) of [[eq:tl5-hff-routes]], let 𝔨_Γ, 𝔷₁^k and 𝔷₂^k be as in [[lem:tl5-hfk-rec]]
and C₁^k as in [[lem:tl5-hfk-fam]], at each point p, and put

    𝔨_rec^k := 𝔨_♯ (C₁^k + 𝔷₁^k μ^(1/2) C₁^l + 𝔷₂^k μ C_S^h) + (1 − 𝔰₁^v)⁻¹ μ 𝔯_♯ C_S^h,
    𝔨_rec^(ϱ,k) := 𝔨_♯ (𝔨_Γ + 𝔷₁^k μ^(1/2)) C_(1,ϱ)^l,
    𝔨_rec^(0,k) := 𝔨_♯ ((𝔨_Γ + 𝔷₁^k μ^(1/2)) C_(1,0)^p + 𝔷₂^k μ C_(0,0)^h)
                   + (1 − 𝔰₁^v)⁻¹ μ 𝔯_♯ C_(0,0)^h,                                                    {#eq:tl5-hfk-krec}

with C_S^h and C_(0,0)^h as in [[lem:tl5-hff-zero]] and C_(1,0)^p in its form with index l. These are 𝔨_rec^p,
𝔨_rec^(ϱ,p) and 𝔨_rec^(0,p) of [[def:tl5-hfp-constants]], in their forms with index f, with 𝔨_♯ C₁^k, 𝔨_♯ 𝔨_Γ, 𝔨_♯ 𝔷₁^k
and 𝔨_♯ 𝔷₂^k in place of 𝔨_♯ K_rec C₁^(Γ,l), 𝔨_♯ K_rec √7, 𝔨_♯ K_rec 𝔷₁′ and 𝔨_♯ K_rec 𝔷₂′. The constants with index k
are the constants with index f formed with 𝔨_rec^k, 𝔨_rec^(ϱ,k) and 𝔨_rec^(0,k) in place of 𝔨_rec^p, 𝔨_rec^(ϱ,p) and
𝔨_rec^(0,p) in their forms with index f: in C_P^v, C_(P,ϱ)^v and C_(P,0)^v of [[lem:tl5-hfv-rec]], and in every constant
formed from these, among them 𝔎, 𝔎_ϱ and 𝔎₀ of [[def:tl5-hfs-constants]], 𝔎^D, 𝔎^D_ϱ and 𝔎^D₀ of
[[def:tl5-hfd-constants]], S_F, 𝔯 and 𝔰_*. Let S_F^k, S_M^k, ε_M^k and 𝔯^k be S_F^f, S_M^f, ε_M^f and 𝔯^f formed with
them, ε^k := ε^f, and

    η_k := 1 − max(ϑ₁, ϑ₂) − 𝔯^k,      A_k := η_k^(−1/2) δ_w + η_k⁻¹ (ε^k + ε_M^k),      B_k := η_k⁻¹ (S_F^k + S_M^k).

For a number 𝔜 ≥ 0 let 𝔰_*^k[𝔜] be 𝔰_*^f[𝔜] formed with the constants with index k, and, when 4A_k B_k < 1, put

    Y_k := 2A_k/(1 + (1 − 4A_k B_k)^(1/2)),      𝔰_*^k := 𝔰_*^k[Y_k].                            {#eq:tl5-hfk-constants}

**Theorem {#thm:tl5-hfk}** (Existence with the seven fields through the map of the recovery.) Let N = 4. In the setting
of [[thm:tl5-hff]], with route (𝔰) and the constants with index k of [[def:tl5-hfk-constants]], suppose: (a) η₀ < 𝔰₁^v;
(b) the rates (1 − ϑ₁) a_o, (1 − ϑ₂) a_i are admissible for (𝔅_N, E_o^N, E_i^N); (c) η_k > 0, the closing condition

    4 A_k B_k = 4 η_k^(−3/2) (δ_w + η_k^(−1/2) (ε^k + ε_M^k)) (S_F^k + S_M^k) < 1,                 {#eq:tl5-hfk-closing}

and 𝔰_*^k < 𝔰₁^v. Then there is a solution g of the reduced problem on D^κ with Y_σ(g) ≤ Y_k for every σ ∈ [1/2, v*],
and the other conclusions of [[thm:tl5-hf4]] hold with 𝔰_*^k in place of 𝔰_*. Each constant with index k is at most the
one with index f it replaces, ε^k = ε^f, η_k ≥ η_f, A_k ≤ A_f, B_k ≤ B_f, Y_k ≤ Y_f and 𝔰_*^k ≤ 𝔰_*^f; so the hypotheses
of [[thm:tl5-hff]] at N = 4 imply these.

*Proof.* The proof of [[thm:tl5-hff]] with route (𝔰) applies with the constants with index k, ε^k, 𝔯^k, η_k, A_k, B_k,
Y_k, 𝔰_*^k[𝔜] and [[eq:tl5-hfk-closing]] in place of those with index f, with one change: the bound of 𝔰_P at a point of
[[lem:tl5-hfv-rec]], in the form of [[lem:tl5-hfp-rec]] with the constants with index f, holds with 𝔨_rec^k, 𝔨_rec^(ϱ,k)
and 𝔨_rec^(0,k) in place of 𝔨_rec^p, 𝔨_rec^(ϱ,p) and 𝔨_rec^(0,p).

To see this, let p be a point at which that bound is formed. Then 𝔰 ≤ 𝔰₁^v on Q(a, b), so |H(p)| ≤ 𝔰(p) ≤ 𝔰₁^v, and
[[lem:tl5-hfk-rec]] (b) with 𝔥 = 𝔰₁^v applies to h at p, with 𝔣 as in the proof of [[lem:tl5-hfv-rec]]. In the proof of
[[lem:tl5-hfp-rec]] use it in place of [[lem:tl5-hfz-rec]]: the leading term of the recovery is then 𝔨_♯ (|𝒳_p
(D̂Ψ_Z(p))_Z| + 𝔷₁^k |D̂h| + 𝔷₂^k |h|), where that proof has 𝔨_♯ K_rec ((Σ_Z |D̂Ψ_Z|²)^(1/2) + 𝔷₁′ |D̂h| + 𝔷₂′ |h|).
Multiply by μ². By [[lem:tl5-hfk-fam]], μ² |𝒳_p (D̂Ψ_Z(p))_Z| is at most C₁^k ℰ_g(p)^(1/2) + 𝔨_Γ (C_(1,ϱ)^l ϱ(p) +
C_(1,0)^p η₀(p)), with the weights of the step, where that proof has K_rec times the bound C₁^(Γ,l) ℰ_g(p)^(1/2) + √7
(C_(1,ϱ)^l ϱ(p) + C_(1,0)^p η₀(p)) of μ² (Σ_Z |D̂Ψ_Z|²)^(1/2). The jets μ^(3/2) |D̂h| and μ |h| are bounded as there, by
the first-order step with B = ∅ and by the step for h of [[lem:tl5-hff-zero]], with C₁^l, C_(1,ϱ)^l, C_(1,0)^p, C_S^h
and C_(0,0)^h; and the residual and the nonlinear terms are as there. Collecting the parts with ℰ_g(p)^(1/2), ϱ(p) and
η₀(p) of the leading term and of (1 − 𝔰₁^v)⁻¹ 𝔯_♯ μ² |h| gives 𝔨_rec^k, 𝔨_rec^(ϱ,k) and 𝔨_rec^(0,k) where that proof
gives the 𝔨_rec^(·,p), and the rest of the proof of [[lem:tl5-hfv-rec]] holds as written. The proofs on which that of
[[thm:tl5-hff]] rests use the 𝔨_rec^(·,p) only through this bound, in C_P^v, C_(P,ϱ)^v and C_(P,0)^v, from which the
other constants are formed in the same way for all values of these numbers; so they hold with the constants with index
k.

For the last claim, by [[lem:tl5-hfk-rec]] (a) and [[lem:tl5-hfk-fam]], 𝔨_Γ ≤ √7 K_rec, 𝔷₁^k ≤ K_rec 𝔷₁′, 𝔷₂^k ≤ K_rec
𝔷₂′ and C₁^k ≤ K_rec C₁^(Γ,l), so 𝔨_rec^k, 𝔨_rec^(ϱ,k) and 𝔨_rec^(0,k) are at most the numbers they replace, term by
term. Every constant with index f is nondecreasing in these numbers, so each constant with index k is at most the one it
replaces, and ε^k = ε^f. Then η_k ≥ η_f, A_k ≤ A_f, B_k ≤ B_f and 4A_k B_k ≤ 4A_f B_f, as in the proof of
[[thm:tl5-hff]]; the smaller root 2A/(1 + (1 − 4AB)^(1/2)) is nondecreasing in A and in B, so Y_k ≤ Y_f, and 𝔰_*^k ≤
𝔰_*^k[Y_f] ≤ 𝔰_*^f[Y_f] = 𝔰_*^f, as 𝔰_*^k[𝔜] is nondecreasing in 𝔜 and in the constants. ∎

**Remark {#rem:tl5-hfk-what}** (What changes.) In the proof of [[lem:tl5-hf-recovery]] the components of D̂²Ψ in the
directions E₀ and f_j are the image under 𝒳_p of the family of the D̂ℒ_ZΨ − 𝔷_(Z,·), and [[eq:tl5-hfz-rec]] bounds the
image by K_rec, the operator norm of 𝒳_p, times the norm of the family. [[eq:tl5-hfk-rec]] keeps the image of the family
of the D̂ℒ_ZΨ, and at level four [[lem:tl5-hfk-fam]] bounds it at p through the Sobolev inequality of the face for the
four fields that 𝒳_p makes of the D̂Ψ_Z, its coefficients at p being numbers. In the bound that results the map costs
each kind of term its own factor. The terms of the first kind are bounded through 𝒟_g and 𝒥_g over the words JZ, Z′JZ
and σZ, which end in the field Z, and take K_rec(p) = max(|T(p)|⁻¹, λ_M(p)^(−1/2)), the factor of [[lem:tl5-hfp-rec]]; a
smaller factor for them would need bounds that separate the face energies of the words ending in T from those of the
words ending in a rotation, which ℰ_g(p) does not give. The terms of the second kind have one bound u for the seven
fields, and |𝒳_p y| ≤ 𝔨_Γ u for a family y with |y_Z| ≤ u, against √7 K_rec u in [[lem:tl5-hfp-rec]]. The ratio 𝔨_Γ/(√7
K_rec) is 1 at |T|⁻¹ = λ_M^(−1/2); where |T|⁻¹ > λ_M^(−1/2) it lies between 7^(−1/2) and 1 and tends to 7^(−1/2) as
λ_M^(−1/2)/|T|⁻¹ tends to 0, and where λ_M^(−1/2) > |T|⁻¹ it lies between (6/7)^(1/2) and 1. These terms are the
nonlinear part of the bounds of the second derivatives on the face, whose count 301^(1/2) K_rec(p) becomes 43^(1/2) 𝔨_Γ,
the parts with ϱ and the terms on S_a; so the parts with ϱ(p) and η₀(p) of the leading term of the recovery, in
𝔨_rec^(ϱ,k) and 𝔨_rec^(0,k), take 𝔨_Γ in place of √7 K_rec whole. The couplings 𝔄 take the norm 𝔞_𝔄^k of their map with
its components weighted, which is at most K_rec(p) 𝔞_𝔄(Γ). In the recovery at p the terms 𝔷_Z take the weights of their
fields, with 𝔷₁^k ≤ K_rec 𝔷₁′ and 𝔷₂^k ≤ K_rec 𝔷₂′. The recovery at the points of the face, in 𝔩_D(Γ), in k₁ and in the
bounds of the second derivatives, is left as it is; there [[lem:tl5-hfk-rec]] would give its leading term, through the
words Z′JZ, which begin with each of the seven fields, only as a term of the first kind. The counts of the products, the
Sobolev constants, the weights 𝔲₀, 𝔲₁, 𝔲_M, 𝔶₀, 𝔶₁ and 𝔶₀^h, the constants of one word, the thresholds 𝔰₀ and 𝔰₁^v and
the rates are unchanged, and at the levels N ≥ 6 nothing changes. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the
hypotheses of [[thm:tl5-hfk]] are established in this paper for no background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
Old texts are quoted exactly from chapters/87-ten-l5.md at HEAD 5d38849f, where sec:tl5-hff is merged (Section 57.30,
merge becf0eb0). Line numbers serve only to find the place.

*1. Where the section goes.* The section above, from its heading (label sec:tl5-hfk) through the last line of
[[rem:tl5-hfk-what]], is inserted at the end of [[ch:ten-l5]], after the last line of [[rem:tl5-hff-what]] (line 7838,
as changed by item 2), with one blank line before it, as a sibling "###" section. No number already printed changes.

*2. The last sentence of [[rem:tl5-hff-what]] (lines 7836–7837).* Old:

𝔰₁^v and the rates are unchanged. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hff]] are
established in this paper for no background at 10 l5.

New (one line added, of 119 characters; the two old lines are unchanged):

𝔰₁^v and the rates are unchanged. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hff]] are
established in this paper for no background at 10 l5.
[[sec:tl5-hfk]] bounds the recovery of D̂²h at a point at level four through the image under its map ([[thm:tl5-hfk]]).

*3. Nothing else changes.* No earlier text is edited: the sites listed in the Comparison keep their texts, and the new
constants are defined in def:tl5-hfk-constants by reference to them.

### Comparison and the factors for the evaluation

Not chapter text. thm:tl5-hfk acts at N = 4 only, on thm:tl5-hff with route (𝔰), the only route offered there. At the
levels N ≥ 6 nothing changes.

**Containment.** There is no new choice: for all admissible weights and choices every new factor is at most the old one,
so thm:tl5-hfk contains thm:tl5-hff at N = 4, and through it every earlier level-four theorem in the range where
thm:tl5-hff contains it. Exactly where:
- the last claim of thm:tl5-hfk and the last paragraph of its proof;
- 𝔨_Γ ≤ √7 K_rec, 𝔷₁^k ≤ K_rec 𝔷₁′ and 𝔷₂^k ≤ K_rec 𝔷₂′: lem:tl5-hfk-rec (a), from lem:tl5-hf-fields (a) and
  K_rec² = max(|T|⁻², λ_M⁻¹);
- 𝔞_𝔄^k ≤ K_rec 𝔞_𝔄(Γ) and C₁^k ≤ K_rec C₁^(Γ,l): the last paragraph of the proof of lem:tl5-hfk-fam (a diagonal
  multiplication of norm at most K_rec; the integrands of C₁^(U,l), C₁^(D,l), C₁^(J,l) nondecreasing in (43n)^½ and in
  𝔞_𝔄, as k₁^p ≥ k₁^D);
- so 𝔨_rec^(·,k) ≤ 𝔨_rec^(·,p) (index f forms) term by term, and every constant with index f is nondecreasing in them;
- ε^k = ε^f; Y_k ≤ Y_f, the smaller root being nondecreasing in A and in B; 𝔰_*^k ≤ 𝔰_*^f.
Equality holds where |T|⁻¹ = λ_M^(−½) at p, as then both weights of |·|_Γ are K_rec² and 𝔨_Γ = √7 K_rec. The present
closing conditions stay valid beside the new one: no earlier theorem is changed, and thm:tl5-hff (N = 4) is the case
just named.

**Both constraints.** The change enters 𝔨_rec^(·,k), hence C_P^v, C_(P,ϱ)^v and C_(P,0)^v (lem:tl5-hfv-rec). These
enter 𝔰_* through its terms with A, ϱ and η₀, and the closing condition through S_F (𝔣₀C_P,
𝔣₁C_P and 𝔎 = max(C_P⁰𝔨_A, C_P^v𝔨_B), so 𝔎^D) and through 𝔯 (𝔎_ϱ, 𝔎₀, 𝔎^D_ϱ, 𝔎^D₀), so through B_k and η_k, which
enter A_k, Y_k and 𝔰_*^k as well.

Unchanged: all counts of the products (𝔠^♮, 𝔠^D, 𝔠^(D,7), 𝔠^ϱ, 𝔠^Mq), the Sobolev and leaf constants, the
recovery constants at the points of the face (𝔨_♯, K_rec, k₁^D, k₁, k₂^z, 𝔷′), the first-order constants of one word
and of the other families (C₁^l(𝔚), C₁^l, C_(1,ϱ)^l, C_(1,0)^p), C_S^f, C_S^h, C_(0,0)^h, C_P⁰, C_(P,0)⁰, 𝔐_p^(m), the
weights 𝔲₀, 𝔲₁, 𝔲_M, 𝔶₀, 𝔶₁, 𝔶₀^h, θ, ϑ₁, ϑ₂, the functions 𝔨₁, 𝔨₂, 𝔷, 𝔵^z, 𝔤₁, the thresholds 𝔰₀ and 𝔰₁^v with the
cap, the rule of the threshold (Y_k has the form of Y_f), S_M, ε_M, ε and the rates.

1. The scoping, done first, as mathematics (the C₁ term 𝔨_♯K_rec C₁^Γ of 𝔨_rec^p).
   - Where the factor K_rec comes from. In the proof of lem:tl5-hf-recovery (87:4060–4064), X^½ = |𝒳_p(v_Z)_Z| with
     v_Z = D̂ℒ_ZΨ − 𝔷_(Z,·), and only then X^½ ≤ K_rec((Σ|D̂ℒ_ZΨ|²)^½ + (Σ𝔷_Z²)^½). lem:tl5-hfz-rec uses X only through
     that bound (87:6422–6423), and lem:tl5-hfp-rec then bounds (Σ_Z|D̂Ψ_Z(p)|²)^½ by the family bound
     eq:tl5-hfp-family with 𝔚 = Γ (87:6816–6820). So the factor is the operator norm of 𝒳_p applied to a family norm,
     and what the recovery needs is |𝒳_p(D̂Ψ_Z(p))_Z|, the weighted quantity of the question.
   - The route. The coefficients |T(p)|⁻¹ and c^ab_j(p) are numbers, so eq:tl5-hfe-face applies to the four fields
     Ã₀ = |T(p)|⁻¹D̂Ψ_T, Ã_j = Σ c^ab_j(p) D̂Ψ_(K_ab), whose Lie derivatives along J are the same combinations; on the
     face Σ_i|ℒ^JÃ_i|² ≤ |T(p)|⁻²|ℒ^JD̂Ψ_T|² + λ_M(p)⁻¹Σ|ℒ^JD̂Ψ_(K_ab)|² by lem:tl5-hf-fields (a). This needs no new
     energy: the proof of lem:tl5-hfp-c1 runs with a weighted Euclidean norm over the 301 pairs (J, Z).
   - Per-word information that the family estimate threw away, found by going through the proofs of lem:tl5-hfp-c1
     (87:6772–6802) and lem:tl5-hfp-words (87:6744–6758) term by term:
     - first kind, bounds forming a family over the pairs (J, Z) bounded in the Euclidean norm through 𝒟_g, 𝒥_g: the
       leading terms D̂Ψ_(JZ) (87:6775–6776), the remainders R′_(J,Z), D̂R′_(J,Z) (87:6776–6780), the leading term of
       the face recovery through Z′JZ (87:6747–6748), the terms with 𝔷_(Z′) and 𝔯_♯|Ψ_(JZ)| (87:6748–6749). Under the
       weights these take K_rec(p), no more and no less;
     - second kind, one bound per J for all seven Z: the nonlinear part 𝔵^z(k₁^D𝒟_g + (k₁^p − k₁^D + 2)𝒥_g)/(1 − 𝔵^z)
       (87:6751–6754), the part with ϱ 𝔬_J P_C (87:6754–6755), the terms on S_a (87:6796–6801). Under the weights
       they take 𝔨_Γ = (|T|⁻² + 6λ_M⁻¹)^½ in place of √7 K_rec;
     - third kind, the couplings 𝔄 (87:6749–6750): the weighted operator norm 𝔞_𝔄^k ≤ K_rec 𝔞_𝔄(Γ).
   - Correction to the previous scoping (P-GRD15's "Not done", at 7cad931e). It said a weighted family bound "needs
     the face energies split by the last letter of the words". That holds only for a gain on the first kind. The
     first kind is bounded by K_rec(p) times its present bound with no split (|y|_Γ ≤ K_rec|y|), and the second and
     third kinds gain with no split; so the bound with the gain on the second and third kinds is proved here, and only
     the first kind is left. The earlier count "(43|T|⁻² + 258λ_M⁻¹)^½ against 301^½ K_rec" is 43^½𝔨_Γ against
     301^½K_rec, as in lem:tl5-hfk-fam.
   - In the recovery at p itself, the terms 𝔷_Z = 3|D̂Z||D̂h| + 2|D̂²Z||h| depend on Z, so they take
     𝔷₁^k = 3|(|D̂Z|)_Z|_Γ and 𝔷₂^k = 2|(|D̂²Z|)_Z|_Γ (lem:tl5-hfk-rec (b)); the parts with ϱ(p) and η₀(p) of the
     family bound have one bound for the seven fields, so 𝔨_rec^(ϱ,k) and the C_(1,0)^p part of 𝔨_rec^(0,k) take 𝔨_Γ
     in place of √7K_rec whole.
2. The obstruction for the first kind, exactly (not drafted).
   - The quantity those parts need is |T(p)|⁻²E_T + λ_M(p)⁻¹E_R, with E_T and E_R the weighted face energies of the
     words ending in T and in a rotation, of the forms Σ_W μ^|W|∫ε₁[Ψ_W]. Every bound of the chapter enters the face
     energies only through ℰ_g(p): ∫g𝒥_g² ≤ sup(g𝔨₂)ℰ_g(p) and ∫g𝒟_g² ≤ sup(g𝔨₂′)ℰ_g(p) (87:6794), Σ_W μ^|W|∫ε₁[Ψ_W] ≤
     ℰ_g(p) for distinct words (87:7720); then ℰ_g(p) ≤ e^(φ(p))Y_s² (87:7604–7605, 87:7802), Y_s being the one
     bootstrap quantity of Σ_I μ^|I|ℰ_I (Step 3, 87:6241–6243). Given only E_T + E_R ≤ ℰ_g(p), the supremum of
     |T|⁻²E_T + λ_M⁻¹E_R is K_rec²ℰ_g(p), attained with all of it on the words ending in T where |T|⁻¹ > λ_M^(−½). So
     on the information the chapter has, the first kind cannot take a factor below K_rec(p) by this route.
   - What would be needed: a bound of E_T by a fraction of ℰ_g(p) at the supremum, or a bootstrap with weights by the
     last letter, Σ_I w_(ℓ(I)) μ^|I| ℰ_I. In the commuted equation (lem:tl5-hf-system, 87:4028–4031) the commutator
     terms with k < j keep the last letter Z_j; those with k = j carry π^(Z_j) and change it; π^(K₁₂) = π^(K₃₄) = 0
     always and π^Z = 0 for the seed (lem:tl5-hf-fields (b), 87:3940); the nonlinear terms ℒ^I N(h) mix all subwords.
     A weighted bootstrap would carry the ratio of the weights in these couplings and in the products, and would put
     the weights on δ_w and on s_N[2R̂ic]. Where the forcing sits on the words ending in T, A_k grows by the factor by
     which B_k falls (deduced, a sketch), so 4A_kB_k need not fall: this is a restructuring of Steps 2–3 and of
     prop:tl5-hf-linear-n, priced by the split of the energies and of the forcing by last letter, which no report
     measures.
3. The sites, at HEAD 5d38849f, old → new:
   - 87:6675–6677 (def:tl5-hfp-constants, "𝔨_rec^p := 𝔨_♯ K_rec (C₁^Γ + 𝔷₁′ μ^(1/2) C₁^p + 𝔷₂′ μ C_S^p) …", in the
     forms with index f of 87:7755) → eq:tl5-hfk-krec: 𝔨_♯C₁^k, 𝔨_♯𝔨_Γ, 𝔨_♯𝔷₁^k, 𝔨_♯𝔷₂^k in place of 𝔨_♯K_rec C₁^(Γ,l),
     𝔨_♯K_rec√7, 𝔨_♯K_rec𝔷₁′, 𝔨_♯K_rec𝔷₂′;
   - 87:6816–6820 (proof of lem:tl5-hfp-rec, "use [[lem:tl5-hfz-rec]] for h at p … Bound μ² (Σ_Z |D̂Ψ_Z|²)^(1/2) by
     [[eq:tl5-hfp-family]]") → eq:tl5-hfk-rec and eq:tl5-hfk-fam;
   - the constants formed from C_P^v, C_(P,ϱ)^v, C_(P,0)^v (87:6199–6200 in their index-f forms; 𝔎, 𝔎_ϱ, 𝔎₀ at
     87:5655; 𝔎^D at 87:7197–7198; S_F, 𝔯, 𝔰_*) → index k.
4. The closing condition eq:tl5-hfk-closing is eq:tl5-hff-closing with the constants with index k; it also defines
   Y_k, through 4A_kB_k < 1.

What it gives, deduced, not evaluated; upper figures. Assumptions:
- every supremum at one point: each fall below is that of the leading entry at its supremum, the point where G0q
  measured it; with the new constants the supremum, or the leading entry, may move, so the figures are upper figures;
- the G0q figures are on P-GRD14 (sec:tl5-hfc), before P-GRD15, which G0r is evaluating; the 𝔵^z are G0p's, on
  P-GRD13.
The factor at the supremum of 𝔨_rec^p (G0q §G0q.2 item 2, seed 1 D_A / seed 2 D_A / seed 1 D* / seed 2 D*).
- |T|⁻¹ = 1.098 / 1.088 / 1.578 / 1.371 and λ_M^(−½) = 0.380 / 0.399 / 0.866 / 0.757, so K_rec = |T|⁻¹ (the T part).
- 𝔨_Γ/(√7K_rec) is G0q's "equal shares" ratio, 0.495 (−0.31) / 0.508 (−0.29) / 0.633 (−0.20) / 0.636 (−0.20): the
  exact factor of the second kind and of 𝔨_rec^(ϱ,k)'s and 𝔨_rec^(0,k)'s 𝔨_Γ-parts there. λ_M^(−½)/K_rec is G0q's
  "floor" ratio, 0.346 (−0.46) / 0.367 (−0.44) / 0.549 (−0.26) / 0.552 (−0.26), the least possible factor of 𝔞_𝔄^k.
- So C₁^k/(K_rec C₁^(Γ,l)) lies between the floor ratio and 1; it is at least the equal-shares ratio wherever the part
  with 𝔞_𝔄 is negligible, and equals it only if all of C₁^(Γ,l) were of the second kind. The fall of the C₁ term is at
  most 0.31 / 0.29 / 0.20 / 0.20 decades, or 0.46 / 0.44 / 0.26 / 0.26 if the couplings led it; the first kind keeps
  its size. The C₁ term is 95.8 / 94.2 / 98.6 / 98.0 % of 𝔨_rec^p there (the rest is the 𝔷₁ term, which falls by at
  most the floor figure), so 𝔨_rec^k falls by at most about the first figures (0.311 at seed 1 D_A with the 𝔷₁ term at
  the floor), and by at most the second in all cases.
- A deduced figure for the split (G0p §G0p.0, 𝔵^z = 0.068 / 0.047 / 0.109 / 0.122 at G0p's level-4 optima): in
  𝔩_D(Γ) = k₁^D(1 + u), u = 301^½𝔵^z/(1 − 𝔵^z) = 1.27 / 0.86 / 2.12 / 2.41, the nonlinear part is 0.56 / 0.46 / 0.68
  / 0.71 of the whole, and 1 + u → 1 + 0.495u etc. is a fall of 0.14 / 0.11 / 0.13 / 0.13 decades of 𝔩_D(Γ). 𝔩_J(Γ)'s
  nonlinear part u(k₁^p − k₁^D + 2) falls by the full equal-shares figure; its share is not reported. With 𝔲₁ at its
  pointwise optimum the bracket of C₁^(U,l) is 2(XY)^½ (rem:tl5-hfe-what), so where 2𝔲₁⁻¹|∂_γ|²𝔩′² leads Y the fall of
  C₁ is half that of 𝔩′ = 𝔩_D + 𝔩_J + (2ϖ′)^½, and with 𝔲₁ = 1 all of it. The evaluation may re-choose 𝔲₁ for C₁^k;
  any 𝔲₁ is admissible, but it is one function for all first-order steps.
Through the theorem, at level 4 (G0q §G0q.2 items 1 and 3).
- The gain is nondecreasing in the fall. Alone, on the P-GRD14 constants: at most G0q's price of the C₁ term ÷ 2
  (a fall of 0.30), +0.09 / +0.24 / +0.06 / +0.29. At seed 1 that price is already capped by 𝔤₁C_S, which takes the
  supremum back once 𝔨_rec^p has fallen by 0.098 / 0.185 (sup 𝔨_rec^p over sup 𝔤₁C_S, item 1), so a larger fall gives
  no more there; at seed 2 the falls above are at most 0.29 (D_A) and 0.26 (D*), unless the part with 𝔞_𝔄 leads
  C₁^(Γ,l) at seed 2 D_A (up to 0.44, not priced).
- With C_P⁰ lowered by 0.30 as well (P-GRD15's lever 3a, C_S ÷ 2 in G0q): at most G0q's price of both together,
  +0.26 / +0.25 / +0.30 / +0.29. A larger fall of C_P⁰ is not priced; how far C_P⁰ falls at the supremum is G0r's
  measurement.
- The parts with ϱ(p) and η₀(p): 𝔨_rec^(ϱ,k) and the C_(1,0)^p part of 𝔨_rec^(0,k) fall on their parts with 𝔨_Γ by
  the equal-shares figure at that point, 0.31 / 0.29 / 0.20 / 0.20, and enter C_(P,ϱ)^v, C_(P,0)^v, the terms of 𝔰_*
  with ϱ and η₀, and 𝔎_ϱ, 𝔎₀. Not priced; G0q §G0q.1 has ϱ 0.04–0.44 above f, with f binding.
- At level 6: nothing (the theorem is at N = 4).

The optional levers.
- |H| ≤ |h|/(1 − |h|) in place of 𝔤₁: not drafted. Under 𝔰 ≤ 𝔰_♭ it gains (1 + 2𝔰_♭)(1 − 𝔰_♭) ≤ 1 + 𝔰_♭, at most
  0.0043 decades at 𝔰_♭ = 10⁻² and 4 × 10⁻⁵ at 10⁻⁴ (G0q's level-4 optima take 10⁻⁴ / 10⁻⁴ / 10⁻² / 10⁻⁴), and 𝔤₁
  pays 0 at level 6 (G0q §G0q.0). Every site of lem:tl5-hfc-h would carry it.
- The 𝔨₁ Cauchy–Schwarz sharpening: not drafted. A weighted Cauchy–Schwarz in |D̂_(∂_γ)B|² ≤ 3(…) (87:4189–4190)
  lowers 𝔨₁ by at most the factor 3, which with the optimal 𝔲₀ moves C_S by at most ¼ log₁₀ 3 = 0.12 decades; at level 4
  C_S does not hold sup C_P^v (𝔨_rec^p does, by 0.10–0.52, G0q §G0q.2 item 1), and at level 6 it acts through
  𝔐_p^(2), whose split G0r is measuring.
- Level 6, the family term k₁𝔐_p: not drafted; scoped under "Not done".

Not done (P-GRD17 if the evaluation leaves room).
- The first kind: see 2 above. A bound of the face energy of the words ending in T apart from those ending in a
  rotation, or a bootstrap weighted by the last letter; neither exists in the chapter.
- Level 6, the recovery at low levels term by term. In the step on second derivatives at low levels
  (lem:tl5-hfg-linfty, 87:5185–5193; lem:tl5-hfs-linfty, 87:5585–5590; lem:tl5-hft-small (a), 87:5873–5878;
  lem:tl5-hfp-low, 87:6822–6834) every first-order term of the recovery of D̂²Ψ_B(p), |B| ≤ m, is bounded by L_g, the
  norm of all words of length at most m + 1, with the total coefficient k₁^(m); that is the entry k₁𝔐_p^(m). The
  leading term needs only the seven words ZB, for which eq:tl5-hfk-fam (with 𝔚 = {ZB : Z ∈ Γ}, b = |B| + 1 ≤ N − 3,
  the same proof) gives 𝔨_♯C₁^k({ZB}); the terms with 𝔷 and 𝔯_♯ need only Ψ_B and D̂Ψ_B, bounded by C_S^f, C₁^l as
  in lem:tl5-hfv-rec; only the couplings, (1 − 𝔰₁^v)⁻¹α_𝔄^(m,μ), need the jets of the shorter words, through L_g. So
  k₁𝔐_p^(m) could become max_B [𝔨_♯(C₁^k({ZB}) + 𝔷₁^kμ^½C₁^l + 𝔷₂^kμC_S) + (1 − 𝔰₁^v)⁻¹μ𝔯_♯C_S] +
  (1 − 𝔰₁^v)⁻¹α_𝔄^(m,μ)𝔐_p^(m), with the parts with ϱ and η₀ likewise, in C_(∞,μ)^(m), C_((∞,ϱ),μ)^(m) and
  C_((∞,0),μ)^(m) for both options of def:tl5-hft-constants. Not drafted: it is a restatement of the level-6 step for
  both options and of three constants, not cheap. Its worth: G0q has k₁𝔐_p leading C_P^v at every level-6 point,
  0.79 / 1.20 / 1.01 / 1.39 above sup 𝔤₁C_S (§G0q.2 item 1), and 𝔰_* setting ε 3.45–5.82 decades below the closing
  (§G0q.0), so a fall of the entry passes to ε; G0p §G0p.4 has 𝔐_p^(2)/C₁ = 0.92–1.29 decades at x = 0.05. The
  deciding numbers, not reported: the share of (1 − 𝔰₁^v)⁻¹α_𝔄 in k₁ at level 6, and C₁^l({ZB}) against 𝔐_p^(2).
- The rotation part of 𝔨_Γ² could be taken as min(6λ_M⁻¹, Σ_(ab,cd)|Σ_j c^ab_j c^cd_j|), as |Σ_ab c^ab_j y_ab|²
  summed over j is Σ_(ab,cd)(Σ_j c^ab_j c^cd_j)⟨y_ab, y_cd⟩; as 𝔨_Γ ≥ |T|⁻¹, it is worth at most log₁₀(𝔨_Γ|T|) on the
  second kind (0.12 / 0.13 / 0.22 / 0.23 decades at G0q's points). Not drafted.
- The terms 𝔷 of the recovery at the points of the face (k₁^D𝔷′ in 𝔩_J and k₁): lem:tl5-hfk-rec at q gives
  𝔷^k(q) ≤ K_rec(q)𝔷′(q) there too, a part with the factor μ^½; not drafted.

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hfk	paper/reader/proofs/P-GRD16.md@PENDING:1	P-GRD16, section	new; at the end of ch:ten-l5, after rem:tl5-hff-what; N = 4: the recovery of D^2 h at p through the image under its map X_p of the seven fields, bounded by the Sobolev inequality of the face for the four fields that X_p makes; K_rec(p) on the terms bounded in the Euclidean norm, k_Gamma = (|T|^-2 + 6 lambda_M^-1)^(1/2) in place of sqrt7 K_rec on the terms with one bound for the seven fields, the couplings through their weighted map
    lem:tl5-hfk-rec	paper/reader/proofs/P-GRD16.md@PENDING:23	P-GRD16, Lemma	X_p, |.|_Gamma, k_Gamma, z_1^k, z_2^k; |X_p x| <= |(|x_Z|)|_Gamma <= K_rec |x|; the recovery of lem:tl5-hfz-rec with |X_p (D L_Z Psi)_Z| + z_1^k |D Psi| + z_2^k |Psi| in place of K_rec ((sum |D L_Z Psi|^2)^(1/2) + (sum z_Z^2)^(1/2))
    eq:tl5-hfk-rec	paper/reader/proofs/P-GRD16.md@PENDING:37	P-GRD16, display	new
    lem:tl5-hfk-fam	paper/reader/proofs/P-GRD16.md@PENDING:57	P-GRD16, Lemma	N = 4: |X_p (D Psi_Z(p))_Z| <= mu^(-2) C_1^k E_g(p)^(1/2) + k_Gamma (w C_(1,rho)^l rho(p) + E_0); C_1^k = K_rec(p) C_1^l(Gamma) with 43^(1/2) k_Gamma/K_rec for 301^(1/2) and a_A^k/K_rec for a_A(Gamma); a_A^k <= K_rec a_A(Gamma), C_1^k <= K_rec C_1^(Gamma,l)
    eq:tl5-hfk-fam	paper/reader/proofs/P-GRD16.md@PENDING:66	P-GRD16, display	new
    def:tl5-hfk-constants	paper/reader/proofs/P-GRD16.md@PENDING:115	P-GRD16, Definition	constants with index k (N = 4, route (s)): k_rec^k, k_rec^(rho,k), k_rec^(0,k) in place of k_rec^p, k_rec^(rho,p), k_rec^(0,p) in their forms with index f, in C_P^v, C_(P,rho)^v, C_(P,0)^v and every constant formed from these; eps^k = eps^f; eta_k, A_k, B_k, Y_k, s_*^k
    eq:tl5-hfk-krec	paper/reader/proofs/P-GRD16.md@PENDING:122	P-GRD16, display	k_rec^k = k_sharp (C_1^k + z_1^k mu^(1/2) C_1^l + z_2^k mu C_S^h) + (1 - s_1^v)^(-1) mu r_sharp C_S^h; k_rec^(rho,k) = k_sharp (k_Gamma + z_1^k mu^(1/2)) C_(1,rho)^l; k_rec^(0,k) = k_sharp ((k_Gamma + z_1^k mu^(1/2)) C_(1,0)^p + z_2^k mu C_(0,0)^h) + (1 - s_1^v)^(-1) mu r_sharp C_(0,0)^h
    eq:tl5-hfk-constants	paper/reader/proofs/P-GRD16.md@PENDING:137	P-GRD16, display	new
    thm:tl5-hfk	paper/reader/proofs/P-GRD16.md@PENDING:139	P-GRD16, Theorem	N = 4: thm:tl5-hff (route (s)) with the constants with index k; Y_sigma <= Y_k; its hypotheses are implied by those of thm:tl5-hff at N = 4
    eq:tl5-hfk-closing	paper/reader/proofs/P-GRD16.md@PENDING:143	P-GRD16, display	closing condition: 4 eta_k^(-3/2)(delta_w + eta_k^(-1/2)(eps^k + eps_M^k))(S_F^k + S_M^k) < 1
    rem:tl5-hfk-what	paper/reader/proofs/P-GRD16.md@PENDING:177	P-GRD16, Remark	what changes
