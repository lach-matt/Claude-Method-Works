## Appendix. Results from the literature {#app:standard-results}

The proofs use the published results below as stated, without proof. Each is given with its source, its number and its
page, the pages being those of the versions listed in the references. Quotation marks enclose the source's own wording,
transcribed into this edition's typography; an ellipsis marks words of the statement left out because they define
estimates or spaces that no proof here uses. Inside each item the letters are the source's.

### Linear wave equations on Lorentzian manifolds {#sec:std-linear-wave}

**Definition {#def:std-normally-hyperbolic}** ([BGP, Section 1.5, p. 33].) Let M be a Lorentzian manifold and E → M a
real or complex vector bundle. "A linear differential operator P : C^∞(M, E) → C^∞(M, E) of second order will be called
normally hyperbolic if its principal symbol is given by the metric, σ_P(ξ) = −⟨ξ, ξ⟩ · id_(E_x)."

**Theorem {#thm:std-bgp-cauchy}** ([BGP, Theorem 3.2.11, p. 85].) "Let M be a globally hyperbolic Lorentzian manifold and
let S ⊂ M be a spacelike Cauchy hypersurface. Let n be the future directed timelike unit normal field along S. Let E be
a vector bundle over M and let P be a normally hyperbolic operator acting on sections in E. Then for each u0, u1 ∈
𝒟(S, E) and for each f ∈ 𝒟(M, E) there exists a unique u ∈ C^∞(M, E) satisfying Pu = f, u|_S = u0, and ∇_n u|_S =
u1. Moreover, supp(u) ⊂ J^M(K) where K = supp(u0) ∪ supp(u1) ∪ supp(f)." Here 𝒟 denotes smooth sections with compact
support, and ∇ is the connection on E with which [BGP, Section 3.2] poses the Cauchy problem. Globally hyperbolic
manifolds are connected in [BGP, Definition 1.3.8, p. 23].

**Theorem {#thm:std-bgp-development}** ([BGP, Lemma A.5.9, p. 176].) "For any acausal hypersurface S in a timeoriented
Lorentzian manifold the Cauchy development D(S) is a causally compatible and globally hyperbolic open subset of M."
Its proof records that "by the definition of D(S), the acausal subset S is a Cauchy hypersurface of D(S)". The Cauchy
development D(S) is the set of points p of M such that every inextendible causal curve through p meets S [BGP,
Definition 1.3.5, p. 22].

### Quasilinear hyperbolic systems {#sec:std-hyperbolic}

The setting of [DS23] is the system "∂_t u + A^i(u) ∂_i u = R(u), u(0) = u0, i = 1, 2, …, N" (its (1.1), p. 1) on the
torus 𝕋^N, with A^i : ℝ × 𝕋^N × ℝ^m → ℝ^(m²), R : ℝ × 𝕋^N × ℝ^m → ℝ^m and "N(u)(t, x) = N(t, x, u(t, x)), N ∈ {A^i,
R}" (p. 2). H^r = H^r(𝕋^N), and "I = [−T, T] for some T > 0 and B(I) = C(I; C¹) ∩ C¹(I; C)" (p. 3). For a non-empty
open set U ⊂ ℝ^m the hypotheses are, on p. 3:

- (A1) "A^i ∈ C^∞(ℝ × 𝕋^N × U; ℝ^(m²)) satisfies that for any multi-indices k ∈ ℕ, α ∈ ℕ^n and β ∈ ℕ^m, there is a
  continuous increasing function f^i_(k,α,β) such that |∂^k_t ∂^α_x ∂^β_ζ A^i(t, x, ζ)| ≤ f^i_(k,α,β)(|ζ|)."
- (A2) The same for R ∈ C^∞(ℝ × 𝕋^N × U; ℝ^m), with continuous increasing functions h_(k,α,β).
- (A3) "For any ξ = (ξ_1, …, ξ_N) ∈ ℝ^N ∖ {0} and ζ ∈ U, the matrix A = A(t, x, ζ, ξ) = A^i(t, x, ζ) ξ_i is
  diagonalizable and has only real eigenvalues".
- (A4) "The distinct eigenvalues, λ_1 < λ_2 < ⋯ < λ_l, of A satisfy λ_i ∈ C^(1,0,1,0)(ℝ × 𝕋^N × U × (ℝ^N ∖ {0})) and
  the λ_i's do not meet each other on ℝ × 𝕋^N × U × (ℝ^N ∖ {0})".

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

**Remark {#rem:std-ds-moser}** ([DS23, Remark 2.3(i), p. 4].) The authors state, "following a standard argument": "Based
on (A1) and (A2), … given any compact interval I ⊂ ℝ and s > N/2, it holds for any u ∈ H^s such that ‖N(u)‖_s ≤ C_I +
F_I(‖u‖_∞) ‖u‖_s, N ∈ {A^i, R}", where (p. 3) "F_I : ℝ_+ → ℝ_+ (C_I, resp.) denotes a continuous increasing function
(a positive constant, resp.) depending on the structure of A^i and R such that F_(I_1) ≤ F_(I_2) (C_(I_1) ≤ C_(I_2),
resp.) whenever I_1 ⊂ I_2."

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

**Theorem {#thm:std-cbcl-harmonicity}** ([CBCL06, (3.1) and Section 3, p. 5; Section 5.1, p. 9].) "The vacuum Einstein
equations in wave coordinates on ℝ^(n+1) constitute a set of quasi-diagonal quasi-linear wave equations" (3.1). In
Section 3, p. 5: "We suppose also given on ℝⁿ the lapse N̄, shift β̄ as well as their time derivatives, chosen so that
the corresponding spacetime metric and its first derivatives satisfy on ℝⁿ the harmonicity conditions F^μ = 0. If the
initial data ḡ, K satisfy the constraints, a solution of the Einstein equations in wave coordinates on V is such that
the harmonicity functions F^μ := □_g x^μ satisfy an homogeneous linear system of wave equations on (V, g), with also
∂_t F^μ = 0, hence F^μ = 0 if (V, g) is globally hyperbolic." In Section 5.1, p. 9, under the hypothesis "We suppose
these initial data satisfy the Einstein constraints, and we choose the initial lapse and shift so that the harmonicity
conditions are everywhere initially zero": "Such a solution exists if the initial data belong to H^loc_(s+1) ×
H^loc_s, s > n/2."

**Theorem {#thm:std-lr-propagation}** ([LR05, (1.3), p. 2; Section 2.2, p. 8].) In 3 + 1 dimensions and wave coordinates
the reduced Einstein–scalar field equations are "□̃_g g_μν = F_μν(g)(∂g, ∂g) + 2 ∂_μψ ∂_νψ, □̃_g ψ = 0" (1.3), with
□̃_g := g^(αβ) ∂_α ∂_β; their vacuum case is ψ = 0. With the gauge's data (2.3)–(2.5), p. 8: "any solution of the system
(2.1) with initial data … compatible with (2.2) and constraint equations, gives rise to a solution of the full Einstein
system. In addition, thus constructed tensor g_μν will satisfy the wave coordinate condition (2.2) for all times." For
the verification [LR05, p. 8] refers to Wald: "Verification of the above statements is straightforward and can be found
in e.g. [Wa]."

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

### Function spaces {#sec:std-function-spaces}

In [BH17], s ∈ ℝ and p ∈ (1, ∞) throughout unless stated otherwise (p. 1).

**Theorem {#thm:std-bh-extension}** ([BH17, Theorem 7.21, p. 55].) "Let Ω ⊂ ℝⁿ be a bounded open set with Lipschitz
continuous boundary. Then for all s > 0 and for 1 ≤ p < ∞, there exists a continuous linear extension operator P :
W^(s,p)(Ω) ↪ W^(s,p)(ℝⁿ) such that (Pu)|_Ω = u and ‖Pu‖_(W^(s,p)(ℝⁿ)) ≤ C ‖u‖_(W^(s,p)(Ω)) for some constant C that may
depend on s, p, and Ω but is independent of u."

**Theorem {#thm:std-bh-embedding}** ([BH17, Theorem 7.26, p. 55].) "Let Ω be a nonempty bounded open subset of ℝⁿ with
Lipschitz continuous boundary or Ω = ℝⁿ. If sp > n, then W^(s,p)(Ω) ↪ L^∞(Ω) ∩ C⁰(Ω) and W^(s,p)(Ω) is a Banach
algebra."

**Theorem {#thm:std-bh-manifold}** ([BH17, Theorem 9.14, p. 85].) "Let Mⁿ be a compact smooth manifold. Let π : E → M be
a smooth vector bundle of rank r over M equipped with fiber metric ⟨., .⟩_E … Suppose s ∈ ℝ and p ∈ (1, ∞) are such that
sp > n. Then W^(s,p)(M, E) ↪ L^∞(M, E). Moreover, every element u in W^(s,p)(M, E) has a continuous version."

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

**Theorem {#thm:std-ly-extension}** ([LY22, Theorem 1, pp. 1–2; Theorem 26 and Lemma 27, p. 16].) Theorem 1 gives an
extension operator E for the upper half space ℝⁿ_+ such that "(ii) … E : W^(k,p)(ℝⁿ_+) → W^(k,p)(ℝⁿ) and E :
C^(k,s)(ℝⁿ_+) → C^(k,s)(ℝⁿ) are defined and bounded for all k ∈ ℤ, 0 < p ≤ ∞ and 0 < s < 1. E : C^k(ℝⁿ_+) → C^k(ℝⁿ) is
bounded for all k = 0, 1, 2, …", one operator for all these spaces at once. Theorem 26: "Let Ω ⊂ ℝⁿ be a bounded smooth
domain with a smooth defining function σ, and let U ⊂ ℝⁿ be a bounded neighborhood of Ω̄. Then there exists an
extension operator E : 𝒮′(Ω) → ℰ′(U) that maps extendable distributions in Ω … to compactly supported distributions in
U, such that … (ii) (Universal boundedness) E : W^(k,p)(Ω) → W^(k,p)_c(U) and E : C^(k,s)(Ω) → C^(k,s)_c(U) are defined
and bounded for all k ∈ ℤ, 0 < p ≤ ∞ and 0 < s < 1. In particular E : C^k(Ω) → C^k_c(U) for k ≥ 0." Lemma 27: "Let Φ :
ℝⁿ → ℝⁿ be a bounded diffeomorphism, i.e. Φ is bijective and sup_(x∈ℝⁿ) |∂^α Φ(x)| + |∂^α(Φ⁻¹)(x)| < ∞, ∀ α ∈ ℕⁿ_0 ∖
{0}. Let χ ∈ C_c^∞(ℝⁿ) be a bounded smooth function. Define a linear map T f := (χ · f) ∘ Φ. (i) T : W^(k,p)(ℝⁿ) →
W^(k,p)(ℝⁿ), T : C^(k,s)(ℝⁿ) → C^(k,s)(ℝⁿ) are both defined and bounded for all k ∈ ℤ, 0 < p ≤ ∞ and 0 < s < 1."

**Theorem {#thm:std-sy-extension}** ([SY21, Section 1, p. 2; Section 2.1, p. 6].) After Rychkov, "for a Lipschitz domain
Ω there exists an operator E = E_Ω that is bounded on Besov spaces E : B^s_pq(Ω) → B^s_pq(ℝⁿ) for all 0 < p, q ≤ ∞, s ∈
ℝ … Since E is one single operator which works for all such spaces, we call it an universal extension operator"; and
after Stein, when Ω is a bounded Lipschitz domain, "an extension operator E_S which is independent of k, such that E_S
: W^(k,p)(Ω) → W^(k,p)(ℝⁿ) is bounded for all k ∈ ℕ and 1 ≤ p ≤ ∞".
