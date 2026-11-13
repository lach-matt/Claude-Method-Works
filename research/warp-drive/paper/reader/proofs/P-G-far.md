### The far region by homogeneity {#sec:far-homogeneity}

This section proves the exponents on which the weighted energy estimate of [[ch:own-data]] rests: the decay of the
coefficients of the linearised operator, the degree of the residual of the subtracted expansion, the naturality of the
operator under G, and the weight window they leave. Every exponent is obtained by counting powers of r under one
dilation; no constant beyond those of the chapter's setting enters.

*Setting.* We use the notation of [[ch:own-data]]. In the far region we write t := τ, the time of the chart (τ, x) of
[[sec:background]], so that (t, x) are Cartesian coordinates; r := |x|, x̂ := x/r, v := t + r, k := dv = dt + dr,
μ := μ_end, and

    g_b0 := η + μ m,      m := r⁻² k ⊗ k,      P(h) := Ric^H(g_b0 + h; g_b0).                    {#eq:far-operator}

For Lorentzian metrics g and g′, Ric^H(g; g′) denotes the expression [[eq:gauge]] with g′ in place of g0: the vector
field D and the connection ∇̂ are formed with g′. By [[eq:background]], g_b0 = g0 on {v ≥ v_end}, so there P(h) is
Ric^H(g0 + h) of [[eq:gauge]]. Pointwise norms |·| are those of [[sec:profiles]]: the Euclidean operator norm on
symmetric 2-tensors and the Frobenius norm on arrays of higher rank.

*The wedge.* On r ≥ R₃, Σ^IVP = {t = f(r)}, f being the function F of [[lem:interior-where]] (ii). On r ≥ 4R,
0 < f′ ≤ ¼, 0 ≤ f(r) − f(4R) < R₁/9 and μ r⁻² ≤ 1/400, and 4R ≥ 20R₁ ([[sec:interior-own-data]]); enlarging R if
necessary, we also take 4R ≥ 1. Put t̃ := t − f(r), v1 := 4R + f(4R) and

    W := {v ≥ v1, t̃ ≤ 0, r ≥ 4R},     N := W ∩ {v = v1},     S := Σ^IVP ∩ {r ≥ 4R},     Σ̃_σ := W ∩ {t̃ = σ},

σ ≤ 0, so that Σ̃_0 = S. These are W, H₁ and Σ_far of [[sec:interior-own-data]]: W is the past domain of dependence of
S for g_b0, and its boundary consists of S, N and past null infinity at v ≥ v1 ([[lem:interior-far-part]] (i)). As
v1 ≥ v_end + 2 ([[sec:interior-own-data]]), g_b0 = g0 on W. Put s := (v − v1)/r. On W, v ≥ v1 and t ≤ f(r), so

    0 ≤ v − v1 ≤ (f(r) − f(4R)) + (r − 4R) ≤ (5/4)(r − 4R),

as f′ ≤ ¼; hence 0 ≤ s ≤ 5/4 < 3/2. Also t − v1 = (v − v1) − r ≥ −r and t − v1 ≤ f(r) − f(4R) − 4R < 0,
so |t − v1| ≤ r on W. On Σ̃_σ, v = r + f(r) + σ increases with r, as 1 + f′ > 0, and equals v1 + σ at r = 4R. So Σ̃_σ is
{r ≥ r_σ} along the rays t = f(r) + σ, where r_σ + f(r_σ) = v1 − σ, and

    r_σ = 4R + |σ| − (f(r_σ) − f(4R)) ≥ |σ| + 4R − R₁/9 ≥ c(1 + |σ|),      c := min(1, 4R − R₁/9) > 0.

*The weight.* Put u := t − r, u* := sup_(r≥4R) f + 1 and w := (u* − u)^(2a). On W, t ≤ f(r) ≤ u* − 1 gives
u* − u ≥ r + 1, and v1 − t ≤ r gives u* − u ≤ 2r + |u* − v1|. So r ≤ u* − u ≤ 2r + C and r^(2a) ≤ w ≤ C r^(2a) on W
for a > 0.

*The expansion.* The subtracted expansion is Σ := Σ_(p∈Π) Σ_p, Π := {2, 5/2, 3, 7/2, 4}, Σ_p := r^(−p) F_p(s, x̂),
where F_p(0, ·) = G_(2p)(v1, ·), the G_k being the coefficients of [[prop:bondi-hierarchy]]. For p ≤ 7/2, F_p is the
solution with these data of the flat equation □_η Σ_p = 0 that is smooth at s = 0; harmonic by harmonic on 𝕊³ this
equation is an ordinary differential equation in s with a regular singular point at s = 0, of exponents 0 and
3/2 − p < 0. Σ_4, with the same data, solves

    −(1/2) □_η Σ_4 = −Q_6,                                                                      {#eq:far-sigma4}

Q_6 being the part of P(Σ_2) homogeneous of degree −6 (defined in [[prop:far-residual]]); we also treat the choice
□_η Σ_4 = 0. We use that each F_p is smooth for s in an open interval containing [0, 3/2], the series over the spherical
harmonics converging with all derivatives, and that G_(2p)(v1, ·) = λ Ĝ_(2p) with every derivative of Ĝ_(2p) bounded
independently of λ; so Σ_p = λ Σ̂_p, with every derivative of Σ̂_p bounded on {r = 1, 0 ≤ s ≤ 3/2} independently of λ
[[pending:far-sigma-data]]. The commutators are Γ ∈ {∂_t, L_Ω_ij, Z}, with Ω_ij := x_i ∂_j − x_j ∂_i and
Z := (t − v1) ∂_t + x·∂_x, Z acting on Cartesian components; Γ^α is a product of |α| of them.

*The dilation.* For ς > 0 put D_ς(t, x) := (v1 + ς(t − v1), ς x). It fixes s and x̂, maps {r = 1} onto {r = ς}, and
Z = (d/dς) D_ς at ς = 1. A function, or a tensor read through its Cartesian components, is *homogeneous of degree −q*
if f(D_ς X) = ς^(−q) f(X) for all ς > 0. Then ∂_a f is homogeneous of degree −q − 1, Z f = −q f (differentiate in ς at
ς = 1), and L_Ω_ij f is homogeneous of degree −q, D_ς commuting with rotations. The region 𝒞_1 := {r ≥ 1,
0 ≤ s ≤ 3/2} is the union of the D_ς-images, ς ≥ 1, of the compact set K := {r = 1, 0 ≤ s ≤ 3/2}, and W ⊂ 𝒞_1. So a
smooth f homogeneous of degree −q satisfies |∂^j f| ≤ (max_K |∂^j f|) r^(−q−j) on 𝒞_1. In particular m and every Σ_p
are homogeneous, of degrees −2 and −p, and Γ^α Σ_p is λ times a sum of homogeneous tensors of degrees at most −p (Z and
L_Ω_ij keep the degree, ∂_t lowers it by one). Hence on 𝒞_1

    |∂^j m| ≤ C_j r^(−2−j),      |∂^j Γ^α Σ_p| ≤ C_(j,α) λ r^(−p−j).                               {#eq:far-sigma-bounds}

**Lemma {#lem:far-scaling}** (structure and scaling of the operator). (a) With g := g_b0 + h and Γ̂ := Γ[g_b0],

    P(h)_mn = −(1/2) g^(ab) ∂_a ∂_b g_mn + q_mn(g)(∂g, ∂g) + l_mn(g)(Γ̂, ∂g) + c_mn(g)(∂Γ̂) + c′_mn(g)(Γ̂, Γ̂),

where q, l, c and c′ are multilinear in the displayed arguments with coefficients polynomial in the components of g
and g⁻¹. The components of Γ̂ are μ times a homogeneous function of degree −3 plus μ² times one of degree −5.
(b) For every ς > 0 and every h, writing P_μ for P and h^(ς) := h ∘ D_ς,

    ς² P_μ(h)(D_ς X) = P_(μ ς⁻²)(h^(ς))(X).                                                    {#eq:far-scaling}

*Proof.* (a) In Cartesian coordinates Γ[η] = 0, so [[eq:gauge]] with reference metric η reads Ric^H(g; η)_mn =
−(1/2) g^(ab) ∂_a∂_b g_mn + q_mn(g)(∂g, ∂g) with q purely quadratic, its coefficients polynomial in g and g⁻¹; and the
gauge term of Ric^H(g; η) is −(1/2)(g_mρ ∂_n Γ^ρ + g_nρ ∂_m Γ^ρ), Γ^ρ := g^(ab) Γ[g]^ρ_ab. For the reference g_b0,
D^ρ = Γ^ρ − g^(ab) Γ̂^ρ_ab and ∇̂_n D^ρ = ∂_n D^ρ + Γ̂^ρ_nσ D^σ. So Ric^H(g; g_b0) is Ric^H(g; η) plus the symmetrisation
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
symmetric tensor with |H| ≤ 1/50, g := g_b0 + H, and write

    DP(H)[k] = −(1/2) g^(ab) ∂_a ∂_b k + B(H)·∂k + C(H) k.

There are constants C and C_j, depending only on μ and j, such that:
(a) |B(H)| ≤ C(μ r⁻³ + |∂H|) and |C(H)| ≤ C(μ r⁻⁴ + |∂∂H| + |∂H|²);
(b) |g⁻¹ − g_b0⁻¹| ≤ C|H|, |B(H) − B(0)| ≤ C(|∂H| + μ r⁻³ |H|) and
    |C(H) − C(0)| ≤ C(|∂∂H| + |∂H|² + μ r⁻³ |∂H| + μ r⁻⁴ |H|);
(c) for every j ≥ 1, the coefficients of (μ ∂_μ)^j DP(H) are bounded by C_j μ r⁻² (second order),
    C_j μ (r⁻³ + r⁻²|∂H|) (first order) and C_j μ (r⁻⁴ + r⁻² |∂∂H| + r⁻² |∂H|² + r⁻³ |∂H|) (zero order).
In particular B(0) = O(μ r⁻³) and C(0) = O(μ r⁻⁴); and for λ small and H = Σ on W, by [[eq:far-sigma-bounds]],
g⁻¹ − g_b0⁻¹ = O(λ r⁻²), B(Σ) − B(0) = O(λ r⁻³) and C(Σ) − C(0) = O(λ r⁻⁴).

*Proof.* Differentiating [[lem:far-scaling]] (a) in h in the direction k,

    DP(H)[k] = −(1/2) g^(ab) ∂_a∂_b k + (1/2)(g⁻¹ k g⁻¹)^(ab) ∂_a∂_b g + 2 q(g)(∂g, ∂k) + (∂_g q)[k](∂g, ∂g)
               + l(g)(Γ̂, ∂k) + (∂_g l)[k](Γ̂, ∂g) + (∂_g c)[k](∂Γ̂) + (∂_g c′)[k](Γ̂, Γ̂),

so B(H)·∂k = 2q(g)(∂g, ∂k) + l(g)(Γ̂, ∂k) and C(H)k is the rest. *Bounds on g.* The array of k has |k|² = 2,
so |μ m| = 2μ r⁻² ≤ 1/8. By [[eq:background]], g_b0⁻¹ = η⁻¹ − μ r⁻² L0 ⊗ L0 with |L0|² = 2, so |g_b0⁻¹| ≤ 9/8.
Hence |g_b0⁻¹ H| ≤ 9/400, and g = g_b0 (1 + g_b0⁻¹ H) is invertible with |g⁻¹| ≤ (9/8)/(1 − 9/400) < 6/5; also
the norm of g is at most 1 + 1/8 + 1/50 < 6/5. So the components of g and g⁻¹ are bounded by an absolute constant,
and so are the coefficients of q, l, c, c′ and their g-derivatives. (a) By [[eq:far-sigma-bounds]] and
[[lem:far-scaling]] (a), |∂g_b0| + |Γ̂| ≤ C μ r⁻³ and |∂∂g_b0| + |∂Γ̂| ≤ C μ r⁻⁴. So |∂g| ≤ C μ r⁻³ + |∂H|
and |∂∂g| ≤ C μ r⁻⁴ + |∂∂H|, and (a) follows term by term, with μ² r⁻⁶ ≤ μ r⁻⁴/16 and 2|Γ̂| |∂H| ≤ |Γ̂|² + |∂H|².
(b) Each coefficient is a polynomial in g^(±1), ∂g, ∂∂g, Γ̂, ∂Γ̂. Between H and 0, g^(±1) change by at most C|H|
(g⁻¹ − g_b0⁻¹ = −g⁻¹ H g_b0⁻¹), ∂g by ∂H, ∂∂g by ∂∂H, and Γ̂ not at all. Bounding the difference of a product by
the sum, over its factors, of the change of one factor times the bounds of the others gives (b). (c) The coefficients
depend on μ only through g = η + μ m + H and Γ̂. The operator μ ∂_μ maps μ m, μ ∂m and μ ∂∂m to themselves and g⁻¹
to −g⁻¹ (μ m) g⁻¹. By [[lem:far-scaling]] (a), Γ̂ = μ A + μ² B with A, B homogeneous of degrees −3 and −5, and μ ∂_μ
maps it to μ A + 2μ² B; likewise ∂Γ̂. So μ ∂_μ of a term of the proof of (a) is a sum of terms in each of which one
factor is replaced: a factor of size O(1) by one of size O(μ r⁻²), and ∂g, ∂∂g, Γ̂, ∂Γ̂ by factors of sizes O(μ r⁻³),
O(μ r⁻⁴), O(μ r⁻³), O(μ r⁻⁴). Collecting the terms gives (c) for j = 1. A further μ ∂_μ acts on the new factors in the
same way: it maps μ m, μ ∂m and μ ∂∂m to themselves, μ A + 2μ² B to μ A + 4μ² B, and a g-derivative of a coefficient
evaluated on μ m to terms of the same size or smaller. So each application replaces a factor by one of the same size
or a smaller one, and induction on j gives (c). ∎

### The residual of the subtracted expansion {#sec:far-residual}

**Proposition {#prop:far-residual}** (the degree of the residual). Let M_1[k] := ∂_μ(DP_μ(0)[k]) at μ = 0, the first
variation of P_μ at 0 differentiated in the mass, and M_2[k, k′] the second variation of Ric^H(η + ·; η) at 0; put

    Q_6 := μ M_1[Σ_2] + (1/2) M_2[Σ_2, Σ_2],

homogeneous of degree −6. For λ small, on W, for every multi-index α of commutators Γ and constants c = (c_i),

    |Π_i (Γ_i + c_i) P(Σ)| ≤ C_(α,c) λ r^(−13/2)    if Σ_4 solves [[eq:far-sigma4]];
    |Π_i (Γ_i + c_i) P(Σ)| ≤ C_(α,c) λ r⁻⁶          if □_η Σ_4 = 0.                                {#eq:far-residual}

*Proof.* For X in a neighbourhood of K, 0 ≤ e ≤ 1/16 and d = (d_p)_(p∈Π) with |d| ≤ d_0, put

    Ψ(X; e, d) := Ric^H(η + e m + Σ_p d_p Σ̂_p; η + e m)(X).

Its components are rational in the jets of the two metrics. The denominators do not vanish there: det(η + e m) = −1,
since k is null for η ([[eq:background]]), and d_0 is small. So Ψ is smooth in all its arguments, with bounds
independent of λ, since the jets of the Σ̂_p near K are. For λ small, the values (e, d) = (μ ς⁻², (λ ς^(−p))_p),
ς ≥ 4R, lie in this set. D_ς preserves the region in which the Σ̂_p are defined, and Σ̂_p ∘ D_ς = ς^(−p) Σ̂_p. So
[[eq:far-scaling]] gives, for X in a neighbourhood of K and ς ≥ 4R,

    P(Σ)(D_ς X) = ς⁻² Ψ(X; μ ς⁻², (λ ς^(−p))_p).                                                    {#eq:far-psi}

Three facts about Ψ. First, Ψ(X; e, 0) = Ric(η + e m)(X) = 0 for every e: the reference and the metric coincide, so
D = 0, and η + e m is flat for e = 0 and the vacuum metric of [[prop:vaidya]] (a) with constant mass e for e > 0. Hence
Ψ = Σ_p d_p Ψ_p with Ψ_p := ∫_0^1 ∂_(d_p) Ψ(X; e, y d) dy smooth, and Taylor's formula for each Ψ_p at
(e, d) = (0, 0) gives

    Ψ(X; e, d) = Σ_p d_p ∂_(d_p)Ψ(X; 0, 0) + Σ_p e d_p ∂_e ∂_(d_p)Ψ(X; 0, 0)
                 + (1/2) Σ_(p,p′) d_p d_p′ ∂_(d_p) ∂_(d_p′) Ψ(X; 0, 0) + Rem(X; e, d),                {#eq:far-taylor}

where Rem = Σ_p d_p ϱ_p with ϱ_p smooth and vanishing to second order at (e, d) = (0, 0). So Rem is at most
C |d| (|e| + |d|)² in norm, uniformly in X and (e, d). Second, since Γ[η] = 0, the linearisation of Ric^H(η + ·; η) at
0 is −(1/2) □_η acting on components. So ∂_(d_p)Ψ(X; 0, 0) = −(1/2) □_η Σ̂_p(X), ∂_e ∂_(d_p)Ψ(X; 0, 0) = M_1[Σ̂_p](X) and
∂_(d_p) ∂_(d_p′) Ψ(X; 0, 0) = M_2[Σ̂_p, Σ̂_p′](X); this holds at every point at which the Σ̂_p are defined. Third,
[[eq:far-psi]] holds for every mass in place of μ and for independent amplitudes λ_p in place of λ, both sides being
smooth in them near 0. By the second fact, the coefficients of μ^i Π_p λ_p^(n_p) in their Taylor expansions at 0
are, on the left, constant multiples of −(1/2) □_η Σ̂_p, M_1[Σ̂_p] and M_2[Σ̂_p, Σ̂_p′] at D_ς X, and on the right
ς^(−2−2i−Σ n_p p) times the same multiples at X. Hence (□_η Σ̂_p)(D_ς X) = ς^(−p−2) (□_η Σ̂_p)(X),
M_1[Σ̂_p](D_ς X) = ς^(−p−4) M_1[Σ̂_p](X) and M_2[Σ̂_p, Σ̂_p′](D_ς X) = ς^(−p−p′−2) M_2[Σ̂_p, Σ̂_p′](X). So, by
[[eq:far-psi]], the term of [[eq:far-taylor]] with e^i Π d_p^(n_p), at e = μ ς⁻² and d_p = λ ς^(−p) and multiplied
by ς⁻², is a term of P(Σ) at D_ς X homogeneous of degree −2 − 2i − Σ n_p p; in particular Q_6 is homogeneous of
degree −6.

Now count degrees, with Σ n_p ≥ 1 and ς = r. The terms of degree greater than −13/2, that is 2 + 2i + Σ n_p p < 13/2,
are: i = 0 and one factor d_p, every p ∈ Π (degree −p − 2); i = 1 and the factor d_2 (degree −6); i = 0 and d_2²
(degree −6). The first vanish for p ≤ 7/2, since □_η Σ_p = 0. The remaining three, at degree −6, sum to
−(1/2) □_η Σ_4 + Q_6, which is 0 by [[eq:far-sigma4]]. Every other term of [[eq:far-taylor]] has degree at most −13/2
and carries a factor λ. Since |d| ≤ C λ ς⁻², Rem contributes ς⁻² |Rem| ≤ C λ ς⁻⁴ (μ ς⁻² + λ ς⁻²)² ≤ C λ r⁻⁸. So P(Σ)
is at most C λ r^(−13/2) in norm. If instead □_η Σ_4 = 0, the degree −6 terms sum to Q_6 = O(λ r⁻⁶), and then
P(Σ) is at most C λ r⁻⁶ in norm. The terms of degree −13/2 are μ M_1[Σ_(5/2)] and M_2[Σ_2, Σ_(5/2)].

The commutators. A homogeneous term of degree −q is mapped by Z to −q times itself, by L_Ω_ij to a homogeneous term of
degree −q and by ∂_t to one of degree −q − 1, so it keeps its bound. The terms of degree greater than −13/2 sum to 0,
so their images under Π_i (Γ_i + c_i) sum to 0; if □_η Σ_4 = 0 they sum to Q_6, homogeneous of degree −6 and
O(λ r⁻⁶). For the remainder put Rem′(D_ς X) :=
ς⁻² Rem(X; μ ς⁻², (λ ς^(−p))_p); it does not depend on the choice of (X, ς) with D_ς X given, since P(Σ) and the
homogeneous terms do not. Differentiation in ς gives Z Rem′ = −ς⁻² (2 + 2e ∂_e + Σ_p p d_p ∂_(d_p)) Rem. Here
e ∂_e Rem and d_p′ ∂_(d_p′) Rem are again of the form Σ_p d_p ϱ′_p, with ϱ′_p vanishing to second order at
(e, d) = (0, 0), and so is an X-derivative of Rem. Further ∂_a Rem′ = ς⁻¹ (∂_X Rem)′, and L_Ω_ij, which commutes with
D_ς, maps Rem′ to (L_Ω_ij Rem)′. So every Π_i (Γ_i + c_i) Rem′ is O(λ r⁻⁸), and [[eq:far-residual]] follows. ∎

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

The error terms of the weighted energy identity for φ := (Γ^α h_R)_ij, |α| ≤ k1, are bounded on Σ̃_σ by three tools.
Norms ‖·‖ are those of L²(Σ̃_σ, d⁴x), with d⁴x = r³ dr dω along the rays of Σ̃_σ, and 𝔈 := 𝔈_k1(σ).
(1) For |H| ≤ 1/50 the energy density √|g| T_g[ψ](w ∂_t, −∇t̃) of a component ψ on Σ̃_σ lies between c_1 w |∂ψ|² and
c_2 w |∂ψ|², for constants c_2 ≥ c_1 > 0; so 𝔈 bounds c_1 ∫_(Σ̃_σ) w |∂Γ^β h_R|² d⁴x for |β| ≤ k1. Moreover, along every
ray of Σ̃_σ, liminf_(R′→∞) R′^(2a+2) |Γ^β h_R(R′)|² = 0 for |β| ≤ k1 [[pending:far-energy-tools]]. Hence a
first-order coefficient c with |c| ≤ c_0 r^(−q) gives ‖w^(1/2) c ∂φ‖ ≤ C c_0 r_σ^(−q) 𝔈^(1/2).
(2) A zero-order coefficient with |c| ≤ c_0 r^(−q), q ≥ 1, gives ‖w^(1/2) c φ‖ ≤ C c_0 r_σ^(−q+1) 𝔈^(1/2). This
follows from (1), r^(2a) ≤ w ≤ C r^(2a) and r^(2−2q) ≤ r_σ^(2−2q), by the Hardy inequality on each ray,

    ∫_(r_σ)^∞ r^(2a+1) ψ² dr ≤ (a + 1)⁻² ∫_(r_σ)^∞ r^(2a+3) (∂_r ψ)² dr,                              {#eq:far-hardy}

valid for a > −1 and ψ smooth with liminf_(R′→∞) R′^(2a+2) ψ(R′)² = 0; here ∂_r = x̂·∂_x + f′ ∂_t is the derivative
along the ray. To prove it, integrate ∂_r(r^(2a+2) ψ²) = (2a + 2) r^(2a+1) ψ² + 2 r^(2a+2) ψ ∂_r ψ over [r_σ, R′].
Drop the boundary term at r_σ, which has the good sign, and apply Cauchy–Schwarz to the last term. Then let R′ → ∞
along a sequence on which R′^(2a+2) ψ(R′)² → 0.
(3) A second-order coefficient with |c| ≤ c_0 r^(−q) on ∂∂ψ, ψ := Γ^β h_R, |β| < |α|, gives C c_0 r_σ^(−q) 𝔈^(1/2).
Indeed x_j Ω_ij = x_i (x·∂_x) − r² ∂_i, so

    ∂_i = r⁻¹ x̂_i (Z − (t − v1) ∂_t) − r⁻² x_j Ω_ij,

and with |t − v1| ≤ r on W this gives |∂∂ψ| ≤ C Σ_Γ (|∂Γψ| + r⁻¹ |Γψ|) + C (|∂ψ| + r⁻¹ |ψ|), the sum over
Γ ∈ {∂_t, Z, L_Ω_ij}. Here Ω_ij acting componentwise differs from L_Ω_ij by a constant linear map of the components,
and the fields Γψ have order |β| + 1 ≤ |α|. The zero-order part goes through (2).
Under the bootstrap assumption of the estimate, on Σ̃_σ and for r ≥ r_σ,

    |Γ^β h_R| ≤ C_S ε r^(−1/2−a),   |∂Γ^β h_R| ≤ C_S ε r^(−3/2−a)   (|β| ≤ k1 − 3),
    |∂∂Γ^β h_R| ≤ C_S ε r^(−3/2−a)   (|β| ≤ k1 − 4)                                             {#eq:far-pointwise}

[[pending:far-pointwise]]. Since r_σ ≥ c(1 + |σ|), a term of the energy identity bounded by C r_σ^(−q) 𝔈^(1/2) in the
norm ‖w^(1/2) ·‖, or by C r_σ^(−q) 𝔈 as an integral over Σ̃_σ, has the *kernel* (1 + |σ|)^(−q).

**Corollary {#cor:far-kernels}** (the kernels). Let 0 < a < 9/2 (0 < a < 4 if □_η Σ_4 = 0). In the weighted energy
inequality

    𝔈_k1(σ) ≤ C_E [ 𝔈_k1(T) + 𝔉_k1 + ∫_T^σ κ 𝔈_k1 + ∫_T^σ κ_Σ 𝔈_k1^(1/2) ]

one may take

    κ(σ) := C (μ + λ)(1 + |σ|)⁻² + C ε (1 + |σ|)^(−1/2−a),      κ_Σ(σ) := C λ (1 + |σ|)^(a − 9/2),    {#eq:far-kernels}

with (1 + |σ|)^(a−4) in place of (1 + |σ|)^(a−9/2) if □_η Σ_4 = 0. Hence ∫_(−∞)^0 κ < ∞ exactly when a > 1/2, and
∫_(−∞)^0 κ_Σ < ∞ exactly when a < 7/2 (when a < 3 if □_η Σ_4 = 0).

*Proof.* Differentiating [[lem:far-scaling]] (a) m times in h, D^m P(H)[k_1, …, k_m] is a sum of products of bounded
coefficients with factors ∂^(j_i) k_i, ∂^j H, μ ∂^j m (j = 1, 2), Γ̂ and ∂Γ̂. In each product the derivatives number
exactly two, μ ∂m and Γ̂ being counted as one and μ ∂∂m and ∂Γ̂ as two. Differentiating [[eq:far-scaling]] in ς at
ς = 1 gives (Z + 2) P(h) = DP(h)[Z h] − 2μ ∂_μ P(h). So the commutation with Z brings in the operators (μ ∂_μ)^j,
j ≥ 1, applied to DP(H) and to the higher variations. The terms (μ ∂_μ)^j D^m P(H), m ≥ 2, have the form of D^m P(H),
with factors of the same sizes or smaller, as in the proof of [[prop:far-coefficients]] (c); they are bounded as the
terms of D^m P(H) below.

The terms linear in Γ^β h_R with every other slot a field Γ^γ Σ have coefficients O(λ r^(−4+j)) on ∂^j Γ^β h_R, since
Γ^γ Σ is O(λ r⁻²) with each derivative gaining r⁻¹ ([[eq:far-sigma-bounds]]). This gives λ r⁻² (second order, on
∂∂Γ^β h_R with |β| < |α|, kernel 2 by (3)), λ r⁻³ (first order, kernel 3 by (1)) and λ r⁻⁴ (zero order, kernel 3 by
(2)). By
[[prop:far-coefficients]] with H = Σ + h_R, [[eq:far-sigma-bounds]] and [[eq:far-pointwise]], the other linear terms
are as follows. The terms (μ ∂_μ)^j DP(H)[Γ^β h_R], j ≥ 1, |β| < |α|, give μ r⁻² (second order, kernel 2) and
smaller. B(H)·∂φ and the first-order part of □_g give (μ + λ) r⁻³ + C ε r^(−3/2−a) (kernels 3 and 3/2 + a). C(H) φ
gives (μ + λ) r⁻⁴ + C ε r^(−3/2−a) (zero order: kernels 3 and a + 1/2). The deformation term (1/2) w T^(ab) ∂_t g_ab
carries ∂_t H = O(λ r⁻³ + ε r^(−3/2−a)) (kernels 3 and 3/2 + a).

The terms with at least two slots h_R have commutation orders, each at least 1, summing to at most |α| ≤ k1. Put the
slot of highest order in L²: through (1), through (2) if it is undifferentiated, through (3) if it carries two
derivatives; its order is at most |α| − 1, so (3) stays within 𝔈_k1. Every other slot then has order at most
k1/2 ≤ k1 − 4, since k1 ≥ 8, so it lies within [[eq:far-pointwise]]: it is at most C_S ε r^(−1/2−a) if
undifferentiated and C_S ε r^(−3/2−a) otherwise. In every distribution of the two derivatives the term is then bounded
by C ε r_σ^(−1/2−a) 𝔈^(1/2) (kernel a + 1/2). The least exponents are 2 for the terms of size μ + λ and a + 1/2 for
those of size ε, which is κ.

The residual: by [[prop:far-residual]], |Π_i (Γ_i + c_i) P(Σ)| ≤ C λ r^(−13/2), and w ≤ C r^(2a) on W, so

    ‖w^(1/2) Π_i (Γ_i + c_i) P(Σ)‖² ≤ C λ² ∫_(r_σ)^∞ r^(2a − 13 + 3) dr = C λ² r_σ^(2a−9)/(9 − 2a)

for a < 9/2, which is κ_Σ(σ)²; with □_η Σ_4 = 0 the exponent −13 becomes −12, and a < 4. Finally
∫_(−∞)^0 (1 + |σ|)^(−q) dσ < ∞ exactly when q > 1: q = 2 always, q = a + 1/2 exactly when a > 1/2, q = 9/2 − a
exactly when a < 7/2, and q = 4 − a exactly when a < 3. ∎

**Proposition {#prop:far-window}** (the weight window). Let ℓ0 ∈ (3, 4) ∖ {7/2}. Suppose that on the initial slice Σ̃_T
of the truncated problems, for |α| ≤ k1, |Γ^α h_R| ≤ C r⁻⁴ and |∂Γ^α h_R| ≤ C r⁻⁵, with C independent of T. Suppose
that on N the fields Γ^α h_R, |α| ≤ k1 + 1, and all their first derivatives are O(r^(−9/2)), and their derivatives
along the generators of N are O(r^(−11/2)) [[pending:far-hr-decay]]. The conditions on the weight a of the weighted
estimate are:
(i) the kernels of [[cor:far-kernels]]: 1/2 < a < 7/2 (a < 3 if □_η Σ_4 = 0);
(ii) the cap: 𝔈_k1(T) ≤ C |T|^(2a−6), with C independent of T, a bound that is finite and tends to 0 as T → −∞ exactly
    when a < 3;
(iii) the flux through N: its density is bounded by C r^(2a−8), and the bound is integrable, with tail C R′^(2a−7)
    beyond r = R′, exactly when a < 7/2;
(iv) the class on S: with ρ := 1/r and L²_b := L²(dρ/ρ dω), the energy places h_R|_S in ρ^(a+1) L²_b, which lies in
    ρ^(ℓ0) L²_b on {ρ ≤ ρ_0} exactly when a ≥ ℓ0 − 1;
(v) the remaining conditions of [[ch:own-data]]: a ≥ 3/2 (the pointwise bounds give |H| ≤ r⁻²/4), a > 1/2
    (uniqueness at a smaller weight), and a < 7/2 and a < 3, from the data on N at weight a and from the finiteness of
    the energies of the full initial slices, on which the data are of orders r⁻⁴ and r⁻⁵; neither restricts a beyond
    (ii) [[pending:far-other-conditions]].
Their intersection is [ℓ0 − 1, 3), and [[thm:own-data]] uses its interior a ∈ (ℓ0 − 1, 3).

*Proof.* (i) is [[cor:far-kernels]]. (ii) The initial slice Σ̃_T is {r ≥ r_T} along its rays, with r_T ≥ c(1 + |T|).
There w ≤ C r^(2a), |∂Γ^α h_R| ≤ C r⁻⁵ by the hypothesis, and d⁴x = r³ dr dω, so the energy is at most
C ∫_(r_T)^∞ r^(2a−10+3) dr = C r_T^(2a−6)/(6 − 2a) ≤ C |T|^(2a−6) for a < 3, with C independent of T; for a ≥ 3 the
integral of the bound diverges. In [[ch:own-data]] the hypothesis on the initial slice is [[lem:own-truncation]] (iii),
with a constant depending on λ and J, so that the cap there is C(λ, J) |T|^(2a−6).
(iii) For g_b0 the covector dv is null and −g_b0⁻¹ dv = L0 ([[prop:vaidya]] (c)), with g_b0(∂_t, L0) = −dv(∂_t) = −1.
With L := ∂_t + ∂_r and ∇̸ the gradient on the spheres {t, r fixed}, |dφ|²_(g_b0) = −(Lφ)(L0φ) + |∇̸φ|² −
μ r⁻² (L0φ)², so the flux density of g_b0 is

    T_(g_b0)[φ](w ∂_t, L0) = w ((1/2)(L0φ)² + (1/2)|∇̸φ|² − (1/2) μ r⁻² (L0φ)²).

It contains only derivatives tangent to N, L0 being the generator. By the hypothesis, L0φ = O(r^(−11/2)) on N,
and |∇̸φ| ≤ r⁻¹ Σ_(i<j) |Ω_ij φ| = O(r^(−11/2)), Ω_ij φ being a combination of components of L_Ω_ij Γ^α h_R and Γ^α h_R,
of orders at most k1 + 1. For g = g_b0 + H the density √|g| T_g[φ](w ∂_t, −g⁻¹ dv) differs from √|g_b0| times that of
g_b0 by at most C w |H| |∂φ|²: g(w ∂_t, −g⁻¹ dv) = −w for both metrics, and g⁻¹ − g_b0⁻¹ = O(|H|). This term contains
the transverse derivative. On N, |H| ≤ C r⁻² by [[eq:far-sigma-bounds]] and the hypothesis, and |∂φ| = O(r^(−9/2)),
so it is at most C r^(2a) r⁻² r⁻⁹. With w ≤ C r^(2a) and d⁴x = r³ dr dω the flux density is therefore at most
C r^(2a − 11 + 3) = C r^(2a−8). Its integral beyond R′ is C R′^(2a−7)/(7 − 2a) for a < 7/2, and the bound is not
integrable for a ≥ 7/2. (iv) The weighted energy on S bounds ∫ r^(2a+3) |∂h_R|² dr, hence by [[eq:far-hardy]]
∫ r^(2a+1) h_R² dr. With r = 1/ρ and dr = −ρ⁻² dρ, ∫ r^(2a+1) h_R² dr = ∫ (ρ^(−(a+1)) h_R)² dρ/ρ, so h_R|_S ∈
ρ^(a+1) L²_b, and ρ^(a+1) L²_b ⊂ ρ^(ℓ0) L²_b on ρ ≤ ρ_0 exactly when a + 1 ≥ ℓ0. (v) is cited. Since
ℓ0 − 1 > 2 > 3/2 > 1/2, the conditions reduce to ℓ0 − 1 ≤ a < 3. ∎

**Remark {#rem:far-window-sigma4}** (the term Σ_4). With □_η Σ_4 = 0 every condition keeps its form except (i)'s
upper end, which becomes a < 3; it coincides with the cap's. The hypotheses on h_R hold for either choice of Σ_4. On
N, where s = 0, the two choices of F_4 have the same value G_8(v1, ·), so the two Σ_4 coincide there. On the initial
slice the hypothesis is [[lem:own-truncation]] (iii), whose proof uses of Σ_4 only that it is smooth and homogeneous of
degree −4 with F_4(0, ·) = G_8(v1, ·), and that P(Σ) is tame of order 6, which [[prop:far-residual]] gives for either
choice; the continuation Σ′_J of [[def:cutoff-extension]] is formed with the Taylor coefficients F_(4,n) of the chosen
F_4, and beyond the band the two choices of Σ + Σ′_J differ by a term homogeneous of degree −4. So the window
(ℓ0 − 1, 3) does not depend on whether Σ_4 solves [[eq:far-sigma4]]. Without the term p = 4 in Σ, h_R contains
r⁻⁴ G_8(v1, ·) on N, so that its derivatives along the generators and along the spheres are O(r⁻⁵) there and the flux
density of (iii) is bounded by C r^(2a−7), with tail C R′^(2a−6) beyond R′, integrable exactly when a < 3; on the
initial slice Σ′_J then contains the terms r⁻⁴ s^n G_(8+2n,n), n ≥ 0, still homogeneous of degree −4, so the cap keeps
its exponent 2a − 6; and P(Σ) keeps its terms Q_6 of degree −6, so (i) gives a < 3. The conditions then leave
[ℓ0 − 1, 3) again.
