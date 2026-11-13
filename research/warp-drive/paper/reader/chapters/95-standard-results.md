## Appendix. Results from the literature {#app:standard-results}

The proofs use the published results below as stated; they are not proved here. Five items are consequences of these
results and are proved here: [[thm:std-hormander-cauchy]], [[cor:std-moser-product]], [[thm:std-gn-moser]],
[[cor:std-kato-ponce]] and [[cor:std-zero-sobolev]]; [[thm:std-mazzeo-melrose]] (5) and the closing sentences of a few
other items draw short consequences of the quoted statements, each with its reason. Each published result is cited by
its source, with its number and its page where given. Pages are those of the arXiv versions listed in the references;
the arXiv text of [BGP] carries the book's page numbers, [See64] and [MM87] are cited by their journal pages, [Mel93] by
the page of the author's online edition (version 5.0E, 1993), [Hö90], [RS1] and [Tre19] by the pages of the printed
books, and [DLMF] by equation number. Quotation marks enclose the source's own wording, transcribed into this edition's
typography; an ellipsis marks words of the statement left out because no proof here depends on them. Inside each item
the letters are the source's.

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

**Theorem {#thm:std-hormander-cauchy}** (The Cauchy problem for wave operators on Minkowski space; proved below from
[BW15, Definition 7 and Theorem 8, p. 13] and [BGP, Definition 3.4.1, pp. 88–89; Corollary 3.4.3, p. 89].) Let
M = ℝ^(1+n) with the Minkowski metric and the Minkowski time t, and write J_±(A) = A + J_±(0) for the causal future and
past of A ⊂ M. Let P be a normally hyperbolic operator ([[def:std-normally-hyperbolic]]) acting on ℂ^N-valued functions
on M, with smooth coefficients. Let s ∈ ℤ, t0 ∈ ℝ and f ∈ H^(s−1)_loc(M; ℂ^N) with supp f ⊂ {t ≥ t0}. Then there is exactly one
u ∈ 𝒟′(M; ℂ^N) with Pu = f and supp u ⊂ {t ≥ t0}; it lies in H^(s)_loc(M; ℂ^N), and supp u ⊂ J_+(supp f).

If the principal symbol of a second-order operator Q is the dual metric function times the identity, then Q or −Q is
normally hyperbolic, the sign depending only on the convention for principal symbols, and the theorem applies to Q
with f replaced by ±f.

The proof uses the two results (1) and (2) below and the estimate (3), which is proved from (2). Distributions act on
test functions through the bilinear pairing ∫ φ · u dV, and P^* denotes the formally dual operator,
∫ φ · (Pψ) dV = ∫ (P^*φ) · ψ dV ([BW15, Section 1.4.2, p. 6] writes P† for it). In the coordinates of
[[def:std-normally-hyperbolic]], with the constant Minkowski g^(ij),

    P = −Σ g^(ij) ∂²/∂x^i∂x^j + Σ A_j ∂/∂x^j + B_1,    P^*φ = −Σ g^(ij) ∂²φ/∂x^i∂x^j − Σ ∂(A_j^T φ)/∂x^j + B_1^T φ,

T denoting the transpose; so P^* is again normally hyperbolic with smooth coefficients. Here 𝒟 denotes smooth sections
with compact support, and E = M × ℂ^N.

(1) [BGP, Definition 3.4.1, pp. 88–89; Corollary 3.4.3, p. 89]. "A linear map G_+ : 𝒟(M, E) →
C^∞(M, E) satisfying (i) P ∘ G_+ = id_(𝒟(M,E)), (ii) G_+ ∘ P|_(𝒟(M,E)) = id_(𝒟(M,E)), (iii) supp(G_+φ) ⊂
J^M_+(supp(φ)) for all φ ∈ 𝒟(M, E), is called an advanced Green's operator for P. Similarly, a linear map G_− :
𝒟(M, E) → C^∞(M, E) satisfying (i), (ii), and (iii′) supp(G_−φ) ⊂ J^M_−(supp(φ)) for all φ ∈ 𝒟(M, E) instead of
(iii) is called a retarded Green's operator for P." Corollary 3.4.3: "Let M be a globally hyperbolic Lorentzian
manifold. Let P be a normally hyperbolic operator acting on sections in a vector bundle E over M. Then there exist
unique advanced and retarded Green's operators G_± : 𝒟(M, E) → C^∞(M, E) for P." We use (1) for P and for P^*.

(2) [BW15, Definition 7 and Theorem 8, p. 13]. [BW15] considers a wave operator P (a second-order operator whose
principal symbol is given by the metric, P = −Σ g^(ij) ∂²/∂x^i∂x^j + lower order terms, [BW15, Section 1.8, p. 12])
acting on sections of a vector bundle S with a Riemannian or Hermitian metric and a compatible connection ∇, over a
globally hyperbolic manifold with a Cauchy temporal function t, in which the metric is g = −β dt² + g_t (p. 3);
Σ_s := t⁻¹(s), and H^k(Σ_s) is the Sobolev space of [BW15, Section 1.6, pp. 6–8]. Definition 7: "Given a Cauchy
temporal function t, we briefly write E_k(u, s) := E_k(u, Σ_s) = ‖u|_(Σ_s)‖²_(H^k(Σ_s)) + ‖β^(−1/2)∇_t u‖²_(H^(k−1)(Σ_s))."
Theorem 8: "Let [T0, T1] ⊂ t(M), let K ⊂ M be compact, and let k ∈ ℝ. Then there exists a constant C > 0 such that

    E_k(u, t1) ≤ E_k(u, t0) · e^(C(t1−t0)) + ∫_(t0)^(t1) e^(C(t1−s)) ‖Pu‖²_(H^(k−1)(Σ_s)) ds      (4)

holds for all t0, t1 ∈ [T0, T1] with t0 < t1 and for all u ∈ FE^(k+1)_sc(M, t; S) with supp(u) ⊂ J(K) and
Pu ∈ C⁰_sc(t(M), H^(k−1)(Σ•))." Here J(K) = J_+(K) ∪ J_−(K) (p. 4), and FE^(k+1)_sc(M, t; S) is the space of finite
(k + 1)-energy sections [BW15, Definition 1, p. 9]; the proof of [BW15, Corollary 12, p. 15] applies (4) to every
smooth u with supp u ⊂ J(K), and so do we. On M = ℝ^(1+n) take S = M × ℂ^N with the standard Hermitian metric and the
trivial connection, and t the Minkowski time: then β = 1, g_t is the Euclidean metric, Σ_s = {s} × ℝⁿ and ∇_t = ∂_t.
Let B ⊂ ℝⁿ be a closed ball and j ≥ 0 an integer. On functions on Σ_s supported in B, ‖·‖_(H^j(Σ_s)) is equivalent,
with constants independent of s, to ‖v‖_(H^j) := (Σ_(|γ|≤j) ‖∂^γ v‖²_(L²(ℝⁿ)))^(1/2): by [BW15, Section 1.6.2, p. 7]
it is the norm of the double of a larger closed ball, the same for every s; by [BW15, Section 1.6.1, p. 7], "for
k ∈ ℕ_0, a norm equivalent to ‖·‖_(H^k(Σ)) is given by ‖u‖² = Σ_(ℓ=0)^k ‖∇^ℓ u‖²_(L²(Σ))"; and for v supported in B
these terms are Euclidean, with |∇^ℓ v|² between Σ_(|γ|=ℓ) |∂^γ v|² and ℓ! times it.

