## Appendix. Results from the literature {#app:standard-results}

The proofs use the published results below as stated, without proof. Each is cited by its source, with its number and
its page where given. Pages are those of the arXiv versions listed in the references; the arXiv text of [BGP] carries
the book's page numbers, [See64] is cited by its journal page, [Mel93] by the page of the author's online edition
(version 5.0E, 1993), and [DLMF] by equation number. Quotation marks enclose the source's own wording, transcribed into
this edition's typography; an ellipsis marks words of the statement left out because no proof here depends on them.
Inside each item the letters are the source's.

### Linear wave equations on Lorentzian manifolds {#sec:std-linear-wave}

**Theorem {#thm:std-bgp-causal}** ([BGP, Definition 1.3.8, p. 23; Corollary 1.3.12 and Theorem 1.3.13, p. 24;
Corollary A.5.4 and Lemma A.5.6, p. 174; Lemma A.5.9, p. 176].)

(1) Definition 1.3.8: "A connected timeoriented Lorentzian manifold is called globally hyperbolic if it satisfies the
strong causality condition and if for all p, q ∈ M the intersection J^M_+(p) ∩ J^M_−(q) is compact."

(2) Corollary 1.3.12: "On every globally hyperbolic Lorentzian manifold M there exists a smooth function h : M → ℝ
whose gradient is past directed timelike at every point and all of whose level-sets are spacelike Cauchy
hypersurfaces." Such an h is a Cauchy time-function, and "a Cauchy time-function is strictly monotonically increasing
along any future directed causal curve" (p. 24).

(3) Theorem 1.3.13: "Let M be a globally hyperbolic manifold and S be a spacelike smooth Cauchy hypersurface in M. Then
there exists a Cauchy time-function h : M → ℝ such that S = h⁻¹({0})."

(4) Corollary A.5.4: "Let S be a Cauchy hypersurface in a globally hyperbolic Lorentzian manifold M and let K ⊂ M be
compact. Then J^M_±(K) ∩ S and J^M_±(K) ∩ J^M_∓(S) are compact."

(5) Lemma A.5.6: "Let M be a timeoriented Lorentzian manifold and let S ⊂ M be a spacelike hypersurface. Then for every
point p in S, there exists a basis of open neighborhoods Ω of p in M such that S ∩ Ω is a Cauchy hypersurface in Ω."

(6) Lemma A.5.9 is [[thm:std-bgp-development]].

