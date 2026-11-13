## The Nash–Moser theorem; Fourier transforms, resolvent bounds and the radiation field {#ch:s10}

This chapter proves two sets of general tools in dimension 4 + 1. The first half carries the three tools of [Hin26c,
Section 12.2, pp. 233–243] on which the nonlinear step rests: a Nash–Moser theorem with support classes
([[thm:ii-g-2-1]]), smoothing operators on spaces of supported weighted b-Sobolev functions ([[prop:ii-g-3-1]]), and
tame bounds for products and nonlinear functions ([[lem:ii-g-4-1]]). None of the three depends on the dimension; the
dimension enters only through the spaces to which they are applied, and [[sec:ii-g-5]] records the weights of a forward
problem in dimension 4 + 1. The Nash–Moser theorem is proved by Saint Raymond's iteration [SR89], with a smoothing step
at each stage and with the supports tracked. The smoothing operators are built with the support bookkeeping and the
charts at the hypersurface {t^♭ = 1} written out for the domain Ω_* of [[sec:ii-f1-1-1]], and the tame bounds are proved
from the Gagliardo–Nirenberg inequality, read off the Fourier transform.

The second half carries [Hin26c, Sections 13.1–13.3, pp. 243–260], the tools by which forward solutions are shown to
decay faster than [[thm:ii-f1-1-1]] alone gives: the Fourier transform in time on weighted b-Sobolev spaces, on the line
and on the resolved product spaces ([[sec:ii-g1-2]], [[sec:ii-g1-3]]); the translation of the resolvent estimates of
[[ch:s01]], [[ch:s02]] and [[ch:s03]] at nonzero, high and low frequencies into b-Sobolev spaces with a loss of
b-regularity independent of the order ([[sec:ii-g1-4]]); and the radiation field at null infinity ([[sec:ii-g1-5]]).
The facts on the line are proved from the Gagliardo seminorm and two Hardy inequalities by a dyadic argument, and the
two ordinary differential equation lemmas used for the radiation field are proved in [[lem:ii-g1-3-2]] and
[[lem:ii-g1-5-3]].

Throughout, ℕ = {1, 2, …}, ℕ₀ = ℕ ∪ {0}, and constants C may change from line to line, depending only on the quantities
named. The radii 0 < r_0 − 2δ_0 < r_0 < r_2 < r_h are those of [[sec:i-a-1-1]]; the inner radius r_0 is a parameter, and
nothing in this chapter depends on it beyond these inequalities.

### Scope of the first half {#sec:ii-g-1}

[Hin26c, Section 12], "Application I: nonlinear scalar waves", has five subsections. Its Section 12.2 holds the three
general tools used later: the Nash–Moser theorem ([Hin26c, Theorem 12.4], with [Hin26c, Remark 12.5] on the norms),
smoothing operators on spaces of supported b-Sobolev functions ([Hin26c, Proposition 12.6 and Example 12.7]), and tame
bounds for products and nonlinear functions ([Hin26c, Lemma 12.8]). They are proved in [[sec:ii-g-2]],
[[sec:ii-g-3]] and [[sec:ii-g-4]]. The rest of [Hin26c, Section 12] concerns the scalar wave operator □_g on a
subextremal Kerr spacetime: its 0-admissibility ([Hin26c, Theorem 12.2], through [Hin26c, Theorem 12.3], "mode
stability implies 0-admissibility", and the mode stability of Kerr) and three model problems ([Hin26c, Theorems 12.9,
12.11 and 12.12]: a power nonlinearity, a quasilinear equation and a null form). The stability theory does not use
them. Its linear operator is the gauge-fixed linearised Einstein operator, whose admissibility has a loss ℵ > 0 from
zero-energy states and is established in [[ch:s18]], not by [Hin26c, Theorem 12.2]; [Hin26c, Theorem 12.3] in dimension
4 + 1, the passage from the spectral theory of [[ch:s01]]–[[ch:s03]] to the estimate [[eq:ii-c-2-2]] of
[[def:ii-c-2-7]] (3) with ℵ = 0, is the model for that admissibility proof ([[sec:ii-g-5-2]]).

### The Nash–Moser theorem {#sec:ii-g-2}

#### The statement {#sec:ii-g-2-1}

[Hin26c] writes the two families of spaces with the same letter in two fonts; here B^k are the spaces of unknowns and
F^k those of right sides.

