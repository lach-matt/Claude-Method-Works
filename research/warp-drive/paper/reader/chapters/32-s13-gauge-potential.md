## The gauge potential operator {#ch:s13}

This chapter studies the gauge potential wave operator □^Υ_b, a wave operator on 1-forms built from the Myers–Perry
metric g_b of [[ch:s11]] and a modification E^Υ of its divergence, for b near the Tangherlini parameter b_0. It proves,
in dimension 4 + 1, what [Hin26, Section 6] proves on Kerr (pp. 113–134): the structure of □^Υ_b as a stationary
wave-type operator ([[lem:iii-d-2-1]]), its Minkowski model ([[lem:iii-d-3-1]]), the indicial roots at zero energy
([[lem:iii-d-4-1]]), the threshold at the horizon and the bound at the trapped set ([[sec:iii-d-5]]), invertibility of
the spectral family at high energies and mode stability away from zero frequency ([[sec:iii-d-6]]), tf-admissibility
([[lem:iii-d-7-1]]), the kernel and cokernel at zero energy of the unmodified operator and mode stability of □^Υ_b on
the whole closed upper half plane ([[sec:iii-d1-2]]–[[sec:iii-d1-5]]), and the large zero energy states and the
generalised zero energy states of □^Υ_b ([[sec:iii-d2-1]]–[[sec:iii-d3-3]]). These are [Hin26, Lemmas 6.1, 6.3, 6.4,
6.6, 6.8, 6.10, 6.11, 6.13, 6.14, Propositions 6.5, 6.9, 6.12, 6.15, 6.18] in dimension 4 + 1.

The dimensional changes are these. The mass of g_b enters g_b − ḡ at |x|⁻² and its rotation at |x|⁻³, where those of
Kerr enter at |x|⁻¹ and |x|⁻²; so every comparison with Minkowski space gains a power of |x|⁻¹. The radial weight
ρ∂_ρ − 1 becomes ρ∂_ρ − 3/2, the trace weight of the modification is 2/3 = 2/(D − 2), and the harmonics are those of
𝕊³, which has six rotations and a tensor type. The indicial roots move: the gap of the unmodified operator at zero
energy is (0, 2), and that of □^Υ_b is (0, ι^Υ_(s1,2)) with ι^Υ_(s1,2) just above 2. Two inputs that [Hin26] takes
from [AHW24, Theorem 5.1] on Kerr, mode stability of the unmodified operator away from zero frequency and its kernel at
zero frequency, are proved here on five-dimensional Tangherlini, by ordinary differential equations whose potentials
are positive. The corrections to the boosts and to the time translation carry no logarithm.

Seven results of the main argument enter as inputs and are proved in this chapter, with every identity derived:
[[prop:np-10-15]] (the zero energy data of the unmodified operator), [[prop:np-10-16]] (the mode equations on
Tangherlini), [[prop:np-10-18]] (the structure at infinity and the horizon threshold), [[prop:np-10-20]] (the
transition face and the weights), [[prop:np-10-28]] (the symmetries and the linearised Myers–Perry metrics),
[[prop:np-10-29]] and [[prop:np-10-30]] (the model generalised states and their root facts). The trapping results
of [[prop:np-10-17-i]]–[[prop:np-10-17-v]] and [[prop:np-10-19-ii]]–[[prop:np-10-19-iii]] are proved in
[[ch:s12]].

*The dynamical hypotheses.* The theory of [[ch:s01]]–[[ch:s03]] applies to operators on a trivial bundle satisfying
hypotheses (H1)–(H8), (G), (Z) and (TF). Some of these concern the metric alone: the radial structure of the horizon in
(H3) and (H4), the time function and the Lorentzian metric in (H6), the normally hyperbolic trapping (Γ.1)–(Γ.3) in
(H7), and the global dynamics (H8). We write (Dyn) for them. For g_b, b near b_0, they hold by [[thm:vi-a-6-1]] (at
b_0) and [[thm:vi-b1-5-1]] (near b_0), for every operator with principal symbol G Id. This chapter proves the operator
hypotheses for □^Υ_b: (H1) and (H2) with the endomorphism S̄ ([[sec:iii-d-2]]), the horizon threshold
([[sec:iii-d-5-1]]), the bound (Γ.4) at the trapped set ([[sec:iii-d-5-2]]), the gap (G) ([[sec:iii-d-4]]) and (TF)
([[sec:iii-d-7]]).

*The inner radius.* The radii 0 < r_0 − 2δ_0 < r_0 < r_2 < r_h are those of [[sec:i-a-1-1]]. The only step below the
horizon, part (d) of the proof of [[prop:iii-d-6-2]] (repeated in [[lem:iii-d1-2-1]]), holds on (r_0, r_h) for every
r_0 ∈ (0, r_h); every other step reaches the inner boundary only through the theorems of [[ch:s01]]–[[ch:s03]], which
hold with r_0 as a parameter. So every result of this chapter holds with the inner radius r_0 as a parameter.

*Notation.* b = (m, A) are the parameters of [[sec:iii-b-3]], b_0 = (m_0, 0), and g_m := g_((m,0)) is the
five-dimensional Schwarzschild–Tangherlini metric of mass parameter m. On g_(b_0) we write f := 1 − m_0/r²,
r_h := m_0^(1/2), r := |x|, ρ := r⁻¹ near infinity, and x̂ := x/|x|. On 𝕊³, g_𝕊 is the round metric, and d_𝕊, δ_𝕊,
δ*_𝕊 and Δ_𝕊 := δ_𝕊 d_𝕊 ≥ 0 its differential, divergence, symmetric gradient and Laplacian, with the conventions of
[[sec:iii-a1-1]]; 𝒮_l and 𝒱_l are the scalar and vector harmonics of degree l ([[def:iii-a1-1-3]]), and κ := l(l + 2)
is the eigenvalue of Δ_𝕊 on 𝒮_l. The variable of indicial families is ι ∈ ℂ, and an indicial root is a value of ι.
When we use the static chart of g_(b_0) we write t for its static time, so that g_(b_0) = −f dt² + f⁻¹dr² + r²g_𝕊 on
{r > r_h}; this t differs from the time of [[eq:iii-b-3-6]] by a function of r. The ingoing time is v := t + r_*, with
the tortoise coordinate r_* of [[prop:np-10-16]] (v).

### The operator {#sec:iii-d-1}

