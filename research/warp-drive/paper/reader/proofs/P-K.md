### The order of the data and of the approximant {#sec:uc-data-order}

[[thm:settling]] builds g_λ with an approximant of order K = d_1 + 14, d_1 the regularity of [[thm:iii-k-4-3]], and
[[thm:own-data]] takes k1 := max(8, d_1 + 4), M := 15 + 2(k1 + 1) and K > max(d_1 + 14, K*(a, M, k1)). The proof of
[[thm:iii-k-3-2]] takes d_1 := max(d_0, N_NM + k″) with k″ := d + 3 + k′_(N_NM+d+3), where d is the loss with which it
applies [[thm:ii-g-2-1]], N_NM = 21d + 6, d_0 is the regularity of [[prop:iii-k-1-2]], and k + k′_k is the order at
which [[prop:iii-k-1-2]] (3) reads the data to bound the initial family at the order k + 2. Its proof gives d_0 as the
largest, and k′_k as the sum, of finitely many orders of derivatives, and does not evaluate them. This section counts
those orders ([[lem:uc-data-losses]]) and evaluates d_0, k′_k, d_1, K, k1 and K* in terms of d
([[prop:uc-data-order]]). The count holds at every choice of the parameters of [[thm:vi-c-2-1]]. The numbers that
follow from it use the upper bound for d at the computational point, which lies outside the set on which
[[thm:settling]] is proved ([[rem:ec-point-outside]]).

*Conventions.* ‖·‖_n is the norm ‖(γ̃, k̃)‖_(H^n) of [[sec:s27-class]], built from ℰ_0 of [[eq:vii-0-1]] or from ℰ_0^½
of [[eq:half-class]]. Put L_F := 132 = 153 − 21: the data of [[thm:iv3-2-2]] and of [[thm:iv2-3-1]] at the order 153 + k
control the solution at the order 21 + k. For quantities A and B that depend on the data (γ̃, k̃) of
[[prop:iii-k-1-2]], and possibly on (S, S⁰) with |S| + |S⁰| ≤ σ_0, we say that *A at the order m controls B at the order
n* if for every η > 0 there is s > 0 such that, for all data small in H^(d_0) as [[prop:iii-k-1-2]] asks, the norm of
A of order m below s gives the norm of B of order n below η, for all such (S, S⁰); the norms are named in each case.
Control composes: if A at the order m controls B at the order n, and B at the order n controls C at the order q, then A
at the order m controls C at the order q. As the norms are non-decreasing in the order, A at the order m controls A at
every order n ≤ m. *The data at the order m* means (γ̃, k̃) with the norm ‖·‖_m.

*The spaces.* On 𝒟⁺ let 𝒜^n := H^(n,ℓ^♭_0,(−,ℓ^♭_I))_b(𝒟⁺), normed by decompositions as in [[sec:iv3-1]], and
ℬ^n := H^(n,(ℰ_0,ℓ_0),⟨ℰ^C_I⟩,ℓ_I)_b(𝒟⁺), the class of [[cor:iv3-2-3]]. For pairs of Cauchy data on Σ^IVP, with the sum
of the two norms, let 𝒜^n_Σ := H^(n,ℓ^♭_0)_b(Σ^IVP) and ℬ^n_Σ := H^(n,(ℰ_0,ℓ_0))_b(Σ^IVP); ℬ^n_Σ lies continuously in
𝒜^n_Σ, as ℓ^♭_0 < 2 = min Re ℰ_0. Let 𝒪_𝒟 := 𝒟 ∩ 𝒪, where 𝒪 = {|t_IVP| < 2c′r} is the set of the proof of (1) of
[[prop:iii-k-1-2]]: a neighbourhood of Σ^IVP in 𝒟 that contains φ_(S,S⁰)(𝒰′), so a neighbourhood of φ_(S,S⁰)(Σ^IVP),
for |S| + |S⁰| small. Near infinity t is at most C + r/8 on 𝒪, so 𝒪 stays away from ℐ⁺, and we put
𝒜^n(𝒪_𝒟) := H^(n,ℓ^♭_0)_b(𝒪_𝒟) and ℬ^n(𝒪_𝒟) := H^(n,(ℰ_0,ℓ_0))_b(𝒪_𝒟), with weights and expansions at I₀ only.
We write h_0 := h_(0,0), (h⁰, h¹) := (h⁰_(S,S⁰), h¹_(S,S⁰)), and ∂ and ∂² for all first and second derivatives in the
finitely many parameters (S, S⁰).

*The numbers L_0, J and L_P.* Step 1 of the proof of [[thm:iii-c1-3-1]] raises the weight at I₀ in steps. A step from
the weight α₀ to α₁ := min(α₀ + 1, ℓ₀) applies R = Π_((z,k)∈ℰ_(0,≤))(X₀ − z), where ℰ_(0,≤) is the set of the (z, k) ∈
ℰ₀ with Re z ≤ α₁; let p := |ℰ_(0,≤)| be its number of factors. With p_1, p_2, … these numbers at the successive steps,
put L_0 := Σ_i (p_i + 6). Let J be the number of repetitions of Step 2 of that proof, and L_P := L_0 + 2J. The same
steps run on 𝒟⁺ in the proof of [[cor:iv3-2-3]].

