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

### Solvability on slabs {#sec:ii-e-3}

Throughout, α < −1/2 + p̄_1, and h is a fibre inner product equal to h_I of [[eq:ii-e-1-2]] near ℐ⁺ (patched with the
standard one by a partition of unity; the conditions are convex in the Gram matrix). P* is the adjoint of P (or of
P^ext) for |dg| and h. Changing the density from |dt dx| ([[sec:ii-c-1-1]]) to |dg| = μ|dt dx| adds to σ_1(Im_h P) the
term (1/2) H_G log μ, which vanishes at the radial sets, where 𝖧 = 0; so the thresholds below are those of [[ch:s06]].
R := ∂R_(ℐ⁺,out) is the outgoing radial set over ℐ⁺, and R_([a,b]) := R ∩ {a ≤ t_* ≤ b}.

#### Radial estimates at ∂R_(ℐ⁺,out) localised in time {#sec:ii-e-3-1}

We use the eb-coordinates of [[sec:ii-b-7]] near ℐ⁺: ρ_+ = t_*⁻¹, x′_I = (t_*/r)^(1/2), ρ := σ_eb⁻¹, ξ̂, η̂,
ℓ := G_eb = x′_I^(−2) ρ_+^(−2) G and 𝖧 := ρ H_ℓ ([[eq:ii-b-7-3]]), as in [[prop:ii-d-3-5]] and [[prop:ii-d-3-6]]. For
κ > 0 put

    F := t_* − κ x′_I^(2ℓ_I).

x′_I^(2ℓ_I) has bounded eb-derivatives of every order, so functions of F are admissible factors of a commutant.