Let ℬ be the parameter set of [[sec:iii-b-3]], g_b the Myers–Perry metric of [[prop:iii-b-3-6]], t_* the time function
of [[eq:iii-b-3-6]], and E_Υ = (c_Υ, e_Υ, γ_Υ; c_(Υ,H), γ_(Υ,H)) as in [[def:iii-b-6-1]], with the trace weight 2/3.
As [Hin26, (6.1)] requires, the supports of c_(Υ,H) and of c_Υ on {|x| < 5R_1} are disjoint from a fixed neighbourhood
U_Γ of the projection of the trapped sets of all g_b, b ∈ ℬ; by (Dyn) these lie over a fixed compact subset of
{r_h < |x| < 5R_1} near |x|² = 2m_0 ([[sec:iii-d-5-2]]). The *gauge potential wave operator* is

    □^Υ_b := □^Υ_(g_b,E_Υ) = 2δ_(g_b,E_Υ) G_(g_b) δ*_(g_b) = □_(g_b) + 2E^Υ_(g_b) G_(g_b) δ*_(g_b),       {#eq:iii-d-1-1}

acting on 1-forms, with □_g := 2δ_g G_g δ*_g. On a Ricci-flat metric, □_g = dδ_g + δ_g d = ∇*∇, the Hodge and the
Bochner d'Alembertian ([[prop:np-10-16]] (i)). Its spectral family is

    (□^Υ_b)^(σ) := e^(iσt_*) □^Υ_b e^(−iσt_*),

acting on stationary 1-forms on X, which we trivialise by dt_*, dx¹, …, dx⁴: the bundle E of [[sec:i-a-1]] with
N_E = 5. We also write P̂_b(σ) for it when E_Υ is fixed.

### Structure {#sec:iii-d-2}

The Minkowski model is ḡ := −(dt_* + d|x|)² + Σ_(i=1)^4 (dx^i)², Minkowski space in the time t̄ := t_* + |x|. Put
c̄ := |x|⁻¹ dt̄, Ē h := −γ_Υ(2ι_(ḡ⁻¹c̄) h − (2/3)(1 − e_Υ) c̄ tr_ḡ h) and □̄^Υ := 2(δ̄ + Ē)Ḡ δ̄*. In the coordinates
t_*, ρ, x̂ this is the Minkowski space of [[sec:iii-a1-2]], with t_* = t̄ − r there.

**Lemma {#lem:iii-d-2-1}** (Structure; [Hin26, Lemma 6.1] in dimension 4 + 1.) (1) □^Υ_b is stationary with principal
symbol g_b⁻¹(ζ, ζ) Id, and (□^Υ_b)^(σ) = P̂(0) + σT + σ²P_2 satisfies (H1) and the operator part of (H6) of
[[sec:i-a-1-3]] with g = g_b and t = t_*: P_2 = g_b^00 Id with g_b^00 := g_b⁻¹(dt_*, dt_*), σ_1(T) = −2g_b⁻¹(dt_*, ·) Id,
and P̂(0) − □_(g_b) Id is of first order with t_*-independent coefficients.

(2) On {|x| > 0}, exactly,

    □̄^Υ = −2∂_(t_*) ρ(ρ∂_ρ − 3/2 − S̄) + (□̄^Υ)^(0),                                                     {#eq:iii-d-2-1}

with S̄ and (□̄^Υ)^(0) ∈ ρ² Diff_b² given in [[lem:iii-d-3-1]], and no ∂_(t_*)² term.

(3) On {|x| > 3R_1},

    □^Υ_b = □̄^Υ − g_b^00 ∂_(t_*)² + Q_b ∂_(t_*) + R_b,     g_b^00 ∈ ρ²C^∞(X̄),  Q_b ∈ ρ³ Diff_b¹,  R_b ∈ ρ⁴ Diff_b²,
                                                                                                          {#eq:iii-d-2-2}

all stationary and smooth in b (and in e_Υ, γ_Υ). Hence (H2) holds with S := S̄ near infinity (in the Cartesian frame,
Θ⁻¹S̄Θ with Θ = Θ(x̂) the change from the null splitting [[eq:iii-a1-2-2]]; its spectrum is that of S̄), Q := Q_b,
P⁽⁰⁾ := ρ⁻²((□̄^Υ)^(0) + R_b), and P⁽⁰⁾ − ((ρD_ρ)² + Δ_𝕊) Id ∈ Diff_b¹ + ρ² Diff_b². The normal operator of P⁽⁰⁾ at
ρ = 0, its indicial roots, and S̄ do not depend on b.

*Proof.* (1) The terms 2E^Υ G δ* and the connection terms of □_(g_b) are of order at most 1, so the principal part is
−g_b^(μν) ∂_μ ∂_ν Id in the frame. Conjugating by e^(−iσt_*) replaces ∂_(t_*) by ∂_(t_*) − iσ; the σ² term is
−g_b^00 (−iσ)² = σ²g_b^00, and the principal symbol of the σ¹ coefficient is −2g_b⁻¹(dt_*, ζ), times the identity.
g_b^00 < 0 on X°, as dt_* is timelike ([[lem:iii-b-3-7]] (a)).

(2) By [[lem:iii-a1-2-1]] (1) at N = 3, □̄ = −2∂_(t_*) ρ(ρ∂_ρ − 3/2) + ᵇ□̄(0), and by [[lem:iii-d-3-1]] below
2ĒḠδ̄* = 2∂_(t_*) ρS̄ + γ_Υ ρ²M_E; this is [[eq:iii-d-2-1]]. The dual metric
ḡ⁻¹ = 2ρ∂_(t_*) ⊗_s ρ∂_ρ + ρ²((ρ∂_ρ)² + g_𝕊⁻¹) ([[eq:iii-a1-2-3]]) has no ∂_(t_*) ⊗ ∂_(t_*) term, and ĒḠδ̄* is of
first order.

(3) *The metric.* By [[prop:iii-b-3-6]], g_b − η ∈ |x|⁻²C^∞ with η = −dt² + dx² in the time t of
[[eq:iii-b-3-6]], and t_* = t − ψ(|x|) with ψ′ = 1 − 8m_0|x|⁻² on {|x| ≥ 3R_1}. So
η − ḡ = −(ψ′ − 1) d|x| ⊗_s (2dt_* + (ψ′ + 1)d|x|) ∈ ρ²C^∞, and k := g_b − ḡ ∈ ρ²C^∞(X̄; S²) in the frame dt_*, dx^i,
stationary; likewise g_b⁻¹ − ḡ⁻¹ ∈ ρ²C^∞, and ḡ^00 = 0 gives g_b^00 ∈ ρ²C^∞. *Derivatives.* ∂_(t_*) annihilates
stationary coefficients and ∂_(x^i) ∈ ρ𝒱_b(X̄), so ∂_(x^i) maps ρ^a C^∞(X̄) to ρ^(a+1)C^∞(X̄). The coefficients of ḡ
are homogeneous of degree 0, so Γ(ḡ) ∈ ρC^∞, and Γ′ := Γ(g_b) − Γ(ḡ) ∈ ρ³C^∞. *The 1-form d'Alembertian.* □_g ω
written out in Christoffel symbols has second-order coefficients g^(μν), first-order coefficients bilinear in g⁻¹ and
Γ, and zeroth-order coefficients in g⁻¹∂Γ and g⁻¹ΓΓ. Hence □_(g_b) − □̄ has second-order coefficients in ρ²C^∞
(vanishing in the ∂_(t_*)∂_(t_*) slot except for g_b^00), first-order coefficients in ρ³C^∞ (from Γ′ and from
(g_b⁻¹ − ḡ⁻¹)Γ(ḡ)) and zeroth-order coefficients in ρ⁴C^∞. *The modification.* Near infinity c_Υ = |x|⁻¹dt
([[def:iii-b-6-1]]) and c_Υ − c̄ = |x|⁻¹(ψ′ − 1)d|x| ∈ ρ³C^∞; with g_b⁻¹ − ḡ⁻¹ ∈ ρ² this gives
E^Υ_(g_b,∞) − Ē ∈ ρ³C^∞ (of order zero); G_(g_b) − Ḡ ∈ ρ²C^∞; δ*_(g_b) − δ̄* ∈ ρ³C^∞ (of order zero, by Γ′); and
E^Υ_(g_b,H) = 0 there. So 2E^Υ G δ* − 2ĒḠδ̄* is a sum of terms (zeroth-order ρ³ coefficients) times ∂, and of
zeroth-order terms in ρ⁴. *Sorting.* A Cartesian derivative is ∂_(t_*) or lies in ρ𝒱_b. Terms ρ²∂_(t_*)² form
−g_b^00 ∂_(t_*)²; terms ρ²∂_(t_*)∂_(x^i) and ρ³∂_(t_*) form Q_b ∂_(t_*) with Q_b ∈ ρ³ Diff_b¹; terms
ρ²∂_(x^i)∂_(x^j), ρ³∂_(x^i) and ρ⁴ form R_b ∈ ρ⁴ Diff_b². Smoothness in b is that of g_b ([[sec:iii-b-3]]). *(H2).*
By (2), the ∂_(t_*)-coefficient of □^Υ_b is −2ρ(ρ∂_ρ − 3/2 − S̄) + Q_b, so T = 2iρ(ρ∂_ρ − 3/2 − S̄) − iQ_b. In the
Cartesian frame □̄ acts componentwise as the scalar operator (proof of [[lem:iii-a1-2-1]]), so
ᵇ□̄(0) = ρ²(−(ρ∂_ρ)² + 2ρ∂_ρ + Δ_𝕊) Id there, and γ_Υ ρ²M_E ∈ ρ² Diff_b¹ after the change of frame Θ(x̂), which
commutes with ρ∂_ρ. With (ρD_ρ)² = −(ρ∂_ρ)² the last claim of (3) follows; the normal operator of P⁽⁰⁾ is that of
ρ⁻²(□̄^Υ)^(0), which does not involve b. ∎

On Kerr, g_b − ḡ ∈ ρC^∞, so that S − S̄ ∈ ρC^∞ and the zero energy operators differ by ρ³ Diff_b² [Hin26, (6.7)]. In
dimension 4 + 1 the mass enters at ρ², and each difference gains one power.

### The Minkowski model {#sec:iii-d-3}

We use the splitting [[eq:iii-a1-2-2]] of 1-forms: (ω_0, ω_1, ω_𝕊) is ω_0 dx̄⁰ + ω_1 dx̄¹ + rω_𝕊, with
x̄⁰ := t̄ + r and x̄¹ := t̄ − r = t_*; and (a, b, c, e′, f, q) is the symmetric 2-tensor
a(dx̄⁰)² + 2b dx̄⁰dx̄¹ + 2dx̄⁰ ⊗_s rc + e′(dx̄¹)² + 2dx̄¹ ⊗_s rf + r²q.

**Lemma {#lem:iii-d-3-1}** (The Minkowski model; [Hin26, Lemma 6.3] in dimension 4 + 1.) Let N ≥ 2 and m_N := 2/N,
the trace weight 2/(D − 2) of dimension D = N + 2 (2/3 at N = 3). In the splitting [[eq:iii-a1-2-2]] for 𝕊^N, with
D := ρ∂_ρ, e := e_Υ and γ := γ_Υ:

    c̄ = ρ(½, ½, 0),     ḡ⁻¹(c̄) = −ρ(∂_0 + ∂_1),

           ⎛ 2   2 − 2m_N(1 − e)   0   0   0   ½m_N(1 − e) tr ⎞
    Ē = γρ ⎜ 0   2 − 2m_N(1 − e)   0   2   0   ½m_N(1 − e) tr ⎟ ;
           ⎝ 0   0                 2   0   2   0              ⎠                                           {#eq:iii-d-3-1}

                                        ⎛ 1 − e   0   0 ⎞
    2ĒḠδ̄* = 2∂_(t_*) ρS̄ + γρ²M_E,   S̄ = γ ⎜ 1 − e   2   0 ⎟ ,
                                        ⎝ 0       0   1 ⎠

          ⎛ −(1 + e)D + Ne    −(1 − e)D − Ne   −e δ_𝕊 ⎞
    M_E = ⎜ (1 − e)D + Ne     (1 + e)D − Ne    −e δ_𝕊 ⎟ ;
          ⎝ 2d_𝕊              2d_𝕊             0      ⎠                                                   {#eq:iii-d-3-2}

so that □̄^Υ = −2∂_(t_*) ρ(D − N/2 − S̄) + (□̄^Υ)^(0) with

    (□̄^Υ)^(0) = ᵇ□̄(0) + γρ²M_E.                                                                         {#eq:iii-d-3-3}

At N = 2 these are [Hin26, (6.10)–(6.11)]. The spectrum of S̄ is γ(1 − e), 2γ and γ (with multiplicity N) at every N,
so min Re spec S̄ = γ min(1 − e, 1).

*Proof.* dt̄ = ½(dx̄⁰ + dx̄¹) and ḡ⁻¹(dt̄) = −∂_(t̄) = −(∂_0 + ∂_1) give the first two. For h = (a, b, c, e′, f, q),
ι_(ḡ⁻¹c̄)h = −ρ(a + b, b + e′, c + f) in the 1-form splitting, and tr h = −4b + tr q ([[sec:iii-a1-2]]), so
Ēh = −γ(2ιh − m_N(1 − e)c̄ tr h) is [[eq:iii-d-3-1]]. By [[lem:iii-b-6-2]], ĒḠh = −γ(2ι_(ḡ⁻¹c̄)h − e c̄ tr h), so

    2ĒḠh = 2γρ(2a + 2(1 − e)b + ½e tr q,  2(1 − e)b + 2e′ + ½e tr q,  2(c + f)).

Insert h = δ̄*ω from [[lem:iii-a1-2-1]] (1): a = −½ρDω_0, b = ½∂_(t_*)ω_0 + ¼ρD(ω_0 − ω_1),
c = ρ(½d_𝕊ω_0 − ¼(D + 1)ω_𝕊), e′ = ∂_(t_*)ω_1 + ½ρDω_1, f = ½∂_(t_*)ω_𝕊 + ρ(½d_𝕊ω_1 + ¼(D + 1)ω_𝕊), and
tr q = ρ(N(ω_0 − ω_1) − δ_𝕊ω_𝕊) (as tr g_𝕊 = N and tr δ*_𝕊 = −δ_𝕊). The ∂_(t_*)-terms are
2γρ∂_(t_*)((1 − e)ω_0, (1 − e)ω_0 + 2ω_1, ω_𝕊), which is 2∂_(t_*)ρS̄ω. The rest is γρ² times: in the first row
−2Dω_0 + (1 − e)D(ω_0 − ω_1) + eN(ω_0 − ω_1) − eδ_𝕊ω_𝕊; in the second (1 − e)D(ω_0 − ω_1) + 2Dω_1 + eN(ω_0 − ω_1) −
eδ_𝕊ω_𝕊; in the third 2d_𝕊ω_0 + 2d_𝕊ω_1 (the (D + 1)ω_𝕊 terms of c and f cancel). This is M_E. With
[[lem:iii-a1-2-1]] (1) for □̄ we get [[eq:iii-d-3-3]]. S̄ is lower triangular with diagonal γ(1 − e), 2γ, γ. At N = 2,
m_N = 1, 2 − 2m_N(1 − e) = 2e and ½m_N = ½, which is [Hin26, (6.10)]; and ±Ne = ±2e is [Hin26, (6.11)]. ∎

### Indicial roots {#sec:iii-d-4}

Write z := 4e_Υγ_Υ², κ := l(l + 2) and, for l ≥ 1,

    s_(l,1) := (l + 1)² + z/2 − ((l + 1)² + z + z²/4)^(1/2),   s_(l,2) := (l + 1)² + z/2 + ((l + 1)² + z + z²/4)^(1/2),

    ι^Υ_(sl,l+j) := ½ + (¼ + s_(l,j))^(1/2)  (j = 1, 2),     ι^Υ_(s0,2) := ½ + (9/4 + z)^(1/2).           {#eq:iii-d-4-1}

The type-wise indicial matrices are read off from [[eq:iii-d-3-3]], [[lem:iii-a1-2-1]] (1) and the identities
[[lem:iii-a1-1-5]]. On a scalar type l 1-form (aS, bS, c d_𝕊S), S ∈ 𝒮_l, l ≥ 1, the operator ρ⁻²(□̄^Υ)^(0) acts on
ρ^ι(a, b, c) as ρ^ι N_sl(ι)(a, b, c), where, with p := −ι² + 2ι,

               ⎛ p + κ + 3/2 − γ((1 + e)ι − 3e)   −3/2 − γ((1 − e)ι + 3e)            −κ(1 + eγ) ⎞
    N_sl(ι) =  ⎜ −3/2 + γ((1 − e)ι + 3e)           p + κ + 3/2 + γ((1 + e)ι − 3e)    κ(1 − eγ)  ⎟ ,
               ⎝ −2 + 2γ                           2 + 2γ                            p + κ − 1  ⎠           {#eq:s13-nsl}

with e := e_Υ and γ := γ_Υ. Indeed, by [[eq:iii-a1-2-11]] the operator ᵇ□̄(0) contributes p + κ on the first two
components, p + κ − 2 on the third, and the matrix with rows (3/2, −3/2, −κ), (−3/2, 3/2, κ), (−2, 2, 1); and M_E acts
by δ_𝕊(c d_𝕊S) = cκS and d_𝕊(aS) = a d_𝕊S. The scalar type 0 matrix N_s0(ι) is the upper left 2 × 2 block of
N_sl(ι) at κ = 0, acting on (aS, bS), S constant. On a vector type l 1-form (0, 0, cV), V ∈ 𝒱_l, the operator is
multiplication by N_vl(ι) := p + κ: ᵇ□̄(0) gives −ι² + 2ι + (κ − 1) + 1 by Δ_𝕊V = (κ − 1)V ([[lem:iii-a1-1-5]]), and
M_E vanishes on it, as δ_𝕊V = 0 and its third column is zero.

**Lemma {#lem:iii-d-4-1}** (Indicial roots; [Hin26, Lemma 6.6 and (6.17)] in dimension 4 + 1.) Let z ∈ [0, ½]. The
indicial roots of (□^Υ_b)^(0), which are those of (□̄^Υ)^(0), are, in the terminology of [[def:iii-a1-2-2]]:

s0: 1 − ι^Υ_(s0,2), 0, ι^Υ_(s0,2), 3;

sl, l ≥ 1: 1 − ι^Υ_(sl,l+2), 1 − ι^Υ_(sl,l+1), 1 − l, ι^Υ_(sl,l+1), ι^Υ_(sl,l+2), l + 3;

vl, l ≥ 1: −l, l + 2.

All are real and simple: each is a simple zero of the determinant of its type's indicial matrix, so the inverse of the
indicial family has at most simple poles. At z = 0, ι^Υ_(s0,2) = 2 and ι^Υ_(sl,l+j) = l + j, the roots of
[[lem:iii-a1-2-3]] for 1-forms. For 0 < z ≤ ½,

    ι^Υ_(sl,l+j) ∈ (l + j, l + j + ¼),     ι^Υ_(s0,2) ∈ (2, 2 + z/3],     2 < ι^Υ_(s1,2) < min(ι^Υ_(s0,2), 3),
                                                                                                          {#eq:iii-d-4-2}

and (0, ι^Υ_(s1,2)) is an indicial gap (at z = 0 the gap is (0, 2)). As z → 0, ι^Υ_(s0,2) = 2 + z/3 + O(z²),
ι^Υ_(sl,l+1) = l + 1 + lz/(2(l + 1)(2l + 1)) + O(z²) and ι^Υ_(sl,l+2) = l + 2 + (l + 2)z/(2(l + 1)(2l + 3)) + O(z²).
The s0 indicial solutions for the root 0 are spanned by dt̄, and the s1 ones, for each S ∈ 𝒮_1, by d(rS).

*Proof.* By [[lem:iii-d-2-1]] (3) the normal operator is that of the model. *The determinants.* Put
Q_l(s) := s² − (2 + 2κ + z)s + κ(κ + 1) + zκ. We show

    det N_s0(ι) = ι(ι − 3)(ι² − ι − 2 − z),   det N_sl(ι) = (l + 3 − ι)(l + ι − 1) Q_l(ι² − ι),
    N_vl(ι) = (ι + l)(l + 2 − ι).                                                                          {#eq:s13-dets}

The last is p + κ = −ι² + 2ι + l² + 2l. For s0, expanding the 2 × 2 determinant,

    det N_s0 = (p + 3/2)² − γ²((1 + e)ι − 3e)² − 9/4 + γ²((1 − e)ι + 3e)² = p(p + 3) − 4eγ²ι(ι − 3),

and p = −ι(ι − 2), p + 3 = −(ι − 3)(ι + 1), so det N_s0 = ι(ι − 3)((ι − 2)(ι + 1) − z). For sl, pass to the
coordinates u := a + b, w := a − b (the coefficients of dt̄ and dr) and take the sum and the difference of the first
two rows; this does not change the determinant (the row operation and the change of coordinates have determinants −2
and −½). With P := p + κ the matrix becomes

        ⎛ P         −2eγ(ι − 3)   −2eγκ ⎞
    M = ⎜ −2γι      P + 3         −2κ   ⎟ ,
        ⎝ 2γ        −2            P − 1 ⎠

acting on (u, w, c). Expanding along the first row and collecting the terms in γ²,

    det M = P((P + 3)(P − 1) − 4κ) + z(P(κ − ι² + 3ι) + ι² − 3ι − 3κ).

Now (P + 3)(P − 1) − 4κ = (P + 1)² − 4(l + 1)² = (P − 2l − 1)(P + 2l + 3), and P = −(ι − l − 2)(ι + l),
P − 2l − 1 = −(ι − l − 1)(ι + l − 1), P + 2l + 3 = −(ι − l − 3)(ι + l + 1). With s := ι² − ι one has
(ι − l − 1)(ι + l) = s − l(l + 1) and (ι − l − 2)(ι + l + 1) = s − (l + 1)(l + 2), so the first term is
(l + 3 − ι)(l + ι − 1)(s − l(l + 1))(s − (l + 1)(l + 2)). For the second, put Y := κ − ι² + 3ι; then P = Y − ι,
ι² − 3ι − 3κ = −Y − 2κ, (l + 3 − ι)(l + ι − 1) = Y + ι − 3 and κ − s = Y − 2ι. So the bracket of the second term
is PY − Y − 2κ = Y² − ιY − Y − 2κ, while (Y + ι − 3)(Y − 2ι) = Y² − ιY − 3Y − 2ι² + 6ι; their difference
2Y + 2ι² − 6ι − 2κ vanishes by the definition of Y. So the second term is z(l + 3 − ι)(l + ι − 1)(κ − s). Finally

    (s − l(l + 1))(s − (l + 1)(l + 2)) = s² − (2 + 2κ)s + κ(κ + 1),                                     {#eq:s13-qfactor}

since l(l + 1) + (l + 1)(l + 2) = 2(l + 1)² = 2 + 2κ and l(l + 1)²(l + 2) = κ(κ + 1); so Q_l(s) is
(s − l(l + 1))(s − (l + 1)(l + 2)) + z(κ − s), and [[eq:s13-dets]] follows.

*The list.* The discriminant of Q_l is 4(l + 1)² + 4z + z² > 0 (as 1 + κ = (l + 1)²), so its roots are
s_(l,1) < s_(l,2), and ι² − ι = s gives ι = ½ ± (¼ + s)^(1/2); ι² − ι = 2 + z gives the s0 pair. This is the list.

*Bounds.* By [[eq:s13-qfactor]], Q_l(l(l + 1)) = lz and Q_l((l + 1)(l + 2)) = −(l + 2)z. So for z > 0,
l(l + 1) < s_(l,1) < (l + 1)(l + 2) < s_(l,2), and as ι ↦ ι² − ι increases on ι > ½, ι^Υ_(sl,l+1) > l + 1 and
ι^Υ_(sl,l+2) > l + 2. For the upper bounds, ∂_z s_(l,j) ≤ ½ + (1 + z/2)/(2(l + 1)) ≤ 1 + z/4, so
s_(l,j) − s_(l,j)|_(z=0) ≤ z(1 + z/8), and ι − (l + j) ≤ (s − s|_(z=0))/(2(l + j) − 1) ≤ z(1 + z/8)/3 < ¼ for z ≤ ½;
similarly (9/4 + z)^(1/2) ≤ 3/2 + z/3. *The ordering.* ι^Υ_(s1,2) < ι^Υ_(s0,2) iff s_(1,1) < 2 + z, iff
2 − z/2 < (4 + z + z²/4)^(1/2), iff (squaring, z < 4) z > 0; ι^Υ_(s1,2) > 2 iff s_(1,1) > 2, iff
2 + z/2 > (4 + z + z²/4)^(1/2), iff z > 0; and ι^Υ_(s1,2) < 9/4 < 3. *The gap.* Every root in the list other than
ι^Υ_(s1,2) is ≤ 0 or ≥ min(ι^Υ_(s0,2), 3): the negative ones are 1 − ι ≤ −l, 1 − l ≤ 0 and −l; the positive ones are
3, ι^Υ_(s0,2), l + 3 ≥ 4, l + 2 ≥ 3, and ι^Υ_(sl,l+j) ≥ l + j ≥ 3 unless (l, j) = (1, 1). *Simplicity.* Within each
type the roots are distinct for z ∈ [0, ½] by the bounds (ι^Υ_(sl,l+1) < l + 5/4 < l + 2 ≤ ι^Υ_(sl,l+2) < l + 9/4 <
l + 3, and the negative ones likewise), so each is a simple zero of a polynomial determinant, and
N(ι)⁻¹ = adj N(ι)/det N(ι) has at most a simple pole there. *Expansions.* s_(l,1) = l(l + 1) + lz/(2(l + 1)) + O(z²),
s_(l,2) = (l + 1)(l + 2) + (l + 2)z/(2(l + 1)) + O(z²), and dι/ds = (2ι − 1)⁻¹. *Indicial solutions at 0.* dt̄ and
d(rS) are Killing 1-forms of the model (translations), homogeneous of degree 0, of types s0 and s1
([[lem:iii-a1-2-4]]); □̄^Υ = 2(δ̄ + Ē)Ḡδ̄* annihilates them, and they are stationary, so they solve the indicial
equation at ι = 0; the root being simple, they span. ∎

On Kerr the s0 pair is ±(1 + 4eγ²)^(1/2), symmetric about 0, and the gap is (0, λ^Υ_(s1,1)) [Hin26, (6.17)]. In
dimension 4 + 1 the roots pair about different points: the roots of ι² − ι = s, the s0 pair and the ι^Υ_(sl,·) with
their partners 1 − ι, pair about ½; the vl roots −l, l + 2 about 1; the s0 roots 0, 3 about 3/2; and the sl roots
1 − l, l + 3 about 2. The index of ι^Υ_(sl,·) is shifted by one, and the gap is (0, ι^Υ_(s1,2)) with ι^Υ_(s1,2) just
above 2.

**Remark {#rem:s13-trace-weight}** (The trace weight.) If the trace weight 2/3 of [[def:iii-b-6-1]] is replaced by
1, then, as tr_g G_g h = −(3/2) tr_g h in dimension 5, ĒḠh = −γ(2ι_(ḡ⁻¹c̄)h − ½(3e − 1)c̄ tr h): every formula of
[[lem:iii-d-3-1]] and [[eq:s13-dets]] holds with e replaced by (3e − 1)/2. In particular the spectrum of S̄ becomes
(3/2)(1 − e)γ, 2γ, γ, and the s0 root 2 of the unmodified operator moves to (1 + (9 − 8γ²(1 − 3e))^(1/2))/2, which
lies in (1, 2) when e < 1/3 and 0 < γ²(1 − 3e) < 1, inside the gap (0, 2). The weight 2/3 = 2/(D − 2) avoids this:
(2/(D − 2))(1 − D/2) = −1 in every dimension D, so that ĒḠ takes the same form −γ(2ι − e c̄ tr) as in dimension 4
with the weight 1.

### The subprincipal data {#sec:iii-d-5}

#### The structure at infinity and the horizon threshold {#sec:iii-d-5-1}

On g_(b_0), in the ingoing chart (v, r, y), y = (y¹, y², y³) coordinates on 𝕊³, the metric is
g = −f dv² + 2dv dr + r²g_𝕊, so g^vv = 0, g^vr = 1, g^rr = f, g^(ra) = g^(va) = 0, and |dg| = r³|dv dr dg_𝕊|. Its
Christoffel symbols with a lower index v are, from g_vv = −f and g_vr = 1,

    Γ^v_vv = f′/2,   Γ^r_vv = ff′/2,   Γ^r_vr = −f′/2,   Γ^v_vr = 0,   Γ^λ_va = 0,                        {#eq:s13-chris}

since Γ^λ_vν = ½g^(λκ)(∂_ν g_κv − ∂_κ g_vν) for the stationary metric, g_κv does not depend on the angles, and
g_va = 0. At r_h, f = 0 and f′(r_h) = 2m_0 r_h⁻³ = 2/r_h.

**Proposition {#prop:np-10-18}** (Structure at infinity and the horizon threshold.)

(i) On 4 + 1 Minkowski space, in the time t_* = t̄ − r and the Cartesian frame (dt̄, dx^i), □̄^Υ is
−2∂_(t_*) ρ(ρ∂_ρ − 3/2 − S̄) plus a stationary operator, with no ∂_(t_*)² term, and

    S̄ω = γ_Υ(ω + ω(∂_(t̄)) dt_* + e_Υ ḡ⁻¹(dt_*, ω) dt̄).

(ii) The spectrum of S̄ is γ_Υ(1 − e_Υ), 2γ_Υ, and γ_Υ on the three angular directions.

(iii) On g_(b_0), let c_H = c_v dv + c_r dr near r_h, E_H h := 2ι_(g⁻¹c_H) h − (2/3)c_H tr_g h, and γ_H ∈ ℝ. At
N*ℋ, that is at r = r_h and ζ = ξ dr, the subprincipal symbol of □_(g_(b_0)) + 2γ_H E_H G δ*, on half-densities by
|dg| and in the coordinate frame (dv, dr, dy^a), is iξf′(r_h)K, where

        ⎛ 1 + c_vγ_H r_h    0                    0               ⎞
    K = ⎜ c_rγ_H r_h        −1 + 2c_vγ_H r_h     0               ⎟ .
        ⎝ 0                 0                    c_vγ_H r_h Id_3 ⎠

(iv) On g_(b_0), with t the static time and t_* := t − r, g⁻¹(dt_*, dt_*) = −(2m_0ρ² − m_0²ρ⁴)/(1 − m_0ρ²), which
lies in ρ²C^∞; and g − ḡ = m_0ρ²dt² + m_0ρ²(1 − m_0ρ²)⁻¹dr² for ḡ := −dt² + dr² + r²g_𝕊, which is O(ρ²) in the frame
(dt, dr, r dx̂).

*Proof.* (i) The first part is [[eq:iii-d-2-1]]. In the null splitting, dt_* = dx̄¹, dt̄ = ½(dx̄⁰ + dx̄¹),
ω(∂_(t̄)) = ω_0 + ω_1 (as ∂_(t̄) = ∂_0 + ∂_1), and ḡ⁻¹(dt_*, ω) = −2ω_0 by [[eq:iii-a1-2-3]]. So the right side is
γ_Υ((1 − e_Υ)ω_0, (1 − e_Υ)ω_0 + 2ω_1, ω_𝕊), which is S̄ω by [[eq:iii-d-3-2]]; the expression does not depend on the
frame. (ii) is [[lem:iii-d-3-1]].

(iii) *The unmodified operator.* Let 𝔪 := r³|g_𝕊|^(1/2), so |dg| = 𝔪|dv dr dy|. For an operator P on ℂ⁵-valued
functions with scalar principal part −g^(αβ)∂_α∂_β, the subprincipal symbol on half-densities by |dg| is that of
P̃ := 𝔪^(1/2)P𝔪^(−1/2) on half-densities by |dv dr dy|, namely p̃_1 − (1/2i)Σ_j ∂_(x^j)∂_(ζ_j) p̃_2, p̃_k the
homogeneous parts of the full symbol of P̃. Since ∇_α∇_βω_ν = ∂_α(∂_βω_ν − Γ^μ_βν ω_μ) − Γ^κ_αβ ∇_κω_ν
− Γ^μ_αν ∇_βω_μ, in coordinates

    (□ω)_ν = □_0 ω_ν + 2g^(αβ)Γ^μ_(αν) ∂_β ω_μ + (terms without derivatives of ω),
    □_0 := −g^(αβ)∂_α∂_β + g^(αβ)Γ^κ_(αβ)∂_κ.

The scalar wave operator □_0 is formally self-adjoint for |dg| and has real coefficients; so 𝔪^(1/2)□_0𝔪^(−1/2) is
formally self-adjoint for |dv dr dy| and real, and its subprincipal symbol is both real and purely imaginary, hence
zero. Conjugation by 𝔪^(1/2) changes the term 2g^(αβ)Γ^μ_(αν)∂_β only by terms without derivatives. So the
subprincipal symbol of □ is the matrix u ↦ (2iζ^αΓ^μ_(αν)u_μ)_ν, ζ^α := g^(αβ)ζ_β. At N*ℋ, ζ^α = ξg^(αr), that is
ζ♯ = ξ∂_v, and by [[eq:s13-chris]] the matrix is u ↦ (iξf′u_v, −iξf′u_r, 0) at r_h. *The modification.* By
[[lem:iii-b-6-2]], E_H G h = 2ι_(c_H♯) h, so 2γ_H E_H G δ*u = 4γ_H ι_(c_H♯) δ*u, whose first-order part is
2γ_H c^α(∂_α u_ν + ∂_ν u_α), c^α := g^(αβ)(c_H)_β. It has no second-order part, so it adds to the subprincipal symbol
its symbol 2iγ_H(g⁻¹(c_H, ζ)u_ν + ζ_ν g⁻¹(c_H, u)). At r_h and ζ = ξdr, g⁻¹(c_H, ζ) = ξc_v,
g⁻¹(c_H, u) = c_v u_r + c_r u_v and ζ_ν = ξδ^r_ν. So the total is
iξ((f′ + 2γ_H c_v)u_v, 2γ_H c_r u_v + (−f′ + 4γ_H c_v)u_r, 2γ_H c_v u_a), and dividing by f′(r_h) = 2/r_h gives K.

(iv) g⁻¹(dt − dr, dt − dr) = g^tt + g^rr = −f⁻¹ + f = −(1 − f)(1 + f)/f with 1 − f = m_0ρ² and 1 + f = 2 − m_0ρ²;
and g − ḡ = (1 − f)dt² + (f⁻¹ − 1)dr². ∎

**Lemma {#lem:iii-d-5-1}** (The threshold.) Let c_(Υ,H) = −½χ(r)dr near r_h, with χ = 1 near r_h (the choice of
[[sec:iii-d1-1]]). Then at b_0 the threshold quantity ϑ_ℋ of [[eq:i-a-1-5]], computed in a suitable fibre inner
product, is 1 for every γ_(Υ,H), and the regularity condition s > ½ + ϑ_ℋ is s > 3/2. For every δ > 0 there is a
neighbourhood of b_0 (and of (e_Υ, γ_Υ, γ_(Υ,H)) in a compact set) on which ϑ_ℋ < 1 + δ in a fixed fibre inner
product.

*Proof.* Near r_h, E^Υ_(g,∞) vanishes and the horizon part of □^Υ_(b_0) is 2γ_(Υ,H)E_H G δ* with E_H as in
[[prop:np-10-18]] (iii) and c_H = c_(Υ,H) ([[def:iii-b-6-1]]). Here c_v = 0, so by [[prop:np-10-18]] (iii) K has the
distinct eigenvalues 1, −1, 0, the last with a diagonal block; K is diagonalisable, and in the inner product making its
eigenvectors orthonormal its self-adjoint part is diagonal with largest eigenvalue 1. The normalisation of
[[eq:i-a-1-5]], β_0⁻¹p_(1,±)(0) with p_(1,±) = ±ρ_∞σ_1(Im_h P̂), divides ξf′(r_h) by the red-shift rate β_0ρ_∞⁻¹,
which on Tangherlini is ξf′(r_h) up to the orientation sign that the ± removes; so ϑ_ℋ is the largest eigenvalue, 1.
The subprincipal symbol at N*ℋ_b and β_0 depend continuously on b (the horizon ℋ_b and its conormal bundle depend
smoothly on b, by (Dyn)), so the largest eigenvalue in the fixed inner product is continuous. ∎

On Kerr, [Hin26, footnote 71] gives the threshold 3/2 for γ_(Υ,H) = 0 and a value close to 3/2 for small γ_(Υ,H). In
dimension 4 + 1 it is the same at γ_(Υ,H) = 0, and for this c_(Υ,H) it is exactly 3/2 for every γ_(Υ,H).

#### The trapped set {#sec:iii-d-5-2}

[Hin26, Lemma 6.4] proves that □^Υ_b is strongly trapping admissible ([Hin26c, Definition 5.8]: for every ϵ > 0 some
fibre inner product makes the skew part at the trapped set smaller than ϵ) at every subextremal Kerr parameter. The
theory of [[ch:s02]] does not use that property: [[thm:i-b-1-3]] assumes (Γ.4), the condition γ_− < 0, that is
sup_Γ λ_max(p_1^Γ) < ½ν_min, and its losses are governed by δ_Γ ([[eq:i-b-1-4]]). That condition is open, and we
prove it near b_0. We use the following facts on Tangherlini, proved in [[ch:s12]].

(a) The subprincipal operator of □_(g_(b_0)) on half-densities by |dg| is −i∇^(π*T*)_(H_G) ([[prop:np-10-17-i]]).

(b) The trapped set in the future characteristic set is {r² = 2m_0, ξ = 0}; at the value 1 of the semiclassical
parameter it is {r² = 2m_0, ξ = 0, C = 4m_0}, C = r²|η|² the Casimir of 𝕊³, with expansion rates ±ν,
ν = 4(2m_0)^(−1/2), {φ_u, φ_s} = ν/f > 0, dG_1 ≠ 0, and β_0 = 1/f(r_ph) = 2 ([[prop:np-10-17-ii]],
[[prop:np-10-19-ii]]).

(c) On the characteristic set, the frame e_0 = ζ, e_1 = r(ζ_(1)w^(0) + ζ_(0)w^(1)),
e_2 = ½r²(ζ_(0)w^(0) + ζ_(1)w^(1) − η), with w^(0) = f^(1/2)dt and w^(1) = f^(−1/2)dr, has Gram matrix CJ,
J = ((0, 0, −1), (0, 1, 0), (−1, 0, 0)), and ∇_(H_G)e_0 = 0, ∇_(H_G)e_1 = −2σe_0, ∇_(H_G)e_2 = −2σe_1; an angular
covector is orthogonal to all three if and only if it is orthogonal to η ([[prop:np-10-17-iii]], [[prop:np-10-17-iv]]).

(d) In the inner product diag(1, ϵ_1⁻¹, ϵ_1⁻²) on span{e_0, e_1, e_2}/C^(1/2), the endomorphism p_1 = −½(M + M*), M
the connection matrix of (c), has spectrum 0, ±(2ϵ_1)^(1/2) ([[prop:np-10-17-v]], [[prop:np-10-19-iii]]).

**Lemma {#lem:iii-d-5-2}** (The trapped set; [Hin26, Lemma 6.4] in dimension 4 + 1, in the form [[thm:i-b-1-3]]
uses.) Assume (Dyn), with the trapped sets Γ_b (at z_0 = ±1) depending continuously on b and Γ_(b_0) as in (b). For
every ϵ > 0 there are a stationary fibre inner product h_Γ on π*T* over a neighbourhood of Γ_(b_0) in phase space,
homogeneous of degree 0 (it depends on the covector, as (H7) of [[sec:i-b-1-2]] and [[def:ii-c-2-1]] allow,
[[lem:i-b-6-0]] reducing it to a standard one), and a neighbourhood ℬ_ϵ of b_0, such that for b ∈ ℬ_ϵ and every E_Υ
as in [[sec:iii-d-1]], sup_(Γ_b) λ_max(p_1^Γ) < ϵ. In particular (Γ.4) holds with γ_− < 0 (take ϵ < ½ν_min), and
δ_Γ(0), which by [[eq:i-b-1-4]] tends to 0 with γ_+, is as small as wished.

*Proof.* E^Υ vanishes over U_Γ ⊃ π(Γ_b) ([[sec:iii-d-1]]), so p_1^Γ is that of □_(g_b). *At b_0.* Near Γ_(b_0),
where C > 0, split π*T* = 𝒫 ⊕ V_⊥ with 𝒫 := span{e_0, e_1, e_2} and V_⊥ its g-orthogonal complement, the angular
covectors orthogonal to η, by (c); g is positive definite on V_⊥. 𝒫 is ∇_(H_G)-invariant by (c), and as ∇ is metric,
so is V_⊥, on which ∇_(H_G) is g-skew. Take h_Γ := diag(1, ϵ_1⁻¹, ϵ_1⁻²) on 𝒫 in the frame e_j/C^(1/2), and g on
V_⊥; it is stationary and homogeneous of degree 0, as H_G C = 0 and C has degree 2. In these frames h_Γ is constant,
−iH_G is symmetric for the symplectic volume, and H_G σ = 0, so by (a) p_1^Γ is −½(M + M*) on 𝒫 and 0 on V_⊥, with
largest eigenvalue (2ϵ_1)^(1/2) by (d) at the point considered. The isometries of Tangherlini (time translations and
SO(4)) act transitively on Γ_(b_0) and preserve the construction of the frame, so this holds at every point. Choose
ϵ_1 with (2ϵ_1)^(1/2) < ϵ/2. *Near b_0.* Extend h_Γ to a stationary inner product on a neighbourhood of Γ_(b_0). The
endomorphism p_1 is built from the subprincipal symbol of □_(g_b) and h_Γ, continuous in b uniformly near Γ_(b_0),
and Γ_b → Γ_(b_0) by (Dyn); so sup_(Γ_b) λ_max(p_1^Γ) < ϵ for b near b_0. ν_min and β_0 are continuous in b by (Dyn)
and positive at b_0. Two conventions enter. First, p_1^Γ is the endomorphism of [[lem:i-b-6-0]] for this h_Γ, which
in the frame e_j/C^(1/2), where h_Γ is constant, is the h_Γ-imaginary part of the subprincipal operator. Second, (a)
uses half-densities by |dg|, while the adjoints of [[ch:s01]] are for |dx| = r³dr dx̂ and dt_*. On Tangherlini
|dg| = |dt_*| r³dr dx̂, so the two agree at b_0; near b_0 the change of density by f_b := |dg_b|/|dg_(b_0)| adds the
scalar ½f_b⁻¹H_G f_b = O(|b − b_0|) to p_1 (the remark after [[lem:ii-c-2-2]]), which the continuity step absorbs. ∎

### High energies and bounded frequencies {#sec:iii-d-6}

**Proposition {#prop:iii-d-6-1}** ([Hin26, Proposition 6.5] in dimension 4 + 1.) Assume (Dyn). Fix c_Υ and c_(Υ,H) as
in [[sec:iii-d-1]]. There are C_0 and a neighbourhood ℬ′ of b_0 such that for b ∈ ℬ′ and (e_Υ, γ_Υ, γ_(Υ,H)) in a
fixed compact set, (□^Υ_b)^(σ): 𝒳_σ → 𝒴_σ ([[thm:i-a-7-2]], orders as in [[thm:i-b-1-3]] (3)) is invertible for
Im σ ≥ 0, |σ| ≥ C_0.

*Proof.* [[lem:iii-d-2-1]] gives (H1), (H2) and the operator part of (H6); [[lem:iii-d-5-1]] the threshold in (H3),
with s > 3/2 + δ; [[lem:iii-d-5-2]] (Γ.4) with γ_− < 0; (Dyn) the rest of (H3)–(H8); and the continuity in
(b, e_Υ, γ_Υ, γ_(Υ,H)) of every datum is (H5), extended as in [[sec:i-b-9]]. [[thm:i-b-1-3]] (3) applies, with
constants uniform in the parameters by [[sec:i-b-9]]. ∎

Mode stability at bounded nonzero frequencies needs that of the unmodified operator at b_0, which [Hin26] takes from
[AHW24, Theorem 5.1] on Kerr. On five-dimensional Tangherlini it reduces to three ordinary differential equations, by
the following identities. Write □ := □_(g_(b_0)), and let fields be e^(−iσt) times stationary ones, σ ∈ ℂ, in the
static chart on {r > r_h}; Φ_* := dΦ/dr_* = fΦ′.

**Proposition {#prop:np-10-16}** (The mode equations on Tangherlini.)

(i) For every metric, on 1-forms, 2δ_g G_g δ*_g = ∇*∇ − Ric and dδ_g + δ_g d = ∇*∇ + Ric. So on g_(b_0),
□ = dδ + δd = ∇*∇.

(ii) For u = r^(−3/2)Φ(r)S e^(−iσt), S ∈ 𝒮_l: −fr^(3/2)e^(iσt)(δdu)/S = f(fΦ′)′ + σ²Φ − V_0Φ, with
V_0 := (f/r²)(κ + 3/4 + 9m_0/(4r²)).

(iii) For A = r^(−1/2)Φ(r)Y e^(−iσt), Y a co-closed 1-form on 𝕊³ with δ_𝕊 d_𝕊 Y = ΛY: δA = 0, and δdA = 0 if and
only if f(fΦ′)′ + σ²Φ − V_1Φ = 0, with V_1 := (f/r²)(Λ − 1/4 + 5m_0/(4r²)). For Y ∈ 𝒱_l, Λ = (l + 1)².

(iv) Let A = (a(r)S dt + b(r)S dr)e^(−iσt), S ∈ 𝒮_l; every scalar type 1-form (aS dt + bS dr + c d_𝕊S)e^(−iσt)
differs from one of this form by d(cS e^(−iσt)), which does not change dA. Write dA = F_tr S e^(−iσt) dt ∧ dr + …,
so that F_tr = −iσb − a′, and M := δdA = (M_t S dt + M_r S dr)e^(−iσt) + (angular part). Then W := r³F_tr satisfies

    R[W] := (fW′/r)′ − κW/r³ + σ²W/(rf) = (r²M_t)′ + iσr²M_r,

and fr^(1/2)R[r^(1/2)Φ] = f(fΦ′)′ + σ²Φ − V_2Φ with V_2 := (f/r²)(κ + 3/4 − 7m_0/(4r²)). Where F_tr = 0,
M_t = κa/r² and M_r = κb/r². At l = 0, M_r = −iσF_tr/f, and F_tr S dt ∧ dr is all of dA. For l ≥ 1 and every
solution of R[W] = 0, A(W) := (κr)⁻¹(−fW′S dt + iσf⁻¹WS dr)e^(−iσt) satisfies δdA(W) = 0 and r³F_tr = W.

(v) For r > r_h: V_0 > 0; V_1 > 0 when Λ ≥ 2; V_2 > 0 when κ ≥ 3, while at l = 0 V_2 is negative near r_h. The
tortoise coordinate r_* := r + ½r_h log((r − r_h)/(r + r_h)) has dr_*/dr = 1/f and
r_* = r − m_0/r − (m_0²/3)r⁻³ + O(r⁻⁵); f′(r_h)/2 = 1/r_h; and dι_Tω + ι_Tdω = −iσω for T = ∂_t and every
ω = e^(−iσt)ω_0, ω_0 stationary.

*Proof.* (i) With δω = −∇^μω_μ and δ*ω = ½(∇_μω_ν + ∇_νω_μ), tr δ*ω = −δω, so Gδ*ω = δ*ω + ½gδω and
2(δGδ*ω)_ν = −∇^μ∇_μω_ν − ∇^μ∇_νω_μ − ∇_ν δω. The Ricci identity gives
∇^μ∇_νω_μ = ∇_ν∇^μω_μ + Ric_ν^μ ω_μ = −∇_νδω + (Ric ω)_ν, so 2δGδ*ω = ∇*∇ω − Ric ω. Likewise
(δdω)_ν = −∇^μ(∇_μω_ν − ∇_νω_μ) = (∇*∇ω)_ν − (dδω)_ν + (Ric ω)_ν. g_(b_0) is Ricci-flat ([[prop:iii-b-3-4]]).

(ii) On functions δdu = −|g|^(−1/2)∂_μ(|g|^(1/2)g^(μν)∂_νu) with |g|^(1/2) = r³|g_𝕊|^(1/2), g^tt = −1/f,
g^rr = f and g^(ab) = r⁻²g_𝕊^(ab); so for u = e^(−iσt)u_0(r)S, e^(iσt)δdu = (−σ²f⁻¹u_0 − r⁻³(r³fu_0′)′ + κr⁻²u_0)S.
With u_0 = r^(−3/2)Φ, r³f u_0′ = f(r^(3/2)Φ′ − (3/2)r^(1/2)Φ), and
r⁻³(r³fu_0′)′ = r^(−3/2)((fΦ′)′ − (3/2)r⁻¹f′Φ − (3/4)r⁻²fΦ). Multiplying by −fr^(3/2) gives the equation with
V_0 = f((3/2)r⁻¹f′ + (3/4)r⁻²f + κr⁻²), and (3/2)r⁻¹f′ = 3m_0r⁻⁴, (3/4)r⁻²f = (3/4)r⁻² − (3/4)m_0r⁻⁴.

(iii) Put ψ := r^(−1/2)Φe^(−iσt). Then δA = −r⁻³|g_𝕊|^(−1/2)∂_a(r|g_𝕊|^(1/2)g_𝕊^(ab)ψY_b) = r⁻²ψδ_𝕊Y = 0. For
the 2-form F := dA, (δF)^ν = −|g|^(−1/2)∂_μ(|g|^(1/2)F^(μν)), with F_ta = ∂_tψ Y_a, F_ra = ∂_rψ Y_a and
F_ab = ψ(d_𝕊Y)_ab. The t- and r-components of δF are angular divergences of multiples of Y, which vanish as
δ_𝕊Y = 0. The angular component is

    (δF)_a = (f⁻¹∂_t²ψ − r⁻¹∂_r(rf∂_rψ) + Λr⁻²ψ)Y_a,

the last term from the angular divergence of F^(ab) = r⁻⁴ψ(d_𝕊Y)^(ab), lowered by g_ab = r²(g_𝕊)_ab. With
∂_t² = −σ² and r⁻¹(rf(r^(−1/2)Φ)′)′ = r^(−1/2)((fΦ′)′ − ½r⁻¹f′Φ + ¼r⁻²fΦ), multiplying by −fr^(1/2)e^(iσt) gives the
equation with V_1 = f(½r⁻¹f′ − ¼r⁻²f + Λr⁻²), and ½r⁻¹f′ = m_0r⁻⁴, −¼r⁻²f = −¼r⁻² + ¼m_0r⁻⁴. For Y ∈ 𝒱_l,
δ_𝕊d_𝕊Y = Δ_𝕊Y + 2Y on co-closed 1-forms of 𝕊³ (the Ricci identity on the unit 𝕊³, where Ric = 2g_𝕊), and
Δ_𝕊Y = (κ − 1)Y ([[lem:iii-a1-1-5]]); so Λ = κ + 1 = (l + 1)².

(iv) Up to the factor e^(−iσt), F_tr = −iσb − a′, F_at = a∂_aS, F_ar = b∂_aS and F_ab = 0. Then
F^(rt) = g^rr g^tt F_rt = F_tr and F^(at) = −(fr²)⁻¹a∇^a_𝕊S, so, using ∇_(𝕊,a)∇^a_𝕊S = −κS,
(δF)^t = (−r⁻³W′ − κa(fr²)⁻¹)S and M_t = −f(δF)^t/S = fW′r⁻³ + κar⁻². Similarly F^(tr) = −F_tr and
F^(ar) = fr⁻²b∇^a_𝕊S give (δF)^r = (−iσr⁻³W + κfbr⁻²)S, so M_r = f⁻¹(δF)^r/S = −iσW/(fr³) + κb/r². Hence

    (r²M_t)′ + iσr²M_r = (fW′/r)′ + κa′ + σ²W/(fr) + iσκb = (fW′/r)′ + σ²W/(rf) − κF_tr = R[W].

The two formulas give M_t = κa/r², M_r = κb/r² where W = 0, and M_r = −iσF_tr/f at κ = 0, where d_𝕊S = 0, so that
dA = F_tr S dt ∧ dr. Next, with W = r^(1/2)Φ, (fW′/r)′ = r^(−1/2)(fΦ′)′ + ½r^(−3/2)f′Φ − (3/4)r^(−5/2)fΦ, so
fr^(1/2)R[r^(1/2)Φ] = f(fΦ′)′ + σ²Φ − f(κr⁻² + (3/4)fr⁻² − ½f′r⁻¹)Φ, and (3/4)f − ½rf′ = 3/4 − (7/4)m_0r⁻².
Finally, for A(W), a = −fW′/(κr) and b = iσW/(κrf), so F_tr = σ²W/(κrf) + (fW′/r)′/κ = W/r³ when R[W] = 0;
M_t = M_r = 0 by the formulas above; and the angular component of δdA, which by the same calculation is
r⁻¹(iσra/f + (rfb)′)d_𝕊S, vanishes since iσra/f = −iσW′/κ and (rfb)′ = iσW′/κ.

(v) V_0 > 0 is clear; Λ − 1/4 > 0; and κ + 3/4 − (7/4)m_0/r² > κ − 1 ≥ 2 for κ ≥ 3, as m_0/r² < 1, while at κ = 0
and r = r_h the bracket is −1. dr_*/dr = 1 + ½r_h((r − r_h)⁻¹ − (r + r_h)⁻¹) = r²/(r² − m_0) = 1/f, and
log((1 − x)/(1 + x)) = −2x − (2/3)x³ + O(x⁵), x = r_h/r, gives the expansion. f′(r_h) = 2m_0r_h⁻³ = 2/r_h. The last
identity is Cartan's formula, as the Lie derivative along T is ∂_t in the static chart. ∎

The potentials are positive at l ≥ 1. They differ from those on four-dimensional Schwarzschild by the terms that 𝕊³
brings: 3/4 in V_0 and V_2, −1/4 in V_1, and 9/4, 5/4 and −7/4 times m_0/r². At l = 0 the Maxwell scalar potential is
negative near the horizon, and that sector is settled by the relation M_r = −iσF_tr/f, not by positivity.

**Proposition {#prop:iii-d-6-2}** (Mode stability of □ on Tangherlini away from zero frequency.) Assume (Dyn) at b_0.
For σ ≠ 0 with Im σ ≥ 0, □̂(σ): 𝒳_σ → 𝒴_σ is invertible.

*Proof.* By [[thm:i-a-7-2]] (3) and [[thm:i-b-1-3]] (3), which apply to □, the case E_Υ = 0 of
[[sec:iii-d-2]]–[[sec:iii-d-5]], □̂(σ) is Fredholm of index 0, so it suffices to show injectivity. Let u ∈ 𝒳_σ with
□̂(σ)u = 0. By [[thm:i-a-7-2]] (5) with S̄ = 0, u ∈ 𝒜^(3/2−ϵ)(X̄) for every ϵ > 0, smooth up to {|x| = r_0}, hence
across the horizon r = r_h > r_0, and conormal at infinity. Let ω := e^(−iσt_*)u, so □ω = 0.

*The class.* The time t_* of [[eq:iii-b-3-6]] is regular across the future horizon and outgoing at infinity:
t_* = v + F_H(r) near r_h with F_H smooth across r_h in the ingoing chart, and t_* = t − r_* + c′ + O(r⁻¹), with all
derivatives, as r → ∞ ([[eq:iii-b-3-6]] and [[lem:iii-b-3-5]] at A = 0). So in the static chart ω = e^(−iσt)ω_0
with ω_0 = e^(−iσr_*) × (smooth across r_h in (v, r)) near r_h and ω_0 = e^(iσr_*) × (conormal, O(r^(−3/2+ϵ))) near
infinity. In the static frame the coefficients a, b of [[prop:np-10-16]] (iv) are singular at r_h (b = A_r + A_v/f);
the argument below uses only F_tr = F_vr and ω(∂_t) = ω(∂_v), which are smooth across r_h. Expanding in spherical
harmonics ([[lem:iii-a1-1-6]]; the projections act in the angles and preserve both properties, with bounds), every
component inherits them.

We use repeatedly the following fact. *If −Φ_** + VΦ = σ²Φ on (r_h, ∞) with V real, V = O(r⁻²) with all derivatives
at infinity and V = O(f) near r_h, Φ = e^(−iσr_*)h with h smooth at r_h, and Φ = e^(iσr_*)k with k conormal and
O(r^N) at infinity for some N, then Φ = 0, provided V > 0.* Indeed the solutions at infinity are
e^(±iσr_*)(1 + O(r⁻¹)) (Volterra iteration, V ∈ L¹(dr_*) at infinity); the given form excludes e^(−iσr_*), which is
e^(iσr_*)e^(−2iσr_*), and e^(−2iσr_*) grows exponentially if Im σ > 0 and is not conormal if σ ∈ ℝ ∖ 0; so
Φ = c e^(iσr_*)(1 + O(r⁻¹)). If Im σ > 0, Φ and Φ_* decay exponentially at both ends (r_* → ∓∞), and pairing with Φ̄
gives ∫(|Φ_*|² + V|Φ|²)dr_* = σ²∫|Φ|²dr_*; if Φ ≠ 0 the left side is positive, forcing σ² > 0, so σ real: a
contradiction. If σ is real, the Wronskian Im(Φ̄Φ_*) is constant; at r_h, Φ_* = −iσΦ + e^(−iσr_*)fh′ gives
−σ|h(r_h)|², and at infinity σ|c|²; so c = 0 and Φ = 0.

*(a) The scalar step.* δω solves δd(δω) = δ□ω = 0 by [[prop:np-10-16]] (i). For each component r^(−3/2)ΦS of δω,
[[prop:np-10-16]] (ii) gives −Φ_** + V_0Φ = σ²Φ (multiply by f), and the class holds with the extra factor r^(3/2)
(polynomial growth); so Φ = 0, and δω = 0.

*(b) The Maxwell step.* Then δdω = □ω − dδω = 0. The vector type components r^(−1/2)ΦY of ω, Y ∈ 𝒱_l, have
δ_𝕊d_𝕊Y = (l + 1)²Y with (l + 1)² ≥ 4, so [[prop:np-10-16]] (iii) and the fact give Φ = 0. For the scalar type part
at l ≥ 1, W = r³F_tr solves R[W] = 0 by [[prop:np-10-16]] (iv) (as M = 0), so Φ := r^(−1/2)W solves the equation
with V_2 > 0; F_tr dt ∧ dr = F_vr dv ∧ dr is a component of dω, so Φ is in the class, and Φ = 0. Then F_tr = 0 and
M = 0 give a = b = 0 in the gauge of [[prop:np-10-16]] (iv), κ ≠ 0: that part of ω is a gradient. At l = 0,
M_r = −iσF_tr/f = 0 gives F_tr = 0, which is all of dω there. So dω = 0.

*(c) The gauge step.* By [[prop:np-10-16]] (v) and dω = 0, ω = (i/σ)dφ with φ := ω(T), which is in the scalar class.
δdφ = −iσδω = 0, so φ = 0 by (a), and ω = 0 on {r > r_h}.

*(d) Inside the horizon.* So u = 0 on {r > r_h}. The horizon is null, so a Cauchy argument does not apply, and we use
the mode equations. Expand u in harmonics ([[lem:iii-a1-1-6]]): □̂(σ) commutes with the rotations, so the coefficients
of each component of fixed type and degree l form a vector U(r) (at most three functions on (r_0, ∞)), smooth across
r_h, vanishing on (r_h, ∞), which solves a system −fU″ + AU′ + BU = 0 with A, B smooth on (0, ∞). Indeed, in the
ingoing chart (v, r, y), regular across r_h, in which t_* − v is a function of r, g^vv = 0, g^vr = 1, g^rr = f and
g^(ra) = 0; conjugation by e^(−iσt_*) turns ∂_v into −iσ and ∂_r into ∂_r − iσ∂_r t_*, so the only second
r-derivative of □̂(σ) is −f∂_r², and on a harmonic component the angular derivatives are algebraic. Put
Y := (U, (r − r_h)U′). Since (r − r_h)/f = r²/(r + r_h),

    (r − r_h)Y′ = MY,     M = ⎛ 0                          1                     ⎞ ,
                              ⎝ r²(r − r_h)(r + r_h)⁻¹B    1 + r²(r + r_h)⁻¹A    ⎠

with M smooth on (0, ∞). For r_0 < r_1 < r < r_h and m_1 := max_([r_1,r_h]) ‖M‖, wherever Y ≠ 0,
(d/dr) log|Y|² = 2Re⟨Y, MY⟩/((r − r_h)|Y|²) ≥ −2m_1/(r_h − r), so if Y(r_1) ≠ 0 then
|Y(r)| ≥ |Y(r_1)|((r_h − r)/(r_h − r_1))^(m_1) on [r_1, r_h) (the bound holds up to the first zero of Y after r_1, if
there is one, and by continuity keeps |Y| positive there, so there is none), which contradicts the vanishing of Y to
infinite order at r_h. So Y(r_1) = 0 for every r_1 ∈ (r_0, r_h), every component vanishes, and u = 0. ∎

**Proposition {#prop:iii-d-6-3}** ([Hin26, Proposition 6.9] in dimension 4 + 1.) Assume (Dyn). Let c_0 > 0. There are
ϵ > 0 and a neighbourhood ℬ″ of b_0 such that if |e_Υ|, |γ_Υ|, |γ_(Υ,H)| < ϵ and b ∈ ℬ″, then (□^Υ_b)^(σ) is
invertible for all σ with Im σ ≥ 0 and |σ| ≥ c_0.

*Proof.* Let 𝗉 := (b, e_Υ, γ_Υ, γ_(Υ,H)), a parameter in a compact set, with 𝗉_0 := (b_0, 0, 0, 0), at which the
operator is □. For |σ| ≥ C_0, [[prop:iii-d-6-1]] applies. The set K := {c_0 ≤ |σ| ≤ C_0, Im σ ≥ 0} is compact, and at
each σ ∈ K, □̂(σ) is invertible by [[prop:iii-d-6-2]]. By [[thm:i-a-8-1]] (invertibility is open in (σ, 𝗉), the
hypotheses holding uniformly by [[sec:iii-d-2]] and (Dyn)), each σ ∈ K has a neighbourhood U_σ and an ϵ_σ with
invertibility on U_σ × {|𝗉 − 𝗉_0| < ϵ_σ}; finitely many U_σ cover K. ∎

### tf-admissibility {#sec:iii-d-7}

The transition face of [[sec:i-c-4]] sees the operator only at infinity. For the unmodified Minkowski operator its
model is the conjugated Helmholtz operator, componentwise.

**Proposition {#prop:np-10-20}** (The transition face and the weights.) Let Δ_e := −Σ_(i=1)^4 ∂_(x^i)² on ℝ⁴.

(i) At γ_Υ = 0, □̄^Υ = □̄ acts componentwise in the Cartesian frame (dt̄, dx^i) on 4 + 1 Minkowski space, as the
scalar operator ∂_(t̄)² + Δ_e, and its spectral family (□̄)^(σ) = e^(iσt_*)□̄e^(−iσt_*), t_* = t̄ − r, satisfies
e^(iσr)(□̄)^(σ)e^(−iσr) = Δ_e − σ² on each component.

(ii) For l ∈ ℕ_0 the substitution u = r⁻¹w turns −u″ − (3/r)u′ + l(l + 2)r⁻²u − u = 0 into Bessel's equation
r²w″ + rw′ + (r² − (l + 1)²)w = 0 of order l + 1. The exponents of u at r = 0 are l and −(l + 2); in the variable
1/r they are −l and l + 2, the indicial roots of the scalar operator on degree l harmonics ([[lem:iii-a1-2-3]]), with
the gap (0, 2) at l = 0. As x → 0, x^(l+1)H^(1)_(l+1)(x) → −(i/π)Γ(l + 1)2^(l+1); as x → ∞,
e^(−ix)x^(1/2)H^(1)_(l+1)(x) → (2/π)^(1/2)e^(−i((l+1)π/2 + π/4)); and on the positive imaginary half-axis H^(1)_(l+1)
decays exponentially and H^(2)_(l+1) grows exponentially.

(iii) ρ^a lies in ρ^α L²(r³dr) near infinity if and only if a > α + 2: the shift between decay rates and b-weights
for the Euclidean density of ℝ⁴ is 2. On g_(b_0), with t the static time and t_* := t − r,
∂_σ²□̂(0) = 2P_2 = 2g^00 Id ([[lem:iii-d-2-1]] (1)), and 2g^00 W* = −4m_0ρ⁴dt + O(ρ⁵), with W* of [[eq:iii-d1-2-1]].

*Proof.* (i) The Christoffel symbols of ḡ vanish in Cartesian coordinates, so □̄ = −ḡ^(μν)∂_μ∂_ν = ∂_(t̄)² + Δ_e on
each component. On stationary functions, e^(iσt_*)□̄e^(−iσt_*) = e^(−iσr)(e^(iσt̄)□̄e^(−iσt̄))e^(iσr)
= e^(−iσr)(Δ_e − σ²)e^(iσr). (ii) With u = w/r, −u″ − 3u′/r = −w″/r − w′/r² + w/r³; adding l(l + 2)w/r³ − w/r and
multiplying by −r³ gives r²w″ + rw′ − (1 + l(l + 2))w + r²w = 0, and 1 + l(l + 2) = (l + 1)². Bessel's equation of
order l + 1 has exponents ±(l + 1) at 0, so u has exponents l and −l − 2. The limits are [DLMF, (10.7.7)] and
[DLMF, (10.17.5)], and the behaviour on the imaginary axis is [DLMF, (10.17.5)–(10.17.6)], which hold uniformly in the
sector |arg x| ≤ π − δ and in −2π + δ ≤ arg x ≤ π − δ respectively; these are the facts stated in [[lem:i-c-5-4]].
(iii) ∫^∞ ρ^(2(a−α))r³dr = ∫^∞ r^(3−2(a−α))dr is finite if and only if a − α > 2. By [[prop:np-10-18]] (iv),
g^00 = −2m_0ρ² + O(ρ⁴), and W* = ρ²dt + r_hρ³f⁻¹dr, so 2g^00W* = −4m_0ρ⁴dt + O(ρ⁵). ∎

**Lemma {#lem:iii-d-7-1}** (tf-admissibility; [Hin26, Lemma 6.8] in dimension 4 + 1.) There is ϵ > 0 such that for e_Υ ∈
[0, ϵ), |γ_Υ| < ϵ, every γ_(Υ,H) and every b ∈ ℬ, the family σ ↦ (□^Υ_b)^(σ) is tf-admissible ([[def:i-c-5-1]]) with
every weight in the indicial gap (0, ι^Υ_(s1,2)) of [[lem:iii-d-4-1]] (with (0, 2) when e_Υγ_Υ² = 0).

*Proof.* The transition face operator N_tf(e^(iθ)) of [[sec:i-c-4]] is built from the data of the operator at ρ = 0
only: S_0, the normal operator N(P⁽⁰⁾) and H_0. By [[lem:iii-d-2-1]] (3) these are the model's, independent of b and
of the horizon modification; so it suffices to consider □̄^Υ. *At γ_Υ = 0.* The model is □̄, which in the Cartesian
frame has S_0 = 0, N(P⁽⁰⁾) = (−(ρ∂_ρ)² + 2ρ∂_ρ + Δ_𝕊) Id ([[lem:iii-d-2-1]] (3), [[prop:np-10-20]] (i)) and, with the
standard inner product, H_0 = Id: by [[prop:i-c-5-3]] it is tf-admissible with every weight in (0, 2). *Small γ_Υ.*
Fix the weight β = 1, which lies in the gap for all small parameters ([[lem:iii-d-4-1]]), q = 2 − β, and orders s, α_+,
𝗋_± as in [[thm:i-c-4-3]], admissible with margins at γ_Υ = 0; as S̄ = O(γ_Υ) ([[lem:iii-d-3-1]]) and the thresholds
of [[eq:i-a-1-5]] move continuously, they remain admissible for small parameters. The perturbation

    N^γ_tf − N^0_tf = −2ie^(iθ)ρ̂S̄ + γ_Υ ρ̂²M_E(ρ̂∂_ρ̂, ∂_x̂)

([Hin26, (6.18a)] with [[lem:iii-d-3-1]]) is bounded from the space H_(sc,b)^(s,(𝗋+α_+,q)) of 𝒳_(tf,θ) into that of
𝒴_(tf,θ) with norm O(|γ_Υ|), uniformly in θ: near the end ρ̂ → 0, ρ̂ · (order 0) gains one order of decay and
ρ̂² Diff_b¹ = ρ̂ Diff_sc¹ gains one order of decay for one sc-derivative; near ρ̂ → ∞ the weights q and q − 2 allow the
factors ρ̂ and ρ̂². So 𝒳_(tf,θ) is the same space for all small γ_Υ, and by [[cor:i-c-5-2]] (b) at γ_Υ = 0, uniformly
over the three sectors, ‖w‖ ≤ C‖N^0_tf w‖ ≤ C‖N^γ_tf w‖ + C′|γ_Υ|‖w‖; for C′|γ_Υ| ≤ ½ this gives injectivity of
N^γ_tf(e^(iθ)) for all θ ∈ [0, π], and the adjoint estimate [[eq:i-c-5-2]] gives that of N^γ_tf(1)^(*h) in the same
way. So the family of □̄^Υ is tf-admissible with weight 1, and by [[cor:i-c-5-2]] (c) with every weight in the gap.
The condition e_Υ ≥ 0 makes z ≥ 0, so that [[lem:iii-d-4-1]] describes the gap. ∎

### The zero energy setting {#sec:iii-d1-1}

The rest of the chapter concerns σ = 0 and its neighbourhood: [Hin26, Section 6.4 and Lemma 6.13] (pp. 119–125) in
dimension 4 + 1 here and in [[sec:iii-d1-2]]–[[sec:iii-d1-5]], and [Hin26, Section 6.5] in [[sec:iii-d2-1]] and after.
The kernel of the unmodified operator at zero energy is proved on Tangherlini from the mode equations of
[[prop:np-10-16]], and its cokernel from a distributional identity at the horizon, with the index from [[ch:s03]]. The
first step of the proof of mode stability ([[prop:iii-d1-4-1]]) is a Grushin problem with a fixed compactly supported
augmentation, to which [[thm:i-c-6-4]] and [[thm:i-c-7-1]] apply as proved; its Schur complement is computed from two
pairings alone, so the augmented estimate [Hin26, (6.27)] with a joint parameter, and the decay of
∂_σ□̂(0)ω_(0) that it needs [Hin26, footnote 69], are not used. The second step is carried out at every frequency at
once, around a base point at which invertibility is already known.

ℬ, g_b, t_*, ρ, E_Υ and □^Υ_b are as in [[sec:iii-d-1]], with c_(Υ,H) := −½χ(r)dr, χ ∈ C_c^∞, χ = 1 near r_h and
supp χ ∩ U_Γ = ∅. Write 𝗉 := (b, e_Υ, γ_Υ, γ_(Υ,H)), P̂_𝗉(σ) := (□^Υ_b)^(σ), 𝗉_0 := (b_0, 0, 0, 0) and
P̂ := P̂_(𝗉_0), the spectral family of □ = □_(g_(b_0)) = dδ + δd. On g_(b_0), in the ingoing chart,
g = −f dv² + 2dv dr + r²g_𝕊 and |dg| = r³|dv dr dg_𝕊|, and t_* − v is a smooth function of r near r_h
([[eq:iii-b-3-6]]).

*The spaces.* For σ ≠ 0, Im σ ≥ 0: 𝒳_σ, 𝒴_σ of [[eq:i-c-6-4]] (those of [[thm:i-a-7-2]] with the orders of
[[thm:i-b-1-3]] (3)); at σ = 0: 𝒳_0, 𝒴_0 of [[eq:i-c-3-1]], with the Euclidean density, so that the b-weight of
H̄_b^(s,α) is α + 2 ([[sec:i-c-1-2]]). By [[sec:iii-d-2]]–[[sec:iii-d-5]], [[sec:iii-d-7]] and (Dyn), every P̂_𝗉, 𝗉 in
a compact neighbourhood 𝒦 of 𝗉_0 with e_Υ ≥ 0, satisfies (H1)–(H5) with ϑ_ℋ = 1 ([[lem:iii-d-5-1]]), (G) for every α
with α + 2 ∈ (0, 2) ([[lem:iii-d-4-1]]: (0, 2) lies in the gap (0, ι^Υ_(s1,2)), which is (0, 2) when
e_Υγ_Υ² = 0), and (TF) ([[lem:iii-d-7-1]]), and has index 0 at σ ≠ 0 ([[thm:i-b-1-3]] (3) at high frequencies, as in
[[prop:iii-d-6-1]], and the constancy of the index, [[thm:i-a-7-2]] (3), at bounded ones). We fix such an α and a
constant s > 5/2; by [[thm:i-c-3-1]] (3)–(4) and [[thm:i-a-7-2]] (3), kernels, annihilators of ranges and
invertibility do not depend on these choices.

*The horizon functional.* Let ω* := d(H(r − r_h)) = δ(r − r_h)dr, H the Heaviside function, a stationary
distributional 1-form supported on the horizon sphere, and

    ℓ(v) := ∫_X g⁻¹(v, ω*) |dg_X| = r_h³ ∫_(𝕊³) v(∂_(t_*))|_(r=r_h) dx̂,                                 {#eq:iii-d1-1-1}

where |dg| = |dt_*| ⊗ |dg_X|, so |dg_X| = r³|dr dx̂| near r_h, and g⁻¹(v, dr) = v(∇r) = v(∂_v + f∂_r) equals
v(∂_(t_*)) at r_h. ℓ is continuous on H^(s′) near the horizon sphere for s′ > ½ (the trace theorem), so on 𝒴_0 and
𝒴_σ, as s − 1 > ½. It is [Hin26]'s pairing with ω*_(0).

*The modified divergence at the horizon.* With the trace weight 2/3, E_H h := 2ι_(c♯_(Υ,H))h − (2/3)c_(Υ,H) tr_g h
([Hin26, (6.22)] with the weight 2/3), and since tr_g G_g h = −(3/2)tr_g h in dimension 5 ([[lem:iii-b-6-2]]),

    E_H G_g = 2ι_(c♯_(Υ,H)),                                                                             {#eq:iii-d1-1-2}

as [Hin26]'s E_(H⁺,1)G = 2ι_(c♯) in dimension 4 with the weight 1. The horizon part of □^Υ_b is
2γ_(Υ,H)E_H G δ*.

### Kernel and cokernel at zero energy {#sec:iii-d1-2}

Let

    W* := r⁻²dt + r_h r⁻³f⁻¹dr = r⁻²dv − dr/(r(r + r_h)).                                                {#eq:iii-d1-2-1}

The two forms agree, as dt = dv − f⁻¹dr and f = (r − r_h)(r + r_h)/r². The second shows that W* is smooth on
{r > 0} in the ingoing chart, so on X̄ up to ∂_♯X; near infinity dt = dt_* + (f⁻¹ + O(r⁻²))dr with all derivatives
([[eq:iii-b-3-6]]), so W* ∈ 𝒜²(X̄; E), and W* ∈ H̄_b^(s,α) for α + 2 < 2. dW* = 2r⁻³dt ∧ dr, and δW* = 0:
δ(a(r)dt) = 0 for the static metric, and δ(b(r)dr) = −r⁻³(r³fb)′ vanishes for b = r_h r⁻³f⁻¹. δdW* = 0, because
r³F^(rt) is constant for F = 2r⁻³dt ∧ dr (F^(rt) = g^rr g^tt F_rt, g^rr g^tt = −1). So □W* = 0 on {r > r_h}, and on
{r > 0}, since the components of □W* in the ingoing chart are real-analytic in r. By [[prop:np-10-15]] (iii), W* is
the only l = 0 element of the kernel that is smooth at the future horizon and decays.

**Lemma {#lem:iii-d1-2-1}** (Kernel and cokernel; [Hin26, Lemma 6.10] in dimension 4 + 1.) Assume (Dyn) at b_0.
(1) For every stationary u that is smooth near the horizon sphere, ℓ(P̂(0)u) = 0. (2) ker_(𝒳_0) P̂(0) = span{W*}.
(3) The annihilator of the range of P̂(0): 𝒳_0 → 𝒴_0 is spanned by ℓ.

*Proof.* (1) *Symmetry.* For stationary smooth 1-forms u, w with w compactly supported in X°,
B(u, w) := ∫_X g⁻¹(u, w̄)|dg_X| satisfies B(□u, w) = B(u, □w). Indeed, let θ_1 ∈ C_c^∞(ℝ) with ∫θ_1 = 1 and
W := θ_1(t_*)w. As □ = −∇^μ∇_μ, two integrations by parts against the compactly supported W give
∫g⁻¹(□u, W̄)|dg| = ∫g⁻¹(u, □W̄)|dg|. The left side is B(□u, w). On the right,
□(θ_1w) = θ_1□w + (□_0θ_1)w − 2∇_(∇θ_1)w with □_0 = −∇^μ∇_μ on functions, and ∇θ_1 = θ_1′∇t_*,
□_0θ_1 = −θ_1″g⁻¹(dt_*, dt_*) + θ_1′□_0t_*; the coefficients of θ_1′ and θ_1″ are stationary, and
∫θ_1′ = ∫θ_1″ = 0, so the right side is B(u, □w). By continuity the identity extends to w a stationary distribution
with compact support in X° (u smooth). *The identity.* Since □ = dδ + δd and δ² = 0, □d = dδd = d□_0 on functions,
as operators on distributions. In the ingoing chart H(r − r_h) is a v-independent distribution, and

    □_0 H(r − r_h) = −r⁻³∂_μ(r³g^(μr)δ(r − r_h)) = −r⁻³∂_r(r³f δ(r − r_h)) = 0,

as ∂_v annihilates it, g^(ar) = 0, and r³fδ(r − r_h) = r_h³f(r_h)δ(r − r_h) = 0. So □ω* = d□_0H(r − r_h) = 0, and
ℓ(□u) = B(□u, ω*) = B(u, □ω*) = 0; on stationary u, □u = P̂(0)u. Only u near the horizon sphere enters.

(2) W* ∈ 𝒳_0 and P̂(0)W* = 0, by the above. Conversely let u ∈ 𝒳_0 with P̂(0)u = 0. By [[thm:i-c-3-1]] (2), with the
gap (0, 2), u is smooth up to ∂_♯X, hence across the horizon, and u ∈ 𝒜^β near ∂X for every β < 2; fix β ∈ (1, 2).
Let ω := u, a stationary 1-form, and work first on {r > r_h} in the static chart, expanding in harmonics
([[lem:iii-a1-1-6]]; the projections act in the angles and preserve smoothness at r_h in the ingoing chart and the
conormal bounds at infinity). Three facts are used. The *scalar identity*: for a stationary function φ,
δdφ = −r⁻³(r³fφ′)′ + r⁻²Δ_𝕊φ, so a degree l component φ_l of a solution of δdφ = 0 solves (r³fφ_l′)′ = κrφ_l. The
*energy fact*: if −Φ_** + VΦ = 0 on (r_h, ∞), Φ_* = fΦ′, with V > 0 continuous, Φ of class C¹ in r up to r_h, and
Φ_*Φ̄ → 0 as r → ∞, then Φ = 0: integrating Φ̄ times the equation over r_* ∈ [r_*(r_1), r_*(R)] gives
∫(|Φ_*|² + V|Φ|²)dr_* = [Φ_*Φ̄], whose endpoint terms tend to 0 as r_1 → r_h (Φ_* = fΦ′ → 0) and R → ∞. The *mode
equations* [[prop:np-10-16]] (iii)–(iv), which hold for every σ and are used at σ = 0.

*(a) The divergence.* φ := δω is a smooth stationary function in 𝒜^(β+1) near infinity, and
δdφ = δ(□ω − δdω) = 0. Multiplying (r³fφ_l′)′ = κrφ_l by φ̄_l and integrating over [r_1, R]:
[r³fφ_l′φ̄_l]_(r_1)^R = ∫_(r_1)^R (r³f|φ_l′|² + κr|φ_l|²)dr. As r_1 → r_h the bracket tends to 0 (f → 0, φ_l smooth
in r there); as R → ∞ it is O(R^(3−(β+2)−(β+1))) = O(R^(−2β)). So φ_l′ = 0 and κφ_l = 0; at l = 0, φ_0 is a decaying
constant. So δω = 0.

*(b) The field.* F := dω ∈ 𝒜^(β+1) and δF = □ω − dδω = 0. *Vector type.* A component r^(−1/2)Φ(r)Y of ω, Y ∈ 𝒱_l,
l ≥ 1, has δ_𝕊d_𝕊Y = ΛY with Λ = (l + 1)² ≥ 4; by [[prop:np-10-16]] (iii) at σ = 0, −Φ_** + V_1Φ = 0 with V_1 > 0.
Φ is smooth in r at r_h (angular components are the same in the static and the ingoing chart), and since |Y| is r⁻¹
in the Euclidean metric, Φ = O(r^(3/2−β)) and Φ_* = O(r^(1/2−β)), so Φ_*Φ̄ = O(r^(2−2β)) → 0. The energy fact gives
Φ = 0. *Scalar type, l ≥ 1.* In the notation of [[prop:np-10-16]] (iv), W := r³F_tr solves R[W] = (r²M_t)′ = 0
(M = δdω = 0), so Φ := r^(−1/2)W solves −Φ_** + V_2Φ = 0 with V_2 > 0 (κ ≥ 3, m_0/r² < 1). F_tr = F_vr is smooth at
r_h, and Φ = r^(5/2)F_tr = O(r^(3/2−β)), Φ_* = O(r^(1/2−β)); so Φ = 0, F_tr = 0, and with M = 0,
[[prop:np-10-16]] (iv) gives a = b = 0, where (a, b) is the gauge-invariant pair of [[prop:np-10-16]] (iv), defined
after subtracting d(cS); so this part of ω is d(cS) for a function c(r). *Scalar type, l = 0.* κ = 0 and
R[W] = (fW′/r)′ = 0, so fW′/r is constant; it vanishes at r_h, as W is smooth there; so W = q, a constant,
F_tr = qr⁻³, and the l = 0 part a(r)dt + b(r)dr of ω has −a′ = F_tr. Altogether dω = qr⁻³dt ∧ dr = (q/2)dW*.

*(c) The gauge.* ω′ := ω − (q/2)W* is smooth across r_h, in 𝒜^β near infinity, closed on {r > r_h}, and has
δω′ = 0. With T = ∂_t, Cartan's formula and stationarity give d(ω′(T)) = ℒ_Tω′ − ι_Tdω′ = 0, so ω′(T) is a
constant; it decays, so it is 0. {r > r_h} is simply connected, so ω′ = dφ with ∂_tφ = ω′(T) = 0; in the ingoing
chart ω′ has no dv component and its dr component ∂_rφ is smooth at r_h, so φ is smooth in (r, x̂) up to r_h.
dφ ∈ 𝒜^β gives a constant φ_∞ with φ − φ_∞ = O(r^(1−β)), and δdφ = 0. At l = 0, r³fφ_0′ is constant and vanishes at
r_h, so φ_0 is constant. At l ≥ 1, the equation (r³fφ_l′)′ = κrφ_l has at r = ∞ a regular singular point (in
ρ = 1/r: ρ²fφ_ρρ + ρ(ρf_ρ − f)φ_ρ − κφ = 0, f = 1 − m_0ρ²) with indicial equation ν² − 2ν − κ = 0, roots ν = l + 2
and ν = −l for φ ∼ ρ^ν; by Frobenius' theorem every solution is c_1ρ^(l+2)a_1(ρ) + c_2(ρ^(−l)b_1(ρ)
+ c_3 log ρ ρ^(l+2)a_1(ρ)) with a_1, b_1 analytic and a_1(0) = b_1(0) = 1, and φ_l = O(ρ^(β−1)) forces c_2 = 0. So
φ_l = O(r^(−l−2)), φ_l′ = O(r^(−l−3)), and the energy identity of (a) gives φ_l = 0. So ω′ = 0 on {r > r_h}.

*(d) Inside the horizon.* u − (q/2)W* lies in ker P̂(0), is smooth on X̄ and vanishes on {r > r_h}; part (d) of the
proof of [[prop:iii-d-6-2]], which uses only these properties (at σ = 0), shows that it vanishes on {r_0 < r < r_h}.
So u = (q/2)W*.

(3) By (1) and density, ℓ(P̂(0)u) = 0 for u ∈ 𝒳_0: near the horizon sphere u ∈ H^s, smooth u_j → u in H^s there give
P̂(0)u_j → P̂(0)u in H^(s−2), and ℓ is continuous on H^(s−2) as s > 5/2. ℓ ≠ 0 on 𝒴_0 (for instance
ℓ(ζ_1(r)dt_*) = 2π²r_h³ for ζ_1 ∈ C_c^∞ with ζ_1(r_h) = 1). By [[cor:i-c-6-6]], whose hypotheses hold by
[[sec:iii-d1-1]], P̂(0): 𝒳_0 → 𝒴_0 has index 0, so by (2) the annihilator of its range ([[thm:i-c-3-1]] (1)) is
one-dimensional, and it is spanned by ℓ. ∎

### The pairings at the horizon {#sec:iii-d1-3}

**Lemma {#lem:iii-d1-3-1}** (The pairings; [Hin26, Lemma 6.11] in dimension 4 + 1.) (1) ℓ([□, t_*]W*) = 4π².
(2) With c_(Υ,H) = −½χ dr as in [[sec:iii-d1-1]], ℓ(2E_H G δ*W*) = 4π². ([Hin26]'s values are 4π and a number in
(3π, 5π). In dimension 4 + 1 both are (n − 2)|𝕊^(n−1)| = 2 · 2π², and in dimension 3 + 1 the first is 1 · 4π.)

*Proof.* We compute in the ingoing chart at r = r_h, where ℓ(v) = r_h³∫_(𝕊³) v_v dx̂ by [[eq:iii-d1-1-1]],
v_v := v(∂_v), and W*_v = r⁻², W*_r = −(r(r + r_h))⁻¹; the Christoffel symbols are [[eq:s13-chris]].

(1) t_* − v = F(r) near r_h, and ℓ([□, F]W*) = ℓ(□(FW*)) − ℓ(F□W*) = 0 by [[lem:iii-d1-2-1]] (1) and □W* = 0; so t_*
may be replaced by v. For a function φ, □(φw) = φ□w + (□_0φ)w − 2∇_(∇φ)w, so [□, v]W* = (□_0v)W* − 2∇_(∇v)W*, with
∇v = g^vr∂_r = ∂_r and □_0v = −r⁻³∂_r(r³g^rv) = −3/r. Further (∇_(∂_r)W*)_v = ∂_rW*_v − Γ^r_rv W*_r
= −2r⁻³ − f′/(2r(r + r_h)), which at r_h is −5/(2r_h³). So ([□, v]W*)_v(r_h) = −3/r_h³ + 5/r_h³ = 2/r_h³, and
ℓ = 2|𝕊³| = 4π².

(2) By [[eq:iii-d1-1-2]], 2E_H G δ*W* = 4ι_(c♯)δ*W* with c := c_(Υ,H), and at r_h, c♯ = −½∇r = −½(∂_v + f∂_r)
= −½∂_v. So (4ι_(c♯)δ*W*)_v = −2(δ*W*)_vv, and (δ*W*)_vv = ∇_vW*_v = −Γ^v_vv W*_v − Γ^r_vv W*_r = −1/r_h³ at r_h. So
ℓ = r_h³ · (2/r_h³) · 2π² = 4π². ∎

The two lemmas so far carry the zero energy data that the argument below uses. We collect them, with the remaining
facts about the unmodified operator at zero energy.

**Proposition {#prop:np-10-15}** (The zero energy data of the unmodified operator.) On 4 + 1 Minkowski space and on
g_(b_0):

(i) The indicial roots of (□^Υ_b)^(0) are the zeros of ι(ι − 3)(ι² − ι − 2 − z) (type s0),
(l + 3 − ι)(l + ι − 1)Q_l(ι² − ι) (type sl) and (ι + l)(l + 2 − ι) (type vl), z = 4e_Υγ_Υ², with Q_l as in the proof
of [[lem:iii-d-4-1]]. At γ_Υ = 0 the gap is (0, 2); for 0 < z ≤ ½, 2 < ι^Υ_(s1,2) < ι^Υ_(s0,2) and every root other
than ι^Υ_(s1,2) is ≤ 0 or ≥ ι^Υ_(s0,2), so (0, ι^Υ_(s1,2)) is an indicial gap.

(ii) For stationary 1-forms on {r > r_h} the dt part and the spatial part of □ decouple. A S dt, S ∈ 𝒮_l, satisfies
□(AS dt) = 0 if and only if (f/r)(r³A′)′ = κA. For l ≥ 1, ω = B(r)S dr + C(r)d_𝕊S satisfies □ω = 0 if and only if

    −(r³f²B′)′ + rf(κ + 3f)B − 2κfC = 0,     −κ(rfC′)′ − 2κfB + κ²r⁻¹C = 0,

the Euler–Lagrange equations of ∫(r³f²B′² + κrfC′² + Z(B, C))dr, with Z the quadratic form of the matrix
((rf(κ + 3f), −2κf), (−2κf, κ²/r)), whose determinant κ²f(κ − 1 + m_0/r²) is positive for r > r_h. For Y ∈ 𝒱_l,
V(r)Y satisfies □(VY) = 0 if and only if −(rfV′)′ + (l + 1)²r⁻¹V = 0.

(iii) At l = 0 the stationary solutions of □ω = 0 on {r > r_h} are A(r)dt + B(r)dr with A = a_0 + a_2r⁻² and
B = b_3r⁻³f⁻¹ + b_1rf⁻¹, constants a_0, a_2, b_1, b_3. Those that are smooth at the future horizon and decay at
infinity form span{W*}.

(iv) ℓ(P̂(0)u) = 0 for every stationary u smooth near the horizon sphere.

(v) ℓ([□, t_*]W*) = 4π², and δW* = 0. At r_h, ι_(∇r)δ*W* = −r_h⁻³(dv + (3/2)dr), and for c_H = c_v dv + c_r dr at r_h,
ℓ(2E_H G δ*W*) = −12π²c_v − 8π²c_r; so c_H = −½χ dr gives 4π², and for the inhomogeneity
𝔣(σ̂, γ̂) := −iσ̂[□, t_*]W* + 2γ̂E_H G δ*W*, ℓ(𝔣(σ̂, γ̂)) = 4π²(−iσ̂ + γ̂), which is nonzero for Im σ̂ ≥ 0, γ̂ ≥ 0, not
both zero.

(vi) With t the static time and t_* := t − r_*, in the static frame, ∂_σP̂(0)W* = −i[□, t_*]W* = ir⁻³dt + O(r⁻⁴). The
leading term is of order ρ³ because (ρ∂_ρ − 3/2)ρ² = ½ρ², where in dimension 3 + 1 the corresponding (ρ∂_ρ − 1)ρ
vanishes.

*Proof.* (i) is [[eq:s13-dets]] and [[lem:iii-d-4-1]]. (iv) is [[lem:iii-d1-2-1]] (1).

(ii) The static metric is invariant under the reflection t ↦ −t, which maps dt to −dt and fixes dr and the angular
covectors; □ commutes with it, and a stationary 1-form is odd under it exactly when it is a multiple of dt. So □ maps
the dt part to the dt part and the spatial part to the spatial part. *The dt part.* δ(AS dt) = 0, and F := d(AS dt)
has F_rt = A′S, F_at = A∂_aS; as in the proof of [[prop:np-10-16]] (iv), (δF)^t = r⁻³(r³A′)′S − κA(fr²)⁻¹S and the
other components vanish, so □(AS dt) = −f(δF)^t dt = (−fr⁻³(r³A′)′ + κr⁻²A)S dt. *The scalar spatial part.*
δω = φS with φ := −r⁻³(r³fB)′ + κr⁻²C, so dδω = φ′S dr + φ d_𝕊S; and dω = (C′ − B)dr ∧ d_𝕊S, whose divergence is,
as in the proof of [[prop:np-10-16]] (iii)–(iv), δdω = −κr⁻²(C′ − B)S dr − r⁻¹(rf(C′ − B))′d_𝕊S. So □ω = E_B S dr
+ E_C d_𝕊S with E_B := φ′ + κr⁻²(B − C′) and E_C := φ − r⁻¹(rf(C′ − B))′. In r³fE_B the C′ terms cancel, and
r³fE_B = −r³f(r⁻³(r³fB)′)′ + κrfB − 2κfC. Expanding with r⁻³(r³fB)′ = (fB)′ + 3fB/r and f²B′ = f(fB)′ − ff′B,

    −r³f(r⁻³(r³fB)′)′ + (r³f²B′)′ = (r³f′² + 3rf² − (r³ff′)′)B = 3rf²B,

since r³f′² = 4m_0²r⁻³ = (r³ff′)′ for f = 1 − m_0r⁻². So r³fE_B = −(r³f²B′)′ + rf(κ + 3f)B − 2κfC. Likewise
r⁻²(r³fB)′ = 2fB + (rfB)′ gives κrE_C = −κ(rfC′)′ + κ²r⁻¹C − 2κfB. The determinant is
κ²(f(κ + 3f) − 4f²) = κ²f(κ − f) = κ²f(κ − 1 + m_0r⁻²), positive as f > 0 and κ ≥ 3. *The vector part.* By the proof
of [[prop:np-10-16]] (iii) at σ = 0, δ(VY) = 0 and δd(VY) = (−r⁻¹(rfV′)′ + (l + 1)²r⁻²V)Y.

(iii) At l = 0 the dt equation is (r³A′)′ = 0, so A = a_0 + a_2r⁻². The dr equation is φ′ = 0, so (r³fB)′ = c r³ for
a constant c, and r³fB = cr⁴/4 + b_3; this is the stated B with b_1 = c/4. In the ingoing chart
A dt + B dr = A dv + (B − A/f)dr, and B − A/f = (b_3r⁻³ + b_1r − a_0 − a_2r⁻²)/f. Decay at infinity forces
a_0 = b_1 = 0, and smoothness at r_h forces the numerator to vanish at r_h, that is b_3 = a_2r_h. So
A dt + B dr = a_2W*.

(v) The first value is [[lem:iii-d1-3-1]] (1), and δW* = 0 is shown before [[lem:iii-d1-2-1]]. At r_h, ∇r = ∂_v, and
with [[eq:s13-chris]], (δ*W*)_vv = −r_h⁻³ (proof of [[lem:iii-d1-3-1]]). Further ∇_rW*_v = −5/(2r_h³) at r_h (proof of
[[lem:iii-d1-3-1]]) and ∇_vW*_r = −Γ^r_vr W*_r − Γ^v_vr W*_v = (f′/2)W*_r = −1/(2r_h³), so (δ*W*)_rv = ½(∇_rW*_v +
∇_vW*_r) = −3/(2r_h³), and ι_(∇r)δ*W* = (δ*W*)_(v·) = −r_h⁻³(dv + (3/2)dr). By [[eq:iii-d1-1-2]] and c_H♯ = c_v∂_r +
c_r∂_v at r_h, (2E_H G δ*W*)_v = 4(c_v(δ*W*)_rv + c_r(δ*W*)_vv) = −(6c_v + 4c_r)r_h⁻³, and ℓ multiplies by 2π²r_h³. The
value of ℓ(𝔣) then follows from (1) and the case c_v = 0, c_r = −½; and |−iσ̂ + γ̂|² = |σ̂|² + 2γ̂ Im σ̂ + γ̂² > 0.

(vi) In the static chart the nonzero Christoffel symbols with indices in {t, r} are Γ^t_tr = f′/(2f), Γ^r_tt = ff′/2
and Γ^r_rr = −f′/(2f), and W* has no angular component. ∇t_* = −f⁻¹∂_t − ∂_r and □_0t_* = −r⁻³∂_r(r³f · (−f⁻¹)) = 3/r.
With f′ = 2m_0r⁻³: (∇_tW*)_t = −Γ^r_tt W*_r = O(r⁻⁶), (∇_tW*)_r = −Γ^t_tr W*_t = O(r⁻⁵),
(∇_rW*)_t = −2r⁻³ − Γ^t_rt W*_t = −2r⁻³ + O(r⁻⁵), and (∇_rW*)_r = O(r⁻⁴). So
[□, t_*]W* = (3/r)W* + 2f⁻¹∇_tW* + 2∇_rW* has dt component 3r⁻³ − 4r⁻³ + O(r⁻⁵) and dr component O(r⁻⁴).
T = ∂_σP̂(0) = −i[□, t_*] because e^(iσt_*)□e^(−iσt_*) = □ − iσ[□, t_*] + O(σ²). For the last sentence, by
[[eq:iii-d-2-1]] at S̄ = 0 the ∂_(t_*) coefficient of □ near infinity is −2ρ(ρ∂_ρ − 3/2) up to ρ³ Diff_b¹, applied to
the leading part ρ²dt of W*. ∎

### Mode stability on the closed upper half plane {#sec:iii-d1-4}

**Proposition {#prop:iii-d1-4-1}** ([Hin26, Proposition 6.12] in dimension 4 + 1.) Assume (Dyn). There is ϵ_0 > 0
such that for every γ_(Υ,H) ∈ (0, ϵ_0] there are ϵ_1 > 0 and a neighbourhood ℬ(γ_(Υ,H)) of b_0 such that, for
b ∈ ℬ(γ_(Υ,H)), e_Υ ∈ [0, ϵ_1] and |γ_Υ| < ϵ_1, (□^Υ_b)^(σ) is invertible for every σ with Im σ ≥ 0: as a map
𝒳_σ → 𝒴_σ when σ ≠ 0, and when σ = 0 as a map 𝒳_0 → 𝒴_0 for every s > 3/2 and every α with
α + 2 ∈ (0, ι^Υ_(s1,2)). In particular (□^Υ_b)^(0) has trivial kernel on 𝒜^ϵ(X̄; E) for every ϵ > 0.

*Proof. Step 1: the horizon modification alone, at b_0.* For γ ∈ [0, 1] let 𝗉_γ := (b_0, 0, 0, γ) and
P̂_γ := P̂_(𝗉_γ), so

    P̂_γ(σ) = P̂(σ) + 2γE_H G (δ*)^(σ),     (δ*)^(σ) = δ* + σδ*_1,     δ*_1w := −i dt_* ⊗_s w,

and P̂(σ) = P̂(0) + σT + σ²P_2 ([[sec:i-a-1]]) with T = ∂_σP̂(0) = −i[□, t_*] (as
e^(iσt_*)□e^(−iσt_*) = □ − iσ[□, t_*] + O(σ²)) and P_2 of order 0. Fix ψ, ϕ ∈ C_c^∞(X°; E) with ℓ(ψ) ≠ 0
([[lem:iii-d1-2-1]] (3)) and ⟨W*, ϕ⟩_h = 1, and let 𝒫_γ(σ) be the augmented operator of [[eq:i-c-6-5]] with
m_1 = m_2 = 1,

    𝒫_γ(σ)(u, c) := (P̂_γ(σ)u + cψ, ⟨u, ϕ⟩_h).

*(Z_𝒫) at γ = 0.* 𝒫_0(0): 𝒳_0 ⊕ ℂ → 𝒴_0 ⊕ ℂ is invertible. If P̂(0)u + cψ = 0 and ⟨u, ϕ⟩_h = 0, applying ℓ gives
cℓ(ψ) = 0 ([[lem:iii-d1-2-1]] (3)), so c = 0, u = kW* ([[lem:iii-d1-2-1]] (2)) and k = ⟨u, ϕ⟩_h = 0. Given (f_1, e_1),
c := ℓ(f_1)/ℓ(ψ) makes f_1 − cψ annihilated by ℓ, so f_1 − cψ = P̂(0)u_0 (the range is closed and its annihilator is
spanned by ℓ), and u := u_0 + (e_1 − ⟨u_0, ϕ⟩_h)W* solves 𝒫_0(0)(u, c) = (f_1, e_1).

*Uniform low-energy theory.* The family γ ↦ P̂_γ, γ ∈ [0, 1], satisfies (H1)–(H5), (G) and (TF)
([[sec:iii-d1-1]]; the horizon term is compactly supported in X°, so the normal operators at ∂X and at tf do not
depend on γ). By [[thm:i-c-7-1]] at γ = 0 and [[thm:i-c-6-4]], there are γ_1 ∈ (0, 1], c_0 > 0 and C such that for
γ ∈ [0, γ_1]: 𝒫_γ(σ) is invertible for |σ| ≤ c_0, Im σ ≥ 0 (σ = 0 by [[thm:i-c-7-1]] (1), σ ≠ 0 by
[[thm:i-c-6-4]] (3)); ‖(u, c)‖ ≤ C‖𝒫_γ(0)(u, c)‖ on 𝒳_0 ⊕ ℂ (proof of [[thm:i-c-7-1]]); and the estimate
[[eq:i-c-6-6]] of [[thm:i-c-6-4]] (1) with k = 0 holds with the constant C for 0 < |σ| ≤ c_0. Let

    (u_(σ,γ), c_(σ,γ)) := 𝒫_γ(σ)⁻¹(0, 1).

*The Schur complement.* If c_(σ,γ) ≠ 0, then P̂_γ(σ) is invertible (on 𝒳_σ → 𝒴_σ, or 𝒳_0 → 𝒴_0 at σ = 0). Write
(u, c) := (u_(σ,γ), c_(σ,γ)), so P̂_γ(σ)u = −cψ and ⟨u, ϕ⟩_h = 1. If P̂_γ(σ)w = 0, then
𝒫_γ(σ)(w, 0) = ⟨w, ϕ⟩_h(0, 1), so (w, 0) = ⟨w, ϕ⟩_h(u, c), whence ⟨w, ϕ⟩_h c = 0, ⟨w, ϕ⟩_h = 0 and w = 0. Given
f_1, let (w, d) := 𝒫_γ(σ)⁻¹(f_1, 0); then P̂_γ(σ)(w − (d/c)u) = f_1 − dψ + dψ = f_1.

*The expansion.* By [[lem:iii-d1-2-1]] (1) and density, ℓ(P̂(0)v) = 0 for every v that is H^s near the horizon
sphere (s > 5/2), so applying ℓ to P̂_γ(σ)u + cψ = 0 gives, with u = u_(σ,γ),

    c_(σ,γ) ℓ(ψ) = −σℓ(Tu) − σ²ℓ(P_2u) − 2γℓ(E_H G δ*u) − 2γσℓ(E_H G δ*_1u).                             {#eq:iii-d1-4-1}

*Claim:* as (σ, γ) → (0, 0) with |σ| ≤ c_0, Im σ ≥ 0 and γ ∈ [0, γ_1], c_(σ,γ) → 0 and u_(σ,γ) → W* in H^(s′)(K)
for every compact K ⊂ X° and s′ < s. Let (σ_j, γ_j) → (0, 0), and (u_j, c_j) the corresponding pairs; |c_j| ≤ C. Let
φ_1 ∈ C^∞([0, ∞)) vanish on [0, 1] and equal 1 on [2, ∞), and put w_j := φ_1(ρ/ς_j)u_j, ς_j := |σ_j| (and w_j := u_j
if σ_j = 0). By [[lem:i-c-6-2]] (b) and (a) (with q = 0, l = α), w_j, supported in {ρ ≥ ς_j}, has
‖w_j‖_(H̄_b^(s,α)) ≤ C′‖u_j‖_(s,(𝗋+α_+,α,0),ς_j) ≤ C′C, uniformly in j. Pass to a subsequence with w_j ⇀ w weakly
in H̄_b^(s,α) and c_j → c. As w_j = u_j on {ρ > 2ς_j}, on each compact K′ ⊂ X° the u_j equal the w_j for large j and
are bounded in H^s(K′); so u_j → w in distributions on X̄ ∖ ∂X, and by Rellich's theorem u_j → w in H^(s′)(K). The
coefficients of P̂_γ(σ) depend polynomially on (σ, γ), so P̂(0)w + cψ = 0, whence w ∈ 𝒳_0, and
⟨w, ϕ⟩_h = lim⟨u_j, ϕ⟩_h = 1. So 𝒫_0(0)(w, c) = (0, 1), and (w, c) = (W*, 0). The limit does not depend on the
subsequence, which proves the claim.

Since ℓ involves only the values at the horizon sphere of Tu and E_H G δ*u, first-order operators, the claim with
s′ ∈ (3/2, s) gives ℓ(Tu_(σ,γ)) → ℓ(TW*) = −iℓ([□, t_*]W*) = −4π²i and
2ℓ(E_H G δ*u_(σ,γ)) → 2ℓ(E_H G δ*W*) = 4π² ([[lem:iii-d1-3-1]]), while ℓ(P_2u) and ℓ(E_H G δ*_1u) stay bounded. So
[[eq:iii-d1-4-1]] reads

    c_(σ,γ) ℓ(ψ) = −4π²(−iσ + γ) + o(|σ| + γ).

For Im σ ≥ 0 and γ ≥ 0, |−iσ + γ|² = |σ|² + 2γ Im σ + γ² ≥ ½(|σ| + γ)². So there are c_1 ∈ (0, c_0] and
γ_2 ∈ (0, γ_1] with c_(σ,γ) ≠ 0 whenever |σ| ≤ c_1, γ ∈ [0, γ_2], Im σ ≥ 0 and (σ, γ) ≠ (0, 0). By the Schur
complement, *for γ ∈ (0, γ_2], P̂_γ(σ) is invertible for all |σ| ≤ c_1 with Im σ ≥ 0, σ = 0 included*; c_1 does not
depend on γ.

*Step 2: the whole family, at every frequency.* Let ϵ and ℬ″ be those of [[prop:iii-d-6-3]] for its c_0 := c_1, and
ϵ_0 := min(γ_2, ½ϵ). Fix γ ∈ (0, ϵ_0]. At 𝗉_γ, P̂_γ(σ) is invertible for every σ with Im σ ≥ 0: for |σ| ≤ c_1 by
Step 1, for |σ| ≥ c_1 by [[prop:iii-d-6-3]] (γ < ϵ, b_0 ∈ ℬ″). Now vary 𝗉 = (b, e_Υ, γ_Υ, γ) near 𝗉_γ, with
e_Υ ≥ 0. (i) *Low energies.* (Z) holds at 𝗉_γ, so by [[thm:i-c-7-1]] (with m_1 = m_2 = 0 and base point 𝗉_γ) and
[[thm:i-c-6-4]] (3) there are c_0(γ) > 0 and a neighbourhood N_1 of 𝗉_γ on which P̂_𝗉(0) is invertible and P̂_𝗉(σ) is
invertible for 0 < |σ| ≤ c_0(γ). (ii) *High energies.* By [[prop:iii-d-6-1]] there is C_0 with invertibility for
|σ| ≥ C_0 and all 𝗉 in 𝒦. (iii) *The compact middle.* On {c_0(γ) ≤ |σ| ≤ C_0, Im σ ≥ 0}, a compact set, P̂_(𝗉_γ)(σ)
is invertible at each point, and invertibility is open in (σ, 𝗉) ([[thm:i-a-8-1]], as in the proof of
[[prop:iii-d-6-3]]); finitely many neighbourhoods cover it, giving N_2. On N_1 ∩ N_2 ∩ 𝒦, which contains
ℬ(γ) × [0, ϵ_1] × (−ϵ_1, ϵ_1) × {γ} for some neighbourhood ℬ(γ) and some ϵ_1 > 0, invertibility holds for every σ. At
σ = 0 it holds for one pair (s, α), hence for all s > 3/2 and all α with α + 2 in the gap (0, ι^Υ_(s1,2))
([[thm:i-c-3-1]] (4)); for σ ≠ 0 the kernel and the annihilator of the range do not depend on the admissible orders
([[thm:i-a-7-2]] (3)).

*The kernel on 𝒜^ϵ.* 𝒜^ϵ(X̄; E) ⊂ H̄_b^(s,α) when α + 2 < ϵ: its elements are smooth up to ∂_♯X, and near ∂X they and
their b-derivatives are O(ρ^ϵ), which lies in ρ^(α+2)L²(μ_b) = H̄_b^(0,α) ([[sec:i-c-1-2]]); and
α + 2 ∈ (0, min(ϵ, ι^Υ_(s1,2))) is allowed. A kernel element there lies in 𝒳_0 and vanishes. ∎

*Remarks.* (a) [Hin26, Proposition 6.12] states triviality of the nullspace on 𝒜^α for every α also when σ ≠ 0.
That needs 𝒜^α ⊂ 𝒳_σ for suitable admissible orders, which [[thm:i-a-7-2]] (5) gives only for the weight
3/2 + S̄ − ϵ; it is not used here. (b) The neighbourhood ℬ(γ_(Υ,H)) of b_0 depends on γ_(Υ,H), as ϵ_1 does in
[Hin26]. The later chapters fix γ_(Υ,H) once and then work near b_0.

### The zero energy operator {#sec:iii-d1-5}

**Lemma {#lem:iii-d1-5-1}** ([Hin26, Lemma 6.13] in dimension 4 + 1.) Assume (Dyn), and let E_Υ and b be as in
[[prop:iii-d1-4-1]]. Use an unweighted b-density near ∂X to define L², so that H̄_b^(s,α) here is the space
H̄_b^(s,α−2) of [[ch:s03]]. (1) For s > 3/2 and α ∈ (0, ι^Υ_(s1,2)),
(□^Υ_b)^(0): {u ∈ H̄_b^(s,α) : (□^Υ_b)^(0)u ∈ H̄_b^(s−1,α+2)} → H̄_b^(s−1,α+2) is invertible. (2) If
f_1 ∈ 𝒜^(2+ℰ)(X̄; E) for an index set ℰ with min Re ℰ > 0, then (□^Υ_b)^(0)⁻¹f_1 ∈ 𝒜^(ℰ′)(X̄; E) for an index set
ℰ′ with min Re ℰ′ > 0.

*Proof.* (1) With α′ := α − 2, the map is 𝒳_0 → 𝒴_0 of [[eq:i-c-3-1]] with the weight α′, α′ + 2 = α in the gap;
this is [[prop:iii-d1-4-1]] at σ = 0. The threshold is 3/2 for every γ_(Υ,H) ([[lem:iii-d-5-1]]).

(2) Fix α ∈ (0, min(min Re ℰ, ι^Υ_(s1,2))). Then f_1 ∈ H̄_b^(s−1,α+2) for every s (in b-densities
ρ^(2+z) ∈ H_b^(∞,α+2) near ∂X when Re z > α, and f_1 is smooth up to ∂_♯X). Let u_s be the inverse image given by
(1) for the regularity s. For s′ > s, u_(s′) lies in the domain for s and solves the same equation, so
u_(s′) = u_s =: u, and u ∈ ⋂_s H̄_b^(s,α): smooth up to ∂_♯X, and of class H_b^(∞,α) near ∂X. Near ∂X,
(□^Υ_b)^(0) = ρ²A with A := P⁽⁰⁾ an elliptic b-operator on the trivial bundle ([[eq:i-c-1-1]]–[[eq:i-c-1-3]]), and
χ_1Au = χ_1ρ⁻²f_1 ∈ 𝒜^ℰ ⊂ H_b^(∞,(ℰ,β)) for every β, χ_1 a cut-off near ∂X. [[lem:iii-a-1-4]] then gives
χ̃_1u ∈ H_b^(∞,(ℰ_β,β)) for every β ∉ Re spec_b(A), where the index set built there from E(α) (the boundary spectrum
with Re ι > α), ℰ and their shifts by ℕ_0 does not depend on β; call it ℰ′. So u ∈ 𝒜^(ℰ′), and
min Re ℰ′ ≥ min(α, min Re ℰ) > 0. [[lem:iii-a-1-4]] is stated for scalar operators; its proof uses A only through the
meromorphy of N(A, ι)⁻¹ with bounds on vertical strips, which hold for the matrix-valued indicial family
[[eq:i-c-1-3]] by [[lem:i-c-2-4]]; so it applies verbatim on E. The same holds for [[lem:iii-a-1-5]]. ∎

### Zero energy states from the symmetries of Minkowski space {#sec:iii-d2-1}

This section and the next two prove [Hin26, Sections 6.5.1–6.5.2] (pp. 125–134) in dimension 4 + 1: the comparison of
the operators of g_b with those of Minkowski space and of g_m, and the stationary and generalised zero energy states
of □^Υ_b. The mass of g_b enters at |x|⁻² and the rotation at |x|⁻³ ([[eq:iii-b-3-5]]), so every comparison of
[Hin26, Lemma 6.14] gains one power of ρ, and so do the corrections and the symmetric gradients built from it. The
correction to the boost then sits at ρ¹, which is no indicial root, so [Hin26, (6.31)]'s logarithm and the formal
solution lemma it needs do not occur; the corrections to the translations and rotations sit at ρ², which is an s1 root
when e_Υγ_Υ² = 0, so here the modification at infinity is used with e_Υ > 0 and γ_Υ ≠ 0.

*Setting.* ℬ, g_b (b = (m, A), A ∈ 𝔰𝔬(4)), t_*, ρ, the trivialisation by dt_*, dx¹, …, dx⁴ and the bundle E are as in
[[sec:iii-d-1]], and g_m := g_((m,0)). The model is ḡ = −dt̄² + dx², t̄ = t_* + |x|, with δ̄*, □̄^Υ as in
[[sec:iii-d-2]]. Fix γ_(Υ,H) ∈ (0, ϵ_0] and then b ∈ ℬ(γ_(Υ,H)), e_Υ ∈ (0, ϵ_1] and 0 < |γ_Υ| < ϵ_1 as in
[[prop:iii-d1-4-1]], so that

    z := 4e_Υγ_Υ² ∈ (0, ½],                                                                              {#eq:iii-d2-1-1}

and write □^Υ_b := □^Υ_(g_b,E_Υ). We take c_Υ and c_(Υ,H) invariant under the rotations of x
(c_Υ = ζ_∞(|x|)|x|⁻¹dt with ζ_∞ = 1 for large |x|, and c_(Υ,H) = −½χ(|x|)d|x|), which [[def:iii-b-6-1]] and
[[sec:iii-d1-1]] allow. By [[prop:iii-d1-4-1]] and [[lem:iii-d1-5-1]], (□^Υ_b)^(0) is invertible on the b-spaces with
an unweighted b-density, for every s > 3/2 and every weight in the gap (0, ι^Υ_(s1,2)), and maps 𝒜^(2+ℰ),
min Re ℰ > 0, into polyhomogeneous spaces. *All b-spaces from here on use an unweighted b-density near ∂X*, as
[Hin26, Section 6.5] does.

*Indicial roots.* By [[lem:iii-d-4-1]] the indicial roots of (□^Υ_b)^(0) do not depend on b or on the horizon
modification, and for 0 < z ≤ ½: at s0 they are 0, 3, ι^Υ_(s0,2) ∈ (2, 3) and 1 − ι^Υ_(s0,2); at s1 they are 0, 4,
ι^Υ_(s1,2) ∈ (2, ι^Υ_(s0,2)), a root in (3, 4), and their mirror images 1 − ι; at sl, l ≥ 2, and vl, l ≥ 1, every
root is ≤ 0 or ≥ 3. In particular *neither 1 nor 2 is an indicial root, of any type*: the integer roots are 0, 3,
1 − l, l + 3, −l and l + 2, none of which is 1 or 2 for l ≥ 1, and by [[eq:iii-d-4-2]] the others lie strictly
between consecutive integers for 0 < z ≤ ½. Fix ϵ_ind > 0 less than d(Re ι, ℤ) for every indicial root ι with
Re ι ∉ ℤ and |Re ι| ≤ 10. ℰ_ind denotes an index set with min Re ℰ_ind ≥ ϵ_ind, which may change from line to line,
and (k, 0) the index set {(k + j, 0) : j ∈ ℕ_0}.

*The model symmetries* ([Hin26, (6.29)] in dimension 4 + 1). For S ∈ 𝒮_1, so |x|S = ξ · x for some ξ ∈ ℝ⁴, and
V ∈ 𝒱_1, so V = Σ_(i<j) c_ij(x^i dx^j − x^j dx^i) with c ∈ 𝔰𝔬(4) (the Euclidean duals of the rotation fields;
[[def:iii-a1-1-7]]),

    ω̄^(0)_s0 := ḡ(∂_(t_*), ·) = −dt̄,   ω̄^(0)_s1(S) := d(|x|S),   ω̆̄^((0),1)_s1(S) := |x|d(|x|S) − |x|S dt̄,
    ω̄^(−1)_v1(V) := V.                                                                                  {#eq:iii-d2-1-2}

ω̄_s1(S) = ξ · dx is dual to a translation, B̄(S) := t_*ω̄_s1(S) + ω̆̄¹_s1(S) = t̄ d(ξ · x) − (ξ · x)dt̄ to a Lorentz
boost, and V to the rotation field R_V := ḡ⁻¹V = Σ c_ij(x^i∂_j − x^j∂_i) (the same vector field in the coordinates
(t̄, x) and (t_*, x), as R_V|x| = 0). All four are Killing 1-forms of ḡ, so δ̄* annihilates them and
□̄^Υ = 2δ̄_Ē Ḡδ̄* does too. Their components are smooth on X̄, of orders ρ⁰, ρ⁰, ρ⁻¹ and ρ⁻¹.

### Comparison of operators {#sec:iii-d2-2}

**Lemma {#lem:iii-d2-2-1}** ([Hin26, Lemma 6.14] in dimension 4 + 1.) For b = (m, A) ∈ ℬ, near ∂X and on stationary
sections,

    (δ*_(g_b))^(0) ∈ ρ Diff_b¹,  (δ*_(g_b))^(0) − (δ̄*)^(0) ∈ ρ³ Diff_b⁰,  (δ*_(g_b))^(0) − (δ*_(g_m))^(0) ∈ ρ⁴ Diff_b⁰,
                                                                                                         {#eq:iii-d2-2-1}
    (□^Υ_b)^(0) ∈ ρ² Diff_b²,   (□^Υ_b)^(0) − (□̄^Υ)^(0) ∈ ρ⁴ Diff_b²,   (□^Υ_b)^(0) − (□^Υ_(g_m,E_Υ))^(0) ∈ ρ⁵ Diff_b²,
                                                                                                         {#eq:iii-d2-2-2}

and [□^Υ_b, t_*] ∈ ρ Diff_b¹, [□^Υ_b − □^Υ_(g_m,E_Υ), t_*] ∈ ρ⁴ Diff_b¹ on stationary sections. ([Hin26] has ρ², ρ³
in the first line and ρ³, ρ⁴ in the second.)

*Proof.* Near ∂X the components of g_b, g_b⁻¹, ḡ and ḡ⁻¹ in the coordinates (t_*, x) are smooth functions on X̄
(functions of (ρ, x̂)), and

    g_b − ḡ ∈ ρ²C^∞,     g_b − g_m ∈ ρ³C^∞,                                                              {#eq:iii-d2-2-3}

and the same for the inverses. Indeed [[eq:iii-b-3-5]] gives g_b − g_m ∈ |x|⁻³C^∞ and g_m − η ∈ |x|⁻²C^∞,
η = −dt² + dx² in the time t of [[eq:iii-b-3-6]], with the duals; by [[eq:iii-b-3-6]], t̄ = t + C′ − 8m_0|x|⁻¹ near
infinity, so ḡ − η = −16m_0|x|⁻²dt d|x| − 64m_0²|x|⁻⁴d|x|² ∈ |x|⁻²C^∞; and the frame change
dt = dt_* + (1 − 8m_0|x|⁻²)d|x| has coefficients smooth on X̄, so it preserves ρ^kC^∞. The Cartesian derivatives
∂_(x^i) lie in ρ Diff_b¹, and ∂_(t_*) annihilates stationary sections. Hence Γ(g) ∈ ρC^∞ for g = g_b, ḡ, and
g_1 − g_2 ∈ ρ^kC^∞ (with the inverses) implies Γ(g_1) − Γ(g_2) ∈ ρ^(k+1)C^∞. On stationary 1-forms
δ*_gω = ½(∂_μω_ν + ∂_νω_μ) − Γ^λ_μν ω_λ, whose first part does not depend on g: this gives [[eq:iii-d2-2-1]] with
k = 2, 3. For [[eq:iii-d2-2-2]]: δ_g = −g^(μν)∇_μ lies in ρ Diff_b¹ with δ_(g_1) − δ_(g_2) ∈ ρ^(k+1) Diff_b¹;
G_(g_1) − G_(g_2) ∈ ρ^k Diff_b⁰; and near ∂X, E^Υ_g h = −γ_Υ(2ι_(g⁻¹c_Υ)h − (2/3)(1 − e_Υ)c_Υ tr_g h) with
c_Υ ∈ ρC^∞ ([[def:iii-b-6-1]]; the horizon term is supported in {|x| < 5R_1}), so E^Υ_g ∈ ρ Diff_b⁰ and
E^Υ_(g_1) − E^Υ_(g_2) ∈ ρ^(k+1) Diff_b⁰; the model's Ē uses c̄ = |x|⁻¹dt̄, which differs from c_Υ by ρ³C^∞. Expanding
2(δ_1 + E_1)G_1δ*_1 − 2(δ_2 + E_2)G_2δ*_2 into terms each containing one difference gives ρ^(k+2) Diff_b², and
(□^Υ_b)^(0) ∈ ρ² Diff_b² in the same way. For the commutators: on stationary sections [□^Υ_g, t_*] is the first-order
operator obtained from the terms of □^Υ_g with one ∂_(t_*) (those with ∂_(t_*)² give 2∂_(t_*), which vanishes on
stationary sections); these are −2g^(t_*ν)∂_ν plus connection and E terms, so the same counting applies, with
g^(t_*ν) ∈ C^∞ and its differences in ρ^kC^∞; and [[lem:iii-d-2-1]] (2)–(3) gives
[□^Υ_b, t_*] = −2ρ(ρ∂_ρ − 3/2 − S̄) + Q_b ∈ ρ Diff_b¹. ∎

**Lemma {#lem:iii-d2-2-2}** (Smooth dependence on b.) Let α ∈ (0, ι^Υ_(s1,2)) and let b ↦ f_b be of class C^k from
ℬ(γ_(Υ,H)) into H̄_b^(s−1,α+2) for every s. Then b ↦ u_b := (□^Υ_b)^(0)⁻¹f_b is of class C^k into H̄_b^(s,α) for
every s, and its derivatives are the inverse images ∂_b u_b = (□^Υ_b)^(0)⁻¹(∂_b f_b − (∂_b(□^Υ_b)^(0))u_b) and their
iterates.

*Proof.* Write P_b := (□^Υ_b)^(0). As in the proof of [[lem:iii-d1-5-1]] (2), u_b ∈ ⋂_s H̄_b^(s,α). The coefficients
of P_b depend smoothly on b in C^∞ ([[prop:iii-b-3-6]]), so P_(b′) − P_b maps H̄_b^(s+1,α) to H̄_b^(s−1,α+2) with norm
O(|b′ − b|); and ‖P_(b′)⁻¹‖ from H̄_b^(s−1,α+2) to H̄_b^(s,α) is bounded for b′ near b, by [[thm:i-c-7-1]] (2) (the
estimate without error term, uniform near a point where (Z) holds). So
u_(b′) − u_b = P_(b′)⁻¹((f_(b′) − f_b) − (P_(b′) − P_b)u_b) → 0 in H̄_b^(s,α); that is, b ↦ P_b⁻¹w is continuous for
every fixed w ∈ ⋂_s H̄_b^(s−1,α+2), uniformly on bounded sets of each H̄_b^(s−1,α+2). With u̇ := P_b⁻¹(ḟ − Ṗu_b),

    (u_(b+h) − u_b)/h − u̇ = P_(b+h)⁻¹((f_(b+h) − f_b)/h − ((P_(b+h) − P_b)/h)u_b) − P_b⁻¹(ḟ − Ṗu_b) → 0,

since the bracket converges in every H̄_b^(s−1,α+2) and P_(b+h)⁻¹ → P_b⁻¹ strongly there. Induction gives C^k. ∎

### The states {#sec:iii-d2-3}

**Proposition {#prop:iii-d2-3-1}** ([Hin26, Proposition 6.15] in dimension 4 + 1.) Assume (Dyn), and let E_Υ and b be
as in [[sec:iii-d2-1]]. There are stationary 1-forms, linear in S ∈ 𝒮_1 and V ∈ 𝒱_1 and smooth in b,

    ω^(0)_(b,s0) := g_b(∂_(t_*), ·),   ω^(0)_(b,s1)(S),   ω̆^((0),1)_(b,s1)(S),   ω^(−1)_(b,v1)(V),      {#eq:iii-d2-3-1}

smooth on X, with components in ρ⁻¹C^∞(X̄) at most ([Hin26, footnote 72]), with

    ω^(0)_(b,s0) − ω̄^(0)_s0 ∈ ρ²C^∞,                ω^(0)_(b,s1)(S) − ω̄^(0)_s1(S) ∈ 𝒜^((2,0)∪(2+ℰ_ind)),
    ω̆^((0),1)_(b,s1)(S) − ω̆̄^((0),1)_s1(S) ∈ 𝒜^((1,0)∪(1+ℰ_ind)),   ω^(−1)_(b,v1)(V) − V ∈ 𝒜^((2,0)∪(2+ℰ_ind)),
                                                                                                         {#eq:iii-d2-3-2}

such that

    □^Υ_b ω^(0)_(b,s0) = 0,   □^Υ_b ω^(0)_(b,s1)(S) = 0,   □^Υ_b(t_*ω^(0)_(b,s1)(S) + ω̆^((0),1)_(b,s1)(S)) = 0,
    □^Υ_b ω^(−1)_(b,v1)(V) = 0.                                                                          {#eq:iii-d2-3-3}

(1) (*No logarithm.*) In place of [Hin26, (6.31)]: the correction to the boost has no logarithmic term;
c_(b,s1) = 0.

(2) (*Symmetric gradients.*) δ*_(g_b)ω^(0)_(b,s0) = 0, and

    h_(b,s1)(S) := δ*_(g_b)ω^(0)_(b,s1)(S) ∈ 𝒜^((3,0)∪(3+ℰ_ind)),
    δ*_(g_b)(t_*ω^(0)_(b,s1)(S) + ω̆^((0),1)_(b,s1)(S)) =: t_*h_(b,s1)(S) + h̆¹_(b,s1)(S),
    h̆¹_(b,s1)(S) ∈ 𝒜^((2,0)∪(2+ℰ_ind)),     h_(b,v1)(V) := δ*_(g_b)ω^(−1)_(b,v1)(V) ∈ 𝒜^((3,0)∪(3+ℰ_ind));
                                                                                                         {#eq:iii-d2-3-4}

the ρ² leading term of h̆¹_(b,s1)(S) is of scalar type 1, given by the same S; and h_(b,s1)(S),
t_*h_(b,s1)(S) + h̆¹_(b,s1)(S) and h_(b,v1)(V) lie in the kernels of D_(g_b)Ric and of δ_(g_b,E_Υ)G_(g_b).

(3) (*Killing rotations*, [Hin26, Remark 6.17].) If R_V is a Killing field of g_b, then
ω^(−1)_(b,v1)(V) = g_b(R_V, ·) and h_(b,v1)(V) = 0. At b = (m, 0) this holds for every V ∈ 𝒱_1: six independent
rotations, where Kerr has three.

*Proof.* Throughout, P_b := (□^Υ_b)^(0), and we use two facts. (F1) *If f_1 ∈ 𝒜^(2+ℱ) is smooth on X̄, ℱ an index set
with min Re ℱ = k ∈ {1, 2} and (k, 0) its only element with real part below k + ϵ_ind, then
P_b⁻¹f_1 ∈ 𝒜^((k,0)∪(k+ℰ_ind)).* Indeed, by [[lem:iii-d1-5-1]], u := P_b⁻¹f_1 ∈ ⋂_s H̄_b^(s,α) for every α < k in the
gap (as k ≤ 2 < ι^Υ_(s1,2)), and [[lem:iii-a-1-4]] with A = ρ⁻²P_b near ∂X ([[eq:i-c-1-1]]) and
α ∈ (k − ϵ_ind, k) gives u ∈ 𝒜^ℰ with ℰ generated by ℱ and the boundary spectrum above α; the latter has no point with
real part in (k − ϵ_ind, k + ϵ_ind) (no root at 1 or 2), so the only element of ℰ there is ℱ's (k, 0), without
logarithm. (F2) *For a Killing 1-form K of g_b, δ*_(g_b)K = 0, hence □^Υ_bK = 0; and for any stationary 1-form ω,
h := δ*_(g_b)ω satisfies D_(g_b)Ric(h) = ½ℒ_(ω♯)Ric(g_b) = 0 and δ_(g_b,E_Υ)G_(g_b)h = ½□^Υ_bω; the same holds for
t_*ω + ω̆.*

*Time translation.* ∂_(t_*) is Killing for g_b, so (F2) gives □^Υ_bω_(b,s0) = 0 and δ*ω_(b,s0) = 0; and
ω_(b,s0) − ω̄_s0 = (g_b − ḡ)(∂_(t_*), ·) ∈ ρ²C^∞ by [[eq:iii-d2-2-3]].

*Translations.* δ̄*ω̄_s1 = 0, so by [[eq:iii-d2-2-1]]
δ*_(g_b)ω̄_s1 = ((δ*_(g_b))^(0) − (δ̄*)^(0))ω̄_s1 ∈ ρ³C^∞, and f_b := □^Υ_bω̄_s1 = 2δ_(g_b,E_Υ)G_(g_b)δ*_(g_b)ω̄_s1
is smooth on X̄ and in ρ⁴C^∞ near ∂X (δ_(g_b) + E^Υ_(g_b,∞) ∈ ρ Diff_b¹ there), that is in 𝒜^(2+(2,0)). By (F1) with
k = 2, ω′_b := −P_b⁻¹f_b ∈ 𝒜^((2,0)∪(2+ℰ_ind)), and ω_(b,s1) := ω̄_s1 + ω′_b solves
□^Υ_bω_(b,s1) = f_b + P_bω′_b = 0. Then h_(b,s1) = (δ*_(g_b))^(0)ω′_b + ((δ*_(g_b))^(0) − (δ̄*)^(0))ω̄_s1 lies in
ρ Diff_b¹ 𝒜^((2,0)∪(2+ℰ_ind)) + ρ³C^∞ ⊂ 𝒜^((3,0)∪(3+ℰ_ind)). f_b depends smoothly on b in ρ⁴C^∞, so
[[lem:iii-d2-2-2]] gives smoothness in b.

*Boosts.* B̄ = t_*ω̄_s1 + ω̆̄¹_s1 is Killing for ḡ, so □̄^ΥB̄ = 0, and □̄^Υω̄_s1 = 0. Hence

    f̆_b := □^Υ_b(t_*ω_(b,s1) + ω̆̄¹_s1) = [□^Υ_b − □̄^Υ, t_*]ω̄_s1 + ((□^Υ_b)^(0) − (□̄^Υ)^(0))ω̆̄¹_s1
            + [□^Υ_b, t_*]ω′_b,                                                                          {#eq:iii-d2-3-5}

as the terms with a factor t_*, t_*(□^Υ_b − □̄^Υ)ω̄_s1 = t_*f_b and t_*□^Υ_bω′_b = −t_*f_b, cancel. By
[[lem:iii-d-2-1]] (3), near ∂X, □^Υ_b − □̄^Υ = −g_b^00∂_(t_*)² + Q_b∂_(t_*) + R_b with Q_b ∈ ρ³ Diff_b¹ and
R_b = (□^Υ_b)^(0) − (□̄^Υ)^(0) ∈ ρ⁴ Diff_b² (also [[eq:iii-d2-2-2]]); on stationary sections
[□^Υ_b − □̄^Υ, t_*] = Q_b. So the first term of [[eq:iii-d2-3-5]] is Q_bω̄_s1 ∈ ρ³C^∞, the second
R_bω̆̄¹_s1 ∈ ρ⁴ Diff_b²(ρ⁻¹C^∞) ⊂ ρ³C^∞, and the third, by [[lem:iii-d2-2-1]], in
ρ Diff_b¹ 𝒜^((2,0)∪(2+ℰ_ind)) ⊂ 𝒜^((3,0)∪(3+ℰ_ind)). So f̆_b ∈ 𝒜^(2+((1,0)∪(1+ℰ_ind))), smooth on X̄, and by (F1) with
k = 1, ω̆′_b := −P_b⁻¹f̆_b ∈ 𝒜^((1,0)∪(1+ℰ_ind)). Put ω̆_(b,s1) := ω̆̄¹_s1 + ω̆′_b; then
□^Υ_b(t_*ω_(b,s1) + ω̆_(b,s1)) = f̆_b + P_bω̆′_b = 0. No logarithm arises, since 1 is not an indicial root; this is
(1). Smoothness in b: f̆_b is smooth in b ([[lem:iii-d2-2-2]] for ω′_b), and [[lem:iii-d2-2-2]] again.

For (2): [δ*_g, t_*] = dt_* ⊗_s (·) for every metric, and δ̄*B̄ = 0 gives dt_* ⊗_s ω̄_s1 + (δ̄*)^(0)ω̆̄¹_s1 = 0. So

    h̆¹_(b,s1) = dt_* ⊗_s ω′_b + ((δ*_(g_b))^(0) − (δ̄*)^(0))ω̆̄¹_s1 + (δ*_(g_b))^(0)ω̆′_b
              ∈ 𝒜^((2,0)∪(2+ℰ_ind)) + ρ³ Diff_b⁰(ρ⁻¹C^∞) + ρ Diff_b¹ 𝒜^((1,0)∪(1+ℰ_ind)) ⊂ 𝒜^((2,0)∪(2+ℰ_ind)).

*Its leading term.* At b_S := (m, 0) the metric g_m, t_* and E_Υ are invariant under the rotations of x
([[sec:iii-d2-1]]); the construction is linear and, by the uniqueness of the inverse images, equivariant, so
S ↦ h̆¹_(b_S,s1)(S) is an SO(4)-equivariant linear map from 𝒮_1, the representation ℝ⁴. The decomposition of
[[lem:iii-a1-1-6]] is into SO(4)-invariant subspaces, and among the types only scalar type 1 contains ℝ⁴ (at each l
the scalar, vector and tensor types are, for SO(4), the representations of highest weights (l/2, l/2),
((l ± 1)/2, (l ∓ 1)/2) and ((l ± 2)/2, (l ∓ 2)/2), and ℝ⁴ is (½, ½)); so h̆¹_(b_S,s1)(S) is of scalar type 1, given
by S. For general b, by [[eq:iii-d2-2-2]], f_b − f_(b_S) = (P_b − P_(b_S))ω̄_s1 ∈ ρ⁵C^∞, so
ω′_b − ω′_(b_S) = −P_b⁻¹((f_b − f_(b_S)) + (P_b − P_(b_S))ω′_(b_S)), whose argument lies in
ρ^(2+3)C^∞ + 𝒜^(2+(5,0)∪(5+ℰ_ind)), lies in H̄_b^(∞,α) for some α > 2 ([[lem:iii-d1-5-1]], any
α ∈ (2, ι^Υ_(s1,2))). Then, term by term in [[eq:iii-d2-3-5]],
f̆_b − f̆_(b_S) ∈ ρ⁴C^∞ + H̄_b^(∞,α+1) + 𝒜^((6,0)∪(6+ℰ_ind)) by [[lem:iii-d2-2-1]] (the commutator bound and
R_b − R_(b_S) ∈ ρ⁵ Diff_b²), and ω̆′_b − ω̆′_(b_S) = −P_b⁻¹((f̆_b − f̆_(b_S)) + (P_b − P_(b_S))ω̆′_(b_S)) lies in
H̄_b^(∞,α″) for every α″ < 2 ([[lem:iii-d1-5-1]]), so that (δ*_(g_b))^(0) of it is O(ρ^(α″+1)), α″ ∈ (1, 2). So, in
the formula for h̆¹, the differences dt_* ⊗_s (ω′_b − ω′_(b_S)),
((δ*_(g_b))^(0) − (δ*_(g_m))^(0))ω̆̄¹_s1 ∈ ρ³C^∞, (δ*_(g_b))^(0)(ω̆′_b − ω̆′_(b_S)) and
((δ*_(g_b))^(0) − (δ*_(g_m))^(0))ω̆′_(b_S) ∈ ρ⁵C^∞ are all O(ρ^(2+ϵ)) for some ϵ > 0, and h̆¹_b and h̆¹_(b_S) have the
same ρ² term.

*Rotations.* g_m(R_V, ·) = V, since g_m = η + m|x|⁻²(dt − d|x|)² ([[eq:iii-b-3-4]]) and R_V t = R_V|x| = 0; and R_V is
Killing for the spherically symmetric g_m, so δ*_(g_m)V = 0. By [[eq:iii-d2-2-1]],
δ*_(g_b)V = ((δ*_(g_b))^(0) − (δ*_(g_m))^(0))V ∈ ρ⁴ Diff_b⁰(ρ⁻¹C^∞) ⊂ ρ³C^∞ near ∂X, smooth on X̄, so
f_b := □^Υ_bV ∈ 𝒜^(2+(2,0)), and (F1) gives ω′_b := −P_b⁻¹f_b ∈ 𝒜^((2,0)∪(2+ℰ_ind)), smooth in b by
[[lem:iii-d2-2-2]]. ω_(b,v1)(V) := V + ω′_b solves [[eq:iii-d2-3-3]], and
h_(b,v1)(V) = δ*_(g_b)V + (δ*_(g_b))^(0)ω′_b ∈ ρ³C^∞ + 𝒜^((3,0)∪(3+ℰ_ind)).

The kernel statements in (2) are (F2).

(3) If R_V is Killing for g_b, K := g_b(R_V, ·) has □^Υ_bK = 0 by (F2), and
K − V = (g_b − ḡ)(R_V, ·) ∈ ρ²C^∞ · ρ⁻¹ ⊂ ρC^∞ by [[eq:iii-d2-2-3]]. So ω_(b,v1)(V) − K ∈ 𝒜^((1,0)∪(1+ℰ_ind)) is in
the kernel of P_b on H̄_b^(s,α) for α ∈ (0, 1), which is trivial ([[lem:iii-d1-5-1]] (1)); so ω_(b,v1)(V) = K and
h_(b,v1)(V) = δ*K = 0. At b = (m, 0), K = V for every V by the above, and 𝒱_1 ≅ 𝔰𝔬(4) has dimension 6. ∎

*Remarks.* (a) *The decay rates* ([Hin26, Remark 6.16]). h_(b,s1) gains three powers over ω_(b,s1), not one, because
g_b is translation-invariant to two orders (g_b − ḡ ∈ ρ²C^∞); h_(b,v1) gains four powers over ω_(b,v1) because g_b is
spherically symmetric to three orders (g_b − g_m ∈ ρ³C^∞). (b) Which R_V are Killing for g_b depends on the rotation
A; at A = 0 all are, and (3) is used there.

The following proposition collects the facts about the symmetries, and about the linearised Myers–Perry metrics at
zero rotation, that this section and [[ch:s15]] use.

**Proposition {#prop:np-10-28}** (Symmetries and linearised metrics on Tangherlini.) Let g = g_m.

(i) In Cartesian coordinates g − ḡ ∈ ρ²C^∞ and Γ(g) ∈ ρ³C^∞; hence (δ*_g)^(0) − (δ̄*)^(0) ∈ ρ³ Diff_b⁰ and
(□^Υ_g)^(0) − (□̄^Υ)^(0) ∈ ρ⁴ Diff_b². The tortoise coordinate satisfies r_* − r → 0, with no logarithm.

(ii) δ*_g dx¹ ∈ ρ³C^∞ and □dx¹ = 2δGδ*dx¹ ∈ ρ⁴C^∞. The number 2 is an s1 root of (□^Υ_b)^(0) at z = 0 and not for
z > 0, where the s1 root near 2 is ι^Υ_(s1,2) = ½(1 + (17 + 2z − 2(z² + 4z + 16)^(1/2))^(1/2)) > 2.

(iii) For the boost B̄ = t̄ dx¹ − x¹dt̄, which is Killing for ḡ, δ*_gB̄ − t_*δ*_g dx¹ is stationary and lies in
ρ²C^∞, and the stationary residual □^Υ_gB̄ − t_*□^Υ_g dx¹ lies in ρ³C^∞. The number 1 is not an s1 root for z ≥ 0:
the s1 determinant at ι = 1 is 3(12 + 3z).

(iv) Each of the six 1-forms x^i dx^j − x^j dx^i equals g(R, ·) for the rotation field R = ḡ⁻¹(x^i dx^j − x^j dx^i)
and is Killing for g; they are linearly independent, as are the four functions x^i/r on 𝕊³.

(v) h_m := ∂_m g and, for w := x¹dx² − x²dx¹, h_A := (m/r⁴)(dt ⊗ w + w ⊗ dt) (t the static time) solve
D_g Ric(h) = 0 and lie in ρ²C^∞ and ρ³C^∞. η_m := δ_(g,E)G_g h_m lies in ρ³C^∞ and is spherically symmetric. h_A is
trace-free with δ_g h_A = 0, so η_A := δ_(g,E)G_g h_A = E^Υ h_A = (2γ_Υ m/(fr⁵))w near infinity, of order ρ⁴ and of
vector type 1. The number 1 is not an s0 root and 2 is not a v1 root: the s0 determinant at ι = 1 is 2(2 + z), and the
v1 determinant at ι = 2 is 3.

(vi) The single-spin Myers–Perry metric [ER08, Section 4.1, (32)–(33)] in five dimensions,

    −dt² + (m/Σ)(dt − a sin²ϑ dφ)² + (Σ/Δ)dr² + Σdϑ² + (r² + a²)sin²ϑ dφ² + r²cos²ϑ dψ²,

Σ := r² + a²cos²ϑ, Δ := r² + a² − m, is Ricci-flat [ER08, Section 4.1]; at a = 0 it is g_m, in the coordinates
x¹ + ix² = r sin ϑ e^(iφ), x³ + ix⁴ = r cos ϑ e^(iψ) on the round 𝕊³; and ∂_a of it at a = 0 is −h_A, with
w = r²sin²ϑ dφ.

*Proof.* (i) is [[eq:iii-d2-2-3]] and the proof of [[lem:iii-d2-2-1]] (the static time and the time of
[[eq:iii-b-3-6]] differ by a function of r with derivative in ρ²C^∞), and r_* − r = −m/r + O(r⁻³) by
[[prop:np-10-16]] (v). (ii) δ̄*dx¹ = 0, so δ*_g dx¹ = ((δ*_g)^(0) − (δ̄*)^(0))dx¹ ∈ ρ³C^∞, and 2δ_gG_g ∈ ρ Diff_b¹. The
s1 root is [[eq:iii-d-4-1]] at l = 1, since ½ + (¼ + s)^(1/2) = ½(1 + (1 + 4s)^(1/2)) and
1 + 4s_(1,1) = 17 + 2z − 2(z² + 4z + 16)^(1/2); at z = 0 it is 2, and for z > 0 it exceeds 2 by [[lem:iii-d-4-1]].
(iii) δ̄*B̄ = 0 gives dt_* ⊗_s dx¹ + (δ̄*)^(0)B̆ = 0 with B̆ := B̄ − t_*dx¹ stationary in ρ⁻¹C^∞, so
δ*_gB̄ − t_*δ*_g dx¹ = ((δ*_g)^(0) − (δ̄*)^(0))B̆ ∈ ρ²C^∞; the residual is the sum of the first two terms of
[[eq:iii-d2-3-5]], in ρ³C^∞. At l = 1, ι = 1, [[eq:s13-dets]] gives (3)(1)Q_1(0) = 3(κ(κ + 1) + zκ) with κ = 3.
(iv) g_m = η + (m/r²)(dt − dr)² ([[eq:iii-b-3-4]]) and R annihilates t and r, so g(R, ·) = η(R, ·), which is the
given form; R is Killing for every spherically symmetric metric. Independence: 𝔰𝔬(4) has dimension 6, and the
coordinate functions are independent. (v) g_m is Ricci-flat for every m, so D Ric(∂_m g) = 0; by (vi), h_A is minus
the derivative of a Ricci-flat family, so D Ric(h_A) = 0. The orders follow from [[eq:iii-b-3-4]] and from
|w| = O(r) in Cartesian components. η_m is spherically symmetric because g_m, c_Υ and E_Υ are, and its order follows
as in [[lem:iii-d2-2-1]]: δ_(g,E)G_g maps ρ²C^∞ into ρ³C^∞. For h_A: g^tφ = 0 and w is angular, so tr_g h_A = 0; for
the divergence of a symmetric tensor, ∇_μh^μ_ν = |g|^(−1/2)∂_μ(|g|^(1/2)h^μ_ν) − ½(∂_ν g_αβ)h^(αβ), where the last
term vanishes as h^(αβ) has only tφ components and g_tφ = 0 identically; h^φ_t = m/r⁴ and h^t_φ = −(m/(fr²))sin²ϑ do
not depend on t or φ, so δ_g h_A = 0. Then G_g h_A = h_A and
E^Υ h_A = −2γ_Υ ι_(g⁻¹c)h_A with g⁻¹c = −(fr)⁻¹∂_t, which gives (2γ_Υ m/(fr⁵))w. The determinants are [[eq:s13-dets]]:
1 · (−2)(−2 − z) and (2 + 1)(3 − 2). (vi) At a = 0, Σ = r², Δ = r² − m = r²f, and the metric is
−f dt² + f⁻¹dr² + r²(dϑ² + sin²ϑ dφ² + cos²ϑ dψ²), the last bracket being the round metric of 𝕊³ in these
coordinates. ∂_a of (m/Σ)(dt − a sin²ϑ dφ)² at a = 0 is −(m/r²)sin²ϑ(dt ⊗ dφ + dφ ⊗ dt), and the other coefficients
have vanishing a-derivative at a = 0; with w = x¹dx² − x²dx¹ = r²sin²ϑ dφ this is −h_A. ∎

### Generalised zero energy states: the setting {#sec:iii-d3-1}

The generalised zero energy states of □^Υ_b are polynomials in t_* in its kernel, built on the time translation, the
translations and boosts, the rotations, and the indicial roots of (□^Υ_b)^(0) below −1, with their symmetric gradients
([Hin26, Proposition 6.18 and Remark 6.19] in dimension 4 + 1). The zero energy operator of g_b differs from
Minkowski's by ρ⁴ Diff_b² ([[lem:iii-d2-2-1]]), one power more than on Kerr, so the correction to the leading term of
every stationary state lies two orders below it instead of one. The leading terms are computed exactly on Minkowski
space, and part (1) carries no logarithm.

E_Υ, b, □^Υ_b, P_b := (□^Υ_b)^(0), the model ḡ, t̄ = t_* + |x|, □̄^Υ, the unweighted b-density and the 1-forms
ω^(0)_(b,s0), ω^(0)_(b,s1)(S), ω̆^((0),1)_(b,s1)(S), ω^(−1)_(b,v1)(V) are those of [[sec:iii-d2-1]]–[[sec:iii-d2-3]],
with z = 4e_Υγ_Υ² ∈ (0, ½]. Near ∂X write

    □^Υ_b = A_0 + A_1∂_(t_*) + A_2∂_(t_*)²,   A_0 = P_b ∈ ρ² Diff_b²,   A_1 ∈ ρ Diff_b¹,   A_2 = −g_b^00 ∈ ρ²C^∞,
                                                                                                         {#eq:iii-d3-1-1}

and Ā_0, Ā_1 for the model (Ā_2 = 0). By [[lem:iii-d-2-1]] and [[lem:iii-d2-2-1]], A_0 − Ā_0 ∈ ρ⁴ Diff_b²,
A_1 − Ā_1 = Q_b ∈ ρ³ Diff_b¹, and A_0 − A_0^(m) ∈ ρ⁵ Diff_b², A_1 − A_1^(m) ∈ ρ⁴ Diff_b¹ against the non-rotating
g_m. Also

    δ*_(g_b) = (δ*_(g_b))^(0) + dt_* ⊗_s (·)∂_(t_*),     (δ*_(g_b))^(0) ∈ ρ Diff_b¹.                     {#eq:iii-d3-1-2}

By [[eq:iii-d-2-1]] and [[lem:iii-d-3-1]], Ā_1 = ρN_1(ρ∂_ρ) with N_1(ι) := −2(ι − 3/2 − S̄), and Ā_0 = ρ²N_0(ρ∂_ρ)
with N_0 the indicial family of [[sec:iii-d-4]]; so Ā_1(ρ^a w) = ρ^(a+1)N_1(a)w and Ā_0(ρ^a w) = ρ^(a+2)N_0(a)w for w
on 𝕊³.

*Generalised states.* For stationary 1-forms ω̆⁰ := ω, ω̆¹, …, ω̆^K and k ≤ K put
ω^(≤k) := Σ_(i=0)^k (k!/(k − i)!) t_*^(k−i) ω̆^i ([Hin26, (6.36a)]). The coefficient of t_*^(k−j) in □^Υ_b ω^(≤k) is
(k!/(k − j)!)(A_0ω̆^j + A_1ω̆^(j−1) + A_2ω̆^(j−2)) (ω̆^(−1) = ω̆^(−2) := 0), so

    ω^(≤k) ∈ ker □^Υ_b  (k ≤ K)  ⟺  A_0ω̆^j = −A_1ω̆^(j−1) − A_2ω̆^(j−2)  (0 ≤ j ≤ K).                   {#eq:iii-d3-1-3}

(The proof of [Hin26, Proposition 6.18] prints A_0ω̆^(l−2) for A_2ω̆^(l−2) in this recursion.) By
[[eq:iii-d3-1-2]], δ*_(g_b)ω^(≤k) = Σ_(j=0)^k (k!/(k − j)!) t_*^(k−j) h̆^j with

    h̆^j := (δ*_(g_b))^(0)ω̆^j + dt_* ⊗_s ω̆^(j−1),                                                      {#eq:iii-d3-1-4}

so its constant coefficient is k! h̆^k; and δ*_(g_b)ω^(≤k) lies in ker D_(g_b)Ric ∩ ker δ_(g_b,E_Υ)G_(g_b) whenever
ω^(≤k) ∈ ker □^Υ_b (fact (F2) in the proof of [[prop:iii-d2-3-1]]).

*Exponents.* Let ℳ be the finite set of real numbers in [−10, 10] of the form Re ι + j, ι an indicial root of P_b
([[lem:iii-d-4-1]]; they do not depend on b, and all are real) and j ∈ ℤ, and fix ϵ_ind > 0 less than half the least
distance between distinct points of ℳ (this implies the condition of [[sec:iii-d2-1]]). ℰ_ind denotes an index set
with min Re ℰ_ind ≥ ϵ_ind, changing from line to line. Every exponent below lies in ℳ.

*The model states.* The leading terms of the states are the following exact solutions on 4 + 1 Minkowski space, with
E_Υ at the trace weight 2/3 and c̄ = r⁻¹dt̄. We write e := e_Υ, γ := γ_Υ, and S ∈ 𝒮_1, V ∈ 𝒱_1 as in
[[eq:iii-d2-1-2]]; V = r²V_𝕊 with V_𝕊 a 1-form on the unit 𝕊³, so that V is (0, 0, ρ⁻¹V_𝕊) in the splitting.

**Proposition {#prop:np-10-29}** (The model states of the symmetries.)

(i) With W̄ := |x|(−dt̄ + β_e d|x|) and β_e := (2 − e)/(4e), t_*ω̄^(0)_s0 + W̄ ∈ ker □̄^Υ. The tensor
h̄^(0)_s0 := δ̄*(t_*ω̄^(0)_s0 + W̄) = dt_* ⊗_s ω̄^(0)_s0 + (δ̄*)^(0)W̄ is stationary, homogeneous of degree 0, of scalar
type 0, and in the splitting [[eq:iii-a1-2-2]]

    h̄^(0)_s0 = (16e)⁻¹(2 − 5e, −(2 + 3e), 0, 2 − 5e, 0, 4(2 − e)g_𝕊) ≠ 0;

it lies in the kernels of D_ḡRic and δ_(ḡ,Ē)Ḡ. For 0 < z < 4, none of −1, −2, −3, −4 is an s0 root of P_b; −2 is one
at z = 4.

(ii) With B̆ := ω̆̄^((0),1)_s1(S) and W̄_2 := r²(a_2S dx̄⁰ + b_2S dx̄¹) + k_2r³dS,
(a_2, b_2, k_2) := (24e)⁻¹(4 − 7e, −(4 + 17e), (2/3)(25e − 4)), the polynomial
t_*²ω̄^(0)_s1(S) + 2t_*B̆ + 2W̄_2 lies in ker □̄^Υ. Its halved symmetric gradient
h̄²_s1(S) := dt_* ⊗_s B̆ + (δ̄*)^(0)W̄_2 is stationary, homogeneous of degree −1, of scalar type 1, nonzero for S ≠ 0
and 0 < e < 4/7, and in both kernels. For 0 < z < 20/3, none of −2, −3, −4 is an s1 root of P_b; −2 is one at z = 0
and −3 at z = 20/3.

(iii) t_*V + k_1|x|V ∈ ker □̄^Υ if and only if k_1 = 1 + 2γ/5. Then

    h̄¹_v1(V) := dt_* ⊗_s V + (δ̄*)^(0)(k_1|x|V) = (0, 0, ¼(1 + ⅖γ)ρ⁻¹V_𝕊, 0, ¼(1 − ⅖γ)ρ⁻¹V_𝕊, 0),       {#eq:iii-d3-3-3}

stationary and in both kernels. None of −2, −3, −4 is a v1 root, for every z.

(iv) ι^Υ_(s1,2) = ½(1 + (17 + 2z − 2(z² + 4z + 16)^(1/2))^(1/2)) = 2 + z/12 + O(z²) and
ι^Υ_(s0,2) = ½(1 + (9 + 4z)^(1/2)) = 2 + z/3 + O(z²), and ι^Υ_(s1,2) < ι^Υ_(s0,2) for every z > 0. In particular 1 and
2 lie in the gap (0, ι^Υ_(s1,2)) for z > 0, and 2 is its end at z = 0.

*Proof.* For a stationary u, □̄^Υ(t_*u) = t_*□̄^Υu + Ā_1u, and Ā_1 = −2ρ(ρ∂_ρ − 3/2 − S̄). In the splitting we use the
coefficients (a, b, c) of a type s1 1-form (aS, bS, c d_𝕊S) and the matrices [[eq:s13-nsl]]; write D := ρ∂_ρ.

(i) ω̄ := ω̄^(0)_s0 = −dt̄ = (−½, −½, 0) is Killing, so □̄^Υ(t_*ω̄ + W̄) = Ā_1ω̄ + Ā_0W̄. Here S̄ω̄ = −½γ(1 − e, 3 − e,
0) and (D − 3/2)ω̄ = (¾, ¾, 0), so Ā_1ω̄ = −ρ(3/2 + γ(1 − e), 3/2 + γ(3 − e), 0). Since dt̄ = ½(dx̄⁰ + dx̄¹) and d|x| =
½(dx̄⁰ − dx̄¹), W̄ = ρ⁻¹w with w = ½(β_e − 1, −β_e − 1), and Ā_0W̄ = ρN_s0(−1)w with

    N_s0(−1) = ( −3/2 + γ(1 + 4e) , −3/2 + γ(1 − 4e) ; −3/2 + γ(4e − 1) , −3/2 − γ(1 + 4e) ).

So N_s0(−1)w = (3/2 + γ(4eβ_e − 1), 3/2 + γ(4eβ_e + 1)), which equals (3/2 + γ(1 − e), 3/2 + γ(3 − e)) exactly when
4eβ_e = 2 − e. By [[lem:iii-a1-2-1]] (1), (δ̄*)^(0)(ρ⁻¹w) has a = ½w_0, b = −¼(w_0 − w_1), e′ = −½w_1, q = (w_0 − w_1)g_𝕊
and c = f = 0, and dt_* ⊗_s ω̄ = dx̄¹ ⊗_s ω̄ has b = −¼, e′ = −½; with w_0 − w_1 = β_e this gives the stated
components. h̄^(0)_s0 = δ̄*(t_*ω̄ + W̄) because δ̄*(t_*u) = t_*δ̄*u + dt_* ⊗_s u and δ̄*ω̄ = 0; it lies in the kernels by
fact (F2) of the proof of [[prop:iii-d2-3-1]] for ḡ. The s0 roots below 0 are 1 − ι^Υ_(s0,2) = ½ − (9/4 + z)^(1/2),
which equals −k exactly when z = (k + 2)(k − 1); for k = 1, 2, 3, 4 these are 0, 4, 10, 18.

(ii) By [[eq:iii-d3-1-3]] with Ā_2 = 0, the polynomial lies in the kernel if Ā_0ω̄_s1 = 0, Ā_1ω̄_s1 + Ā_0B̆ = 0 and
Ā_1B̆ + Ā_0W̄_2 = 0. The first two hold since ω̄_s1 and the boost t_*ω̄_s1 + B̆ are Killing. In the splitting,
d(rS) = (½S, −½S, d_𝕊S), so B̆ = r d(rS) − rS dt̄ = ρ⁻¹(0, −S, d_𝕊S), with coefficients ρ⁻¹(0, −1, 1), and
S̄(0, −1, 1) = γ(0, −2, 1); so −Ā_1B̆ = 2(D − 3/2 − S̄)(0, −1, 1) = (0, 5 + 4γ, −5 − 2γ). W̄_2 = ρ⁻²(a_2, b_2, k_2) and
Ā_0W̄_2 = N_s1(−2)(a_2, b_2, k_2), where at l = 1 (κ = 3), N_s1(−2) = N⁰ + γN¹ with

    N⁰ = ( −7/2 , −3/2 , −3 ; −3/2 , −7/2 , 3 ; −2 , 2 , −6 ),
    N¹ = ( 2 + 5e , 2 − 5e , −3e ; 5e − 2 , −(2 + 5e) , −3e ; 2 , 2 , 0 ).

Multiplying out, N⁰(a_2, b_2, k_2) = (24e)⁻¹(0, 120e, −120e) = (0, 5, −5) and
N¹(a_2, b_2, k_2) = (24e)⁻¹(0, 96e, −48e) = (0, 4, −2). For instance the first entry of N⁰(a_2, b_2, k_2) is
(24e)⁻¹(−(7/2)(4 − 7e) + (3/2)(4 + 17e) − 2(25e − 4)) = 0, and the second entry of N¹(a_2, b_2, k_2) is
(24e)⁻¹((5e − 2)(4 − 7e) + (2 + 5e)(4 + 17e) − e(50e − 8)) = (24e)⁻¹ · 96e. So the third relation holds. By
[[eq:iii-d3-1-2]] for ḡ, δ̄*(t_*²ω̄_s1 + 2t_*B̆ + 2W̄_2) = 2t_*δ̄*(t_*ω̄_s1 + B̆) + 2(dt_* ⊗_s B̆ + (δ̄*)^(0)W̄_2), and
the first term vanishes; so h̄²_s1 is stationary, and it lies in the kernels by (F2). Its (dx̄¹)² component is
−ρ⁻¹S from dt_* ⊗_s B̆ plus ½ρD(ρ⁻²b_2S) = −b_2ρ⁻¹S, in all −(1 + b_2)ρ⁻¹S, and 1 + b_2 = (7e − 4)/(24e). For the
roots: the s1 roots other than 1 − ι^Υ_(s1,j) are 0, 4 and the positive ι^Υ_(s1,j); and 1 − ι = −k exactly when
ι² − ι = k(k + 1), that is when Q_1(k(k + 1)) = 0. With Q_1(s) = s² − (8 + z)s + 12 + 3z, Q_1(6) = −3z,
Q_1(12) = 60 − 9z and Q_1(20) = 252 − 17z.

(iii) V = ρ⁻¹(0, 0, V_𝕊) and |x|V = ρ⁻²(0, 0, V_𝕊). On v1, Ā_0(ρ^a(0, 0, V_𝕊)) = ρ^(a+2)(−a² + 2a + 3)(0, 0, V_𝕊) and
S̄ = γ on angular components, so Ā_0(k_1|x|V) = −5k_1(0, 0, V_𝕊) and Ā_1V = −2(−1 − 3/2 − γ)(0, 0, V_𝕊)
= (5 + 2γ)(0, 0, V_𝕊). The relation Ā_1V + Ā_0(k_1|x|V) = 0 holds exactly when k_1 = 1 + 2γ/5. By
[[lem:iii-a1-2-1]] (1), (δ̄*)^(0)(ρ⁻²(0, 0, V_𝕊)) has c = −¼ρ(D + 1)ρ⁻²V_𝕊 = ¼ρ⁻¹V_𝕊, f = −¼ρ⁻¹V_𝕊 and
q = ρ⁻¹δ*_𝕊V_𝕊 = 0 (V_𝕊 is Killing on 𝕊³), and dt_* ⊗_s V has f = ½ρ⁻¹V_𝕊; with k_1 this is [[eq:iii-d3-3-3]].
Stationarity and the kernels follow as in (ii). The v1 roots are −1 and 3.

(iv) ½ + (¼ + s)^(1/2) = ½(1 + (1 + 4s)^(1/2)), and 1 + 4s_(1,1) = 17 + 2z − 2(z² + 4z + 16)^(1/2),
1 + 4(2 + z) = 9 + 4z. The expansions are those of [[lem:iii-d-4-1]]. ι^Υ_(s1,2) < ι^Υ_(s0,2) if and only if
s_(1,1) < 2 + z, that is 2 − z/2 < (4 + z + z²/4)^(1/2), which holds for z ≥ 4 trivially and for 0 < z < 4 after
squaring. ∎

**Proposition {#prop:np-10-30}** (The classes without symmetry.) On 4 + 1 Minkowski space, for □̄^Υ:

(i) (*The indicial families.*) On the types s0, sl (l ≥ 1) and vl, Ā_2 = 0, Ā_0 = ρ²N_0(ρ∂_ρ) with det N_0 given by
[[eq:s13-dets]], and Ā_1 = ρN_1(ρ∂_ρ) with N_1(ι) = −2(ι − 3/2 − S̄), S̄ independent of ι. At vl,
N_0(ι) = −(ι + l)(ι − l − 2) and N_1(ι) = −2(ι − 3/2 − γ_Υ).

(ii) (*The classes.*) For every l ≥ 1, Q_l(l(l + 1)) = lz, Q_l((l + 1)(l + 2)) = −(l + 2)z and
Q_l((l + 2)(l + 3)) = (l + 2)(8l + 12 − 3z). So for 0 < z < 20/3 the negative sl roots other than 1 − l,
μ_(l,0) := 1 − ι^Υ_(sl,l+1) and μ_(l,1) := 1 − ι^Υ_(sl,l+2), satisfy −l − 1 < μ_(l,0) < −l and
−l − 2 < μ_(l,1) < −l − 1, with μ_(l,0) = −l − lz/(2(l + 1)(2l + 1)) + O(z²) and
μ_(l,1) = −l − 1 − (l + 2)z/(2(l + 1)(2l + 3)) + O(z²). μ_s0 := 1 − ι^Υ_(s0,2) = ½(1 − (9 + 4z)^(1/2))
= −1 − z/3 + O(z²) lies in (−2, −1) for 0 < z < 4. The sl roots 1 − l and the vl roots −l are roots at every z. For
0 < z < 4 the roots ≤ 0 of each type are these, together with 0 at s0.

(iii) (*The symmetric gradient.*) N(δ̄*(0), ι) is injective on the types sl and vl for l ≥ 2 and every ι ∈ ℂ, on s0
and s1 for ι ≠ 0, and on v1 for ι ≠ −1.

(iv) (*No resonance.*) Let 0 < z < 4. Call a class root each of μ_s0 (type s0, range K = 2), μ_(l,0) and μ_(l,1)
(type sl, l = 1, 2, 3, K = 2), 1 − l (type sl, 2 ≤ l ≤ 5, K = 5 − l) and −l (type vl, 2 ≤ l ≤ 4, K = 4 − l). For each
class root μ of type τ, μ is a simple root of type τ, and neither μ + 2 nor μ − k, 1 ≤ k ≤ K, is a root of type τ.
The bound 4 is sharp: at z = 4, μ_s0 = −2 and μ_s0 + 2 = 0 is an s0 root. At z = 0 the classes meet at sl:
μ_(l,0) − 1 = μ_(l,1), μ_(l,1) + 2 = 1 − l, and 1 − l − k = μ_(l,k−1) for k ≤ min(2, 5 − l); never at vl.

(v) (*The states.*) For each class root μ of type τ with a nonzero indicial solution ρ^μ w̄_0 of the model, the
recursion N_0(μ − i)w̄_i = −N_1(μ − i + 1)w̄_(i−1), 1 ≤ i ≤ K, has a unique solution of type τ, and
Σ_(i=0)^k (k!/(k − i)!) t_*^(k−i) ρ^(μ−i)w̄_i ∈ ker □̄^Υ for k ≤ K. At vl, w̄_i = k_i w̄_0 with k_0 = 1 and
k_i = k_(i−1)(2l + 2i + 1 + 2γ_Υ)/(i(2l + i + 2)); at l = 1, k_1 = 1 + 2γ_Υ/5.

*Proof.* (i) is [[eq:iii-d-2-1]], [[lem:iii-d-3-1]] and [[sec:iii-d-4]]; on vl, S̄ acts as γ_Υ and N_0 = p + κ.
(ii) By [[eq:s13-qfactor]], Q_l(s) = (s − l(l + 1))(s − (l + 1)(l + 2)) + z(κ − s), and κ − l(l + 1) = l,
κ − (l + 1)(l + 2) = −(l + 2), κ − (l + 2)(l + 3) = −3(l + 2), while the product at (l + 2)(l + 3) is
(4l + 6) · 2(l + 2). As Q_l is a monic quadratic, its roots s_(l,1) < s_(l,2) satisfy
l(l + 1) < s_(l,1) < (l + 1)(l + 2) < s_(l,2) < (l + 2)(l + 3) when 0 < z < (8l + 12)/3, which holds for z < 20/3;
and ι ↦ ι² − ι is increasing on ι > ½, which gives the intervals. The expansions and μ_s0 are those of
[[lem:iii-d-4-1]], and ½ − (9/4 + z)^(1/2) ∈ (−2, −1) for 0 < z < 4. The last sentence follows from the list of
[[lem:iii-d-4-1]], whose positive roots are > 0. (iii) is [[lem:iii-a1-2-4]].
(iv) *Simplicity.* For 0 < z < 4 the roots of type s0 are μ_s0 ∈ (−2, −1), 0, ι^Υ_(s0,2) ∈ (2, 3) and 3, and those of
type sl are μ_(l,1) < −l − 1 < μ_(l,0) < −l < 1 − l < l + 1 < ι^Υ_(sl,l+1) < l + 2 < ι^Υ_(sl,l+2) < l + 3; they are
distinct, so each is a simple zero of the determinant [[eq:s13-dets]], whose degree is their number. *μ_s0.* μ_s0 + 2
∈ (0, 1), μ_s0 − 1 ∈ (−3, −2) and μ_s0 − 2 ∈ (−4, −3) contain no s0 root. *μ_(l,0).* μ_(l,0) + 2 ∈ (−l + 1, −l + 2)
and μ_(l,0) − 2 ∈ (−l − 3, −l − 2) contain no sl root. μ_(l,0) − 1 ∈ (−l − 2, −l − 1) could only be μ_(l,1); but
μ_(l,0) − 1 = μ_(l,1) means ι_2 = ι_1 + 1 for ι_j := ι^Υ_(sl,l+j). Then s_(l,1) = ι_1² − ι_1 and
s_(l,2) = ι_1² + ι_1, and the relations s_(l,1) + s_(l,2) = 2 + 2κ + z and s_(l,1)s_(l,2) = κ(κ + 1) + zκ give
ι_1² = (l + 1)² + z/2 =: X and X(X − 1) = κ((l + 1)² + z); since X − 1 = κ + z/2, the difference of the two sides is
z/2 + z²/4, which vanishes only at z = 0 and z = −2. *μ_(l,1).* μ_(l,1) + 2 ∈ (−l, −l + 1), μ_(l,1) − 1 and
μ_(l,1) − 2 lie below −l − 2, and none of these intervals contains an sl root. *The integer classes.* For μ = 1 − l
(sl), μ + 2 = 3 − l and μ − k = 1 − l − k are integers different from 1 − l and l + 3, the only integer sl roots, and
the noninteger roots are not integers. For μ = −l (vl), μ + 2 = 2 − l and −l − k differ from −l and l + 2. *At
z = 4*, ½ − (9/4 + 4)^(1/2) = −2. *At z = 0*, μ_(l,0) = −l, μ_(l,1) = −l − 1, and the coincidences are immediate.
(v) By (iv), N_0(μ − i) is invertible on type τ for 1 ≤ i ≤ K, and N_0, N_1 preserve the type
([[sec:iii-a1-2]]), so the recursion has a unique solution. With ω̆^i := ρ^(μ−i)w̄_i, Ā_0ω̆^i = ρ^(μ−i+2)N_0(μ − i)w̄_i
and Ā_1ω̆^(i−1) = ρ^(μ−i+2)N_1(μ − i + 1)w̄_(i−1), so [[eq:iii-d3-1-3]] holds for the model with Ā_2 = 0. At vl,
N_0(−l − i) = −i(2l + i + 2) and N_1(−l − i + 1) = 2l + 2i + 1 + 2γ_Υ, which gives the recursion for k_i; at l = 1,
i = 1 it is (5 + 2γ_Υ)/5. ∎

We collect the root facts used below; all hold for 0 < z ≤ ½.

(R1) −1, −2, −3, −4 are not s0 roots of P_b ([[prop:np-10-29]] (i)).

(R2) −2, −3, −4 are not s1 roots ([[prop:np-10-29]] (ii)).

(R3) −2, −3, −4 are not v1 roots ([[prop:np-10-29]] (iii)).

(R4) The class roots of [[prop:np-10-30]] (iv) are simple, and for each class root μ of type τ with range K, neither
μ + 2 nor μ − k, 1 ≤ k ≤ K, is a type τ root ([[prop:np-10-30]] (ii), (iv)).

(R5) The indicial family N(δ̄*(0), ι) is injective on each type except at ι = 0 (s0, s1) and ι = −1 (v1)
([[lem:iii-a1-2-4]]).

### Solving with a prescribed leading term {#sec:iii-d3-2}

**Lemma {#lem:iii-d3-2-1}** Let m_* ∈ ℳ, m_* ≤ 2, and let f_1 be smooth on X with ρ⁻²f_1 ∈ 𝒜^ℱ near ∂X, where
ℱ ⊂ {(m_*, 0)} ∪ {Re ≥ m_* + ϵ_ind}, and suppose that the ρ^(m_*)-coefficient f_(m_*) of ρ⁻²f_1 has components only of
types τ for which m_* is not a type τ root. Then there is u ∈ 𝒜^((m_*,0)∪(m_*+ℰ_ind)), smooth on X, with P_bu = f_1
and ρ^(m_*)-coefficient u_(m_*) = N(ρ⁻²P_b, m_*)⁻¹f_(m_*), of the types of f_(m_*). If f_1 depends smoothly on b (in
the topology of these spaces), u can be chosen to.

*Proof.* Near ∂X, A := ρ⁻²P_b is an elliptic b-operator whose normal operator is the model's ([[lem:iii-d-2-1]] (3))
and so commutes with the rotations; its indicial family N(A, ι) preserves the types, and on type τ it is invertible
exactly off the type τ roots. So w := N(A, m_*)⁻¹f_(m_*) is defined, smooth on 𝕊³, of the types of f_(m_*). With
χ_∂ the cut-off of [[ch:s03]], u_0 := χ_∂ρ^(m_*)w has P_bu_0 = χ_∂ρ^(m_*+2)f_(m_*) + ρ²(A − N(A))(χ_∂ρ^(m_*)w)
+ (smooth, compactly supported), and A − N(A) ∈ ρ Diff_b², so f_2 := f_1 − P_bu_0 has ρ⁻²f_2 ∈ 𝒜^(ℱ_1) with
ℱ_1 ⊂ {Re ≥ m_* + ϵ_ind}. [[lem:iii-a-1-5]] (formal solutions; on the bundle, by the argument given for
[[lem:iii-a-1-4]] in the proof of [[lem:iii-d1-5-1]]) with β = 3 gives u_1 ∈ 𝒜^(ℰ_1) near ∂X,
ℰ_1 ⊂ {Re ≥ m_* + ϵ_ind} (its exponents are those of ℱ_1 plus ℕ_0, with logarithms where they meet roots), such that
f_3 := f_2 − P_b(χ_∂u_1) is smooth on X̄ with ρ⁻²f_3 ∈ 𝒜^𝒢, 𝒢 ⊂ {Re ≥ 3}. Finally u_2 := P_b⁻¹f_3
([[lem:iii-d1-5-1]]): u_2 ∈ ⋂_s H̄_b^(s,α) for every α < ι^Υ_(s1,2), and [[lem:iii-a-1-4]] with α just below
ι^Υ_(s1,2) (no root in between) gives u_2 ∈ 𝒜^(ℰ_2) with ℰ_2 ⊂ {Re ≥ ι^Υ_(s1,2)} ⊂ {Re ≥ m_* + ϵ_ind}, as m_* ≤ 2 and
ι^Υ_(s1,2) − 2 > 2ϵ_ind. Then u := u_0 + χ_∂u_1 + u_2. Smoothness in b: w depends smoothly on b (the normal operator
does not depend on b, and f_(m_*) does smoothly), [[lem:iii-a-1-5]] states smooth dependence for a smoothly varying A,
and [[lem:iii-d2-2-2]] covers u_2. ∎

When the leading term of f_1 is that of a model right side, that is f_1 = f̄ + f′ with ρ⁻²f̄ ∈ ρ^(m_*)C^∞ near ∂X the
right side of a model equation Ā_0ū = f̄ solved by a homogeneous ū = ρ^(m_*)w̄, and f′ two orders lower, the leading term
of u is ū: indeed f_(m_*) = f̄_(m_*) and N(A, m_*) = N(ρ⁻²Ā_0, m_*), so u_(m_*) = w̄.

### The generalised states {#sec:iii-d3-3}

**Proposition {#prop:iii-d3-3-1}** ([Hin26, Proposition 6.18] in dimension 4 + 1.) Assume (Dyn), and let E_Υ and b be
as in [[sec:iii-d3-1]]. All 1-forms below are stationary, smooth on X, smooth in b, and linear in S ∈ 𝒮_l and
V ∈ 𝒱_l; every ω^(≤k) lies in ker □^Υ_b, and every symmetric gradient δ*_(g_b)ω^(≤k) in
ker D_(g_b)Ric ∩ ker δ_(g_b,E_Υ)G_(g_b).

(1) (*The time translation; the s0 root 0 of the linearised operator.*) Let W̄ and β_e be as in [[prop:np-10-29]] (i).
There are ω̆^((0),1)_(b,s0) with ω̆^((0),1)_(b,s0) − χ_∂W̄ ∈ 𝒜^((1,0)∪(1+ℰ_ind)), and
ω̆^((0),k)_(b,s0) ∈ 𝒜^((−k,0)∪(−k+ℰ_ind)), k = 2, 3, 4, with scalar type 0 leading terms, such that, with
ω^(0)_(b,s0) as the zeroth term, ω^((0),≤k)_(b,s0) ∈ ker □^Υ_b for k ≤ 4. The stationary tensor

    h^(0)_(b,s0) := δ*_(g_b)ω^((0),≤1)_(b,s0) ∈ 𝒜^((0,0)∪(2,0)∪(2+ℰ_ind))                                {#eq:iii-d3-3-1}

has the leading term h̄^(0)_s0 of [[prop:np-10-29]] (i), nonzero, homogeneous of degree 0 and of scalar type 0. For
k = 0, …, 3, h^((0),≤k)_(b,s0) := (k + 1)⁻¹δ*_(g_b)ω^((0),≤k+1)_(b,s0)
= t_*^k h^(0)_(b,s0) + Σ_(i=1)^k (k!/(k − i)!) t_*^(k−i) h̆^((0),i)_(b,s0), with

    h̆^((0),i)_(b,s0) := (δ*_(g_b))^(0)ω̆^((0),i+1)_(b,s0) + dt_* ⊗_s ω̆^((0),i)_(b,s0) ∈ 𝒜^((−i,0)∪(−i+ℰ_ind)).
                                                                                                         {#eq:iii-d3-3-2}

(2) (*The boosts to higher order; the s1 root −1.*) There are ω̆^((0),k)_(b,s1)(S) ∈ 𝒜^((−k,0)∪(−k+ℰ_ind)),
k = 2, 3, 4, with scalar type 1 leading terms, continuing ω^(0)_(b,s1)(S), ω̆^((0),1)_(b,s1)(S) of
[[prop:iii-d2-3-1]], such that ω^((0),≤k)_(b,s1)(S) ∈ ker □^Υ_b for k ≤ 4. With [[eq:iii-d3-1-4]], the constant
coefficient of h^(≤k)_(b,s1)(S) := δ*_(g_b)ω^((0),≤k)_(b,s1)(S) is k! h̆^k_(b,s1)(S), with
h̆^k_(b,s1)(S) ∈ 𝒜^((−k+1,0)∪(−k+1+ℰ_ind)) (k = 2, 3, 4), and the leading term of h̆²_(b,s1)(S) is h̄²_s1(S) of
[[prop:np-10-29]] (ii), homogeneous of degree −1, of scalar type 1, nonzero for S ≠ 0; here the leading term of
ω̆^((0),2)_(b,s1)(S) is the model solution W̄_2 of Ā_0W̄_2 = −Ā_1ω̆̄^((0),1)_s1.

(3) (*The rotations to higher order; the v1 root −1.*) There are ω̆^((−1),k)_(b,v1)(V) ∈ 𝒜^((−k−1,0)∪(−k−1+ℰ_ind)),
k = 1, 2, 3, with vector type 1 leading terms, the first being (1 + ⅖γ_Υ)|x|V, such that
ω^((−1),≤k)_(b,v1)(V) ∈ ker □^Υ_b for k ≤ 3. The constant coefficient of
h^(≤k)_(b,v1)(V) := δ*_(g_b)ω^((−1),≤k)_(b,v1)(V) is k! h̆^k_(b,v1)(V), with
h̆^k_(b,v1)(V) ∈ 𝒜^((−k,0)∪(−k+ℰ_ind)), and the leading term of h̆¹_(b,v1)(V) is h̄¹_v1(V) of [[eq:iii-d3-3-3]] (in
[Hin26]'s splitting, the analogue of [Hin26, (6.40)]). If R_V is Killing for g_b (at A = 0, every V), then
h^(≤1)_(b,v1)(V) = h̆¹_(b,v1)(V) is stationary ([Hin26, Remark 6.19]).

(4)–(7) (*The classes without symmetry.*) Let μ be a class root of [[prop:np-10-30]] (iv), of type
τ ∈ {s0, sl, vl}, K its range, and ω̄ = ρ^μ w̄ a nonzero indicial solution of the model of type τ (given by S ∈ 𝒮_l or
V ∈ 𝒱_l). There are ω^(μ)_b ∈ 𝒜^((μ,0)∪(μ+ℰ_ind)) with leading term ω̄ and
ω^(μ)_b − χ_∂ω̄ ∈ 𝒜^((μ+2,0)∪(μ+2+ℰ_ind)), P_bω^(μ)_b = 0, and ω̆^((μ),k)_b ∈ 𝒜^((μ−k,0)∪(μ−k+ℰ_ind)), 1 ≤ k ≤ K,
with type τ leading terms, such that ω^((μ),≤k)_b ∈ ker □^Υ_b for k ≤ K. The symmetric gradient
h^(μ+1)_b := δ*_(g_b)ω^(μ)_b ∈ 𝒜^((μ+1,0)∪(μ+1+ℰ_ind)) has the nonzero leading term (δ̄*)^(0)ω̄, of type τ, and the
constant coefficient of δ*_(g_b)ω^((μ),≤k)_b is k! h̆^((μ),k)_b, with
h̆^((μ),k)_b ∈ 𝒜^((μ+1−k,0)∪(μ+1−k+ℰ_ind)).

*Proof.* Each step solves an equation A_0ω̆ = f_1 by [[lem:iii-d3-2-1]]; we name its m_*, the type of the leading
coefficient of f_1 and the root fact that applies, and identify the leading term by the remark after
[[lem:iii-d3-2-1]]. *Types.* At b = (m, 0) the operators are invariant under the rotations of x (with c_Υ and c_(Υ,H)
radial, [[sec:iii-d2-1]]), so every construction from S ∈ 𝒮_l (or V ∈ 𝒱_l) stays in the corresponding isotypic
component, the type of the class (as in the proof of [[prop:iii-d2-3-1]] (2)); for general b, A_i − A_i^(m) is one
order lower than A_i − Ā_i ([[sec:iii-d3-1]]), so leading coefficients are unchanged and keep their types. *Model
solutions.* The model leading terms named below solve the model equations exactly, by [[prop:np-10-29]] and
[[prop:np-10-30]] (v).

*(1).* ω_s0 := ω^(0)_(b,s0) is Killing, so A_0ω_s0 = 0 and A_1ω_s0 = □^Υ_b(t_*ω_s0)
= 2δ_(g_b,E_Υ)G_(g_b)(dt_* ⊗_s ω_s0) ∈ ρC^∞. The model has Ā_0W̄ = −Ā_1ω̄_s0 ([[prop:np-10-29]] (i)). So
ω̆¹ := χ_∂W̄ + ω̆′ with A_0ω̆′ = −(A_1ω_s0 − Ā_1ω̄_s0) − (A_0 − Ā_0)W̄ + (compactly supported). Here
A_1ω_s0 − Ā_1ω̄_s0 = Q_bω_s0 + Ā_1(ω_s0 − ω̄_s0) ∈ ρ³C^∞ ([[eq:iii-d2-3-2]]) and
(A_0 − Ā_0)W̄ ∈ ρ⁴ Diff_b²(ρ⁻¹C^∞) ⊂ ρ³C^∞, so [[lem:iii-d3-2-1]] with m_* = 1 (no root) gives
ω̆′ ∈ 𝒜^((1,0)∪(1+ℰ_ind)). In particular the right side □^Υ_b(t_*ω_s0) has the model's ρ¹ term and no ρ² term. Then
h^(0)_(b,s0) = dt_* ⊗_s ω_s0 + (δ*_(g_b))^(0)ω̆¹, and
h^(0)_(b,s0) − h̄^(0)_s0 = dt_* ⊗_s (ω_s0 − ω̄_s0) + ((δ*_(g_b))^(0) − (δ̄*)^(0))W̄ + (δ*_(g_b))^(0)ω̆′, which lies in
ρ²C^∞ + ρ³ Diff_b⁰(ρ⁻¹C^∞) + 𝒜^((2,0)∪(2+ℰ_ind)); this is [[eq:iii-d3-3-1]]. h̄^(0)_s0 is stationary, homogeneous of
degree 0, nonzero, and lies in the kernels of D_ḡRic and δ_(ḡ,Ē)Ḡ ([[prop:np-10-29]] (i)). For k = 2, 3, 4,
[[eq:iii-d3-1-3]] asks A_0ω̆^k = −A_1ω̆^(k−1) − A_2ω̆^(k−2); inductively the right side lies in
ρ Diff_b¹ 𝒜^((−k+1,0)∪(−k+1+ℰ_ind)) + ρ²𝒜^((−k+2,0)∪…), so ρ⁻² of it has m_* = −k, its leading coefficient that of
−Ā_1ω̆̄^(k−1), of type s0, and −k is no s0 root (R1); [[lem:iii-d3-2-1]] gives ω̆^k ∈ 𝒜^((−k,0)∪(−k+ℰ_ind)). The
formula for h^((0),≤k): by [[eq:iii-d3-1-4]] with h̆′^j := (δ*_(g_b))^(0)ω̆^j + dt_* ⊗_s ω̆^(j−1), h̆′^0 = 0 and
h̆′^1 = h^(0)_(b,s0), δ*_(g_b)ω^(≤k+1) = Σ_(i=0)^k ((k + 1)!/(k − i)!) t_*^(k−i) h̆′^(i+1)
= (k + 1)Σ_(i=0)^k (k!/(k − i)!) t_*^(k−i) h̆′^(i+1), and h̆^((0),i)_(b,s0) = h̆′^(i+1); the orders follow from
[[eq:iii-d3-1-2]].

*(2).* Inductively, for k = 2, 3, 4, the right side of [[eq:iii-d3-1-3]] is −A_1ω̆^(k−1) − A_2ω̆^(k−2) with
ω̆¹ = ω̆^((0),1)_(b,s1) ∈ 𝒜^((−1,0)∪(1,0)∪(1+ℰ_ind)) ([[eq:iii-d2-3-2]]); ρ⁻² of it has m_* = −k and leading
coefficient that of −Ā_1ω̆̄^(k−1), of scalar type 1, and −k is no s1 root (R2). [[lem:iii-d3-2-1]] gives ω̆^k, with
leading term the model's ω̆̄^k_s1. By [[eq:iii-d3-1-4]],
h̆^k = (δ*_(g_b))^(0)ω̆^k + dt_* ⊗_s ω̆^(k−1) ∈ 𝒜^((−k+1,0)∪…). Its ρ⁻¹ term at k = 2 is h̄²_s1(S), which is half the
symmetric gradient of t_*²ω̄_s1 + 2t_*ω̆̄¹_s1 + 2W̄_2, stationary because t_*ω̄_s1 + ω̆̄¹_s1 is a boost, and nonzero
for S ≠ 0 ([[prop:np-10-29]] (ii), as e_Υ ≤ ϵ_1 < 4/7).

*(3).* For k = 1: ω_v1 := ω^(−1)_(b,v1)(V) = V + 𝒜^((2,0)∪…), and −A_1ω_v1 has ρ⁻² of it with m_* = −2 and leading
coefficient that of −Ā_1V, of vector type 1; −2 is no v1 root (R3), so [[lem:iii-d3-2-1]] gives ω̆¹ with leading
term the model's, (1 + ⅖γ_Υ)|x|V ([[prop:np-10-29]] (iii)). k = 2, 3 are as in (2), with m_* = −k − 1 and (R3).
h̆¹ = (δ*_(g_b))^(0)ω̆¹ + dt_* ⊗_s ω_v1 has the leading term (δ̄*)^(0)((1 + ⅖γ_Υ)|x|V) + dt_* ⊗_s V, which is
[[eq:iii-d3-3-3]]. If R_V is Killing for g_b, ω_v1 = g_b(R_V, ·) ([[prop:iii-d2-3-1]] (3)), so δ*_(g_b)ω_v1 = 0 and
h^(≤1)_(b,v1) = h̆¹_(b,v1).

*(4)–(7).* P_b(χ_∂ω̄) = χ_∂(A_0 − Ā_0)ω̄ + (compactly supported), and
(A_0 − Ā_0)ω̄ ∈ ρ⁴ Diff_b²(ρ^μC^∞) ⊂ ρ^(μ+4)C^∞, whose leading coefficient comes from g_m − ḡ (the rotation enters one
order lower) and so is of type τ; [[lem:iii-d3-2-1]] with m_* = μ + 2 ≤ 2 (no type τ root, (R4)) gives ω′ with
P_bω′ = −P_b(χ_∂ω̄), and ω^(μ)_b := χ_∂ω̄ + ω′. Its symmetric gradient:
(δ*_(g_b))^(0)ω^(μ)_b = (δ̄*)^(0)ω̄ + ((δ*_(g_b))^(0) − (δ̄*)^(0))ω̄ + (δ*_(g_b))^(0)ω′, the last two in ρ^(μ+3); the
first is ρ^(μ+1)N(ρ⁻¹(δ̄*)^(0), μ)w̄, nonzero by (R5), as μ ∉ {0, −1}. The recursion [[eq:iii-d3-1-3]]: for
1 ≤ k ≤ K, the right side −A_1ω̆^(k−1) − A_2ω̆^(k−2) has ρ⁻² of it with m_* = μ − k and leading coefficient that of
−Ā_1ω̆̄^(k−1), of type τ, while its other terms are lower by at least ϵ_ind, which is all the identification of the
leading coefficient needs: (A_1 − Ā_1)ω̆̄^(k−1) and A_2ω̆^(k−2) are in ρ^(μ−k+4), Ā_1(ω̆^(k−1) − ω̆̄^(k−1)) is in
𝒜^(μ−k+2+ℰ_ind) by [[lem:iii-d3-2-1]], and (A_0 − Ā_0) applied to the leading term to be found is in ρ^(μ−k+4).
μ − k is no type τ root (R4), so [[lem:iii-d3-2-1]] gives ω̆^k with leading term the model's ω̆̄^k
([[prop:np-10-30]] (v)). The corrections, lower by at least ϵ_ind, may meet roots, and their logarithms are in
μ − k + ℰ_ind. The statements about h̆^((μ),k)_b follow from [[eq:iii-d3-1-4]]. ∎

*Remarks.* (a) [Hin26] also states that the leading terms h̄^(0)_s0, h̄²_s1(S), h̄¹_v1(V) and (δ̄*)^(0)ω̄ span the
kernels of the indicial families of the model of the linearised gauge-fixed Einstein operator at the corresponding
roots, N_τ(L̄(0), ι), ι = 0, −1, −1, μ + 1. That is a statement about L̄, whose indicial roots and kernels are
[Hin26, Lemma 8.4] in dimension 4 + 1; it is proved with that lemma, in [[ch:s15]]. (b) *The window.* The classes and
their degrees are [Hin26]'s, chosen there to capture the pure gauge contributions down to t_*⁻⁴ in the late-time
expansion on Kerr. Which window dimension 4 + 1 needs is decided by the decay proved in [[ch:s19]]–[[ch:s24]]; if it
is wider, the same construction applies to the further roots, given the corresponding root facts. (c) *No logarithm in
(1).* [Hin26]'s ω̆^((0),1)_(b,s0) lies in 𝒜^((−1,0)∪(0,1)∪(1+ℰ_ind)), with log ρ at the s0 root 0, from the ρ² term of
its right side; in dimension 4 + 1 that term vanishes. (d) The coefficients β_e and (a_2, b_2, k_2) of
[[prop:np-10-29]] carry e_Υ⁻¹: at e_Υ = 0, −1 at s0 and −2 at s1 are indicial roots of P_b, the integer coincidences
that e_Υ > 0 removes [Hin26, p. 81]. The same coincidences at e_Υ = 0 are those of [[prop:np-10-30]] (iv) at z = 0.
