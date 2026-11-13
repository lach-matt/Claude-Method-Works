## The linear solution in a Regge–Wheeler-type gauge {#ch:rw-gauge}

[[thm:viii-2-2]] and [[cor:viii-2-3]] give, for every linearised data set in the class, a linearised vacuum
development in the gauge of the nonlinear problem which settles to a change of mass, and [[cor:ix-2-3]] shows that a
solution in any other gauge with the same data differs from it by a linearised diffeomorphism L_X g, about which
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
at the horizon ([[lem:np-10-1b]]), and it suffices, by a red-shift commutation that is exact in the class
([[lem:np-10-1a]]). Uniformly in r the statement fails: on the outgoing part of [HKW18]'s leaves the orbit-space
components can grow as r^(1/2) ([[thm:rwg-1]]), and with that weight, and only with it, they settle pointwise and
uniformly in r ([[thm:rwg-2]], [[thm:rwg-2-prime]]).

### Setting {#sec:rw-setting}

*The metric and the charts.* Throughout, g := g_(b₀), b₀ = (m₀, 0), is the five-dimensional Schwarzschild–Tangherlini
metric of mass m₀ in the coordinates (t, x) of [[sec:iii-b-3]]: g = Φ*_(m₀) g^KS_(m₀), with Φ_m(t, x) = (t − T_m(|x|), x)
and g^KS_m = η + m|x|⁻²(dt_KS + d|x|)² ([[eq:iii-b-3-3]], [[prop:iii-b-3-4]]). So r := |x| is the area radius of the
spheres {t = c, |x| = r}, and SO(4), acting on x, acts by isometries. Put

    v := t − T_(m₀)(r) + r   (that is, t_KS + r),     f := 1 − m₀/r²,     r_h := m₀^(1/2) = R₁,     ς := m₀/r².