**Lemma {#lem:ii-e-3-1}** (A time function adapted to R.) Let t̄ > 1. There are κ, x_0 > 0 and C, depending on t̄,
such that on U_F := {|ξ̂| ≤ 1/2, x′_I ≤ x_0, 1/2 ≤ t_* ≤ t̄} in ^(eb)S*M, for P with ε_P ≤ 1,

    𝖧F = h_F − t_* ρ² ℓ,     h_F = t_* ((1/2) ξ̂² + |η̂|² + (1/4) x′_I² ξ̂²) + x′_I^(2ℓ_I) h̃_F,     h̃_F ≥ (1/2) κ ℓ_I,
                                                                                                     {#eq:ii-e-3-1}

with h̃_F of class C^(d_0−2) with bounded eb-derivatives.

*Proof.* In eb-coordinates σ_eb is dual to ρ_+∂_(ρ_+), so H_ℓ ρ_+ = ρ_+ ∂_(σ_eb) ℓ and 𝖧t_* = −t_* ρ ∂_(σ_eb) ℓ. For
Ḡ_eb = (1/2) ξ(ξ − 2σ) + |η|² + (1/4) x′_I² ξ² ([[eq:ii-b-7-1]]), −∂_σ Ḡ_eb = ξ, and
ρ² Ḡ_eb = (1/2) ξ̂(ξ̂ − 2) + |η̂|² + (1/4) x′_I² ξ̂², so

    ξ̂ = (1/2) ξ̂² + |η̂|² + (1/4) x′_I² ξ̂² − ρ² Ḡ_eb.

Put d := ℓ − Ḡ_eb; by [[eq:ii-c-5-1]] and [[lem:ii-c-4-1]] (a), d ∈ x′_I^(2ℓ_I) C^(d_0−1) P^[2], with norm bounded for
ε_P ≤ 1. Hence

    𝖧t_* = t_* ((1/2) ξ̂² + |η̂|² + (1/4) x′_I² ξ̂²) − t_* ρ² ℓ + t_* (ρ² d − ρ ∂_σ d),

and the last term is x′_I^(2ℓ_I) times a function bounded by C_d t_* on the cosphere bundle. By [[eq:ii-b-7-4]] and
[[eq:ii-c-5-1]], x′_I⁻¹ 𝖧x′_I = ξ̂ − 1 + O(x′_I^(2ℓ_I)), so 𝖧(x′_I^(2ℓ_I)) = 2ℓ_I x′_I^(2ℓ_I)(ξ̂ − 1 + O(x′_I^(2ℓ_I))).
Therefore [[eq:ii-e-3-1]] holds with

    h̃_F = 2κℓ_I (1 − ξ̂) + t_* x′_I^(−2ℓ_I) (ρ² d − ρ ∂_σ d) + κ O(x′_I^(2ℓ_I)),

and h̃_F ≥ κℓ_I − C_d t̄ − Cκ x_0^(2ℓ_I) ≥ (1/2) κℓ_I on U_F for κ := 4C_d t̄/ℓ_I and x_0 small. ∎

So 𝖧F is, up to a multiple of ℓ, a sum of squares of symbols on a full neighbourhood of R at bounded times, on and off
the characteristic set: h_F = Σ_i c_i² with c_i among (t_*/2)^(1/2) ξ̂, t_*^(1/2) η̂_j, (1/2) t_*^(1/2) x′_I ξ̂ and
x′_I^(ℓ_I) h̃_F^(1/2). For t^♭ in place of F this fails: at x_I = 0, 𝖧t^♭ = t_* ξ̂, which is negative off the
characteristic set near R (the paragraph after [[prop:ii-d-3-6]]).

**Proposition {#prop:ii-e-3-2}** (Localised radial estimates at R.) Let t_− < t_+ and ω_0 ∈ (0, 1] with
t_− − ω_0 ≥ 1/2, let s > s_0 be constants, and suppose [[eq:ii-e-1-2]] holds with 2δ′ in place of δ′ on
R_([t_−−ω_0, t_++ω_0]) (for P^ext below t_* = 1, [[lem:ii-e-1-2]] (iii)). There are B, E, E_±, G ∈ C_b^∞Ψ⁰_(e3b) such
that

(1) their operator wave front sets lie in any given neighbourhood of R_([t_−−ω_0, t_++ω_0]);

(2) their Schwartz kernels lie in 𝒦 × 𝒦 for any given compact neighbourhood 𝒦 of ℐ⁺ ∩ {t_− − ω_0 ≤ t_* ≤ t_+ + ω_0};

(3) B is elliptic at R_([t_−,t_+]);

(4) WF′(E_−) ⊂ {t_* ≤ t_−}, WF′(E_+) ⊂ {t_* ≥ t_+}, and WF′(E) ∩ R = ∅;

and such that, in the strong sense and uniformly for ε_P small,

    ‖Bu‖_(s,2α) ≤ C (‖GPu‖_(s−1,2α+2) + ‖E_−u‖_(s,2α) + ‖Eu‖_(s,2α) + ‖χ̃u‖_(s_0,2α)),               {#eq:ii-e-3-2}

    ‖Bv‖_(s,−2α−2) ≤ C (‖GP*v‖_(s−1,−2α) + ‖E_+v‖_(s,−2α−2) + ‖χ̃v‖_(s_0,−2α−2)),                     {#eq:ii-e-3-3}

with χ̃ as in [[prop:ii-d-3-6]] and the norms of H^(·,(2β,0))_(e3b) near ℐ⁺ at finite times.

[[eq:ii-e-3-2]] is the sink estimate of [[prop:ii-d-3-6]] localised to t_* ≤ t_+, with no error term at late times;
[[eq:ii-e-3-3]] is the estimate for the adjoint at R, which is then a radial source, propagating backward in time. In
the proof of [Hin26c, Proposition 8.3] the first is taken from [Hin26c, Proposition 7.9] with a finite final time, and
the second is left to the reader.

*Proof.* We follow the pattern of [[sec:ii-d-3]] at R, with W′ := x′_I² ρ_+², ρ and 𝖧 as above, A := A_I the frame of
h_I, and the weight w := x′_I^(2α) for [[eq:ii-e-3-2]], w* := x′_I^(2α*) with α* := −α − 1 for [[eq:ii-e-3-3]]. The
commutant is ǎ = ρ^(−s+1/2) Ψ χ_∞ with

    Ψ := ψ(𝔐_Σ ρ²ℓ) ψ(𝔐_R q) ψ(𝔐 x′_I) ψ_−(F) ψ_+(F),        q := ξ̂² + |η̂|²,
    ψ_−(F) := η_t((F − t_−)/ω_0),        ψ_+(F) := η_t((t_+ − F)/ω_0),

η_t as in [[prop:ii-d-3-6]], and t̄ := t_+ + 2 in [[lem:ii-e-3-1]]. On supp ψ(𝔐_R q) ψ(𝔐 x′_I), |ξ̂| ≤ 1/2 and
x′_I ≤ x_0 for 𝔐_R and 𝔐 large, and 0 ≤ t_* − F ≤ κ𝔐^(−2ℓ_I) ≤ ω_0/4. As η_t = 0 on (−∞, −1/2], η_t = 1 on
[−1/4, ∞) and η_t′ ≠ 0 only on (−1/2, −1/4), on supp Ψ we have t_− − ω_0/2 ≤ F ≤ t_+ + ω_0/2; so
supp Ψ ⊂ U_F ∩ {t_− − ω_0/2 ≤ t_* ≤ t_+ + 3ω_0/4}, which is compact, and Ψ = 1 at R_([t_−,t_+]), where F = t_*. In
[[eq:ii-d-3-1]], which is used below, ℓ_I denotes, as there, the principal symbol of the imaginary part of the
conjugated operator, not the decay order at ℐ⁺.

*[[eq:ii-e-3-2]], with ς = 1.* [[eq:ii-d-3-1]] gives
H_ℓ(ǎ_ε²) + 2ǎ_ε² ℓ_I = ρ^(−2s) φ_ε² (−Ψ² Q_ε + 𝖧(Ψ²)), and at R, as in [[prop:ii-d-3-6]],

    Q_ε = 4A⁻¹(Re_(h_I) p_1)A − 2 − 4α ≥ 4(p̄_1 − 2δ′) − 2 − 4α = 8δ′,

by [[eq:ii-e-1-2]] with 2δ′, as 4(p̄_1 − 1/2 − α) = 16δ′. The factors ψ(𝔐_Σ ρ²ℓ), ψ(𝔐_R q) and ψ(𝔐 x′_I) contribute as
in [[prop:ii-d-3-6]]: j_ε ℓ, and +e*e terms supported in {q ≥ (2𝔐_R)⁻¹} ∪ {x′_I ≥ (2𝔐)⁻¹}, which give E. For the time
factors, by the chain rule and [[eq:ii-e-3-1]] [[pending:issue-3]],

    𝖧(ψ_−(F)²) = (2/ω_0) ψ_− η_t′((F − t_−)/ω_0) (h_F − t_* ρ² ℓ),
    𝖧(ψ_+(F)²) = −(2/ω_0) ψ_+ η_t′((t_+ − F)/ω_0) (h_F − t_* ρ² ℓ).

The part with t_* ρ² ℓ is of the form j_ε ℓ ([[lem:ii-d-2-1]]). The part with h_F = Σ_i c_i² is, up to its sign,
Σ_i ((2/ω_0)^(1/2) (ψ_± η_t′)^(1/2) c_i)², a finite sum of squares of symbols, since (η_t η_t′)^(1/2) is smooth. For
ψ_+ it enters with the sign −: a term −b′*b′, so no error term arises at late times. For ψ_− it enters with the sign +:
a term +e_−*e_−, supported where η_t′((F − t_−)/ω_0) ≠ 0, so where F < t_− − ω_0/4, and hence t_* < t_− on supp Ψ;
this gives E_−. Then [[lem:ii-d-2-1]]–[[lem:ii-d-2-3]] give [[eq:ii-e-3-2]].

*[[eq:ii-e-3-3]], with ς = −1.* For P* the conjugated operator has 𝔭′_(P*) = −𝔭′ ([[lem:ii-d-1-1]], as
Im_h P* = −Im_h P), so [[eq:ii-d-3-1]] gives

    −(H_ℓ(ǎ_ε²) + 2ǎ_ε² ℓ_(I,P*)) = ρ^(−2s) φ_ε² (−Ψ² Q*_ε − 𝖧(Ψ²)),
    Q*_ε := −(2s_ε − 1) ρ⁻¹𝖧ρ − 2A⁻¹(𝔭′ + (1/2) 𝖧 log W′ + 𝖧 log w*)A.

At R, ρ⁻¹𝖧ρ = 0, 𝔭′ = −2 Re_(h_I) p_1 ([[lem:ii-d-3-4]]), 𝖧 log W′ = 2x′_I⁻¹ 𝖧x′_I + 2ρ_+⁻¹ 𝖧ρ_+ = −2 and
𝖧 log w* = −2α* = 2α + 2 ([[eq:ii-b-7-4]]). So Q*_ε = 4A⁻¹(Re_(h_I) p_1)A + 2 − 4α − 4, the same quantity as Q_ε in
[[eq:ii-e-3-2]], and positive; near R the term with ρ⁻¹𝖧ρ is small, as in [[sec:ii-d-3]]. Now the localisers enter
with the opposite sign. As 𝖧q ≤ −q and 𝖧x′_I ≤ −x′_I/2 near R ([[prop:ii-d-3-6]]), the factors ψ(𝔐_R q) and
ψ(𝔐 x′_I) give −b′*b′ terms: for −𝖧 the set R is a radial source, and no error term arises from them.
ψ(𝔐_Σ ρ²ℓ) gives j_ε ℓ. Of the time factors, ψ_− gives −b′*b′ and ψ_+ gives +e_+*e_+, supported where
F > t_+ + ω_0/4, hence in {t_* > t_+}; this is E_+. [[lem:ii-d-2-1]]–[[lem:ii-d-2-3]] hold with ς = −1, as
[[lem:ii-a1-4-1]], on which they rest, allows either sign; they give [[eq:ii-e-3-3]].

Both estimates use the operator only through the pattern, so they hold for P^ext near {t_* ≤ 1}, and for systems
P ⊗ Id − Q with Q of first order whose principal symbol vanishes at R, as in [[lem:ii-d1-2-5]]. The constants depend on
P through finitely many coefficient norms and the margins, which are uniform for ε_P small. ∎

#### Regularity on slabs {#sec:ii-e-3-2}

Below, 𝗌 is a **slab order**: 𝗌 ∈ C^∞(^(e3b)S*M) with ±𝖧𝗌 ≤ 0 on ∂Σ^± over the region considered, and 𝗌 constant
near R. Admissible order functions ([[def:ii-c-5-2]]) are slab orders over Ω_*, by [[prop:ii-c-5-1]] (2) and (5); so
are constants.

*The order on the extension region.* [[prop:ii-c-5-1]] (2) concerns Ω_* only, while [[lem:ii-e-3-3]] (a) at T_0 = 1
propagates through the collar {1 − η_0/2 < t^♭ < 1}, part of which lies in {t_* < 1}, and over {r^♯ ≤ r ≤ r_0}. There
the admissible order is extended by its own formula [[eq:ii-c-5-3]]: 𝗌 = s_in − (s_in − s_out)χ, with
χ = ψ_0(x_I) χ_I + (1 − ψ_0(x_I)) χ_ι. The second term is supported in

    Ω_ι ∩ {ϱ < ε_ι δ} ⊂ {r > (ε_ι δ)⁻¹, t_* ≥ r/C_ι}

([[sec:ii-c-5-2]], with ϱ = r⁻¹ and ρ_K = r/t_* ≤ C_ι on Ω_ι), which, after decreasing ε_ι so that (C_ι ε_ι δ)⁻¹ > 1,
meets neither {t_* ≤ 1} nor {r ≤ r_0} (as (ε_ι δ)⁻¹ > r_h + 1). The factor χ_I is a function of the eb-fibre variables
ξ̂, |η̂|² and σ_eb²/|ν|²_eb alone, defined and invariant under translation in t_* for t_* ≥ 1/2. So on {t_* ≥ 1/2}
outside Ω_*, 𝗌 = s_in − (s_in − s_out) ψ_0(x_I) χ_I, which is s_in where x_I ≥ ε_I (in particular over
{r^♯ ≤ r ≤ r_0} at these times). It is a slab order there: where it is constant, trivially; near ℐ⁺,
±𝖧(ψ_0(x_I) χ_I) ≥ 0 on ∂Σ^± by the monotonicity argument of [[sec:ii-c-5-2]] (ψ_0′ ≤ 0 with 𝖧x_I ≤ −x_I/4, and
φ′(ξ̂) 𝖧ξ̂ ≥ 0), which uses only [[lem:ii-c-5-3]] and [[lem:ii-c-5-4]] near ℐ⁺. Their proofs use only the bounds
𝖧^eb − 𝖧^0 = O(x_I^(2ℓ_I)) on ξ̂ and O(x_I^(1+2ℓ_I)) on x_I, uniformly in t_*, which [[lem:ii-e-1-2]] (ii) provides for
P^ext on {t_* ≥ 1/2}, the coefficients of P^ext − P_0 being small there in the norms of [[def:ii-c-3-3]]. "Slab order"
in [[prop:ii-e-3-4]], [[prop:ii-e-4-3]], [[prop:ii-e-4-4]] and [[thm:ii-e-6-1]] refers to this extension.

Two slabs Ω_1 ⊂ Ω_2 are **nested with room δ > 0** if they have the same initial face and each final face of Ω_1 lies
at distance at least δ (in t^♭, resp. in r) inside Ω_2. Typical choices are Ω_1 = Ω_(T_0,T_1) and

    Ω_2 = Ω^♯_(T_0,T_1) := {T_0 ≤ t^♭ ≤ T_1 + 1, r ≥ r^♯}

with P^ext; or Ω_1 = Ω_(T_0,T_1−δ) ∩ {r ≥ r_0 + δ} and Ω_2 = Ω_(T_0,T_1). The spaces, [[lem:ii-e-1-3]],
[[lem:ii-e-2-5]], [[lem:ii-e-2-6]] and [[prop:ii-e-2-7]] hold for these domains with the same proofs, {r = r_0 + δ} and
{r = r^♯} being spacelike final faces ([[lem:ii-e-1-2]] (iv)).

**Lemma {#lem:ii-e-3-3}** (Regularity on slabs.) (a) Let Ω_1 ⊂ Ω_2 be nested with room δ, with initial face
{t^♭ = T_0}, T_0 ≥ 1 − η_0/2, let 𝗌_0 < 𝗌 be slab orders, and let u ∈ H^(𝗌_0,2α)(Ω_2)^(•,−) with
Pu ∈ H^(𝗌−1,2α+2)(Ω_2)^(•,−) (P^ext where defined). Then u|_(Ω_1) ∈ H^(𝗌,2α)(Ω_1)^(•,−) and

    ‖u‖_(H^(𝗌,2α)(Ω_1)^(•,−)) ≤ C (‖Pu‖_(H^(𝗌−1,2α+2)(Ω_2)^(•,−)) + ‖u‖_(H^(𝗌_0,2α)(Ω_2)^(•,−))).

(b) Let Ω_1 = Ω_(T_0,T_1) ⊂ Ω_3 := Ω_(T_0−δ,T_1) (the same final faces; T_0 − δ ≥ 1 − η_0), let s_0 < s be constants,
and let v ∈ H^(s_0,−2α−2)(Ω_3)^(−,•) with P*v ∈ H^(s−1,−2α)(Ω_3)^(−,•). Then v|_(Ω_1) ∈ H^(s,−2α−2)(Ω_1)^(−,•), with the
corresponding estimate.

The constants are uniform for ε_P small, with d_0 depending only on the orders.

*Proof.* (a) Let ũ be an extension of u supported in {t^♭ ≥ T_0}, and f ∈ H^(𝗌−1,2α+2)_e the minimal extension of Pu.
Let U_2 be the union of the interior of Ω_2 relative to its final faces and of {t^♭ < T_0}, near the slab. On U_2,
Pũ = f: U_2 is the open set to which the spaces of Ω_2 restrict, and this is what Pu ∈ H^(𝗌−1,2α+2)(Ω_2)^(•,−) means. So
for operators with Schwartz kernels in U_2 × U_2 the microlocal estimates below see Pũ only through f. Let ω_0 be as
below; fix a cut-off χ_1 equal to 1 near Ω_1 and supported in U_2 ∩ {t^♭ > T_0 − ω_0/2}, and let all operators be
carried by such cut-offs. We control ũ microlocally at order 𝗌 at every point of ^(e3b)S*M over supp χ_1 (a compact
set in the compactified bundle).

Off the characteristic set we use the elliptic estimate ([[thm:ii-a1-3-1]]). On it over M°: by [[prop:ii-c-4-2]] and
[[lem:ii-e-1-2]] (iv), the backward curve reaches {t^♭ < T_0}, where ũ = 0, in finite time, and stays in
{r > r_0 − δ}, as dr is future timelike near {r = r_0}, so that r cannot decrease along a backward curve there.
Propagation ([[thm:ii-a1-5-4]], at the order 𝗌, with 𝖧𝗌 ≤ 0) controls ũ there. Over ℐ⁺ off R: the curves of
[[lem:ii-b-7-2]] (1) (i), (iii) reach {t_* < T_0} backward (below t_* = 1 the flow over ℐ⁺ is still given by
[[eq:ii-b-7-5]], the normal form of P^ext being that of P_0 there); propagation applies as before. At
R_([T_0, T_1+δ/2]) we use [[prop:ii-e-3-2]], [[eq:ii-e-3-2]], with

    t_− := T_0 − ω_0/2,     t_+ := T_1 + δ/2,     ω_0 := min(δ/2, η_0/4),

at the constant value of 𝗌 near R. Its E_− is microsupported in {t_* ≤ t_−}, where ũ = 0 (kernels in {t^♭ < T_0}²),
and its E in a punctured neighbourhood of R at times in [t_− − ω_0, t_+ + ω_0], from whose points the backward curves
reach {t^♭ < T_0}, as above; by compactness of WF′(E) and the local boundedness of the entrance times
([[sec:ii-a-9-1]], (O)), propagation bounds ‖Eũ‖_𝗌. The finitely many operators so obtained are jointly elliptic over
supp χ_1, and [[lem:ii-a-8-4]] (c) gives

    ‖χ_1 ũ‖_(𝗌,2α) ≤ C (‖χ_1′ f‖_(𝗌−1,2α+2) + ‖χ_1′ ũ‖_(𝗌_0,2α)).

χ_1 ũ is an extension of u|_(Ω_1) supported in {t^♭ ≥ T_0}, and χ_1′f, χ_1′ũ depend only on Pu and u (the cut-off χ_1′
being supported in U_2), with norms at most C times the quotient norms. This is (a), in the strong sense, since each
estimate used holds in it.

(b) The same with −𝖧. Let ṽ be an extension of v supported in F_3 := Ω ∩ {t^♭ ≤ T_1, r ≥ r_0}; P*ṽ is controlled on
the set V_3 formed by the interior of Ω_3 relative to its initial face, together with {t^♭ > T_1} ∪ {r < r_0}, where
ṽ = 0. Propagation for the backward problem is propagation for −P*, whose rescaled Hamilton field is −𝖧; it applies to
constant orders. Every forward curve from a point of the characteristic set over Ω_1 either reaches
{t^♭ > T_1} ∪ {r < r_0} in finite time, or enters any given neighbourhood of R_([T_0,T_1]). Indeed t^♭ increases along
it; if it stays in the slab, its ω-limit set is non-empty, compact and invariant; a point of it over M° would have its
orbit in the limit set with t^♭ strictly increasing there, against t^♭ being constant (equal to lim t^♭) on the limit
set; so the limit set lies over ℐ⁺ at the time t_∞ := lim t^♭ ∈ [T_0, T_1], where 𝖧t_* = t_* ξ̂ = 0, so ξ̂ = 0 and
|η̂|² = (1/2) ξ̂(2 − ξ̂) = 0: it lies in R. Over ℐ⁺ the curves (iii) of [[lem:ii-b-7-2]] reach {t_* > T_1} and the
curves (i) tend to R. At R_([T_0−δ/2, T_1]) use [[eq:ii-e-3-3]] with t_− := T_0 − δ/2 and t_+ := T_1 + ω_0/2 (ω_0 as in
(a)). Its E_+ quantises e_+, whose symbol is supported in {t_* > t_+} (proof of [[prop:ii-e-3-2]]), and its Schwartz
kernel lies in 𝒦 × 𝒦. Neither places the kernel in {t^♭ > T_1}: the operator wave front set does not locate a kernel,
and 𝒦 covers ℐ⁺ ∩ {t_− − ω_0 ≤ t_* ≤ t_+ + ω_0}. So quantise e_+ with Schwartz kernel within ω_0/8 of the diagonal in
t_*, as is done for E after [[prop:ii-d-3-6]]; this changes E_+ by an operator of order −∞ with kernel in 𝒦 × 𝒦,
which the low-order term of [[eq:ii-e-3-3]] absorbs, and the kernel now lies in (𝒦 ∩ {t_* > t_+ − ω_0/8})². 𝒦 is any
compact neighbourhood of a compact part of ℐ⁺, where x_I = 0, so we take it so small that
t_*^(1+ℓ_I) x_I^(2ℓ_I) < ω_0/4 on 𝒦. Then on 𝒦 ∩ {t_* > t_+ − ω_0/8},

    t^♭ = t_* − t_*^(1+ℓ_I) x_I^(2ℓ_I) > T_1 + ω_0/8,

where ṽ = 0, so E_+ṽ = 0. Conclude as in (a). ∎

#### Solvability {#sec:ii-e-3-3}

**Proposition {#prop:ii-e-3-4}** (Solvability of forward problems on slabs.) Let α < −1/2 + p̄_1, Ω′ = Ω_(T_0,T_1) with
T_0 ≥ 1 (P^ext below t^♭ = 1), and 𝗌 a slab order. There are d_0, depending only on 𝗌 (and, in (i), on s′), and C,
uniform for ε_P small, such that:

(i) (*uniqueness*) if u ∈ H^(s′,2α)(Ω′)^(•,−) for some s′ ∈ ℝ and Pu = 0, then u = 0;

(ii) (*existence*) for every f ∈ H^(𝗌−1,2α+2)(Ω′)^(•,−) there is u ∈ H^(𝗌,2α)(Ω′)^(•,−) with Pu = f and

    ‖u‖_(H^(𝗌,2α)(Ω′)^(•,−)) ≤ C ‖f‖_(H^(𝗌−1,2α+2)(Ω′)^(•,−)).                                         {#eq:ii-e-3-4}

The same holds for P* and backward problems on H^(s,−2α−2)(Ω′)^(−,•), s constant, and for the systems of
[[sec:ii-e-4]] and of [[prop:ii-e-3-2]].

This is [Hin26c, Corollary 8.2 and Proposition 8.3] in dimension 4 + 1.

*Proof.* (i) For δ > 0 small let Ω_δ := Ω_(T_0,T_1−δ) ∩ {r ≥ r_0 + δ}, nested in Ω′ with room δ. By [[lem:ii-e-3-3]]
(a) at the constant orders s′ < m′, u|_(Ω_δ) ∈ H^(m′,2α)(Ω_δ)^(•,−) for every m′ > s′, hence
u|_(Ω_δ) ∈ H^(2,2α)(Ω_δ)^(•,−). By [[lem:ii-e-1-3]] (c), D(Ω_δ) is dense in H^(2,2α)(Ω_δ)^(•,−); both sides of the
first estimate [[eq:ii-e-2-4]] on Ω_δ are continuous in that norm (P maps it to H^(0,2α+2), whose quotient norm is the
L²-norm on the slab). So ‖u‖_(H^(1,2α)(Ω_δ)) ≤ C‖Pu‖ = 0, and u = 0 on Ω_δ for every δ.

(ii) *Step 1: weak solutions in L².* Let Ω^♯ := Ω^♯_(T_0,T_1) and let f^♯ be the restriction to Ω^♯ of the minimal
extension of f in H^(𝗌−1,2α+2)_e; assume first inf 𝗌 ≥ 0, so that f^♯ ∈ H^(−1,2α+2)(Ω^♯)^(•,−) with norm ≤ C‖f‖. For
v ∈ D_*(Ω^♯), by [[lem:ii-e-1-3]] (a),

    |⟨f^♯, v⟩| ≤ C ‖f‖ ‖v‖_(H^(1,−2α−2)(Ω^♯)^(−,•)) ≤ C′ ‖f‖ ‖v‖_(H^(1,−2α−2)(Ω^♯)) ≤ C″ ‖f‖ ‖P*v‖_(H^(0,−2α)(Ω^♯)),

the second inequality by Seeley's extension E_0 of [[lem:ii-e-1-3]] (b), which is bounded from the slab norm, and the
third by [[eq:ii-e-2-4]] for the adjoint of P^ext on Ω^♯. So P*v ↦ ⟨f^♯, v⟩ is a bounded functional on P*D_*(Ω^♯) in
the L²-norm. By the Hahn–Banach theorem and the Riesz representation theorem there is u^♯ ∈ H^(0,2α)(Ω^♯), with
‖u^♯‖ ≤ C‖f‖ and ⟨u^♯, P*v⟩ = ⟨f^♯, v⟩ for v ∈ D_*(Ω^♯). Extended by zero, u^♯ is supported in {t^♭ ≥ T_0}, and for
v ∈ D_* (a test function on M) ⟨Pu^♯, v⟩ = ⟨u^♯, P*v⟩. So Pu^♯ and f^♯ agree on D_*(Ω^♯), which contains the
C_c^∞-functions supported in {t^♭ < T_1 + 1, r > r^♯}: Pu^♯ = f^♯ on Ω^♯.

*Step 2: regularity.* [[lem:ii-e-3-3]] (a) with Ω′ ⊂ Ω^♯ (room 1, resp. r_0 − r^♯) and 𝗌_0 := min(0, inf 𝗌) − 1 gives
u := u^♯|_(Ω′) ∈ H^(𝗌,2α)(Ω′)^(•,−) and [[eq:ii-e-3-4]]. By (i) it is the solution.

*Step 3: the backward problem at nonnegative orders.* The same argument applies with the roles exchanged. For
g ∈ H^(m_1−1,−2α)(Ω′)^(−,•), m_1 ≥ 1 an integer, let Ω_3 := Ω_(T_0−δ,T_1) (with P^ext if T_0 − δ < 1; δ := η_0/2) and
let g_3 be the restriction of the minimal extension, in L². For u ∈ D(Ω_3),

    |⟨u, g_3⟩| ≤ ‖u‖_(H^(0,2α)) ‖g_3‖ ≤ C ‖Pu‖_(H^(0,2α+2)) ‖g‖

by [[eq:ii-e-2-4]] on Ω_3, the H⁰ quotient norm being the L²-norm, so that no extension operator is needed. The
Hahn–Banach theorem gives v_3 ∈ H^(0,−2α−2)(Ω_3) with P*v_3 = g_3 (by the density of D(Ω_3), [[lem:ii-e-1-3]] (c)), and
[[lem:ii-e-3-3]] (b) gives S_* g := v_3|_(Ω′) ∈ H^(m_1,−2α−2)(Ω′)^(−,•) with ‖S_* g‖ ≤ C‖g‖. Uniqueness for the backward
problem is (i) with the roles exchanged. So S_* is the solution operator, and S_* P*v = v for v ∈ D_*(Ω′).

*Step 4: negative orders.* Let inf 𝗌 < 0 and m ∈ ℕ with −m < inf 𝗌 − 1. Work on Ω^♯ with
f^♯ ∈ H^(−m−1,2α+2)(Ω^♯)^(•,−). For g ∈ H^(m,−2α)(Ω^♯)^(−,•) put Λ(g) := ⟨f^♯, S_* g⟩, with S_* of Step 3 on Ω^♯ (at
the order m_1 = m + 1); |Λ(g)| ≤ C‖f‖‖g‖. By [[lem:ii-e-1-3]] (b) (at m, on Ω^♯) there is
u^♯ ∈ H^(−m,2α)(Ω^♯)^(•,−), ‖u^♯‖ ≤ C‖f‖, with ⟨u^♯, g⟩ = Λ(g). For v ∈ D_*(Ω^♯),

    ⟨Pu^♯, v⟩ = ⟨u^♯, P*v⟩ = ⟨f^♯, S_* P*v⟩ = ⟨f^♯, v⟩,

so Pu^♯ = f^♯ as in Step 1. Step 2 with 𝗌_0 := −m concludes.

The constants depend on P through finitely many coefficient norms and the structural margins (the timelike conditions,
the threshold, the dynamics), uniformly for ε_P small; for the systems of [[sec:ii-e-4]] the same margins hold, the
coupling being of first order with principal symbol vanishing at R and not entering the threshold of [[lem:ii-e-2-5]]
(it decays at ℐ⁺). ∎

[Hin26c] proves the step 𝗌 ≥ 1 with its Proposition 7.9 for a finite final time, a case whose proof fails off the
characteristic set (the paragraph after [[prop:ii-d-3-6]]); [[prop:ii-e-3-2]] replaces it. [Hin26c, Corollary 8.2]
constructs the H¹-solution by smoothing the coefficients, quoting finite-time solvability of wave equations with smooth
coefficients and passing to a weak limit, and asserts its uniqueness, which [Hin26c, (8.5)], proved for u ∈ H², gives
for solutions in H¹ only after a density argument. Steps 1–3 construct the solution by duality from the energy
estimates for P and P* instead, and (i) proves uniqueness in every H^(s′) by regularity on nested slabs
([[lem:ii-e-3-3]]) and the energy estimate on the dense class ([[lem:ii-e-1-3]] (c)).

### b-regularity on slabs, and the tame estimates {#sec:ii-e-4}

#### Operators on slab spaces {#sec:ii-e-4-1}

**Lemma {#lem:ii-e-4-1}** (Operators, products and words on slab spaces.) Let Ω′ be a slab of [[sec:ii-e-3]] (or of
[[sec:ii-e-5]]), 𝗌 an order function and k ∈ ℕ_0; the spaces are those of [[sec:ii-e-1-1]] with any weight.

(a) A differential operator Q of order m whose coefficients, in a fixed frame (products of ∂_(t_*), x_I∂_(x_I) and
x_I∂_ω near ℐ⁺, of coordinate fields elsewhere), lie in C^((d_0;k))_(e;b) on a neighbourhood of Ω′ maps
H^((𝗌;k))(Ω′)^(•,−) to H^((𝗌−m;k))(Ω′)^(•,−), and H^((𝗌;k))(Ω′)^(−,•) to H^((𝗌−m;k))(Ω′)^(−,•), with norm at most C_k
times the coefficient norms; d_0 depends only on 𝗌 and m.

(b) (*Tame products, with room.*) Let Ω′ ⊂ Ω″ be nested with room δ. There are d_0 and d̃, depending only on 𝗌, such
that for all k, 0 ≤ j ≤ k, ℓ ∈ C^((d_0;k))_(e;b) near Ω″ and w ∈ H^((𝗌;k))(Ω″)^(•,−),

    ‖(D^j_[b] ℓ)(D^(k−j)_[b] w)‖_(H^𝗌(Ω′)^(•,−))
        ≤ C_k (‖ℓ‖_((d_0;d̃)) ‖w‖_(H^((𝗌;k))(Ω″)^(•,−)) + ‖ℓ‖_((d_0;k)) ‖w‖_(H^((𝗌;d̃))(Ω″)^(•,−))),

with D_[b] the schematic notation of [[sec:ii-a-9]] and C_k depending also on δ.

(c) (*Norms through words, with room.*) Let 𝒳 = (X_1, …, X_J), X_J = I, be b-differential operators of order 1
spanning 𝒱_b over a neighbourhood of Ω″, and for a word γ = (γ_1, …, γ_q) ∈ {1, …, J}^q put X^γ := X_(γ_1) ⋯ X_(γ_q)
and |γ| := q. Then ‖X^γ w‖_(H^𝗌(Ω″)^(•,−)) ≤ C ‖w‖_(H^((𝗌;|γ|))(Ω″)^(•,−)), and, for Ω′ ⊂ Ω″ nested with room,

    ‖w‖_(H^((𝗌;k))(Ω′)^(•,−)) ≤ C_k Σ_(|γ|≤k) ‖X^γ w‖_(H^𝗌(Ω″)^(•,−)).

This is [Hin26c, Lemmas 8.7–8.8] in dimension 4 + 1.

*Proof.* (a) Extend the coefficients by Seeley's operator across the final faces of Ω′ (in t^♭, resp. r, with the other
coordinates as parameters, and successively near the corner, where dt^♭ and dr are independent), as in
[[lem:ii-e-1-2]]. The extension is bounded on C^((d_0;k))_(e;b) for all d_0 and k ([Hin26c, Lemma 8.5 (2)], whose proof
is that of [[lem:ii-e-1-3]] (b) with suprema in place of L²-norms: the reflection commutes with the tangential fields,
and j derivatives in the normal variable cost Σ_l |c_l| ε_l^(−j)). Call the extended operator Q^♯. If w̃ extends w and
is supported in {t^♭ ≥ T_0}, then χQ^♯w̃ extends Qw, for a cut-off χ equal to 1 near Ω′, and is supported there;
[[lem:ii-a-8-6]] (a) bounds it. Take the infimum over w̃. The case (−,•) is the same with the initial face.

(b) Let χ_3 be a cut-off equal to 1 near Ω′, supported in the union of {t^♭ < T_0} and of the interior of Ω″ relative to
its final faces, with bounded b-derivatives. For w ∈ H^((𝗌;k))(Ω″)^(•,−) the distribution z := χ_3 w̃ does not depend
on the extension w̃ supported in {t^♭ ≥ T_0}, as all such extensions agree where χ_3 ≠ 0. So, taking w̃ minimal for the
norm of order (𝗌;i), ‖z‖_((𝗌;i)) ≤ C_i ‖w‖_(H^((𝗌;i))(Ω″)^(•,−)) for every i, with the same z ([[lem:ii-a-8-4]] (a) for
multiplication by χ_3). z extends w|_(Ω′). Let ℓ^♯ be the Seeley extension of ℓ, and χ_1, χ_2 cut-offs equal to 1 near
Ω′ with χ_2 = 1 near supp χ_1 and χ_3 = 1 near supp χ_2. Then χ_1 (D^j_[b] ℓ^♯)(D^(k−j)_[b] z) extends
(D^j_[b] ℓ)(D^(k−j)_[b] w), and [[prop:ii-a-9-6]] with B = χ_1 and B^♯ = χ_2 bounds its H^𝗌-norm by the right side, the
terms with ‖χz‖_((𝗌_0;·)) being bounded by those with 𝗌.

(c) The first bound holds as X^γ w̃ extends X^γ w. For the second, with z as in (b), ‖z‖_((𝗌;k)) is equivalent to
Σ_(|γ|≤k) ‖X^γ z‖_𝗌 ([[eq:ii-a-8-1]] and [[sec:ii-a-9]]: two spanning sets give equivalent norms), and by the Leibniz
rule for words X^γ z is a sum of terms χ′ X^β w̃ with |β| ≤ |γ| and χ′ a b-derivative of χ_3, supported where χ_3 is;
each such term is independent of the extension, and its H^𝗌-norm is at most C ‖X^β w‖_(H^𝗌(Ω″)^(•,−)). ∎

[Hin26c, Lemma 8.8 (3)] proves (b) on Ω′ itself, with a crude bound in the middle range of j through the extension
operator of its Lemma 8.7 on integer b-Sobolev spaces, and notes in its footnote 64 that no single extension operator
respects all variable orders. With room, the cut-off χ_3 is such an operator. Room is always available below, as every
slab sits inside a larger one on which P (or P^ext) is given.

#### The commuted system on slabs {#sec:ii-e-4-2}

On {r ≥ r^♯} ∩ {1/2 ≤ t_* ≤ t̄} let

    𝒳_sl := (V_1, V_2, Ω_12, …, Ω_34, I),        V_1 := 2t_* ∂_(t_*),     V_2 := x_I∂_(x_I) = −2r∂_r,

with Ω_ab the rotation fields of 𝕊³, as in [[sec:ii-d1-3]]. It spans 𝒱_b there: near ℐ⁺ the b-vector fields are spanned
by ∂_(t_*), x_I∂_(x_I) and ∂_ω; elsewhere, as r ≥ r^♯ > 0 and t_* ≥ 1/2, ∂_(t_*) = (2t_*)⁻¹ V_1, ∂_r = −(2r)⁻¹ V_2, and
the Ω_ab span the tangent fields of the spheres. Put W := x_I² t_*⁻¹, which near ℐ⁺ is the weight x′_I² ρ_+² of
[[sec:ii-d1-3]], and L := W⁻¹P.

**Lemma {#lem:ii-e-4-2}** (The commutators on slabs.) For P of class ((d_0;k),(2ℓ_I,ℓ_+,ℓ_K)), the family 𝒳_sl
satisfies condition (C) of [[sec:ii-d1-2]] on the region above with R_i = 0: [L, X_i] = Σ_j Q_ij X_j, where Q_ij is
the sum of an operator of order 0 with bounded coefficients and a first-order edge operator whose coefficients lie in
C^((d_0;k−1))_(e;b) and, near ℐ⁺, in x_I C^∞ + x_I^(2ℓ_I) C^((d_0;k−1))_(e;b).

This is [Hin26c, Lemma 7.12] on slabs.

*Proof.* Near ℐ⁺ this is [[lem:ii-d1-3-1]] (b), whose proof uses only [[lem:ii-c-3-4]] near ℐ⁺ ∩ Ω, which holds at
finite times. Away from ℐ⁺, [L, X_i] is a second-order operator with coefficients in C^((d_0;k−1)), as X_i
differentiates the coefficients once; writing each coordinate field as Σ_j c_j X_j with smooth c_j gives the form
Σ_j Q_ij X_j, the first-order part of [L, X_i] going into Q_iJ X_J. Patch the two representations with a partition of
unity in x_I. ∎

Consequently, by [[lem:ii-d1-2-1]] in its case without loss of derivatives (the case of the radial sets) and with
R_i = 0, for u on a slab and f := Pu the words u^(j) := (X^γ u)_(γ∈𝒲_j) satisfy

    P^(j) u^(j) = W (X^γ(W⁻¹ f))_γ + W f̃^(j),        P^(j) := W L^(j) = P ⊗ Id − W Q^(j),                {#eq:ii-e-4-1}

with Q^(j) the coupling of [[eq:ii-d1-2-2]] and f̃^(j)_γ = −Σ_(|S|≥2) (ad_(X_S) L) X^(γ∖S) u, the sum over sets S of
positions in γ, X^(γ∖S) the word with those letters deleted, and ad_(X_S) the iterated commutator. P^(j) acts on
𝒲_j-tuples of sections. It has the principal symbol of P; its first-order coupling W Q^(j) has coefficients
O(x_I^(2+min(1,2ℓ_I))) near ℐ⁺, so its normal form at ℐ⁺, [[eq:ii-e-1-1]], has the same p_1 as P ⊗ Id (its
zeroth-order part, of size O(x_I²), changes p_0, which is never used), and its principal symbol of order 1 vanishes at
R. So P^(j) satisfies everything [[sec:ii-e-2]] and [[sec:ii-e-3]] use, with the same margins, and [[prop:ii-e-3-4]]
holds for it (by the last paragraph of its proof), with constants depending on finitely many coefficient norms of
W Q^(j), which carry at most one b-derivative of those of P ([[lem:ii-d1-2-1]]). As
X^γ(W⁻¹f) = W⁻¹ Π_i (X_(γ_i) + c_(γ_i)) f with constants c_i = −X_i log W ∈ {2, −2, 0}, the first term on the right of
[[eq:ii-e-4-1]] is a word in shifted fields applied to f.

**Proposition {#prop:ii-e-4-3}** (b-regularity on slabs.) Let α < −1/2 + p̄_1, Ω′ = Ω_(T_0,T_1) with T_0 ≥ 1, 𝗌 a slab
order and k ∈ ℕ_0. There is d_0, depending only on 𝗌, such that for P of class ((d_0;k),(2ℓ_I,ℓ_+,ℓ_K)) with
‖P − P_0‖_((d_0;k),(2ℓ_I,ℓ_+,ℓ_K)) small, the forward solution of Pu = f satisfies

    ‖u‖_(H^((𝗌;k),2α)(Ω′)^(•,−)) ≤ C_k ‖f‖_(H^((𝗌−1;k),2α+2)(Ω′)^(•,−)),                               {#eq:ii-e-4-2}

uniformly for such P.

This is [Hin26c, Proposition 8.6] in dimension 4 + 1.

*Proof.* Let Ω″ := Ω^♯_(T_0,T_1), nested around Ω′ with room; let f″ be the restriction to Ω″ of the minimal
extension of f in H^((𝗌−1;k),2α+2)_e, and u″ the forward solution on Ω″ of P^ext u″ = f″ ([[prop:ii-e-3-4]]). By
uniqueness u″|_(Ω′) = u. We show by induction on j ≤ k that

    Σ_(|γ|≤j) ‖X^γ u″‖_(H^(𝗌,2α)(Ω″)^(•,−)) ≤ C_j ‖f″‖_(H^((𝗌−1;j),2α+2)(Ω″)^(•,−)).                     {#eq:ii-e-4-3}

j = 0 is [[eq:ii-e-3-4]]. Let j ≥ 1. Each b-vector field maps H^(𝗍,2β)_e into H^(𝗍−1,2β−1)_e (as
∂_ω = x_I⁻¹ x_I∂_ω), so a priori u″^(j) ∈ H^(𝗌−j,2α−j)(Ω″)^(•,−). The threshold holds also for the weight α − j/2, so by
[[prop:ii-e-3-4]] (i) for P^(j) at that weight, u″^(j) is the forward solution of [[eq:ii-e-4-1]], which by
[[prop:ii-e-3-4]] (ii) at the weight α lies in H^(𝗌,2α)(Ω″)^(•,−), with norm at most C times that of the right side of
[[eq:ii-e-4-1]] in H^(𝗌−1,2α+2)(Ω″)^(•,−). The first term of the right side has norm at most C‖f″‖_((𝗌−1;j)), by
[[lem:ii-e-4-1]] (c). For f̃^(j), let |S| = q ≥ 2. W ad_(X_S) L is a second-order edge operator with coefficients in
C^((d_0;j−q))_(e;b), as each commutator with an element of 𝒳_sl preserves Diff²_e ([[lem:ii-a-2-6]] near ℐ⁺) and
differentiates the coefficients once, and W(ad_(X_S) L)W⁻¹ differs from it by lower order. Every edge vector field is a
combination of the X_i with bounded coefficients (x_I∂_ω = x_I · ∂_ω), so W ad_(X_S) L = Σ_i A_i X_i with A_i
first-order edge operators with C^((d_0;j−q)) coefficients, and by [[lem:ii-e-4-1]] (a)

    ‖W (ad_(X_S) L) X^(γ∖S) u″‖_(H^(𝗌−1,2α+2)) ≤ C Σ_i ‖X_i X^(γ∖S) u″‖_(H^(𝗌,2α)),

a sum over words of length j − q + 1 ≤ j − 1, bounded by [[eq:ii-e-4-3]] at j − 1. This proves [[eq:ii-e-4-3]] at j,
the order staying 𝗌, so that d_0 depends only on 𝗌. Finally, by [[lem:ii-e-4-1]] (c) with room,
‖u‖_(H^((𝗌;k))(Ω′)) ≤ C_k Σ_(|γ|≤k) ‖X^γ u″‖_(H^𝗌(Ω″)) ≤ C_k ‖f″‖ ≤ C_k ‖f‖. ∎

*The extension in the tame estimates.* A tame bound controls a low and a high b-regularity of one function at once, so
its proof needs one extension of the right-hand side f across the final faces of the slab that is nearly minimal for
the norms of every order (𝗌 − 1; j) at once; the minimal extension used in the proof of [[prop:ii-e-4-3]] is minimal
for one norm only. Across {r = r_0}, where Ω_* ends and no room is available, the extension of [[lem:ii-f1-2-5]]
provides it when the order is constant near {r ≤ r_0} with value a nonnegative integer there: it is a Seeley extension
in r at fixed (t^♭, ω), glued to any extension away from {r = r_0}, and it is bounded at every order of b-regularity at
once. Its construction uses nothing from this section, so the reference is not circular. Across the time-final face
{t^♭ = T_1} the right-hand side is, wherever the tame estimates below are applied (in [[thm:ii-e-6-1]], in
[[sec:ii-f1-3]] and [[sec:ii-f1-4]], and in the proof of [[thm:ii-f-8-1]]), the restriction to the slab of one given on
a larger slab, and the cut-off χ_3 of the proof of [[lem:ii-e-4-1]] (b) provides the extension there
[[pending:issue-2]]. The orders of [[lem:ii-f1-2-3]], at which [[eq:ii-e-4-4]], [[eq:ii-e-5-6]] and [[eq:ii-e-6-2]] are
applied, are constant near {r ≤ r_0}, with a nonnegative integer value there.

**Proposition {#prop:ii-e-4-4}** (Tame estimates on slabs.) In the setting of [[prop:ii-e-4-3]], let 𝗌 be constant near
{r ≤ r_0}, with value a nonnegative integer there [[pending:issue-1]]. There is d ∈ ℕ, depending only on 𝗌, such that
for all k and all P of class ((d_0;k),(2ℓ_I,ℓ_+,ℓ_K)) with ‖P − P_0‖_((d_0;d),(2ℓ_I,ℓ_+,ℓ_K)) small,

    ‖u‖_(H^((𝗌;k),2α)(Ω′)^(•,−))
        ≤ C_k (‖f‖_(H^((𝗌−1;k),2α+2)(Ω′)^(•,−)) + ε_(P,k) ‖f‖_(H^((𝗌−1;d),2α+2)(Ω′)^(•,−))),               {#eq:ii-e-4-4}

with ε_(P,k) := ‖P − P_0‖_((d_0;k),(2ℓ_I,ℓ_+,ℓ_K)), which may be taken over a neighbourhood of Ω′, and C_k depending on P
only through a bound for ε_(P,d).

This is [Hin26c, Proposition 8.9] in dimension 4 + 1. [Hin26c] states it for "s ∈ ℕ an admissible order function"; the
proof uses only what [[prop:ii-e-4-3]] uses, together with the extension just described.

*Proof.* Let d̃ and the regularity of [[prop:ii-a-9-6]] be those of [[lem:ii-e-4-1]] (b) at the orders 𝗌 + 1 and
𝗌 − 1, and d := d̃ + 3. For k ≤ d, [[eq:ii-e-4-4]] is [[eq:ii-e-4-2]], whose constant depends on ε_(P,k) ≤ ε_(P,d).
For k > d, let Ω″ := Ω^♯_(T_0,T_1) and u″ be as in the proof of [[prop:ii-e-4-3]], with f″ now the restriction to Ω″ of
the extension of f described before the statement, so that ‖f″‖_((𝗌−1;j)) ≤ C_j ‖f‖_((𝗌−1;j)) for every j at once.
Run the induction of [[prop:ii-e-4-3]] on nested slabs

    Ω′ ⊂ Ω_(2k) ⊂ Ω_(2k−1) ⊂ ⋯ ⊂ Ω_(0) = Ω″,

with room 2^(−i−2) min(1, r_0 − r^♯) between Ω_(i) and Ω_(i−1), two slabs per step: step j proves the bound
[[eq:ii-e-4-3]] on Ω_(2j) in the tame form C_j(‖f″‖_((𝗌−1;j)) + ε_(P,j) ‖f″‖_((𝗌−1;d))). The coefficients of P^(j) carry
at most one b-derivative of those of P, so the constant of [[prop:ii-e-3-4]] for P^(j) depends on ε_(P,d) only. In
f̃^(j) write L = L_0 + (L − L_0), L_0 the operator of P_0. The terms of L_0, and those of L − L_0 in which at most 2
b-derivatives fall on the coefficients, are bounded as in [[prop:ii-e-4-3]] by norms of u″ with at most j − 1 words, on
Ω_(2j−2), with constants depending on ε_(P,2); by the induction hypothesis they are tame. In the others, q′ ≥ 3
b-derivatives fall on a coefficient p of P − P_0. As in [[lem:ii-d1-2-4]] (b) and [Hin26c, (7.55)–(7.56)], commute the
second-order factor to the front; it remains to bound

    ‖(D^(q′)_[b] D^(≤2)_e p)(D^(j−q)_[b] u″)‖_(H^(𝗌+1)(Ω_(2j))),     q′ ≤ q.

[[lem:ii-e-4-1]] (b) on Ω_(2j) ⊂ Ω_(2j−1), with D²_[b] D^(≤2)_e p in the place of ℓ and (q′ − 2, j − q + q′ − 2) in the
place of (j, k), bounds it by

    C_j (‖p‖_((d_1+2;d̃+2)) ‖u″‖_((𝗌+1;j−2)) + ‖p‖_((d_1+2;j)) ‖u″‖_((𝗌+1;d̃)))

on Ω_(2j−1), with d_1 the regularity of [[lem:ii-e-4-1]] (b) and d_0 ≥ d_1 + 2. Here ‖u″‖_((𝗌+1;j−2)) ≤ C‖u″‖_((𝗌;j−1))
on Ω_(2j−1) ([[lem:ii-a-8-4]] (d), on slab spaces by taking extensions), which [[lem:ii-e-4-1]] (c) bounds by the words
of length at most j − 1 on the larger slab Ω_(2j−2), tame by step j − 1;
‖u″‖_((𝗌+1;d̃)) ≤ C‖u″‖_((𝗌;d̃+1)) ≤ C‖f″‖_((𝗌−1;d̃+1)) by [[eq:ii-e-4-2]] at d̃ + 1 < d; and
‖p‖_((d_1+2;d̃+2)) ≤ Cε_(P,d), ‖p‖_((d_1+2;j)) ≤ Cε_(P,j). The finitely many nested slabs used for a given k make C_k
depend on k only. Conclude with [[lem:ii-e-4-1]] (c) and the bound on f″. ∎

### The black hole interior {#sec:ii-e-5}

The region {r_0 ≤ r ≤ r^♮} at late times is unbounded in time: its closure meets K⁺. There dr is timelike, and −r
serves as a time function. The estimates of [[sec:ii-e-2]]–[[sec:ii-e-4]] hold there with −r in place of t^♭, with no
radial set and no threshold; this is [Hin26c, Section 8.2] in dimension 4 + 1.

#### r-slabs {#sec:ii-e-5-1}

By [[lem:ii-e-1-2]] (iv) there is δ_♮ > 0 such that dr is future timelike for the metric of P^ext on
{r^♯ ≤ r ≤ r^♮ + δ_♮} ∩ {t^♭ ≥ 1 − η_0}. For T_0 ≥ 1 − η_0/2 and r^♯ ≤ a < b ≤ r^♮ + δ_♮ the **r-slab** is

    Ω^K_([a,b]) := {t^♭ ≥ T_0, a ≤ r ≤ b},

with T_0 understood and P^ext in place of P where P is not given. Its faces in M° are {t^♭ = T_0} and {r = b}, which are
initial, and {r = a}, which is final: future causal vectors point into it across the first two and out of it across the
last, as ∇t^♭ is past and ∇r future timelike, and dt^♭, dr are independent where the faces meet. Its closure meets ∂M
only in K⁺ ∩ {a ≤ r ≤ b}. There, in the coordinates (ρ_K = t_*⁻¹, x), the e3b-vector fields are spanned by
∂_(t_*) = −ρ_K² ∂_(ρ_K) and ∂_x, and the b-vector fields by t_*∂_(t_*) and ∂_x ([[sec:ii-a-1]]; [Hin26c] calls these
spaces cusp spaces). Only the weight at K⁺ matters, and near the r-slabs we write

    H^(𝗌,α_K)_K := H^(𝗌,(0,0,α_K))_(e3b),        H^((𝗌;k),α_K)_K := H^((𝗌;k),(0,0,α_K))_(e3b;b),

with the density |dg|, a smooth positive multiple of |dt_* dx| there. So ‖u‖_(H^(1,α_K)_K) is equivalent to the
L²-norm of t_*^(α_K)(|u| + |∂_(t_*)u| + |∂_x u|). [Hin26c] glosses the left side of its (8.38) as controlling
t_*^(−α_K) u; with its multiplier ρ_K^(−2α_K)∇r and (8.39) the norm is that of ρ_K^(α_K) L², which controls
t_*^(α_K) u = ρ_K^(−α_K) u.

Let U^K := M° ∩ {r > a}, V^K := M° ∩ {t^♭ > T_0, r < b} and U^K_0 := M° ∩ {a < r < b}, and define, with quotient norms,

    H^(𝗌,α_K)(Ω^K_([a,b]))^(•,−) := {u|_(U^K) : u ∈ H^(𝗌,α_K)_K, supp u ⊂ {t^♭ ≥ T_0, r ≤ b}},
    H^(𝗌,α_K)(Ω^K_([a,b]))^(−,•) := {v|_(V^K) : v ∈ H^(𝗌,α_K)_K, supp v ⊂ {r ≥ a}},
    H^(𝗌,α_K)(Ω^K_([a,b]))^•    := {u|_(U^K_0) : u ∈ H^(𝗌,α_K)_K, supp u ⊂ {t^♭ ≥ T_0}},

and the mixed spaces of order (𝗌;k) likewise. The first are the spaces of forward problems, the second those of backward
problems; the third is supported at {t^♭ = T_0} only and extendible at both r-faces, the space of the continuation
estimates. D(Ω^K_([a,b])) is the set of restrictions to U^K of functions in C_c^∞(M°) supported in
{t^♭ > T_0, r < b}, and D_*(Ω^K_([a,b])) that of restrictions to V^K of functions in C_c^∞(M°) supported in {r > a}.
Both consist of functions vanishing near K⁺.

[[lem:ii-e-1-3]] holds for r-slabs, with these changes in its proof. The collar field is Z := ∇t^♭:
Z t^♭ = G(dt^♭) < 0, and Z r = g⁻¹(dt^♭, dr) > 0, as ∇t^♭ is past and ∇r future timelike. Near K⁺, Z is a stationary
vector field in (t_*, x) plus one with coefficients O(ρ_K^(ℓ_K)), so its flow changes t_* by a bounded amount in bounded
time and is bounded on H^(m,α_K)_K, uniformly for bounded times, and strongly continuous. −Z moves supports in
{t^♭ ≥ T_0, r ≤ b} into {t^♭ > T_0, r < b}, and Z moves supports in {r ≥ a} into {r > a}. Seeley's operator is applied
first across {r = b} in the variable r, with (t_*, ω) as parameters, and then across {t^♭ = T_0} in the collar
coordinates of Z, with collar width η_0/2; along a collar line r increases as t^♭ decreases, so the extension of a
function vanishing on {r < a} vanishes there. For density, one cuts off also at large times by 1 − χ_0(t_*/T),
T → ∞, whose derivative along ∂_(t_*) is O(T⁻¹) and along ∂_x is zero.

#### Energy estimates {#sec:ii-e-5-2}

**Lemma {#lem:ii-e-5-1}** (Energy estimates on r-slabs.) Let α_K ∈ ℝ and Ω^K := Ω^K_([a,b]). There is C, uniform for
ε_P small with d_0 = 2 (the norm of P − P_0 with the weights (0, 0, ℓ_K) suffices), such that

    ‖u‖_(H^(1,α_K)(Ω^K)) ≤ C ‖Pu‖_(H^(0,α_K)(Ω^K)),          u ∈ D(Ω^K),
    ‖v‖_(H^(1,−α_K)(Ω^K)) ≤ C ‖P*v‖_(H^(0,−α_K)(Ω^K)),       v ∈ D_*(Ω^K).                              {#eq:ii-e-5-1}

Here H^(1,β)(Ω^K) and H^(0,β)(Ω^K) are the L²(Ω^K, |dg|)-norms of t_*^β(|u| + |∂_(t_*)u| + |∂_x u|) and of t_*^β u,
and P* is the adjoint for |dg| and a fixed smooth fibre inner product h_K. The same holds on Ω^K ∩ {t^♭ ≤ T_1}, with
{t^♭ = T_1} a further final face.

This is [Hin26c, Lemma 8.10] in dimension 4 + 1.

*Proof.* Let w := t_*^(2α_K) = ρ_K^(−2α_K), Y_r := ∇r/|G(dr)|, which is future timelike with Y_r(−r) = 1, and
|ζ|² := ζ_(t_*)² + |ζ_x|² for covectors ζ = ζ_(t_*) dt_* + ζ_x dx. On the r-slab, by stationarity of g_0, compactness
in x and the decay of g − g_0, there are constants, uniform for ε_P small with d_0 = 2, with: |div_g Y_r| ≤ C_0 and
|Y_r log w| = 2|α_K| |Y_r t_*|/t_* ≤ C_1; T(∇r, ∇r)(ζ) ≥ c_r |ζ|², by [[lem:ii-e-2-2]]; and
|K_(w^(±1)∇r)(ζ)| ≤ C_3 w^(±1) |ζ|², by the formula for K_(fX) in [[lem:ii-e-2-1]], as |∇w| ≤ Cw and ∇r has bounded
first derivatives. P − P_□ is of first order with bounded coefficients in the frame ∂_(t_*), ∂_x, so for any vector
field X with |X| ≤ C_X f, |2 Re⟨(P − P_□)u, Xu⟩| ≤ C_4 f (|du|² + |u||du|), with C_4 depending on C_X and h_K only.

*Forward.* Let X := e^(2Φr) w ∇r, which is future timelike. By [[lem:ii-e-2-1]],

    K_X = e^(2Φr) (K_(w∇r) + 2Φ w T(∇r, ∇r)) ≥ e^(2Φr) w (2Φ c_r − C_3) |ζ|².

Apply [[eq:ii-e-2-1]] on O := Ω^K to u ∈ D(Ω^K), which has compact support in Ō. The only face near which u ≠ 0 is
{r = a} (and {t^♭ = T_1}), where ∇φ = ∇r (resp. −∇t^♭) is future timelike; with X future timelike the boundary term is
≥ 0 by [[lem:ii-e-2-2]]. So

    ∫ e^(2Φr) w (4Φ c_r − 2C_3 − C_4) |du|² ≤ 2 Re ∫ ⟨Pu, Xu⟩ + C_4 ∫ e^(2Φr) w |u||du|
                                          ≤ C_5 ∫ e^(2Φr) w |Pu||du| + C_4 ∫ e^(2Φr) w |u||du|.

[[lem:ii-e-2-3]] with Y = Y_r, τ := −r, the weight w and Φ ≥ C_0 + C_1 applies, as u vanishes near the faces with
Y_r φ > 0, namely {t^♭ = T_0} (Y_r φ = dt^♭(Y_r) > 0) and {r = b} (Y_r φ = −dr(Y_r) = 1); it gives

    ∫ e^(2Φr) w |u|² ≤ 4Φ⁻² ∫ e^(2Φr) w |Y_r u|² ≤ C_6 Φ⁻² ∫ e^(2Φr) w |du|².

With the Cauchy–Schwarz inequality the last term above is at most C_4 C_6^(1/2) Φ⁻¹ ∫ e^(2Φr) w |du|², and
C_5 |Pu||du| ≤ Φ c_r |du|² + C_5² (4Φ c_r)⁻¹ |Pu|². Fix Φ large: ∫ e^(2Φr) w |du|² ≤ C ∫ e^(2Φr) w |Pu|². As e^(2Φr)
lies between e^(2Φa) and e^(2Φb), this and the Poincaré inequality give the first estimate [[eq:ii-e-5-1]].

*Backward.* Let X_* := −e^(−2Φr) w⁻¹ ∇r, which is past timelike. By [[lem:ii-e-2-1]],

    K_(X_*) = e^(−2Φr) (−K_(w⁻¹∇r) + 2Φ w⁻¹ T(∇r, ∇r)) ≥ e^(−2Φr) w⁻¹ (2Φ c_r − C_3) |ζ|².

For v ∈ D_*(Ω^K) the faces near which v ≠ 0 are {t^♭ = T_0} and {r = b}, with ∇φ = ∇t^♭, resp. −∇r, past timelike, so
the boundary terms 2T(X_*, ∇φ)(dv) are ≥ 0 by [[lem:ii-e-2-2]]. P* = P_□ + (P* − P_□), with P* − P_□ of first order
with bounded coefficients. [[lem:ii-e-2-3]] in the reverse direction, with the weight w⁻¹, applies, as v vanishes near
{r = a} (and {t^♭ = T_1}), the only faces with Y_r φ < 0. The rest is as before. ∎

#### Solvability, uniqueness and continuation {#sec:ii-e-5-3}

A **slab order on an r-slab** is 𝗌 ∈ C^∞(^(e3b)S*M) with ±𝖧𝗌 ≤ 0 on ∂Σ^± over it. Admissible order functions are slab
orders on the r-slabs inside Ω_*, by [[prop:ii-c-5-1]] (2); so are constants.

**Lemma {#lem:ii-e-5-2}** (The flow in the interior.) There is c > 0 such that, over
{r^♯ ≤ r ≤ r^♮ + δ_♮} ∩ {t^♭ ≥ 1 − η_0}, up to K⁺ and for ε_P small, 𝖧r ≤ −c on ∂Σ^+ and 𝖧r ≥ c on ∂Σ^−. So r
decreases strictly along the future field, at a rate bounded below, and there is no radial set and no trapping there.

*Proof.* 𝖧 = ρH_G with ρ a positive defining function of fibre infinity, homogeneous of degree −1, and
H_G r = 2g⁻¹(ζ, dr). On ∂Σ^+ the future field is 𝖧 ([[sec:ii-c-2-3]]): the projection of H_G there, 2g⁻¹(ζ, ·), is
future null, so g⁻¹(ζ, dr) = g(ζ^♯, ∇r) < 0, ∇r being future timelike. On ∂Σ^− the signs reverse. ρ g⁻¹(ζ, dr) is
homogeneous of degree 0 and continuous on the compactified cosphere bundle over the closure of the region, up to K⁺,
where it is that of the stationary metric g_0; it does not vanish on the characteristic set, which is compact. ∎

**Lemma {#lem:ii-e-5-3}** (Regularity on r-slabs.) (a) Let r^♯ ≤ a′ < a < b < r^♮ + δ_♮,
Ω_1 := Ω^K_([a,b]) ⊂ Ω_2 := Ω^K_([a′,b]), let 𝗌_0 < 𝗌 be slab orders, and let u ∈ H^(𝗌_0,α_K)(Ω_2)^(•,−) with
Pu ∈ H^(𝗌−1,α_K)(Ω_2)^(•,−). Then u|_(Ω_1) ∈ H^(𝗌,α_K)(Ω_1)^(•,−) and

    ‖u‖_(H^(𝗌,α_K)(Ω_1)^(•,−)) ≤ C (‖Pu‖_(H^(𝗌−1,α_K)(Ω_2)^(•,−)) + ‖u‖_(H^(𝗌_0,α_K)(Ω_2)^(•,−))).

(b) Let δ > 0 with T_0 − δ ≥ 1 − η_0 and b + δ ≤ r^♮ + δ_♮, let Ω_3 be the r-slab {t^♭ ≥ T_0 − δ, a ≤ r ≤ b + δ},
let s_0 < s be constants, and let v ∈ H^(s_0,−α_K)(Ω_3)^(−,•) with P*v ∈ H^(s−1,−α_K)(Ω_3)^(−,•). Then
v|_(Ω_1) ∈ H^(s,−α_K)(Ω_1)^(−,•), with the corresponding estimate.

Both hold for systems P ⊗ Id − Q, Q of first order, with constants depending on finitely many coefficient norms; they
are uniform for ε_P small, with d_0 depending only on the orders.

*Proof.* (a) Let ũ be an extension of u supported in {t^♭ ≥ T_0, r ≤ b} and f one of Pu; that Pu lies in
H^(𝗌−1,α_K)(Ω_2)^(•,−) means Pũ = f on U_2 := M° ∩ {r > a′}, which contains the region outside the initial faces. Let
χ_1 be a cut-off equal to 1 near Ω_1 and supported in {r > (a + a′)/2}, and carry all operators by such cut-offs. Off
the characteristic set use the elliptic estimate ([[thm:ii-a1-3-1]]). On it, by [[lem:ii-e-5-2]], the backward curve
from any point over supp χ_1 has r increasing at a rate at least c, so within parameter time (b − a′ + 1)/c it reaches
{r > b} or, earlier, {t^♭ < T_0}, where ũ = 0, staying in {r > (a + a′)/2}; this holds also over K⁺. Propagation
([[thm:ii-a1-5-4]], at the order 𝗌, with 𝖧𝗌 ≤ 0 along the future field) controls ũ at every such point. Finitely many
of these operators are jointly elliptic over supp χ_1, and [[lem:ii-a-8-4]] (c) gives

    ‖χ_1 ũ‖_𝗌 ≤ C (‖χ_1′ f‖_(𝗌−1) + ‖χ_1′ ũ‖_(𝗌_0))

with χ_1′ supported in U_2, which is (a) after taking infima over the extensions.

(b) The same with the future field: let ṽ extend v with support in {r ≥ a}; P*ṽ is controlled on
V_3 := M° ∩ {t^♭ > T_0 − δ, r < b + δ}; forward curves from points over Ω_1 reach {r < a}, where ṽ = 0, within bounded
time, staying in V_3, as t^♭ increases and r decreases along them. Propagation for −P* applies to constant orders. For
systems the principal symbol is scalar and the coupling of lower order, which the elliptic and real principal type
estimates allow. ∎

**Proposition {#prop:ii-e-5-4}** (Solvability, uniqueness and continuation on r-slabs.) Let α_K ∈ ℝ,
T_0 ≥ 1 − η_0/2, r^♯ < a < b ≤ r^♮, and 𝗌 a slab order. There are d_0, depending only on 𝗌, and C, uniform for ε_P
small, such that:

(i) (*uniqueness*) if u ∈ H^(s′,α_K)(Ω^K_([a,b]))^(•,−) for some s′ ∈ ℝ and Pu = 0, then u = 0;

(ii) (*existence*) for every f ∈ H^(𝗌−1,α_K)(Ω^K_([a,b]))^(•,−) there is u ∈ H^(𝗌,α_K)(Ω^K_([a,b]))^(•,−) with Pu = f
and

    ‖u‖_(H^(𝗌,α_K)(Ω^K_([a,b]))^(•,−)) ≤ C ‖f‖_(H^(𝗌−1,α_K)(Ω^K_([a,b]))^(•,−));                     {#eq:ii-e-5-2}

(iii) (*continuation*) for a < a⁺ < b, every u ∈ H^(s′,α_K)(Ω^K_([a,b]))^•, s′ ∈ ℝ, with
Pu ∈ H^(𝗌−1,α_K)(Ω^K_([a,b]))^• satisfies, in the strong sense,

    ‖u‖_(H^(𝗌,α_K)(Ω^K_([a,b]))^•)
        ≤ C (‖Pu‖_(H^(𝗌−1,α_K)(Ω^K_([a,b]))^•) + ‖u‖_(H^(𝗌,α_K)(Ω^K_([a⁺,b]))^•)).                     {#eq:ii-e-5-3}

The same holds for P* and backward problems at constant orders, and for systems P ⊗ Id − Q with Q of first order.

This is [Hin26c, Proposition 8.11 and (8.40)] in dimension 4 + 1.

*Proof.* (i) and (ii) are proved as [[prop:ii-e-3-4]], with [[lem:ii-e-5-1]] in place of [[eq:ii-e-2-4]],
[[lem:ii-e-5-3]] in place of [[lem:ii-e-3-3]], and the r-slab form of [[lem:ii-e-1-3]]. For (i),
Ω_δ := Ω^K_([a+δ,b]), and D(Ω_δ) is dense in H^(2,α_K)(Ω_δ)^(•,−). For Step 1 of (ii), Ω^♯ := Ω^K_([a−δ_1,b]),
δ_1 := min(1, a − r^♯), with P^ext; for Step 3, Ω_3 := {t^♭ ≥ T_0 − δ, a ≤ r ≤ b + δ} with δ := min(η_0/2, δ_♮), so
that b + δ ≤ r^♮ + δ_♮, and the backward estimate [[eq:ii-e-5-1]] on Ω_3. There is no threshold, so the weight is any
α_K, and P does not shift it.

(iii) Let δ_2 := (b − a⁺)/4 and χ = χ(r) equal 1 for r ≤ a⁺ + δ_2 and 0 for r ≥ b − δ_2. If ũ extends u with support
in {t^♭ ≥ T_0}, then χũ is supported in {t^♭ ≥ T_0, r ≤ b − δ_2}, so v := χu ∈ H^(s′,α_K)(Ω^K_([a,b]))^(•,−), and
Pv = g := χPu + [P, χ]u. [P, χ] is a first-order operator with coefficients supported in {a⁺ + δ_2 ≤ r ≤ b − δ_2}, so
by [[lem:ii-e-4-1]] (a), with a cut-off,

    ‖g‖_(H^(𝗌−1,α_K)(Ω^K_([a,b]))^(•,−))
        ≤ C (‖Pu‖_(H^(𝗌−1,α_K)(Ω^K_([a,b]))^•) + ‖u‖_(H^(𝗌,α_K)(Ω^K_([a⁺,b]))^•)).

By (i), v is the solution of (ii) with f := g, so ‖v‖_𝗌 ≤ C‖g‖_(𝗌−1), and in the strong sense, as (ii) produces a
solution in H^𝗌 whenever g ∈ H^(𝗌−1). As u = v on {r ≤ a⁺ + δ_2}, a partition of unity in r gives [[eq:ii-e-5-3]]. ∎

#### b-regularity and the tame estimates {#sec:ii-e-5-4}

On {r^♯ ≤ r ≤ r^♮ + δ_♮} ∩ {t_* ≥ 1/2}, with x = (x¹, …, x⁴) the Cartesian coordinates of [[def:ii-a-1-3]] (A), let

    𝒳_K := (V_1, …, V_5, I),        V_1 := t_* ∂_(t_*),     V_(1+j) := ∂_(x^j)  (j = 1, …, 4),

acting componentwise in a fixed trivialisation of the bundle. The V_i commute. They span 𝒱_b near the closures of the
r-slabs, as near (K⁺)° the b-vector fields are spanned by t_*∂_(t_*) and ∂_x and in M° by all vector fields; and every
e3b-vector field there is a combination of the V_i with bounded coefficients, as ∂_(t_*) = t_*⁻¹ V_1 with t_* ≥ 1/2.

**Lemma {#lem:ii-e-5-5}** (The commutators in the interior.) For P of class ((d_0;k),(2ℓ_I,ℓ_+,ℓ_K)), 𝒳_K satisfies
condition (C) of [[sec:ii-d1-2]] there, with W = 1 and R_i = 0: [P, X_i] = Σ_j Q_ij X_j, with Q_ij first-order
e3b-operators whose coefficients lie in C^((d_0;k−1))_(e3b;b) (a stationary part plus a part O(ρ_K^(ℓ_K))).

This is [Hin26c, (8.41)–(8.42)] in dimension 4 + 1.

*Proof.* In (t_*, x) write P = Σ a^(μν) ∂_μ ∂_ν + Σ b^μ ∂_μ + c, the coefficients of P_0 independent of t_* and smooth,
those of P − P_0 in ρ_K^(ℓ_K) C^((d_0;k))_(e3b;b) near K⁺ ([[def:ii-c-3-3]]). [P, ∂_(x^j)] has the coefficients
differentiated by −∂_(x^j); [P, t_*∂_(t_*)] = [P, t_*]∂_(t_*) − (t_*∂_(t_*) applied to the coefficients), with
[P, t_*] = 2 Σ_ν a^(t_* ν) ∂_ν + b^(t_*). In both cases a second-order operator in ∂_(t_*), ∂_x results, with
coefficients in C^((d_0;k−1))_(e3b;b), as V_i is a b-vector field. Write each second-order term ∂_μ ∂_ν as
∂_μ ∘ Σ_j c_(νj) V_j with c_(νj) ∈ {0, 1, t_*⁻¹}; this is Σ_j Q_ij V_j with Q_ij of first order. [P, I] = 0. ∎

By [[lem:ii-d1-2-1]] in its case without loss of derivatives and with R_i = 0, as in [[eq:ii-e-4-1]], for u on an
r-slab and f := Pu the words u^(j) := (X^γ u)_(γ∈𝒲_j) satisfy

    P^(j) u^(j) = (X^γ f)_γ + f̃^(j),     P^(j) := P ⊗ Id − Q^(j),
    f̃^(j)_γ = −Σ_(|S|≥2) (ad_(X_S) P) X^(γ∖S) u.                                                       {#eq:ii-e-5-4}

P^(j) is a system with scalar principal part and first-order coupling, whose coefficients carry at most one
b-derivative of those of P; [[lem:ii-e-5-1]], [[lem:ii-e-5-2]], [[lem:ii-e-5-3]] and [[prop:ii-e-5-4]] hold for it,
with no condition on the coupling, as on r-slabs every first-order term is absorbed by the factor Φ in
[[lem:ii-e-5-1]].

**Proposition {#prop:ii-e-5-6}** (b-regularity and tame estimates in the interior.) Let α_K, T_0 and
r^♯ < a < a⁺ < b ≤ r^♮ be as in [[prop:ii-e-5-4]], and 𝗌 a slab order.

(a) There is d_0, depending only on 𝗌, such that for all k ∈ ℕ_0 and P of class ((d_0;k),(2ℓ_I,ℓ_+,ℓ_K)) with ε_(P,k)
small, every u ∈ H^((s′;k),α_K)(Ω^K_([a,b]))^•, s′ ∈ ℝ, with f := Pu satisfies, in the strong sense,

    ‖u‖_(H^((𝗌;k),α_K)(Ω^K_([a,b]))^•)
        ≤ C_k (‖f‖_(H^((𝗌−1;k),α_K)(Ω^K_([a,b]))^•) + ‖u‖_(H^((𝗌;k),α_K)(Ω^K_([a⁺,b]))^•)).                {#eq:ii-e-5-5}

(b) If 𝗌 is constant near {r = a}, with value a nonnegative integer there [[pending:issue-1]], there is d ∈ ℕ,
depending only on 𝗌, such that for all k and P of that class with ε_(P,d) small,

    ‖u‖_((𝗌;k)) ≤ C_k (‖f‖_((𝗌−1;k)) + ‖u‖^([a⁺,b])_((𝗌;k))
                       + ε_(P,k) (‖f‖_((𝗌−1;d)) + ‖u‖^([a⁺,b])_((𝗌;d)))),                             {#eq:ii-e-5-6}

with the spaces of [[eq:ii-e-5-5]], the superscript marking the norm on Ω^K_([a⁺,b]), and C_k depending on P only
through a bound for ε_(P,d). Here ε_(P,k) may be the norm of P − P_0 over Ω^K_([a,b]) alone: on the room below
{r = a} used in the proof, P is replaced by the operator whose coefficients are the Seeley extensions across {r = a}
of those on Ω^K_([a,b]) (as in [[lem:ii-e-1-2]]), which agrees with P on the r-slab.

This is [Hin26c, Propositions 8.12 and 8.13] in dimension 4 + 1.

*Proof.* (a) *Reduction to a forward problem.* With χ and δ_2 as in the proof of [[prop:ii-e-5-4]] (iii), v := χu lies
in H^((s′;k),α_K)(Ω^K_([a,b]))^(•,−) and solves Pv = g := χf + [P, χ]u, and by [[lem:ii-e-4-1]] (a)

    ‖g‖_(H^((𝗌−1;k),α_K)(Ω^K_([a,b]))^(•,−))
        ≤ C_k (‖f‖_(H^((𝗌−1;k),α_K)(Ω^K_([a,b]))^•) + ‖u‖_(H^((𝗌;k),α_K)(Ω^K_([a⁺,b]))^•)).               {#eq:ii-e-5-7}

As u = v on {r ≤ a⁺ + δ_2}, it suffices to bound ‖v‖_((𝗌;k)) by C_k ‖g‖_((𝗌−1;k)).

*Induction.* Let Ω″ := Ω^K_([a−δ_1,b]), δ_1 := (1/2) min(1, a − r^♯), let g″ be the restriction to Ω″ of the minimal
extension of g, and let v″ be the forward solution of Pv″ = g″ on Ω″ ([[prop:ii-e-5-4]] (ii)); by uniqueness
v″|_(Ω^K_([a,b])) = v. We show by induction on j ≤ k that

    Σ_(|γ|≤j) ‖X^γ v″‖_(H^(𝗌,α_K)(Ω″)^(•,−)) ≤ C_j ‖g″‖_(H^((𝗌−1;j),α_K)(Ω″)^(•,−)).                    {#eq:ii-e-5-8}

j = 0 is [[eq:ii-e-5-2]]. Let j ≥ 1. A b-vector field maps H^(𝗍,β)_K into H^(𝗍−1,β−1)_K, as
t_*∂_(t_*) = ρ_K⁻¹ ∂_(t_*), so a priori v″^(j) ∈ H^(𝗌_−,α_K−j)(Ω″)^(•,−) for some order 𝗌_−. By [[prop:ii-e-5-4]] (i)
for P^(j) at the weight α_K − j, v″^(j) is the forward solution of [[eq:ii-e-5-4]], which by [[prop:ii-e-5-4]] (ii) at
the weight α_K lies in H^(𝗌,α_K)(Ω″)^(•,−), with norm at most C times that of the right side of [[eq:ii-e-5-4]] in
H^(𝗌−1,α_K)(Ω″)^(•,−). By [[lem:ii-e-4-1]] (c), ‖X^γ g″‖_(𝗌−1) ≤ C ‖g″‖_((𝗌−1;j)). For |S| = q ≥ 2, ad_(X_S) P is a
second-order e3b-operator with coefficients in C^((d_0;k−q))_(e3b;b), as each commutator with a V_i differentiates the
coefficients once ([[lem:ii-e-5-5]]); so it is Σ_i A_i X_i with A_i first-order e3b-operators, and by
[[lem:ii-e-4-1]] (a) ‖(ad_(X_S) P) X^(γ∖S) v″‖_(𝗌−1) ≤ C Σ_i ‖X_i X^(γ∖S) v″‖_𝗌, a sum over words of length
j − q + 1 ≤ j − 1, bounded by [[eq:ii-e-5-8]] at j − 1. This proves [[eq:ii-e-5-8]]. By [[lem:ii-e-4-1]] (c) with room,
‖v‖_((𝗌;k)) ≤ C_k Σ_(|γ|≤k) ‖X^γ v″‖_𝗌 ≤ C_k ‖g‖_((𝗌−1;k)). Each step holds in the strong sense, so
[[eq:ii-e-5-5]] does.

(b) As in [[prop:ii-e-4-4]], with 𝒳_K, W = 1, nested r-slabs

    Ω^K_([a,b]) ⊂ Ω_(2k) ⊂ ⋯ ⊂ Ω_(0) = Ω″

with room 2^(−i−2) δ_1 at the final face, two per step as there, and d := d̃ + 3; the right-hand side is extended
across {r = a} by an extension bounded at every order of b-regularity at once, as described before
[[prop:ii-e-4-4]]. The one new term is [P, χ]u in [[eq:ii-e-5-7]]. Its coefficients are χ′ times those of P, which are
stationary smooth ones plus O(ε_(P,k)) in C^((d_0;k)); by [[lem:ii-e-4-1]] (b), whose proof applies verbatim to the
spaces H(·)^• with room at both r-faces, here {a⁺ + δ_2 ≤ r ≤ b − δ_2} inside Ω^K_([a⁺,b]),

    ‖[P, χ]u‖_((𝗌−1;k)) ≤ C_k (‖u‖^([a⁺,b])_((𝗌;k)) + ε_(P,k) ‖u‖^([a⁺,b])_((𝗌;d̃))),

the stationary part contributing ‖u‖_((𝗌;d̃)) ≤ ‖u‖_((𝗌;k)) for k ≥ d̃. The induction then gives [[eq:ii-e-5-6]], the
norms of g at order (𝗌 − 1; d) being bounded by [[eq:ii-e-5-7]] at k = d. ∎

[Hin26c] states its Propositions 8.11–8.13 for constant orders ("We do not need variable orders in this part", its
footnote 66), and its Theorem 8.14 applies them with the admissible order functions, which need not be constant on
r⁻¹([m, r^♮]). Here they are proved for slab orders ([[lem:ii-e-5-3]] at the variable order, [[prop:ii-e-5-4]] (ii) by
the scheme of [[prop:ii-e-3-4]]), and admissible orders are slab orders by [[prop:ii-c-5-1]] (2).

### The global estimate {#sec:ii-e-6}

**Theorem {#thm:ii-e-6-1}** (The global estimate.) Let the weights satisfy

    α_I < −1/2 + p̄_1,        α_+ < α_I − 1/2,        α_K ∈ ℝ

([[eq:ii-d-1-3]]), and let 𝗌_0 < 𝗌 be order functions admissible for P_0 with weights α_+, α_K and margin 0
([[def:ii-c-5-2]]). For every k ∈ ℕ_0 there is C_k such that

    ‖u‖_(H^((𝗌;k),(2α_I,α_+,α_K))_(e3b;b)(Ω_*)^(•,−))
        ≤ C_k (‖Pu‖_(H^((𝗌;k),(2α_I+2,α_++2,α_K))_(e3b;b)(Ω_*)^(•,−))
               + ‖u‖_(H^((𝗌_0;k),(2α_I,α_+,α_K))_(e3b;b)(Ω_*)^(•,−)))                               {#eq:ii-e-6-1}

for P = P_0, in the strong sense, and for every weakly admissible P of class ((d_0;k),(2ℓ_I,ℓ_+,ℓ_K)) with ε_(P,k)
small, with C_k uniform; d_0 depends only on 𝗌_0 and 𝗌. Moreover, if 𝗌 and 𝗌_0 are constant near {r ≤ r_0}, with
nonnegative integer values there [[pending:issue-1]], there is d ∈ ℕ such that for every k and every P of that class
with ε_(P,d) small,

    ‖u‖_((𝗌;k)) ≤ C_k (‖Pu‖_((𝗌;k)) + ‖u‖_((𝗌_0;k)) + ε_(P,k) (‖Pu‖_((𝗌;d)) + ‖u‖_((𝗌_0;d)))),           {#eq:ii-e-6-2}

with the spaces and weights of [[eq:ii-e-6-1]], ε_(P,k) := ‖P − P_0‖_((d_0;k),(2ℓ_I,ℓ_+,ℓ_K)) over Ω_*, and C_k depending
on P only through a bound for ε_(P,d). Both hold uniformly when P_0 is replaced by the stationary models of nearby
parameters, or perturbed within the stationary wave-type operators.

This is [Hin26c, Theorem 8.14] in dimension 4 + 1. [Hin26c] assumes only the first condition on the weights; the second,
α_+ < α_I − 1/2, is the threshold at the incoming radial set over ℐ⁺ ∩ ι⁺, where the quantity 4(α_I − α_+ − 1/2) must
be positive ([[prop:ii-d-3-5]]; [Hin26c, (7.19)]), and [Hin26c, Proposition 7.11], invoked in its proof, assumes it. It
does not involve the orders. [Hin26c] prints its tame estimate (8.46) with the weights (2α_I, α_+, α_K) on Pu, where
(8.45) and [Hin26c, Proposition 7.11] have (2α_I + 2, α_+ + 2, α_K); as printed it would bound u by a weaker norm of Pu
than (8.45) does, which is not what the proof gives. [[eq:ii-e-6-2]] carries the weights of [[eq:ii-e-6-1]].

*Proof.* Let f := Pu, and assume the right side of [[eq:ii-e-6-1]] finite; then u ∈ H^((𝗌_0;k)), and u is the forward
solution of Pu = f on every slab and r-slab below, by [[prop:ii-e-3-4]] (i) and [[prop:ii-e-5-4]] (i).

*A partition of unity.* Let χ and r_1^+ be the cut-off and the radius of [[eq:ii-d-1-2]]: r_0 < r_1 < r_1^+ < r^♮, χ = 0
on (t^♭)⁻¹([1, 2]) ∪ r⁻¹([r_0, r_1]) and χ = 1 on {t^♭ ≥ 3} ∩ {r ≥ r_1^+}. Let ψ_t ∈ C^∞(ℝ) equal 1 on (−∞, 7/2] and
0 on [4, ∞), and ψ_r ∈ C^∞(ℝ) equal 1 on (−∞, r_1^+ + δ_3] and 0 on [r^♮ − δ_3, ∞), δ_3 := (r^♮ − r_1^+)/4. Put

    φ_A := ψ_t(t^♭),     φ_C := (1 − ψ_t(t^♭)) ψ_r(r),     φ_B := (1 − ψ_t(t^♭))(1 − ψ_r(r)).

They are smooth on M with bounded b-derivatives (ψ_r(r) = 0 near ι⁺ and ℐ⁺, and r is smooth near (K⁺)°), and
φ_A + φ_B + φ_C = 1. φ_A is supported in {t^♭ ≤ 4}; φ_B in {t^♭ ≥ 7/2, r ≥ r_1^+ + δ_3}, where χ = 1; φ_C in
{t^♭ ≥ 7/2, r ≤ r^♮ − δ_3}. Let Ω_(1,5) be the slab of [[sec:ii-e-1-1]] and Ω^K := Ω^K_([r_0,r^♮]) the r-slab with
T_0 = 1, which is Ω_* ∩ {r ≤ r^♮}. On Ω_(1,5), ρ_+ and ρ_K are bounded above and below, and the spaces of
[[eq:ii-e-6-1]] restrict to those of [[sec:ii-e-1-1]] with the weight 2α_I; on Ω^K, ρ_I and ρ_+ are, and they restrict
to those of [[sec:ii-e-5-1]] with the weight α_K. An extension of u|_(Ω_(1,5)) supported in {t^♭ ≥ 1}, multiplied by
φ_A, extends φ_A u; likewise for Ω^K and φ_C. As multiplication by the φ's is bounded ([[lem:ii-a-8-4]] (a)),

    ‖u‖_((𝗌;k)) ≤ C (‖u‖_(H^((𝗌;k),2α_I)(Ω_(1,5))^(•,−)) + ‖χu‖_((𝗌;k)) + ‖u‖_(H^((𝗌;k),α_K)(Ω^K)^•)).   {#eq:ii-e-6-3}

*(A) Finite times.* 𝗌 is a slab order ([[sec:ii-e-3-2]]). By [[prop:ii-e-4-3]] on Ω_(1,5), with P^ext below t^♭ = 1,

    ‖u‖_(H^((𝗌;k),2α_I)(Ω_(1,5))^(•,−)) ≤ C_k ‖f‖_(H^((𝗌−1;k),2α_I+2)(Ω_(1,5))^(•,−)) ≤ C_k ‖f‖_((𝗌;k)).

[Hin26c] applies its Propositions 8.6 and 8.9 "on a t_*-interval [1, 4]", below the range T_0 ≥ inf_Ω t_* + 1 = 2 in
which they are stated, the margin giving room below the initial face for its extension argument; [[lem:ii-e-1-2]]
extends P below t^♭ = 1, and [[lem:ii-e-1-3]] uses a collar of width η_0/2, so the slabs with T_0 ≥ 1 are covered.

*(B) Away from the initial surface and the interior.* [[thm:ii-d1-1-1]], [[eq:ii-d1-1-1]]:
‖χu‖_((𝗌;k)) ≤ C_k (‖f‖_((𝗌;k)) + ‖u‖_((𝗌_0;k))).

*(C) The interior.* 𝗌 is a slab order on Ω^K ([[sec:ii-e-5-3]]). [[prop:ii-e-5-6]] (a) with a := r_0, a⁺ := r_1^+ and
b := r^♮ gives

    ‖u‖_(H^((𝗌;k),α_K)(Ω^K)^•) ≤ C_k (‖f‖_((𝗌−1;k)) + ‖u‖^([r_1^+,r^♮])_((𝗌;k))).

On Ω^K_([r_1^+,r^♮]), u = ψ_t(t^♭)u + (1 − ψ_t(t^♭))χu, as χ = 1 on {t^♭ ≥ 7/2, r ≥ r_1^+}; so the last norm is at most
C times the sum of the first two norms on the right of [[eq:ii-e-6-3]], which (A) and (B) bound.

Inserting (A)–(C) in [[eq:ii-e-6-3]] gives [[eq:ii-e-6-1]], and in the strong sense, as each of (A)–(C) holds in it.
For [[eq:ii-e-6-2]] use [[prop:ii-e-4-4]], [[eq:ii-d1-1-2]] and [[prop:ii-e-5-6]] (b) instead; in (A) the right-hand
side f is the restriction of Pu, given on all of Ω_*, so its norms on the larger slabs used in the proof of
[[prop:ii-e-4-4]] are bounded by the norms on Ω_*. The term ε_(P,k) ‖u‖^([r_1^+,r^♮])_((𝗌;d)) of [[eq:ii-e-5-6]] is
bounded by (A) and (B) at k = d, with constants depending on ε_(P,d) only. d_0 and d are the largest of those of the
three pieces. Uniformity in P_0: the constants of [[sec:ii-e-2]]–[[sec:ii-e-5]] depend on P_0 through finitely many
coefficient norms and the margins of [[lem:ii-c-3-2]], of [[eq:ii-e-1-2]] and of the dynamics of [[ch:s05]], which are
uniform as in [[rem:ii-d-1-3]]; so are those of (B). ∎
