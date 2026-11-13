### The far region by homogeneity {#sec:far-homogeneity}

This section proves the exponents on which the weighted energy estimate of [[ch:own-data]] rests: the decay of the
coefficients of the linearised operator, the degree of the residual of the subtracted expansion, the naturality of the
operator under G, and the weight window they leave. Every exponent is obtained by counting powers of r under one
dilation; no constant beyond those of the chapter's setting enters.

*Setting.* We use the notation of [[ch:own-data]]. In the Cartesian coordinates (t, x) of the far region, r := |x|,
v := t + r, k := dv = dt + dr, μ := μ_end, and

    g_b0 := η + μ m,      m := r⁻² k ⊗ k,      P(h) := Ric^H(g_b0 + h; g_b0),                    {#eq:far-operator}

Ric^H as in [[eq:gauge]] with g_b0 as the reference metric, which is g0 on {v ≥ v_end}. For v_1 the value of v on N,
put s := (v − v_1)/r. The wedge W satisfies v ≥ v_1, |t − v_1| ≤ r and, for r ≥ 4R, s ≤ 3/2; its slices are
Σ̃_σ := {t − f(r) = σ} ∩ W with f bounded, and on Σ̃_σ, r ≥ r_σ ≥ c(1 + |σ|) with c > 0
[[pending:far-wedge-geometry]]. The subtracted expansion is Σ := Σ_(p∈Π) Σ_p,
Π := {2, 5/2, 3, 7/2, 4}, Σ_p := r^(−p) F_p(s, x̂), where for p ≤ 7/2 F_p is the regular solution of the flat equation
□_η Σ_p = 0, and Σ_4 solves

    −(1/2) □_η Σ_4 = −Q_6,                                                                      {#eq:far-sigma4}

Q_6 being the part of P(Σ_2) homogeneous of degree −6 (defined in [[prop:far-residual]]); we also treat the choice
□_η Σ_4 = 0. Each F_p is smooth for s in an open interval containing [0, 3/2], and Σ_p = λ Σ̂_p with every derivative
of Σ̂_p bounded on {r = 1, 0 ≤ s ≤ 3/2} independently of λ [[pending:far-sigma-data]]. The commutators are
Γ ∈ {∂_t, L_Ω_ij, Z}, Z := (t − v_1) ∂_t + x·∂_x acting on Cartesian components, and the weight is w = (u* − u)^(2a),
u := t − r, with r ≤ u* − u ≤ 2r + C on W.

*The dilation.* For ς > 0 put D_ς(t, x) := (v_1 + ς(t − v_1), ς x). It fixes s and x̂, maps {r = 1} onto {r = ς}, and
Z = (d/dς) D_ς at ς = 1. A function, or a tensor read through its Cartesian components, is *homogeneous of degree −q*
if f(D_ς X) = ς^(−q) f(X) for all ς > 0. Then ∂_a f is homogeneous of degree −q − 1, Z f = −q f (differentiate in ς at
ς = 1), and L_Ω_ij f is homogeneous of degree −q, D_ς commuting with rotations. Since the region C_1 := {r ≥ 1,
0 ≤ s ≤ 3/2} is the union of the D_ς-images, ς ≥ 1, of the compact set K := {r = 1, 0 ≤ s ≤ 3/2}, a smooth f
homogeneous of degree −q satisfies |∂^j f| ≤ (max_K |∂^j f|) r^(−q−j) on C_1. In particular m and every Σ_p are
homogeneous, of degrees −2 and −p, and on C_1

    |∂^j m| ≤ C_j r^(−2−j),      |∂^j Σ_p| ≤ C_j λ r^(−p−j),      |Γ^α Σ_p| ≤ C_α λ r^(−p).          {#eq:far-sigma-bounds}

**Lemma {#lem:far-scaling}** (structure and scaling of the operator). (a) With g := g_b0 + h and Γ̂ := Γ[g_b0],

    P(h)_mn = −(1/2) g^(ab) ∂_a ∂_b g_mn + q_mn(g)(∂g, ∂g) + l_mn(g)(Γ̂, ∂g) + c_mn(g)(∂Γ̂) + c′_mn(g)(Γ̂, Γ̂),

where q, l, c and c′ are multilinear in the displayed arguments with coefficients polynomial in the components of g
and g⁻¹. The components of Γ̂ are μ times a homogeneous function of degree −3 plus μ² times one of degree −5.
(b) For every ς > 0 and every h, writing P_μ for P and h^(ς) := h ∘ D_ς,

    ς² P_μ(h)(D_ς X) = P_(μ ς⁻²)(h^(ς))(X).                                                    {#eq:far-scaling}

*Proof.* (a) In Cartesian coordinates Γ[η] = 0, so [[eq:gauge]] with reference metric η reads Ric^H(g; η)_mn =
−(1/2) g^(ab) ∂_a∂_b g_mn + q_mn(g)(∂g, ∂g) with q purely quadratic, its coefficients polynomial in g and g⁻¹; and the
gauge term of Ric^H(g; η) is −(1/2)(g_mρ ∂_n Γ^ρ + g_nρ ∂_m Γ^ρ), Γ^ρ := g^(ab) Γ[g]^ρ_ab. For the reference g_b0,
D^ρ = Γ^ρ − g^(ab) Γ̂^ρ_ab and ∇̂_n D^ρ = ∂_n D^ρ + Γ̂^ρ_nσ D^σ, so Ric^H(g; g_b0) is Ric^H(g; η) plus the symmetrisation
of g_mρ (∂_n(g^(ab) Γ̂^ρ_ab) − Γ̂^ρ_nσ (Γ^σ − g^(ab) Γ̂^σ_ab)). Here ∂_n g^(ab) = −g^(ac) g^(bd) ∂_n g_cd and Γ^σ is
linear in ∂g with coefficients polynomial in g⁻¹, which gives the form stated. By [[eq:background]], g_b0⁻¹ = η⁻¹ −
μ r⁻² L0 ⊗ L0 with L0 homogeneous of degree 0, and ∂g_b0 = μ ∂m, which gives the degrees of Γ̂. (b) D_ς^* dt =
ς dt and D_ς^* dx^i = ς dx^i, so D_ς^* η = ς² η and D_ς^* m = m (k is homogeneous of degree 0 and D_ς^* k = ς k): hence
D_ς^* g_b0(μ) = ς² g_b0(μ ς⁻²), and the components of ς⁻² D_ς^* h are those of h^(ς). Ric^H is built from the two
metrics by Levi-Civita connections, curvature and contraction, so φ^* Ric^H(g; g′) = Ric^H(φ^* g; φ^* g′) for every
diffeomorphism φ, and Ric^H(c g; c g′) = Ric^H(g; g′) for every constant c > 0 (Christoffel symbols are unchanged,
D^ρ is multiplied by c⁻¹ and g_mρ by c). With φ = D_ς and c = ς⁻², D_ς^* P_μ(h) = P_(μ ς⁻²)(ς⁻² D_ς^* h), and the
components of D_ς^* T are ς² T(D_ς ·). ∎

### The coefficients of the linearised operator {#sec:far-coefficients}

**Proposition {#prop:far-coefficients}** (decay of the coefficients). On {r ≥ 4R}, where μ r⁻² ≤ 1/16, let H be a
symmetric tensor with |H| ≤ 1/50 and |∂H| ≤ 1, g := g_b0 + H, and write

    DP(H)[k] = −(1/2) g^(ab) ∂_a ∂_b k + B(H)·∂k + C(H) k.

There is C depending only on μ such that:
(a) |B(H)| ≤ C(μ r⁻³ + |∂H|) and |C(H)| ≤ C(μ r⁻⁴ + |∂∂H| + |∂H|²);
(b) |g⁻¹ − g_b0⁻¹| ≤ C|H|, |B(H) − B(0)| ≤ C(|∂H| + μ r⁻³ |H|) and
    |C(H) − C(0)| ≤ C(|∂∂H| + |∂H|² + μ r⁻³ |∂H| + μ r⁻⁴ |H|);
(c) the coefficients of μ ∂_μ DP(H) are bounded by C μ r⁻² (second order), C μ (r⁻³ + r⁻²|∂H|) (first order) and
    C μ (r⁻⁴ + r⁻² |∂∂H| + r⁻² |∂H|² + r⁻³ |∂H|) (zero order).
In particular B(0) = O(μ r⁻³), C(0) = O(μ r⁻⁴), and for H = Σ on W ∩ {r ≥ 4R}, by [[eq:far-sigma-bounds]],
g⁻¹ − g_b0⁻¹ = O(λ r⁻²), B(Σ) − B(0) = O(λ r⁻³) and C(Σ) − C(0) = O(λ r⁻⁴): the decay exponents are 2, 3, 4, 3, 4.

*Proof.* Differentiating [[lem:far-scaling]] (a) in h in the direction k,

    DP(H)[k] = −(1/2) g^(ab) ∂_a∂_b k + (1/2)(g⁻¹ k g⁻¹)^(ab) ∂_a∂_b g + 2 q(g)(∂g, ∂k) + (∂_g q)[k](∂g, ∂g)
               + l(g)(Γ̂, ∂k) + (∂_g l)[k](Γ̂, ∂g) + (∂_g c)[k](∂Γ̂) + (∂_g c′)[k](Γ̂, Γ̂),

so B(H)·∂k = 2q(g)(∂g, ∂k) + l(g)(Γ̂, ∂k) and C(H)k is the rest. Since |g − η| ≤ |μ m| + |H| ≤ 1/16 + 1/50, the
components of g and g⁻¹ are bounded by an absolute constant, hence so are the coefficients of q, l, c, c′ and their
g-derivatives. By [[eq:far-sigma-bounds]] and [[lem:far-scaling]] (a), |∂g_b0| + |Γ̂| ≤ C μ r⁻³ and |∂∂g_b0| + |∂Γ̂| ≤
C μ r⁻⁴; so |∂g| ≤ C μ r⁻³ + |∂H| and |∂∂g| ≤ C μ r⁻⁴ + |∂∂H|, and (a) follows term by term, with μ² r⁻⁶ ≤ μ r⁻⁴/16
and 2|Γ̂| |∂H| ≤ |Γ̂|² + |∂H|². (b) Each coefficient is a polynomial in g^(±1), ∂g, ∂∂g, Γ̂, ∂Γ̂; between H and 0, g^(±1)
change by at most C|H|, ∂g by ∂H, ∂∂g by ∂∂H, and Γ̂ not at all. Bounding the difference of a product by the sum, over
its factors, of the change of one factor times the bounds of the others gives (b). (c) The coefficients depend on μ through g = η + μ m + H
and Γ̂ only, and μ ∂_μ g = μ m, μ ∂_μ ∂g = μ ∂m, μ ∂_μ ∂∂g = μ ∂∂m, μ ∂_μ g⁻¹ = −g⁻¹ (μ m) g⁻¹, μ ∂_μ Γ̂ = O(μ r⁻³),
μ ∂_μ ∂Γ̂ = O(μ r⁻⁴). By the product rule μ ∂_μ of each term of the proof of (a) replaces one factor by its μ ∂_μ: a
factor of size O(1) by one of size O(μ r⁻²), and ∂g, ∂∂g, Γ̂, ∂Γ̂ by factors of sizes O(μ r⁻³), O(μ r⁻⁴), O(μ r⁻³),
O(μ r⁻⁴). Collecting the terms gives (c). ∎

### The residual of the subtracted expansion {#sec:far-residual}

**Proposition {#prop:far-residual}** (the degree of the residual). Let M[k] be the part of DP_μ(0)[k] linear in μ,
divided by μ, and B[k, k′] := D² Ric^H(η + ·; η)(0)[k, k′]; put

    Q_6 := μ M[Σ_2] + (1/2) B[Σ_2, Σ_2],

homogeneous of degree −6. For λ small, on W ∩ {r ≥ 4R}, for every multi-index α of commutators Γ and constants c_i,

    |Π_i (Γ_i + c_i) P(Σ)| ≤ C_α λ r^(−13/2)    if Σ_4 solves [[eq:far-sigma4]];
    |Π_i (Γ_i + c_i) P(Σ)| ≤ C_α λ r⁻⁶          if □_η Σ_4 = 0.                                   {#eq:far-residual}

*Proof.* Put Ψ(X; e, d) := Ric^H(η + e m + Σ_p d_p Σ̂_p; η + e m)(X), d = (d_p)_(p∈Π), for X near K and (e, d) near 0;
it is smooth in all its arguments, its components being rational in the jets of the two metrics with nonvanishing
denominators near (e, d) = 0; for λ small, the values (e, d) = (μ ς⁻², (λ ς^(−p))_p), ς ≥ 4R, lie in a compact set on
which it is smooth. Since D_ς preserves the region in which Σ̂_p is defined and Σ̂_p ∘ D_ς = ς^(−p) Σ̂_p,
[[eq:far-scaling]] gives, for X ∈ K and ς ≥ 4R,

    P(Σ)(D_ς X) = ς⁻² Ψ(X; μ ς⁻², (λ ς^(−p))_p).                                                    {#eq:far-psi}

Three facts about Ψ. First, Ψ(X; e, 0) = Ric(η + e m)(X) = 0 for every e: the reference and the metric coincide, so
D = 0, and η + e m is the vacuum metric of [[prop:vaidya]] with constant mass e. Hence Ψ = Σ_p d_p Ψ_p with Ψ_p :=
∫_0^1 ∂_(d_p) Ψ(X; e, τ d) dτ smooth, and Taylor's formula for each Ψ_p at (e, d) = (0, 0) gives

    Ψ(X; e, d) = Σ_p d_p ∂_(d_p)Ψ(X; 0, 0) + Σ_p e d_p ∂_e ∂_(d_p)Ψ(X; 0, 0)
                 + (1/2) Σ_(p,p′) d_p d_p′ ∂_(d_p) ∂_(d_p′) Ψ(X; 0, 0) + Rem(X; e, d),                {#eq:far-taylor}

where Rem = Σ_p d_p ρ_p with ρ_p smooth and vanishing to second order at (e, d) = (0, 0), so that |Rem| ≤ C |d| (|e| +
|d|)², uniformly for X ∈ K and (e, d) in that compact set. Second, since Γ[η] = 0, the linearisation of Ric^H(η + ·; η) at 0 is −(1/2) □_η acting on
components, so ∂_(d_p)Ψ(X; 0, 0) = −(1/2) □_η Σ̂_p(X), and ∂_e ∂_(d_p)Ψ(X; 0, 0) = M[Σ̂_p](X), ∂_(d_p) ∂_(d_p′) Ψ(X; 0, 0)
= B[Σ̂_p, Σ̂_p′](X). Third, each of these coefficient functions, extended to C_1 by the homogeneity of degree −p − 2,
−p − 4 and −p − p′ − 2 respectively, is the corresponding term of P(Σ) at D_ς X: inserting e = μ ς⁻² and d_p = λ ς^(−p)
into [[eq:far-taylor]] and multiplying by ς⁻², the term with e^i Π d_p^(n_p) has the factor ς^(−2−2i−Σ n_p p).

Now count degrees, with Σ n_p ≥ 1 and ς = r. The terms of degree greater than −13/2, that is 2 + 2i + Σ n_p p < 13/2,
are: i = 0 and one factor d_p, every p ∈ Π (degree −p − 2); i = 1 and the factor d_2 (degree −6); i = 0 and d_2²
(degree −6). The first vanish for p ≤ 7/2, since □_η Σ_p = 0. The remaining three, at degree −6, sum to
−(1/2) □_η Σ_4 + Q_6, which is 0 by [[eq:far-sigma4]]. Every other term of [[eq:far-taylor]] has degree at most −13/2
and carries λ (or λ² ≤ λ), and Rem contributes ς⁻² |Rem| ≤ C λ ς⁻² ς⁻² (μ ς⁻² + λ ς⁻²)² ≤ C λ r⁻⁸, |d| ≤ C λ ς⁻².
So |P(Σ)| ≤ C λ r^(−13/2). If instead □_η Σ_4 = 0, the degree −6 terms sum to Q_6 = O(λ r⁻⁶), and |P(Σ)| ≤ C λ r⁻⁶.
The terms of degree −13/2 are μ M[Σ_(5/2)] and the cross terms of B[Σ_2, Σ_(5/2)].

The commutators. A homogeneous term of degree −q is mapped by Z to −q times itself, by L_Ω_ij to a homogeneous term of
degree −q and by ∂_t to one of degree −q − 1, so it keeps its bound. For the remainder Rem′(D_ς X) := ς⁻² Rem(X; μ ς⁻²,
(λ ς^(−p))_p), differentiation in ς gives Z Rem′ = −ς⁻² (2 + 2e ∂_e + Σ_p p d_p ∂_(d_p)) Rem, and e ∂_e Rem and
d_(p′) ∂_(d_p′) Rem are again of the form Σ_p d_p ρ′_p with ρ′_p vanishing to second order at (e, d) = (0, 0); an
X-derivative of Rem has the same form, and ∂_a Rem′ = ς⁻¹ (∂_X Rem)′, while L_Ω_ij, which commutes with D_ς and is
homogeneous of degree 0, maps Rem′ to (L_Ω_ij Rem)′. So every Π_i (Γ_i + c_i) Rem′ is O(λ r⁻⁸), and
[[eq:far-residual]] follows. ∎

### Naturality under the symmetry group {#sec:far-naturality}

**Lemma {#lem:far-naturality}** (naturality). Let O ∈ O(4), Õ(t, x) := (t, O x) and Λ := diag(1, O). For every
symmetric h, in Cartesian components,

    P(Λᵀ h(Λ ·) Λ) = Λᵀ P(h)(Λ ·) Λ.

In particular, for O ∈ G = O(2) × O(2), P maps G-invariant tensors to G-invariant tensors, and Õ^* g solves
Ric^H(·; g_b0) = 0 whenever g does.

*Proof.* r ∘ Õ = r and t ∘ Õ = t, so Õ^* η = η, Õ^* k = k and Õ^* g_b0 = g_b0. By the naturality of Ric^H used in the
proof of [[lem:far-scaling]] (b), Õ^* P(h) = Ric^H(Õ^* g_b0 + Õ^* h; Õ^* g_b0) = P(Õ^* h), and the Cartesian components
of Õ^* h are Λᵀ h(Λ ·) Λ. ∎

### The kernels of the energy estimate and the weight window {#sec:far-window}

The error terms of the weighted energy identity for φ := (Γ^α h_R)_ij are bounded, on Σ̃_σ, by three tools of
[[ch:own-data]] [[pending:far-energy-tools]]: a first-order coefficient bounded by c_0 r^(−q) gives
‖w^(1/2) c ∂φ‖ ≤ C c_0 r_σ^(−q) 𝔈^(1/2); a zero-order one gives C c_0 r_σ^(−q+1) 𝔈^(1/2), by the Hardy inequality
∫_(r_σ)^∞ r^(2a+1) φ² dr ≤ (a + 1)⁻² ∫_(r_σ)^∞ r^(2a+3) (∂_r φ)² dr; and a second-order one on ∂∂Γ^β h_R, |β| < |α|,
gives C c_0 r_σ^(−q) times the energies of one more commutation, by the identity ∂_i = r⁻¹ x̂_i (Z − (t − v_1) ∂_t) −
r⁻² x_j Ω_ij and |t − v_1| ≤ r. With the pointwise bounds of the bootstrap, |Γ^β h_R| ≤ C_S ε r^(−1/2−a) and
|∂Γ^β h_R| + |∂∂Γ^β h_R| ≤ C_S ε r^(−3/2−a) [[pending:far-pointwise]], and r_σ ≥ c(1 + |σ|), a term whose coefficient
decays like r^(−q) has the *kernel* (1 + |σ|)^(−q).

**Corollary {#cor:far-kernels}** (the kernels). In the weighted energy inequality

    𝔈_k1(σ) ≤ C_E [ 𝔈_k1(T) + 𝔉_k1 + ∫_T^σ κ 𝔈_k1 + ∫_T^σ ρ 𝔈_k1^(1/2) ]

one may take

    κ(σ) := C (μ + λ)(1 + |σ|)⁻² + C ε (1 + |σ|)^(−1/2−a),      ρ(σ) := C λ (1 + |σ|)^(a − 9/2),     {#eq:far-kernels}

with (1 + |σ|)^(a−4) in place of (1 + |σ|)^(a−9/2) if □_η Σ_4 = 0. Hence ∫_(−∞)^0 κ < ∞ exactly when a > 1/2, and
∫_(−∞)^0 ρ < ∞ exactly when a < 7/2 (when a < 3 if □_η Σ_4 = 0).

*Proof.* Differentiating [[lem:far-scaling]] (a) m times in h, D^m P(H)[k_1, …, k_m] is a sum of products of bounded
coefficients with factors ∂^(j_i) k_i, ∂^j H, Γ̂ and ∂Γ̂ in which the derivatives, Γ̂ counted as one and ∂Γ̂ as two,
number exactly two. The terms linear in Γ^β h_R with every other slot a field Γ^γ Σ, which is O(λ r⁻²) with each
derivative gaining r⁻¹ ([[eq:far-sigma-bounds]]), therefore have coefficients O(λ r^(−4+j)) on ∂^j Γ^β h_R: λ r⁻²
(second order, kernel 2), λ r⁻³ (first order, 3) and λ r⁻⁴ (zero order, 3). By [[prop:far-coefficients]] with H = Σ + h_R, the bounds of Σ and the
pointwise bounds: the terms μ ∂_μ DP(H) give μ r⁻² (second order, 2) and smaller; B(H)·∂φ and the first-order part
of □_g give (μ + λ) r⁻³ + C ε r^(−3/2−a) (kernels 3 and 3/2 + a); C(H) φ gives (μ + λ) r⁻⁴ + C ε r^(−3/2−a) (zero
order: kernels 3 and a + 1/2); the deformation term (1/2) w T^(ab) ∂_t g_ab carries ∂_t H = O(λ r⁻³ + ε r^(−3/2−a))
(kernels 3 and 3/2 + a). The terms with at least two slots h_R have one slot in L², an undifferentiated one through
Hardy, and the others bounded pointwise by C_S ε r^(−3/2−a), which gives ε r^(−1/2−a) (kernel a + 1/2). The least
exponents are 2 for the terms of size μ + λ and a + 1/2 for those of size ε, which is κ. The residual: by
[[prop:far-residual]], |Π_i (Γ_i + c_i) P(Σ)| ≤ C λ r^(−13/2), and w ≤ C r^(2a) on W, so with d⁴x = r³ dr dω on Σ̃_σ

    ‖w^(1/2) Π_i (Γ_i + c_i) P(Σ)‖²_(L²(Σ̃_σ)) ≤ C λ² ∫_(r_σ)^∞ r^(2a − 13 + 3) dr = C λ² r_σ^(2a−9)/(9 − 2a)

for a < 9/2, which is ρ(σ)²; with □_η Σ_4 = 0 the exponent −13 becomes −12. Finally ∫_(−∞)^0 (1 + |σ|)^(−q) dσ < ∞
exactly when q > 1: q = 2 always, q = a + 1/2 when a > 1/2, q = 9/2 − a when a < 7/2, and q = 4 − a when a < 3. ∎

**Proposition {#prop:far-window}** (the weight window). Let ℓ0 ∈ (3, 4) ∖ {7/2} and suppose that on the initial slice
of the truncated problems the field h_R vanishes off {v_1 ≤ v ≤ v_1 + C}, that there the fields Γ^α h_R, |α| ≤ k1,
and their first derivatives are O(r^(−9/2)), and that on N the fields Γ^α h_R are O(r^(−9/2)), their derivatives
along the generators O(r^(−11/2)) [[pending:far-hR-decay]]. The
conditions on the weight a of the weighted estimate are:
(i) the kernels of [[cor:far-kernels]]: 1/2 < a < 7/2 (a < 3 if □_η Σ_4 = 0);
(ii) the cap: 𝔈_k1(T) ≤ C(λ) |T|^(2a−6), which tends to 0 as T → −∞ exactly when a < 3;
(iii) the flux through N: finite, with tail C R^(2a−7) beyond r = R, exactly when a < 7/2;
(iv) the class on S: the energy places h_R|_S in ρ^(a+1) L²_b(dρ/ρ), ρ := 1/r, inside ρ^(ℓ0) L²_b when a ≥ ℓ0 − 1;
(v) the remaining conditions of [[ch:own-data]]: a ≥ 3/2 (the pointwise bounds give |H| ≤ r⁻²/4) and a > 1/2
    (uniqueness at a smaller weight) [[pending:far-other-conditions]].
Their intersection is (ℓ0 − 1, 3) up to its lower end point, and the theorem uses a ∈ (ℓ0 − 1, 3).

*Proof.* (i) is [[cor:far-kernels]]. (ii) On the initial slice at t̃ = T the support of h_R lies where v − v_1 ≤ C and
t = T + f(r), so r = |T| + O(1), f being bounded; there w ≤ C r^(2a), |∂h_R| ≤ C r^(−9/2) (a cut-off in v of bounded derivative included)
and the volume is at most C r³, so the energy is at most C r^(2a − 9 + 3) = C |T|^(2a−6). (iii) On N, the flux density
of the weighted energy of h_R involves its derivatives tangent to N, of size r^(−11/2) along the generators and r⁻¹
times r^(−9/2) along the spheres; with w ≤ C r^(2a) and r³ dr dω it is at most C r^(2a − 11 + 3) = C r^(2a−8), whose
integral beyond R is C R^(2a−7)/(7 − 2a) for a < 7/2 and infinite otherwise. (iv) The weighted energy on S bounds
∫ r^(2a+3) |∂h_R|² dr, hence by Hardy ∫ r^(2a+1) h_R² dr; with r = 1/ρ, dr = −ρ⁻² dρ, ∫ r^(2a+1) h_R² dr =
∫ (ρ^(−(a+1)) h_R)² dρ/ρ, so h_R|_S ∈ ρ^(a+1) L²_b, and ρ^(a+1) L²_b ⊂ ρ^(ℓ0) L²_b on ρ ≤ ρ_0 exactly when
a + 1 ≥ ℓ0. (v) is cited. Since ℓ0 − 1 > 2 > 3/2 > 1/2, the conditions reduce to ℓ0 − 1 ≤ a < 3. ∎

**Remark {#rem:far-window-sigma4}** (the term Σ_4). With □_η Σ_4 = 0 every condition keeps its form except (i)'s
upper end, which becomes a < 3; it coincides with the cap's. So the window (ℓ0 − 1, 3) does not depend on whether Σ_4
solves [[eq:far-sigma4]]. Without the term p = 4 in Σ, h_R is O(r⁻⁴) on the initial slice and on N, the cap's exponent
becomes 2a − 5 and the flux's 2a − 6, and the conditions leave a < 5/2, which meets a ≥ ℓ0 − 1 only for ℓ0 < 7/2.