**Theorem {#thm:ii-g-2-1}** (Nash–Moser theorem with support classes.) Let d ∈ ℕ, δ > 0 and η_0 ∈ (0, 1]. For k ∈ ℕ₀
let (B^k, |·|_k) and (F^k, ‖·‖_k) be Banach spaces with continuous inclusions B^s ↪ B^t, F^s ↪ F^t for s ≥ t, along
which the norms do not increase: |v|_t ≤ |v|_s, ‖f‖_t ≤ ‖f‖_s ([[rem:ii-g-2-2]]). Put B^∞ := ⋂_k B^k and F^∞ :=
⋂_k F^k. For η ∈ [0, 1] let B^k_η ⊂ B^k be closed linear subspaces, non-increasing in η, with B^k_0 = B^k, and B^∞_η :=
⋂_k B^k_η; let F^∞_η ⊂ F^∞ be linear subspaces, non-increasing in η, with F^∞_0 = F^∞. Assume:

(i) (*Smoothing.*) For every θ > 1 there is a linear map S_θ : B^∞_(θ^(−1/2)) → B^∞ with S_θ(B^∞_η) ⊂
B^∞_(η−θ^(−1/2)) for η ∈ [θ^(−1/2), 1], and constants C_(s,t), independent of θ, with

    |S_θ v|_s ≤ C_(s,t) θ^(s−t) |v|_t   (s ≥ t),        |v − S_θ v|_s ≤ C_(s,t) θ^(s−t) |v|_t   (s ≤ t),
                                                                     v ∈ B^∞_(θ^(−1/2)).          {#eq:ii-g-2-1}

(ii) (*The map.*) Φ : U → F^∞, U := {u ∈ B^∞ : |u|_(3d) < δ}, maps U ∩ B^∞_η into F^∞_η for η ∈ [0, η_0], and is
twice differentiable in the following sense: for u ∈ U there are a linear map Φ′(u) : B^∞ → F^∞ and a symmetric
bilinear map Φ″(u) : B^∞ × B^∞ → F^∞ such that for u, u + h ∈ U the maps s ↦ Φ′(u + sh)h and s ↦ Φ″(u + sh)(h, h),
s ∈ [0, 1], are continuous into F^(2d) and

    Φ(u + h) − Φ(u) = ∫_0^1 Φ′(u + sh)h ds,
    Φ(u + h) − Φ(u) − Φ′(u)h = ∫_0^1 (1 − s) Φ″(u + sh)(h, h) ds                                   {#eq:ii-g-2-2}

in F^(2d). There are constants C_1, C_2 and C_k, k ≥ d, such that for u ∈ U and v, w ∈ B^∞

    ‖Φ(u)‖_k ≤ C_k (1 + |u|_(k+d))   (k ≥ d),        ‖Φ′(u)v‖_(2d) ≤ C_1 |v|_(3d),
    ‖Φ″(u)(v, w)‖_(2d) ≤ C_2 |v|_(3d) |w|_(3d).                                                     {#eq:ii-g-2-3}

(iii) (*Right inverses.*) For u ∈ U there is a linear map Ψ(u) : F^∞ → B^∞ with Ψ(u)(F^∞_η) ⊂ B^∞_η for η ∈ [0, 1]
whenever u ∈ U ∩ B^∞_η, Φ′(u)Ψ(u)f = f for f ∈ F^∞, and (with the same constants C_k, enlarged if necessary)

    |Ψ(u)f|_k ≤ C_k (‖f‖_(k+d) + |u|_(k+d) ‖f‖_(2d)),        k ≥ d,  f ∈ F^∞.                     {#eq:ii-g-2-4}

Let N_NM := 21d + 6. There is ε > 0, depending only on d, δ, η_0, C_1, C_2 and the constants C_k, C_(s,t) with k, s,
t ≤ N_NM, such that if ‖Φ(0)‖_(2d) < ε, then there is u ∈ B^∞_(η_0/2) with |u|_(3d) < δ and Φ(u) = 0.

This is [Hin26c, Theorem 12.4], which quotes the theorem from [SR89] in the form of [Hin24a, Theorem 6.11] with the
regularity 16d² + 43d + 24, made precise where it is stated loosely. [Hin26c, Theorem 12.4] states (ii) for all η ∈ [0,
1], together with Φ(0) ∈ F^∞_(η_0); as 0 ∈ B^∞_η for every η, the hypothesis for all η ∈ [0, 1] would force Φ(0) ∈
F^∞_1. The form above asks (ii) only for η ≤ η_0; in the applications of [Hin26c] both forms hold, with η_0 = 1, the
right side being supported in {t_* ≥ 2}. The conclusion of [Hin26c, Theorem 12.4] is u ∈ B^∞; as its B^k_0 is the whole
space ([Hin26c, (12.21)]), that is the support t_* ≥ 1 its applications use [Hin26c, p. 240], the better support
t_* ≥ 2 being obtained there by local uniqueness. [[thm:ii-g-2-1]] strengthens the conclusion to u ∈ B^∞_(η_0/2),
which costs the closedness of the B^k_η; the spaces of [[prop:ii-g-3-1]] have it.

**Remark {#rem:s10-right-inverses}** (The support hypothesis on the right inverses.) [Hin26c, Theorem 12.4] asks the
support property of the right inverses at every u ∈ U. Hypothesis (iii) asks it only at u ∈ U ∩ B^∞_η, which is all
the proof uses: in the step *Supports* of the proof, u_j ∈ B^∞_(η_j) and e_j ∈ F^∞_(η_j). So the conclusion is
unchanged. The weaker hypothesis is what the right inverses of the nonlinear stability theorem provide
([[lem:iii-k-2-3]]): at a base point whose tail does not vanish below the level, the linearisation contains a term in
the boost direction that need not vanish there. The right inverses of [Hin26, p. 322, Step 3 (3)] have the support
property only under the same restriction.

**Remark {#rem:ii-g-2-2}** ([Hin26c, Remark 12.5].) The monotonicity of the norms costs nothing: if the inclusions are
continuous, |v|′_s := max_(t≤s) |v|_t is an equivalent norm on B^s and is non-decreasing in s, and likewise for F^s.
[[eq:ii-g-2-1]] persists with other constants: for s ≥ t and t′ ≤ s, |S_θ v|_(t′) ≤ C_(t′,t) θ^(t′−t) |v|_t if t′ ≥ t
and |S_θ v|_(t′) ≤ C_(t′,t′) |v|_(t′) if t′ < t, both at most C θ^(s−t) |v|′_t; for s ≤ t and t′ ≤ s, |v −
S_θ v|_(t′) ≤ C_(t′,t) θ^(t′−t) |v|_t ≤ C_(t′,t) θ^(s−t) |v|′_t. [[eq:ii-g-2-3]] and [[eq:ii-g-2-4]] persist, the
norms of index below d (resp. 2d) being bounded by those of index d (resp. 2d).

#### The proof {#sec:ii-g-2-2}

*Proof of [[thm:ii-g-2-1]].* *Parameters.* Let κ := 3/2, α := 8d + 2 and β := 4d + 2; then

    N_NM = 5d + β + κα + 1,        4d − 2α = −κα − 1,        β + 2d + 1 = κβ.                       {#eq:ii-g-2-5}

Indeed 5d + (4d + 2) + (12d + 3) + 1 = 21d + 6, 4d − 2(8d + 2) = −12d − 4 = −(3/2)(8d + 2) − 1, and (4d + 2) + 2d + 1 =
6d + 3 = (3/2)(4d + 2). For θ_0 ≥ 2, to be fixed, put θ_j := θ_0^(κ^j). As κ^j ≥ 1 + j/2 (Bernoulli's inequality), for
γ > 0 with θ_0^(γ/2) ≥ 2,

    Σ_(j≥0) θ_j^(−γ) ≤ θ_0^(−γ) Σ_(j≥0) θ_0^(−γj/2) ≤ 2 θ_0^(−γ).                                  {#eq:ii-g-2-6}

*The iteration.* Put u_0 := 0 and η_j := η_0 − Σ_(i<j) θ_i^(−1/2). As long as u_j ∈ U ∩ B^∞_(η_j) with η_j ≥ η_0/2,
put

    e_j := Φ(u_j),        v_j := Ψ(u_j) e_j,        w_j := S_(θ_j) v_j,        u_(j+1) := u_j − w_j.       {#eq:ii-g-2-7}

*The induction.* We show that, for θ_0 large (depending only on the quantities named in the theorem) and
‖Φ(0)‖_(2d) ≤ θ_0^(−α), every j ≥ 0 satisfies

(a_j) u_j ∈ B^∞_(η_j), η_j ≥ η_0/2, and |u_j|_(3d) ≤ δ/2;

(b_j) ‖e_j‖_(2d) ≤ θ_j^(−α);

(c_j) |u_j|_(N_NM) ≤ θ_j^β.

For j = 0 this is the hypothesis (u_0 = 0). Assume (a_i)–(c_i) for i ≤ j.

*Bounds on v_j.* By [[eq:ii-g-2-4]] at k = d, with |u_j|_(2d) ≤ |u_j|_(3d) ≤ δ, and (b_j),

    |v_j|_d ≤ C_d (1 + δ) ‖e_j‖_(2d) ≤ A_1 θ_j^(−α).

By [[eq:ii-g-2-4]] at k = N_NM − 2d ≥ d, [[eq:ii-g-2-3]] at k = N_NM − d, the monotonicity of the norms and
‖e_j‖_(2d) ≤ 1,

    |v_j|_(N_NM−2d) ≤ C_(N_NM−2d) (C_(N_NM−d)(1 + |u_j|_(N_NM)) + |u_j|_(N_NM)) ≤ A_2 (1 + |u_j|_(N_NM))
                    ≤ 2 A_2 θ_j^β.

*Supports.* By (ii), e_j ∈ F^∞_(η_j) (η_j ≤ η_0); by (iii), as u_j ∈ B^∞_(η_j), v_j ∈ B^∞_(η_j). Choose θ_0 ≥
16 η_0^(−2), with θ_0^(1/4) ≥ 2. Then θ_j^(−1/2) ≤ θ_0^(−1/2) ≤ η_0/4 ≤ η_j, so S_(θ_j) applies to v_j, and w_j ∈
B^∞_(η_j − θ_j^(−1/2)) = B^∞_(η_(j+1)); also u_j ∈ B^∞_(η_j) ⊂ B^∞_(η_(j+1)), so u_(j+1) ∈ B^∞_(η_(j+1)). By
[[eq:ii-g-2-6]] with γ = 1/2, η_(j+1) ≥ η_0 − 2θ_0^(−1/2) ≥ η_0/2.

*Bounds on w_j.* By [[eq:ii-g-2-1]],

    |w_j|_(3d) ≤ C_(3d,d) θ_j^(2d) |v_j|_d ≤ A_3 θ_j^(2d−α),
    |w_j|_(N_NM) ≤ C_(N_NM,N_NM−2d) θ_j^(2d) |v_j|_(N_NM−2d) ≤ A_4 θ_j^(β+2d),
    |v_j − w_j|_(3d) ≤ C_(3d,N_NM−2d) θ_j^(5d−N_NM) |v_j|_(N_NM−2d) ≤ A_5 θ_j^(5d−N_NM+β).               {#eq:ii-g-2-8}

*(a_(j+1)).* By [[eq:ii-g-2-8]] and [[eq:ii-g-2-6]] with γ = α − 2d = 6d + 2, |u_(j+1)|_(3d) ≤ Σ_(i≤j) |w_i|_(3d) ≤
2 A_3 θ_0^(−6d−2) ≤ δ/2 for θ_0 large.

*(c_(j+1)).* |u_(j+1)|_(N_NM) ≤ θ_j^β + A_4 θ_j^(β+2d) ≤ (1 + A_4) θ_j^(β+2d) ≤ θ_j^(β+2d+1) = θ_j^(κβ) =
θ_(j+1)^β, for θ_0 ≥ 1 + A_4, by [[eq:ii-g-2-5]].

*(b_(j+1)).* u_j and u_(j+1) lie in U, which is convex. By [[eq:ii-g-2-2]] with h = −w_j, and Φ′(u_j)v_j = e_j,

    e_(j+1) = Φ′(u_j)(v_j − w_j) + ∫_0^1 (1 − s) Φ″(u_j − s w_j)(w_j, w_j) ds,

so by [[eq:ii-g-2-3]], [[eq:ii-g-2-8]] and [[eq:ii-g-2-5]], as 5d − N_NM + β = −12d − 4 = −κα − 1,

    ‖e_(j+1)‖_(2d) ≤ C_1 A_5 θ_j^(5d−N_NM+β) + (1/2) C_2 A_3² θ_j^(4d−2α) = (C_1 A_5 + (1/2) C_2 A_3²) θ_j^(−κα−1)
                   ≤ θ_j^(−κα) = θ_(j+1)^(−α)

for θ_0 ≥ C_1 A_5 + (1/2) C_2 A_3². This completes the induction.

The constants A_1, …, A_5 depend only on d, δ and C_d, C_(N_NM−2d), C_(N_NM−d), C_(3d,d), C_(N_NM,N_NM−2d),
C_(3d,N_NM−2d). Fix θ_0 as required above and put ε := θ_0^(−α); it depends only on the quantities named in the
theorem.

*Higher norms.* Let M ≥ N_NM. By [[eq:ii-g-2-4]] at k = M − 2d, [[eq:ii-g-2-3]] at k = M − d and (b_j),
|v_j|_(M−2d) ≤ A_M (1 + |u_j|_M), so by [[eq:ii-g-2-1]], |w_j|_M ≤ A′_M θ_j^(2d) (1 + |u_j|_M), with A′_M ≥ 1, and

    1 + |u_(j+1)|_M ≤ (1 + A′_M θ_j^(2d)) (1 + |u_j|_M).

Hence 1 + |u_j|_M ≤ ∏_(i<j) 2A′_M θ_i^(2d) = (2A′_M)^j θ_0^(2d(κ^j−1)/(κ−1)) ≤ (2A′_M)^j θ_j^(4d). As θ_j ≥ 2^(κ^j)
and κ^j/j → ∞, L_M := sup_j (2A′_M)^j θ_j^(−1) is finite, and

    |u_j|_M ≤ L_M θ_j^(4d+1),        |w_j|_M ≤ L′_M θ_j^(6d+1).                                    {#eq:ii-g-2-9}

*Convergence in every B^k.* Let k > 3d, μ := (3d + 1)/(k − 3d) and M := max(N_NM, 3k − 6d), so that μ(M − k) ≥
6d + 2. For j so large that θ_j^μ ≥ 16 η_0^(−2), S_(θ_j^μ) applies to w_j ∈ B^∞_(η_(j+1)) (η_(j+1) ≥ η_0/2 ≥
θ_j^(−μ/2)), and by [[eq:ii-g-2-1]], [[eq:ii-g-2-8]] and [[eq:ii-g-2-9]]

    |w_j|_k ≤ |S_(θ_j^μ) w_j|_k + |w_j − S_(θ_j^μ) w_j|_k
            ≤ C_(k,3d) θ_j^(μ(k−3d)) A_3 θ_j^(−6d−2) + C_(k,M) θ_j^(μ(k−M)) L′_M θ_j^(6d+1) ≤ C (θ_j^(−3d−1) + θ_j^(−1)).

So Σ_j |w_j|_k < ∞ for every k (for k ≤ 3d by [[eq:ii-g-2-8]] and monotonicity), and u_j = −Σ_(i<j) w_i converges in
every B^k; the limits agree, the inclusions being continuous, and define u ∈ B^∞ with |u|_(3d) ≤ δ/2 < δ. As u_j ∈
B^k_(η_0/2) for all j and k ((a_j), the subspaces being non-increasing in η) and B^k_(η_0/2) is closed, u ∈
B^∞_(η_0/2).

*The equation.* u and u_j lie in U; by [[eq:ii-g-2-2]] and [[eq:ii-g-2-3]], ‖Φ(u) − Φ(u_j)‖_(2d) ≤ C_1 |u − u_j|_(3d)
→ 0, and ‖Φ(u_j)‖_(2d) ≤ θ_j^(−α) → 0. So Φ(u) = 0. ∎

### Smoothing operators {#sec:ii-g-3}

#### The setting and the statement {#sec:ii-g-3-1}

Let M be a compact manifold with corners whose boundary hypersurfaces are embedded, its set of boundary hypersurfaces
split as ℋ = ℋ_b ⊔ ℋ̄, and M′ ⊃ M an extension of M across the faces in ℋ̄: a manifold with corners containing M as a
closed subset, whose boundary hypersurfaces are those of ℋ_b, extended. Let μ be a smooth positive b-density on M′ (b at
the faces of ℋ_b), and 𝒱_b the smooth vector fields on M′ tangent to every face of ℋ_b. For k ∈ ℕ₀, H^k_b(M′) is the
space of u ∈ L²(M′, μ) with Au ∈ L² for every product A of at most k elements of 𝒱_b, normed by the sum of the
L²-norms of Au over a finite spanning set ([[sec:ii-a-4]]: the Sobolev spaces of the bounded geometry structure of
𝒱_b, (S3) of [[sec:ii-a-3]]); H̄^k_b(M) is the space of restrictions to M°, with the quotient norm. For a weight w =
∏_(H∈ℋ_b) ρ_H^(a_H), a_H ∈ ℝ, ρ_H defining functions, w H̄^k_b(M) := {u : w⁻¹u ∈ H̄^k_b(M)} with ‖u‖_(wH̄^k_b) :=
‖w⁻¹u‖_(H̄^k_b).

Let t be a real function on M′ ∖ ⋃_(H∈ℋ_b) H, and c_1 ∈ (0, 1], such that:

(T1) t is smooth with dt ≠ 0 on {|t| < 2c_1}, and this set meets each H ∈ ℋ̄ only in H° (away from all other faces),
with dt|_(TH) ≠ 0 there;

(T2) every point p of the closure of {|t| ≤ c_1} ∩ H, H ∈ ℋ_b, lies on no other boundary hypersurface, and has a
neighbourhood V in M′ with a function t̄ ∈ C^∞(V) such that dt̄|_(TH) ≠ 0 on V ∩ H and t − t̄ ∈ ρ_H^ε C^∞_b(V) for some
ε > 0, C^∞_b denoting the functions bounded with all their derivatives along 𝒱_b;

(T3) the functions of t used below, ψ(t) with ψ ∈ C^∞(ℝ) constant on (−∞, −c_1] and on [c_1, ∞), are smooth on M′
with all derivatives along 𝒱_b bounded (that is, ψ(t) ∈ C^∞_b).

For η ∈ ℝ let Ω_η := M ∩ {t ≥ η} and w H̄^k_b(Ω_η)^(•,−) := {u ∈ w H̄^k_b(M) : supp u ⊂ Ω_η}, a closed subspace, with the
norm of w H̄^k_b(M).

**Proposition {#prop:ii-g-3-1}** (Smoothing operators with support control; [Hin26c, Proposition 12.6].) Let c_0 :=
c_1/8, and for η ∈ [0, 1] and k ∈ ℕ₀ let B^k := w H̄^k_b(Ω_0)^(•,−), B^k_η := w H̄^k_b(Ω_(c_0 η))^(•,−), with the norms
|·|_k of w H̄^k_b(M). There are linear maps S_θ : B^0 → ⋂_k w H̄^k_b(M), θ > 1, with S_θ(B^∞_η) ⊂ B^∞_(η−θ^(−1/2))
for η ∈ [θ^(−1/2), 1], and constants C_(s,t), independent of θ, such that for v ∈ B^∞_0

    |S_θ v|_s ≤ C_(s,t) θ^(s−t) |v|_t   (s ≥ t),        |v − S_θ v|_s ≤ C_(s,t) θ^(s−t) |v|_t   (s ≤ t).  {#eq:ii-g-3-1}

In particular the B^k_η satisfy hypothesis (i) of [[thm:ii-g-2-1]], and are closed subspaces of B^k.

**Remark {#rem:ii-g-3-2}** (The domain Ω_* in dimension 4 + 1; [Hin26c, Example 12.7].) Let M be the closure of
{t_* ≥ 1/2, r ≥ r_0} in the compactified spacetime M̃ of [[sec:ii-a-1]], a compact manifold with corners with boundary
hypersurfaces ℐ⁺, ι⁺, K⁺ (forming ℋ_b) and {r = r_0}, {t_* = 1/2} (forming ℋ̄), and M′ the closure of {t_* > 1/4,
r > r^♯} less its faces at t_* = 1/4 and r = r^♯; μ := |dt_* dx|/(t_* ⟨x⟩⁴), a smooth positive b-density
([[cor:ii-f1-1-2]], [[lem:ii-a-8-8]]); w := ρ_I^(a_I) ρ_+^(a_+) ρ_K^(a_K) with the defining functions [[eq:ii-f1-1-1]];
t := t^♭ − 1, with t^♭ the time function of [[lem:ii-c-3-2]], defined on M′ ∩ {t_* ≥ 1/2} by [[lem:ii-e-1-2]] (iv),
and t := −1 on M′ ∩ {t_* < 1/2}. As t^♭ ≤ t_* ([[lem:ii-c-3-2]] (b)), t < −c_1 on {t_* < 7/8}, so every function ψ(t)
of (T3) is constant there, and t is smooth wherever (T1) asks. The spaces B^k_0 of [[prop:ii-g-3-1]] are then the
spaces H^(k,(α_I,α_+,α_K))_b(Ω_*; E)^(•,−) of [[eq:ii-f1-1-2]], componentwise and with w adjusted by the factor
relating |dt dx| to μ, which is a product of powers of ρ_I, ρ_+, ρ_K ([[cor:ii-f1-1-2]]), with equivalent norms: there
the quotient is over extensions supported in {t^♭ ≥ 1}, here over all extensions to M′, and the extension of
[[lem:ii-f1-2-5]] preserves that support and is bounded at every order. B^k_η consists of their elements supported in
{t^♭ ≥ 1 + c_0 η}. The hypotheses hold with c_1 := 1/8:

(T1): dt^♭ is past timelike, so non-zero. On {|t^♭ − 1| < 1/4}, t_* ≤ (5/4)/C′ ([[lem:ii-c-3-2]] (b)), so this set
stays away from ι⁺ and K⁺, and t_* ≥ t^♭ > 3/4, so it does not meet {t_* = 1/2}; it meets {r = r_0} only away from the
other faces, and there dt^♭ = C′ dt_* ([[lem:ii-c-3-2]] (c); its proof takes r′_0 large, so r′_0 − 1 > r_2 > r_0),
whose restriction to {r = r_0} is non-zero.

(T2): as t^♭ ≥ C′ t_*, {t^♭ ≤ 9/8} meets ℋ_b only in ℐ⁺ ∩ {t_* ≤ (9/8)/C′}, away from ι⁺, and on ℐ⁺, t^♭ = t_*, so the
points concerned have t_* ∈ [7/8, 9/8], on no other face. Near them t̄ := t_* − 1 is smooth, t_* is a coordinate along
ℐ⁺, and t − t̄ = −t_* (t_*/r)^(ℓ_I) ([[lem:ii-c-3-2]] (a)), with t_*/r = ρ_I/(1 − ρ_I), lies in ρ_I^(ℓ_I) C^∞_b.

(T3): near ℐ⁺ at bounded t_*, t^♭ = t_*(1 − (t_*/r)^(ℓ_I)) or a smooth function of t_* and r glued to it
([[lem:ii-c-3-2]]), with derivatives along t_*∂_(t_*), r∂_r, ∂_ω bounded; and ψ(t) is constant on {t^♭ ≥ 1 + c_1},
which contains a neighbourhood of ι⁺ ∪ K⁺ in M′.

#### The proof {#sec:ii-g-3-2}

*Proof of [[prop:ii-g-3-1]].* *Step 1: smoothing on ℝ^m.* Fix φ ∈ C^∞_c(ℝ^m) with 0 ≤ φ ≤ 1, φ = 1 on {|ξ| ≤ 1} and
supp φ ⊂ {|ξ| ≤ 2}, and put φ̌ := ℱ⁻¹φ ∈ 𝒮(ℝ^m). For Λ ≥ 1 let S^(0)_Λ v := k_Λ ∗ v with k_Λ(y) := φ(Λ^(1/2) y)
Λ^m φ̌(Λy). Then supp S^(0)_Λ v lies in the 2Λ^(−1/2)-neighbourhood of supp v, and, with ‖v‖_(H^s) := ‖⟨ξ⟩^s v̂‖_(L²),
for s, t ∈ ℕ₀,

    ‖S^(0)_Λ v‖_(H^s) ≤ C Λ^(s−t) ‖v‖_(H^t)   (s ≥ t),        ‖v − S^(0)_Λ v‖_(H^s) ≤ C Λ^(s−t) ‖v‖_(H^t)   (s ≤ t).
                                                                                                  {#eq:ii-g-3-2}

Indeed, M_Λ v := Λ^m φ̌(Λ·) ∗ v is the Fourier multiplier φ(ξ/Λ), and on supp φ(·/Λ), ⟨ξ⟩ ≤ 3Λ, while on
supp(1 − φ(·/Λ)), ⟨ξ⟩ ≥ Λ; so [[eq:ii-g-3-2]] holds for M_Λ with C = 3^(|s−t|). R_Λ := M_Λ − S^(0)_Λ is the
convolution with r_Λ(y) := (1 − φ(Λ^(1/2) y)) Λ^m φ̌(Λy). By the Leibniz rule ∂^γ r_Λ is a sum of terms
Λ^(|γ_1|/2) (∂^(γ_1)(1 − φ))(Λ^(1/2) y) Λ^(m+|γ_2|) (∂^(γ_2) φ̌)(Λy), γ_1 + γ_2 = γ, supported in {|Λy| ≥ Λ^(1/2)};
with |∂^(γ_2) φ̌(z)| ≤ C_L ⟨z⟩^(−L),

    ‖∂^γ r_Λ‖_(L¹) ≤ C Λ^(|γ|) ∫_(|z|≥Λ^(1/2)) ⟨z⟩^(−L) dz ≤ C_(γ,L) Λ^(|γ|−(L−m)/2),

which is at most C Λ^(−J) for any J, choosing L. By Young's inequality, ‖∂^γ R_Λ v‖_(L²) ≤ ‖∂^γ r_Λ‖_(L¹) ‖v‖_(L²),
so ‖R_Λ v‖_(H^s) ≤ C_(s,J) Λ^(−J) ‖v‖_(L²) for all s and J, and [[eq:ii-g-3-2]] holds for R_Λ, hence for S^(0)_Λ =
M_Λ − R_Λ and I − S^(0)_Λ = (I − M_Λ) + R_Λ.

*Step 2: orthants.* For ℝ^m_l := [0, ∞)^l × ℝ^(m−l), H̄^s(ℝ^m_l) is the space of restrictions of H^s(ℝ^m), with the
quotient norm. Let E be the composition of Seeley's extension operators [See64] across the hyperplanes {x_i = 0}, i ≤ l
([Hin26c, Lemma 8.5]; the operator, with infinitely many reflections, is written out in the proof of [[lem:ii-e-1-3]]
(b) and is the one of [[lem:ii-f1-2-5]]): each acts in x_i with the other variables as parameters, is bounded H̄^s →
H̄^s (one orthant face fewer) for every s ∈ ℕ₀, and is the identity on {x_i ≥ 0}; so E : H̄^s(ℝ^m_l) → H^s(ℝ^m) is
bounded for every s, Ev = v on ℝ^m_l, and if supp v ⊂ {x_m ≥ a} with m > l, then supp Ev ⊂ {x_m ≥ a}. Put
S^(l)_Λ v := (S^(0)_Λ Ev)|_(ℝ^m_l). Then ‖S^(l)_Λ v‖_(H̄^s) ≤ ‖S^(0)_Λ Ev‖_(H^s), and v − S^(l)_Λ v is the restriction
of Ev − S^(0)_Λ Ev; so [[eq:ii-g-3-2]] holds for S^(l)_Λ on the spaces H̄^s(ℝ^m_l), with C multiplied by the norm of E
on H̄^t. If supp v ⊂ {x_m ≥ a}, m > l, then supp S^(l)_Λ v ⊂ {x_m ≥ a − 2Λ^(−1/2)}.

*Step 3: charts at {|t| ≤ c_1}.* We use charts φ_α : U_α → ℝ^m_(l_α) (m = dim M, l_α ∈ {0, 1}) of two kinds, in each
of which t is the last coordinate x_m. (a) Near a point of M ∩ {|t| ≤ c_1} on no face of ℋ_b: by (T1), t and, at a face
H ∈ ℋ̄, a defining function x_1 of H are part of a coordinate system (dt|_(TH) ≠ 0), giving a chart onto an open subset
of ℝ^m_1, or of ℝ^m away from ℋ̄, with image in {|x_m| < 2c_1}. (b) Near a point p as in (T2): shrinking V, (ρ, z, t̄),
ρ := ρ_H, are coordinates on V ≅ [0, 2) × (−2, 2)^(m−2) × (−a, a), and the cells V_j := {2^(−j−2) < ρ < 2^(−j+1)},
j ≥ 3, with the coordinates (x^(j), z, t̄), x^(j) := −log_2 ρ − j ∈ (−1, 2), are unit cells of the b-structure: ρ∂_ρ,
∂_z, ∂_(t̄) are constant multiples of the coordinate fields, uniformly in j. As t − t̄ ∈ ρ^ε C^∞_b(V), in these
coordinates t − t̄ and all its derivatives are O(2^(−εj)); so for j ≥ j_0, (x^(j), z, t) are coordinates on V_j (shrunk
slightly), with transition maps to (x^(j), z, t̄) bounded in C^∞ uniformly in j. The cells with j < j_0 lie in a compact
subset of M′°, near which charts of kind (a) serve. By compactness of M ∩ {|t| ≤ c_1} ∖ ⋃_(H∈ℋ_b) {ρ_H < ρ_1} for small
ρ_1, finitely many charts of kind (a) and finitely many families of cells of kind (b) cover M ∩ {−c_1 ≤ t ≤ c_1};
together they form a family of finite multiplicity with transition maps uniformly bounded in C^∞, a bounded geometry
structure on a neighbourhood W of that set in the sense of (S1) of [[sec:ii-a-3]] ([Hin26d, Definitions 1.1, 1.3]),
the b-structure there, and contained in {|t| < 2c_1}. Choose χ_α ∈ C^∞_c(U_α), uniformly bounded in C^∞ in the chart
coordinates, with Σ_α χ_α = 1 on M ∩ {−c_1/2 ≤ t ≤ 3c_1/4}, and χ̃_α ∈ C^∞_c(U_α), likewise uniform, equal to 1 on the
1/2-neighbourhood (in the chart coordinates) of supp χ_α (shrinking the supports of the χ_α within the cells if
necessary).

*Step 4: the operators.* Let ψ, ψ_3 ∈ C^∞(ℝ) with ψ = 1 on (−∞, c_1/2], ψ = 0 on [3c_1/4, ∞), ψ_3 = 0 on (−∞, c_1/8]
and ψ_3 = 1 on [c_1/4, ∞); by (T3), ψ(t), ψ_3(t) ∈ C^∞_b, so multiplication by them is bounded on every w H̄^k_b(M). Let
S̃_θ be a smoothing operator on all of w H̄^0_b(M), built in the same way from a bounded geometry cover of a
neighbourhood of M in M′ by b-cells and, at the faces of ℋ̄ and their corners with those of ℋ_b, charts onto orthants
ℝ^m_l, with no condition on supports: S̃_θ v := Σ_β χ̃_β φ_β^* S^(l_β)_θ((φ_β)_*(χ_β v)). With Λ := 4θ/c_0² (≥ 16), put

    S_θ u := Σ_α χ̃_α φ_α^* S^(l_α)_Λ((φ_α)_*(χ_α ψ(t) u)) + ψ_3(t) S̃_θ((1 − ψ(t)) u),     u ∈ B^0.     {#eq:ii-g-3-3}

*Supports.* Let u ∈ B^0_η, η ∈ [θ^(−1/2), 1], so supp u ⊂ {t ≥ c_0 η}. In the chart φ_α, (φ_α)_*(χ_α ψ(t) u) is
supported in {x_m ≥ c_0 η}, so by Step 2 the α-term is supported in {t ≥ c_0 η − 2Λ^(−1/2)} = {t ≥ c_0(η −
θ^(−1/2))}. The last term is supported in {t ≥ c_1/8} = {t ≥ c_0} ⊂ Ω_(c_0(η−θ^(−1/2))). So S_θ u ∈ B^∞_(η−θ^(−1/2))
when u ∈ B^∞_η. For u ∈ B^0 the same argument gives supp S_θ u ⊂ Ω_(−c_0 θ^(−1/2)), within the domain of the charts.

*Estimates.* By (S3) of [[sec:ii-a-3]], on the bounded geometry structure of Step 3 (and on that of S̃_θ), the norm of
w H̄^k_b(M) on functions supported in W is equivalent to (Σ_α w_α^(−2) ‖(φ_α)_*(χ_α u)‖²_(H̄^k(ℝ^m_(l_α))))^(1/2),
w_α := sup_(U_α) w, the weight w being bounded above and below by a fixed multiple of w_α on each cell (b-weights vary
by bounded factors on b-cells), with constants independent of the choice of the uniform family χ_α. (S3) concerns charts
onto cubes in a manifold without boundary, and the norm of w H̄^k_b(M) is a quotient norm, so at the faces of ℋ̄ the
equivalence takes two more lines. The bound of the sum by the norm follows from (S3) on M′ applied to an extension of u
with almost minimal norm. Conversely, Σ_α χ̃_α φ_α^* E((φ_α)_*(χ_α u)), with the Seeley operator E of Step 2, is an
extension of u whose norm (S3) bounds by the sum; and multiplication by χ̃_α and the maps φ_α^* are uniformly bounded.
Hence, with [[eq:ii-g-3-2]] for S^(l_α)_Λ, Λ ≤ Cθ, and the finite multiplicity,

    |Σ_α χ̃_α φ_α^* S^(l_α)_Λ((φ_α)_*(χ_α ψu))|_s² ≤ C Σ_α w_α^(−2) θ^(2(s−t)) ‖(φ_α)_*(χ_α ψu)‖²_(H̄^t)
                                                   ≤ C θ^(2(s−t)) |ψu|_t² ≤ C θ^(2(s−t)) |u|_t²

for s ≥ t, and the same for S̃_θ and for the product with ψ_3(t). For s ≤ t: ψu is supported in {0 ≤ t ≤ 3c_1/4},
where Σ_α χ_α = 1, and χ̃_α χ_α = χ_α; so ψu − Σ_α χ̃_α φ_α^* S^(l_α)_Λ(⋯) = Σ_α χ̃_α φ_α^* (I −
S^(l_α)_Λ)((φ_α)_*(χ_α ψu)). As ψ_3 = 1 on supp(1 − ψ(t)), (1 − ψ)u − ψ_3 S̃_θ((1 − ψ)u) = ψ_3 (I − S̃_θ)((1 − ψ)u).
Adding, and estimating as before with the second inequality of [[eq:ii-g-3-2]], |u − S_θ u|_s ≤ C θ^(s−t) |u|_t.
Finally S_θ u ∈ ⋂_k w H̄^k_b(M), every term being smooth with all norms bounded by [[eq:ii-g-3-2]] with t = 0. ∎

The weights enter only through the factors w_α. The proof of [Hin26c, Proposition 12.6] covers {t > 0} by charts
contained in {t > 0} (its Step 3). For the supports to stay in Ω_(c_0(η−θ^(−1/2))) for η up to 1, such charts must lie
in {t > c_0}, which near ℐ⁺ requires charts small in t; and towards ι⁺ the function t^♭ is not a b-smooth coordinate
(t_*∂_(t_*) t^♭ ∼ t^♭). The splitting [[eq:ii-g-3-3]] by ψ(t) avoids the charts away from {|t| ≤ c_1}, smooths the part
in {t ≥ c_1/2} without support control, and multiplies back by ψ_3(t). In Step 1 of [Hin26c, Proposition 12.6] φ
equals 1 on {|ξ| < 1}, so its support is not in the unit ball, and the localiser φ(θ^(1/2) y) enlarges supports by
sup{|ξ| : ξ ∈ supp φ} · θ^(−1/2), not by θ^(−1/2); the factor is absorbed by the choice Λ = 4θ/c_0² in Step 4.

### Tame bounds {#sec:ii-g-4}

**Lemma {#lem:ii-g-4-1}** (Tame bounds; [Hin26c, Lemma 12.8].) Let l, m, n ∈ ℕ₀, D := l + m + n, M := [0, ∞)^l_ρ ×
[0, ∞)^m_x × ℝ^n_y with the density |(dρ_1/ρ_1) ⋯ (dρ_l/ρ_l) dx dy|, and for k ∈ ℕ₀ let H̄^k_b(M) be the space of u ∈
L²(M) with (ρ∂_ρ)^a ∂_x^b ∂_y^c u ∈ L²(M) for |a| + |b| + |c| ≤ k (distributional derivatives on M°), ‖u‖_k the sum of
these L²-norms. Let d ∈ ℕ, d > D/2.

(1) (*Sobolev embedding.*) There is C_Sob with ‖u‖_(L^∞) ≤ C_Sob ‖u‖_d.

(2) (*Products.*) For k ∈ ℕ₀ there is C_k with ‖uv‖_k ≤ C_k (‖u‖_d ‖v‖_k + ‖u‖_(k+d) ‖v‖_0) for u ∈ H̄^(k+d)_b(M),
v ∈ H̄^k_b(M).

(3) (*Nonlinear functions.*) Let δ > 0 and F : [−δ, δ] → ℝ smooth with F(0) = 0. For k ∈ ℕ₀ there is C_k with
‖F(u)‖_k ≤ C_k ‖u‖_(k+d) for real u ∈ H̄^(k+d)_b(M) with ‖u‖_d ≤ δ/C_Sob.

*Proof.* *Reductions.* In s_i := −log ρ_i ∈ ℝ, ρ_i∂_(ρ_i) = −∂_(s_i) and dρ_i/ρ_i = ds_i, so H̄^k_b(M) is isometric
to the space defined in the same way on [0, ∞)^m × ℝ^(n+l) with standard derivatives; relabel, l = 0. Seeley's
extension E across the hyperplanes {x_i = 0} (Step 2 of the proof of [[prop:ii-g-3-1]]) is bounded from H̄^k to
H^k(ℝ^D) for every k, with Ew = w on M, the space defined by distributional derivatives on the interior of an orthant
being that of restrictions, with equivalent norms, by this boundedness. As uv = (Eu Ev)|_M and F(u) = F(Eu)|_M when
|Eu| ≤ δ, it suffices to prove (1)–(3) on ℝ^D, with ‖u‖_k := Σ_(|γ|≤k) ‖∂^γ u‖_(L²), and to take for M the constant
C_Sob of ℝ^D times the norm of E on H̄^d, which makes ‖u‖_d ≤ δ/C_Sob imply ‖Eu‖_(L^∞) ≤ δ.

*(1)* ‖u‖_(L^∞) ≤ (2π)^(−D) ‖û‖_(L¹) ≤ (2π)^(−D) ‖⟨ξ⟩^(−d)‖_(L²) ‖⟨ξ⟩^d û‖_(L²), and ⟨ξ⟩^(−d) ∈ L² as 2d > D;
‖⟨ξ⟩^d û‖_(L²) ≤ C ‖u‖_d by Plancherel.

*Interpolation.* For 0 ≤ p ≤ k, k ≥ 1, and w ∈ H^k(ℝ^D), Hölder's inequality with the exponents k/(k − p), k/p gives
‖|ξ|^p ŵ‖_(L²) ≤ ‖ŵ‖_(L²)^(1−p/k) ‖|ξ|^k ŵ‖_(L²)^(p/k), and Σ_(|γ|=p) ‖∂^γ w‖_(L²) is bounded above and below by
constant multiples of ‖|ξ|^p ŵ‖_(L²); so

    Σ_(|γ|=p) ‖∂^γ w‖_(L²) ≤ C ‖w‖_0^(1−p/k) ‖w‖_k^(p/k).                                          {#eq:ii-g-4-1}

*(2)* For k = 0, ‖uv‖_0 ≤ ‖u‖_(L^∞) ‖v‖_0 ≤ C_Sob ‖u‖_d ‖v‖_0. Let k ≥ 1, |γ| ≤ k and β ≤ γ, p := |β|, q := |γ| −
p ≤ k − p. By (1) and [[eq:ii-g-4-1]] applied to ∂^ε u, |ε| ≤ d,

    ‖∂^β u‖_(L^∞) ≤ C_Sob Σ_(|ε|≤d) ‖∂^β ∂^ε u‖_(L²) ≤ C ‖u‖_d^(1−p/k) ‖u‖_(k+d)^(p/k),

and by [[eq:ii-g-4-1]], as q/k ≤ 1 − p/k and ‖v‖_0 ≤ ‖v‖_k, ‖∂^(γ−β) v‖_(L²) ≤ C ‖v‖_0^(1−q/k) ‖v‖_k^(q/k) ≤
C ‖v‖_0^(p/k) ‖v‖_k^(1−p/k). So

    ‖∂^β u ∂^(γ−β) v‖_(L²) ≤ C (‖u‖_d ‖v‖_k)^(1−p/k) (‖u‖_(k+d) ‖v‖_0)^(p/k) ≤ C (‖u‖_d ‖v‖_k + ‖u‖_(k+d) ‖v‖_0),

by a^(1−λ) b^λ ≤ a + b; the Leibniz rule and the sum over |γ| ≤ k give (2).

*(3)* |F(s)| ≤ C|s| on [−δ, δ], so ‖F(u)‖_0 ≤ C ‖u‖_0. Let k ≥ 1; as k + d > k + D/2, u has bounded continuous
derivatives of order ≤ k, and for 1 ≤ |γ| ≤ k, by the chain rule, ∂^γ F(u) is a sum of terms c F^(r)(u) ∂^(γ_1)u ⋯
∂^(γ_r)u with 1 ≤ r ≤ |γ|, γ_1 + ⋯ + γ_r = γ and p_i := |γ_i| ≥ 1. |F^(r)(u)| ≤ C, and, as in (2),
‖∂^(γ_i) u‖_(L^∞) ≤ C ‖u‖_d^(1−p_i/k) ‖u‖_(k+d)^(p_i/k) for i ≥ 2, and ‖∂^(γ_1) u‖_(L²) ≤ C ‖u‖_0^(1−p_1/k)
‖u‖_k^(p_1/k) ≤ C ‖u‖_d^(1−p_1/k) ‖u‖_(k+d)^(p_1/k). So the term is bounded in L² by

    C ‖u‖_d^(r−|γ|/k) ‖u‖_(k+d)^(|γ|/k) ≤ C ‖u‖_d^(r−1) ‖u‖_(k+d) ≤ C′ ‖u‖_(k+d),

as ‖u‖_d ≤ ‖u‖_(k+d) and ‖u‖_d ≤ δ/C_Sob. ∎

[Hin26c, Lemma 12.8] states (3) for u ∈ H̄^k_b(M); the bound is in terms of ‖u‖_(k+d), which is finite only for u ∈
H̄^(k+d)_b(M), and its (2) has the same feature. The proof of (2) there interpolates by iterating an integration by
parts; [[eq:ii-g-4-1]] is the same inequality read off the Fourier transform.

### The weights of a forward problem in dimension 4 + 1, and what is not used {#sec:ii-g-5}

#### The weights {#sec:ii-g-5-1}

Let P_0 be a stationary wave-type operator with S̄ = 0 which is 0-admissible with sf-loss 0, as [Hin26c, Theorem 12.2]
proves for the scalar wave operator on Kerr. [[thm:ii-f1-1-1]], with ℵ = δ = 0, then applies for weights with α_I <
−1/2 and α_+ < α_I − 1/2 ([[eq:ii-f1-1-3]]), and α_+ + 2 must lie in the indicial gap of P̂_0(0) ([[def:ii-c-2-7]]
(2)). For the scalar wave operator in dimension 4 + 1 the gap is (0, 2), the indicial roots at angular momentum 0 being
0 and 2 (the remark after [[def:ii-c-2-7]]); so α_+ ∈ (−2, α_I − 1/2), and with α_I = −1/2 − ε_I, α_+ = −1 − ε_+,

    0 < ε_I < ε_+ < 1.                                                                             {#eq:ii-g-5-1}

In dimension 3 + 1 the same reasoning, with the gap shifted to (−3/2, −1/2) for α_+, gives 0 < ε_I < ε_+ < 1/2;
[Hin26c, (12.7)] prints 0 < ε_+ < ε_I < 1/2, whereas the condition α_+ < α_I − 1/2 of [Hin26c, (11.5), p. 228] is
ε_+ > ε_I. In the b-weights of [[cor:ii-f1-1-2]], b_I = α_I + 2 = 3/2 − ε_I and b_+ = α_+ + 5/2 = 3/2 − ε_+, and
[[eq:ii-f1-1-8]] gives, for k ≥ 3 and forward solutions of Pu = f with P as in [[thm:ii-f1-1-1]] and f in the space
[[eq:ii-f1-1-4]], with the density μ_b of [[eq:ii-f1-1-7]],

    |(t_*∂_(t_*), r∂_x)^(≤k−3) u| ≤ C ρ_I^(3/2−ε_I) ρ_+^(3/2−ε_+) ρ_K^(1/2),                       {#eq:ii-g-5-2}

the form in dimension 4 + 1 of [Hin26c, (12.8a)], whose exponents in dimension 3 + 1 are 1 − ε_I and 1 − ε_+: at ℐ⁺,
where ρ_I ∼ r⁻¹ at bounded t_*, waves decay nearly like r^(−3/2) in five spacetime dimensions, against r⁻¹ in four.

#### What of [Hin26c, Section 12] is not used {#sec:ii-g-5-2}

(a) [Hin26c, Theorem 12.2], the 0-admissibility of □_g on Kerr, is a four-dimensional statement resting on the mode
stability of Kerr. Its analogue for the scalar wave operator on the five-dimensional background would rest on scalar
mode stability there, which the stability theory does not use.

(b) [Hin26c, Theorem 12.3], mode stability implies 0-admissibility. Its proof assembles the estimates of
[[ch:s01]]–[[ch:s03]] at high, bounded and low frequencies on the Fourier transform in t_* and closes with a
Paley–Wiener argument for the support. Its version with a loss ℵ > 0, which the gauge-fixed linearised Einstein operator
needs, is proved in [[ch:s18]].

(c) The model problems: [Hin26c, Theorem 12.9] (power nonlinearity, p ≥ 4), [Hin26c, Remark 12.10], [Hin26c, Theorem
12.11] (a quasilinear equation with spatially compact metric perturbations), [Hin26c, Theorem 12.12] (a null form) and
[Hin26c, Remark 12.13]. Their weights are subject to the reversal noted after [[eq:ii-g-5-1]]: [Hin26c, Theorem 12.9]
asks 0 < ε_+ < min(1/3, ε_I) and [Hin26c, Theorem 12.11] asks 0 < ε_+ < ε_I < 1/2, while the b-weights of [Hin26c,
(11.5)], β_I = 1 − ε_I and β_+ = 1 − ε_+, require β_+ < β_I, that is ε_+ > ε_I; in [Hin26c, Theorem 12.9] the
conditions [Hin26c, (12.23)] of its proof, (p − 1)(1 − ε_I) ≥ 1 and (p − 1)(1 − ε_+) ≥ 2, hold for p ≥ 4 and ε_I <
ε_+ ≤ 1/3. [Hin26c, Theorem 12.12] prints β_+ = −1 − ε_+, while its proof uses β_+ = 1 − ε_+ [Hin26c, p. 243].
