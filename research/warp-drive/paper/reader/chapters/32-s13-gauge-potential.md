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
[[prop:np-10-29]] and [[prop:np-10-30]] (the model generalised states and their root facts). The trapping computations
of [[prop:np-10-17]] and [[prop:np-10-19]] are proved in [[ch:s12]].

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

    □^Υ_b := □^Υ_(g_b,E_Υ) = 2δ_(g_b,E_Υ) G_(g_b) δ*_(g_b) = □_(g_b) + 2E^Υ_(g_b) G_(g_b) δ*_(g_b),          {#eq:iii-d-1-1}

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

    □̄^Υ = −2∂_(t_*) ρ(ρ∂_ρ − 3/2 − S̄) + (□̄^Υ)^(0),                                                      {#eq:iii-d-2-1}

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
    Ē = γρ ⎜ 0   2 − 2m_N(1 − e)   0   2   0   ½m_N(1 − e) tr ⎟ ;                                      {#eq:iii-d-3-1}
           ⎝ 0   0                 2   0   2   0              ⎠

                                        ⎛ 1 − e   0   0 ⎞
    2ĒḠδ̄* = 2∂_(t_*) ρS̄ + γρ²M_E,   S̄ = γ ⎜ 1 − e   2   0 ⎟ ,
                                        ⎝ 0       0   1 ⎠

          ⎛ −(1 + e)D + Ne    −(1 − e)D − Ne   −e δ_𝕊 ⎞
    M_E = ⎜ (1 − e)D + Ne     (1 + e)D − Ne    −e δ_𝕊 ⎟ ;                                              {#eq:iii-d-3-2}
          ⎝ 2d_𝕊              2d_𝕊             0      ⎠

so that □̄^Υ = −2∂_(t_*) ρ(D − N/2 − S̄) + (□̄^Υ)^(0) with

    (□̄^Υ)^(0) = ᵇ□̄(0) + γρ²M_E.                                                                          {#eq:iii-d-3-3}

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

    ι^Υ_(sl,l+j) := ½ + (¼ + s_(l,j))^(1/2)  (j = 1, 2),     ι^Υ_(s0,2) := ½ + (9/4 + z)^(1/2).            {#eq:iii-d-4-1}

The type-wise indicial matrices are read off from [[eq:iii-d-3-3]], [[lem:iii-a1-2-1]] (1) and the identities
[[lem:iii-a1-1-5]]. On a scalar type l 1-form (aS, bS, c d_𝕊S), S ∈ 𝒮_l, l ≥ 1, the operator ρ⁻²(□̄^Υ)^(0) acts on
ρ^ι(a, b, c) as ρ^ι N_sl(ι)(a, b, c), where, with p := −ι² + 2ι,

               ⎛ p + κ + 3/2 − γ((1 + e)ι − 3e)   −3/2 − γ((1 − e)ι + 3e)            −κ(1 + eγ) ⎞
    N_sl(ι) =  ⎜ −3/2 + γ((1 − e)ι + 3e)           p + κ + 3/2 + γ((1 + e)ι − 3e)    κ(1 − eγ)  ⎟ ,       {#eq:s13-nsl}
               ⎝ −2 + 2γ                           2 + 2γ                            p + κ − 1  ⎠

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

    ι^Υ_(sl,l+j) ∈ (l + j, l + j + ¼),     ι^Υ_(s0,2) ∈ (2, 2 + z/3],     2 < ι^Υ_(s1,2) < min(ι^Υ_(s0,2), 3),    {#eq:iii-d-4-2}

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

    (s − l(l + 1))(s − (l + 1)(l + 2)) = s² − (2 + 2κ)s + κ(κ + 1),                                        {#eq:s13-qfactor}

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

    Γ^v_vv = f′/2,   Γ^r_vv = ff′/2,   Γ^r_vr = −f′/2,   Γ^v_vr = 0,   Γ^λ_va = 0,                         {#eq:s13-chris}

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

(a) The subprincipal operator of □_(g_(b_0)) on half-densities by |dg| is −i∇^(π*T*)_(H_G) ([[prop:np-10-17]] (i)).

(b) The trapped set in the future characteristic set is {r² = 2m_0, ξ = 0}; at the value 1 of the semiclassical
parameter it is {r² = 2m_0, ξ = 0, C = 4m_0}, C = r²|η|² the Casimir of 𝕊³, with expansion rates ±ν,
ν = 4(2m_0)^(−1/2), {φ_u, φ_s} = ν/f > 0, dG_1 ≠ 0, and β_0 = 1/f(r_ph) = 2 ([[prop:np-10-17]] (ii),
[[prop:np-10-19]] (ii)).

(c) On the characteristic set, the frame e_0 = ζ, e_1 = r(ζ_(1)w^(0) + ζ_(0)w^(1)),
e_2 = ½r²(ζ_(0)w^(0) + ζ_(1)w^(1) − η), with w^(0) = f^(1/2)dt and w^(1) = f^(−1/2)dr, has Gram matrix CJ,
J = ((0, 0, −1), (0, 1, 0), (−1, 0, 0)), and ∇_(H_G)e_0 = 0, ∇_(H_G)e_1 = −2σe_0, ∇_(H_G)e_2 = −2σe_1; an angular
covector is orthogonal to all three if and only if it is orthogonal to η ([[prop:np-10-17]] (iii)–(iv)).

(d) In the inner product diag(1, ϵ_1⁻¹, ϵ_1⁻²) on span{e_0, e_1, e_2}/C^(1/2), the endomorphism p_1 = −½(M + M*), M
the connection matrix of (c), has spectrum 0, ±(2ϵ_1)^(1/2) ([[prop:np-10-17]] (v), [[prop:np-10-19]] (iii)).

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
M_t = M_r = 0 by the formulas above; and the angular component of δdA, which by the same computation is
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

**Lemma {#lem:iii-d-7-1}** (tf-admissibility; [Hin26, Lemma 6.8] in dimension 4 + 1.) There is ϵ > 0 such that for
e_Υ ∈ [0, ϵ), |γ_Υ| < ϵ, every γ_(Υ,H) and every b ∈ ℬ, (□^Υ_b)^ is tf-admissible ([[def:i-c-5-1]]) with every
weight in the indicial gap (0, ι^Υ_(s1,2)) of [[lem:iii-d-4-1]] (with (0, 2) when e_Υγ_Υ² = 0).

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
way. So (□̄^Υ)^ is tf-admissible with weight 1, and by [[cor:i-c-5-2]] (c) with every weight in the gap. The condition
e_Υ ≥ 0 makes z ≥ 0, so that [[lem:iii-d-4-1]] describes the gap. ∎

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

    ℓ(v) := ∫_X g⁻¹(v, ω*) |dg_X| = r_h³ ∫_(𝕊³) v(∂_(t_*))|_(r=r_h) dx̂,                                    {#eq:iii-d1-1-1}

where |dg| = |dt_*| ⊗ |dg_X|, so |dg_X| = r³|dr dx̂| near r_h, and g⁻¹(v, dr) = v(∇r) = v(∂_v + f∂_r) equals
v(∂_(t_*)) at r_h. ℓ is continuous on H^(s′) near the horizon sphere for s′ > ½ (the trace theorem), so on 𝒴_0 and
𝒴_σ, as s − 1 > ½. It is [Hin26]'s pairing with ω*_(0).

*The modified divergence at the horizon.* With the trace weight 2/3, E_H h := 2ι_(c♯_(Υ,H))h − (2/3)c_(Υ,H) tr_g h
([Hin26, (6.22)] with the weight 2/3), and since tr_g G_g h = −(3/2)tr_g h in dimension 5 ([[lem:iii-b-6-2]]),

    E_H G_g = 2ι_(c♯_(Υ,H)),                                                                               {#eq:iii-d1-1-2}

as [Hin26]'s E_(H⁺,1)G = 2ι_(c♯) in dimension 4 with the weight 1. The horizon part of □^Υ_b is
2γ_(Υ,H)E_H G δ*.

### Kernel and cokernel at zero energy {#sec:iii-d1-2}

Let

    W* := r⁻²dt + r_h r⁻³f⁻¹dr = r⁻²dv − dr/(r(r + r_h)).                                                  {#eq:iii-d1-2-1}

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
