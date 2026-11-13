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
With the 1-form modification of [[eq:iii-b-6-2]], for v_C ∈ (0, 1), e_C, γ_C and a stationary c_C ∈ |x|⁻¹C^∞ equal to
|x|⁻¹(dt − v_C d|x|) for large |x|, put

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
below fail: the scalar type 0 then has an indicial root in (−1, 1) for all small h > 0 ([[prop:np-10-12]] (iv)), and
the fibre inner product B of [[prop:np-10-13]] (i) is indefinite.

*The constants.* We fix, once for the whole stability theory,

    v_C := 1/2,     e_C := 1/102400,     C_0 ∈ [3/2, 100],     γ_C := h⁻¹,  h ∈ 𝖧,                          {#eq:iv4-0-1}

where 𝖧 := (0, h_*) ∖ 𝖹. Here h_* := min(10⁻⁶, h_0, h_tf), with h_0 the smaller of the thresholds of
[[thm:iv5-7-3]] at these (v_C, e_C), with the regularity range C₁ := C_0 + 1, for the weights [[eq:iv4-2-1]] at C_0
and at C_0 − 1, and h_tf the threshold of [[thm:iv6-3-1]]; and 𝖹 := 𝖹₁ ∪ 𝖹₂ ∪ 𝖹₃ ⊂ (0, 10⁻⁶] is the countable set
made of the set 𝖹₁ of [[lem:iv4-1-3]] (b) and the sets 𝖹₂, 𝖹₃ of [[prop:np-10-52]] (ii), (iii). The nonlinear theorem
of [[ch:s27]] takes C_0 = 100.
The 1-form c_C is that of [[prop:np-10-14]] at m = 1 and r_0 = 100, smoothed near r_0/2 and 2r_0 and rescaled to m₀
(every condition on it depends on m r_0⁻² and r/r_0 only, by scaling). It is stationary and equals
|x|⁻¹(dt − v_C d|x|) for large |x| up to O(m₀|x|⁻³) d|x|: [[prop:np-10-14]] states this in the static time, and the
time t of [[sec:iii-b-3-1]] is the outgoing Kerr–Schild time, whose differential differs from the static one by
O(m₀|x|⁻²) d|x|, which changes |x|⁻¹(dt − v_C d|x|) by O(m₀|x|⁻³) d|x|.

Every result of this chapter that names (v_C, e_C, C_0, γ_C) uses these values, and so do all later chapters. The
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

and the coefficient of g⟨c, ω⟩ is −e for every e exactly when m_tr(D/2 − 1) = 1, that is m_tr = 2/(D − 2). With
δ(f g) = −df and δ(2c ⊗_s ω)_a = −∇^b(c_a ω_b + c_b ω_a) = −(∇_(ω♯)c)_a − c_a div ω − (div c) ω_a − (∇_(c♯)ω)_a, this gives
2δ_g G_g E^C ω = h⁻¹ 𝓛_c ω. Finally 2δ_g G_g δ*_g ω = 2δδ*ω + d(div ω), and
2(δδ*ω)_a = −∇^b∇_a ω_b − ∇^b∇_b ω_a = −∇_a(div ω) − Ric(g)_a^b ω_b − ∇^b∇_b ω_a; on a Ricci-flat metric the sum is
−∇^b∇_b ω = □_g ω. ∎

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
ι_w := (7v² − 1 + 3e(1 + v²))/(5v² + 1 − 3e(1 + v²)), which at e = 0 lies in (−1, 1) for every v ∈ (0, 1); and for
every sufficiently small h > 0 the scalar type 0 has an indicial root ι_w(h) with ι_w(h) → ι_w as h → 0⁺.

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
(0, 1). The coefficients of C are polynomials in h, so by Hurwitz's theorem, as in [[lem:s14-small-h]] (b), C has a
root ι_w(h) → ι_w as h → 0⁺; it differs from 2, so it is a root of P_0. ∎

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

*Scalar type l ≥ 1.* The claim is: for every h ∈ (0, 10⁻⁶] and every l ≥ 1, P_l has no root with real part in
[−100, 19/10], and, with multiplicity, exactly three roots with real part > 19/10 and three with real part < −100;
for every l ≥ 2 no root of P_l has real part in (19/10, 2]; and at l = 1 the only root with real part in (19/10, 2] is
ι = 2, a simple root. [[pending:computational-1]]

(iii) Fix h. By [[prop:np-10-12]] (iii), P_l(ι) = h³(κ − ι²)³ + Σ_(j+2k≤5) a_(jk)ι^jκ^k, with coefficients a_(jk)
depending on (v, e, h) and not on l: the part of top weight is h³(κ − ι²)³, and every other term has weight at most
5. Put ι = κ^(1/2)w. Then

    κ⁻³P_l(κ^(1/2)w) = h³(1 − w²)³ + Σ_(j+2k≤5) a_(jk)κ^(j/2+k−3)w^j,

a polynomial in w of degree 6 with leading coefficient −h³ and the other coefficients bounded for κ ≥ 1, since
j/2 + k − 3 ≤ −1/2. So its roots lie in a disc |w| ≤ W independent of l, and on that disc it converges uniformly to
h³(1 − w²)³ as κ → ∞. By Hurwitz's theorem, for κ large its six roots lie within ½ of ±1, three near each; so every
root of P_l satisfies |Re ι| ≥ ½κ^(1/2) once κ ≥ κ_h, for some κ_h depending on h. Likewise
κ⁻¹p_(v)(κ^(1/2)w) = h(1 − w²) + (2h − 2v)κ^(−1/2)w + 6vκ⁻¹, whose two roots tend to ±1. Hence a root with
|Re ι| ≤ R occurs only where κ < κ_h or κ ≤ 4R², that is for finitely many l, each contributing at most six
roots. ∎

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

(iii) (*The interior saddle.*) With c = r_0⁻²(r_0 dt − v(r − r_0) dr) on Minkowski space, at the point r = r_0(1 +
xe^(1/2)/v), r₀²S is block diagonal in the splitting by dt, dr and r dω: the angular block is v(6e^(1/2)x +
v)/(e^(1/2)x + v) Id, and the (dt, dr) block has, at e = 0, trace 5v and determinant 2v²(3 − 2x²), positive for |x| ≤
6/5 < (3/2)^(1/2). At (v, e) = (1/2, 1/102400) the block has trace and determinant

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

    S = −(b′ + 5b/r)     on r dω.                                                                          {#eq:s14-s-ang}

On span{dt, dr}, in the basis (dt, dr), the matrices of s and B are

    s = (0, a′; a′, −2b′) + (tr K)(1, 0; 0, −1) + (1 + e)a′G⁻¹(−2ab, a² + b²; a² + b², −2ab)
        + ((1 + e)²G⁻¹ tr K + 2(1 − e²)G⁻²b(bb′ − aa′))(a², −ab; −ab, b²),
    B = (−1, 0; 0, 1) − (1 + e)G⁻¹(a², −ab; −ab, b²),                                                       {#eq:s14-s-rad}

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

(iii) Here a = r_0⁻¹ and b = −v(r − r_0)r_0⁻², so a′ = 0, b′ = −vr_0⁻² and F = 0. Put y := xe^(1/2)/v, so that
r = r_0(1 + y) and r_0b = −xe^(1/2). Then

    r_0²G = ex² − 1,     r_0² tr K = −v(1 + 4y)/(1 + y),     r_0⁴K(c♯, c♯) = −evx²,

and [[eq:s14-s-rad]] gives, with Λ := (1 + e)²(r_0²G)⁻¹r_0² tr K − 2(1 − e²)(r_0²G)⁻²evx²,

    r_0²s = (0, 0; 0, 2v) + r_0² tr K (1, 0; 0, −1) + Λ(1, xe^(1/2); xe^(1/2), ex²),
    B = (−1, 0; 0, 1) − (1 + e)(r_0²G)⁻¹(1, xe^(1/2); xe^(1/2), ex²).

By [[eq:s14-s-ang]] the angular entry of r_0²S is v + 5vy/(1 + y) = v(6e^(1/2)x + v)/(e^(1/2)x + v). The trace and the
determinant of r_0²S = B⁻¹(r_0²s) on span{dt, dr} are therefore rational in (x, e^(1/2), v); their values at e = 0, with
x fixed, are 5v and 2v²(3 − 2x²), and at (v, e) = (1/2, 1/102400), e^(1/2) = 1/320, they are the stated functions.
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

**Proposition {#prop:np-10-14}** (A damping 1-form on Tangherlini space.) Let m = 1, so that r_h = 1, and let

    g = −f dt² + 2(1 − f) dt dr + (2 − f) dr² + r² 𝑔̸,     f = 1 − mr⁻²,                                   {#eq:s14-tang}

the Tangherlini metric in Kerr–Schild time, regular across the horizon; its t differs from the static time by
∫(f⁻¹ − 1) dr, and g⁻¹ has (t, r) block g^(tt) = −1 − mr⁻², g^(tr) = mr⁻², g^(rr) = f. Let r_0 := 100 and

    c := (2r_0)⁻¹(dt + (v/2) dr)  (r ≤ r_0/2),   ½ r_0⁻²(r_0 dt − v(r − r_0) dr)  (r_0/2 ≤ r ≤ 2r_0),
    c := r⁻¹(dt − v dr)  (r ≥ 2r_0).                                                                      {#eq:s14-cform}

Then c is continuous, and:

(i) r c is past timelike on [r_h/2, ∞);

(ii) ⟨c, dr⟩ > 0 on [r_h/2, r_0 − r_0e^(1/2)/v] and ⟨c, dr⟩ < 0 on [r_0 + r_0e^(1/2)/v, ∞), and on both intervals
f eG(c) + 2(1 − e)⟨c, dr⟩² > 0; so ℓ(−dr), resp. ℓ(dr), is negative definite there ([[prop:np-10-13]] (i));

(iii) S, defined by [[eq:s14-s]] for the metric [[eq:s14-tang]] and the 1-form [[eq:s14-cform]], is a bundle map, free
of the angles and block diagonal in the splitting by dt, dr and r dω, equal at m = 0 to the S of
[[prop:np-10-13]] (iii), and positive definite on |r − r_0| ≤ (6/5)r_0e^(1/2)/v;

(iv) for c = r⁻¹(dt − v dr) on Minkowski space, T = r²(−ℓ(dw/w) + S) of [[prop:np-10-13]] (ii) is B-self-adjoint and
depends on ρ_K and the weights only, and the characteristic polynomial of its (dt, dr) block at ρ_K = 0 is q(d,
ν)/102400,

    q(d, ν) := 102400ν² − (307202 − 307199d)ν + 204795d² − 409605d + 204801;                              {#eq:s14-q}

its eigenvalues are positive at the corner ∂K⁺ (ρ_K = 0) if and only if b_K > b_sf − b*, and at the sink R_v (b_K = 0)
if and only if b_sf < b*, where b* = 0.99340731… is the smaller root of 204795d² − 409605d + 204801;

(v) the condition 2(1 − e)(v − ρ)²/(e(1 − v²)) > 1 − ρ² of [Hin26a, (5.8)] holds for ρ = r/t in
[δ_r, v(1 − δ_sf)] ∪ [v(1 + δ_sf), 10], with δ_sf = 1/100 and every δ_r > 0.

Moreover: (a) conditions (4)–(5) of [Hin26a, Proposition 5.1] off 𝗌𝖿, for 0 < ρ_sf ≤ 2δ_r with some δ_r > 0, follow
from (iv) by continuity, since Tangherlini space differs from its Minkowski model by terms in ρ_sf C^∞ ([Hin26a, p. 39]);
(b) a smoothing of c near r_0/2 and 2r_0 preserves (i) and (ii), which there involve only c and not its derivatives
([Hin26a, p. 41]); (c) in the static time t_s the outer piece is r⁻¹(dt_s − v dr) + O(mr⁻³) dr.

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
α⁻²·2(1 − e)⟨c, dr⟩² ≥ 1.87b² ≥ 1.87e, while α⁻² f e|G(c)| ≤ e(1 − b² + r⁻²(1 − b)) ≤ 1.0002e. *r ≥ 200*:
α⁻¹⟨c, dr⟩ = r⁻² − f/2 < −0.49, α⁻²|G(c)| ≤ 3, and 2(1 − e)·0.24 > 3e.

(iii) [[pending:computational-3]]

(iv) By [[prop:np-10-13]] (ii) at (v, e) = (1/2, 1/102400): 2v(2 − d) = 2 − d, and 102400 q_(1/2,e)(ν) = q(d, ν). The
two roots of q(d, ·) are real (T is B-self-adjoint); their sum (307202 − 307199d)/102400 is positive iff
d < 307202/307199, and their product q(d, 0)/102400 is positive iff d < b* or d > b*′, where
b*, b*′ = (409605 ∓ 7372845^(1/2))/409590, so b* = 0.99340731… and b*′ = 1.00666… > 307202/307199. So all eigenvalues
are positive iff d < b* (which also gives 2 − d > 0). At ρ_K = 0, d = b_sf − b_K; at the sink b_K = 0 and T does not
depend on ρ_K, so d = b_sf.

(v) 2(1 − e)/(e(1 − v²)) = 273064, and |ρ − 1/2| ≥ 1/200 gives 273064(ρ − 1/2)² ≥ 6.8 > 1 ≥ 1 − ρ².

(a)–(c) are the stated arguments: (a) the positivity in (iv) is strict and stable under perturbations of the metric
and the 1-form by ρ_sf C^∞ terms near 𝗌𝖿; (b) the conditions in (i)–(ii) are open conditions on the value of c at each
point; (c) the static time t_s satisfies dt = dt_s + (f⁻¹ − 1) dr with f⁻¹ − 1 = O(mr⁻²). ∎

**Proposition {#prop:np-10-21}** (The structure at infinity.) On 4 + 1 Minkowski space with c = r⁻¹(dt − v dr), in the
coordinates t_* = t − r, ρ = r⁻¹ and the Cartesian frame:

(i) □^C = −2∂_(t_*) ρ(ρ∂_ρ − 3/2 − S̄^C) plus a stationary operator: the coefficient of ∂_(t_*)∂_r is 2 Id, there is no
term ∂_(t_*) times a tangential derivative and no ∂²_(t_*) term, and S̄^C = h⁻¹M with

    M(dr) = 2(1 − v) dr + (1 − ev) dt_*,     M(dt_*) = (1 − e)(1 − v) dt_*,     M = (1 − v) on r dω;

so in the splitting by dr, dt_* and r dω, S̄^C is lower triangular with diagonal h⁻¹(2(1 − v), (1 − e)(1 − v), 1 − v),
diagonalisable, with spectrum h⁻¹{2(1 − v), (1 − e)(1 − v), 1 − v (three times)}, all positive for 0 < v < 1, 0 ≤ e < 1;

(ii) (*the incoming radial set*) the isometry t ↦ −t of η carries c_v := r⁻¹(dt − v dr) to −c_(−v), so it conjugates
□^C with (c_v, h⁻¹) to the operator with (c_(−v), −h⁻¹); the matrix M with −v for v has spectrum
{2(1 + v), (1 − e)(1 + v), 1 + v (three times)};

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

(ii) (t, x) ↦ (−t, x) preserves η and pulls dt back to −dt; c_v becomes −r⁻¹(dt + v dr) = −c_(−v), and E^C changes
sign with c, which is the operator with (c_(−v), −h⁻¹). The spectrum of M at −v is read off (i).

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
(61439800 + 2150399 − 1228796ρ_K)/204800 > 0 and determinant 3(1092260ρ_K² − 113048512ρ_K + 2925089043)/409600, which
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
components. With c = α(dt + b dr), b = v/2, one has G(c)α⁻² = 2(b − 1), c♯α⁻¹ = (b − 2)∂_t + ∂_r, B = g⁻¹ − (1 +
e)G(c)⁻¹c♯ ⊗ c♯; the B-symmetric part X_s of 2Γ_t on the (t, r) block has trace 0 and determinant −(1 + e)²/(e r_h²),
for every b. So its eigenvalues are ±(1 + e)/(e^(1/2)r_h).

(iii) is [[prop:np-10-13]] (i) with ζ = dr, G(dr) = 0, ⟨c, dr⟩ = a.

(iv) By the definition, ϑ_ℋ = (r_h/2) × the largest eigenvalue of ρ_∞σ₁((P_0 − P_0^*)/(2i)) − h⁻¹ℓ(dr), the
damping L contributing −h⁻¹ℓ(ζ)ρ_∞ ([[eq:s14-lh]]). On the angular components the matrix is −2a h⁻¹. On the (t, r)
block, a direct evaluation of the 2 × 2 matrices of (ii) and (iii) gives the characteristic polynomial χ, for every b.

(v) At e = 1/102400, (1 + e)²/(4e) = 10485964801/409600 and s ≥ 5000 for h ≤ 10⁻⁶. The vertex of χ is at
−(3 − e)s/2 < −201/2, so ν₊ < −201/2 iff χ(−201/2) > 0, and

    χ(−201/2) = (102399 − 3077109850h − 31744512005000h²)/(2048000000h²),

which is positive iff h < h_2. The angular eigenvalue −s is below
−201/2 as well. At h = 10⁻⁶ the roots of χ are −10004.11… and −4995.83…. Finally X_s and ℓ(dr) are B-self-adjoint, so
by Weyl's inequality the largest eigenvalue of (r_h/2)(X_s − h⁻¹ℓ(dr)) is at most (r_h/2)(λ_max(X_s) −
h⁻¹λ_min(ℓ(dr))) = ϑ_0 − c₁h⁻¹. ∎

### The inputs in dimension 4 + 1 {#sec:iv4-1}

**Lemma {#lem:iv4-1-1}** (The fibre algebra; [Hin26a, Lemmas 3.3–3.8] in dimension 4 + 1.) On each fibre, with G(c) < 0,
B := g⁻¹ − (1 + e)G(c)⁻¹c♯ ⊗ c♯ is positive definite for e > 0, ℓ_(g,c,e)(ζ) of [[eq:s14-ell]] is B-self-adjoint for
every ζ, and the characteristic polynomial of ½ℓ(ζ) is (ν − G(c)ζ_0)³ times the quadratic of [Hin26a, (3.8)], where
ζ = ζ_0 c + ζ′ with ζ′ ⊥ c. [Hin26a, Lemmas 3.3–3.8] hold in dimension 4 + 1 verbatim.

*Proof.* The three statements are [[prop:np-10-13]] (i), with ⟨c, ζ⟩ = G(c)ζ_0. [Hin26a, Lemmas 3.3–3.8] are proved on a
single fibre from these three facts and from the splitting T* = ℝc ⊕ c^⊥, in which G(ζ) = G(c)ζ_0² + G(ζ′) and ℓ(ζ) has
the block form [Hin26a, (3.5)]. In dimension 4 + 1, c^⊥ has dimension 4 instead of 3, and the factor (ν − G(c)ζ_0)
appears to the third power instead of the second, which no step uses beyond its eigenvalue. ∎

**Lemma {#lem:iv4-1-2}** (The structure at infinity; [Hin26a, (6.4)] in dimension 4 + 1.) Near ∂X, in t_*, ρ and
spherical coordinates,

    □^C_b = −2∂_(t_*) ρ(ρ∂_ρ − 3/2 − S̄^C − ρS̃) + P^C_b + Q∂_(t_*) + R∂²_(t_*),                            {#eq:iv4-1-1}

with S̃ smooth, Q ∈ ρ³Diff¹_b, R ∈ ρ²C^∞, P^C_b ∈ ρ²Diff²_b, and S̄^C constant with spectrum
γ_C{2(1 − v_C), (1 − e_C)(1 − v_C), 1 − v_C (three times)}, all positive.

*Proof.* On 4 + 1 Minkowski space with c = |x|⁻¹(dt − v dr) this is [[prop:np-10-21]] (i): the ∂_(t_*)∂_ρ-coefficient
is 2 Id, there is no ∂_(t_*) times a tangential derivative, and S̄^C is r/2 times the ∂_(t_*)-coefficient less
(n − 1)/2 = 3/2. The metric g_b differs from ḡ by ρ²C^∞ ([[prop:iii-b-3-6]]), and c_C from the model's 1-form by
ρ³C^∞; the differences enter S̃, Q, R and P^C_b as in the proof of [Hin26a, (6.4)], by the same counting
([[sec:iii-e-1]]). ∎

**Lemma {#lem:iv4-1-3}** (The indicial roots; [Hin26a, Theorem 4.9] in dimension 4 + 1.) Let h ∈ (0, 10⁻⁶] and b near
b₀.

(a) Every indicial root ι of P^C_b satisfies Re ι ∉ [−100, 19/10]; the only roots with real part in [−100, 2] are ι = 2
at scalar type 0 and at scalar type 1, each simple. At each type and degree as many roots have real part ≥ 2 as
< −100: three each at scalar type l ≥ 1, two each at scalar type 0, one each at vector type l ≥ 1. The real parts
accumulate only at ±∞.

(b) There is a countable set 𝖹 ⊂ (0, 10⁻⁶] such that for h ∉ 𝖹 the roots are simple and the remaining clauses of
[[thm:iii-e-1-1]] (3) hold.

*Proof.* The indicial family of P^C_b at ∂X is that of the Minkowski model with c = |x|⁻¹(dt − v_C d|x|), independent of
b: g_b − ḡ ∈ ρ²C^∞ and the deviation of c_C are of lower order ([[lem:iv4-1-2]]; [Hin26a, p. 29]: the indicial roots are
determined by the leading part as ρ → 0). In the decomposition into scalar and vector type harmonics of 𝕊³, the
indicial roots of type and degree l are, in the variable ι of [[prop:np-10-12]] (ii) (the 1-form decaying like
ρ^ι = r^(−ι)), the roots of p_(v) and of P_l. (a) is [[prop:np-10-54]].

(b) Fix l. Each condition is the non-vanishing at h of a polynomial in h, and we show that none of these polynomials
vanishes identically; then each fails for at most finitely many h, and 𝖹, the union over l and over the finitely many
conditions at each l, is countable. *Simplicity.* By [[lem:s14-small-h]], for all sufficiently small h > 0 the roots
of P_l, of C and of p_(v) are simple; so their discriminants, polynomials in h, do not vanish identically; and
ι = 2 is not a root of C (proof of [[prop:np-10-54]]). *Excluded points.* For a fixed real x, P_l(x) is a polynomial
in h with value 8v(x − 2)Q_5(x) at h = 0, and p_(v)(x) has value −2v(x − 3) at h = 0. For the scalar type the points
are x ∈ {1 − l, 3 − l, l + 3, l + 5} ∖ {2}: each satisfies x ≤ 1 or x ≥ 4 when l ≥ 1, so Q_5(x) < 0
([[lem:s14-q5]] (a)); at l = 0 the points are 1, 3, 5, and C(x)|_(h=0) = (5e − 2)x + 5e + 4 is 10e + 2, 20e − 2 and
30e − 6 there. For the vector type with l ≥ 2 the points 1 − l, 2 − l, l + 3, l + 4 differ from 3. *Real parts.* Let
k ∈ [3, 51] be an integer, and write P_l(k + iy) = A_k(y²) + iyB_k(y²) with A_k, B_k real polynomials. A non-real root
k + iy, y ≠ 0, makes y² a common root of A_k and B_k, so the resultant Res(A_k, B_k), a polynomial in h, vanishes; it
vanishes in general exactly when P_l has two roots with sum 2k or a double root at k. By [[lem:s14-small-h]], as h → 0⁺
the roots of P_l converge to 2, ι₊, ι₋ or have real parts tending to −∞. The limit sums are 2 + ι_± and
ι₊ + ι₋ = 5 + 1/13653 ([[lem:s14-q5]] (b)); 2 + ι_± = 2k would make 2k − 2 ≥ 4 a real root of Q_5, which
[[lem:s14-q5]] (a) excludes. So for small h > 0 no two roots have sum 2k and no root is double, and Res(A_k, B_k) does
not vanish identically. The same argument applies to C, whose finite limit root is (4 + 5e)/(2 − 5e), and p_(v) has real
roots only. ∎

**Lemma {#lem:iv4-1-4}** (The 1-form; [Hin26a, Proposition 5.1] in dimension 4 + 1.) With the weights

    α_K := 1,     α_sf := −C_0 − 5/2,                                                                       {#eq:iv4-2-1}

w := ρ_sf^(α_sf+1)ρ_K^(α_K) and w′ := ρ_sf^(α_sf+1), c_C satisfies [Hin26a, Proposition 5.1] (1)–(6) on Tangherlini
space g_(b₀), for some δ_r > 0 and with δ_sf = 1/100; and on g_b for b near b₀, with smaller δ_r and the same δ_sf,
conditions (5)–(6) on 𝗌𝖿 not depending on b. The same holds with C_0 − 1 for C_0 in [[eq:iv4-2-1]], that is at
α_sf = −C_0 − 3/2, for every C_0 ≥ 0: the conditions at 𝗌𝖿 are then b_sf = −C_0 − 1/2 < b* and b_K = 1 > b_sf − b*.

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
future null, so [[lem:iv4-1-1]] ([Hin26a, Lemma 3.5]) makes ℓ of them B-negative definite, with the sign that damps.
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
[−100, 19/10] ∪ (19/10, 2), so (β_−, 2) with β_− := max{Re ι < −100} < −100 ≤ −C_0 is a gap. ∎

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

Throughout n = 4. The mass m₀, R₁ = m₀^(1/2), ℬ and b₀ = (m₀, 0) are those of [[sec:iii-b-3-1]]. Let r_♯ := ½R₁ be the
inner radius (the radius m of [Hin26a]) and r_c := 100R₁ the radius of the saddle point of c_C (the radius r_0 of
[Hin26a]; the r_0 = 100 of [[prop:np-10-14]] at m = 1, rescaled). Let v := v_C = 1/2 and e := e_C = 1/102400.

*Coordinates.* We work in the Kerr–Schild coordinates (t, x) of [[sec:iii-b-3-1]], with r := |x|. For b ∈ ℬ,
g := g^KS_b = η + H_b k_b ⊗ k_b is defined and smooth with H_b > 0 on ℝ_t × {r ≥ ½r_♯}, smoothly in b. Indeed the
estimate of [[sec:iii-b-3-1]], run at r = ¼R₁ with ‖A‖² < R₁²/100, gives |x|² > 2‖A‖² ≥ s and
r_A² ≥ (1/16 − 1/100)R₁², under which the condition ‖A‖²(r_A² + ‖A‖²) < r_A⁴ of [[lem:iii-b-3-3]] (c) holds. The metric
g_b of [[sec:iii-b-3-1]] is Φ_m*g with Φ_m(t, x) = (t − T_m(|x|), x), and [[rem:iv5-7-4]] transfers the results to it.
The 1-form c := c_C of [[sec:iv4-0]] is defined in these coordinates on {r ≥ r_♯}. We extend it to {r ≥ ½r_♯} as a
stationary smooth past timelike 1-form; such an extension exists, the past timelike covectors at a point forming an open
convex cone.

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
Diff^k_3b with weights; ∂_(z^μ) ∈ ρ_sf 𝒱_3b(M^♭) by [Hin26a, Section 2];

- the projection (t, x) ↦ x extends to a smooth map π : M^♭ → X̄_♯ := X̄ ∩ {r ≥ r_♯}, so π*C^∞(X̄_♯) ⊂ C^∞(M^♭).

The semiclassical 3b-pseudodifferential calculus Ψ_(3b,ħ)(M^♭) carries with it its principal symbols, the operator wave
front set WF′_(3b,ħ), the elliptic set Ell_(3b,ħ), elliptic parametrices, the sharp Gårding inequality and the Sobolev
spaces H^s_(3b,h); it exists in this dimension by [[prop:np-10-65-a]]. Write

    H^(s,(β_sf,β_K))_(3b,h) := ρ_sf^(β_sf) ρ_K^(β_K) H^s_(3b,h)(M^♭; 𝒯*)

([Hin26a, (5.19)]), normed with the density |dg| and the fibre inner product B of [[lem:iv5-0-4]]. On Ω there are three
kinds of space: H^(s,(·))_(3b,h)(Ω)^(•,−), restrictions to Ω° of elements with support in {t ≥ 0}, so supported at X_0
and extendible at Σ^♯; (·)^(−,•), extendible at X_0 and supported at Σ^♯; and H̄, extendible at both ([Hin26a,
Section 2.3]). In all of these constructions the dimension enters only as the number of coordinates.

**Proposition {#prop:np-10-65-a}** (The calculus in every dimension.) The semiclassical 3b-calculus of [Hin26a,
Section 2.3] is constructed on ℝ_t × ℝ^(N−1)_x for every N ([Hin23d, pp. 3, 7, 10–12, and Proposition 5.10, p. 109],
N the spacetime dimension), as bounded geometry pseudodifferential operators in the sense of [Shu92] ([Hin23d, p. 12]),
and its bounded geometry construction is that of [Hin26d] for a smooth manifold of any dimension ([Hin26d, Definitions
1.3 and 1.9 and Section 3], with the 3b-algebra among its examples in every dimension, [Hin26d, p. 14, example (10)]).
At N = 5 it is the calculus of the compactification M^♭ of [[def:iv5-0-1]], with fibres 𝕊³.

*Proof.* These are the cited results, stated there for every dimension. ∎

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
because ∂_(z^μ) ∈ ρ_sf 𝒱_3b. The rest is [Hin26a, (2.13)–(2.14)], with the same proof. (On Tangherlini space,
Γ ∈ mρ³C^∞ by [[prop:np-10-22]] (i).)

(d) c is stationary and smooth on {r ≥ ½r_♯}, and equals r⁻¹(dt − v dr) for r ≥ 3r_c ([[prop:np-10-14]] (b)). Its
components (r⁻¹, −vr⁻¹x̂) lie in |x|⁻¹C^∞(X̄), so c ∈ ρ_sf C^∞(M^♭; 𝒯*). By [[sec:iv4-0]], the trace weight 2/3 gives
hG_gE^C the form of [Hin26a], so L_h = 4ih δ_g(c ⊗_s ·) + 2ihe dι_(c♯) is [Hin26a, (3.2)]. Now δ_g and d lie in
ρ_sf Diff¹_3b by (c), and multiplication by c or ι_(c♯) lies in ρ_sf C^∞; so L_h ∈ hρ_sf²Diff¹_3b. The principal
symbols are [Hin26a, Lemma 3.2], a pointwise identity free of the dimension ([[prop:np-10-13]] (i)). ∎

**Lemma {#lem:iv5-0-3}** (The causal facts; [Hin26a, p. 15] and the uses in [Hin26a, Propositions 5.6, 5.16] in
dimension 4 + 1.) Let r̂ := ¾R₁ and T_0 := ½. There is a neighbourhood U ⊂ ℬ of b₀ such that for b ∈ U:

(a) for every β ∈ (−1, 1], d(t − βr) is past timelike on {r ≥ ½r_♯}, with
g⁻¹(dt − β dr, dt − β dr) ≤ −(1 − β²); in particular dt and d(t ± κr), κ ∈ (0, 1), are past timelike, X_0 is
spacelike, and future timelike vectors point into Ω at X_0;

(b) r²g⁻¹(dτ, dτ) ≤ −¾ on τ⁻¹([0, T_0]); so dτ is past timelike for g_3b := ρ_sf²g there, uniformly up to 𝗌𝖿;

(c) on {½r_♯ ≤ r ≤ r̂}, dr is future timelike, with g⁻¹(dr, dr) ≤ −½; so Σ^♯ is spacelike, future timelike vectors
point out of Ω there, and −dr is past timelike;

(d) dρ_K/ρ_K² = −dt with ρ_K = t⁻¹ near (K⁺)°, and dρ_sf/ρ_sf² = −dr.

*Proof.* (a) The time orientation is the one in which dt is past timelike ([Hin26a, p. 14]). By [[lem:iii-b-3-3]] (e),
g⁻¹(dt − β dr, dt − β dr) = −(1 − β²) − H_b(1 + βr_A/|x|)² < 0 for β ∈ (−1, 1], wherever the condition of
[[lem:iii-b-3-3]] (c) holds, which is all of {r ≥ ½r_♯}. The family s ↦ d(t − sβr), s ∈ [0, 1], is timelike throughout
and starts at dt, so it stays in the past cone. A future timelike V has dt(V) > 0, since dt is past timelike.

(b) dτ = r⁻¹(dt − τ dr), so r²g⁻¹(dτ, dτ) is the quantity of (a) at β = τ ∈ [0, ½], at most −(1 − ¼). As
g_3b⁻¹ = r²g⁻¹, this is the claim; on Tangherlini space it is [[prop:np-10-22]] (ii).

(c) At b₀, g⁻¹(dr, dr) = 1 − m₀r⁻² ≤ 1 − 16/9 on [½r_♯, r̂] and g⁻¹(dr, dt) = m₀r⁻² > 0 ([[prop:np-10-22]] (iii)). The
second says that the timelike covectors dr and dt lie in opposite cones, so dr is future timelike. Both strict
inequalities hold on a compact set, and g⁻¹ is continuous in b there, so they persist on a neighbourhood U of b₀. A
future timelike V has dr(V) < 0, so V points out of {r ≥ r_♯}.

(d) is direct. ∎

**Lemma {#lem:iv5-0-4}** (The fibre algebra and the subprincipal symbol; [Hin26a, Lemmas 3.3–3.9, Corollary 3.6] in
dimension 4 + 1.) At every point of M^♭, [Hin26a, Lemmas 3.3–3.8 and Corollary 3.6] hold for (g, c, e), with
B := g⁻¹ − (1 + e)G(c)⁻¹c♯ ⊗ c♯. The skew-adjoint part S := (2ih)⁻¹(L_h − L_h*), adjoint for |dg| and B, is the bundle
map of [Hin26a, Lemma 3.9], with the same formula. There is C > 0, uniform for b ∈ U, such that
C(ρ_sf⁻²ℓ(ζ))² + ρ_sf⁻²G(ζ) is B-positive definite for 0 ≠ ζ ∈ ³ᵇT*_Ω M^♭.

*Proof.* [Hin26a, Lemmas 3.3–3.8] are [[lem:iv4-1-1]]; [Hin26a, Corollary 3.6] follows from [Hin26a, Lemma 3.5] on
one fibre, as there. For [Hin26a, Lemma 3.9], the proof evaluates (L_h − L_h*)ω at a point p for an ω covariantly
constant at p. It uses [Hin26a, (3.10)], the formula (2ih)⁻¹L_h^(*g⁻¹) = −ec δ_g − 2ι_(c♯)δ*_g, which follows from
[Hin26a, (3.2)], and the map b̃_(g,c,e) of [Hin26a, (3.7)]. These are index calculations in which the dimension
appears only as the range of summation, and the metric adjoint is taken with |dg| in every dimension ([[eq:s14-s]]).
For the uniform C, note that ρ_sf⁻²G and ρ_sf⁻²ℓ are smooth homogeneous functions on ³ᵇT*M^♭ ([[lem:iv5-0-2]] (a),
(d)), and B is continuous on the compact Ω, K⁺ and 𝗌𝖿 included. [Hin26a, Corollary 3.6] at each point and compactness
of the unit sphere bundle over Ω give one C ([Hin26a, p. 47]), and continuity in b gives it for b ∈ U, shrinking U. ∎

**Lemma {#lem:iv5-0-5}** (The 1-form; [Hin26a, Proposition 5.1] in dimension 4 + 1.) Let (α_sf, α_K) = (−C_0 − 5/2, 1)
with C_0 ∈ [0, 100], the weights [[eq:iv4-2-1]]. Put w := ρ_sf^(α_sf+1)ρ_K^(α_K) and w′ := ρ_sf^(α_sf+1). Shrinking U,
there are δ_r ∈ (0, (4r_c)⁻¹) and δ_sf = 1/100 such that for b ∈ U, c satisfies [Hin26a, Proposition 5.1] (1)–(6)
with r_c for r_0 and r_♯ for the inner radius of [Hin26a, Proposition 5.1]. The positivity statements (3)–(6) hold with lower bounds uniform in b ∈ U.

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

#### Elliptic estimates and the characteristic set at fibre infinity {#sec:iv5-1}

**Lemma {#lem:iv5-1-1}** ([Hin26a, Lemma 5.4].) The semiclassical 3b-characteristic set of ρ_sf⁻²P_h is ∂Σ ∪ o.

*Proof.* ρ_sf⁻²G and ρ_sf⁻²ℓ are homogeneous of degrees 2 and 1 on the fibres ([[lem:iv5-0-2]]), so the symbol vanishes
on o. At finite ζ ≠ 0, p(ζ) is invertible by [[lem:iv5-0-4]] ([Hin26a, Lemma 3.7]). At fibre infinity G is principal
and ℓ subprincipal, so the characteristic set there is ∂Σ. ∎

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
χ_(τ,2)χ_(r,2)ω = χ_(τ,2)χ_(r,2)ω′. By [[lem:iv5-1-1]], ρ_sf⁻²P_h is elliptic on WF′(B_1). A microlocal parametrix in
the calculus of [[def:iv5-0-1]] gives the estimate; the weights only add terms of lower order, since
w⁻¹[P_h, w] ∈ hρ_sf²Diff¹_3b for w = ρ_sf^β ρ_K^(β′). ∎

**Proposition {#prop:iv5-1-3}** ([Hin26a, Proposition 5.6].) The estimates [Hin26a, (5.21) and (5.22)] hold on
(M^♭, g, c) with the cut-offs above, in the strong sense stated there.

*Proof.* We prove [Hin26a, (5.21)] for ω ∈ H^(s,(α_sf,α_K))_(3b,h); the strong sense follows by the standard
regularisation ([Hin26a, p. 45]). By [[prop:iv5-1-2]] it suffices to work in an h-independent neighbourhood of ∂Σ_±;
replace ω by χ_(τ,0)χ_(r,0)ω. Let ρ̂ define fibre infinity, Ĝ := ρ̂²ρ_sf⁻²G, χ ∈ C_c^∞(ℝ) equal to 1 near 0, and χ_±
localise near ∂Σ_±. Take the commutant [Hin26a, (5.24)],

    a := ρ_sf^(−α_sf−1) ρ_K^(−α_K) ρ̂^(−s+½) χ_± χ(𝔛ρ̂) χ(𝔛Ĝ) χ_(τ,1)χ_(r,1),

and a quantisation A = A* with WF′(A) = supp a. Then [Hin26a, (5.25)] holds:

    ∓Im⟨P_hω, A²ω⟩ = ⟨(±(Re L_h − Im □_h)A² ∓ (i/2)[P_h, A²])ω, ω⟩.

*The main term.* On supp a, for 𝔛 large, the covectors are close to future (for +), resp. past (for −) lightlike
covectors. c is past timelike ([[lem:iv5-0-5]] (1)), so [[lem:iv5-0-4]] ([Hin26a, Lemma 3.5]) makes ±ρ_sf⁻²ℓ positive
definite there, with a lower bound fixed by compactness. Im □_h ∈ h Diff¹_(3b,ħ) is semiclassically subprincipal, □_h
having real scalar principal symbol. This gives [Hin26a, (5.26)]: ±(Re L_h − Im □_h)A² = A(B̃_0*B̃_0 + c_0Λ*Λ)A + hE.

*The commutator and the cut-offs.* ∓(i/2)[P_h, A²] has principal symbol ∓aH_Ga at order h ([Hin26a, (5.27)]). In
[Hin26a, (5.29)] it is split as follows. Differentiation of χ_± and of χ(𝔛Ĝ) lands off the characteristic set, so these
terms are hAQP_h. Differentiation of χ(𝔛ρ̂) gives order −∞. Differentiation of the weights gives bounded multiples of
a², the term hAB̃_2A. Next, ∓χ_(τ,1)H_Gχ_(τ,1) = ∓χ_(τ,1)χ′_(τ,1)H_Gτ = −e_T², because H_Gτ = 2g⁻¹(ζ, dτ) is positive
at future and negative at past lightlike ζ over supp dχ_(τ,1) ⊂ τ⁻¹([0, T_0)), where dτ is past timelike
([[lem:iv5-0-3]] (b)). Finally ∓χ_(r,1)H_Gχ_(r,1) = +e_R², because H_Gr = 2g⁻¹(ζ, dr) is negative at future and
positive at past lightlike ζ over supp dχ_(r,1) ⊂ r⁻¹([r_♯, r̂)), where dr is future timelike ([[lem:iv5-0-3]] (c)).

*Conclusion.* Cauchy–Schwarz on the left of [Hin26a, (5.25)] gives [Hin26a, (5.30)]. Drop ‖E_Rω‖², which has the sign
of the main term, and absorb h⟨B̃_2Aω, Aω⟩ ≤ Ch‖B̃_0Aω‖² + h^N‖ω‖². Iterate in h^(1/2) on the error term
h^(1/2)‖B̃′_0ω‖, whose wave front set lies near supp a. This proves [Hin26a, (5.21)]; the a priori term is h^(1/2)‖E_Tω‖,
supported over supp dχ_(τ,1).

For [Hin26a, (5.22)], P_h* = □_h* + iL_h* with □_h* − □_h ∈ hDiff¹ and L_h* − L_h ∈ hDiff⁰, and [Hin26a, (5.28)] has
main term ∓ρ_sf⁻²ℓ, now negative definite. The weights in a become (−α_sf − 2, −α_K). [Hin26a, (5.29)] holds for P_h*,
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

**Proposition {#prop:iv5-2-1}** ([Hin26a, Proposition 5.8].) The estimates [Hin26a, (5.33) and (5.34)] hold with r_c
for r_0.

*Proof.* (1) By [[prop:iv5-1-2]] and the ellipticity of 1 + iCL_h*ρ_sf⁻² it suffices to prove [Hin26a, (5.33)] with 𝓛_h
for P_h, near o. With χ_0, χ_K and ψ as in [Hin26a, (5.35)] (r_c for r_0), take the commutant [Hin26a, (5.36)],
a = ρ_K^(−α_K)ψ(r)χ_K(𝔛ρ_K)χ_0(𝔛|ζ|), and A = A*. The pairing is [Hin26a, (5.37)–(5.38)]:

    h⁻¹Im⟨𝓛_hω, A²ω⟩ = ⟨𝒞ω, ω⟩,     𝒞 = ((i/(2h))[−L_h + J, A²] − h⁻¹(Im L_h)A²) − h⁻¹AQA − (1/(2h))[A, [A, Q]].

The bracket has principal symbol aH_(−ℓ+j)a − Sa². As ℓ is linear in the fibre, H_(−ℓ)f = −ℓ(df) for a function f on
M^♭. This gives [Hin26a, (5.39)], aH_(−ℓ+j)a − Sa² = −c_0a² − b_0² − b_R² + e² + f, with b_0, b_R, e and f those of
[Hin26a, (5.40)–(5.43)]. Their square roots exist for the following reasons.

- b_0: S is positive definite on {|r − r_c| ≤ (6/5)r_c e^(1/2)/v} ([[lem:iv5-0-5]] (3)), so S ≥ 2c_0 there; ℓ(dρ_K/ρ_K²)
= −ℓ(dt) and H_jρ_K⁻¹ are bounded on supp χ_0(𝔛|ζ|) and carry the factor ρ_K ≲ 𝔛⁻¹.

- b_R: on supp ψ′ ∩ {±(r − r_c) > 0}, −ℓ(±dr) ≥ 2c₁ ([[lem:iv5-0-5]] (6)), and |H_jr| = O(|ζ|²) < c₁ on
supp χ_0(𝔛|ζ|) for 𝔛 large.

- e: dρ_K/ρ_K² = −dt is future timelike ([[lem:iv5-0-3]] (d)), so ℓ(−dt) is positive definite ([[lem:iv5-0-4]]), and
−χ_Kχ′_K ≥ 0; e is supported away from ρ_K = 0.

- f is supported off o, where [[prop:iv5-1-2]] applies.

For Q: Q_0 has the positive definite principal symbol G + Cρ_sf⁻²ℓ² ([[lem:iv5-0-4]]), so Q_0 = Θ*Θ + R with
R ∈ Ψ^(−∞)_3b, which is [Hin26a, (5.44)]; the symbol of h⁻¹h³Q_1 vanishes quadratically at o, so it is O(𝔛⁻²) on
supp a, which gives [Hin26a, (5.45)] by Gårding; and the double commutator lies in hΨ and gives [Hin26a, (5.46)].
Collecting, fix 𝔛 large and then h small to absorb ‖Aω‖². Then [Hin26a, (5.47)], with WF′(F) ⊂ Ell(𝓛_h), gives
[Hin26a, (5.48)], and finitely many iterations in h^(1/2) give [Hin26a, (5.33)], with δ := 𝔛⁻¹.

(2) Replace P_h* by 𝓛_h* = iP_h*(1 − iCρ_sf⁻²L_h) = −L_h* + J + iQ and take
a = ρ_K^(α_K)ψχ_K(𝔛ρ_K)χ_0(𝔛|ζ|). The main symbol is aH_(−ℓ+j)a + Sa² = c_0a² + b_0² + b_K² − e² + f with the b_0, b_K,
e, f of [Hin26a]. The same three facts give the square roots, now with b_K from the sign of −ℓ(dt) and e from
[[lem:iv5-0-5]] (6) on supp ψ′. Q enters with a lower bound by [Hin26a, (5.44)–(5.45)], and the iteration is the same. ∎

#### The saddle point at the corner ∂K⁺ {#sec:iv5-3}

From here on, ρ_K = r/t and ρ_sf = 1/r.

**Proposition {#prop:iv5-3-1}** ([Hin26a, Proposition 5.9].) The estimates [Hin26a, (5.51) and (5.52)] hold with the
weights of [[lem:iv5-0-5]].

*Proof.* (1) Replace P_h by 𝓛_h. With χ_sf, χ_K and χ_0 as in [Hin26a], take the commutant [Hin26a, (5.53)],
a = w⁻¹χ_sf(𝔛ρ_sf)χ_K(ρ_K)χ_0(𝔛|ζ|). Then 𝒞 ∈ ρ_sf^(−2α_sf)ρ_K^(−2α_K)Ψ_3b, and [Hin26a, (5.54)] holds:
aH_(−ℓ+j)a − Sa² = −c_0ρ_sf²a² − b_0² − b_sf² + e² + f, with the b_0, b_sf, e and f of [Hin26a]. Their square roots
exist for the following reasons.

- b_0: ρ_sf⁻²(−ℓ(dw/w) + S) is positive definite on {ρ_sf ≤ 2δ_r, ρ_K ≤ 2δ_r} ([[lem:iv5-0-5]] (4)), with a fixed lower
bound; ρ_sf⁻²w⁻¹H_jw vanishes at o, since ρ_sf⁻²j vanishes cubically there.

- b_sf: on supp χ′_K, ρ_K ∈ [(5/4)δ_r, (3/2)δ_r), and [[lem:iv5-0-5]] (6) on 𝗌𝖿 ∩ {r/t ∈ [δ_r, v(1 − δ_sf)]} gives
ρ_sf⁻²(−ℓ(dρ_K)) > 0 near 𝗌𝖿 for 𝔛 large.

- e: dρ_sf/ρ_sf² = −dr, and −ℓ(dr) is positive definite for r ≥ r_c + r_c e^(1/2)/v ([[lem:iv5-0-5]] (6)); H_jr
vanishes at o.

e is supported away from 𝗌𝖿 and gives the a priori term. Estimating the left side by
c_0⁻¹h⁻²‖ρ_sf⁻¹A𝓛_hω‖² + ¼c_0‖ρ_sfAω‖² produces the weights of [Hin26a, (5.51)]. The rest is the proof of
[[prop:iv5-2-1]], with δ := 𝔛⁻¹.

(2) Take a = wχ_sf(𝔛ρ_sf)χ_K(ρ_K)χ_0(𝔛|ζ|) and the pairing with 𝓛_h*. Then
aH_(−ℓ+j)a + Sa² = c_0ρ_sf²a² + b_0² + b_K² − e² + f, with the symbols of [Hin26a]. These are those of (1) with
−α_sf − 2 for α_sf; b_0 comes from [[lem:iv5-0-5]] (4), and the a priori term from supp χ′_K. ∎

#### The sink in 𝗌𝖿° {#sec:iv5-4}

**Proposition {#prop:iv5-4-1}** ([Hin26a, Proposition 5.11].) The estimates [Hin26a, (5.55) and (5.56)] hold with
w′ = ρ_sf^(α_sf+1) and δ_sf of [[lem:iv5-0-5]].

*Proof.* (1) The commutant is a = (w′)⁻¹χ_sf(𝔛ρ_sf)χ_R((r/t)/v − 1)χ_0(𝔛|ζ|), with χ_R supported in
(−2δ_sf, 2δ_sf) and equal to 1 on [−(5/4)δ_sf, (5/4)δ_sf]. Then [Hin26a, (5.57)] holds:
aH_(−ℓ+j)a − Sa² = −c_0ρ_sf²a² − b_0² + e₁² + e₂² + f. Their square roots exist for the following reasons.

- b_0: [[lem:iv5-0-5]] (5), for 𝔛 large.

- e₁: dρ_sf/ρ_sf² = −dr, H_j(ρ_sf⁻¹) = H_jr, and [[lem:iv5-0-5]] (6) for large r.

- e₂: on supp dχ_R, |(r/t)/v − 1| ∈ [(5/4)δ_sf, 2δ_sf], where the sign of −r²ℓ(d(r/t)) is that of χ′_R
([[lem:iv5-0-5]] (6) on the two sides of the sink).

e₁ and e₂ are supported away from {|(r/t)/v − 1| ≤ δ_sf, ρ_sf ≤ 𝔛⁻¹} and give ‖Eω‖. The rest is the proof of
[[prop:iv5-2-1]].

(2) Take a = w′χ_sf(𝔛ρ_sf)χ_R((r/t)/v − 1)χ_0(𝔛|ζ|). Then aH_(−ℓ+j)a + Sa² = c_0ρ_sf²a² + b_0² + b₁² + b₂² + f. Every
term except f, which is elliptic, has the sign of the main term, by the same three facts. So [Hin26a, (5.56)] carries no
a priori term. ∎

#### Propagation between the critical sets {#sec:iv5-5}

**Proposition {#prop:iv5-5-1}** ([Hin26a, Proposition 5.12].) The estimates [Hin26a, (5.58) and (5.59)] hold with
r_3 := r_c − (52/50)r_c e^(1/2)/v, r_4 := r_c − (51/50)r_c e^(1/2)/v and r_♯ < r_1 < r_2 < r_3, near K⁺ with
ρ_K = t⁻¹.

*Proof.* (1) The commutant is a = ρ_K^(−α_K)χ₁(r − r_1)χ₂(r)χ_K(ρ_K)χ_0(𝔛|ζ|), where χ₁(x) = e^(−𝔛/x) for x > 0, so
χ₁′(x) = 𝔛x⁻²χ₁(x). Then [Hin26a, (5.60)] holds: aH_(−ℓ+j)a − Sa² = −a² − b_0² + e_R² + e_T² + f, with the b_0, e_R,
e_T and f of [Hin26a]. The square roots exist for the following reasons.

- b_0: on [r_1, r_4] ⊂ [r_♯, r_c − r_c e^(1/2)/v], −ℓ(−dr) is positive definite ([[lem:iv5-0-5]] (6)), so
−𝔛(r − r_1)⁻²(−ℓ(dr) + H_jr) ≥ C for any fixed C once 𝔛 is large.

- e_R: χ₂ is decreasing and ℓ(dr) is positive definite there.

- e_T: dρ_K/ρ_K² = −dt is future timelike, so ℓ(−dt) > 0 ([[lem:iv5-0-3]] (d), [[lem:iv5-0-4]]).

e_R (on supp χ₂′χ_K) and e_T (on supp χ₂χ′_K) give ‖Eω‖. The rest is as before.

(2) Take a = ρ_K^(α_K)χ₁(r_4 − r)χ̃₂(r)χ_K(ρ_K)χ_0(𝔛|ζ|), with χ̃₂ = 0 near (−∞, r_1] and 1 near [r_2, ∞). Then
aH_(−ℓ+j)a + Sa² = a² + b_0² + b_T² − e_R² + f, and the only a priori term is e_R, on supp χ̃₂′. ∎

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
is the proof of [[prop:iv5-2-1]]: 𝓛_h, the Q-terms [Hin26a, (5.44)–(5.46)], and the iteration.

In (2) the commutant is Wχ₁(φ − φ_1)χ̃₃(φ)χ_⋆χ_0, with χ̃₃ = 1 near φ ≤ φ_3 and 0 near φ ≥ φ_4. The main term
H_(−ℓ)χ₁(φ − φ_1) = χ₁′(−ℓ(dφ)) is now positive, the sign the adjoint pairing [Hin26a, (5.49)] needs. The χ_⋆-terms,
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
([[lem:iv5-0-4]], [Hin26a, Lemma 3.5]), with a lower bound by compactness. On supp χ_r′ ⊂ [r_♯, r_♯ + ε_r],
−ℓ(−dr) > 0 ([[lem:iv5-0-5]] (6), as r_♯ + ε_r < r_c − r_c e^(1/2)/v). Take a = χ₁(T_2 − φ)χ̃(t)χ_r(r)χ_0(𝔛|ζ|), with
χ̃ = 0 on t ≤ ½ε_X and 1 on t ≥ ε_X, and χ_r = 0 near r ≤ r_♯ + ½ε_r and 1 on r ≥ r_♯ + ε_r, both non-decreasing. The
terms of aH_(−ℓ+j)a are signed as follows: H_(−ℓ)χ₁(T_2 − φ) = −χ₁′(−ℓ(dφ)) is the negative main term, dominating S and
j for 𝔛 large; H_(−ℓ)χ̃(t) = χ̃′(−ℓ(dt)) ≥ 0 needs control on supp χ̃′ ⊂ Ell(E); and
H_(−ℓ)χ_r(r) = χ_r′(−ℓ(dr)) = −χ_r′(−ℓ(−dr)) ≤ 0 has the sign of the main term and is dropped. The rest is the proof of
[[prop:iv5-2-1]]. The supports avoid X_0 and Σ^♯, as the convention on Schwartz kernels requires.

(2) d(t − κr) is past timelike ([[lem:iv5-0-3]] (a), β = κ). Take

    a = χ₁(t − t_1)χ_late(t)f(t − κr)χ_r(r)χ_0(𝔛|ζ|),

with χ_late non-increasing, 1 on t ≤ t_2 and 0 on t ≥ t_2 + 1, and f non-decreasing, 0 on (−∞, −c₁] and 1 on [0, ∞). In
the adjoint pairing [Hin26a, (5.49)] the main term must be positive. The terms are signed as follows:
H_(−ℓ)χ₁(t − t_1) = χ₁′(−ℓ(dt)) is positive and dominant; H_(−ℓ)f = f′(−ℓ(d(t − κr))) ≥ 0 has its sign and is dropped;
H_(−ℓ)χ_late = χ_late′(−ℓ(dt)) ≤ 0 needs control on {t_2 ≤ t ≤ t_2 + 1}; and H_(−ℓ)χ_r ≤ 0 needs control near Σ^♯. On
supp a, r ≤ (t + c₁)/κ and t ≤ t_2 + 1, so the support is compact, and χ₁(t − t_1) is bounded below on WF′(B_0). The rest
is as in (1), with 𝓛_h*. ∎

#### Energy estimates {#sec:iv5-6}

[Hin26a, Lemma 5.14] is stated for an arbitrary time-oriented Lorentzian vector space, and [Hin26a, Corollary 5.15] on
ℝ^(1+n) for every n and on n-dimensional manifolds of bounded geometry ([Hin26a, pp. 58–60]). Both are used as stated,
with n = 4. Near X_0 the bounded geometry is that of the τ-level sets, with preferred charts products of charts on 𝕊³
with dyadic intervals in r. Near Σ^♯ it is that of the r-level sets, with charts on 𝕊³ times unit intervals in t. The
data required to lie in a compact subset of C^∞(I × B_3) are g, B, a 3b-connection, ℓ and φ; they do so by
[[lem:iv5-0-2]] (a), (c), (d), uniformly for b ∈ U. The hypothesis on ℓ, positive definite on future causal covectors,
is [[lem:iv5-0-4]] ([Hin26a, Lemma 3.5]).

**Proposition {#prop:iv5-6-1}** ([Hin26a, Proposition 5.16] in dimension 4 + 1.) The estimates [Hin26a, (5.66)–(5.69)]
hold with T := T_0, with the radii of [Hin26a] read as r_♯ ≤ r_1 < r_2 < r_3 ≤ r̂, and with the level-set density
r⁴|dr d𝑔̸| for the density r³|dr d𝑔̸| of [Hin26a] in the norms on τ⁻¹(T). Moreover, at fixed h, for
ω ∈ ρ_sf^(α_sf)H̄²_3b without support condition,

    ‖ω‖_(ρ_sf^(α_sf)H̄¹_3b(τ⁻¹([0,T_0]))) ≤ C_h(‖P_hω‖_(ρ_sf^(α_sf+2)L²(τ⁻¹([0,T_0])))
                                                + ‖(ω, r𝓛_(∂_t)ω)|_(X_0)‖_(ℋ_data)),                {#eq:iv5-6-1}

where ℋ_data := ρ_sf^(α_sf)H̄¹_b(X_0, r⁴|dr d𝑔̸|) ⊕ ρ_sf^(α_sf)H̄⁰_b(X_0, r⁴|dr d𝑔̸|).

*Proof.* [Hin26a, (5.66)]. Take the multiplier a²L_h with a = ρ_sf^(−α_sf−2)e^(−𝔛τ)H(T_0 − τ)H(r − r_♯) (H the
Heaviside function), and the pairing [Hin26a, (5.70)],
h⁻¹Im⟨P_hω, a²L_hω⟩ = ⟨𝒞ω, ω⟩ − h⁻¹‖aL_hω‖². The principal symbol of 𝒞 is aT_(G,da,ℓ) − a²E in the notation of
[Hin26a, (5.61)], since H_Ga = 2g⁻¹(ζ, da). This leads to the decomposition [Hin26a, (5.71)], whose derivation only
expands (i/2)(□_h*bL_h − L_h*b□_h) in local coordinates with b = a². Then a da is [Hin26a, (5.72)], and the weight
identity [Hin26a, (5.73)] holds: aT_(G,−da,ℓ) = ρ_sf⁴T_(ρ_sf⁻²G, −a da, ρ_sf⁻²ℓ), by bilinearity, free of the dimension.

−a da is past timelike for 𝔛 large, since dτ is past timelike with r²g⁻¹(dτ, dτ) ≤ −¾ ([[lem:iv5-0-3]] (b)) and the
δ(r − r_♯)-part of −a da is a positive multiple of −dr, past timelike ([[lem:iv5-0-3]] (c)). So [Hin26a, Corollary
5.15] is integrated over {r ≥ r_♯, 0 ≤ τ ≤ T_0} twice: with dτ and φ² = 𝔛a² + ρ_sf^(−2α_sf−4)e^(−2𝔛τ)δ(T_0 − τ), and
with −dr and φ² = ρ_sf^(−2α_sf−4)e^(−2𝔛τ)δ(r − r_♯). Here the level sets of τ carry r⁴|dr d𝑔̸|, which tensored with
|dτ| is |dg| ([[lem:iv5-0-2]] (b)). This gives [Hin26a, (5.74)].

The other terms of [Hin26a, (5.71)] carry the total weight ρ_sf⁴ of ∇*T∇ and are bounded by [Hin26a, (5.75)] and its
companions. The left side of [Hin26a, (5.70)] is at least −½h⁻¹(‖aP_hω‖² + ‖aL_hω‖²), which gives [Hin26a, (5.76)].
The fundamental theorem of calculus for L_h, [Hin26a, (5.77)], uses [[lem:iv5-0-4]] ([Hin26a, Lemma 3.5]) for the
future timelike covector ρ_sf a d(ρ_sf a). It gives the bulk term C𝔛ρ_sf⁴a² and the two positive δ-terms, hence
[Hin26a, (5.78)]. Adding [Hin26a, (5.76)] and (5.78) and absorbing for h small gives [Hin26a, (5.66)].

[Hin26a, (5.68)] follows by the same argument with a = ρ_K^(−α_K)e^(𝔛r)H(r − r_1), applied to χω (χ = 1 on r ≤ r_2,
0 on r ≥ r_3), as −dr is past timelike on [r_♯, r̂] ([[lem:iv5-0-3]] (c)). [Hin26a, (5.67) and (5.69)] are the same
arguments for P_h* = □_h* + iL_h*, whose damping acts backwards, as in [Hin26a].

[[eq:iv5-6-1]]. Run the proof of [Hin26a, (5.66)] at fixed h with a multiplied by H(τ). The boundary τ = 0 then adds to
[Hin26a, (5.74) and (5.77)] the terms of the boundary τ = T_0 with the opposite sign. Each is a quadratic form in
(ω, ∂_τω)|_(τ=0) with bounded coefficients in the 3b frame, so it is bounded by
C‖(ω, r𝓛_(∂_t)ω)|_(X_0)‖²_(ℋ_data). Here ∂_τ = r∂_t at fixed (r, ω), and the weight matches by [[lem:iv5-0-2]] (b):
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
[[prop:iv5-6-1]] are used, with ¾r_♯ for r_♯; they need only [[lem:iv5-0-3]] (c) and [[lem:iv5-0-4]], which hold for
every stationary past timelike extension of c, [[lem:iv5-0-3]] holding on {r ≥ ½r_♯}. [[prop:iv5-1-3]] needs only
[[lem:iv5-0-3]] (c) there. Moreover ω̃ = ω on Ω, by uniqueness of forward solutions: Σ^♯ is spacelike with future
timelike vectors pointing out, and X_0 is spacelike ([[lem:iv5-0-3]] (a), (c)). The microlocal estimates of
[[sec:iv5-1]]–[[sec:iv5-5]] hold for every s in the strong sense; near the zero section the order is irrelevant. They
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
H^(s,(α_sf,α_K))(Ω)^(•,−) and H^(−s,(−α_sf,−α_K))(Ω)^(−,•) ([Hin26a, Section 2.3]). So the Hahn–Banach theorem gives
ω ∈ H^(s,(α_sf,α_K))_(3b,h)(Ω)^(•,−) with P_hω = h²f and the bound [Hin26a, (5.18)]. *s > 0.* Higher regularity follows
by extension and restriction with the propagation estimates, as in [[prop:iv5-7-1]]. *Uniqueness*, for every
distribution ω on Ω supported in {t ≥ 0} with P_hω = 0, follows by the classical duality argument. For
φ ∈ C_c^∞(Ω°), the backward solution ψ of P_h*ψ = φ is smooth, with support in the causal past of supp φ. That set is
compact, since t decreases and |dr/dt| is bounded along causal curves. It is disjoint from Σ^♯: along past-directed
causal curves r increases inside {r ≤ r̂} ([[lem:iv5-0-3]] (c)), so r stays above min(min_(supp φ) r, r̂). Pairing the
extension of ω by zero across X_0 with ψ gives ⟨ω, φ⟩ = ⟨P_hω, ψ⟩ = 0.

(b) By [[lem:iv5-0-2]] (b) the data space is ℋ_data of [[eq:iv5-6-1]], with the density r⁴|dr d𝑔̸| that tensors with
dτ to |dg|; the shift ½ does not depend on the dimension ([Hin26a, p. 65]). *Smooth data.* Take f and data smooth with
compact support in Ω° ∪ X_0°. The initial value problem then has a solution ω smooth on Ω ∖ (K⁺ ∪ 𝗌𝖿), for the
following reasons. □^C_b has scalar principal symbol G Id ([[lem:iv5-0-2]] (d)). Every past-inextendible causal curve in
Ω° meets X_0: t decreases along it ([[lem:iv5-0-3]] (a)), r increases along it inside {r ≤ r̂} ([[lem:iv5-0-3]] (c)),
and |dr/dt| is bounded along causal curves, since g is a 3sc-metric. So the classical theory of the Cauchy problem for
linear wave equations with scalar principal symbol applies ([Hin26a, p. 42]). By finite speed of propagation, ω
vanishes on τ⁻¹([0, T_0]) near 𝗌𝖿, the speed being 1 + O(r⁻²) and T_0 < 1; so
ω ∈ ρ_sf^(α_sf)H̄²_3b(τ⁻¹([0, T_0])) and [[eq:iv5-6-1]] applies. Let χ = χ(τ) equal 1 for τ ≥ ½T_0 and 0 for
τ ≤ ¼T_0. Then P_h(χω) = h²χf + [P_h, χ]ω ∈ H^(0,(α_sf+2,α_K))(Ω)^(•,−), with norm bounded by ‖f‖ and by
‖ω‖_(ρ^(α_sf)H̄¹(τ⁻¹([0,T_0]))). By the uniqueness in (a), which holds for distributions, χω is the forward solution,
so it lies in H^(1,(α_sf,α_K)). Using [[eq:iv5-6-1]],

    ‖ω‖_(ρ_sf^(α_sf)ρ_K^(α_K)H̄¹_3b(Ω)) ≤ C(‖f‖ + ‖(ω, r𝓛_(∂_t)ω)|_(X_0)‖_(ℋ_data)).

*General data.* Approximate f and the data in their spaces by such smooth data. By this estimate the solutions converge
in ρ_sf^(α_sf)ρ_K^(α_K)H̄¹_3b(Ω). Near X_0 they also converge in
C([0, T_0]_τ; ρ_sf^(α_sf)H̄¹_b) ∩ C¹([0, T_0]_τ; ρ_sf^(α_sf)H̄⁰_b): the boundary term at τ = T of [Hin26a, (5.74) and
(5.77)], run at every T ∈ [0, T_0] in the proof of [[eq:iv5-6-1]], bounds the norm of (ω, ∂_τω)|_(τ=T) by the right
side of [[eq:iv5-6-1]]. So the limit takes the data and solves [[eq:iv5-5-16]]. For uniqueness, let
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
constant C and the margin of [Hin26a, Lemma 3.5] on compact sets) and [[lem:iv5-0-5]] (uniform by its statement); and
the cut-offs, commutants and the parameters 𝔛, δ, δ′, t_j, r_j, κ, chosen from these bounds alone, hence independently
of b. The calculus estimates used (composition, elliptic parametrices, the sharp Gårding inequality, L²-boundedness)
have constants depending on finitely many seminorms of the symbols involved, which depend continuously on b. Each
absorption step needs h below a threshold determined by these quantities. So each h_0 and C is uniform on U, after
shrinking U to a compact neighbourhood. ∎

### The transition face model {#sec:iv6}

This section proves that □^C_b is tf-admissible with every weight in [−C_0, 2) ([[thm:iii-e-1-1]] (4)), through
[Hin26a, Theorem B.1] in dimension 4 + 1 ([[thm:iv6-3-1]]): the invertibility of the spectral family of the
dilation-invariant model on 4 + 1 Minkowski space, which is the transition face normal operator of □^C_b. The proof has
three steps, as in [Hin26a, Appendix B, pp. 85–98]: the Fredholm property and index 0 ([[sec:iv6-1]]), by radial
estimates and Melrose's relative index theorem, sector by sector on 𝕊³; solvability on edge-b spaces
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

(ii) r^μ lies in r^β L²(r³ dr) near r = 0 iff μ > β − 2. So if the indicial roots of (□^C)^(0) in ρ at infinity avoid
[−C_0, 2), those in r at the origin, which are their negatives, avoid (−2, C_0], and the root-free weights at the origin
are β ∈ (0, 2 + C_0].

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
r^(2μ−2β)r³ dr < ∞ iff 2μ − 2β + 4 > 0. By (i) and the inversion ρ = r⁻¹, the indicial roots at the origin are the
negatives of those at infinity. (iii) The first statement is [[prop:np-10-14]] (iv) with b_sf − b_K = d. For the
second, with ζ = dr/r, ⟨c, ζ⟩ = −v r⁻², G(c) = −(1 − v²)r⁻², G(ζ) = r⁻²; by [[prop:np-10-13]] (i), ½ℓ(ζ) has eigenvalue
−vr⁻² three times and on span{c, ζ} trace −(3 − e)vr⁻² and determinant (2(1 − e)v² − e(1 − v²))r⁻⁴; multiplying by −r²
gives (ν − v)³(ν² − (3 − e)vν + (2 − e)v² − e). At (1/2, 1/102400) the quadratic has positive sum (3 − e)/2 and
positive product (2 − e)/4 − e; at e = 0 its roots are v and 2v. (iv) is arithmetic, with b* ∈ (0.9934, 0.9935) and dt
= r dτ + τ dr. (v) On stationary sections □_η = −Δ componentwise in the frame dt, dx^i. A section of scalar type l has
its dt-component r^μS, with −Δ(r^μS) = 0 at leading order iff μ ∈ {l, −l − 2}, and its spatial part a 1-form whose
Cartesian components are, at each order r^μ, combinations of harmonics of degree l ± 1 (for l = 0, of degree 1 only),
with the roots μ ∈ {l − 1, −l − 1} and {l + 1, −l − 3}; a section of vector type has Cartesian components of degree l,
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
R_in := {ξ = 2σ, η = 0}, and for Im σ > 0 the characteristic set over ρ = 0 is R_out ([Hin26a, (B.15)–(B.18)], free of
the dimension).

**Definition {#def:iv6-0-2}** (Admissible orders; [Hin26a, (B.13)] in dimension 4 + 1.) (s, ℓ, β) is *admissible at σ*
if β ∈ (0, 2 + C_0], ℓ < −½ + h⁻¹(1 − e)(1 − v) at R_out, and, when σ = ±1, ℓ > −½ − h⁻¹(1 − e)(1 + v) at R_in, with ℓ
constant near R_in and R_out and non-increasing along σH_(G_σ).

#### Fredholm property and index 0 {#sec:iv6-1}

**Proposition {#prop:iv6-1-1}** ([Hin26a, Proposition B.2] in dimension 4 + 1.) For (s, ℓ, β) admissible at
σ ∈ e^(i[0,π]),

    (□^C)^(σ) : {ω ∈ H^(s,(ℓ,β))_(sc,b) : (□^C)^(σ)ω ∈ H^(s−2,(ℓ+1,β−2))_(sc,b)}
                  → H^(s−2,(ℓ+1,β−2))_(sc,b)                                                             {#eq:iv6-1-1}

is Fredholm of index 0, and its nullspace and the annihilator of its range do not depend on the admissible (s, ℓ, β).
The estimate

    ‖ω‖_(H^(s,(ℓ,β))_(sc,b)) ≤ C(‖(□^C)^(σ)ω‖_(H^(s−2,(ℓ+1,β−2))_(sc,b)) + ‖ω‖_(H^(s_0,(ℓ_0,β_0))_(sc,b)))  {#eq:iv6-1-2}

(for admissible s_0 < s, ℓ_0 < ℓ, β_0 < β, in the strong sense) and its dual ([Hin26a, (B.28)]) hold uniformly for σ in
e^(i[0,π−δ]) near 1 and in e^(i[δ,π]) near −1, for fixed orders admissible there.

*Proof.* *Real σ*, say σ = 1 (σ = −1 by reversing the propagation). Off the characteristic set the operator is elliptic,
by [[lem:iv6-0-1]] (c). Over ρ = 0:

- *Sink R_out.* With the commutant [Hin26a, (B.21)], a = ρ^(−ℓ−½)χ_0(ρ)χ₁(|η|²)χ₂(ξ), the principal symbol of
(i/2)[(□^C)^(σ), A²] is [Hin26a, (B.23)]. That of (2i)⁻¹((□^C)^(σ) − (□^C)^(σ)*)A² adds at the zero section the shift
[Hin26a, (B.24)]. By [[lem:iv6-0-1]] the shift comes only from −2iσρh⁻¹S̄: (□^C)^(0) − (□^C)^(0)* ∈ ρ²Diff¹_b, whose
quotient by ρ has scattering symbol vanishing at (ξ, η) = 0; and 2iσ(ρ²∂_ρ − (3/2)ρ) is symmetric on L²(ρ⁻⁴dρ/ρ)
([[lem:iv6-0-1]] (b)), so its imaginary part lies in ρ²C^∞ for any fibre inner product. Taking the fibre inner product
for which an eigenbasis of S̄ is orthonormal ([[lem:iv6-0-1]] (b)), the shift is −2h⁻¹S̄, which gives [Hin26a, (B.25)].
The main term (2ℓ + 1)(σ − ξ) − 2h⁻¹S̄ is negative near the zero section iff
ℓ < −½ + h⁻¹ min spec S̄ = −½ + h⁻¹(1 − e)(1 − v); this is [Hin26a, (B.26)].

- *The incoming radial set R_in.* The isometry t ↦ −t of η pulls c_v := r⁻¹(dt − v dr) back to −c_(−v), so it
conjugates □^C with (c_v, h⁻¹) to the operator with (c_(−v), −h⁻¹) ([[prop:np-10-21]] (ii)). On stationary sections,
e^(2iσr)(□^C)^(σ)e^(−2iσr) is the pullback of the spectral family at −σ of that operator, by the identity after
[Hin26a, (B.27)], which is free of the dimension. With an eigenbasis of S̄_(−v) orthonormal, the shift at R_in is
(−1)(−2(−h⁻¹)S̄_(−v)). S̄_(−v) has spectrum {2(1 + v), (1 − e)(1 + v), 1 + v}, with bottom (1 − e)(1 + v). The
threshold is ℓ > −½ − h⁻¹(1 − e)(1 + v).

- In between, real principal type propagation applies along Char_σ, which flows from R_in to R_out by [Hin26a, (B.16)].

The regularisation argument gives the strong form, and this proves [Hin26a, (B.20)], whose error term carries the
b-weight β. Near r = 0 the operator r²(□^C)^(σ) is b-elliptic ([[lem:iv6-0-1]] (c)), with Mellin transformed normal
operator that of r²(□^C)^(0). By (a) and the inversion ρ = r⁻¹, its indicial roots at r = 0 are −μ, with μ running over
those of [[lem:iv4-1-3]] at infinity. These have Re μ ∉ [−100, 19/10], and only μ = 2 in [−100, 2]. So no root at 0 has
real part in (−2, 100], and the b-weight β − 2 ∈ (−2, C_0] is root-free. With [β_0 − 2, β − 2] root-free as well, the
inverse Mellin transform of the normal operator gives [[eq:iv6-1-2]] from [Hin26a, (B.20)] ([[lem:s14-tf-inputs]]
(ii); [Hin26a, p. 89]). The dual estimate is the same with the propagation reversed.

*Complex σ.* Only R_out is characteristic. Write σ⁻¹(□^C)^(σ) = P − iQ as in [Hin26a, (B.29)], with Q_0 = 2ρh⁻¹S̄,
P_1 = Re 2i(ρ²∂_ρ − (3/2)ρ), and Q_3 = (Im σ)Re (□^C)^(0) a nonnegative absorption. With the same commutant, the
zero-section symbol is (2ℓ + 1 − 2h⁻¹S̄)ρ^(−2ℓ). −AQ_3A has the sign of the main term, because the b-principal symbol of
(□^C)^(0) is ξ_b² + |η_b|², so (□^C)^(0) = Σ_jT_j*T_j + R with T_j ∈ ρDiff¹_b and R ∈ ρ²Diff¹_b. The rest is
subprincipal or elliptic ([Hin26a, p. 90]). *Uniformity* in σ near ±1 is the limiting absorption principle: the full
Hamilton field on the cut-offs keeps the sign structure of [Hin26a, (B.23)] ([Hin26a, p. 91]).

So [[eq:iv6-1-1]] is Fredholm, and by [[eq:iv6-1-2]] and elliptic and propagation regularity its nullspace consists of
elements in every admissible space; it is the same for every admissible (s, ℓ, β). The annihilator of the range is the
nullspace of the adjoint on the dual spaces; by the dual estimate and the propagation regularity of the adjoint it too
consists of elements of every dual space, so it does not depend on the orders either, as in the proof of
[[thm:i-c-4-3]] (3). Hence the index does not depend on the admissible orders.

*Index 0.* (□^C)^(σ) commutes with the rotations of 𝕊³, and with the dilations up to the factor of (a). Decompose
sections of 𝒯*_X by harmonics on 𝕊³ ([[ch:s11]]): scalar type of degree l ≥ 0 (three components for l ≥ 1, the dt, dr
and gradient parts; two for l = 0), and vector type of degree l ≥ 1 (one component, the co-closed 1-forms on 𝕊³). The
projections onto a type and degree are bounded on the spaces with rotation-invariant orders (the proof of
[[prop:i-c-5-3]]), and (□^C)^(σ) commutes with them. So [[eq:iv6-1-1]] is the direct sum of its restrictions to the
sectors. Each restriction is Fredholm, and only finitely many have nonzero kernel or cokernel. Fix a sector and write I
for its index on [[eq:iv6-1-1]], with ℓ a variable order > −½ at R_in and < −½ at R_out. Take for ℓ the order of
[[ch:s03]] for the free operator at this σ = e^(iθ): that of [[lem:i-a-7-1]] with θ_in = 0 and S̄ = 0 for θ ∈ {0, π},
or r_mid for θ ∈ (0, π). It is invariant under the rotations of 𝕊³, > −½ at R_in and < −½ at R_out, so it is admissible
for every h⁻¹ ≥ 0; as the index does not depend on the admissible orders, I is the index of the sector for all of them.

(i) *Lowering β.* In the sector, (□^C)^(0) has finitely many indicial roots at r = 0, continuous in
h⁻¹ ∈ [0, h_f⁻¹], h_f ∈ (0, 10⁻⁶] the value at hand ([[eq:iv6-0-2]]: they are the roots of the sector's indicial
polynomial, whose coefficients are polynomial in h⁻¹ with leading coefficient free of it). Fix β₁ below all of them for
all such h⁻¹. Moving the weight from β to β₁ raises the index by the number of roots, with multiplicity, whose real
part lies in [β₁ − 2, β − 2). This is Melrose's relative index theorem [Mel93, Theorem 6.5], a theorem on b-operators
in every dimension ([Hin26a, p. 91]). These are the roots −μ with Re μ ≥ 2: two in the scalar sector l = 0, three in
each scalar sector l ≥ 1, one in each vector sector ([[lem:iv4-1-3]] (a)). The index becomes I + j, with j = 2, 3, 1.

(ii) *Removing the damping.* Deform h⁻¹ to 0 at the weight β₁. The family is continuous in operator norm between the
fixed spaces, as the h⁻¹-terms (2iσρh⁻¹S̄, and the first-order part h⁻¹ρ²Q̃ of (□^C)^(0) from L_h) map H^(s,(ℓ,β₁))
boundedly to H^(s−2,(ℓ+1,β₁−2)). It stays Fredholm, by the estimates above, whose thresholds hold for every h⁻¹ ≥ 0
with this ℓ and whose weight β₁ stays root-free. So the index I + j is kept at h⁻¹ = 0. There the operator is
2δ_ηG_ηδ*_η = □_η on 1-forms (Ric(η) = 0, [[lem:s14-box-c]]), acting componentwise in the frame dt, dx^i.

(iii) *Raising β for the free operator.* Its roots at r = 0 are those of [[lem:s14-tf-inputs]] (v), and the window
between the groups contains (−2, 0). Raising β₁ to β₂ with β₂ − 2 ∈ (−2, 0) crosses 2, 3 or 1 roots and lowers the
index by as many, to I. On these spaces (□_η)^(σ) is invertible: it is N_tf of the free operator, which is
tf-admissible with every weight in (0, 2) ([[prop:i-c-5-3]], whose data are those of □_η componentwise). By
[[cor:i-c-5-2]] (a) it is invertible on the spaces of [[sec:i-c-4]] with q ∈ (0, 2), the free gap being (0, 2), and
these are the spaces here with β = q and ℓ the order fixed above ([[sec:iv6-4]]); take β₂ := q. So I = 0 in every
sector, and the index of [[eq:iv6-1-1]] is 0. ∎

#### Solvability on edge-b spaces {#sec:iv6-2}

On M the edge-b vector fields are spanned by r∂_t, r∂_(x^i). Unit cells
(2^j(k − 2), 2^j(k + 2))_t × (2^(j−2), 2^(j+2))_r × U̸_β, with U̸_β charts of 𝕊³, give the parameterised scaled bounded
geometry ([[prop:np-10-65-a]]). On it P_h := h²□^C = □_h − iL_h ∈ r⁻²Diff²_(eb,ħ)(M; 𝒯*) has principal symbol G − iℓ
([[lem:iv5-0-2]] (d) on the model). H^(s,(α_sf,α_cf))_(eb,h) is weighted with L²(|dg|),
|dg| = |dt dx| = r⁴|dt (dr/r) d𝑔̸|, and the fibre inner product B of [[lem:iv5-0-4]]. Let Ω := {t ≥ 0},
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
[[prop:iv5-6-1]] ([Hin26a, Lemma 5.14 and Corollary 5.15], stated in every dimension, with charts on 𝕊³ and the
level-set density r⁴|dr d𝑔̸|) gives [Hin26a, (B.34) and (B.35)] at T := ½, with ρ_sf = (1 + r)⁻¹ and
ρ_cf = r(1 + r)⁻¹ there.

*Nonzero and infinite frequencies.* [Hin26a, (B.37)] is [[prop:iv5-1-3]] with the cut-offs χ_j(τ) of
[Hin26a, (B.36)] and no cut-off in r. There is no E_r term; the E_τ term is a negative square because ±H_Gτ > 0 at
future, resp. past, lightlike covectors, dτ being past timelike on supp χ₁′.

*The cone face 𝖼𝖿.* Use 𝓛_h := −i(1 + iCL_h*r²)P_h = −L_h + J − iQ as in [[eq:iv5-2-1]], with r⁻¹ for ρ_sf. In
t ≥ −r/2 let ρ_sf := (t + r + 1)⁻¹ and ρ_cf := r(t + r + 1)⁻¹. Take the commutant
a = w⁻¹χ_cf(𝔛ρ_cf)χ_0(𝔛|ζ|)χ₁(t/r), w := ρ_sf^(α_sf+1)ρ_cf^(α_cf−1). The symbol identity is [Hin26a, (B.38)]:
aH_(−ℓ+j)a − Sa² = −c_0r⁻²a² − b_0² − b_cf² + e_τ² + f. Since dw/w ≡ (α_cf − 1)dr/r modulo
ρ_cf C^∞(M; ^(eb)T*M), the square roots exist for the following reasons.

- b_0: r²(−ℓ(dw/w) + S) at ρ_cf = 0 is the T of [[prop:np-10-14]] (iv) at ρ_K = 0 with d = 1 − α_cf. It is positive
definite iff d < b*, that is α_cf > 1 − b* ([[lem:s14-tf-inputs]] (iii)). Positivity extends to supp a for 𝔛 large,
and w⁻¹H_jw vanishes at o.

- b_cf: −½r²ℓ(dr/r) has the characteristic polynomial of [[lem:s14-tf-inputs]] (iii), with positive roots at
(v, e) = (1/2, 1/102400). It is B-self-adjoint ([[lem:iv5-0-4]]), so it is B-positive definite. Moreover
dρ_cf/ρ_cf ≡ dr/r modulo ρ_cf, and −χ_cfχ_cf′ ≥ 0.

- e_τ: d(t/r) is past timelike on supp χ₁′, so r²ℓ(d(t/r)) is negative definite ([[lem:iv5-0-4]]).

- f is elliptic.

This gives [Hin26a, (B.39)], whose a priori term lies in τ ≤ (2.75/10)T, covered by [Hin26a, (B.34)]; and
[Hin26a, (B.40)] for P_h* likewise.

*The other zero-section estimates.* The model is stationary and dilation invariant ([[lem:iv6-0-1]] (a)). So each
rescaled symbol of the commutator arguments at a point of Ω°, such as r²ℓ(d(r/t)) or r²S, is a function of s := r/t and
ω; the derivatives of the weights enter only through bounded terms, which the escape terms dominate. The 1-form is the
Minkowski model's, for which [[lem:iv5-0-5]] (4)–(6) hold at 𝗌𝖿 ([[prop:np-10-14]] (iv)–(v)). At s → 0,
−r²ℓ(ds) = 2s(−½r²ℓ(dr/r)) + O(s²) is positive by the b_cf positivity, so δ_r may be shrunk. Fix δ_r > 0 so small that
the b_0 positivity at 𝖼𝖿 holds on {ρ_cf ≤ 4δ_r} (it is constant along 𝖼𝖿, and 𝖼𝖿 ∩ Ω is a product [0, ∞]_t × 𝕊³ up to
the dilations), and that (6) holds on 𝗌𝖿 ∩ {s ∈ [δ_r, v(1 − δ_sf)]}. Then:

(a) [Hin26a, (B.39) and (B.40)] hold on {ρ_cf ≤ 4δ_r} ∩ {τ ≥ T/40}, globally in t, with a priori sets in
{τ ≤ (2.75/10)T} and in {(5/2)δ_r ≤ ρ_cf ≤ 4δ_r} respectively.

(b) [[prop:iv5-5-2]] (b)–(c) hold with s = r/t near 𝗌𝖿 on [δ_r, v(1 − δ_sf)] and [v(1 + δ_sf), 10], and
[[prop:iv5-4-1]] at the sink s = v (with α_sf < b* − 1), by their proofs, which use only these signs. For η,
⟨c, ds⟩ = (s − v)/(rt), so the flow of −rc♯ moves s towards v from both sides.

(c) [[prop:iv5-5-3]] (1)–(2) hold on compact subsets of Ω ∩ {ρ_cf ≥ 2δ_r}, with the escape functions t + κr and t and
the cut-off t − κr (d(t − βr) is past timelike for |β| < 1 on η). The cut-off χ_r(r) at Σ^♯ is replaced by
f(ρ_cf/(2δ_r)), with f non-decreasing, 0 near [0, ½] and 1 on [1, ∞). Its term is f′·(−ℓ(dρ_cf))/(2δ_r) ≥ 0, as
−ℓ(dρ_cf) > 0 near 𝖼𝖿 (dρ_cf/ρ_cf ≡ dr/r, the b_cf positivity). So it needs a priori control on
{δ_r ≤ ρ_cf ≤ 2δ_r} in the forward direction and has the sign of the main term in the adjoint one.

*Combination.* *Forward*: [Hin26a, (B.34)] on {τ ≤ ½} and [Hin26a, (B.37)]; (a) forward; (c) (1) on every compact
subset of Ω ∩ {ρ_cf ≥ 2δ_r}, from [Hin26a, (B.34)] and (a), with ε_X ≤ δ_rT so that its set {½ε_X ≤ t ≤ ε_X} lies
under [Hin26a, (B.34)], as τ ≤ ε_X/δ_r on {ρ_cf ≥ δ_r}; (b) along 𝗌𝖿 from s ∈ [2δ_r, 3δ_r] (by (a), as
ρ_cf = s/(1 + s) + O(ρ_sf) near 𝗌𝖿) and from s ∈ [5, 10] (by [Hin26a, (B.34)]), their interior a priori sets by (c);
and the sink, its a priori sets by (b) and (c). These cover a neighbourhood of o over Ω: near 𝖼𝖿 by (a) and
[Hin26a, (B.34)], near 𝗌𝖿 by (a), (b), the sink and [Hin26a, (B.34)], and the compact rest by (c). This gives
[Hin26a, (B.41)] at the Sobolev order 1, and at every order ≥ 1 by extension and restriction. *Adjoint*: the sink,
which has no a priori term; (b) (2) outward along 𝗌𝖿, the 𝗌𝖿-cut-off terms having the good sign; (c) (2) on compact
subsets of Ω ∩ {ρ_cf ≥ 2δ_r} ∩ {τ > κ}, the set of [[prop:iv5-7-2]] (viii) (t − κr > 0; there t ≥ 2t_1 once
t_1 < δ_r/9, as ρ_cf ≥ 2δ_r gives r ≥ 2δ_r), which contains the a priori set of [Hin26a, (B.40)], its χ₂(τ) being
supported in τ ≥ (2.25/10)T > κ; its late set (large t, r ≤ (t + c₁)/κ, ρ_cf ≥ δ_r) lies near 𝗌𝖿 with s ∈ [δ_r, 10], by
κ = 1/9, covered by the previous two steps; (a) adjoint, that is [Hin26a, (B.40)], its a priori set
{(5/2)δ_r ≤ ρ_cf ≤ 4δ_r} covered by (c) (2) and, near 𝗌𝖿, by (b) (2); and [Hin26a, (B.35)], its a priori set
τ⁻¹([T/2, T]) covered by the steps before. Each step's a priori set lies in the controlled set of an earlier step, as in
[[prop:iv5-7-1]] and [[prop:iv5-7-2]]. Duality, extension and restriction, and the initial value problem are the
arguments of [[thm:iv5-7-3]] with these estimates. The data weights in [[eq:iv6-2-1]] follow because
|dg| = r⁴|dt (dr/r) d𝑔̸| = r|dτ| ⊗ r³|dr d𝑔̸| on {t/r ∈ I}, so the weights shift by ½ at both faces
([[lem:s14-tf-inputs]] (iv)).

*Strong uniqueness.* By finite speed of propagation for wave equations with smooth coefficients in {r > 0}, a solution
vanishing on {t ≤ 0} vanishes on {0 ≤ t ≤ 1, r > t}. On Ω′ := cl{0 ≤ t ≤ 1, r ≤ 1 − t} the a priori estimate
‖ω‖_(ρ_cf^(α_cf)H^s_(eb,h)(Ω′)^(•,−)) ≤ Ch⁻¹‖P_hω‖_(ρ_cf^(α_cf−2)H^(s−1)_(eb,h)(Ω′)^(•,−)) holds. It is proved by the
energy estimates near X_0 and near the final surface {r = 1 − t} (spacelike, with d(1 − t − r) past timelike;
localisation in (t − 1)/r), together with [Hin26a, (B.37) and (B.39)]. So a solution with zero forcing that is supported
in {t ≥ 0} and lies in that space vanishes on Ω′, hence on {0 ≤ t ≤ ½}. Translating in t, which commutes with □^C, and
iterating gives vanishing for all t. ∎

#### The kernel and [Hin26a, Theorem B.1] in dimension 4 + 1 {#sec:iv6-3}

**Theorem {#thm:iv6-3-1}** ([Hin26a, Theorem B.1] in dimension 4 + 1.) There is h_tf > 0 such that for h ∈ (0, h_tf),
every σ ∈ e^(i[0,π]) and every (s, ℓ, β) admissible at σ, the map [[eq:iv6-1-1]] is invertible, with inverse bounded
uniformly for σ in each sector where fixed orders are admissible ([[prop:iv6-1-1]]).

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
α_K > α_sf + 1 − b* ([[lem:iv4-1-4]]; [[prop:np-10-22]] (iv)), allows, and with C_0 + 1 for C_0, as in
[Hin26a, p. 67].

*(1).* Let ω′ ∈ 𝒜^γ(X̄; E) with (□^C_b)^(σ)ω′ = 0, and ω := e^(−iσt_*)ω′, a solution of □^C_bω = 0. It is outgoing in
the sense of [Hin26a, Definition 6.1]: t_* = t − ψ(|x|) with ψ(r) = r − C_ψ + 8m₀r⁻¹ for large r ([[eq:iii-b-3-6]]), and
the tortoise coordinate of g_(b₀) is r_* = r − m₀r⁻¹ + O(r⁻³) (dr_*/dr = (1 − m₀r⁻²)⁻¹), so
ω = e^(−iσt)e^(iσr_*)ω₁ with ω₁ = e^(iσ(ψ−r_*))ω′ ∈ 𝒜^γ, ψ − r_* being bounded and conormal. By [[eq:iv4-1-1]],

    2iσρ(ρ∂_ρ − 3/2 − S̄^C)ω′ ∈ (ρ²Diff²_b + σρ³Diff¹_b + σ²ρ²Diff⁰_b)ω′ ⊂ 𝒜^(γ+2),

the term ρS̃ of [[eq:iv4-1-1]] included in the first class. Dividing by 2iσρ and solving the regular-singular equation
in ρ gives ω′ ∈ 𝒜^(γ+1) as long as γ + 1 < 3/2 + min spec S̄^C; iterating, ω′ ∈ 𝒜¹, as S̄^C > 0 ([[lem:iv4-1-2]]).
[[thm:iv5-7-3]] is applied in the Kerr–Schild coordinates of [[sec:iv5-0]] ([[rem:iv5-7-4]]), in which
t = t_KS + T_m(|x|) ([[sec:iii-b-3-1]]). The data
(ω, r𝓛_(∂_t)ω)|_(t_KS=0) = (e^(iσ(ψ−T_m))ω′, −iσre^(iσ(ψ−T_m))ω′) satisfy |ω^(0)| ≤ Cr⁻¹,
|(r∂_r, ∂_ω)ω^(0)| ≤ C (the phase contributes σr, and ω′ ∈ 𝒜¹ is conormal) and |ω^(1)| ≤ C. Indeed
|e^(iσ(ψ−T_m))| = e^(−(Im σ)(ψ−T_m)) is bounded, ψ − T_m being continuous on [r_♯, ∞) and tending to +∞. So the data
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
ϱ₁ > C_0 + 2 is the least real part of an indicial root of (P^C_b)* above C_0 + 2, which exists as the roots are discrete
([[lem:iv4-1-3]] (a)); the roots of real part ≤ 0 are below the weight. So ω′(t, x) := v(x) is a stationary solution of
(□^C_b)*ω′ = 0. Put α′_sf := −C_0 − 3/2, the weight [[eq:iv4-2-1]] at C_0 − 1. A stationary function of pointwise decay
ρ^k lies in ρ^aρ_K⁻¹L²(Ω, |dg|) near ∂X iff k > a + 5/2: the shift is 2 for ρ^aL²(r³dr) ([[prop:np-10-21]] (iii)),
plus ½ from ∫_0^∞ρ_K²dt = ∫_0^∞(r/(t + r))²dt = r. At a = −α′_sf − 2 = C_0 − ½ this asks k > C_0 + 2, which
k ∈ (C_0 + 2, ϱ₁) meets. So ω′ ∈ ρ_sf^(−α′_sf−2)ρ_K^(−α_K)H^(s′)_3b(Ω)^(−,•) for s′ = 1 − s near ∂X. The adjoint estimate
[[eq:iv5-5-81]] at the weights (α′_sf, α_K), which satisfy its hypotheses by [[lem:iv4-1-4]] at C_0 − 1, holds for
h < h_* and makes (□^C_b)* injective there, so v = 0. (At the weight [[eq:iv4-2-1]] itself the membership would ask
k > C_0 + 3, which [[lem:iv4-1-3]] does not give at C_0 = 100; this is why h_* is below the threshold of
[[thm:iv5-7-3]] at C_0 − 1 as well.) So P^C_b is surjective, hence invertible, and by [[thm:i-c-3-1]] (4) the estimates
hold without the error terms. ∎

*Remark.* [Hin26a] has two further routes to the surjectivity: the index 0 from [Hin26a, Theorem B.1] with
[[cor:i-c-6-6]], and the radial ordinary differential operators of a static metric with [Hin26a, Theorem 4.9 (3)]. They
are not used: the first needs the tf-admissibility and the index at σ ≠ 0, the second an index count for operators that
are singular at the horizon. The route through the adjoint estimate needs only what the proof of [[thm:iv5-7-3]]
provides.

### tf-admissibility {#sec:iv6-4}

**Theorem {#thm:iv6-4-1}** ([[thm:iii-e-1-1]] (4).) For b near b₀, h ∈ (0, min(h_*, h_tf)) and C_0 ∈ [3/2, 100], □^C_b
is tf-admissible ([[def:i-c-5-1]]) with every weight β_tf ∈ [−C_0, 2).

*Proof.* We check (i)–(iii) of [[def:i-c-5-1]].

(i) By [[lem:iv4-1-6]], (β_−, 2) with β_− < −100 ≤ −C_0 is an indicial gap of (□^C_b)^(0), and it contains β_tf.

*The spaces.* Put q := 2 − β_tf ∈ (0, 2 + C_0]. The spaces of [[sec:i-c-4]] are the H^(s,(𝗋+α₊,q))_(sc,b)(tf) of
[[def:i-c-4-1]], normed with the Euclidean density |dx̂| near both ends. These are the spaces H^(s,(ℓ,β))_(sc,b) of
[[sec:iv6-0]] with ℓ := 𝗋 + α₊ and β := q: X is tf, ρ_sc and ρ_b are ρ_sctf and ρ_ztf, and the density is r³|dr d𝑔̸| in
both. The map 𝒳_(tf,θ) → 𝒴_(tf,θ) of [[sec:i-c-4]] is then [[eq:iv6-1-1]] at σ = e^(iθ), by [[lem:iv6-0-1]] (d).
These orders are admissible in the sense of [[def:iv6-0-2]]: q = β ∈ (0, 2 + C_0]; the orders 𝗋_± with weight α₊ are
those of [[lem:i-a-7-1]] at σ_* = ±1, constant near the radial sets and monotone along the flow, functions of ξ and
|η|²; and their thresholds are those of [[sec:i-a-1]] for (□^C_b)^, which are the data of □^C_b at ρ = 0
([[sec:i-c-4]]): −½ + min spec S̄^C at R_out, and at R_in the bound −½ − S_in with S_in = h⁻¹(1 − e)(1 + v)
([[prop:np-10-21]] (ii)). These are the thresholds of [[def:iv6-0-2]].

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

(b) *Vanishing inside the horizon.* On {r_0 < |x| < r_h} the Killing field ∂_(t_*) is spacelike, so the quotient metric
is Lorentzian with |x| timelike, and on stationary sections (P^C_b)* is a wave operator in the time −|x| there. An
element of its kernel, or a solution with a forcing supported in {|x| > r_h}, that lies in a Ḣ space vanishes, extended
by zero, on {|x| < r_0} (the supported character), and so on {r_0 < |x| < r_h} by uniqueness for the Cauchy problem on
the spacelike hypersurfaces {|x| = c}, c < r_h, run from {|x| < r_0} across {|x| = r_0}, where the operator is still
hyperbolic in |x|.

**Proposition {#prop:np-10-31}** (The adjoint's indicial values and the translations on Tangherlini space.) On
4 + 1 Minkowski space, with the notation of [[prop:np-10-12]]:

(i) for every type and degree, the indicial polynomial of the adjoint at ι equals that of □^C at 2 − ῑ; at vector type
l = 1 (κ = 3) the roots of □^C are 3 and −1 − 2vγ_C, those of the adjoint −1 and 3 + 2vγ_C, and the indicial value of
the adjoint at 2 is N_(v,1)(0) = 3(1 + 2v_Cγ_C);

(ii) on Tangherlini space, with S ∈ 𝒮₁ a linear function, (□^C)*(dS) ∈ ρ⁴C^∞ near ∂X, so that
(□^C)*(χ dS) ∈ C_c^∞ + ρ⁴C^∞, and the correction ρ²(A S dt + B S dr + C r dS) that cancels its ρ⁴ term is unique, 2
being no root of the adjoint at scalar type 1.

*Proof.* (i) The first statement is [[lem:iii-e-2-1]] (2). At κ = 3, p_(v)(ι) = −hι² + (2h − 2v)ι + 3h + 6v vanishes at
ι = 3, and the product of its roots is −(3h + 6v)/h, so the other root is −1 − 2v/h. The adjoint's are 2 − 3 = −1 and
2 − (−1 − 2v/h) = 3 + 2vγ_C, and N_(v,1)(2 − 2) = h⁻¹p_(v)(0) = 3 + 6v/h.

(ii) dS is parallel for η, so δ*_η dS = 0 and (□^C_η)*(dS) = 0; on Tangherlini space δ*_g dS = −(Γ_g − Γ_η)·dS has
coefficients in mρ³C^∞ by [[prop:np-10-22]] (i), and (δ*_(g,E_C))*G_g ∈ ρDiff¹_b near ∂X, so (□^C)*(dS) ∈ ρ⁴C^∞. The
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
vanish on {r_0 < |x| < r_h} ([[sec:iii-e-2]], (b)).

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

*Remarks.* (a) *Counting.* At A = 0 the dual states are one for the time translation, four for the translations and six
for the rotations: eleven, against seven (1 + 3 + 3) in dimension 3 + 1. The h* of the time translation and of the six
rotations decay to the weight C_0 + 3, and those of the four translations begin at ρ³; that their ρ³ coefficient is
nonzero on Tangherlini space is [[pending:computational-4]]. (b) The memberships can be improved to full
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
for c ∈ C^∞(∂X; T*X|_(∂X)). For 3 ≤ j ≤ J, N(ρ⁻²P*, j) is invertible on C^∞(∂X), since the indicial roots of P* are 0,
have negative real part, or have real part > C_0 + 2 ≥ J ([[lem:iii-e-2-1]] (2)), and it is elliptic (the ellipticity
hypothesis (E2) of [[ch:s11]]). Removing in turn, for j = 3, …, J, the coefficient of ρ^(j+2) of the current remainder
by ρ^jc_j(W), c_j(W) := −N(ρ⁻²P*, j)⁻¹ applied to that coefficient, gives ω′♯₁(W) := Σ_(j=3)^J ρ^jc_j(W), linear in W
and smooth in b, with

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

*Remark.* [Hin26, (7.31) and (7.18)] are the counterparts in dimension 3 + 1 of c_0|x|⁻³V(W) and
[[eq:iii-e1-3-3]]: with m ↔ 2m_K (the mass enters as m|x|⁻² where the Kerr mass m_K of [Hin26] enters as 2m_K|x|⁻¹), ρ³ ↔ ρ² and the
bracket for the cross product, the same coefficients 1 + 2(v_C ∓ 1)γ_C over 1 + 2v_Cγ_C appear, up to the orientation
convention of the spin, and the indicial value 3(1 + 2v_Cγ_C) replaces 2 + 4γ_Cv_C. In [Hin26] the term
ρS(a)S′dr + ½d̸(S(a)S′) of the ansatz cancels the pure gauge term of [Hin26, (7.20)]; here there is none to cancel.

### Simplicity of the roots and their distance from the integers {#sec:s14-simple}

The indicial roots of the linearised gauge-fixed Einstein operator, studied in [[ch:s15]], are made of the roots of
□^C shifted by −1, the roots of the gauge potential operator of [[ch:s13]] shifted by +1, and the roots of the physical
part. This section proves the two properties of the roots of □^C and of the explicit polynomials of [[ch:s13]] that
[[ch:s15]] uses for every degree l ≥ 2: simplicity, and a positive distance of the real parts from the integers, the
condition [Hin26, (8.13)]. Throughout, (v, e) = (1/2, 1/102400), and

    z := 4e_Υγ_Υ² = 4·10⁻⁶,     Q_l(ι′) := s² − (2 + 2κ + z)s + κ(κ + 1) + zκ,  s := ι′(ι′ − 1),  κ = l(l + 2),

where (e_Υ, γ_Υ) = (1/100, 1/100) are the constants of the gauge modification of [[ch:s13]]. For l ≥ 2 let ℛ^sc_l be the
list of the numbers −l, l + 2, 2 − l, l + 4, the four roots of ι ↦ Q_l(ι − 1), and ι − 1 for the six roots ι of P_l;
let ℛ^v_l be the list of −l, l + 2, 1 − l, l + 3 and ι − 1 for the two roots ι of p_(v); and let ℛ^t_l be the list
−l, l + 2. These are the indicial roots of that operator at scalar, vector and tensor type l ≥ 2 ([[ch:s15]]).

**Proposition {#prop:np-10-52}** (Simplicity and [Hin26, (8.13)] for every l.) (i) For l ≥ 2 put u := l + 1. The four
roots of Q_l(ι − 1) are real and equal to l + 3 + d₁, −l − d₁, l + 2 + d₂ and 1 − l − d₂, where

    d₁ := ½((2u + 1)² + 2z + 4w)^(1/2) − ½(2u + 1),     d₂ := ½((2u − 1)² + 2z − 4w)^(1/2) − ½(2u − 1),
    w := (u² + z + z²/4)^(1/2) − u;

and d₁ = z(u + 1)(1 + θ₁)/(2u(2u + 1)), d₂ = z(u − 1)(1 + θ₂)/(2u(2u − 1)) with |θ₁|, |θ₂| ≤ z. In particular
0 < d₂ < d₁ < 1, and none of these roots is an integer.

(ii) There is a countable set 𝖹′ ⊂ (0, 10⁻⁶] such that for h ∈ (0, 10⁻⁶] ∖ 𝖹′ and every l ≥ 2 the entries of each of
ℛ^sc_l, ℛ^v_l and ℛ^t_l are pairwise distinct.

(iii) For h ∈ (0, 10⁻⁶] let ε_ind(h) be the infimum of dist(Re ι, ℤ) over the entries ι ∉ ℤ with |ι| ≤ 50 of the lists of
(ii), l ≥ 2, and of the lists ι − 1, ι a root of P_0, P_1 or of p_(v) at l = 1. Then ε_ind(h) > 0 for h ∉ 𝖹′. For every
h, ε_ind(h) ≤ δ_50, where δ_50 := d₂ at l = 50 = 1.94137… · 10⁻⁸ is the distance of the root −49 − δ_50 of
Q_50(ι − 1) from −49; and among the entries that do not depend on h, the least distance of a non-integer entry with
|ι| ≤ 50 from ℤ is δ_50.

*Proof.* (i) As a quadratic in s, Q_l has discriminant (2 + 2κ + z)² − 4κ(κ + 1) − 4zκ = (z + 2)² + 4κ = 4u² + 4z + z²,
so its roots are s_± = (2 + 2κ + z ± (4u² + 4z + z²)^(1/2))/2 = u² + z/2 ± (u + w), both positive. For each, ι′ = (1 ±
(1 + 4s)^(1/2))/2, and 1 + 4s_± = (2u ± 1)² + 2z ± 4w. So the roots in ι = ι′ + 1 are as stated. Since w = (z +
z²/4)/((u² + z + z²/4)^(1/2) + u), one has z(1 − z)/(2u) ≤ w ≤ z(1 + z)/(2u); for u ≥ 2, 2z − 4w ≥ 2z − 2z(1 + z)/u >
0, so d₂ > 0. The elementary bounds ε/(2A) − ε²/(8A³) ≤ (A² + ε)^(1/2) − A ≤ ε/(2A) for A > 0, ε ≥ 0, applied with A =
2u ± 1 and ε = 2z ± 4w = (2z/u)(u ± 1) + O(z²/u), give the stated forms with |θ_i| ≤ z. The roots lie in the open unit
intervals (l + 3, l + 4), (−l − 1, −l), (l + 2, l + 3) and (−l, 1 − l).

(ii) *The entries free of h.* −l, l + 2, 2 − l, l + 4 are distinct for l ≥ 2, and so are −l, l + 2, 1 − l, l + 3; the
four roots of Q_l(ι − 1) lie in four disjoint open unit intervals, so they are distinct and differ from the integers.
*The roots of P_l and p_(v).* For h ∉ 𝖹 ([[lem:iv4-1-3]] (b)) they are simple. Let y be one of the h-independent
entries of ℛ^sc_l plus 1, that is y ∈ {1 − l, l + 3, 3 − l, l + 5} or y in one of (l + 4, l + 5), (1 − l, 2 − l), (l +
3, l + 4), (2 − l, 3 − l). For l ≥ 2 each such y satisfies y ≤ 1 or y ≥ 4, so P_l(y)|_(h=0) = 8v(y − 2)Q_5(y) ≠ 0 by
[[lem:s14-q5]] (a); hence P_l(y), a polynomial in h, vanishes for finitely many h. For ℛ^v_l, y ∈ {1 − l, l + 3, 2 − l,
l + 4} and p_(v)(y)|_(h=0) = −2v(y − 3) ≠ 0. Let 𝖹′ be the union of 𝖹 and of these finite sets over all l ≥ 2.

(iii) Fix h > 0. By (i), the h-independent non-integer entries with |ι| ≤ 50 occur only for l ≤ 50, and by
[[prop:np-10-54]] (iii) only finitely many l have a root of P_l or p_(v) with |ι| ≤ 51; so the infimum is over finitely
many entries. The roots of Q_l(ι − 1) and of p_(v) are real, so for them dist(Re ι, ℤ) > 0 unless ι ∈ ℤ. A non-real
entry is ι − 1 for a non-real root ι of P_l (l ≥ 0), and dist(Re(ι − 1), ℤ) = 0 means Re ι = k with k ∈ [−49, 51] an
integer. By the argument of the proof of [[lem:iv4-1-3]] (b), the set of h at which P_l has a non-real root with real
part k is finite for each (l, k): the limits of [[lem:s14-small-h]] admit no two roots with sum 2k, as ι₊ + ι₋ = 5 +
1/13653, and 2 + ι_± = 2k would make 2k − 2 a root of Q_5, which [[lem:s14-q5]] (a) excludes for 2k − 2 ≤ 1 and
2k − 2 ≥ 4, and which is false for 2k − 2 = 2. The same holds for C, whose finite limit root (4 + 5e)/(2 − 5e) is real
and not an integer. Adding these finite sets to 𝖹′ keeps it countable, and for h ∉ 𝖹′ every non-integer entry with
|ι| ≤ 50 has dist(Re ι, ℤ) > 0; so ε_ind(h) > 0.

For the upper bound, 1 − l − d₂ at l = 50 is −49 − δ_50, an entry with |ι| < 50 for every h, at distance δ_50 from ℤ;
and δ_50 = z·50(1 + θ₂)/(2·51·101) = (2·10⁻⁴/10302)(1 + θ₂), |θ₂| ≤ 4·10⁻⁶, which is 1.94137… · 10⁻⁸. Among the
h-independent entries, the distances are d₁ and d₂ at the admissible l: 1 − l − d₂ has |ι| ≤ 50 iff l ≤ 50, l + 2 + d₂
iff l ≤ 47, −l − d₁ iff l ≤ 49, and l + 3 + d₁ iff l ≤ 46. The function z(u − 1)/(2u(2u − 1)) is decreasing for u ≥ 2,
and its values at consecutive u ≤ 51 differ by a factor at least 1.0198 > (1 + z)/(1 − z), while
z(u + 1)/(2u(2u + 1)) > z(u − 1)/(2u(2u − 1)); so the least distance is d₂ at l = 50. ∎

*Remark.* At the single value h = 10⁻⁶ the infimum ε_ind(10⁻⁶) equals δ_50, the roots of P_l and p_(v) staying farther
from the integers for every l < 10⁴. [[pending:computational-2]] Later chapters use only ε_ind(h) > 0 and
ε_ind(h) ≤ δ_50, which hold for every admissible h by (iii).

