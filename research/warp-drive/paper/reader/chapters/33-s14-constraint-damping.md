## Constraint propagation and constraint damping {#ch:s14}

This chapter proves, in spatial dimension n = 4 and for the Myers–Perry metrics g_b with b near b₀ = (μ₀, 0), the
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
of [[sec:iii-e-3]] carry subscripts and are not to be confused with it.

### The constraint propagation operator {#sec:iii-e-1}

The parameter space 𝓑, the metrics g_b, b = (μ, A), the time function t_*, the boundary defining function ρ = |x|⁻¹
near ∂X, the bundle E (trivialised by dt_*, dx¹, …, dx⁴) and the Minkowski metric ḡ are those of [[sec:iii-d2-1]].
With the 1-form modification of [[eq:iii-b-6-2]], for v_C ∈ (0, 1), e_C, γ_C and a stationary c_C ∈ |x|⁻¹C^∞ equal to
|x|⁻¹(dt − v_C d|x|) for large |x|, put

    δ*_(g,E_C) := δ*_g + E^C_g,     E^C_g ω = γ_C (2 c_C ⊗_s ω − (2/3)(1 − e_C) g ι_(g⁻¹c_C) ω),
    □^C_b := 2 δ_(g_b) G_(g_b) δ*_(g_b,E_C),                                                                 {#eq:iii-e-1-1}

the *constraint propagation operator*; P^C_b := (□^C_b)^(0) is its zero energy operator. Here
δ*ω = ½(ω_(a;b) + ω_(b;a)), G_g = Id − ½ g tr_g, (δk)_a = −g^(bc) k_(ab;c) and a ⊗_s b = ½(a ⊗ b + b ⊗ a). The formal
adjoint of □^C_b for the fibre pairing g_b⁻¹ and the volume density |dg_b| is

    (□^C_b)* = 2 (δ*_(g_b,E_C))* G_(g_b) δ*_(g_b)                                                             {#eq:iii-e-1-2}

([Hin26, (7.11)]), as δ_g = (δ*_g)* and G_g is symmetric. On stationary sections the spectral family of (□^C_b)* at zero
energy is the formal adjoint of P^C_b for the pairing B(u, w) := ∫_X g_b⁻¹(u, w̄) |dg_b|_X|, |dg_b| = |dt_*| ⊗ |dg_b|_X|,
by the argument of [[lem:iii-d1-2-1]] (1): a cut-off θ(t_*) with ∫θ = 1, the terms with θ′ and θ″ integrating to zero.
We write (P^C_b)* for it.

**Theorem {#thm:iii-e-1-1}** (The constraint propagation operator; [Hin26, Theorem 7.1] in dimension 4 + 1.) Let
(v_C, e_C) = (1/2, 1/102400) and C_0 ∈ [3/2, 100]. Let c_C be the stationary past timelike 1-form of [[sec:iv4-0]],
which lies in ρC^∞(X̄; T*X) and equals |x|⁻¹(dt − v_C d|x|) for large |x| up to O(μ₀|x|⁻³) d|x|, and let γ_C = h⁻¹ with
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

    h² □^C_b = 2h² δ_g G_g δ*_g − i L_(g,c,e,h),     L_(g,c,e,h) = 4ih δ_g(c ⊗_s ·) + 2ihe d ι_(c♯).            {#eq:iv4-0-2}

The weight 2/3 = 2/(D − 2) is the one for which h G_g E^C ω has the form 2c ⊗_s ω − e g⟨c, ω⟩ for every e
([[prop:np-10-12]] (i)). With the weight 1, the literal transcription of the four-dimensional operator, the conclusions
below fail ([[prop:np-10-12]] (iv), [[prop:np-10-13]] (i)).

*The constants.* We fix, once for the whole stability theory,

    v_C := 1/2,     e_C := 1/102400,     C_0 ∈ [3/2, 100],     γ_C := h⁻¹,  h ∈ 𝖧,                          {#eq:iv4-0-1}

where 𝖧 := (0, h_*) ∖ 𝖹. Here h_* := min(10⁻⁶, h_0, h_tf), with h_0 the smaller of the thresholds of
[[thm:iv5-7-3]] at these (v_C, e_C) for the weights [[eq:iv4-1-2]] at C_0 and at C_0 − 1, h_tf the threshold of
[[thm:iv6-3-1]], and 𝖹 the countable set of [[lem:iv4-1-3]] (b). The nonlinear theorem of [[ch:s27]] takes C_0 = 100.
The 1-form c_C is that of [[prop:np-10-14]] at μ = 1 and r_0 = 100, smoothed near r_0/2 and 2r_0 and rescaled to μ₀
(every condition on it depends on μ r_0⁻² and r/r_0 only, by scaling). It is stationary and equals
|x|⁻¹(dt − v_C d|x|) for large |x| up to O(μ₀|x|⁻³) d|x|: [[prop:np-10-14]] states this in the static time, and the
time t of [[sec:iii-b-3-1]] is the outgoing Kerr–Schild time, whose differential differs from the static one by
O(μ₀|x|⁻²) d|x|, which changes |x|⁻¹(dt − v_C d|x|) by O(μ₀|x|⁻³) d|x|.

Every result of this chapter that names (v_C, e_C, C_0, γ_C) uses these values, and so do all later chapters. The
statements of [Hin26, Theorem 7.1] "for v_C ∈ (0, 1), C_0 > 0 and all sufficiently large γ_C" are proved here at this
choice: for every γ_C > 1/h_* outside a countable set, which is what every later use requires, as each takes one
admissible γ_C.

