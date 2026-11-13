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
