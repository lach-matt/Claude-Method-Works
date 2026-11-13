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
