## Appendix. Results from the literature {#app:standard-results}

The proofs use the published results below as stated, without proof. Each is given with its source, its number and,
where known, its page. Quotation marks enclose the source's own wording, transcribed into the notation of this edition's
typography; an ellipsis marks words of the statement omitted because the use does not depend on them. Inside each item
the letters are the source's.

### Quasilinear hyperbolic systems {#sec:std-hyperbolic}

**Theorem {#thm:std-ds-existence}** ([DS23, Theorem 2.4] [[pending:issue-1]].) Consider the system ∂_t u + A^i(u) ∂_i u
= R(u) on the torus 𝕋^N (the system (1.1) of [DS23]), whose coefficients A^i and R are smooth in (t, x, ζ) on their
domain U (hypotheses (A1)–(A2) of [DS23]), such that A^i ξ_i is diagonalisable with real eigenvalues (A3) that "do not
meet each other" (A4). "Let r > N/2 + 1 … for any u0 ∈ H^r with M̃ = dist(U^c, Im(u0)) > 0, there exists some T > 0
depending on ‖u0‖_r and M̃ such that (1.1) has a unique solution u in B(I) on I = [−T, T]", where B(I) = C(I; C¹) ∩
C¹(I; C). The statement allows R(t, x, 0) ≠ 0.

**Theorem {#thm:std-ds-continuation}** ([DS23, Theorem 2.6] [[pending:issue-1]].) Under the hypotheses of
[[thm:std-ds-existence]], let [0, T*) be the maximal interval of existence. Then "one and only one of the following
statements holds. T* = ∞; inf dist(U^c, Im u(t)) = 0; lim ‖u‖_(B([0,T])) = +∞".

**Theorem {#thm:std-ds-moser}** ([DS23, Remark 2.3(i)] [[pending:issue-1]].) For the composition N(u) of a smooth
function N with u, "for any u ∈ H^s … ‖N(u)‖_s ≤ C_I + F_I(‖u‖_∞) ‖u‖_s", with the constant C_I and the function F_I
of [DS23, Remark 2.3].

**Theorem {#thm:std-ao-existence}** ([AO14, Theorem 1.1, p. 2, and Remark 1.2].) For quasilinear wave equations on the
torus 𝕋^n, under the hypothesis (1.3) of [AO14], "1/γ |ξ|² ≤ A^ij(U) ξ_i ξ_j ≤ γ |ξ|² and A^00(U) ≤ −κ": "Suppose n ≥
3, s ∈ ℤ_(> n/2) … Then there exist a T > 0 and a map U … the unique solution … Moreover, if ‖u‖_(W^(1,∞)((0,T) ×
𝕋^n)) < ∞, then … u can be continued uniquely". The statement assumes F(0, 0) = 0 and is used in the case H = 0 of its
notation. By Remark 1.2 (i)(a), A and F may "depend explicitly on x", and by Remark 1.2 (ii)(b) the theorem holds for
"A^μν(U, ∂U) ∂_μ ∂_ν U = F(U, ∂U) … provided that we take s > n/2 + 1 and change the continuation principle to that of
bounding ‖U‖_(W^(2,∞))".

**Remark {#rem:std-iteration}** (The iteration of Kato and Majda; [AO14, Section 4.1], [AG22, p. 1 and (9.6)–(9.7), p.
24].) [AO14, Section 4.1] describes "the well-known strategy … of setting up an appropriate iterative approximation
scheme and showing convergence by establishing boundedness in a high norm followed by contraction in a low norm". In
[AG22, Section 9] the iterates are bounded in H^s and a subsequence converges weakly, (9.6); the abstract, p. 1, names
"the boundedness in the high norm and contraction in the low norm".

### The reduced Einstein equations and the gauge {#sec:std-gauge}

**Theorem {#thm:std-cbcm-reduced}** ([CBCM10, (2.7)–(2.9), p. 8].) In n + 1 dimensions, let ĝ be a background metric
with connection D̂ and Christoffel symbols Γ̂, and for a metric g put W^λ := g^(αβ) Γ̂^λ_(αβ) and H^λ := g^(αβ)
Γ^λ_(αβ) − W^λ = g^(αβ)(Γ^λ_(αβ) − Γ̂^λ_(αβ)) (2.7). Then

    "R_(αβ) = R^(H)_(αβ) + 1/2 (g_(αλ) D̂_β H^λ + g_(βλ) D̂_α H^λ)"   (2.8),
    "R^(H)_(αβ) = −1/2 g^(λμ) D̂_λ D̂_μ g_(αβ) + f̂[g, D̂g]_(αβ)"       (2.9),

with f̂ "independent of the second derivatives of g".

**Theorem {#thm:std-cbcl-harmonicity}** ([CBCL06, (3.1), Sections 3 and 5.1] [[pending:issue-1]].) "The vacuum Einstein
equations in wave coordinates on ℝ^(n+1) constitute a set of quasi-diagonal quasi-linear wave equations" (3.1); "the
harmonicity functions F^μ := □_g x^μ satisfy an homogeneous linear system of wave equations on (V, g), with also ∂_t
F^μ = 0, hence F^μ = 0 if (V, g) is globally hyperbolic" (Section 3); and "Such a solution exists if the initial data
belong to H^loc_(s+1) × H^loc_s, s > n/2" (Section 5.1).

**Theorem {#thm:std-lr-propagation}** ([LR05, p. 1, (1.3) p. 2, Section 2.2 p. 8].) In 3 + 1 dimensions and wave
coordinates the reduced equations are "g^(αβ) ∂_α ∂_β g_μν = F_μν(g)(∂g, ∂g)" (1.3), with the gauge's data (2.3)–(2.5),
and "any solution of the system (2.1) with initial data … compatible with (2.2) and constraint equations, gives rise to a
solution of the full Einstein system. In addition, thus constructed tensor g_μν will satisfy the wave coordinate
condition (2.2) for all times". The argument is the contracted Bianchi identity, p. 1: "The Bianchi identities D_μ G^μν
= 0".

**Theorem {#thm:std-cd-constraints}** ([CD03, (2.1)–(2.2), p. 4].) On a spacelike slice with induced metric γ and
second fundamental form K, the constraint map is

    (J, ρ) = (2 (−div K + d tr K), R(γ) − |K|² + (tr K)²),

and its vanishing gives the vacuum constraints: "These are the general relativistic constraint equations whatever the
space-dimension n".

**Remark {#rem:std-racz}** ([Rac16, (3.3), p. 6].) Rácz writes the constraint equations as an evolutionary system (3.3)
in a coordinate ρ transverse to a foliation of the slice by codimension-one surfaces, and observes: "Notice that the
coefficients of ∂ρ and ∂K are symmetric, and that the coefficient of ∂ρ is also positive definite".

### Function spaces {#sec:std-function-spaces}

**Theorem {#thm:std-bh-extension}** ([BH17, Theorem 7.21] [[pending:issue-1]].) "Let Ω ⊂ ℝⁿ be a bounded open set with
Lipschitz continuous boundary. Then for all s > 0 and for 1 ≤ p < ∞, there exists a continuous linear extension
operator" from W^(s,p)(Ω) to W^(s,p)(ℝⁿ).

**Theorem {#thm:std-bh-embedding}** ([BH17, Theorem 7.26] [[pending:issue-1]].) "If sp > n, then W^(s,p)(Ω) ↪ L^∞(Ω) ∩
C⁰(Ω) and W^(s,p)(Ω) is a Banach algebra."

**Theorem {#thm:std-bh-manifold}** ([BH17, Theorem 9.14] [[pending:issue-1]].) The embedding of
[[thm:std-bh-embedding]] holds on compact manifolds: if sp > n, then W^(s,p)(M) ↪ L^∞(M) ∩ C⁰(M) for a compact
n-dimensional manifold M.

**Theorem {#thm:std-kato-ponce}** ([GO13, p. 1].) With J^s := (1 − Δ)^(s/2) on ℝⁿ,

    ‖J^s(f g) − f (J^s g)‖_(L^p) ≤ C [‖∇f‖_(L^∞) ‖J^(s−1) g‖_(L^p) + ‖J^s f‖_(L^p) ‖g‖_(L^∞)]

"for 1 < p < ∞ and s > 0".

**Theorem {#thm:std-ly-extension}** ([LY22, Theorem 1, Theorem 26 and Lemma 27] [[pending:issue-1]].) There is an
extension operator E from the upper half space ℝⁿ_+ with "(ii) … E : W^(k,p)(ℝⁿ_+) → W^(k,p)(ℝⁿ) and E : C^(k,s)(ℝⁿ_+)
→ C^(k,s)(ℝⁿ) are defined and bounded for all k ∈ ℤ, 0 < p ≤ ∞ and 0 < s < 1. E : C^k(ℝⁿ_+) → C^k(ℝⁿ) is bounded for
all k = 0, 1, 2, …" (Theorem 1), one operator for all these spaces at once. "Universal Seeley's extension on smooth
domains" (Theorem 26): for a bounded smooth domain Ω, "E : W^(k,p)(Ω) → W^(k,p)_c(U) … bounded for all k ∈ ℤ, 0 < p ≤
∞". Lemma 27 gives the composition of such operators with bounded diffeomorphisms. Of Seeley's operator, "E : C^k(ℝⁿ_+)
→ C^k(ℝⁿ) for all k = 0, 1, 2, … In particular Seeley's extension [preserves] C^∞-smoothness".

**Theorem {#thm:std-sy-extension}** ([SY21, Sections 1 and 2.1] [[pending:issue-1]].) After Rychkov, "for a Lipschitz
domain Ω there exists an operator E = E_Ω that is bounded on Besov spaces E : B^s_pq(Ω) → B^s_pq(ℝⁿ) for all 0 < p, q ≤
∞, s ∈ ℝ … Since E is one single operator which works for all such spaces, we call it an universal extension operator";
and after Stein, "an extension operator E_S which is independent of k, such that E_S : W^(k,p)(Ω) → W^(k,p)(ℝⁿ) is
bounded for all k ∈ ℕ and 1 ≤ p ≤ ∞".
