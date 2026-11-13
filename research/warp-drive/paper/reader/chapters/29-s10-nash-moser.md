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

This is [Hin26c, Theorem 12.4], with its hypotheses made precise where they are stated loosely; [Hin26c] quotes the
theorem from [SR89] in the form of [Hin24a, Theorem 6.11], with the regularity 16d² + 43d + 24 in place of N_NM. The
proof below needs the constants up to the order N_NM. [Hin26c, Theorem 12.4] states (ii) for all η ∈ [0, 1], together
with Φ(0) ∈ F^∞_(η_0); as 0 ∈ B^∞_η for every η, the hypothesis for all η ∈ [0, 1] would force Φ(0) ∈ F^∞_1. The form
above asks (ii) only for η ≤ η_0; in the applications of [Hin26c] both forms hold, with η_0 = 1, the right side being
supported in {t_* ≥ 2}. The conclusion of [Hin26c, Theorem 12.4] is u ∈ B^∞; as its B^k_0 is the whole space ([Hin26c,
(12.21)]), that is the support t_* ≥ 1 its applications use [Hin26c, p. 240], the better support t_* ≥ 2 being obtained
there by local uniqueness. [[thm:ii-g-2-1]] strengthens the conclusion to u ∈ B^∞_(η_0/2), which costs the closedness of
the B^k_η; the spaces of [[prop:ii-g-3-1]] have it.

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

**Remark {#rem:ii-g-3-2}** (The domain Ω_* in dimension 4 + 1; [Hin26c, Example 12.7].) Let M be the closure of {t_* ≥
1/2, r ≥ r_0} in the compactified spacetime M̃ of [[sec:ii-a-1]], a compact manifold with corners with boundary
hypersurfaces ℐ⁺, ι⁺, K⁺ (forming ℋ_b) and {r = r_0}, {t_* = 1/2} (forming ℋ̄), and M′ the closure of {t_* > 1/4, r >
r^♯} less its faces at t_* = 1/4 and r = r^♯, where r^♯ ∈ (r_0 − δ_0, r_0) is the radius of [[lem:ii-e-1-2]];
μ := |dt_* dx|/(t_* ⟨x⟩⁴), a smooth positive b-density ([[cor:ii-f1-1-2]], [[lem:ii-a-8-8]]); w := ρ_I^(a_I) ρ_+^(a_+)
ρ_K^(a_K) with the defining functions [[eq:ii-f1-1-1]]; t := t^♭ − 1, with t^♭ the time function of [[lem:ii-c-3-2]],
defined on M′ ∩ {t_* ≥ 1/2} by [[lem:ii-e-1-2]] (iv), and t := −1 on M′ ∩ {t_* < 1/2}. As t^♭ ≤ t_* ([[lem:ii-c-3-2]]
(b)), t < −c_1 on {t_* < 7/8}, so every function ψ(t) of (T3) is constant there, and t is smooth wherever (T1) asks. The
spaces B^k_0 of [[prop:ii-g-3-1]] are then the spaces H^(k,(α_I,α_+,α_K))_b(Ω_*; E)^(•,−) of [[eq:ii-f1-1-2]],
componentwise and with w adjusted by the factor relating |dt dx| to μ, which is a product of powers of ρ_I, ρ_+, ρ_K
([[cor:ii-f1-1-2]]), with equivalent norms: there the quotient is over extensions supported in {t^♭ ≥ 1}, here over all
extensions to M′, and the extension of [[lem:ii-f1-2-5]] preserves that support and is bounded at every order. B^k_η
consists of their elements supported in {t^♭ ≥ 1 + c_0 η}. The hypotheses hold with c_1 := 1/8:

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

### Improving decay: scope, and what dimension 4 + 1 changes {#sec:ii-g1-1}

[Hin26c, Section 13], "Improving decay", has four subsections. Its Sections 13.1–13.3 are general tools, proved here in
dimension 4 + 1 in the forms used later: the Fourier transform on the line ([Hin26c, Lemmas 13.2, 13.4, 13.6,
Corollaries 13.3, 13.5, 13.7]) and on the resolved spaces ([Hin26c, Lemma 13.8, Propositions 13.9 and 13.11, Lemma
13.10, Remark 13.12]); the resolvent bounds ([Hin26c, Lemma 13.13, Corollary 13.14, Proposition 13.16, Corollary 13.17,
the bounds (13.30), Proposition 13.18]); and the radiation field ([Hin26c, Definition 13.19, Proposition 13.20]). Its
Section 13.4 ([Hin26c, Theorem 13.21 and Remark 13.22]) is a model application to the scalar wave equation on Kerr and
is not used ([[sec:ii-g1-6-1]]). The tools are used in the linear theory, where the decay of solutions of the
linearised gauge-fixed Einstein equations is improved beyond [[thm:ii-f1-1-1]] as [Hin26c, Section 14] does for its
1-form example.

In dimension 4 + 1 the statements change as follows; each change is derived where the statement is proved.

(a) *Densities.* On X, μ := |dx| and μ_b := |dx|/⟨x⟩⁴, so L²(X, μ) = ρ² L²(X, μ_b), ρ := ⟨x⟩⁻¹: a scattering decay
order 𝗋 is a b-weight 𝗋 + 2. The shifts 5/2 and 3/2 of [Hin26c, (13.23a)–(13.23b)] become 3 and 2, and its 5/2, 7/2,
3/2 in [Hin26c, (13.30)] become 3, 4, 2.

(b) *Thresholds.* The condition β_scf < 1 + S̄ of [Hin26c, Corollaries 13.14, 13.17, Propositions 13.16, 13.18] becomes
β_scf < 3/2 + S̄, the threshold 𝗋 < −1/2 + S̄ at the outgoing radial set of [[eq:i-a-1-5]], read as a b-weight.

(c) *The zero energy gap.* The gap condition of [Hin26c, Proposition 13.18] is on the b-weight for μ_b, as in (G) of
[[sec:i-c-1-2]]: β_tf − β_zf lies in an indicial gap of P̂(0).

(d) *The radiation field.* Near ℐ⁺ ∩ ι⁺ the stationary model has the form (1/2) ρ_I⁻¹ ρ_+^(−2) P_0 = −(ρ_I∂_(ρ_I) −
3/2)(ρ_I∂_(ρ_I) − ρ_+∂_(ρ_+)) + P̃ ([[lem:ii-g1-5-1]]), where [Hin26c, (13.32)] has ρ_I∂_(ρ_I) − 1; the radiation field
is the coefficient of ρ_I^(3/2), that is of r^(−3/2) at bounded t_*, and [Hin26c, Proposition 13.20] holds with 3/2 in
place of 1 ([[prop:ii-g1-5-4]]).

From here to the end of the chapter, ℋ denotes a separable Hilbert space, functions may be ℋ-valued, and |·| is the norm
of ℋ. For the bundle E of [[sec:i-a-1-2]] every space is taken componentwise.

### The Fourier transform on the line {#sec:ii-g1-2}

#### Conventions {#sec:ii-g1-2-1}

(ℱu)(σ) := ∫ e^(iσt) u(t) dt and (ℱ⁻¹v)(t) := (2π)⁻¹ ∫ e^(−iσt) v(σ) dσ, as in [Hin26c]. Plancherel's theorem
‖ℱu‖_(L²(dσ)) = (2π)^(1/2) ‖u‖_(L²(dt)) holds for ℋ-valued functions (componentwise in an orthonormal basis).
ℱ(∂_t u) = −iσ ℱu and ℱ(tu) = D_σ ℱu, D_σ := −i∂_σ. For γ ∈ ℝ let H^γ(ℝ_σ; ℋ) := {v ∈ 𝒮′ : ⟨t⟩^γ ℱ⁻¹v ∈ L²(dt)},
‖v‖_(H^γ) := (2π)^(1/2) ‖⟨t⟩^γ ℱ⁻¹v‖_(L²); as (ℱ⁻¹v)(t) = (2π)⁻¹ v̂(t) with v̂(τ) := ∫ e^(−iστ) v(σ) dσ, this is the
usual Sobolev space, with the usual norm (2π)^(−1/2) ‖⟨τ⟩^γ v̂‖.

