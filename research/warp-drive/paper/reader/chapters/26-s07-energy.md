## Energy estimates, solvability on slabs, the black hole interior and the global estimate {#ch:s07}

This chapter proves, in spatial dimension n = 4, the results of [Hin26c, Section 8, pp. 141–157]: solvability of
forward problems on bounded time slabs, with energy estimates, on edge Sobolev spaces with and without b-regularity and
tame in it ([Hin26c, Lemma 8.1, Propositions 8.3, 8.6 and 8.9]); the same in the black hole interior, with r as the
time function ([Hin26c, Lemma 8.10, Propositions 8.11–8.13]); and the global estimate [Hin26c, Theorem 8.14], which
joins these to the microlocal estimate of [[ch:s06]]. The dimension enters through the normal form of the operator at
ℐ⁺ ([[lem:ii-e-1-1]]) and through the current of the multiplier ([[lem:ii-e-2-4]]); the threshold α < −1/2 + p̄_1 is
the same as in dimension 3 + 1.

The energy estimates are proved with a vector field multiplier. Near ℐ⁺ the multiplier is a weighted edge vector field
whose deformation tensor is positive in the time derivative only through the threshold of the weight; the other
derivatives come from an exponential weight in time. Every first-order term of the operator is kept as a pointwise
quadratic form in the first derivatives, and every zeroth-order term is absorbed by a Poincaré inequality with the
exponential weight. So the fibre inner product need only make Re p_1 large; it need not also make Im p_1 and p_0 small,
as [Hin26c, (8.4)] asks. Solvability at all orders follows from the energy estimates for P and for its adjoint, by
duality, and from microlocal regularity on slabs. That regularity needs the radial estimates at the outgoing radial set
over ℐ⁺, localised in time, for P and for P*. [Hin26c] takes the first from its Proposition 7.9 with a finite final
time, whose proof uses H_G t_* ≥ 0 on the support of the commutant, and this fails off the characteristic set (the
paragraph after [[prop:ii-d-3-6]]); the second it leaves to the reader. [[sec:ii-e-3-1]] proves both, with a time
cut-off in the function t_* − κ x_I^(2ℓ_I), which is monotone along the flow on a full neighbourhood of the radial set
up to a multiple of the principal symbol.

*Organisation.* [[sec:ii-e-1]]: slabs and spaces, the operator near ℐ⁺, extensions of the operator, duality.
[[sec:ii-e-2]]: the energy estimates. [[sec:ii-e-3]]: the localised radial estimates, regularity on slabs,
solvability. [[sec:ii-e-4]]: b-regularity and the tame estimates. [[sec:ii-e-5]]: the black hole interior.
[[sec:ii-e-6]]: the global estimate.

*Standing notation.* The notation is that of [[ch:s04]], [[ch:s05]] and [[ch:s06]]: the compactified spacetime M with
its faces ι⁺, ℐ⁺ and K⁺; the b-, e3b- and eb-structures; the spaces H^((𝗌;k),(2α_I,α_+,α_K))_(e3b;b) of
[[eq:ii-a-8-1]], with their supported and extendible versions ([[sec:ii-a-7]]); the model operator P_0, the quantity
p̄_1 of [[def:ii-c-3-5]], the time function t^♭_* and the domains Ω and Ω_* of [[lem:ii-c-3-2]]; and the radial
estimates of [[sec:ii-d-3]]. An estimate holds *in the strong sense* if, whenever its right side is finite, so is its
left side, and the estimate holds. The operators act on sections of the trivial bundle of [[sec:i-a-1]]; b-vector
fields act on them componentwise, and a fibre inner product is a smooth family of Hermitian inner products on the fibre.
The radii r_0 − 2δ_0 < r_0 < r_2 < r_h are those of [[sec:i-a-1]]. They are parameters: every constant chosen below from
them is chosen by an inequality that a smaller inner radius r_0 does not make harder to satisfy (for instance the bound
(ε_ι δ)⁻¹ > r_h + 1 in [[sec:ii-e-3-2]]), so every result of this chapter holds at every inner radius r_0 for which the
hypotheses of [[sec:i-a-1]], [[sec:i-b-1-2]] and [[sec:ii-b-1-1]] hold.

### Setting {#sec:ii-e-1}

#### Slabs and spaces {#sec:ii-e-1-1}

Ω, Ω_* = cl_M{t^♭_* ≥ 1} and the time function t^♭_* are those of [[lem:ii-c-3-2]]; below t^♭ := t^♭_*, and t_* = t − r
is the coordinate of [[def:ii-a-1-3]]. P is weakly admissible of class ((d_0;k),(2ℓ_I,ℓ_+,ℓ_K)) relative to P_0
([[def:ii-c-3-3]]), with

    ε_P := ‖P − P_0‖_((d_0;0),(2ℓ_I,ℓ_+,ℓ_K))

small, so that the metric g of P satisfies the hypotheses of [[lem:ii-c-3-2]]: dt^♭ is past timelike on Ω°, and dr is
future timelike on {r_0 ≤ r ≤ r^♮}, where r^♮ = (r_0 + r_2)/2. For 1 ≤ T_0 < T_1 < ∞ the **slab** is

    Ω_(T_0,T_1) := Ω_* ∩ {T_0 ≤ t^♭ ≤ T_1}.

For 1 − η_0 ≤ T_0 < 1 the slab is defined in the same way in the region Ω⁻_* of [[lem:ii-e-1-2]] (iv), with P^ext in
place of P. In M° its boundary consists of the *initial face* {t^♭ = T_0} and the *final faces* {t^♭ = T_1} and
{r = r_0}, which are spacelike: their conormals dt^♭ and dr are timelike, and future directed causal vectors point out of
the slab at the final faces and into it at the initial face. Its closure meets ∂M only in ℐ⁺ ∩ {T_0 ≤ t_* ≤ T_1}, as
t^♭ = t_* on ℐ⁺ ([[lem:ii-c-3-2]] (a)).

Near ℐ⁺ at finite times we use (t_*, x_I, ω) with x_I := r^(−1/2) ([[def:ii-a-1-3]] (B)); it differs from the
x_I = (t_*/r)^(1/2) of [[sec:ii-b-7]] by the factor t_*^(1/2), which is smooth and positive at finite times. The edge
vector fields are spanned by ∂_(t_*), x_I∂_(x_I) and x_I∂_ω, and the b-vector fields by ∂_(t_*), x_I∂_(x_I) and ∂_ω; at
finite times the e3b- and eb-structures are the edge structure, and ρ_+, ρ_K are smooth and positive. We write

    H^(𝗌,2α)_e := H^(𝗌,(2α,0,0))_(e3b),        H^((𝗌;k),2α)_(e;b) := H^((𝗌;k),(2α,0,0))_(e3b;b)

([[sec:ii-a-4]] and [[eq:ii-a-8-1]]), with the L²-density |dg|. Near ℐ⁺, |dg| is a smooth positive multiple of
r³|dt_* dr dω| = 2x_I^(−8)|dt_* (dx_I/x_I) dω|.