(3) *The slab estimate.* For t0 < t1 let S(t0, t1) := {t0 < t < t1} ⊂ M and, for an integer k ≥ 0,
‖v‖_(k,S(t0,t1)) := (Σ_(|α|≤k) ‖∂^α v‖²_(L²(S(t0,t1))))^(1/2), α ranging over the multi-indices in (t, x). For a
function u on M write u(s) := u(s, ·). Let K ⊂ M be compact, t0 < t1 and k ≥ 1 an integer. There is C such that

    ‖u‖²_(k,S(t0,t1)) ≤ C (‖u(t0)‖²_(H^k) + ‖∂_t u(t0)‖²_(H^(k−1)) + ‖Pu‖²_(k−1,S(t0,t1)))      {#eq:std-slab}

for every smooth u with supp u ⊂ J(K); and [[eq:std-slab]] also holds with u(t1), ∂_t u(t1) in place of u(t0),
∂_t u(t0).

*Proof of (3).* The set L := J(K) ∩ {t0 ≤ t ≤ t1} is compact, as J_±(K) = K + J_±(0). Let B be a closed ball
containing the projection of L to ℝⁿ, so that u(s) is supported in B for s ∈ [t0, t1]; the coefficients of P and all
their derivatives are bounded on L. Put e(s) := ‖u(s)‖²_(H^k) + ‖∂_t u(s)‖²_(H^(k−1)). By (2), with [T0, T1] := [t0, t1],
applied to the pairs (t0, s), and by the equivalence of norms,

    e(s) ≤ C (e(t0) + ∫_(t0)^(t1) ‖(Pu)(σ)‖²_(H^(k−1)) dσ) ≤ C (e(t0) + ‖Pu‖²_(k−1,S(t0,t1))),      t0 ≤ s ≤ t1,

the second inequality because ‖(Pu)(σ)‖_(H^(k−1)) involves x-derivatives only. For 1 ≤ ℓ ≤ k let N_ℓ be the sum of
‖∂_t^i ∂_x^γ u‖²_(L²(S(t0,t1))) over i ≤ ℓ and i + |γ| ≤ k. Then N_k = ‖u‖²_(k,S(t0,t1)), and N_1 ≤ ∫_(t0)^(t1) e(s) ds.
In the form of P displayed above, ∂_t² u = Pu + Δ_x u − Σ_j A_j ∂u/∂x^j − B_1 u, with x⁰ = t. For 2 ≤ i ≤ k and
i + |γ| ≤ k apply ∂_t^(i−2) ∂_x^γ: the term from Pu is a derivative of Pu of order at most k − 2; the term from Δ_x u
is a sum of derivatives of u of order at most k with at most i − 2 derivatives in t; by Leibniz's rule the remaining
terms are derivatives of u of order at most k − 1 with at most i − 1 derivatives in t, times functions bounded on L.
So N_ℓ ≤ C (N_(ℓ−1) + ‖Pu‖²_(k−1,S(t0,t1))) for 2 ≤ ℓ ≤ k, and

    ‖u‖²_(k,S(t0,t1)) ≤ C (∫_(t0)^(t1) e(s) ds + ‖Pu‖²_(k−1,S(t0,t1))) ≤ C (e(t0) + ‖Pu‖²_(k−1,S(t0,t1))),

which is [[eq:std-slab]]. (This is the argument of the proof of [BW15, Corollary 12, p. 15], written for the norm
‖·‖_(k,S(t0,t1)).) For the data at t1, apply this to ũ(t, x) := u(−t, x): it satisfies P̃ũ(t, x) = (Pu)(−t, x) for the
operator P̃ obtained from P by the substitution t ↦ −t, which is normally hyperbolic with smooth coefficients, and
supp ũ ⊂ J(K̃) with K̃ the image of K; the slab S(t0, t1) becomes S(−t1, −t0). ∎

*Proof.* *Uniqueness.* For every p ∈ M the set {t ≥ t0} ∩ J_−(p) is compact, so a distribution supported in
{t ≥ t0} has past compact support; by [[thm:std-bgp-cauchy]] (2), Pu = 0 and supp u ⊂ {t ≥ t0} imply u = 0.

*Reduction to compact support.* Let (χ_j) be a locally finite smooth partition of unity on M by functions with
compact supports, and f_j := χ_j f ∈ H^(s−1)(ℝ^(1+n); ℂ^N). Suppose that for every j there is u_j ∈ H^(s)_loc with
Pu_j = f_j and supp u_j ⊂ J_+(supp f_j). A compact set L meets J_+(supp f_j) only if supp f_j meets the compact set
J_−(L) ∩ {t ≥ t0}, so only finitely many u_j are nonzero near L. Hence u := Σ_j u_j lies in H^(s)_loc, Pu = f, and
supp u ⊂ ⋃_j J_+(supp f_j) ⊂ supp f + J_+(0) ⊂ {t ≥ t0}.

So let g ∈ H^(s−1)(ℝ^(1+n); ℂ^N) have compact support K, and let G_± and G^*_± be the Green's operators of P and of
P^* given by (1).

*The case s ≥ 1.* Let ρ_ε be a standard mollifier and g_k := ρ_(1/k) ∗ g. It is smooth, supported in the closed
(1/k)-neighbourhood K_k of K, and g_k → g in H^(s−1). Put u_k := G_+ g_k: it is smooth, Pu_k = g_k and
supp u_k ⊂ J_+(K_k) ⊂ J_+(K_1). Fix T0 < min_(K_1) t and T1 > T0. The functions u_k − u_l are smooth, supported in
J_+(K_1) ⊂ J(K_1) ∩ {t > T0}, and so vanish with their t-derivatives on {t = T0}. By [[eq:std-slab]] of order s, with
K_1 in place of K and (T0, T1) in place of (t0, t1),

    ‖u_k − u_l‖_(s,S(T0,T1)) ≤ C ‖g_k − g_l‖_(s−1,S(T0,T1)) ≤ C ‖g_k − g_l‖_(H^(s−1)(ℝ^(1+n))),

the last norm being equivalent, for the integer s − 1 ≥ 0, to the sum of the L²-norms of the derivatives of order at
most s − 1, by Plancherel's theorem.

As T1 is arbitrary and u_k = 0 for t < T0, (u_k) converges in H^(s)_loc(M) to some u with Pu = g, and
supp u ⊂ ⋂_k (K_k + J_+(0)) = K + J_+(0) = J_+(K).

*The case s ≤ 0.* Put m := 1 − s ≥ 1, so g ∈ H^(−m). Let χ ∈ C_c^∞(M) equal 1 near K. For φ ∈ 𝒟(M; ℂ^N) put

    u(φ) := g(χ G^*_− φ).

If supp φ lies in a compact set L, choose T1 > max_L t and T0 < min_(supp χ) t. Then w := G^*_− φ is smooth,
P^* w = φ, and w is supported in J_−(L) ⊂ J(L) ∩ {t ≤ max_L t}, so w and ∂_t w vanish on {t = T1}. By [[eq:std-slab]]
for P^*, of order m, with the data at T1, with L in place of K and (T0, T1) in place of (t0, t1),
‖w‖_(m,S(T0,T1)) ≤ C ‖φ‖_(m−1,S(T0,T1)) ≤ C ‖φ‖_(H^(m−1)); as χw is supported in {T0 < t < T1},

    |u(φ)| ≤ ‖g‖_(H^(−m)) ‖χw‖_(H^m) ≤ C_L ‖φ‖_(H^(m−1)),      supp φ ⊂ L.

So u is a distribution, and ψu ∈ H^(1−m) for every ψ ∈ C_c^∞(M), that is, u ∈ H^(s)_loc. For φ ∈ 𝒟,
G^*_− P^* φ = φ by (1) (ii), so (Pu)(φ) = u(P^*φ) = g(χφ) = g(φ): Pu = g. If supp φ ∩ J_+(K) = ∅, then
J_−(supp φ) ∩ K = ∅, so χ G^*_− φ vanishes near K and u(φ) = 0; hence supp u ⊂ J_+(K). ∎

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

**Theorem {#thm:std-bh17-embedding}** ([BH17, Theorem 7.27, p. 56].) "Let Ω be a nonempty bounded open subset of ℝⁿ with
Lipschitz continuous boundary. Suppose 1 ≤ p, q < ∞ (p does not need to be less than or equal to q) and 0 ≤ t ≤ s
satisfy s − n/p ≥ t − n/q. Then W^(s,p)(Ω) ↪ W^(t,q)(Ω). In particular, W^(s,p)(Ω) ↪ W^(t,p)(Ω)." For an integer
k ≥ 0, W^(k,p)(Ω) is the space of u ∈ L^p(Ω) with ‖u‖_(W^(k,p)(Ω)) := Σ_(|ν|≤k) ‖∂^ν u‖_(L^p(Ω)) < ∞ [BH17,
Definition 7.11, p. 50]; W^(0,q)(Ω) = L^q(Ω).

**Theorem {#thm:std-moser-taylor}** ([GO13, Theorem 1, (2), p. 2].) With J^s := (1 − Δ)^(s/2) on ℝⁿ (p. 1): "Let
1/2 < r < ∞, 1 < p_1, p_2, q_1, q_2 ≤ ∞ satisfy 1/r = 1/p_1 + 1/q_1 = 1/p_2 + 1/q_2. Given s > max(0, n/r − n) or
s ∈ 2ℕ, there exists a constant C = C(n, s, r, p_1, q_1, p_2, q_2) < ∞ such that for all f, g ∈ 𝒮(ℝⁿ) we have …

    ‖J^s(fg)‖_(L^r(ℝⁿ)) ≤ C(s, n) [‖f‖_(L^(p_1)(ℝⁿ)) ‖J^s g‖_(L^(q_1)(ℝⁿ))
                                   + ‖J^s f‖_(L^(p_2)(ℝⁿ)) ‖g‖_(L^(q_2)(ℝⁿ))]      (2)."

For r = 2, p_1 = q_2 = ∞ and q_1 = p_2 = 2 the condition on s is s > 0, and (2) reads, for f, g ∈ 𝒮(ℝⁿ),

    ‖fg‖_(H^s) ≤ C (‖f‖_(L^∞) ‖g‖_(H^s) + ‖f‖_(H^s) ‖g‖_(L^∞)),      ‖u‖_(H^s) := ‖J^s u‖_(L²).      {#eq:std-moser}

**Corollary {#cor:std-moser-product}** (Moser's product estimate.) Let s ≥ 1 be an integer.

(1) If f, g ∈ H^s(ℝⁿ) ∩ L^∞(ℝⁿ), then fg ∈ H^s(ℝⁿ) and [[eq:std-moser]] holds with the same constant.

(2) Let N be a compact manifold without boundary, of dimension d, with a smooth Riemannian metric, let k ≥ 0, and let
X := ℝ^k × N carry the product metric and its measure. Let W_1, …, W_q be smooth vector fields on N spanning TN at
every point, 𝒱 := {∂_(z_1), …, ∂_(z_k), W_1, …, W_q}, and let H^s(X) be the space of u ∈ L²(X) with V_1 ⋯ V_j u ∈
L²(X) for all V_i ∈ 𝒱 and j ≤ s, normed by the sum of the L²-norms of these derivatives. There is C such that, for
f, g ∈ H^s(X) ∩ L^∞(X), fg ∈ H^s(X) and

    ‖fg‖_(H^s(X)) ≤ C (‖f‖_(L^∞) ‖g‖_(H^s(X)) + ‖f‖_(H^s(X)) ‖g‖_(L^∞)).

(3) Let 0 ≤ χ ∈ C_c^∞(ℝ^k) with Σ_(j∈ℤ^k) χ(z − j) = 1, put χ_j(z, y) := χ(z − j) on X and
‖u‖_(H^s_ul(X)) := sup_j ‖χ_j u‖_(H^s(X)). Then the bound of (2) holds with the uniformly local norms in place of the
H^s(X)-norms, for all f, g ∈ L^∞(X) whose uniformly local norms are finite.

*Proof.* (1) For integer s the norm ‖J^s u‖_(L²) is equivalent to (Σ_(|α|≤s) ‖∂^α u‖²_(L²))^(1/2), by Plancherel's
theorem. Let θ ∈ C_c^∞(ℝⁿ) with 0 ≤ θ ≤ 1 and θ = 1 near 0, let ρ_ε be a standard mollifier, and put
f_ℓ := θ(·/ℓ)(ρ_(1/ℓ) ∗ f) and g_ℓ := θ(·/ℓ)(ρ_(1/ℓ) ∗ g). These are Schwartz functions with ‖f_ℓ‖_(L^∞) ≤ ‖f‖_(L^∞)
and ‖g_ℓ‖_(L^∞) ≤ ‖g‖_(L^∞), and f_ℓ → f, g_ℓ → g in H^s. Indeed, by Leibniz's rule
∂^α(θ(·/ℓ)v) − θ(·/ℓ)∂^α v is a sum of terms ℓ^(−|β|)(∂^β θ)(·/ℓ) ∂^(α−β) v with β ≠ 0; so multiplication by
θ(·/ℓ), ℓ ≥ 1, is bounded on H^s uniformly in ℓ, and θ(·/ℓ)v → v in H^s for each fixed v ∈ H^s, as
θ(·/ℓ)∂^α v → ∂^α v in L² by dominated convergence. Writing f_ℓ − f = θ(·/ℓ)(ρ_(1/ℓ) ∗ f − f) + (θ(·/ℓ)f − f), the
first term tends to 0 in H^s because ρ_(1/ℓ) ∗ f → f in H^s, and the second by the fixed-v case. So the right side of [[eq:std-moser]] for (f_ℓ, g_ℓ) is at most ‖f‖_(L^∞)‖g_ℓ‖_(H^s) +
‖f_ℓ‖_(H^s)‖g‖_(L^∞), which converges to the right side for (f, g). Further ‖f_ℓ g_ℓ − fg‖_(L²) ≤ ‖f_ℓ − f‖_(L²)
‖g‖_(L^∞) + ‖f(g_ℓ − g)‖_(L²), and along a subsequence g_ℓ → g almost everywhere with |f(g_ℓ − g)| ≤ 2‖g‖_(L^∞)|f|,
so f_ℓ g_ℓ → fg in L² and J^s(f_ℓ g_ℓ) → J^s(fg) as tempered distributions. The J^s(f_ℓ g_ℓ) are bounded in L²; a
subsequence converges weakly in L², its limit is J^s(fg), and its norm is at most the limit inferior of the norms.

(2) Choose charts κ_i : U_i → ℝ^d, i = 1, …, I, of N, functions φ_i ∈ C_c^∞(U_i) with Σ_i φ_i² = 1 and ψ_i ∈
C_c^∞(U_i) equal to 1 near supp φ_i. For v on X supported in ℝ^k × supp ψ_i let v^(i) := v ∘ (id × κ_i⁻¹), extended
by zero to ℝ^(k+d). On ℝ^k × supp ψ_i the fields of 𝒱 have, in the coordinates (z, κ_i), coefficients bounded with
all their derivatives, they span the tangent spaces, and the measure has a density bounded above and below; so there
is C with C⁻¹‖v‖_(H^s(X)) ≤ ‖v^(i)‖_(H^s(ℝ^(k+d))) ≤ C‖v‖_(H^s(X)) for such v, and multiplication by φ_i or ψ_i is
bounded on H^s(X). As u = Σ_i φ_i(φ_i u), ‖u‖_(H^s(X)) ≤ C Σ_i ‖(φ_i u)^(i)‖_(H^s). Now (φ_i fg)^(i) =
(ψ_i f)^(i) (φ_i g)^(i) lies in H^s(ℝ^(k+d)) by (1), so φ_i fg ∈ H^s(X) and fg = Σ_i φ_i(φ_i fg) ∈ H^s(X); and (1)
gives

    ‖fg‖_(H^s(X)) ≤ C Σ_i (‖f‖_(L^∞) ‖(φ_i g)^(i)‖_(H^s) + ‖(ψ_i f)^(i)‖_(H^s) ‖g‖_(L^∞))
                  ≤ C (‖f‖_(L^∞) ‖g‖_(H^s(X)) + ‖f‖_(H^s(X)) ‖g‖_(L^∞)).

(3) Let supp χ ⊂ {|z|_∞ ≤ R}, R a positive integer, and χ̃_j := Σ_(|l−j|_∞ ≤ 2R) χ_l. Then χ̃_j = 1 on supp χ_j,
0 ≤ χ̃_j ≤ 1, χ_j fg = (χ̃_j f)(χ_j g), and ‖χ̃_j f‖_(H^s(X)) ≤ (4R + 1)^k ‖f‖_(H^s_ul(X)). Applying (2) to χ̃_j f and
χ_j g and taking the supremum over j gives the bound. ∎

**Theorem {#thm:std-gn-moser}** (Products of derivatives.) Let s ≥ 1 be an integer.

(1) There is C, depending only on n and s, such that for f, g ∈ H^s(ℝⁿ) ∩ L^∞(ℝⁿ) and multi-indices α, β with
|α| + |β| ≤ s, ∂^α f ∂^β g ∈ L²(ℝⁿ) and

    ‖∂^α f ∂^β g‖_(L²) ≤ C (‖f‖_(L^∞) ‖g‖_(H^s) + ‖f‖_(H^s) ‖g‖_(L^∞)).      {#eq:std-gn-moser}

(2) In the setting of [[cor:std-moser-product]] (2) there is C such that for f, g ∈ H^s(X) ∩ L^∞(X) and V_1, …, V_p,
V′_1, …, V′_q ∈ 𝒱 with p + q ≤ s,

    ‖(V_1 ⋯ V_p f)(V′_1 ⋯ V′_q g)‖_(L²(X)) ≤ C (‖f‖_(L^∞) ‖g‖_(H^s(X)) + ‖f‖_(H^s(X)) ‖g‖_(L^∞)).

*Proof.* (1) We use the norm ‖u‖²_(H^s) := Σ_(|γ|≤s) ‖∂^γ u‖²_(L²), equivalent to that of [[eq:std-moser]] by
Plancherel's theorem. Splitting f and g into real and imaginary parts, which increases neither norm, we may take f
and g real-valued, at the cost of a factor 4 in C. If |α| + |β| = s′ < s, the claim at the order s′ (or, for s′ = 0,
‖fg‖_(L²) ≤ ‖f‖_(L^∞) ‖g‖_(L²)) gives the claim at the order s, as ‖·‖_(H^(s′)) ≤ ‖·‖_(H^s). So let |α| + |β| = s, and
let f and g first be real Schwartz functions.

*An interpolation inequality.* For 0 ≤ j ≤ s put p_j := 2s/j (p_0 := ∞) and a_j := max_(|γ|=j) ‖∂^γ f‖_(L^(p_j)).
Let 1 ≤ j ≤ s − 1 and p := p_j, so 2 < p ≤ 2s. Let |γ| = j, write ∂^γ = ∂_k ∂^(γ′) with |γ′| = j − 1, and put
u := ∂^(γ′) f. The function τ ↦ τ|τ|^(p−2) on ℝ is C¹ with derivative (p − 1)|τ|^(p−2), so integration by parts gives

    ∫ |∂_k u|^p dx = ∫ ∂_k u · ∂_k u |∂_k u|^(p−2) dx = −(p − 1) ∫ u · ∂_k² u · |∂_k u|^(p−2) dx.

Hölder's inequality with the exponents p_(j−1), p_(j+1) and p/(p − 2), whose reciprocals add to
(j − 1)/(2s) + (j + 1)/(2s) + 1 − j/s = 1, gives ‖∂_k u‖^p_(L^p) ≤ (p − 1) ‖u‖_(L^(p_(j−1))) ‖∂_k² u‖_(L^(p_(j+1)))
‖∂_k u‖^(p−2)_(L^p). As ∂_k² u is a derivative of f of order j + 1, this is a_j² ≤ 2s a_(j−1) a_(j+1). If f ≠ 0,
every a_j is positive, since a Schwartz function whose derivatives of order j all vanish is a polynomial, hence 0.
Then d_j := log a_j + ½ j² log(2s) satisfies d_(j−1) + d_(j+1) − 2d_j ≥ 0 for 1 ≤ j ≤ s − 1, so (d_j) is convex on
{0, 1, …, s} and d_j ≤ (1 − j/s) d_0 + (j/s) d_s, that is,

    a_j ≤ (2s)^(j(s−j)/2) a_0^(1−j/s) a_s^(j/s),      0 ≤ j ≤ s,

which holds trivially if f = 0. Here a_0 = ‖f‖_(L^∞) and a_s ≤ ‖f‖_(H^s); the same holds for g.

*The product.* Put σ := |α|/s ∈ [0, 1], so |β|/s = 1 − σ. Hölder's inequality with the exponents p_(|α|) and p_(|β|),
whose reciprocals add to 1/2, and the interpolation inequality for f and for g give

    ‖∂^α f ∂^β g‖_(L²) ≤ ‖∂^α f‖_(L^(p_(|α|))) ‖∂^β g‖_(L^(p_(|β|)))
                       ≤ C (‖f‖_(L^∞)^(1−σ) ‖f‖_(H^s)^σ)(‖g‖_(L^∞)^σ ‖g‖_(H^s)^(1−σ))
                       = C (‖f‖_(H^s) ‖g‖_(L^∞))^σ (‖f‖_(L^∞) ‖g‖_(H^s))^(1−σ),

and x^σ y^(1−σ) ≤ σx + (1 − σ)y for x, y ≥ 0 gives [[eq:std-gn-moser]].

*General f and g.* Let f_ℓ, g_ℓ be the Schwartz functions of the proof of [[cor:std-moser-product]] (1); they are real
when f and g are, ‖f_ℓ‖_(L^∞) ≤ ‖f‖_(L^∞), ‖g_ℓ‖_(L^∞) ≤ ‖g‖_(L^∞), and f_ℓ → f, g_ℓ → g in H^s. Then ∂^α f_ℓ → ∂^α f
and ∂^β g_ℓ → ∂^β g in L², hence almost everywhere along a subsequence, and Fatou's lemma gives
‖∂^α f ∂^β g‖_(L²) ≤ lim inf ‖∂^α f_ℓ ∂^β g_ℓ‖_(L²), which is at most the right side of [[eq:std-gn-moser]].

(2) Let κ_i, φ_i, ψ_i and v ↦ v^(i) be as in the proof of [[cor:std-moser-product]] (2), and
Π := (V_1 ⋯ V_p f)(V′_1 ⋯ V′_q g). As Σ_i φ_i² = 1, ‖Π‖²_(L²(X)) = Σ_i ‖φ_i Π‖²_(L²(X)). As ψ_i = 1 near supp φ_i,
on a neighbourhood of supp φ_i we have Π = (V_1 ⋯ V_p(ψ_i f))(V′_1 ⋯ V′_q(ψ_i g)). In the coordinates (z, κ_i) on
ℝ^k × supp ψ_i, V_1 ⋯ V_p = Σ_(|γ|≤p) c_γ ∂^γ and V′_1 ⋯ V′_q = Σ_(|δ|≤q) e_δ ∂^δ with coefficients bounded there,
the fields of 𝒱 having coefficients bounded with all their derivatives. So (φ_i Π)^(i) is a finite sum of terms
b ∂^γ F_i ∂^δ G_i with b bounded, |γ| + |δ| ≤ s, F_i := (ψ_i f)^(i) and G_i := (ψ_i g)^(i). By (1), and as the
measure has a density bounded above and below,

    ‖φ_i Π‖_(L²(X)) ≤ C (‖F_i‖_(L^∞) ‖G_i‖_(H^s) + ‖F_i‖_(H^s) ‖G_i‖_(L^∞)).

Finally ‖F_i‖_(L^∞) ≤ C ‖f‖_(L^∞) and ‖F_i‖_(H^s) ≤ C ‖ψ_i f‖_(H^s(X)) ≤ C ‖f‖_(H^s(X)), by the chart comparison and
the boundedness of multiplication by ψ_i recorded in that proof; likewise for G_i. ∎

**Theorem {#thm:std-kato-ponce}** ([GO13, p. 1].) Grafakos and Oh recall the commutator estimate of Kato and Ponce
[KP88]: with J^s := (1 − Δ)^(s/2) on ℝⁿ, for Schwartz functions f and g,

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

**Theorem {#thm:std-sbg-calculus}** ([Hin26d, Definitions 1.1–4.20, Lemma 3.24, Propositions 3.2–4.22, Remarks
3.13–3.48, Theorems 3.21–3.52, (1.6), (3.2), (3.26), (3.28), (4.24a–b), pp. 2–75].) On a smooth manifold M of any
dimension n, without boundary, the
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
all weights w′ … and for all s ∈ ℝ, the operator P : w′ H^s_𝒱(M) → w w′ H^(s−m)_𝒱(M) is Fredholm." By [Hin26d,
Definition 3.27, p. 41], 𝒱 is fully symbolic if, equivalently to two other conditions given there, "For all ϵ > 0
there exists a compact subset K ⊂ M so that ρ < ϵ on M ∖ K", ρ being a scaling weight (S2).

(S6) Regularity of symbols [Hin26d, Remark 3.33, p. 45]: "one only needs uniform bounds by ⟨ξ⟩^(m−|γ|) on
|(ρ_α ∂_(x_α))^β ∂_ξ^γ a_α(x_α, ξ)|, corresponding to '𝒱-regular' symbols", together with their derivatives for the
spaces with k orders of 𝒲-regularity.

(S7) Parameterised structures [Hin26d, Definitions 3.58–3.59, p. 59].

(S8) Variable orders [Hin26d, Definition 4.6, p. 66]: for m, l ∈ S⁰(𝒱T*M),

    ρ^(−l) S^m(𝒱T*M) := ρ^(−l) λ^(−m) ⋂_(δ∈(0,1/2)) S⁰_(1−δ,δ)(𝒱T*M),

where λ is an elliptic weight [Hin26d, Lemma 3.24 (2), p. 40]: "Let λ ∈ S^(−1)(𝒱T*M) with λ > 0 and
λ^(−1) ∈ S¹(𝒱T*M). Then λ is a weight on (𝒱T*M, 𝓑*). Moreover, such functions λ exist." Here 𝓑* is the phase
space b.g. structure of [Hin26d, Definition 3.23, p. 40]. Further, w Ψ^(m,l)_𝒱(M) := {Op_𝒱(a) + R}. The principal
symbol is taken modulo ⋂_δ w ρ^(−l+1−2δ) S^(m−1+2δ) (4.10), and
w H^(m,l)_𝒱(M) := {u ∈ w ρ^(inf l) H^(inf m)_𝒱(M) : Au ∈ L²(M)} for a fixed elliptic A. On the same page [Hin26d]
says that "Theorem 3.51 thus remains valid, mutatis mutandis" for the (1 − δ, δ) classes, and, for variable orders,
that "by mimicking the proof of Proposition 4.2, one shows … (wH^(m,l)_𝒱(M))* = w⁻¹H^(−m,−l)_𝒱(M)".

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

(S12) Compatible structures [Hin26d, Definition 1.3 (4), p. 6; Definition 3.1, p. 27; Proposition 3.2, p. 28;
pp. 32, 36, 52]. The large operator Lie algebra 𝒱′ consists of "all smooth vector fields V on M so that the components
V^i_α in each coordinate chart are uniformly (in α) bounded in absolute value, and so are the derivatives
(ρ_(α,1)∂_1)^(γ_1) ⋯ (ρ_(α,n)∂_n)^(γ_n)((φ_α)_* V)^j for any fixed γ ∈ ℕ^n_0" (Definition 1.3 (4)), the components
being those of (φ_α)_* V = Σ V^i_α ρ_(α,i) ∂_i. Definition 3.1: "Two scaled b.g. structures 𝓑^× = {(U_α, φ_α, ρ_α)}
and 𝓑̃^× = {(Ũ_α̃, φ̃_α̃, ρ̃_α̃)} are compatible if the b.g. structures {(U_α, φ_α)} and {(Ũ_α̃, φ̃_α̃)} are compatible
and if, moreover, there exist constants C_γ < ∞ so that the transition functions τ_(αα̃) := φ_α ∘ φ̃_α̃⁻¹ and
τ_(α̃α) := φ̃_α̃ ∘ φ_α⁻¹ satisfy

    |∂^γ ρ̃_(α̃,i) ∂_i τ^j_(αα̃)| ≤ C_γ ρ_(α,j),   |∂^γ ρ_(α,i) ∂_i τ^j_(α̃α)| ≤ C_γ ρ̃_(α̃,j)
    ∀ i, j = 1, …, n, γ ∈ ℕ^n_0,      (3.1)

…". Proposition 3.2: "Let 𝓑^× and 𝓑̃^× be two scaled b.g. structures on M. Then the operator Lie algebras 𝒱 and 𝒱̃
of 𝓑^× and 𝓑̃^× are equal if and only if 𝓑^× and 𝓑̃^× are compatible. In particular, 𝒱 = 𝒱̃ implies the equality also
of the coefficient Lie algebras and large operator Lie algebras of 𝓑^× and 𝓑̃^×." Moreover Diff^m_𝒱(M) "is unchanged
when passing to a compatible scaled b.g. structure" (p. 32); the weighted Sobolev spaces "are unchanged when defined
with respect to a scaled b.g. structure compatible with 𝓑^×" (p. 36); and "wΨ^m_𝒱(M) only depends on 𝒱 and m, w"
(p. 52).

(S13) The secondary structure [Hin26d, pp. 28 and 36; Proposition 3.3, p. 29; Remark 3.48, p. 52]. The charts of ρ𝓑
are obtained from those of 𝓑^× by subdividing (−3/2, 3/2)^n in the chart φ_α into overlapping cuboids with side
lengths 4/(D · D_(α,i)), where D_(α,i) is "the largest integer with ρ_(α,i) D_(α,i) ≤ 1, or D_(α,i) = 4, whichever is
larger" and D ∈ ℕ is a fixed number, each cuboid being mapped onto (−2, 2)^n by a monotone affine map in each
coordinate (p. 28). Proposition 3.3: "In the above notation, ρ𝓑 is a b.g. structure provided we choose D large enough.
If 𝒱, resp. 𝒱′ denote the operator, resp. large operator Lie algebra of 𝓑^×, then

    𝒱′ = C^∞_(uni,ρ𝓑)(M; TM) = 𝒱 ⊗_(C^∞_(uni,𝓑)(M)) C^∞_(uni,ρ𝓑)(M)."      (3.2)

On p. 36: "H^s_𝒱(M) is the uniform Sobolev space for the secondary b.g. structure ρ𝓑; thus, recalling the large
operator Lie algebra 𝒱′ from Definition 1.3, we have H^s_(𝒱′)(M) = H^s_𝒱(M)." Remark 3.48: "Recall Proposition 3.3,
and define Ψ^m_(𝒱′)(M) using Definition 3.43 with respect to the b.g. structure ρ𝓑 and the trivial scaling (i.e. all
scalings are 1). (Thus, the operator and coefficient Lie algebras coincide and are equal to 𝒱′.) Then
Ψ^m_𝒱(M) ⊂ Ψ^m_(𝒱′)(M); similarly for spaces of weighted ps.d.o.s. We stress that the validity of this inclusion rests
in particular on the fact that we do not require residual 𝒱′-ps.d.o.s to be localized near the diagonal …".

(S14) Vector bundles [Hin26d, Remark 3.13, p. 34; (3.8), p. 32; Remark 3.46, p. 52]. Remark 3.13: "The vector bundles
of interest are vector bundles of bounded geometry E → M [Shu92, §A.1.1], which means that for each α ∈ 𝒜 a
trivialization E|_(U_α) ≅ U_α × ℂ^k is chosen so that the transition functions (which are GL(ℂ, k)-valued smooth
functions on U_α ∩ U_β) are uniformly bounded in C^∞. If E, F → M are vector bundles of bounded geometry, then
Diff^m_𝒱(M; E, F) ⊂ Diff^m(M; E, F) is characterized as the subspace of operators which, in the charts U_α and in such
trivializations of E|_(U_α) and F|_(U_α), are matrices of operators of the form (3.8) (with coefficients which are
uniformly bounded in C^∞). We then have a principal symbol map

    σ^m_𝒱 : Diff^m_𝒱(M; E, F) → P^m(𝒱T*M; π^* Hom(E, F))/ρP^(m−1)(𝒱T*M; π^* Hom(E, F))

where π : 𝒱T*M → M is the base projection." The form (3.8) is (φ_α)_* P = Σ_(|γ|≤m) p_(αγ)(x)(ρ_α D)^γ with
(ρ_α D)^γ = Π_j (ρ_(α,j) i⁻¹ ∂_(x^j))^(γ_j), "where the p_(αγ) are uniformly bounded in C^∞((−2, 2)^n)". Remark 3.46: for
such E and F "one defines wΨ^m_𝒱(M; E, F) as sums of matrices of quantizations of symbols of class wS^m in local charts
and residual operators which are smoothing (in the sense of 𝒱-regularity and ρ-decay) between Sobolev spaces of
sections of E, F. We leave the details to the interested reader."

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

**Theorem {#thm:std-mazzeo-melrose}** (Boundedness of the small 0-calculus; [Usu26, Definition 2.1, p. 11; p. 26;
Theorem 5.20 (1), p. 119] and [MM87, Lemma (5.10), p. 284].) Let X be a compact manifold with boundary, of dimension
n + 1, x a boundary defining function and ω a smooth positive density on X.

(1) [Usu26, p. 11]. X²_0 = [X²; ∂Δ] is the blow-up of X² at the boundary of its diagonal Δ; its boundary
hypersurfaces are lf and rf, the lifts of ∂X × X and X × ∂X, and the front face ff_0; Δ_0 is the lifted diagonal,
β_0 : X²_0 → X² the blow-down map and β_(0,R) the lift of the right projection. Definition 2.1: "Let m ∈ ℝ. We denote
by Ψ^m_0(X) the space of operators A ∈ Op(X) whose Schwartz kernels K_A lift via β_0 to elements

    κ_A ∈ 𝒜^((∞,∞,0))_phg I^m(X²_0, Δ_0; r_(ff_0)^(−n−1) β^*_(0,R) D¹_X).

This means that κ_A is a section of r_(ff_0)^(−n−1) β^*_(0,R) D¹_X vanishing to infinite order at the faces lf, rf,
smooth across ff_0, and with an interior conormal singularity of order m along Δ_0." Here Op(X) is the class of
continuous linear operators Ċ^∞(X) → C^(−∞)(X), D¹_X is the density bundle of X, and r_(ff_0) is a boundary defining
function of ff_0.

(2) [Usu26, p. 26 and footnote 6, p. 119]. L²_b(X) is the space of functions on X° that are square integrable with
respect to x⁻¹ω. For an integer k ≥ 0, H^k_0(X) is "the space of L²_b functions u on X such that, for any set
V_1, …, V_j ∈ 𝒱_0(X) with j ≤ k, the weak multiple 0-derivative V_1 ⋯ V_j u is still in L²_b(X)", where 𝒱_0(X)
is the space of smooth vector fields on X vanishing at ∂X, and x^δ H^k_0(X) := {x^δ u : u ∈ H^k_0(X)}, normed by
means of a finite set of 0-vector fields spanning ⁰TX at every point.

(3) [Usu26, Theorem 5.20 (1), p. 119]: "If P ∈ Ψ^m_0(X), then P is bounded as a map x^δ H^(k+m)_0(X) →
x^δ H^k_0(X) for every k and δ." Here m ∈ ℤ and k, k + m ≥ 0 ([Usu26, p. 26]). [Usu26] gives this with the
attribution to [Maz91, Theorem 3.25, Corollary 3.23 and Proposition 3.29] and [Lau03, Theorem 5.2.2].

(4) [MM87, Lemma (5.10), p. 284]: "The space 𝒱_0 of vector fields on X acting on the left factor of X × X lifts under
b into the Lie algebra, 𝒱_l, of those C^∞ vector fields on X ×_0 X tangent to the front and bottom faces and vanishing
at the top face." Here X ×_0 X = X²_0, b = β_0, the top face is lf and the bottom face is rf.

(5) Operators on 0-half-densities. Let ν = x^(−n−1)ω̃, with ω̃ a smooth positive density, be a smooth positive
0-density on X. Then A ↦ (u ↦ ν^(−1/2) A(u ν^(1/2))) maps the operators of [Hin23e, Definition 1.1, p. 3], whose
Schwartz kernels are the elements of I^m(X²_0, diag_0, KD_0) that vanish to infinite order at lb ∪ rb, with
KD_0 = π^*_L(⁰Ω^(1/2)X) ⊗ π^*_R(⁰Ω^(1/2)X) [Hin23e, (1.2)], onto Ψ^m_0(X) of (1). Indeed ν^(1/2) ⊗ ν^(1/2) lifts to a
smooth nowhere vanishing section of KD_0, so these kernels are c ν^(1/2) ⊗ ν^(1/2) with c conormal of order m at Δ_0,
smooth across ff_0 and vanishing to infinite order at lf ∪ rf; the corresponding right density is
c (β^*_(0,R) x)^(−n−1) β^*_(0,R) ω̃, and β^*_(0,R) x = r_(ff_0) r_rf a with a smooth and positive, so the factor
r_rf^(−n−1) is absorbed by the vanishing of c at rf, and conversely.

**Corollary {#cor:std-zero-sobolev}** (All integer orders.) In the setting of [[thm:std-mazzeo-melrose]], for integers
k ≥ 0 and δ ∈ ℝ let x^δ H^(−k)_0(X) be the dual space of x^(−δ) H^k_0(X) for the pairing ⟨u, v⟩ := ∫ u v x⁻¹ω.
Then x^δ L²_b(X) embeds injectively and densely into x^δ H^(−k)_0(X). Let m ≤ 0 be an integer, δ ∈ ℝ and
P ∈ Ψ^m_0(X). For every k ∈ ℤ there is C with

    ‖Pu‖_(x^δ H^k_0(X)) ≤ C ‖u‖_(x^δ H^(k+m)_0(X)),      u ∈ C_c^∞(X°),

so P extends to a bounded map x^δ H^(k+m)_0(X) → x^δ H^k_0(X); for k, k + m ≥ 0 this is the map of
[[thm:std-mazzeo-melrose]] (3).

*Proof.* (a) *Density.* C_c^∞(X°) is dense in x^δ H^j_0(X) for every integer j ≥ 0. Let χ ∈ C^∞(ℝ) vanish on
(−∞, 1] and equal 1 on [2, ∞), and put φ_ε := χ(x/ε). In a collar [0, 1)_x × ∂X the 0-vector fields are combinations
with smooth coefficients of x∂_x and of xY, Y a vector field on ∂X; since (x∂_x)^a φ_ε = ((t∂_t)^a χ)(x/ε) and
xYφ_ε = 0, every product V_1 ⋯ V_l φ_ε with V_i ∈ 𝒱_0(X) and l ≥ 1 is bounded uniformly in ε ∈ (0, 1/2] and is
supported in {ε ≤ x ≤ 2ε}. By Leibniz's rule and dominated convergence, φ_ε v → v in x^δ H^j_0(X) for every
v ∈ x^δ H^j_0(X). The function φ_ε v has compact support in X°, where the 0-vector fields span the tangent spaces, and
mollification in coordinate charts gives approximants in C_c^∞(X°). Since C_c^∞(X°) is dense in x^(−δ)H^j_0(X), the map
taking u ∈ x^δ L²_b(X) to ⟨u, ·⟩ is injective; its range is dense, because x^(−δ) H^j_0(X) is reflexive and an element
of it annihilated by all ⟨u, ·⟩, u ∈ x^δ L²_b(X), vanishes. So C_c^∞(X°) is dense in every x^δ H^k_0(X), k ∈ ℤ.

(b) *Weights.* The lifts of x and of x′ = x ∘ π_R to X²_0 are r_lf r_(ff_0) a and r_rf r_(ff_0) a′ with a, a′ smooth
and positive, so (x/x′)^δ is a smooth positive function times r_lf^δ r_rf^(−δ). Multiplying an element of
𝒜^((∞,∞,0))_phg I^m by it gives again such an element; hence x^(−δ) P x^δ ∈ Ψ^m_0(X). As u ↦ x^δ u maps H^j_0(X)
isometrically onto x^δ H^j_0(X) for j ≥ 0, and by duality (⟨x^δ u, x^(−δ) v⟩ = ⟨u, v⟩) also for j < 0, it suffices to
take δ = 0.

(c) *Transposes and compositions.* Write κ_P = b r_(ff_0)^(−n−1) β^*_(0,R) ω, with b ∈ 𝒜^((∞,∞,0))_phg I^m, so that
K_P(z, z′) = k(z, z′) ω(z′) with β_0^* k = b r_(ff_0)^(−n−1). The transpose P^t, ⟨Pu, v⟩ = ⟨u, P^t v⟩ for
u, v ∈ C_c^∞(X°), has kernel k(z′, z) x(z) x(z′)⁻¹ ω(z′). The exchange of the factors of X² preserves ∂Δ, so it lifts
to a diffeomorphism R of X²_0 that preserves Δ_0 and ff_0 and exchanges lf and rf. The lift of k(z′, z) x(z) x(z′)⁻¹ is
(x/x′)(b ∘ R)((r_(ff_0) ∘ R)/r_(ff_0))^(−n−1) r_(ff_0)^(−n−1), and by (b) the first three factors form an element of
𝒜^((∞,∞,0))_phg I^m; so P^t ∈ Ψ^m_0(X). For V ∈ 𝒱_0(X) the kernel of VP lifts to Ṽ(b r_(ff_0)^(−n−1)) β^*_(0,R) ω,
where Ṽ is the lift of V acting on the left factor; by (4) Ṽ is a smooth vector field tangent to every boundary
hypersurface of X²_0, so Ṽ(b r_(ff_0)^(−n−1)) = (Ṽb − (n + 1)(Ṽ r_(ff_0)/r_(ff_0)) b) r_(ff_0)^(−n−1) with
Ṽ r_(ff_0)/r_(ff_0) smooth and Ṽb ∈ 𝒜^((∞,∞,0))_phg I^(m+1); so VP ∈ Ψ^(m+1)_0(X). Finally Ψ^(m′)_0(X) ⊂ Ψ^m_0(X)
for m′ ≤ m.

(d) *The bounds,* with δ = 0. For u ∈ C_c^∞(X°), Pu ∈ H^j_0(X) for every j ≥ 0, by (3). If k ≥ 0 and k + m ≥ 0, the
bound is (3). If k ≤ 0 and k + m ≤ 0, then for u, v ∈ C_c^∞(X°)

    |⟨Pu, v⟩| = |⟨u, P^t v⟩| ≤ ‖u‖_(H^(k+m)_0) ‖P^t v‖_(H^(−k−m)_0) ≤ C ‖u‖_(H^(k+m)_0) ‖v‖_(H^(−k)_0)

by (3) for P^t, and the bound follows by the density in (a). As m ≤ 0, the remaining case is k > 0 > k + m. Then
‖Pu‖_(H^k_0) is bounded by a constant times the sum of ‖V_1 ⋯ V_j P u‖_(L²_b) over j ≤ k and V_i in a finite
spanning set of 𝒱_0(X); by (c) V_1 ⋯ V_j P ∈ Ψ^(k+m)_0(X), and the previous case, with target order 0 and order
k + m ≤ 0, bounds each term by C‖u‖_(H^(k+m)_0). The extension agrees with the map of (3) on the dense subspace
C_c^∞(X°). ∎

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

**Theorem {#thm:std-analytic-fredholm}** ([RS1, Theorem VI.14, p. 201].) Let D ⊂ ℂ be open and connected, 𝓗 a Hilbert
space, and f : D → 𝓛(𝓗) analytic with f(z) compact for every z ∈ D. Then either (I − f(z))⁻¹ exists for no z ∈ D, or
(I − f(z))⁻¹ exists for all z ∈ D ∖ S, where S is a discrete subset of D; in the second case (I − f(z))⁻¹ is
meromorphic in D and analytic in D ∖ S, its residues at the poles are finite rank operators, and for z ∈ S the
equation f(z)ψ = ψ has a nonzero solution in 𝓗.

Applied to f = −F: if F : D → 𝓛(𝓗) is analytic with compact values and Id + F(z0) is invertible for one z0 ∈ D, then
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

**Theorem {#thm:std-dlmf-modified}** ([DLMF, (10.25.1)–(10.25.3), (10.28.2), (10.30.2), (10.40.1)–(10.40.2), (10.17.1),
(2.1.13)–(2.1.14)].) The modified Bessel equation is z² w″ + z w′ − (z² + ν²) w = 0 (10.25.1). Its standard solutions
are I_ν, defined by the series (10.25.2), and K_ν, characterised by K_ν(z) ∼ (π/(2z))^(1/2) e^(−z) "as z → ∞ in
|ph z| ≤ 3π/2 − δ (< 3π/2)" (10.25.3). Their Wronskian is

    𝒲{K_ν(z), I_ν(z)} = I_ν(z) K_(ν+1)(z) + I_(ν+1)(z) K_ν(z) = 1/z      (10.28.2).

"When ν is fixed and z → 0", K_ν(z) ∼ ½ Γ(ν) (½z)^(−ν) for Re ν > 0 (10.30.2). As z → ∞ with ν fixed,

    I_ν(z) ∼ (e^z/(2πz)^(1/2)) Σ_(k=0)^∞ (−1)^k a_k(ν)/z^k,   |ph z| ≤ π/2 − δ      (10.40.1),

    K_ν(z) ∼ (π/(2z))^(1/2) e^(−z) Σ_(k=0)^∞ a_k(ν)/z^k,   |ph z| ≤ 3π/2 − δ      (10.40.2),

with a_0(ν) = 1 (10.17.1). By the definition of an asymptotic expansion, f(x) = Σ_(s=0)^(n−1) a_s x^(−s) + O(x^(−n))
for each n (2.1.13)–(2.1.14), the first terms give I_ν(z) = e^z (2πz)^(−1/2)(1 + O(1/z)) and
K_ν(z) = (π/(2z))^(1/2) e^(−z)(1 + O(1/z)) as z → ∞ in these sectors, in particular for z > 0.

**Theorem {#thm:std-paley-wiener}** ([Hö90, Theorem 7.3.1, p. 181].) For a compact set K ⊂ ℝⁿ the supporting function
is H(ξ) = sup_(x∈K) ⟨x, ξ⟩, ξ ∈ ℝⁿ, and the Fourier–Laplace transform of a distribution u with compact support is the
entire function û(ζ) = u(e^(−i⟨·,ζ⟩)), ζ ∈ ℂⁿ. Let K be a convex compact subset of ℝⁿ with supporting function H. If u
is a distribution of order N with support contained in K, then

    |û(ζ)| ≤ C (1 + |ζ|)^N e^(H(Im ζ)),   ζ ∈ ℂⁿ.

Conversely, every entire analytic function in ℂⁿ satisfying an estimate of this form is the Fourier–Laplace transform
of a distribution with support contained in K. If u ∈ C_c^∞(ℝⁿ) has support in K, there is for every N a constant C_N
with |û(ζ)| ≤ C_N (1 + |ζ|)^(−N) e^(H(Im ζ)), ζ ∈ ℂⁿ; conversely, every entire analytic function in ℂⁿ satisfying
these estimates for every N is the Fourier–Laplace transform of a function in C_c^∞(ℝⁿ) supported in K.
