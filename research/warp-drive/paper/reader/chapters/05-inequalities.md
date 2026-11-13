# Part. Uniform existence {#part:existence}

## Inequalities on the slices {#ch:inequalities}

This chapter collects the four estimates on the slices Σ_τ of Ω on which the uniform existence theorem
[[thm:uniform-existence]] rests: Sobolev and product inequalities in the scaled norms; a mollifier at scale λ that maps
functions on the annulus Σ_τ to functions on it, with the bounds of Bernstein and Friedrichs type; the energy inequality
for wave equations on Ω; and the estimate for transport along L0.

The domain Ω, its slices Σ_τ = A(τ) := {a ≤ |x| ≤ b(τ)} with outer radius b(τ), the numbers a, δ0, τ0 and τ_end, and
the properties of Ω under g0 and its small perturbations are those of [[pending:setting-domain]] and
[[pending:setting-domain-lemma]]; the scaled norms |f|_j = Σ_(i≤j) λ^i ‖∂^i f‖, with ‖·‖ the flat L²(Σ_τ) norm and ∂^i
all spacetime coordinate derivatives of order i, and the chain rule for profiles are those of
[[pending:setting-scaled-norms]]; and the numbers ε1 and s0 are those of [[pending:setting-eps1-s0]]. All constants below
depend on Ω, through a, b(τ0) and δ0, and not on λ, and throughout

    0 < λ ≤ λ1 := min(1, δ0)/10.                                                                        {#eq:lambda-one}

The outer radius is b(τ) = V + 1 − τ + (τ_end − τ), so b' = −2, and b(τ) − a ≥ 1 + δ0 and b(τ) ≤ b(τ0) on [τ0, τ_end]
[[pending:setting-domain-lemma]].

### Sobolev inequalities and products {#sec:sobolev}

**Lemma {#lem:sobolev}** (Sobolev inequality and products.) On A(τ),

    ‖f‖_(L^∞) ≤ C Σ_(i≤3) ‖∂_x^i f‖,     hence     ‖∂^i f‖_(L^∞) ≤ C λ^(−3−i) |f|_(i+3).                  {#eq:sobolev}

For k = 6, |f g|_k ≤ C λ⁻³ |f|_k |g|_k; and if a is a profile, |[a] f|_k ≤ C |f|_k.

*Proof.* The annuli A(τ) are images of the fixed annulus {a ≤ |x| ≤ a + 1 + δ0} under radial maps with derivatives of
all orders bounded uniformly in τ, since b(τ) − a ∈ [1 + δ0, b(τ0) − a]. So Sobolev's embedding of H³ into L^∞ in four
dimensions [[thm:std-bh-embedding]] holds on A(τ) with a constant independent of τ. Applied to ∂^i f, and with λ ≤ 1,
it gives ‖∂^i f‖_(L^∞) ≤ C Σ_(j≤3) λ^(−i−j) λ^(i+j) ‖∂^(i+j) f‖ ≤ C λ^(−3−i) |f|_(i+3).

For products, expand λ^j ∂^j (f g) for j ≤ 6 by Leibniz's rule into terms λ^i ∂^i f · λ^(j−i) ∂^(j−i) g and put the
factor with at most three derivatives in L^∞. If i ≤ 3, then ‖λ^i ∂^i f‖_(L^∞) ≤ C λ⁻³ |f|_(i+3) ≤ C λ⁻³ |f|_6 by
[[eq:sobolev]], and ‖λ^(j−i) ∂^(j−i) g‖ ≤ |g|_6; if i ≥ 4, then j − i ≤ 2 and the roles are exchanged. For the last
claim, the chain rule for profiles [[pending:setting-scaled-norms]] gives ‖λ^i ∂^i [a]‖_(L^∞) ≤ C_i for every i, so
each term λ^i ∂^i [a] · λ^(j−i) ∂^(j−i) f of λ^j ∂^j ([a] f) is bounded in L² by C |f|_k. ∎

### The mollifier {#sec:mollifier}

The decomposition of the remainder in the proof of [[thm:uniform-existence]] needs a smoothing operator at scale λ on
each slice. A Fourier multiplier supported in {|ξ| ≤ 1/λ}, as in [Tou23a, Section 3.2.3, p. 21], needs no boundary; on
the annulus A(τ) we use a compactly supported mollifier whose averaging ball is shifted 2λ inward near the outer sphere
and outward near the inner one, so that it maps functions on A(τ) to functions on A(τ).

**Lemma {#lem:ramp}** (The shift profile.) Let L be the function on ℝ equal to 1 on (−∞, 7/20], to −1 on [13/20, ∞), and
linear on [7/20, 13/20], and let σ0 be its mollification with a smooth even nonnegative kernel of integral one supported
in [−1/120, 1/120], restricted to [0, 1]. Then σ0 is smooth and non-increasing, |σ0| ≤ 1, |σ0'| ≤ 20/3 ≤ 7, σ0 = 1 on
[0, 1/3] and σ0 = −1 on [2/3, 1].

*Proof.* σ0 is smooth as a mollification. Its derivative is the mollification of L', which equals −20/3 on (7/20, 13/20)
and 0 elsewhere; as the kernel is nonnegative with integral one, σ0' takes values in [−20/3, 0]. Likewise |σ0| ≤ 1
because |L| ≤ 1. For t ≤ 1/3 = 40/120 the window [t − 1/120, t + 1/120] lies in (−∞, 41/120] ⊂ (−∞, 7/20], where L = 1,
so σ0(t) = 1; for t ≥ 2/3 = 80/120 it lies in [79/120, ∞) ⊂ [13/20, ∞), where L = −1. ∎

For f on A(τ) put

    σ(τ, x) := σ0((|x| − a)/(b(τ) − a)),     Φ(x) := x + 2 λ σ(τ, x) x̂,

and fix ρ ∈ C_c^∞(B_1) with ρ ≥ 0 and ∫ ρ = 1. The mollifier is

    𝒫 f (x) := ∫ ρ(z) f(Φ(x) − λ z) dz          (spatial, at fixed τ).                                 {#eq:mollifier}

**Lemma {#lem:shift-map}** (The shifted ball stays in the annulus.) For x ∈ A(τ), |z| ≤ 1 and t ∈ [0, 1], the point x +
t (Φ(x) − λ z − x) lies in A(τ), the segment from x to Φ(x) − λz has length at most 3λ, and Φ(x) − λz lies at distance
at least λ from the boundary of A(τ) near either sphere. The map Φ is a diffeomorphism of A(τ) onto its image, DΦ = I +
λ E with E bounded with all its derivatives, and the eigenvalues of DΦ lie in [3/10, 1] (radially) and in [2/5, 1 +
2λ1/a] (angularly). For t ∈ [0, 1] the map x ↦ x + t (Φ(x) − λz − x) has Jacobian eigenvalues at least 3/10 radially
and 2/5 angularly.

*Proof.* The length of the segment is |2λ σ x̂ − λ z| ≤ 2λ + λ = 3λ. Near the inner sphere, where |x| − a ≤ (b − a)/3,
σ = 1, and for t ∈ [0, 1]

    |x + t (2λ x̂ − λ z)| ≥ x̂·(x + t (2λ x̂ − λ z)) ≥ |x| + 2tλ − tλ = |x| + tλ,

so the segment stays outside the inner sphere and its end point Φ(x) − λz lies at least λ outside it; it stays inside
the outer sphere because |x| + 3λ ≤ a + (b − a)/3 + 3λ < b. Near the outer sphere, where |x| − a ≥ 2(b − a)/3, σ = −1,
and |x − t (2λ x̂ + λ z)| ≤ |x| − 2tλ + tλ = |x| − tλ, so the segment stays inside the outer sphere, its end point at
least λ inside it, and outside the inner sphere because |x| − 3λ ≥ a + 2(b − a)/3 − 3λ > a. In the middle third the
distance to the boundary is at least (b − a)/3 ≥ 1/3 > 3λ, which exceeds the length of the segment. So every point of
the segment lies in A(τ).

The map Φ is radial, r ↦ r + 2λ σ0((r − a)/(b − a)), so DΦ has the radial eigenvalue 1 + 2λ σ0'/(b − a) and three
angular eigenvalues 1 + 2λσ/r. Since λ/(b − a) ≤ λ1/(1 + δ0) ≤ 1/20 and σ0' ∈ [−7, 0] ([[lem:ramp]]), the radial one
lies in [1 − 14/20, 1] = [3/10, 1]. Since σ < 0 only where r − a > (b − a)/3 ≥ 1/3, so r > 1/3, and |σ| ≤ 1, the angular
ones are at least 1 − 2λ1/(1/3) ≥ 1 − 3/5 = 2/5, and at most 1 + 2λ1/a. A radial map whose radial and angular
eigenvalues are positive is a diffeomorphism onto its image, and DΦ − I = λ E with E built from σ0' , σ, r⁻¹ and their
derivatives, bounded with all derivatives. For the last claim, the Jacobian of x ↦ x + t (Φ(x) − λz − x) is (1 − t) I +
t DΦ, with the eigenvalues 1 + t (e − 1), e those of DΦ, which lie between 1 and e. ∎

**Lemma {#lem:mollifier}** (The mollifier.) For f on A(τ) and a smooth bounded function or profile a, with E1 and E2
bounded matrices of functions:

    (M1)   ‖𝒫 f‖ ≤ C ‖f‖;                                                                              {#eq:mollifier-m1}
    (M2)   ‖∂_x 𝒫 f‖ ≤ C λ⁻¹ ‖f‖;                                                                      {#eq:mollifier-m2}
    (M3)   ‖f − 𝒫 f‖ ≤ C λ ‖∂_x f‖;                                                                    {#eq:mollifier-m3}
    (M4)   ∂_x 𝒫 f = 𝒫(∂_x f) + λ E1 𝒫(∂_x f),   and   λ ‖𝒫 ∂_x f‖ ≤ C ‖f‖;                            {#eq:mollifier-m4}
    (M5)   ‖[a, 𝒫] ∂_x f‖ ≤ C ‖∂_x a‖_∞ ‖f‖   and   ‖[a, 𝒫] f‖ ≤ C λ ‖∂_x a‖_∞ ‖f‖;                    {#eq:mollifier-m5}
    (M6)   ∂_τ 𝒫 f = 𝒫(∂_τ f) + λ E2 𝒫(∂_x f).                                                         {#eq:mollifier-m6}

Iterating, λ^j ‖∂^j 𝒫 f‖ ≤ C Σ_(i≤j) λ^i ‖∂^i f‖, and the same holds with 1 − 𝒫 in place of 𝒫.

*Proof.* (M1): for fixed z, x ↦ Φ(x) − λz maps A(τ) into itself with Jacobian bounded above and below uniformly in λ
([[lem:shift-map]]); changing variables in ‖f(Φ(·) − λz)‖ and integrating against ρ(z) gives (M1).

(M2): with y = Φ(x) − λz, 𝒫 f(x) = λ⁻⁴ ∫ ρ((Φ(x) − y)/λ) f(y) dy, and ∂_x falls on ρ, producing λ⁻¹ DΦ^T (∇ρ)((Φ(x) −
y)/λ); the bound follows as in (M1).

(M3): f(x) − f(Φ(x) − λz) is the integral of ∂_x f along the segment from x to Φ(x) − λz, of length at most 3λ, which
stays in A(τ) ([[lem:shift-map]]). Writing the segment as x + t (Φ(x) − λz − x), t ∈ [0, 1], and changing variables x ↦
x + t (Φ(x) − λz − x), whose Jacobian has eigenvalues at least 3/10 radially and 2/5 angularly ([[lem:shift-map]]), gives
the bound.

(M4): by the chain rule ∂_x [f(Φ(x) − λz)] = DΦ^T (∂f)(Φ(x) − λz) = (I + λ E^T)(∂f)(Φ(x) − λz), which integrated against
ρ(z) is the identity with E1 := E^T. Further (∂_j f)(Φ(x) − λz) = −λ⁻¹ ∂_(z_j) [f(Φ(x) − λz)], and integrating by parts
onto ρ gives 𝒫(∂_j f) = λ⁻¹ ∫ (∂_j ρ)(z) f(Φ(x) − λz) dz, so λ ‖𝒫 ∂_x f‖ ≤ C ‖f‖ as in (M1).

(M5) is Friedrichs' lemma in this form:

    [a, 𝒫] ∂_j f (x) = ∫ ρ(z) (a(x) − a(Φ(x) − λz)) (∂_j f)(Φ(x) − λz) dz.

Integrating by parts in z as in (M4), the factor λ⁻¹ meets either ∂_z of a(Φ(x) − λz), which is −λ (∂a)(Φ(x) − λz), or
a(x) − a(Φ(x) − λz), whose size is at most 3λ ‖∂_x a‖_∞ by the length of the segment. Both are O(λ ‖∂_x a‖_∞), and the
change of variables of (M1) gives the first bound. The second is the same without the integration by parts.

(M6): σ depends on τ through b(τ), with ∂_τ σ = −σ0' (|x| − a) b'/(b − a)², bounded since b' = −2 and b − a ≥ 1. So
∂_τ [f(τ, Φ(τ, x) − λz)] = (∂_τ f)(Φ(x) − λz) + 2λ (∂_τ σ) x̂·(∂_x f)(Φ(x) − λz); integrating against ρ gives (M6) with
E2 := 2 (∂_τ σ) x̂.

Higher derivatives follow by induction, each derivative of 𝒫 f being moved onto f by (M4) and (M6) at the cost of
bounded factors. ∎

### The energy inequality {#sec:energy}

**Lemma {#lem:energy}** (Energy inequality.) Let g̃ be a Lorentzian metric on Ω with |g̃ − g0| ≤ ε1, ε1 the number of
[[pending:setting-eps1-s0]], so that the conclusions of [[pending:setting-domain-lemma]] (e) apply to g̃ and |g̃⁻¹| ≤ (s0
− ε1)⁻¹, and with ‖∂g̃‖_∞ ≤ M1. Let u, a function or a Cartesian array, satisfy −(1/2) g̃^(ab) ∂_a ∂_b u = f on Ω. Then
for τ ∈ [τ0, τ_end],

    ‖∂u(τ)‖ + ‖u(τ)‖ ≤ C(M1) (‖∂u(τ0)‖ + ‖u(τ0)‖ + ∫_(τ0)^τ ‖f(s)‖ ds).                                {#eq:energy}

*Proof.* Take the multiplier Y := −g̃⁻¹ dτ, future timelike by [[pending:setting-domain-lemma]] (e), the energy current
J^a = T^a_b Y^b with T_ab = ∂_a u ∂_b u − (1/2) g̃_ab g̃(du, du), and apply the divergence theorem on Ω ∩ {τ0 ≤ s ≤ τ}
in the coordinate density. The flux through Σ_τ equals the flux through Σ_τ0, minus the fluxes through the lateral
boundaries, plus the bulk integral. The lateral boundaries are spacelike with Ω to their past
([[pending:setting-domain-lemma]] (b), (c), (e)), so their fluxes are nonnegative and are dropped. The fluxes through
Σ_τ are comparable to ‖∂u‖², by the dominant energy condition, since Y and the normal are uniformly timelike by
[[pending:setting-domain-lemma]] (e) and |g̃⁻¹| ≤ (s0 − ε1)⁻¹. The bulk is bounded by C(M1)(‖∂u‖² + ‖f‖ ‖∂u‖), since ∂g̃,
g̃⁻¹ and ∂Y = g̃⁻¹ (∂g̃) g̃⁻¹ dτ are bounded, the constant depending also on Ω and s0 − ε1. The norm ‖u‖ is added through
∂_τ ‖u‖² = 2 ⟨u, ∂_τ u⟩ plus the boundary term b'(τ) ∫_(|x|=b) |u|² ≤ 0. Gronwall's inequality concludes. ∎

### The transport estimate {#sec:transport}

**Lemma {#lem:transport}** (Transport estimate.) Let L0 φ − c(X) φ = f on Ω, with φ a function or an array and c a
bounded function, or a bounded matrix acting on the components of φ. Then

    ‖φ(τ)‖ ≤ e^(C (τ − τ0)) (‖φ(τ0)‖ + ∫_(τ0)^τ ‖f(s)‖ ds),     C := max(0, sup_Ω (c − 3/(2r))),         {#eq:transport}

where for a matrix c is read as the largest eigenvalue of its symmetric part. For example, c = 2/r gives C = 1/(2a),
since 2/r − 3/(2r) = 1/(2r) ≤ 1/(2a).

*Proof.* Since L0 = ∂_τ − x̂·∂_x, ∂_τ φ = L0 φ + x̂·∂_x φ. In ℝ⁴, div x̂ = Σ_i ∂_i (x_i/r) = 4/r − |x|²/r³ = 3/r, so the
divergence theorem on A(τ), with outer normal x̂ on {|x| = b} and −x̂ on {|x| = a}, gives

    ∫_(A(τ)) 2 φ x̂·∂_x φ = ∫_(A(τ)) x̂·∂_x (φ²) = ∫_(|x|=b) φ² − ∫_(|x|=a) φ² − ∫_(A(τ)) (3/r) φ².

The outer sphere moves with speed b', so

    ∂_τ ‖φ‖² = 2 ⟨φ, f + c φ⟩ − ∫ (3/r) φ² + (1 + b') ∫_(|x|=b) φ² − ∫_(|x|=a) φ²,

and 1 + b' = −1 < 0. As ⟨φ, c φ⟩ − ∫ (3/(2r)) φ² ≤ sup_Ω (c − 3/(2r)) ‖φ‖², this gives ∂_τ ‖φ‖² ≤ 2 ‖φ‖ ‖f‖ + 2 C
‖φ‖², hence ∂_τ ‖φ‖ ≤ ‖f‖ + C ‖φ‖, and Gronwall's inequality concludes. ∎
