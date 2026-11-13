## The linear solution in a Regge–Wheeler-type gauge {#ch:rw-gauge}

[[thm:viii-2-2]] and [[cor:viii-2-3]] give, for every linearised data set in the class, a linearised vacuum
development in the gauge of the nonlinear problem which settles to a change of mass, and [[cor:ix-2-3]] shows that a
solution in any other gauge with the same data differs from it by a linearised diffeomorphism ℒ_X g, about which
nothing is asserted ([[rem:ix-2-4]] (b)). This chapter determines X for the gauge of Kodama and Ishibashi's master
equations [KI03], in which the scalar modes have no mixed and no trace-free angular components, and proves the decay
of every metric component there. The class carries no vector-type perturbation and no harmonic of degree l = 1
([[lem:gd-1-2]]), so the gauge is reached by an explicit gauge vector, local in the orbit coordinates and built on
each sphere by inverting the Laplacian and (2/3)Δ̂(Δ̂ + 3) ([[lem:gd-1-3]]); its spherically symmetric part is a time
integral ([[lem:gd-1-4]]). In this gauge the perturbation settles to the change of mass at the rate of
[[thm:viii-2-2]], with all derivatives and the horizon included, with a loss of two derivatives and no sum over
harmonics ([[thm:rw-settling]]).

The rest of the chapter compares this with the decay of the master quantities proved by Hung, Keller and Wang
[HKW18], who leave the metric components to "a suitable choice of linearized gauge" ([HKW18, p. 4]). In the class the
components are, mode by mode, Kodama and Ishibashi's reconstruction from the master fields, with coefficients bounded
uniformly in l in a suitable normalisation ([[prop:np-10-1]]). For [HKW18]'s data they settle on each region r ≤ R at
[HKW18]'s rate τ⁻² in energy, once one more datum is finite: the second derivative of the master fields transversal
to the horizon. That datum is needed, because [HKW18]'s energies are first order and the master equation degenerates
at the horizon ([[lem:np-10-1b]]), and it suffices, by a red-shift commutation that is exact for the class's master
equations ([[lem:np-10-1a]]). Uniformly in r the statement fails: on the outgoing part of [HKW18]'s leaves the
orbit-space components can grow as r^(1/2) ([[thm:rwg-1]]), and with that weight, and only with it, they settle
pointwise and uniformly in r ([[thm:rwg-2]], [[thm:rwg-2-prime]]).

### Setting {#sec:rw-setting}

*The metric and the charts.* Throughout, g := g_(b₀), b₀ = (m₀, 0), is the five-dimensional Schwarzschild–Tangherlini
metric of mass m₀ in the coordinates (t, x) of [[sec:iii-b-3]]: g = Φ*_(m₀) g^KS_(m₀), with Φ_m(t, x) = (t − T_m(|x|), x)
and g^KS_m = η + m|x|⁻²(dt_KS + d|x|)² ([[eq:iii-b-3-3]], [[prop:iii-b-3-4]]). So r := |x| is the area radius of the
spheres {t = c, |x| = r}, and SO(4), acting on x, acts by isometries. Put

    v := t − T_(m₀)(r) + r   (that is, t_KS + r),     f := 1 − m₀/r²,     r_h := m₀^(1/2) = R₁,     ς := m₀/r².

