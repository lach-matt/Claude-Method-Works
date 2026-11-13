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