On {r ≥ r_♭} (r_♭ ∈ (0, ½R₁] the inner radius of [[ch:s11]]), with γ = dϑ² + c²dφ1² + s²dφ2² the round metric of the
unit sphere (c := cos ϑ, s := sin ϑ, in the coordinates of [[sec:background]]),

    g = −f dv² + 2 dv dr + r² γ,                                                                         {#eq:rw-ingoing}

since −dt_KS² + d|x|² = −(dv − dr)² + dr² = −dv² + 2 dv dr. The surface gravity of the horizon {r = r_h} is
f′(r_h)/2 = m₀/r_h³ = 1/r_h. The function t_* of [[eq:iii-b-3-6]] has t_* − v = T_(m₀)(r) − ψ(r) − r, a function of r
alone; so on {r ≤ R′}, |t_* − v| ≤ C_(R′), and ∂_v = ∂_t = ∂_(t_*) at fixed x.

*The class.* G = O(2) × O(2) acts as in [[sec:class]]. In the coordinates (v, r, ϑ, φ1, φ2) the torus acts by
translation of φ1, φ2, so the components of a G-invariant tensor in the coordinate frame do not depend on φ1, φ2, and
the reflection φ_i ↦ −φ_i changes the sign of every component with an odd number of φ_i indices. So a G-invariant
symmetric 2-tensor has eight components, functions of (v, r, ϑ): h_ab, h_aϑ, h_ϑϑ, h_(φ1φ1), h_(φ2φ2) (a, b ∈ {v, r});
a G-invariant 1-form has X_v, X_r, X_ϑ. We write y^a for (v, r), z^i for the angles, D for the covariant derivative of
the orbit metric g_ab dy^a dy^b = −f dv² + 2 dv dr, □ := D^aD_a, and D̂, Δ̂ for the covariant derivative and Laplacian
of (S³, γ). "Class" means G-invariant.

*The mass change.* Put K := r⁻² dv² and K_V := ∂_m g_((m,0))|_(m=m₀), the change of mass of [[cor:viii-2-3]]. At fixed
(t_KS, x), ∂_m g^KS_m = |x|⁻²(dt_KS + d|x|)² = r⁻² dv², and Φ_(m+ε) = Φ_m ∘ φ_ε + O(ε²) with φ_ε(t, x) =
(t − ε ∂_mT_m(|x|), x), the flow of V := −(∂_mT_m)|_(m₀)(r) ∂_t. Hence

    K_V = K + ℒ_V g,        ℒ_V g = 0 on {r ≤ 2R₁},                                                         {#eq:gd-0-1}

since T_m(ϱ) = T_m(2R₁) for ϱ ≤ 2R₁ (χ_∞ = 0 there, [[eq:iii-b-3-3]]), so that V is a constant multiple of the Killing
field ∂_t there. V is smooth, stationary and spherically symmetric. K and K_V are linearised vacuum solutions: K is
the derivative in m of the Ricci-flat metrics −(1 − m/r²) dv² + 2 dv dr + r²γ at m₀, and DRic(ℒ_V g) = 0
([[lem:ix-2-1]] (b)).

*Part VIII's solution in the class.* Let (γ̇, k̇) be G-invariant data of [[cor:viii-2-3]], ġ its solution and ṁ its
mass change. ġ is G-invariant, smooth on the interior of N = {t_IVP ≥ −ν(r)}, with DRic(ġ) = 0 there, and its
restriction to N⁺ = M°_♭ ∩ {t_IVP ≥ 0} is smooth up to Σ° ([[lem:s29-g-on-n]], [[sec:ix-0]]). N and N⁺ are unions of
spheres, t_IVP = t − ψ_IVP(r) ([[lem:iii-b-3-7]] (b)). Put

    h := ġ − ṁ K_V,        w := α − 2,

so that w > 2 + ε_t by [[thm:viii-2-2]] (4). For a tensor field u put

    |u|_k(v, r) := Σ_(j≤k) sup_(S³_(v,r)) |D^j u|,

D^j ranging over the products of j of the operators ℒ_(∂_v), ℒ_(∂_r) (the coordinate fields of (v, r, x/r)) and the
Lie derivatives along the rotation fields Ω_ij = x^i∂_j − x^j∂_i, and |·| the Euclidean norm of the components in the
coordinates (t, x). On {r_♭ ≤ r ≤ R′} these operators and ∂_t, ∂_(x^i) span the same module over functions with bounded
derivatives, and ∂_t = t_*⁻¹ (t_*∂_(t_*)) at fixed x. So [[eq:viii-2-3]] with ḃ = (ṁ, 0) reads: for every k, R′ and
ε′ > 0 there are C, k₁ = k₁(k) and T′ with

    |h|_k ≤ C ‖(γ̇, k̇)‖_(H^(k₁)) t_*^(−w+ε′)     on {r_♭ ≤ r ≤ R′, t_* ≥ T′}.                              {#eq:gd-0-2}

We take T′ ≥ 0; then this set lies in N⁺, as t_IVP ≥ t_* there ([[cor:ix-2-3]]).

### The decomposition on the spheres {#sec:rw-spheres}

All operators below act on the sphere S³ at a point (v, r) of the orbit space, with (v, r) as parameters. For a
function u on S³ put ⟨u⟩ := |S³|⁻¹ ∫_(S³) u dω, |S³| = 2π², dω the measure of γ, and ‖·‖ the norm of L²(S³, dω). For a
class tensor h at (v, r) we write h_(a·) for the 1-form h_ai dz^i on S³, and h^TF for the γ-trace-free part of the
angular block h_ij dz^i dz^j. Its spherical harmonics are described by [[lem:gd-1-2]] (a) below, by which the
operator 𝒢 := [(2/3)Δ̂(Δ̂ + 3)]⁻¹ is defined on class functions of mean zero. We put:

- the *l = 0 part* h_0 := ⟨h_ab⟩ dy^a dy^b + 2r²⟨H_L⟩ γ, where H_L := γ^(ij)h_ij/(6r²);
- the *1-form potentials* β_a := Δ̂⁻¹ D̂^i h_ai, with ⟨β_a⟩ = 0;
- the *scalar potential* τ := 𝒢 D̂^iD̂^j h^TF_ij;
- the *tensor part* h^TT := h^TF − (D̂D̂ − (1/3)γΔ̂)τ.

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
of dimension (l + 1)², on which −Δ̂ = l(l + 2). For an L²-orthonormal basis Y_1, …, Y_((l+1)²) of it, Σ_m |Y_m(ω)|² does
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
Cartesian components T_AB (A, B = 1, …, 4) restrict to functions on S³ with Σ_(A,B) T_AB² = |T|². The rotations
preserve P, so the Lie derivative of the extension along Ω_i is the extension of L_iT, and in Cartesian components
Ω_i(T_AB) = (L_iT)_AB − (ωᵀT + Tω)_AB, ω the constant antisymmetric generator of Ω_i, of operator norm 1. So, with
|·|_F the Frobenius norm, |Ω_iT|_F ≤ |L_iT| + 2|T| and |Ω_iΩ_jT|_F ≤ |L_iL_jT| + 2|L_jT| + 2|L_iT| + 4|T|. Sum the
inequality for functions over (A, B), use (a + b + c + d)² ≤ 4(a² + b² + c² + d²) and count the six rotations: the
coefficient of ‖T‖² is 1 + 4 · 16 · 36 = 2305, that of Σ_i ‖L_iT‖² is 4 · 4 · 6 + 4 · 4 · 6 = 192, and that of
Σ_(i,j) ‖L_iL_jT‖² is 4. ∎

**Lemma {#lem:gd-1-2}** (The sphere.) (a) The T²-invariant spherical harmonics on S³ are the functions P_j(cos 2ϑ),
P_j the Legendre polynomials, with Δ̂P_j(cos 2ϑ) = −l(l + 2)P_j(cos 2ϑ), l = 2j; they are complete in the T²-invariant
part of L²(S³). So class functions carry only even l, and on their mean-zero part k² = l(l + 2) ≥ 8 and
(2/3)k²(k² − 3) ≥ 80/3: 𝒢 is defined.

(b) For every function τ, D̂^iD̂^j(D̂_iD̂_j − (1/3)γ_ijΔ̂)τ = (2/3)Δ̂(Δ̂ + 3)τ. So D̂^iD̂^jh^TT_ij = 0.

(c) A class 1-form on S³ with zero divergence vanishes, and every class 1-form on S³ is exact: there is no
vector-type part in the class, and h_ai dz^i = dβ_a. The divergence of a class symmetric 2-tensor is a class 1-form;
so D̂^ih^TT_ij = 0, and h^TT is transverse and trace-free (the tensor type).

(d) (Bounds uniform in l.) For a harmonic S of degree l, ‖D̂S‖² = k²‖S‖² and
‖(D̂D̂ − (1/3)γΔ̂)S‖² = (2/3)k²(k² − 3)‖S‖². Hence, for a class tensor h,

    ‖β_a‖_(H^1) ≤ (9/8)^(1/2) ‖h_(a·)‖,        ‖τ‖_(H^2) ≤ (243/80)^(1/2) ‖h^TF‖,

and, with constants independent of h and of l,

    sup|β_a| ≤ C|h_(a·)|_1,     sup|τ| ≤ C|h^TF|_0,     sup|D̂τ| ≤ C|h^TF|_1,

the same holding with any product D^j of ℒ_(∂_v), ℒ_(∂_r) and the rotations applied to both sides. Here |h_(a·)|_k and
|h^TF|_k are taken with the norm of the unit sphere; on {r_♭ ≤ r ≤ R′} each is at most C_(R′)|h|_k. No sum over
harmonics is formed.

*Proof.* (a) In the coordinates (ϑ, φ1, φ2), dω = cs dϑ dφ1 dφ2, and on functions of ϑ alone
Δ̂u = (cs)⁻¹∂_ϑ(cs ∂_ϑu) = (sin 2ϑ)⁻¹∂_ϑ(sin 2ϑ ∂_ϑu). With x := cos 2ϑ, ∂_ϑ = −2 sin 2ϑ ∂_x, so
sin 2ϑ ∂_ϑu = −2(1 − x²)∂_xu and Δ̂u = 4∂_x((1 − x²)∂_xu). Legendre's equation ((1 − x²)P_j′)′ = −j(j + 1)P_j gives
Δ̂P_j(cos 2ϑ) = −4j(j + 1)P_j = −2j(2j + 2)P_j. The T²-orbits are the level sets of ϑ, so T²-invariant functions are
functions of ϑ, and after the φ integrals dω = 4π² cs dϑ = π² dx; the Legendre polynomials are complete in L²(−1, 1).
For l = 2j ≥ 2, k² ≥ 8 and (2/3)k²(k² − 3) ≥ (2/3) · 8 · 5 = 80/3.

(b) On the unit S³, Ric = 2γ, so D̂^jD̂_iD̂_jτ = D̂_iΔ̂τ + 2D̂_iτ, and D̂^iD̂^jD̂_iD̂_jτ = Δ̂²τ + 2Δ̂τ. Subtracting
(1/3)Δ̂²τ gives (2/3)Δ̂² τ + 2Δ̂τ = (2/3)Δ̂(Δ̂ + 3)τ. D̂^iD̂^jh^TF_ij is a divergence, so of mean zero, and by
definition of τ, D̂^iD̂^jh^TT_ij = D̂^iD̂^jh^TF_ij − (2/3)Δ̂(Δ̂ + 3)τ = 0.

(c) A class 1-form on S³ is a(ϑ) dϑ: the components along dφ1, dφ2 have one φ_i index. Its divergence is
(cs)⁻¹∂_ϑ(cs a); if this vanishes, a = C/sin 2ϑ, and |a dϑ| = |a| is bounded near ϑ = 0 only if C = 0. For any class
1-form α let η be the mean-zero solution of Δ̂η = D̂^iα_i; η is a class function (Δ̂ commutes with G), so α − dη is
a class 1-form with zero divergence, hence 0. Every operator above is G-equivariant, so the divergence of a class
tensor is a class 1-form; by (b) D̂^ih^TT_ij has zero divergence, so it vanishes. For h_(a·): h_(a·) = dη_a with
Δ̂η_a = D̂^ih_ai, so η_a = β_a.

(d) Integrating by parts, ‖D̂S‖² = −⟨S, Δ̂S⟩ = k²‖S‖², and, with (b),
‖(D̂D̂ − (1/3)γΔ̂)S‖² = ⟨S, D̂^iD̂^j(D̂_iD̂_j − (1/3)γ_ijΔ̂)S⟩ = ⟨S, (2/3)Δ̂(Δ̂ + 3)S⟩ = (2/3)k²(k² − 3)‖S‖².
As h_(a·) = dβ_a, ‖h_(a·)‖² = Σ_l k²‖β_(a,l)‖², and ‖β_a‖²_(H^1) = Σ_l (1 + k²)‖β_(a,l)‖² ≤ (9/8)‖h_(a·)‖², since
(1 + k²)/k² decreases in k² ≥ 8. The two parts of h^TF are orthogonal:
⟨(D̂D̂ − (1/3)γΔ̂)τ, h^TT⟩ = ⟨τ, D̂^iD̂^jh^TT_ij⟩ = 0. So ‖h^TF‖² ≥ Σ_l (2/3)k²(k² − 3)‖τ_l‖², and
‖τ‖²_(H^2) ≤ (243/80)‖h^TF‖², since (1 + k²)²/((2/3)k²(k² − 3)) decreases in k² ≥ 8 (the logarithmic derivative in
x = k² is 2/(1 + x) − 1/x − 1/(x − 3) = (3 − 5x)/(x(1 + x)(x − 3)) < 0) and equals 243/80 at k² = 8.

The rotations are Killing fields of (S³, γ), so they commute with D̂, Δ̂, 𝒢 and the decomposition, and preserve the
degree. By [[lem:rwg-a]], sup|β_a|² ≤ (1/12)‖β_a‖²_(H^2), and
‖β_a‖²_(H^2) = Σ_l (1 + k²)²‖β_(a,l)‖² ≤ (9/8) Σ_l (k² + k⁴)‖β_(a,l)‖² = (9/8)(‖h_(a·)‖² + Σ_i ‖L_ih_(a·)‖²),
as Σ_i ‖L_i dβ_(a,l)‖² = Σ_i ‖dΩ_iβ_(a,l)‖² = k²Σ_i‖Ω_iβ_(a,l)‖² = k⁴‖β_(a,l)‖² by [[lem:rwg-a]]. The L² norms are at
most 2π² times the squared suprema. Likewise sup|τ|² ≤ (1/12)‖τ‖²_(H^2) ≤ C‖h^TF‖², and
sup|D̂τ|² = sup Σ_i (Ω_iτ)² ≤ (1/12) Σ_i ‖Ω_iτ‖²_(H^2) ≤ (1/12) Σ_l (1 + k²)³‖τ_l‖², which is at most
(243/80)(1/12)(‖h^TF‖² + Σ_i ‖L_ih^TF‖²), the projection of h^TF on its scalar-derived part being orthogonal and
commuting with the L_i. Finally ℒ_(∂_v) and ℒ_(∂_r) commute with every operator on the spheres, γ not depending on
(v, r). ∎

**Definition {#def:gd-1-1}** (The Regge–Wheeler-type gauge in the class.) A class tensor h is in the
*Regge–Wheeler-type gauge* if β_v = β_r = 0, τ = 0 and h_0 = cK_V for a constant c. When K replaces K_V in the last
condition we say *with the mass change K*; on {r ≤ 2R₁} the two conditions agree ([[eq:gd-0-1]]).

For a scalar mode the conditions β_a = 0, τ = 0 are Kodama and Ishibashi's f_a = 0 = H_T ([[lem:gd-1-3]] (b)).

**Lemma {#lem:gd-1-3}** (The gauge vector.) For a class tensor h put

    ξ[h] := (−β_a + (r²/2) ∂_a(τ/r²)) dy^a − (1/2) D̂τ.                                                    {#eq:gd-1-1}

(a) ℒ_(ξ[h]) g has the mixed components (ℒ_ξ g)_(aj) dz^j = −dβ_a, and its angular block has trace-free part
−(D̂D̂ − (1/3)γΔ̂)τ. So h + ℒ_(ξ[h])g has β = 0, τ = 0, the same h^TT as h, and the same l = 0 part.

(b) For a scalar mode of degree l ≥ 2 written as in [KI03, (2.4)–(2.6), p. 4],

    h_ab = f_ab S,  h_ai = r f_a S_i,  h_ij = 2r²(H_L γ_ij S + H_T S_ij),
    S_i = −D̂_iS/k,  S_ij = D̂_iD̂_jS/k² + γ_ijS/3,

one has β_a = −(r/k)f_a S and τ = 2r²H_TS/k²; the orbit part of ξ[h] is X_aS with Kodama and Ishibashi's
X_a = (r/k)(f_a + (r/k)D_aH_T) [KI03, (2.8), p. 5], and

    h + ℒ_(ξ[h]) g = F_ab S dy^a dy^b + 2r²F S γ,

with their gauge invariants F = H_L + H_T/3 + r⁻¹D^arX_a and F_ab = f_ab + D_aX_b + D_bX_a [KI03, (2.7), p. 5].

(c) (Uniqueness.) For a class 1-form Z with no l = 0 part, ξ[ℒ_Z g] = −Z. In particular ℒ_Z g has β = τ = 0 only if
Z = 0.

*Proof.* For g = g_ab dy^ady^b + r²γ the Christoffel symbols mixing the factors are Γ^a_ij = −r D^ar γ_ij and
Γ^i_aj = (∂_ar/r) δ^i_j, the others being those of the two factors. So for a 1-form ξ = ξ_a dy^a + ξ_i dz^i,

    (ℒ_ξg)_ab = D_aξ_b + D_bξ_a,   (ℒ_ξg)_ai = ∂_iξ_a + r²∂_a(ξ_i/r²),   (ℒ_ξg)_ij = D̂_iξ_j + D̂_jξ_i + 2rD^arξ_a γ_ij.

(a) With ξ_i = −(1/2)D̂_iτ and ξ_a = −β_a + (r²/2)∂_a(τ/r²): (ℒ_ξg)_ai = ∂_i(ξ_a − (r²/2)∂_a(τ/r²)) = −∂_iβ_a, and
(ℒ_ξg)_ij = −D̂_iD̂_jτ + (a multiple of γ_ij), whose trace-free part is −(D̂D̂ − (1/3)γΔ̂)τ. As h_(a·) = dβ_a
([[lem:gd-1-2]] (c)), h + ℒ_ξg has vanishing mixed components, so β = 0; its h^TF is h^TT, so τ = 0 and the tensor part
is unchanged. The components of ξ have mean zero on each sphere, so the SO(4)-average of ξ vanishes; rotations are
isometries, so the average of ℒ_ξg is ℒ of the average of ξ, which is 0.

(b) h_ai = rf_a(−D̂_iS/k) = ∂_i(−(r/k)f_aS), so β_a = −(r/k)f_aS. As Δ̂S = −k²S,
h^TF = 2r²H_T(D̂D̂S − (1/3)γΔ̂S)/k², so h^TT = 0 and τ = 2r²H_TS/k². Then
ξ_a = (r/k)f_aS + (r²/2)∂_a(2H_TS/k²) = (r/k)(f_a + (r/k)D_aH_T)S = X_aS. The orbit block of h + ℒ_ξg is
(f_ab + D_aX_b + D_bX_a)S = F_abS. Its angular block is

    2r²(H_LγS + H_T(D̂D̂S/k² + γS/3)) − (2r²H_T/k²)D̂D̂S + 2rD^arX_aSγ = 2r²(H_L + H_T/3 + r⁻¹D^arX_a)Sγ = 2r²FSγ.

(c) Write Z = Z_a dy^a + Z_ϑ dϑ; by [[lem:gd-1-2]] (c), Z_ϑ dϑ = dη on each sphere with ⟨η⟩ = 0, and ⟨Z_a⟩ = 0. By the
formulas above, (ℒ_Zg)_ai dz^i = d(Z_a + r²∂_a(η/r²)), so β_a[ℒ_Zg] = Z_a + r²∂_a(η/r²); and the trace-free angular
part of ℒ_Zg is 2(D̂D̂ − (1/3)γΔ̂)η, so τ[ℒ_Zg] = 2η by (b) of [[lem:gd-1-2]]. Inserting in [[eq:gd-1-1]]:
ξ[ℒ_Zg] = (−Z_a − r²∂_a(η/r²) + r²∂_a(η/r²))dy^a − dη = −Z. ∎

### The spherically symmetric part {#sec:rw-l0}

**Lemma {#lem:rw-warped}** (Warped products over S³.) Let g′ = g′_ab dy^a dy^b + R²γ, with g′_ab a Lorentzian metric
and R > 0 a function on a two-dimensional manifold, D, □ and 𝓇 the covariant derivative, wave operator and scalar
curvature of g′_ab. Then Ric[g′]_ab = (𝓇/2)g′_ab − (3/R)D_aD_bR, Ric[g′]_ai = 0 and
Ric[g′]_ij = ρ γ_ij with ρ := 2(1 − |dR|²) − R□R. The Misner–Sharp mass m(g′) := R²(1 − |dR|²) satisfies

    ∂_a m(g′) = (2R³/3)(Ric_ab − (1/2)g′_ab g′^(cd)Ric_cd) D^bR + Rρ ∂_aR,                                 {#eq:rw-ms}

with Ric := Ric[g′] and indices raised by g′_ab.

*Proof.* The Christoffel symbols mixing the factors are Γ^a_ij = −RD^aR γ_ij and Γ^i_aj = (∂_aR/R)δ^i_j; the others are
those of g′_ab and of γ. Inserting them in R_bd = ∂_μΓ^μ_bd − ∂_dΓ^μ_bμ + Γ^μ_μνΓ^ν_bd − Γ^μ_dνΓ^ν_bμ, as in the proof
of [[lem:warped-ricci]]: for b, d on the base, the fibre indices add −3∂_b∂_dR/R + 3Γ^c_bd∂_cR/R = −3D_bD_dR/R, and the
Ricci tensor of a two-dimensional metric is (𝓇/2)g′_ab. For i, j on the fibre, the base derivatives of Γ^a_ij give
−D_a(RD^aR)γ_ij = −(R□R + |dR|²)γ_ij, the products containing mixed symbols give −3|dR|²γ_ij + 2|dR|²γ_ij, and
the fibre gives Ric[γ] = 2γ. The mixed
components vanish since every term carries an odd number of fibre indices of a tensor built from γ and its connection
alone. For [[eq:rw-ms]]: ∂_am = 2R∂_aR(1 − |dR|²) − 2R²D^bR D_aD_bR. By the formulas just proved,
D_aD_bR = (R/3)((𝓇/2)g′_ab − Ric_ab), 2(1 − |dR|²) = ρ + R□R and □R = (R/3)(𝓇 − g′^(cd)Ric_cd). Inserting these, the
terms in 𝓇 cancel and [[eq:rw-ms]] remains. ∎

**Lemma {#lem:gd-1-4}** (The spherically symmetric part: the linearised mass and Birkhoff's theorem.) Let
h_0 = A dv² + 2B dv dr + C dr² + 2r²H_L γ, with A, B, C, H_L functions of (v, r) on a simply connected open subset U of
the orbit space of {r > r_♭}, and write Ṙ := DRic(h_0).

(a) The linearisation of the Misner–Sharp mass at g (where it equals m₀) is

    δm[h_0] = 2m₀H_L + r²(A + 2fB + f²C) − 2r²(∂_v + f∂_r)(rH_L).

It vanishes on ℒ_Y g for every spherically symmetric vector field Y; δm[K] = δm[K_V] = 1; and

    ∂_v δm = (2/3)r³(Ṙ_vv + fṘ_vr),        ∂_r δm = (1/3)r³fṘ_rr + rṘ_ϑϑ.

(b) If DRic(h_0) = 0 on U, then δm[h_0] =: c is constant; with Y_1 := −rH_L∂_r and h′ := h_0 − cK + ℒ_(Y_1)g =
A′dv² + 2B′dvdr + C′dr², the 1-form ω := (B′ + (f/2)C′)dv + (1/2)C′dr is closed, and for dζ = ω, ℒ_(ζ∂_v)g = h′. So

    h_0 = cK + ℒ_(Y[h_0]) g,        Y[h_0] := ζ∂_v + rH_L∂_r.                                               {#eq:gd-1-2}

(c) The spherically symmetric Killing fields of g are the multiples c′∂_v of ∂_v = ∂_t. So Y[h_0] is unique up to
c′∂_v, the choice of the constant in ζ.

*Proof.* (a) For ε small, g + εh_0 has the orbit metric g_ab + εh_ab, h_ab dy^ady^b := A dv² + 2B dvdr + C dr², and the
area radius R_ε with R_ε² = r²(1 + 2εH_L), so R_ε = r + εrH_L + O(ε²). The inverse orbit metric of g is
g^(vv) = 0, g^(vr) = 1, g^(rr) = f, and its variation is −h^(ab) = −g^(ac)g^(bd)h_cd, with h^(rr) = A + 2fB + f²C. So
δ|dR|² = −(A + 2fB + f²C) + 2g^(rb)∂_b(rH_L) = −(A + 2fB + f²C) + 2(∂_v + f∂_r)(rH_L), and
δm = 2r·rH_L(1 − f) − r²δ|dR|², which is the formula, as r²(1 − f) = m₀. A spherically symmetric Y is a field
Y^a(y)∂_a (S³ carries no SO(4)-invariant vector field), so its flow φ_s maps spherically symmetric metrics to
spherically symmetric metrics, with R(φ_s*g) = R(g) ∘ φ_s, and m(φ_s*g) = m(g) ∘ φ_s = m₀; differentiating at s = 0,
δm[ℒ_Yg] = 0. For K, A = r⁻² and the rest vanish, so δm[K] = 1; δm[K_V] = 1 by [[eq:gd-0-1]], V being spherically
symmetric. Finally, linearise [[eq:rw-ms]] at g, where Ric = 0, R = r and D^br = g^(br): only the variation of the
Ricci tensor survives, ρ̇ = Ṙ_ϑϑ, and ∂_aδm = (2r³/3)(Ṙ_ab − (1/2)g_ab g^(cd)Ṙ_cd)g^(br) + rṘ_ϑϑ∂_ar. For a = v,
g^(br)(Ṙ_vb − (1/2)g_vb tr) = Ṙ_vv + fṘ_vr − (1/2)(g_vv + fg_vr)tr = Ṙ_vv + fṘ_vr, as g_vv + fg_vr = 0, and ∂_vr = 0.
For a = r, Ṙ_rv + fṘ_rr − (1/2)(g_rv + fg_rr)(2Ṙ_vr + fṘ_rr) = (1/2)fṘ_rr.

(b) U is connected, so δm[h_0] is constant by (a). For a field Y = Y^r∂_r, (ℒ_Yg)_ij = Y(r²)γ_ij = 2rY^rγ_ij, so
ℒ_(Y_1)g removes the angular block, and h′ has the stated form. DRic(K) = 0, DRic(ℒ_(Y_1)g) = 0 ([[lem:ix-2-1]] (b)),
so DRic(h′) = 0, and δm[h′] = c − c + 0 = 0 by (a), that is A′ = −2fB′ − f²C′. The metrics g + εh′ keep R = r, so by
[[lem:rw-warped]] their rr Ricci component is (𝓇_ε/2)(g + εh′)_rr − (3/r)D^ε_rD^ε_r r. At ε = 0, g_rr = 0 and
𝓇 = −f″ (the scalar curvature of −f dv² + 2 dv dr), and D_rD_rr = −Γ^r_rr; the first-order variation of Γ^r_rr is
(1/2)g^(rd)(2∂_rh′_dr − ∂_dh′_rr) = (1/2)(2∂_rB′ − ∂_vC′ + f∂_rC′), the term with the variation of g^(rd) vanishing
as the lowered symbols Γ_(d,rr) of g vanish. So

    0 = Ṙ_rr[h′] = −(f″/2)C′ + (3/(2r))(2∂_rB′ − ∂_vC′ + f∂_rC′) = (3/r)(∂_r(B′ + (f/2)C′) − ∂_v(C′/2)),

using −rf″/6 = m₀/r³ = f′/2. So dω = 0, and ω = dζ on the simply connected U. For Y = ζ∂_v, ∂_v being Killing,
ℒ_Yg = dζ ⊗ (∂_v)^♭ + (∂_v)^♭ ⊗ dζ with (∂_v)^♭ = −f dv + dr, that is

    ℒ_(ζ∂_v)g = −2f∂_vζ dv² + 2(∂_vζ − f∂_rζ) dv dr + 2∂_rζ dr².

With ∂_rζ = C′/2 and ∂_vζ = B′ + fC′/2 this is A′dv² + 2B′dvdr + C′dr², by A′ = −2fB′ − f²C′. Hence
h_0 = h′ + cK − ℒ_(Y_1)g = cK + ℒ_(ζ∂_v − Y_1)g, which is [[eq:gd-1-2]].

(c) For Y = a∂_v + b∂_r with ℒ_Yg = 0, the angular block 2rbγ forces b = 0, and the formula for ℒ_(a∂_v)g forces
∂_ra = 0 and ∂_va = 0. ∎

### The theorem {#sec:rw-theorem}

The following theorem passes the decay of [[thm:viii-2-2]] to the Regge–Wheeler-type gauge directly, sphere by sphere;
it uses neither the reconstruction of the metric from the master fields nor the estimates of [HKW18].

**Theorem {#thm:rw-settling}** (Part VIII's solution in the Regge–Wheeler-type gauge.) Let ġ, ṁ and h = ġ − ṁK_V be
as in [[sec:rw-setting]], h_0 the l = 0 part of h, and N⁺ = M°_♭ ∩ {t_IVP ≥ 0}.

(a) δm[h_0] = 0, and with Y[h_0] of [[eq:gd-1-2]], ζ normalised by ζ(v, r) → 0 as v → ∞,

    X_RW := ξ[h] − Y[h_0]^♭,        ġ_RW := ġ + ℒ_(X_RW) g = ṁK_V + (h − h_0) + ℒ_(ξ[h]) g

is a smooth G-invariant linearised vacuum solution on N⁺, smooth up to Σ°, in the Regge–Wheeler-type gauge with l = 0
part exactly ṁK_V, inducing (γ̇, k̇) plus the data of the linearised diffeomorphism ℒ_(X_RW)g. Except for the data,
the same holds on the open set int N ∩ M°_♭.

(b) (Decay.) For every k, R′ and ε′ > 0 there are C and T′ with

    |ġ_RW − ṁK_V|_k ≤ C ‖(γ̇, k̇)‖_(H^(k₁(k+2))) t_*^(−w+ε′)     on {r_♭ < r ≤ R′, t_* ≥ T′}:

the rate of [[thm:viii-2-2]], with a loss of two derivatives, the horizon included (r_♭ < r_h), uniformly in l (no
sum over harmonics is formed). The constant depends on R′; nothing is claimed uniformly in r.

(c) (The gauge vector.) On the same set, |ξ[h]|_k ≤ C‖(γ̇, k̇)‖_(H^(k₁(k+1))) t_*^(−w+ε′); the radial component rH_L
of Y[h_0] = ζ∂_v + rH_L∂_r, and every derivative of ξ[h] and of the components ζ and rH_L, are O(t_*^(−w+ε′)); and
|ζ| ≤ Ct_*^(−w+1+ε′). As a 1-form, X_(RW,0) := −Y[h_0]^♭ = (fζ − rH_L) dv − ζ dr; its dr component, and the term f′ζ
in the r-derivative of its dv component, are only O(t_*^(−(w−1)+ε′)). So X_RW = O(t_*^(−(w−1)+ε′)). X_RW is unique up
to c′(∂_t)^♭, and these are the only G-invariant Killing fields.

(d) (Uniqueness of the representative.) Let U ⊂ U^♯ be open and SO(4)-invariant, Ω′_+ := D_U(Σ_U) ∩ {t_IVP ≥ 0}, and
let ġ′ be a G-invariant linearised vacuum solution on Ω′_+, smooth up to Σ_U, in the Regge–Wheeler-type gauge,
inducing (γ̇, k̇) plus the data of ℒ_Z g for a vector field Z near Σ_U, smooth up to Σ_U. Then ġ′ = ġ_RW on Ω′_+.

*Proof.* (a) β and τ depend smoothly on (v, r, ϑ) (elliptic inverses on S³ with smooth parameters, commuting with
ℒ_(∂_v), ℒ_(∂_r)), so ξ[h] is smooth up to Σ°, and its β and τ are those of ġ, K_V being spherically symmetric. DRic
commutes with the SO(4)-average, so DRic(h_0) = (DRic ġ)_0 − ṁ DRic(K_V) = 0. The orbit space of the interior of N⁺,
{t > ψ_IVP(r), r > r_♭}, lies above a graph, so it is simply connected, and the upward rays {(v′, r) : v′ ≥ v} stay in
it, t_IVP increasing with v at fixed r. [[lem:gd-1-4]] (b) applies there: δm[h_0] is a constant, and being an
expression in h_0 and its first derivatives it tends to 0 along {r = r_1}, for any r_1 ∈ (r_♭, R′], by [[eq:gd-0-2]];
so it vanishes, and h_0 = ℒ_(Y[h_0])g. The 1-form ω of [[lem:gd-1-4]] (b) is algebraic in h_0 and the first
derivatives of H_L, so |ω|_k ≤ C|h|_(k+1), integrable in v by [[eq:gd-0-2]] as w − ε′ > 1. Put
ζ(v, r) := −∫_v^∞ ω_v(v′, r) dv′. Then ∂_vζ = ω_v, and as dω = 0, ∂_rζ = −∫_v^∞ ∂_(v′)ω_r dv′ = ω_r; so dζ = ω, ζ → 0
as v → ∞, and ζ is smooth up to Σ°, its derivatives being those of ω. Hence ġ_0 − ℒ_(Y[h_0])g = ṁK_V, and with
[[lem:gd-1-3]] (a), ġ_RW is in the Regge–Wheeler-type gauge with l = 0 part ṁK_V. DRic(ℒ_Xg) = 0
([[lem:ix-2-1]] (b)), and ℒ_Xg changes the induced data by those of a linearised diffeomorphism, read from one side
up to Σ° ([[lem:viii-1-1]]). Every step is O(4)-equivariant and ġ is G-invariant, so ġ_RW is G-invariant.

(b) ġ_RW − ṁK_V = (h − h_0) + ℒ_(ξ[h])g. Averaging does not increase |·|_k. ℒ_ξg is first order in ξ, and by
[[lem:gd-1-2]] (d) and [[eq:gd-1-1]] each component of ξ costs one derivative of h (β_a one angular derivative, ∂_aτ one
orbit derivative, D̂τ one angular derivative), so |ℒ_(ξ[h])g|_k ≤ C|ξ[h]|_(k+1) ≤ C|h|_(k+2). Apply [[eq:gd-0-2]].

(c) The bounds on ξ[h] and rH_L are [[lem:gd-1-2]] (d) and [[eq:gd-0-2]]; those on the derivatives of ζ are those on ω,
and |ζ| ≤ C∫_v^∞ v′^(−w+ε′)dv′ ≤ C′v^(−w+1+ε′), with |t_* − v| ≤ C_(R′). The form of X_(RW,0) follows from
(∂_v)^♭ = −f dv + dr and (∂_r)^♭ = dv. A G-invariant Killing field Z has ξ[ℒ_Zg] = −Z_(≥2) = 0 by [[lem:gd-1-3]] (c),
where Z_(≥2) := Z − Z_0 has only harmonics of degree l ≥ 2 ([[lem:gd-1-2]]), and Z_0 = c′∂_v by [[lem:gd-1-4]] (c).
For two gauge vectors X_RW and X′ as in (a), Z := X′ − X_RW has ℒ_Zg in the Regge–Wheeler-type gauge with l = 0
part 0, so ℒ_Zg = 0 by the argument of (d), and Z = c′(∂_v)^♭.

(d) By [[cor:ix-2-3]] and [[rem:ix-2-4]] (c), ġ′ = ġ + ℒ_(X′)g on Ω′_+ with X′ G-invariant: an SO(4)-invariant U is a
union of sets {(t, x) : (t, |x|) ∈ A}, hence O(4)- and G-invariant. So ġ′ − ġ_RW = ℒ_Zg, Z := X′ − X_RW, is in the
Regge–Wheeler-type gauge, with l = 0 part c″K_V for a constant c″. By [[lem:gd-1-3]] (c), Z_(≥2) = 0, as the β and
τ of ℒ_Zg are those of ℒ_(Z_(≥2))g. Its l = 0 part ℒ_(Z_0)g is c″K_V, and c″ = δm[ℒ_(Z_0)g] = 0 by
[[lem:gd-1-4]] (a). So ℒ_Zg = 0. ∎

**Remark {#rem:rw-zeta}** (The loss of one power in ζ.) It comes from the time integral and is attained by the
implication "ℒ_Yg decays ⇒ Y decays": by the formula for ℒ_(ζ∂_v)g, Y = (1 + v)^(−q)∂_v has
ℒ_Yg = 2q(1 + v)^(−q−1)(f dv² − dv dr) = O(v^(−q−1)), with every derivative, while Y is only O(v^(−q)). Whether
Part VIII's own h_0 makes ζ decay faster is not determined here.

### The master fields {#sec:rw-master}

The scalar and tensor modes of the class are carried by Kodama and Ishibashi's master fields. We use the following
results of [KI03], stated at n = 3, K = 1, Λ = 0 and 2M = m₀, so that their f is ours and their x is ς; page numbers
are those of the arXiv version. Their frequency-domain form is [[thm:s15-ki]]; here the time-domain form is needed.

**Theorem {#thm:rw-ki}** ([KI03, (2.4)–(2.8), pp. 4–5; (2.13), p. 5; (3.11)–(3.14), pp. 9–10; (5.1)–(5.6), p. 13].)
Let k² = l(l + 2), 𝔪 := k² − 3 (the m of [KI03, (3.3)]), H := 𝔪 + 6ς, Q the polynomial [[eq:s15-ki-q]] with 𝔪 in
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

*Proof.* Substitute 𝔪 = H − 6ς in [[eq:s15-ki-q]]: 16𝔪³ = 16H³ − 288ςH² + 1728ς²H − 3456ς³,
60𝔪² = 60H² − 720ςH + 2160ς², 36𝔪(𝔪 − 12)ς = 36ςH² − 432ς²H − 432ςH + 1296ς³ + 2592ς², and
(624𝔪 − 144)ς² = 624ς²H − 3744ς³ − 144ς². Adding these and 1296ς³,

    Q = 16H³ + (60 − 252ς)H² − (1152ς − 1920ς²)H + 4608ς²(1 − ς).

Divide by 16H² and use H = k² − 3 + 6ς: H + 15/4 − (63/4)ς = k² + 3/4 − (39/4)ς, which is the first formula, as
1 − ς = f. The second is k_T² + 2 = k². Each term of r²W − k² − 3/4 is a product of powers of ς, f and 1/H with
coefficients independent of l; on {r ≥ r_h}, 0 < ς ≤ 1, 0 ≤ f < 1 and 0 < 1/H ≤ 1/5 (H ≥ 𝔪 ≥ 5), and
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
[[eq:gd-1-1]], with orbit part X_aS, X_a = (r/k)(f_a + (r/k)D_aH_T), and angular part −(1/2)D̂τ, τ = 2r²H_TS/k²; it
is smooth wherever h is. In it the mode is h_S = F_abS dy^ady^b + 2r²FS γ, with F, F_ab its gauge invariants. The
tensor part needs no gauge: h_T = 2r²H_T T, H_T being gauge invariant.

(iii) (Reconstruction.) With Φ the master field of the mode, F and F_ab are given by [[eq:np-10-1]], and H_T = r^(−3/2)Φ
for the tensor type. With ψ := r^(3/2)Φ, so that Φ̃ = Hψ, every component of h_S and h_T in a chart regular at the
horizon (the ingoing chart (v, r)) and the orthonormal frame of the spheres is a combination of ∂_v²ψ, ∂_v∂_rψ,
∂_r²ψ, ∂_vψ, ∂_rψ, ψ and 𝔪ψ, with coefficients bounded on {r ≥ r_h} uniformly in l ([[lem:rw-coefficients]]): two
orbit-space derivatives, and the factor 𝔪 (two angular derivatives) through F and the trace of F_ab. In Φ itself
the coefficients of F̃ and F̃_ab are O(r^(3/2)), and in r^(−3/2)Φ they are O(r³), uniformly in l, those powers being
attained.

(iv) (Decay.) In the gauge of (ii) for every l ≥ 2, fix the l = 0 part to h_0 = cK, K = r⁻²dv² the change of mass
regular at the horizon (the static
chart's ∂_m g = r⁻²dt² + r²(r² − m₀)⁻²dr² equals K + ℒ_(ζ∂_v)g with ζ′ = (r²f²)⁻¹, singular at r_h; the gauge
h_0 = cK is reached by the gauge vector Y[h_0] of [[eq:gd-1-2]], smooth wherever h_0 is). Then h settles to cK on each
region {r ≤ R}, the horizon included, uniformly in l, in two data classes:

(iv-a) (Part VIII's data class.) Let h be a solution on N⁺, which reaches inside the horizon (r_♭ < r_h). If the data
h induces on Σ^IVP are, up to those of a linearised diffeomorphism, G-invariant data (γ̇, k̇) of [[thm:viii-2-2]]
(γ̇ ∈ H^(∞,(ℰ_0,ℓ_0))_b, k̇ ∈ H^(∞,(ℰ_0+1,ℓ_0+1))_b, solving the linearised constraints), then h + cℒ_Vg, which is in
the Regge–Wheeler-type gauge with l = 0 part cK_V, is the ġ_RW of [[thm:rw-settling]]; so c = ṁ, h = ġ_RW on
{r ≤ 2R₁}, and h − cK = ġ_RW − ṁK_V everywhere. For every k, R′ and ε′ > 0,

    |h − cK|_k ≤ C ‖(γ̇, k̇)‖_(H^(k₁(k+2))) t_*^(−w+ε′)     on {r_♭ < r ≤ R′, t_* ≥ T′}:

every component, with k derivatives along ∂_v, ∂_r and the rotations, pointwise, the horizon included, uniformly in l
(no sum over modes is formed), with a loss of two derivatives and a constant depending on R′ (not shown to grow as a
power of R′).

(iv-b) ([HKW18]'s data class, with the red-shift datum.) Let h be smooth up to and including the future horizon, with
h_0 = cK. Put

    D := Σ_X I_(XΨ)(Σ_0),     X ∈ {1, T, T², Ω, Ω²},
    Q_0 := Σ_l ‖Y_l‖² ∫_(Σ_0 ∩ {r ≤ R_1}) |∂_r²Φ_l|² dr,

D summed over the scalar and tensor master quantities Ψ of h ([[lem:rw-hkw-field]]), Ω standing for the six rotations
summed, Φ_l the master field of the mode l, ∂_r at fixed v (transversal to the horizon), Y_l the harmonic that carries
the mode in h's components (S for the scalar type and T for the tensor type, as in (ii)), and R_1 the radius of
[HKW18] below which Σ_0 is spacelike. Then for τ ≥ 0 and R ≥ R_1,

    ∫_(Σ_τ ∩ {r ≤ R}) Σ_c |(h − cK)_c|² dr dω ≤ C R⁵ (D + Q_0)(1 + τ)⁻²,                               {#eq:np-10-1-iv-b}

dω the measure of the unit sphere, the components c taken in the chart (v, r) and the orthonormal frame of the spheres,
C depending on m₀ and Σ_0 only, uniformly in l: the squared L² norm of the components, which are second derivatives of
the master fields, decays at [HKW18]'s energy rate for data with two more commutations. The scalar-type part of Q_0
cannot be dropped: with D it is bounded by the left side at any one time, and it is not bounded by any sum of
I_(XΨ)(Σ_0) over products X of the Killing fields, for smooth h either ([[lem:np-10-1b]]). The tensor-type part can,
the tensor type's components 2r^(−3/2)Φ carrying no derivative of Φ.

So in the Regge–Wheeler-type gauge for l ≥ 2, with h_0 = cK, every metric component of h settles to the change of mass
cK on each region {r ≤ R}, the horizon included: pointwise with all derivatives at the rate of [[thm:viii-2-2]] for
its data (iv-a), and at [HKW18]'s rate τ⁻² in energy against dr dω, uniformly in l with a constant growing as R⁵ and
the loss of two derivatives counted as in (iii), for [HKW18]'s data with the red-shift datum (iv-b). Uniformly in r
the energy statement fails, and on the outgoing part of the leaves the components settle with the weights r^(−1/2) on
the orbit block and r^(1/2) on the angular block, weights that are attained ([[thm:rwg-1]], [[thm:rwg-2]]).

**Lemma {#lem:rw-coefficients}** (The coefficients of the reconstruction.) In the ingoing chart (v, r), with
ψ = r^(3/2)Φ,

    rF = (𝔪/(6r²))ψ + ((ς − 12fς/H)/(2r²))ψ + (1/(2r))∂_vψ + (f/(2r))∂_rψ,

    rF_ab + rF g_ab = D_aD_bψ − (12ς/(rH))(δ^r_a∂_bψ + δ^r_b∂_aψ) + (ψ/H)D_aD_bH
                      − (1/2)g_ab(□ψ − (24ς/(rH))(∂_vψ + f∂_rψ) + (ψ/H)□H),

with D_vD_vu = ∂_v²u − (f′/2)∂_vu − (ff′/2)∂_ru, D_vD_ru = ∂_v∂_ru + (f′/2)∂_ru, D_rD_ru = ∂_r²u,
□u = 2∂_v∂_ru + f′∂_ru + f∂_r²u, and H′ = −12ς/r, H″ = 36ς/r². Every coefficient, but the 𝔪/(6r²) of rF, is a sum of
terms m₀^c H^a r^b with a ≤ 0 and b ≤ 0, so bounded on {r ≥ r_h} uniformly in l; the 𝔪/(6r²) enters rF_ab only
through the trace, rFg_ab, and not rF_rr (g_rr = 0). In rF_rr the coefficient of ∂_r²ψ is 1. In terms of Φ, every
coefficient is O(r^(3/2)) uniformly in l, attained by ∂_r²Φ in rF_rr; in terms of r^(−3/2)Φ, O(r³), attained likewise.

*Proof.* In the chart (v, r), g_vv = −f, g_vr = 1, g_rr = 0 and g^(vv) = 0, g^(vr) = 1, g^(rr) = f; the only lowered
Christoffel symbols that do not vanish are Γ_(r,vv) = f′/2 and Γ_(v,vr) = −f′/2, which give the Hessian above. By
[[eq:np-10-1]], with Φ̃ = Hψ, Dr · DΦ̃ = ∂_vΦ̃ + f∂_rΦ̃ = H(∂_vψ + f∂_rψ) + fH′ψ, and 2H − 3rf′ = 2𝔪 + 6ς; this gives
rF, as 6rfH′/H = −72fς/H. For the second, D_aD_b(Hψ) = HD_aD_bψ + H′(δ^r_a∂_bψ + δ^r_b∂_aψ) + ψD_aD_bH and
□(Hψ) = H□ψ + 2H′(∂_vψ + f∂_rψ) + ψ□H; divide by H. The monomial structure is read off: f = 1 − m₀r⁻²,
f′ = 2m₀r⁻³, ς = m₀r⁻², H′/H, H″/H and D_aD_bH/H carry r⁻¹ or r⁻² and 1/H, and H ≥ 5. In ψ = r^(3/2)Φ, a derivative of
order j ≤ 2 of ψ is r^(3/2) times one of Φ plus lower-order terms with smaller powers of r; so the coefficients in Φ
are O(r^(3/2)), and the coefficient r^(3/2) of ∂_r²Φ in rF_rr = ∂_r²ψ + 2(H′/H)∂_rψ + (H″/H)ψ is attained; with
ψ = r³(r^(−3/2)Φ) the same argument gives r³. Finally h_ab = F_abS = ((rF_ab + rFg_ab) − rFg_ab)S/r, and the angular
block of h_S in the orthonormal frame of the spheres is 2FSδ_ij = (2/r)(rF)Sδ_ij: each component is r⁻¹ times a
combination with the stated coefficients. For the tensor type the frame components of 2r²H_TT are 2H_T|T| with
H_T = r^(−3)ψ. ∎

*Proof of [[prop:np-10-1]] (i)–(iii) and (iv-a).* (i) Every class tensor is h_0 plus the part with l ≥ 2, which by
[[lem:gd-1-2]] (c) consists of the orbit block h_ab − ⟨h_ab⟩, the mixed components h_(a·) = dβ_a and the angular block
2r²(H_L − ⟨H_L⟩)γ + (D̂D̂ − (1/3)γΔ̂)τ + h^TT: scalar type, built from harmonics of [[lem:gd-1-2]] (a), which have even
degree, and the tensor type h^TT. The class carries no co-closed 1-form on S³ ([[lem:gd-1-2]] (c)), so there is no
vector-type part, and no harmonic of degree 1. The tensor type is supported in l ≥ 2 ([HKW18, Proposition 6, p. 14]:
"the components H_2, ĥ_α, and ĥ_αβ are necessarily supported in ℓ ≥ 2"). The domain of outer communication to the
future of Σ_0 has a simply connected orbit space, the region above a graph, so by [[lem:gd-1-4]] (b), h_0 = cK + ℒ_Yg
with c the linearised mass: a change of mass plus a pure gauge solution. This is [HKW18, Theorem 1, p. 3] in the
class, where its linearised rotations, of vector type l = 1, are absent.

(ii) is [[lem:gd-1-3]] (b) with (a); the gauge vector is smooth wherever h is, since β and τ are. For the tensor type,
[[thm:rw-ki]] (T). By [KI03, p. 5] the gauge invariants exist for k²(k² − 3) ≠ 0, that is l ≥ 2; the modes with l = 1
carry no physical degree of freedom ("This implies that there exist no physical degrees of freedom for l = 1",
[KI03, p. 7]) and are absent in the class anyway.

(iii) is [[thm:rw-ki]] (S) and (T) with [[lem:rw-coefficients]].

(iv) The formula for ∂_m g in the static chart is the derivative of −(1 − m/r²)dt² + (1 − m/r²)⁻¹dr²; with
dv = dt + f⁻¹dr, K = r⁻²dt² + 2r⁻²f⁻¹dt dr + r⁻²f⁻²dr², and by the formula for ℒ_(ζ∂_v)g in the proof of
[[lem:gd-1-4]] (b), with ζ = ζ(r), ℒ_(ζ∂_v)g = −2fζ′dv dr + 2ζ′dr² = −2fζ′dt dr, which removes the dt dr term for
ζ′ = (r²f²)⁻¹.

(iv-a) h induces (γ̇, k̇) plus the data of some ℒ_Zg, and cℒ_Vg induces those of ℒ_(cV)g. h + cℒ_Vg is G-invariant,
smooth up to Σ°, a linearised vacuum solution in the Regge–Wheeler-type gauge, its l = 0 part being cK + cℒ_Vg = cK_V
([[eq:gd-0-1]]). By [[thm:rw-settling]] (d) with U = U^♯, for which Ω′_+ = N⁺ ([[lem:ix-1-2]]), h + cℒ_Vg = ġ_RW.
Comparing the l = 0 parts, c = ṁ. So h − cK = ġ_RW − cℒ_Vg − cK = ġ_RW − ṁK_V, and ℒ_Vg = 0 on {r ≤ 2R₁}. The
bound is [[thm:rw-settling]] (b). ∎

[[pending:issue-rw-continue]]