On {r ≥ r_♭} (r_♭ ∈ (0, ½R₁] the inner radius of [[ch:s11]]), with γ = dϑ² + cos²ϑ dφ1² + sin²ϑ dφ2² the round
metric of the unit sphere in the coordinates of [[sec:background]],

    g = −f dv² + 2 dv dr + r² γ,                                                                         {#eq:rw-ingoing}

since −dt_KS² + d|x|² = −(dv − dr)² + dr² = −dv² + 2 dv dr. The surface gravity of the horizon {r = r_h} is
f′(r_h)/2 = m₀/r_h³ = 1/r_h. The function t_* of [[eq:iii-b-3-6]] has t_* − v = T_(m₀)(r) − ψ(r) − r, a function of r
alone; so on {r ≤ R′}, |t_* − v| ≤ C_(R′), and ∂_v = ∂_t = ∂_(t_*) at fixed x. On {r > r_h} put

    r_* := r + (r_h/2) log((r − r_h)/(r + r_h)),        t_s := v − r_*,

so that dr_*/dr = 1 + r_h²/(r² − r_h²) = f⁻¹; t_s is the static time, g = −f dt_s² + f⁻¹dr² + r²γ (insert
dv = dt_s + f⁻¹dr in [[eq:rw-ingoing]]), and ∂_(t_s) at fixed r is ∂_v. The letter t without index is kept for the
coordinate of [[sec:iii-b-3]].

*The class.* G = O(2) × O(2) acts as in [[sec:class]]. In the coordinates (v, r, ϑ, φ1, φ2) the torus acts by
translation of φ1, φ2, so the components of a G-invariant tensor in the coordinate frame do not depend on φ1, φ2, and
the reflection φ_i ↦ −φ_i changes the sign of every component with an odd number of φ_i indices. So a G-invariant
symmetric 2-tensor has eight components, functions of (v, r, ϑ): h_ab, h_aϑ, h_ϑϑ, h_(φ1φ1), h_(φ2φ2) (a, b ∈ {v, r});
a G-invariant 1-form has X_v, X_r, X_ϑ. We write y^a for (v, r), z^i for the angles, D for the covariant derivative of
the orbit metric g_ab dy^a dy^b = −f dv² + 2 dv dr, □ := D^aD_a, and D̂, Δ̂ for the covariant derivative and Laplacian
of (S³, γ). "Class" means G-invariant.

*The mass change.* Put K̄ := r⁻² dv² and K_V := ∂_m g_((m,0))|_(m=m₀), the change of mass of [[cor:viii-2-3]]. At fixed
(t_KS, x), ∂_m g^KS_m = |x|⁻²(dt_KS + d|x|)² = r⁻² dv², and Φ_(m+ε) = Φ_m ∘ φ_ε + O(ε²) with φ_ε(t, x) =
(t − ε ∂_mT_m(|x|), x), the flow of V := −(∂_mT_m)|_(m₀)(r) ∂_t. Hence

    K_V = K̄ + ℒ_V g,        ℒ_V g = 0 on {r ≤ 2R₁},                                                         {#eq:gd-0-1}

since T_m(ϱ) = T_m(2R₁) for ϱ ≤ 2R₁ (χ_∞ = 0 there, [[eq:iii-b-3-3]]), so that V is a constant multiple of the Killing
field ∂_t there. V is smooth, stationary and spherically symmetric. K̄ and K_V are linearised vacuum solutions: K̄ is
the derivative in m of the Ricci-flat metrics −(1 − m/r²) dv² + 2 dv dr + r²γ at m₀, and DRic(ℒ_V g) = 0
([[lem:ix-2-1]] (b)).

*The linear solution in the class.* Let (γ̇, k̇) be G-invariant data of [[cor:viii-2-3]], ġ its solution and ṁ its
mass change. ġ is G-invariant, smooth on the interior of N_ν = {t_IVP ≥ −ν(r)}, with DRic(ġ) = 0 there, and its
restriction to N⁺ = M°_♭ ∩ {t_IVP ≥ 0} is smooth up to Σ° ([[lem:s29-g-on-n]], [[sec:ix-0]]). N_ν and N⁺ are unions of
spheres, t_IVP = t − ψ_IVP(r) ([[lem:iii-b-3-7]] (b)). Put

    h := ġ − ṁ K_V,        w := α − 2,

with α chosen as in [[thm:viii-2-2]] (4), α > 4 + ε_t, so that w > 2 + ε_t; of this, the present chapter uses only
w − ε′ > 1. For a tensor field u put

    |u|_k(v, r) := Σ_(j≤k) sup_(S³_(v,r)) |𝒫_j u|,

𝒫_j ranging over the products of j of the operators ℒ_(∂_v), ℒ_(∂_r) (the coordinate fields of (v, r, x/r)) and the
Lie derivatives along the rotation fields Ω_ij = x^i∂_j − x^j∂_i, and |·| the Euclidean norm of the components in the
coordinates (t, x). (In |·|_k and k₁(k) the letter k counts derivatives; elsewhere k := (l(l + 2))^(1/2) is the number
of [KI03] for a harmonic of degree l.)
On {r_♭ ≤ r ≤ R′} these operators and ∂_t, ∂_(x^i) span the same module over functions with bounded
derivatives, and ∂_t = t_*⁻¹ (t_*∂_(t_*)) at fixed x. So [[eq:viii-2-3]] with ḃ = (ṁ, 0) reads: for every k, R′ and
ε′ > 0 there are C, k₁ = k₁(k) and T′ with

    |h|_k ≤ C ‖(γ̇, k̇)‖_(H^(k₁)) t_*^(−w+ε′)     on {r_♭ ≤ r ≤ R′, t_* ≥ T′}.                              {#eq:gd-0-2}

Enlarging T′, we take T′ ≥ 0. The set in [[eq:gd-0-2]] contains points with r = r_♭, which do not lie in
N⁺ = M°_♭ ∩ {t_IVP ≥ 0}, M°_♭ = ℝ_t × {|x| > r_♭}. Its part in {r > r_♭} lies in N⁺, as t_IVP ≥ t_* ≥ T′ ≥ 0 there
([[cor:ix-2-3]]); [[eq:gd-0-2]] is used below only on that part.

### The decomposition on the spheres {#sec:rw-spheres}

All operators below act on the sphere S³ at a point (v, r) of the orbit space, with (v, r) as parameters. For a
function u on S³ put ⟨u⟩ := |S³|⁻¹ ∫_(S³) u dω, |S³| = 2π², dω the measure of γ, and ‖·‖ the norm of L²(S³, dω). For a
class tensor h at (v, r) we write h_(a·) for the 1-form h_ai dz^i on S³, and h^TF for the γ-trace-free part of the
angular block h_ij dz^i dz^j. Its spherical harmonics are described by [[lem:gd-1-2]] (a) below, by which the
operator 𝒢 := [(2/3)Δ̂(Δ̂ + 3)]⁻¹ is defined on class functions of mean zero. We put:

- the *l = 0 part* h_0 := ⟨h_ab⟩ dy^a dy^b + 2r²⟨H_L⟩ γ, where H_L := γ^(ij)h_ij/(6r²);
- the *1-form potentials* β_a := Δ̂⁻¹ D̂^i h_ai, with ⟨β_a⟩ = 0;
- the *scalar potential* 𝓉 := 𝒢 D̂^iD̂^j h^TF_ij;
- the *tensor part* h^TT := h^TF − (D̂D̂ − (1/3)γΔ̂)𝓉.

h_0 is the average of h over SO(4): the orbit components average to ⟨h_ab⟩, the mixed ones to 0 (S³ carries no
SO(4)-invariant 1-form), and the angular block to an invariant symmetric tensor on S³, a multiple of γ, fixed by its
trace. In [[lem:gd-1-2]] the spectral norm of a function u = Σ_l u_l on S³ (u_l of degree l, −Δ̂u_l = k²u_l,
k² := l(l + 2)) is ‖u‖²_(H^σ) := Σ_l (1 + k²)^σ ‖u_l‖², and the six rotation fields of R⁴ restricted to S³ are written
Ω_1, …, Ω_6.

**Lemma {#lem:rwg-a}** (A Sobolev inequality on S³ with rotations.) For a function w on S³,

    sup |w|² ≤ (1/12) ‖(1 − Δ̂)w‖² ≤ (1/6) (‖w‖² + Σ_(i,j) ‖Ω_iΩ_j w‖²),

and for a symmetric 2-tensor T on S³, with L_i the Lie derivative along Ω_i and |·| the norm of γ,

    sup |T|² ≤ (1/6) (2305 ‖T‖² + 192 Σ_i ‖L_iT‖² + 4 Σ_(i,j) ‖L_iL_jT‖²).

Moreover Σ_i Ω_i² = Δ̂ on functions, and Σ_i (Ω_i w)² = |D̂w|².

*Proof.* The harmonics of degree l on S³, the restrictions of the harmonic polynomials of degree l on R⁴, form a space
of dimension (l + 1)², on which −Δ̂ = l(l + 2). For an L²-orthonormal basis S_1, …, S_((l+1)²) of it, Σ_m |S_m(ω)|² does
not depend on the basis and is carried to itself by the rotations, so it is constant, equal to
(l + 1)²/|S³| = (l + 1)²/(2π²). By Cauchy–Schwarz in the coefficients, |w_l(ω)| ≤ (l + 1)‖w_l‖/(2π²)^(1/2) for w_l of
degree l. So, by Cauchy–Schwarz in l,

    sup |w| ≤ Σ_l (l + 1)‖w_l‖/(2π²)^(1/2) ≤ (Σ_l (l + 1)⁻²)^(1/2) (Σ_l (l + 1)⁴‖w_l‖²)^(1/2)/(2π²)^(1/2),

and (l + 1)² = 1 + l(l + 2), Σ_(l≥0) (l + 1)⁻² = π²/6: this is the first inequality, with (π²/6)/(2π²) = 1/12. For a
function u on R⁴ and the rotation fields Ω_ab = x_a∂_b − x_b∂_a (a < b), Lagrange's identity gives
Σ_(a<b) (Ω_ab u)² = |x|²|∇u|² − (x · ∇u)², which on |x| = 1 is |D̂u|² for the tangential gradient. Applied to
u = w(x/|x|) and polarised, Σ_i ∫ (Ω_iw)(Ω_iw′) dω = ∫ ⟨D̂w, D̂w′⟩ dω; each Ω_i is skew on L²(S³), so
−Σ_i Ω_i² = −Δ̂ in the weak sense, and Σ_i Ω_i² = Δ̂. Each Ω_i commutes with Δ̂ (it is a Killing field), so
‖Δ̂w‖² = ⟨w, Δ̂²w⟩ = Σ_(i,j) ⟨w, Ω_i²Ω_j²w⟩ = Σ_(i,j) ‖Ω_iΩ_jw‖², and ‖(1 − Δ̂)w‖² ≤ 2‖w‖² + 2‖Δ̂w‖² gives the second
inequality.

For T: extend T to R⁴ ∖ 0 by T(PX, PY), P = 1 − xxᵀ/|x|² the projection onto the tangent spaces of the spheres; its
Cartesian components T_IJ (I, J = 1, …, 4) restrict to functions on S³ with Σ_(I,J) T_IJ² = |T|². The rotations preserve
P, so the Lie derivative of the extension along Ω_i is the extension of L_iT, and in Cartesian components Ω_i(T_IJ) =
(L_iT)_IJ − (A_iᵀT + TA_i)_IJ, A_i the constant antisymmetric matrix with Ω_i = (A_ix) · ∂_x, of operator norm 1. So,
with |·|_F the Frobenius norm, |Ω_iT|_F ≤ |L_iT| + 2|T| and |Ω_iΩ_jT|_F ≤ |L_iL_jT| + 2|L_jT| + 2|L_iT| + 4|T|. Sum the
inequality for functions over (I, J), use (a + b + c + d)² ≤ 4(a² + b² + c² + d²) and count the six rotations: the
coefficient of ‖T‖² is 1 + 4 · 16 · 36 = 2305, that of Σ_i ‖L_iT‖² is 4 · 4 · 6 + 4 · 4 · 6 = 192, and that of Σ_(i,j)
‖L_iL_jT‖² is 4. ∎

**Lemma {#lem:gd-1-2}** (The sphere.) (a) The T²-invariant spherical harmonics on S³ are the functions P_j(cos 2ϑ),
P_j the Legendre polynomials, with Δ̂P_j(cos 2ϑ) = −l(l + 2)P_j(cos 2ϑ), l = 2j; they are complete in the T²-invariant
part of L²(S³). So class functions carry only even l, and on their mean-zero part k² = l(l + 2) ≥ 8 and
(2/3)k²(k² − 3) ≥ 80/3: 𝒢 is defined.

(b) For every function u on S³, D̂^iD̂^j(D̂_iD̂_j − (1/3)γ_ijΔ̂)u = (2/3)Δ̂(Δ̂ + 3)u. So D̂^iD̂^jh^TT_ij = 0.

(c) A class 1-form on S³ with zero divergence vanishes, and every class 1-form on S³ is exact: there is no
vector-type part in the class, and h_ai dz^i = dβ_a. The divergence of a class symmetric 2-tensor is a class 1-form;
so D̂^ih^TT_ij = 0, and h^TT is transverse and trace-free (the tensor type).

(d) (Bounds uniform in l.) For a harmonic S of degree l, ‖D̂S‖² = k²‖S‖² and
‖(D̂D̂ − (1/3)γΔ̂)S‖² = (2/3)k²(k² − 3)‖S‖². Hence, for a class tensor h,

    ‖β_a‖_(H^1) ≤ (9/8)^(1/2) ‖h_(a·)‖,        ‖𝓉‖_(H^2) ≤ (243/80)^(1/2) ‖h^TF‖,

and, with constants independent of h and of l,

    sup|β_a| ≤ C|h_(a·)|_1,     sup|𝓉| ≤ C|h^TF|_0,     sup|D̂𝓉| ≤ C|h^TF|_1,

the same holding with any product 𝒫_j of ℒ_(∂_v), ℒ_(∂_r) and the rotations applied to both sides. Here |h_(a·)|_k and
|h^TF|_k are taken with the norm of the unit sphere; on {r_♭ ≤ r ≤ R′} each is at most C_(R′)|h|_k. No sum over
harmonics is formed.

*Proof.* (a) In the coordinates (ϑ, φ1, φ2), dω = cos ϑ sin ϑ dϑ dφ1 dφ2 = (1/2) sin 2ϑ dϑ dφ1 dφ2, and on
functions of ϑ alone Δ̂u = (sin 2ϑ)⁻¹∂_ϑ(sin 2ϑ ∂_ϑu). With x := cos 2ϑ, ∂_ϑ = −2 sin 2ϑ ∂_x, so
sin 2ϑ ∂_ϑu = −2(1 − x²)∂_xu and Δ̂u = 4∂_x((1 − x²)∂_xu). Legendre's equation ((1 − x²)P_j′)′ = −j(j + 1)P_j gives
Δ̂P_j(cos 2ϑ) = −4j(j + 1)P_j = −2j(2j + 2)P_j. The T²-orbits are the level sets of ϑ, so T²-invariant functions are
functions of ϑ, and after the φ integrals dω becomes 2π² sin 2ϑ dϑ, which is π² dx as a measure on (−1, 1); the
Legendre polynomials are complete in L²(−1, 1).
For l = 2j ≥ 2, k² ≥ 8 and (2/3)k²(k² − 3) ≥ (2/3) · 8 · 5 = 80/3.

(b) On the unit S³, Ric = 2γ, so D̂^jD̂_iD̂_ju = D̂_iΔ̂u + 2D̂_iu, and D̂^iD̂^jD̂_iD̂_ju = Δ̂²u + 2Δ̂u. Subtracting
(1/3)Δ̂²u gives (2/3)Δ̂²u + 2Δ̂u = (2/3)Δ̂(Δ̂ + 3)u. D̂^iD̂^jh^TF_ij is a divergence, so of mean zero, and by
definition of 𝓉, D̂^iD̂^jh^TT_ij = D̂^iD̂^jh^TF_ij − (2/3)Δ̂(Δ̂ + 3)𝓉 = 0.

(c) A class 1-form on S³ is a(ϑ) dϑ: the components along dφ1, dφ2 have one φ_i index. Its divergence is
(sin 2ϑ)⁻¹∂_ϑ(sin 2ϑ a); if this vanishes, a = C/sin 2ϑ, and |a dϑ| = |a| is bounded near ϑ = 0 only if C = 0. For any
class 1-form α let η be the mean-zero solution of Δ̂η = D̂^iα_i; η is a class function (Δ̂ commutes with G), so α − dη is
a class 1-form with zero divergence, hence 0. Every operator above is G-equivariant, so the divergence of a class tensor
is a class 1-form; by (b) D̂^ih^TT_ij has zero divergence, so it vanishes. For h_(a·): h_(a·) = dη_a with Δ̂η_a =
D̂^ih_ai, so η_a = β_a.

(d) Integrating by parts, ‖D̂S‖² = −⟨S, Δ̂S⟩ = k²‖S‖², and, with (b),
‖(D̂D̂ − (1/3)γΔ̂)S‖² = ⟨S, D̂^iD̂^j(D̂_iD̂_j − (1/3)γ_ijΔ̂)S⟩ = ⟨S, (2/3)Δ̂(Δ̂ + 3)S⟩ = (2/3)k²(k² − 3)‖S‖².
As h_(a·) = dβ_a, ‖h_(a·)‖² = Σ_l k²‖β_(a,l)‖², and ‖β_a‖²_(H^1) = Σ_l (1 + k²)‖β_(a,l)‖² ≤ (9/8)‖h_(a·)‖², since
(1 + k²)/k² decreases in k² ≥ 8. The two parts of h^TF are orthogonal:
⟨(D̂D̂ − (1/3)γΔ̂)𝓉, h^TT⟩ = ⟨𝓉, D̂^iD̂^jh^TT_ij⟩ = 0. So ‖h^TF‖² ≥ Σ_l (2/3)k²(k² − 3)‖𝓉_l‖², and
‖𝓉‖²_(H^2) ≤ (243/80)‖h^TF‖², since (1 + k²)²/((2/3)k²(k² − 3)) decreases in k² ≥ 8 (the logarithmic derivative in
x = k² is 2/(1 + x) − 1/x − 1/(x − 3) = (3 − 5x)/(x(1 + x)(x − 3)) < 0) and equals 243/80 at k² = 8.

The rotations are Killing fields of (S³, γ), so they commute with D̂, Δ̂, 𝒢 and the decomposition, and preserve the
degree. By [[lem:rwg-a]], sup|β_a|² ≤ (1/12)‖β_a‖²_(H^2), and
‖β_a‖²_(H^2) = Σ_l (1 + k²)²‖β_(a,l)‖² ≤ (9/8) Σ_l (k² + k⁴)‖β_(a,l)‖² = (9/8)(‖h_(a·)‖² + Σ_i ‖L_ih_(a·)‖²),
as Σ_i ‖L_i dβ_(a,l)‖² = Σ_i ‖dΩ_iβ_(a,l)‖² = k²Σ_i‖Ω_iβ_(a,l)‖² = k⁴‖β_(a,l)‖² by [[lem:rwg-a]]. The L² norms are at
most 2π² times the squared suprema. Likewise sup|𝓉|² ≤ (1/12)‖𝓉‖²_(H^2) ≤ C‖h^TF‖², and
sup|D̂𝓉|² = sup Σ_i (Ω_i𝓉)² ≤ (1/12) Σ_i ‖Ω_i𝓉‖²_(H^2) ≤ (1/12) Σ_l (1 + k²)³‖𝓉_l‖², which is at most
(243/80)(1/12)(‖h^TF‖² + Σ_i ‖L_ih^TF‖²), the projection of h^TF on its scalar-derived part being orthogonal and
commuting with the L_i. Finally ℒ_(∂_v) and ℒ_(∂_r) commute with every operator on the spheres, γ not depending on
(v, r). ∎

**Definition {#def:gd-1-1}** (The Regge–Wheeler-type gauge in the class.) A class tensor h is in the
*Regge–Wheeler-type gauge* if β_v = β_r = 0, 𝓉 = 0 and h_0 = cK_V for a constant c. When K̄ replaces K_V in the last
condition we say *with the mass change K̄*; on {r ≤ 2R₁} the two conditions agree ([[eq:gd-0-1]]).

For a scalar mode the conditions β_a = 0, 𝓉 = 0 are Kodama and Ishibashi's f_a = 0 = H_T ([[lem:gd-1-3]] (b)).

**Lemma {#lem:gd-1-3}** (The gauge vector.) For a class tensor h put

    ξ[h] := (−β_a + (r²/2) ∂_a(𝓉/r²)) dy^a − (1/2) D̂𝓉.                                                    {#eq:gd-1-1}

(a) ℒ_(ξ[h]) g has the mixed components (ℒ_ξ g)_(aj) dz^j = −dβ_a, and its angular block has trace-free part
−(D̂D̂ − (1/3)γΔ̂)𝓉. So h + ℒ_(ξ[h])g has β = 0, 𝓉 = 0, the same h^TT as h, and the same l = 0 part.

(b) For a scalar mode of degree l ≥ 2 written as in [KI03, (2.4)–(2.6), p. 4],

    h_ab = f_ab S,  h_ai = r f_a S_i,  h_ij = 2r²(H_L γ_ij S + H_T S_ij),
    S_i = −D̂_iS/k,  S_ij = D̂_iD̂_jS/k² + γ_ijS/3,

one has β_a = −(r/k)f_a S and 𝓉 = 2r²H_TS/k²; the orbit part of ξ[h] is X_aS with Kodama and Ishibashi's
X_a = (r/k)(f_a + (r/k)D_aH_T) [KI03, (2.8), p. 5], and

    h + ℒ_(ξ[h]) g = F_ab S dy^a dy^b + 2r²F S γ,

with their gauge invariants F = H_L + H_T/3 + r⁻¹D^arX_a and F_ab = f_ab + D_aX_b + D_bX_a [KI03, (2.7), p. 5].

(c) (Uniqueness.) For a class 1-form Z with no l = 0 part, ξ[ℒ_Z g] = −Z. In particular ℒ_Z g has β = 𝓉 = 0 only if
Z = 0.

*Proof.* For g = g_ab dy^ady^b + r²γ the Christoffel symbols mixing the factors are Γ^a_ij = −r D^ar γ_ij and
Γ^i_aj = (∂_ar/r) δ^i_j, the others being those of the two factors. So for a 1-form ξ = ξ_a dy^a + ξ_i dz^i,

    (ℒ_ξg)_ab = D_aξ_b + D_bξ_a,   (ℒ_ξg)_ai = ∂_iξ_a + r²∂_a(ξ_i/r²),   (ℒ_ξg)_ij = D̂_iξ_j + D̂_jξ_i + 2rD^arξ_a γ_ij.

(a) With ξ_i = −(1/2)D̂_i𝓉 and ξ_a = −β_a + (r²/2)∂_a(𝓉/r²): (ℒ_ξg)_ai = ∂_i(ξ_a − (r²/2)∂_a(𝓉/r²)) = −∂_iβ_a, and
(ℒ_ξg)_ij = −D̂_iD̂_j𝓉 + (a multiple of γ_ij), whose trace-free part is −(D̂D̂ − (1/3)γΔ̂)𝓉. As h_(a·) = dβ_a
([[lem:gd-1-2]] (c)), h + ℒ_ξg has vanishing mixed components, so β = 0; its h^TF is h^TT, so 𝓉 = 0 and the tensor part
is unchanged. The components of ξ have mean zero on each sphere, so the SO(4)-average of ξ vanishes; rotations are
isometries, so the average of ℒ_ξg is ℒ of the average of ξ, which is 0.

(b) h_ai = rf_a(−D̂_iS/k) = ∂_i(−(r/k)f_aS), so β_a = −(r/k)f_aS. As Δ̂S = −k²S,
h^TF = 2r²H_T(D̂D̂S − (1/3)γΔ̂S)/k², so h^TT = 0 and 𝓉 = 2r²H_TS/k². Then
ξ_a = (r/k)f_aS + (r²/2)∂_a(2H_TS/k²) = (r/k)(f_a + (r/k)D_aH_T)S = X_aS. The orbit block of h + ℒ_ξg is
(f_ab + D_aX_b + D_bX_a)S = F_abS. Its angular block is

    2r²(H_LγS + H_T(D̂D̂S/k² + γS/3)) − (2r²H_T/k²)D̂D̂S + 2rD^arX_aSγ = 2r²(H_L + H_T/3 + r⁻¹D^arX_a)Sγ = 2r²FSγ.

(c) Write Z = Z_a dy^a + Z_ϑ dϑ; by [[lem:gd-1-2]] (c), Z_ϑ dϑ = dη on each sphere with ⟨η⟩ = 0, and ⟨Z_a⟩ = 0. By the
formulas above, (ℒ_Zg)_ai dz^i = d(Z_a + r²∂_a(η/r²)), so β_a[ℒ_Zg] = Z_a + r²∂_a(η/r²); and the trace-free angular
part of ℒ_Zg is 2(D̂D̂ − (1/3)γΔ̂)η, so 𝓉[ℒ_Zg] = 2η by (b) of [[lem:gd-1-2]]. Inserting in [[eq:gd-1-1]]:
ξ[ℒ_Zg] = (−Z_a − r²∂_a(η/r²) + r²∂_a(η/r²))dy^a − dη = −Z. ∎

### The spherically symmetric part {#sec:rw-l0}

**Lemma {#lem:rw-warped}** (Warped products over S³.) Let g′ = g′_ab dy^a dy^b + R²γ, with g′_ab a Lorentzian metric
and R > 0 a function on a two-dimensional manifold, D, □ and 𝓇 the covariant derivative, wave operator and scalar
curvature of g′_ab. Then Ric[g′]_ab = (𝓇/2)g′_ab − (3/R)D_aD_bR, Ric[g′]_ai = 0 and
Ric[g′]_ij = ρ_S γ_ij with ρ_S := 2(1 − |dR|²) − R□R. The Misner–Sharp mass m(g′) := R²(1 − |dR|²) satisfies

    ∂_a m(g′) = (2R³/3)(Ric_ab − (1/2)g′_ab g′^(cd)Ric_cd) D^bR + Rρ_S ∂_aR,                                 {#eq:rw-ms}

with Ric := Ric[g′] and indices raised by g′_ab.

*Proof.* The Christoffel symbols mixing the factors are Γ^a_ij = −RD^aR γ_ij and Γ^i_aj = (∂_aR/R)δ^i_j; the others are
those of g′_ab and of γ. Inserting them in R_bd = ∂_μΓ^μ_bd − ∂_dΓ^μ_bμ + Γ^μ_μνΓ^ν_bd − Γ^μ_dνΓ^ν_bμ, as in the proof
of [[lem:warped-ricci]]: for b, d on the base, the fibre indices add −3∂_b∂_dR/R + 3Γ^c_bd∂_cR/R = −3D_bD_dR/R, and the
Ricci tensor of a two-dimensional metric is (𝓇/2)g′_ab. For i, j on the fibre, the base derivatives of Γ^a_ij give
−D_a(RD^aR)γ_ij = −(R□R + |dR|²)γ_ij, the products containing mixed symbols give −3|dR|²γ_ij + 2|dR|²γ_ij, and
the fibre gives Ric[γ] = 2γ. The mixed
components vanish since every term carries an odd number of fibre indices of a tensor built from γ and its connection
alone. For [[eq:rw-ms]]: ∂_am = 2R∂_aR(1 − |dR|²) − 2R²D^bR D_aD_bR. By the formulas just proved,
D_aD_bR = (R/3)((𝓇/2)g′_ab − Ric_ab), 2(1 − |dR|²) = ρ_S + R□R and □R = (R/3)(𝓇 − g′^(cd)Ric_cd). Inserting these, the
terms in 𝓇 cancel and [[eq:rw-ms]] remains. ∎

**Lemma {#lem:gd-1-4}** (The spherically symmetric part: the linearised mass and Birkhoff's theorem.) Let
h_0 = A dv² + 2B dv dr + C dr² + 2r²H_L γ, with A, B, C, H_L functions of (v, r) on a simply connected open subset U of
the orbit space of {r > r_♭}, and write Ṙ := DRic(h_0).

(a) The linearisation of the Misner–Sharp mass at g (where it equals m₀) is

    δm[h_0] = 2m₀H_L + r²(A + 2fB + f²C) − 2r²(∂_v + f∂_r)(rH_L).

It vanishes on ℒ_Y g for every spherically symmetric vector field Y; δm[K̄] = δm[K_V] = 1; and

    ∂_v δm = (2/3)r³(Ṙ_vv + fṘ_vr),        ∂_r δm = (1/3)r³fṘ_rr + rṘ_ϑϑ.

(b) If DRic(h_0) = 0 on U, then δm[h_0] =: c is constant; with Y_1 := −rH_L∂_r and h′ := h_0 − cK̄ + ℒ_(Y_1)g =
A′dv² + 2B′dvdr + C′dr², the 1-form 𝔷 := (B′ + (f/2)C′)dv + (1/2)C′dr is closed, and for dζ = 𝔷, ℒ_(ζ∂_v)g = h′. So

    h_0 = cK̄ + ℒ_(Y[h_0]) g,        Y[h_0] := ζ∂_v + rH_L∂_r.                                               {#eq:gd-1-2}

(c) The spherically symmetric Killing fields of g are the multiples c′∂_v of ∂_v = ∂_t. So Y[h_0] is unique up to
c′∂_v, the choice of the constant in ζ.

*Proof.* (a) For ε small, g + εh_0 has the orbit metric g_ab + εh_ab, h_ab dy^ady^b := A dv² + 2B dvdr + C dr², and the
area radius R_ε with R_ε² = r²(1 + 2εH_L), so R_ε = r + εrH_L + O(ε²). The inverse orbit metric of g is
g^(vv) = 0, g^(vr) = 1, g^(rr) = f, and its variation is −h^(ab) = −g^(ac)g^(bd)h_cd, with h^(rr) = A + 2fB + f²C. So
δ|dR|² = −(A + 2fB + f²C) + 2g^(rb)∂_b(rH_L) = −(A + 2fB + f²C) + 2(∂_v + f∂_r)(rH_L), and
δm = 2r·rH_L(1 − f) − r²δ|dR|², which is the formula, as r²(1 − f) = m₀. A spherically symmetric Y is a field
Y^a(y)∂_a (S³ carries no SO(4)-invariant vector field), so its flow φ_s maps spherically symmetric metrics to
spherically symmetric metrics, with R(φ_s*g) = R(g) ∘ φ_s, and m(φ_s*g) = m(g) ∘ φ_s = m₀; differentiating at s = 0,
δm[ℒ_Yg] = 0. For K̄, A = r⁻² and the rest vanish, so δm[K̄] = 1; δm[K_V] = 1 by [[eq:gd-0-1]], V being spherically
symmetric. Finally, linearise [[eq:rw-ms]] at g, where Ric = 0, R = r and D^br = g^(br): only the variation of the
Ricci tensor survives, ρ̇_S = Ṙ_ϑϑ, and ∂_aδm = (2r³/3)(Ṙ_ab − (1/2)g_ab g^(cd)Ṙ_cd)g^(br) + rṘ_ϑϑ∂_ar. For a = v,
g^(br)(Ṙ_vb − (1/2)g_vb tr) = Ṙ_vv + fṘ_vr − (1/2)(g_vv + fg_vr)tr = Ṙ_vv + fṘ_vr, as g_vv + fg_vr = 0, and ∂_vr = 0.
For a = r, Ṙ_rv + fṘ_rr − (1/2)(g_rv + fg_rr)(2Ṙ_vr + fṘ_rr) = (1/2)fṘ_rr.

(b) U is connected, so δm[h_0] is constant by (a). For a field Y = Y^r∂_r, (ℒ_Yg)_ij = Y(r²)γ_ij = 2rY^rγ_ij, so
ℒ_(Y_1)g removes the angular block, and h′ has the stated form. DRic(K̄) = 0, DRic(ℒ_(Y_1)g) = 0 ([[lem:ix-2-1]] (b)),
so DRic(h′) = 0, and δm[h′] = c − c + 0 = 0 by (a), that is A′ = −2fB′ − f²C′. The metrics g + εh′ keep R = r, so by
[[lem:rw-warped]] their rr Ricci component is (𝓇_ε/2)(g + εh′)_rr − (3/r)D^ε_rD^ε_r r. At ε = 0, g_rr = 0 and
𝓇 = −f″ (the scalar curvature of −f dv² + 2 dv dr), and D_rD_rr = −Γ^r_rr; the first-order variation of Γ^r_rr is
(1/2)g^(rd)(2∂_rh′_dr − ∂_dh′_rr) = (1/2)(2∂_rB′ − ∂_vC′ + f∂_rC′), the term with the variation of g^(rd) vanishing
as the lowered symbols Γ_(d,rr) of g vanish. So

    0 = Ṙ_rr[h′] = −(f″/2)C′ + (3/(2r))(2∂_rB′ − ∂_vC′ + f∂_rC′) = (3/r)(∂_r(B′ + (f/2)C′) − ∂_v(C′/2)),

using −rf″/6 = m₀/r³ = f′/2. So d𝔷 = 0, and 𝔷 = dζ on the simply connected U. For Y = ζ∂_v, ∂_v being Killing,
ℒ_Yg = dζ ⊗ (∂_v)^♭ + (∂_v)^♭ ⊗ dζ with (∂_v)^♭ = −f dv + dr, that is

    ℒ_(ζ∂_v)g = −2f∂_vζ dv² + 2(∂_vζ − f∂_rζ) dv dr + 2∂_rζ dr².

With ∂_rζ = C′/2 and ∂_vζ = B′ + fC′/2 this is A′dv² + 2B′dvdr + C′dr², by A′ = −2fB′ − f²C′. Hence
h_0 = h′ + cK̄ − ℒ_(Y_1)g = cK̄ + ℒ_(ζ∂_v − Y_1)g, which is [[eq:gd-1-2]].

(c) For Y = a∂_v + b∂_r with ℒ_Yg = 0, the angular block 2rbγ forces b = 0, and the formula for ℒ_(a∂_v)g forces
∂_ra = 0 and ∂_va = 0. ∎

### The theorem {#sec:rw-theorem}

The following theorem passes the decay of [[thm:viii-2-2]] to the Regge–Wheeler-type gauge directly, sphere by sphere;
it uses neither the reconstruction of the metric from the master fields nor the estimates of [HKW18].

**Theorem {#thm:rw-settling}** (The linear solution in the Regge–Wheeler-type gauge.) Let ġ, ṁ and h = ġ − ṁK_V be
as in [[sec:rw-setting]], h_0 the l = 0 part of h, and N⁺ = M°_♭ ∩ {t_IVP ≥ 0}.

(a) δm[h_0] = 0, and with Y[h_0] of [[eq:gd-1-2]], ζ normalised by ζ(v, r) → 0 as v → ∞,

    X_RW := ξ[h] − Y[h_0]^♭,        ġ_RW := ġ + ℒ_(X_RW) g = ṁK_V + (h − h_0) + ℒ_(ξ[h]) g

is a smooth G-invariant linearised vacuum solution on N⁺, smooth up to Σ°, in the Regge–Wheeler-type gauge with l = 0
part exactly ṁK_V, inducing (γ̇, k̇) plus the data of the linearised diffeomorphism ℒ_(X_RW)g. The same formulas define
a smooth G-invariant linearised vacuum solution ġ_RW = ġ + ℒ_(X_RW)g on the open set int N_ν ∩ M°_♭, which contains the
interior of N⁺, in the Regge–Wheeler-type gauge with l = 0 part exactly ṁK_V.

(b) (Decay.) For every k, R′ and ε′ > 0 there are C and T′ with

    |ġ_RW − ṁK_V|_k ≤ C ‖(γ̇, k̇)‖_(H^(k₁(k+2))) t_*^(−w+ε′)     on {r_♭ < r ≤ R′, t_* ≥ T′}:

the rate of [[thm:viii-2-2]], with a loss of two derivatives, the horizon included (r_♭ < r_h), uniformly in l (no
sum over harmonics is formed). The constant depends on R′; nothing is claimed uniformly in r.

(c) (The gauge vector.) On the same set, |ξ[h]|_k ≤ C‖(γ̇, k̇)‖_(H^(k₁(k+1))) t_*^(−w+ε′); the radial component rH_L
of Y[h_0] = ζ∂_v + rH_L∂_r, and every derivative of ξ[h] and of the components ζ and rH_L, are O(t_*^(−w+ε′)); and
|ζ| ≤ Ct_*^(−w+1+ε′). As a 1-form, X_(RW,0) := −Y[h_0]^♭ = (fζ − rH_L) dv − ζ dr; its dr component, and the term f′ζ
in the r-derivative of its dv component, are only O(t_*^(−(w−1)+ε′)). So X_RW = O(t_*^(−(w−1)+ε′)). Among the
G-invariant 1-forms X on N⁺ for which ġ + ℒ_Xg is in the Regge–Wheeler-type gauge with l = 0 part ṁK_V, X_RW is unique
up to c′(∂_v)^♭, c′ a constant, and the c′∂_v are the only G-invariant Killing fields.

(d) (Uniqueness of the representative.) Let U ⊂ U^♯ be open and SO(4)-invariant, Ω′_+ := D_U(Σ_U) ∩ {t_IVP ≥ 0}, and
let ġ′ be a G-invariant linearised vacuum solution on Ω′_+, smooth up to Σ_U, in the Regge–Wheeler-type gauge,
inducing (γ̇, k̇) plus the data of ℒ_Z g for a vector field Z near Σ_U, smooth up to Σ_U. Then ġ′ = ġ_RW on Ω′_+.

*Proof.* (a) β and 𝓉 depend smoothly on (v, r, ϑ) (elliptic inverses on S³ with smooth parameters, commuting with
ℒ_(∂_v), ℒ_(∂_r)), so ξ[h] is smooth up to Σ°, and its β and 𝓉 are those of ġ, K_V being spherically symmetric. DRic
commutes with the SO(4)-average, so DRic(h_0) = (DRic ġ)_0 − ṁ DRic(K_V) = 0. The orbit space of the interior of N⁺,
{t > ψ_IVP(r), r > r_♭}, lies above a graph, so it is simply connected, and the upward rays {(v′, r) : v′ ≥ v} stay in
it, t_IVP increasing with v at fixed r. [[lem:gd-1-4]] (b) applies there: δm[h_0] is a constant, and being an
expression in h_0 and its first derivatives it tends to 0 along {r = r′}, for any r′ ∈ (r_♭, R′], by [[eq:gd-0-2]];
so it vanishes, and h_0 = ℒ_(Y[h_0])g. The 1-form 𝔷 of [[lem:gd-1-4]] (b) is algebraic in h_0 and the first
derivatives of H_L, so |𝔷|_k ≤ C|h|_(k+1), integrable in v by [[eq:gd-0-2]] as w − ε′ > 1. Put
ζ(v, r) := −∫_v^∞ 𝔷_v(v′, r) dv′. Then ∂_vζ = 𝔷_v, and as d𝔷 = 0, ∂_rζ = −∫_v^∞ ∂_(v′)𝔷_r dv′ = 𝔷_r; so dζ = 𝔷, ζ → 0
as v → ∞, and ζ is smooth up to Σ°, its derivatives being those of 𝔷. Hence ġ_0 − ℒ_(Y[h_0])g = ṁK_V, and with
[[lem:gd-1-3]] (a), ġ_RW is in the Regge–Wheeler-type gauge with l = 0 part ṁK_V. DRic(ℒ_Xg) = 0
([[lem:ix-2-1]] (b)), and ℒ_Xg changes the induced data by those of a linearised diffeomorphism, read from one side
up to Σ° ([[lem:viii-1-1]]). Every step is O(4)-equivariant and ġ is G-invariant, so ġ_RW is G-invariant.

*The open set int N_ν ∩ M°_♭.* At fixed x, t_IVP + ν(r) = t − ψ_IVP(r) + ν(r) increases strictly with t, so the interior
of N_ν = {t_IVP ≥ −ν(r)} is {t > ψ_IVP(r) − ν(r)}. With v = t − T_(m₀)(r) + r, the orbit space of int N_ν ∩ M°_♭ is

    {(v, r) : r > r_♭, v > b(r)},        b(r) := ψ_IVP(r) − ν(r) − T_(m₀)(r) + r,

with b continuous; (v, r) ↦ (v − b(r), r) maps it homeomorphically onto (0, ∞) × (r_♭, ∞), so it is simply connected,
and it contains the upward ray from each of its points. ġ is smooth there with DRic(ġ) = 0 ([[lem:s29-g-on-n]]), and
int N_ν ∩ M°_♭ contains the interior of N⁺, as ν ≥ 0. The steps above use, besides these properties, only
[[eq:gd-0-2]] on the rays {r = r′}, r′ ∈ (r_♭, R′], for v so large that t_* ≥ T′. So they apply verbatim on
int N_ν ∩ M°_♭, with "smooth" in place of "smooth up to Σ°": the same formulas define ζ, X_RW and ġ_RW there, agreeing
with the above on the interior of N⁺, and ġ_RW is a smooth G-invariant linearised vacuum solution on int N_ν ∩ M°_♭ in
the Regge–Wheeler-type gauge with l = 0 part ṁK_V. Nothing is said there about induced data, int N_ν ∩ M°_♭ being open.

(b) ġ_RW − ṁK_V = (h − h_0) + ℒ_(ξ[h])g. Averaging does not increase |·|_k. ℒ_ξg is first order in ξ, and by
[[lem:gd-1-2]] (d) and [[eq:gd-1-1]] each component of ξ costs one derivative of h (β_a one angular derivative, ∂_a𝓉 one
orbit derivative, D̂𝓉 one angular derivative), so |ℒ_(ξ[h])g|_k ≤ C|ξ[h]|_(k+1) ≤ C|h|_(k+2). Apply [[eq:gd-0-2]].

(c) The bounds on ξ[h] and rH_L are [[lem:gd-1-2]] (d) and [[eq:gd-0-2]]; those on the derivatives of ζ are those on 𝔷,
and |ζ| ≤ C∫_v^∞ v′^(−w+ε′)dv′ ≤ C′v^(−w+1+ε′), with |t_* − v| ≤ C_(R′). The form of X_(RW,0) follows from
(∂_v)^♭ = −f dv + dr and (∂_r)^♭ = dv. A G-invariant Killing field Z has ξ[ℒ_Zg] = −Z_(≥2) = 0 by [[lem:gd-1-3]] (c),
where Z_(≥2) := Z − Z_0 has only harmonics of degree l ≥ 2 ([[lem:gd-1-2]]), and Z_0 = c′(∂_v)^♭ by
[[lem:gd-1-4]] (c). If X′ is another G-invariant 1-form for which ġ + ℒ_(X′)g is in the Regge–Wheeler-type gauge with
l = 0 part ṁK_V, then Z := X′ − X_RW is G-invariant and ℒ_Zg = (ġ + ℒ_(X′)g) − ġ_RW is in the Regge–Wheeler-type gauge
with l = 0 part 0; so ℒ_Zg = 0 by the argument of (d), and Z = c′(∂_v)^♭.

(d) By [[cor:ix-2-3]] and [[rem:ix-2-4]] (c), ġ′ = ġ + ℒ_(X′)g on Ω′_+ with X′ G-invariant: an SO(4)-invariant U is a
union of sets {(t, x) : (t, |x|) ∈ A}, hence O(4)- and G-invariant. So ġ′ − ġ_RW = ℒ_Zg, Z := X′ − X_RW, is in the
Regge–Wheeler-type gauge, with l = 0 part c″K_V for a constant c″. By [[lem:gd-1-3]] (c), Z_(≥2) = 0, as the β and
𝓉 of ℒ_Zg are those of ℒ_(Z_(≥2))g. Its l = 0 part ℒ_(Z_0)g is c″K_V, and c″ = δm[ℒ_(Z_0)g] = 0 by
[[lem:gd-1-4]] (a). So ℒ_Zg = 0. ∎

**Remark {#rem:rw-zeta}** (The loss of one power in ζ.) It comes from the time integral and is attained by the
implication "ℒ_Yg decays ⇒ Y decays": by the formula for ℒ_(ζ∂_v)g, Y = (1 + v)^(−q)∂_v has
ℒ_Yg = 2q(1 + v)^(−q−1)(f dv² − dv dr) = O(v^(−q−1)), with every derivative, while Y is only O(v^(−q)). Whether
the h_0 of [[cor:viii-2-3]] makes ζ decay faster is not determined here.

### The master fields {#sec:rw-master}

The scalar and tensor modes of the class are carried by Kodama and Ishibashi's master fields. We use the following
results of [KI03], stated at n = 3, Λ = 0, 2M = m₀ and with their curvature constant K = 1 (spherical orbits), so that
their f is ours and their x is ς; page numbers are those of the arXiv version. Their frequency-domain form is
[[thm:s15-ki]]; here the time-domain form is needed.

**Theorem {#thm:rw-ki}** ([KI03, (2.4)–(2.8), pp. 4–5; (2.13), p. 5; (3.11)–(3.14), pp. 9–10; (5.1)–(5.6), p. 13].)
Let k² = l(l + 2), 𝔭 := k² − 3 (the m of [KI03, (3.3)], and the number written p in [[thm:s15-ki]]; here p is the
exponent of [HKW18]'s r^p hierarchy, [[thm:rw-hkw]] (P)), H := 𝔭 + 6ς, Q the polynomial [[eq:s15-ki-q]] with 𝔭 in
place of p, and V_S := fQ/(16r²H²).

(S) For a scalar mode of degree l ≥ 2, with the variables of [KI03, (2.4)] and the gauge invariants F, F_ab of
[KI03, (2.7)], put F̃ := rF and F̃_ab := rF_ab [KI03, (2.13)]. The vacuum equations are equivalent to the master wave
equation □Φ − (V_S/f)Φ = 0 [KI03, (3.11)] for a function Φ on the orbit space, through the covariant expressions

    F̃ = (1/(12r²H)) [(2H − 3rf′)Φ̃ + 6r Dr · DΦ̃],
    F̃_ab + F̃ g_ab = (1/H)(D_aD_bΦ̃ − (1/2)(□Φ̃)g_ab),                                                     {#eq:np-10-1}

with Φ̃ := r^(3/2)HΦ [KI03, (3.13)–(3.14)]. Kodama and Ishibashi state that these expressions, inserted into the
perturbed Einstein equations, give linear combinations of the master wave equation and its derivatives, and that
"these equations are equivalent to the original perturbed Einstein equations" (p. 10).

(T) For a tensor mode, h = 2r²H_T T_ij dz^i dz^j with (Δ̂ + k_T²)T = 0, T trace-free and divergence-free and
k_T² = l(l + 2) − 2 [KI03, (5.1)–(5.2)]: "H_T is gauge-invariant by itself" (p. 13), and Φ := r^(3/2)H_T [KI03, (5.4)]
satisfies □Φ − (V_T/f)Φ = 0 with V_T = (f/r²)(k_T² + 2 + 3/4 + 9m₀/(4r²)) [KI03, (5.5)–(5.6)].

**Lemma {#lem:rw-potentials}** (The potentials.) Put W_S := V_S/f and W_T := V_T/f. Then

    r²W_S = k² + 3/4 − (39/4)ς − (72ς − 120ς²)/H + 288ς²f/H²,     r²W_T = k² + 3/4 + (9/4)ς.        {#eq:rw-potentials}

Both are smooth on {r > 0}, and for every j there is C_j, independent of l, with
|∂_r^j(W − (k² + 3/4)r⁻²)| ≤ C_jr^(−2−j) on {r ≥ r_h}, for W = W_S and W = W_T. In particular every r-derivative of W
is bounded on {r ≥ r_h} by C_j(1 + k²), and |V| ≤ C(1 + k²)r⁻² there.

*Proof.* Substitute 𝔭 = H − 6ς in [[eq:s15-ki-q]]: 16𝔭³ = 16H³ − 288ςH² + 1728ς²H − 3456ς³,
60𝔭² = 60H² − 720ςH + 2160ς², 36𝔭(𝔭 − 12)ς = 36ςH² − 432ς²H − 432ςH + 1296ς³ + 2592ς², and
(624𝔭 − 144)ς² = 624ς²H − 3744ς³ − 144ς². Adding these and 1296ς³,

    Q = 16H³ + (60 − 252ς)H² − (1152ς − 1920ς²)H + 4608ς²(1 − ς).

Divide by 16H² and use H = k² − 3 + 6ς: H + 15/4 − (63/4)ς = k² + 3/4 − (39/4)ς, which is the first formula, as
1 − ς = f. The second is k_T² + 2 = k². Each term of r²W − k² − 3/4 is a product of powers of ς, f and 1/H with
coefficients independent of l; on {r ≥ r_h}, 0 < ς ≤ 1, 0 ≤ f < 1 and 0 < 1/H ≤ 1/5 (H ≥ 𝔭 ≥ 5), and
∂_rς = −2ς/r, ∂_rf = 2ς/r, ∂_r(1/H) = 12ς/(rH²), so each r-derivative gains a factor r⁻¹ with constants independent
of l. H > 0 on {r > 0}, so W is smooth there. ∎

**Proposition {#prop:np-10-1}** (The Regge–Wheeler-type gauge and the master fields.) Let h be a smooth solution of
the linearised vacuum equations about g on the domain of outer communication, in the class, with the data [HKW18,
Theorem 2] requires on a slice Σ_0 of their decay foliation ([[thm:rw-hkw]]). Then:

(i) (Decomposition.) h = h_0 + h_S + h_T: h_0 is the l = 0 part, a change of mass plus a pure gauge solution; h_S and
h_T are the scalar- and tensor-type parts, h_S supported on the even harmonics l = 2, 4, … and h_T on l ≥ 2. There is
no vector-type part and no l = 1 part. (Whether only even l occur for the class tensor harmonics is not needed and not
shown.)

(ii) (The gauge.) For every scalar mode l ≥ 2 the gauge f_a = 0 = H_T is reached by the gauge vector ξ[h] of
[[eq:gd-1-1]], with orbit part X_aS, X_a = (r/k)(f_a + (r/k)D_aH_T), and angular part −(1/2)D̂𝓉, 𝓉 = 2r²H_TS/k²; it
is smooth wherever h is. In it the mode is h_S = F_abS dy^ady^b + 2r²FS γ, with F, F_ab its gauge invariants. The
tensor part needs no gauge: h_T = 2r²H_T T, H_T being gauge invariant.

(iii) (Reconstruction.) With Φ the master field of the mode, F and F_ab are given by [[eq:np-10-1]], and H_T = r^(−3/2)Φ
for the tensor type. With ψ := r^(3/2)Φ, so that Φ̃ = Hψ, every component of h_S and h_T in a chart regular at the
horizon (the ingoing chart (v, r)) and the orthonormal frame of the spheres is a combination of ∂_v²ψ, ∂_v∂_rψ,
∂_r²ψ, ∂_vψ, ∂_rψ, ψ and 𝔭ψ, with coefficients bounded on {r ≥ r_h} uniformly in l ([[lem:rw-coefficients]]): two
orbit-space derivatives, and the factor 𝔭 (two angular derivatives) through F and the trace of F_ab. In Φ itself, with
𝔭Φ counted as a jet as 𝔭ψ is, the coefficients of F̃ and F̃_ab are O(r^(3/2)), and in r^(−3/2)Φ, with 𝔭r^(−3/2)Φ
counted likewise, they are O(r³), uniformly in l, those powers being attained. Without that convention the bound is not
uniform in l: the coefficient of Φ in F̃, the 𝔭-term included, is r^(−1/2)(𝔭/6 + ς/2 − 6fς/H + 3f/4), of size k²r^(−1/2)
for large l.

(iv) (Decay.) In the gauge of (ii) for every l ≥ 2, fix the l = 0 part to h_0 = cK̄, K̄ = r⁻²dv² the change of mass
regular at the horizon (the static chart's ∂_m g = r⁻²dt_s² + r²(r² − m₀)⁻²dr² equals K̄ + ℒ_(ζ∂_v)g with ζ′ = (r²f²)⁻¹,
singular at r_h; the gauge h_0 = cK̄ is reached by the gauge vector Y[h_0] of [[eq:gd-1-2]], smooth wherever h_0 is).
Then h settles to cK̄ on each region {r ≤ R}, the horizon included, uniformly in l, in two data classes:

(iv-a) (The data class of [[thm:viii-2-2]].) Let h be a solution on N⁺, smooth up to Σ°; N⁺ reaches inside the horizon
(r_♭ < r_h). If the data h induces on Σ^IVP are, up to those of a linearised diffeomorphism, G-invariant data (γ̇, k̇)
of [[thm:viii-2-2]] (γ̇ ∈ H^(∞,(ℰ_0,ℓ_0))_b, k̇ ∈ H^(∞,(ℰ_0+1,ℓ_0+1))_b, solving the linearised constraints), then h +
cℒ_Vg, which is in the Regge–Wheeler-type gauge with l = 0 part cK_V, is the ġ_RW of [[thm:rw-settling]]; so c = ṁ, h =
ġ_RW on {r ≤ 2R₁}, and h − cK̄ = ġ_RW − ṁK_V everywhere. For every k, R′ and ε′ > 0,

    |h − cK̄|_k ≤ C ‖(γ̇, k̇)‖_(H^(k₁(k+2))) t_*^(−w+ε′)     on {r_♭ < r ≤ R′, t_* ≥ T′}:

every component, with k derivatives along ∂_v, ∂_r and the rotations, pointwise, the horizon included, uniformly in l
(no sum over modes is formed), with a loss of two derivatives and a constant depending on R′ (not shown to grow as a
power of R′).

(iv-b) ([HKW18]'s data class, with the red-shift datum.) Let h be smooth up to and including the future horizon, with
h_0 = cK̄. Put

    𝒟 := Σ_X I_(XΨ)(Σ_0),     X ∈ {1, T, T², Ω, Ω²},
    Q_0 := Σ_l ‖U_l‖² ∫_(Σ_0 ∩ {r ≤ R_H}) |∂_r²Φ_l|² dr,

𝒟 summed over the scalar and tensor master quantities Ψ of h ([[lem:rw-hkw-field]]), Ω standing for the six rotations
summed, Φ_l the master field of the mode l, ∂_r at fixed v (transversal to the horizon), U_l the harmonic that carries
the mode in h's components (S for the scalar type and T for the tensor type, as in (ii)), and R_H the radius of
[HKW18] below which Σ_0 is spacelike. Then for τ ≥ 0 and R ≥ R_H,

    ∫_(Σ_τ ∩ {r ≤ R}) Σ_j |(h − cK̄)_j|² dr dω ≤ C R⁵ (𝒟 + Q_0)(1 + τ)⁻²,                              {#eq:np-10-1-iv-b}

dω the measure of the unit sphere, the components (h − cK̄)_j taken in the chart (v, r) and the orthonormal frame of the
spheres,
C depending on m₀ and Σ_0 only, uniformly in l: the squared L² norm of the components, which are second derivatives of
the master fields, decays at [HKW18]'s energy rate for data with two more commutations. The scalar-type part of Q_0
cannot be dropped: with 𝒟 it is bounded by the left side at any one time, and it is not bounded by any sum of
I_(XΨ)(Σ_0) over products X of the Killing fields, for smooth h either ([[lem:np-10-1b]]). The tensor-type part can,
the tensor type's components 2r^(−3/2)Φ carrying no derivative of Φ.

So in the Regge–Wheeler-type gauge for l ≥ 2, with h_0 = cK̄, every metric component of h settles to the change of mass
cK̄ on each region {r ≤ R}, the horizon included: pointwise with all derivatives at the rate of [[thm:viii-2-2]] for
its data (iv-a), and at [HKW18]'s rate τ⁻² in energy against dr dω, uniformly in l with a constant growing as R⁵ and
the loss of two derivatives counted as in (iii), for [HKW18]'s data with the red-shift datum (iv-b). Uniformly in r
the energy statement fails; on the outgoing part of the leaves, {r ≥ R_H}, the components settle in the L² norm on the
spheres at fixed (τ, r), and pointwise with the data of [[thm:rwg-2-prime]], with the weights r^(−1/2) on the orbit block
and r^(1/2) on the angular block, weights that are attained ([[thm:rwg-1]], [[thm:rwg-2]], [[thm:rwg-2-prime]]).

**Lemma {#lem:rw-coefficients}** (The coefficients of the reconstruction.) In the ingoing chart (v, r), with
ψ = r^(3/2)Φ,

    rF = (𝔭/(6r²))ψ + ((ς − 12fς/H)/(2r²))ψ + (1/(2r))∂_vψ + (f/(2r))∂_rψ,

    rF_ab + rF g_ab = D_aD_bψ − (12ς/(rH))(δ^r_a∂_bψ + δ^r_b∂_aψ) + (ψ/H)D_aD_bH
                      − (1/2)g_ab(□ψ − (24ς/(rH))(∂_vψ + f∂_rψ) + (ψ/H)□H),

with D_vD_vu = ∂_v²u − (f′/2)∂_vu − (ff′/2)∂_ru, D_vD_ru = ∂_v∂_ru + (f′/2)∂_ru, D_rD_ru = ∂_r²u,
□u = 2∂_v∂_ru + f′∂_ru + f∂_r²u, and H′ = −12ς/r, H″ = 36ς/r². Every coefficient, but the 𝔭/(6r²) of rF, is a sum of
terms (number)·m₀^j H^a r^b with a ≤ 0 and b ≤ 0, the numbers independent of l, so bounded on {r ≥ r_h} uniformly in
l; the 𝔭/(6r²) enters rF_ab only through the trace, rFg_ab, and not rF_rr (g_rr = 0). In rF_rr the coefficient of ∂_r²ψ
is 1. In terms of Φ, with the jet 𝔭Φ taken apart (the term (𝔭/(6r²))ψ = (𝔭/6)r^(−1/2)Φ of rF), every coefficient is
O(r^(3/2)) uniformly in l, attained by ∂_r²Φ in rF_rr; in terms of r^(−3/2)Φ, with 𝔭r^(−3/2)Φ taken apart likewise,
O(r³), attained likewise. The coefficient of Φ in rF with the 𝔭-term included, r^(−1/2)(𝔭/6 + ς/2 − 6fς/H + 3f/4), is
not bounded uniformly in l.

*Proof.* In the chart (v, r), g_vv = −f, g_vr = 1, g_rr = 0 and g^(vv) = 0, g^(vr) = 1, g^(rr) = f; the only lowered
Christoffel symbols that do not vanish are Γ_(r,vv) = f′/2 and Γ_(v,vr) = −f′/2, which give the Hessian above. By
[[eq:np-10-1]], with Φ̃ = Hψ, Dr · DΦ̃ = ∂_vΦ̃ + f∂_rΦ̃ = H(∂_vψ + f∂_rψ) + fH′ψ, and 2H − 3rf′ = 2𝔭 + 6ς; this gives
rF, as 6rfH′/H = −72fς/H. For the second, D_aD_b(Hψ) = HD_aD_bψ + H′(δ^r_a∂_bψ + δ^r_b∂_aψ) + ψD_aD_bH and
□(Hψ) = H□ψ + 2H′(∂_vψ + f∂_rψ) + ψ□H; divide by H. The monomial structure is read off: f = 1 − m₀r⁻²,
f′ = 2m₀r⁻³, ς = m₀r⁻², H′/H, H″/H and D_aD_bH/H carry r⁻¹ or r⁻² and 1/H, and H ≥ 5. In ψ = r^(3/2)Φ, a derivative of
order j ≤ 2 of ψ is r^(3/2) times one of Φ plus lower-order terms with smaller powers of r, and 𝔭ψ = r^(3/2)(𝔭Φ); so
the coefficients in the jets of Φ, 𝔭Φ among them, are O(r^(3/2)), and the coefficient r^(3/2) of ∂_r²Φ in rF_rr = ∂_r²ψ +
2(H′/H)∂_rψ + (H″/H)ψ is attained; with ψ = r³(r^(−3/2)Φ) the same argument gives r³. Finally h_ab = F_abS = ((rF_ab +
rFg_ab) − rFg_ab)S/r, and the angular block of h_S in the orthonormal frame of the spheres is 2FSδ_ij = (2/r)(rF)Sδ_ij:
each component is r⁻¹ times a combination with the stated coefficients. For the tensor type the frame components of
2r²H_TT are 2H_T|T| with H_T = r^(−3)ψ. ∎

*Proof of [[prop:np-10-1]] (i)–(iii) and (iv-a).* (i) Every class tensor is h_0 plus the part with l ≥ 2, which by
[[lem:gd-1-2]] (c) consists of the orbit block h_ab − ⟨h_ab⟩, the mixed components h_(a·) = dβ_a and the angular block
2r²(H_L − ⟨H_L⟩)γ + (D̂D̂ − (1/3)γΔ̂)𝓉 + h^TT: scalar type, built from harmonics of [[lem:gd-1-2]] (a), which have even
degree, and the tensor type h^TT. The class carries no co-closed 1-form on S³ ([[lem:gd-1-2]] (c)), so there is no
vector-type part, and no harmonic of degree 1. The tensor type is supported in l ≥ 2 ([HKW18, Proposition 6, p. 14]:
"the components H_2, ĥ_α, and ĥ_αβ are necessarily supported in ℓ ≥ 2"). The domain of outer communication to the
future of Σ_0 has a simply connected orbit space, the region above a graph. DRic commutes with the SO(4)-average,
the rotations being isometries, so DRic(h_0) = (DRic h)_0 = 0 there; so by [[lem:gd-1-4]] (b), h_0 = cK̄ + ℒ_(Y[h_0])g
with c the linearised mass: a change of mass plus a pure gauge solution. This is [HKW18, Theorem 1, p. 3] in the
class, where its linearised rotations, of vector type l = 1, are absent.

(ii) is [[lem:gd-1-3]] (b) with (a); the gauge vector is smooth wherever h is, since β and 𝓉 are. For the tensor type,
[[thm:rw-ki]] (T). By [KI03, p. 5] the gauge invariants exist for k²(k² − 3) ≠ 0, that is l ≥ 2; the modes with l = 1
carry no physical degree of freedom ("This implies that there exist no physical degrees of freedom for l = 1",
[KI03, p. 7]) and are absent in the class anyway.

(iii) is [[thm:rw-ki]] (S) and (T) with [[lem:rw-coefficients]].

(iv) The formula for ∂_m g in the static chart (t_s, r) is the derivative of −(1 − m/r²)dt_s² + (1 − m/r²)⁻¹dr²;
with dv = dt_s + f⁻¹dr, K̄ = r⁻²dt_s² + 2r⁻²f⁻¹dt_s dr + r⁻²f⁻²dr², and by the formula for ℒ_(ζ∂_v)g in the proof of
[[lem:gd-1-4]] (b), with ζ = ζ(r), ℒ_(ζ∂_v)g = −2fζ′dv dr + 2ζ′dr² = −2fζ′dt_s dr, which removes the dt_s dr term for
ζ′ = (r²f²)⁻¹.

(iv-a) h induces (γ̇, k̇) plus the data of some ℒ_Zg, and cℒ_Vg induces those of ℒ_(cV)g. h + cℒ_Vg is G-invariant,
smooth up to Σ°, a linearised vacuum solution in the Regge–Wheeler-type gauge, its l = 0 part being cK̄ + cℒ_Vg = cK_V
([[eq:gd-0-1]]). By [[thm:rw-settling]] (d) with U = U^♯, for which Ω′_+ = N⁺ ([[lem:ix-1-2]]), h + cℒ_Vg = ġ_RW.
Comparing the l = 0 parts, c = ṁ. So h − cK̄ = ġ_RW − cℒ_Vg − cK̄ = ġ_RW − ṁK_V, and ℒ_Vg = 0 on {r ≤ 2R₁}. The
bound is [[thm:rw-settling]] (b). ∎

### [HKW18]'s data and the red-shift datum {#sec:rw-redshift}

We use the following parts of [HKW18] as stated, in addition to [[thm:std-hkw-decay]]; their n is 3, their M is
m₀/2, their μ is ς, their t is the static time t_s of [[sec:rw-setting]] up to an additive constant, and page numbers
are those of the arXiv version. Letters inside quotations are theirs: their K, X, Y and Z below are not the objects of
this chapter written with those letters.

**Theorem {#thm:rw-hkw}** ([HKW18, Theorem 1, p. 3; Theorem 2, (6)–(7), p. 4; (13), p. 5; (15)–(16), (19)–(20), p. 6;
(35)–(36), p. 8; (89), p. 29; Section 7.3 and (92), p. 30; p. 38; (114)–(116) and Lemma 11, p. 39; (124), p. 43;
(127)–(128), p. 46; (129)–(131), p. 47; (134), p. 49; (159)–(162), p. 58; (163)–(169), pp. 58–59; (173), p. 60; p. 61;
p. 67; Theorem 22, (183)–(184), pp. 68–69; (186), p. 69].)

(F) (The decay foliation.) With their null coordinates u = (1/2)(t − r_*) and v = (1/2)(t + r_*) (13) (their t and
r_*), which we write u_H and v_H, and L := ∂/∂v_H = ∂/∂t + ∂/∂r_* (92),
"Fixing radii r_1 and R_1 satisfying r_h < r_1 < r_P < R_1, we choose a Lipschitz hypersurface Σ_0 with the following
properties: Σ_0 intersects the future horizon H⁺ transversely and Σ_0 is spacelike in r_h ≤ r ≤ R_1, Σ_0 ∩ {r_1 ≤ r ≤
R_1} = {t = 0} ∩ {r_1 ≤ r ≤ R_1}, Σ_0 ∩ {R_1 ≤ r} = {u = −(1/2)(R_1)_*} ∩ {R_1 ≤ r} … Flowing along the static Killing
vector field T, we construct our decay foliation Σ_τ := φ_τ(Σ_0). We define n_(Σ_τ) as the unit timelike normal vector
for Σ_τ for r ≤ R_1 and n_(Σ_τ) := L for r > R_1" (p. 30), the volume form of the null part being r^n dv_H dVol_(S^n).
We write R_H for their radius R_1.

(E) (The energies.) For a symmetric trace-free two-tensor Ψ on the spheres, "Ť_ab[Ψ] := ∇_aΨ · ∇_bΨ −
(1/2)g_ab(∇_cΨ · ∇^cΨ)" (89), with the projected covariant derivative; their red-shift vector field Y, which we write
Y_H, has "Y|_(r=r_h) = −∂/∂R" (p. 38) and is extended "such that Y is causal and Y = 0 for r ≥ r_1"; N := T + Y_H is
"the strictly timelike red-shift multiplier", and "E^N_Ψ(Σ_τ) := ∫_(Σ_τ) J^N_a[Ψ]n^a_(Σ_τ) dVol_(Σ_τ), Ě^N_Ψ(Σ_τ) :=
∫_(Σ_τ) Ť_ab[Ψ]n^a_(Σ_τ)N^b dVol_(Σ_τ)" (115); by Lemma 11, E^N_Ψ(Σ_τ) ≈ Ě^N_Ψ(Σ_τ) (p. 39).

(B) (Boundedness and decay.) For Ψ solving any of the master equations (134), (149), (153), (174),
Ě^N_Ψ(Σ_τ) ≲ Ě^N_Ψ(Σ_0) (116) and, in spacetime dimension six and below, Ě^N_Ψ(Σ_τ) ≲ I_Ψ(Σ_0)/τ² (130). As (116) and
(130) these are their Theorems 12 and 18, which assume their comparison (111) and Lemma 13; for the master quantities
they are stated without further hypothesis in [HKW18, Theorem 2, (6)–(7), p. 4] ([[thm:std-hkw-decay]]) and Theorem 22,
(183)–(184), pp. 68–69, and it is in this form that they are used below. Here
"I_Ψ(Σ_0) := E²_(Ψ,L_KΨ)(Σ_0) + E^N_(Ψ,L_KΨ,L²_KΨ)(Σ_0)" (131), "with K := {T, Ω_i} ranging over the background Killing
fields" (129) (their K a set of Killing fields), the constants depending only on n and M. In the proof of (130),
with τ_k = 2^k, "there exist τ̃_k ∈ [τ_(k−1), τ_k] such that E¹_Ψ(Σ_(τ̃_k)) ≤ (C/τ_k)(E²_Ψ(Σ_(τ_(k−1))) +
Ě^N_Ψ(Σ_(τ_(k−1)))) ≤ (C/τ_k)(E²_Ψ(Σ_(τ_0)) + Ě^N_Ψ(Σ_(τ_0)))" (p. 47).

(P) (The r^p hierarchy.) "Φ := r^(n/2)Ψ" (124), and "E^p_Ψ(Σ_τ) := ∫_(Σ_τ∩{r≥R_1}) (r^(p−n)/(1 − μ)^k)
(|∇_LΦ|²/(1 − μ)) r^n dv dVol_(S^n)" (127), with an exponent k ≥ 0 fixed in their Proposition 15, which we write k_H.
Theorem 16: "For 1 ≤ p ≤ 2 and τ_1 < τ_2, we have the r^p-estimate: E^p_Ψ(Σ_(τ_2)) + (1/C)∫_(τ_1)^(τ_2)
(E^(p−1)_Ψ(Σ_τ) + (2 − p)A^(p−1)_Ψ(Σ_τ))dτ ≤ E^p_Ψ(Σ_(τ_1)) + CĚ^N_Ψ(Σ_(τ_1))" (128), A^(p−1) ≥ 0.

(M) (The master quantities.) The two-tensor portion ĥ_αβ of δg satisfies (134). For the scalar portion, in terms of
the quantities ȟ_AB, Ȟ of (159)–(162), "X = ȟ^t_t − 2Ȟ, Y = ȟ^r_r − 2Ȟ, Z = ȟ^r_t" (163); the vacuum equation
δĚ^r_t = 0 reads

    (k²/r² − ∂_r²f − n∂_rf/r)Z + f(∂_t∂_rX + ∂_t∂_rY) − ((n − 2)f/r + ∂_rf/2)∂_tX + (2f/r − ∂_rf/2)∂_tY = 0 (167);

Z̃ := (k²/r² − ∂_r²f − n∂_rf/r)⁻¹ (f(∂_rX + ∂_rY) − ((n − 2)f/r + ∂_rf/2)X + (2f/r − ∂_rf/2)Y) (168),
Φ := (nZ̃ − r(X + Y))/(r^(n/2−1)(k² − n + n(n + 1)μ/2)) (169), and the scalar master quantity is
Q^(+) := (r^(k_s)Φ)Y_αβ dx^αdx^β (173), with k_s = (4 − n)/2 (p. 61; their k) and Y_αβ := ∇̊_α∇̊_βY − (1/n)σ̊_αβΔ̊Y
(35), which satisfies Δ̊Y_αβ = (2n − ℓ(ℓ + n − 1))Y_αβ (36). "The estimates for the Q^(+) … are uniform in the angular
mode numbers ℓ and m" (p. 67), and the sum over the modes satisfies (186).

(1) [HKW18, Theorem 1]: "For the lower frequency portion δg_(ℓ<2) of δg, there exists a smooth co-vector X_(ℓ<2) on
the Schwarzschild-Tangherlini background, unique modulo Killing fields, and constants c, d_m such that
δg_(ℓ<2) = π_(X_(ℓ<2)) + cK + Σ_m d_mK_m" (5), their K and K_m being the linearised Myers–Perry solutions (p. 3).

(G) On the metric components: "It is expected that, after estimating the master quantities and making a suitable
choice of linearized gauge, the remaining linearized metric components can be controlled by the gauge-invariant master
quantities … We do not treat this matter in the current paper" (p. 4).

**Lemma {#lem:rw-hkw-field}** ([HKW18]'s master quantities in the class.) For h in the Regge–Wheeler-type gauge, the
master quantities of [HKW18] are, mode by mode, Ψ = r^(1/2)Φ𝒴 with Φ the master field of [[thm:rw-ki]]: for the scalar
type 𝒴 = Y_αβ := (D̂D̂ − (1/3)γΔ̂)S, with ‖Y_αβ‖² = (2/3)k²(k² − 3)‖S‖² ≥ (80/3)‖S‖², and for the tensor type 𝒴 = 2T.
Φ solves □Φ = WΦ with W = W_S or W_T of [[lem:rw-potentials]], and in the ingoing chart □ = 2∂_v∂_r + ∂_r(f∂_r)
([HKW18, (16)]). The pointwise norm of Ψ is r^(−3/2)|Φ||𝒴|, and the field r^(3/2)Ψ of (124), whose r^p energies (127)
[HKW18] bound, has norm |Φ||𝒴|.

*Proof.* The tensor type: ĥ_αβ = 2r²H_T T = 2r^(1/2)ΦT by [[thm:rw-ki]] (T). The scalar type: in the gauge
f_a = 0 = H_T, the quantities of [HKW18, (159)–(162)] are ȟ_AB = rF_AB and Ȟ = rF. By the trace of [[eq:np-10-1]],
g^(ab)rF_ab = −2rF, so X + Y = −6rF. In the static chart (t_s, r), in which ∂_r is taken at fixed t_s,
g_(t_s r) = 0 and Γ^(t_s)_(t_s r) = f′/(2f), so by [[eq:np-10-1]]
rF_(t_s r) = H⁻¹D_(t_s)D_rΦ̃ = H⁻¹∂_(t_s)(∂_rΦ̃ − (f′/(2f))Φ̃), and with ∂_rΦ̃ = r^(3/2)H(∂_rΦ + (3/(2r) − 12ς/(rH))Φ),

    Z = g^(rr)rF_(r t_s) = −∂_(t_s)Z̃_0,        Z̃_0 := r^(1/2)((ς − (3/2)f + 12fς/H)Φ − rf∂_rΦ).

By (167), in which their ∂_t is ∂_(t_s), Z = −∂_(t_s)Z̃ with Z̃ of (168). So E := Z̃ − Z̃_0, a linear expression in the
derivatives of Φ with coefficients depending on r alone, satisfies ∂_(t_s)E[Φ′] = 0 for every solution Φ′ of the
master equation near any point (each such solution gives a vacuum perturbation, [[thm:rw-ki]] (S)). Given a solution Φ
on a product {t_0 − δ < t_s < t_0 + δ, r ∈ J}, let Π solve the linear ordinary differential equation
(fΠ′)′ − WΠ = f⁻¹∂_(t_s)Φ(t_0, ·) on J; then Φ′ := ∫_(t_0)^(t_s) Φ(t″, ·)dt″ + Π solves the master equation (its defect
−f⁻¹∂_(t_s)²Φ′ + ∂_r(f∂_rΦ′) − WΦ′ has t_s-derivative □Φ − WΦ = 0 and vanishes at t_s = t_0), and ∂_(t_s)Φ′ = Φ. So
E[Φ] = E[∂_(t_s)Φ′] = ∂_(t_s)E[Φ′] = 0, and Z̃ = Z̃_0. In the static chart Dr · DΦ̃ = f∂_rΦ̃, and [[eq:np-10-1]] gives

    rF = (r^(−1/2)/12)((2H − 6ς + 9f − 72fς/H)Φ + 6rf∂_rΦ).

Hence 3Z̃ − r(X + Y) = 3Z̃_0 + 6r·rF = r^(1/2)HΦ, and (169) at n = 3, where k² − 3 + 6ς = H, gives back Φ. The
pointwise norm: |Y_αβ|_g = r⁻²|Y_αβ|_γ. The norm of Y_αβ is [[lem:gd-1-2]] (d). ∎

**Lemma {#lem:rwg-cone}** (The energies on the outgoing part.) Let Ψ = r^(1/2)Φ𝒴 be a master quantity of a mode, as in
[[lem:rw-hkw-field]], and f_1 := f(R_H). On the outgoing part C_τ := Σ_τ ∩ {r ≥ R_H}, with ∂_r at fixed u_H,

    ∫_(R_H)^∞ ((∂_rΦ)² + k²Φ²/r²) dr ≤ C_1 Ě^N_Ψ(Σ_τ)/‖𝒴‖²,        C_1 = 9/(2f_1) + 8,

and the same for T^aΨ = r^(1/2)(T^aΦ)𝒴, a ≥ 1, with T^aΦ in place of Φ, as T^aΦ solves the same master equation, T
being Killing. A rotation acts on the harmonic and not on Φ: Ω_iΨ = r^(1/2)Φ L_i𝒴, L_i the Lie derivative along Ω_i
on S³; it enters only through the identity Σ_i Ě^N_(Ω_iΨ) = λĚ^N_Ψ, mode by mode, with λ := k² for the scalar type and
λ := k² + 4 for the tensor type, which holds as well with T^aΨ or Ω_jΨ in place of Ψ, so that
Σ_i Ě^N_(Ω_iT^aΨ) = λĚ^N_(T^aΨ) and Σ_(i,j) Ě^N_(Ω_iΩ_jΨ) = λ²Ě^N_Ψ. On the spacelike part Σ_τ ∩ {r ≤ R_H},
Ě^N_Ψ(Σ_τ) ≥ c∫((∂_vΦ)² + (∂_rΦ)² + k²Φ²) dr ‖𝒴‖², with c > 0 depending on m₀ and Σ_0 only.

*Proof.* On C_τ, n_(Σ_τ) = L, and at fixed u_H, L = f∂_r (v_H − u_H = r_*) and dv_H = dr/f; N = T there, as Y_H = 0
for r ≥ R_H > r_1. From (89), with g(L, T) = −f and g̃⁻¹ = f⁻¹(−∂_(t_s)² + ∂_(r_*)²) on the orbit space,
Ť(L, T) = (1/2)|∇_LΨ|² + (f/(2r²))|∇̊Ψ|². For Ψ = r^(1/2)Φ𝒴, ∇_LΨ = r²L(r⁻²Ψ) = r²L(r^(−3/2)Φ)𝒴
= r^(1/2)f(∂_rΦ − 3Φ/(2r))𝒴, so |∇_LΨ|² = r⁻³f²(∂_rΦ − 3Φ/(2r))²|𝒴|² and r⁻²|∇̊Ψ|² = r⁻⁵Φ²|∇̊𝒴|², with |𝒴| and
|∇̊𝒴| taken in the metric of the unit sphere; and ∫_(S³) |∇̊𝒴|² dω = (k² − 6)‖𝒴‖² for the scalar type by (36),
(k² − 2)‖𝒴‖² for the tensor type by [KI03, (5.2)]. Integrating Ť(L, T) against r³dv_H dω = r³f⁻¹dr dω,

    Ě^N_Ψ(Σ_τ ∩ {r ≥ R_H}) = (1/2)∫_(R_H)^∞ (f(∂_rΦ − 3Φ/(2r))² + (k² − 6)Φ²/r²) dr ‖𝒴‖²

for the scalar type; for the tensor type the same holds with k² − 2 in place of k² − 6, so the right side is a lower
bound for both types.

With a := ∂_rΦ − 3Φ/(2r), (∂_rΦ)² ≤ 2a² + (9/2)Φ²/r², so the left side of the claim is at most
∫(2a² + (k² + 9/2)Φ²/r²)dr ≤ max(4/f_1, 2(k² + 9/2)/(k² − 6)) Ě/‖𝒴‖², and for k² ≥ 8,
2(k² + 9/2)/(k² − 6) ≤ 25/2 ≤ 9/(2f_1) + 8 and 4/f_1 ≤ 9/(2f_1) + 8, as f_1 ≤ 1. The rotations commute with the
equations and with the energy densities. On functions Σ_iΩ_i² = Δ̂ ([[lem:rwg-a]]), and the L_(Ω_i) commute with D̂,
so −Σ_iL_(Ω_i)² Y_αβ = k²Y_αβ. On symmetric 2-tensors on S³, −Σ_iL_(Ω_i)² = ∇̊*∇̊ + 𝒜 with 𝒜 algebraic: writing
L_(Ω_i) = ∇̊_(Ω_i) + (∇̊Ω_i)·, the second-order part is −Σ_i∇̊²_(Ω_i,Ω_i) = ∇̊*∇̊, as Σ_iΩ_i ⊗ Ω_i = γ (Lagrange's
identity) and Σ_i∇̊_(Ω_i)Ω_i = −(1/2)∇̊Σ_i|Ω_i|² = 0; and the first-order part vanishes, as for Ω = Ax (A antisymmetric)
the endomorphism ∇̊Ω is e ↦ P(Ae), P the tangential projection, and Σ_(a<b)(A_ab)_ij(A_ab)_kl = δ_ikδ_jl − δ_ilδ_jk
gives Σ_i (PA_ie) ⊗ (A_ix) = (e · x)P − (Px) ⊗ e = 0 for e tangent. 𝒜 is O(4)-equivariant, and the isotropy group O(3)
acts irreducibly on trace-free symmetric 2-tensors at a point, so 𝒜 is a constant on them; by (36), ∇̊*∇̊Y_αβ =
(k² − 6)Y_αβ, so 𝒜 = 6. On the tensor harmonics, ∇̊*∇̊T = k_T²T = (k² − 2)T ([KI03, (5.1)–(5.2)]), so
−Σ_iL_(Ω_i)²T = (k² + 4)T. As the L_(Ω_i) are skew on L²(S³) and commute with the operators in the energy density,
Σ_iĚ^N_(Ω_iΨ) is the eigenvalue λ of −Σ_iL_(Ω_i)² times Ě^N_Ψ. The same holds for T^aΨ, which carries the same 𝒴, and
for Ω_jΨ = r^(1/2)ΦL_j𝒴: L_j commutes with Σ_iL_(Ω_i)² (the sum is invariant under the adjoint action of SO(4)) and
maps the harmonics of degree l of each type to harmonics of degree l of that type, so L_j𝒴 lies in the same
eigenspace; summing over j gives Σ_(i,j)Ě^N_(Ω_iΩ_jΨ) = λΣ_jĚ^N_(Ω_jΨ) = λ²Ě^N_Ψ. On the spacelike part, N and n_(Σ_τ)
are timelike, uniformly on the compact set {r_h ≤ r ≤ R_H} of the leaf modulo the flow of T, so Ť(n, N) bounds c(|∇_vΨ|²
+ |∇_rΨ|² + r⁻²|∇̊Ψ|²); there ∇_AΨ = r²∂_A(r^(−3/2)Φ)𝒴, the angular term carries (k² − 6) ≥ k²/4, and the term in Φ/r of
∂_r(r^(−3/2)Φ) is absorbed by it. ∎

**Lemma {#lem:np-10-1a}** (The red-shift commutation for the class's master fields.) Let Φ be a smooth solution, up
to and including the future horizon, of □Φ = WΦ on {r ≥ r_h}, □ = 2∂_v∂_r + ∂_r(f∂_r), W the potential of a mode of
either type, and let v_Σ be the function with Σ_τ ∩ {r ≤ R_H} = {v = τ + v_Σ(r)}; 0 < v_Σ′ < 2/f, the leaves being
spacelike there. With u_j := ∂_r^jΦ (∂_r at fixed v), for the mode l put

    Q(τ) := ∫_(r_h)^(R_H) (1 − v_Σ′f/2) u_2²(τ + v_Σ(r), r) dr,     𝒟_l := I_Ψ(Σ_0) + Σ_(i,j) I_(Ω_iΩ_jΨ)(Σ_0).

Then Q(τ) ≤ C(Q(0) + 𝒟_l/‖𝒴‖²)(1 + τ)⁻², ‖𝒴‖ the L²(S³) norm of the harmonic in Ψ = r^(1/2)Φ𝒴, with C depending on m₀
and Σ_0 only. Summed over the modes with the weights ‖U_l‖² of Q_0,
∫_(Σ_τ ∩ {r ≤ R_H}) |∂_r²Φ|² dr dω ≤ C(Q_0 + 𝒟)(1 + τ)⁻², Φ := Σ_l Φ_lU_l for each type.

*Proof.* (1) The commutation. With L := ∂_v + (f/2)∂_r, the outgoing null direction, □ = 2L∂_r + f′∂_r, so the
equation is the transport Lu_1 + (f′/2)u_1 = Wu_0/2. Since [∂_r, L] = (f′/2)∂_r, applying ∂_r^j gives

    Lu_(j+1) + ((j + 1)f′/2)u_(j+1) = F_j,                                                                 {#eq:np-10-1a}

F_j a combination of u_0, …, u_j with coefficients built from derivatives of f and W and no v-derivative; for j = 1,
∂_r(Lu_1) = Lu_2 + (f′/2)u_2 and ∂_r((f′/2)u_1) = (f″/2)u_1 + (f′/2)u_2, so F_1 = (1/2)(W′u_0 + (W − f″)u_1). The top
coefficient (j + 1)f′/2 does not involve W (Leibniz on Wu_0 reaches u_j only), and at the horizon it is
(j + 1)/r_h > 0, (j + 1) times the surface gravity. This is the red-shift commutation of Dafermos and Rodnianski
([DR08, Theorem 7.2, p. 87 of the arXiv version]); in 1 + 1 dimensions it is exact.

(2) The energy identity. For u = u_(j+1), 2u · [[eq:np-10-1a]] and 2uLu = ∂_v(u²) + ∂_r((f/2)u²) − (f′/2)u² give

    ∂_v(u²) + ∂_r((f/2)u²) + ((2j + 1)f′/2)u² = 2uF_j.                                                     {#eq:np-10-1b}

Integrate over {τ_1 ≤ v − v_Σ(r) ≤ τ_2, r_h ≤ r ≤ R_H} in the (v, r)-plane. The leaves carry the flux density
(1 − v_Σ′f/2)u² dr, positive as they are spacelike; the horizon carries none (f = 0), and {r = R_H} the outgoing flux
(f/2)u² ≥ 0. With j = 1, b := 3m₀/R_H³ ≤ 3f′/2 on [r_h, R_H], Q(w) ≤ ∫u_2² dr on Σ_w, and
2|uF_1| ≤ (b/2)u² + (2/b)F_1²,

    Q(τ_2) + (b/2)∫_(τ_1)^(τ_2) Q(w) dw ≤ Q(τ_1) + (2/b)∫_(τ_1)^(τ_2) G(w) dw,
    G(w) := ∫_(r_h)^(R_H) F_1²(w + v_Σ(r), r) dr.

(3) The forcing. |W′| + |W − f″| ≤ C(1 + k²) on [r_h, R_H] ([[lem:rw-potentials]]), and u_0, u_1 are bounded in L² on
the spacelike part by Ě^N_Ψ ([[lem:rwg-cone]]). So G(w) ≤ C(1 + k²)²Ě^N_Ψ(Σ_w)/‖𝒴‖² ≤ C(Ě^N_Ψ + Σ_(i,j)
Ě^N_(Ω_iΩ_jΨ))(Σ_w)/‖𝒴‖² ≤ C𝒟_l(1 + w)⁻²/‖𝒴‖², by [[lem:rwg-cone]] and (B) of [[thm:rw-hkw]] with Lemma 11.

(4) Gronwall. A continuous Q ≥ 0 satisfying the inequality of (2) for all τ_1 ≤ τ_2 satisfies
Q(τ) ≤ e^(−bτ/2)Q(0) + (2/b)∫_0^τ e^(−b(τ−w)/2)G(w) dw: the right side R(τ) satisfies the inequality with equality, so
d := Q − R has d(0) = 0 and d(τ_2) + (b/2)∫_(τ_1)^(τ_2)d ≤ d(τ_1); if d(τ) > 0, then from the last zero τ′ < τ of d,
d(τ) ≤ −(b/2)∫_(τ′)^τ d < 0, a contradiction. And for c > 0,
∫_0^τ e^(−c(τ−w))(1 + w)⁻² dw ≤ C_c(1 + τ)⁻², C_c = max(1, 16e^(c/2−2)/c²) + 4/c: split at τ/2; the part over
[0, τ/2] is at most e^(−cτ/2) ≤ max(1, 16e^(c/2−2)/c²)(1 + τ)⁻² (the maximum of e^(−cτ/2)(1 + τ)² over τ ≥ 0), and
the part over [τ/2, τ] at most (1 + τ/2)⁻²/c ≤ 4(1 + τ)⁻²/c. Also e^(−bτ/2) ≤ C_(b/2)(1 + τ)⁻². Since
c_Σ ∫u_2² dr ≤ Q, c_Σ := min (1 − v_Σ′f/2) > 0, this is the lemma for the mode; every constant is uniform in l. Multiply
by ‖U_l‖²: for the tensor type U_l and the harmonic in Ψ are one harmonic up to the factor 2, and for the scalar type
‖Y_αβ‖² ≥ (80/3)‖S‖² ([[lem:rw-hkw-field]]); with Σ_l ‖U_l‖²Q_l(0) ≤ Q_0 and the orthogonality of the harmonics, the
sum gives the rest. ∎

**Lemma {#lem:np-10-1b}** (The red-shift datum cannot be dropped.) (a) For every τ ≥ 0 there is C(τ) with
Q(0) ≤ C(τ)(Q(τ) + (𝒟_l + I_(TΨ)(Σ_0) + Σ_i I_(Ω_iΨ)(Σ_0))/‖𝒴‖²), ‖𝒴‖ as in [[lem:np-10-1a]]. For the scalar type the
left side of [[eq:np-10-1-iv-b]] at any one time bounds the red-shift datum (in rF_rr the coefficient of ∂_r²ψ is 1,
[[lem:rw-coefficients]]); the tensor type's components, 2r^(−3/2)Φ, carry no derivative of Φ.

(b) For each mode of either type and each σ with 1/2 < σr_h ≤ 3/2, σr_h ≠ 1, there are solutions of □Φ = WΦ, smooth
on {r > r_h}, with every I_(XΨ)(Σ_0) finite, X any product of T and the rotations, and Q(0) = ∞; for them Q(τ) = ∞
for every τ. So, for the scalar type, no bound of the left side of [[eq:np-10-1-iv-b]] by [HKW18]'s data, commuted
with the Killing fields any number of times, holds up to the horizon, for smooth h either: the scalar-type part of Q_0
is the one input their class lacks, and nothing weaker than it suffices.

*Proof.* (a) An outgoing null ray r = ρ(v), ρ′ = f/2, carries no flux of [[eq:np-10-1b]]: along it the flux density
u²ρ′ − (f/2)u² vanishes. So the identity on the region between Σ_0, Σ_τ, the horizon and the ray from (Σ_0, ρ_1), ρ_1
close enough to r_h that the ray stays below R_H until Σ_τ, has no outer term. With 2|uF_1| ≤ u² + F_1² and
3f′/2 ≤ 3/r_h it gives q(w) ≤ q(τ) + C∫_w^τ q + C∫_w^τ G, for q the integral of (1 − v_Σ′f/2)u_2² between the horizon
and the ray, and Gronwall backward in time gives q(0) ≤ e^(Cτ)(q(τ) + C∫_0^τ G). On [ρ_1, R_H] the equation,
f∂_r²Φ = WΦ − 2∂_r(TΦ) − f′∂_rΦ with f ≥ f(ρ_1) > 0, bounds ∂_r²Φ on Σ_0 by the energies of Ψ, TΨ and the
Ω_iΩ_jΨ. For the scalar type, by [[lem:rw-coefficients]], ∂_r²ψ = rF_rr − 2(H′/H)∂_rψ − (H″/H)ψ, and the lower terms
are bounded by the energies; so the left side of [[eq:np-10-1-iv-b]] at time τ, with 𝒟, bounds Q(τ).

(b) Take Φ_* := e^(−σv)R(r). The equation becomes fR″ + (f′ − 2σ)R′ − WR = 0; at r_h,
f = (2/r_h)(r − r_h) + O((r − r_h)²), and the indicial roots are 0 and σr_h. Take R = (r − r_h)^(σr_h)(1 + O(r − r_h)),
the convergent Frobenius series of the larger root, continued to (r_h, ∞) as a solution of the equation: the
coefficients of the equation divided by f are analytic near r_h with a simple pole there, and the recursion's
denominators (2/r_h)n(n + σr_h) do not vanish for n ≥ 1. Fix r_h < ρ_0′ < ρ_0 < R_H and a smooth χ_0(r), equal to 1 on
{r ≤ ρ_0′} and to 0 on {r ≥ ρ_0}, and let Φ be the solution whose data on Σ_0 are those of χ_0Φ_*. It is smooth on
{r > r_h}, since the past of each of its points meets Σ_0 there, and it equals Φ_* on the part of the future of Σ_0
in {r > r_h} where v < v_Σ(ρ_0′): v does not increase along a past directed causal curve, so such a curve from a point
there meets Σ_0 where v_Σ(r) < v_Σ(ρ_0′), that is r < ρ_0′, and that part is in the domain of dependence of
Σ_0 ∩ {r < ρ_0′}. On Σ_0 near the horizon T^aΦ = (−σ)^aΦ, and R and R′ ~ (r − r_h)^(σr_h−1) are square integrable
(σr_h > 1/2), so every I_(XΨ)(Σ_0) is finite; but R″ ~ σr_h(σr_h − 1)(r − r_h)^(σr_h−2), whose coefficient is not 0
(σr_h ≠ 1), is not square integrable (σr_h ≤ 3/2): Q(0) = ∞.

*Approximation.* The bounds (B) of [[thm:rw-hkw]] and Lemma 11 are stated for solutions smooth up to and including the
horizon, and Φ is not one. They extend to it, as follows. Write the data of Φ on the spacelike part of Σ_0 as
a(r) := Φ(v_Σ(r), r) and b(r) := ∂_vΦ(v_Σ(r), r), r_h < r ≤ R_H: they vanish for r ≥ ρ_0, a, a′ and b are square
integrable, and a(r)² ≤ C(r − r_h)^(2σr_h). For n with r_h + 2/n < ρ_0′ let χ_n be smooth, 0 on [r_h, r_h + 1/n] and 1
on [r_h + 2/n, ∞), with 0 ≤ χ_n ≤ 1 and |χ_n′| ≤ 2n; let Φ_n be the solution with data (χ_na, χ_nb) on the spacelike part
of Σ_0 and 0 on its null part, and Ψ_n := r^(1/2)Φ_n𝒴.

(i) Φ_n is smooth up to and including the future horizon: its data are smooth and vanish near the horizon, and the
master equation is a linear wave equation whose coefficients are smooth across {r = r_h} in the chart (v, r)
([[thm:std-bgp-cauchy]]). So (B) and Lemma 11 hold for Ψ_n and for each difference Ψ_n − Ψ_m.

(ii) On the spacelike part of a leaf, Ě^N_Ψ lies between c and C times ∫((∂_vΦ)² + (∂_rΦ)² + k²Φ²) dr ‖𝒴‖² (the
lower bound is [[lem:rwg-cone]]; the upper bound holds as N and n_(Σ_τ) are bounded there), and on Σ_0,
∂_rΦ = a′ − v_Σ′b. The data of Φ − Φ_n are ((1 − χ_n)a, (1 − χ_n)b), supported in [r_h, r_h + 2/n]. The integrals of
((1 − χ_n)a)², ((1 − χ_n)a′)² and ((1 − χ_n)b)² tend to 0, and
∫(χ_n′a)² dr ≤ 4n² ∫_(r_h)^(r_h+2/n) C(r − r_h)^(2σr_h) dr ≤ C′n^(1−2σr_h) → 0, as 2σr_h > 1. So the energy of the data
of Ψ − Ψ_n on Σ_0 tends to 0, and Ě^N_(Ψ_n−Ψ_m)(Σ_0) → 0 as n, m → ∞.

(iii) Φ_n = Φ on the part of the future of Σ_0 on or to the right of the outgoing null ray from the point of Σ_0 with
r = r_h + 2/n: that part is the domain of dependence of Σ_0 ∩ {r ≥ r_h + 2/n}, a past directed causal curve from one of
its points staying to the right of the ray, and the two solutions have the same data there. On Σ_w this part is
{r ≥ ρ_n(w)}, and ρ_n(w) → r_h as n → ∞ for each w, the outgoing ray from the point of Σ_0 on the horizon being the
horizon itself.

(iv) By (B) for Ψ_n − Ψ_m and (ii), Ě^N_(Ψ_n−Ψ_m)(Σ_w) ≤ CĚ^N_(Ψ_n−Ψ_m)(Σ_0) → 0, uniformly in w ≥ 0. So on each leaf
Φ_n converges in the norm that Ě^N defines, which on the spacelike part is that of ∂_vΦ, ∂_rΦ and Φ in L²(dr), and on
the null part Φ_n = Φ for n large, by (iii); and by (iii) the limit is Φ on Σ_w ∩ {r > r_h}. Hence, for every w ≥ 0,

    Ě^N_Ψ(Σ_w) = lim_n Ě^N_(Ψ_n)(Σ_w) ≤ C lim_n Ě^N_(Ψ_n)(Σ_0) = CĚ^N_Ψ(Σ_0) ≤ CI_Ψ(Σ_0),

the last by Lemma 11 at Σ_0, a comparison of two quadratic forms in the data that passes to the limit. Likewise
Ě^N_(Ψ_n−Ψ)(Σ_t) → 0 uniformly in t ≥ 0.

*Q(τ) = ∞.* For τ > 0 run (a)'s argument between the outgoing rays from (Σ_0, r_h + ε) and from (Σ_0, ρ_1), both of
which carry no flux and stay in {r_h < r < R_H} until Σ_τ, so that Φ is smooth on the region between them. It gives
q_ε(0) ≤ e^(Cτ)(q_ε(τ) + C∫_0^τ G), q_ε the integral of (1 − v_Σ′f/2)u_2² between the two rays and
G(w) ≤ C(1 + k²)²Ě^N_Ψ(Σ_w)/‖𝒴‖² ≤ C(1 + k²)²I_Ψ(Σ_0)/‖𝒴‖² by [[lem:rwg-cone]] and (iv), a bound independent of ε. As
ε → 0, q_ε(0) → ∞, so q_ε(τ) → ∞, and q_ε(τ) ≤ Q(τ).

*For smooth h.* Let χ ≥ 0 be smooth, not identically 0, with support in (0, t_0), 0 < t_0 < v_Σ(ρ_0′) − v_Σ(r_h), and
let Φ̄_n := ∫χ(t)Φ_n∘φ_t dt and Φ̄ := ∫χ(t)Φ∘φ_t dt, φ_t the flow of T. The Φ̄_n are solutions smooth up to and
including the horizon, and they converge to Φ̄ in every I_(XΨ)(Σ_0). Each T falls on χ: T^aΦ̄_n =
(−1)^a∫χ^((a))(t)Φ_n∘φ_t dt, and the energy on Σ_0 of Φ_n∘φ_t − Φ∘φ_t is Ě^N_(Ψ_n−Ψ)(Σ_t), φ_t being an isometry that
maps Σ_0 to Σ_t, so the energies of T^a(Φ̄_n − Φ̄) on Σ_0 are at most (∫|χ^((a))|)² sup_(0≤t≤t_0) Ě^N_(Ψ_n−Ψ)(Σ_t) → 0 by
(iv). The rotations act within the mode and multiply these energies by λ or λ² ([[lem:rwg-cone]]). The r^p energies of
the differences on the null part of Σ_0 vanish for n large, as Φ_n = Φ on the null parts of the Σ_t, 0 ≤ t ≤ t_0, by
(iii). Near the horizon on Σ_0, φ_t maps the points of Σ_0 into {v < v_Σ(ρ_0′)} for 0 ≤ t ≤ t_0, where Φ = Φ_*, so there
Φ̄ = (∫χ(t)e^(−σt) dt)Φ_*, a positive multiple of Φ_*: Q(0) = ∞ for Φ̄. The Q(0) of the Φ̄_n tend to ∞: for each ρ ∈
(r_h, R_H) the part of Q(0) over [ρ, R_H] converges, as there f∂_r²Φ = WΦ − 2∂_r(TΦ) − f′∂_rΦ with f ≥ f(ρ) > 0 expresses
u_2 through first derivatives of Φ and TΦ, which converge in L²; and for Φ̄ that part tends to ∞ as ρ → r_h. A bound of
the left side of [[eq:np-10-1-iv-b]] by the data would bound the Q(0) of the Φ̄_n by (a), the perturbations built from
them being smooth up to and including the horizon and in the class. ∎

*Proof of [[prop:np-10-1]] (iv-b).* By [[lem:rw-hkw-field]] the master quantities of [HKW18] are Ψ = r^(1/2)Φ𝒴, and
(B) of [[thm:rw-hkw]] with Lemma 11 gives Ě^N_(XΨ)(Σ_τ) ≤ CI_(XΨ)(Σ_0)(1 + τ)⁻² for each X, which commutes with their
equations, its fields being Killing; the constant is uniform in l ((M) of [[thm:rw-hkw]]). By
[[prop:np-10-1]] (iii) every component in the chart (v, r) and the orthonormal frame of the spheres is a combination of
∂_v²ψ, ∂_v∂_rψ, ∂_r²ψ, ∂ψ, ψ and 𝔭ψ with coefficients bounded on {r ≥ r_h} uniformly in l, so O(r^(3/2)) in the
jets of Φ, 𝔭Φ counted among them. On the spacelike part, ∂_v²Φ = ∂_v(TΦ) and ∂_r∂_vΦ = ∂_r(TΦ) are bounded in L² by
Ě^N_(TΨ), k²Φ, and with it 𝔭Φ (0 < 𝔭 < k²), by Σ_iĚ^N_(Ω_iΨ) = λĚ^N_Ψ ≥ k²Ě^N_Ψ ([[lem:rwg-cone]]), and
∂_r²Φ by [[lem:np-10-1a]], the horizon included ([[lem:rwg-cone]]). On the outgoing part (f ≥ f_1), with
∂_r|_v = ∂_r|_u − (2/f)T, they are bounded by Ě^N_(T²Ψ), Ě^N_(TΨ), Ě^N_(ΩΨ) and the equation, which gives ∂_r²Φ at
fixed u ([[eq:rwg-master]] below); there the zeroth-order terms carry the weight r⁻² in [[lem:rwg-cone]], which costs
R² on {R_H ≤ r ≤ R}, and the squared coefficients cost R³: C R⁵. The tensor type is the same, with Ψ = 2r^(1/2)ΦT and
components 2r^(−3/2)Φ, which carry no derivative. h_0 − cK̄ = 0 by the gauge condition. Summing over the modes with the
orthogonality of the harmonics and ‖S‖² ≤ (3/80)‖Y_αβ‖² gives [[eq:np-10-1-iv-b]]. That the scalar-type part of Q_0
cannot be dropped is [[lem:np-10-1b]]. ∎

### Uniformly in r {#sec:rw-uniform}

The statements on the regions {r ≤ R} have constants growing with R. This section decides what holds uniformly in r,
on the outgoing part of [HKW18]'s leaves.

*Notation.* r_* and the static time t_s are those of [[sec:rw-setting]], so that v = t_s + r_*; r_* differs from the
r_* of [HKW18], normalised by r_*(r_P) = 0, by a constant. Put u := t_s − r_*; u and v are 2u_H and 2v_H up to
constants. In the outgoing chart (u, r), g = −f du² − 2 du dr + r²γ and T = ∂_(t_s) = ∂_u. A scalar mode of the class has
harmonic S = P_j(cos 2ϑ), l = 2j ≥ 2, master field Φ(u, r), and in the gauge of [[prop:np-10-1]] (ii) it is h = F_abS
dy^ady^b + 2r²FSγ with [[eq:np-10-1]]. The orthonormal frame of the static observers on {r > r_h} is e_0 =
f^(−1/2)∂_(t_s) = f^(−1/2)∂_u, e_1 = f^(1/2)∂_r|_(t_s) = f^(1/2)∂_r − f^(−1/2)∂_u, and the unit frame e_i of the sphere
of radius r, in which h(e_i, e_j) = 2FSδ_ij. The master equation □Φ = W_SΦ, with □ = −2∂_u∂_r + ∂_r(f∂_r) in this chart,
reads

    2f∂_rTΦ = f∂_r(f∂_rΦ) − VΦ,        V = V_S.                                                         {#eq:rwg-master}

Its jets are Φ, TΦ, T²Φ, ∂_rΦ, ∂_rTΦ, ∂_r²Φ, ∂_r at fixed u. The leaves of [[thm:rw-hkw]] (F) meet {r ≥ R_H} in the
outgoing cones C_τ := {u = u_τ, r ≥ R_H}, u_τ = u_0 + τ.

**Lemma {#lem:rwg-1}** (The components on the outgoing chart.) With ∂_r²Φ eliminated by [[eq:rwg-master]],

    r^(1/2)·2F = −TΦ + f∂_rΦ + ((2𝔭 + 6ς + 9f − 72fς/H)/(6r))Φ,
    h(e_0, e_1) = r^(1/2)S (−f⁻¹T²Φ + ∂_rTΦ − r⁻¹(ς/f − 3/2 + 12ς/H)TΦ),
    h(e_0, e_0) = r^(1/2)S (f⁻¹T²Φ + r⁻¹(ς/f − 2 + 12ς/H)TΦ + r⁻¹(2f − ς − 12fς/H)∂_rΦ + r⁻²a_00Φ),
    h(e_1, e_1) = r^(1/2)S (f⁻¹T²Φ + r⁻¹(ς/f − 1 + 12ς/H)TΦ + r⁻¹(f − ς − 12fς/H)∂_rΦ + r⁻²a_11Φ),

with a_00 := (2/3)H + 3 − (19/2)ς − (42ς − 66ς²)/H + 144ς²f/H² and a_11 := H/3 + 3/2 − 7ς − (30ς − 54ς²)/H + 144ς²f/H².
In particular: (i) the coefficient of T²Φ in h(e_0, e_0), h(e_0, e_1), h(e_1, e_1) is r^(1/2)/f, −r^(1/2)/f, r^(1/2)/f,
and T²Φ does not occur in h(e_i, e_j); the coefficient of TΦ in 2F is −r^(−1/2); ∂_rTΦ occurs only in h(e_0, e_1).
(ii) Every coefficient of r^(−1/2)h(e_a, e_b) (a, b ∈ {0, 1}) and of r^(1/2)·2F is f^(−1) times a finite sum of terms
H^α r^β (times powers of m₀) with α ≤ 0, except that the coefficient of Φ carries α ≤ 1 (the factor 𝔭, two angular
derivatives), and the largest β are

    jet                T²Φ      ∂_rTΦ    TΦ      ∂_rΦ     Φ
    orbit block         0         0      −1      −1      −2
    angular block     absent    absent    0       0      −1

the 0's being attained by T²Φ in h(e_0, e_0) and by TΦ in 2F. On {r ≥ R_H}, f⁻¹ ≤ (1 − m₀/R_H²)⁻¹, so r^(−1/2)h(e_a, e_b)
and r^(1/2)h(e_i, e_j) are bounded by the jets with the weights r^β, uniformly in r ≥ R_H and in l (5 ≤ H ≤ (11/8)k²).

*Proof.* In the chart (u, r), g_uu = −f, g_ur = −1, g_rr = 0, and the Christoffel symbols that do not vanish are
Γ^u_uu = −f′/2, Γ^r_uu = ff′/2 and Γ^r_ur = f′/2; so D_uD_u = ∂_u² + (f′/2)∂_u − (ff′/2)∂_r,
D_uD_r = ∂_u∂_r − (f′/2)∂_r, D_rD_r = ∂_r², □ = −2D_uD_r + fD_rD_r and Dr · DΦ̃ = −∂_uΦ̃ + f∂_rΦ̃. A symmetric
B has B(e_0, e_0) = f⁻¹B_uu, B(e_0, e_1) = B_ur − f⁻¹B_uu, B(e_1, e_1) = fB_rr − 2B_ur + f⁻¹B_uu. Write Φ̃ = ρΦ,
ρ := r^(3/2)H; with H′ = −12ς/r, ρ′/ρ = 3/(2r) − 12ς/(rH) and ρ″/ρ = 3/(4r²) (ρ = 𝔭r^(3/2) + 6m₀r^(−1/2)). The
first line is [[eq:np-10-1]], with rF = (r^(−1/2)/12)((2H − 6ς + 9f − 72fς/H)Φ − 6rTΦ + 6rf∂_rΦ). Put
A_ab := H⁻¹(D_aD_bΦ̃ − (1/2)(□Φ̃)g_ab), trace-free, so A(e_1, e_1) = A(e_0, e_0); by [[eq:np-10-1]],
h(e_a, e_b) = r⁻¹S(A(e_a, e_b) − rF g(e_a, e_b)), with g(e_0, e_0) = −1, g(e_1, e_1) = 1 and g(e_0, e_1) = 0. In
f⁻¹D_uD_uΦ̃ − D_uD_rΦ̃ the terms in ∂_rΦ and Φ cancel:

    f⁻¹D_uD_uΦ̃ − D_uD_rΦ̃ = ρ(f⁻¹T²Φ − ∂_rTΦ + (f′/(2f) − ρ′/ρ)TΦ).

So A(e_0, e_1) = −(ρ/H)(f⁻¹T²Φ − ∂_rTΦ + (f′/(2f) − ρ′/ρ)TΦ), which gives h(e_0, e_1) with f′/(2f) = ς/(rf). And
A(e_0, e_0) = H⁻¹(f⁻¹D_uD_uΦ̃ − D_uD_rΦ̃ + (f/2)D_rD_rΦ̃), where (f/2)ρ∂_r²Φ = ρ∂_rTΦ − (f′/2)ρ∂_rΦ + (ρW/2)Φ by
[[eq:rwg-master]]; the ∂_rTΦ terms cancel and

    A(e_0, e_0) = r^(3/2)(f⁻¹T²Φ + (f′/(2f) − ρ′/ρ)TΦ + (fρ′/ρ − f′/2)∂_rΦ + (W/2 + fρ″/(2ρ))Φ).

Adding and subtracting rF and inserting r²W from [[eq:rw-potentials]] gives h(e_0, e_0) and h(e_1, e_1); for instance
the coefficient of Φ in r^(3/2)h(e_0, e_0)/S is r²W/2 + 3f/8 + (2H − 6ς + 9f − 72fς/H)/12 = a_00, using
k² = H + 3 − 6ς and f = 1 − ς. (i) and (ii) are read off: the coefficients of TΦ and ∂_rΦ in the orbit block carry
r^(−1/2) = r^(1/2)r⁻¹, those of Φ carry r^(−3/2) and a factor H, and those of the angular block r⁰ and r⁻¹. Finally
H = k² − 3 + 6ς ≤ k² + 3 ≤ (11/8)k² for k² ≥ 8. ∎

**Theorem {#thm:rwg-1}** (Uniformly in r the statement fails.) For every τ_1 ≥ 0, every even l ≥ 2 and every
(A, B) ∈ ℝ² there is a smooth linearised vacuum solution h about g, on the future of Σ_0 in the exterior and up to the
future horizon, in the class, consisting of the single scalar mode l in the gauge f_a = 0 = H_T (no l = 0 part, no
tensor part), such that

(i) its master quantity has I_(XΨ)(Σ_0) < ∞ for every X a product of T and the rotations (all orders);

(ii) on C_(τ_1), with Φ_uu(r) := T²Φ(u_(τ_1), r) = B + (A/2)∫_r^∞ (V/f) dr′,

    h(e_i, e_j) = −Ar^(−1/2)Sδ_ij,        h(e_0, e_0) = r^(1/2)f⁻¹Φ_uu(r)S + c_A(r)AS,

with c_A = −(2𝔭r⁴ − 3𝔭m₀r² − 6m₀²)/(r^(1/2)(r² − m₀)(𝔭r² + 6m₀)) = O(r^(−1/2)), and for A = 0:

    h(e_0, e_0) = Br^(1/2)f⁻¹S,   h(e_0, e_1) = −Br^(1/2)f⁻¹S,   h(e_1, e_1) = Br^(1/2)f⁻¹S,   h(e_i, e_j) = 0.

In particular, for B ≠ 0, sup_(Σ_(τ_1)) |h(e_0, e_0)| = ∞ and ∫_(R_H)^∞ r⁻²‖h(e_0, e_0)‖² dr = ∞ on that leaf, while
I_Ψ(Σ_0) < ∞: no estimate sup_(Σ_τ) |h(e_a, e_b)| ≤ C(τ)𝒟^(1/2), and no estimate of ∫r⁻²‖h(e_a, e_b)‖² dr along the
leaf, holds at any τ, whatever the data norm 𝒟 built from the energies of [[thm:rw-hkw]]. For A ≠ 0,
r^(1/2)|h(e_i, e_j)| = |A||S| on C_(τ_1), so the weight r^(1/2) of [[thm:rwg-2]] (c) on the angular block is attained.

*Proof.* Step 1 (the Kruskal form of the master equation). Put 𝒰 := −e^(−u/r_h) and 𝒱 := e^(v/r_h). Then
−𝒰𝒱 = e^(2r_*/r_h) = F(r) := e^(2r/r_h)(r − r_h)/(r + r_h), and F′(r) = 2r²e^(2r/r_h)/(r_h(r + r_h)²) > 0 on (0, ∞),
F(0) = −1, F → ∞; so r is a smooth function of 𝒰𝒱 on {𝒰𝒱 < 1}. With ∂_u = −(𝒰/r_h)∂_𝒰 and ∂_v = (𝒱/r_h)∂_𝒱, the
orbit metric is −f du dv and the master equation 4∂_u∂_vΦ + VΦ = 0 becomes ∂_𝒰∂_𝒱Φ = 𝔠Φ with

    𝔠 := −(r_h²/4)(V/f)(f/(−𝒰𝒱)) = −(r_h²/4) W_S (r + r_h)² e^(−2r/r_h)/r²,

smooth wherever r > 0. The past horizon is {𝒱 = 0}, the future horizon {𝒰 = 0}, and C_(τ_1) lies on {𝒰 = 𝒰_1},
𝒰_1 := −e^(−u_(τ_1)/r_h).

Step 2 (the Goursat problem). Let g(𝒰) := α(𝒰 − 𝒰_1) + (β/2)(𝒰 − 𝒰_1)², and on each rectangle
Q = [𝒰_−, 𝒰_+] × [0, 𝒱_+] with 𝒰_− ≤ 𝒰_1 ≤ 𝒰_+ and 𝒰_+𝒱_+ < 1 consider

    Φ(𝒰, 𝒱) = g(𝒰) + ∫_(𝒰_1)^𝒰 ∫_0^𝒱 𝔠(𝒰′, 𝒱′)Φ(𝒰′, 𝒱′) d𝒱′ d𝒰′                                         {#eq:rwg-goursat}

(signed integrals). Its n-th Picard iterate differs from the previous one by at most
sup_Q|g| (M|𝒰 − 𝒰_1|𝒱)^n/(n!)², M := sup_Q|𝔠|, by induction; so [[eq:rwg-goursat]] has a unique continuous
solution on Q, which is smooth (differentiate [[eq:rwg-goursat]] repeatedly), and the solutions on nested rectangles
agree. The union of these rectangles contains the exterior {𝒰 < 0, 𝒱 > 0}, the future horizon and a neighbourhood of
it inside. This gives a smooth Φ with ∂_𝒰∂_𝒱Φ = 𝔠Φ, Φ(𝒰, 0) = g(𝒰) and Φ(𝒰_1, 𝒱) = 0.

Step 3 (the jets on C_(τ_1)). On 𝒰 = 𝒰_1, Φ = 0, so ∂_𝒱^kΦ = 0 for every k; ∂_𝒱∂_𝒰Φ = 𝔠Φ = 0 gives
∂_𝒰Φ = g′(𝒰_1) = α there, and ∂_𝒱∂_𝒰²Φ = ∂_𝒰(𝔠Φ) = (∂_𝒰𝔠)Φ + 𝔠∂_𝒰Φ = 𝔠α, so
∂_𝒰²Φ(𝒰_1, 𝒱) = β + α∫_0^𝒱 𝔠(𝒰_1, 𝒱′)d𝒱′. In the chart (u, r) the coordinate field ∂_u is T, which in the chart (u, v)
is ∂_u + ∂_v = (𝒱∂_𝒱 − 𝒰∂_𝒰)/r_h; so

    r_h²T² = 𝒱²∂_𝒱² + 𝒱∂_𝒱 − 2𝒰𝒱∂_𝒰∂_𝒱 + 𝒰²∂_𝒰² + 𝒰∂_𝒰,

and on 𝒰 = 𝒰_1, where ∂_𝒱Φ = ∂_𝒱²Φ = 0 and ∂_𝒰∂_𝒱Φ = 0, T²Φ = (𝒰_1²∂_𝒰²Φ + 𝒰_1∂_𝒰Φ)/r_h². (The operator
(𝒰²∂_𝒰² + 𝒰∂_𝒰)/r_h² alone is the second u-derivative at fixed v, not at fixed r; on C_(τ_1) the two agree on Φ by
these vanishings, and nowhere else is the formula used.) Along C_(τ_1), ∂_r at fixed u is a multiple of ∂_𝒱, so
Φ = ∂_rΦ = ∂_r²Φ = 0 there, and TΦ = −𝒰_1∂_𝒰Φ/r_h = A := −𝒰_1α/r_h; then ∂_rTΦ = 0 by [[eq:rwg-master]], and its
u-derivative gives 2f∂_rT²Φ = −VA, so T²Φ = B + (A/2)∫_r^∞ (V/f)dr′, the integral finite as V/f = O(r⁻²), B being its
limit at null infinity. Along C_(τ_1), d𝒱 = (𝒱/r_h)dv and dv = 2dr/f, so
∫_0^∞|𝔠(𝒰_1, 𝒱)|d𝒱 = (r_h/(2|𝒰_1|))∫(V/f)dr < ∞, and letting 𝒱 → ∞ in the formula for T²Φ on C_(τ_1),

    B = (𝒰_1²(β + α∫_0^∞ 𝔠(𝒰_1, 𝒱)d𝒱) + 𝒰_1α)/r_h²,

affine in β with slope 𝒰_1²/r_h² ≠ 0; every (A, B) is reached by choosing α and then β.

Step 4 (the metric). With S = P_(l/2)(cos 2ϑ), [[eq:np-10-1]] applied to ΦS gives h in the gauge f_a = 0 = H_T; it is
a linearised vacuum solution by [[thm:rw-ki]] (S). It is smooth up to the future horizon, because Φ is smooth in
(𝒰, 𝒱) and 𝒰 = −e^(−v/r_h)F(r), 𝒱 = e^(v/r_h) are smooth functions of the ingoing chart (v, r) there; it is in the
class because S depends on ϑ alone. [[lem:rwg-1]] and the jets of Step 3 give (ii): the coefficient of TΦ in
h(e_0, e_0) is r^(−1/2)(ς/f − 2 + 12ς/H) = c_A, and the angular block is r^(−1/2)(−TΦ)Sδ_ij.

Step 5 (the data). On Σ_0 ∩ {r ≤ R_H} the solution is smooth on a compact set, so every energy there is finite. On
C_0 = Σ_0 ∩ {r ≥ R_H} (u_0 ≤ u_(τ_1)): the rotations act within the mode, so it suffices to take X = T^a. Each T^aΦ
solves the master equation (T = (𝒱∂_𝒱 − 𝒰∂_𝒰)/r_h is Killing), with data on {𝒱 = 0} and on {𝒰 = 𝒰_1} that are bounded
(on 𝒰 = 𝒰_1 they are the T^aΦ found below, bounded along the cone). On the strip u_0 ≤ u ≤ u_(τ_1),
∫∫|𝔠| d𝒰 d𝒱 = (1/4)∫∫V du dv = (1/2)(u_(τ_1) − u_0)∫_(r_h)^∞ (V/f)dr < ∞, so the Picard bound of Step 2 gives
sup|T^aΦ| < ∞ on the strip. Along u = u_0, integrating 4∂_u∂_vΦ = −VΦ in u,

    ∂_vT^aΦ(u_0, v) = ∂_vT^aΦ(u_(τ_1), v) + (1/4)∫_(u_0)^(u_(τ_1)) VT^aΦ du′;

the first term is (f/2)∂_rT^aΦ on C_(τ_1), and the second is O(r⁻²), V being O(r⁻²) uniformly for u in a compact
interval at fixed v. On C_(τ_1) the T^aΦ =: Φ_a are determined by Φ_0 = 0, Φ_1 = A through the u-derivatives of
[[eq:rwg-master]], ∂_rΦ_(a+1) = (1/2)∂_r(f∂_rΦ_a) − (1/2)r⁻²qΦ_a, q := r²V/f = r²W_S, which is analytic in 1/r at
null infinity ([[eq:rw-potentials]], H → 𝔭 ≥ 5); if Φ_a = c_a + O(1/r) and ∂_rΦ_a = O(r⁻²) as convergent power series
in 1/r, then ∂_rΦ_(a+1) = O(r⁻²) and Φ_(a+1) = c_(a+1) + O(1/r). So for every a, ∂_rT^aΦ = O(r⁻²) and T^aΦ = O(1) on
C_0, and every energy in I_(XΨ)(Σ_0), which on C_0 is bounded by ∫r^p(∂_rT^aΦ)² dr with p ≤ 2 and by
∫((∂_rT^aΦ)² + k²(T^aΦ)²/r²) dr ([[lem:rwg-cone]], [[thm:rw-hkw]] (P)), is finite. For τ_1 = 0 the strip is empty. ∎

In words: on [HKW18]'s leaves, which run out to null infinity, the gauge f_a = 0 = H_T puts T²Φ, the radiation of the
master field, into the orbit-space components with the weight r^(1/2) ([[lem:rwg-1]] (i)).

**Lemma {#lem:rwg-s}** (A weighted Hardy-type bound.) If w is a C¹ function on [R, ∞) with
∫_R^∞ (w²/ϱ² + w′²) dϱ < ∞, then

    sup_(r≥R) w(r)²/r ≤ 2(∫_R^∞ w²/ϱ² dϱ)^(1/2)(∫_R^∞ w′² dϱ)^(1/2) + ∫_R^∞ w²/ϱ² dϱ;

and if ∫_R^∞ (w² + w′²) dϱ < ∞, then sup w² ≤ 2(∫w²)^(1/2)(∫w′²)^(1/2).

*Proof.* d(w²/ϱ)/dϱ = 2ww′/ϱ − w²/ϱ², and liminf_(ϱ→∞) w²/ϱ = 0, for otherwise w²/ϱ² ≥ c/ϱ would not be integrable.
Integrate from r to a sequence ϱ_n → ∞ along which w²/ϱ_n → 0 and apply Cauchy–Schwarz. For the second,
d(w²)/dϱ = 2ww′ and liminf |w| = 0. ∎

**Theorem {#thm:rwg-2}** (What holds uniformly in r.) Let h be a perturbation of the class in the gauge of
[[prop:np-10-1]] (ii) for every l ≥ 2, with h_0 = cK̄, and Ψ_l the master quantities of its modes. On {r ≥ R_H} write
h_(ab) := (h − cK̄)(e_a, e_b) and h_(ij) := (h − cK̄)(e_i, e_j), the frame components of h − cK̄, ‖·‖ the L²(S³) norm at
fixed (τ, r), the argument (τ, r) meaning the point of C_τ at radius r, and

    𝒟 := Σ_l Σ_X I_(XΨ_l)(Σ_0),        X ∈ {1, T, T², Ω, TΩ, Ω²},

Ω standing for each of the six rotations Ω_i and Ω² for each product Ω_iΩ_j, all summed; Ě^N_(ΩΨ), Ě^N_(TΩΨ) and
Ě^N_(Ω²Ψ) below are summed in the same way. Then, with C depending on m₀ and R_H only, for τ ≥ 1 and every 0 < δ ≤ 1/2:

    (a) ∫_(R_H)^∞ (r⁻³‖h_(ab)‖² + r⁻¹‖h_(ij)‖²)(τ, r) dr ≤ C 𝒟 τ⁻²,
    (b) sup_(r≥R_H) (r⁻¹‖h_(ab)‖ + ‖h_(ij)‖)(τ, r) ≤ C 𝒟^(1/2) τ⁻¹,
    (c) sup_(r≥R_H) (r^(−1/2)‖h_(ab)‖ + r^(1/2)‖h_(ij)‖)(τ, r) ≤ C δ^(−1/2) 𝒟^(1/2) τ^(δ−1/2).

The integral in (a) is against dr dω, dω the measure of the unit sphere; against the leaf's own volume form
r³f⁻¹dr dω it is false (for the family of [[thm:rwg-1]], ∫r⁻³|h(e_0, e_0)|²r³f⁻¹ dr = B²‖S‖²∫rf⁻³ dr = ∞). The
weights in (c) are the exact growth and decay of [[thm:rwg-1]] and cannot be raised; in (a), r⁻³ cannot be replaced by
r⁻². The subtraction of cK̄ is needed: K̄(e_a, e_b) = 1/(r² − m₀) for a, b ∈ {0, 1} and K̄(e_i, e_j) = 0, and as the
class harmonics of degree l ≥ 2 have mean zero, ‖h(e_a, e_a)‖² = ‖h_(aa)‖² + 2π²c²/(r² − m₀)², which does not decay for c
≠ 0.

*Proof.* Step 1 is [[lem:rwg-cone]]: on C_τ, for a ≤ 2, ∫((∂_rT^aΦ)² + k²(T^aΦ)²/r²) dr ≤ C_1Ě^N_(T^aΨ)(Σ_τ)/‖𝒴‖²,
and for the energies commuted with rotations Σ_iĚ^N_(Ω_iT^aΨ) = λĚ^N_(T^aΨ) and Σ_(i,j)Ě^N_(Ω_iΩ_jΨ) = λ²Ě^N_Ψ, with
λ = k² for the scalar type and k² + 4 for the tensor type, so λ ≥ k². By [[thm:rw-hkw]] (B) applied to XΨ for each X
in the list defining 𝒟, Ě^N_(XΨ)(Σ_τ) ≤ CI_(XΨ)(Σ_0)τ⁻².

Step 2, (a). By [[lem:rwg-1]] and [[eq:rwg-master]], r^(−3/2)h_(ab) and r^(−1/2)h_(ij) are, mode by mode, combinations
of T²Φ, TΦ and Φ with coefficients O(r⁻¹) (times H ≤ (11/8)k² for Φ), and of ∂_rTΦ and ∂_rΦ with coefficients O(1),
uniformly in l. So, with ‖S‖² ≤ (3/80)‖Y_αβ‖², the left side of (a) is bounded by C times the sum over a ≤ 2 of the
left sides of Step 1 for T^aΨ and the term C∫H²Φ²/r² dr ‖S‖². That term is bounded by the Ω-commuted energy:
H² ≤ (11/8)²k⁴, and k²∫k²Φ²/r² dr ≤ C_1k²Ě^N_Ψ/‖𝒴‖² ≤ C_1Σ_iĚ^N_(Ω_iΨ)/‖𝒴‖². Hence the bound C𝒟τ⁻².

Step 3, (b). Apply [[lem:rwg-s]] with Step 1, mode by mode. For w = T^aΦ (a ≤ 2), ∫w²/ϱ² ≤ (1/8)∫k²w²/ϱ², so
sup r^(−1/2)|T^aΦ| ≤ C(Ě^N_(T^aΨ)/‖𝒴‖²)^(1/2). For w = k²Φ, ∫w²/ϱ² ≤ C_1k²Ě^N_Ψ/‖𝒴‖² ≤ C_1Ě^N_(ΩΨ)/‖𝒴‖² and
∫w′² ≤ C_1k⁴Ě^N_Ψ/‖𝒴‖² ≤ C_1Ě^N_(Ω²Ψ)/‖𝒴‖², so sup r^(−1/2)k²|Φ| ≤ C((Ě^N_(ΩΨ) + Ě^N_(Ω²Ψ))/‖𝒴‖²)^(1/2).
For w = ∂_rT^aΦ (a ≤ 1), w′ = ∂_r²T^aΦ = (2/f)∂_rT^(a+1)Φ − (f′/f)∂_rT^aΦ + (V/f²)T^aΦ by [[eq:rwg-master]], and
|V| ≤ Ck²r⁻² ([[lem:rw-potentials]]), so sup|∂_rT^aΦ| ≤ C((Ě^N_(T^aΨ) + Ě^N_(T^(a+1)Ψ) + Ě^N_(T^aΩΨ))/‖𝒴‖²)^(1/2). Each
is at most C𝒟^(1/2)τ⁻¹ by Step 1. [[lem:rwg-1]] (ii), with the weight r⁻¹ on the orbit block and r⁰ on the angular
block, puts every term under one of these suprema with a bounded coefficient.

Step 4, (c). The new input is sup|T²Φ| and sup|TΦ|, the terms of weight r⁰ in [[lem:rwg-1]] (ii); the others are
handled by Step 3. For w = T^aΦ (a = 1, 2) on C_τ and p := 1 + 2δ,

    |w(r)| ≤ |w(R_H)| + ∫_(R_H)^∞|w′| ≤ R_H^(1/2) sup r^(−1/2)|w| + (∫ϱ^pw′²)^(1/2)(R_H^(1−p)/(p − 1))^(1/2).

The first term is at most C𝒟^(1/2)τ⁻¹ by Step 3. For the second: on the cone, by [[thm:rw-hkw]] (P) and
[[lem:rw-hkw-field]], the field r^(3/2)Ψ has norm |Φ||𝒴|, L = f∂_r and dv_H = dr/f, so
E^p_(T^aΨ) = ∫r^pf^(−k_H)(∂_rT^aΦ)² dr ‖𝒴‖², and ∫ϱ^pw′² ≤ E^p_(T^aΨ)/‖𝒴‖². By Hölder's inequality with
ϱ^p = ϱ^(2−p)(ϱ²)^(p−1), E^p ≤ (E¹)^(2−p)(E²)^(p−1). By (128) at p = 2 and Lemma 11,
E²_(T^aΨ)(Σ_τ) ≤ E²_(T^aΨ)(Σ_0) + CĚ^N_(T^aΨ)(Σ_0) ≤ CI_(T^aΨ)(Σ_0). For τ ∈ [τ̃_k, τ̃_(k+1)], (128) at p = 1 from τ̃_k,
the bound on E¹(Σ_(τ̃_k)) in (B) and (130) give E¹_(T^aΨ)(Σ_τ) ≤ C(τ_k⁻¹ + τ̃_k⁻²)𝒟 ≤ C𝒟/τ, as τ ≤ τ_(k+1) = 2τ_k and
τ̃_k ≥ τ_k/2. So the second term is at most Cδ^(−1/2)𝒟^(1/2)τ^(−(2−p)/2) = Cδ^(−1/2)𝒟^(1/2)τ^(−1/2+δ).

The tensor type. Its frame components are 2H_TT = 2r^(−3/2)Φ_TT, two powers of r^(1/2) better than the angular block
of the scalar type; Step 1 and [[lem:rwg-s]] give (a)–(c) for it directly, and it is included in h_(ij). The l = 0
part: h_0 − cK̄ = 0 by the gauge condition. The mode sum: every constant above is uniform in l, and
‖h_(ab)‖² = Σ_l‖h_(ab),l‖², with the supremum over r of a sum at most the sum of the suprema; so (a)–(c) for the modes
add up to (a)–(c) for h. The frame components of K̄ follow from dv(e_0) = dv(e_1) = f^(−1/2). ∎

The proof uses the class only through three properties: there is no vector-type part, no l = 1 part, and h_0 = cK̄.
[[lem:rwg-1]] holds for every scalar harmonic, its formulas seeing S only through k², and the estimates of
[[thm:rw-hkw]] hold for every perturbation. So [[thm:rwg-2]] holds for every perturbation of scalar and tensor type with
l ≥ 2 in the gauge, class or not.

**Theorem {#thm:rwg-2-prime}** (The pointwise form.) With h as in [[thm:rwg-2]], put
𝒟′ := 𝒟[h] + Σ_i 𝒟[L_ih] + Σ_(i,j) 𝒟[L_iL_jh], L_i the Lie derivative along Ω_i and 𝒟[·] the 𝒟 of [[thm:rwg-2]] for
the perturbation in brackets; it is at most C Σ I_(XΨ)(Σ_0) over X = T^aΩ^b with a ≤ 2, b ≤ 4, a + b ≤ 4.
Then for τ ≥ 1 and 0 < δ ≤ 1/2, with C depending on m₀ and R_H only, |h_(ab)| the components as functions on S³ and
|h_(ij)| the norm of the angular block in the unit sphere's metric:

    (b′) sup_(r≥R_H, ω) (r⁻¹|h_(ab)| + |h_(ij)|)(τ, r, ω) ≤ C 𝒟′^(1/2) τ⁻¹,
    (c′) sup_(r≥R_H, ω) (r^(−1/2)|h_(ab)| + r^(1/2)|h_(ij)|)(τ, r, ω) ≤ C δ^(−1/2) 𝒟′^(1/2) τ^(δ−1/2).

*Proof.* At fixed (τ, r), h_(ab) is a function on S³ and h_(ij) is the symmetric tensor r⁻²(h − cK̄) restricted to the
sphere, in the unit metric. The rotations commute with e_0, e_1 and with the restriction to the sphere, so
Ω_iΩ_j(h_(ab)) = (L_iL_jh)_(ab) and L_iL_j(h_(ij)) = (L_iL_jh)_(ij). Each of L_ih and L_iL_jh is a linearised vacuum
solution in the same gauge (the gauge and the decomposition into types are SO(4)-equivariant), of scalar and tensor
type only, with modes l ≥ 2 only and no l = 0 part (L_i(cK̄) = 0). By the remark after [[thm:rwg-2]], (b)–(c) hold for
h, L_ih and L_iL_jh with the data 𝒟[h], 𝒟[L_ih] and 𝒟[L_iL_jh], and [[lem:rwg-a]] gives (b′)–(c′). ∎

The weights are sharp in the strongest sense available: the family of [[thm:rwg-1]] realises
r^(−1/2)h(e_0, e_0) = Bf⁻¹S and r^(1/2)h(e_i, e_j) = −ASδ_ij on a whole cone. The rates in (b)–(c) are what the energy
decay of [[thm:rw-hkw]] gives through [[lem:rwg-s]] and (128); they are not claimed sharp. A bounded change of frame
(any frame uniformly comparable to the static one on {r ≥ R_H}) leaves the conclusions unchanged; on {r ≤ R_H} the
statement for the regions {r ≤ R} is [[prop:np-10-1]] (iv). Nothing here concerns the harmonic gauge.

**Remark {#rem:rw-numerics}** (Numerical observation.) Evolving the master equations in time, no growing mode appears
in either type for l = 2, …, 10 up to τ = 275 r_h: on the region r_* ∈ [−20, 50] r_h, covered by the computed slices up
to that time, the field falls by at least five orders of magnitude within 150 r_h of the launch of the pulse and keeps
falling to 275 r_h. This is a finite-time observation; it excludes growth rates above ln(10⁵)/(150 r_h) ≈ 0.08/r_h and
not slower ones, and with the sign of the potential reversed the field grows. The late-time tail of the l = 2 master
fields, measured from the launch, is a power law with local exponent 7.05 for the tensor type (7.03 at half the step)
and 7.06 for the scalar type on τ ∈ [550, 700] r_h, approaching 7 from above (7.41, 7.22, 7.12, 7.07 on the four
earlier windows); shifting the time origin by the launch radius, 15 r_h, either way moves the exponent on
[550, 700] r_h to 6.89 and 7.23, so the limit 7 is resolved and the direction of approach is not. The l = 4 tensor
field gives 11.5 on [150, 250] r_h. This is the law Ψ ∼ t_s^(−(2l+D−2)) of [CYDL03, (14), p. 4] for odd D, 7 and 11 at
D = 5 (their own five-dimensional values are 7.1 and 11.4, [CYDL03, Fig. 2, p. 4]), the tail of the flat
five-dimensional Green's function rather than of the hole ([CYDL03, p. 4]). The least-damped of the modes tabulated in
[CLY03b, Tables 1–3, pp. 8–9] (l ≤ 4) is the scalar-type one with l = 2, σr_h = 0.9477 − 0.2561i for the time
dependence e^(−iσt_s) (the table prints 0.9477 + 0.2561i for the time dependence e^(iσt_s)), which the time evolution on
the scalar-type barrier reproduces to 1%: an e-folding time of 3.905 r_h. No proof in this paper uses these observations;
the rate proved for the class is that of [[thm:viii-2-2]] and [[thm:settling]].