**Definition {#def:ii-g1-2-1}** ([Hin26c, Section 13.1.1].) For k ∈ ℕ₀ and β ∈ ℝ, H^(k,β)_b(ℝ; ℋ) is the space of u ∈ 𝒮′
with ⟨t⟩^(β−1/2) ∂_t^p (t∂_t)^q u ∈ L²(ℝ, dt; ℋ) for p + q ≤ k, normed by the sum of these norms.

This is the space ⟨t⟩^(−β) H^k_b(ℝ, |dt/⟨t⟩|) of [Hin26c]: ⟨t⟩^(−β) L²(dt/⟨t⟩) = ⟨t⟩^(−β+1/2) L²(dt), and the
b-vector fields of the radial compactification, spanned by ⟨t⟩∂_t over its smooth functions, are spanned by ∂_t =
⟨t⟩⁻¹ · ⟨t⟩∂_t and t∂_t = (t/⟨t⟩) ⟨t⟩∂_t, as ⟨t⟩∂_t = ⟨t⟩⁻¹ ∂_t + (t/⟨t⟩) t∂_t; the words of length ≤ k in ∂_t, t∂_t
span the same space as the ordered products ∂_t^p (t∂_t)^q, as [∂_t, t∂_t] = ∂_t.

**Lemma {#lem:ii-g1-2-2}** ([Hin26c, (13.1)].) u ∈ H^(k,β)_b(ℝ; ℋ) if and only if σ^p (σ∂_σ)^q ℱu ∈ H^(β−1/2)(ℝ; ℋ)
for all p + q ≤ k, with equivalent norms.

*Proof.* ℱ(t∂_t u) = D_σ(−iσ ℱu) = −(1 + σ∂_σ) ℱu, so ℱ(∂_t^p (t∂_t)^q u) = (−iσ)^p (−1 − σ∂_σ)^q ℱu. The operators
σ^p (1 + σ∂_σ)^q, p + q ≤ k, and σ^p (σ∂_σ)^q, p + q ≤ k, are related by a triangular matrix with ones on the diagonal
(binomial expansion), so they span the same space. And ‖⟨t⟩^(β−1/2) w‖_(L²) = (2π)^(−1/2) ‖ℱw‖_(H^(β−1/2)) by
definition. ∎

#### The Gagliardo seminorm and two Hardy inequalities {#sec:ii-g1-2-2}

For θ ∈ (0, 1) and g ∈ L²(ℝ; ℋ) let [g]_θ² := ∬ |g(x) − g(y)|² |x − y|^(−1−2θ) dx dy ∈ [0, ∞].

**Lemma {#lem:ii-g1-2-3}** (The Gagliardo seminorm and two Hardy inequalities.) Let θ ∈ (0, 1).

(a) [g]_θ² = c_θ (2π)⁻¹ ∫ |ξ|^(2θ) |ĝ(ξ)|² dξ with c_θ := ∫ |e^(is) − 1|² |s|^(−1−2θ) ds ∈ (0, ∞). So ‖g‖²_(L²) +
[g]_θ² is equivalent to ‖g‖²_(H^θ), and for ψ ∈ C^∞_c(ℝ) and ε > 0, [ψ(·/ε)]_θ² = ε^(1−2θ) [ψ]_θ².

(b) If θ < 1/2, then ∫_(−1)^1 |x|^(−2θ) |g|² dx ≤ C_θ (‖g‖²_(L²(−1,1)) + [g]_θ²).

(c) If θ > 1/2 and g ∈ H^θ, then g is continuous, and if g(0) = 0 then ∫_(−1)^1 |x|^(−2θ) |g|² dx ≤ C_θ [g]_θ².

(d) If θ < 1/2 and w ∈ L¹_loc is supported in [−1, 1] with |x|^θ w ∈ L², then w ∈ H^(−θ) and ‖w‖_(H^(−θ)) ≤
C_θ ‖|x|^θ w‖_(L²).

*Proof.* (a) For fixed h, ∫ |g(x + h) − g(x)|² dx = (2π)⁻¹ ∫ |e^(ihξ) − 1|² |ĝ(ξ)|² dξ by Plancherel. Integrating
against |h|^(−1−2θ) dh (Tonelli) and substituting s = hξ gives the identity; c_θ < ∞ as |e^(is) − 1|² ≤ min(s², 4),
and c_θ > 0. Then 1 + c_θ |ξ|^(2θ) is comparable to ⟨ξ⟩^(2θ). The scaling follows by substituting x = εx′, y = εy′.

(b), (c). By symmetry consider (0, 1]. Let I_k := [2^(−k−1), 2^(−k)], k ≥ 0, a_k := 2^(k+1) ∫_(I_k) g, and

    E_k := ∬_(I_k×I_k) |g(x) − g(y)|² |x − y|^(−1−2θ) dx dy,
    E′_k := ∬_(I_k×I_(k+1)) |g(x) − g(y)|² |x − y|^(−1−2θ) dx dy,

so Σ_k (E_k + E′_k) ≤ 2[g]_θ², the regions being disjoint. By Jensen's inequality, |g(x) − a_k|² ≤ 2^(k+1) ∫_(I_k)
|g(x) − g(y)|² dy, and |x − y| ≤ 2^(−k−1) on I_k × I_k, so ∫_(I_k) |g − a_k|² ≤ 2^(−2θ(k+1)) E_k. Likewise |a_k −
a_(k+1)|² ≤ 2^(2k+3) ∬_(I_k×I_(k+1)) |g(x) − g(y)|², and |x − y| ≤ 2^(−k) there, so |a_k − a_(k+1)|² ≤ 8 ·
2^(k(1−2θ)) E′_k. Hence

    ∫_0^1 x^(−2θ) |g|² ≤ Σ_k 2^(2θ(k+1)) · 2 (∫_(I_k) |g − a_k|² + 2^(−k−1) |a_k|²) ≤ 2 Σ_k E_k + 2^(2θ) Σ_k b_k²,
                                                                          b_k := 2^(k(θ−1/2)) |a_k|.

For (b), θ < 1/2: |a_k| ≤ |a_0| + Σ_(j<k) |a_(j+1) − a_j|, so with q := 2^(θ−1/2) < 1 and e_j := E′_j^(1/2), b_k ≤
q^k |a_0| + √8 Σ_(j<k) q^(k−j) e_j. By Cauchy–Schwarz (Σ_(j<k) q^(k−j) e_j)² ≤ (q/(1 − q)) Σ_(j<k) q^(k−j) e_j², and
summing over k, Σ_k b_k² ≤ (2/(1 − q²)) |a_0|² + 16 (q/(1 − q))² Σ_j e_j²; finally |a_0|² ≤ 2 ‖g‖²_(L²(I_0)). For
(c), θ > 1/2: ĝ ∈ L¹ as ∫ |ĝ| ≤ ‖⟨ξ⟩^θ ĝ‖ ‖⟨ξ⟩^(−θ)‖, so g is continuous; if g(0) = 0 then a_k → 0, so a_k =
Σ_(j≥k) (a_j − a_(j+1)), and with q := 2^(1/2−θ) < 1, b_k ≤ √8 Σ_(j≥k) q^(j−k) e_j, whence Σ_k b_k² ≤ 8 (1 − q)^(−2)
Σ_j e_j² in the same way.

(d) For φ ∈ 𝒮, |∫ ⟨w, φ⟩_ℋ| ≤ ‖|x|^θ w‖_(L²) ‖|x|^(−θ) φ‖_(L²(−1,1)) ≤ C ‖|x|^θ w‖_(L²) ‖φ‖_(H^θ) by (b) and (a), and
H^(−θ) is the dual of H^θ for the L² pairing. ∎

#### Taylor expansions at σ = 0 {#sec:ii-g1-2-3}

For γ > −1/2 let n_0(γ) be the number of ℓ ∈ ℕ₀ with ℓ < γ − 1/2.

**Lemma {#lem:ii-g1-2-4}** (Taylor expansion at σ = 0; the content of [Hin26c, Corollary 13.3 and Lemma 13.4] that is
used.) Let γ ∈ (0, ∞) ∖ (1/2 + ℕ₀), n_0 := n_0(γ) and g ∈ H^γ(ℝ; ℋ). Then g ∈ C^(n_0−1) (no condition if n_0 = 0),
|g^(ℓ)(0)| ≤ C ‖g‖_(H^γ) for ℓ < n_0, and with P_g(σ) := Σ_(ℓ<n_0) g^(ℓ)(0) σ^ℓ/ℓ!,

    ‖|σ|^(−γ) (g − P_g)‖_(L²(−1,1)) ≤ C ‖g‖_(H^γ).                                                  {#eq:ii-g1-2-1}

*Proof.* For ℓ < γ − 1/2, ∫ |τ|^ℓ |ĝ(τ)| dτ ≤ ‖⟨τ⟩^γ ĝ‖ ‖⟨τ⟩^(ℓ−γ)‖_(L²), which gives the continuity of g^(ℓ) and the
bound. Write γ = p + θ, p ∈ ℕ₀, θ ∈ [0, 1) ∖ {1/2}.

If θ ∈ [0, 1/2), then n_0 = p. Put f := g^(p), so ‖f‖_(H^θ) ≤ ‖g‖_(H^γ), and ‖|σ|^(−θ) f‖_(L²(−1,1)) ≤ C ‖g‖_(H^γ):
for θ = 0 trivially, for θ > 0 by [[lem:ii-g1-2-3]] (a), (b).

If θ ∈ (1/2, 1), then n_0 = p + 1. Put f := g^(p) − g^(p)(0). With ψ ∈ C^∞_c((−2, 2)) equal to 1 on [−1, 1], ψf =
ψg^(p) − g^(p)(0)ψ ∈ H^θ with norm ≤ C ‖g‖_(H^γ) and (ψf)(0) = 0, so ‖|σ|^(−θ) f‖_(L²(−1,1)) ≤ C ‖g‖_(H^γ) by
[[lem:ii-g1-2-3]] (c).

In both cases, if p = 0 then g − P_g = f on (−1, 1) and [[eq:ii-g1-2-1]] is the bound on f. If p ≥ 1, Taylor's formula
with integral remainder (g^(p−1) is absolutely continuous, as g ∈ H^p_loc) gives g(σ) − P_g(σ) = σ^p ∫_0^1 f(sσ)
(1 − s)^(p−1)/(p − 1)! ds; for θ > 1/2 this uses ∫_0^σ g^(p)(0) (σ − τ)^(p−1)/(p − 1)! dτ = g^(p)(0) σ^p/p!. By
Minkowski's inequality and ‖|sσ|^(−θ) f(sσ)‖_(L²(−1,1;dσ)) = s^(−1/2) ‖|τ|^(−θ) f‖_(L²(−s,s)),

    ‖|σ|^(−γ) (g − P_g)‖_(L²(−1,1)) ≤ ∫_0^1 s^(θ−1/2) ((1 − s)^(p−1)/(p − 1)!) ds · ‖|τ|^(−θ) f‖_(L²(−1,1)),

and θ − 1/2 > −1. ∎

**Lemma {#lem:ii-g1-2-5}** (Taylor coefficients under σ^j (σ∂_σ)^l.) Let n_0 ≥ 1, J ∈ {(−1, 1), (0, 1)}, R ∈
C^(n_0−1)(J̄ ∩ (−1, 1); ℋ) with R^(i)(0) = 0 for i < n_0 (one-sided derivatives if J = (0, 1)), and j, l ∈ ℕ₀. If the
distribution G := σ^j (σ∂_σ)^l R on J extends to an element of C^(n_0−1)(J̄ ∩ (−1, 1)), then G^(i)(0) = 0 for i < n_0.

*Proof.* Fix i < n_0. The moments m_(i′)(φ) := ∫ s^(i′) φ(s) ds, i′ < n_0, are linearly independent functionals on
C^∞_c((1, 2)), so there is φ with m_(i′)(φ) = δ_(ii′) i!. By Taylor's formula with Peano remainder, G(εs) =
Σ_(i′<n_0) G^(i′)(0) (εs)^(i′)/i′! + o(ε^(n_0−1)) uniformly for s ∈ [1, 2], so ε^(−1−i) ∫ G(σ) φ(σ/ε) dσ → G^(i)(0) as
ε → 0. On the other hand, as (σ∂_σ)^T = −1 − σ∂_σ and σ∂_σ commutes with dilations, ∫ G φ(σ/ε) dσ = ∫ R(σ) ε^j
Φ(σ/ε) dσ with Φ := (−1 − s∂_s)^l (s^j φ) ∈ C^∞_c((1, 2)), and this is ε^(j+1) ∫ R(εs) Φ(s) ds = ε^(j+1)
o(ε^(n_0−1)). So ε^(−1−i) ∫ G φ(σ/ε) dσ = o(ε^(j+n_0−1−i)) → 0. ∎

**Lemma {#lem:ii-g1-2-6}** (Gluing.) Let γ ∈ (−1/2, ∞) ∖ (1/2 + ℕ₀) and m := ⌈γ_+⌉, where γ_± := max(±γ, 0). Let w be
a function on ℝ ∖ {0}, vanishing for |σ| ≥ 2, with (σ∂_σ)^l w ∈ |σ|^γ L²(±(0, ∞); ℋ) on each side for l ≤ m, and
N(w) := Σ_(l≤m) ‖|σ|^(−γ) (σ∂_σ)^l w‖_(L²(ℝ∖0)). Then w ∈ L¹_loc(ℝ) and, as a distribution on ℝ, w ∈ H^γ(ℝ; ℋ) with
‖w‖_(H^γ) ≤ C N(w).

*Proof.* |σ|^γ L² ⊂ L¹_loc near 0 as γ > −1/2. If γ ∈ (−1/2, 0) this is [[lem:ii-g1-2-3]] (d) with θ = −γ (scaled to
[−2, 2]); if γ = 0 it is trivial. Let γ > 0, γ = p + θ as before. On each side ∂_σ^l w = σ^(−l) Σ_(i≤l) a_(li)
(σ∂_σ)^i w with constants a_(li), so ∂_σ^l w ∈ |σ|^(γ−l) L² on each side for l ≤ m, with norm ≤ C N(w).

*No distributions at 0.* For ℓ < γ − 1/2 we have ℓ + 1 ≤ m, and ∂^(ℓ+1) w ∈ |σ|^(γ−ℓ−1) L² ⊂ L¹ near 0 on each side
(γ − ℓ − 1 > −1/2), so ∂^ℓ w has one-sided limits at 0; as ∂^ℓ w ∈ |σ|^(γ−ℓ) L² with γ − ℓ > 1/2, they vanish. A function
that is W^(1,1) on each side of 0 near 0 and continuous at 0 has as distributional derivative its pointwise derivative.
Inductively the distributional derivatives ∂^i w, i ≤ n_0(γ), are the functions ∂^i w on ℝ ∖ 0. As n_0(γ) ≥ p, w ∈ H^p
with norm ≤ C N(w) (γ − i ≥ 0 for i ≤ p, and the support is compact). If θ = 0 we are done.

*The fractional part.* Let θ ∈ (0, 1) and G := ∂^p w, so G ∈ |σ|^θ L² and G′ ∈ |σ|^(θ−1) L² on each side (as m =
p + 1). Let A := {(x, y) : |x − y| ≤ |x|/2}; on A, x and y have the same sign. With J_k := [2^(−k), 2^(−k+1)], k ∈ ℤ,
and J_k^* := [2^(−k−1), 3 · 2^(−k)], for |h| ≤ 2^(−k) we have G(x + h) − G(x) = h ∫_0^1 G′(x + sh) ds and so
∫_(J_k) |G(x + h) − G(x)|² dx ≤ h² ∫_(J_k^*) |G′|². Hence

    ∬_(A∩{x>0}) |G(x) − G(y)|² |x − y|^(−1−2θ) ≤ Σ_k ∫_(|h|≤2^(−k)) |h|^(1−2θ) dh ∫_(J_k^*) |G′|²
                                                ≤ C Σ_k ∫_(J_k^*) |x|^(2−2θ) |G′|² ≤ C ‖|σ|^(1−θ) G′‖²,

as θ < 1, |x| ∼ 2^(−k) on J_k^* and the J_k^* overlap boundedly; likewise for x < 0. On the complement of A, |G(x) −
G(y)|² ≤ 2|G(x)|² + 2|G(y)|²; ∫_(|x−y|>|x|/2) |x − y|^(−1−2θ) dy = C|x|^(−2θ), and for fixed y the set of x with |x −
y| > |x|/2 lies in {|x − y| ≥ |y|/4} (if |x − y| < |y|/4 then |x| > (3/4)|y| and |x − y| < (1/3)|x|), so
∫ |x − y|^(−1−2θ) dx ≤ C|y|^(−2θ) there. So [G]_θ² ≤ C ‖|σ|^(−θ) G‖² + C ‖|σ|^(1−θ) G′‖² ≤ C N(w)², G ∈ H^θ by
[[lem:ii-g1-2-3]] (a), and w ∈ H^(p+θ), as ⟨τ⟩^(2γ) ≤ C(1 + |τ|^(2p) ⟨τ⟩^(2θ)). ∎

#### The lossy Fourier transform {#sec:ii-g1-2-4}

Fix χ ∈ C^∞_c((−2, 2)), even, equal to 1 on [−1, 1].

**Definition {#def:ii-g1-2-7}** (The target spaces of the Fourier transform.) For a ∈ (−1, ∞) ∖ ℕ₀ and k ∈ ℕ₀,
X^(k,a)(ℋ) is the space of pairs (v_−, v_+) of functions on (−∞, 0) and (0, ∞) of the form v_± = χP + w_±, with P a
polynomial of degree < a with coefficients in ℋ, the same for both signs, and σ^j (σ∂_σ)^l w_± ∈ |σ|^(a+1/2)
L²(±(0, ∞); ℋ) for j + l ≤ k; the norm is the sum of the norms of the coefficients of P and of
‖|σ|^(−a−1/2) σ^j (σ∂_σ)^l w_±‖.

The decomposition is unique: a polynomial of degree < a that lies in |σ|^(a+1/2) L² near 0 vanishes (its lowest term
would not). Its elements are locally integrable on ℝ (a > −1) and of polynomial growth in L² at infinity, so v := v_− on
(−∞, 0), v_+ on (0, ∞) is a tempered distribution. As |σ|^(a+1/2) L²(dσ) = |σ|^a L²(|dσ/σ|), X^(k,a) is the space of
[Hin26c, Corollary 13.7], with the Taylor polynomial carried by v and the b-regularity by the remainder. The Taylor
terms are indexed by the weight. [Hin26c, (13.7)–(13.8)] index the sum by the regularity ("the sum is empty for s <
1/2"), and the b+-spaces are defined through H^(0,((0,0),β))_b, in which the sum is empty; with no Taylor terms,
[Hin26c, Corollary 13.7 (1)] would fail for β > 1: for u ∈ C^∞_c(ℝ) with ∫ u ≠ 0, u lies in every H^(k,β)_b, while
ℱu(0) ≠ 0 and ℱu ∉ |σ|^(β−1) L²(|dσ/σ|) near 0. The matching condition v_−^(l)(0) = v_+^(l)(0), l < β − 1, of
[Hin26c, Corollary 13.7] presupposes Taylor terms of degree < β − 1, which is the reading of [[def:ii-g1-2-7]].

**Proposition {#prop:ii-g1-2-8}** (The lossy Fourier transform; [Hin26c, Corollary 13.7].) Let β ∈ (0, ∞) ∖ ℕ, γ :=
β − 1/2, ℓ_±(β) := ⌈γ_±⌉ and k ∈ ℕ₀.

(1) If u ∈ H^(k+ℓ_−(β),β)_b(ℝ; ℋ), then (ℱu|_((−∞,0)), ℱu|_((0,∞))) ∈ X^(k,β−1), with norm ≤ C ‖u‖.

(2) If (v_−, v_+) ∈ X^(k+ℓ_+(β),β−1), then ℱ⁻¹v ∈ H^(k,β)_b(ℝ; ℋ), with norm ≤ C ‖(v_−, v_+)‖.

*Proof.* (1) Let v := ℱu and F_(jl) := σ^j (σ∂_σ)^l v; by [[lem:ii-g1-2-2]], F_(jl) ∈ H^γ for j + l ≤ k + ℓ_−.

*Case γ > 0*, so ℓ_− = 0. Let n_0 := n_0(γ) and P := P_v ([[lem:ii-g1-2-4]]), of degree < n_0, that is < γ − 1/2 =
β − 1. Fix j + l ≤ k. If n_0 ≥ 1, R := v − P ∈ C^(n_0−1) with R^(i)(0) = 0 for i < n_0, and σ^j (σ∂_σ)^l R = F_(jl) −
σ^j (σ∂_σ)^l P is C^(n_0−1) ([[lem:ii-g1-2-4]] for F_(jl)); by [[lem:ii-g1-2-5]] its derivatives of order < n_0 at 0
vanish, so P_(F_(jl)) is the part of σ^j (σ∂_σ)^l P of degree < n_0. On (−1, 1) ∖ 0, where χ = 1,

    σ^j (σ∂_σ)^l (v − χP) = (F_(jl) − P_(F_(jl))) − (σ^j (σ∂_σ)^l P − P_(F_(jl))),

the first term in |σ|^γ L²(−1, 1) by [[eq:ii-g1-2-1]], the second a polynomial whose terms have degree ≥ n_0 > γ − 1/2,
hence also in |σ|^γ L²(−1, 1); the bounds are by ‖F_(jl)‖_(H^γ) and the coefficients of P, so by C ‖u‖. If n_0 = 0,
P = 0 and this is [[eq:ii-g1-2-1]] for F_(jl). On |σ| ≥ 1, σ^j (σ∂_σ)^l (v − χP) = F_(jl) minus a smooth function
supported in |σ| ≤ 2, and F_(jl) ∈ L² ⊂ |σ|^γ L² there. So w_± := (v − χP)|_(±(0,∞)) satisfy [[def:ii-g1-2-7]] with
a = β − 1 (|σ|^(a+1/2) = |σ|^γ).

*Case γ = 0*: P = 0 (a = −1/2), and F_(jl) ∈ L².

*Case γ ∈ (−1/2, 0)*, so ℓ_− = 1 and P = 0. Fix j + l ≤ k and let F := F_(jl), G := σF = F_(j+1,l) ∈ H^γ. Then
∂_σ G = (1 + j)F + F_(j,l+1) ∈ H^γ, so G ∈ H^(γ+1) with norm ≤ C ‖u‖. By [[lem:ii-g1-2-4]] at γ + 1 ∈ (1/2, 1), G is
continuous and G − G(0) ∈ |σ|^(γ+1) L²(−1, 1). We show G(0) = 0. Let ψ ∈ C^∞_c((1, 2)) with ∫ ψ(s) ds/s = 1 and
ψ_ε := ψ(·/ε). On (0, ∞), F = G/σ, so ∫ F ψ_ε = G(0) + ∫ (G − G(0)) ψ_ε dσ/σ, and the last term is at most
‖|σ|^(−γ−1) (G − G(0))‖ ‖|σ|^γ ψ_ε‖_(L²) = O(ε^(γ+1/2)) → 0. But |∫ F ψ_ε| ≤ ‖F‖_(H^γ) ‖ψ_ε‖_(H^(−γ)), and by
[[lem:ii-g1-2-3]] (a) with θ = −γ, ‖ψ_ε‖²_(H^(−γ)) ≤ C(ε ‖ψ‖² + ε^(1+2γ) [ψ]²_(−γ)) → 0. So G(0) = 0, and on (−1, 1) ∖
0, F = G/σ ∈ |σ|^γ L²; on |σ| ≥ 1, F = G/σ ∈ |σ|⁻¹ L² ⊂ |σ|^γ L².

(2) Write v = χP + w, w := w_± on ±(0, ∞). σ^p (σ∂_σ)^q (χP) ∈ 𝒮 ⊂ H^γ. *Distributional derivatives.* If f is a
function on ℝ ∖ 0 with f and σ∂_σ f integrable near 0 on both sides, then σf is absolutely continuous on each side
near 0, with one-sided limits at 0 that vanish (else |f| ≥ c/|σ| near 0); so σf is continuous, its distributional
derivative is f + σ∂_σ f, and the distributional σ∂_σ f = ∂_σ(σf) − f is the function σ∂_σ f. Applied repeatedly (each
σ^j (σ∂_σ)^l w lies in |σ|^(a+1/2) L² ⊂ L¹_loc, a + 1/2 = γ > −1/2), W := σ^p (σ∂_σ)^q w, p + q ≤ k, is the same
whether computed on ℝ or on each side. As σ^j (σ∂_σ)^l σ^p (σ∂_σ)^q = σ^(j+p) (σ∂_σ + p)^l (σ∂_σ)^q, σ^j (σ∂_σ)^l W ∈
|σ|^γ L² on each side for j + l ≤ ℓ_+, with norm ≤ C ‖(v_−, v_+)‖. Let ψ ∈ C^∞_c((−2, 2)) equal 1 on [−1, 1]. Then
(σ∂_σ)^l (ψW) ∈ |σ|^γ L² for l ≤ m := ⌈γ_+⌉ = ℓ_+, so ψW ∈ H^γ by [[lem:ii-g1-2-6]]. If γ ≤ 0, (1 − ψ)W ∈ |σ|^γ L² ⊂
L² ⊂ H^γ on |σ| ≥ 1. If γ > 0: for i ≤ m, ∂^i_σ W = σ^(−i) Σ_(i′≤i) a_(ii′) (σ∂_σ)^(i′) W, and σ^(m−i′) (σ∂_σ)^(i′) W
∈ |σ|^γ L² gives σ^(−i) (σ∂_σ)^(i′) W ∈ |σ|^(γ−m+i′−i) L² ⊂ L² on |σ| ≥ 1, as γ ≤ m and i′ ≤ i; so (1 − ψ)W ∈ H^m ⊂
H^γ. Hence σ^p (σ∂_σ)^q v ∈ H^γ for p + q ≤ k, and [[lem:ii-g1-2-2]] gives the claim. ∎

**Remark {#rem:ii-g1-2-9}** (What of [Hin26c, Section 13.1.1] is used.) [Hin26c, Lemma 13.2] (supported and extendible
spaces) and [Hin26c, Lemma 13.6] (the lossless transform) are not used later; [[lem:ii-g1-2-3]] (d) and
[[lem:ii-g1-2-6]] contain what the proof of [[prop:ii-g1-2-8]] needs of them. [Hin26c, Lemma 13.4] is used only in the
form of [[lem:ii-g1-2-4]], for the weight at σ = 0. With the weight at σ = ∞ as well, which [Hin26c] asks for after its
Corollary 13.5, the identification Ḣ^s([0, ∞)) ≅ σ^(s−1/2) H^s_b([0, ∞), |dσ/σ|) of [Hin26c, Lemma 13.4] fails. For s
= 1 let u := (1 − χ_0) σ^(2/5) with χ_0 ∈ C^∞_c([0, 2)) equal to 1 on [0, 1]. Then σ⁻¹u, ∂_σ u and σ⁻¹ σ∂_σ u lie in
L²(dσ), so u ∈ σ H^1_b([0, ∞), |dσ|) = σ^(1/2) H^1_b([0, ∞), |dσ/σ|); but u ∉ L²(dσ), so u ∉ Ḣ¹. The same u lies in
H^(1,((0,0),1/2))_b([0, ∞)) and not in H̄¹((0, ∞)), so [Hin26c, Corollary 13.5] fails as printed as well, and the
inverse transform of the same example, extended by 0, shows that [Hin26c, Lemma 13.6] fails at σ = ∞. The proof of
[Hin26c, Lemma 13.2] draws on [Tay11a, Chapter 4, Proposition 5.3] and that of [Hin26c, Lemma 13.4] on complex
interpolation; [[sec:ii-g1-2-2]]–[[sec:ii-g1-2-4]] use neither.

### The Fourier transform on the resolved product spaces {#sec:ii-g1-3}

#### The spaces {#sec:ii-g1-3-1}

X := ℝ⁴, X̄ its radial compactification, ρ := ⟨x⟩⁻¹ and μ_X := |dx|/⟨x⟩⁴, a b-density. H^(k,γ)_b(X; ℋ) is the space of
u with ρ^(−γ) (⟨x⟩∂_x)^α u ∈ L²(μ_X) for |α| ≤ k; the fields ⟨x⟩∂_(x^i) span 𝒱_b(X̄) ([[sec:i-a-4-6]]).

M := [ℝ̄_(t_*) × X̄; ∂ℝ̄ × ∂X̄] ([Hin26c, (13.9)]), with the defining functions of its faces ℐ, ι and K ([Hin26c,
(13.10)])

    ρ_I := ⟨t_*⟩/(⟨t_*⟩ + ⟨x⟩),     ρ_ι := (⟨t_*⟩ + ⟨x⟩)/(⟨t_*⟩⟨x⟩),     ρ_K := ⟨x⟩/(⟨t_*⟩ + ⟨x⟩),
    ρ_I ρ_ι = ⟨x⟩⁻¹,     ρ_ι ρ_K = ⟨t_*⟩⁻¹,                                                       {#eq:ii-g1-3-1}

and the b-density μ_M := |dt_*/⟨t_*⟩| μ_X. For weights β = (β_I, β_ι, β_K) and w_β := ρ_I^(β_I) ρ_ι^(β_ι) ρ_K^(β_K),
H^(k,β)_b(M; ℋ) is the space of u with w_β⁻¹ (⟨t_*⟩∂_(t_*))^j (⟨x⟩∂_x)^α u ∈ L²(μ_M; ℋ) for j + |α| ≤ k. These fields
are b-vector fields on M and span 𝒱_b(M), the blow-up of a codimension-two corner being a b-blow-up, and the derivatives
of log ρ_I, log ρ_ι, log ρ_K along them are bounded with all their derivatives (for instance ⟨t_*⟩∂_(t_*) log(⟨t_*⟩ +
⟨x⟩) = t_*/(⟨t_*⟩ + ⟨x⟩)), so weights and derivatives may be taken in either order, with equivalent norms; this is
[Hin26c, (13.11)].

For c ∈ (0, 1], X^±_(sc-b) := [±[0, c]_σ × X̄; {0} × ∂X̄] ([Hin26c, (13.12)], with c = 1 there), with the defining
functions of the faces scf, tf, zf ([Hin26c, (13.13)])

    ρ_scf := ρ/(ρ + |σ|),     ρ_tf := |σ| + ρ,     ρ_zf := |σ|/(ρ + |σ|),     ρ_scf ρ_tf = ρ,     ρ_tf ρ_zf = |σ|,
                                                                                                  {#eq:ii-g1-3-2}

and the b-density |dσ/σ| μ_X. For γ = (γ_scf, γ_tf, γ_zf), H^(k,γ)_b(X^±_(sc-b); ℋ) is the space of u on ±(0, c] × X
with w_γ⁻¹ (σ∂_σ)^j (⟨x⟩∂_x)^α u ∈ L²(|dσ/σ| μ_X) for j + |α| ≤ k ([Hin26c, (13.14)]; the face at |σ| = c is an
extendible end, at which nothing is asked). Let r̂ := |σ|⟨x⟩, a defining function of zf near zf, and χ_zf := χ_1(r̂)
with χ_1 ∈ C^∞([0, ∞)) equal to 1 on [0, 1/8] and to 0 on [1/4, ∞); χ_zf and its derivatives along σ∂_σ, ⟨x⟩∂_x are
bounded (σ∂_σ r̂ = r̂, ⟨x⟩∂_x r̂ = r̂ x/⟨x⟩). For γ_zf ∈ (−1, ∞) ∖ ℕ₀ let ([Hin26c, (13.15)] with ζ = 0)

    H^(k,(γ_scf,γ_tf,((0,0),γ_zf)))_b(X^±_(sc-b))
        := {χ_zf Σ_(ℓ∈ℕ₀, ℓ<γ_zf) r̂^ℓ v_ℓ + ũ : v_ℓ ∈ H^(k,γ_tf)_b(X), ũ ∈ H^(k,γ)_b(X^±_(sc-b))},          {#eq:s10-zf}

normed by Σ ‖v_ℓ‖ + ‖ũ‖; the decomposition is unique ([[lem:ii-g1-3-1]] (c) below and the uniqueness after
[[def:ii-g1-2-7]]). As r̂^ℓ v_ℓ = (±σ)^ℓ ⟨x⟩^ℓ v_ℓ(x) on the side ±, we call c^±_ℓ := (±1)^ℓ ⟨x⟩^ℓ v^±_ℓ the
*σ-Taylor coefficients*. [Hin26c] writes ρ_zf^ℓ u_ℓ(x) with ρ_zf = r̂/(1 + r̂); Taylor expansion of (1 + r̂)^(−ℓ) at
r̂ = 0 turns one form into the other, the remainders lying in ũ's space.

At high frequencies ([Hin26c, (13.16)]): for c > 0, H^(k,β,γ)_(b+)(±[c, ∞) × X; ℋ) is the space of v with
|σ|^γ σ^j (σ∂_σ)^l v ∈ L²(±[c, ∞), |dσ/σ|; H^(k−j−l,β)_b(X; ℋ)) for j + l ≤ k; the powers of σ stand on the same footing
as the b-derivatives, and H^(k+p,β,γ)_(b+) ⊂ H^(k,β,γ+p)_(b+) for p ∈ ℕ₀.

**Lemma {#lem:ii-g1-3-1}** (Product structure; [Hin26c, Lemma 13.8].) For k ∈ ℕ₀ and β, γ ∈ ℝ, with equivalent norms,

(a) H^(k,(γ,β+γ,β))_b(M; ℋ) = ⋂_(j=0)^k H^(j,β)_b(ℝ; H^(k−j,γ)_b(X; ℋ));

(b) H^(k,(γ,β+γ,β))_b(X^±_(sc-b); ℋ) = ⋂_(j=0)^k H^(j,β)_b(±(0, c]; H^(k−j,γ)_b(X; ℋ)), where H^(j,β)_b(±(0, c]; ℋ)
is the space of v with |σ|^(−β) (σ∂_σ)^i v ∈ L²(|dσ/σ|; ℋ), i ≤ j;

(c) for u supported in {r̂ ≤ 1/2}, in the coordinates (r̂, x) ∈ (0, 1/2] × X, ‖u‖_(H^(k,γ)_b(X^±_(sc-b))) is
equivalent to the norm of ⋂_(j≤k) H^(j,γ_zf)_b((0, 1/2]_(r̂); H^(k−j,γ_tf)_b(X)), the order γ_scf playing no role.

*Proof.* (a) By [[eq:ii-g1-3-1]], ρ_I^γ ρ_ι^(β+γ) ρ_K^β = ⟨t_*⟩^(−β) ⟨x⟩^(−γ), a product. The norm on the left is
equivalent to Σ_(j+|α|≤k) ‖⟨t_*⟩^β ⟨x⟩^γ (⟨t_*⟩∂_(t_*))^j (⟨x⟩∂_x)^α u‖_(L²(μ_M)), the two families of fields acting on
different variables, and by Fubini this is the norm on the right (with ⟨t⟩^β L²(dt/⟨t⟩) = ⟨t⟩^(β−1/2) L²(dt) and the
equivalence after [[def:ii-g1-2-1]]). (b) Likewise, with ρ_scf^γ ρ_tf^(β+γ) ρ_zf^β = ρ^γ |σ|^β by [[eq:ii-g1-3-2]].
(c) On {r̂ ≤ 1/2}, ρ_scf = (1 + r̂)⁻¹ ∈ [2/3, 1], ρ_tf = ρ(1 + r̂) and ρ_zf = r̂/(1 + r̂); at fixed x, σ∂_σ = r̂∂_(r̂)
and |dσ/σ| = |dr̂/r̂|; and ⟨x⟩∂_x at fixed σ is ⟨x⟩∂_x at fixed r̂ plus (x/⟨x⟩) r̂∂_(r̂). ∎

#### A b-ordinary differential equation {#sec:ii-g1-3-2}

**Lemma {#lem:ii-g1-3-2}** (A b-ordinary differential equation.) Let ℋ be a Hilbert space, d, c ∈ ℝ, c ≠ d, and let W ∈
L²_loc((0, 1); ℋ) satisfy (s∂_s − d)W = h on (0, 1) with h ∈ s^c L²((0, 1), |ds/s|; ℋ). Let χ ∈ C^∞([0, 1)) equal 1 on
[0, 1/4] and 0 on [1/2, 1). Write ‖·‖ for the norm of L²((0, 1), |ds/s|; ℋ) and ‖·‖′ for that over (1/4, 1/2).

(a) If c > d, then L := lim_(s→0) s^(−d) W(s) exists in ℋ, |L| ≤ C(‖W‖′ + ‖s^(−c) h‖), and W_1 := χ(W − s^d L)
satisfies ‖s^(−c) W_1‖ ≤ C(‖W‖′ + ‖s^(−c) h‖).

(b) If c < d, then W_1 := χW satisfies ‖s^(−c) W_1‖ ≤ C(‖W‖′ + ‖s^(−c) h‖).

(c) If moreover (s∂_s)^i h ∈ s^c L² for i ≤ k, then ‖s^(−c) (s∂_s)^i W_1‖ ≤ C Σ_(i′≤i) (‖(s∂_s)^(i′) W‖′ +
‖s^(−c) (s∂_s)^(i′) h‖) in both cases.

*Proof.* In τ := log s ∈ (−∞, 0), |ds/s| = dτ, and s∂_s(s^(−d) W) = s^(−d) h says ∂_τ(e^(−dτ) W) = e^(−dτ) h in
distributions, so e^(−dτ) W is absolutely continuous. (a) e^(−dτ) h = e^((c−d)τ) e^(−cτ) h is integrable on (−∞, τ_0)
by Cauchy–Schwarz, as c > d, so L exists and e^(−dτ) W(τ) = L + ∫_(−∞)^τ e^(−dτ′) h(τ′) dτ′. Averaging this over τ ∈
(log(1/4), log(1/2)) bounds |L|. And e^(−cτ)(W − e^(dτ) L) = ∫_(−∞)^τ e^(−(c−d)(τ−τ′)) e^(−cτ′) h(τ′) dτ′, a
convolution with e^(−(c−d)τ) 1_(τ>0), whose L¹ norm is (c − d)⁻¹; Young's inequality bounds it in L²(dτ), and
multiplying by χ costs nothing. (b) (s∂_s − d)(χW) = χh + (s∂_s χ)W =: h̃, with ‖s^(−c) h̃‖ ≤ ‖s^(−c) h‖ + C‖W‖′. χW
vanishes near τ = log(1/2), so e^(−dτ) χW(τ) = −∫_τ^(log(1/2)) e^(−dτ′) h̃(τ′) dτ′, and e^(−cτ) χW is the convolution
of e^(−cτ′) h̃ with −e^((d−c)τ) 1_(τ<0), of L¹ norm (d − c)⁻¹. (c) W_1 satisfies (s∂_s − d)W_1 = χh + (s∂_s χ)(W −
s^d L) in case (a) (as (s∂_s − d)s^d = 0), resp. h̃ in case (b), so s∂_s W_1 = dW_1 + (…), and induction on i; the
derivatives of W on (1/4, 1/2) enter through the terms with s∂_s χ. ∎

#### The Fourier transform of b-Sobolev functions {#sec:ii-g1-3-3}

**Proposition {#prop:ii-g1-3-3}** (The Fourier transform of b-Sobolev functions; [Hin26c, Proposition 13.9].) Let β =
(β_I, β_ι, β_K) and u ∈ H^(k+ℓ,β)_b(M; ℋ), with ℓ as below.

(1) (*Low energies.*) Let β_K ∈ (0, ∞) ∖ ℕ, ε ∈ (0, 1) and β_I ≥ β_ι − min(β_K, 1 − ε), and ℓ = 1. Then

    (ℱu)|_(σ∈±(0,1]) ∈ H^(k,(min(β_I,β_ι)−ε, β_ι−1, ((0,0),β_K−1)))_b(X^±_(sc-b); ℋ),

with norm ≤ C ‖u‖, and the σ-Taylor coefficients c^±_ℓ, ℓ < β_K − 1, of the two signs agree.

(2) (*High energies.*) Let ℓ := ⌈(1/2 − min(β_K, β_ι − β_I))_+⌉. Then (ℱu)|_(σ∈±[1/2,∞)) ∈ H^(k,β_I,0)_(b+)(±[1/2,
∞) × X; ℋ), with norm ≤ C ‖u‖.

Here ℱ acts in t_*; by [[lem:ii-g1-3-1]] (a) and [[lem:ii-g1-2-2]], u is a tempered distribution in t_* with values in
H^(k,γ)_b(X) for suitable γ. In (2), ⌈·⌉ makes ℓ an integer, as integer b-regularity requires; [Hin26c, Proposition
13.9 (2)] takes ℓ = (1/2 − min(β_K, β_ι − β_I))_+.

*Proof.* Lowering a weight is a bounded inclusion, as ρ_I, ρ_K ≤ 1 and ρ_ι ≤ 2; and two memberships with the same
tf-weight combine: if v lies in H^(k,(a,b,c))_b and in H^(k,(a′,b,c′))_b on X^±_(sc-b), then v ∈ H^(k,(a,b,c′))_b, by
the partition 1 = χ_1(2r̂) + (1 − χ_1(2r̂)), whose first term is supported away from scf and the second away from zf
(and likewise on M, with a partition into neighbourhoods of ℐ and of K). This is used twice below and in
[[prop:ii-g1-3-5]].

(1), *the case β_K ∈ (0, 1).* For η ≥ 0 with β_K − η > 0 and β_I ≥ β_ι − β_K + η, u ∈
H^(k+1,(β_ι−β_K+η,β_ι,β_K−η))_b(M), so by [[lem:ii-g1-3-1]] (a) u ∈ ⋂_(j≤k) H^(j+1,β_K−η)_b(ℝ; ℋ_j) with ℋ_j :=
H^(k−j,β_ι−β_K+η)_b(X). As β_K − η ∈ (0, 1), ℓ_−(β_K − η) ≤ 1, and [[prop:ii-g1-2-8]] (1) (with ℋ_j-values; no Taylor
terms, as β_K − η − 1 < 0) gives (σ∂_σ)^i ℱu ∈ |σ|^(β_K−η−1) L²(|dσ/σ|; ℋ_j) on each side, i ≤ j. Restricted to
|σ| ≤ 1 this is, by [[lem:ii-g1-3-1]] (b),

    ℱu ∈ H^(k,(β_ι−β_K+η, β_ι−1, β_K−η−1))_b(X^±_(sc-b)).

With η = 0 the zf-weight is β_K − 1; with η := max(0, min(β_K, β_I − β_ι + β_K) − ε) the scf-weight is ≥ min(β_I,
β_ι) − ε (if the maximum is 0 then min(β_K, β_I − β_ι + β_K) ≤ ε, and β_ι − β_K ≥ min(β_I, β_ι) − ε). Combining the two
gives the claim; the matching statement is empty.

(1), *the case β_K ∈ (b, b + 1), b ∈ ℕ.* (i) Applying the first case to u ∈ H^(k+1,(β_I,β_ι,1−ε))_b(M) (its hypothesis
β_I ≥ β_ι − (1 − ε) is ours, as min(β_K, 1 − ε) = 1 − ε) gives V := ℱu ∈ H^(k,(min(β_I,β_ι)−ε,β_ι−1,−ε))_b(X^±_(sc-b)).
(ii) t_*^b u ∈ H^(k+1,(β_I,β_ι−b,β_K−b))_b(M), as t_*^b = (t_*/⟨t_*⟩)^b (ρ_ι ρ_K)^(−b), and β_K − b ∈ (0, 1) with β_I ≥
β_ι − 1 + ε ≥ (β_ι − b) − min(β_K − b, 1 − ε); so by the first case ℱ(t_*^b u) ∈ H^(k,(a,β_ι−b−1,β_K−b−1))_b for some
a. As ∂_σ ℱu = iℱ(t_* u) and |σ|^b = ρ_tf^b ρ_zf^b,

    h := σ^b ∂_σ^b V = (iσ)^b ℱ(t_*^b u) ∈ H^(k,(a,β_ι−1,β_K−1))_b(X^±_(sc-b)).                     {#eq:ii-g1-3-3}

(iii) On Z := {r̂ < 1/2} use the coordinates (r̂, x) of [[lem:ii-g1-3-1]] (c), in which σ = ±r̂/⟨x⟩, so σ^b ∂_σ^b =
r̂^b ∂_(r̂)^b at fixed x. By (i), [[eq:ii-g1-3-3]] and [[lem:ii-g1-3-1]] (c), with ℋ_j := H^(k−j,β_ι−1)_b(X), V ∈
⋂_j H^(j,−ε)_b((0, 1/2)_(r̂); ℋ_j) and h ∈ ⋂_j H^(j,β_K−1)_b((0, 1/2); ℋ_j). As β_K − 1 − b > −1, r̂^(−b) h ∈
r̂^(β_K−1−b) L²(|dr̂/r̂|; ℋ_0) is integrable near r̂ = 0. Let

    R(r̂) := ((b − 1)!)⁻¹ ∫_0^(r̂) τ^(−b) h(τ) (r̂ − τ)^(b−1) dτ = ((b − 1)!)⁻¹ ∫_0^1 s^(−b) h(sr̂) (1 − s)^(b−1) ds,

the b-fold iterated integral of r̂^(−b) h from 0, so that ∂^b_(r̂) R = r̂^(−b) h = ∂^b_(r̂) V on (0, 1/2). Dilations r̂ ↦
sr̂ commute with r̂∂_(r̂) and with ⟨x⟩∂_x at fixed r̂, and preserve |dr̂/r̂|, so by Minkowski's inequality

    ‖r̂^(1−β_K) (r̂∂_(r̂))^j R‖_(L²(ℋ_j))
        ≤ ((b − 1)!)⁻¹ ∫_0^1 s^(β_K−1−b) (1 − s)^(b−1) ds · ‖r̂^(1−β_K) (r̂∂_(r̂))^j h‖_(L²(ℋ_j)),

finite as β_K − 1 − b > −1. V − R is an ℋ_0-valued distribution on (0, 1/2) with ∂^b_(r̂)(V − R) = 0, hence a
polynomial Σ_(d<b) r̂^d v_d; each v_d is a fixed linear combination of the averages ∫ (V − R) r̂^(d′) φ(r̂) dr̂, d′ < b,
with φ ∈ C^∞_c((1/4, 1/2)) (the monomials being linearly independent there), so v_d ∈ ℋ_0 = H^(k,β_ι−1)_b(X) with norm
≤ C(‖V‖ + ‖h‖). So on Z, V = Σ_(d<b) r̂^d v_d + R with R ∈ r̂^(β_K−1) and the full b-regularity k, and the d < b are
exactly the ℓ < β_K − 1. With χ_zf (supported in {r̂ ≤ 1/4}), V = χ_zf Σ_d r̂^d v_d + Ṽ, where Ṽ = χ_zf R + (1 −
χ_zf)V; the first term has tf-weight β_ι − 1 and zf-weight β_K − 1 and is supported away from scf, and the second is
supported away from zf, where (i) gives the scf-weight min(β_I, β_ι) − ε and the tf-weight β_ι − 1. This proves the
first claim.

*Matching.* On {|x| < R}, ρ_K ∼ ⟨t_*⟩⁻¹ and the weights at ℐ, ι are irrelevant, so u ∈ H^(k+1,β_K)_b(ℝ; L²({|x| <
R})), and ℱu ∈ H^(β_K−1/2)(ℝ; L²({|x| < R})) by [[lem:ii-g1-2-2]]. As β_K − 1/2 > 1/2, [[lem:ii-g1-2-4]] makes ℱu of
class C^ℓ in σ across σ = 0 for ℓ < β_K − 1, with ℱu − P_(ℱu) ∈ |σ|^(β_K−1/2) L² near 0. On the other hand, on {|x| <
R} the expansion gives ℱu = Σ_(ℓ<β_K−1) c^±_ℓ σ^ℓ + O_(L²)(|σ|^(β_K−1/2)) on each side, as r̂^(β_K−1) L²(|dr̂/r̂|) =
|σ|^(β_K−1/2) L²(dσ) locally in x. A polynomial of degree < β_K − 1 in |σ|^(β_K−1/2) L² near 0 vanishes, so c^±_ℓ =
∂^ℓ_σ ℱu(0)/ℓ! on {|x| < R} for both signs; R is arbitrary.

(2) Let β′_K := min(β_K, β_ι − β_I). Then u ∈ H^(k+ℓ,(β_I,β_I+β′_K,β′_K))_b(M) = ⋂_j H^(j,β′_K)_b(ℝ;
H^(k+ℓ−j,β_I)_b(X)), so by [[lem:ii-g1-2-2]] F_(pq) := σ^p (σ∂_σ)^q ℱu ∈ H^(β′_K−1/2)(ℝ; H^(k+ℓ−p−q,β_I)_b(X)) for p
+ q ≤ k + ℓ. Let ψ ∈ C^∞(ℝ) vanish on [−1/4, 1/4] and equal 1 outside (−1/2, 1/2). For p + q ≤ k and i ≤ ℓ,
∂^i_σ(ψF_(pq)) is a combination of ψ_(i′)(σ) σ^(−i′) (σ∂_σ)^(i′) F_(pq), i′ ≤ i, with ψ_(i′) smooth, supported in |σ| ≥
1/4 and bounded with all derivatives, multiplication by which is bounded on H^(β′_K−1/2) (by Peetre's inequality, as
in (K1) (i) of [[sec:i-c-2-1]]); σ^(−i′) is such a multiplier on |σ| ≥ 1/4. So ψF_(pq) ∈ H^(β′_K−1/2+ℓ) ⊂ L², as ℓ ≥
1/2 − β′_K, with values in H^(k−p−q,β_I)_b(X) (the b-derivatives (σ∂_σ)^(i′) used, i′ ≤ ℓ, cost ℓ of the
X-regularity). On ±[1/2, ∞), L²(dσ) ⊂ L²(|dσ/σ|), which is the claim. ∎

**Lemma {#lem:ii-g1-3-4}** (Stationary functions; [Hin26c, Lemma 13.10].) Let γ ∈ ℝ and v_0 ∈ H^(k,γ)_b(X; ℋ). Then
v(t_*, x) := v_0(x) lies in H^(k,(γ−ε,γ,−ε))_b(M; ℋ) for every ε > 0.

*Proof.* ⟨t_*⟩∂_(t_*) v = 0, and the ⟨x⟩∂_x-derivatives fall on v_0, so it suffices to show ‖w_β⁻¹ f‖_(L²(μ_M)) ≤
C_ε ‖ρ^(−γ) f‖_(L²(μ_X)) for t_*-independent f, β = (γ − ε, γ, −ε). By [[eq:ii-g1-3-1]], w_β = ⟨x⟩^(−γ) (ρ_I
ρ_K)^(−ε), and ρ_I ρ_K = T⟨x⟩/(T + ⟨x⟩)² with T := ⟨t_*⟩. As

    ∫ (T⟨x⟩/(T + ⟨x⟩)²)^(2ε) dt_*/⟨t_*⟩ ≤ 2√3 + (4/√3) ∫_0^∞ (ς/(1 + ς)²)^(2ε) dς/ς =: C_ε < ∞

(the integrand is at most 1, and {T ≤ 2} has t_*-length 2√3; on {T ≥ 2}, T dT = |t_*| dt_* gives dt_*/⟨t_*⟩ =
dT/(T² − 1)^(1/2) ≤ (2/√3) dT/T on each half-line, and T = ⟨x⟩ς), uniformly in x, the claim follows by Fubini. ∎

**Proposition {#prop:ii-g1-3-5}** (The inverse Fourier transform; [Hin26c, Proposition 13.11].) Let β_K ∈ (0, ∞) ∖ ℕ,
β_ι, β_scf, β_I, δ ∈ ℝ, ε ∈ (0, 1), and χ ∈ C^∞_c((−1, 1)) equal to 1 near [−1/2, 1/2].

(1) (*Low energies.*) Let ℓ := ⌈(max(β_ι − β_scf, β_K) + ε − 1/2)_+⌉. If v_± ∈
H^(k+ℓ,(β_scf,β_ι−1,((0,0),β_K−1)))_b(X^±_(sc-b); ℋ) (c = 1) have the same σ-Taylor coefficients, then for v :=
χ(σ) Σ_± 1_(±σ>0) v_±,

    ℱ⁻¹v ∈ H^(k,(min(β_scf,β_ι)−ε, β_ι, β_K))_b(M; ℋ),

with norm ≤ C Σ_± ‖v_±‖.

(2) (*High energies.*) Let β′ := max(β_K, β_ι − β_I) and ℓ := ⌈(3/2 − δ)_+⌉ + ⌈(β′ − 1/2)_+⌉. If v_± ∈
H^(k+ℓ,β_I,δ−1)_(b+)(±[1/2, ∞) × X; ℋ), then ℱ⁻¹((1 − χ)v_±) ∈ H^(k,(β_I,β_ι,β_K))_b(M; ℋ), with norm ≤ C ‖v_±‖.

*Proof.* (1) *The expansion.* For each ℓ < β_K − 1 (here ℓ indexes the expansion, not the loss), by the matching, the
terms of index ℓ of the two signs add up to χ(σ) χ_1(|σ|⟨x⟩) σ^ℓ c_ℓ(x) = φ_ℓ(σ⟨x⟩) v_ℓ(x), where c_ℓ = ⟨x⟩^ℓ v_ℓ is
the common coefficient, v_ℓ ∈ H^(k,β_ι−1)_b(X), and φ_ℓ(s) := χ_1(|s|) s^ℓ ∈ C^∞_c((−1/4, 1/4)); χ(σ) = 1 where
χ_1(|σ|⟨x⟩) ≠ 0, as |σ| ≤ 1/4 there. Substituting s = σ⟨x⟩,

    ℱ⁻¹(φ_ℓ(σ⟨x⟩))(t_*) = ρ φ̌_ℓ(ρ t_*),        φ̌_ℓ(τ) := (2π)⁻¹ ∫ e^(−isτ) φ_ℓ(s) ds ∈ 𝒮(ℝ).

⟨ρ t_*⟩ is comparable to ρ_K⁻¹ = (⟨t_*⟩ + ⟨x⟩)/⟨x⟩, and ⟨t_*⟩∂_(t_*), ⟨x⟩∂_x map φ̌_ℓ(ρ t_*) to (⟨t_*⟩/⟨x⟩)
φ̌′_ℓ(ρ t_*) and −(x/⟨x⟩)(ρ t_*) φ̌′_ℓ(ρ t_*), with ⟨t_*⟩/⟨x⟩ ≤ C⟨ρ t_*⟩; so ρ_K^(−p) φ̌_ℓ(ρ t_*) is bounded with all its
b-derivatives, for every p ≥ 0. With ρ = ρ_I ρ_ι and [[lem:ii-g1-3-4]] for v_ℓ, the inverse transform of the expansion
lies in H^(k,(β_ι−ε,β_ι,p))_b(M) for every p.

*The remainder.* Let ṽ_± ∈ H^(k+ℓ,(γ,β_ι−1,β_K−1))_b(X^±_(sc-b)), γ := β_scf, and split ṽ_± = w_1 + w_2 with w_2 :=
χ_1(r̂/4) ṽ_±, supported in {r̂ ≤ 1}, away from scf, and w_1 supported in {r̂ ≥ 1/2}, away from zf. We treat the side
+; the function χw_i on (0, 1), extended by 0 to σ < 0, has the pair (0, χw_i) with zero Taylor polynomial.

For w_1: for η ≥ 0, w_1 ∈ H^(k+ℓ,(γ−η,β_ι−1,β_ι−1−γ+η))_b (lowering scf; the zf-weight is free away from zf), so by
[[lem:ii-g1-3-1]] (b) χw_1 ∈ ⋂_j H^(j+ℓ,a)_b((0, 1); H^(k−j,γ−η)_b(X)), a := β_ι − 1 − γ + η; the powers σ^j, |σ| ≤ 1,
are harmless, so (0, χw_1) ∈ X^(j+ℓ,a) with values in H^(k−j,γ−η)_b(X). If β := a + 1 = β_ι − γ + η ∈ (0, ∞) ∖ ℕ and ℓ ≥
ℓ_+(β), [[prop:ii-g1-2-8]] (2) and [[lem:ii-g1-3-1]] (a) give

    ℱ⁻¹(χw_1) ∈ ⋂_j H^(j,β_ι−γ+η)_b(ℝ; H^(k−j,γ−η)_b(X)) = H^(k,(γ−η, β_ι, β_ι−γ+η))_b(M).

Take η_0 := max(0, γ − β_ι) + ε′ and η_1 := max(0, β_K − β_ι + γ) + ε′, ε′ ∈ (0, ε] chosen so that neither β_ι − γ +
η_i is an integer. With η_0, β > 0 and the ℐ-weight is min(γ, β_ι) − ε′; with η_1 ≥ η_0 the K-weight is ≥ β_K. The
larger loss is ℓ_+(β_ι − γ + η_1) = ⌈(max(β_ι − γ, β_K) + ε′ − 1/2)_+⌉ ≤ ℓ ([Hin26c, (13.22)]). Combining the two
memberships (same ι-weight) gives ℱ⁻¹(χw_1) ∈ H^(k,(min(γ,β_ι)−ε,β_ι,β_K))_b(M). ([Hin26c] applies [Hin26c, (13.22)]
with η = max(η_0, η_1) and states the ℐ-weight obtained with η_0. One η gives the ℐ-weight γ − η and the K-weight β_ι −
γ + η, and with η_1 the first may be smaller than min(γ, β_ι) − ε; so the two memberships must be combined.)

For w_2: for η ≥ 0 with β_K − η ∈ (0, ∞) ∖ ℕ, w_2 ∈ H^(k+ℓ,(β_ι−β_K+η,β_ι−1,β_K−1−η))_b (the scf-weight is free away
from scf), so as before ℱ⁻¹(χw_2) ∈ H^(k,(β_ι−β_K+η,β_ι,β_K−η))_b(M), with loss ℓ_+(β_K − η) ≤ ⌈(β_K − 1/2)_+⌉ ≤ ℓ.
With η = 0 the K-weight is β_K; with η := β_K − ε the ℐ-weight is β_ι − ε. Combining gives
H^(k,(β_ι−ε,β_ι,β_K))_b(M). The three pieces give (1).

(2) w := (1 − χ)v_±, extended by 0, vanishes on (−1/2, 1/2). By [[lem:ii-g1-3-1]] (a),
H^(k,(β_I,β_I+β′,β′))_b(M) ⊂ H^(k,(β_I,β_ι,β_K))_b(M), and by [[lem:ii-g1-2-2]] it suffices to show W :=
σ^p (σ∂_σ)^q w ∈ H^(β′−1/2)(ℝ; H^(k−j,β_I)_b(X)) for p + q ≤ j ≤ k. Let m := ⌈(β′ − 1/2)_+⌉ and m′ := ⌈(3/2 − δ)_+⌉,
so ℓ = m′ + m. The hypothesis says σ^a (σ∂_σ)^b v_± ∈ |σ|^(1−δ) L²(|dσ/σ|) = |σ|^(3/2−δ) L²(dσ), with values in
H^(k+ℓ−a−b,β_I)_b(X), for a + b ≤ k + ℓ. For i ≤ m, ∂^i_σ W = σ^(−i) Σ_(i′≤i) a_(ii′) (σ∂_σ)^(i′) W on |σ| ≥ 1/2, and
(σ∂_σ)^(i′) W is a combination of σ^p (σ∂_σ)^(q+i″) w, i″ ≤ i′; writing σ^p = σ^(−m′) σ^(p+m′), each lies in
|σ|^(3/2−δ−m′) L² ⊂ L²(dσ) on |σ| ≥ 1/2, with values in H^(k+ℓ−p−m′−q−i″,β_I)_b(X) ⊂ H^(k−j,β_I)_b(X), as p + m′ + q +
i″ ≤ j + m′ + m = j + ℓ. The derivatives of 1 − χ are smooth and compactly supported in 1/2 ≤ |σ| ≤ 1. So W ∈ H^m ⊂
H^(β′−1/2) (if β′ ≤ 1/2, m = 0 and W ∈ L² ⊂ H^(β′−1/2)). ∎

**Remark {#rem:ii-g1-3-6}** ([Hin26c, Remark 13.12].) The losses of b-regularity in [[prop:ii-g1-3-3]] and
[[prop:ii-g1-3-5]] depend only on the weights, not on k. [[prop:ii-g1-3-5]] (2) is proved directly from
[[lem:ii-g1-2-2]], with the loss ⌈(3/2 − δ)_+⌉ + ⌈(β′ − 1/2)_+⌉, which is not sharp. It differs from the loss
⌈2ℓ′ + δ⌉ of [Hin26c, Proposition 13.11 (2)], whose ℓ′ is printed with an unbalanced bracket. The first step there
trades ℓ′ orders of b+-regularity for decay, from the space with weight δ − 1, which means σ^j (σ∂_σ)^l v ∈
|σ|^(1−δ) L²(|dσ/σ|), into the space of [Hin26c, (13.8)] with weight δ + ℓ′ − 1, which means |σ|^(δ+ℓ′−1)
L²(|dσ/σ|). The trade gives |σ|^(1−δ−ℓ′) L² near ∞, which is contained in |σ|^(δ+ℓ′−1) L² there only if ℓ′ ≥ 1 − δ.
For δ = −1/2, β_ι − β_I ≤ 1/2 and β_K ≤ 1/2 the printed ℓ′ is 1, less than 1 − δ = 3/2, and the step fails. The final
loss of [Hin26c] is not shown to be insufficient; only its intermediate step is.

**Remark {#rem:ii-g1-3-7}** (The exterior X̄.) [[sec:ii-g1-4]] and [[sec:ii-g1-5]] use X̄ := {|x| ≥ r_0} ∪ ∂X̄ of
[[sec:i-a-1-1]], with spaces extendible at {|x| = r_0}. Every statement of this section holds with X replaced by X̄ and
the b-spaces in x by their extendible versions (quotient norms of restrictions): apply it to ℰu and restrict, where ℰ is
Seeley's extension in |x| across |x| = r_0 (the operator with infinitely many reflections written out in the proof of
[[lem:ii-e-1-3]] (b), as in [[lem:ii-f1-2-5]]). ℰ acts in x alone, near |x| = r_0 where the weights are bounded above
and below; it commutes with t_*, with ℱ in t_* and with σ∂_σ, and is bounded on the extendible b-spaces of every order
at once, so the norms of ⋂_j H^(j,β)_b(ℝ; H̄^(k−j,γ)_b(X̄)) and of the restrictions of H^(k,(γ,β+γ,β))_b(M) are
equivalent, as in [[lem:ii-g1-3-1]].

### Resolvent bounds in dimension 4 + 1 {#sec:ii-g1-4}

#### Fixed frequencies {#sec:ii-g1-4-1}

On X̄, μ = |dx| and μ_b = |dx|/⟨x⟩⁴. The spaces H̄^((s;k),𝗋) are those of [[sec:i-a-4-6]] (scattering regularity s,
decay order 𝗋, k b-derivatives, for μ). For a constant decay order and s = 0, H̄^((0;k),β−2) = H̄^(k,β)_b(X̄, μ_b), the
b-Sobolev space with weight β for μ_b, as ⟨x⟩^(−β+2) L²(μ) = ⟨x⟩^(−β) L²(μ_b); and the space H̄^(s,a)_b of
[[def:i-c-2-8]] is H̄^(s,a+2)_b(X̄, μ_b). R_out is the zero section of the boundary face over ∂X ([[eq:i-a-4-6]]).

**Lemma {#lem:ii-g1-4-1}** (Scattering spaces and b-spaces; [Hin26c, Lemma 13.13] in dimension 4 + 1.) Let s ∈ ℝ be
constant and 𝗋 a decay order ([[sec:i-a-1-4]]) equal to the constant 𝗋_out on a neighbourhood of R_out. Let α ∈ ℝ,
k ∈ ℕ₀, ε > 0, and

    ℓ := max(⌈sup 𝗋 − 𝗋_out⌉, ⌈(s − 1)_+⌉),        ℓ̃ := max(⌈𝗋_out − inf 𝗋⌉, ⌈(−s)_+⌉).

Then there are continuous inclusions

    H̄^(k+ℓ, 𝗋_out+α+3+ε)_b(X̄, μ_b) ↪ H̄^((s−1;k), 𝗋+α+1),                                           {#eq:ii-g1-4-1a}

    H̄^((s;k), 𝗋+α) ↪ H̄^(k−ℓ̃, 𝗋_out+α+2−ε)_b(X̄, μ_b)        (k ≥ ℓ̃),                               {#eq:ii-g1-4-1b}

and likewise on ℝ⁴ without the artificial boundary.

[Hin26c, (13.23a)–(13.23b)] have 5/2 and 3/2 in place of 3 and 2, and allow a variable regularity order and a decay
order that is not constant near R_out (with its supremum, resp. infimum, there); the orders of [[ch:s01]] have constant
regularity order ([[rem:i-a-1-1]]) and decay orders constant near R_out ((O2) of [[sec:i-a-1-4]]).

*Proof.* It suffices to prove the inequalities for distributions on ℝ⁴: for the extendible spaces, apply them to an
extension of almost minimal norm and restrict. We use the scattering calculus with variable orders of [[sec:i-a-2]]
(boundedness Ψ^(m,l) : H^(s,𝗋) → H^(s−m,𝗋−l), microlocality, composition) and [[lem:i-a-4-10]]. Let q_0 be a symbol
of order (0, 0), equal to 1 near R_out and supported in a neighbourhood U of it, at finite frequencies, on which 𝗋 =
𝗋_out; Q_0 := Op(q_0) and Q_1 := I − Q_0, so WF′(Q_1) ∩ R_out = ∅. For a multi-index γ and V^γ := (⟨x⟩D_x)^γ, as
⟨x⟩D_(x_j) ∈ Ψ^(1,1) and commutators with elements of Ψ^(0,0) lie in Ψ^(0,0), V^γ Q_0 = Σ_(γ′≤γ) Q_(γγ′) V^(γ′) with
Q_(γγ′) ∈ Ψ^(0,0) microsupported in WF′(Q_0).

[[eq:ii-g1-4-1b]]: put k′ := k − ℓ̃. On WF′(Q_(γγ′)) ⊂ U the frequencies are finite and 𝗋 + α ≥ 𝗋_out + α − ε, so
Q_(γγ′) maps H^(s,𝗋+α) to H^(0,𝗋_out+α−ε) (its symbol lies in the class of order (−L, 𝗋 − 𝗋_out + ε) for every L),
and ‖Q_0 u‖_((0;k′),𝗋_out+α−ε) ≤ C ‖u‖_((s;k′),𝗋+α). For Q_1, [[lem:i-a-4-10]] and its converse give

    ‖Q_1 u‖_((0;k′),𝗋_out+α−ε) ≤ C (‖Q_1 u‖_(k′,𝗋_out+α−ε+k′) + ‖u‖_(−L,−L))
                                 ≤ C (‖Q_1 u‖_(s+k,𝗋+α+k) + ‖u‖_(−L,−L)) ≤ C ‖u‖_((s;k),𝗋+α),

the middle inequality as k′ ≤ s + k and 𝗋_out − ε + k′ ≤ inf 𝗋 + k (both by the choice of ℓ̃), the last as Q_1 is
bounded on H^((s;k),𝗋+α) (commute V^γ through it as above). With H̄^((0;k′),𝗋_out+α−ε) =
H̄^(k′,𝗋_out+α+2−ε)_b(μ_b) this is [[eq:ii-g1-4-1b]].

[[eq:ii-g1-4-1a]]: for f in the space on the left, f ∈ H^((0;k+ℓ),𝗋_out+α+1+ε). On WF′(Q_(γγ′)), 𝗋 + α + 1 = 𝗋_out
+ α + 1, so ‖Q_0 f‖_((s−1;k),𝗋+α+1) ≤ C ‖f‖_((0;k),𝗋_out+α+1+ε). And

    ‖Q_1 f‖_((s−1;k),𝗋+α+1) ≤ C (‖Q_1 f‖_(s−1+k,𝗋+α+1+k) + ‖f‖_(−L,−L))
                              ≤ C (‖Q_1 f‖_(k+ℓ,𝗋_out+α+1+ε+k+ℓ) + ‖f‖_(−L,−L)) ≤ C ‖f‖_((0;k+ℓ),𝗋_out+α+1+ε),

as s − 1 ≤ ℓ and sup 𝗋 ≤ 𝗋_out + ℓ. ∎

**Corollary {#cor:ii-g1-4-2}** (Resolvent bounds at bounded nonzero frequencies; [Hin26c, Corollary 13.14] in dimension
4 + 1.) Assume (H1)–(H4) of [[sec:i-a-1-3]], and let β_scf < 3/2 + S̄ and ε ∈ (0, 1). There is ℓ ∈ ℕ₀, depending only
on P̂ and β_scf, such that:

(1) if σ_0 ≠ 0, Im σ_0 ≥ 0, and P̂(σ_0) : 𝒳_(σ_0) → 𝒴_(σ_0) is invertible ([[thm:i-a-7-2]]; this does not depend on
the admissible orders), then for j, k ∈ ℕ₀

    ∂^j_σ P̂(σ_0)⁻¹ : H̄^(k+j+ℓ, β_scf+1)_b(X̄, μ_b) → H̄^(k, β_scf−ε)_b(X̄, μ_b)   is bounded;

(2) if I ⊂ ℝ is a bounded open interval with 0 ∉ Ī and P̂(σ) is invertible for every σ ∈ Ī, then P̂⁻¹ : f̂ ↦ (σ ↦
P̂(σ)⁻¹ f̂(σ)) is bounded from H̄^(k+ℓ,β_scf+1)_b(I × X̄) to H̄^(k,β_scf−ε)_b(I × X̄), where ‖v‖²_(H̄^(k,β)_b(I×X̄)) :=
Σ_(k′≤k) ∫_I ‖∂^(k′)_σ v(σ)‖²_(H̄^(k−k′,β)_b(X̄,μ_b)) dσ.

[Hin26c, Corollary 13.14 (2)] asks only that P̂(σ) be invertible on the open interval I. The bound on I × X̄ needs
constants uniform in σ ∈ I, which the cited estimates give on a compact set of invertible σ; on a bounded open I with
P̂(σ) invertible on I but not at an endpoint, the norm of P̂(σ)⁻¹ may be unbounded on I.

*Proof.* *Orders.* Let 𝗋_out := β_scf − 2 − ε/2, which is < −1/2 + S̄, the threshold at R_out of [[eq:i-a-1-5]] with
weight α_+ = 0; 𝗋_in := max(𝗋_out, (1/2)(−1 + ϑ_in) + 1); and s := s_c a fixed constant > 1/2 + ϑ_ℋ, with ϑ_in, ϑ_ℋ
the thresholds of [[eq:i-a-1-5]]. If Re σ_0 ≠ 0, [[lem:i-a-7-1]] at σ_* := Re σ_0 gives an order pair (s, 𝗋)
admissible for every real part near σ_*, with 𝗋 = 𝗋_out + (𝗋_in − 𝗋_out) Θ χ_c taking values in [𝗋_out, 𝗋_in] and
equal to 𝗋_out near R_out (Θ = 0 near ξ = 0). If Re σ_0 = 0, then Im σ_0 > 0 and the constant order 𝗋 ≡ 𝗋_out is
allowed by [[thm:i-a-7-2]] (2). In both cases [[lem:ii-g1-4-1]] applies with

    ℓ_a := max(⌈((1/2)(−1 + ϑ_in) + 7/2 − β_scf)_+⌉, ⌈(s − 1)_+⌉),

which is at least ⌈𝗋_in − 𝗋_out⌉ for every ε ∈ (0, 1) ([[lem:ii-g1-4-1]] holds with any larger loss), so that ℓ does
not depend on ε, and ℓ̃ := ⌈(−s)_+⌉; put ℓ := ℓ_a + ℓ̃.

(1) By [[thm:i-a-7-2]] (6), [[eq:i-a-7-6]], with α_+ = 0 (at Re σ_0 = 0 the proof of [[eq:i-a-7-6]] uses only
[[thm:i-a-7-2]] (4) and the invertibility at the orders (s + ℓ, 𝗋), which hold with the constant order): ∂^j_σ
P̂(σ_0)⁻¹ : H̄^((s−1;k+ℓ̃+j),𝗋+1) → H̄^((s+j;k+ℓ̃),𝗋) ⊂ H̄^((s;k+ℓ̃),𝗋). Precompose with [[eq:ii-g1-4-1a]] at α = 0, ε/2
and order k + ℓ̃ + j, whose domain is H̄^(k+j+ℓ,β_scf+1)_b as 𝗋_out + 3 + ε/2 = β_scf + 1, and compose with
[[eq:ii-g1-4-1b]] at ε/2 and order k + ℓ̃, whose target is H̄^(k,β_scf−ε)_b.

(2) For σ_* ∈ Ī, the orders chosen at σ_* serve for all σ near σ_* ([[lem:i-a-7-1]], resp. [[thm:i-a-7-2]] (2)), and by
[[thm:i-a-7-2]] (6) the estimates [[eq:i-a-7-1]], [[eq:i-a-7-3]] hold there without their last terms uniformly, so
P̂(σ)⁻¹ is bounded uniformly near σ_*; as ∂_σ P̂⁻¹ = −P̂⁻¹(∂_σ P̂)P̂⁻¹, the bounds [[eq:i-a-7-6]] for ∂^j_σ P̂⁻¹ are
uniform near σ_* too. By compactness of Ī, finitely many such neighbourhoods cover it, and (1) holds with constants
uniform in σ ∈ Ī. For f̂ smooth in σ, ∂^(k′)_σ(P̂⁻¹ f̂) = Σ_(k″≤k′) c_(k′k″) (∂^(k″)_σ P̂⁻¹)(∂^(k′−k″)_σ f̂), with
binomial coefficients c_(k′k″), by the strong differentiability of [[thm:i-a-7-2]] (6), and (1) with k − k′ in place of
k and j = k″ bounds the k″-th term in H̄^(k−k′,β_scf−ε)_b by C ‖∂^(k′−k″)_σ f̂(σ)‖_(H̄^(k−k′+k″+ℓ,β_scf+1)_b), a term of
the norm of f̂ in H̄^(k+ℓ,β_scf+1)_b(I × X̄); such f̂ are dense. ∎

#### High frequencies {#sec:ii-g1-4-2}

The semiclassical spaces and the norms ‖·‖_((s;k),𝗋,𝖻;+) are those of [[eq:i-b-1-5]], with the quantisation Op_h of
[[sec:i-b-2]]. For constant orders (0, 𝗋′, 0), H^(0,𝗋′,0)_h = ⟨x⟩^(−𝗋′) L² for every h ([[sec:i-b-2-3]]), so

    ‖v‖_((0;k),𝗋′,0;+) = Σ_(j≤k) h^(−j) ‖v‖_(H̄^(k−j,𝗋′+2)_b(X̄,μ_b)),                              {#eq:ii-g1-4-2}

which at h = |σ|⁻¹ is the norm at fixed σ of the spaces H^(k,β,γ)_(b+) of [[sec:ii-g1-3-1]].

*Admissible orders.* For z_0 ∈ {1, −1} and constants 𝗋_out < −1/2 + S̄, 𝗋_in ≥ 𝗋_out with 𝗋_in > (1/2)(−1 + ϑ_in), the
order 𝗋 := 𝗋_out + (𝗋_in − 𝗋_out) Θ(ξ) χ_c(ξ² + |η|²) of [[lem:i-a-7-1]] at σ_* := z_0, read in the semiclassical
frequency ζ = (ξ, η) on the face over ∂X and extended off it independently of ρ, is admissible for z_0 with weight 0 in
the sense of [[sec:i-b-1-4]]. It is constant near R_(z_0,in) = {ξ = −2z_0, η = 0} and near R_out. By [[eq:i-a-4-5]],
𝖧_(z_0) ξ = 2|η|² on the whole face, 𝖧_(z_0) being, up to a positive factor, the field of [[eq:i-a-4-5]] there
([[lem:i-b-4-1]]); so on W := {χ_c = 1}°, a neighbourhood of Σ^∂_(z_0) in the face, 𝖧_(z_0) 𝗋 = 2(𝗋_in − 𝗋_out)
Θ′(ξ)|η|². On supp Θ′, ε_* ξ ∈ [−3/2, −1/2] (ε_* = z_0), and q = −2ξ there ([[lem:i-b-4-1]] (b)), so sgn q̂_(z_0) =
z_0 and 𝖧^♮ 𝗋 = z_0 𝖧_(z_0) 𝗋 ≤ 0, as z_0 Θ′ ≤ 0. The semiclassical order 𝖻 ≡ 0 is admissible (constant orders are).
Below, (s, 𝗋, 𝖻) are these orders, with s := s_c.

**Lemma {#lem:ii-g1-4-3}** (b-spaces and semiclassical spaces.) Let z_0 and (s, 𝗋, 𝖻) be as above, 𝖻 being any order
constant near R_out, and ε > 0. There are ℓ_1, ℓ_2, ν ∈ ℕ₀, depending only on the orders, such that for h ∈ (0, h_0] and
k ∈ ℕ₀

    ‖f‖_((s−1;k),𝗋+1,𝖻;+) ≤ C_k h^(−ν) ‖f‖_((0;k+ℓ_1),𝗋_out+1+ε,0;+),                                {#eq:ii-g1-4-3a}

    ‖u‖_((0;k),𝗋_out−ε,0;+) ≤ C_k h^(−ν) ‖u‖_((s;k+ℓ_2),𝗋,𝖻;+).                                    {#eq:ii-g1-4-3b}

*Proof.* As in [[lem:ii-g1-4-1]] it suffices to work on ℝ⁴, with the b-derivatives V := ⟨x⟩D_x ([[sec:i-b-5-5]]: on
X̄ they and the V's there span the b-vector fields, with equivalent norms). By [[eq:i-b-5-9]], ‖u‖_((s;k),𝗋,𝖻;+) is
equivalent, uniformly in h, to h^(−k) ‖u‖_(𝐨;k) with ‖u‖_(𝐨;k) := Σ_(|γ|≤k) ‖(hV)^γ u‖_𝐨, 𝐨 := (s, 𝗋, 𝖻). The
operators hV_j have scalar symbols ⟨x⟩ζ_j, of order (1, 1, 0), and by [[eq:i-b-2-5]] their commutators with Q ∈ Ψ^0 lie
in Ψ^((0,0,−1)+ε′𝟏), microsupported in WF′_h(Q); inductively (hV)^γ Q = Σ_(γ′≤γ) Q_(γγ′) (hV)^(γ′) with Q_(γγ′) ∈
Ψ^(ε′𝟏) microsupported in WF′_h(Q). Choose c, ρ_* ∈ (0, 1) such that 𝗋 and 𝖻 are constant (𝗋_out, 𝖻_out) on U_0 :=
{ρ < 2ρ_*, |ζ| < 2c}, and functions ϕ_0, ϕ_1, ϕ_2 on the compactified phase space 𝒫 of [[sec:i-b-2]] with ϕ_0 + ϕ_1 +
ϕ_2 = 1, supp ϕ_0 ⊂ U_0, supp ϕ_1 ⊂ {|ζ| > c}, supp ϕ_2 ⊂ {|ζ| < 2c, ρ > ρ_*}; Q_i := Op_h(ϕ_i), Σ Q_i = I.

[[eq:ii-g1-4-3b]]: let 𝐨_t := (0, 𝗋_out − ε, 0); we show ‖u‖_(𝐨_t;k) ≤ C h^(−ν) ‖u‖_(𝐨;k+ℓ_2), which with
[[eq:i-b-5-9]] and [[eq:ii-g1-4-2]] gives [[eq:ii-g1-4-3b]]. On U_0, w_(𝐨_t) w_𝐨⁻¹ = ⟨ζ⟩^(−s) ⟨x⟩^(−ε) h^(𝖻_out) ≤
C h^(𝖻_out), and on supp ϕ_2, where x ranges over a compact set and ζ is bounded, w_(𝐨_t) w_𝐨⁻¹ ≤ C h^(inf 𝖻); so for
i = 0, 2, W_(𝐨_t) Q_(i,γγ′) W_𝐨⁻¹ has a symbol bounded by C h^(min(𝖻_out, inf 𝖻)−2ε′) times a symbol of order 0, and by
[[thm:i-b-2-7]] and [[prop:i-b-2-8]], ‖(hV)^γ Q_i u‖_(𝐨_t) ≤ C h^(−ν_0) ‖u‖_(𝐨;|γ|) + C ‖u‖_(−L𝟏), ν_0 :=
⌈(−min(𝖻_out, inf 𝖻))_+ + 1⌉. For i = 1: (hV)^γ ∈ Ψ^(|γ|(1,1,0)), so by [[prop:i-b-2-8]] ‖(hV)^γ Q_1 u‖_(𝐨_t) ≤
C ‖Q_1 u‖_(𝐨_t+k(1,1,0)) for |γ| ≤ k. With ℓ_2 := max(⌈(−s)_+⌉, ⌈𝗋_out − inf 𝗋⌉), m := k + ℓ_2 and ν_1 := ⌈(−inf
𝖻)_+⌉, 𝐨_t + k(1, 1, 0) ≤ 𝐨 + m(1, 1, 0) + (0, 0, ν_1) componentwise, so ‖Q_1 u‖_(𝐨_t+k(1,1,0)) ≤ C ‖Q_1
u‖_(𝐨+m(1,1,0)+(0,0,ν_1)) = C h^(−ν_1) ‖Q_1 u‖_(𝐨+m(1,1,0)). Finally A := Σ_(|γ|=m) ((hV)^γ)^* (hV)^γ ∈
Ψ^(2m(1,1,0)) has principal symbol Σ_(|γ|=m) |⟨x⟩^m ζ^γ|² ≥ c′ ⟨x⟩^(2m) ⟨ζ⟩^(2m) on {|ζ| ≥ c}, so it is elliptic on
WF′_h(Q_1) (as in the proof of [[thm:i-b-1-3]] (4), [[sec:i-b-8-5]], step (ii)), and [[prop:i-b-2-10]] gives ‖Q_1
u‖_(𝐨+m(1,1,0)) ≤ C(‖Au‖_(𝐨−m(1,1,0)) + ‖u‖_(−L𝟏)) ≤ C(‖u‖_(𝐨;m) + ‖u‖_(−L𝟏)), by [[prop:i-b-2-8]] for ((hV)^γ)^* ∈
Ψ^(m(1,1,0)). As ‖u‖_(−L𝟏) ≤ C ‖u‖_𝐨, [[eq:ii-g1-4-3b]] holds with ν := max(ν_0, ν_1).

[[eq:ii-g1-4-3a]] is proved in the same way, with 𝐨_d := (0, 𝗋_out + 1 + ε, 0) as the orders of the domain and 𝐨′ :=
(s − 1, 𝗋 + 1, 𝖻) as the target: w_(𝐨′) w_(𝐨_d)⁻¹ ≤ C h^(−𝖻_out) on U_0 and ≤ C h^(−sup 𝖻) on supp ϕ_2; and 𝐨′ +
k(1, 1, 0) ≤ 𝐨_d + (k + ℓ_1)(1, 1, 0) + (0, 0, ν_1) with ℓ_1 := max(⌈(s − 1)_+⌉, ⌈sup 𝗋 − 𝗋_out⌉) and ν_1 :=
⌈(sup 𝖻)_+⌉. ∎

**Proposition {#prop:ii-g1-4-4}** (Resolvent bounds at high frequencies; [Hin26c, Proposition 13.16] in dimension 4 + 1.)
Assume (H1)–(H8) of [[sec:i-a-1-3]], [[sec:i-b-1-2]] and [[sec:i-b-1-5]], and let C_0 be as in [[thm:i-b-1-3]] (3). Let
β_scf < 3/2 + S̄, ε ∈ (0, 1), η > 0, δ_1, δ_2 ∈ ℝ, and δ := δ_Γ(−η) ([[eq:i-b-1-4]]). There is ℓ ∈ ℕ₀ such that for
all k ∈ ℕ₀, P̂⁻¹ : f̂ ↦ (σ ↦ P̂(σ)⁻¹ f̂(σ)) is bounded

    H^(k+⌈kδ⌉+ℓ, β_scf+1, δ_1)_(b+)(±[C_0, ∞) × X̄) → H^(k, β_scf−ε, δ_2)_(b+)(±[C_0, ∞) × X̄),          {#eq:ii-g1-4-4}

the spaces of [[sec:ii-g1-3-1]] with X̄ and μ_b.

[Hin26c, Proposition 13.16] writes the loss as k(1 + δ_Γ(−ε)) + ℓ, which need not be an integer, and states the
proposition without proof. It also notes that the loss in k is harmless for strongly trapping admissible operators with
ε = 1/k. In the terms of [[eq:i-b-1-4]]: if γ_+ < 0, then δ_Γ(−η) = 0 for η < −γ_+; if γ_+ = 0, then δ_Γ(−η) =
η/(−γ_−) for 0 < η ≤ −γ_−, and ⌈k δ_Γ(−1/k)⌉ = ⌈1/(−γ_−)⌉ for every k ≥ 1/(−γ_−) [[pending:issue-1]].

*Proof.* Take z_0 := ±1, h := |σ|⁻¹ (so z = hσ = z_0 for real σ), α_+ := 0, and the orders above with 𝗋_out := β_scf −
2 − ε/2, 𝖻 ≡ 0; let ℓ_1, ℓ_2, ν be those of [[lem:ii-g1-4-3]] with ε/2. For ±σ ≥ C_0, P̂(σ) is invertible
([[thm:i-b-1-3]] (3)), and [[eq:i-b-1-8]] reads

    ‖(σ∂_σ)^j P̂(σ)⁻¹ g‖_((s+j;m),𝗋,0;+) ≤ C |σ|^(−1+(j+1)δ) ‖g‖_((s−1;m+j),𝗋+1,0;+).

By [[eq:ii-g1-4-2]] at h = |σ|⁻¹, the norm of v := P̂⁻¹ f̂ in the target of [[eq:ii-g1-4-4]] is equivalent to (Σ_(l≤k)
∫ |σ|^(2δ_2) ‖(σ∂_σ)^l v‖²_((0;k−l),𝗋_out−ε/2,0;+) |dσ/σ|)^(1/2), as β_scf − ε − 2 = 𝗋_out − ε/2. By Leibniz' rule
(first for f̂ in the dense subspace of functions smooth in σ, as in [[cor:ii-g1-4-2]] (2), then by continuity),
(σ∂_σ)^l v is a combination of ((σ∂_σ)^(l′) P̂⁻¹) g_(l′), g_(l′) := (σ∂_σ)^(l−l′) f̂, l′ ≤ l ([[thm:i-b-1-3]] (5)
gives the differentiability), and by [[eq:ii-g1-4-3b]], [[eq:i-b-1-8]] and [[eq:ii-g1-4-3a]], at fixed σ,

    ‖((σ∂_σ)^(l′) P̂⁻¹) g‖_((0;k−l),𝗋_out−ε/2,0;+) ≤ C |σ|^(2ν−1+(l′+1)δ) ‖g‖_((0;k_1),𝗋_out+1+ε/2,0;+),
                                                          k_1 := k − l + l′ + ℓ_1 + ℓ_2,

and 2ν − 1 + (l′ + 1)δ ≤ 2ν + kδ as l′ ≤ k, δ ≤ 1, |σ| ≥ 1. By [[eq:ii-g1-4-2]], as 𝗋_out + 1 + ε/2 + 2 = β_scf + 1,
the last norm is Σ_(j≤k_1) |σ|^j ‖g‖_(H̄^(k_1−j,β_scf+1)_b). Let m_1 := 2ν + ⌈kδ⌉ + ⌈(δ_2 − δ_1)_+⌉, so |σ|^(δ_2)
|σ|^(2ν+kδ) |σ|^j ≤ |σ|^(δ_1) |σ|^(j+m_1). The function σ^(j+m_1) (σ∂_σ)^(l−l′) f̂ with values in
H̄^(k_1−j,β_scf+1)_b is a term of the norm of f̂ in H^(k′,β_scf+1,δ_1)_(b+) with k′ = (j + m_1) + (l − l′) + (k_1 − j) =
k + m_1 + ℓ_1 + ℓ_2. So [[eq:ii-g1-4-4]] holds with ℓ := ℓ_1 + ℓ_2 + 2ν + ⌈(δ_2 − δ_1)_+⌉. ∎

**Corollary {#cor:ii-g1-4-5}** (The high-frequency part of a forward solution; [Hin26c, Corollary 13.17] in dimension 4
+ 1.) Assume (H1)–(H8) of [[sec:i-a-1-3]], [[sec:i-b-1-2]] and [[sec:i-b-1-5]] for the spectral family P̂ of a
stationary wave-type operator P_0 ([[lem:ii-c-1-2]]), let C_0 ≥ 1 be as in [[thm:i-b-1-3]] (3) (enlarged if necessary,
which preserves invertibility), χ ∈ C^∞_c(ℝ) equal to 1 on [−C_0, C_0], and χ_T ∈ C^∞(ℝ) equal to 0 on (−∞, 1] and to
1 on [2, ∞). Let β_I, β_ι, β_K, β′_ι, β′_K ∈ ℝ, β′_I < min(β_I, 3/2 + S̄), η > 0 and δ := δ_Γ(−η). There is ℓ ∈ ℕ₀
such that for every k and every f ∈ H^(k+⌈kδ⌉+ℓ,(β_I+1,β_ι+2,β_K))_b(M; E) (M over X̄, [[rem:ii-g1-3-7]]), u :=
ℱ⁻¹((1 − χ(σ)) P̂(σ)⁻¹ f̂(σ)) lies in H^(k,(β′_I,β′_ι,β′_K))_b(M; E), with norm ≤ C_k ‖f‖. If f ∈
H^(k+⌈kδ⌉+ℓ,(β_I+1,β_ι+2,β_K))_b(Ω; E)^(•,−) (extended by 0 to t_* < 1), then χ_T(t_*) u ∈
H^(k,(β′_I,β′_ι,β′_K))_b(Ω; E)^(•,−).

Here, as in [Hin26c, Section 13], the b-spaces on Ω are those of [[eq:ii-f1-1-2]] with the unweighted b-density μ_b of
[[cor:ii-f1-1-2]]; on Ω the defining functions [[eq:ii-g1-3-1]] and those of [[eq:ii-f1-1-1]] (ρ_I, ρ_+, ρ_K for ℐ⁺,
ι⁺, K⁺) are comparable with ratios bounded with all their b-derivatives, and μ_M and μ_b likewise, so these spaces are
restrictions of those on M.

*Proof.* Let k_f be the order of f. By [[prop:ii-g1-3-3]] (2) with the weights (β_I + 1, β_ι + 2, β_K),
f̂|_(±[1/2,∞)) ∈ H^(k_f−ℓ_5,β_I+1,0)_(b+), ℓ_5 := ⌈(1/2 − min(β_K, β_ι + 1 − β_I))_+⌉. Let β_scf := β′_I + ε with ε > 0
so small that β_scf < min(β_I, 3/2 + S̄); then H^(·,β_I+1,·)_(b+) ⊂ H^(·,β_scf+1,·)_(b+). Let ℓ_3 := 1 + ⌈(max(β′_K,
β′_ι − β′_I) − 1/2)_+⌉, the loss of [[prop:ii-g1-3-5]] (2) with δ = 1 and the weights (β′_I, β′_ι, β′_K), and ℓ_4 that
of [[prop:ii-g1-4-4]] with δ_1 = 0 = δ_2. By [[prop:ii-g1-4-4]] at the order k + ℓ_3 (and ⌈(k + ℓ_3)δ⌉ ≤ ⌈kδ⌉ + ℓ_3),
P̂⁻¹ f̂ ∈ H^(k+ℓ_3,β′_I,0)_(b+)(±[C_0, ∞) × X̄) when k_f ≥ k + ⌈kδ⌉ + 2ℓ_3 + ℓ_4 + ℓ_5. Multiplied by 1 − χ, which
vanishes on [−C_0, C_0] and is smooth with bounded σ∂_σ-derivatives, and extended by 0, it lies in
H^(k+ℓ_3,β′_I,0)_(b+)(±[1/2, ∞) × X̄) and vanishes near [−1/2, 1/2]; [[prop:ii-g1-3-5]] (2) (with δ − 1 = 0) gives u ∈
H^(k,(β′_I,β′_ι,β′_K))_b(M). So ℓ := 2ℓ_3 + ℓ_4 + ℓ_5. Finally χ_T(t_*) is smooth with bounded b-derivatives on M, and
χ_T(t_*) u is supported in {t_* ≥ 1}, so its restriction lies in the space on Ω. ∎

#### Low frequencies {#sec:ii-g1-4-3}

For ς > 0 and weights β = (β_scf, β_tf, β_zf), let w_β(ς) be the product of ρ_scf^(β_scf), ρ_tf^(β_tf) and
ρ_zf^(β_zf) of [[eq:ii-g1-3-2]] at |σ| = ς, a function of x, and ‖u‖_(H^(k,β)_(b,ς)) := ‖w_β(ς)⁻¹ u‖_(H̄^k_b(X̄,μ_b))
([Hin26c, after (13.30a)]). The b-derivatives of log w_β(ς) in x are bounded uniformly in ς, so weights and derivatives
may be ordered either way, and the norm of H^(k,β)_b(X^±_(sc-b)) is equivalent to (Σ_(k′≤k) ∫ ‖(σ∂_σ)^(k′)
u(σ)‖²_(H^(k−k′,β)_(b,|σ|)) |dσ/σ|)^(1/2), as σ∂_σ log w_β is bounded too. The norms ‖·‖_((s;k),(𝗋,l,q),ς) are those
of [[def:i-c-6-1]], with a decay order 𝗋 on the scattering face of tf, and ς_1 that of [[lem:i-c-6-2]].

**Lemma {#lem:ii-g1-4-6}** (Low-energy spaces and b-spaces; [Hin26c, (13.30a)–(13.30b)] in dimension 4 + 1.) Let (s, 𝗋)
be an order pair with s constant and 𝗋 equal to 𝗋_out near the zero section over the scattering face of tf, let ℓ, ℓ̃
be as in [[lem:ii-g1-4-1]], and l ∈ ℝ, k ∈ ℕ₀, ε > 0. Uniformly in ς ∈ (0, ς_1],

    ‖u‖_((s−1;k),(𝗋+1,l+2,0),ς) ≤ C ‖u‖_(H^(k+ℓ,(𝗋_out+3+ε, l+4, 0))_(b,ς)),                           {#eq:ii-g1-4-5a}

    ‖u‖_(H^(k−ℓ̃,(𝗋_out+2−ε, l+2, 0))_(b,ς)) ≤ C ‖u‖_((s;k),(𝗋,l,0),ς)        (k ≥ ℓ̃).               {#eq:ii-g1-4-5b}

[Hin26c, (13.30a)–(13.30b)] have 5/2, 7/2 and 3/2, 3/2 in place of 3, 4 and 2, 2 (the shift n/2 with n the spatial
dimension), and are written with α_+, α_tf (here absorbed in 𝗋 and l).

*Proof.* By [[def:i-c-6-1]], ‖u‖²_((s;k),(𝗋,l,0),ς) = ‖(1 − χ_∂)u‖²_(H̄^(s+k)) + ς^(−2(l+2)) ‖S_ς(χ_∂
u)‖²_(H^((s;k),(𝗋,−l))_(sc,b;b)(tf)), and by [[lem:i-c-6-2]] (b) multiplication by χ_∂ is bounded uniformly on both
sides. *The interior.* On supp(1 − χ_∂), a compact set, ρ_tf and ρ_scf are bounded above and below and
ρ_zf^(β_zf) = 1 (β_zf = 0), so the norms on the right of [[eq:ii-g1-4-5a]] and the left of [[eq:ii-g1-4-5b]] are
equivalent to H̄^(k+ℓ), resp. H̄^(k−ℓ̃), there, and k + ℓ ≥ s − 1 + k, k − ℓ̃ ≤ s + k. *Near ∂X.* Let x̂ := ςx and ρ̂ :=
⟨x⟩⁻¹/ς; then ρ_scf = ρ̂/(1 + ρ̂), ρ_tf = ς(1 + ρ̂) and ρ_zf = (1 + ρ̂)⁻¹ exactly, so w_β(ς) = ς^(β_tf) W_β(ρ̂) with
W_β(ρ̂) := (ρ̂/(1 + ρ̂))^(β_scf) (1 + ρ̂)^(β_tf−β_zf), independent of ς. On supp χ_∂ (|x| ≥ R_1) the dilation S_ς
preserves μ_b and maps the b-fields ⟨x⟩∂_x to fields spanning, with bounded coefficients, the b-fields of tf
([[sec:i-c-4]]: r̂∂_(x̂) near ztf, ⟨x̂⟩∂_(x̂) near sctf). Hence ‖χ_∂ u‖_(H^(k,β)_(b,ς)) is equivalent, uniformly in ς,
to ς^(−β_tf) ‖W_β⁻¹ S_ς(χ_∂ u)‖_(H^k_b(tf,μ_b)), a b-norm on tf with the weight ρ̂^(β_scf) at sctf (ρ̂ → 0) and
r̂^(β_zf−β_tf), r̂ = |x̂|, at ztf. For [[eq:ii-g1-4-5b]], β = (𝗋_out + 2 − ε, l + 2, 0): the powers ς^(−(l+2)) agree;
at ztf both norms are b-norms ([[def:i-c-4-1]]: b-regularity is regularity there) with the b-weight −l − 2 for μ_b; at
sctf the tf norm is that of H^((s;k),𝗋)_sc(ℝ⁴_(x̂)) and the b-norm has the scattering decay order 𝗋_out − ε
([[def:i-c-4-1]] and the density shift), and [[lem:ii-g1-4-1]] [[eq:ii-g1-4-1b]] on ℝ⁴_(x̂), with α = 0, compares them;
in between, on compact subsets of tf°, both are standard Sobolev norms of orders s + k ≥ k − ℓ̃. [[eq:ii-g1-4-5a]] is
the same with β = (𝗋_out + 3 + ε, l + 4, 0): the powers are ς^(−(l+4)) on both sides (the norm of [[def:i-c-6-1]] has
l + 2 in place of l), the b-weight at ztf is −l − 4 on both sides (q − (l + 2) − 2 with q = 0), and at sctf
[[eq:ii-g1-4-1a]] compares the decay orders 𝗋_out + 1 + ε and 𝗋 + 1. ∎

**Proposition {#prop:ii-g1-4-7}** (Resolvent bounds at low frequencies; [Hin26c, Proposition 13.18] in dimension 4 + 1.)
Assume (H1)–(H4) of [[sec:i-a-1-3]] and (G), (Z) and (TF) of [[sec:i-c-1-2]] with the weight α (α + 2 in an indicial gap
of P̂(0), for μ_b). Let β_scf < 3/2 + S̄ and ε ∈ (0, 1). There is ℓ ∈ ℕ₀, depending only on P̂ and β_scf, and for each
k ∈ ℕ₀ there is c_k > 0 such that, with X^±_(sc-b) built on ±[0, c_k], for all β_tf, β_zf with β_tf − β_zf = α + 2,

    P̂⁻¹ : H^(k+ℓ,(β_scf+1, β_tf+2, β_zf))_b(X^±_(sc-b)) → H^(k,(β_scf−ε, β_tf, β_zf))_b(X^±_(sc-b))   is bounded.
                                                                                                  {#eq:ii-g1-4-6}

[Hin26c, Proposition 13.18] fixes one c for all k; [[thm:i-c-6-4]] (4) gives radii c_(j,k) depending on j and k
([[rem:i-c-6-7]] (a)), so here c_k depends on k. The gap condition is on the b-weight for μ_b, as in (G). As
[[thm:i-c-6-4]] (5) gives its conclusions at every weight of the gap ((Z) by [[thm:i-c-3-1]] (4), (TF) by
[[cor:i-c-5-2]] (c)), and ℓ = ℓ_a + ℓ̃ does not depend on α, the proposition holds for every β_tf − β_zf in the gap with
one ℓ, as [Hin26c, (13.31)] states; only c_k and the constants depend on the weight.

*Proof.* As |σ|^(β_zf) = ρ_tf^(β_zf) ρ_zf^(β_zf) is scalar in σ, commutes with P̂(σ)⁻¹, and σ∂_σ |σ|^(β_zf) = β_zf
|σ|^(β_zf), dividing by it reduces to β_zf = 0, β_tf = α + 2. Take α_+ := 0, 𝗋_out := β_scf − 2 − ε/2, 𝗋_in and s as in
[[cor:ii-g1-4-2]], and the decay orders 𝗋_± of [[sec:i-c-4-3]] built from them ([[lem:i-a-7-1]] at σ_* = ±1), which
equal 𝗋_out near the zero section over sctf; let ℓ_a, ℓ̃ be those of [[lem:ii-g1-4-1]] for them and ℓ := ℓ_a + ℓ̃. By
[[thm:i-c-6-4]] (4) (with m_1 = m_2 = 0, which (Z) allows) and (5), for 0 < |σ| ≤ c_(j,m), Im σ ≥ 0,

    ‖(σ∂_σ)^j P̂(σ)⁻¹ g‖_((s+j;m),(𝗋,α,0),ς) ≤ C ‖g‖_((s−1;m+j),(𝗋+1,α+2,0),ς),        ς = |σ|.

Let c_k := min(ς_1, min{c_(j,m) : j ≤ k, m ≤ k + ℓ̃}). For k′ ≤ k, Leibniz' rule (first for f̂ in the dense subspace of
functions smooth in σ, as in [[cor:ii-g1-4-2]] (2), then by continuity) writes (σ∂_σ)^(k′)(P̂⁻¹ f̂) as a combination of
((σ∂_σ)^(k″) P̂⁻¹) g, g := (σ∂_σ)^(k′−k″) f̂, and at fixed σ, by [[eq:ii-g1-4-5b]] with l = α and ε/2, the estimate
above with m = k − k′ + ℓ̃, and [[eq:ii-g1-4-5a]] with l = α and ε/2,

    ‖((σ∂_σ)^(k″) P̂⁻¹) g‖_(H^(k−k′,(β_scf−ε,α+2,0))_(b,ς)) ≤ C ‖g‖_(H^(k−k′+k″+ℓ,(β_scf+1,α+4,0))_(b,ς)),

as 𝗋_out + 2 − ε/2 = β_scf − ε and 𝗋_out + 3 + ε/2 = β_scf + 1. The total order (k′ − k″) + (k − k′ + k″ + ℓ) = k + ℓ
is that of the domain, so integrating in |dσ/σ| gives [[eq:ii-g1-4-6]]. ∎


### The radiation field in dimension 4 + 1 {#sec:ii-g1-5}

#### The normal form near null infinity {#sec:ii-g1-5-1}

We use the defining functions [[eq:ii-f1-1-1]], ρ_I = t_*/(t_* + r) and ρ_+ = (t_* + r)/(t_* r), of ℐ⁺ and ι⁺. On
{t_* > 0, r > 0} the map (t_*, r) ↦ (ρ_I, ρ_+) is a diffeomorphism onto {0 < ρ_I < 1, ρ_+ > 0}, with inverse t_* =
(ρ_+(1 − ρ_I))⁻¹, r = (ρ_I ρ_+)⁻¹, and ρ_K = 1 − ρ_I. For c_0 ∈ (0, 1/4] let

    𝒞 := {0 ≤ ρ_I < c_0, 0 ≤ ρ_+ < 4} × 𝕊³,        𝒞_a := 𝒞 ∩ {ρ_I < a}    (0 < a ≤ c_0),

a neighbourhood of ℐ⁺ ∩ {t_* > 1/4} (including its corner with ι⁺) in the compactified spacetime, on which r >
1/(4c_0). On 𝒞 the b-vector fields are spanned by ρ_I∂_(ρ_I), ρ_+∂_(ρ_+) and the vector fields on 𝕊³, and μ_𝒞 :=
|(dρ_I/ρ_I)(dρ_+/ρ_+) dω| is a b-density equivalent to μ_b = |dt_* dx|/(t_* ⟨x⟩⁴): in logarithmic coordinates the
Jacobian of (log ρ_I, log ρ_+) ↦ (log t_*, log r) has determinant (1 − ρ_I)⁻¹ ∈ [1, 4/3]. H^(k,(b_I,b_+))_b(𝒞_a) :=
ρ_I^(b_I) ρ_+^(b_+) H^k_b(𝒞_a, μ_𝒞); near ℐ⁺ these are the spaces of [[cor:ii-g1-4-5]] and of [[eq:ii-f1-1-2]] with
μ_b, the weight at K⁺ being irrelevant (ρ_K ≥ 3/4 on 𝒞). Let

    𝖶 := ρ_I∂_(ρ_I) − ρ_+∂_(ρ_+),

which commutes with ρ_I∂_(ρ_I), ρ_+∂_(ρ_+) and the fields on 𝕊³. On {t_*, r > 0}, with ρ := r⁻¹,

    t_*∂_(t_*)|_r = (1 − ρ_I) 𝖶,    ρ∂_ρ|_(t_*) = ρ_I∂_(ρ_I) − ρ_I 𝖶,    ρ t_*⁻¹ = ρ_I ρ_+² (1 − ρ_I).  {#eq:ii-g1-5-1}

Indeed t_*∂_(t_*) ρ_I = ρ_I(1 − ρ_I), t_*∂_(t_*) ρ_+ = −ρ_+(1 − ρ_I), ρ∂_ρ ρ_I = ρ_I(1 − ρ_I) and ρ∂_ρ ρ_+ = ρ_I ρ_+,
so t_*∂_(t_*) = (1 − ρ_I)(ρ_I∂_(ρ_I) − ρ_+∂_(ρ_+)) and ρ∂_ρ = ρ_I(1 − ρ_I)∂_(ρ_I) + ρ_I ρ_+∂_(ρ_+) = ρ_I∂_(ρ_I) −
ρ_I 𝖶; and ρ t_*⁻¹ = (ρ_I ρ_+)(ρ_+(1 − ρ_I)).

**Lemma {#lem:ii-g1-5-1}** (The normal form in dimension 4 + 1; [Hin26c, (13.32)].) Let P_0 be a stationary wave-type
operator ([[def:ii-c-1-1]]) with S ∈ ρ C^∞(X̄) in [[eq:ii-c-1-1]], that is S|_(∂X) = 0. If c_0 is small, then on 𝒞

    (1/2) ρ_I⁻¹ ρ_+^(−2) P_0 = −(ρ_I∂_(ρ_I) − 3/2) 𝖶 + P̃,        P̃ ∈ ρ_I Diff²_b(𝒞),                {#eq:ii-g1-5-2}

with coefficients smooth on 𝒞̄. If S|_(∂X) ≠ 0, the left side differs from −(ρ_I∂_(ρ_I) − 3/2)𝖶 by S|_(∂X) 𝖶 modulo
ρ_I Diff²_b, and [[eq:ii-g1-5-2]] fails.

*Proof.* Choose c_0 so small that ρ < ρ_1 on 𝒞, where [[eq:ii-c-1-1]] holds: P_0 = −2∂_(t_*) ρ(ρ∂_ρ − 3/2 − S) +
P̂_0(0) + Q∂_(t_*) − g_00 ∂²_(t_*), all coefficients t_*-independent and smooth in (ρ, ω), so smooth in (ρ_I, ρ_+, ω) as
ρ = ρ_I ρ_+. By [[eq:ii-g1-5-1]], as ρ does not depend on t_*,

    −2∂_(t_*) ρ(ρ∂_ρ − 3/2) = −2ρ t_*⁻¹ (t_*∂_(t_*))(ρ∂_ρ − 3/2) = −2ρ_I ρ_+² (1 − ρ_I)² 𝖶 (ρ_I∂_(ρ_I) − ρ_I 𝖶 − 3/2),

so (1/2) ρ_I⁻¹ ρ_+^(−2) times it is −(1 − ρ_I)² 𝖶(ρ_I∂_(ρ_I) − 3/2) + (1 − ρ_I)² 𝖶 ρ_I 𝖶; as (1 − ρ_I)² − 1 ∈ ρ_I C^∞
and 𝖶ρ_I = ρ_I(𝖶 + 1), this is −(ρ_I∂_(ρ_I) − 3/2)𝖶 modulo ρ_I Diff²_b. The other terms, times (1/2) ρ_I⁻¹ ρ_+^(−2):
2∂_(t_*) ρS = 2ρ t_*⁻¹ S t_*∂_(t_*) gives (1 − ρ_I)² S𝖶, in ρ_I Diff¹_b as S ∈ ρ C^∞ = ρ_I ρ_+ C^∞; P̂_0(0) ∈ ρ²
Diff²_b(X̄) gives (1/2) ρ_I Diff²_b, the b-fields ρ∂_ρ, ∂_ω of X̄ being b-fields on 𝒞 by [[eq:ii-g1-5-1]]; Q∂_(t_*), Q ∈
ρ³ Diff¹_b, gives ρ³ t_*⁻¹ ρ_I⁻¹ ρ_+^(−2) = ρ_I² ρ_+² (1 − ρ_I) times b-operators; and g_00 ∂²_(t_*) = g_00 t_*^(−2)
((t_*∂_(t_*))² − t_*∂_(t_*)), g_00 ∈ ρ² C^∞ (the remarks after [[def:ii-c-1-1]]), gives ρ_I ρ_+² (1 − ρ_I)² times
b-operators. If S|_(∂X) ≠ 0, the term (1 − ρ_I)² S𝖶 contributes S|_(∂X) 𝖶 at ρ_I = 0. ∎

In dimension 4 + 1 the stationary models of [[ch:s05]] have coefficients in C^∞(X̄), so the remainder gains a full
power of ρ_I; [Hin26c, (13.32)] allows P̃ ∈ ρ_I^(1/2) Diff²_b, for coefficients smooth in x_I = ρ_I^(1/2), and notes the
gain ρ_I for Kerr. [[prop:ii-g1-5-4]] is stated for P̃ ∈ ρ_I^κ Diff²_b(𝒞), κ ∈ (0, 1], with coefficients bounded with
all their b-derivatives. For the tensor wave operators of [[lem:ii-c-1-3]], S = 0 in the coordinate frame; which
operators of the linear theory satisfy S|_(∂X) = 0 is examined where [[prop:ii-g1-5-4]] is applied to them.

**Definition {#def:ii-g1-5-2}** (Spaces with a radiation field; [Hin26c, Definition 13.19].) Let χ_I ∈ C^∞([0, ∞)) equal
1 on [0, 1/4] and 0 on [1/2, ∞). For a ∈ (0, c_0], ζ, b_I, b_+ ∈ ℝ with ζ < b_I and k ∈ ℕ₀,

    H^(k,(((ζ,0),b_I),b_+))_b(𝒞_a) := {χ_I(ρ_I/a) ρ_I^ζ u_0 + ũ : u_0 ∈ H^(k,b_+)_b(ℐ⁺), ũ ∈ H^(k,(b_I,b_+))_b(𝒞_a)},

normed by ‖u_0‖ + ‖ũ‖, where H^(k,b_+)_b(ℐ⁺) := ρ_+^(b_+) H^k_b([0, 4) × 𝕊³, |(dρ_+/ρ_+) dω|) and u_0(ρ_+, ω) is
extended to 𝒞_a as a function independent of ρ_I. If ζ ≥ b_I, the space is H^(k,(b_I,b_+))_b(𝒞_a) (take u_0 = 0).

For ζ = 3/2 and bounded t_*, ρ_I^(3/2) u_0 = (t_*/r)^(3/2) (1 + O(t_*/r)) u_0(ρ_+, ω) with ρ_+ = t_*⁻¹ + O(r⁻¹): the
leading term is r^(−3/2) times a function of (t_*, ω), the *radiation field*. The decomposition is unique when ζ < b_I,
as ρ_I^ζ ∉ ρ_I^(b_I) L²(dρ_I/ρ_I) near 0. [Hin26c, Definition 13.19] leaves the extension of u_(1,0) off ℐ⁺ unstated;
here it is extended independently of ρ_I in the coordinates of 𝒞.

#### Transport along 𝖶 {#sec:ii-g1-5-2}

In the coordinates p := −log ρ_I, q := −log ρ_+, μ_𝒞 = |dp dq dω| and 𝖶 = −∂_p + ∂_q; with c := p + q = log r, 𝖶 = ∂_q at
fixed c. So the integral curves of 𝖶 are the curves {r = const, ω = const}, run towards ι⁺ (ρ_+ decreasing, ρ_I
increasing).

**Lemma {#lem:ii-g1-5-3}** (Transport along 𝖶.) Let a ∈ (0, c_0], b, b_+ ∈ ℝ, b ≠ b_+, k ∈ ℕ₀, and let u ∈
L²_loc(𝒞_a) with 𝖶u = w ∈ H^(k,(b,b_+))_b(𝒞_a), and (ρ_I∂_(ρ_I))^i (ρ_+∂_(ρ_+))^j Z^γ u ∈ L²_loc for i + j + |γ| ≤ k
(Z the fields on 𝕊³).

(a) If b > b_+ and u = 0 on {ρ_+ > 2}, then u ∈ H^(k,(b,b_+))_b(𝒞_a), with ‖u‖ ≤ C ‖w‖.

(b) If b < b_+ and u ∈ H^(k,(b_0,b_+))_b(𝒞_a ∩ {ρ_I > a/2}) for some (any) b_0, then u ∈ H^(k,(b,b_+))_b(𝒞_(a/2)),
with ‖u‖ ≤ C(‖w‖ + ‖u‖_(H^(k,(b_0,b_+))_b(𝒞_a∩{ρ_I>a/2}))).

This replaces the integration lemma [Hin26, Lemma 2.23] used in [Hin26c].

*Proof.* The fields ∂_p, ∂_q, Z commute with 𝖶 and preserve the hypotheses, so it suffices to take k = 0 and apply the
result to the derivatives. In the coordinates (c, q, ω) the region 𝒞_a is {q > −log 4, q < c − p_a}, p_a := −log a, the
weight is ρ_I^(−b) ρ_+^(−b_+) = e^(bp+b_+q) = e^(bc+(b_+−b)q), and ∂_q u = w in distributions, so for almost every (c,
ω), q ↦ u(c, q, ω) is absolutely continuous.

(a) u = 0 for q < −log 2, so u(c, q) = ∫_(−log 2)^q w(c, q′) dq′ and

    e^(bc+(b_+−b)q) u(c, q) = ∫_(−log 2)^q e^(−(b−b_+)(q−q′)) [e^(bc+(b_+−b)q′) w(c, q′)] dq′.

The kernel e^(−(b−b_+)s) 1_(s>0) has L¹ norm (b − b_+)⁻¹; Young's inequality in q, then integration over (c, ω), gives
‖u‖ ≤ (b − b_+)⁻¹ ‖w‖.

(b) For (c, q) in 𝒞_(a/2), that is c − q > p_a + log 2, let J_c := (c − p_a − log 2, c − p_a), the values q′ with ρ_I
∈ (a/2, a) on the same curve; q′ > q there. Averaging u(c, q) = u(c, q′) − ∫_q^(q′) w(c, q″) dq″ over q′ ∈ J_c,

    u(c, q) = (log 2)⁻¹ ∫_(J_c) u(c, q′) dq′ − (log 2)⁻¹ ∫_(J_c) ∫_q^(q′) w(c, q″) dq″ dq′.

On J_c, e^(b_+q′) is comparable to e^(b_+(c−p_a)) and e^(b_0 p′) to a constant, so the first term is at most C e^(−b_+c)
U(c), U(c)² := ∫_(J_c) |e^(b_0 p′+b_+q′) u(c, q′)|² dq′; times the weight it is at most C e^((b−b_+)(c−q)) U(c) = C
e^((b−b_+)p) U(c), whose L² norm over p > p_a + log 2 is at most C U(c), as b < b_+; and ∫ U(c)² dc is the norm of u
on the strip. In the second term, for each q′, e^(bc+(b_+−b)q) ∫_q^(q′) w = ∫_q^(q′) e^(−(b_+−b)(q″−q))
e^(bc+(b_+−b)q″) w(c, q″) dq″, and the kernel e^(−(b_+−b)s) 1_(s>0) has L¹ norm (b_+ − b)⁻¹; Minkowski's inequality
over q′ and Young's inequality bound it by (b_+ − b)⁻¹ ‖e^(bc+(b_+−b)q) w‖. ∎

#### The radiation field {#sec:ii-g1-5-3}

**Proposition {#prop:ii-g1-5-4}** (The radiation field; [Hin26c, Proposition 13.20] in dimension 4 + 1.) Suppose that on
𝒞, (1/2) ρ_I⁻¹ ρ_+^(−2) P_0 = −(ρ_I∂_(ρ_I) − 3/2)𝖶 + P̃ with P̃ ∈ ρ_I^κ Diff²_b(𝒞), κ ∈ (0, 1] (by [[lem:ii-g1-5-1]],
κ = 1 when S|_(∂X) = 0). Let β_I, β_+, β′_I ∈ ℝ with

    β_+ ≠ 3/2,        β′_I < 3/2 + κ,        β′_I ∉ {3/2, β_+}.

There are ℓ ∈ ℕ₀ and a ∈ (0, c_0], depending only on β_I, β′_I, κ and c_0, such that: if u ∈
H^(k+ℓ,(β_I,β_+))_b(𝒞) vanishes on {t_* < 1} and P_0 u ∈ H^(k+ℓ,(β′_I+1,β_++2))_b(𝒞), then

    u ∈ H^(k,(((3/2,0),β′_I),β_+))_b(𝒞_a).                                                         {#eq:ii-g1-5-3}

So u has a radiation field ρ_I^(3/2) u_0, the coefficient of r^(−3/2), plus a remainder with the weight of P_0 u at ℐ⁺,
shifted by the factor ρ_I ρ_+² of [[eq:ii-g1-5-2]]. In dimension 3 + 1, [Hin26c, Proposition 13.20] has the exponent 1,
the condition 1 ≠ β_+ < β_I, and β′_I < 3/2 = 1 + 1/2 (κ = 1/2); here the hypothesis β_+ < β_I is not used, and the loss
depends on κ as well as on β_I and β′_I.

*Proof.* If β_I ≥ β′_I there is nothing to prove (u_0 = 0). Otherwise we improve the weight at ℐ⁺ in steps. On 𝒞,
{ρ_+ > 2} ⊂ {t_* < 1} (as 1 − ρ_I ≥ 3/4), so u = 0 there.

*The step.* Suppose u ∈ H^(k_1,(((3/2,0),b),β_+))_b(𝒞_(a′)) with k_1 ≥ 2 and b < β′_I, u = χ_I(ρ_I/a′) ρ_I^(3/2) u_0 + ũ
(with u_0 = 0 if b ≤ 3/2). Let b″ ∈ (b, min(b + κ, β′_I)], with b″ = β′_I if b + κ ≥ β′_I and b″ ≥ b + κ/2 otherwise,
chosen outside {3/2, β_+}. We show u ∈ H^(k_1−2,(((3/2,0),b″),β_+))_b(𝒞_(a′/8)).

(i) Let h := P̃u − (1/2) ρ_I⁻¹ ρ_+^(−2) P_0 u, so that (ρ_I∂_(ρ_I) − 3/2)𝖶u = h. P̃ maps χ_I ρ_I^(3/2) u_0 into
H^(k_1−2,(3/2+κ−ε,β_+))_b for every ε > 0 (ρ_I^(3/2) lies in ρ_I^(3/2−ε) L²(dρ_I/ρ_I) near 0), hence into
H^(k_1−2,(b″,β_+))_b as b″ ≤ β′_I < 3/2 + κ; it maps ũ into H^(k_1−2,(b+κ,β_+))_b ⊂ H^(k_1−2,(b″,β_+))_b; and (1/2)
ρ_I⁻¹ ρ_+^(−2) P_0 u ∈ H^(k_1,(β′_I,β_+))_b. So h ∈ H^(k_1−2,(b″,β_+))_b(𝒞_(a′)). (The proof of [Hin26c,
Proposition 13.20] expands h with a ρ_I^(3/2) term and then places h in a space with ℐ⁺-weight below 3/2, where that
term already lies in the remainder; no expansion of h is needed.)

(ii) Let w := 𝖶u ∈ H^(k_1−1,(·,β_+))_b. In the product 𝒞_(a′) = [0, a′)_(ρ_I) × ([0, 4) × 𝕊³), apply
[[lem:ii-g1-3-2]] in s := ρ_I/a′ to (s∂_s − 3/2)w = h, with values in ℋ_j := H^(k_1−2−j,β_+)_b([0, 4) × 𝕊³) and
s-regularity j, j ≤ k_1 − 2 (the fields in (ρ_+, ω) commute with ρ_I∂_(ρ_I), and w has k_1 − 1 b-derivatives on the
annulus). If b″ > 3/2, [[lem:ii-g1-3-2]] (a) gives, on 𝒞_(a′/4), w = ρ_I^(3/2) w_0 + w̃ with w_0 ∈
H^(k_1−2,β_+)_b(ℐ⁺) and w̃ ∈ H^(k_1−2,(b″,β_+))_b; w_0 = 0 on {ρ_+ > 2}, as w vanishes there. If b″ < 3/2,
[[lem:ii-g1-3-2]] (b) gives w ∈ H^(k_1−2,(b″,β_+))_b(𝒞_(a′/4)).

(iii) *Transport.* Write a_1 := a′/4. *If b″ < 3/2:* if b″ > β_+, [[lem:ii-g1-5-3]] (a) on 𝒞_(a_1) gives u ∈
H^(k_1−2,(b″,β_+))_b(𝒞_(a_1)); if b″ < β_+, [[lem:ii-g1-5-3]] (b), with the a priori bound on the strip {ρ_I ∈ (a_1/2,
a_1)} from u ∈ H^(k_1,(b,β_+))_b there, gives it on 𝒞_(a_1/2). As b″ < 3/2 this is the space of [[eq:ii-g1-5-3]] at b″.

*If b″ > 3/2 and b″ > β_+:* the backward integral curve of 𝖶 from a point of 𝒞_(a_1) stays in 𝒞_(a_1) until ρ_+ = 2,
where u = 0. Let

    u_0^v(ρ_+) := ρ_+^(3/2) ∫_(ρ_+)^2 s^(−3/2) w_0(s) ds/s,

which vanishes for ρ_+ ≥ 2 and satisfies (3/2 − ρ_+∂_(ρ_+)) u_0^v = w_0, so 𝖶(ρ_I^(3/2) u_0^v) = ρ_I^(3/2) w_0. Then u −
ρ_I^(3/2) u_0^v vanishes on {ρ_+ > 2} and 𝖶(u − ρ_I^(3/2) u_0^v) = w̃, so by [[lem:ii-g1-5-3]] (a), u − ρ_I^(3/2) u_0^v ∈
H^(k_1−2,(b″,β_+))_b(𝒞_(a_1)). If β_+ < 3/2, then u_0^v ∈ H^(k_1−2,β_+)_b(ℐ⁺): in log ρ_+, ρ_+^(−β_+) u_0^v is the
convolution of s^(−β_+) w_0 with the kernel (ρ_+/s)^(3/2−β_+) 1_(s>ρ_+), of L¹(ds/s) norm (3/2 − β_+)⁻¹, and
ρ_+∂_(ρ_+) commutes with it. If β_+ > 3/2, then L := ∫_0^2 s^(−3/2) w_0(s) ds/s converges (Cauchy–Schwarz, β_+ > 3/2)
and u_0^v = ρ_+^(3/2) L − u_0^(0) with u_0^(0)(ρ_+) := ρ_+^(3/2) ∫_0^(ρ_+) s^(−3/2) w_0 ds/s ∈ H^(k_1−2,β_+)_b(ℐ⁺), by
the same convolution with the kernel (ρ_+/s)^(3/2−β_+) 1_(s<ρ_+). On {ρ_I ∈ (a_1/4, a_1/2)}, u, u − ρ_I^(3/2) u_0^v and
ρ_I^(3/2) u_0^(0) lie in ρ_+^(β_+) L²(μ_𝒞), hence so does ρ_I^(3/2) ρ_+^(3/2) L(ω); as ∫_0^4 ρ_+^(2(3/2−β_+))
dρ_+/ρ_+ = ∞, L = 0, and u_0^v = −u_0^(0) ∈ H^(k_1−2,β_+)_b(ℐ⁺). In both cases u = ρ_I^(3/2) u_0^v + (u − ρ_I^(3/2)
u_0^v) is in the space of [[eq:ii-g1-5-3]] at b″ on 𝒞_(a_1/2) (replacing ρ_I^(3/2) u_0^v by χ_I(ρ_I/(a_1/2))
ρ_I^(3/2) u_0^v changes it by a function supported in {ρ_I ≥ a_1/8}, in every ρ_I-weight).

*If b″ > 3/2 and b″ < β_+* (so β_+ > 3/2): let u_0 := −u_0^(0) ∈ H^(k_1−2,β_+)_b(ℐ⁺) (as above), which satisfies (3/2
− ρ_+∂_(ρ_+)) u_0 = w_0, and U := χ_I(4ρ_I/a_1) ρ_I^(3/2) u_0, supported in {ρ_I < a_1/8}. Then

    𝖶(u − U) = w̃ + ρ_I^(3/2) (1 − χ_I(4ρ_I/a_1)) w_0 − (ρ_I∂_(ρ_I) χ_I(4ρ_I/a_1)) ρ_I^(3/2) u_0
             ∈ H^(k_1−2,(b″,β_+))_b(𝒞_(a_1)),

the last two terms being supported in {ρ_I ≥ a_1/16}; and u − U = u on {ρ_I > a_1/2}. [[lem:ii-g1-5-3]] (b) gives u − U
∈ H^(k_1−2,(b″,β_+))_b(𝒞_(a_1/2)).

*Iteration.* Each step raises b by at least κ/2 until b = β′_I, costs two b-derivatives, and shrinks the region by a
factor 8. Starting from b := β_I (with u_0 = 0), after n_s := ⌈2(β′_I − β_I)/κ⌉ steps b = β′_I; so [[eq:ii-g1-5-3]]
holds with ℓ := 2n_s and a := c_0 8^(−n_s). ∎

**Remark {#rem:ii-g1-5-5}** (The radiation field of a forward solution.) With [[lem:ii-g1-5-1]], [[prop:ii-g1-5-4]]
applies in dimension 4 + 1 with κ = 1 to stationary wave-type operators with S|_(∂X) = 0, for β′_I < 5/2; at the level
of P_0 u ∈ ρ_I^(β′_I+1), the remainder of u after its radiation field r^(−3/2) u_I decays like ρ_I^(β′_I). The proof of
[Hin26c, Proposition 13.20] integrates the equation by [Hin26, Lemmas 2.12 and 2.23]; [[lem:ii-g1-3-2]] and
[[lem:ii-g1-5-3]] replace them, and the case distinction in step (iii) follows that proof (b″ against β_+, and the
transport of the radiation field to a term ρ_+^(3/2) at ι⁺, which the a priori decay at ι⁺ excludes).

### What is not used, and uniformity in the operator {#sec:ii-g1-6}

#### Not used {#sec:ii-g1-6-1}

(a) [Hin26c, Remark 13.1] (nonlinear variants) describes how stronger decay of the right side can be fed back through
the inverse of the linear operator. It states nothing to prove. The stability theory improves decay at the level of the
linearised equations, which is the alternative the remark recommends.

(b) [Hin26c, Remark 13.15] (losses in b-regularity) explains why [[sec:ii-g1-4]] proves its bounds on variable order
spaces before passing to b-spaces: a lossy b-estimate on P̂(σ)⁻¹, iterated for ∂^j_σ P̂(σ)⁻¹, would lose a number of
b-derivatives growing with j, which tame estimates do not tolerate. [[lem:ii-g1-4-1]], [[cor:ii-g1-4-2]] and
[[prop:ii-g1-4-7]] follow that plan, with a loss depending only on the weights ([[rem:ii-g1-3-6]]).

(c) [Hin26c, Theorem 13.21] (small data global existence for □_g u = f + u³ on Kerr) and [Hin26c, Remark 13.22] (almost
t_*^(−2) decay of linear scalar waves on Kerr) are model applications on the four-dimensional Kerr spacetime. They rest
on the 0-admissibility of □_g on Kerr ([Hin26c, Theorem 12.2]) and on the proof of [Hin26c, Theorem 12.9], neither of
which is used ([[sec:ii-g-5-2]] (a), (c)), and their weights in dimension 4 + 1 are not derived.

(d) [Hin26c, Lemmas 13.2 and 13.6], and the parts of [Hin26c, Lemma 13.4 and Corollary 13.5] beyond [[lem:ii-g1-2-4]]:
[[rem:ii-g1-2-9]].

(e) The figures of [Hin26c, Section 13] illustrate the spaces M and X^±_(sc-b) and the weights in [Hin26c, Propositions
13.9 (1) and 13.11 (1)]; they carry no statement. The commentary after [Hin26c, Proposition 13.18] (inputs with weight
−1/2 at zf, and the decay they give in [Hin26c, (11.7)]) states nothing to prove.

#### Uniformity in the operator {#sec:ii-g1-6-2}

[[sec:ii-g1-2]] and [[sec:ii-g1-3]] involve no operator. In [[sec:ii-g1-4]], [[lem:ii-g1-4-1]], [[lem:ii-g1-4-3]] and
[[lem:ii-g1-4-6]] depend on the orders alone; the orders depend on P̂ only through the quantities of [[ch:s01]] that
fix them (S̄, ϑ_in, ϑ_ℋ and the data of [[lem:i-a-7-1]]). [[cor:ii-g1-4-2]], [[prop:ii-g1-4-4]], [[cor:ii-g1-4-5]] and
[[prop:ii-g1-4-7]] depend on P̂ further only through the constants of the estimates they cite: [[thm:i-a-7-2]],
[[thm:i-b-1-3]] with the constant C_0 and the function δ_Γ, and [[thm:i-c-6-4]] with its radii c_(j,k). In
[[sec:ii-g1-5]], [[prop:ii-g1-5-4]] depends on P_0 only through κ, c_0, the coordinates of 𝒞 and finitely many
seminorms of the coefficients of P̃ in [[eq:ii-g1-5-2]], as a b-differential operator on 𝒞̄, the number of seminorms
depending on k and ℓ.

So every bound of this half of the chapter, and every loss ℓ and radius c_k, is uniform over any family of operators for
which these quantities are uniform. [[sec:i-a-8]], [[sec:i-b-9]] and [[sec:i-c-7]] give conditions under which the
cited estimates are uniform over a family of operators. For the family of stationary models that the nonlinear theory
uses, the forward problem is solved uniformly in [[thm:iii-h2-4-1]]; this chapter adds no condition to that.