For a slab Ω′ = Ω_(T_0,T_1) put

    U′ := Ω° ∩ {t^♭ < T_1, r > r_0},     V′ := Ω° ∩ {t^♭ > T_0},     F′ := Ω ∩ {t^♭ ≤ T_1, r ≥ r_0},

and define, with quotient norms,

    H^(𝗌,2α)(Ω′)^(•,−) := {u|_(U′) : u ∈ H^(𝗌,2α)_e, supp u ⊂ {t^♭ ≥ T_0}},
    H^(𝗌,2α)(Ω′)^(−,•) := {v|_(V′) : v ∈ H^(𝗌,2α)_e, supp v ⊂ F′},

and H^((𝗌;k),2α)(Ω′)^(•,−), H^((𝗌;k),2α)(Ω′)^(−,•) likewise. The first are distributions supported at the initial face
and extendible at the final ones, the spaces of forward problems; the second the reverse, the spaces of backward
problems. We call D(Ω′) the set of restrictions to U′ of functions in C_c^∞(M°) supported in {t^♭ > T_0}, and D_*(Ω′)
the set of restrictions to V′ of functions in C_c^∞(M°) supported in {t^♭ < T_1, r > r_0}.

#### The operator near ℐ⁺ {#sec:ii-e-1-2}

**Lemma {#lem:ii-e-1-1}** (The normal form near ℐ⁺.) Near ℐ⁺ at finite times, in (t_*, x_I = r^(−1/2), ω),

    P − (1/2) x_I² [−2(x_I∂_(x_I) − 3 − 2p_1)∂_(t_*) + 2x_I² Δ_(𝕊³) + t_*⁻¹ p_0]
        ∈ x_I² C^((d_0;k),2ℓ_I)_(e;b) Diff²_e,                                                         {#eq:ii-e-1-1}

with p_0, p_1 of [[def:ii-c-3-3]] and Δ_(𝕊³) ≥ 0 the Laplacian of the round sphere. Hence, for covectors
ζ = ζ_(t_*) dt_* + ξ dx_I/x_I + η, G(ζ) ≡ x_I²(ξ ζ_(t_*) + x_I²|η|²) modulo x_I^(2+2ℓ_I) times a quadratic form in
(ζ_(t_*), ξ, x_I η); that is, g⁻¹ ≡ x_I²(x_I∂_(x_I) ⊗_s ∂_(t_*) + x_I² g̸⁻¹), with a ⊗_s b := (a ⊗ b + b ⊗ a)/2 and g̸
the round metric.

This is [Hin26c, (8.3)] in dimension 4 + 1.

*Proof.* In the coordinates ρ_+ = t_*⁻¹, x′_I := (t_*/r)^(1/2) = t_*^(1/2) x_I of [[lem:ii-c-3-4]], x′_I∂_(x′_I) at
fixed ρ_+ is −2r∂_r = x_I∂_(x_I) at fixed t_*, and x′_I∂_(x′_I) − 2ρ_+∂_(ρ_+) = 2t_*∂_(t_*) at fixed r. As
x′_I^(−2) ρ_+^(−2) = t_* x_I^(−2) and x′_I² = t_* x_I², [[eq:ii-c-3-3]] reads

    2t_* x_I^(−2) P ≡ −2t_*(x_I∂_(x_I) − 3 − 2p_1)∂_(t_*) + 2t_* x_I² Δ_(𝕊³) + p_0,

as t_* commutes with x_I∂_(x_I) and with multiplication by p_1. Multiply by x_I²/(2t_*); the remainder class becomes
x_I² C^((d_0;k),2ℓ_I)_(e;b) Diff²_e, t_* being bounded above and below. For the principal symbol,
σ(x_I∂_(x_I)) = iξ and σ(∂_(t_*)) = iζ_(t_*). As a check of the signs: for Minkowski space, with
□ = −∂_t² + ∂_r² + (3/r)∂_r + r⁻² Δ_lap and ∂_r|_t = ∂_r|_(t_*) − ∂_(t_*), ∂_r|_(t_*) = −(1/2) x_I² x_I∂_(x_I), one
finds

    −□ = x_I² (−(x_I∂_(x_I) − 3)∂_(t_*) − x_I² Δ_lap) + O(x_I⁴) Diff²_e,

which is [[eq:ii-e-1-1]] with p_0 = p_1 = 0 and Δ_(𝕊³) = −Δ_lap. ∎

In dimension 3 + 1 the bracket of [[eq:ii-e-1-1]] reads −2(x_I∂_(x_I) − 2(1 + p_1))∂_(t_*) + 2x_I² Δ̸ + p_0
[Hin26c, (8.3)]: the constant 3 = n − 1 here is 2 there, and p_0 stands where the normal form gives t_*⁻¹p_0. At bounded
times t_*⁻¹ is a bounded positive factor, and zeroth-order terms are absorbed by the Poincaré inequality
([[lem:ii-e-2-3]]), so nothing below depends on it.

#### The fibre inner product {#sec:ii-e-1-3}

Let δ′ > 0. As in the proof of [[prop:ii-d-3-6]] there is a smooth fibre inner product h_I = ⟨A_I⁻¹·, A_I⁻¹·⟩ over a
neighbourhood of cl(ℐ⁺ ∩ Ω), extended independently of x_I, with

    Re_(h_I) p_1 ≥ p̄_1 − δ′     on cl(ℐ⁺ ∩ Ω).                                                     {#eq:ii-e-1-2}

[Hin26c, (8.4)] asks in addition |Im_h p_1| < ε and ‖p_0‖_h < ε. That is not needed below: in [[lem:ii-e-2-5]] every
first-order term other than the one carrying p_1 is kept as a quadratic form in the edge derivatives and absorbed by the
exponential weight in time, and p_0 by the Poincaré inequality, so only [[eq:ii-e-1-2]] is used.

#### Extensions of the operator {#sec:ii-e-1-4}

The microlocal estimates of [[sec:ii-e-3]] are applied on a neighbourhood of a slab, beyond its final faces, and, for
T_0 = 1, below its initial face, where P is not given.

**Lemma {#lem:ii-e-1-2}** (Extension; [Hin26c, Lemma 8.5 and the paragraph after it].) There are r^♯ ∈ (r_0 − δ_0, r_0)
and an operator P^ext on {r ≥ r^♯} ∩ {t_* ≥ 1/2} such that:

(i) P^ext = P on Ω;

(ii) P^ext − P_0 has coefficients bounded in the norms of P − P_0, in C^((d_0;k)) with the weights of [[def:ii-c-3-3]],
by a constant times those of P − P_0;

(iii) near ℐ⁺, P^ext has the form [[eq:ii-e-1-1]] with the data p_0, p̃_1 extended to t_* ∈ [1/2, 1], and
[[eq:ii-e-1-2]] holds for t_* ∈ [1 − η_0, 1] with 2δ′ in place of δ′, for some η_0 > 0;

(iv) t^♭ extends to {r ≥ r^♯, t_* ≥ 1/2}, and for ε_P small there is δ_♮ > 0 such that, after shrinking η_0: dt^♭ is
past timelike for the metric of P^ext on the region Ω⁻_*, the union of {t^♭ ≥ 1, r ≥ r^♯} and of the collar
{1 − η_0 ≤ t^♭ ≤ 1} below its face {t^♭ = 1} (in the collar coordinates of [[sec:ii-e-1-5]]), which lies in
{t_* > 1/2}; and dr is future timelike on Ω⁻_* ∩ {r^♯ ≤ r ≤ r^♮ + δ_♮}.

*Proof.* Write P_0 and P − P_0 in a fixed frame as sums of coefficients times fixed operators Id, ∂_(z^μ),
∂_(z^μ)∂_(z^ν), z = (t_*, x), as in the paragraph after [Hin26c, Lemma 8.5]; those of P_0 are independent of t_*.
Extend each coefficient across {r = r_0} by Seeley's extension operator E_0 (see the proof of [[lem:ii-e-1-3]] (b)) in
the variable r − r_0, with (t_*, ω) as parameters, and across {t_* = 1} by E_0 in t_*, with (r, ω), resp. (x_I, ω) near
ℐ⁺, as parameters. Seeley's operator preserves C^((d_0;k))-regularity and weights in the parameters, which gives (ii),
and acts on the data p_0, p̃_1 of [[eq:ii-c-3-1]]–[[eq:ii-c-3-2]] in [[def:ii-c-3-3]] in the same way, which gives the
form in (iii). The extended p_1 is continuous in t_* and equals p_1 at t_* = 1, so [[eq:ii-e-1-2]] persists with 2δ′ on
[1 − η_0, 1]. The extension of P_0 in r keeps it stationary.

(iv) t^♭ is not extended by E_0: Seeley's extension of a function is not given by the function's own formula, which is
what is used below. On {t_* ≥ 1/2} it is defined by the gluing formulae of the proof of [[lem:ii-c-3-2]], with the
constant C there taken ≥ 4(r′_0 + 1), so that the overlap {r′_0 + 1 ≤ r ≤ C t_*/2} of the regions being glued is
non-empty for every t_* ≥ 1/2; the formulae make sense for t_* > 0. In particular t^♭ = t_*(1 − (t_*/r)^(ℓ_I)) near ℐ⁺
([[lem:ii-c-3-2]] (a)) and t^♭ = C′(t_* + r′_0) for r ≤ r′_0 − 1 ([[lem:ii-c-3-2]] (c)), on all of {t_* ≥ 1/2}.

*dr.* By [[lem:ii-c-3-2]] (1) with h = 0, dr is future timelike for g_0 on {r_0 ≤ r ≤ r^♮}; g_0 is stationary and the
range of x is compact, so by continuity this holds on {r^♯ ≤ r ≤ r^♮ + δ_♮} for r^♯ close to r_0 and δ_♮ small, and for
the extended metric, which differs from g_0 by O(ε_P) there.

*dt^♭.* For r ≤ r′_0 − 1, dt^♭ = C′dt_*, and dt_* is past timelike for g_0 there (by hypothesis (H6) of
[[sec:i-b-1-2]], as in the proof of [[lem:ii-c-3-2]]), hence for the extended metric, by stationarity and continuity
down to r^♯. Near ℐ⁺ the proof of [[lem:ii-c-3-2]] bounds g⁻¹ − ḡ⁻¹ in the basis used there by
C(ε_P + ρ_I^(1−ℓ_I)) ρ_I^(ℓ_I), using ρ_+ ≤ 1 only to bound powers of ρ_+; for t_* ≥ 1/2, ρ_+ ≤ 2, and the argument
applies with larger constants. On the rest of {t^♭ ≤ T}, namely {x_I ≥ c, r ≥ r′_0 − 1}, which is compact at bounded
t_* (and t_* ≤ T/C′ on {t^♭ ≤ T} ∩ Ω by [[lem:ii-c-3-2]] (b)), dt^♭ is past timelike on Ω_* with a margin, hence on a
neighbourhood, by continuity.

*The collar.* Near the face {t^♭ = 1}, which lies in {t_* ≥ 1} by [[lem:ii-c-3-2]] (b), dt^♭ is past timelike, so the
field Z/(−Z t^♭) of [[sec:ii-e-1-5]] is defined there; its flow from the face for times at most η_0 sweeps the collar,
which for η_0 small lies in the neighbourhood just obtained and in {t_* > 1/2}: near ℐ⁺ the flow is translation in t_*
by at most 2η_0, and elsewhere at bounded times it stays in a compact set. ∎

#### Duality {#sec:ii-e-1-5}

*A collar.* There is a vector field Z on a neighbourhood of Ω⁻_* ∩ {t^♭ ≤ T_1 + 2}, an edge vector field, equal to
−∂_(t_*) near ℐ⁺, with Z t^♭ ≤ −c < 0 and, near {r = r_0}, Z r ≥ c. Take Z := −χ_I ∂_(t_*) + (1 − χ_I)∇t^♭, with
χ_I = χ_I(r) equal to 1 for r ≥ R and to 0 for r ≤ R − 1, R large. Near ℐ⁺,
∂_(t_*) t^♭ = 1 − (1 + ℓ_I)(t_*/r)^(ℓ_I) ≥ 1/2 by [[lem:ii-c-3-2]] (a). On {r ≤ R}, ∇t^♭ is past timelike
([[lem:ii-c-3-2]] (2) and [[lem:ii-e-1-2]] (iv)), so Z t^♭ = g⁻¹(dt^♭, dt^♭) < 0 there, with a negative bound on the
compact part at bounded times, and (∇t^♭) r = g⁻¹(dt^♭, dr) > 0 near r = r_0, dr being future timelike. Near ℐ⁺ the
flow Φ_τ of Z is translation in t_*, which preserves the edge structure, the weight and the density; elsewhere it is a
smooth flow on a compact set. So (Φ_τ)_* is bounded on H^(m,2α)_e, m ∈ ℕ_0, uniformly for |τ| ≤ τ_0, and strongly
continuous at τ = 0, by the chain rule and the density of C_c^∞.

As Z and Φ_τ are defined only near Ω⁻_* ∩ {t^♭ ≤ T_1 + 2}, in [[lem:ii-e-1-3]] below (Φ_(±τ))_* is applied only after
multiplication by a cut-off χ_Z, a function of t^♭ equal to 1 on {T_0 − η_0/4 ≤ t^♭ ≤ T_1 + 1} and supported in
{T_0 − η_0/2 ≤ t^♭ ≤ T_1 + 2} (there T_0 ≥ 1 − η_0/2). This changes neither the pairings, as the supports of the two
factors meet only where χ_Z = 1, nor the restrictions to U′ and V′. The level sets of t^♭ near {t^♭ = T}, with the flow
lines of Z/(−Z t^♭), give collar coordinates (t^♭, y) in which Z/(−Z t^♭) = −∂_(t^♭); near ℐ⁺, y = (x_I, ω), and in
(t^♭, x_I, ω) the edge vector fields are spanned by ∂_(t^♭), x_I∂_(x_I) and x_I∂_ω, as
t^♭ − t_* = −t_*^(1+ℓ_I) x_I^(2ℓ_I) has bounded edge derivatives.

**Lemma {#lem:ii-e-1-3}** (Pairing, duality and density.) Let Ω′ = Ω_(T_0,T_1) with T_0 ≥ 1 − η_0/2, α ∈ ℝ and
m ∈ ℤ; the weights are 2α on u and −2α on v.

(a) (*Separation.*) Let u ∈ H^(m,2α)_e and v ∈ H^(−m,−2α)_e with supp u ⊂ {t^♭ ≥ T_0}. If supp v ⊂ {t^♭ ≤ T_0}, or if
supp v ⊂ F′ and u|_(U′) = 0, then ⟨u, v⟩ = 0. Hence the pairing of u|_(U′) ∈ H^(m,2α)(Ω′)^(•,−) with
v|_(V′) ∈ H^(−m,−2α)(Ω′)^(−,•), taken with extensions supported in {t^♭ ≥ T_0}, resp. F′, is well defined, and
bounded by C times the product of the quotient norms.

(b) (*Duality.*) If m ≥ 0, every bounded functional Λ on H^(m,2α)(Ω′)^(−,•) is Λ = ⟨·, u⟩ for some
u ∈ H^(−m,−2α)(Ω′)^(•,−) with ‖u‖ ≤ C‖Λ‖.

(c) (*Density.*) If m ≥ 0, D(Ω′) is dense in H^(m,2α)(Ω′)^(•,−) and D_*(Ω′) is dense in H^(m,2α)(Ω′)^(−,•); likewise
for the mixed spaces of order (m;k).

*Proof.* (a) The pairing is that of [[lem:ii-a-7-1]], bounded on H^m × H^(−m). In the first case, (Φ_(−τ))_* u is
supported in {t^♭ ≥ T_0 + cτ} for τ > 0 small, as −Z increases t^♭, so ⟨(Φ_(−τ))_* u, v⟩ = 0, and
(Φ_(−τ))_* u → u in H^(m,2α)_e as τ ↓ 0 (for m < 0, (Φ_τ)_* is the transpose of (Φ_(−τ))_* on H^(−m), bounded
uniformly, and converges on the dense set C_c^∞). In the second case, (Φ_τ)_* v is supported, within
{t^♭ ≥ T_0 − η_0/2}, in U′, as Z points into F′ across {t^♭ = T_1} and {r = r_0} there; u vanishes on U′ and on
{t^♭ < T_0}, so ⟨u, (Φ_τ)_* v⟩ = 0, and τ ↓ 0 gives the claim. For the pairing, two extensions of u|_(U′) supported
in {t^♭ ≥ T_0} differ by an element vanishing on U′, and two extensions of v|_(V′) supported in F′ by an element
supported in {t^♭ ≤ T_0}; the bound follows by taking minimal extensions.

(b) Let E_0 be Seeley's extension operator across {t^♭ = T_0}, as in [Hin26c, Lemma 8.5], in the collar coordinates:
E_0 w := w on {t^♭ > T_0} and

    (E_0 w)(T_0 − τ, y) := Σ_(l≥0) c_l (χ w)(T_0 + τ/ε_l, y)     for τ > 0,

where ε_l = 3^(−l), sin(πs/2) = Σ_l c_l s^l (so that Σ_l |c_l| ε_l^(−j) < ∞ and Σ_l c_l ε_l^(−j) = (−1)^j for all
j ∈ ℕ_0), and χ = χ(t^♭ − T_0) is a cut-off equal to 1 near 0 and supported in [0, η_0/2). It maps H̄^(m,2α)(V′)
boundedly into H^(m,2α)_e: the reflection acts in t^♭ only, commutes with x_I∂_(x_I) and x_I∂_ω in the collar
coordinates near ℐ⁺, matches all t^♭-derivatives at t^♭ = T_0, and after j derivatives in t^♭ is bounded on L² by
Σ_l |c_l| ε_l^(1/2−j). E_0 w is supported in {t^♭ > T_0 − η_0/2}, within Ω⁻_*. It preserves support in F′: on a
collar line r increases as t^♭ decreases (near {r = r_0}, as Z r > 0 there), so if (T_0 − τ, y) has r < r_0, so has
(T_0 + τ/ε_l, y). Hence on H^(m,2α)(Ω′)^(−,•) the quotient norm and the norm of H̄^(m,2α)(V′) are equivalent. Given Λ,
extend it by the Hahn–Banach theorem to H̄^(m,2α)(V′) with comparable norm. By [[lem:ii-a-7-3]] and its proof (the case
of functionals on extendible spaces), there is ũ ∈ Ḣ^(−m,−2α)(V̄′), ‖ũ‖ ≤ C‖Λ‖, with Λ(y) = ⟨ỹ, ũ⟩ for every
extension ỹ ∈ H^(m,2α)_e of y. Take ỹ supported in F′; then u := ũ|_(U′) represents Λ in the pairing of (a).

(c) Given v supported in F′, (Φ_τ)_* v → v as τ ↓ 0, and for small τ > 0 its part in {t^♭ > T_0 − η_0/2} is
supported in {t^♭ < T_1, r > r_0}; the part in {t^♭ ≤ T_0 − η_0/2} does not affect the restriction to V′. Then
multiply by 1 − χ_0(x_I/δ), χ_0 a cut-off equal to 1 near 0, which converges strongly to the identity as δ → 0 (by
dominated convergence; the derivatives (x_I∂_(x_I))^j (x_I∂_ω)^β ∂_(t_*)^i of χ_0(x_I/δ) are bounded uniformly in δ),
and mollify on the resulting compact set. For D(Ω′) use Φ_(−τ), which moves supports into {t^♭ > T_0}. For the mixed
spaces the same holds, as the operations commute with b-vector fields up to terms bounded on these spaces. ∎

The equivalence of the quotient norm on H^(m,2α)(Ω′)^(−,•) with the norm on the slab, proved in (b), is what the
duality step of [Hin26c, Proposition 8.3] uses.

### Energy estimates {#sec:ii-e-2}

#### Three identities {#sec:ii-e-2-1}

For a C¹ Lorentzian metric g, a real C¹ vector field X and real covectors ζ put

    K_X(ζ) := (1/2) (H_G(ζ(X)) − (div_g X) G(ζ)),        T(V,W)(ζ) := ζ(V) ζ(W) − (1/2) g(V,W) G(ζ),

with G(ζ) = g⁻¹(ζ, ζ). For u with values in the fibre, K_X(du) and T(V,W)(du) are the corresponding Hermitian forms in
du (sums over the real and imaginary parts of the components in a unitary frame). In coordinates
K_X(ζ) = (∇_μ X_ν) ζ^μ ζ^ν − (1/2)(div_g X) G(ζ), as

    H_G(X^ν ζ_ν) = 2 g^(μλ) ζ_λ (∂_μ X^ν) ζ_ν − (∂_κ g^(μν)) X^κ ζ_μ ζ_ν,
    2 ζ^μ ζ_ν Γ^ν_(μκ) = ζ^μ ζ^λ ∂_κ g_(λμ) = −(∂_κ g^(μν)) ζ_μ ζ_ν.

P_□ := −□_g acts componentwise; σ_2(P_□) = G.

**Lemma {#lem:ii-e-2-1}** (Energy identity.) Let O be a region whose boundary in M° consists of finitely many C¹
hypersurfaces {φ_j = 0} meeting transversally, with O = {φ_j > 0 for all j} near them, and let X be a real C¹ vector
field. For u ∈ C²(Ō) with values in the fibre and with compact support in Ō,

    2 Re ∫_O ⟨P_□ u, Xu⟩ |dg| = ∫_O 2K_X(du) |dg| + Σ_j ∫ 2T(X, ∇φ_j)(du) δ(φ_j) |dg|.                {#eq:ii-e-2-1}

For f ∈ C¹ real, K_(fX) = f K_X + 2T(X, (1/2)∇f), that is,
K_(fX)(ζ) = f K_X(ζ) + ζ(X) g⁻¹(df, ζ) − (1/2)(Xf) G(ζ).

*Proof.* For a real component a of u, with J := −(Xa)∇a + (1/2) G(da) X,

    div J = −(Xa) □a − (∇_μ X_ν) ∇^μ a ∇^ν a − (1/2) X(G(da)) + (1/2) X(G(da)) + (1/2)(div X) G(da),

using ∇^μ a ∇_μ(X^ν ∇_ν a) = (∇_μ X_ν) ∇^μ a ∇^ν a + (1/2) X(G(da)). So (−□a)(Xa) = div J + K_X(da). Integrate over O:
∫ div(1_O J) |dg| = 0 and div(1_O J) = 1_O div J + Σ_j δ(φ_j) J(dφ_j) (the divergence theorem on the Lipschitz domain
O), and −J(dφ_j) = (Xa) da(∇φ_j) − (1/2)(Xφ_j) G(da) = T(X, ∇φ_j)(da). Sum over the real and imaginary parts of all
components. The formula for K_(fX) follows from H_G(f ζ(X)) = f H_G(ζ(X)) + ζ(X) H_G f, H_G f = 2g⁻¹(df, ζ) and
div(fX) = f div X + Xf. ∎

**Lemma {#lem:ii-e-2-2}** (Dominant energy.) If V and W are both future causal, or both past causal, then
T(V,W)(ζ) ≥ 0 for all real ζ. If V is timelike, T(V,V)(ζ) ≥ c|ζ|² with c > 0 depending continuously on V and on a
Riemannian norm.

*Proof.* T is bilinear in (V, W), so the past case follows from the future one. Let Z := ζ^♯ and
Y := g(Z,V) Z − (1/2) g(Z,Z) V. Then T(V,W)(ζ) = g(Y,W), g(Y,Y) = (1/4) g(Z,Z)² g(V,V) ≤ 0, and
g(Y,V) = T(V,V)(ζ). In an orthonormal frame with V a positive multiple of e_0 (if V is timelike),
T(V,V)(ζ) = (1/2)|V|²(Z_0² + |Z_⊥|²), which is the second claim; if V is null, T(V,V)(ζ) = g(Z,V)² ≥ 0. So Y is causal
or zero, with g(Y,V) ≥ 0, hence past causal or zero, and g(Y,W) ≥ 0 for W future causal. In the remaining case,
g(Y,V) = 0 with V null, g(Z,V)² = T(V,V)(ζ) = 0, so Y = −(1/2) g(Z,Z) V; and Z ⊥ V with V null forces Z spacelike or
parallel to V, so g(Z,Z) ≥ 0, and Y is a non-positive multiple of V, again past causal or zero. ∎

**Lemma {#lem:ii-e-2-3}** (Poincaré inequality with an exponential weight.) Let O be as in [[lem:ii-e-2-1]], Y a C¹
vector field and τ a C¹ function with Yτ = 1 and |div_g Y| ≤ C_0 on O, w > 0 a C¹ weight with |Y log w| ≤ C_1, and
Φ ≥ C_0 + C_1. Let u ∈ C¹(Ō) have compact support in Ō and vanish near the part of every boundary face {φ_j = 0} where
Yφ_j > 0. Then

    ∫_O e^(−2Φτ) w |u|² |dg| ≤ 4Φ⁻² ∫_O e^(−2Φτ) w |Yu|² |dg|.                                     {#eq:ii-e-2-2}

*Proof.* With Y_Φ := e^(−2Φτ) w Y,

    div(|u|² Y_Φ) = e^(−2Φτ) w Y|u|² + e^(−2Φτ) w (div Y + Y log w − 2Φ) |u|².

Integrating as in [[lem:ii-e-2-1]], ∫_O div(|u|² Y_Φ) |dg| = −Σ_j ∫ δ(φ_j) |u|² Y_Φ φ_j |dg| ≥ 0, as u = 0 near the
faces with Yφ_j > 0. With |Y|u|²| ≤ 2|u||Yu| and the Cauchy–Schwarz inequality,

    (2Φ − C_0 − C_1) ∫ e^(−2Φτ) w |u|² ≤ 2 (∫ e^(−2Φτ) w |u|²)^(1/2) (∫ e^(−2Φτ) w |Yu|²)^(1/2),

which gives [[eq:ii-e-2-2]], as 2Φ − C_0 − C_1 ≥ Φ. ∎

With Y replaced by −Y and τ by −τ this is the inequality for the reverse direction:
∫ e^(2Φτ) w |u|² ≤ 4Φ⁻² ∫ e^(2Φτ) w |Yu|² when u vanishes near the faces with Yφ_j < 0.

#### The multiplier near ℐ⁺ {#sec:ii-e-2-2}

Near ℐ⁺ at finite times put, for β ∈ ℝ,

    X_0^(β) := x_I^(−4β−2) (∂_(t_*) − x_I∂_(x_I)) = r^(2β+1) (∂_(t_*) + 2r∂_r).

For covectors write ζ = ζ_(t_*) dt_* + ξ dx_I/x_I + η and η̂ := x_I η, so that ζ(∂_(t_*)), ζ(x_I∂_(x_I)) and η̂ are the
components of ζ on the edge frame, and |η̂|² = x_I² |η|²_(g̸).

**Lemma {#lem:ii-e-2-4}** (The current of the multiplier.) For the Minkowski metric ḡ = −dt_*² − 2dt_* dr + r² g̸,

    K_(X_0^(β))(ζ) = x_I^(−4β) [−(2β+1) ζ_(t_*)² − 3 ζ_(t_*) ξ − (2β+3)|η̂|²
                                 + x_I² ((2β−1)/4 · ξ² − (2β+1)/2 · ζ_(t_*) ξ)],
    T(X_0^(β), −∇t_*)(ζ) = (1/2) x_I^(−4β) (ξ² + |η̂|² + (1/4) x_I² ξ²).

For the metric g of P, the two sides change by x_I^(−4β) O(x_I^(2ℓ_I)) (ζ_(t_*)² + ξ² + |η̂|²), uniformly for ε_P ≤ 1,
with d_0 ≥ 2.

This is [Hin26c, (8.10)] in dimension 4 + 1. In dimension 3 + 1 the cross term −3ζ_(t_*)ξ is −2ζ_(t_*)ξ and the angular
coefficient −(2β+3) is −2(β+1); the coefficient −(2β+1) of ζ_(t_*)², which carries the threshold, is the same in both
dimensions, so the threshold of [[lem:ii-e-2-5]] is the same as there. The cross term is absorbed whatever its size.

*Proof.* With ⊗_s as in [[lem:ii-e-1-1]], ḡ⁻¹ = −2 ∂_(t_*) ⊗_s ∂_r + ∂_r ⊗ ∂_r + r⁻² g̸⁻¹, so in (t_*, r, ω)

    G(ζ) = −2 ζ_(t_*) ζ_r + ζ_r² + r⁻² |η|²,

and div_ḡ Y = r⁻³ ∂_μ(r³ Y^μ) for Y = Y^(t_*) ∂_(t_*) + Y^r ∂_r. Put c := 2β + 1 and X := r^c (∂_(t_*) + 2r∂_r). Then
ζ(X) = r^c (ζ_(t_*) + 2r ζ_r), which does not depend on t_*, ω or η, so

    H_G(ζ(X)) = ∂_(ζ_r)G · ∂_r(ζ(X)) − ∂_r G · ∂_(ζ_r)(ζ(X)),

with ∂_(ζ_r)G = −2ζ_(t_*) + 2ζ_r, ∂_r G = −2r⁻³|η|², ∂_r(ζ(X)) = r^(c−1)(c ζ_(t_*) + 2(c+1) r ζ_r) and
∂_(ζ_r)(ζ(X)) = 2r^(c+1); and div X = r⁻³ ∂_r(2r^(c+4)) = 2(c+4) r^c. So

    2K_X = r^(c−1) [(−2ζ_(t_*) + 2ζ_r)(c ζ_(t_*) + 2(c+1) r ζ_r) + 4r⁻¹|η|²]
           − 2(c+4) r^c (−2ζ_(t_*) ζ_r + ζ_r² + r⁻² |η|²).

Insert ζ_r = −ξ/(2r) (as dr = −2r dx_I/x_I) and |η|² = r|η̂|², and use r^(c−1) = x_I^(−4β) and r⁻¹ = x_I². The terms
are, after division by r^(c−1):

- ζ_(t_*)²: from the first product, −2c.
- ζ_(t_*)ξ: the first product gives ζ_(t_*)ζ_r(2c − 4(c+1)r) = ζ_(t_*)ξ(2(c+1) − c x_I²), and the second term gives
  4(c+4) r ζ_(t_*) ζ_r = −2(c+4) ζ_(t_*) ξ; the sum is −6 − c x_I².
- |η̂|²: 4 from the first bracket and −2(c+4) from the second term; the sum is −2c − 4.
- ξ²: the first product gives 4(c+1) r ζ_r² = (c+1) x_I² ξ², and the second term gives
  −2(c+4) r ζ_r² = −(c+4)/2 · x_I² ξ²; the sum is (c−2)/2 · x_I².

Halving gives K, with −c = −(2β+1), −3 − (c/2) x_I² = −3 − (2β+1)/2 · x_I², −c − 2 = −(2β+3) and
(c−2)/4 = (2β−1)/4. For T: ζ(X_0^(β)) = r^c(ζ_(t_*) + 2rζ_r) = r^c(ζ_(t_*) − ξ),
ζ(−∇t_*) = −ḡ⁻¹(dt_*, ζ) = ζ_r = −ξ/(2r), and ḡ(X_0^(β), −∇t_*) = −dt_*(X_0^(β)) = −r^c; so

    T = r^c (ζ_(t_*) − ξ)(−ξ/(2r)) + (1/2) r^c (−2ζ_(t_*)ζ_r + ζ_r² + r⁻²|η|²)
      = r^(c−1) (−(1/2)ζ_(t_*)ξ + (1/2)ξ²) + r^(c−1) ((1/2)ζ_(t_*)ξ + (1/8) r⁻¹ ξ² + (1/2)|η̂|²),

which is (1/2) r^(c−1)(ξ² + |η̂|² + (1/4) r⁻¹ ξ²), the ζ_(t_*)ξ terms cancelling. For g: by [[lem:ii-e-1-1]] and
[[eq:ii-c-5-1]], g⁻¹ − ḡ⁻¹ is x_I^(2+2ℓ_I) times a quadratic form in (ζ_(t_*), ξ, η̂) with coefficients bounded in
C^(d_0−1)_e, and |dg|/|dḡ| − 1 ∈ x_I^(2ℓ_I) C^(d_0−1)_e; K and T involve these and one edge derivative of them. ∎

**Lemma {#lem:ii-e-2-5}** (Energy estimate near ℐ⁺.) Let α < −1/2 + p̄_1 and Ω′ = Ω_(T_0,T_1), T_0 ≥ 1; put
t′ := t_* + r^(ℓ_I/2). There are δ_I > 0 and T_2, with Ω′ ∩ {t′ ≥ T_2} ⊂ {x_I ≤ δ_I}, and C, such that:

(i) for u ∈ D(Ω′) supported in {x_I ≤ δ_I}, ‖u‖_(H^(1,2α)(Ω′)) ≤ C ‖Pu‖_(H^(0,2α+2)(Ω′));

(ii) for v ∈ C^∞(Ω̄′ ∩ {t′ ≥ T_2}) vanishing near {t^♭ = T_1} and near ℐ⁺,
‖v‖_(H^(1,−2α−2)(Ω′∩{t′≥T_2})) ≤ C ‖P*v‖_(H^(0,−2α)(Ω′∩{t′≥T_2})).

Here H^(1,2β)(O) and H^(0,2β)(O) denote the norms

    (∫_O x_I^(−4β) (|u|² + |∂_(t_*)u|² + |x_I∂_(x_I)u|² + |x_I∂_ω u|²) |dg|)^(1/2),     (∫_O x_I^(−4β) |u|² |dg|)^(1/2),

and P* is the adjoint for |dg| and the fibre inner product h_I of [[eq:ii-e-1-2]]. C is uniform for ε_P small, with
d_0 = 2.

This is [Hin26c, Lemma 8.1] in dimension 4 + 1.

*Proof.* *The level sets of t′.* With α′ := ℓ_I/2, dt′ = dt_* + α′ r^(α′−1) dr has
ḡ⁻¹(dt′, dt′) = −2α′ r^(α′−1) + α′² r^(2α′−2). The proof of [[lem:ii-c-3-2]] bounds the coefficients of g⁻¹ − ḡ⁻¹ in
its basis by C(ε_P + ρ_I^(1−ℓ_I)) ρ_I^(ℓ_I), ρ_I = t_*/r; the basis evaluated on (dt′)^(⊗2) gives ρ_I, O(r^(α′−1)), 0,
ρ_I⁻¹ α′² r^(2α′−2), 0, 0, all at most C r^(α′−1) · r^(α′) at bounded t_*. So g⁻¹(dt′, dt′) ≤ −α′ r^(α′−1) for r ≥ R_0,
as ρ_I^(ℓ_I) r^(α′) = O(r^(−ℓ_I/2)). Moreover dt′(V) = t_* + α′ r^(α′) > 0 for the future timelike V = t∂_t + r∂_r of
the proof of [[lem:ii-c-3-2]], so dt′ is past timelike there, and t′ increases along future causal curves. As t_* is
bounded on Ω′, Ω′ ∩ {t′ ≥ T_2} ⊂ {x_I ≤ δ_I} for T_2 large.

*Conjugation.* Put v_♭ := A_I⁻¹ u and P̃ := A_I⁻¹ P A_I. As A_I is independent of x_I, P̃ − P is of first order: the
commutator [x_I² x_I∂_(x_I) ∂_(t_*), A_I] is x_I² (∂_(t_*)A_I) x_I∂_(x_I), the commutator with x_I⁴ Δ_(𝕊³) is x_I³ times
a first-order edge operator, and the rest is of order 0 with coefficient O(x_I²). By [[lem:ii-e-1-1]], with P_□ for g
satisfying [[eq:ii-e-1-1]] with p_0 = p_1 = 0 (its difference from −□_ḡ comes from g − ḡ), near ℐ⁺

    P̃ = P_□ + 2x_I² p_1^A ∂_(t_*) + x_I² b x_I∂_(x_I) + R_1 + R_0,        p_1^A := A_I⁻¹ p_1 A_I,         {#eq:ii-e-2-3}

with b bounded, R_1 a first-order edge operator with coefficients O(x_I^(2+2ℓ_I)) (of class C^(d_0−1)_e), and R_0 of
order 0 with coefficient O(x_I²). By [[eq:ii-e-1-2]], Re p_1^A = A_I⁻¹ (Re_(h_I) p_1) A_I, so
⟨Re p_1^A w, w⟩ = h_I(Re_(h_I) p_1 A_I w, A_I w) ≥ (p̄_1 − δ′)|w|²; take δ′ := (p̄_1 − 1/2 − α)/4.

*(i).* Let X := e^(−2Φt_*) X_0^(α), future timelike near ℐ⁺: ḡ(X_0^(α), X_0^(α)) = r^(2c)(−1 − 4r), c = 2α + 1, which
dominates the change O(x_I^(2ℓ_I)) r^(2c+1) from g − ḡ. Apply [[lem:ii-e-2-1]] on O := Ω′. Its faces near supp u are
{t^♭ = T_0}, where v_♭ = 0, and {t^♭ = T_1}, with φ = T_1 − t^♭ and ∇φ = −∇t^♭ future timelike, so the boundary term is
≥ 0 by [[lem:ii-e-2-2]]. So

    2 Re ∫ ⟨P̃ v_♭, X v_♭⟩ ≥ ∫ 2K_X(dv_♭) + 2 Re ∫ ⟨(P̃ − P_□) v_♭, X v_♭⟩.

By [[lem:ii-e-2-1]] and [[lem:ii-e-2-4]], K_X = e^(−2Φt_*) (K_(X_0^(α)) + 2Φ T(X_0^(α), −∇t_*)). Write
τ_0 := |∂_(t_*) v_♭|, τ_1 := |x_I∂_(x_I) v_♭| and τ_2 := |x_I∂_ω v_♭|. Pointwise, after division by
e^(−2Φt_*) x_I^(−4α), the integrand on the right is at least

    (−2(2α+1) + 4(p̄_1 − δ′)) τ_0² − C_1 τ_0 τ_1 − C_1 τ_1² + 2Φ(τ_1² + τ_2²) − 2(2α+3)_+ τ_2²
        − C_2 (1 + Φ)(δ^(2ℓ_I) + δ²)(τ_0² + τ_1² + τ_2²) − C_2 |v_♭| (τ_0 + τ_1 + τ_2)

on {x_I ≤ δ}: the first term is 4⟨Re p_1^A ∂_(t_*) v_♭, ∂_(t_*) v_♭⟩ plus the ζ_(t_*)² part of 2K_(X_0^(α)); C_1 bounds
the cross terms −6 Re⟨∂_(t_*) v_♭, x_I∂_(x_I) v_♭⟩, −4 Re⟨p_1^A ∂_(t_*) v_♭, x_I∂_(x_I) v_♭⟩ and those of b; C_2 bounds
the x_I²-terms of [[lem:ii-e-2-4]], the change from ḡ to g, and R_1, R_0. The first coefficient is
a := −2(2α+1) + 4(p̄_1 − δ′) = 16δ′ − 4δ′ = 12δ′ > 0. Use C_1 τ_0 τ_1 ≤ (a/4) τ_0² + (C_1²/a) τ_1² and
C_2 |v_♭| τ_j ≤ (a/16) τ_j² + (4C_2²/a) |v_♭|², and [[lem:ii-e-2-3]] with Y = ∂_(t_*), τ = t_*, w = x_I^(−4α) (as
∂_(t_*)φ > 0 only at the initial face, where v_♭ = 0, and |div_g ∂_(t_*)| ≤ C_0), which gives
∫ e^(−2Φt_*) x_I^(−4α) |v_♭|² ≤ 4Φ⁻² ∫ e^(−2Φt_*) x_I^(−4α) τ_0². Choose Φ large, then δ ≤ δ_I small depending on Φ, to
get

    2 Re ∫ ⟨P̃ v_♭, X v_♭⟩ ≥ ∫ e^(−2Φt_*) x_I^(−4α) ((a/4) τ_0² + (Φ/4)(τ_1² + τ_2²)) |dg|
                          ≥ c ‖e^(−Φt_*) v_♭‖²_(H^(1,2α)).

The left side is at most

    2 ∫ e^(−2Φt_*) x_I^(−4α−2) |P̃ v_♭| (τ_0 + τ_1) ≤ (c/2) ‖e^(−Φt_*) v_♭‖²_(H^(1,2α))
                                                  + C ‖e^(−Φt_*) P̃ v_♭‖²_(H^(0,2α+2)).

As t_* is bounded on Ω′ and A_I, A_I⁻¹ are bounded with bounded derivatives, (i) follows.

*(ii).* Let β := −α − 1, O := Ω′ ∩ {t′ ≥ T_2}, w_♭ := A_I⁻¹ v and X_* := −e^(2Φt_*) X_0^(β), which is past timelike.
P̃* is the standard adjoint of P̃, and A_I⁻¹ P* A_I = P̃* (the proof of [[lem:ii-d-1-1]]). P_□ is symmetric for |dg|. So

    P̃* = P_□ − 2x_I² (p_1^A)* ∂_(t_*) − x_I² b* x_I∂_(x_I) + R_1′ + R_0′,

with R_1′, R_0′ as before ((x_I∂_(x_I))* = −x_I∂_(x_I) + 8 + O(x_I^(2ℓ_I)) for |dg|). Apply [[lem:ii-e-2-1]] on O with
the multiplier X_*: the faces with w_♭ ≠ 0 nearby are {t^♭ = T_0} and {t′ = T_2}, with ∇φ = ∇t^♭, resp. ∇t′, past
timelike, so the boundary terms 2T(X_*, ∇φ)(dw_♭) are ≥ 0 by [[lem:ii-e-2-2]] (both vectors past causal). By
[[lem:ii-e-2-1]], K_(X_*) = e^(2Φt_*) (−K_(X_0^(β)) + 2Φ T(X_0^(β), −∇t_*)). The ζ_(t_*)² coefficient of −2K_(X_0^(β))
is 2(2β+1) = −2(2α+1), and the term 2 Re⟨−2x_I² (p_1^A)* ∂_(t_*) w_♭, X_* w_♭⟩ contributes
4⟨Re p_1^A ∂_(t_*) w_♭, ∂_(t_*) w_♭⟩, so the coefficient is again a. The rest is as in (i), with [[lem:ii-e-2-3]] in the
reverse direction (w_♭ = 0 near {t^♭ = T_1}, the only face of O with ∂_(t_*)φ < 0). ∎

**Lemma {#lem:ii-e-2-6}** (Energy estimate on a compact region.) Let Ω′ and t′ be as in [[lem:ii-e-2-5]], T ≥ T_2 and
O_T := Ω′ ∩ {t′ ≤ T}, which is compact. There is C such that ‖u‖_(H¹(O_T)) ≤ C ‖Pu‖_(L²(O_T)) for u ∈ C^∞(Ō_T)
vanishing near {t^♭ = T_0}, and ‖v‖_(H¹(O_T)) ≤ C ‖P*v‖_(L²(O_T)) for v ∈ C^∞(Ō_T) vanishing near {t^♭ = T_1},
{r = r_0} and {t′ = T}; uniformly for ε_P small, with d_0 = 2.

*Proof.* Let Y_♭ := −∇t^♭, which is future timelike and of class C^(d_0−1), Ŷ_♭ := Y_♭/(Y_♭ t^♭), and
X := e^(−2Φt^♭) Y_♭. By [[lem:ii-e-2-1]], K_X = e^(−2Φt^♭)(K_(Y_♭) + 2Φ T(Y_♭, Y_♭)), and by [[lem:ii-e-2-2]] and
compactness, T(Y_♭, Y_♭)(ζ) ≥ c|ζ|² on Ō_T. The faces with u ≠ 0 nearby are {t^♭ = T_1}, {r = r_0} and {t′ = T}, with
∇φ equal to −∇t^♭, ∇r and −∇t′, all future timelike ([[lem:ii-c-3-2]] and [[lem:ii-e-2-5]]); the boundary terms are
≥ 0 by [[lem:ii-e-2-2]]. The first- and zeroth-order terms of P − P_□ contribute at most
C e^(−2Φt^♭)(|du|² + |u||du|), and [[lem:ii-e-2-3]] with Y = Ŷ_♭ and τ = t^♭ bounds ∫ e^(−2Φt^♭)|u|² by
4Φ⁻² ∫ e^(−2Φt^♭)|Ŷ_♭ u|², the only face with Ŷ_♭ φ > 0 being the initial one. For Φ large this gives the first
estimate, as in [[lem:ii-e-2-5]]. For P* use −e^(2Φt^♭) Y_♭ and the reverse inequality of [[lem:ii-e-2-3]]. ∎

**Proposition {#prop:ii-e-2-7}** (Energy estimates on slabs.) Let α < −1/2 + p̄_1 and Ω′ = Ω_(T_0,T_1), T_0 ≥ 1. There
is C, uniform for ε_P small with d_0 = 2, such that for u ∈ D(Ω′) and v ∈ D_*(Ω′)

    ‖u‖_(H^(1,2α)(Ω′)) ≤ C ‖Pu‖_(H^(0,2α+2)(Ω′)),     ‖v‖_(H^(1,−2α−2)(Ω′)) ≤ C ‖P*v‖_(H^(0,−2α)(Ω′)).   {#eq:ii-e-2-4}

The same holds on Ω′ ∩ {t′ ≤ T} for T ≥ T_2, with {t′ = T} a further final face, and for P^ext on the slabs
{T_0 ≤ t^♭ ≤ T_1, r ≥ r^♯} of [[lem:ii-e-1-2]], T_0 ≥ 1 − η_0.

This is [Hin26c, Lemma 8.1 and (8.23)] in dimension 4 + 1.

*Proof.* Let χ = χ(t′) equal 1 for t′ ≤ T_2 and 0 for t′ ≥ T_2 + 1. For u: ‖χu‖_(H¹) ≤ C‖u‖_(H¹(O_(T_2+1))) ≤ C‖Pu‖ by
[[lem:ii-e-2-6]], the weights being bounded on O_(T_2+1). (1 − χ)u ∈ D(Ω′) is supported in {x_I ≤ δ_I}, so by
[[lem:ii-e-2-5]] (i), ‖(1 − χ)u‖_(H^(1,2α)) ≤ C(‖Pu‖ + ‖[P, χ]u‖_(H^(0,2α+2))), and [P, χ]u is supported in O_(T_2+1)
with norm at most C‖u‖_(H¹(O_(T_2+1))). For v, in the reverse order: [[lem:ii-e-2-5]] (ii) bounds v on
Ω′ ∩ {t′ ≥ T_2}, which contains the support of [P*, χ]v; then [[lem:ii-e-2-6]] applied to χv, which vanishes near
{t′ = T_2 + 1}, bounds χv. On the extended slabs the proofs apply verbatim, by [[lem:ii-e-1-2]] (iii)–(iv), with
[[eq:ii-e-1-2]] holding at 2δ′, so that the coefficient of [[lem:ii-e-2-5]] is a = −2(2α+1) + 4(p̄_1 − 2δ′) = 8δ′ in
place of 12δ′. ∎
