## Constraint propagation and constraint damping {#ch:s14}

This chapter proves, in spatial dimension n = 4 and for the Myers–Perry metrics g_b with b near b₀ = (m₀, 0), the
properties of the constraint propagation operator □^C_b that the linear and nonlinear theory of the later chapters
uses: mode stability at nonzero frequencies, invertibility of the zero energy operator on weighted spaces, the
location, multiplicity and counting of its indicial roots, and its admissibility at the transition face. It then
constructs the large zero energy states of the adjoint operator and their trace-reversed symmetric gradients. This is
[Hin26, Section 7 to Proposition 7.4] in dimension 4 + 1, resting on [Hin26a, Sections 3–6 and Appendices A–B], which
we write out in dimension 4 + 1.

Four things change with the dimension. The trace weight of the damping modification is 2/(D − 2) = 2/3 in spacetime
dimension D = 5, the value for which the damping symbol keeps the form of [Hin26a, Lemma 3.2]. The top of the strip of
weights on which the zero energy operator is invertible is the Coulomb root 2, where in dimension 3 + 1 it is 1. The
volume density r³ |dr d𝑔̸| shifts every weight at infinity by 2 instead of 3/2. And the dual states carry one more order
of decay: the corrections of the translations and rotations begin at ρ², their trace-reversed symmetric gradients at
ρ³, and there are eleven dual states at A = 0, against seven. The constants of the damping are fixed once, in
[[sec:iv4-0]], and every later chapter uses them as fixed there.

Throughout, an *indicial root* is written ι, and ν is the variable of a characteristic polynomial. The letter h denotes
the semiclassical parameter h = γ_C⁻¹ of the damping; the symmetric 2-tensors h*_(b,s0), h*_(b,s1)(S), h*_(b,v1)(V)
of [[sec:iii-e-3]] carry subscripts and are not to be confused with it. The black-hole parameters are b = (m, A), with
m the mass parameter and b₀ = (m₀, 0), as in [[ch:s11]].

*The inner radius.* The inner radius r_♭ ∈ (0, ½R₁] of [[ch:s11]], R₁ = m₀^(1/2), is a parameter, and every result of
this chapter holds for every such r_♭. The radius r₀ of the artificial boundary of [[sec:i-a-1-1]] is put at r_♭
([[ch:s12]]), so the spaces on X̄ have their inner boundary at {|x| = r_♭}. Only three steps touch the region near
it: the 1-form c_C is past timelike there, at every radius ([[prop:np-10-14]] (i)); the analysis of [[sec:iv5]] has
its inner boundary at r_♭ and is placed relative to it ([[sec:iv5-0]]); and the vanishing of the dual states inside
the horizon ([[sec:iii-e-2]], (b)) runs from {|x| = r_♭}. Every other step reaches the inner boundary only through the
theorems of [[ch:s01]]–[[ch:s03]] and [[ch:s11]]–[[ch:s13]], which hold with r_♭ as a parameter. Nothing is claimed
uniform in r_♭; the neighbourhood of b₀ and the thresholds in h may depend on it.

### The constraint propagation operator {#sec:iii-e-1}

The parameter space ℬ, the metrics g_b, b = (m, A), the time function t_*, the boundary defining function ρ = |x|⁻¹
near ∂X, the bundle E (trivialised by dt_*, dx¹, …, dx⁴) and the Minkowski metric ḡ are those of [[sec:iii-d2-1]].
With the 1-form modification of [[eq:iii-b-6-2]], for v_C ∈ (0, 1), e_C, γ_C and a stationary c_C ∈ |x|⁻¹C^∞
equal to |x|⁻¹(dt − v_C d|x|) for large |x|, put

    δ*_(g,E_C) := δ*_g + E^C_g,     E^C_g ω = γ_C (2 c_C ⊗_s ω − (2/3)(1 − e_C) g ι_(g⁻¹c_C) ω),
    □^C_b := 2 δ_(g_b) G_(g_b) δ*_(g_b,E_C),                                                              {#eq:iii-e-1-1}

the *constraint propagation operator*; P^C_b := (□^C_b)^(0) is its zero energy operator. Here
δ*ω = ½(ω_(a;b) + ω_(b;a)), G_g = Id − ½ g tr_g, (δk)_a = −g^(bc) k_(ab;c) and a ⊗_s b = ½(a ⊗ b + b ⊗ a). The formal
adjoint of □^C_b for the fibre pairing g_b⁻¹ and the volume density |dg_b| is

    (□^C_b)* = 2 (δ*_(g_b,E_C))* G_(g_b) δ*_(g_b)                                                         {#eq:iii-e-1-2}

([Hin26, (7.11)]), as δ_g = (δ*_g)* and G_g is symmetric. On stationary sections the spectral family of (□^C_b)* at zero
energy is the formal adjoint of P^C_b for the pairing B(u, w) := ∫_X g_b⁻¹(u, w̄) |dg_b|_X|, |dg_b| = |dt_*| ⊗ |dg_b|_X|,
by the argument of [[lem:iii-d1-2-1]] (1): a cut-off θ(t_*) with ∫θ = 1, the terms with θ′ and θ″ integrating to zero.
We write (P^C_b)* for it.

**Theorem {#thm:iii-e-1-1}** (The constraint propagation operator; [Hin26, Theorem 7.1] in dimension 4 + 1.) Let
(v_C, e_C) = (1/2, 1/102400) and C_0 ∈ [3/2, 100]. Let c_C be the stationary past timelike 1-form of [[sec:iv4-0]],
which lies in ρC^∞(X̄; T*X) and equals |x|⁻¹(dt − v_C d|x|) for large |x| up to O(m₀|x|⁻³) d|x|, and let γ_C = h⁻¹ with
h ∈ 𝖧, the set of [[eq:iv4-0-1]]: every h ∈ (0, h_*) outside a countable set. Then for all b near b₀:

(1) (*Mode stability, σ ≠ 0.*) For σ ≠ 0, Im σ ≥ 0, (□^C_b)^(σ) has trivial nullspace on 𝒜^γ(X̄; E) for every γ ∈ ℝ.

(2) (*Enhanced mode stability, σ = 0.*) □^C_b satisfies the hypotheses (H1)–(H4) of [[sec:i-a-1]] with a horizon
threshold ½ + ϑ_ℋ < −C_0, and for every α with α + 2 ∈ [−C_0, 2) and every s ≥ −C_0,

    P^C_b : {ω ∈ H̄_b^(s,α) : P^C_b ω ∈ H̄_b^(s−1,α+2)} → H̄_b^(s−1,α+2)

is invertible, with the Euclidean density ([[eq:i-c-3-1]]).

(3) (*Indicial roots.*) The indicial roots of P^C_b satisfy Re ι ≥ 2 or Re ι < −C_0; the only root with real part 2 is
ι = 2, a simple root of scalar type 0 and of scalar type 1. At each type and degree as many roots, with multiplicity,
have real part ≥ 2 as have real part < −C_0: two each at scalar type 0, three each at scalar type l ≥ 1, one each at
vector type l ≥ 1. The roots are simple; at scalar type l none lies in {1 − l, 3 − l, l + 3, l + 5} ∖ {2}, at vector type
l ≥ 2 none lies in {1 − l, 2 − l, l + 3, l + 4}; and a root whose real part is an integer in [3, 51] is real.

(4) (*tf-admissibility.*) □^C_b is tf-admissible ([[def:i-c-5-1]]) with every weight in [−C_0, 2).

Parts (1)–(3) are [[thm:iv4-2-1]], and (4) is [[thm:iv6-4-1]]. The clauses of (3) after the first sentence are the
inputs (C1)–(C4) of the indicial analysis of the linearised gauge-fixed Einstein operator in [[ch:s15]].

The structure near infinity is that of [Hin26, (7.3)–(7.6)] with the shift 3/2:

    □^C_b = −2 ∂_(t_*) ρ (ρ∂_ρ − 3/2 − S̄^C) + P^C_b + Q ∂_(t_*) + R ∂²_(t_*),

with S̄^C of spectrum γ_C{2(1 − v_C), (1 − e_C)(1 − v_C), 1 − v_C (three times)} ([[prop:np-10-21]] (i)), and
P^C_b − P̄^C ∈ ρ⁴ Diff²_b against the Minkowski model □̄^C := 2 δ̄ Ḡ δ̄*_(Ē_C), as in [[lem:iii-d2-2-1]]: the
modification E^C has coefficients in ρC^∞, and c_C differs from the model's |x|⁻¹(dt̄ − v_C d|x|) by ρ³C^∞.

Below, C_0, v_C, e_C, c_C and γ_C are fixed as in [[thm:iii-e-1-1]], and b is near b₀. *An unweighted b-density is used
near ∂X*, as in [Hin26, Section 7.2], unless the Euclidean density is named; for it, H̄_b^(k,β)(|dx|) =
H̄_b^(k,β+2)(μ_b) ([[sec:i-c-1-2]]). The function χ ∈ C^∞(X̄) equals 1 near ∂X and 0 near {|x| ≤ r_h}.

### The damping constants {#sec:iv4-0}

The bundle E, the operators □^C_b, P^C_b and (P^C_b)* are those of [[sec:iii-e-1]]. Write h := γ_C⁻¹. Then

    E^C_g ω = h⁻¹ (2 c_C ⊗_s ω − (2/3)(1 − e_C) g ι_(g⁻¹c_C) ω)

is the modification C_(g,c,e,h) of [Hin26a, (3.1)] with the trace weight 2/3 in place of 1, and □^C_b = □^(C_h)_g of
[Hin26a, (3.2)], with

    h² □^C_b = 2h² δ_g G_g δ*_g − i L_(g,c,e,h),     L_(g,c,e,h) = 4ih δ_g(c ⊗_s ·) + 2ihe d ι_(c♯).        {#eq:s14-lh}

The weight 2/3 = 2/(D − 2) is the one for which h G_g E^C ω has the form 2c ⊗_s ω − e g⟨c, ω⟩ for every e
([[prop:np-10-12]] (i)). With the weight 1, the literal transcription of the four-dimensional operator, the conclusions
below fail: at the constants v_C = 1/2, e_C = 1/102400 of [[eq:iv4-0-1]] the scalar type 0 then has, for all small
h > 0, an indicial root near ι_w = (1 + 5e_C)/(3 − 5e_C), which lies in (1/3, 1), so a root with real part in (−1, 1)
([[prop:np-10-12]] (iv)); and the fibre inner product B of [[prop:np-10-13]] (i) is indefinite.

*The constants.* We fix, once for the whole stability theory,

    v_C := 1/2,     e_C := 1/102400,     C_0 ∈ [3/2, 100],     γ_C := h⁻¹,  h ∈ 𝖧,                          {#eq:iv4-0-1}

where 𝖧 := (0, h_*) ∖ 𝖹. Here h_* := min(10⁻⁶, h_0, h_tf), with h_0 the smaller of the thresholds of
[[thm:iv5-7-3]] at these (v_C, e_C), with the regularity range C₁ := C_0 + 1, for the weights [[eq:iv4-2-1]] at C_0
and at C_0 − 1, and h_tf the threshold of [[thm:iv6-3-1]]; and 𝖹 := 𝖹₁ ∪ 𝖹₂ ∪ 𝖹₃ ⊂ (0, 10⁻⁶] is the countable set
made of the set 𝖹₁ of [[lem:iv4-1-3]] (b) and the sets 𝖹₂, 𝖹₃ of [[prop:np-10-52]] (ii), (iii). The set 𝖹₂ is
empty, the point 10⁻⁶ is not in 𝖹, and 𝖹 meets [5·10⁻¹¹, 10⁻⁶] ([[sec:s14-exceptional]]). The nonlinear theorem
of [[ch:s27]] takes C_0 = 100.
The 1-form c_C is that of [[prop:np-10-14]] at m = 1 and r_0 = 100, smoothed near r_0/2 and 2r_0 as in
[[prop:np-10-14]] (b), with ε small enough that (i) and (ii) of that proposition hold, only on [r_0/4, r_0/2] and
[2r_0, 3r_0], so that it is unchanged on [r_0/2, 2r_0] and equals r⁻¹(dt − v_C dr) for r ≥ 3r_0, and rescaled to m₀
(every condition on it depends on m r_0⁻² and r/r_0 only, by scaling). It is stationary and equals |x|⁻¹(dt − v_C d|x|)
for large |x| up to O(m₀|x|⁻³) d|x|: [[prop:np-10-14]] states this in the static time, and the
time t of [[sec:iii-b-3-1]] is the outgoing Kerr–Schild time, whose differential differs from the static one by
O(m₀|x|⁻²) d|x|, which changes |x|⁻¹(dt − v_C d|x|) by O(m₀|x|⁻³) d|x|.

Every result of this chapter that names (v_C, e_C, C_0, γ_C) uses these values, and so do all later chapters; the
results that [[thm:vi-c-adm-holds]] (1) lists hold as well with γ_C = h⁻¹ at every admissible point
([[def:vi-c-admissible]]). The
statements of [Hin26, Theorem 7.1] "for v_C ∈ (0, 1), C_0 > 0 and all sufficiently large γ_C" are proved here at this
choice: for every γ_C > 1/h_* outside a countable set, which is what every later use requires, as each takes one
admissible γ_C.

### The model at infinity: indicial families and the damping symbols {#sec:s14-model}

This section collects the facts about the constraint propagation operator on 4 + 1 Minkowski space and on
Tangherlini space that the proofs of [[sec:iv4-1]] use. Throughout it, D = 5 is the spacetime dimension, n = 4,
κ := l(l + 2) is the eigenvalue of the Laplacian of 𝕊³ on spherical harmonics of degree l, v ∈ (0, 1), e ∈ [0, 1) and
h > 0, and

    E^C ω = h⁻¹ (2c ⊗_s ω − m_tr(1 − e) g ι_(g⁻¹c) ω)

is the modification with trace weight m_tr; □^C := 2δ_g G_g (δ*_g + E^C). We write ⟨·, ·⟩ for the pairing by g⁻¹,
G(ζ) := g⁻¹(ζ, ζ), c♯ := g⁻¹c and div ω := ∇^a ω_a = −δω.

**Lemma {#lem:s14-box-c}** (The operator as a wave operator plus a first-order damping.) Let m_tr = 2/(D − 2) = 2/3
and let g be Ricci-flat. Then □^C = □_g + h⁻¹ 𝓛_c, where □_g = −∇^a ∇_a on 1-forms and

    𝓛_c ω = −2 (div ω) c − 2 ∇_(ω♯) c − 2 (div c) ω − 2 ∇_(c♯) ω + 2e d⟨c, ω⟩.                            {#eq:s14-lc}

*Proof.* Since tr_g g = D, G_g(f g) = (1 − D/2) f g, and G_g(2c ⊗_s ω) = 2c ⊗_s ω − g⟨c, ω⟩. Hence

    h G_g E^C ω = 2c ⊗_s ω + (−1 + m_tr(1 − e)(D/2 − 1)) g⟨c, ω⟩,

and the coefficient of g⟨c, ω⟩ is −e for every e exactly when m_tr(D/2 − 1) = 1, that is m_tr = 2/(D − 2). With δ(f g) =
−df and δ(2c ⊗_s ω)_a = −∇^b(c_a ω_b + c_b ω_a) = −(∇_(ω♯)c)_a − c_a div ω − (div c) ω_a − (∇_(c♯)ω)_a, this gives 2δ_g
G_g E^C ω = h⁻¹ 𝓛_c ω. Finally 2δ_g G_g δ*_g ω = 2δδ*ω + d(div ω), and 2(δδ*ω)_a = −∇^b∇_a ω_b − ∇^b∇_b ω_a = −∇_a(div
ω) − Ric(g)_a^b ω_b − ∇^b∇_b ω_a; on a Ricci-flat metric the sum is −∇^b∇_b ω = □_g ω. ∎

**Proposition {#prop:np-10-12}** (The indicial families on 4 + 1 Minkowski space.) Let g = η = −dt² + dr² + r² 𝑔̸ on
ℝ_t × ℝ⁴, c = r⁻¹(dt − v dr), let S be a spherical harmonic of degree l on 𝕊³, and let V be a co-closed eigen-1-form of
the Laplacian on 𝕊³ of degree l ≥ 1 (vector type), so that r V is a 1-form on ℝ⁴ whose Cartesian components are
r^(−l) times harmonic polynomials of degree l.

(i) (*The trace weight.*) h G_g E^C ω equals 2c ⊗_s ω − e g⟨c, ω⟩ for every e if and only if m_tr = 2/3. With m_tr = 1
it equals 2c ⊗_s ω − e′ g⟨c, ω⟩ with e′ = (3e − 1)/2.

(ii) (*The indicial families.*) Let m_tr = 2/3. For ι ∈ ℂ and constants A, B, C,

    □^C (r^(−ι)(A S dt + B S dr + C r dS)) = r^(−ι−2)(A′ S dt + B′ S dr + C′ r dS),   (A′, B′, C′)ᵀ = N_l(ι)(A, B, C)ᵀ,
    □^C (r^(−ι) r V) = N_(v,l)(ι) r^(−ι−2) r V,

with N_(v,l)(ι) = h⁻¹ p_(v)(ι), p_(v)(ι) := −hι² + (2h − 2v)ι + hκ + 6v, and hN_l(ι) the matrix with rows

    ( h(κ − ι² + 2ι) − 2v(ι − 2),   2(ι − 2),   2κ ),
    ( 2e(ι + 1),   h(κ + 3 − ι² + 2ι) + 2ev(ι + 1) − 4v(ι − 2),   −2κ(h + v) ),                             {#eq:s14-nl}
    ( −2e,   −2(ev + h),   h(κ − 1 − ι² + 2ι) − 2v(ι − 3) )

for l ≥ 1; at l = 0 the term with dS is absent and hN_0(ι) is the upper left 2 × 2 block of hN_l(ι) at κ = 0.

(iii) (*The polynomials.*) Let P_l(ι) := det(hN_l(ι)) for l ≥ 1, a polynomial of degree 6 in ι with leading coefficient
−h³, and P_0(ι) := det(hN_0(ι)). Then

    P_0(ι) = −(ι − 2) C(ι),
    C(ι) := −h²ι³ + h(2h + 2ev − 6v)ι² + (3h² + 2ehv + 12hv + 4e(1 + v²) − 8v²)ι + 6hv + 4e(1 + v²) + 16v²,
                                                                                                          {#eq:s14-c0}

and P_1(2) = 0. At h = 0,

    P_l(ι)|_(h=0) = 8v(ι − 2) Q_5(ι),     Q_5(ι) := e((v² − 1)κ + (1 + v²)(ι − 3)(ι + 1)) − 2v²(ι − 2)(ι − 3),
                                                                                                          {#eq:s14-q5}

which at e = 0 is −16v³(ι − 3)(ι − 2)². Giving ι the weight 1 and κ the weight 2, the parts of top weight of P_l and of
p_(v) are h³(κ − ι²)³ and h(κ − ι²).

(iv) (*The weight 1 fails.*) Let m_tr = 1 and e ∈ [0, 1/3). At h = 0 the scalar type l = 0 has the indicial root
ι_w := (7v² − 1 + 3e(1 + v²))/(5v² + 1 − 3e(1 + v²)), which at e = 0 lies in (−1, 1) for every v ∈ (0, 1), and at
v = 1/2 equals (1 + 5e)/(3 − 5e), which lies in (1/3, 1) for 0 < e < 1/5; and for every sufficiently small h > 0 the
scalar type 0 has an indicial root ι_w(h) with ι_w(h) → ι_w as h → 0⁺.

*Proof.* (i) is the first identity in the proof of [[lem:s14-box-c]], which uses only tr_g g = D; with m_tr = 1
and D = 5 the coefficient is −1 + (3/2)(1 − e) = −e′.

(ii) η is flat, so [[lem:s14-box-c]] applies. On stationary 1-forms □_η = −Δ componentwise in the frame dt, dx^i, Δ
the Euclidean Laplacian of ℝ⁴. In the splitting by dt, dr and r dS, −Δ(r^(−ι)S) = (κ + 2ι − ι²) r^(−ι−2) S, and for
the spatial part

    −Δ(r^(−ι)(B S dr + C r dS)) = r^(−ι−2)( ((κ + 3 + 2ι − ι²)B − 2κC) S dr + (−2B + (κ − 1 + 2ι − ι²)C) r dS ),

which follows from two identities. First, d(r^α S) = r^(α−1)(αS dr + r dS) and Δd = dΔ give Δ d(r^α S) = (α(α + 2) − κ)
r^(α−3)((α − 2)S dr + r dS). Second, the Cartesian components of r^β S x·dx = r^(β+1) S dr are r^β S x_i, and Δ(r^β S
x_i) = Δ(r^β S) x_i + 2∂_i(r^β S) gives Δ(r^(β+1) S dr) = r^(β−1)((β(β + 2) − κ + 2β) S dr + 2 r dS). Writing r^(−ι)(B
S dr + C r dS) = C d(r^(1−ι)S) + (B − (1 − ι)C) r^(−ι) S dr and adding (α = 1 − ι, β = −ι − 1) gives the formula. The
vector type gives −Δ(r^(−ι) r V) = (κ + 2ι − ι²) r^(−ι−2) r V, the Cartesian components of r^(−ι) r V being r^(−ι−l)
times harmonic polynomials of degree l. These are the terms with the factor h. For the damping, c♯ = −r⁻¹(∂_t + v∂_r),
div c = r⁻³∂_r(r³ c_r) = −2v r⁻² and, with ∇dr = r⁻¹(dx² − dr ⊗ dr) (dx² the Euclidean metric), ∇c = −r⁻² dr ⊗ dt − v
r⁻²(dx² − 2 dr ⊗ dr), where (∇c)(X, Y) = (∇_X c)(Y). Inserting these into [[eq:s14-lc]], with ⟨c, ω⟩ = −r⁻¹(ω_t + v
ω_r) for ω = ω_t dt + ω_r dr + ω_⊥ and div(r^(−ι)S dt) = 0, gives the terms without the factor h; for the vector type
⟨c, V⟩ = 0 and div V = 0, and only −2∇_(c♯)ω − 2(div c)ω − 2∇_(ω♯)c contribute, giving −2v(ι − 3).

(iii) Setting κ = 0 in the upper left block and expanding gives [[eq:s14-c0]], and the leading coefficient of P_l comes
from the diagonal. At l = 1 (κ = 3) and ι = 2 the rows of [[eq:s14-nl]] are (3h, 0, 6), (6e, 6h + 6ev, −6(h + v)) and
(−2e, −2(ev + h), 2h + 2v), and the determinant is
3h(12(h + ev)(h + v) − 12(h + v)(h + ev)) + 6(−12e(ev + h) + 12e(h + ev)) = 0. At h = 0 the rows are
(−2v(ι − 2), 2(ι − 2), 2κ), (2e(ι + 1), 2ev(ι + 1) − 4v(ι − 2), −2κv) and (−2e, −2ev, −2v(ι − 3)). Adding v times the
second column to the first makes the first column (0, a₂, a₃)ᵀ with a₂ = 2e(1 + v²)(ι + 1) − 4v²(ι − 2) and
a₃ = −2e(1 + v²). Expanding along it,

    det = 4v( a₂((ι − 2)(ι − 3) − eκ) + a₃κ((ι − 2) − e(ι + 1)) ).

The terms in e²κ cancel, and what remains is 4v(ι − 2)(2e(1 + v²)(ι + 1)(ι − 3) − 4v²(ι − 2)(ι − 3) + 2eκ(v² − 1)),
which is [[eq:s14-q5]]. The parts of top weight come from the product of the diagonal terms h(κ − ι² + …), the other
terms of the expansion having lower weight, and from −hι² + hκ.

(iv) By (i), the operator with m_tr = 1 is the operator with m_tr = 2/3 and e replaced by e′ = (3e − 1)/2, and the
proofs of (ii)–(iii) do not use the sign of e; so its scalar type 0 polynomial is P_0 = −(ι − 2)C with e′ for e. At
h = 0, [[eq:s14-c0]] is the linear polynomial (4e(1 + v²) − 8v²)ι + 4e(1 + v²) + 16v², whose root is
(4v² + e(1 + v²))/(2v² − e(1 + v²)); with e′ for e this is ι_w, and the leading coefficient 4e′(1 + v²) − 8v² is
negative, as e′ < 0 for e < 1/3. At e = 0, ι_w = (7v² − 1)/(5v² + 1), which increases from −1 to 1 as v runs over
(0, 1). At v = 1/2, 7v² − 1 = 3/4 and 5v² + 1 = 9/4, so ι_w = (3/4 + 15e/4)/(9/4 − 15e/4) = (1 + 5e)/(3 − 5e), which
exceeds 1/3 for e > 0, as 3(1 + 5e) > 3 − 5e, and is below 1 for e < 1/5, as 1 + 5e < 3 − 5e. The coefficients of C
are polynomials in h, so by Hurwitz's theorem, as in [[lem:s14-small-h]] (b), C has a root ι_w(h) → ι_w as h → 0⁺; it
differs from 2, so it is a root of P_0. ∎

From now on in this section (v, e) = (1/2, 1/102400), and we write P_l, p_(v), C and Q_5 for the polynomials of
[[prop:np-10-12]] at this point. Then 4Q_5(ι) = e(5(ι − 3)(ι + 1) − 3κ) − 2(ι − 2)(ι − 3).

**Lemma {#lem:s14-q5}** (The polynomial Q_5.) For every l ≥ 0:

(a) Q_5(2) = −(15 + 3κ)e/4 ≠ 0, and Q_5(x) < 0 for every real x ≤ 1 and every real x ≥ 4.

(b) The two roots of Q_5 are distinct, and their sum is (10 − 10e)/(2 − 5e) = 5 + 1/13653.

*Proof.* (a) For x ≥ 4, (x + 1)/(x − 2) ≤ 5/2, so 5e(x − 3)(x + 1) ≤ (25/2)e(x − 2)(x − 3) < 2(x − 2)(x − 3), and
4Q_5(x) < −3eκ ≤ 0. For x ≤ 1, |x − 2| ≥ 1 and |x + 1| ≤ |x − 2| + 3 ≤ 4|x − 2|, so 5e|x − 3||x + 1| ≤ 20e(x − 2)(x − 3)
< 2(x − 2)(x − 3), and again 4Q_5(x) < 0. (b) Q_5(ι) = αι² + βι + γ with α = 5e/4 − 1/2, β = 5(1 − e)/2 and
γ = −3 − 15e/4 − 3eκ/4. The sum of the roots is −β/α = (10 − 10e)/(2 − 5e). The discriminant is
β² − 4αγ = (1 − 10e)²/4 − (3e/2)(1 − 5e/2)κ, which vanishes only at κ = (1 − 10e)²/(6e(1 − 5e/2)) = 232971380/13653,
not an integer. ∎

**Lemma {#lem:s14-small-h}** (The roots as h → 0.) Fix l. As h → 0⁺:

(a) for l ≥ 1, three roots of P_l converge to the roots 2, ι₊, ι₋ of (ι − 2)Q_5(ι), which are pairwise distinct, and
the other three satisfy hι → 1/τ_j, j = 1, 2, 3, where τ_j are the roots of

    T(τ) := (τ + 1)((5e − 2)τ² + (e − 3)τ − 1),                                                          {#eq:s14-ttau}

which are pairwise distinct and negative; in particular the real parts of these three roots tend to −∞;

(b) at l = 0, one root of C converges to (4 + 5e)/(2 − 5e) ≠ 2 and the other two satisfy hι → 1/τ_j for the two roots
τ_j of the quadratic factor of [[eq:s14-ttau]];

(c) the two roots of p_(v) are real and distinct for every h > 0, of opposite signs.

*Proof.* (a) Every entry of [[eq:s14-nl]] is a polynomial in (ι, h) whose terms h^a ι^b have b ≤ a + 1, so the
coefficient of h^a in P_l has degree at most a + 3 in ι, and P_l(ι)|_(h=0) = 8v(ι − 2)Q_5(ι) has degree 3 with leading
coefficient 8v(e(1 + v²) − 2v²) ≠ 0. By Hurwitz's theorem three roots converge to the roots of (ι − 2)Q_5, and these are
distinct by [[lem:s14-q5]]. Substituting ι = 1/(hτ) and multiplying by h³τ⁶, the terms h^a ι^b with b = a + 3 give, at
h = 0, the polynomial 8v(e(1 + v²) − 2v²)τ³ + (4e(1 + 2v²) − 20v²)τ² + 2v(e − 4)τ − 1, read off from the products of
the terms of top degree in ι of the entries; the other terms carry positive powers of h. At v = 1/2 this is T(τ).
Its constant term is −1, so three roots of the rescaled polynomial converge to the roots of T. The quadratic factor has
discriminant e² + 14e + 1 > 0, product of roots 1/(2 − 5e) > 0 and sum (3 − e)/(5e − 2) < 0, and its value at τ = −1
is 4e ≠ 0. (b) is the same argument applied to [[eq:s14-c0]]: at h = 0, C is linear with root
(4v² + e(1 + v²))/(2v² − e(1 + v²)) = (4 + 5e)/(2 − 5e), and the terms h^a ι^(a+1) of C give the quadratic factor of
T. (c) The product of the roots of p_(v) is −(hκ + 6v)/h < 0. ∎

**Proposition {#prop:np-10-54}** (The indicial roots for every h ∈ (0, 10⁻⁶].) For every h ∈ (0, 10⁻⁶]:

(i) no root of p_(v), of P_0 or of P_l, l ≥ 1, has real part in [−100, 19/10]; with multiplicity, p_(v) has one root
with real part > 19/10 and one with real part < −100, P_0 has two and two, and P_l, l ≥ 1, three and three;

(ii) the only roots with real part in [−100, 2] are ι = 2 at l = 0 and at l = 1, each simple;

(iii) (*no accumulation in a strip*) for every R > 0 only finitely many l have a root of P_l or of p_(v) in the strip
{|Re ι| ≤ R}; so, over all types and degrees, only finitely many roots lie in each such strip, and the real parts of
the roots accumulate only at ±∞. In particular for every R > 0 only finitely many roots satisfy |ι| ≤ R.

*Proof.* *The vector type.* p_(v)(ι) = −(hι² − (2h − 1)ι − hκ − 3). At ι = 2, hι² − (2h − 1)ι − hκ − 3 = −hκ − 1 < 0,
so 2 lies strictly between the two real roots of [[lem:s14-small-h]] (c), and the larger root exceeds 2. At ι = −100
the same quantity is h(10200 − κ) − 103 ≤ 10200·10⁻⁶ − 103 < 0, so the smaller root is below −100.

*Scalar type 0.* P_0 = −(ι − 2)C. We show C > 0 on [−100, 2]. Write C = C₀ + C_h with C₀ := (5e − 2)ι + 5e + 4, the
value at h = 0, and C_h := −h²ι³ + h(2h + e − 3)ι² + (3h² + eh + 6h)ι + 3h. On [0, 2],
C_h = 3h(1 + 2ι − ι²) + h²ι(3 + 2ι − ι²) + ehι(ι + 1) ≥ 3h, as 1 + 2ι − ι² ≥ 1 and 3 + 2ι − ι² > 0 there, and
C₀ ≥ C₀(2) = 15e; so C > 0. On [−100, 0], C₀ ≥ 5e + 4 > 4, and −h²ι³ ≥ 0, h(2h + e − 3)ι² ≥ −3·10⁴h,
(3h² + eh + 6h)ι ≥ −700h, so C ≥ 4 − 0.031 > 0. Hence ι = 2 is a simple root of P_0 and C has no real root in
[−100, 2]. As C(ι) → −∞ for ι → +∞ and C(2) > 0, C has one or three real roots in (2, ∞). The sum of the three roots of
C is (2h² + eh − 3h)/h² = 2 − (3 − e)/h < −2.9·10⁶; so C has exactly one root ι₁ > 2, and the other two have sum
< −2.9·10⁶ − ι₁: if they are not real, their common real part is below −100; if they are real, neither lies in
[−100, 2] nor in (2, ∞), so both are below −100.

*Scalar type l ≥ 1.* Let h ∈ (0, 10⁻⁶] and l ≥ 1. By [[prop:s14-scalar-every-h]], counted with multiplicity, P_l has
three roots with real part less than −1/(2h) and three with real part at least 2; for l ≥ 2 the latter have real part
greater than 2, and for l = 1 they are the simple root ι = 2 and two roots with real part greater than 2. As
−1/(2h) ≤ −5·10⁵ < −100 and 2 > 19/10, P_l has no root with real part in [−100, 19/10], and exactly three roots with
real part > 19/10 and three with real part < −100; for l ≥ 2 no root has real part in (19/10, 2]; and at l = 1 the only
root with real part in (19/10, 2] is ι = 2, a simple root.

(iii) Fix h. By [[prop:np-10-12]] (iii), P_l(ι) = h³(κ − ι²)³ + Σ_(j+2k≤5) a_(jk)ι^jκ^k, with coefficients a_(jk)
depending on (v, e, h) and not on l: the part of top weight is h³(κ − ι²)³, and every other term has weight
at most 5. Put ι = κ^(1/2)w. Then

    κ⁻³P_l(κ^(1/2)w) = h³(1 − w²)³ + Σ_(j+2k≤5) a_(jk)κ^(j/2+k−3)w^j,

a polynomial in w of degree 6 with leading coefficient −h³ and the other coefficients bounded for κ ≥ 1, since
j/2 + k − 3 ≤ −1/2. So its roots lie in a disc |w| ≤ W independent of l, and on that disc it converges uniformly to
h³(1 − w²)³ as κ → ∞. By Hurwitz's theorem, for κ large its six roots lie within ½ of ±1, three near each; so every
root of P_l satisfies |Re ι| ≥ ½κ^(1/2) once κ ≥ κ_h, for some κ_h depending on h. Likewise
κ⁻¹p_(v)(κ^(1/2)w) = h(1 − w²) + (2h − 2v)κ^(−1/2)w + 6vκ⁻¹, whose two roots tend to ±1. Hence a root
with |Re ι| ≤ R occurs only where κ < κ_h or κ ≤ 4R², that is for finitely many l, each contributing at most six
roots. ∎

**Remark {#rem:s14-u6}** (Numerical observation.) At v = 1/2, for e, h ∈ {10⁻², 10⁻³, 10⁻⁴} and 85 sampled degrees
l ≤ 10⁶, the roots were computed to 50 digits. Besides ι = 2 at l = 1, the three roots of P_l that stay bounded as
h → 0 ([[lem:s14-small-h]] (a)) stayed above 1.93; they were above 2 exactly at the six points with h ≤ e, and between
1.939 and 1.967 at the three with h > e. The other three lay near −1/h; at h = e = 10⁻² the largest of them was −96.3,
inside [−100, 2). This is why h is taken below e_C in [[eq:iv4-0-1]]. No proof uses this observation.

**Proposition {#prop:np-10-13}** (The fibre algebra and the damping symbols.) Let g be a Lorentzian metric on a vector
space of dimension D, c a past timelike covector, e ∈ [0, 1), and

    ℓ(ζ)ω := 2(⟨c, ζ⟩ω + ⟨ζ, ω⟩c − e⟨ω, c⟩ζ),     B := g⁻¹ − (1 + e)G(c)⁻¹ c♯ ⊗ c♯,                      {#eq:s14-ell}

the semiclassical principal symbol of L_(g,c,e,h) in [[eq:s14-lh]] ([Hin26a, Lemma 3.2]).

(i) B is positive definite for e > 0; ℓ(ζ) is B-self-adjoint for every ζ; and the characteristic polynomial of ½ℓ(ζ) is
(ν − ⟨c, ζ⟩)^(D−2) times ν² − (3 − e)⟨c, ζ⟩ν + 2(1 − e)⟨c, ζ⟩² + eG(c)G(ζ). Hence ℓ(ζ) is negative definite if and only
if ⟨c, ζ⟩ < 0 and 2(1 − e)⟨c, ζ⟩² + eG(c)G(ζ) > 0. With the trace weight 1 in place of 2/3, the damping symbol has this
form with e′ = (3e − 1)/2 < 0, for which B is indefinite.

(ii) (*The bundle map S, and the critical sets on 𝗌𝖿.*) Let g be a Lorentzian metric on a manifold of dimension D, c
a past timelike 1-form, e ∈ (0, 1), and A := (2ih)⁻¹L_(g,c,e,h) = 2δ_g(c ⊗_s ·) + e dι_(c♯). Let
K(X, Y) := (∇_X c)(Y), K_s its symmetric part, tr K := g^(μν)K_(μν) = div c, F(ω) := (dc)(ω♯, c♯) and G := G(c). Then
S := A + A*, A* the formal adjoint of A for |dg| and the fibre inner product B, is the bundle map given by
B(Sω, ω′) = s(ω, ω′), where

    s(ω, ω′) := −2K_s(ω♯, ω′♯) − (tr K)⟨ω, ω′⟩ + (1 + e)G⁻¹(⟨c, ω⟩F(ω′) + ⟨c, ω′⟩F(ω))
                + ((1 + e)²G⁻¹ tr K + 2(1 − e²)G⁻²K(c♯, c♯))⟨c, ω⟩⟨c, ω′⟩.                                {#eq:s14-s}

So S is B-self-adjoint, and S(λc) = λS(c) for λ > 0; it is the map S of [Hin26a, Lemma 3.9]. On 4 + 1 Minkowski
space with c = r⁻¹(dt − v dr), let w := ρ_sf^(b_sf) ρ_K^(b_K) with ρ_sf = 1/r, ρ_K = r/t, and d := b_sf − b_K. The
entries of T := r²(−ℓ(dw/w) + S) are polynomials in e; at e = 0 its eigenvalues are 2v(1 − d), 4v(1 − d) and
2v(2 − d) (three times) at ρ_K = 0, and, at b_K = 0, the same with d = b_sf at every ρ_K. They are positive if and
only if d < 1.

(iii) (*The interior saddle.*) With c = r_0⁻²(r_0 dt − v(r − r_0) dr) on Minkowski space and e ∈ (0, 1), at a point
r = r_0(1 + xe^(1/2)/v) > 0 at which c is timelike, that is ex² < 1, r₀²S is block diagonal in the splitting by dt, dr
and r dω: the angular block is v(6e^(1/2)x + v)/(e^(1/2)x + v) Id; and as e → 0 with x and v fixed, the trace and the
determinant of the (dt, dr) block tend to 5v and 2v²(3 − 2x²), which are positive for |x| ≤ 6/5 < (3/2)^(1/2). At
(v, e) = (1/2, 1/102400) the block has trace and determinant

    tr = (614401x³ + 24575920x² − 73400524800x − 4194312192000) / (102400 (x − 320)(x + 160)(x + 320)),
    det = N(x) / (51200 (x − 320)²(x + 160)²(x + 320)²),
    N(x) = 409601x⁶ + 32767960x⁵ − 536975114601600x⁴ − 171809597046784000x³ − 13737721299599360000x²
           + 773097888153600000x + 20615943684096000000,

both positive for |x| ≤ 6/5; so r₀²S is positive definite there.

(iv) (*The saddle's neighbourhood.*) For c as in (iii) and r ∈ [r_0/2, 2r_0], ℓ(±dr) is negative definite for
±(r − r_0) ≥ r_0 e^(1/2)/v as long as c is timelike.

*Proof.* (i) Split the covectors as ℝc ⊕ c^⊥. As c is timelike, g⁻¹ is positive definite on c^⊥, and B(c, X) = 0 for
X ∈ c^⊥, B(c, c) = −eG(c) > 0; so B is positive definite. Using ⟨½ℓ(ζ)ω, c⟩ = (1 − e)⟨ζ, c⟩⟨ω, c⟩ + G(c)⟨ζ, ω⟩,

    B(½ℓ(ζ)ω, ω′) = ⟨ζ, c⟩⟨ω, ω′⟩ − e⟨ζ, ω⟩⟨c, ω′⟩ − e⟨c, ω⟩⟨ζ, ω′⟩ − (1 − e²)G(c)⁻¹⟨ζ, c⟩⟨ω, c⟩⟨ω′, c⟩,

which is symmetric in (ω, ω′). Let ζ ∉ ℝc; the case ζ ∈ ℝc follows by continuity. On the (D − 2)-dimensional space
orthogonal to c and ζ, ½ℓ(ζ) = ⟨c, ζ⟩; on span{c, ζ},
½ℓ(ζ)c = 2⟨c, ζ⟩c − eG(c)ζ and ½ℓ(ζ)ζ = G(ζ)c + (1 − e)⟨c, ζ⟩ζ, a matrix with trace (3 − e)⟨c, ζ⟩ and determinant
2(1 − e)⟨c, ζ⟩² + eG(c)G(ζ). The eigenvalues are real, ℓ(ζ) being B-self-adjoint, and all are negative exactly under
the stated conditions. With the weight 1, [[prop:np-10-12]] (i) replaces e by e′, and B(c, c) = −e′G(c) < 0 while B is
positive on c^⊥.

(ii) *The formula for S.* In index notation, Aω = ∇_μ(M^μω) with (M^μω)_a := −c_aω^μ − c^μω_a + e⟨c, ω⟩δ^μ_a, as
2δ(c ⊗_s ω)_a = −∇^μ(c_aω_μ + c_μω_a) and e(d⟨c, ω⟩)_a = e∇_μ(⟨c, ω⟩δ^μ_a). For a covector ζ, ζ_μM^μ = −½ℓ(ζ),
which is B-self-adjoint by (i); so each M^μ is B-self-adjoint. Expanding the divergence, Aω = M^μ∇_μω + 𝒩ω with the
bundle map 𝒩 := ∇_μM^μ (ω held parallel),

    (𝒩ω)_a = −K(ω♯, ∂_a) − (tr K)ω_a + eK(∂_a, ω♯).

For compactly supported ω, ω′,

    B(Aω, ω′) = ∇_μ(B(M^μω, ω′)) − (∇_μB)(M^μω, ω′) − B(M^μω, ∇_μω′),

and B(M^μω, ∇_μω′) = B(ω, M^μ∇_μω′) = B(ω, Aω′) − B(ω, 𝒩ω′). The divergence integrates to zero against |dg|, so
∫(B(Aω, ω′) + B(ω, Aω′))|dg| = ∫(B(ω, 𝒩ω′) − (∇_μB)(M^μω, ω′))|dg|: A + A* is the bundle map S with

    B(Sω, ω′) = B(ω, 𝒩ω′) − (∇_μB)(M^μω, ω′).

We evaluate the two terms. First, B(ω, 𝒩ω′) = ⟨ω, 𝒩ω′⟩ − (1 + e)G⁻¹⟨c, ω⟩⟨c, 𝒩ω′⟩, with

    ⟨ω, 𝒩ω′⟩ = −K(ω′♯, ω♯) − (tr K)⟨ω, ω′⟩ + eK(ω♯, ω′♯),
    ⟨c, 𝒩ω′⟩ = −K(ω′♯, c♯) − (tr K)⟨c, ω′⟩ + eK(c♯, ω′♯).

Second, ∇_μB = −(1 + e)∇_μ(G⁻¹c♯ ⊗ c♯) with ∂_μG = 2K(∂_μ, c♯); with

    ⟨c, M^μω⟩∂_μ = −Gω♯ − (1 − e)⟨c, ω⟩c♯,     Σ_μ(∇_μc)(M^μω) = −K(ω♯, c♯) − K(c♯, ω♯) + e(tr K)⟨c, ω⟩,

this gives

    (∇_μB)(M^μω, ω′) = −(1 + e)( G⁻¹(K(ω♯, c♯) − K(c♯, ω♯))⟨c, ω′⟩ − (1 − e)G⁻¹⟨c, ω⟩K(c♯, ω′♯) − K(ω♯, ω′♯)
                        + G⁻²(2(1 − e)K(c♯, c♯) + eG tr K)⟨c, ω⟩⟨c, ω′⟩ ).

In the difference the terms in K(ω♯, ω′♯) and K(ω′♯, ω♯) give −2K_s(ω♯, ω′♯), the terms linear in ⟨c, ω⟩ give
(1 + e)G⁻¹⟨c, ω⟩F(ω′), those linear in ⟨c, ω′⟩ give (1 + e)G⁻¹⟨c, ω′⟩F(ω), and the rest is the last line of
[[eq:s14-s]]. So B(Sω, ω′) = s(ω, ω′), which is symmetric. B does not change under c ↦ λc, and every term of s has
degree 1 in c.

*A stationary radial 1-form on Minkowski space.* Let c = a(r) dt + b(r) dr on 4 + 1 Minkowski space, with a² > b².
With ∇dt = 0 and ∇dr = r⁻¹Π, Π := dx² − dr ⊗ dr (dx² the Euclidean metric),

    K = a′ dr ⊗ dt + b′ dr ⊗ dr + (b/r)Π,     tr K = b′ + 3b/r,     dc = a′ dr ∧ dt;

and with (dt)♯ = −∂_t, (dr)♯ = ∂_r and c♯ = −a∂_t + b∂_r: G = b² − a², ⟨c, ω⟩ = −aω_t + bω_r,
F(ω) = a′(bω_t − aω_r) and K(c♯, c♯) = b(bb′ − aa′). K, Π and ⟨c, ·⟩ have no component mixing span{dt, dr} with the
angular covectors, so S is block diagonal in the splitting by dt, dr and r dω, free of the angles, and scalar on
r dω, where B = g⁻¹ and s = −(2b/r + tr K)⟨·, ·⟩:

    S = −(b′ + 5b/r)     on r dω.                                                                         {#eq:s14-s-ang}

On span{dt, dr}, in the basis (dt, dr), the matrices of s and B are

    s = (0, a′; a′, −2b′) + (tr K)(1, 0; 0, −1) + (1 + e)a′G⁻¹(−2ab, a² + b²; a² + b², −2ab)
        + ((1 + e)²G⁻¹ tr K + 2(1 − e²)G⁻²b(bb′ − aa′))(a², −ab; −ab, b²),
    B = (−1, 0; 0, 1) − (1 + e)G⁻¹(a², −ab; −ab, b²),                                                     {#eq:s14-s-rad}

and S = B⁻¹s, the rows being the components of Sω.

*The critical sets on 𝗌𝖿.* For c = r⁻¹(dt − v dr), a = r⁻¹ and b = −vr⁻¹, so a′ = −r⁻², b′ = vr⁻², tr K = −2vr⁻²,
G = −(1 − v²)r⁻² and K(c♯, c♯) = −v(1 − v²)r⁻⁴. [[eq:s14-s-rad]] gives

    r²s = (1 − v²)⁻¹ ( 2v(2e² + 3e + v²),  4e²v² + 5ev² + e + 2v² ;  4e²v² + 5ev² + e + 2v²,  2v(1 + e)(2ev² + 1) ),
    B = (1 − v²)⁻¹ ( e + v²,  (1 + e)v ;  (1 + e)v,  1 + ev² ),     det B = e,

and so

    r²S = (1 − v²)⁻¹ ( v(5 + 3e − 2v²),  1 + 2v² + 3ev² ;  −(3v² + 4ev² − e),  v(1 + e)(1 − 4v²) ) ⊕ 4v Id,

the angular entry being −r²(b′ + 5b/r) = 4v. Next, dw/w = −d dr/r − b_Kρ_K dt/r, so
T = d rℓ(dr) + b_Kρ_K rℓ(dt) + r²S, and by [[eq:s14-ell]], with rc = dt − v dr,

    rℓ(dr) = ( −2v, 2 ; 2e, −4v + 2ev ) ⊕ (−2v) Id,     rℓ(dt) = ( 2(e − 2), 2ev ; 2v, −2 ) ⊕ (−2) Id.

So T is block diagonal with angular block 2v(2 − d) − 2b_Kρ_K, and its (dt, dr) block at ρ_K = 0, d rℓ(dr) + r²S,
has characteristic polynomial q_(v,e)(ν) with

    q_(v,e)(ν) = ν² − (6v + 4ev − (6 − 2e)vd)ν − (4e(1 + v²) − 8v²)d² − (4e(1 + v²) + 16v²)d + 8v² + 8ev² − e.

At e = 0, q_(v,0)(ν) = (ν − 2v(1 − d))(ν − 4v(1 − d)). At b_K = 0 the terms in ρ_K vanish, and T is the same with
d = b_sf.

(iii) Here a = r_0⁻¹ and b = −v(r − r_0)r_0⁻², so a′ = 0, b′ = −vr_0⁻² and F = 0. Put q := e^(1/2) and y := qx/v,
so that r = r_0(1 + y) and r_0b = −qx; by hypothesis 1 + y > 0, that is v + qx > 0, and 1 − ex² > 0. Then

    r_0²a² = 1,     r_0²b² = ex²,     r_0²b′ = −v,     r_0²G = ex² − 1,
    r_0² tr K = −v(1 + 4y)/(1 + y) = −v(v + 4qx)/(v + qx).

By [[eq:s14-s-ang]] the angular entry of r_0²S is v + 5vy/(1 + y) = v(6qx + v)/(qx + v).

On span{dt, dr} we use the basis c, f with f := b dt + a dr. Then ⟨c, f⟩ = −ab + ba = 0 and G(f) = a² − b² = −G. The
vectors c♯ = −a∂_t + b∂_r and f♯ = −b∂_t + a∂_r lie in span{∂_t, ∂_r}, on which Π vanishes, so on them
K(X, Y) = b′ dr(X) dr(Y), with dr(c♯) = b and dr(f♯) = a: K(c♯, c♯) = b′b², K(c♯, f♯) = K(f♯, c♯) = b′ab and
K(f♯, f♯) = b′a². In [[eq:s14-s]], F = 0 and ⟨c, f⟩ = 0 leave only the first two terms in s(c, f) and s(f, f), and with
⟨c, c⟩ = G, [[eq:s14-s]] and the definition of B in [[eq:s14-ell]] give

    s(c, c) = −2b′b² − G tr K + (1 + e)²G tr K + 2(1 − e²)b′b² = e(−2eb′b² + (2 + e)G tr K),
    s(c, f) = −2b′ab,     s(f, f) = −2b′a² + G tr K,
    B(c, c) = G − (1 + e)G = −eG,     B(c, f) = 0,     B(f, f) = G(f) = −G.

As B(Sω, ω′) = s(ω, ω′), the matrix of S in the basis c, f is the inverse of the Gram matrix of B times that of s; the
former is diagonal, so on span{dt, dr}

    tr S = s(c, c)/B(c, c) + s(f, f)/B(f, f),     det S = (s(c, c)s(f, f) − s(c, f)²)/(B(c, c)B(f, f)).

In tr S the factor e of s(c, c) cancels against B(c, c) = −eG. In det S, B(c, c)B(f, f) = eG², the factor e of
s(c, c) cancels, and s(c, f)² = 4b′²a²b², where r_0²b² = ex², so e cancels there too. Multiplying by r_0² and r_0⁴ and
inserting the values above, the (dt, dr) block of r_0²S has

    tr = 2v(1 + e²x²)/(1 − ex²) − (3 + e)r_0² tr K,
    det = ((2ve²x² − (2 + e)(1 − ex²)r_0² tr K)(2v − (1 − ex²)r_0² tr K) − 4v²x²)/(1 − ex²)²,

valid for every e ∈ (0, 1). With x and v fixed these are rational functions of q, and their denominators, 1 − ex²,
(1 − ex²)² and the factor v + qx of r_0² tr K, equal 1, 1 and v at q = 0. So both are continuous at q = 0 and tend, as
e → 0, to their values at q = 0, where r_0² tr K = −v: the trace to 2v + 3v = 5v and the determinant to
2v·3v − 4v²x² = 2v²(3 − 2x²). At |x| ≤ 6/5 the latter is at least 2v²(3 − 72/25) > 0. Inserting (v, q) = (1/2, 1/320),
that is (v, e) = (1/2, 1/102400), into the two formulas, with 1 − ex² = −(x − 320)(x + 320)/102400 and
v + qx = (x + 160)/320, gives the stated functions.
For |x| ≤ 6/5 the denominator of tr is negative and its numerator is at most −4194312192000 + 73400524800·(6/5) +
24575920·(36/25) + 614401·(216/125) < 0, so tr > 0. The denominator of det is positive. Write N(x) = A₀ + A₁x + A₂x² +
A₃x³ + A₄x⁴ + A₅x⁵ + A₆x⁶ with the coefficients displayed. For |x| ≤ 6/5, A₀ + A₂x² ≥ A₀ + (36/25)A₂ > 8.3·10¹⁷; the
function x(A₁ + A₃x²) is increasing there, as A₁ + 3A₃x² ≥ A₁ + (108/25)A₃ > 0, so
x(A₁ + A₃x²) ≥ −(6/5)(A₁ + (36/25)A₃) > −6.4·10¹⁷; and A₄x⁴ + A₅x⁵ + A₆x⁶ > −1.2·10¹⁵. Hence N(x) > 1.8·10¹⁷ > 0.
At (v, e) = (1/2, 1/102400) the angular entry is (3x + 80)/(x + 160) > 0. So the block, B-self-adjoint with positive
trace and determinant, is positive definite, and so is r_0²S.

(iv) By (i) with ζ = ±dr: G(dr) = 1, ⟨c, ±dr⟩ = ∓v(r − r_0)r_0⁻² and G(c) = r_0⁻⁴(−r_0² + v²(r − r_0)²). With w := v²(r
− r_0)²/r_0² < 1 (c timelike), the second condition of (i) reads 2(1 − e)w > e(1 − w), and for w ≥ e, 2(1 − e)w/(e(1 −
w)) ≥ 2 > 1. The first condition is ±(r − r_0) > 0. ∎

**Remark {#rem:s14-e0}** (Numerical observation.) On a grid of 1201 points in x with bisection in e, the largest e for
which the (dt, dr) block of [[prop:np-10-13]] (iii) stays positive definite on |x| ≤ 6/5 was about 0.000069v²,
against about 0.000154v² for the corresponding block in dimension 3 + 1. No proof uses this observation.

**Proposition {#prop:np-10-14}** (A damping 1-form on Tangherlini space.) Let m = 1, so that r_h = 1, and let

    g = −f dt² + 2(1 − f) dt dr + (2 − f) dr² + r² 𝑔̸,     f = 1 − mr⁻²,                                   {#eq:s14-tang}

the Tangherlini metric in Kerr–Schild time, regular across the horizon; its t differs from the static time by
∫(f⁻¹ − 1) dr, and g⁻¹ has (t, r) block g^(tt) = −1 − mr⁻², g^(tr) = mr⁻², g^(rr) = f. Let r_0 := 100 and

    c := (2r_0)⁻¹(dt + (v/2) dr)  (r ≤ r_0/2),   ½ r_0⁻²(r_0 dt − v(r − r_0) dr)  (r_0/2 ≤ r ≤ 2r_0),
    c := r⁻¹(dt − v dr)  (r ≥ 2r_0).                                                                      {#eq:s14-cform}

Then c is continuous, and:

(i) r c is past timelike at every r > 0;

(ii) ⟨c, dr⟩ > 0 on (0, r_0 − r_0e^(1/2)/v] and ⟨c, dr⟩ < 0 on [r_0 + r_0e^(1/2)/v, ∞), and on both intervals
f eG(c) + 2(1 − e)⟨c, dr⟩² > 0; so ℓ(−dr), resp. ℓ(dr), is negative definite there ([[prop:np-10-13]] (i));

(iii) on r_0/2 ≤ r ≤ 2r_0 the bundle map S of [[eq:s14-s]], for the metric [[eq:s14-tang]] and the 1-form
[[eq:s14-cform]], is free of the angles and block diagonal in the splitting by dt, dr and r dω; for [[eq:s14-tang]]
with m = 0, that is on Minkowski space, it is ½ times the S of [[prop:np-10-13]] (iii), the middle piece of
[[eq:s14-cform]] being ½ times the 1-form there; and it is positive definite on |r − r_0| ≤ (6/5)r_0e^(1/2)/v;

(iv) for c = r⁻¹(dt − v dr) on Minkowski space, T = r²(−ℓ(dw/w) + S) of [[prop:np-10-13]] (ii) is B-self-adjoint and
depends on ρ_K and the weights only, and the characteristic polynomial of its (dt, dr) block at ρ_K = 0 is q(d,
ν)/102400,

    q(d, ν) := 102400ν² − (307202 − 307199d)ν + 204795d² − 409605d + 204801;                              {#eq:s14-q}

its eigenvalues are positive at the corner ∂K⁺ (ρ_K = 0) if and only if b_K > b_sf − b*, and at the sink R_v (b_K = 0)
if and only if b_sf < b*, where b* = 0.99340731… is the smaller root of 204795d² − 409605d + 204801;

(v) the condition 2(1 − e)(v − ρ)²/(e(1 − v²)) > 1 − ρ² of [Hin26a, (5.8)] holds for ρ = r/t in
[δ_r, v(1 − δ_sf)] ∪ [v(1 + δ_sf), 10], with δ_sf = 1/100 and every δ_r > 0.

Moreover: (a) conditions (4)–(5) of [Hin26a, Proposition 5.1], which [[lem:iv4-1-4]] restates, off 𝗌𝖿, for
0 < ρ_sf ≤ 2δ_r with some δ_r > 0, follow from (iv) by continuity, since Tangherlini space differs from its Minkowski
model by terms in ρ_sf C^∞ ([Hin26a, p. 39]);
(b) for every ε ∈ (0, r_0/4] there is a smooth 1-form c_ε equal to c outside (r_0/2 − ε, r_0/2) ∪ (2r_0, 2r_0 + ε),
so on [r_0/2, 2r_0] and for r ≥ 3r_0, with c_ε − c → 0 uniformly as ε → 0; for ε small enough c_ε satisfies (i) and
(ii), which involve only the 1-form and not its derivatives ([Hin26a, p. 41]); (c) in the static time t_s the outer
piece is r⁻¹(dt_s − v dr) + O(mr⁻³) dr.

*Proof.* All three pieces have the form α(dt + b dr) with α > 0; at r_0/2 and 2r_0 adjacent pieces agree, so c is
continuous. With g^(tr) = 1 − f,

    α⁻²G(c) = −2 + 2b + f(1 − b)²,   α⁻¹⟨c, dt⟩ = −(2 − b) + f(1 − b),   α⁻¹⟨c, dr⟩ = 1 − f + fb,

with b = 1/4 for r ≤ 50, b = (100 − r)/200 ∈ [−1/2, 1/4] for 50 ≤ r ≤ 200, and b = −1/2 for r ≥ 200; and f < 1.

(i) For b ∈ [−1/2, 1/4], f(1 − b)² < (1 − b)² ≤ (3/2)(1 − b) and so α⁻²G(c) < −2(1 − b) + (3/2)(1 − b) < 0; and
α⁻¹⟨c, dt⟩ < −(2 − b) + (1 − b) = −1. So c is timelike and in the cone of dt, which is past.

(ii) *r ≤ 50.* α⁻¹⟨c, dr⟩ = 1 − 3f/4 ≥ 1/4. If f ≤ 0, f eG(c) ≥ 0; if 0 < f < 1, α⁻²|G(c)| ≤ 3/2 and
α⁻²(f eG(c) + 2(1 − e)⟨c, dr⟩²) ≥ −3e/2 + (1 − e)/8 > 0. *50 ≤ r ≤ 100 − 0.625*, where r_0e^(1/2)/v = 0.625: here
b ≥ 1/320 = e^(1/2), f ≥ 1 − 1/2500, α⁻¹⟨c, dr⟩ ≥ fb > 0, and α⁻²|G(c)| = (1 − b)(2 − f(1 − b)) ≤ (1 − b)(1 + b + r⁻²)
≤ 1 + 1/2500. So α⁻²·2(1 − e)⟨c, dr⟩² ≥ 2(1 − e)f²b² ≥ 1.99e > 1.0004e ≥ α⁻² f e|G(c)|. *100.625 ≤ r ≤ 200*: here
b ≤ −1/320, |b| ≥ e^(1/2), r⁻² ≤ 10⁻⁴ ≤ 0.032|b|, so α⁻¹⟨c, dr⟩ ≤ r⁻² − f|b| ≤ −0.967|b| < 0, and
α⁻²·2(1 − e)⟨c, dr⟩² ≥ 1.87b² ≥ 1.87e, while α⁻² f e|G(c)| ≤ eα⁻²|G(c)| = e(1 − b)(2 − f(1 − b)) =
e(1 − b² + r⁻²(1 − b)²) ≤ e(1 + 10⁻⁴) ≤ 1.0002e, as r = 100(1 − 2b) and (1 − b)/(1 − 2b) ≤ 1 for b ≤ 0. *r ≥ 200*:
α⁻¹⟨c, dr⟩ = r⁻² − f/2 < −0.49, α⁻²|G(c)| ≤ 3, and 2(1 − e)·0.24 > 3e.

(iii) On r_0/2 ≤ r ≤ 2r_0, c = c_t dt + c_r dr with c_t = (2r_0)⁻¹ and c_r = −v(r − r_0)/(2r_0²); it is closed, so
F = 0 in [[eq:s14-s]]. We first let m ≥ 0 be general. The Christoffel symbols of [[eq:s14-tang]] with indices in
{t, r} are

    Γ^t_tt = m²r⁻⁵,     Γ^t_tr = m(m + r²)r⁻⁵,     Γ^t_rr = m(m + 2r²)r⁻⁵,
    Γ^r_tt = m(r² − m)r⁻⁵,     Γ^r_tr = −m²r⁻⁵,     Γ^r_rr = −m(m + r²)r⁻⁵;

for angular indices A, B, Γ^λ_(AB) = −r g^(λr)𝑔̸_(AB) (λ ∈ {t, r}), and Γ^λ_(tA) = Γ^λ_(rA) = 0 for λ ∈ {t, r}. Hence
K_(μν) = ∂_μc_ν − Γ^λ_(μν)c_λ has no component mixing {t, r} with the angles; its angular part is (c^r/r)Π, with
Π := r²𝑔̸ and c^r := ⟨c, dr⟩ = mr⁻²c_t + fc_r; and on {t, r}

    K_tt = −Γ^t_tt c_t − Γ^r_tt c_r,     K_tr = K_rt = −Γ^t_tr c_t − Γ^r_tr c_r,
    K_rr = −v/(2r_0²) − Γ^t_rr c_t − Γ^r_rr c_r,

with tr K = g^(tt)K_tt + 2g^(tr)K_tr + g^(rr)K_rr + 3c^r/r. As on Minkowski space, s and B do not mix span{dt, dr} with
the angular covectors, on which ⟨c, ·⟩ vanishes; so S is block diagonal and free of the angles, and on r dω it is the
scalar −(2c^r/r + tr K). On span{dt, dr}, in the basis (dt, dr), with g⁻¹ the matrix of the (t, r) block of g⁻¹ and
c♯ = g⁻¹(c_t, c_r)ᵀ, [[eq:s14-s]] reads

    s = −2g⁻¹Kg⁻¹ − (tr K)g⁻¹ + ((1 + e)²G⁻¹ tr K + 2(1 − e²)G⁻²K(c♯, c♯)) c♯c♯ᵀ,     B = g⁻¹ − (1 + e)G⁻¹c♯c♯ᵀ,

and S = B⁻¹s. At m = 0, [[eq:s14-tang]] is Minkowski space and c is ½ times the 1-form of [[prop:np-10-13]] (iii), so
S is ½ times the S there, by the homogeneity in (ii) of that proposition.

Now let m = 1, r_0 = 100, (v, e) = (1/2, 1/102400) and r = 100 + 5x/8; the window |r − r_0| ≤ (6/5)r_0e^(1/2)/v = 3/4
is |x| ≤ 6/5. Inserting the formulas above, the angular entry is

    −(2c^r/r + tr K) = (6vr³ − 5vr_0r² − 4mvr + 3mvr_0 − 3mr_0)/(2r_0²r³) = (3r³ − 250r² − 2r − 150)/(20000r³),

positive for r ≥ 99, as 3r³ − 250r² = r²(3r − 250) ≥ 47r² > 2r + 150. The (dt, dr) block has

    tr = n_T(x)/(51200000000(x + 160)³(x + 320)(25x³ − 1920064x − 204820480)),
    det = n_D(x)/(2560000000000000(x + 160)⁶(x + 320)²(25x³ − 1920064x − 204820480)²),

where n_T = Σ_(k=0)^7 t_kx^k and n_D = Σ_(k=0)^(14) d_kx^k have the integer coefficients of the table of the trace and
determinant numerators on Tangherlini space in [[sec:tab-s14-numerators]]; among them

    t_0 = −1718058975468810403840000,     d_0 = 691283997693777039477894644527792128000000,
    d_1 = 31003448547550721811482399641771704320000,     d_2 = −460291250745815174622431267350323920896000,
    d_3 = −28803457351687623824496336970154455859200.

For |x| ≤ 6/5, 25x³ − 1920064x − 204820480 ≤ 25·(216/125) + 1920064·(6/5) − 204820480 < 0, so the denominator of tr is
negative and that of det is positive. Next Σ_(k≥1)|t_k|(6/5)^k < 8.93·10²² < −t_0, so n_T < 0 and tr > 0. For n_D,
d_0 + d_2x² ≥ d_0 + (36/25)d_2 > 2.846·10⁴⁰, as d_2 < 0. The odd cubic p(x) := d_1x + d_3x³ (d_1 > 0 > d_3)
increases on |x| ≤ x_* := (d_1/(3|d_3|))^(1/2) < 0.6 and decreases outside, so on [−6/5, 6/5] its minimum is
min(p(−x_*), p(6/5)) > −1.26·10⁴⁰; and Σ_(k≥4)|d_k|(6/5)^k < 1.72·10³⁹.
So n_D > 2.846·10⁴⁰ − 1.26·10⁴⁰ − 1.72·10³⁹ > 1.4·10⁴⁰, and det > 0. The block, B-self-adjoint with positive trace
and determinant, is positive definite, and with the angular entry S is positive definite on the window.

(iv) By [[prop:np-10-13]] (ii) at (v, e) = (1/2, 1/102400): 2v(2 − d) = 2 − d, and 102400 q_(1/2,e)(ν) = q(d, ν). The
two roots of q(d, ·) are real (T is B-self-adjoint); their sum (307202 − 307199d)/102400 is positive iff
d < 307202/307199, and their product q(d, 0)/102400 is positive iff d < b* or d > b*′, where
b*, b*′ = (409605 ∓ 7372845^(1/2))/409590, so b* = 0.99340731… and b*′ = 1.00666… > 307202/307199. So all eigenvalues
are positive iff d < b* (which also gives 2 − d > 0). At ρ_K = 0, d = b_sf − b_K; at the sink b_K = 0 and T does not
depend on ρ_K, so d = b_sf.

(v) 2(1 − e)/(e(1 − v²)) = 273064, and |ρ − 1/2| ≥ 1/200 gives 273064(ρ − 1/2)² ≥ 6.8 > 1 ≥ 1 − ρ².

(a) The positivity in (iv) is strict and stable under perturbations of the metric and the 1-form by ρ_sf C^∞ terms
near 𝗌𝖿.

(b) Let c_in, c_mid and c_out be the three formulas of [[eq:s14-cform]], each smooth on r > 0. Choose smooth χ₁, χ₂ with
values in [0, 1], χ₁ = 1 on (0, r_0/2 − ε] and χ₁ = 0 on [r_0/2, ∞), χ₂ = 1 on (0, 2r_0] and χ₂ = 0 on [2r_0 + ε, ∞).
Put c_ε := c_in + (1 − χ₁)(c_mid − c_in) for r ≤ 2r_0 and c_ε := c_mid + (1 − χ₂)(c_out − c_mid) for r ≥ r_0/2. Both
formulas give c_mid on [r_0/2, 2r_0], so c_ε is well defined and smooth. It equals c outside the two intervals; on
(r_0/2 − ε, r_0/2), c_ε − c = (1 − χ₁)(c_mid − c_in), and on (2r_0, 2r_0 + ε), c_ε − c = χ₂(c_mid − c_out). As adjacent
pieces agree at r_0/2 and at 2r_0, these tend to 0 uniformly as ε → 0. The conditions of (i) and (ii) are strict
inequalities between continuous functions of r and of the value of the 1-form at r. They hold for c on the compact sets
[r_0/4, r_0/2] and [2r_0, 3r_0], which lie in (0, r_0 − r_0e^(1/2)/v] and in [r_0 + r_0e^(1/2)/v, ∞) respectively, so
they hold there with a positive margin, and they hold for c_ε once ε is small. Elsewhere c_ε = c.

(c) The static time t_s satisfies dt = dt_s + (f⁻¹ − 1) dr with f⁻¹ − 1 = O(mr⁻²). ∎

**Remark {#rem:s14-r0}** (Numerical observation.) Among integer values of r_0, with m = 1 and
(v, e) = (1/2, 1/102400), conditions (i)–(iii) of [[prop:np-10-14]] held together first at r_0 = 86: (i) at every
r_0 ∈ [2, 86], (ii) from r_0 = 33 on, and (iii), among these, at 86 alone; with e/4 in place of e the first such r_0
was 137. Every condition depends on mr_0⁻² and r/r_0 only, so the threshold is 86r_h. No proof uses this observation.

**Proposition {#prop:np-10-21}** (The structure at infinity.) On 4 + 1 Minkowski space with c = r⁻¹(dt − v dr), in the
coordinates t_* = t − r, ρ = r⁻¹ and the Cartesian frame:

(i) □^C = −2∂_(t_*) ρ(ρ∂_ρ − 3/2 − S̄^C) plus a stationary operator: the coefficient of ∂_(t_*)∂_r is 2 Id, there is no
term ∂_(t_*) times a tangential derivative and no ∂²_(t_*) term, and S̄^C = h⁻¹M with

    M(dr) = 2(1 − v) dr + (1 − ev) dt_*,     M(dt_*) = (1 − e)(1 − v) dt_*,     M = (1 − v) on r dω;

so in the splitting by dr, dt_* and r dω, S̄^C is lower triangular with diagonal h⁻¹(2(1 − v), (1 − e)(1 − v), 1 − v),
diagonalisable, with spectrum h⁻¹{2(1 − v), (1 − e)(1 − v), 1 − v (three times)}, all positive for 0 < v < 1, 0 ≤ e < 1;

(ii) (*the radial sets*) on stationary sections, the first-order part of (□^C)^(0) in the radial direction is that of
−Δ plus 2ρh⁻¹N∂_r, where

    Nω := vω − ω_r(dt − v dr) − e(ω_t + vω_r) dr,     ω = ω_t dt + ω_r dr + ω_⊥;

and M + 2N = D M_(−v) D, where M_(−v) is M with −v for v and D is the reflection
ω_t dt + ω_r dr + ω_⊥ ↦ ω_t dt − ω_r dr + ω_⊥. So h⁻¹(M + 2N) is diagonalisable, with spectrum
h⁻¹{2(1 + v), (1 − e)(1 + v), 1 + v (three times)}. Consequently the number ϑ_in of [[sec:i-a-1-4]] for the spectral
family of □^C, evaluated with a fibre inner product in which an eigenbasis of M + 2N is orthonormal, is

    ϑ_in = −2h⁻¹(1 − e)(1 + v),     (−1 + ϑ_in)/2 = −½ − h⁻¹(1 − e)(1 + v);                {#eq:s14-theta-in}

and the same holds for □^C_b, b near b₀, with c_C. Moreover the isometry t ↦ −t of η carries c_v := r⁻¹(dt − v dr)
to −c_(−v), so it conjugates □^C with (c_v, h⁻¹) to the operator with (c_(−v), −h⁻¹);

(iii) (*the weights*) over a slab 0 ≤ t ≤ Tr the weight rises by 1/2 in every dimension, as
∫_0^(Tr) ρ^(−2a) r^(n−1) dt = Tρ^(−2a−1) r^(n−1); ρ^k lies in ρ^a L²(r³ dr) near infinity iff a < k − 2, so pointwise
bounds r⁻¹ and 1 put data in ρ^(−2−ε) H̄_b(r³|dr d𝑔̸|) for every ε > 0; α_sf + 1/2 = −C_0 − 2 gives α_sf = −C_0 − 5/2;
and the range α + 2 ∈ [−C_0, 2) is α ∈ [−C_0 − 2, 0) for the density r³|dr d𝑔̸|.

*Proof.* (i) Write n_i = x_i/r. In (t_*, x), ∂_t = ∂_(t_*) and ∂_i|_t = ∂_i|_(t_*) − n_i ∂_(t_*). By
[[lem:s14-box-c]], □^C = □_η + h⁻¹𝓛_c, and □_η = ∂²_t − Δ acts componentwise; as |n| = 1 and Σ_i ∂_i n_i = 3/r,
∂²_t − Δ = −Δ + 2∂_(t_*)(∂_r + 3/(2r)) = −Δ − 2∂_(t_*)ρ(ρ∂_ρ − 3/2), the terms ∂²_(t_*) cancelling. In h⁻¹𝓛_c the
derivatives in t_* come from three terms. Write ω = ω_t dt + ω_r dr + ω_⊥. In div ω = −∂_tω_t + ∂_iω_i the
∂_(t_*)-part is −∂_(t_*)(ω_t + ω_r); in ∇_(c♯)ω, c♯ = −r⁻¹(∂_t + v n_i∂_i) has the part −r⁻¹(1 − v)∂_(t_*); and in
d⟨c, ω⟩, ⟨c, ω⟩ = −r⁻¹(ω_t + vω_r) and df has the part ∂_(t_*)f (dt − dr). So the ∂_(t_*)-part of h⁻¹𝓛_cω is
2ρh⁻¹∂_(t_*)Mω with

    Mω = (dt − v dr)(ω_t + ω_r) + (1 − v)ω − e(dt − dr)(ω_t + vω_r),

which on dr and dt_* = dt − dr gives the stated values. The other terms of 𝓛_c contain no derivative in t_*. The
triangular form gives the spectrum, and M is diagonalisable since 2(1 − v) ≠ (1 − e)(1 − v) and M is scalar on r dω.

(ii) On stationary sections ∂_(t_*) acts as 0 and the spatial derivatives are those at fixed t_*. In h⁻¹𝓛_c the
radial derivatives come from the same three terms as in (i): div ω contains ∂_rω_r; c♯ = −r⁻¹((1 − v)∂_(t_*) + v∂_r)
in (t_*, x), so −2∇_(c♯)ω contains 2r⁻¹v∂_rω; and d⟨c, ω⟩ contains ∂_r⟨c, ω⟩ dr = −r⁻¹∂_r(ω_t + vω_r) dr plus terms
of order zero. So the radial first-order part of h⁻¹𝓛_c is 2ρh⁻¹N∂_r. The identity M + 2N = D M_(−v) D: by (i) and the
definition of N,

    (M + 2N)ω = (dt − v dr)(ω_t − ω_r) + (1 + v)ω − e(dt + dr)(ω_t + vω_r),

and D M_(−v) Dω is the same expression, since M_(−v)ω = (dt + v dr)(ω_t + ω_r) + (1 + v)ω − e(dt − dr)(ω_t − vω_r) and D
reverses the signs of dr and of ω_r. So the spectrum of M + 2N is that of M_(−v), read off (i), and it is diagonalisable
as M_(−v) is.

For ϑ_in, recall p_in = σ(ρ⁻¹Im_H P̂(0))|_(ρ=0, ξ=−2, η=0) and the structure [[eq:i-a-1-2]] of the spectral family,
here with S = S̄^C = h⁻¹M at ρ = 0. H denotes the fibre inner product of (ii). In the Cartesian frame, M + 2N depends
on the angles only, and we take H to depend on the angles only, as the eigenspaces of M + 2N allow. Adjoints are
taken for |dx|, as in [[sec:i-a-1]], and A^(*H) := H⁻¹A^†H for a matrix A. For a matrix-valued function A and a
vector field Y, (AY)^(*H) = −A^(*H)Y − H⁻¹Y(HA^(*H)) − (div Y)A^(*H), so

    Im_H(AY) = (Re_H A)(Y/i) + (2i)⁻¹(H⁻¹Y(HA^(*H)) + (div Y)A^(*H)).

We use this with A homogeneous of degree −1 and Y = ∂_r or Y = T_k := ∂_k − n_kn^j∂_j, the part of ∂_k tangent to the
spheres. The coefficients of these Y are homogeneous of degree 0 and their divergences, 3/r and −3n_k/r, of degree −1;
so the second term is of order zero and homogeneous of degree −2, that is r⁻² times a function of the angles, and
ρ⁻¹ times it vanishes at ρ = 0. And ρ⁻¹Re_H A is a function of the angles. The scattering symbols of ∂_r/i and T_k/i
at ξ dr + rη are ξ and (rη)_k, the Cartesian components of rη, which are linear in η.

The radial first-order term 2ρh⁻¹N∂_r, with A = 2ρh⁻¹N, therefore contributes 2h⁻¹(Re_H N)ξ to the symbol of
ρ⁻¹Im_H P̂(0) at ρ = 0, which is −4h⁻¹Re_H N at ξ = −2. The scalar part −Δ Id is symmetric for |dx|, and
−Δ − H⁻¹(−Δ)H = H⁻¹(2Σ_k(∂_kH)∂_k + ΔH) = H⁻¹(2Σ_k(∂_kH)T_k + ΔH), as Σ_k n_k∂_kH = ∂_rH = 0; here ∂_kH is homogeneous
of degree −1 and ΔH of degree −2, so ρ⁻¹Im_H(−Δ) has at ρ = 0 the symbol H⁻¹Σ_k(ρ⁻¹∂_kH)(rη)_k, which vanishes at
η = 0. The remaining terms of P̂(0) are those of h⁻¹𝓛_c other than 2ρh⁻¹N∂_r. Writing ∂_k = n_k∂_r + T_k, its other
first-order terms are tangential: the parts with T_k of −2(div ω)c and of 2e d⟨c, ω⟩, as −2∇_(c♯)ω differentiates
only along c♯ = −r⁻¹((1 − v)∂_(t_*) + v∂_r). They have the form Σ_k A^kT_k, with A^k a matrix whose entries are linear
in the components of c, hence homogeneous of degree −1; so ρ⁻¹Im_H(Σ_k A^kT_k) has at ρ = 0 the symbol
Σ_k(ρ⁻¹Re_H A^k)(rη)_k, which vanishes at η = 0. The terms of order zero of h⁻¹𝓛_c, namely −2∇_(ω♯)c, −2(div c)ω and
the part of 2e d⟨c, ω⟩ in which c is differentiated, have entries linear in the first derivatives of the components of
c, homogeneous of degree −2; so they and their H-adjoints are r⁻² times functions of the angles, and ρ⁻¹ times them
vanishes at ρ = 0. Hence at ρ = 0, η = 0 and ξ = −2 only the radial term contributes, p_in = −4h⁻¹Re_H N, and

    p_in − (S + S^(*H)) = −2h⁻¹ Re_H(M + 2N) = −2h⁻¹(M + 2N),

the last because an H-orthonormal eigenbasis makes M + 2N H-self-adjoint; its largest eigenvalue is
−2h⁻¹ min spec(M + 2N) = −2h⁻¹(1 − e)(1 + v), at every point of ∂X. For □^C_b, b near b₀, the difference
P^C_b − P̄^C lies in ρ⁴Diff²_b ⊂ ρ²Diff²_sc and S − S̄^C in ρC^∞ ([[lem:iv4-1-2]]), which do not change p_in or S at
ρ = 0. Finally, (t, x) ↦ (−t, x) preserves η and pulls dt back to −dt; c_v becomes −r⁻¹(dt + v dr) = −c_(−v), and E^C
changes sign with c, which is the operator with (c_(−v), −h⁻¹).

(iii) ρ^k ∈ ρ^a L²(r³ dr) near infinity iff ∫^∞ r^(2a−2k) r³ dr < ∞, that is 2k − 2a > 4. The rest is arithmetic. ∎

**Proposition {#prop:np-10-22}** (Tangherlini space as a 3sc-metric.) On Tangherlini space in Kerr–Schild time,
g = η + mr⁻² k ⊗ k with k = dt + dr:

(i) in Cartesian coordinates g⁻¹ = η⁻¹ − mr⁻² k♯ ⊗ k♯ exactly, with k♯ = η⁻¹k; the Christoffel symbols are polynomials
of degree at most 2 in m with no constant term and satisfy Γ(λx; m) = λ⁻¹Γ(x; mλ⁻²); and c = r⁻¹(dt − v dr) has
components homogeneous of degree −1;

(ii) r²g⁻¹(dτ, dτ) = −(1 − τ²) − mr⁻²(1 + τ)² and r g⁻¹(dτ, dt) = −1 − mr⁻²(1 + τ), τ = t/r;

(iii) g⁻¹(dr, dr) = f = 1 − mr⁻², increasing with f(r_h) = 0; g⁻¹(dr, dt) = mr⁻² > 0 and g⁻¹(dt, dt) = −1 − mr⁻² < 0
for every r > 0;

(iv) at (v, e) = (1/2, 1/102400) and the weights (α_K, α_sf) = (1, −C_0 − 5/2), that is b_K = 1 and
b_sf = −C_0 − 3/2: the characteristic polynomials of T at ∂K⁺ and at R_v have positive roots for every C_0 ≥ 0, and at
C_0 = 100, T is positive definite for every ρ_K ∈ [0, 10].

*Proof.* (i) k is η-null, so (η + Hk ⊗ k)(η⁻¹ − Hk♯ ⊗ k♯) = Id. With H = mr⁻², the components of g are those of η plus
m times functions homogeneous of degree −2 in x, and those of g⁻¹ likewise; the Christoffel symbols are
½g⁻¹∂g, of degree at most 2 in m and vanishing at m = 0. Under x ↦ λx, H(λx; m) = H(x; mλ⁻²) and k is invariant, and
the derivative contributes λ⁻¹. (ii)–(iii) are the (t, r) block of g⁻¹ (in [[prop:np-10-14]]) applied to
dτ = r⁻¹(dt − τ dr). (iv) At ∂K⁺, d = b_sf − b_K = −C_0 − 5/2 < b*, and at R_v, d = b_sf = −C_0 − 3/2 < b*, so
[[prop:np-10-14]] (iv) applies. At C_0 = 100 the angular entry of T is 2v(2 − d) − 2ρ_K = (209 − 4ρ_K)/2 > 0 for
ρ_K ≤ 10, and the (dt, dr) block, from the formulas of [[prop:np-10-13]] (ii), has trace
(63590199 − 1228796ρ_K)/204800 > 0 and determinant 3(1092260ρ_K² − 113048512ρ_K + 2925089043)/409600, which
is decreasing on [0, 10] (its vertex is at ρ_K > 51) and positive at ρ_K = 10. ∎

**Proposition {#prop:np-10-79}** (The horizon threshold.) Let g be Tangherlini space [[eq:s14-tang]], c the 1-form of
[[prop:np-10-14]] rescaled to m (so that c = (2r_0)⁻¹(dt + (v/2)dr) near the horizon, r_0 = 100r_h), B as in
[[eq:s14-ell]], P_0 := 2δ_gG_gδ*_g, and let the threshold ϑ_ℋ be defined as in [[sec:i-a-1]] ([Hin26c, (5.17)]) with
the fibre inner product B. At ζ = ξ dr over r = r_h, ξ > 0:

(i) the base component of H_G vanishes and ρ_∞⁻¹H_Gρ_∞ = f′(r_h) = 2/r_h for ρ_∞ = ξ⁻¹, so the factor 1/β_0 in
[Hin26c, (5.17)] is r_h/2; (dr)♯ = ∂_t, dr is future null, and a := ⟨c, dr⟩ = c_t(r_h) = (2r_0)⁻¹;

(ii) ρ_∞σ₁((P_0 − P_0^*)/(2i)) is X_s, the B-symmetric part of 2Γ_t, (Γ_t)_k^c = Γ^c_(tk); its eigenvalues are
±(e^(1/2) + e^(−1/2))/r_h and 0 (three times), free of v and of the factor of c;

(iii) ℓ(dr) is B-self-adjoint with eigenvalues 2a (three times), 4a and 2(1 − e)a;

(iv) ϑ_ℋ is the largest eigenvalue of (r_h/2)(X_s − h⁻¹ℓ(dr)): the larger of −ar_h/h, on r dω, and the larger root ν₊
of

    χ(ν) := ν² + (3 − e)sν + (1 + e)s + 2(1 − e)s² − (1 + e)²/(4e),     s := ar_h/h = 1/(200h);             {#eq:s14-chi}

(v) at (v, e) = (1/2, 1/102400), ½ + ϑ_ℋ < −100 for every h ∈ (0, h_2), where h_2 = 2.6197… · 10⁻⁵ is the positive root
of 31744512005000h² + 3077109850h − 102399; in particular for every h ∈ (0, 10⁻⁶]. At h = 10⁻⁶, ϑ_ℋ = −4995.83…; and
ϑ_ℋ ≤ ϑ_0 − c₁h⁻¹ with ϑ_0 = (r_h/2)(e^(1/2) + e^(−1/2))/r_h = 102401/640 and c₁ = (1 − e)ar_h = 102399/20480000.

*Proof.* (i) At r = r_h, g^(rr) = f = 0 and g^(tr) = mr_h⁻² = 1, so (dr)♯ = ∂_t and dr is null. As dt is past
timelike and dt(∂_t) = 1 > 0, ∂_t is future directed, so dr is future null. H_G = 2g^(ab)ζ_a∂_(x^b) − (∂_xG)∂_ζ; at
ζ = ξ dr its base component is 2ξ∂_t, which annihilates every stationary function, and H_Gξ = −ξ²∂_r g^(rr) =
−f′(r_h)ξ². For the rescaled field ρ_∞H_G, ρ_∞ = ξ⁻¹, this gives ρ_∞⁻¹(ρ_∞H_G)ρ_∞ = H_Gρ_∞ = f′(r_h) = 2mr_h⁻³ = 2/r_h.

(ii) On 1-forms, −∇^a∇_aω_k = −g^(ab)∂_a∂_bω_k + 2g^(ab)Γ^c_(ak)∂_bω_c + g^(ab)Γ^d_(ab)∂_dω_k + (order 0). The scalar
part −g^(ab)∂_a∂_b + g^(ab)Γ^d_(ab)∂_d is the scalar wave operator, formally self-adjoint for |dg|; its B-adjoint
differs from it by B⁻¹[·, B], whose principal symbol at ζ is a multiple of H_G B, and H_G B = 2ξ∂_tB = 0, B being
stationary. So only 2g^(ab)Γ^c_(ak)∂_b contributes; its symbol at ζ = ξ dr is 2iξ Γ_t, as ζ♯ = ξ∂_t, and σ₁((P −
P*)/(2i)) = ξ(Γ_t + Γ_t^(*B)). At r_h, with g_(tt) = −f, g_(tr) = 1 − f, g_(rr) = 2 − f, Γ^c_(tk) = ½g^(cd)(∂_kg_(dt) −
∂_dg_(tk)) gives, on the components (ω_t, ω_r), 2Γ_t = (2/r_h)(1, 0; 2, −1) (rows k = t, r), and Γ_t = 0 on the angular
components. With c = α(dt + b dr), b = v/2, one has G(c)α⁻² = 2(b − 1) and c♯α⁻¹ = (b − 2)∂_t + ∂_r. In the
components (ω_t, ω_r), writing matrices by rows with the row index the output component, at r = r_h

    g⁻¹ = (−2, 1; 1, 0),     B = (2(1 − b))⁻¹( (1 + e)b² − 4eb + 4e,  −(1 − e)b − 2e ;  −(1 − e)b − 2e,  1 + e ),

and the B-symmetric part X_s = ½(2Γ_t + B⁻¹(2Γ_t)ᵀB) of 2Γ_t has trace 0 and determinant −(1 + e)²/(e r_h²), for every
b. So its eigenvalues are ±(1 + e)/(e^(1/2)r_h).

(iii) is [[prop:np-10-13]] (i) with ζ = dr, G(dr) = 0, ⟨c, dr⟩ = a.

(iv) By the definition, ϑ_ℋ = (r_h/2) × the largest eigenvalue of ρ_∞σ₁((P_0 − P_0^*)/(2i)) − h⁻¹ℓ(dr), the
damping L contributing −h⁻¹ℓ(ζ)ρ_∞ ([[eq:s14-lh]]). On the angular components the matrix is −2a h⁻¹. On the (t, r)
block, [[eq:s14-ell]] gives, in the convention of (ii),

    ℓ(dr) = 2a( 2, 0 ; (1 − e)b + 2e, 1 − e ),

and the characteristic polynomial of (r_h/2)(X_s − h⁻¹ℓ(dr)), with X_s from (ii), is χ, for every b.

(v) At e = 1/102400, (1 + e)²/(4e) = 10485964801/409600. For h < h_2, s = 1/(200h) > 1/(200h_2) > 190 > 201/(3 − e),
so the vertex of χ is at −(3 − e)s/2 < −201/2, and ν₊ < −201/2 iff χ(−201/2) > 0; and

    χ(−201/2) = (102399 − 3077109850h − 31744512005000h²)/(2048000000h²),

which is positive iff h < h_2. The angular eigenvalue −s is below
−201/2 as well. At h = 10⁻⁶ the roots of χ are −10004.11… and −4995.83…. Finally X_s and ℓ(dr) are B-self-adjoint, so
by Weyl's inequality the largest eigenvalue of (r_h/2)(X_s − h⁻¹ℓ(dr)) is at most (r_h/2)(λ_max(X_s) −
h⁻¹λ_min(ℓ(dr))) = ϑ_0 − c₁h⁻¹. ∎

### The scalar type l ≥ 1 for every h ∈ (0, 10⁻⁶] {#sec:s14-every-h}

This section proves the statements of [[prop:np-10-54]] (i)–(ii) about the polynomials P_l, l ≥ 1, at every
h ∈ (0, 10⁻⁶]. As in [[sec:s14-model]], (v, e) = (1/2, 1/102400). Up to [[prop:s14-scalar-every-h]] the exact
value of e enters only through [[lem:s14-small-h]] (a), proved at this value: there the roots ι₊, ι₋ of Q_5 are
distinct by [[lem:s14-q5]] (b), whose proof uses it. Every inequality proved below uses only 10⁻⁶ < e < 10⁻⁵.
We let κ be any real number ≥ 0 and write P(ι; κ, h) for the determinant of the matrix [[eq:s14-nl]] at v = 1/2 with
this κ, so that P_l(ι) = P(ι; l(l + 2), h). It is a polynomial in (ι, κ, h), of degree 6 in ι with leading coefficient
−h³: this is f₆ of [[eq:s14-f-two]] below, and for κ = l(l + 2) it is [[prop:np-10-12]] (iii).

The argument has three steps. As (κ, h) varies, no root of P(·; κ, h) meets the line Re ι = 2, except the root ι = 2
at κ = 3 ([[lem:s14-line-two]]); no root meets the line Re ι = −1/(2h) ([[lem:s14-line-far]]); and the number of roots
on each side of these lines is read off in the limit h → 0⁺ from [[lem:s14-small-h]].

**Lemma {#lem:s14-half-plane-count}** (Counting roots in a half-plane.) Let Ω ⊂ ℝ² be connected, and for ϖ ∈ Ω let
p_ϖ(z) = a_n(ϖ)zⁿ + … + a_0(ϖ) be a polynomial whose coefficients are continuous functions on Ω, with a_n(ϖ) ≠ 0. Let
H ⊂ ℂ be an open half-plane with boundary line L. If no p_ϖ has a root on L, then the number of roots of p_ϖ in H,
counted with multiplicity, is the same for every ϖ ∈ Ω.

*Proof.* Fix ϖ₀ ∈ Ω. Every root z of p_ϖ satisfies |z| ≤ 1 + max_(j<n) |a_j(ϖ)/a_n(ϖ)|, and the right side is
continuous in ϖ. So there are a neighbourhood V of ϖ₀ in Ω and a number R, larger than the distance from 0 to L, such
that every root of p_ϖ, ϖ ∈ V, has modulus less than R. Let G := H ∩ {|z| < R}, a bounded convex open set whose
boundary Γ consists of a segment of L and an arc of the circle |z| = R. As p_(ϖ₀) has no root on Γ,
m₀ := min_Γ |p_(ϖ₀)| > 0, and after shrinking V, |p_ϖ − p_(ϖ₀)| < m₀ on Γ for ϖ ∈ V, since Γ is bounded and the
coefficients are continuous. By Rouché's theorem p_ϖ and p_(ϖ₀) have equally many roots in G, and these are all their
roots in H. So the number is locally constant on Ω, hence constant, Ω being connected. ∎

#### The line Re ι = 2 {#sec:s14-every-h-two}

At ι = 2 + w the matrix [[eq:s14-nl]] at v = 1/2 is, with a := κ − 2w − w²,

    ( ha − w,        2w,                          2κ               )
    ( 2e(w + 3),     h(a + 3) + e(w + 3) − 2w,    −(1 + 2h)κ       )
    ( −2e,           −(e + 2h),                   h(a − 1) + 1 − w ).                                    {#eq:s14-hn-two}

Write it as M₀ + hM₁, where M₀ is its value at h = 0 and M₁ has rows (a, 0, 0), (0, a + 3, −2κ), (0, −2, a − 1). The
determinant is multilinear in the columns, so P(2 + w; κ, h) = P⁽⁰⁾ + hP⁽¹⁾ + h²P⁽²⁾ + h³P⁽³⁾, where P⁽⁰⁾ = det M₀,
P⁽³⁾ = det M₁, P⁽¹⁾ is the sum of the three determinants of M₀ with one column replaced by the same column of M₁, and
P⁽²⁾ is the sum of the three determinants of M₁ with one column replaced by the same column of M₀. Expanding,

    P⁽⁰⁾ = w(e(5w² + 10w − 15 − 3κ) − 2w² + 2w),
    P⁽¹⁾ = e(6w⁴ + 29w³ + 36w² + 9w − 9κw² − 21κw + 3κ² − 9κ) − 5w⁴ − 7w³ + (5κ + 7)w² − (κ + 3)w,
    P⁽²⁾ = e(w⁵ + 7w⁴ + 17w³ + 17w² + 6w − 2κw³ − 8κw² − 9κw + κ²w + κ² − 3κ)
           − 4w⁵ − 15w⁴ + (8κ − 9)w³ + (16κ + 7)w² − (4κ² − κ + 3)w − κ² + 3κ,
    P⁽³⁾ = −(w² + 2w − κ)(w² + 4w + 3 − κ)(w² − 1 − κ),                                               {#eq:s14-ph-two}

the last because det M₁ = a((a + 3)(a − 1) − 4κ), a = −(w² + 2w − κ) and
a² + 2a − 3 − 4κ = (w² + 4w + 3 − κ)(w² − 1 − κ). (P⁽⁰⁾ = 4wQ_5(2 + w), in accordance with [[eq:s14-q5]].) Collecting
the powers of w, P(2 + w; κ, h) = f₀ + f₁w + … + f₆w⁶ with

    f₀ = hκ(κ − 3)(3e − (1 − e)h + (κ + 1)h²),
    f₁ = −3e(κ + 5) − h(κ + 3 + 21eκ − 9e) − h²((4 − e)κ² − (1 − 9e)κ + 3 − 6e) − 6h³(κ² − 1),
    f₂ = 2 + 10e + h(5κ + 7 − 9eκ + 36e) + h²(16κ + 7 − 8eκ + 17e) − h³(3κ² − 12κ − 11),
    f₃ = −2 + 5e − h(7 − 29e) + h²(8κ − 9 − 2eκ + 17e) + 12h³κ,
    f₄ = −h(5 − 6e) − h²(15 − 7e) + h³(3κ − 10),
    f₅ = −h²(4 − e) − 6h³,
    f₆ = −h³.                                                                                            {#eq:s14-f-two}

**Lemma {#lem:s14-line-two}** (The line Re ι = 2.) Let κ ≥ 3 and 0 < h ≤ 10⁻⁶.

(a) P(2; κ, h) = f₀, which is positive for κ > 3 and zero for κ = 3; and ∂_ιP(2; κ, h) = f₁ < 0.

(b) P(2 + iy; κ, h) ≠ 0 for every real y ≠ 0.

Hence for κ > 3 no root of P(·; κ, h) has real part 2, and for κ = 3 the only one is ι = 2, which is simple.

*Proof.* (a) As h < e, 3e − (1 − e)h > 2e > 0, so f₀ has the sign of κ − 3. In f₁ the brackets are positive:
κ + 3 + 21eκ − 9e > κ, (4 − e)κ² − (1 − 9e)κ + 3 − 6e > 3κ² − κ > 0 and κ² − 1 > 0; so f₁ < −3e(κ + 5) < 0.

(b) The f_j are real, so P(2 + iy; κ, h) = Φ(y²) + iyΨ(y²) with the real polynomials

    Φ(s) := f₀ − f₂s + f₄s² − f₆s³,     Ψ(s) := f₁ − f₃s + f₅s².

Then −Φ(s) − h(κ + s)Ψ(s) = d₀ + d₁s + d₂s² + d₃s³ with d₀ = −f₀ − hκf₁, d₁ = f₂ + hκf₃ − hf₁,
d₂ = −f₄ − hκf₅ + hf₃ and d₃ = f₆ − hf₅, and inserting [[eq:s14-f-two]] and collecting terms,

    d₀ = hκ(24e + h(2κ + 20eκ − 6e) + h²((3 − e)κ² + (1 + 9e)κ + 6 − 6e) + 6h³(κ² − 1)),
    d₁ = 2 + 10e + h((3 − e)κ + 7 + 51e) + h²((10 + 42e)κ + 10 + 8e)
         + h³((9 − 3e)κ² + (2 + 26e)κ + 14 − 6e) + 6h⁴(3κ² − 1),
    d₂ = h(3 − e) + h²(8 + 22e) + h³((9 − 3e)κ + 1 + 17e) + 18h⁴κ,
    d₃ = h³(3 − e) + 6h⁴.                                                                                {#eq:s14-d-two}

For instance, in d₀ the terms of order e give −3e(κ − 3) + 3e(κ + 5) = 24e, those of order h give
(1 − e)(κ − 3) + κ + 3 + 21eκ − 9e = 2κ + 20eκ − 6e, and those of order h² give
−(κ − 3)(κ + 1) + (4 − e)κ² − (1 − 9e)κ + 3 − 6e = (3 − e)κ² + (1 + 9e)κ + 6 − 6e. For κ > 1 and 0 < e < 1/3 every
bracket in [[eq:s14-d-two]] is positive, so d₀, d₂, d₃ > 0 and d₁ > 2. If P(2 + iy; κ, h) = 0 with y ≠ 0, then
Φ(y²) = Ψ(y²) = 0, so −Φ(y²) − h(κ + y²)Ψ(y²) = 0, while d₀ + d₁y² + d₂y⁴ + d₃y⁶ ≥ d₁y² > 0. ∎

#### The line Re ι = −1/(2h) {#sec:s14-every-h-far}

**Lemma {#lem:s14-line-far}** (The line Re ι = −1/(2h).) Let κ ≥ 0 and 0 < h ≤ 10⁻⁶. Then P(·; κ, h) has no root
with real part −1/(2h).

*Proof.* Put K := h²κ and F(σ) := h³P(σ/h; κ, h). Multiply the matrix [[eq:s14-nl]] at v = 1/2 by h, put ι = σ/h and
κ = K/h², then multiply its third column by h and divide its third row by h. The determinant becomes F(σ), and the
matrix becomes, with 𝔪 := K − σ − σ²,

    Y := ( 𝔪 + 2h(σ + 1),   2σ − 4h,                                2K                 )
         ( 2e(σ + h),       𝔪 − σ + 2hσ + 4h + 3h² + e(σ + h),      −(1 + 2h)K         )
         ( −2e,             −(e + 2h),                              𝔪 + 2hσ + 3h − h² ).                  {#eq:s14-y}

A root ι of P(·; κ, h) with real part −1/(2h) gives the root σ = hι = −1/2 + iy of F = det Y, y real. On this line
𝔪 = K + 1/4 + y² is real, |σ|² = 1/4 + y² ≤ 𝔪 and K ≤ 𝔪. Put m := 𝔪^(1/2) ≥ 1/2; then |σ| ≤ m, K ≤ m², 1 ≤ 2m and
m ≤ 2m². Write Y = Y⁰ + Z, where Y⁰ is the upper triangular matrix with rows (𝔪, 2σ, 2K), (0, 𝔪 − σ, −K) and
(0, 0, 𝔪). Then

    det Y⁰ = 𝔪²(𝔪 − σ),     |det Y⁰| ≥ 𝔪² Re(𝔪 − σ) = m⁴(m² + 1/2) > m⁶.

The rows of Z are (2h(σ + 1), −4h, 0), (2e(σ + h), 2hσ + 4h + 3h² + e(σ + h), −2hK) and (−2e, −(e + 2h),
2hσ + 3h − h²). Let α_i and β_i be the sums of the moduli of the entries of row i of Y⁰ and of Z. With the bounds
above,

    α₁ ≤ m² + 2m + 2m² ≤ 7m²,     α₂ ≤ (m² + m) + m² ≤ 4m²,     α₃ = m²,
    β₁ ≤ 2h(m + 1) + 4h ≤ 14hm ≤ 28hm²,
    β₂ ≤ 2e(m + h) + (2hm + 4h + 3h² + e(m + h)) + 2hm² ≤ (6e + 22h + 12eh + 12h²)m² ≤ (6e + 23h)m²,
    β₃ ≤ 2e + (e + 2h) + (2hm + 3h + h²) ≤ (12e + 24h + 4h²)m² ≤ (12e + 25h)m²,

where 1 ≤ 4m² and m ≤ 2m² were used to bring every term to a multiple of m². The determinant is multilinear in the
rows, so det Y − det Y⁰ is the sum, over the seven nonempty sets S ⊂ {1, 2, 3}, of the determinants of the matrices
whose rows i ∈ S are those of Z and whose other rows are those of Y⁰. By Hadamard's inequality, and since the
Euclidean norm of a vector is at most the sum of the moduli of its entries, such a determinant has modulus at most
the product of β_i over i ∈ S and of α_i over i ∉ S. Hence, the expression in the middle being increasing in each α_i
and each β_i,

    |det Y − det Y⁰| ≤ (α₁ + β₁)(α₂ + β₂)(α₃ + β₃) − α₁α₂α₃ ≤ 28m⁶((1 + 4h)(1 + (6e + 23h)/4)(1 + 12e + 25h) − 1).

As e < 10⁻⁵ and h ≤ 10⁻⁶, the numbers 4h, (6e + 23h)/4 and 12e + 25h are below 1.5·10⁻⁴, and the right side is
below 28m⁶((1 + 1.5·10⁻⁴)³ − 1) < 0.02m⁶ < |det Y⁰|. So det Y ≠ 0 on the line Re σ = −1/2. ∎

#### The count {#sec:s14-every-h-count}

**Lemma {#lem:s14-limit-sides}** (The limits as h → 0⁺.) Let l ≥ 1.

(a) The roots ι₊, ι₋ of Q_5 have real part greater than 2.

(b) The three numbers 1/τ_j of [[lem:s14-small-h]] (a) are real and less than −1/2.

*Proof.* (a) By [[eq:s14-q5]] at v = 1/2,

    4Q_5(ι) = e(5(ι − 3)(ι + 1) − 3κ) − 2(ι − 2)(ι − 3) = (5e − 2)ι² + (10 − 10e)ι − 12 − 15e − 3eκ,

a quadratic with leading coefficient 5e − 2 < 0, and 4Q_5(2) = −e(15 + 3κ) < 0, 4Q_5(3) = −3eκ < 0. The midpoint of
its roots is μ := (5 − 5e)/(2 − 5e) = 5/2 + 15e/(4 − 10e), which lies in (5/2, 3) as 0 < e < 1/10. If the roots are
not real, their real part is μ. If they are real, Q_5 ≥ 0 exactly on the closed interval between them, which contains
μ and neither 2 nor 3, so it lies in (2, 3).

(b) The factor τ + 1 of [[eq:s14-ttau]] gives 1/τ = −1. The quadratic factor q(τ) := (5e − 2)τ² + (e − 3)τ − 1 has
q(−2) = 18e − 3 < 0, q(−1) = 4e > 0, q(−1/2) = 3e/4 > 0 and q(0) = −1 < 0; so its roots lie in (−2, −1) and
(−1/2, 0), and their reciprocals in (−1, −1/2) and (−∞, −2). ∎

**Proposition {#prop:s14-scalar-every-h}** (The scalar type l ≥ 1 for every h ∈ (0, 10⁻⁶].) Let l ≥ 1 and
0 < h ≤ 10⁻⁶. Counted with multiplicity, P_l has three roots with real part less than −1/(2h) ≤ −5·10⁵ and three
roots with real part at least 2. For l ≥ 2 the latter three have real part greater than 2. For l = 1 one of them is
ι = 2, a simple root, and the other two have real part greater than 2. In particular no root of P_l has real part in
[−1/(2h), 2), and the only root with real part 2 is ι = 2 at l = 1.

*Proof.* *The roots on the left.* On Ω₁ := [3, ∞) × (0, 10⁻⁶] ∋ (κ, h) consider F(σ) = h³P(σ/h; κ, h) = det Y of
[[eq:s14-y]]. Its coefficients in σ are polynomials in K = h²κ and h, hence continuous on Ω₁; its leading coefficient
is −1, that of P being −h³; and its roots are the numbers hι, ι a root of P(·; κ, h), with the same multiplicities. By
[[lem:s14-line-far]] F has no root with real part −1/2, so by [[lem:s14-half-plane-count]] with H = {Re σ < −1/2} the
number N_− of roots of P(·; κ, h) with real part less than −1/(2h) is the same at every point of Ω₁. At κ = 3, that is
l = 1, [[lem:s14-small-h]] (a) gives, as h → 0⁺, three roots with hι → 1/τ_j, which are less than −1/2 by
[[lem:s14-limit-sides]] (b), and three roots converging to finite limits, for which hι → 0. So N_− = 3 for small h,
hence N_− = 3 on all of Ω₁.

*Degrees l ≥ 2.* On Ω₂ := (3, ∞) × (0, 10⁻⁶] the polynomial P(·; κ, h) has leading coefficient −h³ ≠ 0 and, by
[[lem:s14-line-two]], no root with real part 2. By [[lem:s14-half-plane-count]] with H = {Re ι > 2} the number N_+ of
its roots with real part greater than 2 is the same at every point of Ω₂, and we find it at κ = 8, that is l = 2, for
small h. By [[lem:s14-small-h]] (a), three roots of P_2 converge to the pairwise distinct numbers 2, ι₊, ι₋, and the
real parts of the other three tend to −∞. The roots converging to ι₊ and ι₋ have real part greater than 2 for small h,
by [[lem:s14-limit-sides]] (a). For the third, choose δ > 0 smaller than |ι₊ − 2| and |ι₋ − 2| and such that Q_5 < 0
on [2, 2 + δ], which is possible as Q_5(2) = −(15 + 3κ)e/4 < 0 ([[lem:s14-q5]] (a)). For small h exactly one root ι_h
of P_2 lies in the disc |ι − 2| < δ; its complex conjugate is also a root in that disc, so ι_h is real. Now
P_2(2) = f₀ > 0 by [[lem:s14-line-two]] (a), while P_2(2 + δ/2) tends to 4(δ/2)Q_5(2 + δ/2) < 0 as h → 0⁺, by
[[eq:s14-q5]]. So for small h, P_2 has a root in (2, 2 + δ/2), which is ι_h, and ι_h > 2. Hence N_+ = 3, at every point
of Ω₂. As P(·; κ, h) has six roots and N_− = 3, no root lies in the strip −1/(2h) ≤ Re ι ≤ 2 when (κ, h) ∈ Ω₂, in
particular when κ = l(l + 2) with l ≥ 2.

*Degree l = 1.* P_1(2) = 0 for every h, so P_1 = (ι − 2)P̃_1 with P̃_1 a polynomial of degree 5 in ι, of leading
coefficient −h³, whose coefficients are polynomials in h. By [[lem:s14-line-two]], P̃_1(2 + iy) = P_1(2 + iy)/(iy) ≠ 0
for real y ≠ 0, and P̃_1(2) = ∂_ιP_1(2) = f₁ ≠ 0; so P̃_1 has no root with real part 2, and by
[[lem:s14-half-plane-count]] with Ω = {3} × (0, 10⁻⁶] the number of its roots with real part greater than 2 does not
depend on h. As h → 0⁺, three roots of P_1 converge to the pairwise distinct numbers 2, ι₊, ι₋ and the real parts of
the other three tend to −∞ ([[lem:s14-small-h]] (a)). For small h exactly one root of P_1 lies in a small disc about
2, and ι = 2 is a root there; so the five roots of P̃_1 are the other five. Two of them converge to ι₊ and ι₋ and have
real part greater than 2 for small h ([[lem:s14-limit-sides]] (a)), and three have real parts tending to −∞. So P̃_1
has exactly two roots with real part greater than 2, for every h ∈ (0, 10⁻⁶]. Its roots with real part less than
−1/(2h) are those of P_1, three by the first part. So P̃_1 has no root with real part in [−1/(2h), 2], and the roots
of P_1 are ι = 2, simple as P̃_1(2) ≠ 0, two with real part greater than 2, and three with real part less than
−1/(2h). ∎

Since −1/(2h) ≤ −5·10⁵ < −100 and 2 > 19/10, [[prop:s14-scalar-every-h]] gives the part of [[prop:np-10-54]] (i)–(ii)
that concerns the scalar types l ≥ 1. It holds at every h ∈ (0, 10⁻⁶] and every l ≥ 1, with no exceptional value of h;
as h_* ≤ 10⁻⁶, this includes every h ∈ 𝖧 of [[eq:iv4-0-1]].

### The inputs in dimension 4 + 1 {#sec:iv4-1}

**Lemma {#lem:iv4-1-1}** (The fibre algebra; [Hin26a, Lemmas 3.3–3.8] in dimension 4 + 1.) On each fibre, with G(c) < 0,
B := g⁻¹ − (1 + e)G(c)⁻¹c♯ ⊗ c♯ is positive definite for e > 0, ℓ_(g,c,e)(ζ) of [[eq:s14-ell]] is B-self-adjoint for
every ζ, and the characteristic polynomial of ½ℓ(ζ) is (ν − G(c)ζ_0)³ times the quadratic
ν² − (3 − e)G(c)ζ_0ν + 2(1 − e)G(c)²ζ_0² + eG(c)G(ζ) of [Hin26a, (3.8)], where ζ = ζ_0 c + ζ′ with ζ′ ⊥ c. The
consequences of these facts that the chapter uses from [Hin26a, Lemmas 3.3–3.8 and Corollary 3.6] are stated and
proved in [[lem:iv4-1-causal]].

*Proof.* The three statements are [[prop:np-10-13]] (i) at D = 5, with ⟨c, ζ⟩ = G(c)ζ_0. ∎

**Lemma {#lem:iv4-1-causal}** (Positivity on causal covectors; the statements of [Hin26a, Lemma 3.5, Corollary 3.6 and
Lemma 3.7] used in this chapter.) Let g be a Lorentzian inner product on a real vector space V of dimension D, with
⟨·, ·⟩ and G taken with g⁻¹, let c ∈ V* be timelike, with the time orientation in which c is past timelike, let
e ∈ (0, 1), and let ℓ := ℓ_(g,c,e) and B be as in [[eq:s14-ell]]. Fix a norm |·| on V*.

(a) For every future causal ζ ≠ 0, ⟨c, ζ⟩ > 0 and B(ℓ(ζ)ω, ω) ≥ 2(1 − e)⟨c, ζ⟩B(ω, ω) for every ω ∈ V*. So ℓ(ζ) is
B-positive definite, and ℓ(−ζ) = −ℓ(ζ) is B-negative definite.

(b) For every ζ ≠ 0, G(ζ) − iℓ(ζ) is invertible on V* ⊗ ℂ.

(c) There is C > 0 such that Cℓ(ζ)² + G(ζ) is B-positive definite for every ζ ≠ 0.

(d) Let K be a compact set of such pairs (g, c) on V, e being fixed. There are c₁, c₂, C, ε > 0 such that for every
(g, c) ∈ K, every ω ∈ V* and every ζ ∈ V*: B(ℓ(ζ)ω, ω) ≥ c₁|ζ|B(ω, ω) if |ζ − ζ′| ≤ ε|ζ| for some future causal ζ′,
in particular if ζ is future causal; and B((Cℓ(ζ)² + G(ζ))ω, ω) ≥ c₂|ζ|²B(ω, ω).

*Proof.* (a) Since c is timelike, c^⊥ is spacelike, so a causal ζ ≠ 0 is not orthogonal to c, and ⟨c, ·⟩ has no zero
on the connected cone of future causal covectors. That cone contains −c, and ⟨c, −c⟩ = −G(c) > 0; so ⟨c, ζ⟩ > 0 there.
As ℓ(ζ) is B-self-adjoint ([[prop:np-10-13]] (i)), its eigenvalues are real, and B(ℓ(ζ)ω, ω) is at least the least of
them times B(ω, ω). By [[prop:np-10-13]] (i), with a := ⟨c, ζ⟩, the eigenvalues of ½ℓ(ζ) are a, D − 2 times, and the
two roots of ν² − (3 − e)aν + 2(1 − e)a² + eG(c)G(ζ). Its discriminant is (1 + e)²a² − 4eG(c)G(ζ), at most
(1 + e)²a² since G(c) < 0 and G(ζ) ≤ 0; so both roots are at least ½((3 − e)a − (1 + e)a) = (1 − e)a. Hence every
eigenvalue of ℓ(ζ) is at least 2(1 − e)a > 0.

(b) Let (G(ζ) − iℓ(ζ))ω = 0, and extend B sesquilinearly. B(ℓ(ζ)ω, ω) is real, ℓ(ζ) being real and B-self-adjoint, so
the real and imaginary parts of B((G(ζ) − iℓ(ζ))ω, ω) = 0 give G(ζ)B(ω, ω) = 0 and B(ℓ(ζ)ω, ω) = 0. If ω ≠ 0, then
G(ζ) = 0, so ζ or −ζ is future causal, and (a), applied to the real and imaginary parts of ω, gives B(ℓ(ζ)ω, ω) ≠ 0.
So ω = 0.

(c) is (d) with K := {(g, c)}.

(d) The set F of the (g, c, ζ) with (g, c) ∈ K, |ζ| = 1 and ζ future causal for (g, c), that is G(ζ) ≤ 0 and
⟨c, ζ⟩ ≥ 0, is compact, and ⟨c, ζ⟩ > 0 on it by (a); let 2c₀ be its minimum. The least eigenvalue of ℓ(ζ), a
continuous function of (g, c, ζ), is at least 4(1 − e)c₀ on F by (a); so it is at least c₁ := 2(1 − e)c₀ on a
neighbourhood of F, which for ε small contains, by compactness, every (g, c, ζ) with |ζ| = 1 and |ζ − ζ′| ≤ 2ε for
some (g, c, ζ′) ∈ F. Homogeneity gives the first bound. For the second, let Γ_δ be the set of the (g, c, ζ) with
(g, c) ∈ K, |ζ| = 1 and G(ζ) ≤ δ. On Γ_0, ζ or −ζ is future causal, so B(ℓ(ζ)²ω, ω) = B(ℓ(ζ)ω, ℓ(ζ)ω) ≥ c₁²B(ω, ω), by
the first bound and the Cauchy–Schwarz inequality; by continuity and compactness this holds with ½c₁² in place of
c₁² on Γ_δ, for some δ > 0. Let M be the maximum of |G(ζ)| over K × {|ζ| = 1}, and C := 2(M + 1)c₁⁻². Then
Cℓ(ζ)² + G(ζ) ≥ (M + 1) − M = 1 on Γ_δ, and ≥ G(ζ) > δ off Γ_δ, ℓ(ζ)² being B-positive semidefinite. Homogeneity of
degree 2 gives c₂ := min(1, δ). ∎

**Lemma {#lem:iv4-1-2}** (The structure at infinity; [Hin26a, (6.4)] in dimension 4 + 1.) Near ∂X, in t_*, ρ and
spherical coordinates,

    □^C_b = −2∂_(t_*) ρ(ρ∂_ρ − 3/2 − S̄^C − ρS̃) + P^C_b + Q∂_(t_*) + R∂²_(t_*),                            {#eq:iv4-1-1}

with S̃ smooth, Q ∈ ρ³Diff¹_b, R ∈ ρ²C^∞, P^C_b ∈ ρ²Diff²_b, and S̄^C constant with spectrum
γ_C{2(1 − v_C), (1 − e_C)(1 − v_C), 1 − v_C (three times)}, all positive.

*Proof.* On 4 + 1 Minkowski space with c = |x|⁻¹(dt − v dr) this is [[prop:np-10-21]] (i), with S̃, Q and R zero: the
∂_(t_*)∂_r-coefficient is 2 Id, there is no ∂_(t_*) times a tangential derivative, and S̄^C is r/2 times the
∂_(t_*)-coefficient less (n − 1)/2 = 3/2. (A change of frame by a bundle map depending on x̂ alone, such as
dt = dt_* + x̂ · dx, commutes with ∂_(t_*) and ρ∂_ρ and preserves each class below.) For g_b and c_C we count as in the
proof of [[lem:iii-d2-2-1]]. Near ∂X, in the coordinates (t_*, x), the components of g_b, g_b⁻¹, ḡ and ḡ⁻¹ are smooth
functions on X̄, free of t_*, with g_b − ḡ and g_b⁻¹ − ḡ⁻¹ in ρ²C^∞ ([[eq:iii-d2-2-3]]); c_C and the model's 1-form c̄
lie in ρC^∞ and differ by ρ³C^∞ ([[sec:iii-e-1]]); and ∂_(x^i) ∈ ρDiff¹_b on functions on X̄. So the Christoffel
symbols lie in ρC^∞, and those of g_b and ḡ differ by ρ³C^∞. For g ∈ {g_b, ḡ}, each with its 1-form, write the
factors of □^C = 2δ_gG_g(δ*_g + E^C_g) as polynomials in ∂_(t_*) with stationary coefficients:

    δ*_g + E^C_g = A∂_(t_*) + Δ_g,     δ_g = D_g∂_(t_*) + δ^(0)_g.

Here A, the ∂_(t_*)-part of ω ↦ ½(∂_μω_ν + ∂_νω_μ), is a constant bundle map, the same for both metrics;
Δ_g ∈ ρDiff¹_b, the Christoffel symbols and the coefficients of E^C_g lying in ρC^∞; D_gk := −k(·, g⁻¹(dt_*, ·)) has
coefficients in C^∞; and δ^(0)_g ∈ ρDiff¹_b. Each of Δ_(g_b) − Δ_ḡ, G_(g_b) − G_ḡ, D_(g_b) − D_ḡ and
δ^(0)_(g_b) − δ^(0)_ḡ is a sum of terms each with one factor a difference of components of the metrics, of their
inverses, of the Christoffel symbols or of the 1-forms; so these differences lie in ρ³Diff⁰_b, ρ²C^∞, ρ²C^∞ and
ρ³Diff¹_b. As the coefficients are stationary,

    □^C = 2D_gG_gA∂²_(t_*) + 2(D_gG_gΔ_g + δ^(0)_gG_gA)∂_(t_*) + 2δ^(0)_gG_gΔ_g.

For ḡ the first coefficient vanishes and the second is −2ρ(ρ∂_ρ − 3/2 − S̄^C) ([[prop:np-10-21]] (i)). Expand the
differences into terms with one difference each, and use ρDiff¹_b ∘ ρ²C^∞ ⊂ ρ³Diff¹_b. Then R := 2D_(g_b)G_(g_b)A
lies in ρ²C^∞; the ∂_(t_*)-coefficient of □^C_b is the model's plus some Q ∈ ρ³Diff¹_b; and
P^C_b = 2δ^(0)_(g_b)G_(g_b)Δ_(g_b) lies in ρ²Diff²_b, with P^C_b − P̄^C ∈ ρ⁴Diff²_b. This is [[eq:iv4-1-1]] with S̃ := 0:
the mass enters g_b at ρ², so the part ρ²S̃ of order 0 that [[eq:iv4-1-1]] allows does not arise. ∎

**Lemma {#lem:iv4-1-3}** (The indicial roots; [Hin26a, Theorem 4.9] in dimension 4 + 1.) Let h ∈ (0, 10⁻⁶] and b near
b₀.

(a) Every indicial root ι of P^C_b satisfies Re ι ∉ [−100, 19/10]; the only roots with real part in [−100, 2] are ι = 2
at scalar type 0 and at scalar type 1, each simple. At each type and degree as many roots have real part ≥ 2 as
< −100: three each at scalar type l ≥ 1, two each at scalar type 0, one each at vector type l ≥ 1. Each strip
{|Re ι| ≤ R} contains only finitely many roots, so the real parts accumulate only at ±∞.

(b) There is a countable set 𝖹₁ ⊂ (0, 10⁻⁶] such that for h ∉ 𝖹₁ the roots are simple and the remaining clauses of
[[thm:iii-e-1-1]] (3) hold.

*Proof.* The indicial family of P^C_b at ∂X is that of the Minkowski model with c = |x|⁻¹(dt − v_C d|x|), independent of
b: g_b − ḡ ∈ ρ²C^∞ and the deviation of c_C are of lower order ([[lem:iv4-1-2]]; [Hin26a, p. 29]: the indicial roots are
determined by the leading part as ρ → 0). In the decomposition into scalar and vector type harmonics of 𝕊³, the
indicial roots of type and degree l are, in the variable ι of [[prop:np-10-12]] (ii) (the 1-form decaying like
ρ^ι = r^(−ι)), the roots of p_(v) and of P_l. (a) is [[prop:np-10-54]].

(b) Fix l. Each condition is the non-vanishing at h of a polynomial in h, and we show that none of these polynomials
vanishes identically; then each fails for at most finitely many h, and 𝖹₁, the union over l and over the finitely
many conditions at each l, is countable. *Simplicity.* By [[lem:s14-small-h]], for all sufficiently small h > 0 the roots
of P_l, of C and of p_(v) are simple; so their discriminants, polynomials in h, do not vanish identically; and
ι = 2 is not a root of C (proof of [[prop:np-10-54]]). *Excluded points.* For a fixed real x, P_l(x) is a polynomial
in h with value 8v(x − 2)Q_5(x) at h = 0, and p_(v)(x) has value −2v(x − 3) at h = 0. For the scalar type the points
are x ∈ {1 − l, 3 − l, l + 3, l + 5} ∖ {2}: each satisfies x ≤ 1 or x ≥ 4 when l ≥ 1, so Q_5(x) < 0
([[lem:s14-q5]] (a)); at l = 0 the points are 1, 3, 5, and C(x)|_(h=0) = (5e − 2)x + 5e + 4 is 10e + 2, 20e − 2 and
30e − 6 there. For the vector type with l ≥ 2 the points 1 − l, 2 − l, l + 3, l + 4 differ from 3. *Real parts.* Let
k ∈ [3, 51] be an integer, and write P_l(k + iy) = A_k(y²) + iyB_k(y²) with A_k, B_k real polynomials. A non-real root
k + iy, y ≠ 0, makes y² a common root of A_k and B_k, so the resultant Res(A_k, B_k), a polynomial in h, vanishes.
Conversely, as P_l is real, a common root t of A_k and B_k gives P_l(k ± it^(1/2)) = 0: a conjugate pair with real
part k if t > 0, two real roots k ± |t|^(1/2), of sum 2k, if t < 0, and a double root at k if t = 0. So Res(A_k, B_k)
vanishes exactly when P_l has two roots, counted with multiplicity, of sum 2k. By [[lem:s14-small-h]], as h → 0⁺
the roots of P_l converge to 2, ι₊, ι₋ or have real parts tending to −∞. The limit sums are 2 + ι_± and
ι₊ + ι₋ = 5 + 1/13653 ([[lem:s14-q5]] (b)); 2 + ι_± = 2k would make 2k − 2 ≥ 4 a real root of Q_5, which
[[lem:s14-q5]] (a) excludes. So for small h > 0 no two roots have sum 2k and no root is double, and Res(A_k, B_k) does
not vanish identically. The same argument applies to C, whose finite limit root is (4 + 5e)/(2 − 5e), and p_(v) has real
roots only. ∎

**Lemma {#lem:iv4-1-4}** (The 1-form; [Hin26a, Proposition 5.1] in dimension 4 + 1.) With the weights

    α_K := 1,     α_sf := −C_0 − 5/2,                                                                       {#eq:iv4-2-1}

w := ρ_sf^(α_sf+1)ρ_K^(α_K) and w′ := ρ_sf^(α_sf+1), c_C satisfies the conditions (1)–(6) of [Hin26a, Proposition 5.1]
on Tangherlini space g_(b₀), for some δ_r > 0 and with δ_sf = 1/100. In dimension 4 + 1, with r_c the radius of the
saddle (the r_0 of [Hin26a]) and r_♯ the inner radius ([[sec:iv5-0]]), these conditions are: (1) r c is past timelike on
{r ≥ r_♯}; (2) c = ½r_c⁻²(r_c dt − v(r − r_c) dr) on [r_c/2, 2r_c] and c = r⁻¹(dt − v dr) for r ≥ 3r_c; (3) the S of
[[eq:s14-s]] is positive definite on |r − r_c| ≤ (6/5)r_ce^(1/2)/v; (4) r²(−ℓ(dw/w) + S) is positive definite near the
corner ∂K⁺, on {ρ_sf ≤ 2δ_r, ρ_K ≤ 2δ_r}; (5) r²(−ℓ(dw′/w′) + S) is positive definite near the sink, on
{ρ_sf ≤ 2δ_r, |(r/t)/v − 1| ≤ 2δ_sf}; (6) −ℓ(−dr) is positive definite on [r_♯, r_c − r_ce^(1/2)/v] and −ℓ(dr) on
[r_c + r_ce^(1/2)/v, ∞), and on 𝗌𝖿 the two conditions of [Hin26a, (5.8)] hold: −r²ℓ(d(r/t)) is positive definite for
r/t ∈ [δ_r, v(1 − δ_sf)], and −r²ℓ(−d(r/t)) for r/t ∈ [v(1 + δ_sf), 10]. The conditions also hold on g_b for b near
b₀, with smaller δ_r and the same δ_sf, conditions (5)–(6) on 𝗌𝖿 not depending on b. The same holds with C_0 − 1 for
C_0 in [[eq:iv4-2-1]], that is at α_sf = −C_0 − 3/2, for every C_0 ≥ 0: the conditions at 𝗌𝖿 are then
b_sf = −C_0 − 1/2 < b* and b_K = 1 > b_sf − b*.

*Proof.* (1)–(3) and (6) off 𝗌𝖿 are [[prop:np-10-14]] (i)–(iii). (4)–(6) at 𝗌𝖿: the symbol T = r²(−ℓ(dw/w) + S)
depends only on ρ_K and the weights there; it is positive definite at ∂K⁺ iff b_K > b_sf − b* and at the sink iff
b_sf < b*, with b_K = α_K, b_sf = α_sf + 1 and b* = 0.99340731… ([[prop:np-10-14]] (iv)). At [[eq:iv4-2-1]],
b_sf = −C_0 − 3/2 and b_K = 1, and the characteristic polynomials at ∂K⁺ and at R_v have positive roots for every
C_0 ≥ 0; at C_0 = 100, T is positive definite on all of 𝗌𝖿 with ρ_K ≤ 10 ([[prop:np-10-22]] (iv)). So (4) holds near
∂K⁺ by continuity, and (5) holds on |(r/t)/v − 1| ≤ 2δ_sf because T at the sink, b_K = 0, does not depend on ρ_K.
Off 𝗌𝖿, for ρ_sf ≤ 2δ_r, (4)–(5) hold by continuity, as Tangherlini space differs from its Minkowski model by ρ_sf C^∞
terms ([[prop:np-10-14]] (a); [Hin26a, p. 39]). [Hin26a, (5.8)] holds outside an interval about v of half-width below
1/200, which gives the conditions (6) on 𝗌𝖿 with δ_sf = 1/100 ([[prop:np-10-14]] (v)). For g_b: each condition is a
strict positivity of a continuous function of the metric on a compact set, or holds at 𝗌𝖿, where g_b and g_(b₀) have
the same 3sc model; so it persists for b near b₀. ∎

**Lemma {#lem:iv4-1-5}** (The horizon threshold.) For b near b₀ and every h ∈ (0, 10⁻⁶], the threshold ϑ_ℋ of
[[sec:i-a-1]] of the spectral family of □^C_b satisfies ½ + ϑ_ℋ < −C_0.

*Proof.* ϑ_ℋ is the maximum over the compact ∂ℛ_± of the top eigenvalue of β_0⁻¹p_(1,±)(0), self-adjoint for the fibre
inner product B of [[lem:iv4-1-1]]. By its definition p_(1,±)(0) = A_± − h⁻¹ℓ(±ρ_∞·), where A_± comes from 2δGδ* and is
free of h, and the h⁻¹-part is h⁻¹ρ_∞ times the damping symbol of L at the conormal covectors of the horizon. These are
future null, and c_C is past timelike there ([[prop:np-10-14]] (i) at b₀, and by continuity for b near b₀), so
[[lem:iv4-1-causal]] (a) makes ℓ of them B-positive definite, so that −h⁻¹ℓ is negative definite, the sign that
damps.
So, by Weyl's inequality, ϑ_ℋ ≤ ϑ_0(b) − c(b)h⁻¹ with ϑ_0 and c > 0 continuous in b. At b₀,
ϑ_0 = 102401/640 and c = 102399/20480000, and ϑ_ℋ itself is −4995.83… at h = 10⁻⁶ ([[prop:np-10-79]]); the bound
ϑ_0 − ch⁻¹ is −4839.95… at h = 10⁻⁶. So ½ + ϑ_0(b) − c(b)h⁻¹ < −100 for b near b₀ and h ≤ 10⁻⁶, the margin at b₀ being
more than 4700. ∎

**Lemma {#lem:iv4-1-6}** (The hypotheses of the spectral theory.) For b near b₀ and h ∈ (0, 10⁻⁶], the spectral family
of □^C_b satisfies (H1)–(H4) of [[sec:i-a-1]] ([[eq:i-a-1-2]]–[[eq:i-a-1-3]]), and the gap condition (G) of
[[ch:s03]] for every α with α + 2 ∈ [−C_0, 2), with the gap I = (β_−, 2), β_− < −C_0.

*Proof.* (H1): the principal symbol of □^C_b is that of □_(g_b) ⊗ Id, as E^C has order 0 and 2δGδ* has the scalar
principal symbol g⁻¹(ζ, ζ); so σ₂(P̂(0)) = G_0 Id, σ₁(T) = τ₁ Id with τ₁ = −H_G t_*, and P₂ = g_00 Id. (H2):
[[lem:iv4-1-2]], with S = S̄^C + ρS̃ and P^(0) := ρ⁻²P^C_b, whose principal part at ∂X is that of the Euclidean
Laplacian in b-form, the first-order terms of E^C (coefficients in ρC^∞) lying in Diff¹_b. (H3)–(H4) concern only G_0
and τ₁, that is g_b and t_*: apart from the threshold in (H3), which is [[lem:iv4-1-5]], they are part of the dynamical
hypotheses (Dyn) on the metric alone, verified for g_b, b near b₀, in [[ch:s12]] ([[ch:s13]]), and they hold for every
operator with principal part □_(g_b) ⊗ Id. (G): by [[lem:iv4-1-3]] (a) and [[lem:i-c-2-2]], the indicial roots
relevant to the weight α + 2 (Euclidean density) are the ι with Re ι = α + 2; none has real part in
[−100, 19/10] ∪ (19/10, 2), so (β_−, 2) with β_− := max{Re ι : Re ι < −100} < −100 ≤ −C_0 is a gap. The maximum
exists: some root ι₀ has Re ι₀ < −100, and the strip {Re ι₀ ≤ Re ι ≤ −100} contains only finitely many roots
([[lem:iv4-1-3]] (a)). ∎

### Solvability on weighted 3b-spaces {#sec:iv5}

This section proves [Hin26a, Theorem 5.2] in dimension 4 + 1 ([[thm:iv5-7-3]]) for the constraint propagation operator
on the Myers–Perry metrics, b near b₀, with the 1-form c_C, the constants [[eq:iv4-0-1]] and the weights
[[eq:iv4-2-1]]. The theorem solves the forward problem and the initial value problem on weighted semiclassical
3b-Sobolev spaces, with the a priori estimate [[eq:iv5-5-79]] and the adjoint estimate [[eq:iv5-5-81]], for all h < h_0
with h_0 uniform in b. [Hin26a, Section 5.2] is a chain of semiclassical estimates, each an identity of symbols or a
pairing in which the dimension does not appear. Each is written out below in dimension 4 + 1, and every place where the
dimension enters is named: the compactification and the 3sc structure of the metric ([[sec:iv5-0]]), the volume
density ([[lem:iv5-0-2]] (b)), the causal facts ([[lem:iv5-0-3]]), the fibre algebra ([[lem:iv5-0-4]]) and the 1-form
([[lem:iv5-0-5]]). Three families of estimates that [Hin26a] uses without stating them, the propagation through the
interior of Ω in both directions, along 𝗌𝖿 between its critical sets and along K⁺ outward from the saddle, are stated
and proved in [[prop:iv5-5-2]] and [[prop:iv5-5-3]]. We follow [Hin26a, pp. 12–17, 25–28, 37–39, 41–66].

#### The setting {#sec:iv5-0}

Throughout n = 4. The mass m₀, R₁ = m₀^(1/2), the parameter set ℬ and b₀ = (m₀, 0) are those of [[sec:iii-b-3-1]].
Let r_♯ := r_♭ ∈ (0, ½R₁] be the inner radius of [[ch:s11]] (the inner radius of [Hin26a, Section 5]), r̂ := ¾R₁,
and r_c := 100R₁ the radius of the saddle point of c_C (the radius r_0 of [Hin26a]; the r_0 = 100 of
[[prop:np-10-14]] at m = 1, rescaled). Let v := v_C = 1/2 and e := e_C = 1/102400. Every radius used below near the
inner boundary is placed relative to r_♯ and r̂: ε_X ≤ T_0r_♯/2 and ε_r := (r̂ − r_♯)/10 in [[prop:iv5-5-3]],
r_1 := r_♯ + (2/10)(r̂ − r_♯) and r_2 := r_♯ + (2.75/10)(r̂ − r_♯) in [[prop:iv5-7-1]], the transitions of the
cut-offs χ_(r,j) in [r_♯, r̂], and t_1 < ¼T_0r_♯ in [[prop:iv5-7-2]]. Nothing below is uniform in r_♯.

*Coordinates.* We work in the Kerr–Schild coordinates (t, x) of [[sec:iii-b-3-1]], with r := |x|. For b ∈ ℬ,
g := g^KS_b = η + H_b k_b ⊗ k_b is defined, smooth and Lorentzian with H_b > 0 on ℝ_t × {r ≥ ½r_♯}, smoothly in b,
and the condition of [[lem:iii-b-3-3]] (c) holds there ([[lem:s11-ks-domain]]). The metric g_b of [[sec:iii-b-3-1]]
is Φ_m*g with Φ_m(t, x) = (t − T_m(|x|), x), and [[rem:iv5-7-4]] transfers the results to it. The 1-form c := c_C of
[[sec:iv4-0]] is given by its formula on {r ≥ ½r_♯}; below the smoothing, which lies in [¼r_c, ½r_c], it is a
positive multiple of dt + (v/2) dr. It is past timelike for g_(b₀) at every r > 0 ([[prop:np-10-14]] (i), (b)), so for
g_b, b near b₀, on the compact set {½r_♯ ≤ r ≤ 3r_c}, by continuity; and for r ≥ 3r_c it is r⁻¹(dt − v dr), past
timelike for every g_b by [[lem:iv5-0-3]] (a).

**Definition {#def:iv5-0-1}** (The compactification and the spaces; [Hin26a, Definitions 2.1, 2.2, 2.5, (2.2)–(2.3),
(2.10), (2.11), (5.19)] in dimension 4 + 1.) Let M₀ := [ℝ̄^(1+4); k₊, k₋], where k_± are the poles of the radial
compactification at future and past timelike infinity. Let M^♭ := cl_(M₀)(M₀° ∖ cl({r < r_♯} ∪ {t < −½r})). Its faces
are the *Kerr face* K⁺ := M^♭ ∩ β⁻¹(k₊), the *side face* 𝗌𝖿 := ∂M^♭ ∩ (∂M₀ ∖ (K⁺)°), X_0 := cl{t = 0} and
Σ^♯ := cl{r = r_♯}; and the domain is Ω := cl{t ≥ 0} = {τ ≥ 0}, τ := t/r. (M^♭ is not the compactification M̃ of
[[ch:s04]].) M^♭ is covered by three charts:

- [r_♯, ∞)_r × [−½, ∞)_τ × 𝕊³;

- [0, r_♯⁻¹]_(ρ_sf) × [0, 2]_(ρ_K) × 𝕊³, with (t, r) = (ρ_sf⁻¹ρ_K⁻¹, ρ_sf⁻¹);

- [0, r_♯⁻¹]_(ρ_sf) × [−½, ∞)_τ × 𝕊³.

On {t > ½r} we use ρ_K = r/t and ρ_sf = 1/r. Further:

- 𝒯 and 𝒯* are the pullbacks of the scattering bundles of ℝ̄^(1+4) (the 3sc-bundles; dt, dx¹, …, dx⁴ is a frame of
𝒯*);

- 𝒱_3b(M^♭) is the C^∞(M^♭)-span of r∂_(z^μ), μ = 0, …, 4; with it come ³ᵇTM^♭, ³ᵇT*M^♭ (frame dz^μ/r) and
Diff^k_3b with weights; ∂_(z^μ) = r⁻¹ · r∂_(z^μ) ∈ ρ_sf 𝒱_3b(M^♭), as r⁻¹ ∈ ρ_sf C^∞(M^♭) (r⁻¹ = ρ_sf near 𝗌𝖿,
and r ≥ r_♯);

- the projection (t, x) ↦ x extends to a smooth map π : M^♭ → X̄_♯ := X̄ ∩ {r ≥ r_♯}, so π*C^∞(X̄_♯) ⊂ C^∞(M^♭).

The semiclassical 3b-pseudodifferential calculus Ψ_(3b,ħ)(M^♭), with its principal symbols, operator wave front sets
WF′_(3b,ħ), elliptic sets Ell_(3b,ħ) and Sobolev spaces H^s_(3b,h), is that of [[sec:iv5-calc]]. It is built from the
cells of [[def:iv5-calc-cells]], with four spatial coordinates, and the facts used about it are those of
[[prop:np-10-65-a]], [[lem:iv5-calc-garding]] and [[lem:iv5-calc-q0]]. Write

    H^(s,(β_sf,β_K))_(3b,h) := ρ_sf^(β_sf) ρ_K^(β_K) H^s_(3b,h)(M^♭; 𝒯*)

([Hin26a, (5.19)]), normed with the density |dg| and the fibre inner product B of [[lem:iv5-0-4]]. On Ω there are three
kinds of space, defined in [[lem:iv5-calc-dual]]: H^(s,(·))_(3b,h)(Ω)^(•,−), restrictions to {r > r_♯} of elements with
support in {t ≥ 0}, so supported at X_0 and extendible at Σ^♯; (·)^(−,•), extendible at X_0 and supported at Σ^♯; and
H̄, extendible at both. In all of these constructions the dimension enters only as the number of coordinates.

**Lemma {#lem:iv5-0-2}** (The metric and the 1-form as 3sc-objects; [Hin26a, Lemmas 2.3–2.4, (2.12)–(2.14), Lemma 5.3]
in dimension 4 + 1.) For b ∈ ℬ:

(a) g ∈ C^∞(M^♭; S²𝒯*) is a stationary nondegenerate Lorentzian 3sc-metric, g⁻¹ ∈ C^∞(M^♭; S²𝒯), and g − η,
g⁻¹ − η⁻¹ lie in ρ_sf²C^∞, smoothly in b;

(b) |dg| = |dt dx| = r³|dt dr d𝑔̸| = r⁴|dτ dr d𝑔̸|, d𝑔̸ the round density of 𝕊³;

(c) the Christoffel symbols of g in (t, x) lie in ρ_sf C^∞(M^♭); so ∇ ∈ ρ_sf Diff¹_3b(M^♭; 𝒯^(p,q), 𝒯* ⊗ 𝒯^(p,q)),
□_g ∈ ρ_sf² Diff²_3b and δ*_g, δ_g ∈ ρ_sf Diff¹_3b;

(d) c ∈ ρ_sf C^∞(M^♭; 𝒯*) is stationary, h²□_g ∈ h²ρ_sf²Diff²_3b(M^♭; 𝒯*) and L_h := L_(g,c,e,h) ∈
hρ_sf²Diff¹_3b(M^♭; 𝒯*); the semiclassical 3b-principal symbol of P_h := h²□^C_b = h²□_g − iL_h is p = G − iℓ, with
G(ζ) = g⁻¹(ζ, ζ) and ℓ := ℓ_(g,c,e) of [[eq:s14-ell]].

*Proof.* (a) In (t, x) the components of g do not depend on t, are smooth on {r ≥ ½r_♯}, and near infinity lie in
C^∞(X̄) with g − η ∈ |x|⁻²C^∞(X̄): this is [[prop:iii-b-3-6]] and its proof, which establishes the expansion for g^KS_b
first. The same holds for the inverse, η⁻¹ − H_b k_b♯ ⊗ k_b♯ ([[lem:iii-b-3-3]] (d)). Through π these components are
smooth functions on M^♭, and |x|⁻² = ρ_sf². In the frame dz^μ this gives g ∈ C^∞(M^♭; S²𝒯*), and likewise for g⁻¹.
Since k_b is η-null ([[lem:iii-b-3-3]] (a)), det(η + H_b k_b ⊗ k_b) = det η (1 + H_b η⁻¹(k_b, k_b)) = −1 identically,
so g is nondegenerate on all of M^♭. It is Lorentzian on M^♭: at finite points it is the metric itself, and at 𝗌𝖿 its
components are those of η. Smoothness in b is that of [[sec:iii-b-3-1]].

(b) det g = −1 in (t, x) gives |dg| = |dt dx|. Polar coordinates on ℝ⁴ give |dx| = r³|dr d𝑔̸|, and dt = r dτ + τ dr
gives |dt dr| = r|dτ dr|.

(c) Γ^κ_(μν) = ½g^(κλ)(∂_μg_(νλ) + ∂_νg_(μλ) − ∂_λg_(μν)), with g^(κλ) ∈ C^∞(M^♭) and ∂_μg_(νλ) ∈ ρ_sf C^∞(M^♭)
because ∂_(z^μ) ∈ ρ_sf 𝒱_3b. In the frame dz^μ, ∇_(∂_(z^μ)) acts on components as ∂_(z^μ) + Γ_μ, with one
Christoffel symbol for each index; so ∇ = Σ_μ dz^μ ⊗ (∂_(z^μ) + Γ_μ) lies in ρ_sf Diff¹_3b. For V = r∂_(z^μ), the
function ρ_sf⁻¹V(ρ_sf) is smooth on M^♭: near 𝗌𝖿 it is −∂_(z^μ)r, which is 0 or −x^i/r, and elsewhere ρ_sf is smooth
and positive. Hence ρ_sf^a Diff^k_3b ∘ ρ_sf^b Diff^l_3b ⊂ ρ_sf^(a+b) Diff^(k+l)_3b, and, with g^(μν) ∈ C^∞(M^♭) by
(a), □_g = −g^(μν)(∇∇)_(μν) ∈ ρ_sf² Diff²_3b, while δ*_g, the symmetrisation of ∇, and δ_g, the contraction of ∇ with
−g⁻¹, lie in ρ_sf Diff¹_3b. (On Tangherlini space, Γ ∈ mρ³C^∞ by [[prop:np-10-22]] (i).)

(d) c is stationary and smooth on {r ≥ ½r_♯}, and equals r⁻¹(dt − v dr) for r ≥ 3r_c ([[prop:np-10-14]] (b)). Its
components (r⁻¹, −vr⁻¹x̂) lie in |x|⁻¹C^∞(X̄), so c ∈ ρ_sf C^∞(M^♭; 𝒯*). By [[sec:iv4-0]], the trace weight 2/3 gives
hG_gE^C the form of [Hin26a], so L_h = 4ih δ_g(c ⊗_s ·) + 2ihe dι_(c♯) is [Hin26a, (3.2)]. Now δ_g and d lie in
ρ_sf Diff¹_3b by (c), and multiplication by c or ι_(c♯) lies in ρ_sf C^∞; so L_h ∈ hρ_sf²Diff¹_3b. The principal
symbols are [Hin26a, Lemma 3.2], a pointwise identity free of the dimension ([[prop:np-10-13]] (i)). ∎

**Lemma {#lem:iv5-0-3}** (The causal facts; [Hin26a, p. 15] and the uses in [Hin26a, Propositions 5.6, 5.16] in
dimension 4 + 1.) Let T_0 := ½ and r̂ = ¾R₁. There is a neighbourhood U ⊂ ℬ of b₀ such that for b ∈ U:

(a) for every β ∈ (−1, 1], d(t − βr) is past timelike on {r ≥ ½r_♯}, with
g⁻¹(dt − β dr, dt − β dr) ≤ −(1 − β²); in particular dt and d(t ± κr), κ ∈ (0, 1), are past timelike, X_0 is
spacelike, and future timelike vectors point into Ω at X_0;

(b) r²g⁻¹(dτ, dτ) ≤ −¾ on τ⁻¹([0, T_0]); so dτ is past timelike for g_3b := ρ_sf²g there, uniformly up to 𝗌𝖿;

(c) on {½r_♯ ≤ r ≤ r̂}, dr is future timelike, with g⁻¹(dr, dr) ≤ −½; so Σ^♯ is spacelike, future timelike vectors
point out of Ω there, and −dr is past timelike;

(d) dρ_K/ρ_K² = −dt with ρ_K = t⁻¹ near (K⁺)°, and dρ_sf/ρ_sf² = −dr.

*Proof.* (a) The time orientation is the one in which dt is past timelike ([Hin26a, p. 14]). By [[lem:iii-b-3-3]] (e),
g⁻¹(dt − β dr, dt − β dr) = −(1 − β²) − H_b(1 + βr_A/|x|)² < 0 for β ∈ (−1, 1], wherever the condition of
[[lem:iii-b-3-3]] (c) holds, which is all of {r ≥ ½r_♯} ([[lem:s11-ks-domain]]). The family s ↦ d(t − sβr), s ∈ [0, 1],
is timelike throughout and starts at dt, so it stays in the past cone. A future timelike V has dt(V) > 0, since dt is
past timelike.

(b) dτ = r⁻¹(dt − τ dr), so r²g⁻¹(dτ, dτ) is the quantity of (a) at β = τ ∈ [0, ½], at most −(1 − ¼). As
g_3b⁻¹ = r²g⁻¹, this is the claim; on Tangherlini space it is [[prop:np-10-22]] (ii).

(c) At b₀, g⁻¹(dr, dr) = 1 − m₀r⁻² ≤ 1 − 16/9 on [½r_♯, r̂], its value at r̂, as smaller r make it more negative, and
g⁻¹(dr, dt) = m₀r⁻² > 0 ([[prop:np-10-22]] (iii)). The second says that the timelike covectors dr and dt lie in opposite
cones, so dr is future timelike. Both strict inequalities hold on a compact set, and g⁻¹ is continuous in b there, so
they persist on a neighbourhood U of b₀. A future timelike V has dr(V) < 0, so V points out of {r ≥ r_♯}.

(d) is direct. ∎

**Lemma {#lem:iv5-0-4}** (The fibre algebra and the subprincipal symbol; [Hin26a, Lemmas 3.3–3.9, Corollary 3.6] in
dimension 4 + 1.) At every point of M^♭, [[lem:iv4-1-1]] and [[lem:iv4-1-causal]] hold for (g, rc, e), with
B := g⁻¹ − (1 + e)G(rc)⁻¹(rc)♯ ⊗ (rc)♯. The skew-adjoint part S := (2ih)⁻¹(L_h − L_h*), adjoint for |dg| and B, is the
bundle map of [[eq:s14-s]], which is [Hin26a, Lemma 3.9] in dimension 4 + 1. There is C > 0, uniform for b ∈ U, such that
C(ρ_sf⁻²ℓ(ζ))² + ρ_sf⁻²G(ζ) is B-positive definite for 0 ≠ ζ ∈ ³ᵇT*_Ω M^♭.

*Proof.* c is past timelike on {r ≥ ½r_♯} ([[sec:iv5-0]]), so [[lem:iv4-1-1]] and [[lem:iv4-1-causal]] apply on each
fibre over the interior of M^♭, and at K⁺ ∪ 𝗌𝖿 to the rescaled data below. As (2ih)⁻¹(L_h − L_h*) = A + A* with
A = (2ih)⁻¹L_h, the formula for S is [[prop:np-10-13]] (ii), proved there on a Lorentzian manifold of any dimension
with the adjoint taken for |dg| and B.
For the uniform C, write ζ ∈ ³ᵇT*M^♭ as Σ_μ ζ_μ dz^μ/r, put ζ̂ := Σ_μ ζ_μ dz^μ ∈ 𝒯* and ĉ := rc. As ℓ_(g,c,e)(ζ) is
bilinear in (c, ζ), and B does not change under c ↦ rc, ρ_sf⁻²G(ζ) = G(ζ̂) and ρ_sf⁻²ℓ(ζ) = ℓ_(g,ĉ,e)(ζ̂). The
components of g and ĉ in the frame dz^μ are continuous on Ω, K⁺ and 𝗌𝖿 included, and in b ([[lem:iv5-0-2]] (a), (d));
g is Lorentzian and ĉ past timelike there ([[lem:iv5-0-5]] (1); at 𝗌𝖿, g = η and ĉ = dt − v dr). So for b in a
compact neighbourhood of b₀, shrinking U, these pairs (g, ĉ) form a compact set, and [[lem:iv4-1-causal]] (d) gives
one C. ∎

**Lemma {#lem:iv5-0-5}** (The 1-form; [Hin26a, Proposition 5.1] in dimension 4 + 1.) Let (α_sf, α_K) = (−C_0 − 5/2, 1)
with C_0 ∈ [0, 100], the weights [[eq:iv4-2-1]]. Put w := ρ_sf^(α_sf+1)ρ_K^(α_K) and w′ := ρ_sf^(α_sf+1). Shrinking U,
there are δ_r ∈ (0, min((4r_c)⁻¹, 1/5)) and δ_sf = 1/100 such that for b ∈ U, c satisfies the conditions (1)–(6) of
[[lem:iv4-1-4]] ([Hin26a, Proposition 5.1] with r_c for r_0 and r_♯ for its inner radius). The positivity statements
(3)–(6) hold with lower bounds uniform in b ∈ U.

*Proof.* [[lem:iv4-1-4]]. Each positivity is a strict inequality for a continuous function of (b, point) on a compact
set, or holds at 𝗌𝖿, where every g, b ∈ U, has the 3sc model η ([[lem:iv5-0-2]] (a)); so the lower bounds are uniform
after shrinking U and δ_r, keeping δ_sf. ∎

*Notation* ([Hin26a, (5.19)]). P_h = □_h − iL_h with □_h := h²□_g; ℓ, B and S are as above. ⟨·, ·⟩ is the
L²(M^♭, |dg|; 𝒯*)-pairing with B. Schwartz kernels of pseudodifferential operators are supported in Ω′ × Ω′,
Ω′ := Ω ∖ (X_0 ∪ Σ^♯). Σ ⊂ ³ᵇT*M^♭ is the closure of G⁻¹(0), the characteristic set of h²ρ_sf⁻²□_g;
∂Σ = ∂Σ₊ ⊔ ∂Σ₋ are its components at fibre infinity, the future and past light cones; o is the zero section. |·| is a
fixed fibre norm on ³ᵇT*M^♭. A *square root* below is always of a B-self-adjoint endomorphism field that is positive
semidefinite on the support in question, and it is smooth wherever the argument is a smooth function times a positive
definite field, or is positive definite; [Hin26a] arranges this through the cut-off conditions (∓χχ′)^(1/2) ∈ C^∞.

#### The semiclassical 3b- and eb-calculi {#sec:iv5-calc}

This section constructs the calculi of [[def:iv5-0-1]] and [[sec:iv6-2]] as instances of the parameterised scaled
bounded geometry calculus of [[thm:std-sbg-calculus]], and proves the facts about them that the chapter uses
([[prop:np-10-65-a]]). The sharp Gårding inequality is not used. Its place is taken by two estimates with explicit
margins: a bound by the supremum of the principal symbol plus a margin ([[lem:iv5-calc-garding]]), and a lower bound for
a non-semiclassical operator with positive definite principal symbol ([[lem:iv5-calc-q0]]). The dimension enters only
through the cells. Throughout, A* is the adjoint of A for the pairing ⟨·, ·⟩ of the notation above, extended to
M₀° = ℝ_t × ℝ⁴_x with |dg| = |dt dx| and with B extended from M^♭ to a smooth field on M₀ that is uniformly positive
definite; all operators in this chapter have Schwartz kernels in Ω′ × Ω′ or are differential, so the extension does not
affect any statement. Below, (S1)–(S15) are the items of [[sec:ii-a-3]], which [[thm:std-sbg-calculus]] repeats with
quotations under the same numbers, and (S16) is the item of [[thm:std-sbg-calculus]].

**Definition {#def:iv5-calc-cells}** (The cells and the calculi.) Let ℬ be the following set of charts of M₀°, each with
values in (−2, 2)⁵.

(1) U_((1),j) := (j − 2, j + 2)_t × (−2, 2)⁴_x, with φ := (t − j, x), for j ∈ ℤ.

(2) U_((2),i,±,j,k,m) := {2^k(j − 2) < t < 2^k(j + 2), 2^(k−2) < ±x^i < 2^(k+2), x^a/x^i − m_a ∈ (−2, 2) for a ≠ i},
with φ := (2^(−k)t − j, log₂(±x^i) − k, (x^a/x^i − m_a)_(a≠i)), for i ∈ {1, …, 4}, a sign ±, j ∈ ℤ, k ∈ ℕ₀ and
m = (m_a)_(a≠i) ∈ {−2, …, 2}³.

The *3b-structure* is ℬ with all scalings 1, and the *semiclassical 3b-structure* is the family (ℬ^×_h)_(h∈(0,1]), where
ℬ^×_h is ℬ with all scalings equal to h. Its operator Lie algebra is denoted 𝒱_h, and the coefficient Lie algebra of ℬ
is 𝒲. On M° = ℝ_t × (ℝ⁴_x ∖ 0), the interior of M := [ℝ̄^(1+4); {r = 0}] of [[sec:iv6-0]], fix finitely many charts
ϑ_β : U̸_β → (−2, 2)³ of 𝕊³ such that the sets ϑ_β⁻¹((−1, 1)³) cover 𝕊³, and let ℬ_eb consist of the charts

    U_(j,k,β) := (2^j(k − 2), 2^j(k + 2))_t × (2^(j−2), 2^(j+2))_r × U̸_β,    φ := (2^(−j)t − k, log₂ r − j, ϑ_β(x/r)),

for j, k ∈ ℤ; the *eb-* and *semiclassical eb-structures* are ℬ_eb with scalings 1, respectively h.

For a countable set P′ ⊂ (0, 1] let N_(P′) := P′ × M₀°, with the scaled bounded geometry structure whose charts are
{h} × U_α → (−2, 2)⁵, (h, p) ↦ φ_α(p), with scalings h, for h ∈ P′ and U_α ∈ ℬ. A family of operators
A = (A_h)_(h∈(0,1]) on ℂ⁵-valued functions on M₀° (sections of 𝒯* in the frame dt, dx¹, …, dx⁴) restricts to the
operator A_(P′) := (A_h)_(h∈P′) on N_(P′). For a weight w on (M₀°, ℬ) and m ∈ ℝ, wΨ^m_(3b,ħ) is the space of the
families A such that A_(P′) ∈ wΨ^m_𝒱(N_(P′)) for every countable P′ ([[thm:std-sbg-calculus]], (S4), (S14)). This is
the device by which [Hin26d] proves the uniform boundedness in parameterised settings
((S7), with [Hin26d, footnote 13]). The seminorms of A_(P′) ((S5)) are suprema over h ∈ P′ of seminorms of the A_h; so
they are bounded independently of P′, for otherwise the union of countably many P′ on which some seminorm exceeds 1, 2,
3, … would be a countable set on which it is infinite. We write whΨ^m_(3b,ħ) := {hA : A ∈ wΨ^m_(3b,ħ)} and
wh^∞Ψ^(−∞)_(3b,ħ) := ⋂_N wh^NΨ^(−N)_(3b,ħ); a family of symbols a = (a_h) lies in wS^m if its restriction to every
N_(P′) lies in wS^m(^𝒱T*N_(P′)); and Op(a) := (Op_(𝒱_h)(a_h))_h. The principal symbol of A is the class of the symbols
of the A_(P′), an element of wS^m/whS^(m−1). The classes wΨ^m_3b of the 3b-structure, and wΨ^m_(eb,ħ), wΨ^m_eb on M°,
are defined in the same way (for the structures with scalings 1, P′ is a single point and h is absent).

The Sobolev spaces are wH^s_(3b,h) := w⟨x⟩^(−5/2)H^s_(𝒱_h)(M₀°; ℂ⁵), normed by
‖u‖_(wH^s_(3b,h)) := h^(5/2)‖⟨x⟩^(5/2)u‖_(wH^s_(𝒱_h)) ((S3)); wH^s_3b is the case h = 1; wH^s_(eb,h) and wH^s_eb are
defined with r for ⟨x⟩. For w = ρ_sf^(β_sf)ρ_K^(β_K) these are the spaces H^(s,(β_sf,β_K))_(3b,h) of [[def:iv5-0-1]].

**Lemma {#lem:iv5-calc-structure}** (The structures.)

(a) ℬ and ℬ_eb are bounded geometry structures, and (ℬ^×_h)_h and the semiclassical eb-structure are parameterised
scaled bounded geometry structures ((S1), (S7)). The coefficient Lie algebra 𝒲 of ℬ consists of the vector fields
Σ_μ f^μ⟨x⟩∂_(z^μ) with f^μ ∈ C^∞_(uni,ℬ)(M₀°), and 𝒱_h = h𝒲; the same holds for ℬ_eb with r∂_(z^μ). Restriction to M₀°
maps C^∞(M₀) into C^∞_(uni,ℬ)(M₀°), and restriction to M° maps C^∞(M) into C^∞_(uni,ℬ_eb)(M°).

(b) ⟨x⟩ is a weight for ℬ, and so is every product of real powers of boundary defining functions of M₀ and of a positive
element of C^∞(M₀); in particular ρ_sf^(β_sf)ρ_K^(β_K), with ρ_sf and ρ_K defining functions of 𝗌𝖿 and K⁺ in M₀ ((S2)).
Being independent of h, these are weights for (ℬ^×_h)_h ((S7)). The same holds for ℬ_eb, with r and the boundary
defining functions of M.

(c) There is C, independent of h, with C⁻¹‖u‖_(L²(M₀°, |dt dx|; B)) ≤ ‖u‖_(H⁰_(3b,h)) ≤ C‖u‖_(L²(M₀°, |dt dx|; B)), and
likewise for the eb-spaces on M°.

(d) Identify ³ᵇT*M₀ with M₀ × ℝ⁵ through ζ ↦ Σ_μ ζ_μ dz^μ/⟨x⟩, let ³ᵇT̄*M₀ be its fibrewise radial compactification,
𝒫 := [0, 1]_h × ³ᵇT̄*M₀ and 𝒫° := (0, 1] × ³ᵇT*M₀, and identify (h, z, ζ) ∈ 𝒫° with the covector
h⁻¹Σ_μ ζ_μ dz^μ/⟨x⟩ ∈ ^(𝒱_h)T*_zM₀° = T*_zM₀°. Put ρ_∞ := ⟨ζ⟩⁻¹, |ζ| being the Euclidean norm of (ζ_μ). Then for
a ∈ C^∞(𝒫; End ℂ⁵), m ∈ ℝ and a weight w as in (b), the family (wρ_∞^(−m)a(h, ·))_h lies in wS^m. The same holds for
𝒫_eb := [0, 1] × ^(eb)T̄*M, with ^(eb)T*M ≅ M × ℝ⁵ through ζ ↦ Σ_μ ζ_μ dz^μ/r.

*Proof.* (a) *Cover and multiplicity.* A point with max_q |x^q| < 1 lies in φ⁻¹((−1, 1)⁵) for the chart U_((1),j) with
j an integer nearest to t. Otherwise let |x^i| = max_q |x^q| ≥ 1, and take the sign of x^i, the integer k ≥ 0 nearest
to log₂|x^i|, the integer j nearest to 2^(−k)t and m_a ∈ {−1, 0, 1} nearest to x^a/x^i ∈ [−1, 1]; then every
coordinate of φ has absolute value at most ½. A point lies in at most four charts U_((1),j), and, for each i and sign,
in charts U_((2)) for at most four values of k, then of j, and of each m_a. So ℬ has finite multiplicity.

*Transitions.* On U_((2),i,±,j,k,m) write (T, X, Ω) for the coordinates and Ω̃_a := Ω_a + m_a = x^a/x^i, Ω̃_i := 1. Then
t = 2^k(T + j), x^i = ±2^(k+X) and x^a = x^iΩ̃_a, and |x^i| ≤ |x| < 7|x^i| as |Ω̃_a| < 4. If this chart meets
U_((2),i′,±′,j′,k′,m′), then 2^(k′−2) < |x^(i′)| < 7·2^(k+2) and symmetrically, so |k − k′| ≤ 7, and the second chart
has the coordinates

    T′ = 2^(k−k′)T + (2^(k−k′)j − j′),     X′ = X + k − k′ + log₂|Ω̃_(i′)|,     Ω̃′_b = Ω̃_b/Ω̃_(i′),

with |Ω̃_(i′)| = |x^(i′)|/|x^i| ≥ 2^(k′−k−4) on the closure of the overlap. As |T|, |T′| < 2 there, the number
2^(k−k′)j − j′ ∈ 2^(−7)ℤ is bounded, so it takes finitely many values. Hence these transition maps are restrictions of
finitely many smooth maps, each defined near the closure of the corresponding overlap. A chart U_((1),j) meets charts
U_((2)) only with k ≤ 2, and two charts U_((1)) differ by an integer translation in t of length at most 3. So all
transition maps are uniformly bounded in C^∞, and ℬ is a bounded geometry structure ((S1)). With constant scalings h,
condition [Hin26d, (1.6)] is the uniform C^∞ bound of the transition maps, uniformly in h; so (ℬ^×_h)_h is the
semiclassical case of [Hin26d, Definition 1.9] ((S7)).

*Lie algebras.* On the charts U_((2)),

    ∂_T = 2^(−X)|x^i|∂_t,     ∂_X = (ln 2)(x^i∂_(x^i) + Σ_(a≠i) x^a∂_(x^a)),     ∂_(Ω_a) = x^i∂_(x^a),

and conversely |x^i|∂_t = 2^X∂_T, |x^i|∂_(x^a) = ±∂_(Ω_a) and |x^i|∂_(x^i) = ±((ln 2)⁻¹∂_X − Σ_(a≠i) Ω̃_a∂_(Ω_a)).
Moreover ⟨x⟩/|x^i| = (2^(−2(k+X)) + 1 + Σ_(a≠i) Ω̃_a²)^(1/2) lies in [1, 11] and has bounded derivatives of all orders,
as 2^(k+X) > ¼. On the charts U_((1)) the coordinate fields are ∂_t, ∂_x, and 1 ≤ ⟨x⟩ ≤ √17. So in every chart the
coordinate vector fields and the fields ⟨x⟩∂_(z^μ) are combinations of each other with coefficients bounded with all
derivatives, uniformly in the chart. This is the description of 𝒲, and 𝒱_h = h𝒲 because all scalings equal h ((S1)).

*Smooth functions.* The fields ⟨x⟩∂_(z^μ) extend to smooth vector fields on M₀ tangent to its boundary hypersurfaces.
Near 𝗌𝖿 away from K^±, in the coordinates 1/r, t/r and x/r, one has r∂_t = ∂_(t/r) and r∂_r = −(1/r)∂_(1/r) −
(t/r)∂_(t/r), the angle being fixed. Near the interior of K⁺, in the coordinates s := 1/t and x, ⟨x⟩∂_t = −⟨x⟩s·s∂_s,
and the ⟨x⟩∂_(x^q) are tangent to K⁺. Near K⁺ ∩ 𝗌𝖿, in (ρ_K, ρ_sf) := (r/t, 1/r) and the angle, r∂_t = −ρ_K·ρ_K∂_(ρ_K)
and r∂_r = ρ_K∂_(ρ_K) − ρ_sf∂_(ρ_sf). In all cases r∂_(x^q) = (x^q/r)r∂_r plus vector fields tangent to the spheres
with coefficients smooth in the angle, and ⟨x⟩/r is smooth near r = ∞; K⁻ is the same with −t for t. So every iterated
derivative of f ∈ C^∞(M₀) along the ⟨x⟩∂_(z^μ) is bounded, and by the previous paragraph f is bounded with all
derivatives in the charts, uniformly.

*The eb-structure.* On U_(j,k,β), with coordinates (T, X, θ), r∂_t = 2^X∂_T, r∂_r = (ln 2)⁻¹∂_X, and the r∂_(x^q) are
(x^q/r)r∂_r plus combinations of the ∂_θ with coefficients bounded with all derivatives (finitely many charts of 𝕊³).
Cover, multiplicity and transitions are checked as above, with T′ = 2^(j−j′)T + (2^(j−j′)k − k′), X′ = X + j − j′ and
the transition maps of the charts of 𝕊³. The fields r∂_(z^μ) are smooth on M and tangent to its boundary: near 𝖼𝖿
they are r∂_t, r∂_r and fields tangent to the spheres; near 𝗌𝖿 they are as above; and near 𝖼𝖿 ∩ 𝗌𝖿, in
(ρ_sf, ρ_cf) := (1/t, r/t) for t > 0 and the angle, r∂_t = −ρ_cf(ρ_sf∂_(ρ_sf) + ρ_cf∂_(ρ_cf)) and r∂_r = ρ_cf∂_(ρ_cf).

(b) By (S2), w > 0 is a weight if Ww/w is bounded with all derivatives in the charts for W ∈ 𝒲. Now
⟨x⟩∂_(x^q)⟨x⟩/⟨x⟩ = x^q/⟨x⟩ and ∂_t⟨x⟩ = 0. If ρ_H defines a boundary hypersurface of M₀ and V is a smooth vector field
on M₀ tangent to the boundary, then Vρ_H/ρ_H ∈ C^∞(M₀); with (a) this gives the claim for the products. As the weights
and the charts do not depend on h, the ratios of the weight across overlapping charts of the parameterised structure are
those for ℬ, which are bounded ((S7), the sufficient condition after [Hin26d, Definition 3.58]).

(c) On U_((2),i,±,j,k,m), dt = 2^k dT, dx^i = (ln 2)x^i dX and dx^a = Ω̃_a dx^i + x^i dΩ_a, so the density |dt dx|
equals (ln 2)2^k|x^i|⁴|dT dX dΩ|; as 2^k/|x^i| ∈ (¼, 4) and ⟨x⟩/|x^i| ∈ [1, 11], ⟨x⟩^(−5)|dt dx| is the Lebesgue
measure of the chart times a function lying between two positive constants. On U_((1)) this is clear. By
[Hin26d, (3.14)] ([[rem:std-sbg-sobolev]]) at s = 0, where S_α is the dilation by h⁻¹, ‖v‖²_(H⁰_(𝒱_h)) = Σ_α
‖(S_α)_*(φ_α)_*(χ_αv)‖²_(L²) = h^(−5) Σ_α ∫ |(φ_α)_*(χ_αv)|² dx. As Σ_α χ_α² lies between two positive constants
(finite multiplicity, and χ_α = 1 on the sets φ_α⁻¹([−1, 1]⁵), which cover), this is uniformly equivalent to
h^(−5)‖v‖²_(L²(⟨x⟩^(−5)|dt dx|)). Put v := ⟨x⟩^(5/2)u; the factor h^(5/2) in the norm gives the claim for the Euclidean
inner product of ℂ⁵, and B is uniformly equivalent to it. On U_(j,k,β), |dt dx| = r³|dt dr dω|, and dt = 2^j dT,
dr = (ln 2)r dX, so r⁻⁵|dt dx| is the Lebesgue measure of the chart times a function between two positive constants.

(d) In a chart U_α of ℬ, with coordinates y and the fibre coordinates ξ of (S4), the covector Σ_i ξ_i dy^i/h equals
h⁻¹Σ_μ ζ_μ dz^μ/⟨x⟩ exactly when ξ = C_α(y)ζ, where C_α(y)_(iμ) := ⟨x⟩⁻¹∂z^μ/∂y^i are the coefficients of ∂_(y^i) in
terms of the ⟨x⟩∂_(z^μ). By (a), C_α and C_α⁻¹ are bounded with all derivatives, uniformly in α, and they do not
depend on h; so ⟨ξ⟩/⟨ζ⟩ lies between two positive constants. A smooth function on ³ᵇT̄*M₀ has bounded derivatives of
all orders along the fields ⟨x⟩∂_(z^μ), acting at fixed ζ (smooth vector fields on ³ᵇT̄*M₀ by (a)), and its
ζ-derivatives of order γ are bounded by C⟨ζ⟩^(−|γ|), by the radial compactification. By the chain rule through ζ =
C_α(y)⁻¹ξ, the function (y, ξ) ↦ a(h, y, C_α(y)⁻¹ξ) satisfies |∂_y^β∂_ξ^γ ·| ≤ C_(βγ)⟨ξ⟩^(−|γ|), uniformly in α and h:
a y-derivative at fixed ξ adds a ζ-derivative times (∂_yC_α⁻¹)ξ, and |ξ| ≤ C⟨ζ⟩. The function ρ_∞⟨ξ⟩ and its inverse
satisfy the same estimates, so ρ_∞^(−m) ∈ S^m with uniform bounds; this gives the claim, w being a weight. The eb-case
is the same. ∎

**Definition {#def:iv5-calc-micro}** (Microsupport and elliptic set.) Let ∂_ħ := ({0} × ³ᵇT̄*M₀) ∪ ([0, 1] × ³ᵇS*M₀)
⊂ 𝒫, where ³ᵇS*M₀ is fibre infinity. In statements about WF′ and Ell, a subset S of ³ᵇT̄*M₀, such as the zero section o
or the set ∂Σ of the notation above, or a set described by a condition |ζ| < 1, stands for
({0} × S) ∪ ([0, 1] × (S ∩ ³ᵇS*M₀)) ⊂ ∂_ħ. A family of symbols a is *supported in* a closed set K ⊂ 𝒫 if a vanishes on
𝒫° ∖ K. An operator B ∈ wΨ^m_(3b,ħ) is *microsupported in* a closed set K ⊂ 𝒫 if Op(1 − y)B and BOp(1 − y) lie in
wh^∞Ψ^(−∞)_(3b,ħ) for every real y ∈ C^∞(𝒫) equal to 1 on a neighbourhood of K; here Op(1 − y) ∈ Ψ⁰_(3b,ħ) by
[[lem:iv5-calc-structure]] (d). For A ∈ wΨ^m_(3b,ħ) with principal symbol represented by a, the *elliptic set*
Ell(A) = Ell_(3b,ħ)(A) is the set of p ∈ ∂_ħ having a neighbourhood 𝒰 in 𝒫 such that a is invertible on 𝒰 ∩ 𝒫°,
with |a⁻¹| ≤ Cw⁻¹ρ_∞^m there for some C, |·| being the operator norm for B. It is open in ∂_ħ, and it does not depend on
the representative: a changes by whρ_∞^(1−m)e with e bounded, and hρ_∞ is continuous on 𝒫 and vanishes on ∂_ħ. For
S ⊂ ∂_ħ, *WF′(B) ⊂ S* (WF′ = WF′_(3b,ħ)) means that B is microsupported in a closed set K with K ∩ ∂_ħ ⊂ S, and
*WF′(B) ∩ S = ∅* means that B is microsupported in a closed set K with K ∩ S = ∅. B has *compact operator wave front set*
if it is microsupported in a closed set disjoint from [0, 1] × ³ᵇS*M₀. The same definitions are made with 𝒫_eb for the
eb-calculus.

**Lemma {#lem:iv5-calc-disjoint}** (Disjoint supports.) Let c_1 ∈ w_1S^(m_1) and c_2 ∈ w_2S^(m_2) be supported in closed
sets K_1, K_2 ⊂ 𝒫 with K_1 ∩ K_2 = ∅, and let T ∈ w_3Ψ^(m_3)_(3b,ħ). Then Op(c_1)TOp(c_2) ∈ w_1w_2w_3h^∞Ψ^(−∞)_(3b,ħ).
Consequently:

(a) if c ∈ wS^m is supported in K and R ∈ wh^∞Ψ^(−∞)_(3b,ħ), then Op(c) + R is microsupported in K;

(b) if B is microsupported in K, then so is T_1BT_2 for all T_1, T_2 in the calculus;

(c) if B is microsupported in K_1 and in K_2, then it is microsupported in every closed neighbourhood of K_1 ∩ K_2; and
if K_1 ∩ K_2 = ∅, then B ∈ h^∞Ψ^(−∞)_(3b,ħ);

(d) a symbol c ∈ wS^m supported in a closed set disjoint from ∂_ħ lies in ⋂_N wh^NS^(−N), and Op(c) ∈ wh^∞Ψ^(−∞)_(3b,ħ).

The same holds for the eb-calculus.

*Proof.* Fix a countable P′ ⊂ (0, 1], write N := N_(P′), and denote restrictions to P′ by the same letters; the scaling
weight of N is ρ̄ = h ≤ 1. By (S14) the entries of Op(c_1)TOp(c_2) are sums of operators of the same form with scalar
symbols supported in K_1 and K_2 and scalar T, so we may assume c_1, c_2 and T scalar. Choose a real y ∈ C^∞(𝒫) with
y = 1 near K_1 and y = 0 near K_2. By [[lem:iv5-calc-structure]] (d), y lies in S⁰(^𝒱T*N) = C^∞_(uni,ℬ*)(^𝒱T*N)
([Hin26d, Lemma 3.24 (1)], (S16)), so its continuous extension j(y) to the uniform compactification of ^𝒱T*N is defined
([Hin26d, Definition 3.25], (S16)); as ^𝒱T*N is dense there, j is linear and j(1) = 1. Let ϖ be a point of the
microlocalisation locus of N. If j(y)(ϖ) ≠ 1, then χ := 1 − y has j(χ)(ϖ) ≠ 0 and χc_1 = 0, so ϖ is not in the essential
support of c_1. If j(y)(ϖ) = 1, then χ := y has j(χ)(ϖ) ≠ 0 and χc_2 = 0, so ϖ is not in the essential support of c_2.
Hence the essential supports E_1 of c_1 and E_2 of c_2 are disjoint; they are the operator wave front sets of Op(c_1)
and Op(c_2) ([Hin26d, Definition 3.43], (S16)).

Put w := w_1w_2w_3, m := m_1 + m_2 + m_3 and X := Op(c_1)TOp(c_2). Then X ∈ wΨ^m_𝒱(N) ([Hin26d, Theorem 3.51], (S5)),
and X maps C_c^∞(N) to itself, as quantisations and residual operators do ([Hin26d, p. 44 and Definition 3.34], (S16)).
Let w′ be a weight on N, L ≥ |m| and u ∈ w′ρ̄^(−L)H^(−L)_𝒱(N). For all σ, l ∈ ℝ, the microlocality of
[Hin26d, Proposition 3.55 (2)] ((S16)), applied to Op(c_2), to T and to Op(c_1) in turn, gives
WF^(σ−m_2,w_2w′,l)_𝒱(Op(c_2)u) ⊂ E_2, then WF^(σ−m_2−m_3,w_3w_2w′,l)_𝒱(TOp(c_2)u) ⊂ E_2, and
WF^(σ−m,ww′,l)_𝒱(Xu) ⊂ E_2 ∩ E_1 = ∅; so Xu ∈ ww′ρ̄^lH^(σ−m)_𝒱(N) by [Hin26d, Proposition 3.55 (1)]. Thus X maps
w′ρ̄^(−L)H^(−L)_𝒱(N) into Y := ww′ρ̄^LH^L_𝒱(N). As a map into Z := ww′ρ̄^(−L)H^(−L−m)_𝒱(N) it is bounded
([Hin26d, Theorem 3.44], (S5)), and Y ⊂ Z with a continuous inclusion, by [Hin26d, (3.14)] ([[rem:std-sbg-sobolev]]) and
ρ̄ ≤ 1; so X, as a map into Y, has closed graph and is bounded. Next let w″ be a weight on N, put w′ := (ww″)⁻¹, and let
X* ∈ wΨ^m_𝒱(N) be the formal adjoint of X for a uniformly positive 𝒱-density ([Hin26d, Theorem 3.51]). For u,
v ∈ C_c^∞(N), ⟨X*v, u⟩ = ⟨v, Xu⟩ and |⟨v, Xu⟩| ≤ C‖v‖_(w″ρ̄^(−L)H^(−L))‖Xu‖_(ww′ρ̄^LH^L), as w″ = (ww′)⁻¹. The duality
of [Hin26d, Proposition 3.22] ((S16)) identifies ww″ρ̄^LH^L_𝒱(N) = w′⁻¹ρ̄^LH^L_𝒱(N) with the dual of
w′ρ̄^(−L)H^(−L)_𝒱(N), with equivalent norms by the open mapping theorem; with the density of C_c^∞(N)
([Hin26d, Lemma 3.20], (S16)) and the bound for X, this gives ‖X*v‖_(ww″ρ̄^LH^L) ≤ C‖v‖_(w″ρ̄^(−L)H^(−L)) for
v ∈ C_c^∞(N), and so for all v ∈ w″ρ̄^(−L)H^(−L)_𝒱(N), by density and the continuity of X* into the larger space
ww″ρ̄^(−L)H^(−L−m)_𝒱(N) ([Hin26d, Theorem 3.44]). The spaces decrease as L grows ([Hin26d, (3.14)], ρ̄ ≤ 1), so these
bounds for L ≥ |m| give them for every L ∈ ℝ.

Finally, every chart of N in {h} × M₀° has all scalings equal to h = ρ̄, so ρ̄W ∈ 𝒱 for W ∈ 𝒲 ((S1)), and ρ̄ is constant
on each {h} × M₀°. With the norm of wH^(s;k)_(𝒱;𝒲)(N) of [Hin26d, p. 37] ((S16)), [Hin26d, Proposition 3.19] ((S3)),
applied to the operators (ρ̄W_1)⋯(ρ̄W_j) ∈ Diff^j_𝒱 for j ≤ k, and [Hin26d, (3.14)] give
‖f‖_(w′H^s) ≤ ‖f‖_(w′H^(s;k)) ≤ C‖f‖_(w′ρ̄^kH^(s+k)) for every weight w′. So the bounds above, with N + k for L, give
those of [Hin26d, Definition 3.34] ((S16)) for all N and k, and X ∈ wρ̄^∞Ψ^(−∞)_𝒱(N). For the weight wρ̄^L the
conditions of that definition are those for w, N ranging over ℝ; so X = Op_𝒱(0) + X lies in wρ̄^LΨ^(−L)_𝒱(N) for every L
([Hin26d, Definition 3.43], (S16)), that is, h^(−L)Op(c_1)TOp(c_2) restricted to P′ lies in wΨ^(−L)_𝒱(N). As P′ is
arbitrary, Op(c_1)TOp(c_2) ∈ wh^LΨ^(−L)_(3b,ħ) for every L.

(a) If y = 1 on a neighbourhood V of K, then 1 − y is supported in 𝒫 ∖ V, which is closed and disjoint from K; so
Op(1 − y)Op(c) and Op(c)Op(1 − y) lie in h^∞Ψ^(−∞) (T = I). Products of R with elements of the calculus stay in
wh^∞Ψ^(−∞), by [Hin26d, Theorem 3.51] on each N_(P′).

(b) Let y = 1 near K, and choose a real y′ ∈ C^∞(𝒫) with y′ = 1 near K and y = 1 near supp y′. Then
B = Op(y′)B + Op(1 − y′)B, the second term lying in h^∞Ψ^(−∞), and Op(1 − y)T_1Op(y′) ∈ h^∞Ψ^(−∞) by the first part;
so Op(1 − y)T_1BT_2 ∈ h^∞Ψ^(−∞). On the right, write B = BOp(y′) + BOp(1 − y′) and use Op(y′)T_2Op(1 − y).

(c) Let K be a closed neighbourhood of K_1 ∩ K_2 and y = 1 near K. By compactness there are real y_1, y_2 ∈ C^∞(𝒫) with
y_i = 1 near K_i and supp y_1 ∩ supp y_2 contained in the interior of {y = 1}. Then
1 − y = (1 − y)(1 − y_1) + (1 − y)y_1(1 − y_2), the remaining term (1 − y)y_1y_2 being 0. Choose a real y′_1 equal to 1
near K_1 with supp y′_1 inside the interior of {y_1 = 1}; then B = Op(y′_1)B + Op(1 − y′_1)B, and
Op((1 − y)(1 − y_1))Op(y′_1) ∈ h^∞Ψ^(−∞) by the first part, so Op((1 − y)(1 − y_1))B ∈ h^∞Ψ^(−∞). In the same way
Op((1 − y)y_1(1 − y_2))B ∈ h^∞Ψ^(−∞), using K_2. On the right the argument is the same. If K_1 ∩ K_2 = ∅, the same
argument with y := 0 and supp y_1 ∩ supp y_2 = ∅ gives B = Op(1)B ∈ h^∞Ψ^(−∞).

(d) The function hρ_∞ is continuous on 𝒫 and vanishes exactly on ∂_ħ, so it is at least some δ > 0 on a closed set
disjoint from ∂_ħ; there h ≥ δ and ⟨ζ⟩ ≤ δ⁻¹. Hence c satisfies the estimates of wh^LS^(−L) for every L, as h^(−L)⟨ξ⟩^L
is bounded on its support ([[lem:iv5-calc-structure]] (d)), and Op(c) ∈ wh^LΨ^(−L) for every L.

The eb-case is the same. ∎

**Lemma {#lem:iv5-calc-d}** (Property (D) at X_0 and at Σ^♯.) Each of the open sets Ω₁ := {t > 0} and
Ω₃ := {t > 0, r < r_♯} of M₀°, and {t > 0} ⊂ M°, has property (D) of [[sec:ii-a-7]] for every s ∈ ℝ and every
h ∈ (0, 1]: C_c^∞ of the set is dense in the subspace of H^s_(𝒱_h) of the elements supported in its closure.

*Proof.* Fix h; the property is qualitative. For fixed h, H^s_(𝒱_h) is the space H^s of ℬ with scalings 1, with an
equivalent norm, by [Hin26d, (3.14)] ([[rem:std-sbg-sobolev]]): the maps S_α are dilations by h⁻¹, which are
isomorphisms of H^s(ℝ⁵). By (S12) we may also replace ℬ by a compatible bounded geometry structure. For Ω₁ we keep ℬ.
For Ω₃, let R₀ := r_♯ + 1 and R₁ := 200R₀, take finitely many charts κ_ℓ : V_ℓ → (−2, 2)⁴ of ℝ⁴ such that the sets
κ_ℓ⁻¹((−1, 1)⁴) cover {|x| ≤ R₁}, each V_ℓ either disjoint from {|x| = r_♯} or such that
κ_ℓ(V_ℓ ∩ {|x| < r_♯}) = {y_1 < 0}, and replace the charts of ℬ that meet {|x| ≤ R₀} by the charts
(j − 2, j + 2)_t × V_ℓ, (t − j, κ_ℓ(x)), j ∈ ℤ. The charts of ℬ that are kept still cover {|x| > R₁}: a chart U_((2))
whose set φ⁻¹((−1, 1)⁵) contains a point with |x| > R₁ has 2^(k−2) > R₁/56 > R₀. The charts of ℬ that meet {|x| ≤ R₁}
have k ≤ log₂R₁ + 2, so all transition maps between the two families are translates in t of finitely many smooth maps;
the result is a bounded geometry structure compatible with ℬ. In each chart of the structure so obtained that meets ∂Ω
(Ω = Ω₁ or Ω₃), with coordinates (T, y), the set Ω is {T > a} or {T > a, y_1 < 0} for some a ∈ ℝ, because the charts are
products in t with T an affine function of t with positive slope; a chart not meeting ∂Ω lies in Ω or in its complement,
being connected.

Let e := (1, −1, 0, 0, 0)/√2 in the coordinates (T, y_1, …), and Γ := {Y ∈ ℝ⁵ : Y·e ≥ ¾|Y|}; every Y ∈ Γ ∖ 0 has
positive T-component and negative y_1-component. Fix ϱ ∈ C_c^∞(ℝ⁵) with ∫ϱ = 1 and supp ϱ ⊂ Γ ∩ {½ ≤ |Y| ≤ 1}, and put
ϱ_ε(Y) := ε^(−5)ϱ(Y/ε), ε ∈ (0, ¼]. If a distribution f on ℝ⁵ is supported in the closure of {T > a} or of
{T > a, y_1 < 0}, then ϱ_ε ∗ f is smooth and supported in {T ≥ a + cε} or in {T ≥ a + cε, y_1 ≤ −cε}, c > 0 depending
only on ϱ.

Let χ ∈ C_c^∞((−5/4, 5/4)⁵) be nonnegative and equal to 1 on [−1, 1]⁵, and χ_α := φ_α^*χ/Σ_β φ_β^*χ. For v in H^s
supported in Ω̄ put w_α := (φ_α)_*(χ_αv) and v_ε := Σ_α φ_α^*(ϱ_ε ∗ w_α); ϱ_ε ∗ w_α is supported in (−3/2, 3/2)⁵. Then
v_ε is smooth and supported in Ω, at distance at least cε from ∂Ω in every chart. By [Hin26d, (3.14)], the norm of an
element of H^s is the square root of Σ_β ‖(φ_β)_*(φ_β^*χ ·)‖²_(H^s(ℝ⁵)); hence ‖Σ_α g_α‖² ≤ L Σ_α ‖g_α‖² for any g_α
supported in U_α, L being a bound for the number of charts that meet a given chart (finite by the description of the
transitions), since each term (φ_β)_*(φ_β^*χ Σ_α g_α) involves at most L of the g_α, and since Σ_β
‖(φ_β)_*(φ_β^*χ g_α)‖² is ‖g_α‖². Moreover, for f ∈ H^s(ℝ⁵) supported in (−3/2, 3/2)⁵, ‖φ_α^*f‖_(H^s) ≤ C‖f‖_(H^s(ℝ⁵)),
and Σ_α ‖w_α‖²_(H^s(ℝ⁵)) ≤ C‖v‖²_(H^s), with C independent of α: H^s(ℝ⁵), for distributions supported in a fixed compact
set, is invariant under multiplication by functions bounded in C^∞ and under diffeomorphisms bounded in C^∞ together
with their inverses, and the transition maps and the functions Σ_β φ_β^*χ are so bounded ((S1)). Convolution with
ϱ_ε − δ_0 is the Fourier multiplier ϱ̂(εξ) − 1, bounded by C uniformly in ε and tending to 0 pointwise; so ‖(ϱ_ε − δ_0)
∗ w_α‖_(H^s(ℝ⁵)) ≤ C‖w_α‖_(H^s(ℝ⁵)), and it tends to 0 for each α. As Σ_α χ_α = 1, ‖v_ε − v‖²_(H^s) ≤ LC Σ_α
‖(ϱ_ε − δ_0) ∗ w_α‖²_(H^s(ℝ⁵)), which tends to 0 by dominated convergence for the series.

Finally let ψ ∈ C_c^∞(ℝ) equal 1 near 0 and ψ_R(t, x) := ψ(t/R)ψ(|x|/R), R ≥ 1. The ψ_R are bounded in C^∞_(uni,ℬ)
uniformly in R, since ⟨x⟩ ≤ CR on supp ψ(|x|/R); so multiplication by ψ_R is bounded on H^s uniformly in R ((S3), (S7)
with parameter R), and ψ_Rf → f in H^s for f ∈ C_c^∞, hence for every f ∈ H^s, C_c^∞ being dense ([Hin26d, Lemma
3.20], (S16)). Now ψ_Rv_ε ∈ C_c^∞(Ω), and it tends to v as R → ∞ and then ε → 0. The case of M° is the same, with the
charts of ℬ_eb, in which {t > 0} is {T > −k}, and with ψ_R(t, x) := ψ(t/R)ψ(|x|/R)(1 − ψ(R|x|)), which has compact
support in M° and is bounded in C^∞_(uni,ℬ_eb) uniformly in R, as |x| ≤ CR on supp ψ(|x|/R) and R|x| ≤ C on
supp ψ′(R|x|). ∎

**Lemma {#lem:iv5-calc-dual}** (Supported and extendible spaces.) Let w be a weight as in [[lem:iv5-calc-structure]] (b),
s ∈ ℝ, Ω₁ := {t > 0} and Ω₂ := {r > r_♯} in M₀°, so that Ω° = Ω₁ ∩ Ω₂. Define:

- wH^s_(3b,h)(Ω)^(•,−) := {ũ|_(Ω₂) : ũ ∈ wH^s_(3b,h), supp ũ ⊂ cl Ω₁}, normed by the infimum of ‖ũ‖_(wH^s_(3b,h)) over
such ũ (supported at X_0, extendible at Σ^♯);

- wH^s_(3b,h)(Ω)^(−,•) := {v ∈ wH̄^s_(3b,h)(Ω₁) : supp v ⊂ {r ≥ r_♯}}, with the norm of wH̄^s_(3b,h)(Ω₁), the infimum of
the norms of the extensions of v to M₀° (extendible at X_0, supported at Σ^♯);

- wH̄^s_(3b,h)(Ω) := {ũ|_(Ω°) : ũ ∈ wH^s_(3b,h)}, with the infimum norm (extendible at both).

Then, with constants independent of h:

(a) for u ∈ wH^s(Ω)^(•,−) and v ∈ w⁻¹H^(−s)(Ω)^(−,•) the number ⟨u, v⟩ := ⟨ũ, ṽ⟩ does not depend on the choice of ũ as
above and of ṽ ∈ w⁻¹H^(−s)_(3b,h) with ṽ|_(Ω₁) = v; |⟨u, v⟩| ≤ C‖u‖‖v‖; and ⟨u, v⟩ is the pairing of distributions
when u or v lies in C_c^∞(Ω°);

(b) every bounded linear functional λ on w⁻¹H^(−s)(Ω)^(−,•) is λ(v) = ⟨v, u⟩ := ⟨ṽ, ũ⟩ for some u ∈ wH^s(Ω)^(•,−) with
‖u‖ ≤ C‖λ‖, and every bounded linear functional λ on wH^s(Ω)^(•,−) is λ(u) = ⟨u, v⟩ for some
v ∈ w⁻¹H^(−s)(Ω)^(−,•) with ‖v‖ ≤ C‖λ‖; conjugate-linear functionals are treated by taking complex conjugates.

For the eb-spaces on M° and Ω = {t ≥ 0}, the same holds with Ω₂ := M°: the supported space wḢ^s_(eb,h)(Ω) and the
extendible space w⁻¹H̄^(−s)_(eb,h)(Ω°) are dual in the same sense.

*Proof.* Let Iu := h^(5/2)⟨x⟩^(5/2)u. By definition I is an isometry of wH^s_(3b,h) onto wH^s_(𝒱_h), and it preserves
supports. With μ_h := h^(−5)⟨x⟩^(−5)|dt dx|, a uniformly positive 𝒱_h-density by the proof of
[[lem:iv5-calc-structure]] (c), one has ⟨u, v⟩ = ∫ (B̂Iu)·(Iv)‾ μ_h, B̂ being the matrix of B in the frame.
Multiplication by B̂ and by B̂⁻¹ is bounded on every wH^s_(𝒱_h), uniformly in h (differential operators of order 0 with
coefficients independent of h, (S3), (S7)), and multiplication by w is an isomorphism of H^s_(𝒱_h) onto wH^s_(𝒱_h), with
bounds independent of h ((S3), (S7)), that preserves supports. So [[lem:ii-a-7-1]] and [[lem:ii-a-7-3]], which are
stated for parameterised scaled bounded geometry structures with a uniformly positive density ([[sec:ii-a-7]]), hold for
the pairing ⟨·, ·⟩ and the spaces wH^s_(3b,h), w⁻¹H^(−s)_(3b,h), with constants independent of h. The open sets Ω₁ and
Ω₃ := {t > 0, r < r_♯} have property (D) for every order ([[lem:iv5-calc-d]]).

(a) Let ũ, ũ′ be two choices for u, and ṽ, ṽ′ two for v. Then ũ − ũ′ is supported in cl Ω₁ ∖ Ω₂ = cl Ω₃, so it is the
limit in wH^s_(3b,h) of elements of C_c^∞(Ω₃), by property (D) of Ω₃; these pair to 0 with ṽ, since ṽ = v vanishes on
Ω₃ ⊂ Ω₁ ∩ {r < r_♯}. So ⟨ũ − ũ′, ṽ⟩ = 0, by the bound of [[lem:ii-a-7-1]] (1). Next, ṽ − ṽ′ vanishes on Ω₁, and ũ′ is the
limit of elements of C_c^∞(Ω₁), by property (D) of Ω₁, which pair to 0 with ṽ − ṽ′; so ⟨ũ′, ṽ − ṽ′⟩ = 0. Hence
⟨ũ, ṽ⟩ = ⟨ũ′, ṽ′⟩. The bound follows from [[lem:ii-a-7-1]] (1) by taking infima over ũ and ṽ. If u or v lies in
C_c^∞(Ω°), it is its own choice of ũ or ṽ.

(b) w⁻¹H^(−s)(Ω)^(−,•) is the kernel of the restriction from w⁻¹H̄^(−s)(Ω₁) to Ω₁ ∩ {r < r_♯}, a closed subspace with
the norm of w⁻¹H̄^(−s)(Ω₁). Extend λ to w⁻¹H̄^(−s)(Ω₁) with the same norm (Hahn–Banach). By [[lem:ii-a-7-3]] (3), second
statement, with −s for 𝗌 and Ω₁ for Ω, there is ũ ∈ wH^s_(3b,h) supported in cl Ω₁ with ‖ũ‖ ≤ C‖λ‖ and λ(v) = ⟨ṽ, ũ⟩
for every v and every extension ṽ of v. Then u := ũ|_(Ω₂) lies in wH^s(Ω)^(•,−), with ‖u‖ ≤ ‖ũ‖ ≤ C‖λ‖ and
λ(v) = ⟨v, u⟩. Conversely, let λ be bounded on wH^s(Ω)^(•,−). Then λ̃(ũ) := λ(ũ|_(Ω₂)) is bounded on the space of the
elements of wH^s_(3b,h) supported in cl Ω₁, with norm at most ‖λ‖. By the first statement of [[lem:ii-a-7-3]] (3), with
−s for 𝗌 and Ω₁ for Ω, λ̃(ũ) = ⟨ũ, ṽ⟩ for some ṽ ∈ w⁻¹H^(−s)_(3b,h) with ‖ṽ‖ ≤ C‖λ‖. As λ̃
vanishes on C_c^∞(Ω₃), whose elements restrict to 0 on Ω₂, ṽ vanishes on Ω₃. So v := ṽ|_(Ω₁) is supported in
{r ≥ r_♯}, v ∈ w⁻¹H^(−s)(Ω)^(−,•), ‖v‖ ≤ ‖ṽ‖, and λ(u) = ⟨u, v⟩.

For the eb-spaces, [[lem:ii-a-7-3]] applies directly with Ω := {t > 0} ⊂ M°, which has property (D) by
[[lem:iv5-calc-d]], with the isometry I defined with r for ⟨x⟩. ∎

**Lemma {#lem:iv5-calc-reg}** (A regularising family.) Let K ∈ ℕ, j_ε := ⟨εζ⟩^(−K) for ε ∈ (0, 1], and J_ε := Op(j_ε).

(a) J_ε ∈ Ψ^(−K)_(3b,ħ) for each ε, and the family (J_ε)_(ε) is bounded in Ψ⁰_(3b,ħ): for every countable set P″ of
pairs (ε, h), the family (J_ε)_((ε,h)∈P″) lies in Ψ⁰_𝒱 of P″ × M₀° with the charts of ℬ and scalings h. In particular
J_ε is bounded on every wH^s_(3b,h), uniformly in (ε, h).

(b) For fixed h, J_εu → u in wH^s_(3b,h) as ε → 0, for every u ∈ wH^s_(3b,h).

(c) For p ∈ wS^m, H_pj_ε = ϑ_εj_εe_p, where e_p := −(K/2)⟨ζ⟩^(−2)H_p(|ζ|²) ∈ wS^(m−1) does not depend on ε and
ϑ_ε := ε²⟨ζ⟩²⟨εζ⟩^(−2) takes values in [0, 1] and is bounded in S⁰ uniformly in ε. For P ∈ wΨ^m_(3b,ħ),
h⁻¹i[P, J_ε] is bounded in wΨ^(m−1)_(3b,ħ) uniformly in ε, with principal symbol H_pj_ε, p the principal symbol of P,
computed entrywise. Here H_p is the Hamilton vector field of [[prop:np-10-65-a]] (b).

*Proof.* (a) In a chart, j_ε = f(εC_α(y)⁻¹ξ) with f(η) := ⟨η⟩^(−K) ∈ S⁰(ℝ⁵) ([[lem:iv5-calc-structure]] (d)). A
derivative ∂_y^β∂_ξ^γ of it is a sum of terms (∂^κf)(εC_α⁻¹ξ) times ε^(|κ|) times polynomials in ξ of degree at
most |κ| − |γ| with coefficients bounded uniformly. As |∂^κf(η)| ≤ C⟨η⟩^(−|κ|), and ε⟨ξ⟩ ≤ ⟨εξ⟩ ≤ C⟨εC_α⁻¹ξ⟩ for ε ≤ 1,
each term is at most Cε^(|κ|)⟨ξ⟩^(|κ|−|γ|)⟨εξ⟩^(−|κ|) ≤ C⟨ξ⟩^(−|γ|); so the family is bounded in S⁰, uniformly in (ε,
h). For fixed ε, j_ε ≤ ε^(−K)⟨ζ⟩^(−K), and likewise for the derivatives, so j_ε ∈ S^(−K). The structure with
parameters (ε, h) is parameterised ((S7)), and the boundedness follows from (S5), (S7) as in [[def:iv5-calc-cells]].

(b) For δ ∈ (0, 1], |∂_y^β∂_ξ^γ(j_ε − 1)| ≤ C_δε^δ⟨ξ⟩^(δ−|γ|), since |1 − f(η)| ≤ C min(1, |η|) ≤ C|η|^δ and the terms
of (a) with |κ| ≥ 1 are at most C(ε⟨ξ⟩⟨εξ⟩⁻¹)^(|κ|)⟨ξ⟩^(−|γ|) ≤ C(ε⟨ξ⟩)^δ⟨ξ⟩^(−|γ|). So ε^(−δ)(j_ε − 1) is bounded in
S^δ, and ‖(J_ε − I)u‖_(wH^s_(3b,h)) ≤ Cε^δ‖u‖_(wH^(s+δ)_(3b,h)), by Op(1) = I ([[prop:np-10-65-a]] (a)) and (S5). As
C_c^∞ is dense in wH^s_(3b,h) ([Hin26d, Lemma 3.20], (S16)), so is wH^(s+δ)_(3b,h); with the uniform bound of (a), J_ε
→ I strongly.

(c) By the chain rule, H_pj_ε = −(K/2)(1 + ε²|ζ|²)^(−K/2−1)ε²H_p(|ζ|²) = ϑ_εj_εe_p. The Poisson bracket H_p(|ζ|²) of
p ∈ wS^m and |ζ|² ∈ S² lies in wS^(m+1), by the estimates in the coordinates (y, ξ) of a chart, in which the bracket is
Σ_i (∂_(ξ_i)p ∂_(y^i) − ∂_(y^i)p ∂_(ξ_i)) applied to |ζ|² ([[lem:iv5-calc-structure]] (d)); so e_p ∈ wS^(m−1). Further
ϑ_ε = 1 − (1 − ε²)⟨εζ⟩^(−2), and ⟨εζ⟩^(−2) is bounded in S⁰ uniformly in ε, as in (a). The statement on h⁻¹i[P, J_ε]
is [[prop:np-10-65-a]] (b), applied in the calculus with parameters (ε, h), J_ε being the quantisation of the scalar
symbol j_ε. ∎

**Proposition {#prop:np-10-65-a}** (The calculi.) Let w, w′, w_1, w_2 be weights as in [[lem:iv5-calc-structure]] (b).
All constants below are independent of h ∈ (0, 1].

(a) (*Contents.*) For a ∈ wS^m, Op(a) ∈ wΨ^m_(3b,ħ) has principal symbol a. For a function f on M₀° bounded with all
derivatives in the charts, Op(f) is multiplication by f, Op(1) = I and f·Op(a) = Op(fa). A differential operator
Σ_(|γ|≤k) a_γ(h⟨x⟩∂_z)^γ whose coefficients a_γ, 5 × 5 matrices, are w times elements of C^∞(M₀) lies in wΨ^k_(3b,ħ),
its principal symbol being the class of its semiclassical principal symbol; this applies to h²□_g, L_h, P_h, P_h*, 𝓛_h
and 𝓛_h* (with the weight ρ_sf²), to the products χ_(τ,j)χ_(r,j′) of the cut-offs, to χ_(r,j) and to the weights. For an
h-independent Q ∈ wDiff^k_3b, h^kQ ∈ wΨ^k_(3b,ħ), with principal symbol the principal symbol of Q evaluated at ζ. The
same holds for wΨ_3b, without h.

(b) (*Algebra.*) Let A_i ∈ w_iΨ^(m_i)_(3b,ħ) have principal symbols a_i. Then A_1A_2 ∈ w_1w_2Ψ^(m_1+m_2)_(3b,ħ) with
principal symbol a_1a_2, and A_1* ∈ w_1Ψ^(m_1)_(3b,ħ) with principal symbol a_1^(*_B), the B-adjoint. An element of
wΨ^m_(3b,ħ) with principal symbol 0 lies in whΨ^(m−1)_(3b,ħ). If a_1a_2 = a_2a_1, then h⁻¹i[A_1, A_2] ∈
w_1w_2Ψ^(m_1+m_2−1)_(3b,ħ); if moreover A_1 = Op(a_1) + hE with a_1 scalar and E ∈ w_1Ψ^(m_1−1)_(3b,ħ) of principal
symbol e (every A_1 with scalar principal symbol a_1 has this form), its principal symbol is H_(a_1)a_2 + i[e, a_2],
where H_(a_1)a_2 is computed entrywise and H_(a_1) is the Hamilton vector field of a_1 for the symplectic structure of
T*M₀°, functions on 𝒫° being regarded as functions of the covector Σ_μ ζ_μ dz^μ/⟨x⟩. In particular it is H_(a_1)a_2
when a_2 is scalar.

(c) (*Self-adjoint quantisations.*) Let a ∈ wS^m be real and scalar, or B-self-adjoint, supported in a closed set
K_a ⊂ 𝒫; let K be a closed neighbourhood of K_a, and ψ ∈ C^∞(M₀) real and equal to 1 near the projection of K_a to M₀.
Then there is A = A* ∈ wΨ^m_(3b,ħ) with principal symbol a and A − Op(a) ∈ whΨ^(m−1)_(3b,ħ), microsupported in K, whose
Schwartz kernel is supported in supp ψ × supp ψ. In particular WF′(A) ⊂ K ∩ ∂_ħ.

(d) (*Boundedness.*) A ∈ w_1Ψ^m_(3b,ħ) maps w_2H^s_(3b,h) to w_1w_2H^(s−m)_(3b,h) with norm bounded independently of h.
An element of w_1h^∞Ψ^(−∞)_(3b,ħ) maps w_2H^(−N)_(3b,h) to w_1w_2H^N_(3b,h) with norm O(h^N), for every N.

(e) (*Elliptic estimate.*) Let A ∈ w′Ψ^m_(3b,ħ), G ∈ Ψ⁰_(3b,ħ), and let B ∈ Ψ⁰_(3b,ħ) be microsupported in a closed set
K ⊂ 𝒫 with K ∩ ∂_ħ ⊂ Ell(A) ∩ Ell(G), that is, WF′(B) ⊂ Ell(A) ∩ Ell(G). Then for all s and N there is C such that for
h ∈ (0, 1] and every u ∈ wH^(−N)_(3b,h) with GAu ∈ ww′H^(s−m)_(3b,h), Bu lies in wH^s_(3b,h) and

    ‖Bu‖_(wH^s_(3b,h)) ≤ C(‖GAu‖_(ww′H^(s−m)_(3b,h)) + h^N‖u‖_(wH^(−N)_(3b,h))).                    {#eq:iv5-calc-ell}

(f) (*Square roots.*) Let w be real, q ∈ w²S^(2k) B-self-adjoint, W ⊂ 𝒫 open and c > 0, with
B(qv, v) ≥ cw²ρ_∞^(−2k)B(v, v) on W ∩ 𝒫° for all v. Then the B-self-adjoint square roots q^(±1/2), positive definite,
satisfy on W ∩ 𝒫° the estimates of w^(±1)S^(±k), uniformly. So φq^(±1/2) ∈ w^(±1)S^(±k) for real φ ∈ C^∞(𝒫) supported in
W, and Op(φq^(1/2))*Op(φq^(1/2)) ∈ w²Ψ^(2k)_(3b,ħ) has principal symbol φ²q. If q = fq′, with 0 ≤ f ∈ C^∞(𝒫) scalar,
f^(1/2) ∈ C^∞(𝒫) and q′ as above, then q^(1/2) = f^(1/2)q′^(1/2).

(g) (*Supported and extendible spaces.*) The conclusions of [[lem:iv5-calc-dual]] hold.

(h) (*Regularisation.*) The family of [[lem:iv5-calc-reg]] has the properties stated there.

(i) (*The eb-calculus.*) (a)–(h) hold for wΨ_(eb,ħ) on M°, with r∂_(z^μ) for ⟨x⟩∂_(z^μ), the frame dz^μ/r of
^(eb)T*M, r for ⟨x⟩ and 𝒫_eb for 𝒫; and (a), (b), (d), (f) hold for wΨ_3b and wΨ_eb.

(j) (*Further parameters.*) Let U be a set, and let the operators and symbols above depend on b ∈ U, such that the
families indexed by (b, h) ∈ U × (0, 1] lie in the classes defined as in [[def:iv5-calc-cells]] with the parameter set
U × (0, 1] in place of (0, 1], the charts and scalings not depending on b. If the ellipticity and positivity bounds in
the hypotheses of (e), (f), [[lem:iv5-calc-garding]] and [[lem:iv5-calc-q0]] hold uniformly in b, then the constants in
their conclusions, and in (d), (g), (h), are uniform in b. The same holds for the calculi with scalings 1 and the
parameter set U.

*Proof.* *Reduction.* A statement about families, restricted to a countable P′ ⊂ (0, 1], is a statement about the
scaled bounded geometry structure N_(P′), to which [Hin26d] applies ((S1)–(S6), (S16)). A membership that holds on every
N_(P′) holds for the family, by [[def:iv5-calc-cells]]. A bound that holds on every N_(P′) holds uniformly in h: if it
failed along a sequence h_ℓ, it would fail on N_(P′) for P′ := {h_ℓ}. This is the argument of [Hin26d, p. 59] ((S7)).

(a) Each chart of N_(P′) lies in one slice {h} × M₀°, so the quantisation of (S4) on N_(P′) is the family of the
quantisations Op_(𝒱_h), and Op(a) restricted to P′ is Op_𝒱(a) ∈ wΨ^m_𝒱(N_(P′)), with principal symbol a
([Hin26d, Definition 3.43], (S16)). In the local quantisation of (S4) the symbol is evaluated at the left variable and
ψ = 1 near 0, and the χ_α of (S4) sum to 1; so for a function f of the base Op_α(χ_αf) has the Schwartz kernel
χ_α(x)f(x)δ(x − x′), which gives Op(f) = f, Op(1) = I and f·Op(a) = Op(fa). By [[lem:iv5-calc-structure]] (a), each
h⟨x⟩∂_(z^μ) is, in every chart, a combination of the fields h∂_(y^i) with coefficients bounded with all derivatives, and
C^∞(M₀) ⊂ C^∞_(uni,ℬ); so the operator is, in every chart, Σ_(|β|≤k) w a′_β(y)(h∂_y)^β with a′_β bounded with all
derivatives uniformly. This characterises wDiff^k within the parameterised calculus ((S7), [Hin26d, p. 59]). Modulo
whS^(k−1), only the terms of order k without a further power of h remain, which gives the principal symbol. The
memberships listed follow from [[lem:iv5-0-2]] (a), (d) and [[eq:iv5-2-1]], the coefficients of P_h, given on
{r ≥ ½r_♯}, being extended to elements of C^∞(M₀). For h^kQ, a term of Q of order j < k carries the factor h^(k−j).

(b) Compositions, adjoints, principal symbols and Poisson brackets are [Hin26d, Theorem 3.51] on N_(P′) ((S5), (S16)),
and the exact sequence is [Hin26d, Definition 3.43] with ρ̄ = h. Operators on ℂ⁵ are 5 × 5 matrices of scalar operators
((S14)), so compositions and principal symbols multiply as matrices. The adjoint of [Hin26d, Theorem 3.51] is taken for
a uniformly positive 𝒱-density, such as μ_h of the proof of [[lem:iv5-calc-dual]], and the Euclidean inner product of
ℂ⁵; call it A^⋆. Then A* = (⟨x⟩⁵B̂)⁻¹A^⋆(⟨x⟩⁵B̂), with B̂ the matrix of B; as ⟨x⟩⁵ is a weight and B̂^(±1) ∈ Ψ⁰ by (a),
A* ∈ w_1Ψ^(m_1) with principal symbol B̂⁻¹a_1^⋆B̂ = a_1^(*_B). If a_1a_2 = a_2a_1, then [A_1, A_2] has principal symbol 0
and lies in hΨ by the exact sequence. If A_1 = Op(a_1) + hE with a_1 scalar, then [Op(a_1), A_2] is the matrix of the
scalar commutators [Op(a_1), (A_2)_(kl)], and [Hin26d, Theorem 3.51] gives the principal symbol of i[Op(a_1), (A_2)_(kl)]
as the Poisson bracket of T*M₀°. In terms of the covector h⁻¹Σ_μ ζ_μ dz^μ/⟨x⟩ of [[lem:iv5-calc-structure]] (d), this
is h times the Poisson bracket of a_1 and (a_2)_(kl) for the covector Σ_μ ζ_μ dz^μ/⟨x⟩, that is hH_(a_1)(a_2)_(kl).
Finally h⁻¹[hE, A_2] = [E, A_2] has principal symbol [e, a_2].

(c) Choose a real y ∈ C^∞(𝒫) with y = 1 near K_a and supp y in the interior of K. Put
A_0 := Op(y)·½(Op(a) + Op(a)*)·Op(y)*, which is self-adjoint, and A := ψA_0ψ, which is self-adjoint as ψ is real and
scalar, and whose Schwartz kernel is supported in supp ψ × supp ψ. By (b), A has principal symbol ψ²yay = a, so
A − Op(a) ∈ whΨ^(m−1). Op(y) is microsupported in supp y ([[lem:iv5-calc-disjoint]] (a)), hence so is A
([[lem:iv5-calc-disjoint]] (b)), and so A is microsupported in K.

(d) This is [Hin26d, Theorem 3.44] on N_(P′) ((S5)) and the reduction, after conjugation by the weight ⟨x⟩^(5/2) ((b));
the factor h^(5/2) of the norms appears on both sides. An element of w_1h^(2N)Ψ^(−2N) maps w_2H^(−N) to w_1w_2H^N with
norm O(h^(2N)).

(e) Let a, g be representatives of the principal symbols of A and G. Every point of K ∩ ∂_ħ has a neighbourhood in 𝒫
on which a and g are invertible with the bounds of [[def:iv5-calc-micro]]. As K ∩ ∂_ħ is compact, there are an open set
O′ ⊃ K ∩ ∂_ħ whose closure is covered by finitely many of these neighbourhoods, and C₀, such that ga is invertible on
cl O′ ∩ 𝒫° with |(ga)⁻¹| ≤ C₀w′⁻¹ρ_∞^m.

*Reduction to K ⊂ O′.* Choose a real y ∈ C^∞(𝒫) with y = 1 near K, whose support meets ∂_ħ only inside O′ (possible by
compactness, as K ∩ ∂_ħ ⊂ O′), and a real ψ ∈ C^∞(𝒫) with ψ = 1 near supp y ∩ ∂_ħ and supp ψ ⊂ O′. Then
B = BOp(yψ) + BOp(y(1 − ψ)) + BOp(1 − y). The last term lies in h^∞Ψ^(−∞) by the definition of microsupport, and
y(1 − ψ) is supported in a closed set disjoint from ∂_ħ, so the second lies in h^∞Ψ^(−∞) by [[lem:iv5-calc-disjoint]]
(d). And BOp(yψ) is microsupported in K′ := supp(yψ) ⊂ O′ ([[lem:iv5-calc-disjoint]] (a), (b)).

*One step.* Let B′ ∈ Ψ⁰ be microsupported in a closed set K′ ⊂ O′, and let K″ ⊂ O′ be closed with K′ in its interior.
Choose real φ_1, φ_2, φ_3 ∈ C^∞(𝒫) with φ_1 = 1 near K′, φ_2 = φ_3 = 1 near supp φ_1, and supp φ_2, supp φ_3 ⊂ K″. Put
q := φ_2(ga)⁻¹ ∈ w′⁻¹S^(−m), by [[lem:iv5-calc-structure]] (d) and the formula ∂(e⁻¹) = −e⁻¹(∂e)e⁻¹ applied to
e := w′⁻¹ρ_∞^m ga. By (b), Op(φ_1q)GA has principal symbol φ_1qga = φ_1φ_2 = φ_1, so
R_1 := h⁻¹(Op(φ_1) − Op(φ_1q)GA) ∈ Ψ^(−1). Both Op(φ_1) and Op(φ_1q)GA are microsupported in supp φ_1
([[lem:iv5-calc-disjoint]] (a), (b)), hence so is R_1. Therefore

    B′ = B′Op(φ_1) + B′Op(1 − φ_1) = B′Op(φ_1q)GA + hB′R_1Op(φ_3) + R′,

with R′ ∈ h^∞Ψ^(−∞), as B′Op(1 − φ_1) and B′R_1Op(1 − φ_3) are. By (d), for every σ and N,

    ‖B′u‖_(wH^σ) ≤ C(‖GAu‖_(ww′H^(σ−m)) + h‖Op(φ_3)u‖_(wH^(σ−1)) + h^N‖u‖_(wH^(−N))),

and Op(φ_3) is microsupported in K″ ⊂ O′ ([[lem:iv5-calc-disjoint]] (a)).

*Iteration.* Let J be an integer with J ≥ N + max(s, 0), and choose closed sets K′ = K_0 ⊂ K_1 ⊂ ⋯ ⊂ K_J ⊂ O′, each in
the interior of the next. Apply the step to BOp(yψ) with σ = s and K″ = K_1, then to the operator Op(φ_3) so obtained
with σ = s − 1 and K″ = K_2, and so on. After J steps the remaining term is at most
Ch^J‖u‖_(wH^(s−J)) ≤ Ch^N‖u‖_(wH^(−N)), as J ≥ N and s − J ≤ −N. This gives [[eq:iv5-calc-ell]]. Each identity
B′u = B′Op(φ_1q)GAu + hB′R_1Op(φ_3)u + R′u holds for u ∈ wH^(−N), all terms being defined by (d); if GAu ∈ ww′H^(s−m),
then, going back from the last step, each Op(φ_3)u lies in wH^(σ−1), and so Bu ∈ wH^s.

(f) Put q̂ := w⁻²ρ_∞^(2k)q ∈ S⁰. It is B-self-adjoint, and its spectrum lies in [c, C₁] on W ∩ 𝒫°, C₁ := sup|q̂|. With
γ a fixed contour in {Re z > 0} around [c, C₁], at distance at least c/2 from it, q̂^(±1/2) = (2πi)⁻¹∮_γ z^(±1/2)(z −
q̂)⁻¹dz on W ∩ 𝒫°; this is the B-self-adjoint, positive definite square root and its inverse, as q̂ is diagonalisable
with real eigenvalues in [c, C₁] for B. For z ∈ γ, |(z − q̂)⁻¹| ≤ 2/c in the norm of B, and a derivative ∂_y^β∂_ξ^γ(z
− q̂)⁻¹ in the coordinates of a chart is a sum of products of (z − q̂)⁻¹ and derivatives of q̂, each bounded with the
weights ⟨ξ⟩^(−|γ|) of S⁰, uniformly. So q̂^(±1/2) satisfies the estimates of S⁰ on W ∩ 𝒫°, and q^(±1/2) =
w^(±1)ρ_∞^(∓k)q̂^(±1/2) those of w^(±1)S^(±k). The principal symbol of Op(φq^(1/2))*Op(φq^(1/2)) is
(φq^(1/2))^(*_B)φq^(1/2) = φ²q by (b). If q = fq′ as stated, f^(1/2)q′^(1/2) is B-self-adjoint, positive semidefinite,
and squares to q.

(g) and (h) are [[lem:iv5-calc-dual]] and [[lem:iv5-calc-reg]].

(i) The proofs are the same, with [[lem:iv5-calc-structure]] and [[lem:iv5-calc-disjoint]] for ℬ_eb, |dt dx| = r⁵ times
the eb-density of [[lem:iv5-calc-structure]] (c), and 𝒫_eb. For the calculi with scalings 1, P′ is a single point and ρ̄
is 1, so the exact sequence lowers the order without a factor h.

(j) The family (ℬ^×_h)_((b,h)∈U×(0,1]) is a parameterised scaled bounded geometry structure ((S7)), and the proofs above,
and those of [[lem:iv5-calc-disjoint]]–[[lem:iv5-calc-reg]], [[lem:iv5-calc-garding]] and [[lem:iv5-calc-q0]], apply
verbatim with countable subsets of U × (0, 1] in place of countable subsets of (0, 1]. ∎

**Lemma {#lem:iv5-calc-garding}** (A supremum bound with a margin.) (a) Let T ∈ Ψ⁰_(3b,ħ) have principal symbol
represented by t, put t_R := ½(t + t^(*_B)), and suppose that B(t_Rv, v) ≤ M B(v, v) on 𝒫° for all v, for some M ≥ 0.
Then for every η > 0 there is C such that for h ∈ (0, 1] and v ∈ L²

    Re⟨Tv, v⟩ ≤ (M + η)‖v‖² + Ch‖v‖²_(H^(−1/2)_(3b,h)).                                            {#eq:iv5-calc-garding}

(b) If w is a real weight and T ∈ w²Ψ⁰_(3b,ħ) has principal symbol w²t with t as in (a), then
Re⟨Tv, v⟩ ≤ (M + η)‖wv‖² + Ch‖wv‖²_(H^(−1/2)_(3b,h)) whenever wv ∈ L².

(c) The same holds in the eb-calculus.

The constant C depends only on M, η and on bounds for T and t in their classes; by [[prop:np-10-65-a]] (j) it is
uniform for families depending on a parameter b with such bounds uniform in b.

*Proof.* (a) The symbol M + η − t_R is B-self-adjoint and B((M + η − t_R)v, v) ≥ ηB(v, v) on 𝒫°. By
[[prop:np-10-65-a]] (f), with k = 0, w = 1, W = 𝒫 and φ = 1, θ_η := (M + η − t_R)^(1/2) ∈ S⁰, and Θ_η := Op(θ_η) is such
that Θ_η*Θ_η has principal symbol M + η − t_R. The operator ½(T + T*) has principal symbol t_R, and Op(1) = I
([[prop:np-10-65-a]] (a), (b)). So R := (M + η)I − ½(T + T*) − Θ_η*Θ_η ∈ Ψ⁰_(3b,ħ) has principal symbol 0, and
R ∈ hΨ^(−1)_(3b,ħ) ([[prop:np-10-65-a]] (b)). Pairing with v,

    (M + η)‖v‖² − Re⟨Tv, v⟩ = ‖C₀v‖² + ⟨Rv, v⟩ ≥ −Ch‖v‖²_(H^(−1/2)_(3b,h)),

by [[prop:np-10-65-a]] (d) and the bound of [[lem:ii-a-7-1]] (1), transferred as in the proof of [[lem:iv5-calc-dual]].

(b) Apply (a) to w⁻¹Tw⁻¹ ∈ Ψ⁰_(3b,ħ), which has principal symbol t by [[prop:np-10-65-a]] (b), and to wv:
⟨Tv, v⟩ = ⟨w⁻¹Tw⁻¹(wv), wv⟩, as w is real and scalar.

(c) The proof is the same ([[prop:np-10-65-a]] (i)). ∎

[[lem:iv5-calc-garding]] is a semiclassical analogue of [[lem:ii-a1-2-6]], stated for Re⟨Tv, v⟩ rather than for
‖Op(z)v‖²: the remainder of order −1 + 2δ there becomes a remainder of size O(h) here.

**Lemma {#lem:iv5-calc-q0}** (A lower bound for a non-semiclassical operator.) Let w be a real weight, and let
Q ∈ w²Diff²_3b(M₀°; ℂ⁵) be independent of h, with ⟨Qu, v⟩ = ⟨u, Qv⟩ for u, v ∈ C_c^∞(M₀°). Let 𝒪 ⊂ M₀ be open and K ⊂ 𝒪
closed, and suppose that a representative q of the principal symbol of w⁻¹Qw⁻¹, homogeneous of degree 2, satisfies
B(q(z, ζ)v, v) ≥ c|ζ|²B(v, v) for z ∈ 𝒪 ∩ M₀°, all ζ and all v, for some c > 0. Then there is C such that

    ⟨Qv, v⟩ ≥ −C‖wv‖²_(L²)   for every v with wv ∈ H¹_3b and supp v ⊂ K.                              {#eq:iv5-calc-q0}

The same holds in the eb-calculus. By [[prop:np-10-65-a]] (j), C is uniform for families depending on a parameter b,
when the coefficients are bounded and c is bounded below uniformly in b.

*Proof.* Put u := wv and Q̃ := w⁻¹Qw⁻¹ ∈ Diff²_3b. Then ⟨Qv, v⟩ = ⟨Q̃u, u⟩, Q̃ is symmetric, and its principal symbol
is represented by q, which is B-self-adjoint ([[prop:np-10-65-a]] (a), (b)). Choose φ ∈ C^∞(M₀) with 0 ≤ φ ≤ 1, φ = 1
near K and supp φ ⊂ 𝒪, and put q_* := φ²q + (1 − φ²)|ζ|², where |ζ|² denotes |ζ|² times the identity. Then q_* is
B-self-adjoint and B((q_* + 1)v, v) ≥ min(c, 1)⟨ζ⟩²B(v, v). By [[prop:np-10-65-a]] (f), (i) (non-semiclassical, with
k = 1 and W the whole compactified bundle ³ᵇT̄*M₀), θ := (q_* + 1)^(1/2) ∈ S¹ and θ⁻¹ ∈ S^(−1). Put Θ := Op(θ) and Θ′ :=
Op(θ⁻¹). By [[prop:np-10-65-a]] (b), Θ*Θ − I − Op(q_*) and Q̃ − Op(q) lie in Ψ¹_3b, and Θ′Θ − I ∈ Ψ^(−1)_3b. By
[[prop:np-10-65-a]] (a), Op(q_*) = φ²Op(q) + (1 − φ²)Op(|ζ|²). As φu = u and multiplication by a real scalar function
is symmetric for ⟨·, ·⟩, ⟨φ²Op(q)u, u⟩ = ⟨Op(q)u, u⟩ and ⟨(1 − φ²)Op(|ζ|²)u, u⟩ = 0. Hence

    ⟨Q̃u, u⟩ = ‖Θu‖² − ‖u‖² + ⟨Ru, u⟩,     R ∈ Ψ¹_3b.

Now |⟨Ru, u⟩| ≤ C₁‖u‖²_(H^(1/2)_3b) by [[prop:np-10-65-a]] (d) and [[lem:ii-a-7-1]] (1). For ε > 0,
‖u‖²_(H^(1/2)_3b) ≤ ε‖u‖²_(H¹_3b) + C_ε‖u‖², by [Hin26d, (3.14)] ([[rem:std-sbg-sobolev]]) with scalings 1, the norms
being sums of norms on ℝ⁵ of the same functions and ⟨ξ⟩ ≤ ε⟨ξ⟩² + (4ε)⁻¹. And
‖u‖_(H¹_3b) ≤ ‖Θ′Θu‖_(H¹_3b) + ‖(Θ′Θ − I)u‖_(H¹_3b) ≤ C₂(‖Θu‖ + ‖u‖), by [[prop:np-10-65-a]] (d). With ε := (4C₁C₂²)⁻¹
this gives ⟨Q̃u, u⟩ ≥ ½‖Θu‖² − C‖u‖² ≥ −C‖u‖², which is [[eq:iv5-calc-q0]]. The eb-case is the same. ∎

[[lem:iv5-calc-q0]] is applied to h-independent operators of the form h⁻²Re(□_h + CL_h*ρ_sf⁻²L_h), whose principal
symbol G + Cρ_sf⁻²ℓ² is controlled by [[lem:iv5-0-4]]; only this lower bound is used, not a factorisation of the
operator.

#### Elliptic estimates and the characteristic set at fibre infinity {#sec:iv5-1}

**Lemma {#lem:iv5-1-1}** ([Hin26a, Lemma 5.4].) The semiclassical 3b-characteristic set of ρ_sf⁻²P_h is ∂Σ ∪ o.

*Proof.* ρ_sf⁻²G and ρ_sf⁻²ℓ are homogeneous of degrees 2 and 1 on the fibres ([[lem:iv5-0-2]]), so the symbol vanishes
on o. At finite ζ ≠ 0, p(ζ) is invertible by [[lem:iv5-0-4]] ([[lem:iv4-1-causal]] (b)). At fibre infinity G is
principal and ℓ subprincipal, so the characteristic set there is ∂Σ. ∎

*Cut-offs.* With T := T_0 of [[lem:iv5-0-3]] and r̂ for the radius r₊ of [Hin26a], let χ_(τ,j)(τ) and χ_(r,j)(r),
j = 0, 1, 2, be those of [Hin26a, (5.20)]: χ_(τ,j) = 0 for τ ≤ ((j + ¼)/10)T and χ_(τ,j) = 1 for τ ≥ ((j + ¾)/10)T;
χ_(r,j) = 0 for r ≤ r_♯ + ((j + ¼)/10)(r̂ − r_♯) and χ_(r,j) = 1 for r ≥ r_♯ + ((j + ¾)/10)(r̂ − r_♯); χ′_(•,j) ≥ 0 and
(χ_(•,j)χ′_(•,j))^(1/2) ∈ C^∞. So χ_(•,j) = 1 near supp χ_(•,j+1), supp dχ_(τ,j) ⊂ τ⁻¹([0, T_0)), and
supp dχ_(r,j) ⊂ r⁻¹([r_♯, r̂)).

**Proposition {#prop:iv5-1-2}** ([Hin26a, Proposition 5.5].) Let B_0, B_1 ∈ Ψ⁰_(3b,ħ)(M^♭) with
WF′_(3b,ħ)(B_j) ∩ (o ∪ ∂Σ) = ∅ and WF′_(3b,ħ)(B_0) ⊂ Ell_(3b,ħ)(B_1). Then for all s, N there is C with

    ‖B_0χ_(τ,2)χ_(r,2)ω‖_(H^(s,(α_sf,α_K))_(3b,h))
      ≤ C(‖B_1χ_(τ,1)χ_(r,1)P_hω‖_(H^(s−2,(α_sf+2,α_K))_(3b,h)) + h^N‖χ_(τ,0)χ_(r,0)ω‖_(H^(−N,(α_sf,α_K))_(3b,h))),

and the same for P_h*.

*Proof.* Put ω′ := χ_(τ,0)χ_(r,0)ω. Then χ_(τ,1)χ_(r,1)P_hω′ = χ_(τ,1)χ_(r,1)P_hω and
χ_(τ,2)χ_(r,2)ω = χ_(τ,2)χ_(r,2)ω′. By [[lem:iv5-1-1]], ρ_sf⁻²P_h is elliptic on WF′(B_1), and B_1χ_(τ,1)χ_(r,1) is
elliptic on WF′(B_0χ_(τ,2)χ_(r,2)), as χ_(•,1) = 1 near supp χ_(•,2) ([[lem:iv5-calc-disjoint]] (b), (c)). So
[[prop:np-10-65-a]] (e), applied to ω′ with A := P_h ∈ ρ_sf²Ψ²_(3b,ħ), G := B_1χ_(τ,1)χ_(r,1) and
B := B_0χ_(τ,2)χ_(r,2), gives the estimate, in the weighted spaces and in the strong sense. For P_h* the proof is the
same, its principal symbol being G + iℓ. ∎

**Proposition {#prop:iv5-1-3}** ([Hin26a, Proposition 5.6].) Let B_0, B_1 ∈ Ψ⁰_(3b,ħ)(M^♭) be elliptic at ∂Σ over
supp(χ_(τ,0)χ_(r,0)), with WF′_(3b,ħ)(B_0) ∩ o = ∅ and WF′_(3b,ħ)(B_0) ⊂ Ell_(3b,ħ)(B_1). Then for all s, N there are
h_0 > 0 and C such that for h ∈ (0, h_0)

    ‖B_0χ_(τ,2)χ_(r,2)ω‖_(H^(s,(α_sf,α_K))_(3b,h)) ≤ C(‖B_1χ_(τ,1)χ_(r,1)P_hω‖_(H^(s−1,(α_sf+2,α_K))_(3b,h))
        + h^(1/2)‖B_1χ_(τ,0)(1 − χ_(τ,2))χ_(r,0)ω‖_(H^(s,(α_sf,α_K))_(3b,h))
        + h^N‖χ_(τ,0)χ_(r,0)ω‖_(H^(−N,(α_sf,α_K))_(3b,h))),                                              {#eq:iv5-fib}

    ‖B_0χ_(τ,2)χ_(r,2)ω‖_(H^(−s+1,(−α_sf−2,−α_K))_(3b,h)) ≤ C(‖B_1χ_(τ,1)χ_(r,1)P_h*ω‖_(H^(−s,(−α_sf,−α_K))_(3b,h))
        + h^(1/2)‖B_1χ_(τ,0)χ_(r,0)(1 − χ_(r,2))ω‖_(H^(−s+1,(−α_sf−2,−α_K))_(3b,h))
        + h^N‖χ_(τ,0)χ_(r,0)ω‖_(H^(−N,(−α_sf−2,−α_K))_(3b,h))),                                        {#eq:iv5-fib-adj}

each in the strong sense: if the right side is finite, so is the left side, and the estimate holds. These are
[Hin26a, (5.21) and (5.22)]; the first is a forward, the second a backward propagation estimate.

*Proof.* We prove [Hin26a, (5.21)] for ω ∈ H^(s,(α_sf,α_K))_(3b,h). The strong sense follows by running the same
argument with the commutant aj_ε, j_ε := ⟨εζ⟩^(−K) as in [[lem:iv5-calc-reg]] with K so large that every pairing below
is finite when the right side of [[eq:iv5-fib]] is. By [[lem:iv5-calc-reg]] (c), H_G(aj_ε) = j_εH_Ga + ϑ_εj_εae_G, so
the terms in which j_ε is differentiated are bounded multiples of a²j_ε², uniformly in ε, like the terms in which the
weights are differentiated; they join the term hAB̃_2A below and are absorbed in the same way. The estimate then holds,
by the argument below with [[prop:np-10-65-a]] (e) and the same iteration, with B_0χ_(τ,2)χ_(r,2)ω replaced by
J_εB_0χ_(τ,2)χ_(r,2)ω, J_ε := Op(j_ε), and with a constant independent of ε. As ε → 0, J_εB_0χ_(τ,2)χ_(r,2)ω tends to
B_0χ_(τ,2)χ_(r,2)ω in H^(−N,(α_sf,α_K))_(3b,h) ([[lem:iv5-calc-reg]] (b)) and is bounded in H^(s,(α_sf,α_K))_(3b,h); a
weakly convergent subsequence identifies the limit, which therefore lies in H^(s,(α_sf,α_K))_(3b,h) and satisfies the
estimate. By [[prop:iv5-1-2]] it suffices to work in an h-independent neighbourhood of ∂Σ_±;
replace ω by χ_(τ,0)χ_(r,0)ω. Let ρ̂ define fibre infinity, Ĝ := ρ̂²ρ_sf⁻²G, χ ∈ C_c^∞(ℝ) equal to 1 near 0, and χ_±
localise near ∂Σ_±. Take the commutant [Hin26a, (5.24)],

    a := ρ_sf^(−α_sf−1) ρ_K^(−α_K) ρ̂^(−s+½) χ_± χ(𝔛ρ̂) χ(𝔛Ĝ) χ_(τ,1)χ_(r,1),

and a quantisation A = A* of a ([[prop:np-10-65-a]] (c)), microsupported in a closed neighbourhood of supp a as small as
needed below. Then [Hin26a, (5.25)] holds:

    ∓Im⟨P_hω, A²ω⟩ = ⟨(±(Re L_h − Im □_h)A² ∓ (i/2)[P_h, A²])ω, ω⟩.

*The main term.* On supp a, for 𝔛 large, the covectors are close to future (for +), resp. past (for −) lightlike
covectors. c is past timelike ([[lem:iv5-0-5]] (1)), so [[lem:iv5-0-4]] ([[lem:iv4-1-causal]] (d)) makes ±ρ_sf⁻²ℓ
positive definite there, with a lower bound fixed by compactness. Im □_h ∈ h Diff¹_(3b,ħ) is semiclassically
subprincipal, □_h having real scalar principal symbol. With the square roots of [[prop:np-10-65-a]] (f) and the rules of
[[prop:np-10-65-a]] (b), this gives [Hin26a, (5.26)], with E microsupported near supp a ([[lem:iv5-calc-disjoint]] (b)):
±(Re L_h − Im □_h)A² = A(B̃_0*B̃_0 + c_0Λ*Λ)A + hE.

*The commutator and the cut-offs.* ∓(i/2)[P_h, A²] has principal symbol ∓aH_Ga at order h ([Hin26a, (5.27)]). In
[Hin26a, (5.29)] it is split as follows. Differentiation of χ_± and of χ(𝔛Ĝ) lands off the characteristic set, so these
terms are hAQP_h. Differentiation of χ(𝔛ρ̂) gives order −∞. Differentiation of the weights gives bounded multiples of
a², the term hAB̃_2A. Next, ∓χ_(τ,1)H_Gχ_(τ,1) = ∓χ_(τ,1)χ′_(τ,1)H_Gτ = −e_T², because H_Gτ = 2g⁻¹(ζ, dτ) is positive
at future and negative at past lightlike ζ over supp dχ_(τ,1) ⊂ τ⁻¹([0, T_0)), where dτ is past timelike
([[lem:iv5-0-3]] (b)). Finally ∓χ_(r,1)H_Gχ_(r,1) = +e_R², because H_Gr = 2g⁻¹(ζ, dr) is negative at future and
positive at past lightlike ζ over supp dχ_(r,1) ⊂ r⁻¹([r_♯, r̂)), where dr is future timelike ([[lem:iv5-0-3]] (c)).

*Conclusion.* Let Λ⁻ be a microlocal parametrix of Λ* near supp a. By [Hin26a, (5.25)–(5.26)] and the split of the
commutator, with ∓Im⟨P_hω, A²ω⟩ ≤ (4c_0)⁻¹‖Λ⁻AP_hω‖² + c_0‖ΛAω‖² + h^(2N)‖ω‖²_(H^(−N,(α_sf,α_K))_(3b,h)), the terms
c_0‖ΛAω‖² cancel and

    ‖B̃_0Aω‖² + h‖E_Rω‖² ≤ (4c_0)⁻¹‖Λ⁻AP_hω‖² + h‖E_Tω‖² + h|⟨B̃_2Aω, Aω⟩| + h|⟨(E + F)ω, ω⟩|
                             + h|⟨AQP_hω, ω⟩| + Ch^(2N)‖ω‖²_(H^(−N,(α_sf,α_K))_(3b,h))

([Hin26a, (5.30)]), F collecting the remainders of the split, microsupported near supp a; the term with Q is bounded by
the elliptic estimate, WF′(Q) lying off the characteristic set. Drop ‖E_Rω‖², which has the sign
of the main term, and absorb h⟨B̃_2Aω, Aω⟩ ≤ Ch‖B̃_0Aω‖² + h^N‖ω‖², which holds by [[prop:np-10-65-a]] (e), B̃_0 being
elliptic on a neighbourhood of supp a in which A is microsupported. Iterate in h^(1/2) on the error term
h^(1/2)‖B̃′_0ω‖, whose wave front set lies near supp a. This proves [Hin26a, (5.21)]; the a priori term is h^(1/2)‖E_Tω‖,
supported over supp dχ_(τ,1).

For [Hin26a, (5.22)], P_h* = □_h* + iL_h* with □_h* − □_h ∈ hDiff¹ and L_h* − L_h ∈ hDiff⁰, and the pairing is now
∓Im⟨P_h*ω, A²ω⟩ = ⟨(∓(Re L_h − Im □_h)A² ∓ (i/2)[P_h*, A²])ω, ω⟩ ([Hin26a, (5.28)]), whose main term has the symbol
∓ρ_sf⁻²ℓ, now negative definite. The weights in a become (−α_sf − 2, −α_K). The split of the commutator holds for P_h*,
as only □_h*, with principal symbol G, entered it. Now −e_T² has the sign of the main term and e_R² needs the a priori
term. ∎

#### The saddle point at r = r_c {#sec:iv5-2}

By [[lem:iv5-0-4]] there is C with C(ρ_sf⁻²ℓ)² + ρ_sf⁻²G > 0 on ³ᵇT*_Ω M^♭ ∖ o. As in [Hin26a, (5.31)–(5.32)], define

    𝓛_h := −i(1 + iCL_h*ρ_sf⁻²)P_h = −L_h + J − iQ ∈ ρ_sf²Diff³_(3b,ħ),                                     {#eq:iv5-2-1}

with J = h²J_0 + h³J_1, J_0 = Im □_g, J_1 = Ch⁻³Re(L_h*ρ_sf⁻²□_h), Q = h²Q_0 + h³Q_1,
Q_0 = h⁻²Re(□_h + CL_h*ρ_sf⁻²L_h) and Q_1 = −Ch⁻³Im(L_h*ρ_sf⁻²□_h). The memberships J_0 ∈ ρ²Diff¹_3b,
J_1 ∈ ρ²Diff³_3b, Q_0 ∈ ρ²Diff²_3b and Q_1 ∈ ρ²Diff²_3b follow from [[lem:iv5-0-2]] (d) and the self-adjointness of ℓ.
1 + iCL_h*ρ_sf⁻² is semiclassically elliptic everywhere, its principal symbol 1 + iCρ⁻²ℓ being invertible (ℓ
self-adjoint). The symbol j of J is homogeneous of degree 3 and vanishes cubically at o. Near (K⁺)°, ρ_K := t⁻¹, and the
weight at 𝗌𝖿 and the differential order are dropped.

*Commutants near o.* A *cut-off* below is a smooth function χ of one variable with values in [0, 1], equal to 1 on a
closed interval J, positive on a larger interval I that is open in the range of the variable, and 0 outside I,
non-decreasing to the left of J and non-increasing to its right, such that (χχ′)^(1/2) is smooth to the left of J and
(−χχ′)^(1/2) to its right; "supported in I" refers to this I. Such cut-offs exist: with φ(x) := e^(−1/x) for x > 0
and φ(x) := 0 for x ≤ 0, the function χ(x) := φ(β − x)/(φ(β − x) + φ(x − α)), α < β, is equal to 1 on (−∞, α],
positive on (−∞, β) and 0 on [β, ∞), and near α and near β the function −χχ′ is the square of a smooth positive
function times φ(x − α)^(1/2)(x − α)⁻¹, resp. φ(β − x)(β − x)⁻¹; cut-offs equal to 1 on a bounded J are products of
two such functions, one of them reflected. Also χ₁(x) := e^(−𝔛/x) for x > 0, χ₁(x) := 0 for x ≤ 0, is used, with
χ₁′ = 𝔛x⁻²χ₁ and (χ₁χ₁′)^(1/2) = 𝔛^(1/2)x⁻¹χ₁ smooth. Every commutant in [[sec:iv5-2]]–[[sec:iv5-5]] has the form

    a = w⁻¹φ_1⋯φ_mχ_0(𝔛|ζ|),                                                                                {#eq:iv5-2-a}

with w a positive function (a product of powers of boundary defining functions), each φ_k a cut-off or χ₁, composed
with a function on M^♭, 𝔛 ≥ 1, and χ_0 a cut-off equal to 1 on [0, 1] and supported in [0, 2); we put
a_k := w⁻¹χ_0(𝔛|ζ|)Π_(k′≠k) φ_(k′). The square roots of the symbols below are smooth: each is taken of a product of
a factor ±φ_kφ_k′ ≥ 0 (or χ₁′/χ₁ times a²), whose square root is smooth on the support in question, with a B-self-adjoint
factor that is positive definite there. In [[prop:iv5-5-3]] (2) the factor called f is one of the φ_k, not the symbol f
of [[lem:iv5-2-symbols]]. The commutants on M in [[sec:iv6-2]] have the same form, with functions on M, and
[[lem:iv5-2-symbols]] and its proof hold for them unchanged.

**Lemma {#lem:iv5-2-symbols}** (The commutator symbol of a product commutant; the form of [Hin26a, (5.39)–(5.43)].) For
a as in [[eq:iv5-2-a]] and either choice of sign,

    aH_(−ℓ+j)a ∓ Sa² = −a²(±S − ℓ(dw/w) − wH_j(w⁻¹)) + Σ_k a_k²φ_k(−ℓ(dφ_k) + H_jφ_k) + f,
    f := w⁻²(φ_1⋯φ_m)²χ_0(𝔛|ζ|)H_(−ℓ+j)(χ_0(𝔛|ζ|)),                                                   {#eq:iv5-2-leibniz}

and f is supported in supp a ∩ {1 ≤ 𝔛|ζ| ≤ 2}, off o.

*Proof.* H_(−ℓ+j), the Hamilton vector field of the End-valued symbol −ℓ + j, acts on scalar symbols as a derivation:
H(uv) = uHv + vHu. For a function φ on M^♭, H_(−ℓ)φ = −ℓ(dφ), ℓ being linear in the fibre; so
wH_(−ℓ+j)(w⁻¹) = w⁻¹ℓ(dw) + wH_j(w⁻¹) = ℓ(dw/w) + wH_j(w⁻¹). The Leibniz rule for the m + 2 factors of a gives
H_(−ℓ+j)a = a·wH_(−ℓ+j)(w⁻¹) + Σ_k a_kH_(−ℓ+j)φ_k + w⁻¹φ_1⋯φ_mH_(−ℓ+j)(χ_0(𝔛|ζ|)); multiplying by a and using
a·a_k = a_k²φ_k gives [[eq:iv5-2-leibniz]]. The support of f is that of χ_0′(𝔛|ζ|) within supp a. ∎

**Proposition {#prop:iv5-2-1}** ([Hin26a, Proposition 5.8].) Near K⁺ let ρ_K := t⁻¹; the weight at 𝗌𝖿 and the
differential order play no role here and are dropped. Put ε_c := r_ce^(1/2)/v. There is δ > 0 such that, with
K := {|r − r_c| ≤ (3/2)ε_c, ρ_K ≤ 4δ}, the following holds for every χ ∈ C^∞(M^♭) equal to 1 on K and supported in a
small neighbourhood of K, all B_0, B_1, E ∈ Ψ_(3b,ħ)(M^♭) with compact operator wave front sets and Schwartz kernels
supported in K × K, and all sufficiently small h > 0.

(1) If WF′(B_0) ⊂ {|r − r_c| ≤ (55/50)ε_c, ρ_K ≤ 2δ, |ζ| < 1}, Ell(E) ⊃ {|r − r_c| ≤ (60/50)ε_c, δ ≤ ρ_K ≤ 3δ, |ζ| < 1}
and Ell(B_1) ⊃ {|r − r_c| ≤ (60/50)ε_c, ρ_K ≤ 3δ, |ζ| < 2}, then for every N there is C with

    ‖B_0ω‖_(ρ_K^(α_K)L²) ≤ C(h⁻¹‖B_1P_hω‖_(ρ_K^(α_K)L²) + ‖Eω‖_(ρ_K^(α_K)L²) + h^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h))).

(2) If B_0, B_1 are as in (1) and Ell(E) ⊃ {|r − r_c| ∈ [(55/50)ε_c, (60/50)ε_c], ρ_K ≤ 2δ, |ζ| < 1}, then

    ‖B_0ω‖_(ρ_K^(−α_K)L²) ≤ C(h⁻¹‖B_1P_h*ω‖_(ρ_K^(−α_K)L²) + ‖Eω‖_(ρ_K^(−α_K)L²) + h^N‖χω‖_(ρ_K^(−α_K)H^(−N)_(3b,h))).

These are [Hin26a, (5.33) and (5.34)] with r_c for r_0; (1) propagates control forward into the saddle, (2) backward
out of it.

*Proof.* (1) By [[prop:iv5-1-2]] and the ellipticity of 1 + iCL_h*ρ_sf⁻² it suffices to prove [Hin26a, (5.33)] with 𝓛_h
for P_h, near o. Let χ_K be a cut-off equal to 1 on [0, 1] and supported in [0, 3), and ψ = ψ(r) a cut-off equal to 1
on {|r − r_c| ≤ (55/50)ε_c} and supported in {|r − r_c| < (60/50)ε_c} ([Hin26a, (5.35)]). Take the commutant
a = ρ_K^(−α_K)ψ(r)χ_K(𝔛ρ_K)χ_0(𝔛|ζ|), and A = A* a quantisation of a as in [[prop:np-10-65-a]] (c), with Schwartz kernel
supported in K × K. The pairing is [Hin26a, (5.37)–(5.38)]:

    h⁻¹Im⟨𝓛_hω, A²ω⟩ = ⟨𝒞ω, ω⟩,     𝒞 = ((i/(2h))[−L_h + J, A²] − h⁻¹(Im L_h)A²) − h⁻¹AQA − (1/(2h))[A, [A, Q]].

The bracket has principal symbol aH_(−ℓ+j)a − Sa². As ℓ is linear in the fibre, H_(−ℓ)f = −ℓ(df) for a function f on
M^♭. So [[lem:iv5-2-symbols]], with w = ρ_K^(α_K), φ_1 = ψ(r) and φ_2 = χ_K(𝔛ρ_K), gives
aH_(−ℓ+j)a − Sa² = −c_0a² − b_0² − b_R² + e² + f ([Hin26a, (5.39)]), with f as there and, as ρ_K⁻¹ = t and
dρ_K/ρ_K² = −dt, so that ℓ(dw/w) = −α_Kρ_Kℓ(dt) and wH_j(w⁻¹) = α_Kρ_KH_jt,

    b_0 := a(S − c_0 + α_Kρ_K(ℓ(dt) − H_jt))^(1/2),     b_R := ρ_K^(−α_K)χ_Kχ_0(ψψ′(ℓ(dr) − H_jr))^(1/2),
    e := ρ_K^(−α_K)ψχ_0ρ_K(−𝔛χ_Kχ_K′)^(1/2)(ℓ(−dt) + H_jt)^(1/2),

χ_K and χ_K′ being evaluated at 𝔛ρ_K, χ_0 at 𝔛|ζ|. H_jt and H_jr are O(|ζ|²), j vanishing cubically at o. Their square
roots exist for the following reasons.

- b_0: S is positive definite on {|r − r_c| ≤ (6/5)r_c e^(1/2)/v} ([[lem:iv5-0-5]] (3)), so S ≥ 2c_0 there;
ℓ(dρ_K/ρ_K²) = −ℓ(dt) and H_jρ_K⁻¹ are bounded on supp χ_0(𝔛|ζ|) and carry the factor ρ_K ≲ 𝔛⁻¹.

- b_R: on supp ψ′ ∩ {±(r − r_c) > 0}, −ℓ(±dr) ≥ 2c₁ ([[lem:iv5-0-5]] (6)), and |H_jr| = O(|ζ|²) < c₁ on
supp χ_0(𝔛|ζ|) for 𝔛 large.

- e: dρ_K/ρ_K² = −dt is future timelike ([[lem:iv5-0-3]] (d)), so ℓ(−dt) is positive definite ([[lem:iv5-0-4]]), and
−χ_Kχ′_K ≥ 0; e is supported away from ρ_K = 0.

- f is supported off o, where [[prop:iv5-1-2]] applies.

For Q, write −h⁻¹⟨AQAω, ω⟩ = −h⟨Q_0Aω, Aω⟩ − ⟨h²Q_1Aω, Aω⟩, A being self-adjoint.

*The term with Q_0* ([Hin26a, (5.44)]). Q_0 ∈ ρ_sf²Diff²_3b is independent of h and symmetric, and its principal symbol
G + Cρ_sf⁻²ℓ² satisfies B(ρ_sf⁻²(G + Cρ_sf⁻²ℓ²)v, v) ≥ c|ζ|²B(v, v) over a neighbourhood of Ω, by [[lem:iv5-0-4]] and
continuity from Ω; near K, ρ_sf lies between two positive constants. As the Schwartz kernel of A lies in K × K,
[[lem:iv5-calc-q0]], with w = 1, gives −h⟨Q_0Aω, Aω⟩ ≤ Ch‖Aω‖².

*The term with Q_1* ([Hin26a, (5.45)]). T := h²Q_1 ∈ ρ_sf²Ψ²_(3b,ħ) is self-adjoint, and its principal symbol q₁₀ is the
principal symbol of Q_1 evaluated at ζ, homogeneous of degree 2 ([[prop:np-10-65-a]] (a)). So |q₁₀(z, ζ)| ≤ C₂|ζ|² over
a fixed neighbourhood V of K, where C₂ is the supremum of |q₁₀| over the unit sphere bundle above V, independent of 𝔛.
Let ã := χ̃(𝔛|ζ|)φ(z), with χ̃ ∈ C_c^∞((−3, 3)), 0 ≤ χ̃ ≤ 1, χ̃ = 1 on [−5/2, 5/2], and φ ∈ C^∞(M₀), 0 ≤ φ ≤ 1, equal to
1 near K and supported in V; put Ã := Op(ã). As χ_0 is supported in (−2, 2), A may be taken microsupported in a closed
set near which ã = 1; then (I − Ã)A = Op(1 − ã)A lies in h^∞Ψ^(−∞)_(3b,ħ) ([[def:iv5-calc-micro]]). The self-adjoint
operator Ã*TÃ has principal symbol ã²q₁₀, and |ã²q₁₀| ≤ 9C₂𝔛⁻² everywhere. [[lem:iv5-calc-garding]] (a), applied with
η := 𝔛⁻² to Ã*TÃ and to −Ã*TÃ, gives |⟨Ã*TÃAω, Aω⟩| ≤ ((9C₂ + 1)𝔛⁻² + C_𝔛h)‖Aω‖². The difference
⟨TAω, Aω⟩ − ⟨Ã*TÃAω, Aω⟩ is a sum of three terms, each containing (I − Ã)Aω = (I − Ã)Aχω, whose norm in every H^k_(3b,h)
is O(h^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h))) ([[prop:np-10-65-a]] (d)); so it is at most
𝔛⁻²‖Aω‖² + C_(𝔛,N)h^(2N)‖χω‖²_(ρ_K^(α_K)H^(−N)_(3b,h)). Hence

    |Re h⁻¹⟨Ah³Q_1Aω, ω⟩| ≤ ((9C₂ + 2)𝔛⁻² + C_𝔛h)‖Aω‖² + C_(𝔛,N)h^(2N)‖χω‖²_(ρ_K^(α_K)H^(−N)_(3b,h)),

which is [Hin26a, (5.45)] with 9C₂ + 2 for 2C and an additional term of the form of the last term in (1).

*The double commutator* (1/(2h))[A, [A, Q]] lies in hΨ_(3b,ħ), the principal symbol of A being scalar
([[prop:np-10-65-a]] (b)), and gives [Hin26a, (5.46)].

Collecting, the Q-terms add at most (9C₂ + 2)𝔛⁻² + C′_𝔛h to the coefficient −c_0 of ‖Aω‖², where C₂ does not depend
on 𝔛 and C′_𝔛 does not depend on h: fix 𝔛 large
and then h small to absorb ‖Aω‖². Let B_0, B_R, E and F be quantisations of b_0, b_R, e and f, and
B̃_0 ∈ Ψ_(3b,ħ) elliptic on a neighbourhood of supp a in which A is microsupported. The pairing, the symbol
identity and the bound |h⁻¹⟨A𝓛_hω, Aω⟩| ≤ ¼c_0‖Aω‖² + c_0⁻¹h⁻²‖A𝓛_hω‖² give

    c_0‖Aω‖² + ‖B_0ω‖² + ‖B_Rω‖²
        ≤ C(h⁻²‖A𝓛_hω‖² + ‖Eω‖² + |⟨Fω, ω⟩| + h‖B̃_0ω‖² + h^(2N)‖χω‖²_(ρ_K^(α_K)H^(−N)_(3b,h))),

the term h‖B̃_0ω‖² collecting the remainders of the symbol calculus ([Hin26a, (5.47)]). As WF′(F) lies off o and in
Ell(𝓛_h), [[prop:np-10-65-a]] (e) gives |⟨Fω, ω⟩| ≤ C(‖B̃_0𝓛_hω‖² + h^(2N)‖χω‖²_(ρ_K^(α_K)H^(−N)_(3b,h))). Dropping
‖B_Rω‖²,

    ‖B_0ω‖ ≤ C(h⁻¹‖B̃_0𝓛_hω‖ + ‖Eω‖ + h^(1/2)‖B̃_0ω‖ + h^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h)))                 {#eq:iv5-2-iter}

([Hin26a, (5.48)]). The positivity used holds, by continuity, for commutants whose supports are larger by a fixed small
amount; so the same argument bounds h^(1/2)‖B̃_0ω‖ by h^(1/2) times the right side with B̃_0 replaced by an operator
B̃_1 of the same kind, and after 2N such steps the remaining term is h^N‖B̃_(2N)ω‖, which is at most
Ch^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h)), B̃_(2N) being microsupported in a compact set at finite frequencies. On the operator
wave front set of the B_0 of the statement, b_0 is elliptic where the fibre variable has length at most 𝔛⁻¹, and
[[prop:iv5-1-2]] applies where it has length at least 𝔛⁻¹. The quantisation of e is bounded by the E of the statement,
whose elliptic set contains supp e, and B̃_0𝓛_hω by B_1P_hω, B̃_0 being microsupported in Ell(B_1), each up to
h^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h)). This gives [Hin26a, (5.33)], with δ := 𝔛⁻¹.

(2) Replace P_h* by 𝓛_h* = iP_h*(1 − iCρ_sf⁻²L_h) = −L_h* + J + iQ and take
a = ρ_K^(α_K)ψχ_K(𝔛ρ_K)χ_0(𝔛|ζ|). As J and Q are self-adjoint and Im(−L_h*) = Im L_h = hS, the pairing is

    h⁻¹Im⟨𝓛_h*ω, A²ω⟩ = ⟨𝒞′ω, ω⟩,     𝒞′ = ((i/(2h))[−L_h* + J, A²] + h⁻¹(Im L_h)A²) + h⁻¹AQA + (1/(2h))[A, [A, Q]]
                                                                                                          {#eq:iv5-2-adj}

([Hin26a, (5.49)–(5.50)]), and the bracket has principal symbol aH_(−ℓ+j)a + Sa². By [[lem:iv5-2-symbols]] with
w = ρ_K^(−α_K), the main bracket S + ℓ(dw/w) + wH_j(w⁻¹) is again S + α_Kρ_K(ℓ(dt) − H_jt), and
aH_(−ℓ+j)a + Sa² = c_0a² + b_0² + b_K² − e² + f, where b_0, b_K and e are the b_0, e and b_R of (1) with ρ_K^(α_K) for
ρ_K^(−α_K). The same three facts give the square roots, now with b_K from the sign of −ℓ(dt) and e from
[[lem:iv5-0-5]] (6) on supp ψ′. Q enters with a lower bound, the adjoint pairing containing +h⁻¹⟨AQAω, ω⟩:
h⟨Q_0Aω, Aω⟩ ≥ −Ch‖Aω‖² by [[lem:iv5-calc-q0]], and ⟨h²Q_1Aω, Aω⟩ ≥ −((9C₂ + 2)𝔛⁻² + C_𝔛h)‖Aω‖² − C_(𝔛,N)h^(2N)‖χω‖² as
in (1), by [[lem:iv5-calc-garding]] applied to −Ã*h²Q_1Ã. The iteration is the same. ∎

#### The saddle point at the corner ∂K⁺ {#sec:iv5-3}

From here on, ρ_K = r/t and ρ_sf = 1/r.

**Proposition {#prop:iv5-3-1}** ([Hin26a, Proposition 5.9].) Let (α_sf, α_K) and δ_r be those of [[lem:iv5-0-5]].
There is δ ∈ (0, δ_r] such that, with K := {ρ_K ≤ 3δ_r, ρ_sf ≤ 3δ}, the following holds for χ, B_0, B_1 and E as in
[[prop:iv5-2-1]] with this K, and all sufficiently small h > 0.

(1) If WF′(B_0) ⊂ {ρ_K ≤ (3/2)δ_r, ρ_sf ≤ (3/2)δ, |ζ| < 1}, Ell(E) ⊃ {ρ_K ≤ 2δ_r, (5/4)δ ≤ ρ_sf ≤ 2δ, |ζ| < 1} and
Ell(B_1) ⊃ {ρ_K ≤ 2δ_r, ρ_sf ≤ 2δ, |ζ| < 2}, then for every N there is C with

    ‖B_0ω‖_(ρ_sf^(α_sf)ρ_K^(α_K)L²) ≤ C(h⁻¹‖B_1P_hω‖_(ρ_sf^(α_sf+2)ρ_K^(α_K)L²) + ‖Eω‖_(ρ_sf^(α_sf)ρ_K^(α_K)L²)
        + h^N‖χω‖_(H^(−N,(α_sf,α_K))_(3b,h))).

(2) If B_0, B_1 are as in (1) and Ell(E) ⊃ {(5/4)δ_r ≤ ρ_K ≤ 2δ_r, ρ_sf ≤ 2δ, |ζ| < 1}, then

    ‖B_0ω‖_(ρ_sf^(−α_sf−2)ρ_K^(−α_K)L²) ≤ C(h⁻¹‖B_1P_h*ω‖_(ρ_sf^(−α_sf)ρ_K^(−α_K)L²)
        + ‖Eω‖_(ρ_sf^(−α_sf−2)ρ_K^(−α_K)L²) + h^N‖χω‖_(H^(−N,(−α_sf−2,−α_K))_(3b,h))).

These are [Hin26a, (5.51) and (5.52)].

*Proof.* (1) Replace P_h by 𝓛_h. Let χ_sf be a cut-off equal to 1 on [0, 5/4] and supported in [0, 2), and χ_K a
cut-off equal to 1 on [0, (5/4)δ_r] and supported in [0, 2δ_r). Take the commutant ([Hin26a, (5.53)])
a = w⁻¹χ_sf(𝔛ρ_sf)χ_K(ρ_K)χ_0(𝔛|ζ|). Then 𝒞 ∈ ρ_sf^(−2α_sf)ρ_K^(−2α_K)Ψ_3b, and [[lem:iv5-2-symbols]] gives
aH_(−ℓ+j)a − Sa² = −c_0ρ_sf²a² − b_0² − b_sf² + e² + f ([Hin26a, (5.54)]), with f as there and, as dρ_sf = −ρ_sf²dr,

    b_0 := a(S − ℓ(dw/w) − wH_j(w⁻¹) − c_0ρ_sf²)^(1/2),     b_sf := w⁻¹χ_sfχ_0(−χ_Kχ_K′)^(1/2)(−ℓ(dρ_K) + H_jρ_K)^(1/2),
    e := w⁻¹χ_Kχ_0ρ_sf(−𝔛χ_sfχ_sf′)^(1/2)(−ℓ(dr) + H_jr)^(1/2),

χ_sf and χ_sf′ being evaluated at 𝔛ρ_sf, χ_K and χ_K′ at ρ_K. Their square roots exist for the following reasons.

- b_0: ρ_sf⁻²(−ℓ(dw/w) + S) is positive definite on {ρ_sf ≤ 2δ_r, ρ_K ≤ 2δ_r} ([[lem:iv5-0-5]] (4)), with a fixed lower
bound; ρ_sf⁻²w⁻¹H_jw vanishes at o, since ρ_sf⁻²j vanishes cubically there.

- b_sf: on supp χ′_K, ρ_K ∈ [(5/4)δ_r, 2δ_r) ⊂ [δ_r, v(1 − δ_sf)], as δ_r < 1/5, and [[lem:iv5-0-5]] (6) on
𝗌𝖿 ∩ {r/t ∈ [δ_r, v(1 − δ_sf)]} gives
ρ_sf⁻²(−ℓ(dρ_K)) > 0 near 𝗌𝖿 for 𝔛 large.

- e: dρ_sf/ρ_sf² = −dr, and −ℓ(dr) is positive definite for r ≥ r_c + r_c e^(1/2)/v ([[lem:iv5-0-5]] (6)); H_jr
vanishes at o.

e is supported away from 𝗌𝖿 and gives the a priori term. Estimating the left side by
c_0⁻¹h⁻²‖ρ_sf⁻¹A𝓛_hω‖² + ¼c_0‖ρ_sfAω‖² produces the weights of [Hin26a, (5.51)]. The Q-terms are estimated as in the
proof of [[prop:iv5-2-1]], with the weight ρ_sf: [[lem:iv5-calc-q0]] applies to Q_0 with w = ρ_sf, as
ρ_sf⁻²(G + Cρ_sf⁻²ℓ²) = ρ_sf⁻²G + C(ρ_sf⁻²ℓ)² is positive definite over Ω ([[lem:iv5-0-4]]), and
[[lem:iv5-calc-garding]] (b) applies to Ã*h²Q_1Ã ∈ ρ_sf²Ψ⁰_(3b,ħ), with C₂ the supremum of |ρ_sf⁻²q₁₀| over the unit
sphere bundle above a neighbourhood of K; so ‖Aω‖ is replaced by ‖ρ_sfAω‖ in these bounds. The rest is the proof of
[[prop:iv5-2-1]], with δ := 𝔛⁻¹.

(2) Take a = wχ_sf(𝔛ρ_sf)χ_K(ρ_K)χ_0(𝔛|ζ|) and the pairing with 𝓛_h*. Then
aH_(−ℓ+j)a + Sa² = c_0ρ_sf²a² + b_0² + b_K² − e² + f by [[lem:iv5-2-symbols]] with w⁻¹ in place of w, where b_0, b_K
and e are the b_0, e and b_sf of (1) with the prefactor w in place of w⁻¹: the main bracket S + ℓ(d(w⁻¹)/w⁻¹) + w⁻¹H_jw
is again S − ℓ(dw/w) − wH_j(w⁻¹). b_0 comes from [[lem:iv5-0-5]] (4), and the a priori term from supp χ′_K. ∎

#### The sink in 𝗌𝖿° {#sec:iv5-4}

**Proposition {#prop:iv5-4-1}** ([Hin26a, Proposition 5.11].) Let α_sf, δ_r and δ_sf be those of [[lem:iv5-0-5]];
the weight at K⁺ and the differential order are dropped, and s := r/t. There is δ ∈ (0, δ_r] such that, with
K := {|s/v − 1| ≤ 3δ_sf, ρ_sf ≤ 3δ}, the following holds for χ, B_0, B_1 and E as in [[prop:iv5-2-1]] with this K,
and all sufficiently small h > 0.

(1) If WF′(B_0) ⊂ {|s/v − 1| ≤ (3/2)δ_sf, ρ_sf ≤ (3/2)δ, |ζ| < 1}, Ell(B_1) ⊃ {|s/v − 1| ≤ 2δ_sf, ρ_sf ≤ 2δ, |ζ| < 2} and
Ell(E) ⊃ {|s/v − 1| ≤ 2δ_sf, ρ_sf ≤ 2δ, |ζ| < 1} ∖ {|s/v − 1| ≤ (5/4)δ_sf, ρ_sf ≤ (5/4)δ}, then for
every N there is C with

    ‖B_0ω‖_(ρ_sf^(α_sf)L²) ≤ C(h⁻¹‖B_1P_hω‖_(ρ_sf^(α_sf+2)L²) + ‖Eω‖_(ρ_sf^(α_sf)L²)
        + h^N‖χω‖_(ρ_sf^(α_sf)H^(−N)_(3b,h))).

(2) If B_0, B_1 are as in (1), then

    ‖B_0ω‖_(ρ_sf^(−α_sf−2)L²) ≤ C(h⁻¹‖B_1P_h*ω‖_(ρ_sf^(−α_sf)L²) + h^N‖χω‖_(ρ_sf^(−α_sf−2)H^(−N)_(3b,h))).

These are [Hin26a, (5.55) and (5.56)], with the weight w′ = ρ_sf^(α_sf+1) in the commutant.

*Proof.* (1) The commutant is a = (w′)⁻¹χ_sf(𝔛ρ_sf)χ_R((r/t)/v − 1)χ_0(𝔛|ζ|), with χ_sf as in [[prop:iv5-3-1]] and
χ_R a cut-off supported in (−2δ_sf, 2δ_sf) and equal to 1 on [−(5/4)δ_sf, (5/4)δ_sf]. With s := r/t,
[[lem:iv5-2-symbols]] gives aH_(−ℓ+j)a − Sa² = −c_0ρ_sf²a² − b_0² + e₁² + e₂² + f ([Hin26a, (5.57)]), with f as there,

    b_0 := a(S − ℓ(dw′/w′) − w′H_j((w′)⁻¹) − c_0ρ_sf²)^(1/2),
    e₁ := (w′)⁻¹χ_Rχ_0ρ_sf(−𝔛χ_sfχ_sf′)^(1/2)(−ℓ(dr) + H_jr)^(1/2),
    e₂ := (w′)⁻¹χ_sfχ_0(v⁻¹χ_Rχ_R′(−ℓ(ds) + H_js))^(1/2),

χ_R and χ_R′ being evaluated at s/v − 1. Their square roots exist for the following reasons.

- b_0: [[lem:iv5-0-5]] (5), for 𝔛 large.

- e₁: dρ_sf/ρ_sf² = −dr, H_j(ρ_sf⁻¹) = H_jr, and [[lem:iv5-0-5]] (6) for large r.

- e₂: on supp dχ_R, |(r/t)/v − 1| ∈ [(5/4)δ_sf, 2δ_sf], where the sign of −r²ℓ(d(r/t)) is that of χ′_R
([[lem:iv5-0-5]] (6) on the two sides of the sink).

e₁ and e₂ are supported away from {|(r/t)/v − 1| ≤ δ_sf, ρ_sf ≤ 𝔛⁻¹} and give ‖Eω‖. The rest is the proof of
[[prop:iv5-2-1]], with the weighted Q-terms of [[prop:iv5-3-1]].

(2) Take a = w′χ_sf(𝔛ρ_sf)χ_R((r/t)/v − 1)χ_0(𝔛|ζ|). Then [[lem:iv5-2-symbols]] gives
aH_(−ℓ+j)a + Sa² = c_0ρ_sf²a² + b_0² + b₁² + b₂² + f, with b_0 as in (1) and b₁, b₂ the e₁, e₂ of (1) with the prefactor
w′ in place of (w′)⁻¹. Every
term except f, which is elliptic, has the sign of the main term, by the same three facts. So [Hin26a, (5.56)] carries no
a priori term. ∎

#### Propagation between the critical sets {#sec:iv5-5}

**Proposition {#prop:iv5-5-1}** ([Hin26a, Proposition 5.12].) Near K⁺ let ρ_K := t⁻¹; the weight at 𝗌𝖿 and the
differential order are dropped. Let r_3 := r_c − (52/50)r_c e^(1/2)/v and r_4 := r_c − (51/50)r_c e^(1/2)/v, and fix
0 < t_1 < t_2 < t_3 and r_♯ < r_1 < r_2 < r_3. Let B_0, B_1, E ∈ Ψ_(3b,ħ)(M^♭) have compact operator wave front sets
and Schwartz kernels supported in K × K, K a compact subset of {r_♯ < r < r_c, ρ_K < ∞}, and let χ ∈ C^∞(M^♭) equal 1
on K.

(1) If WF′(B_0) ⊂ {ρ_K ≤ t_2⁻¹, r_1 < r < r_4, |ζ| < 1}, Ell(B_1) ⊃ {ρ_K ≤ t_1⁻¹, r_1 ≤ r ≤ r_4, |ζ| < 2} and
Ell(E) ⊃ {t_3⁻¹ ≤ ρ_K ≤ t_1⁻¹, r_1 ≤ r ≤ r_4, |ζ| < 1} ∪ {ρ_K ≤ t_1⁻¹, r_3 ≤ r ≤ r_4, |ζ| < 1}, then for every N
there is C with, for all sufficiently small h > 0,

    ‖B_0ω‖_(ρ_K^(α_K)L²) ≤ C(h⁻¹‖B_1P_hω‖_(ρ_K^(α_K)L²) + ‖Eω‖_(ρ_K^(α_K)L²) + h^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h))).

(2) If B_0, B_1 are as in (1) and Ell(E) ⊃ {ρ_K ≤ t_1⁻¹, r_1 ≤ r ≤ r_2, |ζ| < 1}, then

    ‖B_0ω‖_(ρ_K^(−α_K)L²) ≤ C(h⁻¹‖B_1P_h*ω‖_(ρ_K^(−α_K)L²) + ‖Eω‖_(ρ_K^(−α_K)L²) + h^N‖χω‖_(ρ_K^(−α_K)H^(−N)_(3b,h))).

These are [Hin26a, (5.58) and (5.59)]: (1) propagates control from the saddle towards the inner boundary, (2) from
the inner boundary towards the saddle.

*Proof.* (1) The commutant is a = ρ_K^(−α_K)χ₁(r − r_1)χ₂(r)χ_K(ρ_K)χ_0(𝔛|ζ|), where χ₁(x) = e^(−𝔛/x) for x > 0, so
χ₁′(x) = 𝔛x⁻²χ₁(x), χ₂ is a cut-off equal to 1 on (−∞, r_3] and supported in (−∞, r_4), and χ_K a cut-off equal to 1
on [0, t_3⁻¹] and supported in [0, t_1⁻¹). Then [[lem:iv5-2-symbols]] with w = ρ_K^(α_K), as in [[prop:iv5-2-1]], gives
aH_(−ℓ+j)a − Sa² = −a² − b_0² + e_R² + e_T² + f ([Hin26a, (5.60)]), with f as there and, χ₁ and χ₁′ being evaluated
at r − r_1,

    b_0 := a(S + α_Kρ_K(ℓ(dt) − H_jt) + (χ₁′/χ₁)(ℓ(dr) − H_jr) − 1)^(1/2),
    e_R := ρ_K^(−α_K)χ₁χ_Kχ_0(−χ₂χ₂′)^(1/2)(ℓ(dr) − H_jr)^(1/2),
    e_T := ρ_K^(−α_K)χ₁χ₂χ_0ρ_K(−χ_Kχ_K′)^(1/2)(ℓ(−dt) + H_jt)^(1/2),

the term of χ₁ being −a²(χ₁′/χ₁)(ℓ(dr) − H_jr). The square roots exist for the following reasons.

- b_0: on [r_1, r_4] ⊂ [r_♯, r_c − r_c e^(1/2)/v], −ℓ(−dr) is positive definite ([[lem:iv5-0-5]] (6)), so
−𝔛(r − r_1)⁻²(−ℓ(dr) + H_jr) ≥ C for any fixed C once 𝔛 is large.

- e_R: χ₂ is decreasing and ℓ(dr) is positive definite there.

- e_T: dρ_K/ρ_K² = −dt is future timelike, so ℓ(−dt) > 0 ([[lem:iv5-0-3]] (d), [[lem:iv5-0-4]]).

e_R (on supp χ₂′χ_K) and e_T (on supp χ₂χ′_K) give ‖Eω‖. The rest is as before.

(2) Take a = ρ_K^(α_K)χ₁(r_4 − r)χ̃₂(r)χ_K(ρ_K)χ_0(𝔛|ζ|), with χ̃₂ a cut-off equal to 0 near (−∞, r_1] and 1 near
[r_2, ∞). Then [[lem:iv5-2-symbols]] gives aH_(−ℓ+j)a + Sa² = a² + b_0² + b_T² − e_R² + f, the symbols formed from the
factors of a as in (1), the term of χ₁(r_4 − r) now being a²(χ₁′/χ₁)(r_4 − r)(ℓ(dr) − H_jr) ≥ 0; the only a priori term
is e_R, on supp χ̃₂′. ∎

[Hin26a, pp. 57–58] states the next propagation estimates as analogous to [[prop:iv5-5-1]]. They are stated and proved
here, both directions included, since the combination in [[sec:iv5-7]] uses each.

**Proposition {#prop:iv5-5-2}** (Propagation along K⁺ outward, and along 𝗌𝖿.) Let B_0, B_1, E ∈ Ψ_(3b,ħ) have compact
operator wave front sets in {|ζ| < 2} and Schwartz kernels supported in a compact set 𝒦 as specified, with χ = 1 on 𝒦.
Each item asserts an estimate (1) for P_h of the form [Hin26a, (5.58)] and an estimate (2) for P_h* of the form
[Hin26a, (5.59)]. In (b)–(c) the 𝗌𝖿-weight ρ_sf^(α_sf) (resp. ρ_sf^(−α_sf−2)) is included, and P_hω carries two more
powers of ρ_sf as in [Hin26a, (5.55)].

(a) (*Along K⁺, r > r_c.*) Let r′_1 := r_c + (51/50)r_c e^(1/2)/v < r′_2 := r_c + (52/50)r_c e^(1/2)/v < r′_3 < r′_4 < ∞
and 0 < t_1 < t_2 < t_3, with ρ_K = t⁻¹. Let WF′(B_0) ⊂ {ρ_K ≤ t_2⁻¹, r′_1 < r < r′_4, |ζ| < 1},
Ell(B_1) ⊃ {ρ_K ≤ t_1⁻¹, r′_1 ≤ r ≤ r′_4, |ζ| < 2}, and in (1)

    Ell(E) ⊃ {t_3⁻¹ ≤ ρ_K ≤ t_1⁻¹, r′_1 ≤ r ≤ r′_4, |ζ| < 1} ∪ {ρ_K ≤ t_1⁻¹, r′_1 ≤ r ≤ r′_2, |ζ| < 1},

while in (2) Ell(E) ⊃ {ρ_K ≤ t_1⁻¹, r′_3 ≤ r ≤ r′_4, |ζ| < 1}.

(b) (*Along 𝗌𝖿, below the sink.*) Let s := r/t, δ_r ≤ s_1 < s_2 < s_3 < s_4 := v(1 − δ_sf) and δ′ > 0 small. Let
WF′(B_0) ⊂ {s_1 < s < s_4, ρ_sf ≤ δ′, |ζ| < 1} and Ell(B_1) ⊃ {s_1 ≤ s ≤ s_4, ρ_sf ≤ 2δ′, |ζ| < 2}. In (1),

    Ell(E) ⊃ {s_1 ≤ s ≤ s_2, ρ_sf ≤ 2δ′} ∪ {s_1 ≤ s ≤ s_4, δ′ ≤ ρ_sf ≤ 2δ′}

(intersected with |ζ| < 1), and in (2) Ell(E) ⊃ {s_3 ≤ s ≤ s_4, ρ_sf ≤ 2δ′, |ζ| < 1}.

(c) (*Along 𝗌𝖿, above the sink.*) The same as (b) with s_4 := v(1 + δ_sf) < s_3 < s_2 < s_1 ≤ 10 and the inequalities in
s reversed.

*Proof.* Each is the proof of [[prop:iv5-5-1]] with a different escape function φ and, in (b)–(c), the 𝗌𝖿-cut-off and
weight of [[prop:iv5-4-1]]. The escape functions are φ = r in (a), φ = s in (b) and φ = −s in (c). Each satisfies
−ℓ(dφ) positive definite on the support in question, by [[lem:iv5-0-5]] (6): −ℓ(dr) > 0 for r ≥ r_c + r_c e^(1/2)/v,
−r²ℓ(ds) > 0 on 𝗌𝖿 ∩ {s ∈ [δ_r, v(1 − δ_sf)]}, and −r²ℓ(−ds) > 0 on 𝗌𝖿 ∩ {s ∈ [v(1 + δ_sf), 10]}. The last two persist to
{ρ_sf ≤ 2δ′} for δ′ small, by continuity on the compact s-intervals. With φ_1 < φ_4 the values of φ at the two ends (in
(a) r′_1, r′_4; in (b) s_1, s_4; in (c) −s_1, −s_4), take in (1)

    a = W⁻¹χ₁(φ_4 − φ)χ̃₂(φ)χ_⋆χ_0(𝔛|ζ|),

with χ₁(x) = e^(−𝔛/x) as before, χ̃₂ = 0 near φ ≤ φ_1 and 1 near φ ≥ φ_2, and (W, χ_⋆) = (ρ_K^(α_K), χ_K(ρ_K)) in (a),
(W, χ_⋆) = (w′, χ_sf(ρ_sf/δ′)) in (b)–(c). The terms of aH_(−ℓ+j)a are signed as follows.

- *Main term.* H_(−ℓ)χ₁(φ_4 − φ) = −χ₁′(φ_4 − φ)(−ℓ(dφ)), which is negative definite with
χ₁′/χ₁ = 𝔛(φ_4 − φ)⁻² ≥ 𝔛(φ_4 − φ_1)⁻². For 𝔛 large it dominates S, the weight term W⁻¹H_(−ℓ)W and the j-terms. These
are bounded on supp a in the rescaled sense: ρ_sf⁻²S, ρ_sf⁻²ℓ(dw′/w′) and ρ_sf⁻²H_j of functions are bounded near 𝗌𝖿
([[lem:iv5-0-2]] (d)), and j = O(|ζ|³). This gives −a² − b_0².

- *χ̃₂.* H_(−ℓ)χ̃₂(φ) = χ̃₂′(−ℓ(dφ)) ≥ 0, of the opposite sign. It is supported near the start, where (1) assumes
control.

- *χ_⋆ in (a).* H_(−ℓ)χ_K(t⁻¹) = χ_K′ ℓ(dt) t⁻², with χ_K′ ≤ 0 and ℓ(dt) < 0 (dt past timelike), so it is ≥ 0; it is
supported at ρ_K ∈ [t_3⁻¹, t_1⁻¹], where (1) assumes control.

- *χ_⋆ in (b)–(c).* H_(−ℓ)χ_sf(ρ_sf/δ′) = δ′⁻¹χ_sf′ ρ_sf² ℓ(dr), with χ_sf′ ≤ 0 and ℓ(dr) < 0 for large r, so it is
≥ 0; it is supported at ρ_sf ∈ [δ′, 2δ′], where (1) assumes control.

Each positive term is the square of a smooth symbol by the cut-off conditions of the notation, and gives ‖Eω‖. The rest
is the proof of [[prop:iv5-2-1]]: 𝓛_h, the Q-terms ([[lem:iv5-calc-q0]] and [[lem:iv5-calc-garding]], with the weight
ρ_sf as in [[prop:iv5-3-1]] in (b)–(c)), the double commutator, and the iteration.

In (2) the commutant is Wχ₁(φ − φ_1)χ̃₃(φ)χ_⋆χ_0, with χ̃₃ = 1 near φ ≤ φ_3 and 0 near φ ≥ φ_4. The main term
H_(−ℓ)χ₁(φ − φ_1) = χ₁′(−ℓ(dφ)) is now positive, the sign the adjoint pairing [[eq:iv5-2-adj]] needs. The χ_⋆-terms,
≥ 0, now have the sign of the main term. The χ̃₃-term, ≤ 0, needs control at the far end. ∎

**Proposition {#prop:iv5-5-3}** (Propagation through the interior of Ω.) Weights play no role here, all supports being
compact in Ω ∖ (K⁺ ∪ 𝗌𝖿).

(1) (*Forward.*) Let κ ∈ (0, 1), φ := t + κr and T_2 > 0. Let 𝒟 := {t ≥ 0, φ ≤ T_2}, which is compact, and let
0 < ε_X ≤ T_0r_♯/2 and ε_r := (r̂ − r_♯)/10. Let WF′(B_0) ⊂ {φ < T_2 − ε, t > ε_X, r > r_♯ + ε_r, |ζ| < 1} for some
ε > 0, let B_1 be elliptic on 𝒟 ∩ {|ζ| ≤ 2} away from X_0 ∪ Σ^♯, and let
Ell(E) ⊃ {½ε_X ≤ t ≤ ε_X, φ ≤ T_2, |ζ| < 1}. Then

    ‖B_0ω‖_(L²) ≤ C(h⁻¹‖B_1P_hω‖_(L²) + ‖Eω‖_(L²) + h^N‖χω‖_(H^(−N)_(3b,h))).

Ell(E) lies in τ⁻¹([0, T_0]), since t ≤ ε_X and r ≥ r_♯ give τ ≤ T_0/2.

(2) (*Backward.*) Let κ := 1/9, 0 < t_1 < t_2 and c₁ > 0. Let 𝒟′ := {t_1 ≤ t ≤ t_2 + 1, t − κr ≥ −c₁}, which is
compact. Let WF′(B_0) ⊂ {2t_1 < t < t_2, t − κr > 0, r > r_♯ + ε_r, |ζ| < 1}, let B_1 be elliptic on 𝒟′ ∩ {|ζ| ≤ 2}
away from Σ^♯, and let

    Ell(E) ⊃ ({t_2 ≤ t ≤ t_2 + 1} ∪ {r_♯ + ½ε_r ≤ r ≤ r_♯ + ε_r}) ∩ 𝒟′ ∩ {|ζ| < 1}.

Then the same estimate holds for P_h*.

*Proof.* (1) dφ and dt are past timelike ([[lem:iv5-0-3]] (a)), so −ℓ(dφ) and −ℓ(dt) are positive definite on 𝒟
([[lem:iv5-0-4]], [[lem:iv4-1-causal]] (a)), with a lower bound by compactness. On supp χ_r′ ⊂ [r_♯, r_♯ + ε_r],
−ℓ(−dr) > 0 ([[lem:iv5-0-5]] (6), as r_♯ + ε_r < r_c − r_c e^(1/2)/v). Take a = χ₁(T_2 − φ)χ̃(t)χ_r(r)χ_0(𝔛|ζ|), with
χ̃ = 0 on t ≤ ½ε_X and 1 on t ≥ ε_X, and χ_r = 0 near r ≤ r_♯ + ½ε_r and 1 on r ≥ r_♯ + ε_r, both non-decreasing. The
terms of aH_(−ℓ+j)a are signed as follows: H_(−ℓ)χ₁(T_2 − φ) = −χ₁′(−ℓ(dφ)) is the negative main term, dominating S and
j for 𝔛 large; H_(−ℓ)χ̃(t) = χ̃′(−ℓ(dt)) ≥ 0 needs control on supp χ̃′ ⊂ Ell(E); and
H_(−ℓ)χ_r(r) = χ_r′(−ℓ(dr)) = −χ_r′(−ℓ(−dr)) ≤ 0 has the sign of the main term and is dropped. The rest is the proof of
[[prop:iv5-2-1]]. The supports avoid X_0 and Σ^♯, as the convention on Schwartz kernels requires.

(2) d(t − κr) is past timelike ([[lem:iv5-0-3]] (a), β = κ). Take

    a = χ₁(t − t_1)χ_late(t)f(t − κr)χ_r(r)χ_0(𝔛|ζ|),

with χ_late non-increasing, 1 on t ≤ t_2 and 0 on t ≥ t_2 + 1, and f non-decreasing, 0 on (−∞, −c₁] and 1 on [0, ∞). In
the adjoint pairing [[eq:iv5-2-adj]] the main term must be positive. The terms are signed as follows:
H_(−ℓ)χ₁(t − t_1) = χ₁′(−ℓ(dt)) is positive and dominant; H_(−ℓ)f = f′(−ℓ(d(t − κr))) ≥ 0 has its sign and is dropped;
H_(−ℓ)χ_late = χ_late′(−ℓ(dt)) ≤ 0 needs control on {t_2 ≤ t ≤ t_2 + 1}; and H_(−ℓ)χ_r ≤ 0 needs control near Σ^♯. On
supp a, r ≤ (t + c₁)/κ and t ≤ t_2 + 1, so the support is compact, and χ₁(t − t_1) is bounded below on WF′(B_0). The rest
is as in (1), with 𝓛_h*. ∎

#### Energy estimates {#sec:iv5-6}

The energy estimates rest on a quadratic form built from G, a covector η and ℓ, which [Hin26a, (5.61)] writes
T_(G,η,ℓ), on its positivity ([Hin26a, Lemma 5.14]) and on an integrated inequality drawn from it ([Hin26a, Corollary
5.15]). They are stated and proved here in the form the proofs below use.

**Lemma {#lem:iv5-6-tform}** (The form T_(G,η,ℓ) of [Hin26a, (5.61)] and its positivity, in place of [Hin26a, Lemma
5.14].) Let g be a time-oriented Lorentzian inner product on a real vector space V of dimension D ≥ 3, with ⟨·, ·⟩ and
G(ζ) = ⟨ζ, ζ⟩ taken with g⁻¹, let E be a real vector space with an inner product B, and let ℓ : V* → End E be linear
with B-self-adjoint values. For η ∈ V* put

    T_(G,η,ℓ)(ζ, ζ′) := ⟨ζ, η⟩ℓ(ζ′) + ⟨ζ′, η⟩ℓ(ζ) − ⟨ζ, ζ′⟩ℓ(η),     T_(G,η,ℓ)(ζ) := T_(G,η,ℓ)(ζ, ζ),     {#eq:iv5-6-t}

so that T_(G,η,ℓ)(ζ) = 2⟨ζ, η⟩ℓ(ζ) − G(ζ)ℓ(η), and let 𝒬_(G,η,ℓ) be the quadratic form on V* ⊗ E of the symmetric
bilinear form with (ζ ⊗ ω, ζ′ ⊗ ω′) ↦ B(T_(G,η,ℓ)(ζ, ζ′)ω′, ω). For a basis (f^μ) of V* and ξ = Σ_μ f^μ ⊗ ξ_μ,
𝒬_(G,η,ℓ)(ξ) = Σ_(μ,ν) B(T_(G,η,ℓ)(f^μ, f^ν)ξ_ν, ξ_μ); and 𝒬_(G,η,ℓ)(ζ ⊗ ω) = B(T_(G,η,ℓ)(ζ)ω, ω). T and 𝒬 are linear
in each of G, η and ℓ. For complex ξ, 𝒬(ξ) := 𝒬(Re ξ) + 𝒬(Im ξ).

(a) If ℓ(ζ) is B-positive definite for every future causal ζ ≠ 0 and η is past timelike, then T_(G,η,ℓ)(ζ) is
B-positive definite for every ζ ≠ 0.

(b) Let E = V*, let c ∈ V* be past timelike and 0 < e < 2/D, and let ℓ = ℓ_(g,c,e) and B be as in [[eq:s14-ell]]. Then
𝒬_(G,η,ℓ) is positive semidefinite for every past null η, with nullspace η ⊗ V*, and positive definite for every past
timelike η.

(c) In (b), let K be a compact set of triples (g, c, η) on a fixed V, with c and η timelike for g and in the same
cone, each g time-oriented so that c is past timelike, e being fixed, and let (f^μ) be a basis of V*. There is c₀ > 0
such that 𝒬_(G,η,ℓ)(ξ) ≥ c₀Σ_μ B(ξ_μ, ξ_μ) for every (g, c, η) ∈ K and every ξ.

*Proof.* (a) T_(G,η,ℓ)(ζ) = ℓ(μ) with μ := 2⟨ζ, η⟩ζ − G(ζ)η. Write ζ = sη + ζ′ with ⟨ζ′, η⟩ = 0; as η is timelike,
G(ζ′) ≥ 0, with equality only for ζ′ = 0. Then G(μ) = G(ζ)²G(η) ≤ 0, and
⟨μ, η⟩ = 2⟨ζ, η⟩² − G(ζ)G(η) = s²G(η)² − G(ζ′)G(η) > 0 for ζ ≠ 0. So μ is causal and nonzero, and ⟨μ, η⟩ > 0 puts it
in the cone opposite to that of η: μ is future causal, and ℓ(μ) is B-positive definite.

(b) Replacing c by λc, λ > 0, multiplies ℓ by λ and leaves B unchanged; so let G(c) = −1. As 𝒬 is linear in η, it
suffices to take η = c + n with n ⊥ c and G(n) = 1: a past null η is αc + η′ with η′ ⊥ c, α = −⟨c, η⟩ > 0 and
G(η′) = α². Choose an orthonormal basis f⁰ := c, f¹ := n, f^a (2 ≤ a ≤ D − 1) of V*, so that ⟨f^μ, f^ν⟩ = ε_μδ_(μν)
with ε_0 = −1 and ε_j = 1 for j ≥ 1, and write ξ_μ = Σ_λ x_(μλ)f^λ. By the proof of [[prop:np-10-13]] (i),

    b(ζ; ω, ω′) := B(½ℓ(ζ)ω, ω′) = ⟨ζ, c⟩⟨ω, ω′⟩ − e⟨ζ, ω⟩⟨c, ω′⟩ − e⟨c, ω⟩⟨ζ, ω′⟩ + (1 − e²)⟨ζ, c⟩⟨ω, c⟩⟨ω′, c⟩,

which is symmetric in (ω, ω′). By [[eq:iv5-6-t]], the two terms of T_(G,η,ℓ)(f^μ, f^ν) with ⟨·, η⟩ give equal sums,
and

    ½𝒬_(G,η,ℓ)(ξ) = 2Σ_μ ⟨η, f^μ⟩β(ξ_μ) − Σ_μ ε_μ b(η; ξ_μ, ξ_μ),     β(w) := Σ_ν b(f^ν; ξ_ν, w).

With ⟨f^ν, c⟩ = −δ_(ν0), ⟨c, ξ_ν⟩ = −x_(ν0), ⟨f^ν, w⟩ = ε_νw_ν for w = Σ_λ w_λf^λ, and tr x := Σ_ν ε_νx_(νν),

    β(w) = −⟨ξ_0, w⟩ + e(tr x)w_0 + eΣ_ν ε_νx_(ν0)w_ν − (1 − e²)x_(00)w_0,

and b(c; ω, ω) = −⟨ω, ω⟩ − (1 + 2e − e²)ω_0², b(n; ω, ω) = 2eω_0ω_1. Inserting these, with y := Σ_a x_(aa) and with the
sums over j, k ≥ 1 and over a, a′ ≥ 2,

    ½𝒬_(G,c,ℓ)(ξ) = e(2 − e)x_(00)² − 2ex_(00)(x_(11) + y) + Σ_j x_(0j)² + e(2 − e)Σ_j x_(j0)² − 2eΣ_j x_(0j)x_(j0)
                    + Σ_(j,k) x_(jk)²,
    ½𝒬_(G,n,ℓ)(ξ) = −2Σ_j x_(0j)x_(1j) + 2ex_(00)x_(01) − 2e(2 − e)x_(00)x_(10) + 2ex_(10)(x_(11) + y)
                    + 2eΣ_a x_(1a)x_(a0) − 2eΣ_a x_(a0)x_(a1).

Adding, and writing u_λ := x_(0λ) − x_(1λ) and q := D − 2, the x_(1λ) enter only through the u_λ, and

    ½𝒬_(G,η,ℓ)(ξ) = (u_1 + eu_0)² + q(q⁻¹y − eu_0)² + e(2 − De)u_0² + Σ_a ((u_a − ex_(a0))² + (x_(a1) − ex_(a0))²
                    + e(2 − 3e)x_(a0)²) + Σ_(a≠a′) x_(aa′)² + Σ_a (x_(aa) − q⁻¹y)².

For 0 < e < 2/D ≤ 2/3 every coefficient is positive. So 𝒬_(G,η,ℓ) ≥ 0, with equality exactly when every square
vanishes, that is when u_λ = 0 for every λ and x_(aλ) = 0 for every a ≥ 2 and every λ: ξ = (f⁰ + f¹) ⊗ ξ_0 = η ⊗ ξ_0.
A past timelike η is λ₁η₁ + λ₂η₂ with λ₁, λ₂ > 0 and η₁, η₂ past null and not proportional (the null lines of a plane
through η and a spacelike covector); so 𝒬_(G,η,ℓ) = λ₁𝒬_(G,η₁,ℓ) + λ₂𝒬_(G,η₂,ℓ) ≥ 0, with nullspace
(η₁ ⊗ V*) ∩ (η₂ ⊗ V*) = 0.

Positivity of 𝒬 on all of V* ⊗ E, as in (b), uses the form of ℓ, not the hypothesis of (a) alone. For D = 3,
g⁻¹ = diag(−1, 1, 1) in a basis f⁰, f¹, f² with f⁰ past timelike, E = ℝ² with Euclidean B, ℓ(f⁰) := −Id, ℓ(f¹) := sJ₁,
ℓ(f²) := sJ₂, where J₁ := diag(1, −1), J₂ has the rows (0, 1) and (1, 0), and 2^(−1/2) < s < 1: a future causal
ζ = −αf⁰ + θ₁f¹ + θ₂f², α ≥ |θ| and α > 0, gives ℓ(ζ) the eigenvalues α ± s|θ| > 0; but
𝒬_(G,f⁰,ℓ)(ξ) = Σ_μ |ξ_μ|² − 2sΣ_(j=1,2) J_jξ_j · ξ_0, which is 1 − 2s² < 0 at ξ_0 = u, ξ_j = sJ_ju, |u| = 1.

(c) The minimum of 𝒬_(G,η,ℓ)(ξ) over Σ_μ B(ξ_μ, ξ_μ) = 1 is continuous in (g, c, η), as B, ℓ and T are, and it is
positive on K by (b). ∎

**Corollary {#cor:iv5-6-energy}** (The energy identity and the integrated inequality, in place of [Hin26a, Corollary
5.15].) Let N ⊂ ℝ_t × (ℝ⁴ ∖ 0) be open, with the coordinates z⁰ = t, z^i = x^i and r = |x|, a smooth Lorentzian metric
g, a smooth timelike 1-form c, g being time-oriented so that c is past timelike, and e ∈ (0, 2/5). Let ℓ := ℓ_(g,c,e)
and B be as in [[eq:s14-ell]], 𝒬 as in [[eq:iv5-6-t]] in the frame dz^μ, ∇ the Levi-Civita connection of g and
ℓ^λ := ℓ(dz^λ); for a 1-form ω put ℓ⟨∇ω⟩ := Σ_λ ℓ^λ∇_λω and |r∇ω|²_B := Σ_μ B(r∇_μω, r∇_μω), and let Bℓ^λ be the
bilinear form (ω₁, ω₂) ↦ B(ℓ^λω₁, ω₂).

(i) (*The divergence identity, integrated.*) Let k ∈ {1, 2, 3}, let f_1, …, f_k ∈ C^∞(N) be such that at each point at
most two of them vanish, and those that vanish there have linearly independent differentials, and let
R := {f_1 ≤ 0, …, f_k ≤ 0}, ∂_iR := R ∩ {f_i = 0}, and σ_i the
density on {f_i = 0} with |dg| = |df_i| ⊗ σ_i. For real w ∈ C^∞(N) and real ω ∈ C²(N; T*N) with R ∩ supp ω compact,

    ½∫_R 𝒬_(G,−d(w²),ℓ)(∇ω) |dg| + ½Σ_i ∫_(∂_iR) w²𝒬_(G,df_i,ℓ)(∇ω) σ_i
        = −∫_R B(□_gω, w²ℓ⟨∇ω⟩) |dg| + ∫_R w²𝓡(ω) |dg|,                                                {#eq:iv5-6-energy}

where, with summation over repeated indices,

    𝓡(ω) := (∇^μB)(∇_μω, ℓ⟨∇ω⟩) + B(∇_μω, (∇^μℓ^λ)∇_λω) + B(∇_μω, ℓ^λ[∇^μ, ∇_λ]ω) − ½(∇_λ(Bℓ^λ))(∇_μω, ∇^μω).

For complex ω, (i) is applied to Re ω and Im ω.

(ii) (*The integrated inequality.*) Suppose that at every point of R ∩ supp ω the components of g and of rc in the
frame dz^μ lie in a compact set K₀ of pairs of a Lorentzian form and a timelike covector, and let κ > 0. There is
c₀ > 0, depending only on K₀, κ and e, such that at these points

    𝒬_(G,η,ℓ)(ξ) ≥ c₀r⁻⁴|rη| Σ_μ B(rξ_μ, rξ_μ)

for every past timelike η with G(rη) ≤ −κ|rη|², |·| being the Euclidean norm of the components, and every ξ. So if in
(i) −d(w²) = 2w²η_0 on R ∩ supp ω and df_i on ∂_iR ∩ supp ω are such covectors, the left side of [[eq:iv5-6-energy]]
is at least

    c₀∫_R w²r⁻⁴|rη_0||r∇ω|²_B |dg| + ½c₀Σ_i ∫_(∂_iR) w²r⁻⁴|r df_i||r∇ω|²_B σ_i.

(iii) (*The remainder.*) If moreover the components of g, g⁻¹ and rc and their derivatives of order at most 2 along
the vector fields r∂_(z^μ) are bounded on R ∩ supp ω, then |𝓡(ω)| ≤ Cr⁻⁴(|r∇ω|²_B + B(ω, ω)) there, with C depending
only on these bounds, K₀ and e.

Replacing c by −c replaces ℓ by −ℓ and leaves B unchanged; so (i)–(iii) hold for −ℓ with the time orientation
reversed.

*Proof.* (i) Write J^λ := G^(μν)B(ℓ^λ∇_μω, ∇_νω). As □_g = −∇^μ∇_μ, for Y := w²ℓ⟨∇ω⟩,

    B(□_gω, Y) = −∇^μ(B(∇_μω, Y)) + (∇^μB)(∇_μω, Y) + B(∇_μω, ∇^μY),

and ∇^μY = (∂^μw²)ℓ⟨∇ω⟩ + w²(∇^μℓ^λ)∇_λω + w²ℓ^λ[∇^μ, ∇_λ]ω + w²ℓ^λ∇_λ∇^μω. In ∇_λJ^λ the two terms with a second
derivative of ω are equal, ℓ^λ being B-self-adjoint; so B(∇_μω, ℓ^λ∇_λ∇^μω) = B(ℓ^λ∇_μω, ∇_λ∇^μω) equals
½∇_λJ^λ − ½(∇_λ(Bℓ^λ))(∇_μω, ∇^μω). Hence

    B(□_gω, w²ℓ⟨∇ω⟩) = ∇_μZ^μ + (∂^μw²)B(∇_μω, ℓ⟨∇ω⟩) − ½(∂_λw²)J^λ + w²𝓡(ω),
    Z^μ := −w²B(∇^μω, ℓ⟨∇ω⟩) + ½w²J^μ.

For a covector η, the definition of 𝒬 gives 𝒬_(G,η,ℓ)(∇ω) = 2⟨dz^μ, η⟩B(∇_μω, ℓ⟨∇ω⟩) − η_λJ^λ, the two terms of
T_(G,η,ℓ) with ⟨·, η⟩ giving the first term, as ℓ^λ is B-self-adjoint, and ℓ(η) = η_λℓ^λ the second. So the middle
terms are ½𝒬_(G,d(w²),ℓ)(∇ω) = −½𝒬_(G,−d(w²),ℓ)(∇ω), and (df_i)_μZ^μ = −½w²𝒬_(G,df_i,ℓ)(∇ω). Integrate over R: by the
divergence theorem on R, whose outward conormal on ∂_iR is df_i, ∫_R ∇_μZ^μ |dg| = Σ_i ∫_(∂_iR) (df_i)_μZ^μ σ_i, as
Z is C¹ and R ∩ supp Z is compact. This is [[eq:iv5-6-energy]].

(ii) As ℓ_(g,c,e)(ζ) is bilinear in (c, ζ), T is linear in η and ℓ, and B does not change under c ↦ rc,

    𝒬_(G,η,ℓ_(g,c,e))(ξ) = r⁻⁴|rη| 𝒬_(G,η̂,ℓ_(g,rc,e))(rξ),     η̂ := rη/|rη|,  rξ := Σ_μ dz^μ ⊗ rξ_μ.

The triples (g, rc, η̂) lie in the compact set of the (g, ĉ, η̂) with (g, ĉ) ∈ K₀, |η̂| = 1, G(η̂) ≤ −κ and
⟨ĉ, η̂⟩ ≤ 0, a set as in [[lem:iv5-6-tform]] (c); that lemma gives c₀. The rest follows, as
½𝒬_(G,2w²η_0,ℓ) = w²𝒬_(G,η_0,ℓ).

(iii) Each term of 𝓡(ω) is a product of components of g⁻¹, of ∇ω ⊗ ∇ω or ∇ω ⊗ ω, and of one of ∇B ⊗ ℓ, ∇ℓ,
ℓ ⊗ Rm (Rm the curvature of g) and ∇(Bℓ). Under the hypothesis, B, a function of g⁻¹ and rc, and its derivatives along
r∂_(z^μ) are bounded, and ℓ = r⁻¹ℓ_(g,rc,e) is O(r⁻¹); as ∂_(z^μ) = r⁻¹(r∂_(z^μ)) and ∂_(z^μ)r is bounded, the
Christoffel symbols are O(r⁻¹), Rm is O(r⁻²), ∇B is O(r⁻¹), and ∇ℓ and ∇(Bℓ) are O(r⁻²). With ∇_μω = r⁻¹(r∇_μω),
each term is at most Cr⁻⁴(|r∇ω|²_B + B(ω, ω)), B being comparable to the Euclidean inner product on K₀. ∎

**Lemma {#lem:iv5-6-transport}** (The damping term as a transport term.) Let N, g, c, e, ℓ, B, ∇, R, f_i, ∂_iR and σ_i
be as in [[cor:iv5-6-energy]], and A := (2ih)⁻¹L_(g,c,e,h) = 2δ_g(c ⊗_s ·) + e dι_(c♯), so that −iL_(g,c,e,h) = 2hA.

(i) Aω = −½ℓ⟨∇ω⟩ + 𝒩ω, with the bundle map 𝒩 of the proof of [[prop:np-10-13]] (ii),
(𝒩ω)_a = −K(ω♯, ∂_a) − (tr K)ω_a + eK(∂_a, ω♯), K(X, Y) = (∇_Xc)(Y).

(ii) For real φ ∈ C^∞(N) and real ω ∈ C¹(N; T*N) with R ∩ supp ω compact, S being the bundle map of [[eq:s14-s]],

    ½∫_R B(ℓ(dφ)ω, ω) |dg| − ½Σ_i ∫_(∂_iR) φB(ℓ(df_i)ω, ω) σ_i = ∫_R φ(2B(Aω, ω) − B(Sω, ω)) |dg|.  {#eq:iv5-6-transport}

(iii) Where the components of g and rc lie in a compact set K₀ as in [[cor:iv5-6-energy]] (ii) and those of g, g⁻¹
and rc have bounded derivatives of order at most 2 along the r∂_(z^μ), we have |𝒩ω|_B + |Sω|_B ≤ C_Nr⁻²|ω|_B, where
the norm is |·|_B := B(·, ·)^(1/2) and C_N depends only on these bounds, K₀ and e.

Replacing c by −c replaces A, ℓ, 𝒩 and S by −A, −ℓ, −𝒩 and −S and leaves B unchanged.

*Proof.* (i) In the proof of [[prop:np-10-13]] (ii), Aω = ∇_μ(M^μω) = M^μ∇_μω + 𝒩ω, with ζ_μM^μ = −½ℓ(ζ) for every
covector ζ; so M^μ = −½ℓ^μ and M^μ∇_μω = −½ℓ⟨∇ω⟩.

(ii) Each M^μ is B-self-adjoint. As in that proof, at every point,
B(Aω, ω) = ∇_μ(B(M^μω, ω)) − (∇_μB)(M^μω, ω) − B(ω, M^μ∇_μω) and B(ω, M^μ∇_μω) = B(ω, Aω) − B(ω, 𝒩ω); so
2B(Aω, ω) = ∇_μ(B(M^μω, ω)) + B(ω, 𝒩ω) − (∇_μB)(M^μω, ω) = ∇_μ(B(M^μω, ω)) + B(Sω, ω), by the formula for S there.
Multiplying by φ and using −(∂_μφ)M^μ = ½ℓ(dφ),

    2φB(Aω, ω) = ∇_μ(φB(M^μω, ω)) + ½B(ℓ(dφ)ω, ω) + φB(Sω, ω).

Integrate over R. By the divergence theorem, as in the proof of [[cor:iv5-6-energy]] (i), the first term gives
Σ_i ∫_(∂_iR) φB((df_i)_μM^μω, ω) σ_i = −½Σ_i ∫_(∂_iR) φB(ℓ(df_i)ω, ω) σ_i, the vector field φB(M^μω, ω)∂_(z^μ) being
C¹ and R ∩ supp ω compact. This is [[eq:iv5-6-transport]].

(iii) With ĉ := rc, K_(μν) = ∂_μc_ν − Γ^λ_(μν)c_λ = r⁻²(r∂_μĉ_ν − (∂_μr)ĉ_ν − rΓ^λ_(μν)ĉ_λ), and
rΓ = ½g⁻¹(r∂g) is bounded; so the components of K are O(r⁻²), and |𝒩ω|_B ≤ Cr⁻²|ω|_B, B being comparable to the
Euclidean inner product on K₀. Each term of [[eq:s14-s]] is a product of one component of K with components of g⁻¹,
of c and of G(c)⁻¹, with twice as many factors c as factors G(c)⁻¹; under c = r⁻¹ĉ, G(c)⁻¹ = r²G(ĉ)⁻¹, with |G(ĉ)|
bounded below on K₀, so each term is O(r⁻²), and |Sω|_B ≤ Cr⁻²|ω|_B. ∎

**Lemma {#lem:iv5-6-core}** (The energy estimate with damping.) Let N, g, c, e ∈ (0, 2/5), ℓ, B, ∇, R, f_i, ∂_iR and
σ_i be as in [[cor:iv5-6-energy]], A as in [[lem:iv5-6-transport]], h ∈ (0, 1], and P := h²□_g + 2hA + hY, where Y is
a linear differential operator of order at most 1 with |Yω|_B ≤ C_Yr⁻²(|ω|_B + h|r∇ω|_B) pointwise. Let ψ ∈ C^∞(N) be
real, w := e^(−ψ), η_0 := dψ = −dw/w and η_1 := η_0 + r⁻¹dr; let κ ∈ (0, 1], λ ≥ 1, and {1, …, k} = I_+ ⊔ I_−. Let
ω ∈ C²(N; T*N) be real, with R ∩ supp ω compact, and suppose that at every point of R ∩ supp ω the components of g
and rc lie in a compact set K₀ as in [[cor:iv5-6-energy]] (ii), the bounds of [[cor:iv5-6-energy]] (iii) hold with a
constant C₁, rη_0 is past timelike with G(rη_0) ≤ −κ|rη_0|², rη_1 is past causal, and |rη_0|, |rη_1| ≥ λ; and that
for i ∈ I_+, at every point of ∂_iR ∩ supp ω, df_i is past timelike with G(r df_i) ≤ −κ|r df_i|². Put

    E_0 := ∫_R w²r⁻⁴|ω|²_B |dg|,     E_1 := ∫_R w²r⁻⁴|r∇ω|²_B |dg|,     F := ∫_R w²|Pω|²_B |dg|,
    β⁰_i := ∫_(∂_iR) w²r⁻⁴|r df_i||ω|²_B σ_i,     β¹_i := ∫_(∂_iR) w²r⁻⁴|r df_i||r∇ω|²_B σ_i.

There are λ_* and C_*, depending only on K₀, κ, e, C₁ and C_Y, such that if λ ≥ λ_*, then

    E_0 + h²E_1 + Σ_(i∈I_+)(β⁰_i + h²β¹_i) ≤ C_*(h⁻²F + Σ_(i∈I_−)(β⁰_i + β¹_i)).                         {#eq:iv5-6-core}

*Proof.* Write |·| for |·|_B, and ∫ for integrals over R against |dg| and over ∂_iR against σ_i. *Constants.* Let c₀
be the constant of [[cor:iv5-6-energy]] (ii) for K₀ and κ, C_R that of [[cor:iv5-6-energy]] (iii) for C₁, K₀ and e,
and C_N that of [[lem:iv5-6-transport]] (iii). By [[lem:iv4-1-causal]] (d) with K := K₀ there is c₁ > 0 with
B(ℓ_(g,ĉ,e)(ζ)v, v) ≥ c₁|ζ||v|² for (g, ĉ) ∈ K₀ and future causal ζ, and by continuity on compact sets there are C_ℓ
and C_Q with |B(ℓ_(g,ĉ,e)(ζ)v, v)| ≤ C_ℓ|ζ||v|² and |𝒬_(G,ζ,ℓ_(g,ĉ,e))(ξ)| ≤ C_Q|ζ|Σ_μ|ξ_μ|² for (g, ĉ) ∈ K₀ and all
ζ, v and ξ. As ℓ_(g,c,e)(ζ) is bilinear in (c, ζ) and B does not change under c ↦ rc, at the points of R ∩ supp ω
B(ℓ(ζ)v, v) ≥ c₁r⁻²|rζ||v|² for future causal ζ, |B(ℓ(ζ)v, v)| ≤ C_ℓr⁻²|rζ||v|², and, by the identity in the proof of
[[cor:iv5-6-energy]] (ii), |𝒬_(G,ζ,ℓ)(ξ)| ≤ C_Qr⁻⁴|rζ|Σ_μ|rξ_μ|². Put C₂ := 2C_Y² + 4C_N² + C_R and

    λ_* := max(1, 2(2C_Y² + C_R)/c₀, 8C_N/c₁, 4C₂^(1/2)/c₁),     C_* := (32c₁⁻² + 4c₀⁻¹)(1 + C₂C_ℓ/c₁ + C_Q) + 2C_ℓ/c₁.

*The energy identity.* Apply [[eq:iv5-6-energy]], with −d(w²) = 2w²η_0. By the hypotheses and [[cor:iv5-6-energy]] (ii),
its bulk term is at least c₀∫w²r⁻⁴|rη_0||r∇ω|² ≥ c₀λE_1, its boundary terms for i ∈ I_+ are at least ½c₀β¹_i, and
those for i ∈ I_− are at least −½C_Qβ¹_i. By [[lem:iv5-6-transport]] (i), h²□_gω = Pω − hYω + hℓ⟨∇ω⟩ − 2h𝒩ω. With
Λ := ∫w²|ℓ⟨∇ω⟩|², the Cauchy–Schwarz inequality, ∫w²|Yω|² ≤ 2C_Y²(E_0 + h²E_1), the bound |𝒩ω| ≤ C_Nr⁻²|ω| and
the bound |𝓡(ω)| ≤ C_Rr⁻⁴(|r∇ω|² + |ω|²) of [[cor:iv5-6-energy]] (iii), the right side of [[eq:iv5-6-energy]] is
at most

    −h⁻¹Λ + h⁻²F^(1/2)Λ^(1/2) + h⁻¹(2C_Y²(E_0 + h²E_1))^(1/2)Λ^(1/2) + 2h⁻¹C_NE_0^(1/2)Λ^(1/2) + C_R(E_0 + E_1)
        ≤ −¼h⁻¹Λ + h⁻³F + 2C_Y²h⁻¹(E_0 + h²E_1) + 4C_N²h⁻¹E_0 + C_R(E_0 + E_1),

each of the three products being at most ¼h⁻¹Λ plus the corresponding square. As h ≤ 1,

    (c₀λ − 2C_Y² − C_R)E_1 + ½c₀Σ_(I_+)β¹_i + ¼h⁻¹Λ ≤ h⁻³F + C₂h⁻¹E_0 + ½C_QΣ_(I_−)β¹_i.               {#eq:iv5-6-core-1}

*The transport identity.* Apply [[eq:iv5-6-transport]] with φ := r⁻²w². Then dφ = −2φη_1, and −rη_1 is future causal,
so ½B(ℓ(dφ)ω, ω) = φB(ℓ(−η_1)ω, ω) ≥ c₁λw²r⁻⁴|ω|²; for i ∈ I_+, −df_i is future timelike, so
−½φB(ℓ(df_i)ω, ω) ≥ ½c₁w²r⁻⁴|r df_i||ω|²; for i ∈ I_−, −½φB(ℓ(df_i)ω, ω) ≥ −½C_ℓw²r⁻⁴|r df_i||ω|². By (i) and (iii)
of [[lem:iv5-6-transport]], |2B(Aω, ω) − B(Sω, ω)| ≤ |ℓ⟨∇ω⟩||ω| + 2C_Nr⁻²|ω|². So

    c₁λE_0 + ½c₁Σ_(I_+)β⁰_i − ½C_ℓΣ_(I_−)β⁰_i ≤ Λ^(1/2)E_0^(1/2) + 2C_NE_0 ≤ (c₁λ)⁻¹Λ + ¼c₁λE_0 + 2C_NE_0,

and as 2C_N ≤ ¼c₁λ,

    ½c₁λE_0 + ½c₁Σ_(I_+)β⁰_i ≤ (c₁λ)⁻¹Λ + ½C_ℓΣ_(I_−)β⁰_i.                                             {#eq:iv5-6-core-2}

*Conclusion.* By [[eq:iv5-6-core-2]] and λ ≥ 1, E_0 ≤ 2(c₁λ)⁻²Λ + (C_ℓ/c₁)Σ_(I_−)β⁰_i. Insert this into
[[eq:iv5-6-core-1]]: as λ ≥ λ_*, c₀λ − 2C_Y² − C_R ≥ ½c₀λ and 2C₂(c₁λ)⁻² ≤ ⅛, so

    ½c₀λE_1 + ½c₀Σ_(I_+)β¹_i + ⅛h⁻¹Λ ≤ h⁻¹Θ,     Θ := h⁻²F + (C₂C_ℓ/c₁)Σ_(I_−)β⁰_i + ½C_QΣ_(I_−)β¹_i.

Hence Λ ≤ 8Θ, h²(E_1 + Σ_(I_+)β¹_i) ≤ 4c₀⁻¹hΘ ≤ 4c₀⁻¹Θ, and, by [[eq:iv5-6-core-2]] once more,
E_0 + Σ_(I_+)β⁰_i ≤ 4c₁⁻²Λ + (2C_ℓ/c₁)Σ_(I_−)β⁰_i ≤ 32c₁⁻²Θ + (2C_ℓ/c₁)Σ_(I_−)β⁰_i. Adding, and using
Θ ≤ h⁻²F + (C₂C_ℓ/c₁ + C_Q)Σ_(I_−)(β⁰_i + β¹_i), gives [[eq:iv5-6-core]] with the C_* above. ∎

**Proposition {#prop:iv5-6-1}** ([Hin26a, Proposition 5.16] in dimension 4 + 1.) Let α_sf, α_K ∈ ℝ.

(1) (*Near X_0*; the weight at K⁺ is dropped.) There are h_0 > 0 and C such that for h ∈ (0, h_0) and every
ω ∈ ρ_sf^(α_sf)H²_(3b,h) vanishing for t < 0,

    ‖ω‖_(ρ_sf^(α_sf)H¹_(3b,h)(τ⁻¹([0,T_0]))) ≤ Ch⁻¹‖P_hω‖_(ρ_sf^(α_sf+2)L²(τ⁻¹([0,T_0]))),

and for every ω ∈ ρ_sf^(−α_sf−2)H²_(3b,h) supported at Σ^♯ (as are the elements of the spaces (·)^(−,•) of
[[def:iv5-0-1]]), without support condition at X_0,

    ‖ω‖_(ρ_sf^(−α_sf−2)H¹_(3b,h)(τ⁻¹([0,T_0/2])))
        ≤ C(h⁻¹‖P_h*ω‖_(ρ_sf^(−α_sf)L²(τ⁻¹([0,T_0]))) + ‖ω‖_(ρ_sf^(−α_sf−2)H¹_(3b,h)(τ⁻¹([T_0/2,T_0])))).

(2) (*Near Σ^♯*; the weight at 𝗌𝖿 is dropped.) Let r_♯ ≤ r_1 < r_2 < r_3 ≤ r̂. There are h_0 > 0 and C such that for
h ∈ (0, h_0) and every ω ∈ ρ_K^(α_K)H²_(3b,h) vanishing for t < 0,

    ‖ω‖_(ρ_K^(α_K)H¹_(3b,h)(r⁻¹([r_1,r_2])))
        ≤ C(h⁻¹‖P_hω‖_(ρ_K^(α_K)L²(r⁻¹([r_1,r_3]))) + ‖ω‖_(ρ_K^(α_K)H¹_(3b,h)(r⁻¹([r_2,r_3])))),

and for every ω ∈ ρ_K^(−α_K)H²_(3b,h) vanishing for r < r_1,

    ‖ω‖_(ρ_K^(−α_K)H¹_(3b,h)(r⁻¹([r_1,r_3]) ∩ {τ ≥ 0})) ≤ Ch⁻¹‖P_h*ω‖_(ρ_K^(−α_K)L²(r⁻¹([r_1,r_3]) ∩ {τ ≥ 0})).

These four estimates are [Hin26a, (5.66)–(5.69)], with T := T_0 and with the radii r_1 < r_2 < r_3 < r₊ of [Hin26a],
from its inner radius on, read as above; in the proofs the level sets of τ carry the density r⁴|dr d𝑔̸|, which
tensored with |dτ| is |dg|. Moreover, at fixed h, for ω ∈ ρ_sf^(α_sf)H̄²_3b without support condition,

    ‖ω‖_(ρ_sf^(α_sf)H̄¹_3b(τ⁻¹([0,T_0]))) ≤ C_h(‖P_hω‖_(ρ_sf^(α_sf+2)L²(τ⁻¹([0,T_0])))
                                                + ‖(ω, r𝓛_(∂_t)ω)|_(X_0)‖_(ℋ_data)),                {#eq:iv5-6-1}

where ℋ_data := ρ_sf^(α_sf)H̄¹_b(X_0, r⁴|dr d𝑔̸|) ⊕ ρ_sf^(α_sf)H̄⁰_b(X_0, r⁴|dr d𝑔̸|).

*Proof.* *The operators.* As g is Ricci-flat, P_h = h²□_g − iL_h = h²□_g + 2hA ([[lem:s14-box-c]]), with A of
[[lem:iv5-6-transport]], a real operator; so it suffices to prove the estimates for real ω, those for complex ω
following by adding the estimates for Re ω and Im ω. For the adjoint, A* = S − A ([[prop:np-10-13]] (ii)), and
B(ω, ω′) = ⟨ω, Θω′⟩ with Θω := ω − (1 + e)G(c)⁻¹⟨c, ω⟩c, which is invertible, B being positive definite; as □_g is
symmetric for ⟨·, ·⟩ and |dg|, □_g* = Θ⁻¹□_gΘ = □_g + Z with Z := −Θ⁻¹(2(∇^μΘ)∇_μ + (∇^μ∇_μΘ)). So

    P_h* = h²□_g + 2h(−A) + hY,     Y := 2S + hZ,

and −A is the operator A of the 1-form −c, which is past timelike for the opposite time orientation
([[lem:iv5-6-transport]]). Θ depends only on g and rc, so ∇Θ = O(r⁻¹) and ∇∇Θ = O(r⁻²) under the bounds below, and
with [[lem:iv5-6-transport]] (iii), |Yω|_B ≤ C_Yr⁻²(|ω|_B + h|r∇ω|_B).

*The hypotheses of [[lem:iv5-6-core]].* Let N := ℝ_t × {r > ½r_♯}. On {r ≥ ½r_♯} ∩ τ⁻¹([0, T_0]) and on
{½r_♯ ≤ r ≤ r̂} ∩ {t ≥ 0}, whose closures in the compactification of [[def:iv5-0-1]] are compact, the components of g,
g⁻¹ and rc are smooth up to the faces at infinity and continuous in b, by the proofs of [[lem:iv5-0-2]] (a), (d), which
hold on {r ≥ ½r_♯}; r∂_(z^μ) ∈ 𝒱_3b; and rc is past timelike there ([[sec:iv5-0]]). So the components of g and rc lie
in a compact set K₀ of pairs, and the bounds of [[cor:iv5-6-energy]] (iii) hold with one C₁, for b ∈ U, for the
pair (g, c) and, with the opposite orientation, for (g, −c); so does the bound on Y with one C_Y. Let Γ bound the
Euclidean operator norm of g⁻¹ over K₀. We use: (∗) if u is past timelike with G(u) ≤ −γ|u|², γ ∈ (0, 1], |·| the
Euclidean norm of the components, |v| ≤ m and 𝔛|u| ≥ 6m max(1, Γ/γ), then 𝔛u + v is past timelike, with
G(𝔛u + v) ≤ −(γ/4)|𝔛u + v|² and |𝔛u + v| ≥ ¾𝔛|u|. Indeed, with q := 𝔛|u| ≥ 6m, so that Γm ≤ γq/6,
G(𝔛u + v) ≤ −γq² + 2Γmq + Γm² ≤ −γq² + (9/4)Γmq ≤ −(5/8)γq² ≤ −(γ/4)(5q/4)², while
q − m ≤ |𝔛u + v| ≤ q + m ≤ 5q/4; the same holds with sv, s ∈ [0, 1], in place of v, so 𝔛u + v lies in the cone of u.
Let λ_* be the number of [[lem:iv5-6-core]] for K₀, κ := ⅛, e, C₁ and C_Y. All constants below are uniform for b ∈ U.

*The first estimate of (1)* ([Hin26a, (5.66)]). There ρ_sf = r⁻¹. Take R := {τ ≤ T_0, r ≥ r_♯} ⊂ N, f_1 := τ − T_0,
f_2 := r_♯ − r, I_+ := {1, 2}, Y := 0 and w := ρ_sf^(−α_sf−2)e^(−𝔛τ). With u := r dτ = dt − τ dr,
rη_0 = 𝔛u − (α_sf + 2)dr and rη_1 = 𝔛u − (α_sf + 1)dr. On τ⁻¹([0, T_0]), G(u) ≤ −¾ ≤ −(3/5)|u|²
([[lem:iv5-0-3]] (b); |u|² = 1 + τ² ≤ 5/4) and |u| ≥ 1, so by (∗) with γ := 3/5 and m := |α_sf| + 2, both are past
timelike with G ≤ −(3/20)|·|² and of length at least ¾𝔛, for 𝔛 ≥ 6m max(1, 5Γ/3). On {τ = T_0}, r df_1 = u; on
Σ^♯, r df_2 = −r dr is past timelike with G(−r dr) ≤ −½|r dr|² ([[lem:iv5-0-3]] (c)). Fix 𝔛 ≥ max(6m max(1, 5Γ/3),
(4/3)λ_*). Then [[eq:iv5-6-core]] holds for every real ω, smooth on N, vanishing for t < 0, with R ∩ supp ω compact.
On R ∩ supp ω ⊂ τ⁻¹([0, T_0]), w²r⁻⁴ = ρ_sf^(−2α_sf)e^(−2𝔛τ) ≥ e^(−𝔛)ρ_sf^(−2α_sf) and w² ≤ ρ_sf^(−2α_sf−4); and
r∇_μω = r∂_(z^μ)ω − rΓ_μω with rΓ_μ bounded ([[lem:iv5-0-2]] (c)), the r∂_(z^μ) spanning 𝒱_3b, and B is comparable to
the Euclidean inner product. So E_0 + h²E_1 ≥ c‖ω‖²_(ρ_sf^(α_sf)H¹_(3b,h)(τ⁻¹([0,T_0]))) for some c > 0 and
F ≤ ‖P_hω‖²_(ρ_sf^(α_sf+2)L²(τ⁻¹([0,T_0]))), and the estimate holds with C := (C_*/c)^(1/2), for every h ∈ (0, 1]. It
extends to every ω ∈ ρ_sf^(α_sf)H²_(3b,h) vanishing for t < 0: such ω are limits in that space of smooth sections
vanishing for t < 0 with compact support (extend across Σ^♯, translate in t, mollify and cut off at large r), and both
sides are continuous in its norm.

*The first estimate of (2)* ([Hin26a, (5.68)]). Let χ = χ(r) be smooth, equal to 1 for r ≤ r_2 and to 0 for r ≥ r_3,
and ω′ := χω, with ω smooth, vanishing for t < 0 and with compact support. On {t > −r} put ρ_K := r/(t + r), extended
smoothly and positively to N; on r⁻¹([r_♯, r̂]) ∩ {t ≥ 0} it is ρ_K′/(1 + ρ_K′), ρ_K′ the ρ_K of [[def:iv5-0-1]]
near K⁺, so the weights are equivalent. Take R := {r ≥ r_1}, f_1 := r_1 − r, I_+ := {1}, Y := 0 and
w := ρ_K^(−α_K)e^(𝔛r). With u := −r dr, rη_0 = 𝔛u + α_K(dr − r(dt + dr)/(t + r)) and rη_1 = rη_0 + dr, the added
covectors having Euclidean norm at most 3|α_K| + 1 on {t ≥ 0}. On r⁻¹([r_1, r_3]) ⊂ r⁻¹([r_♯, r̂]), u is past timelike
with G(u) ≤ −½|u|² and |u| ≥ r_♯ ([[lem:iv5-0-3]] (c)), and so is r df_1 = u. By (∗) with γ := ½ and m := 3|α_K| + 1,
[[lem:iv5-6-core]] applies to ω′, whose support meets R in r⁻¹([r_1, r_3]) ∩ {t ≥ 0}, with κ = ⅛ and λ := ¾𝔛r_♯, for
𝔛 ≥ r_♯⁻¹ max(6(3|α_K| + 1) max(1, 2Γ), (4/3)λ_*). There w²r⁻⁴ and w² lie between positive multiples of ρ_K^(−2α_K), so
‖ω′‖_(ρ_K^(α_K)H¹_(3b,h)(r⁻¹([r_1,r_3]))) ≤ Ch⁻¹‖P_hω′‖_(ρ_K^(α_K)L²(r⁻¹([r_1,r_3]))). Now
P_hω′ = χP_hω + [P_h, χ]ω, where [P_h, χ]ω = −h²(2∇^μχ∇_μω + (∇^μ∇_μχ)ω) − hℓ(dχ)ω by [[lem:iv5-6-transport]] (i),
supported in r⁻¹([r_2, r_3]) with bounded coefficients; so h⁻¹‖[P_h, χ]ω‖ ≤ C‖ω‖_(ρ_K^(α_K)H¹_(3b,h)(r⁻¹([r_2,r_3]))).
As ω′ = ω on r⁻¹([r_1, r_2]), this gives the estimate, which extends by density as before.

*The second estimate of (1)* ([Hin26a, (5.67)]). Let ω be smooth with compact support in {r > r_♯}; such sections are
dense among those supported at Σ^♯, both sides being continuous in the norm of ρ_sf^(−α_sf−2)H²_(3b,h). Let χ = χ(τ)
be smooth, equal to 1 for τ ≤ ½T_0 and to 0 for τ ≥ ¾T_0, and ω′ := χω. Apply [[lem:iv5-6-core]] to P_h*, with the
1-form −c and the opposite time orientation, R := {τ ≥ 0} ∩ N, f_1 := −τ, I_+ := {1} and w := ρ_sf^(α_sf)e^(𝔛τ). Now
rη_0 = −𝔛u + α_sf dr and rη_1 = −𝔛u + (α_sf + 1)dr, with −u past timelike for the opposite orientation, and
r df_1 = −u; by (∗) as before, the hypotheses hold on R ∩ supp ω′ ⊂ τ⁻¹([0, ¾T_0]) ∩ {r > r_♯} for
𝔛 ≥ max(6(|α_sf| + 1) max(1, 5Γ/3), (4/3)λ_*), with λ := ¾𝔛. There
w²r⁻⁴ ≥ ρ_sf^(2α_sf+4) and w² ≤ e^(2𝔛T_0)ρ_sf^(2α_sf), so
‖ω′‖_(ρ_sf^(−α_sf−2)H¹_(3b,h)(τ⁻¹([0,T_0]))) ≤ Ch⁻¹‖P_h*ω′‖_(ρ_sf^(−α_sf)L²(τ⁻¹([0,T_0]))). Here
P_h*ω′ = χP_h*ω + [P_h*, χ]ω, where
[P_h*, χ]ω = −h²(2∇^μχ∇_μω + (∇^μ∇_μχ)ω) + hℓ(dχ)ω − 2h²Θ⁻¹(∇^μΘ)(∂_μχ)ω is supported in τ⁻¹([½T_0, ¾T_0]),
and |[P_h*, χ]ω|_B ≤ Chr⁻²(|ω|_B + h|r∇ω|_B), as dχ = χ′(τ)r⁻¹u; so
h⁻¹‖[P_h*, χ]ω‖_(ρ_sf^(−α_sf)L²) ≤ C‖ω‖_(ρ_sf^(−α_sf−2)H¹_(3b,h)(τ⁻¹([T_0/2,T_0]))). As ω′ = ω on τ⁻¹([0, ½T_0]),
this gives the estimate.

*The second estimate of (2)* ([Hin26a, (5.69)]). Let ω be smooth, with compact support in {r > r_1}, dense as before.
Apply [[lem:iv5-6-core]] to P_h*, with −c and the opposite orientation, R := {τ ≥ 0, r ≤ r_3} ∩ N, f_1 := −τ,
f_2 := r − r_3, I_+ := {1, 2} and w := ρ_K^(α_K)e^(−𝔛r), ρ_K as above. Now rη_0 = −𝔛u − α_K(dr − r(dt + dr)/(t + r))
and rη_1 = rη_0 + dr, with u = −r dr as above, and r df_2 = −u, r df_1 = −r dτ; −u = r dr is past timelike for the
opposite orientation on [r_♯, r̂], with G(−u) ≤ −½|u|², and on {τ = 0}, −r dτ = −dt is past timelike for it, with
G(dt) ≤ −1 = −|dt|² ([[lem:iv5-0-3]] (a)). By (∗) the hypotheses hold, with λ := ¾𝔛r_♯,
for 𝔛 ≥ r_♯⁻¹ max(6(3|α_K| + 1) max(1, 2Γ), (4/3)λ_*), and as there w²r⁻⁴ and w² lie between positive multiples of
ρ_K^(2α_K), [[eq:iv5-6-core]] gives the estimate.

[[eq:iv5-6-1]]. Fix h, and let ω be smooth on N with compact support. Apply [[lem:iv5-6-core]] as for the first
estimate of (1), on R := {0 ≤ τ ≤ T_0, r ≥ r_♯} with the third function f_3 := −τ and I_− := {3}; at most two of
f_1, f_2, f_3 vanish at any point. On X_0 = {τ = 0}, |dg| = |dτ| ⊗ r⁴|dr d𝑔̸| ([[lem:iv5-0-2]] (b)), |r dτ| = 1 and
w²r⁻⁴ = ρ_sf^(−2α_sf); r∇_tω = r𝓛_(∂_t)ω − rΓ_tω, the coordinates being stationary, and
r∇_(x^i)ω = r∂_(x^i)ω − rΓ_iω, the r∂_(x^i) being b-vector fields on X̄; so
β⁰_3 + β¹_3 ≤ C‖(ω, r𝓛_(∂_t)ω)|_(X_0)‖²_(ℋ_data), and [[eq:iv5-6-core]] gives [[eq:iv5-6-1]], which extends to
ω ∈ ρ_sf^(α_sf)H̄²_3b by density, the traces on X_0 depending continuously on ω. Applied with T ∈ (0, T_0] in place of
T_0 in R, the same bounds the term β⁰_1 + h²β¹_1 on {τ = T}, which is comparable to
‖(ω, r∇ω)|_(τ=T)‖² in ρ_sf^(α_sf)L²(r⁴|dr d𝑔̸|), by the right side of [[eq:iv5-6-1]], uniformly in T. Here
∂_τ = r∂_t at fixed (r, ω), and the weight matches by [[lem:iv5-0-2]] (b):
ρ_sf^(α+½)H̄^k_b(X_0, r³|dr d𝑔̸|) = ρ_sf^α H̄^k_b(X_0, r⁴|dr d𝑔̸|). ∎

#### Combination: [Hin26a, Theorem 5.2] in dimension 4 + 1 {#sec:iv5-7}

Fix (α_sf, α_K) as in [[lem:iv5-0-5]] and b ∈ U.

**Proposition {#prop:iv5-7-1}** ([Hin26a, Proposition 5.17] in dimension 4 + 1.) For s ≥ 1 there are h_0 > 0 and C such
that for h ∈ (0, h_0) and ω ∈ H^(s+1,(α_sf,α_K))_(3b,h)(Ω)^(•,−),

    ‖ω‖_(H^(s,(α_sf,α_K))_(3b,h)(Ω)^(•,−)) ≤ Ch⁻¹‖P_hω‖_(H^(s−1,(α_sf+2,α_K))_(3b,h)(Ω)^(•,−)).            {#eq:iv5-5-79}

*Proof.* Take s = 1 first. Every microlocal estimate below bounds ‖B_0ω‖ by h⁻¹‖B_1P_hω‖, an a priori term ‖Eω‖ and
h^N‖χω‖_(H^(−N)). Each step's a priori set lies in the elliptic sets of the B_0's of earlier steps, so the estimates
chain. The B_0's of all the steps together are elliptic on a neighbourhood of o over supp χ_(τ,2)χ_(r,2). The steps are:

(i) [Hin26a, (5.66)] on τ⁻¹([0, T_0]).

(ii) [[prop:iv5-1-2]] and [[prop:iv5-1-3]] off o; the a priori term of [Hin26a, (5.21)] lies in
τ⁻¹([0, (2.75/10)T_0]), covered by (i).

(iii) [[prop:iv5-5-3]] (1) on every 𝒟, with κ = ½ and T_2 arbitrary, from (i). This covers o over every compact subset
of Ω ∖ (K⁺ ∪ 𝗌𝖿), since {t ≤ T′, r ≤ R′} ⊂ {φ < T′ + R′}.

(iv) [[prop:iv5-5-2]] (c) along 𝗌𝖿 from s ∈ [5, 10], where τ ≤ 1/5 < T_0 and (i) applies, to s > v(1 + δ_sf). Its
interior a priori set {δ′ ≤ ρ_sf ≤ 2δ′} is compact in Ω° and covered by (iii).

(v) [[prop:iv5-2-1]] (1) at r = r_c; its E lies at finite t ∈ [1/(3δ), 1/δ], covered by (iii).

(vi) [[prop:iv5-5-1]] (1) towards r_♯, with r_1 := r_♯ + (2/10)(r̂ − r_♯) and t_1 ≥ δ⁻¹; its E is near r_c, by (v), or
at finite times, by (iii).

(vii) [[prop:iv5-5-2]] (a) (1) outward to r′_4 := 2δ_0⁻¹, with r′_3 := δ_0⁻¹, where δ_0 is the δ of [[prop:iv5-3-1]];
its E is near r_c, by (v), or at finite times, by (iii).

(viii) [[prop:iv5-3-1]] (1) at ∂K⁺; its E lies at ρ_sf ∈ [(5/4)δ_0, 2δ_0], ρ_K ≤ 2δ_r, covered by (vii) where t is
large and by (iii) where t is finite.

(ix) [[prop:iv5-5-2]] (b) (1) along 𝗌𝖿 from s ∈ [δ_r, (5/4)δ_r], by (viii), to s < v(1 − δ_sf), its interior part by
(iii); here 2δ′ ≤ δ_0, so that the start set lies in the B_0 of [[prop:iv5-3-1]].

(x) [[prop:iv5-4-1]] (1) at the sink, with its δ ≤ δ′/2. Its E lies at |s/v − 1| ∈ [(5/4)δ_sf, 2δ_sf], covered by (iv)
and (ix), or at ρ_sf ≥ (5/4)δ with r finite, covered by (iii).

Together this is the first form of [Hin26a, (5.80)]:

    ‖ω‖_(H^(1,(α_sf,α_K))_(3b,h)(τ⁻¹([0,T_0]))) + ‖χ_(τ,2)χ_(r,2)ω‖_(H^(1,(α_sf,α_K))_(3b,h))
      ≤ C(h⁻¹‖P_hω‖_(H^(0,(α_sf+2,α_K))_(3b,h)(Ω)^(•,−)) + h^N‖χ_(τ,0)χ_(r,0)ω‖_(H^(−N,(α_sf,α_K))_(3b,h))).

Then [Hin26a, (5.68)] with r_1 = r_♯, r_2 := r_♯ + (2.75/10)(r̂ − r_♯) and r_3 := ½(r_2 + r̂) estimates ω on
r⁻¹([r_♯, r_2]) by the region just controlled. This gives [Hin26a, (5.80)], and absorbing the h^N term for h small gives
[[eq:iv5-5-79]] at s = 1.

For s > 1, the energy estimates are the only step restricted to s = 1, and we extend and restrict, as in [Hin26a].
Extend f := P_hω to f̃ on Ω̃ := cl{t ≥ 0, r ≥ ¾r_♯} with the same quotient norm, and g, c as in [[sec:iv5-0]]. The
forward solution ω̃ ∈ H^(0,(α_sf,α_K))_(3b,h)(Ω̃)^(•,−) exists with ‖ω̃‖ ≤ Ch⁻¹‖f̃‖_(H^(−1)), by [[prop:iv5-7-2]] at
s′ = 1 on Ω̃ and duality. On Ω̃ the argument runs with two changes. [[prop:iv5-5-1]] is used with r_1 ≥ r_♯, and the
transition of χ_r in [[prop:iv5-5-3]] is placed in {r ≥ r_♯}, where c is the 1-form of [[prop:np-10-14]] and
[[lem:iv5-0-5]] (6) holds. On {¾r_♯ ≤ r ≤ r_3}, r_3 < r̂, the estimates [Hin26a, (5.68)–(5.69)] of
[[prop:iv5-6-1]] are used, with ¾r_♯ for r_♯; their proof needs only [[lem:iv5-0-3]] (a), (c),
[[lem:iv5-0-4]] and the bounds it derives for the hypotheses of [[lem:iv5-6-core]], which hold on {r ≥ ½r_♯},
where g is defined and c is past timelike ([[sec:iv5-0]]). [[prop:iv5-1-3]] needs only
[[lem:iv5-0-3]] (c) there. Moreover ω̃ = ω on Ω, by uniqueness of forward solutions: Σ^♯ is spacelike with future
timelike vectors pointing out, and X_0 is spacelike ([[lem:iv5-0-3]] (a), (c)). The microlocal estimates of
[[sec:iv5-1]]–[[sec:iv5-5]] hold for every s in the strong sense: near the zero section the operators have compact
operator wave front sets and the order is irrelevant, and at fibre infinity the regularisation in the proof of
[[prop:iv5-1-3]] applies. They
apply to ω̃ on {r ≥ (7/8)r_♯}, where Σ^♯ is now interior. Near τ = 0 they propagate from τ < 0, where ω̃ = 0, by
[[prop:iv5-5-3]] (1) and [[prop:iv5-1-3]] with the cut-offs moved below τ = 0. Restriction to Ω gives
[[eq:iv5-5-79]] for s ≥ 1. ∎

**Proposition {#prop:iv5-7-2}** (The adjoint estimate [Hin26a, (5.81)] in dimension 4 + 1.) For s′ ≥ 1 there are h_0 > 0
and C such that for h ∈ (0, h_0),

    ‖ω′‖_(H^(s′,(−α_sf−2,−α_K))_(3b,h)(Ω)^(−,•)) ≤ Ch⁻¹‖P_h*ω′‖_(H^(s′−1,(−α_sf,−α_K))_(3b,h)(Ω)^(−,•)).   {#eq:iv5-5-81}

*Proof.* At s′ = 1 the estimates chain as follows, each later a priori set covered by earlier steps.

(i) [[prop:iv5-4-1]] (2) at the sink, which has no a priori term.

(ii) [[prop:iv5-5-2]] (b) (2) and (c) (2) along 𝗌𝖿 outward from the sink, to s ∈ [δ_r, v(1 − δ_sf)] and
[v(1 + δ_sf), 10]. Their a priori sets are at the sink, by (i), and their 𝗌𝖿-cut-off terms have the good sign. Here
2δ′ is at most the δ of the sink, and s_3 ≥ v(1 − (5/4)δ_sf).

(iii) [[prop:iv5-3-1]] (2) at ∂K⁺; its E at ρ_K ∈ [(5/4)δ_r, 2δ_r] is covered by (ii).

(iv) [[prop:iv5-5-2]] (a) (2) along K⁺ inward from r′_4 := 2δ_0⁻¹ to r′_1, with r′_3 := δ_0⁻¹ and δ_0 the δ of
[[prop:iv5-3-1]]; its E at [r′_3, r′_4], where ρ_sf ≤ δ_0, is covered by (iii). Here t_1 ≥ 2/(δ_0δ_r), so that
[r′_3, r′_4] at ρ_K = 1/t ≤ t_1⁻¹ lies in {r/t ≤ (5/4)δ_r}.

(v) [Hin26a, (5.69)] near Σ^♯, which has no a priori term on supported spaces.

(vi) [[prop:iv5-5-1]] (2) from Σ^♯ towards r_c; its E near r_♯ is covered by (v).

(vii) [[prop:iv5-2-1]] (2) at r_c; its E at |r − r_c| ∈ [55/50, 60/50]r_c e^(1/2)/v is covered by (iv) and (vi).

At this point a neighbourhood of o over {ρ_K ≤ ε₁} ∪ ({ρ_sf ≤ ε₁} ∩ {s ≤ 10}) ∪ {r ≤ r_♯ + ε_r} is controlled, for some
ε₁ > 0. Here ρ_K = r/(t + r) globally.

(viii) [[prop:iv5-5-3]] (2) with κ = 1/9, t_1 < ¼T_0r_♯ and t_2 ≥ max(ε₁⁻², 10c₁). Its late set
{t_2 ≤ t ≤ t_2 + 1} ∩ 𝒟′ is covered by (i)–(vii): points there with r ≤ ε₁⁻¹ have ρ_K ≤ ε₁, and the others have
ρ_sf ≤ ε₁ and s = r/t ≤ (t + c₁)/(κt) ≤ 10 once t_2 ≥ 10c₁. Its set near Σ^♯ is covered by (v). It controls o over
{t ≥ 2t_1, t ≥ κr} up to t_2, which covers {τ ≥ κ} there; and κ = 1/9 < ¼ = ½T_0. A point with τ ≥ ½T_0 has
t ≥ ½T_0r_♯ > 2t_1.

(ix) [[prop:iv5-1-2]] and [[prop:iv5-1-3]] (the adjoint estimate [Hin26a, (5.22)]) off o; the a priori term is near
Σ^♯, by (v).

(x) [Hin26a, (5.67)] on τ⁻¹([0, ½T_0]), from τ⁻¹([½T_0, T_0]), which is covered by (ii) near 𝗌𝖿, by (viii) elsewhere,
and by (ix) off o.

Absorbing h^N gives [[eq:iv5-5-81]] at s′ = 1. For s′ > 1, extend and restrict as in [[prop:iv5-7-1]]. ∎

**Theorem {#thm:iv5-7-3}** ([Hin26a, Theorem 5.2] in dimension 4 + 1.) Let (α_sf, α_K) be as in [[lem:iv5-0-5]] and
C₁ > 0. There is h_0 > 0, uniform for b ∈ U ([[lem:iv5-8-1]]), such that for h ∈ (0, h_0), s ∈ [−C₁, C₁] and b ∈ U:

(a) the forward problem □^C_bω = f ∈ H^(s−1,(α_sf+2,α_K))_3b(Ω)^(•,−) has a unique solution
ω ∈ H^(s,(α_sf,α_K))_3b(Ω)^(•,−), with the semiclassical bound ‖ω‖_(H^s_(3b,h)) ≤ Ch⁻¹‖h²f‖_(H^(s−1)_(3b,h)) in these
weights ([Hin26a, (5.18)]);

(b) the initial value problem

    □^C_bω = f ∈ ρ_sf^(α_sf+2)ρ_K^(α_K)H̄⁰_3b(Ω, |dg|),
    (ω, r𝓛_(∂_t)ω)|_(X_0) ∈ ρ_sf^(α_sf+½)H̄¹_b(X_0, r³|dr d𝑔̸|) ⊕ ρ_sf^(α_sf+½)H̄⁰_b(X_0, r³|dr d𝑔̸|)      {#eq:iv5-5-16}

has a unique solution ω ∈ ρ_sf^(α_sf)ρ_K^(α_K)H̄¹_3b(Ω, |dg|), the densities on X_0 being Euclidean;

(c) [[eq:iv5-5-79]] and [[eq:iv5-5-81]] hold for s, s′ ∈ [1, C₁ + 1] and h ∈ (0, h_0), with constants uniform for b ∈ U
(h_0 depending on C₁).

*Proof.* (c) is [[prop:iv5-7-1]] and [[prop:iv5-7-2]] with [[lem:iv5-8-1]].

(a) *Existence for s ≤ 0.* Take s′ := 1 − s ≥ 1. For ω′ in H^(s′,(−α_sf−2,−α_K))_(3b,h)(Ω)^(−,•), the functional
P_h*ω′ ↦ ⟨h²f, ω′⟩ is well defined and bounded by Ch⁻¹‖h²f‖‖P_h*ω′‖, by [[eq:iv5-5-81]]. The spaces
H^(s−1,(α_sf+2,α_K))(Ω)^(•,−) and H^(1−s,(−α_sf−2,−α_K))(Ω)^(−,•) are dual under ⟨·, ·⟩, and so are
H^(s,(α_sf,α_K))(Ω)^(•,−) and H^(−s,(−α_sf,−α_K))(Ω)^(−,•), with constants independent of h ([[lem:iv5-calc-dual]]). So
the Hahn–Banach theorem gives
ω ∈ H^(s,(α_sf,α_K))_(3b,h)(Ω)^(•,−) with P_hω = h²f and the bound [Hin26a, (5.18)]. *s > 0.* Higher regularity follows
by extension and restriction with the propagation estimates, as in [[prop:iv5-7-1]]. *Uniqueness*, for every
distribution ω on Ω supported in {t ≥ 0} with P_hω = 0, follows by the classical duality argument. For
φ ∈ C_c^∞(Ω°), the backward solution ψ of P_h*ψ = φ is smooth, with support in the causal past of supp φ. That set is
compact, since t decreases and |dr/dt| is bounded along causal curves. It is disjoint from Σ^♯: along past-directed
causal curves r increases inside {r ≤ r̂} ([[lem:iv5-0-3]] (c)), so r stays above min(min_(supp φ) r, r̂). Pairing the
extension of ω by zero across X_0 with ψ gives ⟨ω, φ⟩ = ⟨P_hω, ψ⟩ = 0.

(b) By [[lem:iv5-0-2]] (b) the data space is ℋ_data of [[eq:iv5-6-1]], with the density r⁴|dr d𝑔̸| that tensors with
dτ to |dg|; the shift ½ does not depend on the dimension ([Hin26a, p. 65]). *Smooth data.* Take f smooth with compact
support in Ω°, and data smooth on X_0 with compact support in X_0 ∖ 𝗌𝖿. The initial value problem then has a solution
ω smooth on Ω ∖ (K⁺ ∪ 𝗌𝖿), for the following reasons. □^C_b is normally hyperbolic ([[def:std-normally-hyperbolic]]):
its second-order part is that of □_g = −∇^a∇_a ([[lem:s14-box-c]]). Let N := ℝ_t × {r > ½r_♯} and
S := N ∩ {t = 0}, which is acausal, as t increases strictly along future causal curves ([[lem:iv5-0-3]] (a)). Every
inextendible causal curve through a point of Ω ∖ (K⁺ ∪ 𝗌𝖿) meets S: t decreases along it towards the past, r increases
along it inside {r ≤ r̂} ([[lem:iv5-0-3]] (c)), so it stays in N, and |dr/dt| is bounded along causal curves, since g
is a 3sc-metric. So Ω ∖ (K⁺ ∪ 𝗌𝖿) lies in the Cauchy development D of S, which is globally hyperbolic with Cauchy
hypersurface S ([[thm:std-bgp-development]]), and [[thm:std-bgp-cauchy]] (5) on D gives a smooth solution, for the
data extended smoothly to S with compact support (on S, (ω, r𝓛_(∂_t)ω) and (ω, ∇_nω) determine each other); by its
support statement the solution on Ω does not depend on the extension, future causal curves from S ∩ {r < r_♯} staying
in {r < r_♯} ([[lem:iv5-0-3]] (c)). By finite speed of propagation, ω
vanishes on τ⁻¹([0, T_0]) near 𝗌𝖿, the speed being 1 + O(r⁻²) and T_0 < 1; so
ω ∈ ρ_sf^(α_sf)H̄²_3b(τ⁻¹([0, T_0])) and [[eq:iv5-6-1]] applies. Let χ = χ(τ) equal 1 for τ ≥ ½T_0 and 0 for
τ ≤ ¼T_0. Then P_h(χω) = h²χf + [P_h, χ]ω ∈ H^(0,(α_sf+2,α_K))(Ω)^(•,−), with norm bounded by ‖f‖ and by
‖ω‖_(ρ^(α_sf)H̄¹(τ⁻¹([0,T_0]))). By the uniqueness in (a), which holds for distributions, χω is the forward solution,
so it lies in H^(1,(α_sf,α_K)). Using [[eq:iv5-6-1]],

    ‖ω‖_(ρ_sf^(α_sf)ρ_K^(α_K)H̄¹_3b(Ω)) ≤ C(‖f‖ + ‖(ω, r𝓛_(∂_t)ω)|_(X_0)‖_(ℋ_data)).

*General data.* Approximate f and the data in their spaces by such smooth data. By this estimate the solutions converge
in ρ_sf^(α_sf)ρ_K^(α_K)H̄¹_3b(Ω). Near X_0 they also converge in
C([0, T_0]_τ; ρ_sf^(α_sf)H̄¹_b) ∩ C¹([0, T_0]_τ; ρ_sf^(α_sf)H̄⁰_b): the term of [[eq:iv5-6-core]] on {τ = T}, for the
region {0 ≤ τ ≤ T, r ≥ r_♯} of the proof of [[eq:iv5-6-1]] at every T ∈ (0, T_0], bounds the norm of
(ω, ∂_τω)|_(τ=T) by the right side of [[eq:iv5-6-1]]. So the limit takes the data and solves [[eq:iv5-5-16]]. For
uniqueness, let
ω ∈ ρ_sf^(α_sf)ρ_K^(α_K)H̄¹_3b(Ω) solve [[eq:iv5-5-16]] with f = 0 and vanishing data. Its extension by zero across X_0
is a distribution supported in {t ≥ 0} with P_hω = 0, the vanishing data leaving no layer on X_0; so ω = 0 by the
uniqueness in (a). ∎

**Remark {#rem:iv5-7-4}** (In the coordinates of [[sec:iii-b-3-1]].) There g_b = Φ_m*g, with
Φ_m(t, x) = (t − T_m(|x|), x) and T_m ∈ |x|⁻¹C^∞(X̄) near infinity ([[lem:iii-b-3-5]] (a)). Φ_m commutes with ∂_t and
acts on 1-forms by dt ↦ dt − T_m′ dr, where T_m′ ∈ |x|⁻²C^∞. Hence Φ_m intertwines □^C for (g, c_C) with □^C for
(g_b, Φ_m*c_C), and it preserves stationarity, 𝒜^γ(X̄; E), the weighted b-spaces on X̄, and integrals over
[0, ∞)_t × A for an annulus A, up to the shift by the bounded T_m. [[thm:iv4-2-1]] uses [[thm:iv5-7-3]] through this
intertwining, with its initial data at {t_KS = 0}.

#### Uniformity in b {#sec:iv5-8}

**Lemma {#lem:iv5-8-1}** The constants C and the thresholds h_0 in [[prop:iv5-1-2]]–[[prop:iv5-7-2]] and
[[thm:iv5-7-3]] can be taken uniform for b ∈ U.

*Proof.* Every estimate above is proved from three kinds of input, each uniform on U: finitely many seminorms of the
coefficients of P_h as an element of h²ρ_sf²Diff²_3b + hρ_sf²Diff¹_3b in the frames r∂_(z^μ), which are continuous in b
([[lem:iv5-0-2]] (a), (d), and the smooth dependence of [[sec:iii-b-3-1]]); the lower bounds in the positivity
statements, from [[lem:iv5-0-3]] (exact in (a)–(b) for all b ∈ ℬ, by continuity in (c)), [[lem:iv5-0-4]] (the
constant C and the margins of [[lem:iv4-1-causal]] (d) on compact sets) and [[lem:iv5-0-5]] (uniform by its
statement); and the cut-offs, commutants and the parameters 𝔛, δ, δ′, t_j, r_j, κ, chosen from these bounds alone,
hence independently of b. The calculus facts used ([[prop:np-10-65-a]], [[lem:iv5-calc-garding]] and
[[lem:iv5-calc-q0]]) hold with constants uniform in b by [[prop:np-10-65-a]] (j): the coefficients of P_h and of Q_0,
Q_1, the symbols of the commutants, of their square roots and of the auxiliary operators, the ellipticity bounds and the
positivity margins are bounded uniformly for b ∈ U. In particular the constant 9C₂ + 2 in the proof of [[prop:iv5-2-1]]
is uniform, C₂ being the supremum of a symbol continuous in b over a compact set, and for each fixed 𝔛 the constant C_𝔛
is uniform, the square root in [[lem:iv5-calc-garding]] having the margin η = 𝔛⁻² for every b. Each absorption step
needs h below a threshold determined by these quantities. So each h_0 and C is
uniform on U, after shrinking U to a compact neighbourhood. ∎

### The transition face model {#sec:iv6}

This section proves that □^C_b is tf-admissible with every weight in [−C_0, 2) ([[thm:iii-e-1-1]] (4)), through
[Hin26a, Theorem B.1] in dimension 4 + 1 ([[thm:iv6-3-1]]): the invertibility of the spectral family of the
dilation-invariant model on 4 + 1 Minkowski space, which is the transition face normal operator of □^C_b. The proof has
three steps, as in [Hin26a, Appendix B, pp. 85–98]: the Fredholm property and index 0 ([[sec:iv6-1]]), by radial
estimates and the relative index formula of [[lem:iii-f1-3-1]] (for b-elliptic operators on compact manifolds with
boundary this is Melrose's [[thm:std-relative-index]]), with the indicial roots counted by type and degree on 𝕊³;
solvability on edge-b spaces
([[sec:iv6-2]]), by the arguments of [[sec:iv5]]; and the kernel argument of [Hin26a, Section B.4] ([[sec:iv6-3]]).
[[sec:iv6-4]] identifies the spaces with those of [[sec:i-c-4]] and verifies [[def:i-c-5-1]].

#### The model in dimension 4 + 1 {#sec:iv6-0}

Let v := 1/2, e := 1/102400, h ∈ (0, 10⁻⁶], γ_C = h⁻¹ and C_0 ∈ [3/2, 100]. On Minkowski space ℝ_t × ℝ⁴_x,
η = −dt² + dr² + r²𝑔̸, 𝑔̸ the round metric of 𝕊³. Let c := r⁻¹(dt − v dr) ([Hin26a, (B.1)]) and
□^C := 2δ_ηG_η(δ*_η + E^C), with E^C the modification of [[sec:iv4-0]] (trace weight 2/3). As there,
h²□^C = 2h²δGδ* − iL_h with L_h = 4ihδ(c ⊗_s ·) + 2ihe dι_(c♯). Let M := [ℝ̄^(1+4); {r = 0}] ([Hin26a, (B.3)]), with
faces 𝗌𝖿 (the lift of ∂ℝ̄^(1+4)) and 𝖼𝖿 (the lift of {r = 0}). Let 𝒯* be the pullback of the scattering cotangent
bundle, with frame dt, dx¹, …, dx⁴. Let X := [ℝ̄⁴; {0}] = [0, ∞]_ρ × 𝕊³, ρ = r⁻¹, and 𝒯*_X := 𝒯*|_X. In t_* := t − r,
the spectral family is

    (□^C)^(σ) := e^(iσt_*) □^C e^(−iσt_*) on stationary sections,     σ ∈ ℂ ∖ 0, Im σ ≥ 0.                  {#eq:iv6-0-1}

**Lemma {#lem:s14-tf-inputs}** (The model's homogeneity, weights and thresholds.) (i) In the frame dt, dx^i and in
(t_*, x), the coefficient of every derivative of order k in □^C is homogeneous of degree k − 2 in x.

(ii) For real ι, r^ι lies in r^β L²(r³ dr) near r = 0 iff ι > β − 2. So if the indicial roots of (□^C)^(0) in ρ at
infinity avoid [−C_0, 2), those in r at the origin, which are their negatives, avoid (−2, C_0], and the root-free weights
at the origin are β ∈ (0, 2 + C_0].

(iii) The symbol T of [[prop:np-10-14]] (iv) at ρ_K = 0 with d = 1 − α_cf is positive definite iff α_cf > 1 − b*; and
−½r²ℓ(dr/r) has characteristic polynomial (ν − v)³(ν² − (3 − e)vν + (2 − e)v² − e), whose roots are positive at
(v, e) = (1/2, 1/102400), and at e = 0 for every v > 0.

(iv) (α_sf, α_cf) = (−5/2, 5/2) satisfies α_sf < b* − 1 and α_cf > 1 − b*, and 2(α_sf + α_cf) = 0; ℓ = −½ satisfies
−½ − h⁻¹(1 − e)(1 + v) < ℓ < −½ + h⁻¹(1 − e)(1 − v) for every h > 0; β = 7/2 lies in (0, 2 + C_0] iff C_0 ≥ 3/2; and in
(τ = t/r, r) the density |dg| = r⁴|dt (dr/r) d𝑔̸| is r|dτ| times r³|dr d𝑔̸|.

(v) The free 1-form wave operator 2δGδ* = □_η has at the origin the indicial roots −3, −2 | 0, 1 in the scalar sector
l = 0, −l − 3, −l − 2, −l − 1 | l − 1, l, l + 1 in the scalar sector l ≥ 1, and −l − 2 | l in the vector sector, each
simple; the window of β − 2 between the two groups contains (−2, 0).

*Proof.* (i) η has constant components and vanishing Christoffel symbols in (t, x), so □_η = ∂_t² − Δ acts
componentwise, homogeneous of degree −2; the components of c are homogeneous of degree −1, those of ∇c of degree −2,
and by [[eq:s14-lc]] every term of h⁻¹𝓛_c is a product of a component of c with a first derivative or of a component of
∇c with the identity. The change to t_* = t − r preserves the homogeneity, r being homogeneous of degree 1. (ii) ∫_0
r^(2ι−2β)r³ dr < ∞ iff 2ι − 2β + 4 > 0. By (i) and the inversion ρ = r⁻¹, the indicial roots at the origin are the
negatives of those at infinity. (iii) The first statement is [[prop:np-10-14]] (iv) with b_sf − b_K = d. For the
second, with ζ = dr/r, ⟨c, ζ⟩ = −v r⁻², G(c) = −(1 − v²)r⁻², G(ζ) = r⁻²; by [[prop:np-10-13]] (i), ½ℓ(ζ) has eigenvalue
−vr⁻² three times and on span{c, ζ} trace −(3 − e)vr⁻² and determinant (2(1 − e)v² − e(1 − v²))r⁻⁴; multiplying by −r²
gives (ν − v)³(ν² − (3 − e)vν + (2 − e)v² − e). At (1/2, 1/102400) the quadratic has positive sum (3 − e)/2 and
positive product (2 − e)/4 − e; at e = 0 its roots are v and 2v. (iv) is arithmetic, with b* ∈ (0.9934, 0.9935) and
dt = r dτ + τ dr. (v) On stationary sections □_η = −Δ componentwise in the frame dt, dx^i. A section of scalar type l
has its dt-component r^ιS, with −Δ(r^ιS) = 0 at leading order iff ι ∈ {l, −l − 2}, and its spatial part a 1-form whose
Cartesian components are, at each order r^ι, combinations of harmonics of degree l ± 1 (for l = 0, of degree 1 only),
with the roots ι ∈ {l − 1, −l − 1} and {l + 1, −l − 3}; a section of vector type has Cartesian components of degree l,
with roots {l, −l − 2}. These are simple, and each group of three (two at l = 0, one for the vector type) lies on one
side of (−2, 0). ∎

**Lemma {#lem:iv6-0-1}** (The structure; [Hin26a, (B.7)–(B.12)] in dimension 4 + 1.)

(a) □^C is homogeneous of degree −2 under (t, x) ↦ (λt, λx), the components of a section being taken in the frame dt,
dx^i; so r²(□^C)^(0) ∈ Diff²_b(X; 𝒯*_X) is dilation invariant.

(b) In the splitting of 𝒯*_X by dr, dt_* = dt − dr and r dω,

    (□^C)^(σ) = 2iσρ(ρ∂_ρ − 3/2 − h⁻¹S̄) + (□^C)^(0),     (□^C)^(0) ∈ ρ²Diff²_b(X; 𝒯*_X),                   {#eq:iv6-0-2}

where S̄ = M of [[prop:np-10-21]] is constant and lower triangular with diagonal 2(1 − v), (1 − e)(1 − v) and
(1 − v)Id_(T*𝕊³); it is diagonalisable with spectrum {2(1 − v), (1 − e)(1 − v), 1 − v}, the last three times.

(c) (□^C)^(σ) ∈ ρ_b⁻²Diff²_(sc,b)(X; 𝒯*_X), with ρ_sc := ρ/(ρ + 1) and ρ_b := r/(r + 1). The b-principal symbol of
r²(□^C)^(σ) near r = 0 is ξ_b² + |η_b|², and the scattering principal symbol near ρ = 0 is
G_σ(ξ, η) = −2σξ + ξ² + |η|².

(d) (□^C)^(σ) is the transition face normal operator of □^C_b for every b near b₀: N_tf(σ̂) = (□^C)^(σ̂) in
[[eq:i-c-4-1]], with S_0 = h⁻¹S̄ = S̄^C and N(P^(0)) the normal operator of ρ⁻²(□^C)^(0).

*Proof.* (a) is [[lem:s14-tf-inputs]] (i). (b) The form [[eq:iv6-0-2]] is [[eq:iv4-1-1]] on the model, where S̃, Q and R
vanish (g = η and c exactly r⁻¹(dt − v dr); [[prop:np-10-21]] (i)). The 3/2 = (n − 1)/2 is the shift that makes
i(ρ²∂_ρ − kρ) symmetric on L²(ρ⁻⁴dρ/ρ): integrating by parts, i(ρ²∂_ρ − kρ) has adjoint i(ρ²∂_ρ + (1 − a + k)ρ) on
L²(ρ^(−a)dρ/ρ), symmetric iff k = (a − 1)/2, and here a = 4. Diagonalisability: the 2 × 2 block has the distinct
eigenvalues 2(1 − v) ≠ (1 − e)(1 − v), and the angular block is scalar. (c) The memberships follow from
[[eq:iv6-0-2]] and (a). The symbols are computed from ρ²(ρ∂_ρ)², ρ²Δ_(𝕊³) and 2iσρ²∂_ρ; the Diff¹_b-terms of (□^C)^(0)
are subprincipal at both ends. (d) [[eq:i-c-4-1]] defines N_tf from the data of P̂ at ρ = 0, namely S_0 and N(P^(0)).
[[lem:iv4-1-2]] gives these for □^C_b as S̄^C = h⁻¹S̄ and the normal operator of the model, independent of b
(g_b − η ∈ ρ²C^∞, and c_C minus the model's 1-form in ρ³C^∞, as in the proof of [[lem:iv4-1-3]]). The model's spectral
family is [[eq:iv6-0-2]], so the two agree. t_* differs from the t − ψ(|x|) of [[thm:iv4-2-1]] by a constant plus O(ρ),
which does not change the data at ρ = 0. ∎

*Spaces.* H^(s,(ℓ,β))_(sc,b) := ρ_sc^ℓ ρ_b^β H^s_(sc,b)(X; 𝒯*_X), with L² taken for the Euclidean density
r³|dr d𝑔̸| = ρ⁻⁴(dρ/ρ)|d𝑔̸| and a fibre inner product fixed below. ℓ may be a variable order on
^(sc)T*_(∂_sc X)X. Near r = 0, H^(s,β)_b(r³ dr) = H^(s,β−2)_b(dr/r): the b-weight is β − 2
([[lem:s14-tf-inputs]] (ii)). The radial sets over ρ = 0 for σ = ±1 are R_out := {ξ = η = 0} (the zero section) and
R_in := {ξ = 2σ, η = 0}, and for Im σ > 0 the characteristic set over ρ = 0 is R_out ([[lem:iv6-0-flow]]).

**Lemma {#lem:iv6-0-flow}** (The scattering Hamilton flow over ρ = 0; [Hin26a, (B.15)–(B.18) and (B.23)] in dimension
4 + 1.) Write the scattering covectors over {ρ < 1} as ξ dρ/ρ² + rη, with ξ ∈ ℝ, η ∈ T*𝕊³ and |η| the round norm. For
a function p of (ρ, ω, ξ, η), smooth up to ρ = 0, its Hamilton vector field on T*X° is H_p = ρ𝖧_p, where

    𝖧_p = (∂_ξp)(ρ∂_ρ + η·∂_η) − (ρ∂_ρp + η·∂_ηp)∂_ξ + H^(𝕊³)_p,                                        {#eq:iv6-0-flow}

H^(𝕊³)_p is the Hamilton vector field of p(ρ, ·, ξ, ·) on T*𝕊³ and η·∂_η the radial vector field of T*𝕊³; so 𝖧_p is
smooth up to ρ = 0 and tangent to it. For σ ∈ ℂ ∖ 0 put κ := Re σ⁻¹, p_σ := κ(ξ² + |η|²) − 2ξ and
q_σ := −(Im σ⁻¹)(ξ² + |η|²), so that σ⁻¹G_σ = p_σ − iq_σ for the symbol G_σ of [[lem:iv6-0-1]] (c), and q_σ ≥ 0 if
Im σ ≥ 0.

(a) If Im σ > 0, G_σ vanishes at real (ξ, η) only at ξ = η = 0; so the characteristic set over ρ = 0 is R_out.

(b) Let σ = ±1. Then p_σ = σG_σ, and Char_σ := {ρ = 0, G_σ = 0} is the sphere (ξ − σ)² + |η|² = 1 in each fibre over
𝕊³. On Char_σ, 𝖧_(p_σ) = σ𝖧_(G_σ) vanishes exactly at R_in ∪ R_out; every maximal integral curve of 𝖧_(p_σ) in
Char_σ ∖ (R_in ∪ R_out) is defined for all times and tends to R_in as s → −∞ and to R_out as s → +∞, uniformly for
initial points in a compact set; and ρ⁻¹𝖧_(p_σ)ρ = 2 at R_in and −2 at R_out.

(c) Let |σ| = 1, ℓ ∈ ℝ and a := ρ^(−ℓ−½)χ_0(ρ)χ₁(|η|²)χ₂(ξ), with χ_j ≥ 0 smooth, χ_0′ ≤ 0, χ₁′ ≤ 0,
supp χ₁ ⊂ (−∞, 1/16] and supp χ₂ ⊂ [−¼, ¼]. Then

    𝖧_(p_σ)a = ρ^(−ℓ−½)((2ℓ + 1)(1 − κξ)χ_0χ₁χ₂ + 2(κξ − 1)ρχ_0′χ₁χ₂ + 4(κξ − 1)|η|²χ_0χ₁′χ₂ − 2κ|η|²χ_0χ₁χ₂′),

and on supp a, 1 − κξ ∈ [¾, 5/4] and κξ − 1 ≤ −¾. So the principal symbol aH_(p_σ)a = ρa𝖧_(p_σ)a of (i/2)[P, A²],
for an operator P with principal symbol p_σ and A with symbol a, is ρ times the sum of the main term
(2ℓ + 1)(1 − κξ)a², which has the sign of 2ℓ + 1, a term ≥ 0 supported in supp χ_0′, a term ≥ 0 supported in
supp χ₁′, and a term supported in supp χ₂′; these signs and supports, and the bounds of the four terms, are the same
for every σ with |σ| = 1.

*Proof.* In the coordinates (ρ, ω), the covector ξ dρ/ρ² + rη has the canonical fibre coordinates P = ρ⁻²ξ and
W = ρ⁻¹η, η being taken in the coordinates of T*𝕊³ dual to ω. So ∂_P = ρ²∂_ξ, ∂_W = ρ∂_η and
∂_ρ|_(P,W) = ∂_ρ + 2ρ⁻¹ξ∂_ξ + ρ⁻¹η·∂_η. Inserting these into H_p = (∂_Pp)∂_ρ − (∂_ρp)∂_P + ∂_Wp·∂_ω − ∂_ωp·∂_W, in
which ∂_ρ is taken at fixed (ω, P, W), the terms ±2ρξ(∂_ξp)∂_ξ cancel and [[eq:iv6-0-flow]] follows. (At ρ = 0 it is
[[eq:i-a-4-4]] with ξ replaced by −ξ, the covector being written ξ dr + rη there.) As 𝖧_pp = ρ⁻¹H_pp = 0, 𝖧_(p_σ) is
tangent to the level sets of p_σ.

(a) Im G_σ = −2(Im σ)ξ vanishes only at ξ = 0, and then G_σ = |η|².

(b) For σ = ±1, σ⁻¹ = σ is real, so q_σ = 0, p_σ = σG_σ and G_σ = (ξ − σ)² + |η|² − 1. By [[eq:iv6-0-flow]], with
H_(|η|²) the geodesic vector field of T*𝕊³,

    𝖧_(p_σ) = 2(σξ − 1)(ρ∂_ρ + η·∂_η) − 2σ|η|²∂_ξ + σH_(|η|²),     ρ⁻¹𝖧_(p_σ)ρ = 2(σξ − 1).

This vanishes at ρ = 0 where η = 0, and 𝖧_(p_σ)ξ = −2σ|η|² ≠ 0 where η ≠ 0; on Char_σ, η = 0 exactly at R_in, where
ξ = 2σ, and at R_out, where ξ = 0. On Char_σ, y := σξ − 1 = σ(ξ − σ) lies in [−1, 1], |η|² = 1 − y², and along an
integral curve ẏ = σ𝖧_(p_σ)ξ = −2(1 − y²). The solutions with |y| < 1 are y(s) = −tanh(2(s − s_0)), defined for all s
and tending to 1 as s → −∞ and to −1 as s → +∞, with s_0 continuous in the initial point; so ξ tends to 2σ, resp. 0,
and |η| = sech(2(s − s_0)) tends to 0. The ω-component of 𝖧_(p_σ) is that of σH_(|η|²), of length 2|η|, which is
integrable in s; so ω converges as s → ±∞, uniformly for initial points in a compact set. At R_in, y = 1 and
ρ⁻¹𝖧_(p_σ)ρ = 2; at R_out, y = −1 and ρ⁻¹𝖧_(p_σ)ρ = −2.

(c) p_σ does not depend on ρ, so by [[eq:iv6-0-flow]] 𝖧_(p_σ) = 2(κξ − 1)(ρ∂_ρ + η·∂_η) − 2κ|η|²∂_ξ + κH_(|η|²). Hence
𝖧_(p_σ)ρ^(−ℓ−½) = (2ℓ + 1)(1 − κξ)ρ^(−ℓ−½), 𝖧_(p_σ)χ_0(ρ) = 2(κξ − 1)ρχ_0′, 𝖧_(p_σ)χ₁(|η|²) = 4(κξ − 1)|η|²χ₁′, as
η·∂_η|η|² = 2|η|² and H_(|η|²)|η|² = 0, and 𝖧_(p_σ)χ₂(ξ) = −2κ|η|²χ₂′. On supp a, |κξ| ≤ ¼ as |κ| = |Re σ̄| ≤ 1,
which gives the two ranges. The signs follow from χ_0χ_0′ ≤ 0 and χ₁χ₁′ ≤ 0. ∎

**Definition {#def:iv6-0-2}** (Admissible orders; [Hin26a, (B.13)] in dimension 4 + 1.) For real σ₀ ≠ 0 let
R_(σ₀,in) := {ρ = 0, ξ = 2σ₀, η = 0} and Char_(σ₀) := {ρ = 0, G_(σ₀) = 0}, with the real symbol G_(σ₀) of
[[lem:iv6-0-1]] (c); for σ₀ = ±1 these are the R_in of [[sec:iv6-0]] and the Char_σ of [[lem:iv6-0-flow]] (b). For
σ ∈ ℂ ∖ 0 with Im σ ≥ 0, (s, ℓ, β) is *admissible at σ* if β ∈ (0, 2 + C_0], ℓ is constant near R_out with
ℓ < −½ + h⁻¹(1 − e)(1 − v) there, and, when σ is real, ℓ is also constant near R_(σ,in) with
ℓ > −½ − h⁻¹(1 − e)(1 + v) there and σ𝖧_(G_σ)ℓ ≤ 0 on Char_σ, 𝖧 as in [[eq:iv6-0-flow]]. For Im σ > 0 nothing is
asked off R_out, which is then the whole characteristic set over ρ = 0 ([[lem:iv6-0-flow]] (a)). Fixed orders are
*admissible on* a set of such σ if they are admissible at every σ of the set and at Re σ for every σ of the set with
Re σ ≠ 0: as in [[sec:i-a-1-4]], the orders used at a complex σ are those for Re σ.

#### Fredholm property and index 0 {#sec:iv6-1}

**Proposition {#prop:iv6-1-1}** ([Hin26a, Proposition B.2] in dimension 4 + 1.) For (s, ℓ, β) admissible at
σ ∈ e^(i[0,π]),

    (□^C)^(σ) : {ω ∈ H^(s,(ℓ,β))_(sc,b) : (□^C)^(σ)ω ∈ H^(s−2,(ℓ+1,β−2))_(sc,b)}
                  → H^(s−2,(ℓ+1,β−2))_(sc,b)                                                             {#eq:iv6-1-1}

is Fredholm of index 0, and its nullspace and the annihilator of its range do not depend on the admissible (s, ℓ, β).
The estimate

    ‖ω‖_(H^(s,(ℓ,β))_(sc,b)) ≤ C(‖(□^C)^(σ)ω‖_(H^(s−2,(ℓ+1,β−2))_(sc,b)) + ‖ω‖_(H^(s_0,(ℓ_0,β_0))_(sc,b)))  {#eq:iv6-1-2}

(for admissible s_0 < s, ℓ_0 < ℓ, β_0 < β, in the strong sense) and its dual

    ‖ω‖_(H^(−s+2,(−ℓ−1,−β+2))_(sc,b)) ≤ C(‖((□^C)^(σ))*ω‖_(H^(−s,(−ℓ,−β))_(sc,b)) + ‖ω‖_(H^(s_1,(ℓ_1,β_1))_(sc,b)))
                                                                                                          {#eq:iv6-1-3}

(for s_1 < −s + 2, β_1 < −β + 2 and ℓ_1 < −ℓ − 1 with ℓ_1 > −½ − h⁻¹(1 − e)(1 − v) near R_out, in the strong sense,
the adjoint being taken for the L² pairing of these spaces; [Hin26a, (B.28)]) hold uniformly for σ in e^(i[0,π−δ]) near
1 and in e^(i[δ,π]) near −1, for fixed orders admissible on that set ([[def:iv6-0-2]]).

*Proof.* *Real σ*, say σ = 1 (σ = −1 by reversing the propagation). Off the characteristic set the operator is elliptic,
by [[lem:iv6-0-1]] (c). Over ρ = 0:

- *Sink R_out.* With the commutant a = ρ^(−ℓ−½)χ_0(ρ)χ₁(|η|²)χ₂(ξ) ([Hin26a, (B.21)]), the principal symbol of
(i/2)[(□^C)^(σ), A²] is aH_(G_σ)a = ρa𝖧_(p_σ)a, given by [[lem:iv6-0-flow]] (c) ([Hin26a, (B.23)]). That of
(2i)⁻¹((□^C)^(σ) − (□^C)^(σ)*)A² is a²ρ times the principal symbol of (2iρ)⁻¹((□^C)^(σ) − (□^C)^(σ)*), whose value at
the zero section, the shift, adds to the coefficient (2ℓ + 1)σ of the main term. By [[lem:iv6-0-1]] the shift
comes only from −2iσρh⁻¹S̄: (□^C)^(0) − (□^C)^(0)* ∈ ρ²Diff¹_b ([[rem:i-a-hypotheses]] (a)), whose quotient by ρ has
scattering symbol vanishing at
(ξ, η) = 0; and 2iσ(ρ²∂_ρ − (3/2)ρ) is symmetric on L²(ρ⁻⁴dρ/ρ) ([[lem:iv6-0-1]] (b)), so its imaginary part lies in
ρ²C^∞ for any fibre inner product. Taking the fibre inner product for which an eigenbasis of S̄ is orthonormal
([[lem:iv6-0-1]] (b)), the shift is −2h⁻¹S̄. So the principal symbol of the commutator term is
ρ^(−2ℓ)((2ℓ + 1)(σ − ξ) − 2h⁻¹S̄ + O(|ξ| + |η|))χ_0²χ₁²χ₂² plus the three cut-off terms of [[lem:iv6-0-flow]] (c)
([Hin26a, (B.25)]). The main term (2ℓ + 1)(σ − ξ) − 2h⁻¹S̄ is negative near the zero section iff
ℓ < −½ + h⁻¹ min spec S̄ = −½ + h⁻¹(1 − e)(1 − v), the threshold of [[def:iv6-0-2]] at R_out.

- *The incoming radial set R_in.* The isometry t ↦ −t of η pulls c_v := r⁻¹(dt − v dr) back to −c_(−v), so it
conjugates □^C with (c_v, h⁻¹) to the operator with (c_(−v), −h⁻¹) ([[prop:np-10-21]] (ii)). On stationary sections,
e^(2iσr)(□^C)^(σ)e^(−2iσr) is the pullback of the spectral family at −σ of that operator ([Hin26a, (B.27)]): with
Φ(t, x) := (−t, x) and t_* = t − r, Φ*(e^(−iσt_*)u) = e^(−i(−σ)t_*)e^(2iσr)Φ*u for stationary u, as
t_* ∘ Φ = −t_* − 2r, and Φ* maps stationary sections to stationary sections. With an eigenbasis of S̄_(−v)
orthonormal, the shift at R_in is (−1)(−2(−h⁻¹)S̄_(−v)). S̄_(−v) has spectrum {2(1 + v), (1 − e)(1 + v), 1 + v}, with
bottom (1 − e)(1 + v). The threshold is ℓ > −½ − h⁻¹(1 − e)(1 + v).

- In between, real principal type propagation ([[prop:i-a-5-2]], with [[rem:i-a-5-2-uses]] (ii)) applies along
Char_σ, which flows from R_in to R_out by [[lem:iv6-0-flow]] (b).

*The estimates.* These three commutator arguments are those of the estimates of [[ch:s01]] at the boundary face over
∂X, which give them: the pieces (C), (D), (E) and (F) of the proof of [[thm:i-a-7-2]] (1) ([[sec:i-a-7-1]]), namely
[[prop:i-a-4-6]] at R_in, [[prop:i-a-5-2]] with [[rem:i-a-5-2-uses]] (ii) along Char_σ, [[prop:i-a-4-9]] at R_out and
the elliptic estimate [[prop:i-a-5-1]] off Char_σ. These use only the form (H1)–(H2) of [[sec:i-a-1-3]] on {ρ < ρ_1},
their commutants being microsupported at the boundary face, and near ρ = 0, (□^C)^(σ) = (□^C)^(0) + σT has this form
with T := 2iρ(ρ∂_ρ − 3/2 − h⁻¹S̄), S = h⁻¹S̄, Q = 0 and P₂ = 0 ([[eq:iv6-0-2]]; the ξ of [[ch:s01]] is −ξ here). Their
thresholds are those found above: in the fibre inner product for which an eigenbasis of S̄ is orthonormal, S̄ is
self-adjoint and ½ inf min spec(S + S^(*h)) = h⁻¹(1 − e)(1 − v) in [[prop:i-a-4-9]]; and ϑ_in = −2h⁻¹(1 − e)(1 + v)
([[eq:s14-theta-in]]), so that (−1 + ϑ_in)/2 = −½ − h⁻¹(1 − e)(1 + v) in [[prop:i-a-4-6]]. So an order admissible at
σ ([[def:iv6-0-2]]) satisfies the conditions of these estimates at σ₀ := σ. Moreover (□^C)^(σ) = N_tf(σ) for
P̂ := (□^C_b)^ ([[lem:iv6-0-1]] (d)), which satisfies (H1)–(H2) ([[lem:iv4-1-6]]) with the indicial gap (β_−, 2), and
2 − β ∈ [−C_0, 2) lies in that gap. So the proof of [[thm:i-c-4-3]] (1) ([[sec:i-c-4-4]]) applies with q := β and with
these estimates at σ₀ := σ in place of those of [[thm:i-a-7-2]] (1): near the boundary at infinity the pieces, the a
priori term at R_in being absorbed as there; in the interior the elliptic estimate (K2) of [[sec:i-c-2-1]]; and near
r = 0 [[lem:i-c-2-5]] and [[lem:i-c-2-6]] for L := r²(□^C)^(σ), which is b-elliptic with the normal operator of
r²(□^C)^(0) ([[lem:iv6-0-1]] (c), the terms with σ being O(r)), at the b-weight β − 2 ([[lem:s14-tf-inputs]] (ii)). By
[[lem:iv6-0-1]] (a) and the inversion ρ = r⁻¹, the indicial roots at r = 0 are −ι, with ι running over those of
[[lem:iv4-1-3]] at infinity. These have Re ι ∉ [−100, 19/10], and only ι = 2 in [−100, 2]. So no root at 0 has real
part in (−2, 100], and β − 2 ∈ (−2, C_0] is not the real part of a root. This gives, for every M and every ω in the
domain of [[eq:iv6-1-1]],

    ‖ω‖_(H^(s,(ℓ,β))_(sc,b)) ≤ C(‖(□^C)^(σ)ω‖_(H^(s−2,(ℓ+1,β−2))_(sc,b)) + ‖ω‖_(H^(−M,(−M,−M))_(sc,b)))     {#eq:iv6-1-4}

([Hin26a, (B.19)–(B.20)]), which implies [[eq:iv6-1-2]]; its strong sense is that of the pieces ([[rem:i-a-7-3]]) and
of [[lem:i-c-2-5]]. The adjoint chain of the same proof (the estimates (2) of
[[prop:i-a-4-6]] and [[prop:i-a-4-9]], [[prop:i-a-5-2]] along the backward field, and near r = 0 [[lem:i-c-2-5]] and
[[lem:i-c-2-6]] for the normal operator of the adjoint) gives [[eq:iv6-1-3]] with the error term
‖ω‖_(H^(−M,(−M,−M))_(sc,b)), which is smaller, for ω in the domain, and in the strong sense with the a priori orders of
[[eq:iv6-1-3]] ([[rem:i-a-7-3]]).

*Complex σ.* Only R_out is characteristic over ρ = 0 ([[lem:iv6-0-flow]] (a)); so off R_out the elliptic estimate
[[prop:i-a-5-1]] applies at the boundary face, and at R_out [[prop:i-a-4-9]] (1), for σ in any compact subset of
{σ ≠ 0, Im σ ≥ 0}, with the threshold found above. With ℓ constant near R_out and below that threshold, the proof of
[[thm:i-c-4-3]] (2) applies as for real σ and gives [[eq:iv6-1-4]] and the dual estimate.

*Uniformity* in σ near ±1 is the limiting absorption principle. At R_out, [[lem:iv6-0-flow]] (c), with the same
cut-offs for every σ ∈ e^(i[0,π]), gives the main term (2ℓ + 1)(1 − κξ)a², where |κξ| ≤ δ₂ on supp a if
supp χ₂ ⊂ [−δ₂, δ₂]. Take δ₂ ∈ (0, ¼] with δ₂|2ℓ + 1| < m, m := 2h⁻¹(1 − e)(1 − v) − (2ℓ + 1) > 0 the margin of ℓ at
R_out; then (2ℓ + 1)(1 − κξ) − 2h⁻¹S̄ ≤ −(m − δ₂|2ℓ + 1|) < 0 on supp a for every σ; and the lemma gives
cut-off terms whose signs, supports and bounds do not depend on σ; the zero-section term (2ℓ + 1 − 2h⁻¹S̄)ρ^(−2ℓ) does
not depend on σ either, and the absorption (Im σ)Re (□^C)^(0) has the sign of the main term, as
(□^C)^(0) = Σ_jT_j*T_j + R with T_j ∈ ρDiff¹_b and R ∈ ρ²Diff¹_b, its b-principal symbol being ξ_b² + |η_b|²
near ρ = 0 ((H2) of [[sec:i-a-1-3]], which (□^C)^(σ) satisfies, as above). So the estimate at R_out holds with constants
uniform on e^(i[0,π]), as in [[prop:i-a-4-9]]. Over the rest of ρ = 0 the estimates are microlocal near ρ = 0, where
(□^C)^(σ) = (□^C)^(0) + σT has the form (H1)–(H2) of [[sec:i-a-1-3]], with T = 2iρ(ρ∂_ρ − 3/2 − h⁻¹S̄), Q = 0 and
P₂ = 0 ([[eq:iv6-0-2]]; the ξ of [[ch:s01]] is −ξ here), and with ϑ_in as in [[eq:s14-theta-in]]. So the radial
estimate at R_(Re σ,in) and the propagation along Char_(Re σ) are [[prop:i-a-4-6]] and [[prop:i-a-5-2]], with
[[rem:i-a-5-2-uses]] (ii) for the absorption (Im σ)Re T. Their constants are uniform for σ ∈ I + i[0, ν], I the
compact interval of the Re σ, σ in the given set near ±1, which does not contain 0 (for [[prop:i-a-5-2]] by the
argument of the proof of [[thm:i-a-7-2]] (1)): the orders are admissible on that set ([[def:iv6-0-2]]), hence at every
real σ₀ ∈ I, with uniform margins and constancy neighbourhoods, as ℓ is continuous and constant near each R_(σ₀,in),
σ₀ ∈ I, hence near the compact connected union of these. The orders constructed in the proof of [[lem:i-a-7-1]] are of
this kind. Near r = 0 the normal operator of r²(□^C)^(σ) does not depend on σ, the terms with σ being O(r) there.

So [[eq:iv6-1-1]] is Fredholm, and by [[eq:iv6-1-2]] and elliptic and propagation regularity its nullspace consists of
elements in every admissible space; it is the same for every admissible (s, ℓ, β). The annihilator of the range is the
nullspace of the adjoint on the dual spaces; by the dual estimate and the propagation regularity of the adjoint it too
consists of elements of every dual space, so it does not depend on the orders either, as in the proof of
[[thm:i-c-4-3]] (3). Hence the index does not depend on the admissible orders.

*Index 0.* As the index does not depend on the admissible orders, we find it for s := 2, the given β and ℓ the order
of [[ch:s03]] for the free operator at this σ = e^(iθ): that of [[lem:i-a-7-1]] with ϑ_in = 0 and S̄ = 0 for
θ ∈ {0, π}, which is > −½ at R_in and < −½ at R_out, or a constant 𝗋_mid < −½ for θ ∈ (0, π), where only R_out
enters ([[def:iv6-0-2]]); so it is admissible for every h⁻¹ ≥ 0. For λ ∈ [0, 1] let P̂_λ be the spectral family of
□^C_b with γ_C replaced by λh⁻¹. It satisfies (H1)–(H2) of [[sec:i-a-1-3]], by the proof of [[lem:iv4-1-6]], whose
(H1)–(H2) part does not use the value of γ_C. Its transition
face normal operator N_tf(P̂_λ, ·) is (□^C)^(·) with h⁻¹ replaced by λh⁻¹, by the proof of [[lem:iv6-0-1]] (d); at
λ = 0 it is the spectral family of □_η = 2δ_ηG_ηδ*_η, which acts componentwise in the frame dt, dx^i
([[lem:s14-box-c]], Ric(η) = 0). The thresholds of P̂_λ at R_out and at R_in are −½ + λh⁻¹(1 − e)(1 − v) ≥ −½ and
−½ − λh⁻¹(1 − e)(1 + v) ≤ −½ ([[prop:np-10-21]], [[eq:s14-theta-in]]). So these orders are allowed in
[[thm:i-c-4-3]] (1)–(2) for every λ, and with them the map [[eq:iv6-1-1]], with N_tf(P̂_λ, e^(iθ)) in place of
(□^C)^(σ), is the map 𝒳_(tf,θ) → 𝒴_(tf,θ) of [[sec:i-c-4]] for P̂_λ at q = β ([[sec:iv6-4]]). For γ ∈ ℝ that is
not the real part of an indicial root of P̂_λ(0), let ind_λ(γ) be the index of this map at q = 2 − γ, which is
Fredholm by [[thm:i-c-4-3]] (3); this is the index of [[sec:iii-f1-3]] at the weight γ. The index to be found is
ind_1(2 − β), and 2 − β ∈ [−C_0, 2).

For λ ∈ [0, 1] let I_λ be the indicial family ([[eq:i-c-1-3]]) of P̂_λ(0). It is that of ρ⁻²(□^C)^(0) with h⁻¹
replaced by λh⁻¹ (the proof of [[lem:iv4-1-3]]), of the form of [[lem:i-c-2-4]], with coefficients affine in λ that
commute with the action of SO(4) rotating both 𝕊³ and the Cartesian components. For an irreducible representation π
of SO(4) let W_π, the π-isotypic subspace of C^∞(𝕊³; ℂ⁵), and d(π) be as in [[lem:iii-f1-2-4]]; sums over π below
run over the π with W_π ≠ 0. For γ ∈ ℝ let n_π(λ, γ) be the number of roots of I_λ on W_π with real part < γ, with
multiplicity. By *Types and representations* in [[sec:iii-f1-1]], W_π is ℂ^k ⊗ π for the type and degree of π, with
k = 2 at scalar type 0, k = 3 at scalar type l ≥ 1 and k = 1 at vector type, and I_λ(ι) acts on W_π as N(ι) ⊗ Id_π
for a k × k matrix N(ι). So det(I_λ(ι)|_(W_π)) = det(N(ι))^(dim π), and the roots on W_π are those of det N, each
with its multiplicity multiplied by dim π. At λ = 1, in the basis S dt, S dr, r dS (resp. rV) of [[prop:np-10-12]]
(ii), N is N_0, N_l or N_(v,l), so that det N is h⁻²P_0, h⁻³P_l or h⁻¹p_(v) ([[prop:np-10-12]] (iii)).

Let γ_* := C_0 + 2. By [[lem:iii-f1-2-4]] with 𝒯 = [0, 1], there is d_0 > γ_* such that for every λ and every π
with d(π) ≥ d_0 no root of I_λ on W_π has real part in [−γ_*, γ_*]. For λ ∈ [0, 1] and γ ∈ [−γ_*, γ_*] not the real
part of a root of I_λ put

    G(λ, γ) := ind_λ(γ) − Σ_π (n_π(λ, γ) − dim W_π).

The sum is finite. Each H_d ⊗ ℂ⁵, H_d the harmonics of degree d ((K4) of [[sec:i-c-2-1]]), is invariant under the
action of SO(4), so W_π is the sum of its intersections with these spaces, which vanish for d < d(π). At λ = 0, on
H_d ⊗ ℂ⁵, I_0(ι) = −ι² + 2ι + d(d + 2) = −(ι + d)(ι − d − 2), the free operator acting componentwise (the proof of
[[prop:i-c-5-3]]). So at λ = 0, W_π carries dim W_π roots ≤ −d(π) and dim W_π roots ≥ d(π) + 2; hence
n_π(0, γ) = dim W_π for γ ∈ (0, 2), and for every γ ∈ [−γ_*, γ_*] if d(π) ≥ d_0. In the latter case the roots on
W_π, which depend continuously on λ ([[lem:iii-f1-2-4]]), never have real part in [−γ_*, γ_*], so n_π(λ, γ) = dim W_π
for every λ. So the terms with d(π) ≥ d_0 vanish, and only finitely many π have d(π) < d_0.

G(λ, γ) does not depend on γ. Let γ₁ < γ₂ be two such weights, and choose γ₁ = w_0 < w_1 < … < w_M = γ₂ with
w_(i+1) − w_i < 1, none of them the real part of a root of I_λ; this is possible, as only finitely many roots have
real part in [γ₁, γ₂] ([[lem:i-c-2-4]] (b)). By [[lem:iii-f1-3-1]], applied to each pair (w_i, w_(i+1)) as its
weights (β_1, β_2), ind_λ(w_(i+1)) − ind_λ(w_i) is the number of roots of I_λ with real part in (w_i, w_(i+1)), with
multiplicity. Adding, ind_λ(γ₂) − ind_λ(γ₁) is the number of roots with real part in (γ₁, γ₂), which is the change of
the sum.

G(λ, γ) does not depend on λ. Let λ_0 ∈ [0, 1]. Only the finitely many W_π with d(π) < d_0 carry roots with real part
in [−γ_*, γ_*], and these roots depend continuously on λ; so there is γ ∈ (−γ_*, γ_*) that is not the real part of a
root of I_λ for any λ near λ_0. The terms with the factor λh⁻¹, namely −2iσλh⁻¹ρS̄ in [[eq:iv6-0-2]] and the part of
(□^C)^(0) that comes from λh⁻¹𝓛_c ([[lem:s14-box-c]]), which lies in ρ²Diff¹_b ([[lem:s14-tf-inputs]] (i)), map
H^(s,(ℓ,q))_(sc,b) boundedly into H^(s−2,(ℓ+1,q−2))_(sc,b). So the domain of the map does not depend on λ, the map
is continuous in λ in operator norm, and, being Fredholm, it has an index that is constant near λ_0; and every
n_π(λ, γ) is constant near λ_0, as no root crosses the line Re ι = γ. So G is constant near λ_0, and as [0, 1] is
connected, G(1, ·) = G(0, ·).

At λ = 0 and γ ∈ (0, 2), ind_0(γ) = 0: at ρ = 0, P̂_0 has the data of □_η acting componentwise, so it is
tf-admissible with every weight in (0, 2) ([[prop:i-c-5-3]]), and N_tf(P̂_0, e^(iθ)) is invertible at q = 2 − γ by
[[cor:i-c-5-2]] (a). As n_π(0, γ) = dim W_π for every π, G(0, γ) = 0. At λ = 1 and γ = 2 − β, no indicial root of
P̂_1(0) has real part in [−100, 2) ([[lem:iv4-1-3]] (a)), so n_π(1, 2 − β) is the number of roots on W_π with real
part < −100. With multiplicity, P_0 has two such roots, P_l (l ≥ 1) three and p_(v) one ([[prop:np-10-54]] (i)); so
n_π(1, 2 − β) = k dim π = dim W_π for every π. Hence ind_1(2 − β) = G(1, 2 − β) = G(0, 1) = 0, and the index of
[[eq:iv6-1-1]] is 0. ∎

#### Solvability on edge-b spaces {#sec:iv6-2}

On M the edge-b vector fields are spanned by r∂_t, r∂_(x^i). Unit cells
(2^j(k − 2), 2^j(k + 2))_t × (2^(j−2), 2^(j+2))_r × U̸_β, with U̸_β charts of 𝕊³, give the parameterised scaled bounded
geometry of [[def:iv5-calc-cells]], and [[prop:np-10-65-a]] (i) gives the semiclassical eb-calculus. On it
P_h := h²□^C = □_h − iL_h ∈ r⁻²Diff²_(eb,ħ)(M; 𝒯*) has principal symbol G − iℓ
([[lem:iv5-0-2]] (d) on the model). H^(s,(α_sf,α_cf))_(eb,h) is weighted with
L²(|dg|), |dg| = |dt dx| = r⁴|dt (dr/r) d𝑔̸|, and the fibre inner product B of [[lem:iv5-0-4]]. Let Ω := {t ≥ 0},
X_0 := {t = 0} and τ := t/r.

**Theorem {#thm:iv6-2-1}** ([Hin26a, Theorem B.4] in dimension 4 + 1.) Let α_sf < b* − 1 and α_cf > 1 − b*, with
b* = 0.99340731… the smaller root of 204795d² − 409605d + 204801, and C₁ > 0. There is h_0 > 0 such that for
h ∈ (0, h_0):

(1) for s ∈ [−C₁, C₁] the forcing problem □^Cω = f ∈ Ḣ^(s−1,(α_sf+2,α_cf−2))_eb(Ω) has a solution
ω ∈ Ḣ^(s,(α_sf,α_cf))_eb(Ω); it is unique among solutions whose restrictions to Ω_(≤t_0) := Ω ∩ {t ≤ t_0} lie in
H^(−N,(−N,α_cf))_eb(Ω_(≤t_0))^(•,−) for all t_0 and some N ≤ C₁;

(2) the initial value problem with f ∈ H̄^(0,(α_sf+2,α_cf−2))_eb(Ω, |dg|) and

    (ω, r𝓛_(∂_t)ω)|_(X_0) ∈ ρ_sf^(α_sf+½)ρ_cf^(α_cf−½)(H̄¹_b ⊕ H̄⁰_b)(X_0, r³|dr d𝑔̸|)                      {#eq:iv6-2-1}

has a solution ω ∈ H̄^(1,(α_sf,α_cf))_eb(Ω), unique among solutions whose restrictions to every Ω_(≤t_0) lie in
H̄^(1,(−N,α_cf))_eb for some N.

*Proof.* The proof is that of [[thm:iv5-7-3]], on M instead of M^♭, with the following differences.

*Energy near X_0.* η = r²(−dτ² − 2τ dτ (dr/r) + (1 − τ²)dr²/r² + 𝑔̸) is a weighted b-metric on
(−1, 1)_τ × [0, ∞]_r × 𝕊³. Here r²η⁻¹(dτ, dτ) = −(1 − τ²), and b-norms on {t/r ∈ I} are edge-b norms. The proof of
[[prop:iv5-6-1]] (1), with the level-set density r⁴|dr d𝑔̸|, gives at T := ½, with ρ_sf = (1 + r)⁻¹ and
ρ_cf = r(1 + r)⁻¹ there, its two estimates on M with the weight ρ_sf^(α_sf)ρ_cf^(α_cf) in place of ρ_sf^(α_sf)
([Hin26a, (B.34) and (B.35)]): for ω vanishing for t < 0,

    ‖ω‖_(H^(1,(α_sf,α_cf))_(eb,h)(τ⁻¹([0,T]))) ≤ Ch⁻¹‖P_hω‖_(H^(0,(α_sf+2,α_cf−2))_(eb,h)(τ⁻¹([0,T]))),    {#eq:iv6-2-e1}

and, with no support condition, there being no inner boundary,

    ‖ω‖_(H^(1,(−α_sf−2,−α_cf+2))_(eb,h)(τ⁻¹([0,T/2])))
        ≤ C(h⁻¹‖P_h*ω‖_(H^(0,(−α_sf,−α_cf))_(eb,h)(τ⁻¹([0,T]))) + ‖ω‖_(H^(1,(−α_sf−2,−α_cf+2))_(eb,h)(τ⁻¹([T/2,T])))).
                                                                                                         {#eq:iv6-2-e2}

In it, [[lem:iv5-6-tform]], [[cor:iv5-6-energy]], [[lem:iv5-6-transport]] and [[lem:iv5-6-core]] are used on
N := ℝ_t × (ℝ⁴ ∖ 0), with k = 1, f_1 := τ − T and w := ρ_sf^(−α_sf−2)ρ_cf^(−α_cf+2)e^(−𝔛τ) for [[eq:iv6-2-e1]], and
f_1 := −τ and w := ρ_sf^(α_sf)ρ_cf^(α_cf)e^(𝔛τ) for [[eq:iv6-2-e2]]. Their hypotheses hold: the components
of η and of rc = dt − v x̂ · dx in the frame dt, dx^i lie in a compact set of pairs and are bounded with their
derivatives along r∂_t and r∂_(x^i); e = 1/102400 < 2/5; r dτ = dt − τ dr has η⁻¹(r dτ, r dτ) = −(1 − τ²) ≤ −¾ for
0 ≤ τ ≤ ½; and r dρ_sf/ρ_sf and r dρ_cf/ρ_cf are bounded, so that rη_0 and rη_1 of [[lem:iv5-6-core]] are past
timelike (for [[eq:iv6-2-e2]], with −c and the opposite time orientation), with a uniform κ, for 𝔛 large.

*Nonzero and infinite frequencies.* The estimates [[eq:iv5-fib]] and [[eq:iv5-fib-adj]] of [[prop:iv5-1-3]] hold on M,
by its proof, with the weights of [[eq:iv6-2-e1]], resp. [[eq:iv6-2-e2]], the cut-offs χ_(τ,j) of [[sec:iv5-1]]
at T and no cut-off in r (χ_(r,j) := 1) ([Hin26a, (B.36)–(B.37)]). There is no E_r term; the E_τ term is a negative
square because ±H_Gτ > 0 at future, resp. past, lightlike covectors, dτ being past timelike on supp χ′_(τ,1).

*The cone face 𝖼𝖿.* Use 𝓛_h := −i(1 + iCL_h*r²)P_h = −L_h + J − iQ as in [[eq:iv5-2-1]], with r⁻¹ for ρ_sf. In
t ≥ −r/2 let ρ_sf := (t + r + 1)⁻¹ and ρ_cf := r(t + r + 1)⁻¹. Take the commutant
a = w⁻¹χ_cf(𝔛ρ_cf)χ_0(𝔛|ζ|)χ₁(t/r), w := ρ_sf^(α_sf+1)ρ_cf^(α_cf−1), with 𝔛 := δ_r⁻¹, χ_cf a cut-off equal to 1 on
[0, 5/2] and supported in [0, 4), and χ₁ := χ_(τ,0) of [[sec:iv5-1]] at T, δ_r being fixed below so small that 𝔛 is
large enough. By
[[lem:iv5-2-symbols]], with r⁻¹ for ρ_sf, aH_(−ℓ+j)a − Sa² = −c_0r⁻²a² − b_0² − b_cf² + e_τ² + f ([Hin26a, (B.38)]),
with f as there and, χ_cf, χ_cf′ being evaluated at 𝔛ρ_cf and χ₁, χ₁′ at t/r,

    b_0 := a(S − ℓ(dw/w) − wH_j(w⁻¹) − c_0r⁻²)^(1/2),     b_cf := w⁻¹χ₁χ_0(−𝔛χ_cfχ_cf′)^(1/2)(−ℓ(dρ_cf) + H_jρ_cf)^(1/2),
    e_τ := w⁻¹χ_cfχ_0(χ₁χ₁′)^(1/2)(−ℓ(d(t/r)) + H_j(t/r))^(1/2).

Since dw/w ≡ (α_cf − 1)dr/r modulo ρ_cf C^∞(M; ^(eb)T*M), the square roots exist for the following reasons.

- b_0: r²(−ℓ(dw/w) + S) at ρ_cf = 0 is the T of [[prop:np-10-14]] (iv) at ρ_K = 0 with d = 1 − α_cf. It is positive
definite iff d < b*, that is α_cf > 1 − b* ([[lem:s14-tf-inputs]] (iii)). Positivity extends to supp a for 𝔛 large,
and w⁻¹H_jw vanishes at o.

- b_cf: −½r²ℓ(dr/r) has the characteristic polynomial of [[lem:s14-tf-inputs]] (iii), with positive roots at
(v, e) = (1/2, 1/102400). It is B-self-adjoint ([[lem:iv5-0-4]]), so it is B-positive definite. Moreover
dρ_cf/ρ_cf ≡ dr/r modulo ρ_cf, and −χ_cfχ_cf′ ≥ 0.

- e_τ: d(t/r) is past timelike on supp χ₁′, so r²ℓ(d(t/r)) is negative definite ([[lem:iv5-0-4]]).

- f is elliptic.

The Q-terms are those of the proof of [[prop:iv5-2-1]] with r⁻¹ for ρ_sf: [[lem:iv5-calc-q0]] in the eb-calculus with
w = r⁻¹, the constant C being such that r²G + C(r²ℓ)² is positive definite on the model, as in [[lem:iv5-0-4]]; and
[[lem:iv5-calc-garding]] (b), (c) for the term with Q_1.

This gives, by the proof of [[prop:iv5-3-1]] (1), the estimate of the form of [[prop:iv5-3-1]] (1) at 𝖼𝖿, with 𝖼𝖿,
ρ_cf and the weights of [[eq:iv6-2-e1]] in place of ∂K⁺, ρ_K and those of M^♭, its operator E elliptic on
supp χ₁′(t/r) ⊂ {τ ≤ (2.75/10)T}, which [[eq:iv6-2-e1]] covers; we call it the forward cone estimate
([Hin26a, (B.39)]). For P_h*, with the commutant wχ_cf(𝔛ρ_cf)χ_0(𝔛|ζ|)χ̃(τ), χ̃ := χ_(τ,2), and 𝓛_h*,
[[lem:iv5-2-symbols]] gives aH_(−ℓ+j)a + Sa² = c_0r⁻²a² + b_0² − b_cf² + b_τ² + f with the symbols formed in the same
way: the term of χ̃ has the sign of the main term, and that of χ_cf gives the a priori term. This gives the estimate of
the form of [[prop:iv5-3-1]] (2) at 𝖼𝖿, with the weights of [[eq:iv6-2-e2]], its a priori operator elliptic on
supp χ_cf′(𝔛ρ_cf) ∩ supp χ̃; we call it the backward cone estimate ([Hin26a, (B.40)]).

*The other zero-section estimates.* The model is stationary and dilation invariant ([[lem:iv6-0-1]] (a)). So each
rescaled symbol of the commutator arguments at a point of Ω°, such as r²ℓ(d(r/t)) or r²S, is a function of s := r/t and
ω; the derivatives of the weights enter only through bounded terms, which the escape terms dominate. The 1-form is the
Minkowski model's, for which [[lem:iv5-0-5]] (4)–(6) hold at 𝗌𝖿 ([[prop:np-10-14]] (iv)–(v)). At s → 0,
−r²ℓ(ds) = 2s(−½r²ℓ(dr/r)) + O(s²) is positive by the b_cf positivity, so δ_r may be shrunk. Fix δ_r > 0 so small that
the b_0 positivity at 𝖼𝖿 holds on {ρ_cf ≤ 4δ_r} (it is constant along 𝖼𝖿, and 𝖼𝖿 ∩ Ω is a product [0, ∞]_t × 𝕊³ up to
the dilations), that (6) holds on 𝗌𝖿 ∩ {s ∈ [δ_r, v(1 − δ_sf)]}, and that 𝔛 = δ_r⁻¹ is as large as the cone-face
symbols need, a bound that does not grow as δ_r decreases. Then:

(a) The forward cone estimate holds on {ρ_cf < 4δ_r} ∩ {τ ≥ (0.75/10)T} and the backward one on
{ρ_cf < 4δ_r} ∩ {τ ≥ (2.75/10)T}, globally in t, with a priori sets in
{τ ≤ (2.75/10)T} and in {(5/2)δ_r ≤ ρ_cf ≤ 4δ_r} respectively.

(b) [[prop:iv5-5-2]] (b)–(c) hold with s = r/t near 𝗌𝖿 on [δ_r, v(1 − δ_sf)] and [v(1 + δ_sf), 10], and
[[prop:iv5-4-1]] at the sink s = v (with α_sf < b* − 1), by their proofs, which use only these signs. For η,
⟨c, ds⟩ = (s − v)/(rt), so the flow of −rc♯ moves s towards v from both sides.

(c) [[prop:iv5-5-3]] (1)–(2) hold on compact subsets of Ω ∩ {ρ_cf ≥ 2δ_r}, with the escape functions t + κr and t and
the cut-off t − κr (d(t − βr) is past timelike for |β| < 1 on η). The cut-off χ_r(r) at Σ^♯ is replaced by
f(ρ_cf/(2δ_r)), with f non-decreasing, 0 near [0, ½] and 1 on [1, ∞). Its term is f′·(−ℓ(dρ_cf))/(2δ_r) ≥ 0, as
−ℓ(dρ_cf) > 0 near 𝖼𝖿 (dρ_cf/ρ_cf ≡ dr/r, the b_cf positivity). So it needs a priori control on
{δ_r ≤ ρ_cf ≤ 2δ_r} in the forward direction and has the sign of the main term in the adjoint one.

*Combination.* *Forward*: [[eq:iv6-2-e1]] on {τ ≤ ½} and [[eq:iv5-fib]] on M; (a) forward; (c) (1) on every compact
subset of Ω ∩ {ρ_cf ≥ 2δ_r}, from [[eq:iv6-2-e1]] and (a), with ε_X ≤ δ_rT so that its set {½ε_X ≤ t ≤ ε_X} lies
under [[eq:iv6-2-e1]], as τ ≤ ε_X/δ_r on {ρ_cf ≥ δ_r}; (b) along 𝗌𝖿 from s ∈ [2δ_r, 3δ_r] (by (a), as
ρ_cf = s/(1 + s) + O(ρ_sf) near 𝗌𝖿) and from s ∈ [5, 10] (by [[eq:iv6-2-e1]]), their interior a priori sets by (c);
and the sink, its a priori sets by (b) and (c). These cover a neighbourhood of o over Ω: near 𝖼𝖿 by (a) and
[[eq:iv6-2-e1]], near 𝗌𝖿 by (a), (b), the sink and [[eq:iv6-2-e1]], and the compact rest by (c). This gives

    ‖ω‖_(H^(1,(α_sf,α_cf))_(eb,h)(Ω)^(•,−)) ≤ Ch⁻¹‖P_hω‖_(H^(0,(α_sf+2,α_cf−2))_(eb,h)(Ω)^(•,−))           {#eq:iv6-2-ap}

([Hin26a, (B.41)]) at the Sobolev order 1, and the same estimate at every order s ≥ 1, with H^(s) and H^(s−1), by
extension and restriction. *Adjoint*: the sink,
which has no a priori term; (b) (2) outward along 𝗌𝖿, the 𝗌𝖿-cut-off terms having the good sign; (c) (2) on compact
subsets of Ω ∩ {ρ_cf ≥ 2δ_r} ∩ {τ > κ}, the set of [[prop:iv5-7-2]] (viii) (t − κr > 0; there t ≥ 2t_1 once
t_1 < δ_r/9, as ρ_cf ≥ 2δ_r gives r ≥ 2δ_r), which contains the a priori set of the backward cone estimate, its
cut-off χ̃ = χ_(τ,2) being supported in τ ≥ (2.25/10)T > κ; its late set (large t, r ≤ (t + c₁)/κ, ρ_cf ≥ δ_r) lies
near 𝗌𝖿 with s ∈ [δ_r, 10], by κ = 1/9, covered by the previous two steps; (a) adjoint, that is the backward cone
estimate, its a priori set {(5/2)δ_r ≤ ρ_cf ≤ 4δ_r} covered by (c) (2) and, near 𝗌𝖿, by (b) (2); and [[eq:iv6-2-e2]],
its a priori set
τ⁻¹([T/2, T]) covered by the steps before. Each step's a priori set lies in the controlled set of an earlier step, as in
[[prop:iv5-7-1]] and [[prop:iv5-7-2]]. Duality, extension and restriction, and the initial value problem are the
arguments of [[thm:iv5-7-3]] with these estimates. The data weights in [[eq:iv6-2-1]] follow
because |dg| = r⁴|dt (dr/r) d𝑔̸| = r|dτ| ⊗ r³|dr d𝑔̸| on {t/r ∈ I}, so the weights shift by ½ at both faces
([[lem:s14-tf-inputs]] (iv)).

*Strong uniqueness.* By finite speed of propagation for wave equations with smooth coefficients in {r > 0}, a solution
vanishing on {t ≤ 0} vanishes on {0 ≤ t ≤ 1, r > t}. On Ω′ := cl{0 ≤ t ≤ 1, r ≤ 1 − t} the a priori estimate
‖ω‖_(ρ_cf^(α_cf)H^s_(eb,h)(Ω′)^(•,−)) ≤ Ch⁻¹‖P_hω‖_(ρ_cf^(α_cf−2)H^(s−1)_(eb,h)(Ω′)^(•,−)) holds. It is proved by the
energy estimates near X_0 and near the final surface {r = 1 − t} (spacelike, with d(1 − t − r) past timelike;
localisation in (t − 1)/r), together with [[eq:iv5-fib]] on M and the forward cone estimate. So a solution with zero
forcing that is supported
in {t ≥ 0} and lies in that space vanishes on Ω′, hence on {0 ≤ t ≤ ½}. Translating in t, which commutes with □^C, and
iterating gives vanishing for all t. ∎

#### The kernel and [Hin26a, Theorem B.1] in dimension 4 + 1 {#sec:iv6-3}

**Theorem {#thm:iv6-3-1}** ([Hin26a, Theorem B.1] in dimension 4 + 1.) There is h_tf > 0 such that for h ∈ (0, h_tf),
every σ ∈ e^(i[0,π]) and every (s, ℓ, β) admissible at σ, the map [[eq:iv6-1-1]] is invertible, with inverse bounded
uniformly for σ in each set on which fixed orders are admissible ([[def:iv6-0-2]]) and [[eq:iv6-1-2]] holds uniformly
([[prop:iv6-1-1]]).

*Proof.* By [[prop:iv6-1-1]] it suffices to show that the nullspace is trivial for one admissible choice. Take ℓ := −½
and β := 7/2, admissible as C_0 ≥ 3/2 ([[lem:s14-tf-inputs]] (iv)). Apply [[thm:iv6-2-1]] with
(α_sf, α_cf) := (−5/2, 5/2), which satisfy α_sf < b* − 1 and α_cf > 1 − b*. Let h_tf be the h_0 of [[thm:iv6-2-1]] for
these weights and C₁ = 1, with h_tf ≤ 10⁻⁶.

Let ω_0 ∈ H^(1,(ℓ,β))_(sc,b) with (□^C)^(σ)ω_0 = 0. Then ω := e^(−iσ(t−r))ω_0 solves □^Cω = 0, with data (ω^(0), ω^(1))
:= (e^(iσr)ω_0, −iσre^(iσr)ω_0) at t = 0 ([Hin26a, (B.44)]). As Im σ ≥ 0, |e^(iσr)| ≤ 1, and the scattering derivatives
ρ²∂_ρ, ρ∂_ω cost one power against the b-derivatives. So ω^(0) ∈ ρ_sc^(ℓ−1)ρ_b^β H̄¹_b and ω^(1) ∈ ρ_sc^(ℓ−1)ρ_b^β
H̄⁰_b, for r³|dr d𝑔̸|. On X_0, ρ_sf and ρ_cf are ρ_sc and ρ_b. Both data lie in the spaces of [[eq:iv6-2-1]], since ℓ −
1 = −3/2 ≥ α_sf + ½ = −2 and β = 7/2 ≥ α_cf − ½ = 2 ([[lem:s14-tf-inputs]] (iv)). [[thm:iv6-2-1]] (2) gives a solution
ω′ ∈ ρ_sf^(−5/2)ρ_cf^(5/2)H̄¹_eb(Ω). On each Ω_(≤t_0), ω lies in H̄^(1,(−N,α_cf))_eb: near 𝖼𝖿 at bounded t, ω is ω_0
times a smooth bounded factor, and ω_0 ∈ ρ_b^(7/2)H¹ with edge-b derivatives r∂_t, r∂_x; near 𝗌𝖿 at bounded t, the
weight −N absorbs the loss ρ_sc^(−3/2), the edge-b derivative of e^(iσr) costing a further ρ⁻¹. So ω′ = ω by the
uniqueness in [[thm:iv6-2-1]] (2).

Suppose ω_0 ≠ 0: then |ω_0| ≥ c > 0 on an open U with Ū ⊂ ℝ⁴ ∖ 0 compact. In t ≥ 1, r ≤ t, take ρ_cf = r/t and
ρ_sf = 1/t. With T := max(1, sup_U r), |ω| ≥ e^(−(Im σ)r)|ω_0|, and

    ∫_U ∫_T^∞ ρ_sf^(−2α_sf) ρ_cf^(−2α_cf) |ω|² dt dx ≥ c′ ∫_U r⁻⁵ dx ∫_T^∞ t^(2(α_sf+α_cf)) dt = ∞,

as 2(α_sf + α_cf) = 0. This contradicts ω ∈ ρ_sf^(−5/2)ρ_cf^(5/2)L²(|dg|). So the nullspace is trivial, and
[[eq:iv6-1-1]] is invertible at (ℓ, β) = (−½, 7/2), hence at every admissible choice. The uniform bound on the inverse
follows from the uniform estimate [[eq:iv6-1-2]] and invertibility by the compactness argument of [[cor:i-c-5-2]] (b). ∎

### Mode stability and the zero energy operator {#sec:iv4-2}

**Theorem {#thm:iv4-2-1}** ([[thm:iii-e-1-1]] (1)–(3); [Hin26a, Theorem 6.2] in dimension 4 + 1.) With the constants
[[eq:iv4-0-1]] and b near b₀:

(1) for σ ≠ 0, Im σ ≥ 0, (□^C_b)^(σ) has trivial nullspace on 𝒜^γ(X̄; E) for every γ;

(2) for every α with α + 2 ∈ [−C_0, 2) and s ≥ −C_0,
P^C_b : {ω ∈ H̄_b^(s,α) : P^C_bω ∈ H̄_b^(s−1,α+2)} → H̄_b^(s−1,α+2) (Euclidean density) is invertible, and □^C_b
satisfies (H1)–(H4) with ½ + ϑ_ℋ < −C_0;

(3) the indicial roots are as in [[lem:iv4-1-3]], with all clauses of [[thm:iii-e-1-1]] (3) for h ∈ 𝖧.

*Proof.* (3) is [[lem:iv4-1-3]], and the second half of (2) is [[lem:iv4-1-5]] and [[lem:iv4-1-6]]. [[thm:iv5-7-3]] is
used with the weights [[eq:iv4-2-1]], which its hypothesis in dimension 4 + 1, α_sf < b* − 1 and
α_K > α_sf + 1 − b* ([[lem:iv4-1-4]]; [[prop:np-10-22]] (iv)), allows, and with the regularity range C₁ := C_0 + 1,
as in [Hin26a, p. 67].

*(1).* Let ω′ ∈ 𝒜^γ(X̄; E) with (□^C_b)^(σ)ω′ = 0, and ω := e^(−iσt_*)ω′, a solution of □^C_bω = 0. It is outgoing in
the sense of [Hin26a, Definition 6.1]: t_* = t − ψ(|x|) with ψ(r) = r − C_ψ + 8m₀r⁻¹ for large r ([[eq:iii-b-3-6]]), and
the tortoise coordinate of g_(b₀) is r_* = r − m₀r⁻¹ + O(r⁻³) (dr_*/dr = (1 − m₀r⁻²)⁻¹), so
ω = e^(−iσt)e^(iσr_*)ω₁ with ω₁ = e^(iσ(ψ−r_*))ω′ ∈ 𝒜^γ, ψ − r_* being bounded and conormal. By [[eq:iv4-1-1]],

    2iσρ(ρ∂_ρ − 3/2 − S̄^C)ω′ ∈ (ρ²Diff²_b + σρ³Diff¹_b + σ²ρ²Diff⁰_b)ω′ ⊂ 𝒜^(γ+2),

the term ρS̃ of [[eq:iv4-1-1]] included in the first class. Dividing by 2iσρ and solving the regular-singular equation
in ρ gives ω′ ∈ 𝒜^(γ+1) as long as γ + 1 < 3/2 + min spec S̄^C; iterating, ω′ ∈ 𝒜¹, as S̄^C > 0 ([[lem:iv4-1-2]]).
[[thm:iv5-7-3]] is applied in the Kerr–Schild coordinates of [[sec:iv5-0]] ([[rem:iv5-7-4]]), in which
t = t_KS + T_m(|x|) ([[sec:iii-b-3-1]]). The data
(ω, r𝓛_(∂_t)ω)|_(t_KS=0) = (e^(iσ(ψ−T_m))ω′, −iσre^(iσ(ψ−T_m))ω′) satisfy |ω^(0)| ≤ Cr⁻¹, |(r∂_r, ∂_ω)ω^(0)| ≤ C
(the phase contributes σr, and ω′ ∈ 𝒜¹ is conormal) and |ω^(1)| ≤ C. Indeed |e^(iσ(ψ−T_m))| = e^(−(Im σ)(ψ−T_m)) is
bounded, ψ − T_m being continuous on [r_♯, ∞) and tending to +∞. So the data
lie in ρ^(−2−ε)H̄^(1−j)_b(X, r³|dr d𝑔̸|) for every ε > 0 ([[prop:np-10-21]] (iii): ρ^k ∈ ρ^aL²(r³dr) near ∂X iff
a < k − 2), which lies in ρ^(α_sf+½)H̄^(1−j)_b, as α_sf + ½ = −C_0 − 2 < −2 − ε. The initial value problem of
[[thm:iv5-7-3]] (b) has a solution with these data in its class, and it is ω: both are H¹_loc solutions with the same
data, so they agree by local energy uniqueness, every past-inextendible causal curve in Ω° meeting X_0 (the proof of
[[thm:iv5-7-3]] (b)). So ω ∈ ρ_sf^(α_sf)ρ_K^(α_K)H̄¹_3b(Ω, |dg|). On [0, ∞)_t × A, A = {r_1 ≤ r ≤ r_2} an annulus, ρ_sf
is bounded above and below and ρ_K = r/t, so ∫_0^∞∫_A (t/r)²|ω|² < ∞ with |ω| = e^((Im σ)t_*)|ω′|, which forces ω′ = 0
on A, for every annulus. So ω = 0.

*(2), injectivity.* Let u be in the kernel. By [[thm:i-c-3-1]] (2) ([[lem:iv4-1-5]], [[lem:iv4-1-6]]), u is smooth up
to the inner boundary and lies in 𝒜^β near ∂X for every β < 2. So ω(t, x) := u(x) solves □^C_bω = 0 with data (u, 0) in
ρ^(α_sf+½)H̄¹_b ⊕ 0, and [[thm:iv5-7-3]] gives ω ∈ ρ_K^(α_K)L² over [0, ∞) × A as in (1), which for a stationary ω forces
u = 0. By [[thm:i-c-3-1]] (3) the kernel does not depend on s > ½ + ϑ_ℋ, and −C_0 > ½ + ϑ_ℋ by [[lem:iv4-1-5]]; so no
cut-off in time is needed for s < 1.

*(2), surjectivity.* By [[thm:i-c-3-1]] (1), P^C_b : 𝒳_0 → 𝒴_0 is Fredholm and the annihilator of its range is
ker_(𝒳*_0)(P^C_b)*, 𝒳*_0 ⊂ Ḣ_b^(1−s,−α−2) (supported at the inner boundary). Let v be in that kernel. The indicial roots
of (P^C_b)* are 2 − ῑ ([[lem:iii-e-2-1]] (2), which uses only [[lem:iv4-1-3]]), with real part ≤ 0 or > C_0 + 2. As
α + 2 < 2, v has pointwise weight −α > 0 at ∂X, so the normal operator argument (the expansion of v along the roots of
real part above its weight, [[thm:i-c-3-1]] (2) for the adjoint) gives v ∈ 𝒜^k near ∂X for every k < ϱ₁. Here
ϱ₁ > C_0 + 2 is the least real part of an indicial root of (P^C_b)* above C_0 + 2, which exists as such roots exist and
each strip {|Re ι| ≤ R} contains finitely many roots ([[lem:iv4-1-3]] (a)); the roots of real part ≤ 0 are below the
weight. So ω′(t, x) := v(x) is a stationary solution of (□^C_b)*ω′ = 0. Put α′_sf := −C_0 − 3/2, the weight
[[eq:iv4-2-1]] at C_0 − 1. A stationary function of pointwise decay
ρ^k lies in ρ^aρ_K⁻¹L²(Ω, |dg|) near ∂X iff k > a + 5/2: the shift is 2 for ρ^aL²(r³dr) ([[prop:np-10-21]] (iii)),
plus ½ from ∫_0^∞ρ_K²dt = ∫_0^∞(r/(t + r))²dt = r. At a = −α′_sf − 2 = C_0 − ½ this asks k > C_0 + 2, which
k ∈ (C_0 + 2, ϱ₁) meets. So ω′ ∈ ρ_sf^(−α′_sf−2)ρ_K^(−α_K)H^(s′)_3b(Ω)^(−,•) for s′ = 1 − s near ∂X. The adjoint estimate
[[eq:iv5-5-81]] at the weights (α′_sf, α_K), which satisfy its hypotheses by [[lem:iv4-1-4]] at C_0 − 1, holds for
h < h_* and makes (□^C_b)* injective there, so v = 0. (At the weight [[eq:iv4-2-1]] itself the membership would ask
k > C_0 + 3, which [[lem:iv4-1-3]] does not give at C_0 = 100; this is why h_* is below the threshold of
[[thm:iv5-7-3]] at C_0 − 1 as well.) So P^C_b is surjective, hence invertible, and by [[thm:i-c-3-1]] (4) the estimates
hold without the error terms. ∎

**Remark {#rem:s14-other-routes}** (Other routes to surjectivity.) [Hin26a] has two further routes to the
surjectivity: the index 0 from [Hin26a, Theorem B.1] with
[[cor:i-c-6-6]], and the radial ordinary differential operators of a static metric with [Hin26a, Theorem 4.9 (3)]. They
are not used: the first needs the tf-admissibility and the index at σ ≠ 0, the second an index count for operators that
are singular at the horizon. The route through the adjoint estimate needs only what the proof of [[thm:iv5-7-3]]
provides.

### tf-admissibility {#sec:iv6-4}

**Theorem {#thm:iv6-4-1}** ([[thm:iii-e-1-1]] (4).) For b near b₀, h ∈ (0, h_*) and C_0 ∈ [3/2, 100], □^C_b is
tf-admissible ([[def:i-c-5-1]]) with every weight β_tf ∈ [−C_0, 2).

*Proof.* We check (i)–(iii) of [[def:i-c-5-1]].

(i) By [[lem:iv4-1-6]], (β_−, 2) with β_− < −100 ≤ −C_0 is an indicial gap of (□^C_b)^(0), and it contains β_tf.

*The spaces.* Put q := 2 − β_tf ∈ (0, 2 + C_0]. The spaces of [[sec:i-c-4]] are the H^(s,(𝗋+α₊,q))_(sc,b)(tf) of
[[def:i-c-4-1]], normed with the Euclidean density |dx̂| near both ends. These are the spaces H^(s,(ℓ,β))_(sc,b) of
[[sec:iv6-0]] with ℓ := 𝗋 + α₊ and β := q: X is tf, ρ_sc and ρ_b are ρ_sctf and ρ_ztf, and the density is r³|dr d𝑔̸| in
both. The map 𝒳_(tf,θ) → 𝒴_(tf,θ) of [[sec:i-c-4]] is then [[eq:iv6-1-1]] at σ = e^(iθ), by [[lem:iv6-0-1]] (d).
These orders are admissible in the sense of [[def:iv6-0-2]]: q = β ∈ (0, 2 + C_0]; the orders 𝗋_± with weight α₊ are
those of [[lem:i-a-7-1]] at σ_* = ±1, constant near the radial sets and monotone along the flow, functions of ξ
and |η|², and admissible on {e^(iθ) : θ ∈ Θ_±}, being admissible for every σ₀ ∈ J_± ∋ Re e^(iθ) ([[sec:i-c-4-3]]); the
constant orders used for θ ∈ (0, π) ([[thm:i-c-4-3]] (2)) are admissible at e^(iθ), being constant below the threshold
at R_out; and the thresholds are those of [[eq:i-a-1-5]] for (□^C_b)^, which are the data of □^C_b at ρ = 0
([[sec:i-c-4]]): at R_out, −½ + S̄ with S̄ = min spec S̄^C = h⁻¹(1 − e)(1 − v) ([[prop:np-10-21]] (i)); at R_in,
(−1 + ϑ_in)/2 = −½ − h⁻¹(1 − e)(1 + v) by [[eq:s14-theta-in]]. These are the thresholds of [[def:iv6-0-2]].

(ii) By [[thm:iv6-3-1]], N_tf(e^(iθ)) is invertible, so injective, on 𝒳_(tf,θ) for every θ ∈ [0, π].

(iii) By [[thm:iv6-3-1]] at θ = 0, N_tf(1) is onto 𝒴_(tf,0). By [[thm:i-c-4-3]] (3), the annihilator of its range is
ker_(𝒳*_(tf,0)) N_tf(1)^(*h), so this kernel is trivial.

So □^C_b is tf-admissible with weight β_tf. ∎

[Hin26, proof of Theorem 7.1 (4)] applies [Hin26a, Theorem B.1] at β′ = −β + 3/2 − ε, with the kernel taken on the
conormal spaces 𝒜^(a,−β)(tf) of [Hin26c, Definition 5.10], and the adjoint half through [Hin26c, (9.115)].
[[def:i-c-5-1]] is posed on the Sobolev spaces of [[thm:i-c-4-3]] and needs neither: q = 2 − β_tf exactly, the 3/2 of
dimension 3 + 1 becoming n/2 = 2, with no ε.

### The adjoint at zero energy {#sec:iii-e-2}

**Lemma {#lem:iii-e-2-1}** ([Hin26, Lemma 7.2] in dimension 4 + 1.) (1) (*Invertibility.*) For α ∈ (0, C_0 + 2] and
s ≤ C_0 + 1, (P^C_b)* : {ω ∈ Ḣ_b^(s,α) : (P^C_b)*ω ∈ Ḣ_b^(s−1,α+2)} → Ḣ_b^(s−1,α+2) is invertible.

(2) (*Indicial roots.*) The indicial roots of (P^C_b)* are 2 − ῑ, ι running over those of P^C_b. So they are 0 (scalar
type 0 or 1), have negative real part, or have real part > C_0 + 2.

*Proof.* (1) First for the adjoint (P^C_b)^(*h) of [[ch:s03]], taken for the fibre inner products h and the Euclidean
density. By [[thm:iii-e-1-1]] (2) and [[thm:i-c-3-1]] (1) and (4), for α′ with α′ + 2 ∈ [−C_0, 2) and s′ ≥ −C_0,
[[eq:i-c-3-3]] holds without its last term: (P^C_b)^(*h) is injective with closed range on
𝒳*_0 = {v ∈ Ḣ_b^(1−s′,−α′−2)(|dx|) : (P^C_b)^(*h)v ∈ Ḣ_b^(−s′,−α′)(|dx|)}, and the annihilator of its range is the kernel
of P^C_b on 𝒳_0, which is trivial; so it is onto Ḣ_b^(−s′,−α′)(|dx|), and invertible. In b-densities these spaces are
Ḣ_b^(1−s′,−α′) and Ḣ_b^(−s′,−α′+2); with s := 1 − s′ ≤ C_0 + 1 and α := −α′ ∈ (0, C_0 + 2] this is the claim for
(P^C_b)^(*h). The pairing B of [[sec:iii-e-1]] differs from the h-weighted L²(|dx|) pairing by a bundle map M, smooth and
invertible on X̄ (g_b⁻¹ and h are nondegenerate and smooth up to ∂X, and |dg_b|_X|/|dx| is smooth and positive there),
so (P^C_b)* = M⁻¹(P^C_b)^(*h)M with M preserving every Ḣ_b^(s,α); the claim follows.

(2) Let N := N(ρ⁻²P^C_b) and write * for adjoints for the Euclidean density near ∂X, ρ⁻⁴|(dρ/ρ) d𝑔̸|, and *_b for the
unweighted b-density, so A^(*_b) = ρ⁻⁴A*ρ⁴. As (ρ⁻²P)* = ρ⁻²(ρ²P*ρ⁻²) and N(ρ²P*ρ⁻²) = N(P*) up to the conjugation,
the identity [Hin26, (7.10)] reads in dimension 4 + 1

    N(ρ⁻²P, ι)* = ρ^ῑ N^(*_b) ρ^(−ῑ) = ρ^ῑ ρ⁻⁴ N* ρ⁴ ρ^(−ῑ) = ρ^(ῑ−2) N(ρ⁻²P*) ρ^(2−ῑ) = N(ρ⁻²P*, 2 − ῑ),

the adjoint on the left being on 𝕊³ for d𝑔̸; so ι is a root of P^C_b iff 2 − ῑ is one of the adjoint. The rest is
[[thm:iii-e-1-1]] (3). ∎

Two consequences are used below.

(a) Let f be polyhomogeneous near ∂X with index set ℱ, min Re ℱ > 2, and f ∈ Ḣ_b^(s−1,α+2) for
α ∈ (0, min Re ℱ − 2). Then the solution u = ((P^C_b)*)⁻¹f given by (1) at such an α lies in Ḣ_b^(s,(ℰ,C_0+2)) (partial
polyhomogeneity, [[def:s11-b-analysis]]), where ℰ is the index set of [[lem:iii-a-1-5]] for ρ⁻²f. Indeed, solve ρ⁻²f away
near ∂X to order ρ^(C_0+4+ε) by [[lem:iii-a-1-5]] for the elliptic b-operator ρ⁻²(P^C_b)* (on the bundle), and the
remainder, compactly supported away from ∂X modulo Ḣ_b^(s−1,C_0+4), by (1) at the weight C_0 + 2; the sum lies in
Ḣ_b^(s,α) for the α above (the exponents of ℰ below C_0 + 2 exceed α, by the next sentence) and solves the equation, so
it is u, (1) being injective at that α. Since the adjoint has no root with real part in (0, C_0 + 2], the exponents of ℰ
below C_0 + 2 are those of ℱ less 2 plus ℕ_0, without logarithms.

(b) *Vanishing inside the horizon.* On {r_♭ < |x| < r_h} the Killing field ∂_(t_*) is spacelike, so the quotient
metric is Lorentzian with |x| timelike, and on stationary sections (P^C_b)* is a wave operator in the time −|x| there.
An element of its kernel, or a solution with a forcing supported in {|x| > r_h}, that lies in a Ḣ space vanishes,
extended by zero, on {|x| < r_♭} (the supported character, the inner boundary being {|x| = r_♭}), and so on
{r_♭ < |x| < r_h} by uniqueness for the Cauchy problem on the spacelike hypersurfaces {|x| = c}, c < r_h, run from
{|x| < r_♭} across {|x| = r_♭}. Near {|x| = r_♭} the operator is defined, and hyperbolic in |x|, as dr is timelike on
{½r_♭ ≤ |x| ≤ ¾R₁} for b near b₀ ([[lem:iv5-0-3]] (c), with r_♯ = r_♭).

**Proposition {#prop:np-10-31}** (The adjoint's indicial values and the translations on Tangherlini space.) On
4 + 1 Minkowski space, with the notation of [[prop:np-10-12]]:

(i) for every type and degree, the indicial polynomial of the adjoint at ι equals that of □^C at 2 − ῑ; at vector type
l = 1 (κ = 3) the roots of □^C are 3 and −1 − 2vγ_C, those of the adjoint −1 and 3 + 2vγ_C, and the indicial value of
the adjoint at 2 is N_(v,1)(0) = 3(1 + 2v_Cγ_C);

(ii) on Tangherlini space, with S ∈ 𝒮₁ a harmonic of degree 1, so that |x|S = ξ·x for some ξ ∈ ℝ⁴ and
d(|x|S) = ξ·dx is the translation 1-form ω̄_s1(S), (□^C)*(d(|x|S)) ∈ ρ⁴C^∞ near ∂X, so that
(□^C)*(χ d(|x|S)) ∈ C_c^∞ + ρ⁴C^∞, and the correction ρ²(A S dt + B S dr + C r dS) that cancels its ρ⁴ term is unique,
2 being no root of the adjoint at scalar type 1.

*Proof.* (i) The first statement is [[lem:iii-e-2-1]] (2). At κ = 3, p_(v)(ι) = −hι² + (2h − 2v)ι + 3h + 6v vanishes at
ι = 3, and the product of its roots is −(3h + 6v)/h, so the other root is −1 − 2v/h. The adjoint's are 2 − 3 = −1 and
2 − (−1 − 2v/h) = 3 + 2vγ_C, and N_(v,1)(2 − 2) = h⁻¹p_(v)(0) = 3 + 6v/h.

(ii) d(|x|S) = ξ·dx is parallel for η, so δ*_η d(|x|S) = 0 and (□^C_η)*(d(|x|S)) = 0; on Tangherlini space
δ*_g d(|x|S) = −(Γ_g − Γ_η)·d(|x|S) has coefficients in mρ³C^∞ by [[prop:np-10-22]] (i), and
(δ*_(g,E_C))*G_g ∈ ρDiff¹_b near ∂X, so (□^C)*(d(|x|S)) ∈ ρ⁴C^∞. The
correction is unique because N(ρ⁻²(P^C)*, 2) is invertible at scalar type 1, 2 not being a root of the adjoint there by
(i) and [[lem:iii-e-2-1]] (2). ∎

### The dual states {#sec:iii-e-3}

With ω̄_s0, ω̄_s1(S) and V as in [[eq:iii-d2-1-2]]:

**Proposition {#prop:iii-e-3-1}** ([Hin26, Proposition 7.3] in dimension 4 + 1.) Assume (Dyn). (1) (*States.*) There
are stationary 1-forms

    ω*^((0))_(b,s0), ω*^((0))_(b,s1)(S) ∈ Ḣ_b^(1,((0,0),C_0+2)),
    ω*^((−1))_(b,v1)(V) ∈ Ḣ_b^(1,((−1,0),C_0+2)),                                                        {#eq:iii-e-3-1}

linear in S ∈ 𝒮₁ and V ∈ 𝒱₁, of class C^k in b with values in Ḣ_b^(1−k,((0,0),C_0+2)), resp.
Ḣ_b^(1−k,((−1,0),C_0+2)), with leading terms ω̄_s0, ω̄_s1(S), V, and ω*^((0))_(b,s0) − χg_b(∂_(t_*), ·) ∈ Ḣ_b^(1,C_0+2),
which lie in ker(□^C_b)*. The corrections to the translations and rotations, ω*^((0))_(b,s1)(S) − χω̄_s1(S) and
ω*^((−1))_(b,v1)(V) − χV, lie in Ḣ_b^(1,((2,0),C_0+2)). If R_V is a Killing field of g_b (at A = 0, every V), then
ω*^((−1))_(b,v1)(V) − χg_b(R_V, ·) ∈ Ḣ_b^(1,C_0+2).

(2) (*Dual pure gauge states.*)

    h*_(b,s0) := G_(g_b)δ*_(g_b)ω*^((0))_(b,s0) ∈ Ḣ_b^(0,C_0+3),
    h*_(b,s1)(S), h*_(b,v1)(V) ∈ Ḣ_b^(0,((3,0),C_0+3)),                                                  {#eq:iii-e-3-2}

with h*_(b,s1)(S) := G_(g_b)δ*_(g_b)ω*^((0))_(b,s1)(S) and likewise for V, of class C^k in b in Ḣ_b^(−k,C_0+3), resp.
Ḣ_b^(−k,((3,0),C_0+3)); and h*_(b,v1)(V) ∈ Ḣ_b^(0,C_0+3) when R_V is Killing for g_b. All these 1-forms and tensors
vanish on {r_♭ < |x| < r_h} ([[sec:iii-e-2]], (b)).

*Proof. Time translation.* ∂_(t_*) is Killing, so δ*_(g_b)(χg_b(∂_(t_*), ·)) = dχ ⊗_s g_b(∂_(t_*), ·) ∈ C_c^∞(X°),
and by [[eq:iii-e-1-2]], f_b := (□^C_b)*(χg_b(∂_(t_*), ·)) = 2(δ*_(g_b,E_C))*G_(g_b)(dχ ⊗_s g_b(∂_(t_*), ·)) ∈
C_c^∞(X°), stationary. [[lem:iii-e-2-1]] (1) with α = C_0 + 2, s = 1, gives a unique ω′_b ∈ Ḣ_b^(1,C_0+2) with
(P^C_b)*ω′_b = −f_b; put ω*^((0))_(b,s0) := χg_b(∂_(t_*), ·) + ω′_b. Its expansion is that of g_b(∂_(t_*), ·), smooth on
X̄ with leading term ω̄_s0 ([[prop:iii-d2-3-1]]). And
h*_(b,s0) = G_(g_b)(dχ ⊗_s g_b(∂_(t_*), ·) + (δ*_(g_b))^(0)ω′_b) ∈ C_c^∞ + ρDiff¹_bḢ_b^(1,C_0+2) ⊂ Ḣ_b^(0,C_0+3).

*Translations.* δ*_(g_b)(χω̄_s1) = dχ ⊗_s ω̄_s1 + χ((δ*_(g_b))^(0) − (δ̄*)^(0))ω̄_s1 ∈ C_c^∞ + ρ³C^∞
([[eq:iii-d2-2-1]]; δ̄*ω̄_s1 = 0), and (δ*_(g_b,E_C))*G_(g_b) lies in ρDiff¹_b near ∂X (the adjoint of δ*_(g_b) is
δ_(g_b), and (E^C)* has coefficients in ρC^∞), so f_b := (□^C_b)*(χω̄_s1) ∈ C_c^∞ + ρ⁴C^∞ ([[prop:np-10-31]] (ii)). By
consequence (a) of [[lem:iii-e-2-1]], with ℱ = (4, 0): ω′_b := −((P^C_b)*)⁻¹f_b ∈ Ḣ_b^(1,((2,0),C_0+2)), the coefficient
of ρ² being −N(ρ⁻²(P^C_b)*, 2)⁻¹ of that of ρ⁻²f_b (2 is no root of the adjoint). Put
ω*^((0))_(b,s1)(S) := χω̄_s1(S) + ω′_b. Then

    h*_(b,s1)(S) = G_(g_b)(dχ ⊗_s ω̄_s1 + χ((δ*_(g_b))^(0) − (δ̄*)^(0))ω̄_s1 + (δ*_(g_b))^(0)ω′_b)
                 ∈ C_c^∞ + ρ³C^∞ + Ḣ_b^(0,((3,0),C_0+3)).

*Rotations.* g_m(R_V, ·) = V and δ*_(g_m)V = 0 (the proof of [[prop:iii-d2-3-1]]), so
δ*_(g_b)(χV) = dχ ⊗_s V + χ((δ*_(g_b))^(0) − (δ*_(g_m))^(0))V ∈ C_c^∞ + ρ⁴Diff⁰_b(ρ⁻¹C^∞) ⊂ C_c^∞ + ρ³C^∞, and
f_b := (□^C_b)*(χV) ∈ C_c^∞ + ρ⁴C^∞. As for the translations, ω′_b := −((P^C_b)*)⁻¹f_b ∈ Ḣ_b^(1,((2,0),C_0+2)),
ω*^((−1))_(b,v1)(V) := χV + ω′_b, and
h*_(b,v1)(V) = G_(g_b)(dχ ⊗_s V + χ((δ*_(g_b))^(0) − (δ*_(g_m))^(0))V + (δ*_(g_b))^(0)ω′_b) ∈ Ḣ_b^(0,((3,0),C_0+3)).
*Killing rotations.* If R_V is Killing for g_b, K := g_b(R_V, ·) has δ*_(g_b)(χK) = dχ ⊗_s K, so
(□^C_b)*(χK) ∈ C_c^∞ and ω″ := −((P^C_b)*)⁻¹(□^C_b)*(χK) ∈ Ḣ_b^(1,C_0+2). The difference (χV + ω′_b) − (χK + ω″) lies in
ker(P^C_b)*, and in Ḣ_b^(1,α) for α < 1, as K − V = (g_b − ḡ)(R_V, ·) ∈ ρC^∞ ([[eq:iii-d2-2-3]]) and ω′_b begins at ρ²;
by [[lem:iii-e-2-1]] (1) with such an α ∈ (0, 1) it vanishes. So ω*^((−1))_(b,v1)(V) − χK = ω″ ∈ Ḣ_b^(1,C_0+2) and
h*_(b,v1)(V) = G_(g_b)(dχ ⊗_s K + (δ*_(g_b))^(0)ω″) ∈ Ḣ_b^(0,C_0+3).

*Regularity in b.* For a smooth curve b(τ) with b(0) = b, the formal derivative ω̇′ of ω′_(b(τ)) solves
(P^C_b)*ω̇′ = −(∂_τ(P^C_(b(τ)))*)ω′_b − ∂_τf_(b(τ)). ∂_τ(P^C_(b(τ)))* is a second-order b-operator with coefficients in
ρ⁴C^∞ near ∂X (the mass and rotation enter at ρ² and ρ³, counted as in [[lem:iii-d2-2-1]]), so the first term lies in
ρ⁶C^∞ + Ḣ_b^(−1,C_0+6) (as ω′_b ∈ Ḣ_b^(1,((2,0),C_0+2)); its ρ⁶C^∞ part is carried, like that of ∂_τf, by the expansion
terms of the last sentence), and ∂_τf lies in C_c^∞ + ρ⁴C^∞; [[lem:iii-e-2-1]] (1) with s = 0 bounds ω̇′ in
Ḣ_b^(0,C_0+2), with the loss of one derivative, and difference quotients converge to it as in [[lem:iii-d2-2-2]].
Iterating gives C^k into Ḣ_b^(1−k,C_0+2); the expansion terms, from [[lem:iii-a-1-5]], depend smoothly on b. The
statements for h* follow. *Vanishing inside the horizon* is [[sec:iii-e-2]], (b), as (P^C_b)*ω = 0 there. ∎

**Remark {#rem:s14-counting}** (Counting.) At A = 0 the dual states are one for the time translation, four for the
translations and six for the rotations: eleven, against seven (1 + 3 + 3) in dimension 3 + 1. The h* of the time
translation and of the six rotations decay to the weight C_0 + 3, and those of the four translations begin at ρ³.

**Remark {#rem:s14-polyhom}** (Polyhomogeneity.) The memberships of [[prop:iii-e-3-1]] can be improved to full
polyhomogeneity near ∂X, as in [Hin26]; only the remainder weight C_0 + 2, with C_0 large, is used later.

### The vector type 1 dual states {#sec:iii-e1}

This section proves, for the Myers–Perry metrics g_b with b near b₀, what [Hin26, Section 7.2.1, pp. 140–144]
establishes in dimension 3 + 1: the Lie derivative of g_b along the rotation vector fields ([Hin26, Lemma 7.5]) and the
structure of the vector type 1 dual states ([Hin26, Proposition 7.4]), whose leading term depends on the rotation only
through its bracket with the spin. In dimension 4 + 1 the spin is a matrix A ∈ 𝔰𝔬(4), and the cross product
a(b) × a(V) becomes the bracket W = [A, A_V]. [Hin26, Lemma 7.5] becomes an exact identity, δ*_(g_b)V_b = ½D_Ag_b(W),
from the O(4)-equivariance of the family of [[sec:iii-b-3-1]]; in its coordinates there is no pure gauge term at leading
order, and the leading term sits at ρ³, the order at which the spin enters. The correction of V_b sits at |x|⁻³, its
coefficient c_0 fixed by the vector type 1 indicial value 3(1 + 2v_Cγ_C). The Killing rotations form a space of
dimension 6, 4 or 2. [Hin26, (7.19)] holds in a stronger form: D_(g_b)Ric(0)*h♯ vanishes near ∂X, by the
self-adjointness of G D Ric; the argument of [Hin26] uses G² = Id, which fails in dimension 4 + 1.

#### Setting {#sec:iii-e1-1}

ℬ, b = (m, A), g_b, t_*, ρ = |x|⁻¹ near ∂X, ḡ, t̄ = t_* + |x|, χ, and the constants v_C, e_C, γ_C, C_0 are as in
[[sec:iii-e-1]]; g_b = Φ_m*g^KS_(m,A) as in [[sec:iii-b-3-1]]. C^∞ means smooth on X̄ in the trivialisation by dt_*,
dx^i. For W ∈ 𝔰𝔬(4) put

    R_W := (Wx)·∂_x,     V(W) := ḡ(R_W, ·) = (Wx)·dx,                                                    {#eq:iii-e1-1-1}

so that 𝒱₁ = {V(W) : W ∈ 𝔰𝔬(4)} is the six-dimensional space of rotation 1-forms of [[eq:iii-d2-1-2]], and
ρV(W) = (Wω)·dx ∈ C^∞, ω := x/|x|. For V = V(A_V) ∈ 𝒱₁ write V_b := g_b(R_(A_V), ·) = g_bḡ⁻¹V. P* := (P^C_b)* is the
adjoint of [[sec:iii-e-1]]; on stationary sections (□^C_b)* = 2(δ*_(g_b,E_C))*G_(g_b)δ*_(g_b) acts as P*.
ω*^((−1))_(b,v1)(V) and h*_(b,v1)(V) = G_(g_b)δ*_(g_b)ω*^((−1))_(b,v1)(V) are the states of [[prop:iii-e-3-1]].

#### The rotations {#sec:iii-e1-2}

**Lemma {#lem:iii-e1-2-1}** (Equivariance.) For O ∈ O(4) let φ_O(t, x) := (t, Ox). Then φ_O*g_((m,OAOᵀ)) = g_((m,A)), and
t_*, |x| and χ are φ_O-invariant.

*Proof.* In [[eq:iii-b-3-1]], s = −½tr(A²) and p² = Pf(A)² do not change under A ↦ OAOᵀ (Pf(OAOᵀ) = det O Pf(A)), so
neither does P, while 𝖬 ↦ O𝖬Oᵀ; hence Q(r, Ox) for OAOᵀ equals Q(r, x) for A, and by the uniqueness of the root
([[lem:iii-b-3-1]] (b)), r_(OAOᵀ)(Ox) = r_A(x). The vector 𝖬(rI + A)x/P becomes O times itself, so the 1-form ℓ of
[[eq:iii-b-3-2]] satisfies φ_O*ℓ_(OAOᵀ) = ℓ_A (v(Ox)·d(Ox) = (Ov(x))·O dx = v(x)·dx); xᵀA²𝖬²x, and so F and H, are
invariant; and η and dt are φ_O-invariant. So φ_O*g^KS_(m,OAOᵀ) = g^KS_(m,A). Φ_m and t_* = t − ψ(|x|) depend on x
through |x| only, and so commute with, resp. are invariant under, φ_O; χ is a function of |x|. ∎

**Lemma {#lem:iii-e1-2-2}** ([Hin26, Lemma 7.5] in dimension 4 + 1.) Let b = (m, A), A_V ∈ 𝔰𝔬(4), V := V(A_V),
R := R_(A_V) and W := [A, A_V]. Then exactly

    δ*_(g_b)V_b = ½D_Ag_((m,A))(W),     D_Ag_((m,A))(W) := (d/ds)g_((m,A+sW))|_(s=0),                    {#eq:iii-e1-2-1}

and near ∂X

    δ*_(g_b)V_b = mρ³(dt_* + 2 d|x|) ⊗_s ρV(W) + h̃_b(W),                                                {#eq:iii-e1-2-2}

with h̃_b : 𝔰𝔬(4) → ρ⁴C^∞(X̄; S²T*X) linear and smooth in b. So δ*_(g_b)V_b depends on V only through W, and the right
side of [[eq:iii-e1-2-1]] is defined for every W ∈ 𝔰𝔬(4).

*Proof.* [[eq:iii-e1-2-1]]: R generates φ_(O_s), O_s := e^(sA_V), so 𝓛_Rg_b = (d/ds)φ_(O_s)*g_b|_(s=0). By
[[lem:iii-e1-2-1]] with A replaced by O_sᵀAO_s, φ_(O_s)*g_((m,A)) = g_((m,O_sᵀAO_s)), and
(d/ds)O_sᵀAO_s|_(s=0) = AA_V − A_VA = W; so 𝓛_Rg_b = D_Ag_((m,A))(W). And δ*_g(g(R, ·)) = ½𝓛_Rg for every metric.

[[eq:iii-e1-2-2]]: write x = |x|ω. In [[eq:iii-b-3-1]], r = |x|u turns Q = 0 into
u⁴ − u² + ρ²(su² − s − ωᵀA²ω) + ρ⁴p² = 0, whose root u = 1 at ρ = 0 is simple; by the implicit function theorem
u = U(ρ², ω, A) is smooth with U = 1 + O(ρ²), the O(ρ²) even in A (the equation is). Then H = mρ²(1 + ρ²C^∞),
F = 1 + ρ²C^∞, and

    ℓ_A = ((U²I + ρ²(s + A²))(Uω + ρAω))/(U⁴ + sρ²U² + p²ρ⁴) · dx = d|x| + ρ ρV(A) + ρ²C^∞,

as ω·dx = d|x| and (Aω)·dx = ρV(A), with every coefficient smooth in (ρ, ω, A, m). Hence D_AH(W) ∈ ρ⁴C^∞ (it
differentiates the ρ²-corrections, even in A), D_Aℓ(W) = ρ ρV(W) + ρ²C^∞, and with k = dt + ℓ_A,

    D_Ag^KS(W) = D_AH(W) k ⊗ k + 2H k ⊗_s D_Aℓ(W) = 2mρ³(dt + d|x|) ⊗_s ρV(W) + ρ⁴C^∞,

linear in W, the ρ⁴ part smooth in (m, A). Φ_m does not depend on A, so D_Ag_b(W) = Φ_m*D_Ag^KS(W);
Φ_m*dt = dt − T_m′(|x|) d|x| with T_m′ ∈ ρ²C^∞, and the coefficients do not depend on t, so the expansion holds for g_b
in the coordinates (t, x) of [[sec:iii-b-3-1]]. Finally t = t_* + ψ(|x|) with ψ′(|x|) = 1 − 8m₀ρ² for large |x|
([[eq:iii-b-3-6]]), so dt + d|x| = dt_* + 2 d|x| + ρ²C^∞. With [[eq:iii-e1-2-1]] this is [[eq:iii-e1-2-2]]. ∎

In dimension 3 + 1, [Hin26, (7.20)] has in addition the term −δ*_(g_b)(ρS(a)S′dr + ½d̸(S(a)S′)) at leading order. That
term comes from coordinates built on the Boyer–Lindquist radius, in which the flat part of the Kerr family is not
Cartesian. Here the coordinates are those of [[sec:iii-b-3-1]], Kerr–Schild up to Φ_m, and there is no such term. In
three space dimensions the same argument, with the bracket of 𝔰𝔬(3) the cross product, gives the structure of
[Hin26, Lemma 7.5].

**Lemma {#lem:iii-e1-2-3}** (The Killing rotations.) R_(A_V) is a Killing field of g_b if and only if [A, A_V] = 0. If
A = O(aJ₁₂ + bJ₃₄)Oᵀ with O ∈ SO(4) and J_ij the elementary generators, then dim ker ad_A is 6 if a = b = 0, 4 if
a = ±b ≠ 0, and 2 otherwise.

*Proof.* R is Killing iff δ*_(g_b)V_b = 0, which holds if W = 0 by [[eq:iii-e1-2-1]]. Conversely, if δ*_(g_b)V_b = 0,
the ρ³ term of [[eq:iii-e1-2-2]] vanishes; as m > 0 and ρV(W) is angular, (dt_* + 2 d|x|) ⊗_s ρV(W) = 0 forces V(W) = 0,
so Wx = 0 for all x and W = 0. For the dimension, ad_(OA′Oᵀ) = Ad_O ad_(A′) Ad_O⁻¹, so let O = I.
𝔰𝔬(4) = Λ²₊ ⊕ Λ²₋, the self-dual and anti-self-dual 2-forms, two commuting ideals each isomorphic to 𝔰𝔬(3), and
A = ((a + b)/2)(J₁₂ + J₃₄) + ((a − b)/2)(J₁₂ − J₃₄) with J₁₂ ± J₃₄ ∈ Λ²_±. The centraliser of A is the sum of the
centralisers of its two components, each of dimension 1 for a nonzero element of 𝔰𝔬(3) and 3 for zero; so the dimension
is (1 or 3) + (1 or 3) according as a + b and a − b vanish. ∎

So the rotations for which [Hin26, (7.16)] holds, here h*_(b,v1)(V) ∈ Ḣ_b^(0,C_0+3) ([[prop:iii-e-3-1]] (2)), form a
space of dimension 6 at A = 0, 4 on {a = ±b ≠ 0} and 2 elsewhere ([[prop:iii-e1-3-1]] (3) gives the converse), where in
dimension 3 + 1 the dimensions are 3 and 1.

#### The structure of the vector type 1 dual states {#sec:iii-e1-3}

Let

    c_0 := m(1 + 2(1 + v_C)γ_C)/(3(1 + 2v_Cγ_C)),     κ_C := (1 + 2(v_C − 1)γ_C)/(1 + 2v_Cγ_C).          {#eq:iii-e1-3-1}

**Proposition {#prop:iii-e1-3-1}** ([Hin26, Proposition 7.4] in dimension 4 + 1.) Assume (Dyn). Write A(b) := A for
b = (m, A). The dual states of [[prop:iii-e-3-1]] can be written

    h*_(b,v1)(V) = h♯_(b,v1)([A(b), A_V]) + h♭_(b,v1)(V),     V = V(A_V) ∈ 𝒱₁,                           {#eq:iii-e1-3-2}

where:

(1) h♯_(b,v1)(W) ∈ ρ³C^∞(X̄; S²T*X) is linear in W ∈ 𝔰𝔬(4), smooth in b, vanishes where χ = 0, and has the ρ³ leading
term

    h̄♯(W) = mρ³(dt_* + κ_C d|x|) ⊗_s ρV(W);                                                             {#eq:iii-e1-3-3}

moreover, for every W ∈ 𝔰𝔬(4),

    (δ*_(g_b,E_C))*h♯_(b,v1)(W) ∈ ρ^(⌊C_0⌋+5)C^∞(X̄; T*X),
    (D_(g_b)Ric)^(0)*h♯_(b,v1)(W) ∈ C_c^∞(X°; S²T*X);                                                    {#eq:iii-e1-3-4}

(2) h♭_(b,v1)(V) ∈ Ḣ_b^(0,C_0+3)(X; S²T*X) is linear in V and of class C^k in b with values in Ḣ_b^(−k,C_0+3);

(3) h*_(b,v1)(V) ∈ Ḣ_b^(0,C_0+3) if and only if [A(b), A_V] = 0, that is ([[lem:iii-e1-2-3]]), if and only if R_(A_V)
is Killing for g_b.

*Proof. Step 1, the leading order.* For W ∈ 𝔰𝔬(4) put, on supp χ,

    k_b(W) := G_(g_b)(½D_Ag_b(W) + c_0 δ*_(g_b)(|x|⁻³V(W))),                                             {#eq:iii-e1-3-5}

linear in W and smooth in b. If W = [A, A_V], then k_b(W) = G_(g_b)δ*_(g_b)ω♯(V) with ω♯(V) := V_b + c_0|x|⁻³V(W), by
[[eq:iii-e1-2-1]]. Near ∂X: g_b − ḡ ∈ ρ²C^∞, so G_(g_b) − Ḡ ∈ ρ²C^∞ and δ*_(g_b) − δ̄* ∈ ρ³C^∞ (the Christoffel symbols);
with [[eq:iii-e1-2-2]] and dt_* + 2 d|x| = dt̄ + d|x|,

    k_b(W) = Ḡ(h_0 + c_0δ̄*(|x|⁻³V)) + ρ⁴C^∞,     h_0 := m|x|⁻⁴(dt̄ + d|x|) ⊗_s V,     V := V(W).

On Minkowski space (Cartesian (t̄, x), r := |x|, f = f(r)): δ̄*V = 0, V being Killing, so δ̄*(fV) = f′dr ⊗_s V; every
α ⊗_s V with α ∈ span{dt̄, dr} is trace-free, as V is angular, so Ḡ acts as the identity and e_C drops out;
δ̄(f dt̄ ⊗_s V) = 0 and δ̄(f dr ⊗_s V) = −½(f′ + 5f/r)V, from ∇dr = r⁻¹(dx² − dr²), ∇_(∂_r)V = r⁻¹V, Δr = 3/r and
div V = 0 (here δ̄ = −div); and with c̄_C = r⁻¹(dt̄ − v_C dr), ḡ⁻¹c̄_C = −r⁻¹(∂_t̄ + v_C∂_r),
(Ē_C)*h = γ_C(2ι_(ḡ⁻¹c̄_C)h − (2/3)(1 − e_C)c̄_C tr h) gives (Ē_C)*(f dt̄ ⊗_s V) = −γ_Cr⁻¹fV and
(Ē_C)*(f dr ⊗_s V) = −γ_Cv_Cr⁻¹fV. So

    2(δ̄ + Ē_C*)Ḡh_0 = −m(1 + 2γ_C(1 + v_C))r⁻⁵V,     2(δ̄ + Ē_C*)Ḡδ̄*(c_0r⁻³V) = 3c_0(1 + 2γ_Cv_C)r⁻⁵V,

which cancel by [[eq:iii-e1-3-1]]; 3(1 + 2v_Cγ_C) is the vector type 1 indicial value N(ρ⁻²P*, 2)
([[prop:np-10-31]] (i)). And (δ*_(g_b,E_C))* − (δ̄ + Ē_C*) ∈ ρ³Diff¹_b near ∂X (g_b − ḡ ∈ ρ²C^∞,
c_C − c̄_C ∈ ρ³C^∞, [[sec:iii-e-1]]), while δ̄ + Ē_C* ∈ ρDiff¹_b; hence

    f₁(W) := 2(δ*_(g_b,E_C))*(χk_b(W)) ∈ C_c^∞(X°) + ρ⁵C^∞,                                              {#eq:iii-e1-3-6}

the commutator with χ being supported where dχ ≠ 0. The leading term of k_b(W) is
h_0 − 3c_0r⁻⁴dr ⊗_s V = ρ³(m dt_* + (2m − 3c_0) d|x|) ⊗_s ρV, and 2m − 3c_0 = mκ_C: this is [[eq:iii-e1-3-3]].

*Step 2, the formal solution.* Let J := ⌊C_0⌋ + 2. Near ∂X, ρ⁻²P* is a b-differential operator with coefficients smooth
on X̄ and b-independent normal operator (as P^C_b − P̄^C ∈ ρ⁴Diff²_b), so P*(ρ^jc) = ρ^(j+2)N(ρ⁻²P*, j)c + ρ^(j+3)C^∞
for c ∈ C^∞(∂X; T*X|_(∂X)). For 3 ≤ j ≤ J, N(ρ⁻²P*, j) is invertible on C^∞(∂X). Indeed, in the trivialisation by
dt_*, dx¹, …, dx⁴, ρ⁻²P* is near ∂X a b-operator with values in 5 × 5 matrices. Its principal symbol at ∂X is, like
that of ρ⁻²P^C_b (the proof of [[lem:iv4-1-6]], (H2)), that of the Euclidean Laplacian in b-form times the identity,
since a formal adjoint for a smooth nondegenerate pairing has the adjoint principal symbol and this one is real and
scalar. So ρ⁻²P* is elliptic near ∂X and lies in the setting of [[sec:iii-a-1-1]] with N_E = 5. The number j is not an
indicial root of P*, whose indicial roots are 0, have negative real part, or have real part > C_0 + 2 ≥ J
([[lem:iii-e-2-1]] (2)); so by (E3) there, with Π = Id, N(ρ⁻²P*, j) maps C^∞(∂X) bijectively onto itself. Removing
in turn, for j = 3, …, J, the coefficient of ρ^(j+2) of the current remainder by ρ^jc_j(W), c_j(W) := −N(ρ⁻²P*, j)⁻¹
applied to that coefficient, gives ω′♯₁(W) := Σ_(j=3)^J ρ^jc_j(W), linear in W and smooth in b, with

    r_b(W) := f₁(W) + P*(χω′♯₁(W)) ∈ C_c^∞(X°) + ρ^(J+3)C^∞.                                             {#eq:iii-e1-3-7}

(This is [[lem:iii-a-1-5]] with no pole met.)

*Step 3, the solution.* As J + 3 = ⌊C_0⌋ + 5 > C_0 + 4, r_b(W) ∈ Ḣ_b^(0,C_0+4), and [[lem:iii-e-2-1]] (1) (s = 1,
α = C_0 + 2) gives ω′♭₁(W) := −(P*)⁻¹r_b(W) ∈ Ḣ_b^(1,C_0+2). Let V = V(A_V), W := [A, A_V], and
f₂(V) := 2(δ*_(g_b,E_C))*G_(g_b)(dχ ⊗_s ω♯(V)) ∈ C_c^∞(X°), ω′₂(V) := −(P*)⁻¹f₂(V) ∈ Ḣ_b^(1,C_0+2). Since
G_(g_b)δ*_(g_b)(χω♯(V)) = χk_b(W) + G_(g_b)(dχ ⊗_s ω♯(V)), P*(χω♯(V)) = f₁(W) + f₂(V), and

    ω̃ := χω♯(V) + χω′♯₁(W) + ω′♭₁(W) + ω′₂(V)

satisfies P*ω̃ = f₁ + f₂ + (r_b − f₁) − r_b − f₂ = 0. Moreover ω̃ − ω*^((−1))_(b,v1)(V) ∈ Ḣ_b^(1,α) for α ∈ (0, 1):
ω*^((−1))_(b,v1)(V) = χV + ω′_b with ω′_b ∈ Ḣ_b^(1,((2,0),C_0+2)), χ(V_b − V) = χ(g_b − ḡ)(R_(A_V), ·) ∈ ρC^∞,
χc_0|x|⁻³V(W) ∈ ρ²C^∞ and χω′♯₁ ∈ ρ³C^∞. Both lie in the kernel of P*, so by [[lem:iii-e-2-1]] (1) with such an α they
are equal, as in the argument for the Killing rotations in [[prop:iii-e-3-1]].

*Step 4, the splitting.* h*_(b,v1)(V) = G_(g_b)δ*_(g_b)ω̃ = h♯_(b,v1)(W) + h♭_(b,v1)(V) with

    h♯_(b,v1)(W) := χk_b(W) + G_(g_b)δ*_(g_b)(χω′♯₁(W)),
    h♭_(b,v1)(V) := G_(g_b)(dχ ⊗_s ω♯(V)) + G_(g_b)δ*_(g_b)(ω′♭₁([A, A_V]) + ω′₂(V)).

(1): h♯(W) is defined for every W, is linear in W and smooth in b, vanishes where χ = 0, and lies in ρ³C^∞ with leading
term that of k_b(W), [[eq:iii-e1-3-3]], the second summand being in ρ⁴C^∞. As 2(δ*_(g_b,E_C))*G_(g_b)δ*_(g_b) = P* on
stationary sections, 2(δ*_(g_b,E_C))*h♯(W) = f₁(W) + P*(χω′♯₁(W)) = r_b(W), the first part of [[eq:iii-e1-3-4]]. For
the second, two facts hold at a Ricci-flat g in every dimension: D_gRic(δ*_gω) = ½D_gRic(𝓛_(ω♯)g), which is
½𝓛_(ω♯)Ric(g) = 0; and G_gD_gRic, the linearised Einstein tensor there, is formally self-adjoint (it is, up to sign,
the second variation of the Einstein–Hilbert action), so with G_g symmetric and invertible, D_gRic*G_g = G_gD_gRic. As
every g_((m,A)) is Ricci-flat, D_(g_b)Ric(D_Ag_b(W)) = 0. Hence, writing χδ*y = δ*(χy) − dχ ⊗_s y,

    D_(g_b)Ric*h♯(W) = G_(g_b)D_(g_b)Ric(½χD_Ag_b(W) − c_0 dχ ⊗_s |x|⁻³V(W)),

and D_(g_b)Ric(½χD_Ag_b(W)) = ½[D_(g_b)Ric, χ]D_Ag_b(W) is supported where dχ ≠ 0: so
(D_(g_b)Ric)^(0)*h♯(W) ∈ C_c^∞(X°) (the stationary adjoint being that of the zero energy operator, [[sec:iii-e-1]]).
(2): G_(g_b)(dχ ⊗_s ω♯) ∈ C_c^∞, and δ*_(g_b) ∈ ρDiff¹_b maps Ḣ_b^(1,C_0+2) to Ḣ_b^(0,C_0+3); linearity in V is clear,
and the regularity in b follows as in [[prop:iii-e-3-1]], the sources r_b(W) and f₂(V) being smooth in b in
C_c^∞ + ρ^(J+3)C^∞, resp. C_c^∞. (3): if W = [A, A_V] ≠ 0, then h̄♯(W) ≠ 0 (m > 0, V(W) ≠ 0), a ρ³ term not in
Ḣ_b^(0,C_0+3), while h♭ is in it; if W = 0, h♯(0) = 0. ∎

**Remark {#rem:s14-dim3}** (Comparison with dimension 3 + 1.) [Hin26, (7.31) and (7.18)] are the counterparts in
dimension 3 + 1 of c_0|x|⁻³V(W) and [[eq:iii-e1-3-3]]: with m ↔ 2m_K (the mass enters as m|x|⁻² where the Kerr mass m_K
of [Hin26] enters as 2m_K|x|⁻¹), ρ³ ↔ ρ² and the bracket for the cross product, the same coefficients 1 + 2(v_C ∓ 1)γ_C
over 1 + 2v_Cγ_C appear, up to the orientation convention of the spin, and the indicial value 3(1 + 2v_Cγ_C) replaces
2 + 4γ_Cv_C. In [Hin26] the term ρS(a)S′dr + ½d̸(S(a)S′) of the ansatz cancels the pure gauge term of [Hin26, (7.20)];
here there is none to cancel.

### Simplicity of the roots and their distance from the integers {#sec:s14-simple}

The indicial roots of the linearised gauge-fixed Einstein operator, studied in [[ch:s15]], are made of the roots of
□^C shifted by −1, the roots of the gauge potential operator of [[ch:s13]] shifted by +1, and the roots of the physical
part. This section proves the two properties of the roots of □^C and of the explicit polynomials of [[ch:s13]] that
[[ch:s15]] uses: simplicity for every degree l ≥ 2, and a positive distance of the real parts from the integers, the
condition [Hin26, (8.13)]. Throughout, (v, e) = (1/2, 1/102400), and

    z := 4e_Υγ_Υ² = 4·10⁻⁶,     Q_l(ι′) := s² − (2 + 2κ + z)s + κ(κ + 1) + zκ,  s := ι′(ι′ − 1),  κ = l(l + 2),

where (e_Υ, γ_Υ) = (1/100, 1/100) are the constants of the gauge modification of [[ch:s13]]. For l ≥ 2 let ℛ^sc_l be the
list of the numbers −l, l + 2, 2 − l, l + 4, the four roots of ι ↦ Q_l(ι − 1), and ι − 1 for the six roots ι of P_l;
let ℛ^v_l be the list of −l, l + 2, 1 − l, l + 3 and ι − 1 for the two roots ι of p_(v); and let ℛ^t_l be the list
−l, l + 2. These are the indicial roots of that operator at scalar, vector and tensor type l ≥ 2 ([[ch:s15]]). The lists
ℛ^sc_0, ℛ^sc_1 and ℛ^v_1 of its indicial roots at scalar types 0 and 1 and vector type 1 are formed in the same way,
from the physical roots −l, l + 2, the roots of the gauge potential operator plus 1 and the roots of C, P_1 and p_(v)
minus 1, without the roots that [[ch:s15]] removes; their entries that do not depend on h and are not integers are
2 − ι^Υ_(s0,2) and 1 + ι^Υ_(s0,2) at scalar type 0, and the four roots 2 − ι^Υ_(s1,j), 1 + ι^Υ_(s1,j), j = 2, 3, of
Q_1(ι − 1) at scalar type 1, with ι^Υ_(s0,2) = ½ + (9/4 + z)^(1/2) and ι^Υ_(s1,j) as in [[lem:iii-d-4-1]].

**Proposition {#prop:np-10-52}** (Simplicity and [Hin26, (8.13)] for every l.) (i) For l ≥ 1 put u := l + 1. The four
roots of Q_l(ι − 1) are real and equal to l + 3 + d₁, −l − d₁, l + 2 + d₂ and 1 − l − d₂, where

    d₁ := ½((2u + 1)² + 2z + 4w)^(1/2) − ½(2u + 1),     d₂ := ½((2u − 1)² + 2z − 4w)^(1/2) − ½(2u − 1),
    w := (u² + z + z²/4)^(1/2) − u;

that is, ι^Υ_(sl,l+2) = l + 2 + d₁ and ι^Υ_(sl,l+1) = l + 1 + d₂ in the notation of [[lem:iii-d-4-1]]. Moreover
d₁ = z(u + 1)(1 + θ₁)/(2u(2u + 1)) and d₂ = z(u − 1)(1 + θ₂)/(2u(2u − 1)) with

    −2z/(2u + 1)² ≤ θ₁ ≤ z/(4(u + 1)),     −z/(4(u − 1)) − z/(2(2u − 1)²) ≤ θ₂ ≤ 0.                       {#eq:s14-theta}

In particular 0 < d₂ < d₁ < 1, and none of these roots is an integer.

(ii) There is a countable set 𝖹₂ ⊂ (0, 10⁻⁶] such that for h ∈ (0, 10⁻⁶] ∖ (𝖹₁ ∪ 𝖹₂), 𝖹₁ the set of
[[lem:iv4-1-3]] (b), and every l ≥ 2, the entries of each of ℛ^sc_l, ℛ^v_l and ℛ^t_l are pairwise distinct.

(iii) For h ∈ (0, 10⁻⁶] let ε_ind(h) be the infimum of dist(Re ι, ℤ) over the entries ι ∉ ℤ with |ι| ≤ 50 of all the
lists ℛ^sc_l (l ≥ 0), ℛ^v_l (l ≥ 1) and ℛ^t_l (l ≥ 2). There is a countable set 𝖹₃ ⊂ (0, 10⁻⁶] such that
ε_ind(h) > 0 for h ∉ 𝖹₃. For every h, ε_ind(h) ≤ δ_50, where

    δ_50 := d₂ at l = 50, u = 51,

is the distance of the entry −49 − δ_50 of ℛ^sc_50 from −49; and among the entries that do not depend on h, the least
distance of a non-integer entry with |ι| ≤ 50 from ℤ is δ_50. By (i), δ_50 ≤ 50z/(2·51·101) = 2·10⁻⁴/10302.

*Proof.* (i) As a quadratic in s, Q_l has discriminant (2 + 2κ + z)² − 4κ(κ + 1) − 4zκ = (z + 2)² + 4κ = 4u² + 4z + z²,
so its roots are s_± = (2 + 2κ + z ± (4u² + 4z + z²)^(1/2))/2 = u² + z/2 ± (u + w), both positive. For each,
ι′ = (1 ± (1 + 4s)^(1/2))/2, and 1 + 4s_± = (2u ± 1)² + 2z ± 4w. So the roots in ι = ι′ + 1 are as stated, and the
roots ι′ > ½, ½ + (¼ + s_±)^(1/2), are l + 2 + d₁ and l + 1 + d₂, which are ι^Υ_(sl,l+2) and ι^Υ_(sl,l+1).

For the bounds, w = (z + z²/4)/((u² + z + z²/4)^(1/2) + u). Its denominator lies between 2u and 2u + (z + z²/4)/(2u),
by (u² + y)^(1/2) ≤ u + y/(2u); hence w ≤ z(1 + z/4)/(2u), and w ≥ z/(2u) because
(z + z²/4)·2u ≥ z(2u + (z + z²/4)/(2u)) is equivalent to u² ≥ 1 + z/4. So

    (2z/u)(u − 1 − z/4) ≤ 2z − 4w ≤ (2z/u)(u − 1),     (2z/u)(u + 1) ≤ 2z + 4w ≤ (2z/u)(u + 1 + z/4),

and 2z − 4w > 0 as u ≥ 2. For A > 0 and ε ≥ 0, ε/(2A) − ε²/(8A³) ≤ (A² + ε)^(1/2) − A ≤ ε/(2A). With A = 2u − 1 and
ε = 2z − 4w this gives ε/(4A) − ε²/(16A³) ≤ d₂ ≤ ε/(4A); inserting the bounds on ε and dividing by
z(u − 1)/(2uA) gives θ₂ ≤ 0 and

    1 + θ₂ ≥ 1 − z/(4(u − 1)) − z(u − 1)/(2uA²) ≥ 1 − z/(4(u − 1)) − z/(2A²).

With A = 2u + 1 and ε = 2z + 4w the same gives 1 + θ₁ ≤ 1 + z/(4(u + 1)) and
1 + θ₁ ≥ 1 − z(u + 1 + z/4)²/(2u(u + 1)A²) ≥ 1 − 2z/A², as (u + 1 + z/4)² ≤ 4u(u + 1). These are
[[eq:s14-theta]]; they give θ₂ > −1, so d₂ > 0, and d₁ < 1. Finally

    d₁ − d₂ ≥ z(u + 1)/(2u(2u + 1)) − z(u − 1)/(2u(2u − 1)) − z²/(2u + 1)² = z/((2u + 1)(2u − 1)) − z²/(2u + 1)² > 0,

using θ₂ ≤ 0, θ₁ ≥ −2z/(2u + 1)² and (u + 1)/(u(2u + 1)) ≤ 1. The roots lie in the open unit intervals
(l + 3, l + 4), (−l − 1, −l), (l + 2, l + 3) and (−l, 1 − l).

(ii) *The entries free of h.* −l, l + 2, 2 − l, l + 4 are distinct for l ≥ 2, and so are −l, l + 2, 1 − l, l + 3; the
four roots of Q_l(ι − 1) lie in four disjoint open unit intervals, so they are distinct and differ from the integers.
*The roots of P_l and p_(v).* For h ∉ 𝖹₁ ([[lem:iv4-1-3]] (b)) they are simple. A root ι of P_l gives the entry ι − 1,
which equals an h-independent entry y′ exactly when ι = y′ + 1 =: y. For ℛ^sc_l the numbers y are 1 − l, l + 3, 3 − l,
l + 5 and, by (i), the four roots of Q_l(ι − 1) plus 1, which lie in (l + 4, l + 5), (−l, 1 − l), (l + 3, l + 4) and
(1 − l, 2 − l). For l ≥ 2 each such y satisfies y ≤ 1 or y ≥ 4, so P_l(y)|_(h=0) = 8v(y − 2)Q_5(y) ≠ 0 by
[[lem:s14-q5]] (a); hence P_l(y), a polynomial in h, vanishes for finitely many h. For ℛ^v_l, y ∈ {1 − l, l + 3, 2 − l,
l + 4} and p_(v)(y)|_(h=0) = −2v(y − 3) ≠ 0. Let 𝖹₂ be the union of these finite sets over all l ≥ 2.

(iii) Fix h > 0. By (i), the h-independent non-integer entries with |ι| ≤ 50 occur only for l ≤ 50, and by
[[prop:np-10-54]] (iii) only finitely many l have a root of P_l or p_(v) with |ι| ≤ 51; so the infimum is a minimum
over finitely many entries. The roots of Q_l(ι − 1), the entries 2 − ι^Υ_(s0,2), 1 + ι^Υ_(s0,2) and the roots of p_(v)
are real, so for them dist(Re ι, ℤ) > 0 unless ι ∈ ℤ. A non-real entry is ι − 1 for a non-real root ι of P_l (l ≥ 0),
and dist(Re(ι − 1), ℤ) = 0 means Re ι = k with k ∈ [−49, 51] an integer. By the argument of the proof of
[[lem:iv4-1-3]] (b), the set of h at which P_l has a non-real root with real part k is finite for each (l, k): the
limits of [[lem:s14-small-h]] admit no two roots with sum 2k, as ι₊ + ι₋ = 5 + 1/13653, and 2 + ι_± = 2k would make
2k − 2 a root of Q_5, which [[lem:s14-q5]] (a) excludes for 2k − 2 ≤ 1 and 2k − 2 ≥ 4, and which is false for
2k − 2 = 2. The same holds for C, whose finite limit root (4 + 5e)/(2 − 5e) is real and not an integer. Let 𝖹₃ be the
union of these finite sets over l ≥ 0 and k ∈ [−49, 51]; it is countable, and for h ∉ 𝖹₃ every non-integer entry
with |ι| ≤ 50 has dist(Re ι, ℤ) > 0, so ε_ind(h) > 0.

For the upper bound, 1 − l − d₂ at l = 50 is −49 − δ_50, an entry with |ι| < 50 for every h, at distance δ_50 from ℤ,
and δ_50 ≤ 50z/(2·51·101) by θ₂ ≤ 0. Among the h-independent entries the distances from ℤ are ι^Υ_(s0,2) − 2 at
scalar type 0 and, at l ≥ 1, d₁ and d₂, all below ½: 1 − l − d₂ has |ι| ≤ 50 iff l ≤ 50, l + 2 + d₂ iff l ≤ 47,
−l − d₁ iff l ≤ 49, and l + 3 + d₁ iff l ≤ 46. First, ι^Υ_(s0,2) − 2 = z/((9/4 + z)^(1/2) + 3/2) > z/(3 + z/3) >
10⁻⁶ > δ_50.
Next, f(u) := (u − 1)/(u(2u − 1)) is decreasing for u ≥ 2 (the numerator of f′ is −2u² + 4u − 1 < 0), so for
2 ≤ u ≤ 50, f(u)/f(51) ≥ f(50)/f(51) = 252399/247500 > 1.0197; with [[eq:s14-theta]],

    d₂(u) = ½zf(u)(1 + θ₂) ≥ ½zf(51)·1.0197·(1 − z/4 − z/18) > ½zf(51) ≥ d₂(51) = δ_50,

and d₁(u) > d₂(u) by (i). So the least distance is d₂ at l = 50. ∎

**Remark {#rem:s14-delta50}** (The constants ε_ind(h) and δ_50.) ε_ind(h) is the largest number that the bound
[[eq:iii-f1-2-2]] of [[ch:s15]] admits as its constant ε_ind at γ_C = h⁻¹, when ε_ind(h) ≤ 1; the ε_ind of [[ch:s15]] is
any number in (0, min(1, ε_ind(h))]. The number δ_50 is a constant of its own: it is fixed by the gauge parameters (e_Υ,
γ_Υ) of [[ch:s13]] alone, through z, and not by h, being ι^Υ_(s50,51) − 51, the distance from 51 of a root of the gauge
potential operator at scalar type 50. It is neither the constant of [[ch:s13]] that bounds from below the distances from
ℤ of the roots of the gauge potential operator with |Re ι| ≤ 10, nor the ε_ind of [[ch:s15]], which it bounds from
above. Its value is given by [[lem:s14-delta50]], which does not involve h; [[cor:s14-eps-ind-point]] proves
ε_ind(10⁻⁶) = δ_50.

### The indicial roots at the damping point γ_C = 10⁶ {#sec:s14-pa}

This section determines the number ε_ind(h) of [[prop:np-10-52]] (iii) at h = 10⁻⁶, that is at γ_C = 10⁶, and shows that
there the real parts of the non-integer roots ι with |ι − 1| ≤ 50 of P_l, P_0 and p_(v) keep a distance of more than
2.93·10⁻⁶ from the integers. The point h = 10⁻⁶ is the right end of the interval (0, 10⁻⁶] on which [[prop:np-10-52]]
(iii) defines ε_ind; it does not lie in the set 𝖧 of [[eq:iv4-0-1]] on which [[thm:iii-e-1-1]] is stated, and
[[rem:s14-eps-ind-scope]] says what this section gives for h ∈ 𝖧. As in [[sec:s14-model]], (v, e) = (1/2, 1/102400), κ =
l(l + 2), and P_l, P_0, p_(v) and C are the polynomials of [[prop:np-10-12]] at this point. Throughout this section

    h := 10⁻⁶,     ε₀ := e/h = 625/64,     x := hκ,     δ_C := 2.94·10⁻⁶,

and z = 4e_Υγ_Υ² = 4·10⁻⁶ as in [[sec:s14-simple]]. An entry of the lists of [[prop:np-10-52]] that comes from a
root ι of P_l, P_0 or p_(v) is ι − 1, and its modulus is at most 50 exactly when |ι − 1| ≤ 50. The tables this
section uses are in [[sec:tab-a]].

The elementary bounds, for a > 0 and 0 ≤ y ≤ 8a²,

    a + y/(2a) − y²/(8a³) ≤ (a² + y)^(1/2) ≤ a + y/(2a),                                                {#eq:s14-pa-sqrt}

follow from (a + y/(2a))² = a² + y + y²/(4a²) and (a + y/(2a) − y²/(8a³))² = a² + y − (y³/(8a⁴))(1 − y/(8a²)).

#### The number δ_50 {#sec:s14-pa-delta}

**Lemma {#lem:s14-delta50}** (The value of δ_50.) The number δ_50 of [[prop:np-10-52]] (iii), which depends on z
only and not on h, satisfies

    1.941370568463·10⁻⁸ < δ_50 < 1.941370568464·10⁻⁸,

so δ_50 = 1.94137056846·10⁻⁸ to twelve significant figures; and δ_50 < 2·10⁻⁴/10302 < 1.9413707·10⁻⁸ < 1.94138·10⁻⁸.

*Proof.* By [[prop:np-10-52]] (i) at u = 51, δ_50 = d₂ = ½((101² + B)^(1/2) − 101) = B/(2(101 + (10201 + B)^(1/2))),
where B := 2z − 4w, w := (2601 + A)^(1/2) − 51 = A/(51 + (2601 + A)^(1/2)) and A := z + z²/4 = 4.000004·10⁻⁶. By
[[eq:s14-pa-sqrt]] with a = 51, the denominator of w lies between 102 + A/102 − A²/(8·51³) and 102 + A/102, where
A/102 = 3.921572549019…·10⁻⁸ and A²/(8·51³) < 1.6·10⁻¹⁷. Dividing,

    3.921572547511889·10⁻⁸ < w < 3.921572547511890·10⁻⁸,     7.843137098099524·10⁻⁶ < B < 7.843137098099525·10⁻⁶.

By [[eq:s14-pa-sqrt]] with a = 101,

    B/(404 + B/101) ≤ δ_50 ≤ B/(404 + B/101 − B²/(4·101³)),

with 7.7654·10⁻⁸ < B/101 < 7.7655·10⁻⁸ and B²/(4·101³) < 1.5·10⁻¹⁷. With the bounds on B the left quotient exceeds
1.94137056846335·10⁻⁸ and the right one is below 1.94137056846336·10⁻⁸, which gives the first claim. For the second,
w > z/102: indeed A·102 > z(102 + A/102) because 102(A − z) = 25.5z² > zA/102. So δ_50 < B/404 < (2z − 4z/102)/404 =
50z/10302 = 2·10⁻⁴/10302 = 1.94137060764…·10⁻⁸. ∎

#### The vector type and the scalar type 0 {#sec:s14-pa-vector}

**Lemma {#lem:s14-vector-distance}** (The vector type at γ_C = 10⁶.) Let l ≥ 1 and Γ := 250002000000. The roots of
p_(v) are −499999 ± (Γ + (l + 1)²)^(1/2). The smaller is below −10⁶. The larger, ι_v, is at least 3, and if ι_v ≤ 51
and ι_v ∉ ℤ then

    dist(ι_v, ℤ) ≥ 3/1000100 > 2.9997·10⁻⁶.

*Proof.* At h = 10⁻⁶ and v = 1/2, −h⁻¹p_(v)(ι) = ι² + 999998ι − κ − 3·10⁶ ([[prop:np-10-12]] (ii)). Since
499999² = 249999000001 and κ = (l + 1)² − 1, (ι + 499999)² = Γ + (l + 1)² at a root, which gives the roots; ι_v
increases with l and equals (250002000004)^(1/2) − 499999 = 500002 − 499999 = 3 at l = 1.

Let ι_v ≤ 51 and let n be the integer nearest ι_v; then 3 ≤ n ≤ 51. Put k := n − 1. Expanding,
(n + 499999)² − Γ = n² + 999998n − 2999999 = X_k, where X_k := k² + 10⁶(k − 2). Hence

    (ι_v − n)(ι_v + n + 999998) = (ι_v + 499999)² − (n + 499999)² = (l + 1)² − X_k,

and if ι_v ≠ n the integer (l + 1)² − X_k is not 0. We show that its modulus is at least 3. As 10⁶ = 2⁶·5⁶,
X_k ≡ k² modulo 64 and modulo 25. Modulo 4, (l + 1)² − X_k ≡ (l + 1)² − k² ∈ {0, 1, −1}, so it is not ±2. Suppose
(l + 1)² − X_k = f with f = ±1, that is X_k + f = (l + 1)² is a square. Modulo 8 the squares are 0, 1, 4: if k is
odd, k² + 1 ≡ 2, so f = −1; if k ≡ 2 (mod 4), k² ± 1 ≡ 5 or 3, impossible; if 4 | k, k² − 1 ≡ 7, so f = +1. Modulo
5 the squares are 0, 1, 4: f = +1 excludes k ≡ ±1 and f = −1 excludes k ≡ ±2 (mod 5). If k² + f ≡ 0 (mod 5) it must
be ≡ 0 (mod 25), a square divisible by 5 being divisible by 25; among 2 ≤ k ≤ 50 this leaves, of
k ∈ {8, 12, 28, 32, 48} with f = +1, only k = 32 (k² + 1 = 65, 145, 785, 1025, 2305), and of the odd k ≡ ±1 (mod 5)
with f = −1 only k = 49 (k² − 1 = 2400). What remains is f = +1 with k ∈ {20, 32, 40} and f = −1 with
k ∈ {5, 15, 25, 35, 45, 49}; for these nine, X_k + f lies strictly between two consecutive squares
([[sec:tab-a-vector]]). So |(l + 1)² − X_k| ≥ 3, and since ι_v ≤ 51 and
n ≤ 51, |ι_v − n| = |(l + 1)² − X_k|/(ι_v + n + 999998) ≥ 3/1000100. The smaller root is −499999 − (Γ + (l + 1)²)^(1/2) <
−10⁶. ∎

**Lemma {#lem:s14-scalar-zero}** (The scalar type 0 at γ_C = 10⁶.) The root ι₁ > 2 of C (proof of
[[prop:np-10-54]]) satisfies 2 + δ_C < ι₁ < 5/2.

*Proof.* With C₀(ι) = (5e − 2)ι + 5e + 4 and C_h = 3h(1 + 2ι − ι²) + h²ι(3 + 2ι − ι²) + ehι(ι + 1), as in the proof
of [[prop:np-10-54]], C₀(2 + δ_C) = 15e − (2 − 5e)δ_C > 1.46·10⁻⁴ − 5.9·10⁻⁶ > 0 and C_h(2 + δ_C) > 0, as
1 + 2ι − ι² and 3 + 2ι − ι² are positive at ι = 2 + δ_C. At ι = 5/2, C₀ = −1 + 35e/2 < 0 and
C_h = −3h/4 + 35h²/8 + 35eh/4 < 0. C has exactly one root in (2, ∞), with C(2) > 0, so C > 0 on (2, ι₁) and C < 0 on
(ι₁, ∞), and the two signs place ι₁ in (2 + δ_C, 5/2). ∎

#### The sextic: decomposition, majorants and counting {#sec:s14-pa-sextic}

**Lemma {#lem:s14-sextic-split}** (The sextic at γ_C = 10⁶.) Let l ≥ 1.

(i) P_l(ι) = U(ι, x) + hW(ι, x), where

    U := (2 + x − ι)𝒬(ι, x),   𝒬(ι, x) := 2ι² − (3x + 10)ι + x² + (5 + 3ε₀)x + 12,   W := R₁ + hR₂ + h²R₃,
                                                                                                   {#eq:s14-pa-split}

with R₁, R₂, R₃ the polynomials of [[sec:tab-a-split]]; the coefficients of 64·10¹⁸P_l in ι are those of
[[sec:tab-a-sextic]].

(ii) 𝒬(2 + x, x) = 3(ε₀ − 1)x = 1683x/64, ∂_ι𝒬 = 4ι − 3x − 10, and W(2 + x, x) = −(1683/64)x c(x), with
c = c⁰ + hc₁ + h²c₂,

    c⁰(x) := x² + 5866x/1683 + 5000/561,     c₁(x) := 64x⁴/1683 − 2308x³/1683 − 4439x²/561 − 1019x/99 − 2,
    c₂(x) := 64x⁵/1683 − 241x⁴/1683 − 415x³/187 − 625x²/99 − 11329x/1683 − 1378/561.

One has |hc₁ + h²c₂| < 0.011, 0.43 and 1.43 on [0, 16], [0, 50] and [0, 70]; hence c > 0 on [0, 70], and c ≤ 11, 39,
321, 2684, 5155 on [0, 0.5], [0, 4], [0, 16], [0, 50], [0, 70].

(iii) The discriminant of 𝒬(·, x) is Δ_𝒬(x) := x² − 1715x/8 + 4, with roots x₋ ∈ (0.01866, 0.01867) and x₊ > 214.
For x₋ < x < x₊ the roots of 𝒬(·, x) are ζ and ζ̄,

    ζ := a + ib,     a = a(x) := (3x + 10)/4,     b = b(x) := (−Δ_𝒬(x))^(1/2)/4 > 0,

with |2 + x − ζ|² = 𝒬(2 + x, x)/2 = 1683x/128, |ζ|² = (8x² + 2195x/8 + 96)/16, and b increasing on (x₋, 107].

(iv) For 0 < x ≤ x₋ the roots of 𝒬(·, x) are real, a ± Δ_𝒬(x)^(1/2)/4, and for 0.018 ≤ x ≤ 0.5 both roots of 𝒬(·, x)
lie at distance more than 0.40 from 2 + x.

(v) Let Λ(x) be −½ times the coefficient of ι² in the remainder of W(·, x) on division by U(·, x). Then
Λ = Λ⁰ + hΛ₁ + h²Λ₂ with

    Λ⁰ = 17x²/8 − 5851x/128 − 9055/128,     Λ₁ = 47x³/8 − 2587x²/16 − 1079831x/8192 − 43031/128,
    Λ₂ = 129x⁴/32 − 36419x³/512 − 157055x²/32768 + 1864635x/16384 − 12933/64,

and for x₋ < x < x₊, with Π := Λ − c,

    Re(W(ζ, x)/∂_ιU(ζ, x)) = Π(x)/2.                                                                    {#eq:s14-pa-re}

Here Π⁰ := Λ⁰ − c⁰ = 9x²/8 − 10598081x/215424 − 5719855/71808; |Π − Π⁰| < 0.57 on [0, 35]
and < 4.17 on [0, 70]; |Π⁰| ≤ 618 and |Π⁰′| ≤ 49.2 on [0, 35], |Π⁰| ≤ 1990 and |Π⁰′| ≤ 108.4 on [0, 70].

*Proof.* (i) Put e = ε₀h and κ = x/h in the matrix [[eq:s14-nl]], multiply its third column by h and divide its
third row by h. This leaves the determinant unchanged and gives M⁰ + hM¹, where

    M⁰ := ( 2 + x − ι      2(ι − 2)        2x        )      M¹ := ( 2ι − ι²         0                       0           )
          ( 0              4 + x − 2ι      −x        ),           ( 2ε₀(ι + 1)      (ι + 1)(ε₀ + 3 − ι)     −2x         )
          ( −2ε₀           −(ε₀ + 2)       3 + x − ι )            ( 0               0                       2ι − ι² − 1 )

(the middle entry of M¹ is 3 + 2ι − ι² + ε₀(ι + 1)). Since the determinant is linear in each row, P_l is a
polynomial of degree at most 3 in h: its coefficient of h⁰ is det M⁰, that of h¹ the sum of the three determinants
of M⁰ with one row replaced by the same row of M¹, that of h² the sum of the three determinants of M¹ with one row
replaced by the same row of M⁰, and that of h³ is det M¹. Expanding det M⁰ along its first column and det M¹ along
its first row,

    det M⁰ = (2 + x − ι)((4 + x − 2ι)(3 + x − ι) − (ε₀ + 2)x) + 4ε₀x(2 + x − ι) = (2 + x − ι)𝒬(ι, x) = U,
    det M¹ = (2ι − ι²)(ι + 1)(ε₀ + 3 − ι)(2ι − ι² − 1) = ι(ι − 2)(ι − 1)²(ι + 1)(ε₀ + 3 − ι) = R₃.

The first and the third rows of M¹ have one nonzero entry each; expanding along them, and expanding along its first
column the determinant D₂ of M⁰ with its second row replaced by that of M¹,

    R₁ = (2ι − ι²)((4 + x − 2ι)(3 + x − ι) − (ε₀ + 2)x) + D₂ − (ι − 1)²(2 + x − ι)(4 + x − 2ι),
    D₂ = (2 + x − ι)((ι + 1)(ε₀ + 3 − ι)(3 + x − ι) − 2(ε₀ + 2)x) − 4ε₀(ι + 1)((ι − 2)(3 + x − ι) + (ε₀ + 2)x)
         + 4ε₀x(2(ι − 2) + (ι + 1)(ε₀ + 3 − ι)),

and likewise, replacing the first, the second and the third row of M¹ by that of M⁰,

    R₂ = −(ι − 1)²(ι + 1)((2 + x − ι)(ε₀ + 3 − ι) − 4ε₀(ι − 2)) − (2ι − ι²)(ι − 1)²(4 + x − 2ι)
         + (2ι − ι²)((ι + 1)(ε₀ + 3 − ι)(3 + x − ι) − 2(ε₀ + 2)x).

Multiplying out gives the polynomials R₁ and R₂ of [[sec:tab-a-split]]; these are identities in (ι, x, h, ε₀).
Substituting x = hκ, ε₀ = 625/64 and h = 10⁻⁶ gives the coefficients of [[sec:tab-a-sextic]].

(ii) 𝒬(2 + x, x) = 8 + 8x + 2x² − (3x + 10)(2 + x) + x² + 5x + 3ε₀x + 12 = (3ε₀ − 3)x. The value of W at ι = 2 + x is
the s-free part of R₁(2 + x + s, x) ([[sec:tab-a-split]]), −1683x³/64 − 2933x²/32 − 1875x/8 = −(1683/64)x c⁰(x), plus
h R₂(2 + x, x) + h² R₃(2 + x). From the formulas of (i),

    R₂(2 + x, x) = −x(x⁴ + 3x³ − 3x² − 7x + 6 − ε₀(4x³ + 21x² + 27x + 6)),
    R₃(2 + x) = x(2 + x)(1 + x)²(3 + x)(ε₀ + 1 − x),

which at ε₀ = 625/64 are −(1683/64)x c₁(x) and −(1683/64)x c₂(x); indeed c₂ = (2 + x)(1 + x)²(3 + x)(64x − 689)/1683.
The bounds on hc₁ + h²c₂ follow by summing the absolute values of the terms at the right end of each interval, and
the bounds on c from c⁰(0.5) < 10.92, c⁰(4) < 38.86, c⁰(16) < 320.69, c⁰(50) < 2683.2 and c⁰(70) < 5153, c⁰ being
increasing on [0, ∞).

(iii) The discriminant is (3x + 10)² − 8(x² + (5 + 3ε₀)x + 12) = x² − (24ε₀ − 20)x + 4, and 24ε₀ − 20 = 1715/8;
Δ_𝒬(0.01866) > 0 > Δ_𝒬(0.01867). For complex roots |2 + x − ζ|² = (2 + x − ζ)(2 + x − ζ̄) = 𝒬(2 + x, x)/2,
and |ζ|² = a² + b² = ((3x + 10)² − x² + 1715x/8 − 4)/16. b² = −Δ_𝒬/16 has derivative (1715/8 − 2x)/16 > 0 for x < 107.

(iv) On [0.018, x₋], Δ_𝒬 decreases from Δ_𝒬(0.018) < 0.1416, so the smaller root a − Δ_𝒬^(1/2)/4 exceeds
2 + x + (1/2 − x/4) − 0.0941 > 2 + x + 0.401; the larger one is farther. On [x₋, 0.5], |2 + x − ζ| = (1683x/128)^(1/2)
≥ (1683·0.01866/128)^(1/2) > 0.49.

(v) For x₋ < x < x₊ the roots of U(·, x) are 2 + x, ζ and ζ̄, distinct since 𝒬(2 + x, x) ≠ 0 and b > 0, and U has
leading coefficient −2 in ι. For a cubic U with leading coefficient −2 and distinct roots r₁, r₂, r₃, and any
polynomial F, Σ_j F(r_j)/U′(r_j) = −½·(coefficient of ι² in the remainder of F modulo U), because F and its
remainder agree at the roots, and for the polynomials 1, ι, ι² the sum is 0, 0, −½ (Lagrange interpolation of the
remainder at the three roots). So Λ(x) = Σ_j W(r_j)/∂_ιU(r_j). W and U have real coefficients, so
2 Re(W(ζ)/∂_ιU(ζ)) = W(ζ)/∂_ιU(ζ) + W(ζ̄)/∂_ιU(ζ̄) = Λ(x) − W(2 + x, x)/∂_ιU(2 + x, x), and
∂_ιU(2 + x, x) = −𝒬(2 + x, x), so by (ii) the last quotient is c(x). The quotient of W by U is the polynomial 𝒲 of
[[sec:tab-a-split]]: multiplying out, W − 𝒲U has degree at most 2 in ι, and its coefficient of ι² is
−2(Λ⁰ + hΛ₁ + h²Λ₂). The bounds on Π − Π⁰ = h(Λ₁ − c₁) + h²(Λ₂ − c₂) follow by summing the absolute values of the
terms at x = 35 and x = 70; those on the quadratic Π⁰ and on Π⁰′ = 9x/4 − 10598081/215424 from its vertex value
−617.5 at x = 21.87 and its values −79.66, −423.4 and 1989.1 at x = 0, 35, 70. ∎

**Lemma {#lem:s14-majorant}** (Majorants.) Let g(s, x) = Σ_(j,k) g_jk s^j x^k be a polynomial, p a function of x (the
centre), and f(ι, x) := g(ι − p(x), x). Put ḡ(S, T) := Σ_(j,k) |g_jk| S^j T^k. Then |f(ι, x)| ≤ ḡ(S, T)
whenever |ι − p(x)| ≤ S and 0 ≤ x ≤ T, and ḡ increases in S and in T.

*Proof.* The triangle inequality, term by term. ∎

We write N̄ := R̄₂ + hR̄₃ and N̄′ := R̄₂′ + hR̄₃′, which bound R₂ + hR₃ and its ι-derivative on |ι| ≤ S, 0 ≤ x ≤ T
(centre p = 0), and M̄_B, M̄_a (with M̄_B′, M̄_a′ for the s-derivatives) for the majorants of the re-expansions R₁(2 +
x + s, x) and R₁(a(x) + s, x), polynomials in (s, x) with the centres p = 2 + x and p = a(x); R̄_j, R̄_j′ and the two
re-expansions are printed in [[sec:tab-a-split]], and M̄_B, M̄_a, M̄_B′, M̄_a′ are their majorants. By the lemma, on |ι
− p| ≤ ϱ with p = 2 + x, resp. p = ζ (so that |ι − a| ≤ b + ϱ
and |ι| ≤ |ζ| + ϱ), and x_a ≤ x ≤ x_b for an interval [x_a, x_b] of [[sec:tab-a-pieces]],

    |W| ≤ M̄_B(ϱ, x_b) + hN̄(2 + x_b + ϱ, x_b),   resp.   |W| ≤ M̄_a(b + ϱ, x_b) + hN̄(|ζ| + ϱ, x_b),

and likewise for ∂_ιW with the primed majorants.

**Lemma {#lem:s14-fixed-point}** (A perturbed simple root.) Let p ∈ ℂ, ϱ > 0 and D := {|ι − p| ≤ ϱ}; let V and W be
polynomials with V ≠ 0 on D, and put Ξ := −hW/V. If |Ξ| ≤ ϱ and |Ξ′| ≤ L_Ξ < 1 on D, then (ι − p)V + hW has exactly
one zero ι* in D, and

    |ι* − p| ≤ |Ξ(p)|/(1 − L_Ξ),     |ι* − p − Ξ(p)| ≤ L_Ξ|Ξ(p)|/(1 − L_Ξ).

If p is real and V, W have real coefficients, ι* is real. On D, |Ξ′| ≤ h(sup|W′|/inf|V| + sup|W|·sup|V′|/inf|V|²).

*Proof.* The zeros of (ι − p)V + hW in D are the fixed points of ι ↦ p + Ξ(ι), which maps the closed convex set D into
itself and is a contraction with constant L_Ξ there; so there is exactly one, ι*. Then |ι* − p| = |Ξ(ι*)| ≤ |Ξ(p)| +
L_Ξ|ι* − p|, and |ι* − p − Ξ(p)| = |Ξ(ι*) − Ξ(p)| ≤ L_Ξ|ι* − p|. In the real case the conjugate of ι* is a zero in D,
so equals ι*. The last bound is the quotient rule. ∎

**Lemma {#lem:s14-sextic-count}** (Counting the roots.) (a) For 0 < x ≤ 70, P_l has exactly three roots, counted with
multiplicity, in |ι| < 1000. (b) For x ≥ 70, P_l has no root with |ι − 1| ≤ 50.

*Proof.* (a) For x ≤ 70 the roots of U(·, x) are 2 + x ≤ 72 and the roots of 𝒬(·, x), which by
[[lem:s14-sextic-split]] (iii)–(iv) have modulus at most (3657)^(1/2) < 61. On |ι| = 1000,
therefore, |U| ≥ 928·2·939² > 1.63·10⁹, while by [[lem:s14-majorant]] with p = 0

    |hW| ≤ h(R̄₁(1000, 70) + hR̄₂(1000, 70) + h²R̄₃(1000)) < 10⁻⁶(5.67·10¹² + 4.3·10⁹ + 1.02·10⁶) < 5.7·10⁶.

By Rouché's theorem P_l = U + hW has three zeros in |ι| < 1000, as U has.

(b) If |ι − 1| ≤ 50, then |ι| ≤ 51, Re ι ≤ 51 and |2 + x − ι| ≥ x − 49, and |hW| ≤ h(R̄₁ + hR̄₂ + h²R̄₃)(51, x) ≤
0.00862x² + 1.3823x + 45.381. If 70 ≤ x < x₊, both roots of 𝒬 have real part a = (3x + 10)/4, so they lie at
distance at least y := (3x − 194)/4 ≥ 4 from ι, and |U| ≥ 2(x − 49)y² ≥ 42y²; with x = (4y + 194)/3 the bound
on |hW| becomes at most 0.0156y² + 3.36y + 172, which is less than 42y² for y ≥ 4. If x ≥ x₊, the roots of 𝒬 are real
and at least (3x + 10 − x)/4, as Δ_𝒬(x)^(1/2) < x, so they lie at distance at least y′ := (2x − 194)/4 ≥ 58 from ι,
and |U| ≥ 330y′², while with x = 2y′ + 97 the bound on |hW| becomes at most 0.0345y′² + 6.2y′ + 261 < 330y′². In both
cases |hW| < |U| on the disc, so P_l has no zero there. ∎

**Corollary {#cor:s14-remote-point}** (The remote roots at γ_C = 10⁶.) Let l ≥ 1 and x ≤ 70. The three
roots of P_l in |ι| < 1000 given by [[lem:s14-sextic-count]] (a) are its three roots with real part at least 2, and
its other three roots have real part less than −5·10⁵.

*Proof.* By [[prop:s14-scalar-every-h]], three roots of P_l have real part less than −5·10⁵, hence modulus greater
than 1000, and the other three have real part at least 2. The three roots in |ι| < 1000 of [[lem:s14-sextic-count]] (a)
are therefore the latter. ∎

#### Degrees with κ ≤ 18000 {#sec:s14-pa-small}

**Lemma {#lem:s14-sextic-small}** (The roots near 2 and 3.) Let 1 ≤ l ≤ 133, so that 3 ≤ κ ≤ 17955 and
3h ≤ x < 0.018 < x₋. The three roots of P_l in |ι| < 1000 are real, and:

(a) for l = 1 they are 2 and one root in each of (2 + 3h, a(x)) and (a(x), 3 − δ_C);

(b) for l = 2 they lie one in each of (2 + 2.93h, 2 + 2.94h), (2 + 8h, a(x)) and (a(x), 3 − δ_C);

(c) for 3 ≤ l ≤ 133 they lie one in each of (2 + δ_C, 2 + x), (2 + x, a(x)) and (a(x), 3 − δ_C).

*Proof.* We use four signs.

(α) P_l(2 + x) = hW(2 + x, x) = −(1683/64)h x c(x) < 0, by [[lem:s14-sextic-split]] (ii), as U(2 + x, x) = 0.

(β) P_l(a(x)) > 0. Indeed 2 + x − a = −(2 − x)/4 and 𝒬(a, x) = −Δ_𝒬(x)/8, so U(a, x) = (2 − x)Δ_𝒬(x)/32 ≥
1.982·0.1415/32 > 0.0087, Δ_𝒬 being decreasing on [0, 0.018]; and |W(a, x)| ≤ M̄_a(0, 0.018) + hN̄(2.52, 0.018) < 49,
the s-free part of R₁(a + s, x) being at most 47.6 in modulus there. So |hW| < 5·10⁻⁵.

(γ) P_l(3 − δ_C) < 0. By [[sec:tab-a-expansions]] with ξ = −2.94, P_l(3 − δ_C) = h(L₀(−2.94, κ) + E) with
L₀(−2.94, κ) = −1619κ/64 − 2.12 and |E| ≤ h(10⁻⁶κ³ + 24.3κ² + 414κ + 1290) ≤ 0.439κ + 0.0013 for κ ≤ 18000.

(δ) By [[sec:tab-a-expansions]], P_l(2 + hξ) = h²(G₀(ξ, κ) + E) with |E| ≤ h(κ³ + 20κ² + 690κ + 1251) for |ξ| ≤ 3.
At κ = 8, |E| ≤ 0.0086, G₀(2.93, 8) = 0.8968… and G₀(2.94, 8) = −2.9043…, so P_2(2 + 2.93h) > 0 > P_2(2 + 2.94h).
For 15 ≤ κ ≤ 18000, G₀(2.94, κ) = (1811κ² − 11133.66κ)/64 − 422.1968… ≥ 28.29κ² − 174κ − 422.2, while hκ³ ≤ 0.018κ²
gives |E| ≤ 0.0181κ² + 0.0007κ + 0.0013; the difference exceeds 3300 at κ = 15 and increases, so P_l(2 + δ_C) > 0.

In (c), 2 + δ_C < 2 + x < a(x) < 3 − δ_C and the signs of P_l at these points are +, −, +, −; so P_l has a root in
each of the three open intervals. These are three distinct roots in |ι| < 1000, hence all of them by
[[lem:s14-sextic-count]]. In (b), the signs at 2 + 2.93h, 2 + 2.94h give the first root, and the signs −, +, − at
2 + 8h = 2 + x, a(x), 3 − δ_C the other two. In (a), P_1(2) = 0 ([[prop:np-10-12]] (iii)), and the signs −, +, − at
2 + 3h = 2 + x, a(x), 3 − δ_C give two more roots; so the root 2 is simple. ∎

#### Degrees with κ ≥ 18000 {#sec:s14-pa-large}

**Lemma {#lem:s14-sextic-large}** (Location of the roots.) Let l ≥ 134, so that x ≥ 0.018, and let x ≤ 70. Each
statement uses the row of [[sec:tab-a-pieces]] whose interval [x_a, x_b] contains x.

(a) P_l has exactly one root ι_B with |ι_B − (2 + x)| ≤ ϱ; it is real, and |ι_B − 2 − x + hc(x)| ≤ e_B.

(b) If x ≤ 0.03, the other two roots of P_l in |ι| < 1000 lie in |ι − a(x)| < 0.45.

(c) If x ≥ 0.03, P_l has exactly one root ι_P with |ι_P − ζ| ≤ ϱ, its conjugate is the only root
with |ι − ζ̄| ≤ ϱ, and

    |ι_P − ζ| ≤ Ξ_ζ/(1 − L_Ξ),     |Re ι_P − a(x) + hΠ(x)/2| ≤ e_P,

with Ξ_ζ, L_Ξ and e_P from the row. The roots ι_B, ι_P and ῑ_P are the three roots of P_l in |ι| < 1000.

*Proof.* (a) U = (ι − (2 + x))V_B with V_B := −𝒬, so [[lem:s14-fixed-point]] applies with p = 2 + x, V = −𝒬 and
Ξ_B = hW/𝒬. On the disc, |𝒬| ≥ 2(d_* − ϱ)² ≥ 𝒬_min with d_* the distance bound of the row (from
[[lem:s14-sextic-split]] (iv) in the first row and from |2 + x − ζ| = (1683x/128)^(1/2) ≥ (1683x_a/128)^(1/2) in the
others), and |∂_ι𝒬| = |4(ι − 2 − x) + x − 2| ≤ 4ϱ + max(2, x_b − 2) ≤ 𝒬′_max. With the majorant bounds M₀, M₁ of
the row, |Ξ_B| ≤ hM₀/𝒬_min ≤ ϱ and |Ξ_B′| ≤ L_Ξ < 1. As Ξ_B(2 + x) = hW(2 + x, x)/𝒬(2 + x, x) = −hc(x) by
[[lem:s14-sextic-split]] (ii), the lemma gives the root, real, with |ι_B − 2 − x + hc(x)| ≤ L_Ξhc(x)/(1 − L_Ξ) ≤ e_B.

(b) For 0.018 ≤ x ≤ 0.03, |Δ_𝒬(x)| ≤ max(Δ_𝒬(0.018), −Δ_𝒬(0.03)) < 2.4304, so the roots of 𝒬 lie within 0.3898 of a.
On |ι − a| = 0.45 they are at distance at least 0.0602 from ι, and |2 + x − ι| ≥ (1/2 − x/4) − 0.45 ≥ 0.0425,
so |U| ≥ 0.0425·2·0.0602² > 3.08·10⁻⁴, while |hW| ≤ h(M̄_a(0.45, 0.03) + hN̄(2.98, 0.03)) < 10⁻⁶·94. By Rouché's theorem
P_l has two zeros in |ι − a| < 0.45, as U has (2 + x lies outside, |2 + x − a| = 1/2 − x/4 > 0.49).

(c) U = (ι − ζ)V with V(ι) := 2(2 + x − ι)(ι − ζ̄). On |ι − ζ| ≤ ϱ, |V| ≥ 2(d⁻ − ϱ)(2b⁻ − ϱ) ≥ V_min
and |V′| = |2(2 + x − ι) − 2(ι − ζ̄)| ≤ 2(d⁺ + ϱ) + 2(2b⁺ + ϱ) ≤ V′_max, with the bounds d^±, b^±, r⁺ of the row from
[[lem:s14-sextic-split]] (iii). With M₀, M₁ of the row, |Ξ| ≤ hM₀/V_min ≤ ϱ and |Ξ′| ≤ L_Ξ < 1, and |Ξ(ζ)| =
h|W(ζ)|/|V(ζ)| ≤ hM_ζ/(4d⁻b⁻) ≤ Ξ_ζ, as |V(ζ)| = 2|2 + x − ζ|·2b. [[lem:s14-fixed-point]] gives ι_P and the first
bound. Since V(ζ) = ∂_ιU(ζ), [[eq:s14-pa-re]] gives Re Ξ(ζ) = −hΠ(x)/2,
and |Re(ι_P − ζ − Ξ(ζ))| ≤ L_Ξ|Ξ(ζ)|/(1 − L_Ξ) ≤ e_P. The conjugate statement follows from the real coefficients.
Finally, with ϱ_B and ϱ_P the radii of the two tables, ϱ_P < b⁻ and ϱ_B + ϱ_P < d⁻ for every pair of rows,
so the discs about 2 + x, ζ and ζ̄, resp. the disc of (b) and the disc about 2 + x (as 0.45 + 0.001 < 0.49), are
disjoint and lie in |ι| < 1000; by [[lem:s14-sextic-count]] they hold all three roots there. ∎

**Lemma {#lem:s14-crossings}** (The crossings of the integers.) Let l ≥ 1 with 0.5 ≤ x ≤ 70, and let 3 ≤ n ≤ 51 be an
integer. With K_n and K′_n as in [[sec:tab-a-crossings]]:

(a) if |ι_B − n| ≤ δ_C, then |κ − K_n| < 3.1 when n ≤ 17 and |κ − K_n| < 33 when n ≥ 18;

(b) if |Re ι_P − n| ≤ δ_C, then |κ − K′_n| < 27 when n ≤ 28 and |κ − K′_n| < 103 when n ≥ 29.

*Proof.* (a) By [[lem:s14-sextic-large]] (a), ι_B = 2 + x − hc(x) + ξ_B with |ξ_B| ≤ e_B ≤ 29h. If |ι_B − n| ≤ δ_C,
then |x − (n − 2) − hc(x)| ≤ δ_C + e_B; dividing by h,

    |κ − (n − 2)/h − c(x)| ≤ (δ_C + e_B)/h,     |x − (n − 2)| ≤ hc(x) + δ_C + e_B.

As c ≤ 5155, |x − (n − 2)| < 0.006; so n ≤ 17 gives x < 15.01, where e_B ≤ 0.1h, c ≤ 321 and |x − (n − 2)| ≤ 325h,
and n ≥ 18 gives x ≤ 49.01, where e_B ≤ 29h, c ≤ 2684 and |x − (n − 2)| ≤ 2716h. Since K_n = (n − 2)/h + c⁰(n − 2),

    |κ − K_n| ≤ (δ_C + e_B)/h + |c(x) − c⁰(x)| + |c⁰(x) − c⁰(n − 2)|,

and c⁰′(y) = 2y + 5866/1683 is at most 35.5 on [0, 16] and 103.5 on [0, 50]. By [[lem:s14-sextic-split]] (ii) this is
at most 2.94 + 0.1 + 0.011 + 35.5·325·10⁻⁶ < 3.1 for n ≤ 17, and 2.94 + 29 + 0.43 + 103.5·2716·10⁻⁶ < 33 for n ≥ 18.

(b) By [[lem:s14-sextic-large]] (c), Re ι_P = a(x) − hΠ(x)/2 + ξ_P with |ξ_P| ≤ e_P. Put x_n := (4n − 10)/3, so that
a(x) − n = 3(x − x_n)/4. If |Re ι_P − n| ≤ δ_C, then |x − x_n − 2hΠ(x)/3| ≤ 4(δ_C + e_P)/3, so

    |κ − x_n/h − 2Π(x)/3| ≤ 4(δ_C + e_P)/(3h),     |x − x_n| ≤ 2h|Π(x)|/3 + 4(δ_C + e_P)/3,

and, as K′_n = x_n/h + 2Π⁰(x_n)/3,

    |κ − K′_n| ≤ 4(δ_C + e_P)/(3h) + (2/3)(|Π(x) − Π⁰(x)| + |Π⁰(x) − Π⁰(x_n)|).

If n ≤ 28 then x ≤ 35 (as |x − x_n| < 0.002 and x₂₈ = 34), so e_P ≤ 17h, |Π| ≤ 619, |x − x_n| ≤ 440h, and by
[[lem:s14-sextic-split]] (v) the right side is at most (4/3)(19.94) + (2/3)(0.57 + 49.2·440·10⁻⁶) < 27. If n ≥ 29
then x ≥ 35, e_P ≤ 72h, |Π| ≤ 1995, |x − x_n| ≤ 1430h, and the right side is at most
(4/3)(74.94) + (2/3)(4.17 + 108.4·1430·10⁻⁶) < 103. ∎

#### The distance from the integers, and ε_ind at γ_C = 10⁶ {#sec:s14-pa-distance}

**Proposition {#prop:s14-damping-distance}** (The roots of the constraint damping polynomials at γ_C = 10⁶.) Let
h = 10⁻⁶, and let ι be a root of P_l (l ≥ 1), of P_0 or of p_(v) (l ≥ 1) with |ι − 1| ≤ 50 and ι ∉ ℤ. Then

    dist(Re ι, ℤ) > 2.94·10⁻⁶,

except for the root of P_2 near 2, which satisfies 2.93·10⁻⁶ < ι − 2 < 2.94·10⁻⁶. In particular every such root has
dist(Re ι, ℤ) > 2.93·10⁻⁶ > 2.9·10⁻⁶, the least distance occurring at scalar type l = 2. The only roots of P_l
(l ≥ 1) and of P_0 that are integers and satisfy |ι − 1| ≤ 50 are ι = 2 at l = 0 and at l = 1.

*Proof.* *Vector type.* By [[lem:s14-vector-distance]], the smaller root of p_(v) has |ι − 1| > 50, and a non-integer
larger root ι_v ≤ 51 has distance at least 2.9997·10⁻⁶ > δ_C from ℤ.

*Scalar type 0.* P_0 = −(ι − 2)C; the roots of C other than ι₁ have real part below −100 (proof of
[[prop:np-10-54]]), and ι₁ ∈ (2 + δ_C, 5/2) by [[lem:s14-scalar-zero]].

*Scalar type l ≥ 1, κ ≤ 18000.* By [[lem:s14-sextic-count]] (a) three roots have |ι| > 1000, and by
[[lem:s14-sextic-small]] the other three lie in (2, 3) at distance more than δ_C from 2 and from 3, except ι = 2 at
l = 1 and the root of P_2 in (2 + 2.93h, 2 + 2.94h).

*Scalar type l ≥ 1, 0.018 ≤ x ≤ 70.* Three roots have |ι| > 1000; the others are those of
[[lem:s14-sextic-large]]. For x ≤ 0.5, ι_B lies between 2 + x − hc(x) − e_B > 2.0179 and 2 + x ≤ 2.5; for
x ≤ 0.03 the other two have real parts in (a − 0.45, a + 0.45) ⊂ (2.06, 2.98); and
for 0.03 ≤ x ≤ 0.5, |ι_P − ζ| ≤ 0.0023, so Re ι_P ∈ (2.52, 2.88). For 0.5 ≤ x ≤ 70, ι_B > 2.49 and Re ι_P > 2.87.
If one of them lies in |ι − 1| ≤ 50, its real part is at most 51, so an integer n with |Re ι − n| ≤ δ_C satisfies
3 ≤ n ≤ 51, and for such an n [[lem:s14-crossings]] gives |κ − K_n| < 3.1, resp. 33, or |κ − K′_n| < 27, resp. 103. By
[[sec:tab-a-crossings]], every value l(l + 2) differs from K_n by more than 14.39 for n ≤ 17 and by more than 321.67
for n ≥ 18, and from K′_n by more than 141.07 for n ≤ 28 and by more than 392.12 for n ≥ 29. So no such n exists,
and the real part is more than δ_C from every integer.

*Scalar type l ≥ 1, x ≥ 70.* No root has |ι − 1| ≤ 50, by [[lem:s14-sextic-count]] (b).

The cases show that a root within δ_C of an integer, with |ι − 1| ≤ 50, is ι = 2 at l = 0 or l = 1 or the root of
P_2 near 2. ∎

**Corollary {#cor:s14-eps-ind-point}** (ε_ind at γ_C = 10⁶.) ε_ind(10⁻⁶) = δ_50, where the infimum of [[prop:np-10-52]]
(iii) is taken over all the lists ℛ^sc_l (l ≥ 0), ℛ^v_l (l ≥ 1) and ℛ^t_l (l ≥ 2), the scalar types 0 and 1 included. It
is attained by the entry −49 − δ_50 of ℛ^sc_50, and 1.941370568463·10⁻⁸ < δ_50 < 1.941370568464·10⁻⁸. Every entry of
these lists at h = 10⁻⁶ that comes from a root of P_l, of C or of p_(v), is not an integer and has modulus at most 50
has real part at distance more than 2.93·10⁻⁶ from ℤ.

*Proof.* The entries that do not depend on h are the integers −l, l + 2, 2 − l, l + 4, 1 − l and l + 3, the four
roots of Q_l(ι − 1) for each l ≥ 1 (at l = 1 these are 2 − ι^Υ_(s1,j) and 1 + ι^Υ_(s1,j), j = 2, 3), and at scalar
type 0 the numbers 2 − ι^Υ_(s0,2) and 1 + ι^Υ_(s0,2). By [[prop:np-10-52]] (iii) and its proof, the least distance
from ℤ of such an entry that is not an integer and has |ι| ≤ 50 is δ_50, attained by 1 − l − d₂ at l = 50, which is
−49 − δ_50. At the scalar types 0 and 1 these distances are ι^Υ_(s0,2) − 2 = z/(3/2 + (9/4 + z)^(1/2)) >
z/(3 + z/3) > 1.33·10⁻⁶, and, at u = 2, d₂ = z(1 + θ₂)/12 > 3.3·10⁻⁷ and d₁ = 3z(1 + θ₁)/20 > 5.9·10⁻⁷ by
[[eq:s14-theta]]; all exceed δ_50. The remaining entries are ι − 1 for the roots ι of P_l and of p_(v), l ≥ 1, and of
C at scalar type 0, those that [[ch:s15]] removes left out. The roots of C are roots of P_0 = −(ι − 2)C, so
dist(Re(ι − 1), ℤ) = dist(Re ι, ℤ) > 2.93·10⁻⁶ > δ_50 by [[prop:s14-damping-distance]] whenever ι − 1 ∉ ℤ
and |ι − 1| ≤ 50. So the infimum is a minimum, equal to δ_50, and [[lem:s14-delta50]] gives its value. ∎

**Remark {#rem:s14-eps-ind-scope}** (The point h = 10⁻⁶ and the set 𝖧.) [[thm:iii-e-1-1]] and [[prop:vi-c-adm-exist]]
take h in 𝖧 = (0, h_*) ∖ 𝖹 ([[eq:iv4-0-1]]), and h_* = min(10⁻⁶, h_0, h_tf) ≤ 10⁻⁶; so h = 10⁻⁶ is not in 𝖧.
[[prop:s14-damping-distance]] and [[cor:s14-eps-ind-point]] are used by no step of the proof of [[thm:settling]]; the
first shows that (AP2) of [[def:vi-c-admissible]] holds at h = 10⁻⁶ ([[rem:ec-point-outside]]). For h ∈ 𝖧 the theorems
use only 0 < ε_ind(h) ≤ δ_50, which
[[prop:np-10-52]] (iii) gives for every such h. [[lem:s14-delta50]] and the sums of the gauge potential offsets of
[[prop:gap-sums]] concern numbers fixed by the gauge parameters (e_Υ, γ_Υ) alone, not by h, so they hold whatever h is.
What changes for h ∈ 𝖧 is the location of the roots of P_l, P_0 and p_(v): the arguments of this section use h = 10⁻⁶ in
every constant. For h ∈ 𝖧 this paper gives 0 < ε_ind(h) ≤ δ_50 and the bound ε_ind(h) < 40h/13 of [[lem:ec-lb-ind]],
which is the smaller for h ≤ 6.309·10⁻⁹; and for every h ∈ [4.76·10⁻¹¹, 10⁻⁶] outside a set of total length below
1.7·10⁻¹¹ it gives ε_ind(h) ≥ 1.4619·10⁻¹⁰, the value of ε_Υ in [[def:uc-choice]] ([[prop:tr-eps]],
[[prop:tr-measure]]); that set contains the values of h at which Re ι crosses an integer for a root ι of P_l or
p_(v) with |ι − 1| ≤ 50, near each of which ε_ind(h) is arbitrarily small ([[prop:tr-fail]]).
[[cor:s14-eps-ind-point]] shows that
the upper bound δ_50 is attained at the end h = 10⁻⁶ of the interval on which ε_ind is defined; no positive lower
bound for ε_ind holds on any subinterval of (0, 10⁻⁶] of length 2·10⁻⁹ with the countable set 𝖹 removed
([[prop:t49-vector]]), and the point h = 10⁻⁶ itself lies outside 𝖹 ([[thm:t49-point]]).

### The exceptional sets of the damping and gauge parameters {#sec:s14-exceptional}

The constants of [[eq:iv4-0-1]] leave out a countable set 𝖹 = 𝖹₁ ∪ 𝖹₂ ∪ 𝖹₃ of values of h, and [[prop:iii-f1-2-3]] (e)
leaves out a countable set Z_exc of values of the gauge parameter z = 4e_Υγ_Υ². Each is contained in a union of zero
sets of explicit polynomials. This section decides them at the damping point h = 10⁻⁶ of [[sec:s14-pa]], with
z = 4·10⁻⁶, and describes 𝖹 on the interval

    I := [h₁, 10⁻⁶],     h₁ := 5·10⁻¹¹.

Throughout, (v, e) = (1/2, 1/102400); P(ι; κ, h) is the determinant of [[sec:s14-every-h]], P_l = P(·; l(l + 2), h),
and C and p_(v) are the polynomials of [[prop:np-10-12]] at (v, e). For l ≥ 1 we write K := κ^(1/2), κ = l(l + 2),
and δ_l := l + 1 − K = 1/(l + 1 + K), so that 0 < δ_l ≤ 2 − √3 < 0.268.

**Remark {#rem:t49-sets}** (The four sets.) Each set below is contained in a union, over the types and degrees, of
the zero sets of finitely many polynomials, none of which vanishes identically; 𝖹₁ and 𝖹₂ are such unions.

(a) 𝖹₁ ([[lem:iv4-1-3]] (b)) is the union of the zero sets in (0, 10⁻⁶] of the following polynomials in h: the
discriminants in ι of P_l (l ≥ 1), of C and of p_(v) (l ≥ 1), and C(2); the values P_l(y) for
y ∈ {1 − l, 3 − l, l + 3, l + 5} ∖ {2} (l ≥ 1), C(y) for y ∈ {1, 3, 5}, and p_(v)(y) for y ∈ {1 − l, 2 − l, l + 3, l + 4}
(l ≥ 2); and, for each integer k ∈ [3, 51], the resultants Res(A_k, B_k) of the proof of [[lem:iv4-1-3]] (b), for P_l
(l ≥ 1) and for C, which vanish exactly when two roots, counted with multiplicity, have sum 2k. The set is left out
because [[ch:s15]] uses the clauses (C2)–(C4) of [[sec:iii-f1-1]]. The polynomials of the first group vanish exactly
where a root is multiple, so where (C2) fails; those of the second exactly where (C3) fails; and outside the zero set
of the third no root whose real part is an integer in [3, 51] is non-real, which is (C4). So 𝖹₁ contains the set 𝖹₁′
of the h at which (C2), (C3) or (C4) fails, and a point of 𝖹₁ ∖ 𝖹₁′ is one at which two distinct roots of some P_l,
or of C, that are not complex conjugates of each other, have sum 2k for an integer k ∈ [3, 51].

(b) 𝖹₂ ([[prop:np-10-52]] (ii)), at z = 4·10⁻⁶, is the union over l ≥ 2 of the zero sets in (0, 10⁻⁶] of P_l(y) for
the eight numbers y ∈ {1 − l, 3 − l, l + 3, l + 5, l + 4 + d₁, 1 − l − d₁, l + 3 + d₂, 2 − l − d₂}, d₁ and d₂ those of
[[prop:np-10-52]] (i), and of p_(v)(y) for y ∈ {1 − l, 2 − l, l + 3, l + 4}. A root of P_l at such a y makes the entry
ι − 1 of ℛ^sc_l equal to an entry that does not depend on h (one of −l, 2 − l, l + 2, l + 4 or a root of Q_l(ι − 1)),
and likewise for ℛ^v_l; the set is left out so that the entries of each list are distinct, that is, so that the
indicial roots of the linearised gauge-fixed Einstein operator at the types l ≥ 2 are simple.

(c) 𝖹₃ ([[prop:np-10-52]] (iii)) is the set of the h ∈ (0, 10⁻⁶] at which, for some l ≥ 0 and some integer
k ∈ [−49, 51], P_l (C if l = 0) has a non-real root of real part k. Outside 𝖹₃ no non-integer entry ι of the lists
with |ι| ≤ 50 has integer real part, so ε_ind(h) > 0: the set is left out for the condition [Hin26, (8.13)].

(d) Z_exc ([[prop:iii-f1-2-3]] (e)) is defined at an h at which (C2) and
(C3) hold. It is the set of the z ∈ (0, ½] at which, for some l ≥ 0, a real root of C (l = 0) or of P_l (l ≥ 1) equals
ι^Υ + 2 or 3 − ι^Υ, for a root ι^Υ = ι^Υ_(s0,2) (l = 0), or ι^Υ = ι^Υ_(sl,l+1) or ι^Υ_(sl,l+2) (l ≥ 1), of the gauge
potential operator ([[lem:iii-d-4-1]]). There an entry ι − 1 that comes from □^C equals an entry 1 + ι^Υ or 2 − ι^Υ of
the same type and degree, and the indicial root of L_b^(0) is double; the set is left out so that every indicial root of
L_b^(0) is simple. With d₁ := ι^Υ_(sl,l+2) − l − 2 and d₂ := ι^Υ_(sl,l+1) − l − 1, which lie in (0, ¼) for every
z ∈ (0, ½] by [[eq:iii-d-4-2]], the four numbers ι^Υ + 2 and 3 − ι^Υ at l ≥ 1 are l + 4 + d₁, l + 3 + d₂, 1 − l − d₁
and 2 − l − d₂. So Z_exc at a fixed h and the non-integer part of 𝖹₂ at a fixed z are the two sections of one set of
coincidences in (h, z), taken in (b) for l ≥ 2 and in (d) for l ≥ 0.

#### Values near ±κ^(1/2) {#sec:s14-exc-shifted}

The coefficients of P(ι; κ, h) = Σ_(j=0)^6 a_j(κ, h)ι^j, read off from [[eq:s14-nl]] at (v, e) = (1/2, 1/102400), are

    a₆ = −h³,     a₅ = 6h³ − (409599/102400)h²,
    a₄ = (3κ − 10)h³ + (2559997/102400)h² − (255997/51200)h,
    a₃ = −12κh³ + ((409599/51200)κ − 5017599/102400)h² + (3379181/102400)h − 40959/20480,
    a₂ = (−3κ² + 12κ + 11)h³ − ((819199/25600)κ − 2150403/102400)h² + ((511991/102400)κ − 3635197/51200)h
         + 71679/5120,
    a₁ = (6κ² − 6)h³ − ((409599/102400)κ² − (3379199/102400)κ − 1075199/51200)h²
         − ((430077/20480)κ − 4608021/102400)h − (3/102400)κ − 655359/20480,
    a₀ = (κ³ − 2κ² − 3κ)h³ + ((716799/102400)κ² + (102399/102400)κ − 6)h²
         + ((3/102400)κ² + (2252797/102400)κ + 102399/10240)h + (3/51200)κ + 245763/10240.          {#eq:t49-coeffs}

At h = 10⁻⁶ these are π_j(κ)/(64·10¹⁸), with π_j of [[sec:tab-a-sextic]]. Expanding [[eq:s14-nl]] with ι = ±K + s
and κ = K² gives, for both choices of the sign together, the identity in (K, s, h, e)

    P(±K + s; K², h) = ±K³q₃(s) + K²q₂(s) ± Kq₁(s) + q₀(s),                                          {#eq:t49-shift}

    q₃ = −2(1 + hs)(1 − 2h + 2hs)(1 − e − 4h + 2hs),
    q₂ = 14 − 6s + e(12s − 14) − h(25s² − 78s + 49) + 3eh(9s² − 14s + 1) − 2h²(16s³ − 59s² + 57s − 11)
         + 2eh²(4s³ − 7s² + s + 1) − 4h³(3s⁴ − 12s³ + 12s² − 2),
    q₁ = −2(s − 2)(3s − 8) + 5e(3s² − 8s + 1) − h(20s³ − 99s² + 142s − 45) + 3eh(s − 1)(8s² − 11s − 7)
         − h²(20s⁴ − 100s³ + 147s² − 42s − 21) + eh²(s − 1)(5s³ − 7s² − 4s + 2) − 2h³(s − 1)(3s⁴ − 12s³ + 8s² + 8s − 3),
    q₀ = −2(s − 3)(s − 2)² + 5e(s − 3)(s − 2)(s + 1) − h(s − 2)(5s³ − 23s² + 25s + 5)
         + eh(s − 2)(s + 1)(2s − 1)(3s − 5) − h²(s − 2)(4s⁴ − 17s³ + 15s² + 9s − 3) + eh²s(s − 2)(s − 1)²(s + 1)
         − h³s(s − 3)(s − 2)(s − 1)²(s + 1).

**Lemma {#lem:t49-shifted}** (No root near ±κ^(1/2).) Let 0 < h ≤ 10⁻⁶, l ≥ 1 and K = (l(l + 2))^(1/2).

(a) P_l(y) ≠ 0 for every real y with 2 ≤ y − K ≤ 43/10.

(b) P_l(y) ≠ 0 for every real y ≤ 1 with 7/5 ≤ y + K ≤ 4.

*Proof.* *Bounds on [7/5, 43/10].* Let 7/5 ≤ s ≤ 43/10. The three factors of q₃ are at least 1, 1 and
1 − e − 6h/5, so |q₃(s)| ≥ 2(1 − e − 6h/5) > 1.9999. In q₂, q₁ and q₀ the terms free of e and h have moduli at most
11.8, 22.54 and 13.754 on the interval, at s = 43/10 in each case: |14 − 6s| ≤ 11.8; 2(s − 2)(3s − 8) is 4.56 at
s = 7/5, −2/3 at its vertex 7/3 and 22.54 at 43/10; and 2|s − 3|(s − 2)² is 1.152 at 7/5, at most 8/27 on [2, 3] and
13.754 at 43/10. The terms of order e have the factors 12s − 14, 5(3s² − 8s + 1) and 5(s − 3)(s − 2)(s + 1), of
moduli at most 37.6, 110.4 and 79.3; those of order h have the factors 25s² − 78s + 49, 20s³ − 99s² + 142s − 45 and
(s − 2)(5s³ − 23s² + 25s + 5), of moduli at most 175.9, 325.3 and 195; every other term carries eh, h² or h³, each
at most 10⁻¹¹, times a polynomial factor of modulus at most 2000 on the interval. With e < 0.98·10⁻⁵ and h ≤ 10⁻⁶,

    |q₂(s)| < 11.8006,     |q₁(s)| < 22.5415,     |q₀(s)| < 13.755.

*Large degrees.* For K ≥ 7.6, [[eq:t49-shift]] gives |P(±K + s; K², h)| ≥ g(K), where
g(K) := 1.9999K³ − 11.8006K² − 22.5415K − 13.755; here g(7.6) > 11 and g′(K) = 5.9997K² − 23.6012K − 22.5415 > 0
for K ≥ 7.6. So P_l(K + s) ≠ 0 and P_l(−K + s) ≠ 0 for 7/5 ≤ s ≤ 43/10 when K ≥ 7.6, that is, when l ≥ 7. This
gives (a) and (b) for l ≥ 7, with s = y − K and s = y + K.

*(b) for every l.* If y ≥ −100, then y ∈ [−100, 1] ⊂ [−100, 19/10], and P_l(y) ≠ 0 by [[prop:np-10-54]] (i). If
y < −100, then K ≥ y + K − y > 7/5 + 100, so l ≥ 7 and the previous step applies.

*(a) for 1 ≤ l ≤ 6.* Then κ ≤ 48 and y ∈ [√3 + 2, √48 + 43/10] ⊂ [37/10, 113/10]. By [[eq:s14-q5]] at v = 1/2,
P(y; κ, 0) = 4(y − 2)Q_5(y) with 4Q_5(y) = −2(y − 2)(y − 3) + 5e(y − 3)(y + 1) − 3eκ. For y ≥ 37/10,
(y + 1)/(y − 2) ≤ 47/17, so 5e(y − 3)(y + 1) ≤ 14e(y − 2)(y − 3) and |P(y; κ, 0)| ≥ (2 − 14e)(y − 2)²(y − 3) ≥
1.9997·(17/10)²·(7/10) > 4.04. Each coefficient a_j(κ, h) − a_j(κ, 0) of [[eq:t49-coeffs]] is a sum of terms carrying
a positive power of h; bounding each term by its modulus at κ = 48, h = 10⁻⁶ and multiplying by (113/10)^j, the sum
over j is below 0.19. So |P(y; κ, h) − P(y; κ, 0)| < 0.19 and |P_l(y)| > 3.8. ∎

**Theorem {#thm:t49-uniform}** (The listed points are never roots.) Let 0 < h ≤ 10⁻⁶ and 0 < z ≤ ½.

(i) For every l ≥ 1, P_l has no root in {1 − l, 3 − l, l + 3, l + 5} ∖ {2}; C has no root in {1, 3, 5}; and for every
l ≥ 2, p_(v) has no root in {1 − l, 2 − l, l + 3, l + 4}. So (C3) holds at every h ∈ (0, 10⁻⁶], and none of the
polynomials of the second group of [[rem:t49-sets]] (a) vanishes on (0, 10⁻⁶].

(ii) For every l ≥ 1 and j ∈ {1, 2}, neither ι^Υ_(sl,l+j) + 2 nor 3 − ι^Υ_(sl,l+j) is a root of P_l; and neither
ι^Υ_(s0,2) + 2 nor 3 − ι^Υ_(s0,2) is a root of C.

(iii) 𝖹₂ is empty, whatever z ∈ (0, ½] is used to define it, in particular at z = 4·10⁻⁶; and at every h ∈ (0, 10⁻⁶] at
which (C2) holds, Z_exc is empty: then, for every z ∈ (0, ½], every indicial root of L_b^(0) is simple.

*Proof.* (i) and (ii) for P_l. The numbers to be excluded are, at l ≥ 1, the integers l + 3 and l + 5 and the numbers
l + 3 + d₂ and l + 4 + d₁ above l + 1, and the integers 1 − l and 3 − l (for l ≥ 2) and the numbers 2 − l − d₂ and
1 − l − d₁ below 1, with d₁, d₂ ∈ (0, ¼) as in [[rem:t49-sets]] (d). For the first four, y − (l + 1) lies in
{2, 4} ∪ (2, 9/4) ∪ (3, 13/4), so y − K = y − (l + 1) + δ_l lies in [2, 4 + 0.268] ⊂ [2, 43/10], and
[[lem:t49-shifted]] (a) applies. For the last four, y ≤ 1 and y + (l + 1) lies in {2, 4} ∪ (11/4, 3) ∪ (7/4, 2), so
y + K = y + (l + 1) − δ_l lies in [7/4 − 0.268, 4] ⊂ [7/5, 4], and [[lem:t49-shifted]] (b) applies. (At l = 1 the
integer 3 − l = 2 is not excluded.)

*C.* With C = C₀ + C_h as in the proof of [[prop:np-10-54]],

    C(1) = 2 + 10e + 6h + 2eh + 4h²,     C(3) = −2 + 20e − 6h + 12eh,     C(4) = −4 + 25e − 21h + 20eh − 20h²,
    C(5) = −6 + 30e − 42h + 30eh − 60h²,

so C(1) > 0 > C(3), C(4), C(5). By that proof C > 0 on [−100, 2], and C has exactly one root ι₁ in (2, ∞), with C < 0
on (ι₁, ∞); as C(4) < 0, ι₁ < 4 and C < 0 on [4, ∞). By [[eq:iii-d-4-2]], ι^Υ_(s0,2) ∈ (2, 2 + z/3] ⊂ (2, 13/6], so
ι^Υ_(s0,2) + 2 ∈ (4, 25/6], where C < 0, and 3 − ι^Υ_(s0,2) ∈ [5/6, 1), where C > 0.

*p_(v).* At v = 1/2, p_(v)(y) = h(κ + 2y − y²) + 3 − y. At the four numbers y = l + 3, l + 4, 1 − l and 2 − l the
bracket κ + 2y − y² is −2l − 3, −4l − 8, 2l + 1 and 4l, so p_(v)(y) is −(2l + 3)h − l, −(4l + 8)h − l − 1,
(2l + 1)h + l + 2 and 4lh + l + 1, none zero.

(iii) The polynomials whose zero sets make up 𝖹₂ ([[rem:t49-sets]] (b)) are P_l(y) at the eight numbers listed there,
which are those of (i) and (ii) at l ≥ 2 (with the d₁, d₂ of the z used), and p_(v)(y) at the four numbers of (i). By
(i) and (ii) none vanishes at any h ∈ (0, 10⁻⁶], so 𝖹₂ = ∅. If (C2) holds at h, so does (C3), by (i); and the
coincidences that define Z_exc ([[rem:t49-sets]] (d)) are those excluded by (ii), for every z ∈ (0, ½]. So Z_exc = ∅,
and by [[prop:iii-f1-2-3]] (e), whose hypothesis (C1) holds at every h ∈ (0, 10⁻⁶] by [[prop:np-10-54]], every indicial
root of L_b^(0) is simple for every z ∈ (0, ½]. ∎

#### The damping point γ_C = 10⁶ {#sec:s14-exc-point}

Let 𝒫(ι; κ) := Σ_(j=0)^6 π_j(κ)ι^j = 64·10¹⁸P(ι; κ, 10⁻⁶), with the integer coefficients π_j of [[sec:tab-a-sextic]].
Its discriminant in ι is (−1)^15 times the resultant of 𝒫 and ∂_ι𝒫 divided by the leading coefficient π₆, a
polynomial in κ with integer coefficients; expanding it,

    disc_ι 𝒫(·; κ) = 144·𝔇(κ),                                                                      {#eq:t49-disc}

with 𝔇 the polynomial of degree 9 of [[sec:tab-t49-disc]]. For an integer k write 𝒫(k + w; κ) = Σ_(j=0)^6 φ_j(k, κ)w^j
and put 𝒜_k(s) := φ₀ − φ₂s + φ₄s² − φ₆s³ and ℬ_k(s) := φ₁ − φ₃s + φ₅s², so that 𝒫(k + iy; κ) = 𝒜_k(y²) + iyℬ_k(y²);
these are A_k and B_k of [[lem:iv4-1-3]] (b) at h = 10⁻⁶, up to the factor 64·10¹⁸. Expanding the resultant in s,

    Res_s(𝒜_k, ℬ_k) = 4·𝔖(k, κ),                                                                           {#eq:t49-res}

with 𝔖 the polynomial with integer coefficients, of degree 15 in k and 3 in κ, of [[sec:tab-t49-res]]. The leading
coefficients of 𝒜_k and ℬ_k in s are 64 and φ₅ = −384k − 255998991, both non-zero.

**Proposition {#prop:t49-simple}** (Simple roots at γ_C = 10⁶.) At h = 10⁻⁶, for every l ≥ 1 the six roots of P_l are
simple; the three roots of C and the two roots of p_(v) are simple; and ι = 2 is not a root of C. In particular (C2)
holds at h = 10⁻⁶, and none of the polynomials of the first group of [[rem:t49-sets]] (a) vanishes at h = 10⁻⁶.

*Proof.* *P_l.* The leading coefficient of 𝒫(·; κ) is π₆ = −64 ≠ 0, so 𝒫(·; κ) has a multiple root exactly when its
discriminant vanishes, that is, by [[eq:t49-disc]], when 𝔇(κ) = 0. The coefficients of 𝔇, from κ⁹ to κ⁰, have the
signs +, −, +, +, +, +, −, +, +, + ([[sec:tab-t49-disc]]): four changes of sign, so by Descartes' rule 𝔇 has at most
four positive roots. By the second table of [[sec:tab-t49-disc]], 𝔇(n) and 𝔇(n + 1) have opposite signs for each of
the four integers n = 18656, 214373184, 2354423533873 and 24600231683951, so 𝔇 has a root in each of the four open
intervals (n, n + 1). These are its four positive roots, and none is an integer. So 𝔇(l(l + 2)) ≠ 0, and P_l has
simple roots, for every l ≥ 1.

*C and p_(v).* At h = 10⁻⁶, C(−3·10⁶) > 5.9·10⁶, C(−1.5·10⁶) < −3.7·10⁵, C(−10⁶) < −39 and C(−100) > 0, and
C(2 + δ_C) > 0 > C(5/2) ([[lem:s14-scalar-zero]]); so C has a root in each of (−3·10⁶, −1.5·10⁶), (−10⁶, −100) and
(2 + δ_C, 5/2), three distinct real roots. C(2) > 0 by the proof of [[prop:np-10-54]]. The roots of p_(v) are real and
of opposite signs ([[lem:s14-small-h]] (c)). ∎

**Proposition {#prop:t49-pairs}** (No symmetric pairs at γ_C = 10⁶.) At h = 10⁻⁶, for every l ≥ 1 and every integer
k ∈ [3, 51], no two roots of P_l, counted with multiplicity, have sum 2k; and no two roots of C have sum 2k. In
particular every root of P_l whose real part is an integer in [3, 51] is real, and so, the roots of C and of p_(v)
being real (proof of [[prop:t49-simple]]), (C4) holds at h = 10⁻⁶; and none of the resultants of the third group of
[[rem:t49-sets]] (a) vanishes at h = 10⁻⁶.

*Proof.* As in the proof of [[lem:iv4-1-3]] (b), 𝒫(·; κ) has two roots with sum 2k exactly when 𝒜_k and ℬ_k have a
common root, that is, as their leading coefficients do not vanish, when Res_s(𝒜_k, ℬ_k) = 0, which by [[eq:t49-res]]
is 𝔖(k, κ) = 0. Fix k ∈ {3, …, 51}; 𝔖(k, ·) is a cubic with integer coefficients. For k = 3 its coefficients, from κ³
to κ⁰, have the signs −, −, +, +, one change, so it has exactly one positive root. For 4 ≤ k ≤ 51 its discriminant is
negative, so it has exactly one real root. By the table of [[sec:tab-t49-res]], 𝔖(k, l_k(l_k + 2)) > 0 and
𝔖(k, (l_k + 1)(l_k + 3)) < 0 for the integer l_k listed, so that root is positive and lies strictly between two
consecutive values of l(l + 2). Hence 𝔖(k, l(l + 2)) ≠ 0 for every l ≥ 1. If P_l had a non-real root of real part k,
that root and its conjugate would have sum 2k. For C, its roots at h = 10⁻⁶ are real and lie in
(−3·10⁶, −1.5·10⁶), (−10⁶, −100) and (2, 5/2) (proof of [[prop:t49-simple]]), so any two have sum below 5/2 − 100,
and they are distinct. ∎

**Theorem {#thm:t49-point}** (The damping point avoids the exceptional sets.) h = 10⁻⁶ lies in none of 𝖹₁, 𝖹₂ and
𝖹₃, and not in the set 𝖹₁′ of [[rem:t49-sets]] (a): (C1)–(C4) of [[sec:iii-f1-1]] hold at γ_C = 10⁶, for every b
near b₀. At h = 10⁻⁶ the set Z_exc is empty; so z = 4·10⁻⁶ ∉ Z_exc, and at the computational point of
[[def:ec-point]] every indicial root of L̂_b(0) is simple at each type and degree at which it occurs.

*Proof.* The indicial roots of □^C_b are those of the model, independent of b (proof of [[lem:iv4-1-3]]). (C1) holds at
every h ∈ (0, 10⁻⁶] ([[prop:np-10-54]]); (C2) at 10⁻⁶ by [[prop:t49-simple]], (C3) by [[thm:t49-uniform]] (i) and (C4)
by [[prop:t49-pairs]]. So h = 10⁻⁶ ∉ 𝖹₁′. The three groups of polynomials of [[rem:t49-sets]] (a) do not vanish at
10⁻⁶, by [[prop:t49-simple]], [[thm:t49-uniform]] (i) and [[prop:t49-pairs]], so 10⁻⁶ ∉ 𝖹₁. 𝖹₂ = ∅ by
[[thm:t49-uniform]] (iii). For 𝖹₃: by [[prop:np-10-54]] (i), (ii) no root of P_l or C has real part in [−100, 19/10],
and the only roots with real part in [−100, 2] are ι = 2 at l = 0 and l = 1, which are real; so no non-real root has
real part in [−49, 2]; P_l has no non-real root of real part k ∈ [3, 51] by [[prop:t49-pairs]]; and the
roots of C are real at 10⁻⁶. So 10⁻⁶ ∉ 𝖹₃. As (C2) holds at 10⁻⁶, Z_exc = ∅ there by [[thm:t49-uniform]] (iii), and
every indicial root of L_b^(0) is simple, for z = 4·10⁻⁶ in particular; the indicial roots of L̂_b(0) are those of
L_b^(0), its indicial family being that of the model ([[lem:iii-f-2-1]] (3)). ∎

**Corollary {#cor:t49-right}** (The roots of P_l beyond hκ = 70.) At h = 10⁻⁶, for every real κ ≥ κ₀ := 8365·8367 =
69989955, in particular for κ = l(l + 2) with l ≥ 8365, three roots of P(·; κ, 10⁻⁶) have real part greater than 51
and three have real part less than −5·10⁵. So no root of P_l with hκ > 70 has real part in [2, 51].

*Proof.* A root of real part 51 is either the real number 51, a root of 𝒫(51; ·), or a non-real root 51 + iy, which
with its conjugate gives two roots with sum 102, so 𝔖(51, κ) = 0 ([[eq:t49-res]]). From [[sec:tab-a-sextic]],

    𝒫(51; κ) = 64κ³ − 10733448686κ² + 673357544904696250κ − 14753258230942677244890000;

its derivative 192κ² − 21466897372κ + 673357544904696250 has negative discriminant
(21466897372² < 4·192·673357544904696250), so 𝒫(51; ·) increases and has exactly one real root, which lies in
(49002580, 49002581) as 𝒫(51; 49002580) < 0 < 𝒫(51; 49002581). The only real root of 𝔖(51, ·) lies in
(64657680, 64673763) ([[prop:t49-pairs]]). Both are below κ₀, so no root of P(·; κ, 10⁻⁶) has real part 51 for
κ ≥ κ₀. By [[lem:s14-half-plane-count]] with Ω = [κ₀, ∞) × {10⁻⁶} the number of roots with real part greater than 51
is the same for every κ ≥ κ₀. At κ = κ₀, x = hκ₀ = 69.989955 ∈ [35, 70], and [[lem:s14-sextic-large]] (a), (c) with
the last
rows of [[sec:tab-a-pieces]] give the real root ι_B ≥ 2 + x − h·5155 − 29h > 71 and the pair ι_P, ῑ_P with
Re ι_P ≥ (3x + 10)/4 − h(1990 + 4.17)/2 − 72h > 54.9, by the bound on the function Π of
[[lem:s14-sextic-split]] (v). So the number is 3, and the other three roots have real part less than −5·10⁵ by
[[prop:s14-scalar-every-h]], whose proof counts the roots for every real κ ≥ 3. ∎

#### The interval [5·10⁻¹¹, 10⁻⁶] {#sec:s14-exc-interval}

For l ≥ 1 put, with x = hκ,

    Δ_l(h) := x² − (24e/h − 20)x + 4 = h²κ² + 20hκ + 4 − 24eκ,                                      {#eq:t49-delta}

the discriminant Δ_𝒬(x) of [[lem:s14-sextic-split]] (iii) at ε₀ = e/h. It increases with h, and Δ_l(h) = c exactly
when h = ((96 + c + 24eκ)^(1/2) − 10)/κ.

**Proposition {#prop:t49-six}** (Six points of 𝖹₁ in I.) For 130 ≤ l ≤ 135 put κ = l(l + 2),
h⁻_l := ((96 − 3/500 + 24eκ)^(1/2) − 10)/κ and h⁺_l := ((96 + 1/1000 + 24eκ)^(1/2) − 10)/κ. Then

    (h⁻_l, h⁺_l) ⊂ (4.62·10⁻⁸, 6.67·10⁻⁸), (2.22·10⁻⁷, 2.43·10⁻⁷), (3.94·10⁻⁷, 4.15·10⁻⁷), (5.62·10⁻⁷, 5.83·10⁻⁷),
                    (7.27·10⁻⁷, 7.47·10⁻⁷), (8.88·10⁻⁷, 9.07·10⁻⁷)

for l = 130, …, 135 respectively, six disjoint intervals in I. For each such l there is h ∈ (h⁻_l, h⁺_l) at which
P_l has a double real root in 𝒥 := [21/10, 59/20], and for h ∈ (0, 10⁻⁶] outside (h⁻_l, h⁺_l) P_l has no multiple
root in 𝒥. In particular 𝖹₁ ∩ I and 𝖹₁′ ∩ I each contain at least six points, one in each interval.

*Proof.* *The parts.* [[lem:s14-sextic-split]] (i) holds with e = ε₀h for every ε₀ ([[sec:tab-a-split]]); take
ε₀ = e/h. Then P_l = U + hW, U = (2 + x − ι)𝒬, 𝒬 = 2(ι − a)² − Δ_l(h)/8 with a := (3x + 10)/4, x = hκ; indeed
𝒬 − 2(ι − a)² = (−x² + (24ε₀ − 20)x − 4)/8 and ε₀x = eκ. For 0 < h ≤ 10⁻⁶, 0 < x ≤ 0.018495 and
2.5 < a < 2.514. Writing R_j = ε₀R_jᵉ + R_j⁰ with R_jᵉ, R_j⁰ free of ε₀,

    hW = eR₁ᵉ + hR₁⁰ + ehR₂ᵉ + h²R₂⁰ + eh²R₃ᵉ + h³R₃⁰.

On 𝒥, with 0 ≤ x ≤ 0.0185: R₁ᵉ = 5(ι − 2)(ι − 3)(ι + 1) − x(9ι² − 15ι + 3) + x²(ι − 1), where
0 ≤ (ι − 2)(3 − ι)(ι + 1) < 0.88 and 0 < 9ι² − 15ι + 3 ≤ 37.1, so |R₁ᵉ| < 5.1;
R₁⁰ = (ι − 2)(−5ι³ + 23ι² − 25ι − 5) + x(8ι³ − 32ι² + 33ι + 1) − x²(3ι² − 6ι + 2), where the cubic in the first term
lies in [−6.96, −1.6] and the second in [3.2, 25.3], so |R₁⁰| < 7.1; the sums of the moduli of the terms at
ι = 59/20, x = 0.0185 give |R₂ᵉ| < 1070 and |R₂⁰| < 4310; the factors of R₃ᵉ = ι(ι − 2)(ι − 1)²(ι + 1) and of
R₃⁰ = (3 − ι)R₃ᵉ are positive on 𝒥, so |R₃ᵉ| ≤ (59/20)(19/20)(39/20)²(79/20) < 42.1 and |R₃⁰| < (9/10)·42.1 < 38.
Hence

    |hW| < 5.1e + 7.1h + 1070eh + 4310h² + 43eh² + 38h³ < 5.7·10⁻⁵     on 𝒥, for 0 < h ≤ 10⁻⁶.

*Signs.* For 130 ≤ l ≤ 135 and 0 < h ≤ 10⁻⁶, Δ_l(h) ≤ Δ₁₃₀(10⁻⁶) < 0.3217. So 𝒬(21/10, x) ≥ 2(2/5)² − 0.0403 > 0.279
and 𝒬(59/20, x) ≥ 2(0.436)² − 0.0403 > 0.339, whence U(21/10) ≤ −0.0815·0.279 < −0.022 and
U(59/20) ≤ −0.93·0.339 < −0.31: P_l(21/10) < 0 and P_l(59/20) < 0. Also P_l(2) > 0 ([[lem:s14-line-two]] (a)).

*The count.* Let N(h) be the number of roots of P_l in 𝒥, with multiplicity. By [[prop:s14-scalar-every-h]], P_l has
exactly three roots of real part greater than 2, and one of them is real and lies in (2, 21/10), as P_l(2) > 0 >
P_l(21/10); so N(h) ≤ 2. As P_l(21/10) and P_l(59/20) have the same sign, N(h) is even. If Δ_l(h) ≥ 1/1000, then
U(a) = (2 − x)Δ_l(h)/32 ≥ 6.1·10⁻⁵, so P_l(a) > 0, and P_l has a root in (21/10, a) and one in (a, 59/20): N(h) = 2,
both simple. If Δ_l(h) ≤ −3/500, then on 𝒥, U = (2 + x − ι)𝒬 ≤ −(1/10 − x)(−Δ_l(h)/8) < −6.1·10⁻⁵ < −|hW|, so P_l < 0
on 𝒥 and N(h) = 0. By [[eq:t49-delta]], Δ_l(h) ≤ −3/500 exactly for h ≤ h⁻_l and Δ_l(h) ≥ 1/1000 exactly for h ≥ h⁺_l;
so for h ∉ (h⁻_l, h⁺_l) there is no multiple root in 𝒥. The interval bounds follow from the formulas, with
24eκ = 3κ/12800, and Δ_l(h₁) < −0.0218, Δ_l(10⁻⁶) > 0.0354 give h₁ < h⁻_l < h⁺_l < 10⁻⁶.

*The double root.* Suppose that for no h ∈ [h⁻_l, h⁺_l] does P_l have a multiple root in 𝒥. Then for each such h the
roots in 𝒥 are simple, real (a non-real root has its conjugate as a root and is not in 𝒥) and interior to 𝒥. By the
implicit function theorem each persists, simple and real, for nearby h; and the roots in 𝒥 at nearby h are close to
roots in 𝒥 at h, as the roots depend continuously on h and none lies at an end of 𝒥. So N is locally constant on
[h⁻_l, h⁺_l], hence constant, against N(h⁻_l) = 0 and N(h⁺_l) = 2. So some h ∈ [h⁻_l, h⁺_l] gives a multiple root in
𝒥, and by the count it lies in the open interval and the root is real and double. At such h the discriminant of P_l
vanishes and (C2) fails, so h ∈ 𝖹₁ and h ∈ 𝖹₁′. ∎

**Proposition {#prop:t49-vector}** (The index distance near the integer crossings of the vector roots.) For integers
n ∈ [4, 50] and l ≥ 2 with κ := l(l + 2) > n² − 2n put

    h^v_(n,l) := (n − 3)/(κ − n² + 2n).

(a) At h = h^v_(n,l), n is the larger root of p_(v) at vector type l.

(b) If 0 < h ≤ 10⁻⁶ and δ := (κ − n² + 2n)|h − h^v_(n,l)| satisfies 0 < δ < 1, then ε_ind(h) ≤ δ.

(c) Every subinterval of (0, 10⁻⁶] of length 2·10⁻⁹ contains a point h^v_(4,l). Hence for every η > 0 every such
subinterval contains a non-empty open set on which ε_ind < η, and this set contains points h ∉ 𝖹, at which
0 < ε_ind(h) < η. In particular ε_ind has no positive lower bound on I ∖ 𝖹, nor on any subinterval of length 2·10⁻⁹
with 𝖹 removed. The largest point h^v_(n,l) below 10⁻⁶ with 4 ≤ n ≤ 50 is h^v_(35,5656) = 32/32000493 > 9.99984·10⁻⁷.

*Proof.* At v = 1/2, p_(v)(ι) = −hι² + (2h − 1)ι + hκ + 3, so p_(v)(n) = h(κ − n² + 2n) − (n − 3) =
(κ − n² + 2n)(h − h^v_(n,l)). (a) At h = h^v_(n,l), n > 0 is a root, and the roots have opposite signs
([[lem:s14-small-h]] (c)), so n is the larger. (b) For ι ∈ [3, 51], ∂_ιp_(v)(ι) = −1 − 2h(ι − 1) ∈ [−1.0001, −1].
As |p_(v)(n)| = δ < 1 and 3 < n − δ < n + δ < 51, the mean value theorem gives p_(v)(n − δ) ≥ p_(v)(n) + δ ≥ 0 ≥
p_(v)(n) − δ ≥ p_(v)(n + δ), so p_(v) has a root ι_v ∈ [n − δ, n + δ], positive, hence the larger root; and ι_v ≠ n as
p_(v)(n) ≠ 0. So ι_v − 1, an entry of ℛ^v_l ([[sec:s14-simple]]), is not an integer, |ι_v − 1| < 50, and
dist(Re(ι_v − 1), ℤ) ≤ |ι_v − n| ≤ δ; hence ε_ind(h) ≤ δ ([[prop:np-10-52]] (iii)). (c) h^v_(4,l) = 1/((l + 4)(l − 2)),
which lies in (0, 10⁻⁶) for l ≥ 1000, the largest of these values being 1/1001992 > 10⁻⁶ − 2·10⁻⁹. Consecutive ones
differ by (2l + 3)/((l + 4)(l − 2)(l + 5)(l − 1)), which decreases in l and is below 2·10⁻⁹ at l = 1000. So every
subinterval of (0, 10⁻⁶] of length 2·10⁻⁹ contains some h^v_(4,l); by (b), ε_ind < η on the set of its points h ≠
h^v_(4,l) with (κ − 8)|h − h^v_(4,l)| < min(η, 1), which contains an open interval, and ε_ind > 0 there by
[[prop:np-10-52]] (iii) off the countable set 𝖹₃. That open set is uncountable and 𝖹 is countable. For the last
claim, for each n the largest h^v_(n,l) below 10⁻⁶ comes from the least l with κ > (n − 3)·10⁶ + n² − 2n, and the
largest over 4 ≤ n ≤ 50 is at n = 35, l = 5656, κ = 32001648. ∎

**Remark {#rem:t49-scope}** (What this decides.) At the damping point the exclusions of [[eq:iv4-0-1]] and
[[prop:iii-f1-2-3]] (e) are met, although [[def:vi-c-admissible]] does not ask them: h = 10⁻⁶ ∉ 𝖹, (C1)–(C4) hold, and
Z_exc = ∅ at h = 10⁻⁶, so z = 4·10⁻⁶ ∉ Z_exc ([[thm:t49-point]]); every indicial root of L̂_b(0) at the computational
point is simple. The computational point is not in 𝖧, because 𝖧 ⊂ (0, h_*) and h_* ≤ 10⁻⁶, and whether it is admissible
is decided by the conditions that [[rem:ec-point-outside]] lists as open. Away from the point, 𝖹₂ is empty and (C3) holds
at every h ∈ (0, 10⁻⁶], and Z_exc is empty at every h at which (C2) holds ([[thm:t49-uniform]]); so 𝖹 = 𝖹₁ ∪ 𝖹₃. The set
𝖹 meets I
([[prop:t49-six]]); whether 𝖹 ∩ I is finite is not decided here. For every interval J ⊂ (0, h_*) of length 2·10⁻⁹,
ε_ind has no positive lower bound on J ∖ 𝖹 ([[prop:t49-vector]]); [[prop:np-10-52]] (iii) gives only ε_ind(h) > 0
for h ∈ 𝖧.