**Theorem {#thm:std-bgp-development}** ([BGP, Lemma A.5.9, p. 176].) "For any acausal hypersurface S in a timeoriented
Lorentzian manifold the Cauchy development D(S) is a causally compatible and globally hyperbolic open subset of M."
Its proof records that "by the definition of D(S), the acausal subset S is a Cauchy hypersurface of D(S)". The Cauchy
development D(S) is the set of points p of M such that every inextendible causal curve through p meets S [BGP,
Definition 1.3.5, p. 22].

**Definition {#def:std-normally-hyperbolic}** ([BGP, Section 1.5, p. 33].) Let M be a Lorentzian manifold and E → M a
real or complex vector bundle. "A linear differential operator P : C^∞(M, E) → C^∞(M, E) of second order will be called
normally hyperbolic if its principal symbol is given by the metric, σ_P(ξ) = −⟨ξ, ξ⟩ · id_(E_x)." In local coordinates
and a trivialisation of E,

    P = −Σ g^(ij)(x) ∂²/∂x^i∂x^j + Σ A_j(x) ∂/∂x^j + B_1(x).

**Theorem {#thm:std-bgp-cauchy}** ([BGP, Section 1.5, p. 33; Theorem 3.1.1, p. 68; Remark 3.1.3, p. 72;
Corollary 3.2.4, p. 76; Proposition 3.2.5, p. 79; Theorem 3.2.11, p. 85].) Let E be a vector bundle over a Lorentzian
manifold M. Here 𝒟 denotes smooth sections with compact support.

(1) Normally hyperbolic operators are those of [[def:std-normally-hyperbolic]] (Section 1.5).

(2) Theorem 3.1.1: "Let M be a connected timeoriented Lorentzian manifold such that (1) the causality condition holds,
i. e., there are no causal loops, (2) the relation '≤' is closed, (3) the time separation function τ is finite and
continuous on M × M. Let P be a normally hyperbolic operator acting on sections in a vector bundle E over M. Then any
distribution u ∈ 𝒟′(M, E) with past or future compact support solving the equation Pu = 0 must vanish identically on
M." By Remark 3.1.3 these assumptions "hold for convex Lorentzian manifolds and for globally hyperbolic manifolds".

(3) Corollary 3.2.4: "Let E be a vector bundle over a globally hyperbolic Lorentzian manifold M. Let ∇ be a connection
on E and let P = □^∇ + B be a normally hyperbolic operator acting on sections in E. Let S be a smooth spacelike Cauchy
hypersurface in M, and let n be the future directed (timelike) unit normal vector field along S. If u ∈ C^∞(M, E)
solves Pu = 0 on M, u = 0 along S, ∇_n u = 0 along S, then u = 0 on M."

(4) Proposition 3.2.5 (local solvability on RCCSV-domains). For each RCCSV-domain Ω ⊂ M such that S ∩ Ω is a
(spacelike) Cauchy hypersurface in Ω, and for each u0, u1 ∈ 𝒟(S ∩ Ω, E) and f ∈ 𝒟(Ω, E), "there exists a unique
u ∈ C^∞(Ω, E) satisfying Pu = f …, u = u0 along S, ∇_n u = u1 along S. Moreover, supp(u) ⊂ J^M(K) where
K = supp(u0) ∪ supp(u1) ∪ supp(f)."

(5) Theorem 3.2.11: "Let M be a globally hyperbolic Lorentzian manifold and let S ⊂ M be a spacelike Cauchy
hypersurface. Let n be the future directed timelike unit normal field along S. Let E be a vector bundle over M and let
P be a normally hyperbolic operator acting on sections in E. Then for each u0, u1 ∈ 𝒟(S, E) and for each f ∈ 𝒟(M, E)
there exists a unique u ∈ C^∞(M, E) satisfying Pu = f, u|_S = u0, and ∇_n u|_S = u1. Moreover, supp(u) ⊂ J^M(K) where
K = supp(u0) ∪ supp(u1) ∪ supp(f)."

In (4) and (5), ∇ is the connection on E with which [BGP, Section 3.2] poses the Cauchy problem. Globally hyperbolic
manifolds are connected, by [[thm:std-bgp-causal]] (1).

**Theorem {#thm:std-bgp-riesz}** ([BGP, Definition 1.2.1, p. 10; Lemma 1.2.2 (4), p. 11; Proposition 1.2.4, p. 13],
after [Rie49].) Let V be an n-dimensional Minkowski space, with ⟨x, y⟩ = −x₁y₁ + x₂y₂ + ⋯ + xₙyₙ and
γ(X) := −⟨X, X⟩. For Re α > n,

    R_±(α)(X) := C(α, n) γ(X)^((α−n)/2)  for X ∈ J_±(0),   R_±(α)(X) := 0  otherwise,

    C(α, n) := 2^(1−α) π^((2−n)/2) / ((α/2 − 1)! ((α − n)/2)!).

"The map α ↦ R_±(α) extends uniquely to ℂ as a holomorphic family of distributions". For all α ∈ ℂ: "(3)
□R_±(α + 2) = R_±(α)"; "(4) For every α ∈ ℂ ∖ ({0, −2, −4, …} ∪ {n − 2, n − 4, …}), we have supp(R_±(α)) = J_±(0)
and sing supp(R_±(α)) ⊂ C_±(0)"; "(7) R_±(0) = δ_0".

**Theorem {#thm:std-hormander-cauchy}** ([Hö85, Theorem 23.2.4] [[pending:literature-not-found]].) Let X be a manifold
with a time-oriented Lorentzian metric, globally hyperbolic, and let P be a second-order differential operator on a
vector bundle over X with smooth coefficients and principal symbol the dual metric times the identity. Let t be a time
function whose level sets are Cauchy hypersurfaces. For f ∈ H^(s−1)_loc(X) with supp f ⊂ {t ≥ t0} there is
u ∈ H^(s)_loc(X) with Pu = f and supp u ⊂ {t ≥ t0}.

### Quasilinear hyperbolic systems {#sec:std-hyperbolic}

The setting of [DS23] is the system "∂_t u + A^i(u) ∂_i u = R(u), u(0) = u0, i = 1, 2, …, N" (its (1.1), p. 1) on the
torus 𝕋^N, with A^i : ℝ × 𝕋^N × ℝ^m → ℝ^(m²), R : ℝ × 𝕋^N × ℝ^m → ℝ^m and "N(u)(t, x) = N(t, x, u(t, x)), N ∈ {A^i,
R}" (p. 2). H^r = H^r(𝕋^N), with norm ‖·‖_r, and "I = [−T, T] for some T > 0 and B(I) = C(I; C¹) ∩ C¹(I; C)" (p. 3).
For a non-empty open set U ⊂ ℝ^m, with closure Ū, the hypotheses are, on p. 3:

- (A1) "A^i ∈ C^∞(ℝ × 𝕋^N × Ū; ℝ^(m²)) satisfies that for any multi-indices k ∈ ℕ, α ∈ ℕ^n and β ∈ ℕ^m, there is a
  continuous increasing function f^i_(k,α,β) such that |∂^k_t ∂^α_x ∂^β_ζ A^i(t, x, ζ)| ≤ f^i_(k,α,β)(|ζ|)."
- (A2) The same for R ∈ C^∞(ℝ × 𝕋^N × Ū; ℝ^m), with continuous increasing functions h_(k,α,β).
- (A3) "For any ξ = (ξ_1, …, ξ_N) ∈ ℝ^N ∖ {0} and ζ ∈ Ū, the matrix A = A(t, x, ζ, ξ) = A^i(t, x, ζ) ξ_i is
  diagonalizable and has only real eigenvalues".
- (A4) "The distinct eigenvalues, λ_1 < λ_2 < ⋯ < λ_l, of A satisfy λ_i ∈ C^(1,0,1,0)(ℝ × 𝕋^N × Ū × (ℝ^N ∖ {0})) and
  the λ_i's do not meet each other on ℝ × 𝕋^N × Ū × (ℝ^N ∖ {0})".

The hypotheses do not require R(t, x, 0) = 0.

**Theorem {#thm:std-ds-existence}** ([DS23, Theorem 2.4, p. 4].) "Let r > N/2 + 1. Assume that (A1)-(A4) are satisfied
on some U ⊂ ℝ^m open. Then, for any u0 ∈ H^r with M̃ = dist(U^c, Im(u0)) > 0, there exists some T > 0 depending on
‖u0‖_r and M̃ such that (1.1) has a unique solution u ∈ B(I) on I = [−T, T]. Moreover, the solution satisfies u ∈ C(I;
H^r) ∩ C¹(I; H^(r−1)) (2.2)", together with the energy estimates (2.3)–(2.4) of [DS23], "and ⋃_(t∈I) Im(u(t)) ⊂ U
(2.5)."

**Theorem {#thm:std-ds-continuation}** ([DS23, Theorem 2.6, p. 5].) "Let r > N/2 + 1. Assume that (A1)-(A4) are
satisfied on some U ⊂ ℝ^m open. Given any I = [0, T] for some T > 0, if u ∈ B(I) satisfying (2.5) is a solution to
(1.1) with u0 ∈ H^r, then u satisfies (2.2) and (2.3). Let T* be the supremum times T such that there is a solution u ∈
B(I) to (1.1) on I = [0, T] satisfying (2.5). Then one and only one of the following statements holds. T* = ∞;
inf_(0≤t<T*) dist(U^c, Im u(t)) = 0; lim_(T→T*−) ‖u‖_(B([0,T])) = +∞. Similar results holds on [−T, 0]."

**Remark {#rem:std-ds-moser}** ([DS23, Remark 2.3 (i), p. 4].) In the setting above: "Based on (A1) and (A2),
following a standard argument, given any compact interval I ⊂ ℝ and s > N/2, it holds for any u ∈ H^s such that
‖N(u)‖_s ≤ C_I + F_I(‖u‖_∞) ‖u‖_s, N ∈ {A^i, R}; and given any k ∈ ℕ, it holds for any u ∈ C^k that
‖N(u)‖_(k,∞) ≤ F_I(‖u‖_∞) ‖u‖_(k,∞), N ∈ {A^i, R}." Here (p. 3) ℝ_+ = (0, ∞), and "F_I : ℝ_+ → ℝ_+ (C_I, resp.)
denotes a continuous increasing function (a positive constant, resp.) depending on the structure of A^i and R such that
F_(I_1) ≤ F_(I_2) (C_(I_1) ≤ C_(I_2), resp.) whenever I_1 ⊂ I_2."

**Theorem {#thm:std-ao-existence}** ([AO14, Theorem 1.1, p. 2, and Remark 1.2, p. 3].) The setting is the initial value
problem (p. 2)

    ∂_μ(A^μν(U) ∂_ν U) = F(U, ∂U) + χ_Ω H(U, ∂U)   in [0, T] × ℝⁿ,      (U, ∂_t U)|_(t=0) = (Ũ0, Ũ1)   in ℝⁿ,

"(1.1)–(1.2)", where "(i) Ω is a bounded open set in ℝⁿ with smooth boundary, (ii) U(x) = (U¹(x), …, U^N(x)) is vector
valued, (iii) A(U) = (A^μν(U)), F = (F^I(U, ∂U)) and H = (H^I(U, ∂U)) (I = 1, …, N) are smooth maps with F(0, 0) = 0,
and (iv) for some γ, κ > 0, A^μν(U) satisfies 1/γ |ξ|² ≤ A^ij(U) ξ_i ξ_j ≤ γ |ξ|² and A^00(U) ≤ −κ (1.3) for all (U,
ξ) ∈ ℝ^N × ℝⁿ", and χ_Ω is the indicator function of Ω. The compatibility conditions (1.5) require the time derivatives
of U at t = 0 generated from the data by the equation to lie in the spaces of [AO14, (1.5)]. "Theorem 1.1. Suppose n ≥
3, s ∈ ℤ_(>n/2) and (Ũ0, Ũ1) ∈ H^(s+1)(ℝⁿ) × H^s(ℝⁿ) satisfy the compatibility conditions (1.5). Then there exist a T >
0 and a map U ∈ CX^(s+1)_T(ℝⁿ) such that U is the unique solution in CX²_T(ℝⁿ) ∩ ⋂_(ℓ=0)^1 C^ℓ([0, T), W^(1−ℓ,∞)(ℝⁿ))
to the initial value problem (1.1)-(1.2). Moreover, if ‖u‖_(W^(1,∞)((0,T)×𝕋ⁿ)) < ∞, then there exists a T* > T such
that the u can be continued uniquely to a solution on [0, T*) × 𝕋ⁿ." In the continuation clause 𝕋ⁿ stands for ℝⁿ: the
proof of that clause, [AO14, Section 4.2, p. 22], assumes ‖U‖_(W^(1,∞)((0,T)×ℝⁿ)) ≤ K. By Remark 1.2 (i)(a) A, F and H
may "depend explicitly on x", and by Remark 1.2 (ii)(b) "Theorem 1.1 is also valid for quasi-linear wave equations
A^μν(U, ∂U) ∂_μ ∂_ν U = F(U, ∂U) + χ_Ω H(U, ∂U) in [0, T] × ℝⁿ, provided that we take s > n/2 + 1 and change the
continuation principle to that of bounding ‖U‖_(W^(2,∞)((0,T)×ℝⁿ))."

**Remark {#rem:std-iteration}** (The iteration bounded in a high norm and contracting in a low norm.) [AO14, Section 4.1,
p. 19]: "We establish existence and uniqueness of solutions using the well-known strategy, also used by Koch [12], of
setting up an appropriate iterative approximation scheme and showing convergence by establishing boundedness in a high
norm followed by contraction in a low norm." [AG22] names "the boundedness in the high norm and contraction in the low
norm" in its abstract, p. 1; in its Section 9, p. 24, (9.6) is the bound of the iterates in the high norm and (9.7)
the weakly convergent subsequence.

### The reduced Einstein equations and the gauge {#sec:std-gauge}

**Theorem {#thm:std-cbcm-reduced}** ([CBCM10, (2.7)–(2.9), p. 8].) In n + 1 dimensions, let ĝ be a background metric
with connection D̂ and Christoffel symbols Γ̂, and for a metric g put W^λ := g^(αβ) Γ̂^λ_(αβ) and H^λ := g^(αβ)
Γ^λ_(αβ) − W^λ = g^(αβ)(Γ^λ_(αβ) − Γ̂^λ_(αβ)) (2.7). Then

    "R_(αβ) = R^(H)_(αβ) + 1/2 (g_(αλ) D̂_β H^λ + g_(βλ) D̂_α H^λ)"   (2.8),
    "R^(H)_(αβ) = −1/2 g^(λμ) D̂_λ D̂_μ g_(αβ) + f̂[g, D̂g]_(αβ)"       (2.9),

with f̂ "independent of the second derivatives of g".

**Theorem {#thm:std-cbcl-harmonicity}** ([CBCL06, Section 3 and (3.1), p. 5; Section 5.1, p. 9].) "The vacuum Einstein
equations in wave coordinates on ℝ^(n+1) constitute a set of quasi-diagonal quasi-linear wave equations for the
components g_μν of the spacetime metric g, which we write symbolically as

    g^(αβ) ∂²g/∂x^α∂x^β = F(g)(∂g/∂x)²,      (3.1)

where the right-hand-side is a quadratic form in the first derivatives of the g's with coefficients polynomials in the
g's and their contravariant associates." "The spacetime manifold will be a subset V of ℝ^(n+1). The geometric initial
data on ℝⁿ are a metric ḡ and a symmetric 2-tensor K." In Section 3, p. 5: "We suppose also given on ℝⁿ the lapse N̄,
shift β̄ as well as their time derivatives, chosen so that the corresponding spacetime metric and its first derivatives
satisfy on ℝⁿ the harmonicity conditions F^μ = 0. If the initial data ḡ, K satisfy the constraints, a solution of the
Einstein equations in wave coordinates on V is such that the harmonicity functions F^μ := □_g x^μ satisfy an
homogeneous linear system of wave equations on (V, g), with also ∂_t F^μ = 0, hence F^μ = 0 if (V, g) is globally
hyperbolic." In Section 5.1, p. 9, the initial data (ḡ, K) are given "on a manifold ℝⁿ embedded as a submanifold
M_x := {x⁰ = 2λ} of ℝ^(n+1)_x", and: "We suppose these initial data satisfy the Einstein constraints, and we choose the
initial lapse and shift so that the harmonicity conditions are everywhere initially zero. Any globally hyperbolic
solution (V_x ⊂ ℝ^(n+1)_x, g) of the Einstein equations in wave coordinates taking these initial data is then a
solution of the full Einstein equations. Such a solution exists if the initial data belong to H^loc_(s+1) × H^loc_s,
s > n/2."

**Theorem {#thm:std-lr-propagation}** ([LR05, (1.3), p. 2; Section 2.2, p. 8].) In 3 + 1 dimensions and wave coordinates
the reduced Einstein–scalar field equations are "□̃_g g_μν = F_μν(g)(∂g, ∂g) + 2 ∂_μψ ∂_νψ, □̃_g ψ = 0" (1.3), with
□̃_g := g^(αβ) ∂_α ∂_β; their vacuum case is ψ = 0. With the gauge's data (2.3)–(2.5), p. 8: "any solution of the system
(2.1) with initial data … compatible with (2.2) and constraint equations, gives rise to a solution of the full Einstein
system. In addition, thus constructed tensor g_μν will satisfy the wave coordinate condition (2.2) for all times." For
the verification [LR05, p. 8] refers to Wald: "Verification of the above statements is straightforward and can be found
in e.g. [Wa]."

**Theorem {#thm:std-hin26a-cform}** ([Hin26a, Proposition 5.1, p. 38].) "Fix any v ∈ (0, 1) and C0 > 0. Fix moreover
α_sf, α_K ∈ ℝ subject to the conditions α_sf < −1/2 and α_K > α_sf + 1/2. Set ρ_sf = r⁻¹ and ρ_K = r/t; put
w := ρ_sf^(α_sf+1) ρ_K^(α_K) and w′ := ρ_sf^(α_sf+1). Then for all sufficiently small e > 0, there exists a 1-form
c ∈ ρ_sf C^∞(M; T*) satisfying the following properties for some r0 > 100m, 0 < δ_r < (4r0)⁻¹, and δ_sf > 0:
- (1) (Basic properties.) c is stationary, i.e., ℒ_(∂_t) c = 0 … Moreover, rc ∈ C^∞(M; T*) is past timelike and
  nowhere vanishing.
- (2) (Explicit regions.) We have c = (1/2) r0^(−2) (r0 dt − v(r − r0) dr) for r0/2 ≤ r ≤ 2r0 (5.1), and
  c = r⁻¹ (dt − v dr) for r ≥ 3r0 (5.2).
- (3) (Interior saddle point …) The endomorphism S_(g,c,e) from Lemma 3.9 is positive definite (with respect to the
  inner product B_(g,c,e) on T* from Lemma 3.3) at all points with |r − r0| ≤ (5/6) r0 √(e/v).
- (4) (Saddle point at ∂𝒦⁺ …) For ρ_sf ≤ 2δ_r and ρ_K ≤ 2δ_r, the endomorphism r²(−ℓ_(g,c,e)(dw/w) + S_(g,c,e)) is
  positive definite.
- (5) (Sink in sf° …) At points where r/t/v ∈ [1 − 2δ_sf, 1 + 2δ_sf] and r⁻¹ ≤ 2δ_r, the endomorphism
  r²(−ℓ_(g,c,e)(dw′/w′) + S_(g,c,e)) is positive definite.
- (6) (Positivity along escape functions …) For m ≤ r ≤ r0 − r0√(e/v), −ℓ_(g,c,e)(−dr) is positive definite. For
  r0 + r0√(e/v) ≤ r < ∞, −ℓ_(g,c,e)(dr) is positive definite. On sf ∩ {r/t ∈ [δ_r, v(1 − δ_sf)]},
  −r² ℓ_(g,c,e)(d(r/t)) is positive definite, and on sf ∩ {r/t ∈ [v(1 + δ_sf), 10]}, −r² ℓ_(g,c,e)(−d(r/t)) is
  positive definite."

The objects S_(g,c,e), B_(g,c,e) and ℓ_(g,c,e) are those of [Hin26a, Lemmas 3.3 and 3.9], and r/t/v in (5) is (r/t)/v.

### The constraint equations {#sec:std-constraints}

**Theorem {#thm:std-cd-constraints}** ([CD03, (2.1)–(2.2), p. 4].) "Initial data (g, K) for the vacuum Einstein
equations belong to the zero level set of the constraints map:

    (J, ρ)(K, g) := (2(−∇^j K_ij + ∇_i tr K), R(g) − |K|² + (tr K)²) = (0, 0).   (2.1)

These are the general relativistic constraint equations whatever the space-dimension n." With h = δg and Q = δK, "the
linearisation of the constraints map at (K, g) reads"

    P(Q, h) = ( −K^pq ∇_i h_pq + K^q_i (2∇^j h_qj − ∇_q h^l_l) − 2∇^j Q_ij + 2∇_i tr Q − 2(∇_i K^pq − ∇^q K^p_i) h_pq ,
                −Δ(tr h) + div div h − ⟨h, Ric(g)⟩ + 2 K^pl K^q_l h_pq − 2⟨K, Q⟩ + 2 tr K (−⟨h, K⟩ + tr Q) ).   (2.2)

**Remark {#rem:std-racz}** ([Rac16, (3.3), p. 6; (4.7), p. 8].) Rácz foliates the initial slice by codimension-one
surfaces with a transverse coordinate ρ. The momentum constraint becomes the first-order system (3.3) for the mixed
and trace parts (k_B, K^E_E) of the second fundamental form, with ρ as the evolution parameter, and he observes:
"Notice that the coefficients of ∂_ρ and ∂_K are symmetric, and that the coefficient of ∂_ρ is also positive definite",
K = 2, …, n being an index of coordinates on the leaves. The Hamiltonian constraint becomes a parabolic equation for the
lapse of the foliation, (4.7).

**Theorem {#thm:std-racz-hyperbolic}** ([Rac16, Lemma 4.1, p. 12; Theorem 4.3, p. 14].) In the notation of [Rac16,
Sections 3–4]: the slice Σ is foliated by the level surfaces S_ρ; κ is given algebraically by (4.17); and (4.16) and
(3.2) are the evolution equations for (k_i, K^l_l) in ρ.

Lemma 4.1: "Assume that κ · K^l_l < 0 holds in a subset of Σ. Then equations (4.16) and (3.2) comprise a first order
symmetrizable hyperbolic system there."

Theorem 4.3: "Assume that the freely specifiable part of data N̂, N̂^i, γ̂_ij; K̊_ij; e, p_i (4.28) on Σ, and the
initial data (₀k_i, ₀K^l_l) for the system (4.16) and (3.2) on a ρ = ρ0 level surface are chosen such that they are all
smooth on their respective domains, and that the system comprised by (4.16) and (3.2) can be guaranteed to be
symmetrizable hyperbolic in a sufficiently small neighborhood of S_ρ0 in Σ … Then, there exists a unique smooth (local)
solution (k_i, K^l_l) to (4.16) and (3.2) such that k_i|_(S_ρ0) = ₀k_i, K^l_l|_(S_ρ0) = ₀K^l_l. This solution, along
with the freely specifiable data (4.28), uniquely determines κ via (4.17). The fields h_ij and K_ij which can be built
up from the solution to (4.16), (3.2) and (4.17) and from the freely specifiable part of the data do satisfy the full
constraint system (1.1)–(1.2) in the domain of dependence of S_ρ0 in Σ."

**Theorem {#thm:std-cd-isomorphism}** ([CD03, Theorem 3.6, p. 13].) "Let k ≥ 0, g0 ∈ W^(k+4,∞)_loc, suppose that (A.2)
holds with 0 ≤ i ≤ 4 + k, that Ric(g0) ∈ φ^(−2) W^(k+2,∞)_φ(g0), K0 ∈ φ^(−1) W^(k+3,∞)_φ(g0), and that the weights φ
and ψ have the scaling property … If there exists a compact set 𝒦 ⊂ M such that for all H̊¹_(φ,ψ)(g0) vector fields Y
and H̊²_(φ,ψ)(g0) functions N, both supported in M ∖ 𝒦, the inequality (3.4) holds, then for all (K, g) close to
(K0, g0) in φ^(−1) W^(k+3,∞)_φ(g0) × W^(k+4,∞)_φ(g0) norm, the map

    π_(𝒦0^(⊥g)) L_(φ,ψ) : 𝒦0^(⊥g) ∩ (H̊^(k+3)_(φ,ψ)(g) × H̊^(k+4)_(φ,ψ)(g))
                         → 𝒦0^(⊥g) ∩ (H̊^(k+1)_(φ,ψ)(g) × H̊^k_(φ,ψ)(g))

is an isomorphism such that the norm of its inverse is bounded independently of (K, g)." Condition (A.2), inequality
(3.4), the scaling property and the operator L_(φ,ψ) are those of [CD03, Section 3 and Appendix A]. 𝒦0 is the kernel
of P* at (K0, g0), with (J, ρ) and P as in [[thm:std-cd-constraints]].

**Theorem {#thm:std-cd-bijective}** ([CD03, Theorem 3.9, p. 14].) "Under the hypotheses of Theorem 3.6, if the map

    (Y, N) ↦ π_(𝒦0^(⊥g)) ψ^(−2) [(J, ρ)((K, g) + ψ² Φ² P*(Y, N)) − (J, ρ)(K, g)]      (3.13)

[from 𝒦0^(⊥g) ∩ (H̊^(k+3)_(φ,ψ)(g) × H̊^(k+4)_(φ,ψ)(g)) to 𝒦0^(⊥g) ∩ (H̊^(k+1)_(φ,ψ)(g) × H̊^k_(φ,ψ)(g))] is
differentiable in a neighborhood of zero, then it is bijective in a (perhaps smaller) neighborhood of zero." The
theorem then states the solvability of (3.14) for small (δJ, δρ). Theorem 3.6 is [[thm:std-cd-isomorphism]].

**Theorem {#thm:std-cd-uniform-inverse}** ([CD03, Proposition G.1, pp. 77–78].) "Let (V_x, ‖·‖_(V_x))_(x∈A) and
(W_x, ‖·‖_(W_x))_(x∈A) be two families of Banach spaces. Let r > 0 and let {f_x : B_(V_x)(0, r) → W_x}_(x∈A) be a
family of differentiable functions such that:
1. Df_x(0) : V_x → W_x has a right inverse for all x ∈ A which is bounded independently of x ∈ A.
2. ‖f_x(v + h) − f_x(v) − Df_x(v)h‖_(W_x)/‖h‖²_(V_x) is bounded independently of x ∈ A, v ∈ B_(V_x)(0, r) and h ∈ V
   such that v + h ∈ B_(V_x)(0, r).
3. ‖Df_x(v + h) − Df_x(v)‖_(L(V_x,W_x))/‖h‖_(V_x) is bounded independently of x ∈ A, v ∈ B_(V_x)(0, r) and h ∈ V
   such that v + h ∈ B_(V_x)(0, r).

Then there exists ε > 0 and C > 0 such that for all x ∈ A and all δf ∈ W_x, ‖δf‖_(W_x) < ε, there exists a solution
δx ∈ V_x of the equation f_x(δx) − f_x(0) = δf, which satisfies ‖δx‖_(V_x) ≤ C ‖δf‖_(W_x)."

**Theorem {#thm:std-cd-exponential}** ([CD03, Theorem 5.9, p. 25; Proposition 5.10, p. 26; Corollary 5.11, p. 27].)
Theorem 5.9: "Let M be a compact manifold with boundary, let s > 0, k > n/2 and suppose that g0 is a metric on M which
has (W^(k+4,∞)_(x²), k + 4)–behavior at ∂M, with

    x⁴ |Ric(g0)|_(g0) → 0,   x |∇∇x|_(g0) → 0,   K0 ∈ x^(−2) W^(k+3,∞)_(x²)(g0),   x² |K0|_(g0) + x⁴ |∇K0|_(g0) → 0

as x → 0 ((5.10a–c)). There exists ε > 0 such that for all (K, g) in x^(−2) W^(k+3,∞)_(x²)(g0) × W^(k+4,∞)_(x²)(g0)
for which ‖(K − K0, g − g0)‖ < ε, and for all pairs (δJ, δρ) ∈ H^(k+1)_(x²,e^(s/x))(g) × H^k_(x²,e^(s/x))(g)
satisfying ‖(δJ, δρ)‖ < ε, there exists a solution (δK, δg) = e^(−2s/x) Φ² P*(Y, N) ∈
x² H^(k+2)_(x²,e^(s/x))(g) × x⁴ H^(k+2)_(x²,e^(s/x))(g), close to zero, of the equation

    π_(𝒦0^(⊥g)) e^(2s/x) [(J, ρ)(K + δK, g + δg) − (J, ρ)(K, g)] = π_(𝒦0^(⊥g)) e^(2s/x) (δJ, δρ)."      (5.11)

Proposition 5.10 (p. 26) and Corollary 5.11 (p. 27): let k ≥ k0 := ⌊n/2⌋ + 1 and let g0 have
(C^(k+4,α)_(x²,1), k + 5)–behaviour at ∂M, with (5.10). "If (δJ, δρ) ∈ C^∞_(x²,e^(s/x))(g) × C^∞_(x²,e^(s/x))(g), and
if (K, g) ∈ C^∞(M) × C^∞(M), then the solution given by Theorem 5.9 is in
x² C^∞_(x²,e^(s/x))(g) × x⁴ C^∞_(x²,e^(s/x))(g) ⊂ C^∞(M) × C^∞(M). In fact (δK, δg) can be smoothly extended by zero
across ∂M."

**Theorem {#thm:std-cd-compact}** ([CD03, Theorems 5.4 and 5.6, pp. 23–24; p. 33].) Theorem 5.4: let M be a compact
manifold with boundary and k ≥ 0, and let g0 have (W^(k+4,∞)_x, k + 4)–behaviour at ∂M with x²|Ric(g0)| → 0,
x|∇∇x| → 0, K0 ∈ x^(−1) W^(k+3,∞)_x(g0) and x|K0| + x²|∇K0| → 0 ((5.4a–c)). "Then for all s ≠ (n − 1)/2, (n − 3)/2
and all (K, g) close to (K0, g0) … the map π_(𝒦0^(⊥g)) L_(x,x^(s−n/2)) … is an isomorphism such that the norm of its
inverse does not depend on (K, g)."

Theorem 5.6: "Under the hypotheses of Theorem 5.4 with s ≥ n − 2, s > 1 if n = 3, k > n/2", the map (5.7) "is
bijective in a neighborhood of zero". There is ε > 0 such that for all (K, g) with ‖(K − K0, g − g0)‖ < ε and for all
(δJ, δρ) ∈ H̊^(s−n)_(k+1)(g) × H̊^(s−n)_k(g) with norm < ε, "there exists a solution (δK, δg) = x^(2s−n) Φ² P*(Y, N) ∈
H̊^(s−n+1)_(k+2)(g) × H̊^(s−n+2)_(k+2)(g), close to zero, of the equation π_(𝒦0^(⊥g)) x^(−2s+n) [(J, ρ)(K + δK, g + δg)
− (J, ρ)(K, g)] = π_(𝒦0^(⊥g)) x^(−2s+n) (δJ, δρ)" (5.8).

On p. 33: "Elements in the kernel of P* are called Killing initial data (KIDs). Existence of non-zero KIDs implies
existence of non-zero Killing vectors in the associated vacuum space-time."

The constraint map (J, ρ) and its linearisation P are those of [[thm:std-cd-constraints]]. The theorems hold for every
space dimension n.

**Theorem {#thm:std-corvino-schoen}** ([CS06, Theorem 2, p. 13].) "Let Ω ⊂ M³ be a compactly contained
C^(k+2)-domain, and let g0 be a C^(k+4,α)-metric and π0 a C^(k+3,α)-symmetric (2,0)-tensor. Suppose that the
linearization DΦ_(g0,π0) of the constraint map Φ : C^(k+2,α)(Ω) × S^(k+2,α)_(2,0)(Ω) → C^(k,α)(Ω) × X^(k+1,α)(Ω) has
an injective formal L²-adjoint DΦ*_(g0,π0) at (g0, π0), where we can consider DΦ*_(g0,π0) : H^(2,1)_loc(Ω) →
L²_loc(Ω). Then for a sufficiently decaying weight ρ, there is an ε > 0 such that for any function v ∈ C^(k,α)(Ω) and
any vector field W ∈ X^(k+1,α)(Ω) for which (v, W) − Φ(g0, π0) ∈ C^(k,α)_(ρ⁻¹)(Ω) × X^(k+1,α)_(ρ⁻¹)(Ω) with the
support of (v, W) − Φ(g0, π0) contained in Ω and with ‖(v, W) − Φ(g0, π0)‖_(C^(k,α)_(ρ⁻¹) × X^(k+1,α)_(ρ⁻¹)) < ε,
there is a C^(k+2,α)-metric g and a C^(k+2,α)-symmetric tensor π on M with Φ(g, π) = (v, W) in Ω and
(g, π) = (g0, π0) outside Ω. Moreover, (g, π) depends continuously on (v, W). If in addition (v, W) − Φ(g0, π0) ∈
C_c^∞(Ω), (g0, π0) and ∂Ω are smooth, and we use an exponential weight, then we can solve for (g, π) smooth. If the
adjoint of the linearization has nontrivial kernel, then the analogous theorem holds for solving Φ(g, π) = (v, W) up to
a finite-dimensional error." Here M³ is a three-manifold, and the constraint map Φ, the weight ρ and the weighted
spaces are those of [CS06].

### The characteristic initial value problem {#sec:std-characteristic}

**Theorem {#thm:std-wu-characteristic}** ([Wu26, Theorem 2.1, p. 6].) The setting is that of [Wu26]: the Einstein
vacuum equations in 3 + 1 dimensions, sections S², and the gauge (1.1). "Given initial null hypersurface H0, H̲0 and
regular initial metric (g, Ω, b) on it, we define χ_AB = (1/2) ℒ_(e4) g_AB on H0 and χ̲_AB = (1/2) ℒ_(e3) g_AB on H̲0.
Let ζ be a vector field on H0 ∩ H̲0. Suppose

    e4(tr χ) + |χ|² + 2ω tr χ = 0,    e3(tr χ̲) + |χ̲|² + 2ω̲ tr χ̲ = 0

hold on H0, H̲0 respectively, then there is a future open neighborhood of H0 ∪ H̲0 and metric (g, b, Ω) on it solving
the Einstein vacuum equations and extending the initial data (g, Ω, b) and ζ."

**Theorem {#thm:std-ctg-neighbourhood}** ([CTG23, Theorem 1.1, pp. 2–3].) "The maximal globally hyperbolic development
of smooth initial data for vacuum Einstein equations with a (possibly zero) cosmological constant Λ ∈ ℝ, on two
characteristic hypersurfaces intersecting transversally, contains a future neighborhood of the initial data
hypersurfaces." The theorem holds in every spacetime dimension. The authors add that "the result remains true in
suitable Sobolev spaces" (p. 3).

### Higher-dimensional black holes {#sec:std-black-holes}

**Theorem {#thm:std-myers-perry}** ([ER08, (14)–(16), p. 10; (31)–(34), p. 14; (42)–(45), p. 16], after [MP86].) The
Myers–Perry black holes are vacuum solutions in every dimension d > 4 [MP86]. In Emparan and Reall's words, "the
solutions belong in the Kerr-Schild class

    g_μν = η_μν + 2H(x^ρ) k_μ k_ν      (31)

where k_μ is a null vector with respect to both g_μν and the Minkowski metric η_μν … Of all known vacuum black holes in
d > 4, only the Myers-Perry solutions seem to have this property" (p. 14).

For odd d, with N = (d − 1)/2 rotation planes, the general solution is

    ds² = −dt² + (r² + a_i²)(dμ_i² + μ_i² dφ_i²) + (μr²/(ΠF)) (dt − a_i μ_i² dφ_i)² + (ΠF/(Π − μr²)) dr²      (42)

summed over i = 1, …, N, with Σ μ_i² = 1 and

    F(r, μ_i) = 1 − Σ a_i² μ_i²/(r² + a_i²),    Π(r) = Π_(i=1)^N (r² + a_i²)      (44).

"The event horizon is again at the largest real root of g^(rr)", which for odd d is Π(r0) − μ r0² = 0 (45). "The
relation between μ and a_i and the mass and angular momenta is the same as (34)":

    M = (d − 2) Ω_(d−2) μ/(16πG),    J = 2Ma/(d − 2).      (34)

Here Ω_(d−2) = 2π^((d−1)/2)/Γ((d − 1)/2). The linearised field of a mass M with angular momentum J_ij is (14)–(16).

**Theorem {#thm:std-ki-master}** ([KI03, (2.7)–(2.8), p. 5; (2.14)–(2.16), p. 6; (3.1)–(3.10), pp. 8–9;
(3.11)–(3.14), pp. 9–10; (5.1)–(5.6), p. 13; (5.7)–(5.15), p. 14; (5.16), p. 15].) The background is

    ds² = −f(r) dt² + dr²/f(r) + r² dσ_n²,    f(r) = K − 2M/r^(n−1) − λr²,    λ = 2Λ/(n(n + 1))      (2.14)–(2.16),

with dσ_n² of constant curvature K. □ and D are the d'Alembertian and covariant derivative of the two-dimensional
orbit space with coordinates (t, r).

(1) Tensor type (p. 13). For harmonics T_ij with (Δ̂_n + k_T²) T_ij = 0, T^i_i = 0, D̂_j T^j_i = 0, and
k_T² = l(l + n − 1) − 2 for K = 1 (5.2): "H_T is gauge-invariant by itself, and in vacuum, it satisfies"

    □H_T + (n/r) Dr · DH_T − ((k_T² + 2K)/r²) H_T = 0.      (5.3)

With Φ = r^(n/2) H_T (5.4), this is □Φ − (V_T/f)Φ = 0 (5.5), where

    V_T(r) = (f/r²) [k_T² + 2K + n(n − 2)K/4 − n(n + 2)λr²/4 + n²M/(2r^(n−1))].      (5.6)

(2) Vector type (p. 14). Here k_V² = l(l + n − 1) − 1 (5.8) and V_ij = −(D̂_i V_j + D̂_j V_i)/(2k_V) (5.9). "For
k² > (n − 1)K,

    F_a = f_a + (r/k_V) D_a H_T      (5.10)

is gauge invariant". In vacuum r^(n−1) F^a = ε^(ab) D_b Ω (5.12), with □Ω − (n/r) Dr · DΩ − ((k_V² − (n − 1)K)/r²) Ω
= 0 (5.11). With Φ = r^(−n/2) Ω (5.13) this is □Φ − (V_V/f)Φ = 0 (5.14), where

    V_V(r) = (f/r²) [k_V² + K + n(n − 2)K/4 − n(n − 2)λr²/4 − 3n²M/(2r^(n−1))].      (5.15)

For l = 1, F_ab = r D_a(f_b/r) − r D_b(f_a/r) (5.16).

(3) Scalar type (pp. 5–10). For k²(k² − nK) ≠ 0 the gauge-invariant variables are

    F = H_L + H_T/n + (1/r) D^a r X_a,   F_ab = f_ab + D_a X_b + D_b X_a,   X_a = (r/k)(f_a + (r/k) D_a H_T)
    ((2.7)–(2.8)).

In terms of X, Y, Z of (2.20) and Z = iωZ̃,

    Φ := (nZ̃ − r(X + Y))/(r^(n/2−1) H),   H = m + n(n + 1)x/2,   m = k² − nK,   x = 2M/r^(n−1)      (3.1)–(3.4),

and (2.24) reduces to

    −f d/dr (f dΦ/dr) + V_S Φ = ω² Φ,    V_S = f Q/(16 r² H²)      (3.5)–(3.6).

With y = λr² (3.8), Q is

    Q(r) = [−n³(n + 2)(n + 1)² x² − 12n²(n + 1)(n − 2) m x + 4(n − 2)(n − 4) m²] y + n⁴(n + 1)² x³
           + n(n + 1)[4(2n² − 3n + 4)m + n(n − 2)(n − 4)(n + 1)K] x²
           − 12n[(n − 4)m + n(n + 1)(n − 2)K] m x + 16m³ + 4Kn(n + 2)m².      (3.7)

The original variables are expressed through Φ by (3.9)–(3.10). In the time domain the equation is □Φ − (V_S/f)Φ = 0
(3.11), and the gauge invariants are given covariantly by (3.12)–(3.14).

**Theorem {#thm:std-hkw-decay}** ([HKW18, Theorem 2, p. 4; (19)–(20), p. 6; Lemma 11 and Theorem 12 (116), p. 39;
Theorem 18 (130), p. 47].) Let δg be a smooth, symmetric two-tensor on a Schwarzschild–Tangherlini spacetime with orbit
spheres of dimension n, satisfying the linearised Einstein equation. Then [HKW18, Theorem 2]: "there exist
gauge-invariant master quantities satisfying decoupled Regge-Wheeler type equations (134, 149, 153, 174) for the
scalar, co-vector, and two-tensor portions of δg_(ℓ≥2). With further specification of an initial data slice Σ0 and a
decay foliation Σ_τ := φ_τ(Σ0) formed by flowing along the static Killing vector field, a symmetric traceless
two-tensor Ψ solving any one of the equations (134, 149, 153, 174) satisfies the uniform boundedness estimate

    Ě^N_Ψ(Σ_τ) ≤ C(n, M) Ě^N_Ψ(Σ0),      (6)

and, in spacetime dimension six and below, the uniform decay estimate

    Ě^N_Ψ(Σ_τ) ≤ C(n, M) I_Ψ(Σ0)/τ²,      (7)

with Ě^N_Ψ and I_Ψ(Σ0) representing Sobolev data for Ψ on members of the decay foliation Σ_τ and C(n, M) being a
universal constant depending upon the orbit sphere dimension n and the background mass M."

The energies are those of [HKW18, Section 7]: the red-shift energy Ě^N_Ψ is comparable to E^N_Ψ by Lemma 11 (p. 39);
the bounds (6)–(7) are Theorem 12, (116), p. 39, and Theorem 18, (130), p. 47; and I_Ψ(Σ0) is defined after (130). The
horizon is r = r_h := (2M)^(1/(n−1)) (19), and "along the event horizon, the Schwarzschild-Tangherlini solution has
positive surface gravity κ_n := (n − 1)/(2r_h)" (20).

### Function spaces {#sec:std-function-spaces}

In [BH17], s ∈ ℝ and p ∈ (1, ∞) throughout unless stated otherwise (p. 1).

**Theorem {#thm:std-bh-extension}** ([BH17, Theorem 7.21, p. 55].) "Let Ω ⊂ ℝⁿ be a bounded open set with Lipschitz
continuous boundary. Then for all s > 0 and for 1 ≤ p < ∞, there exists a continuous linear extension operator P :
W^(s,p)(Ω) ↪ W^(s,p)(ℝⁿ) such that (Pu)|_Ω = u and ‖Pu‖_(W^(s,p)(ℝⁿ)) ≤ C ‖u‖_(W^(s,p)(Ω)) for some constant C that may
depend on s, p, and Ω but is independent of u." The spaces are the Sobolev–Slobodeckij spaces of [BH17, Definitions 7.1
and 7.11].

**Theorem {#thm:std-bh-embedding}** ([BH17, Theorem 7.26, p. 55].) "Let Ω be a nonempty bounded open subset of ℝⁿ with
Lipschitz continuous boundary or Ω = ℝⁿ. If sp > n, then W^(s,p)(Ω) ↪ L^∞(Ω) ∩ C⁰(Ω) and W^(s,p)(Ω) is a Banach
algebra."

**Theorem {#thm:std-bh-manifold}** ([BH17, Theorem 9.14, p. 85].) "Let Mⁿ be a compact smooth manifold. Let π : E → M be
a smooth vector bundle of rank r over M equipped with fiber metric ⟨·, ·⟩_E (so it is meaningful to talk about
L^∞(M, E)). Suppose s ∈ ℝ and p ∈ (1, ∞) are such that sp > n. Then W^(s,p)(M, E) ↪ L^∞(M, E). Moreover, every element
u in W^(s,p)(M, E) has a continuous version."

**Theorem {#thm:std-moser-taylor}** ([Tay11, Chapter 13, Propositions 3.6–3.7] [[pending:literature-not-found]].) Moser
estimates for products in Sobolev spaces: for s ≥ 0,

    ‖fg‖_(H^s) ≤ C (‖f‖_(L^∞) ‖g‖_(H^s) + ‖f‖_(H^s) ‖g‖_(L^∞)),

in the form needed on uniformly local Sobolev spaces of ℝ² × 𝕊³.

**Theorem {#thm:std-kato-ponce}** ([GO13, p. 1].) Grafakos and Oh recall the commutator estimate of Kato and Ponce
(T. Kato, G. Ponce, Comm. Pure Appl. Math. 41 (1988) 891–907): with J^s := (1 − Δ)^(s/2) on ℝⁿ, for Schwartz functions
f and g,

    ‖J^s(f g) − f (J^s g)‖_(L^p) ≤ C [‖∇f‖_(L^∞) ‖J^(s−1) g‖_(L^p) + ‖J^s f‖_(L^p) ‖g‖_(L^∞)]

"for 1 < p < ∞ and s > 0", with C a constant depending on n, p and s.

**Corollary {#cor:std-kato-ponce}** (Kato–Ponce for compactly supported functions.) Let s > 0, and let f, g be compactly
supported on ℝⁿ with ∇f ∈ L^∞, J^s f ∈ L², g ∈ L^∞ and J^(s−1) g ∈ L². Then J^s(f g) − f (J^s g) ∈ L² and the
inequality of [[thm:std-kato-ponce]] holds for p = 2 with the same constant.

*Proof.* Let ρ_ε be a standard mollifier and f_ε := ρ_ε ∗ f, g_ε := ρ_ε ∗ g, smooth with compact support, hence
Schwartz functions. Convolution with ρ_ε is a Fourier multiplier of norm at most 1 on L² and on L^∞ and commutes with
J^σ and ∇, so the right side of the inequality for (f_ε, g_ε) is at most the right side for (f, g). As ε → 0, f_ε → f
uniformly, ∇f_ε → ∇f in L², g_ε → g and J^(s−1) g_ε → J^(s−1) g in L². Hence f_ε g_ε → f g in L² and J^s(f_ε g_ε) →
J^s(f g) as tempered distributions. For a test function φ, ⟨f_ε J^s g_ε, φ⟩ = ⟨J^(s−1) g_ε, J(f_ε φ)⟩, and f_ε φ → f φ
in H¹, so J(f_ε φ) → J(f φ) in L² by Plancherel; thus f_ε J^s g_ε → f J^s g as distributions. The left sides for
(f_ε, g_ε) are bounded in L² and converge as distributions; a subsequence converges weakly in L², its limit is J^s(f g)
− f (J^s g), and its norm is at most the limit inferior of the norms. ∎

**Theorem {#thm:std-seeley}** ([See64, Theorem, p. 625].) For x ∈ ℝⁿ and t ∈ ℝ, let S₊ = ℝⁿ × {t > 0} and
"D₊ = {f : f ∈ C^∞(S₊), f and all its derivatives have continuous limits as t → 0+}". D₊ "has the topology of uniform
convergence of each derivative on compact subsets of the closure of S₊ in ℝ^(n+1), and C^∞(ℝ^(n+1)) has a corresponding
topology". "There is a continuous linear extension operator E : D₊ → C^∞(ℝ^(n+1)) such that Ef(x, t) = f(x, t) for
t > 0."

**Theorem {#thm:std-ly-extension}** ([LY22, Theorem 1, pp. 1–2; Theorem 26 and Lemma 27, p. 16].) Theorem 1: "(i)
There exists an extension operator E : C⁰(ℝ̄ⁿ_+) → C⁰(ℝⁿ) that has the form

    Ef(x′, xₙ) = Σ_(j=−∞)^∞ a_j f(x′, −b_j xₙ)  for xₙ < 0,    Ef(x) = f(x)  for xₙ > 0,      (2)

where b_j > 0 such that, for every k ∈ ℤ, Σ_(j=−∞)^∞ a_j (−b_j)^k = 1 and Σ_(j∈ℤ) 2^(δ_k|j|) |a_j| b_j^k < ∞ for some
δ_k > 0 (3). Moreover, when (3) is satisfied, then (2) always defines an extension operator E for functions on ℝⁿ_+,
that has the following boundedness (simultaneously): (ii) … E : W^(k,p)(ℝⁿ_+) → W^(k,p)(ℝⁿ) and
E : C^(k,s)(ℝⁿ_+) → C^(k,s)(ℝⁿ) are defined and bounded for all k ∈ ℤ, 0 < p ≤ ∞ and 0 < s < 1.
E : C^k(ℝⁿ_+) → C^k(ℝⁿ) is bounded for all k = 0, 1, 2, …", one operator for all these spaces at once; its items
(iii)–(iv) give the same for Besov, Triebel–Lizorkin and Morrey-type spaces. Of Seeley's operator
([[thm:std-seeley]]) [LY22, p. 1] records that it satisfies "E : C^k(ℝⁿ_+) → C^k(ℝⁿ) for all k = 0, 1, 2, …. In
particular Seeley's extension [preserves] C^∞-smoothness". Theorem 26: "Let Ω ⊂ ℝⁿ be a bounded smooth domain with a
smooth defining function σ, and let U ⊂ ℝⁿ be a bounded neighborhood of Ω̄. Then there exists an extension operator
E : 𝒮′(Ω) → ℰ′(U) that maps extendable distributions in Ω … to compactly supported distributions in U, such that …
(ii) (Universal boundedness) E : W^(k,p)(Ω) → W^(k,p)_c(U) and E : C^(k,s)(Ω) → C^(k,s)_c(U) are defined and bounded
for all k ∈ ℤ, 0 < p ≤ ∞ and 0 < s < 1. In particular E : C^k(Ω) → C^k_c(U) for k ≥ 0." Lemma 27: "Let Φ : ℝⁿ → ℝⁿ be
a bounded diffeomorphism, i.e. Φ is bijective and sup_(x∈ℝⁿ) |∂^α Φ(x)| + |∂^α(Φ⁻¹)(x)| < ∞, ∀ α ∈ ℕⁿ_0 ∖ {0}. Let
χ ∈ C_c^∞(ℝⁿ) be a bounded smooth function. Define a linear map T f := (χ · f) ∘ Φ. (i) T : W^(k,p)(ℝⁿ) → W^(k,p)(ℝⁿ),
T : C^(k,s)(ℝⁿ) → C^(k,s)(ℝⁿ) are both defined and bounded for all k ∈ ℤ, 0 < p ≤ ∞ and 0 < s < 1. In particular
T : C^k(ℝⁿ) → C^k(ℝⁿ) for k ∈ ℕ₀."

**Theorem {#thm:std-sy-extension}** ([SY21, Section 1, p. 2; Section 2.1, p. 6].) After Rychkov (p. 2): "for a
Lipschitz domain Ω there exists an operator E = E_Ω that is bounded on Besov spaces E : B^s_pq(Ω) → B^s_pq(ℝⁿ) for all
0 < p, q ≤ ∞, s ∈ ℝ and on Triebel-Lizorkin spaces E : F^s_pq(Ω) → F^s_pq(ℝⁿ) for all 0 < p < ∞, 0 < q ≤ ∞, s ∈ ℝ.
Since E is one single operator which works for all such spaces, we call it an universal extension operator on Ω".
After Stein (p. 6), Ω being a bounded Lipschitz domain and W^(k,p)(Ω) defined in the classical way: Stein "used an
alternative approach to construct an extension operator E^S which is independent of k, such that
E^S : W^(k,p)(Ω) → W^(k,p)(ℝⁿ) is bounded for all k ∈ ℕ and 1 ≤ p ≤ ∞".

### Microlocal analysis and Fredholm theory {#sec:std-microlocal}

**Theorem {#thm:std-hjs-calculus}** ([HJS, (2.1), Propositions 2.3, 3.7, 3.11, 3.13, 4.9, 4.10, 7.4, 7.5 and 10.1,
Definitions 7.2 and 10.2, Sections 7.5 and 10.1–10.3, Lemma 12.5, pp. 9–95].) The scattering calculus Ψ^(m,l)_sc on
ℝⁿ, n arbitrary, and on scattering manifolds M has the following properties.

(1) Composition [HJS, (2.1), p. 9]: Ψ^(m,l)_sc ∘ Ψ^(m′,l′)_sc ⊂ Ψ^(m+m′,l+l′)_sc.

(2) Ellipticity [HJS, Proposition 2.3, p. 12]: "Every elliptic element of the scattering calculus has a parametrix",
that is, a B ∈ Ψ^(−m,−l)_sc with AB − Id ∈ Ψ^(−∞,−∞)_sc ∋ BA − Id ((2.9)).

(3) Duality [HJS, Proposition 3.7, p. 19]: the L² pairing "extends boundedly to a (conjugate linear) isomorphism
H^(−s,−r)_sc ≅ (H^(s,r)_sc)*".

(4) Boundedness [HJS, Proposition 3.11 and Remark 3.12, p. 20]: "If A ∈ Ψ^(m,l)_sc, then, for all s, r ∈ ℝ, A maps
A : H^(s,r)_sc → H^(s−m,r−l)_sc, and does so boundedly". Moreover "Op(a), viewed as an element of
L(H^(s,r)_sc, H^(s−m,r−l)_sc), depends continuously on a in the sense that if a_1, a_2, ⋯ ∈ S^(m,l)_sc is some
sequence such that a_n → a in S^(m,l)_sc, then Op(a_n) → Op(a) in L(H^(s,r)_sc, H^(s−m,r−l)_sc)".

(5) Compactness [HJS, Proposition 3.13, p. 20]: "For any s, s′, r, r′, with s < s′ and r < r′, the embedding
H^(s′,r′)_sc ↪ H^(s,r)_sc is compact."

(6) Microlocality [HJS, Proposition 4.9, p. 27]: "If A ∈ Ψ^(m,l)_sc and u ∈ 𝒮′, then
WF^(s,r)_sc(Au) ⊆ WF^(s+m,r+l)_sc(u) ∩ WF′_sc(A)."

(7) Microlocal parametrix [HJS, Proposition 4.10, p. 29]: "Suppose that A ∈ Ψ^(m,l)_sc is elliptic at
p ∈ ∂(ℝⁿ × ℝⁿ). Then, there exists a B ∈ Ψ^(−m,−l)_sc such that AB − 1, BA − 1 have WF′_sc disjoint from p. This also
applies with p replaced by any closed subset."

(8) Adjoints and principal symbols [HJS, Definition 7.2, p. 48; Proposition 7.4, pp. 49–50]. The principal symbol of
A ∈ Ψ^(m,l)_sc(M) is a class σ_(m,l)(A) ∈ S^(m,l)_sc(M)/S^(m−1,l−1)_sc(M). Further,
"A ∈ Ψ^(m,l)_sc(M) ⇒ A* ∈ Ψ^(m,l)_sc(M)", and "σ_(m1+m2,l1+l2)(AB) = σ_(m1,l1)(A) σ_(m2,l2)(B)" (7.29).

(9) Commutators [HJS, Proposition 7.5, p. 50]: for A ∈ Ψ^(m1,l1)_sc(M) and B ∈ Ψ^(m2,l2)_sc(M),
"[A, B] ∈ Ψ^(m1+m2−1,l1+l2−1)_sc(M) and σ_(m1+m2−1,l1+l2−1)(i[A, B]) = {σ_(m1,l1)(A), σ_(m2,l2)(B)}" (7.30). Here
{p, a} = H_p a (7.31), with the scattering Hamilton vector field H_p of (7.34).

(10) Bundles [HJS, Section 7.5, pp. 52–53]: "Ψ^(m,l)_sc(M; E, F) := C^∞(X; Hom(E, F)) ⊗ Ψ^(m,l)_sc(M)" (7.43), the
tensor product being over C^∞(M).

(11) Variable spatial orders [HJS, Sections 10.1–10.3, pp. 77–80]. "We will take the differential order to be
constant, and the spatial order to be variable" (p. 77). A variable order is a classical symbol of order (0, 0).
Proposition 10.1 (p. 79): "Let A ∈ Ψ^(m,l)_sc be elliptic. Then there exists a parametrix B ∈ Ψ^(−m,−l)_sc such that
AB − Id ∈ Ψ^(−∞,−∞)_sc ∋ BA − Id." Definition 10.2 (p. 80): for s ∈ ℝ and a variable spatial order r, a constant
order L ≤ r, an elliptic A ∈ Ψ^(s,r)_sc and Λ = ⟨ξ⟩^s ⟨x⟩^L, "the Sobolev space H^(s,r) is defined to be the set of
u ∈ 𝒮′(ℝⁿ) such that Au ∈ L² and Λu ∈ L²", with ‖u‖²_(H^(s,r)) = ‖Au‖²_(L²) + ‖Λu‖²_(L²) (10.8). By the text that
follows, this space is independent of the choices and is a Hilbert space, and B ∈ Ψ^(m,l)_sc maps H^(s,r) to
H^(s−m,r−l) boundedly.

(12) A regularising family [HJS, Lemma 12.5, p. 95]: "There exists a family of T_r ∈ Ψ^(−∞,−∞)_sc for r ∈ (0, r0]
with some r0 > 0 such that T_r → Id (12.7) as r → 0 with respect to the strong operator topology". The family is
T_r = χ(r⟨z⟩) Op(χ(⟨rζ⟩)), with χ ∈ C_c^∞(ℝⁿ) even, equal to 1 near the origin and decreasing on [0, ∞). Its proof
records that one "can require T_r being uniformly bounded in Ψ^(0,0)_sc and T_r → Id in the operator topology of
Ψ^(δ,δ)_sc".

**Theorem {#thm:std-sbg-calculus}** ([Hin26d, Definitions 1.1–4.20, Propositions 3.3–4.22, Theorems 3.21–3.52,
(1.6), (3.26), (3.28), (4.24a–b), pp. 2–75].) On a smooth manifold M of any dimension n, without boundary, the
following hold.

(S1) Structures [Hin26d, Definitions 1.1 and 1.3, (1.6), pp. 2–6]. A bounded geometry structure is a countable set
{(U_α, φ_α)} of diffeomorphisms φ_α : U_α → (−2, 2)ⁿ such that the U_α have finite multiplicity,
M = ⋃ φ_α⁻¹((−1, 1)ⁿ), and the transition functions τ_βα = φ_β ∘ φ_α⁻¹ are uniformly bounded in C^∞. A scaled
structure 𝓑^× = {(U_α, φ_α, ρ_α)} adds scalings ρ_α ∈ (0, 1]ⁿ with

    |∂^γ(ρ_(α,i) ∂_i τ^j_βα(x))| ≤ C_γ ρ_(β,j)      (1.6).

It defines ρ̄_α := max_i ρ_(α,i); the coefficient Lie algebra 𝒲 := C^∞_(uni,𝓑)(M; TM); and the operator Lie algebra
𝒱 ⊂ 𝒲 of those V with (φ_α)_* V = Σ V^i_α ρ_(α,i) ∂_i, the V^i_α uniformly bounded with all derivatives.

(S2) Weights [Hin26d, Definitions 3.4 and 3.6, pp. 29–30].

(S3) Sobolev spaces [Hin26d, Definitions 3.14 and 3.17, Propositions 3.19 and 3.22, Theorem 3.21, pp. 34–39]. The
spaces are w H^s_𝒱(M) and w H^(s;k)_(𝒱;𝒲)(M). Proposition 3.19: every P ∈ w Diff^m_𝒱(M) maps
w′ H^(s;k)_(𝒱;𝒲)(M) → w w′ H^(s−m;k)_(𝒱;𝒲)(M) boundedly. Theorem 3.21: "Let w, w′ ∈ C^∞(M) be weights on (M, 𝓑) with
w/w′ → 0 at infinity. Let s, s′ ∈ ℝ. Suppose that s > s′. Then the inclusion map w H^s_𝒱(M) ↪ w′ H^(s′)_𝒱(M) is
compact. More generally, if k, k′ ∈ ℕ₀, and s ≥ s′ and k ≥ k′, with at least one inequality strict, then the
inclusion map w H^(s;k)_(𝒱;𝒲)(M) ↪ w′ H^(s′;k′)_(𝒱;𝒲)(M) is compact." Proposition 3.22: duality through a uniformly
positive 𝒱-density.

(S4) Quantization and residual operators [Hin26d, Definitions 3.7, 3.8, 3.31, 3.34 and 3.43, (3.26) p. 43, (3.28)
p. 44, pp. 31–51]. The local quantization (3.26) has phase Σ_j (x^j_α − x′^j_α) ξ_j/ρ_(α,j) and the cut-off
ψ(x_α − x′_α), with ψ ∈ C_c^∞((−1/4, 1/4)ⁿ) equal to 1 near 0. Op_𝒱 is (3.28).

(S5) Boundedness and the calculus [Hin26d, Theorem 3.44 p. 51, Remark 3.47 p. 52, Theorem 3.51 p. 55, Theorem 3.52
p. 56, Proposition 3.55 p. 57]. Theorem 3.44: "Let w, w′ ∈ C^∞(M) be weights on (M, 𝓑); let s, m ∈ ℝ. Then every
A ∈ w Ψ^m_𝒱(M) defines a bounded linear map w′ H^s_𝒱(M) → w w′ H^(s−m)_𝒱(M), and more generally
w′ H^(s;k)_(𝒱;𝒲)(M) → w w′ H^(s−m;k)_(𝒱;𝒲)(M) for all k ∈ ℕ₀." Remark 3.47 gives the seminorms of w Ψ^m_𝒱(M).
Theorem 3.51: closure under adjoints and compositions in w ρ^(−l) Ψ^m_𝒱(M), with σ(A*) = σ(A)‾ and
σ(A_1 ∘ A_2) = σ(A_1) σ(A_2). Theorem 3.52: "Suppose 𝒱 is fully symbolic. Let P ∈ w Ψ^m_𝒱(M) be elliptic … Then, for
all weights w′ … and for all s ∈ ℝ, the operator P : w′ H^s_𝒱(M) → w w′ H^(s−m)_𝒱(M) is Fredholm."

(S6) Regularity of symbols [Hin26d, Remark 3.33, p. 45]: "one only needs uniform bounds by ⟨ξ⟩^(m−|γ|) on
|(ρ_α ∂_(x_α))^β ∂_ξ^γ a_α(x_α, ξ)|, corresponding to '𝒱-regular' symbols", together with their derivatives for the
spaces with k orders of 𝒲-regularity.

(S7) Parameterised structures [Hin26d, Definitions 3.58–3.59, p. 59].

(S8) Variable orders [Hin26d, Definition 4.6, p. 66]: for m, l ∈ S⁰(𝒱T*M),

    ρ^(−l) S^m(𝒱T*M) := ρ^(−l) λ^(−m) ⋂_(δ∈(0,1/2)) S⁰_(1−δ,δ)(𝒱T*M),

and w Ψ^(m,l)_𝒱(M) := {Op_𝒱(a) + R}. The principal symbol is taken modulo ⋂_δ w ρ^(−l+1−2δ) S^(m−1+2δ) (4.10), and
w H^(m,l)_𝒱(M) := {u ∈ w ρ^(inf l) H^(inf m)_𝒱(M) : Au ∈ L²(M)} for a fixed elliptic A. On the same page [Hin26d]
says that "Theorem 3.51 thus remains valid, mutatis mutandis" for the (1 − δ, δ) classes.

(S9) The Fourier transform in t [Hin26d, Definitions 4.11 and 4.14, Propositions 4.15, 4.17 and 4.18, (4.24a) p. 73,
(4.24b) p. 74, pp. 68–74]. For variable orders s, l invariant under translations in t,

    F : w ρ_X^l H^s_𝒱(ℝ × X) → L²(ℝ_σ; w ρ_X^(l̂_σ) ⟨τσ⟩^(−ŝ_σ) H^(ŝ_σ)_(𝒱̂_σ)(X))      (4.24b)

is an isomorphism, with l̂_σ = l|_(σ dt + T*X) and ŝ_σ = s|_(σ dt + T*X) (4.24a).

(S10) Commutator 𝒲-vector fields [Hin26d, Definition 4.20 p. 74, Proposition 4.22 p. 75]. 𝒲_[𝒱] is "the space of all
W ∈ 𝒲 so that [W, V] ∈ 𝒱 for all V ∈ 𝒱". If 𝒲_[𝒱] spans 𝒲 over C^∞_(uni,𝓑)(M) (4.25), then
"ad_(W_1) ⋯ ad_(W_k) A ∈ ρ^(−l) Ψ^m_(𝒱,[ ])(M) for all A ∈ ρ^(−l) Ψ^m_(𝒱,[ ])(M), k ∈ ℕ, W_1, …, W_k ∈ 𝒲_[𝒱]", and
"⋃_(m,l∈ℝ) ρ^(−l) Ψ^m_(𝒱,[ ])(M) is closed under compositions and adjoints. Analogous statements hold for operators
with weights, phase space weights, and variable orders."

(S11) Phase space weights [Hin26d, Proposition 4.2, p. 63]: "(1) Every P ∈ Ψ^w_𝒱(M) defines a bounded map
H^(w′)_𝒱(M) → H^(w w′)_𝒱(M). (2) … (H^w_𝒱(M))* = H^(w⁻¹)_𝒱(M)" (4.4).

See also [Hin26d, Proposition 3.3, p. 29] (the secondary structure ρ𝓑) and [Hin26d, Remark 3.48, p. 52] (relation
with 𝒱′-operators).

**Theorem {#thm:std-zero-calculus}** ([Hin23e, (1.3)–(1.5), Definition 1.2, Proposition 2.7, Corollary 3.3,
Theorem 3.4, Remark 3.5 and Corollary 3.6, pp. 1–34].) Let n ≥ 1 and let X be a smooth n-dimensional manifold with
boundary ∂X ≠ ∅ (p. 1).

(1) Normal operators (p. 4). For P = Σ_(j+|β|≤m) a_(jβ)(x, y)(xD_x)^j(xD_y)^β (1.3), the reduced normal operator at
(0, y0) is

    N̂(P, y0, η̂) = Σ a_(jβ)(0, y0)(tD_t)^j(tη̂)^β,   t = x̃|η̃|,  η̂ = η̃/|η̃|      (1.5).

(2) Definition 1.2 (p. 5). "Let α ∈ ℝ, and let P ∈ Ψ^m_0(X; ⁰Ω^(1/2)X) be an operator with elliptic principal symbol.
We say that N̂(P, y0, η̂) is invertible at the weight α if the following three conditions hold:
- (1) α ≠ Re z for all (z, k) ∈ Spec_b(P, y0).
- (2) If u ∈ t^α L²([0, ∞], |dt/t|) solves N̂(P, y0, η̂)u = 0, then u = 0.
- (3) If v ∈ t^(−α) L²([0, ∞], |dt/t|) solves N̂(P, y0, η̂)*v = 0, then v = 0."

The adjoint is taken for |dt/t|, or for any polynomially weighted b-density. "If N̂(P, y0, η̂) is invertible at the
weight α for all y0, η̂, then we say that P is fully elliptic at the weight α."

(3) Proposition 2.7 (p. 11): composition in the 0-calculus with bounds, under (2.8) and α_rb + β_lb > n − 1.

(4) Corollary 3.3 (p. 31): "Suppose X is compact. Let P ∈ Ψ^m_0(X; ⁰Ω^(1/2)X) be fully elliptic at the weight α. Then

    P : ρ^(α−(n−1)/2) H^s_0(X; ⁰Ω^(1/2)X) → ρ^(α−(n−1)/2) H^(s−m)_0(X; ⁰Ω^(1/2)X)      (3.23)

… is a Fredholm operator." The corollary also describes its generalized inverse.

(5) Theorem 3.4 (p. 33): "Let α0 < α1. Let P ∈ Ψ^m_0(X; ⁰Ω^(1/2)X) be fully elliptic at all weights
α ∈ [α0 − ε, α1 + ε] for some small ε > 0. Then there exists operators

    Q, Q′ ∈ Ψ^(−m)_0 + Ψ^(−∞,(α1,−α0+(n−1)))_0 + Ψ^(−∞,(α1,−α0+(n−1)))      (3.26)

so that PQ = I − R and Q′P = I − R′ with R ∈ Ψ^(−∞,(∞,−α0+(n−1))), R′ ∈ Ψ^(−∞,(α1,∞))". All spaces are of operators
on ⁰Ω^(1/2)X.

(6) Remark 3.5 (p. 33): "When X is compact and P is fully elliptic at the weight α ∈ ℝ, then the hypotheses of
Theorem 3.4 are satisfied when α0 < α and α1 > α are sufficiently close to α and ε > 0 is sufficiently small."

(7) Corollary 3.6 (p. 34): "Suppose X is compact, and let P be an operator satisfying the assumptions of Theorem 3.4 …
Then for any α ∈ [α0, α1], the operator P is a Fredholm operator as in (3.23)." It also places the generalized
inverse in the calculus with bounds.

**Theorem {#thm:std-mazzeo-melrose}** ([MM87] [[pending:literature-not-found]].) Operators of the small 0-calculus
Ψ^m_0(X) are bounded on the weighted 0-Sobolev spaces x^α H^s_0(X) → x^α H^(s−m)_0(X).

**Theorem {#thm:std-relative-index}** ([Mel93, Theorem 6.5, p. 214].) Let X be a compact manifold with boundary whose
boundary has p components. For P ∈ Diff^m_b(X; E, F) elliptic and a multiweight a ∈ ℝ^p,

    ind(P, a) = dim{u ∈ x^a H^M_b(X; E); Pu = 0}
              − codim{v ∈ x^a H^(M−m)_b(X; F); v = Pu, u ∈ x^a H^M_b(X; E)}      (6.15).

"If P ∈ Diff^m_b(X; E, F) is elliptic and a_j, a′_j ∉ −Im spec_(b,j)(P), j = 1, …, p, then the index, as given by
(6.15), satisfies

    ind(P, a) − ind(P, a′) = Σ_(j=1)^p sgn(a′_j − a_j) Σ_(z ∈ spec_(b,j)(P), −Im z ∈ [a_j, a′_j]) rank_j(z)."      (6.16)

Here rank_j(z) is the rank of the zero z of the indicial family at the j-th boundary hypersurface ((5.8)–(5.9)). "If
∂X is connected, so a = α, a′ = α′ are just real numbers, and α > α′ then (6.16) shows that ind(P, α) < ind(P, α′)
and the difference is minus the sum of the ranks of the points of spec_b(P) between the two lines Im z = −α and
Im z = −α′".

**Theorem {#thm:std-analytic-fredholm}** ([RS1, Theorem VI.14].) Let D ⊂ ℂ be open and connected, 𝓗 a Hilbert space,
and F : D → 𝓛(𝓗) analytic with F(z) compact for every z ∈ D. If Id + F(z0) is invertible for one z0 ∈ D, then
(Id + F(z))⁻¹ exists for z off a discrete set S ⊂ D, and it is meromorphic on D with finite-rank residues.

### Special functions and the Fourier–Laplace transform {#sec:std-special}

**Theorem {#thm:std-dlmf-hankel}** ([DLMF, (10.2.1), 10.2(ii) (10.2.5)–(10.2.6), (10.7.7), (10.17.1)–(10.17.2),
(10.17.5)–(10.17.6)].)

(1) Bessel's equation (10.2.1) is z² w″ + z w′ + (z² − ν²) w = 0. Its solutions H^(1)_ν and H^(2)_ν are
characterised by

    H^(1)_ν(z) ∼ (2/(πz))^(1/2) e^(i(z − νπ/2 − π/4))  as z → ∞ in −π + δ ≤ ph z ≤ 2π − δ      (10.2.5),

    H^(2)_ν(z) ∼ (2/(πz))^(1/2) e^(−i(z − νπ/2 − π/4))  as z → ∞ in −2π + δ ≤ ph z ≤ π − δ      (10.2.6),

"where δ is an arbitrary small positive constant". Their principal branches are taken "with a cut in the z-plane along
the interval (−∞, 0]".

(2) As z → 0 with ν fixed, "H^(1)_ν(z) ∼ −H^(2)_ν(z) ∼ −(i/π) Γ(ν) (z/2)^(−ν), Re ν > 0" (10.7.7).

(3) Hankel's expansions. Let a_0(ν) = 1, let a_k(ν) be as in (10.17.1) and let ω = z − νπ/2 − π/4 (10.17.2). Then, as
z → ∞ with ν fixed,

    H^(1)_ν(z) ∼ (2/(πz))^(1/2) e^(iω) Σ_(k=0)^∞ i^k a_k(ν)/z^k,   −π + δ ≤ ph z ≤ 2π − δ      (10.17.5),

    H^(2)_ν(z) ∼ (2/(πz))^(1/2) e^(−iω) Σ_(k=0)^∞ (−i)^k a_k(ν)/z^k,   −2π + δ ≤ ph z ≤ π − δ      (10.17.6).

**Theorem {#thm:std-dlmf-modified}** ([DLMF, (10.25.1), (10.28.2), (10.30.2), (10.40.1)–(10.40.2)].) The modified
Bessel equation is z² w″ + z w′ − (z² + ν²) w = 0 (10.25.1), with solutions I_ν and K_ν. Their Wronskian is
𝒲{K_ν(z), I_ν(z)} = 1/z (10.28.2). As z → 0, K_ν(z) ∼ (1/2) Γ(ν) (z/2)^(−ν) for Re ν > 0 (10.30.2). As z → ∞,
I_ν(z) ∼ e^z (2πz)^(−1/2)(1 + O(1/z)) and K_ν(z) ∼ (π/(2z))^(1/2) e^(−z)(1 + O(1/z)) ((10.40.1)–(10.40.2), first
terms).

**Theorem {#thm:std-paley-wiener}** ([Hö83, Theorem 7.3.1] [[pending:literature-not-found]].) Let K be a convex compact
subset of ℝⁿ with supporting function H(ξ) = sup_(x∈K) ⟨x, ξ⟩. If u is a distribution of order N with support in K,
then its Fourier–Laplace transform û(ζ) = u(e^(−i⟨·,ζ⟩)) is entire and

    |û(ζ)| ≤ C (1 + |ζ|)^N e^(H(Im ζ)),   ζ ∈ ℂⁿ.

Conversely, every entire analytic function in ℂⁿ satisfying an estimate of this form is the Fourier–Laplace transform
of a distribution with support in K.