**Lemma {#lem:uc-data-losses}** (The orders that the initial family reads.) Let the parameters be chosen as in
[[thm:vi-c-2-1]], with ℰ_0 of [[eq:vii-0-1]] or of [[eq:half-class]]. Uniformly for |S| + |S⁰| ≤ σ_0, and for n as
stated:

(i) (gauged data) the data at the order n + 1 control (h̊_0, h̊_1) in ℬ^n_Σ, for n ≥ 3;

(ii) (the three solutions) Cauchy data in 𝒜_Σ at the order max(n, 21) + L_F control the solution of [[thm:iv3-2-2]] for
these data in 𝒜^n; (h̊_0, h̊_1) in 𝒜_Σ at the order max(n, 21) + L_F control the solution of [[thm:iii-c1-2-1]] for their
restriction to Σ_(IVP,r_ext) in H^(n,ℓ^♭_0,(−,ℓ^♭_I))_b(Ω_(ext,r_ext)); and (h̊_0, h̊_1) in H^n × H^n on Σ^IVP ∩ 𝔒⁻
control h_0 in H^n(𝔒⁻), for n ≥ 5;

(iii) (the expansion at I₀, n ≥ 1) Step 1 has at most three steps, L_0 ≤ 23, and L_0 ≤ 28 for ℰ_0^½; the triple
(h_(S,S⁰), ∂h_(S,S⁰), ∂²h_(S,S⁰)) in 𝒜^(n+L_0), with the triple ((h⁰, h¹), ∂(h⁰, h¹), ∂²(h⁰, h¹)) of its data in
ℬ^(n+L_0)_Σ, controls the triple in H^(n,(ℰ_0,ℓ_0),(−,ℓ^♭_I))_b(𝒟⁺); and the solution of [[thm:iii-c1-2-1]] in
H^(n+L_0,ℓ^♭_0,(−,ℓ^♭_I))_b(Ω_(ext,r_ext)), with its data in ℬ^(n+L_0)_Σ, controls it in
H^(n,(ℰ_0,ℓ_0),(−,ℓ^♭_I))_b(Ω_(ext,r_ext));

(iv) (the expansion at ℐ⁺, n ≥ 3) J ≤ 4(ℓ_I − ℓ^♭_I) + 1, and the triple in H^(n+2J,(ℰ_0,ℓ_0),(−,ℓ^♭_I))_b(𝒟⁺)
controls it in ℬ^n;

(v) (pull-back) for l ≤ 2, h_0 in 𝒜^(n+2+l)(𝒪_𝒟) controls ∂^l(h⁰, h¹) in 𝒜^n_Σ, and h_0 in ℬ^(n+4+l)(𝒪_𝒟) controls
∂^l(h⁰, h¹) in ℬ^n_Σ;

(vi) (the derivatives in (S, S⁰)) for n ≥ 4, h_(S,S⁰) in 𝒜^(n+7) and ∂(h⁰, h¹) in 𝒜^(n+4)_Σ control ∂h_(S,S⁰) in 𝒜^n;
and h_(S,S⁰) in 𝒜^(n+7), ∂h_(S,S⁰) in 𝒜^(n+6) and ∂²(h⁰, h¹) in 𝒜^(n+4)_Σ control ∂²h_(S,S⁰) in 𝒜^n.

*Proof.* (i) In the proof of [[prop:iii-c2-4-1]], h̊_0 = γ̃, extended to S²T* by h̊_0(ν_(b₀), ·) := 0, a linear map
with smooth coefficients, bounded on every H^(n,(ℰ₀,ℓ₀))_b. And h̊_1 = rh̃₁, where h̃₁ is determined algebraically by
the first equation at (e_i, e_j) and the e^j- and e⁰-components of the second, whose right sides are k̃ and the
contractions of ∇^(g₀) − ∇^(g_(b₀)) with ν₀ and g₀; their coefficients are smooth functions of the components of g₀ =
g_(b₀) + h̊_0 and of the frame, which is a smooth function of g₀. ∇^(g₀) − ∇^(g_(b₀)) is g₀⁻¹ times first derivatives
of h̊_0 plus Christoffel symbols of g_(b₀) times h̊_0, and an x-derivative is r⁻¹ times a b-derivative. So h̊_1 is a
smooth function of the point, of γ̃ and its first b-derivatives and of k̃, vanishing at 0, linear in k̃ and in the
first b-derivatives of γ̃. On Σ^IVP, of dimension 4, the products of [[lem:iii-c-2-1]] at the order n ≥ 3 > 2, with a
Neumann series for g₀⁻¹ as in Step 1 of the proof of [[prop:iii-c-4-4]] and Taylor expansions of the other smooth
functions of g₀ at g_(b₀), whose terms are such products, bound h̊_1 in H^(n,(ℰ₀,ℓ₀))_b by a quantity that tends to 0
with ‖(γ̃, k̃)‖_(n+1), the index sets being closed under sums and positive multiples (row d1 of [[sec:vi-c-1]]). The
weight and the index set of k̃ are those of h̃₁, one above those of h̊_1.

(ii) By the last clause of [[thm:iv3-2-2]] with k := max(n, 21) − 21, data with ‖h_j‖_(H^(153+k,ℓ^♭_0)_b) < ε_1 give
‖h‖_(H^(21+k,ℓ^♭_0,(−,ℓ^♭_I))_b) < ε, and 21 + k ≥ n. Its constants and thresholds depend on the background
φ_(S,S⁰)^*g_(b₀) only through bounds uniform for |S| + |S⁰| small (*The modulus* in the proof of
[[prop:iii-k-1-2]]). [[thm:iii-c1-2-1]] takes its solution, in the cut-off gauge ([[cor:iv2-4-1]]), from
[[thm:iv2-3-1]], whose last clause has the same orders. For the backward solution, (N) of [[sec:s27-local]] states that
it tends to 0 in H^(r+1)(𝔒⁻) as the data tend to 0 in H^(r+1) × H^r; take r := n − 1 ≥ 4.

(iii) *The number of steps.* ℓ^♭_0 = 3/2 + ½(1 − e_Υ)γ_Υ lies in (3/2, 13/8), as 0 < e_Υ < 1 and γ_Υ < ¼. In both
classes Re π₁ℰ₀ ⊂ ½ℤ, while ℓ^♭_0 + 1 ∈ (5/2, 21/8) and ℓ^♭_0 + 2 ∈ (7/2, 29/8) are not in ½ℤ, and ℓ₀ ∉ Re π₁ℰ₀; so
Step 1 never lowers α₀. Its first step gives α₁ = ℓ^♭_0 + 1 < 3, its second α₁ = min(ℓ^♭_0 + 2, ℓ₀) < 4, and, if
ℓ^♭_0 + 2 < ℓ₀, a third gives α₁ = ℓ₀ < 4, as ℓ^♭_0 + 3 > 4 > ℓ₀. ℰ_0 of [[eq:vii-0-1]] has the exponents 2, 3, 4, …,
without logarithms, so p ≤ 1, 2, 2 at the three steps and L_0 ≤ 7 + 8 + 8 = 23; ℰ_0^½ has the exponents 2, 5/2, 3,
7/2, …, without logarithms, so p ≤ 2, 4, 4 and L_0 ≤ 8 + 10 + 10 = 28.

*One step.* Let a step go from α₀ to α₁ with p factors, and let j ≥ 1. The step obtains Rh from the linear estimate
[[eq:iii-c1-2-2]] at h = 0, with α₁ in place of α₀ (on 𝒟⁺, [[eq:iv2-2-3]] of [[thm:iv3-2-1]] at h = 0, with
α_0 := α₁), whose loss is 4: Rh in H^(j,α₁,(−,ℓ^♭_I))_b is controlled by L(Rh) in the forcing class at the order j + 4
and by the Cauchy data of Rh in H^(j+4,α₁)_b(Σ^IVP), where L = L_(g_(b₀)) on the exterior and L = L^(χ^♮_0)_(g_0,g_0) on
𝒟⁺, g_0 = φ_(S,S⁰)^*g_(b₀). The forcing is ρ₀²R(ρ₀⁻²Lh) + ρ₀²[ρ₀⁻²L, R]h. In the first term R has order p, and Lh is
−∫₀¹(L_(g_0+sh,g_0) − L)h ds, a second-order operator whose coefficients are smooth functions of h and of its first two
derivatives, vanishing at h = 0 ([[prop:iii-c-4-4]]), applied to h; by [[lem:iii-c-2-1]] at the order j + 4 + p ≥ 3 it
is controlled by h at the order j + 6 + p. The commutator has order p + 1, and its action on the expansion terms h_e of
h, written −RAh_e in that proof, reads them at the order j + 6 + p. The data of Rh are formed by R and rℒ_(∂_(t_IVP))
from the jet of h on Σ^IVP of order at most p + 1 (its b-derivatives of total order at most p + 1). The equation is
non-characteristic on Σ^IVP: solved for the second transversal derivative and differentiated, it gives the jet of order
q ≥ 2 as a smooth function of the point and of the jet of order q − 1, polynomial in the b-derivatives along Σ^IVP of
order at most q of h₀ and at most q − 1 of h₁, with coefficients in C^∞ + H^(∞,(ℰ₀,ℓ₀))_b. So, by [[lem:iii-c-2-1]] on
Σ^IVP, the data (h₀, h₁) in ℬ_Σ at the order j + 5 + p control the data of Rh in H^(j+4,(ℰ₀,ℓ₀))_b(Σ^IVP); these have no
expansion terms of real part at most α₁ (the proof of [[thm:iii-c1-3-1]]), so their norm in H^(j+4,α₁)_b(Σ^IVP) is at
most a constant times that norm. The direct part of [[lem:iii-a-1-3]] loses nothing (the last paragraph of its proof):
from Rh at the order j, and from h at the order j away from I₀, it gives h at the order j with its expansion at I₀ up to
α₁, the coefficients in H^j. Every bound tends to 0 with its inputs: the estimates are linear, and Lh is quadratic in h.
So h at the order j + p + 6 in the class of weight α₀, with its data at the order j + p + 5 in ℬ_Σ, controls h at the
order j in the class of weight α₁.

For ∂h and ∂²h the step is the same, for the linear equations of (vi) below: the forcing F₁ or F₂ is added to the
quadratic term, and it carries a factor of h or of ∂h with at most two of its derivatives, of the weight that the step
uses ([[eq:iii-c-5-2]], as in the proof of [[thm:iii-c2-3-1]] (2)); at the order j + 4 + p it reads those factors at the
order j + 6 + p, in the class of the step. The jets of ∂h and ∂²h on Σ^IVP are given by their data, by the linearised
equations and by the jets of h and ∂h, in the same way. So the triple at the order j + p + 6 in the class of weight α₀,
with the triple of data at the order j + p + 5, controls the triple at the order j in the class of weight α₁. Over the
steps the orders add up to L_0, which gives (iii) on 𝒟⁺, and on Ω_(ext,r_ext) for the solution of [[thm:iii-c1-2-1]].

(iv) The bound for J is part of Step 2 of the proof of [[thm:iii-c1-3-1]]. In one repetition the right side f̃ of
[[eq:iii-c1-3-5]] at an order j ≥ 3 reads h at the order j + 2 ([[lem:iii-c-2-1]] asks the order of a product above
5/2): R̃_b ∈ ρ₀²ρ_I²C^∞Diff²_b, and the second term is a second-order operator with coefficients in h and its first two
derivatives applied to h ([[prop:iii-c-4-4]], [[lem:iii-c-2-1]]). w = (X₀ − X_I)h at the order j reads h at the order
j + 1 ((F1) of [[sec:iii-a-1]]). The integrations of [[lem:iii-a-1-2]] and [[lem:iii-a-3-2]] lose nothing: each holds
with the same order k in its hypothesis and its conclusion, and its a priori hypothesis away from the face asks the
same order. So h at the order j + 2 in the class of weight α_I controls h at the order j in the class of weight α′. For
∂h and ∂²h the forcing of (vi) enters f̃ with its factors read at the order j + 2 in the class of the repetition. J
repetitions give (iv).

(v) φ := φ_(S,S⁰) = ψ_(S⁰) ∘ φ_S, φ_S and ψ_(S⁰) being the time-1 flows of b-vector fields that depend linearly on the
parameters and are tangent to every boundary hypersurface ([[lem:s27-translated-exterior]] (a), the proof of
[[lem:s27-boost-move]]). For a family φ_s of diffeomorphisms smooth in s, ∂_s(φ_s^*u) = φ_s^*(ℒ_(X_s)u) with
X_s := (∂_sφ_s) ∘ φ_s⁻¹. For the time-1 flow of a field V that depends smoothly on s, X_s = ∫₀¹ (Φ_(1−t))_*(∂_sV) dt,
Φ_t the flow of V; for a composite the fields of the factors add, the inner one pushed forward by the outer map. The
push-forward of a b-vector field by these maps is a b-vector field, so X_s is one. So ∂^l(φ^*h_0) is a sum of terms
φ^*(ℒ_(Y_1)⋯ℒ_(Y_i)h_0), i ≤ l, with b-vector fields Y_1, …, Y_i smooth in the parameters, and each Lie derivative
costs one order ((F1) of [[sec:iii-a-1]]). Pull-back by
φ is bounded on H^(j,ℓ^♭_0)_b near Σ^IVP, uniformly in (S, S⁰) ([[lem:s27-translated-exterior]] (c), the proof of
[[thm:iii-c2-3-1]]; on the compact part φ is a diffeomorphism smooth in (S, S⁰)); restriction to Σ^IVP costs one
order, and rℒ_(∂_(t_IVP)), a first-order b-differential operator near Σ^IVP, one more (the proof of
[[thm:iii-c2-3-1]]). The data (φ^*h_0)|_(Σ^IVP) and rℒ_(∂_(t_IVP))(φ^*h_0)|_(Σ^IVP) read h_0 on φ(𝒰′) ⊂ 𝒪_𝒟. This
gives the claim in 𝒜.

In ℬ, pull-back costs at most two orders more. Near I₀ write φ in a collar as (ρ₀, y) ↦ (ρ₀α(ρ₀, y), Y(ρ₀, y)), with α
positive and α, Y smooth up to ρ₀ = 0 (φ is smooth on M and preserves I₀). For a term χ(ρ₀)ρ₀^z u_z(y) of the
expansion of u ∈ H^(j,(ℰ₀,ℓ₀))_b, z ∈ π₁ℰ₀ and so z ≥ 2, Taylor's formula in ρ₀ at fixed y gives
α^z u_z(Y) = c_0 + ρ₀c_1 + ρ₀²c_2(ρ₀, y), where c_0 = α(0, ·)^z u_z(Y(0, ·)), c_1 contains first derivatives of u_z,
and c_2 is an integral of terms with at most two derivatives of u_z, all with smooth coefficients. So the pulled-back
term is ρ₀^z c_0 + ρ₀^(z+1)c_1 + ρ₀^(z+2)c_2, up to a cut-off supported away from I₀. The pairs (z, 0) and (z + 1, 0)
lie in ℰ₀, and the term ρ₀^(z+2)c_2, of weight z + 2 ≥ 4 > ℓ₀, lies in H^(j−2,ℓ₀)_b, as does the term at z + 1 when
z + 1 > ℓ₀; the remainder of the expansion is pulled back boundedly. So pull-back maps H^(j,(ℰ₀,ℓ₀))_b to
H^(j−2,(ℰ₀,ℓ₀))_b near Σ^IVP, uniformly in (S, S⁰), and the Lie derivatives, the restriction and rℒ_(∂_(t_IVP)) cost
as before.

(vi) By the proof of [[prop:iii-k-1-2]] (3), the derivative ḣ of h_(S,S⁰) in a direction of (S, S⁰) solves on 𝒟⁺

    Lḣ = F₁ := −[(D₁ + D₂)P^♮(g_0 + h, g_0) − (D₁ + D₂)P^♮(g_0, g_0)]ġ_0,     L := L^(χ^♮_0)_(g_0+h,g_0),

with h := h_(S,S⁰), g_0 := φ_(S,S⁰)^*g_(b₀), ġ_0 its derivative in that direction and the differentiated data. By
[[thm:iv3-2-1]] with α_0 := ℓ^♭_0 and [[eq:iv2-2-3]] at the order n,

    ‖ḣ‖_(𝒜^n) ≤ C(N(F₁, ∂(h⁰, h¹); n + 4) + ‖h‖_(𝒜^(n+7)) N(F₁, ∂(h⁰, h¹); 8)),

with C uniform for h small in 𝒜^10 and for |S| + |S⁰| small; for n ≥ 4 the orders 8 and 10 are at most n + 4 and n + 7.
F₁ is linear in ġ_0, which is smooth with the slots of ρ₀²ρ_I²C^∞ ([[lem:s27-translated-exterior]] (b) differentiated
in (S, S⁰)), with coefficients that carry a factor of h and are smooth functions of the point, of g_0 and of h and its
first two derivatives; so in the forcing class at the order n + 4 it is controlled by h at the order n + 6, by the
Moser estimates of part (ii) of the proof of [[thm:iv3-2-2]]. This is the first claim. The derivative ḧ in two
directions e, f solves Lḧ = F₂ := ∂_fF_(1,e) − (∂_fL)ḣ_e with the twice differentiated data, where ∂_fL is a
second-order operator whose coefficients involve ḣ_f with at most two of its derivatives, ġ_0 and its derivative, and h
and its first two derivatives. So F₂ at the order n + 4 is controlled by ∂h and h at the order n + 6, and
[[eq:iv2-2-3]] gives the second claim. ∎

**Proposition {#prop:uc-data-order}** (The regularity d_1 and the order of the approximant.) Let the parameters be chosen
as in [[thm:vi-c-2-1]], let d be the loss with which [[thm:iii-k-3-2]] applies [[thm:ii-g-2-1]], N_NM = 21d + 6, and
let L_P = L_0 + 2J be as in [[lem:uc-data-losses]] for the class in question.

(a) [[prop:iii-k-1-2]] holds with d_0 := 309, and its part (3) holds with k′_k := 283 + L_P for every k.

(b) In the class of [[eq:vii-0-1]], with these orders the proof of [[thm:iii-k-3-2]] takes

    d_1 = max(d_0, N_NM + k″) = 22d + 292 + L_P,     K = d_1 + 14 = 22d + 306 + L_P,                 {#eq:uc-data-order}

and the proof of [[thm:settling]] builds g_λ with an approximant of order K and N = K + 3 stages. Here L_0 ≤ 23 and
J ≤ 10, so that L_P ≤ 43 and K ≤ 22d + 349.

(c) In the class ℰ_0^½ of [[thm:own-data]] the loss d is that of the class of [[eq:vii-0-1]], L_0 ≤ 28, L_P ≤ 48 and
d_1 = 22d + 292 + L_P. [[thm:own-data]] then takes k1 = d_1 + 4 and M = 2k1 + 17, and for a ∈ (ℓ0 − 1, 3)

    K*(a, M, k1) = k1 + 4 + (4k1 + 35)(k1 + a)/(7 − 2a),                                              {#eq:uc-kstar-own}

which exceeds d_1 + 14; so the orders K that [[thm:own-data]] admits are the integers above [[eq:uc-kstar-own]]. As
(ℓ0 − 1, 3) ⊂ (2, 3), k1 + 4 + (4k1 + 35)(k1 + 2)/3 < K*(a, M, k1) < k1 + 4 + (4k1 + 35)(k1 + 3).

(d) At the computational point, with the index sets as constructed and the choices of [[def:uc-choice]] and
[[def:cs-choices]], J ≤ 8; so L_P ≤ 39 in the class of [[eq:vii-0-1]] and L_P ≤ 44 in the class ℰ_0^½. With D_acc of
[[thm:uc-integer]],

    K ≤ 22D_acc + 345 = 3,457,440,866,880,000,000,000,000,027,691,400,000,000,000,000,000,345 < 3.45745·10⁵¹,

d_1 ≤ 22D_acc + 331 and N ≤ 22D_acc + 348. For the fixed seminorms of [[lem:uc-small-orders]] (d), K < 5.7624·10⁵⁰,
and for those of [[rem:uc-small-reading]], K < 1.15248·10⁵¹; and K > 22d > 2.7493·10²⁵. In the class ℰ_0^½,
k1 ≤ 22D_acc + 340 and 1.0078·10⁵¹ < K*(a, M, k1) < 4.78156·10¹⁰³ for every a ∈ (ℓ0 − 1, 3).

*Proof.* (a) *d_0.* [[thm:iii-c2-3-1]], for φ_(S,S⁰) by [[lem:s27-translated-exterior]] (c), asks the data (h̊_0, h̊_1)
on Σ_(IVP,r_ext) small in H^(k₂,ℓ^♭_0)_b with k₂ = 2 · 153 + 2 = 308, together with the smallness of [[thm:iii-c1-2-1]]
at the order 153 that [[thm:iii-c1-3-1]] asks; by [[lem:uc-data-losses]] (i) the data at the order 309 control both.
[[thm:iv3-2-2]] asks (h⁰, h¹) small in 𝒜^153_Σ, for every (S, S⁰) with |S| + |S⁰| ≤ σ_0. By (v) at l = 0, h_0 in
𝒜^155(𝒪_𝒟) controls them. 𝒪_𝒟 is the union of 𝒪_𝒟 ∩ 𝒟⁺, 𝒪_𝒟 ∩ 𝔒⁻ and 𝒪_𝒟 ∩ Ω_(ext,r_1) ([[lem:s27-cover]] (e)); on
these h_0 is the solution of [[thm:iv3-2-2]] for (h̊_0, h̊_1), the backward solution of (N) and the solution of
[[thm:iii-c1-2-1]] (the proof of [[prop:iii-k-1-2]]). h_0 is smooth across Σ^IVP (*Gluing* there), so at an integer
order its norm on 𝒪_𝒟 is at most a constant times the sum of its norms on the three parts, which (ii) bounds: (h̊_0,
h̊_1) in 𝒜^(155+L_F)_Σ = 𝒜^287_Σ control h_0 in 𝒜^155(𝒪_𝒟), and by (i) the data at the order 288 do. (N) asks the data
small in H^5 × H^4 on Σ^IVP ∩ 𝔒⁻, which (v) and (ii) give at lower orders. The largest of these orders is 309; and the
smallness of γ̃ in H³_b that [[prop:iii-c2-4-1]] asks is weaker. So d_0 := 309 serves.

*k′_k.* Fix k ≥ 0, and put m := k + 3 and n := m + L_P; then m ≥ 3, as (iv) asks, and n ≥ 10, as L_P ≥ L_0 ≥ 7. By
(iii) and (iv) of [[lem:uc-data-losses]], applied in turn, the triple (h_(S,S⁰), ∂h_(S,S⁰), ∂²h_(S,S⁰)) in 𝒜^n, with
the triple of its data in ℬ^n_Σ, controls the triple in ℬ^m, and so the left side of (3) at the order k + 2 < m, which
consists of norms of the triple in the class of (3), on 𝒟 ∩ Ω_* ⊂ 𝒟⁺ ((3) of the proof of [[prop:iii-k-1-2]]).

*The triple in 𝒜^n.* By (vi), ∂²h_(S,S⁰) in 𝒜^n is controlled by ∂h_(S,S⁰) in 𝒜^(n+6), h_(S,S⁰) in 𝒜^(n+7) and
∂²(h⁰, h¹) in 𝒜^(n+4)_Σ, and ∂h_(S,S⁰) in 𝒜^(n+6) by h_(S,S⁰) in 𝒜^(n+13) and ∂(h⁰, h¹) in 𝒜^(n+10)_Σ. So h_(S,S⁰) in
𝒜^(n+13), with ∂^l(h⁰, h¹) in 𝒜^(n+10)_Σ for l ≤ 2, controls the triple in 𝒜^n. As n + 13 ≥ 21, by (ii) (h⁰, h¹) in
𝒜^(n+13+L_F)_Σ control h_(S,S⁰) in 𝒜^(n+13); by (v), h_0 in 𝒜^(n+15+L_F)(𝒪_𝒟) controls (h⁰, h¹) there and
∂^l(h⁰, h¹) in 𝒜^(n+10)_Σ; and, as for d_0, by (ii) (h̊_0, h̊_1) in 𝒜^(n+15+2L_F)_Σ control h_0 in
𝒜^(n+15+L_F)(𝒪_𝒟).

*The data of the triple in ℬ^n_Σ.* By (v), h_0 in ℬ^(n+6)(𝒪_𝒟) controls them. On the parts of 𝒪_𝒟 that meet I₀, h_0 is
the solution of [[thm:iv3-2-2]] or of [[thm:iii-c1-2-1]], and (iii) at (S, S⁰) = (0, 0), with (ii), shows that
(h̊_0, h̊_1) in ℬ^(n+6+L_0+L_F)_Σ control it in ℬ^(n+6)(𝒪_𝒟), as n + 6 + L_0 ≥ 21 and ℬ_Σ lies in 𝒜_Σ; on
𝒪_𝒟 ∩ 𝔒⁻, which does not meet I₀, ℬ^(n+6) is H^(n+6), which (ii) gives at a lower order.

*Collecting.* As L_0 ≤ 28 < L_F + 9, n + 6 + L_0 + L_F < n + 15 + 2L_F, so (h̊_0, h̊_1) in ℬ^(n+15+2L_F)_Σ control all
the above, and by (i) the data at the order n + 16 + 2L_F = k + 3 + L_P + 280 do. So (3) holds with k′_k := 283 + L_P,
s_k half the s of this control at η := 1, and ω_k(s) the supremum of the left side of (3) over the parameters and the
data with ‖(γ̃, k̃)‖_(k+k′_k) ≤ s, which is finite for s ≤ s_k and tends to 0 with s. A constant is non-decreasing in
k, as (3) asks. (The proofs use (3) only at the orders j + 3 of [[eq:s27-theta]] and k + 3 of [[lem:iii-k-2-2]] (d),
where m := k + 2 would serve and give 282 + L_P; the one more order makes the count hold at k = 0 as well.)

(b) d_1 = max(309, 21d + 6 + d + 3 + 283 + L_P) = 22d + 292 + L_P, as d ≥ 1 and L_P ≥ 7. The proof of
[[thm:settling-precise]] in [[sec:vii-4]] takes k := d_1 + 5, then the order k + 5 of [[lem:vii-1-1]] (written J there,
a name not related to the J above) and K := (k + 5) + 4, and each increment counts derivatives. [[cor:vii-2-3]] bounds
‖·‖_(d_1) of the glued data by [[lem:vii-0-1]], through their C^(d_1+3)-norm on a bounded set, and [[eq:vii-2-2]]
controls the glued metric in C^(k−1) and its second fundamental form in C^(k−2); so k − 2 ≥ d_1 + 3. [[eq:vii-2-1]]
reads k + 4 derivatives of the metric of the data and k + 3 of their second fundamental form, which are functions of
the components of g_λ and of their first derivatives; so g_λ is needed in C^(k+5). [[lem:vii-1-1]] bounds k + 5
derivatives of g_λ − g^KS_(μ_end,0) by a constant times λ when K = (k + 5) + 4, its bound C_Kλ^(K−j−3) being at most
C_Kλ for j ≤ K − 4. So K = d_1 + 14 = 22d + 306 + L_P, and N = K + 3 ([[lem:vii-1-1]]). L_0 ≤ 23 by
[[lem:uc-data-losses]] (iii). As ℓ_I < ℓ_0 < 4 and ℓ^♭_I = 3/2 + ¼(1 − e_Υ)γ_Υ > 3/2, 4(ℓ_I − ℓ^♭_I) + 1 < 11, so J ≤ 10
by (iv) there; hence L_P ≤ 43 and K ≤ 22d + 349.

(c) *The loss d.* The d of [[thm:iii-k-3-2]] is the largest of the d's of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and
[[prop:iii-j2-4-3]]. These results, and the constructions on Ω_* on which they rest, involve the data class only through
ℰ^C_I and Λ (Ω_* stays away from I₀), which are the same for ℰ_0^½ as for [[eq:vii-0-1]] with the weights of
[[thm:own-half-settling]] ([[prop:own-same-index-sets]]); and they involve the data only through their constants
([[lem:iii-k-2-2]] (c), [[eq:s27-rinv]]). So d is the same. L_0 ≤ 28 by [[lem:uc-data-losses]] (iii), and J ≤ 10 as in
(b); so L_P ≤ 48, and d_1 = max(309, 22d + 292 + L_P) = 22d + 292 + L_P.

*The threshold of [[thm:own-data]].* k1 = max(8, d_1 + 4) = d_1 + 4 and M = 15 + 2(k1 + 1) = 2k1 + 17, so
2M + 1 = 4k1 + 35. As a > ℓ0 − 1 > 2 and a < 3, (4k1 + 35)/(7 − 2a) > 67/3 > 5/2, and s_R of [[lem:own-e-flux]] is
(4k1 + 35)/(7 − 2a) ≥ (4k1 + 35)/3. The first entry of [[eq:own-kstar]] at j = k1 is k1 + 4 + s_R(a + k1), which is
[[eq:uc-kstar-own]]. The other entries are

    E(k, i) := 3 + i + (s_R max(0, 2a + 2 − k)/2 + (M + i)θ_k)/(1 − θ_k),     4 ≤ k ≤ 8,  0 ≤ i ≤ k1 + 1,

with θ_k = (k − 4)/5 as in [[lem:own-e-flux]]. They increase with i, and M + k1 + 1 = 3k1 + 18; so
E(k, i) ≤ k1 + 4 + s_R(a + k1) when s_R X_k ≥ (3k1 + 18)θ_k, where X_k := (1 − θ_k)(a + k1) − max(0, 2a + 2 − k)/2.
For a ∈ (2, 3),

    X_4 = k1 + 1,  X_5 > (4k1 + 9/2)/5,  X_6 > (3k1 + 4)/5,  X_7 > (4k1 + 7)/10,  X_8 > (k1 + 2)/5.

With s_R ≥ (4k1 + 35)/3 the condition holds at k = 4 at once, and at k = 5, 6, 7, 8 it follows from

    (4k1 + 35)(4k1 + 9/2) ≥ 9k1 + 54,     12k1² + 121k1 + 140 ≥ 18k1 + 108,
    16k1² + 168k1 + 245 ≥ 54k1 + 324,     4k1² + 43k1 + 70 ≥ 36k1 + 216,

the last being 4k1² + 7k1 ≥ 146; all four hold for k1 ≥ 8. So K*(a, M, k1) is [[eq:uc-kstar-own]]. It exceeds
k1 + 10 = d_1 + 14, and it increases with a, its numerator increasing and its denominator decreasing; a ∈ (2, 3) gives
the two bounds.

(d) At the choice of [[def:uc-choice]], ℓ_I < 3.5 and γ_Υ = e_Υ = 1/100 ([[def:ec-point]]), so
ℓ^♭_I = 3/2 + ¼ · (99/100) · (1/100) = 60,099/40,000 and 4(ℓ_I − ℓ^♭_I) + 1 < 4(7/2 − 60,099/40,000) + 1 = 89,901/10,000
< 9; so J ≤ 8, the weights being the same for the two classes ([[thm:own-half-settling]]). With L_0 ≤ 23, resp. 28,
L_P ≤ 39, resp. 44, and K = 22d + 306 + L_P ≤ 22d + 345. Here d is the d_NM of [[prop:uc-d-small]], and d_NM ≤ D_acc
([[thm:uc-integer]]). D_acc = 157,156,403,040 · 10³⁹ + 1,258,700 · 10¹⁸, and 22 · 157,156,403,040 = 3,457,440,866,880 and
22 · 1,258,700 = 27,691,400; so 22D_acc = 3,457,440,866,880 · 10³⁹ + 27,691,400 · 10¹⁸, which with 345 added is the
integer printed, with leading digits 3.4574408. d_1 = K − 14 and N = K + 3 give the next two bounds. By
[[prop:uc-d-small]] (b) and (c), d_NM is at most D_b, resp. D_c, where

    D_b := 26,192,562,436,216,086,593,489,752,012,524,648,819,225,884,778,644,
    D_c := 52,385,124,872,431,314,948,189,146,848,603,890,726,471,509,831,693,

and

    22D_b + 345 = 576,236,373,596,753,905,056,774,544,275,542,274,022,969,465,130,513 < 5.7624·10⁵⁰,
    22D_c + 345 = 1,152,472,747,193,488,928,860,161,230,669,285,595,982,373,216,297,591 < 1.15248·10⁵¹.

By [[eq:uc-lower]], d ≥ d_acc > 1.2497·10²⁴, so K > 22d > 2.74934·10²⁵. In the class ℰ_0^½, d_1 ≤ 22d + 336 and
k1 = d_1 + 4 ≤ 22D_acc + 340 =: k̄, and by (c) K*(a, M, k1) < k̄ + 4 + (4k̄ + 35)(k̄ + 3) = 4k̄² + 48k̄ + 109. As
k̄ > 10⁵¹, 48k̄ + 109 < 10⁻⁴⁹k̄², and as k̄ < 3.4574408669·10⁵¹, k̄² < 11.95389735·10¹⁰²; so
K*(a, M, k1) < (4 + 10⁻⁴⁹) · 11.95389735·10¹⁰² < 4.78156·10¹⁰³. And K*(a, M, k1) > (4/3)k1², with
k1 > 22d > 2.74934·10²⁵, so K*(a, M, k1) > (4/3) · 7.5588·10⁵⁰ > 1.0078·10⁵¹. ∎

**Remark {#rem:uc-data-order-limits}** (What the count gives and what it does not.) [[prop:uc-data-order]] makes d_1
and K explicit in d, with the additive terms 292 + L_P and 306 + L_P, L_P ≤ 48, and makes the threshold K* of
[[thm:own-data]] explicit as a quadratic in d_1; the count is an upper count of the orders the proofs read, and smaller
orders may serve. It gives no number on the set where [[thm:settling]] is proved, on which d is not evaluated and is
bounded only from below, by the lower bounds of this chapter on that set; the numbers of its part (d) are those of the
computational point, outside that set ([[rem:ec-point-outside]]). L_0 and J depend on ℓ_0 and ℓ_I, on the gauge
parameters through ℓ^♭_0 and ℓ^♭_I, and on the ν of Step 2 of the proof of [[thm:iii-c1-3-1]]; [[lem:uc-data-losses]]
bounds them and does not fix them. The number K + 4 + ⌈4β0(k_P)⌉ of stages of the approximant of [[thm:own-data]]
involves β0(k_P) = max(2, 4C(k_P) + 1), whose constants C(q) of [[eq:near-lines]] are not evaluated, and the thresholds
λ1, δ and λ_2 are not evaluated ([[rem:ec-not-evaluated]] and the paragraph after [[thm:own-data]]).

### Placement

Each item names the place, the old text and the new text. Old and new texts are given as the lines of the chapter
source, unindented, each preceded by a line ending "Old:" or "New:". Line numbers are those of the current chapter
sources and serve only to find the place.

*1. Where the section goes.* The section above, from its heading through [[rem:uc-data-order-limits]], is inserted in
[[ch:explicit-constants]] after the paragraph that follows [[prop:uc-d-small]], whose last line is "under both.", and
before the heading "### The first constants of the linear theory {#sec:ec-linear}", with one blank line before and one
after. It defines sec:uc-data-order, lem:uc-data-losses, prop:uc-data-order, eq:uc-data-order, eq:uc-kstar-own and
rem:uc-data-order-limits, none of which is defined elsewhere. No number already printed in any chapter changes.

*2. [[ch:explicit-constants]], its opening paragraph (lines 26–27).* Old:

same formulas bound λ1 by δ, δ by a power of 2 that decreases with d, and the modulus of the initial family
([[prop:iii-k-1-2]]) at 2δ by a power of 2 that decreases with d ([[prop:ec-delta-cap]]). The chapter ends with the parts

New:

same formulas bound λ1 by δ, δ by a power of 2 that decreases with d, and the modulus of the initial family
([[prop:iii-k-1-2]]) at 2δ by a power of 2 that decreases with d ([[prop:ec-delta-cap]]). The regularity d_1 of
[[thm:iii-k-4-3]] is 22d + 292 + L_P and the order of the approximant of [[thm:settling]] is K = d_1 + 14, L_P ≤ 43
being an explicit number of derivatives; at the computational point K is at most an integer below 3.45745 × 10⁵¹
([[prop:uc-data-order]]). The chapter ends with the parts

*3. [[ch:theorems]], the paragraph after [[thm:settling]] (line 311).* Old:

determines which decaying perturbations it reaches, directly or through gluing. The rate holds for every ε < ε_K.

New (the same line, followed by six lines that continue its paragraph):

determines which decaying perturbations it reaches, directly or through gluing. The rate holds for every ε < ε_K.
The order K is explicit in the loss d with which the proof applies the Nash–Moser theorem ([[thm:iii-k-3-2]]): with
the orders that [[prop:uc-data-order]] counts, d_1 = 22d + 292 + L_P and K = 22d + 306 + L_P, where L_P ≤ 43 is an
explicit number of derivatives. d is not evaluated on the set where [[thm:settling]] is proved; there it is bounded
below by explicit functions of the gauge and damping parameters ([[ch:explicit-constants]]). At the computational
point of [[def:ec-point]], which lies outside that set ([[rem:ec-point-outside]]), d is at most an integer below
1.57157 × 10⁵⁰, and K at most one below 3.45745 × 10⁵¹.

*4. [[ch:s27]], [[prop:iii-k-1-2]] (3) (line 248).* Old:

uses it). We take k′_k non-decreasing in k.

New:

uses it). We take k′_k non-decreasing in k; in the classes of [[eq:vii-0-1]] and [[eq:half-class]] a constant serves
([[prop:uc-data-order]]).

*5. [[ch:s27]], *Smallness* in the proof of [[thm:iii-k-3-2]] (line 1603).* Old:

d_1 := max(d_0, N_NM + k″), with d_0 of [[prop:iii-k-1-2]]. By [[lem:iii-k-2-2]] (d),

New:

d_1 := max(d_0, N_NM + k″), with d_0 of [[prop:iii-k-1-2]] ([[prop:uc-data-order]] evaluates d_0 and k′_k in the classes
of [[eq:vii-0-1]] and [[eq:half-class]], which gives there d_1 = 22d + 292 + L_P, L_P ≤ 48 an explicit number of
derivatives). By [[lem:iii-k-2-2]] (d),

*6. [[ch:own-data]], the paragraph after [[thm:own-data]] (line 67).* Old:

The threshold λ_2 is not evaluated, and ε, d_1, λ_2 depend on the class. The order k_P is what the subtracted

New (the three lines that follow it, from "expansion of [[sec:own-sigma]] needs:" through "[[sec:own-proof]]; its
first step checks every use of k_P.", stay, and the paragraph may be refilled):

The threshold λ_2 is not evaluated, and ε, d_1, λ_2 depend on the class. d_1, k1 and K* are explicit in the loss d of
[[thm:iii-k-3-2]]: d_1 = 22d + 292 + L_P, L_P ≤ 48 an explicit number of derivatives, k1 = d_1 + 4, and
K*(a, M, k1) = k1 + 4 + (4k1 + 35)(k1 + a)/(7 − 2a), which exceeds d_1 + 14, so that the least admissible K is
quadratic in d_1 ([[prop:uc-data-order]]); d is bounded above only at the computational point of [[def:ec-point]],
which lies outside the set where the theorem is proved. The order k_P is what the subtracted

*7. [[ch:own-data]], [[rem:own-half-changes]] (b) (lines 291–293).* Old:

and each factor costs one derivative (the converse part of [[lem:iii-a-1-3]]). So d_1 changes by a finite amount, and ε
with it; the thresholds λ1 and δ of [[thm:settling]] change accordingly. None of ε, d_1, λ1, δ is evaluated, in either
class. (c) The weights α_1, α′ avoid finitely many more points in each bounded interval.

New:

and each factor costs one derivative (the converse part of [[lem:iii-a-1-3]]). So d_1 changes by a finite amount, and ε
with it; the thresholds λ1 and δ of [[thm:settling]] change accordingly. In either class d_1 = 22d + 292 + L_P, d the
loss of [[thm:iii-k-3-2]], which is the same for the two classes, with L_P ≤ 43 for ℰ_0^ℤ and L_P ≤ 48 for ℰ_0^½
([[prop:uc-data-order]]). None of ε, λ1, δ is evaluated, in either class, and d is bounded above only at the
computational point. (c) The weights α_1, α′ avoid finitely many more points in each bounded interval.

*8. [[ch:scope]], [[sec:scope-constants]] (lines 72–73).* Old:

d is at most an integer below 1.57157 × 10⁵⁰ and N_NM at most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). The
computational point is a point at which the formulas of the proof can be evaluated, and it lies outside the set on which

New:

d is at most an integer below 1.57157 × 10⁵⁰ and N_NM at most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). The order
of the approximant of [[thm:settling]] is K = d_1 + 14 = 22d + 306 + L_P, with L_P ≤ 43 an explicit number of
derivatives, so that at that point K is at most an integer below 3.45745 × 10⁵¹ ([[prop:uc-data-order]]). The
computational point is a point at which the formulas of the proof can be evaluated, and it lies outside the set on which

*9. [[ch:scope]], [[sec:scope-after]] (lines 130–131).* Old:

reaches the data at spatial infinity ([[ch:own-data]], [[prop:own-tail]]). The constants ε, d_1 and λ_2 depend on the
class ([[thm:own-data]]). The continuation of g_λ to the past domain of dependence of the far

New:

reaches the data at spatial infinity ([[ch:own-data]], [[prop:own-tail]]). The constants ε, d_1 and λ_2 depend on the
class ([[thm:own-data]]); d_1 is explicit in the loss d, and the orders of the approximant that [[thm:own-data]] admits
exceed a quadratic in d_1 ([[prop:uc-data-order]]). The continuation of g_λ to the past domain of dependence of the far

*10. Unchanged.* [[thm:settling]] and [[thm:own-data]] keep their statements, which fix K through d_1 and K*; the proofs
in [[ch:settling-proof]], [[ch:after-shell]], [[ch:interior]] and [[ch:own-data]] use d_1 only as a finite order and
stand. [[lem:viii-2-1]], which takes k′_k as in [[lem:iii-k-2-2]] (d), stands. [[prop:ec-delta-cap]] and its numbers
stand: the chosen ε is still at most s̃, and only the value of k′_k is named. [[rem:ec-not-evaluated]] keeps its
statements, as d_1 and K are now explicit in d while d is bounded above only at the computational point; the proposal
for the lower bounds of d on the proved set rewrites three of its lines (lines 4693–4695), which no text here touches.
That proposal also rewrites lines 16–25 of the opening of [[ch:explicit-constants]], lines 351–357 of [[ch:theorems]]
and lines 66–67 of [[ch:scope]]; none of these overlaps texts 2, 3, 8 or 9. [[ch:introduction]] states no value of K or
d_1.

### Crosswalk rows

New rows for the crosswalk table of [[ch:explicit-constants]], one per label, each given as its four fields (label;
location in this file; name; note), to be written with tab separators:

Row 1. sec:uc-data-order; paper/reader/proofs/P-K.md:1; data-order proof P-K, section heading; new section,
inserted before sec:ec-linear.

Row 2. lem:uc-data-losses; paper/reader/proofs/P-K.md:39; data-order proof P-K, Lemma (The orders that the
initial family reads.); new written count of the orders that prop:iii-k-1-2 (3) reads: gauged data +1, forward and
exterior solutions +132 above order 21, Step 1 L_0 ≤ 23 (28 for the half class), Step 2 2J, pull-back +2+l (+4+l with
expansions), derivatives in (S, S⁰) +7 and +6.

Row 3. prop:uc-data-order; paper/reader/proofs/P-K.md:175; data-order proof P-K, Proposition (The regularity d_1
and the order of the approximant.); new: d_0 = 309, k′_k = 283 + L_P for every k (282 + L_P would serve for k ≥ 1),
d_1 = 22d + 292 + L_P, K = 22d + 306 + L_P ≤ 22d + 349, K*(a, M, k1) of thm:own-data; at the computational point
K ≤ 22D_acc + 345 < 3.45745·10⁵¹.

Row 4. eq:uc-data-order; paper/reader/proofs/P-K.md:183; data-order proof P-K, display; display of d_1 and K.

Row 5. eq:uc-kstar-own; paper/reader/proofs/P-K.md:191; data-order proof P-K, display; display of
K*(a, M, k1) = k1 + 4 + (4k1 + 35)(k1 + a)/(7 − 2a).

Row 6. rem:uc-data-order-limits; paper/reader/proofs/P-K.md:306; data-order proof P-K, Remark (What the count gives
and what it does not.); what stays open: d on the proved set, β0(k_P), λ1, δ, λ_2.

Notes for existing rows: ch:explicit-constants (opening states d_1 and K, text 2); in the crosswalk table of
[[ch:theorems]], sec:settling-statement (the paragraph after thm:settling states K explicit in d, text 3); in that of
[[ch:s27]], prop:iii-k-1-2 and thm:iii-k-3-2 (k′_k and d_1 counted in prop:uc-data-order, texts 4–5); in that of
[[ch:own-data]], thm:own-data and rem:own-half-changes (d_1, k1 and K* explicit in d, texts 6–7); in that of
[[ch:scope]], sec:scope-constants and sec:scope-after (K and d_1 explicit in d, texts 8–9).
