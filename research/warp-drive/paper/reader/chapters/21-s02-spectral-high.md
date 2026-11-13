## The spectral family at high frequencies {#ch:s02}

This chapter proves the high-frequency estimates for the spectral family P̂(σ) of [[ch:s01]]: the semiclassical
estimates in the closed upper half plane away from zero, with a loss of one power of the semiclassical parameter at a
normally hyperbolic trapped set, their b-regular versions, invertibility of P̂(σ) for |σ| large, and the regularity of
the inverse in σ. The main result, [[thm:i-b-1-3]], is [Hin26c, Theorem 9.16] in dimension 4 + 1, for operators on a
trivial bundle of any rank, with constants uniform in the operator ([[sec:i-b-9]]). As in [[ch:s01]] the regularity
order is constant ([[rem:i-a-1-1]]); the decay and semiclassical orders may vary. Every input is proved here or in
[[ch:s01]], except the facts of Fourier analysis used in [[sec:i-b-2]] and the results of [HJS] used in [[ch:s01]]. In
particular the semiclassical scattering calculus with matrix-valued symbols and variable orders is proved in
[[sec:i-b-2]].

[[sec:i-b-1]] fixes the hypotheses and states the theorem. [[sec:i-b-2]] proves the calculus. [[sec:i-b-3]] gives the
positive commutator scheme, which here needs no regularisation. [[sec:i-b-4]] to [[sec:i-b-7]] prove the estimates:
real principal type, radial points, the trapped set, and the artificial boundary. [[sec:i-b-8]] proves the theorem and
[[sec:i-b-9]] its uniformity.

*Notation.* The rank of the bundle is N_E. For an endomorphism A that is self-adjoint for a fibre inner product,
max spec A and min spec A are its largest and smallest eigenvalues. h is the semiclassical parameter; as an index
(^(*h), Re_h, Im_h, h_Γ) it denotes a fibre inner product, as in [[ch:s01]]. ℓ denotes Im z/h, except in
[[prop:i-b-7-1]], where it is the exponent of the weight e^(ℓr). Large integers that bound orders are written M: the
residual terms h^M and ‖u‖_(−M𝟏) of the estimates, the classes S^(−M𝟏), and the number of terms of a symbol
expansion. The letter K occurs only with a subscript, for closed subsets of phase space (K_0, K_1, K_E, K_Γ, …), and
in the deformation term ^(X)K of [[sec:i-b-7-1]]. Multi-orders are written in bold letters (𝐨, 𝐦, 𝐤, 𝐭).

### Setting, hypotheses and the theorem {#sec:i-b-1}

#### Data from the bounded-frequency theory {#sec:i-b-1-1}

The space X̄ ⊂ ℝ̄⁴, the radii r_0, δ_0, r_2, r_h, the bundle E = X̃ × ℂ^(N_E), fibre inner products h = ⟨H·,·⟩ and
h-adjoints A^(*h) = H⁻¹A*H, and the family P̂(σ) = P̂(0) + σT + σ²P_2 are those of [[sec:i-a-1]], and (H1)–(H5) of
[[sec:i-a-1-3]] are assumed. The radii enter only through the ordering 0 < r_0 − 2δ_0 < r_0 < r_2 < r_h, the domains
of the hypotheses and the slabs of [[sec:i-b-7]]; constants depend on them, but no particular value of them is used.
We write ρ = |x|⁻¹ near ∂X, scattering covectors as ξ dr + r η, and use [[lem:i-a-4-4]]: at the boundary face T has
principal symbol 2ξ Id, and Im_h T = −ρ(S + S^(*h)) + T_2 with T_2 ∈ Ψ^(1,−2).

#### The Lorentzian structure {#sec:i-b-1-2}

(H6) (Cf. [Hin26c, Definitions 9.3–9.4].) There is a smooth Lorentzian metric g on ℝ_t × X̃°, of signature (1, 4),
with t-independent components, such that for ζ ∈ T*X̃°

    G_0(ζ) = g⁻¹(ζ, ζ),     τ_1(ζ) = −2 g⁻¹(dt, ζ),     g_00 = g⁻¹(dt, dt).                              {#eq:i-b-1-1}

g_00 ≤ 0 everywhere and g_00 < 0 on X̃°: dt is timelike; we time-orient g so that −∇t is future directed ("dt is past
timelike" in [Hin26c]). Thus G(−σ dt + ζ) := g⁻¹(−σ dt + ζ, −σ dt + ζ) = G_0(ζ) + σ τ_1(ζ) + σ² g_00 is the principal
symbol of P̂(σ) jointly in (σ, ζ). The stationary operator P_0 := P̂(0) + T i∂_t − P_2 ∂_t² satisfies
P_0(e^(−iσt) v) = e^(−iσt) P̂(σ)v, and P_0 − □_g Id is a first order operator with t-independent coefficients, where
□_g := −∇^μ∇_μ acts componentwise.

On {r_0 − 2δ_0 < r < r_2}, (H4) gives G_0(dr) < 0: dr is timelike for g as a covector annihilating ∂_t, and the future
direction decreases r. Write X := ∇r = g⁻¹(dr, ·); it is a future directed timelike vector field there
([[sec:i-a-6-2]], where 𝔤⁻¹ is the restriction of g⁻¹ to T*X̃).

#### The semiclassical family {#sec:i-b-1-3}

For h ∈ (0, 1] and z ∈ ℂ, |z| ∈ [½, 2], put σ := z/h and

    P_(h,z) := h² P̂(z/h) = h² P̂(0) + hzT + z² g_00 Id.                                                  {#eq:i-b-1-2}

**Lemma {#lem:i-b-1-1}** (Cf. [Hin26c, Lemmas 9.20–9.21], on E.) Fix a fibre inner product h.

(a) P_(h,z) = Op_h(p_(h,z)) on X̃°, with p_(h,z) a polynomial of degree 2 in ζ whose coefficients are smooth on the
compactification near ∂X; its principal symbol, modulo S^(1,−1,−1), is G_z Id with G_z(x, ζ) := G(−z dt + ζ). (The
quantisation Op_h and the symbol classes S^𝐨 are defined in [[sec:i-b-2-2]] and [[def:i-b-2-1]].)

(b) Exactly,

    h⁻¹ Im_h P_(h,z) = 𝒫_1(z) − (Im z/h) 𝒬,     𝒫_1(z) := h Im_h P̂(0) + (Re z) Im_h T,
    𝒬 := −h Re_h T − 2 (Re z) g_00.                                                                    {#eq:i-b-1-3}

𝒫_1(z) and 𝒬 are h-self-adjoint semiclassical differential operators of order 1. The principal symbol of 𝒬 is q_z Id,
q_z(ζ) := −τ_1(ζ) − 2 (Re z) g_00 = 2 g⁻¹(−(Re z) dt + ζ, dt), and that of 𝒫_1(z) is p_1(z) := σ_1(Im_h P̂(0))(ζ) +
(Re z) σ_0(Im_h T), an h-self-adjoint endomorphism.

(c) Re G_z = G_(Re z) − (Im z)² g_00 and Im G_z = −(Im z) q_z.

(d) If Im z > 0, then G_z ≠ 0 on T*X̃°: the characteristic set of P_(h,z) over X̃° lies at fibre infinity.

(e) For z_0 ∈ {1, −1}, q_(z_0) ≠ 0 on Σ_(z_0) := {G_(z_0) = 0} ⊂ T*X̃°, and ρ_∞ q_(z_0) ≠ 0 on its boundary ∂Σ_0 at
fibre infinity. We write Σ^±_(z_0) := Σ_(z_0) ∩ {±q_(z_0) > 0}; at fibre infinity this labelling agrees with that of
(H3)–(H4).

*Proof.* (a) h² P̂(0) is a semiclassical scattering differential operator with principal symbol G_0(ζ) ([Hin26c,
(3.37)]); hT has semiclassical symbol τ_1(ζ) plus h times an order-0 symbol; z² g_00 is of order 0. At the boundary
face the lower terms gain ρ ([[lem:i-a-4-4]]).

(b) Im_h(cA) = (Re c) Im_h A + (Im c) Re_h A, g_00 Id is h-self-adjoint, and Im(z²) = 2 Re z Im z. Hence
h⁻¹ Im_h P_(h,z) = h Im_h P̂(0) + (Re z) Im_h T + (Im z) Re_h T + 2h⁻¹ Re z Im z g_00, which is [[eq:i-b-1-3]].
Re_h T has principal symbol τ_1 (by (H1)), so h Re_h T has semiclassical principal symbol τ_1(ζ); Im_h T has order 0;
Im_h P̂(0) has order 1 ([[rem:i-a-hypotheses]] (a)).

(c) Expand G(−(Re z + i Im z) dt + ζ).

(d) If Re G_z = 0 then G(−(Re z) dt + ζ) = (Im z)² g_00 < 0, so ν := −(Re z) dt + ζ is timelike. Hence
g⁻¹(ν, dt) ≠ 0 (dt is timelike, and two timelike covectors are never orthogonal), and
Im G_z = −2 (Im z) g⁻¹(ν, dt) ≠ 0.

(e) A nonzero null covector is not orthogonal to the timelike dt; at fibre infinity the same holds for the null
covectors ζ ∈ T*X̃° with G_0(ζ) = 0, and q_(z_0) is −τ_1 plus a term of lower degree. (H3) gives ∓τ_1 > 0 on ∂ℛ_±, so
the component of ∂Σ_0 containing ∂ℛ_± is the one on which ±q > 0. ∎

The *future-directed* field on Σ^±_(z_0) is ±H_(G_(z_0)) (rescaled, ±ρ_∞ H_(G_(z_0)), near fibre infinity). Where ∂_t
is future directed timelike, a null ν = −z_0 dt + ζ has ν(∂_t) = −z_0, so ν^♯ is future directed if and only if
z_0 > 0, and q_(z_0) = 2ν(∇t) then has the sign of z_0, as −∇t is future directed: only the component
Σ^(z_0)_(z_0) occurs away from an ergoregion ([Hin26c, footnote 80]).

#### Orders and thresholds {#sec:i-b-1-4}

*Orders.* s ∈ ℝ is constant. A *decay order* 𝗋 and a *semiclassical order* 𝖻 are orders in the sense of
[[sec:i-b-2-1]] that are smooth on the compactified phase space 𝒫 of [[sec:i-b-2-4]]. Let z_0 ∈ {1, −1}, let
𝖧_(z_0) be the rescaled Hamilton field of [[sec:i-b-4-1]] and q̂_(z_0) := ⟨ζ⟩⁻¹ q_(z_0), and on {q̂_(z_0) ≠ 0} put
𝖧^♮ := sgn(q̂_(z_0)) 𝖧_(z_0), the future field of [[sec:i-b-1-3]].

𝗋 is *admissible for z_0 with weight α_+* if it is constant near R_(z_0,in) and near R_out; if there is a
neighbourhood W, within the face over ∂X, of the characteristic set Σ^∂_(z_0) there, with 𝖧^♮𝗋 ≤ 0 on
W ∩ {q̂_(z_0) ≠ 0}; and if 𝗋 + α_+ > ½(−1 + ϑ_in) at R_(z_0,in) and 𝗋 + α_+ < −½ + S̄ at R_out (each in the fibre
inner product of (O3), up to any margin; [[prop:i-b-5-3]] and [[prop:i-b-5-5]]).

𝖻 is *admissible for z_0* if it is constant near ∂ℛ_±, near Γ_(z_0) of (H7), near R_(z_0,in) and R_out, and over
{r_0 − δ_0 ≤ r ≤ r_2 − δ_0} ([Hin26c, footnote 78]), and if there is a neighbourhood W of Σ_(z_0) in 𝒫 with
𝖧^♮𝖻 ≤ 0 on W ∩ {q̂_(z_0) ≠ 0}.

Constant orders are admissible. The monotonicity is asked on a neighbourhood of the characteristic set, not on the
set alone: [[prop:i-b-4-5]] needs it on the support of a commutant, where the factor log(1/h) multiplies 𝖧𝖻. It is
stronger than (O2) of [[def:i-a-admissible]], so 𝗋_h(x, ξ) := 𝗋(x, hξ) satisfies (O2)–(O3) of
[[def:i-a-admissible]] at σ_0 = z_0/h ([[sec:i-b-8-4]]).

*Thresholds.* ϑ_ℋ, ϑ_in and S̄ are those of [[eq:i-a-1-5]], each computed in a fibre inner product chosen for its
radial set. The regularity order satisfies s > ½ + ϑ_ℋ.

#### The trapped set and the global dynamics {#sec:i-b-1-5}

(H7) (Normally hyperbolic trapping; cf. [Hin26c, (Γ.1)–(Γ.4)], on E.) For z_0 ∈ {1, −1} write
Σ^♭_(z_0) := Σ^(z_0)_(z_0) and 𝖧_(z_0) := z_0 H_(G_(z_0)), the future field on it. There are a compact set
Γ = Γ_(z_0) ⊂ Σ^♭_(z_0) ∩ T*{r_2 < r < ρ_1⁻¹}, a neighbourhood O of Γ and real functions φ_u, φ_s ∈ C^∞(O) such that,
with Γ_(u/s) := {φ_(u/s) = 0} ∩ Σ^♭_(z_0) ∩ O:

- (Γ.1) Γ_u and Γ_s are smooth hypersurfaces of Σ^♭_(z_0) meeting transversally in Γ, and 𝖧_(z_0) is tangent to both;
- (Γ.2) 𝖧_(z_0) φ_u = −ν_u φ_u and 𝖧_(z_0) φ_s = ν_s φ_s on Σ^♭_(z_0) ∩ O, with
  ν_min := min(inf_Γ ν_u, inf_Γ ν_s) > 0;
- (Γ.3) {φ_u, φ_s} > 0 and dG_(z_0) ≠ 0 on Γ;
- (Γ.4) with β_0 := ½ min_Γ |q_(z_0)| > 0, a fibre inner product h_Γ on π*E over a neighbourhood of Γ (it may depend
  on the covector; one from the base is a special case), p_1^Γ := z_0 p_1^(h_Γ)(z_0)|_Γ with p_1^(h_Γ) of
  [[eq:i-b-6-0]] in [[lem:i-b-6-0]] (an h_Γ-self-adjoint endomorphism, the symbol of h⁻¹ Im P computed in h_Γ, and
  p_1 when h_Γ is the standard inner product) and q^Γ := z_0 q_(z_0)|_Γ ≥ 2β_0, the function
  f(η) := sup_(ϖ∈Γ) max spec(p_1^Γ(ϖ) − η q^Γ(ϖ)) is continuous and decreases at least at the rate 2β_0; let

        f(γ_+) = 0,     f(γ_−) = ½ ν_min,
        δ_Γ(η) := min(1, max((γ_+ − η)/(γ_+ − γ_−), 0)) ∈ [0, 1],                                       {#eq:i-b-1-4}

  and assume γ_− < 0, that is, sup_Γ max spec(p_1^Γ) < ½ ν_min. Then γ_− < γ_+.

The factors z_0 make [[eq:i-b-1-4]] the same for both signs: the future field on Σ^♭_(z_0) is z_0 H_(G_(z_0)), and
[[sec:i-b-6]] works with z_0 p_1 and z_0 q throughout. For z_0 = 1, scalar operators and q_(z_0) constant on Γ,
[[eq:i-b-1-4]] is [Hin26c, (9.79)–(9.81)]; in general γ_± are the exact thresholds that the proof uses, and γ_− < 0 is
what [[thm:i-b-1-3]] (1) needs at Im z = 0 ([[rem:i-b-relation]]).

(H8) (Global dynamics; cf. [Hin26c, Section 9.1.2].) For z_0 ∈ {1, −1} let Γ̄_u (resp. Γ̄_s) be the set of points of
Σ_(z_0) whose maximal integral curve of the future field tends to Γ as t → −∞ (resp. t → +∞): the *global* backward
and forward trapped sets. They are invariant under the flow, so a maximal curve lies in Γ̄_(u/s) or does not meet it.

- (a) For every maximal integral curve γ of the future field in Σ_(z_0) ∩ T*{r > r_0 − 2δ_0} (finite covectors): if
  γ ⊄ Γ̄_u, then γ(t) tends, as t → −∞, to ∂ℛ_+ ∪ ∂ℛ_− (at fibre infinity) or to R_(z_0,in) (over ∂X); and if
  γ ⊄ Γ̄_s, then as t increases γ either tends to R_out or reaches {r < r_0 − δ_0} in finite time. Here "tends to" is
  in 𝒫, and the convergence is uniform on compact sets of initial points away from Γ̄_u (resp. Γ̄_s).
- (b) (No return.) After shrinking O, Γ̄_u ∩ O = Γ_u and Γ̄_s ∩ O = Γ_s: a curve that leaves O does not come back to
  tend to Γ.

(b) makes the chain of [[sec:i-b-8-2]] acyclic. Together with (H4) at fibre infinity and [[lem:i-a-4-5]] over ∂X, (a)
describes the flow on the whole characteristic set. The global sets in (a) cannot be replaced by the local ones
Γ_(u/s): a point of Γ_u ∖ Γ leaves O forward, so its curve is not contained in Γ_u, and with the local sets (a) would
force that curve to tend backward to the radial sets, whereas by (D2) of [[sec:i-b-6-1]] it tends to Γ.

(H5) is extended to (H6)–(H8): g, Γ, φ_(u/s), ν_(u/s) and h_Γ may depend continuously on the parameter b ∈ ℬ (into
C^∞), with ν_min, β_0, γ_± and the convergence in (H8) uniform. For the operators to which this chapter is applied in
the stability theory, (H6)–(H8) are verified in [[ch:s12]] and the chapters that treat each operator; they are not
verified here.

*The two fields.* 𝖧_(z_0) = z_0 H_(G_(z_0)) in (H7) is the future field; the field 𝖧_z of [[eq:i-b-4-1]] is a
positive multiple of H_(G_z), and the future field is ς𝖧_z ([[rem:i-b-1-4]]).

#### The spaces and the theorem {#sec:i-b-1-6}

With the semiclassical Sobolev spaces H_h^(s,𝗋,𝖻) of [[sec:i-b-2-3]] on ℝ⁴, let H̄_h^(s,𝗋,𝖻) and Ḣ_h^(s,𝗋,𝖻) be their
extendible and supported versions at ∂_♯X ([[sec:i-a-6-1]], with the quotient norm, resp. the induced norm; the
constructions there are local at ∂_♯X and do not see h). For k ∈ ℕ_0, let H̄_h^((s;k),𝗋,𝖻) be the space of u with
(⟨x⟩D_x)^α u ∈ H̄_h^(s,𝗋,𝖻) for |α| ≤ k, normed by the sum, and (cf. [Hin26c, (9.58)])

    ‖u‖_((s;k),𝗋,𝖻;+) := Σ_(j=0)^k h^(−j) ‖u‖_(H̄_h^((s;k−j),𝗋,𝖻)).                                        {#eq:i-b-1-5}

**Theorem {#thm:i-b-1-3}** (High-energy estimates. Cf. [Hin26c, Theorem 9.16], in dimension 4 + 1, on E.) Assume
(H1)–(H8). Let α_+ ∈ ℝ, z_0 ∈ {1, −1}, s > ½ + ϑ_ℋ, and let 𝗋, 𝖻 be admissible for z_0, the first with weight α_+.
Write 𝐨 := (s, 𝗋 + α_+, 𝖻) and 𝐨′ := (s − 1, 𝗋 + α_+ + 1, 𝖻).

(1) (High-energy estimates, I.) For ν ≥ 0 there are C, h_0 > 0 such that for z ∈ z_0 + i[0, ν] and h ∈ (0, h_0),

    ‖u‖_(H̄_h^𝐨) ≤ C h⁻² ‖P_(h,z) u‖_(H̄_h^(𝐨′)),
    ‖v‖_(Ḣ_h^(−𝐨′)) ≤ C h⁻² ‖P_(h,z)^(*h) v‖_(Ḣ_h^(−𝐨)),                                                {#eq:i-b-1-6}

for u ∈ H̄_h^𝐨 with P_(h,z) u ∈ H̄_h^(𝐨′), and v ∈ Ḣ_h^(−𝐨′) with P_(h,z)^(*h) v ∈ Ḣ_h^(−𝐨).

(2) (High-energy estimates, II.) For ν′ > 0, [[eq:i-b-1-6]] holds for |z| ∈ [½, 2], Im z ≥ ν′ and h ∈ (0, h_0), for
every decay order 𝗋 constant near R_out with 𝗋 + α_+ < −½ + S̄ there, and every constant 𝖻.

(3) (Invertibility.) There is C_0 such that P̂(σ) : 𝒳_σ → 𝒴_σ ([[thm:i-a-7-2]]) is invertible for every σ with
Im σ ≥ 0 and |σ| ≥ C_0, the orders at σ being those of (1) or (2) read at h = |Re σ|⁻¹, resp. h = |σ|⁻¹
([[sec:i-b-8-4]]).

(4) (Smaller losses; b-regularity.) For z, h_0 as in (1) or (2), k ∈ ℕ_0 and ϵ > 0 there is C with

    ‖u‖_((s;k),𝗋+α_+,𝖻;+) ≤ C h^(−1−δ_Γ(Im(z/h)−ϵ)) ‖P_(h,z) u‖_((s−1;k),𝗋+α_++1,𝖻;+).                    {#eq:i-b-1-7}

(5) (Regularity in the spectral parameter.) For σ as in (3) and j, k ∈ ℕ_0, ϵ > 0, the inverse P̂(σ)⁻¹ is j times
differentiable along σ∂_σ, and with h as in (3) (h := |Re σ|⁻¹ if Im σ < ν′|σ|, h := |σ|⁻¹ otherwise) and
δ := δ_Γ(Im σ − ϵ),

    ‖(σ∂_σ)^j P̂(σ)⁻¹ f‖_((s+j;k),𝗋+α_+,𝖻;+) ≤ C |σ|^(−1+(j+1)δ) ‖f‖_((s−1;k+j),𝗋+α_++1,𝖻;+).               {#eq:i-b-1-8}

For Im(z/h) large, δ_Γ = 0.

**Remark {#rem:i-b-1-4}** In (1), h⁻² is the case k = 0 of [[eq:i-b-1-7]] with δ_Γ ≤ 1; we prove (4) and the adjoint
half of (1), and (1)–(2) follow. Both signs of z_0 are treated together: estimates for P propagate along ς𝖧 with
ς = sgn q ([[sec:i-b-4-4]]), the future field on each component, which for z_0 = −1 on Σ^♭_(z_0) is −H_(G_(−1))
rescaled.

**Remark {#rem:i-b-relation}** (Relation to [Hin26c, Theorem 9.16].) The statement differs from [Hin26c, Theorem 9.16] in
dimension 4 + 1 in three points. The regularity order is constant ([[rem:i-a-1-1]]). The orders are required to be
monotone on a neighbourhood of the characteristic set, not on it alone, because the weight log(1/h) multiplies 𝖧𝖻 on
the whole support of a commutant ([[prop:i-b-4-5]]). And γ_± are the exact thresholds [[eq:i-b-1-4]], with γ_− < 0
assumed in (H7). The value of γ_− in [Hin26c, (9.80)] divides by 2β_0 = min_Γ q. For Im σ < 0, which the interpolation
of [Hin26c, Lemma 9.33] uses on its lower line, −ηq ≤ |η| max_Γ q, so the loss-one argument needs
sup_Γ max spec(p_1 − ηq) < ½ν_min; this follows from the condition printed there only if q is constant on Γ (as for a
static spherically symmetric metric, with Γ at one radius). The thresholds [[eq:i-b-1-4]] agree with [Hin26c, (9.80)]
when q is constant on Γ, and every later use needs only that δ_Γ(0) is small, which holds for either definition when
γ_+ is small. [Hin26c, Theorem 9.16 (1)] asserts the h⁻² estimate for z ∈ ±1 + i[0, ν], while [Hin26c, Theorem 9.28]
is proved for Im(h⁻¹z) ≥ β > γ_−; at Im z = 0 this needs γ_− < 0, which [Hin26c] notes for its applications and
which is part of (H7) here.

### The semiclassical scattering calculus {#sec:i-b-2}

The high-frequency estimates need the semiclassical scattering calculus of Vasy and Zworski. [Hin26c, (3.33)–(3.36)]
defines it and refers to [VZ00] and [Hin25a, Section 6.6]; [HJS] treats only the non-semiclassical calculus. We prove
what we use in this section, on ℝ^n for every n ≥ 1, with matrix-valued symbols and variable orders, from Fourier
analysis, integration by parts and Schur's test. The proofs are the standard ones.

Throughout, h ∈ (0, 1], matrices are N_E × N_E with the operator norm |·|, and a *family* is a map h ↦ a_h; estimates
are uniform in h. Put L_h(x, ζ) := 1 + log⟨x⟩ + log⟨ζ⟩ + log(1/h).

#### Symbols and orders {#sec:i-b-2-1}

An *order* is a real function 𝗈 on ℝ^n_x × ℝ^n_ζ, independent of h, with
|∂_x^α ∂_ζ^β 𝗈| ≤ C_αβ ⟨x⟩^(−|α|) ⟨ζ⟩^(−|β|). Every function smooth on ℝ̄^n × ℝ̄^n (the product of the radial
compactifications) is an order, since derivatives of a smooth function of (⟨x⟩⁻¹, x/⟨x⟩) gain ⟨x⟩⁻¹, and likewise in
ζ. For orders s, 𝗋, 𝖻 put

    w_(s,𝗋,𝖻)(x, ζ) := ⟨ζ⟩^(s(x,ζ)) ⟨x⟩^(𝗋(x,ζ)) h^(−𝖻(x,ζ)):

s is the regularity order, 𝗋 the decay order and 𝖻 the semiclassical order, as in [Hin26c, (3.33)]. We write
𝐨 = (s, 𝗋, 𝖻), w_𝐨, and 𝟏 := (1, 1, 1).

**Definition {#def:i-b-2-1}** S^𝐨 is the space of families of smooth a_h : ℝ^(2n) → ℂ^(N_E×N_E) with |a_h| ≤ C w_𝐨
and, for each (α, β) ≠ 0, constants C_αβ, μ_αβ ≥ 0 with

    |∂_x^α ∂_ζ^β a_h(x, ζ)| ≤ C_αβ w_𝐨(x, ζ) ⟨x⟩^(−|α|) ⟨ζ⟩^(−|β|) L_h(x, ζ)^(μ_αβ).                    {#eq:i-b-2-1}

The best constants with |α| + |β| ≤ k (and fixed exponents) are the seminorms. S^(−∞) := ⋂_M S^(−M𝟏). Note
h^M S^𝐨 = S^(𝐨−(0,0,M)).

**Lemma {#lem:i-b-2-2}** For orders 𝐨, 𝐨′:

(a) w_𝐨 Id ∈ S^𝐨, and w_𝐨⁻¹ = w_(−𝐨).

(b) S^𝐨 S^(𝐨′) ⊂ S^(𝐨+𝐨′).

(c) If 𝐨 ≤ 𝐨′ pointwise in each component, S^𝐨 ⊂ S^(𝐨′).

(d) For a ∈ S^𝐨 and ϵ > 0, ∂_x^α ∂_ζ^β a ∈ S^(𝐨−(|β|,|α|,0)+ϵ𝟏).

(e) If a ∈ S^𝐨, U is open, and for h < h_0, a_h is invertible on U with |a_h⁻¹| ≤ C w_𝐨⁻¹, then φ a⁻¹ ∈ S^(−𝐨) for
every φ ∈ S^0 supported in U (and set to 0 for h ≥ h_0).

*Proof.* (a) log w = s log⟨ζ⟩ + 𝗋 log⟨x⟩ + 𝖻 log(1/h). A derivative of log w falls on an order, gaining that
variable's weight and leaving one logarithm, or on log⟨·⟩, whose derivatives of order k ≥ 1 are O(⟨·⟩^(−k)). So for
(α, β) ≠ 0, |∂_x^α ∂_ζ^β log w| ≤ C ⟨x⟩^(−|α|) ⟨ζ⟩^(−|β|) L_h. By the chain rule ∂^γ w is w times a sum of products of
such derivatives with multi-indices adding to γ. (b) Leibniz's rule, as w_𝐨 w_(𝐨′) = w_(𝐨+𝐨′). (c) w_𝐨 ≤ w_(𝐨′).
(d) L_h^μ ≤ C_(μ,ϵ) ⟨x⟩^ϵ ⟨ζ⟩^ϵ h^(−ϵ). (e) The derivatives of a⁻¹ are sums of products
a⁻¹(∂^(γ_1)a)a⁻¹ ⋯ (∂^(γ_k)a)a⁻¹. ∎

#### Quantisation, composition, adjoints {#sec:i-b-2-2}

For a ∈ S^𝐨 and u ∈ 𝒮(ℝ^n; ℂ^(N_E)),

    Op_h(a)u(x) := (2πh)^(−n) ∫∫ e^(i(x−x′)·ζ/h) a_h(x, ζ) u(x′) dx′ dζ
                 = (2πh)^(−n) ∫ e^(ix·ζ/h) a_h(x, ζ) ℱ_h u(ζ) dζ,

with ℱ_h u(ζ) := ∫ e^(−ix′·ζ/h) u(x′) dx′, Schwartz. Ψ^𝐨 := Op_h(S^𝐨). Op_h(a) maps 𝒮 to itself:
x^γ e^(ix·ζ/h) = (−ih∂_ζ)^γ e^(ix·ζ/h), and integrating by parts gives
|x^γ ∂_x^(γ′) Op_h(a)u(x)| ≤ C_(γγ′) ⟨x⟩^(sup 𝗋+|γ′|) L_h(x, 0)^μ for some μ and every γ.

**Lemma {#lem:i-b-2-3}** (Oscillatory integrals.) Let F ∈ C^∞(ℝ^(2n)_(w,η); ℂ^(N_E×N_E)) satisfy
|∂_w^γ ∂_η^(γ′) F| ≤ A_(γγ′) ⟨w⟩^(M_F) ⟨η⟩^(M_F). Fix χ ∈ C_c^∞(ℝ^n) with χ(0) = 1. Then

    I(F) := lim_(ϵ→0) (2π)^(−n) ∫∫ e^(−iw·η) χ(ϵw) χ(ϵη) F(w, η) dw dη

exists, does not depend on χ, and for 2k > M_F + n

    I(F) = (2π)^(−n) ∫∫ e^(−iw·η) ⟨η⟩^(−2k) (1 − Δ_w)^k [⟨w⟩^(−2k) (1 − Δ_η)^k F] dw dη,
    |I(F)| ≤ C_(n,M_F) max_(|γ|,|γ′|≤2k) A_(γγ′).                                                      {#eq:i-b-2-2}

Moreover I(w^γ F) = I(D_η^γ F), and I(F) = F(·, 0) if F does not depend on w.

*Proof.* (1 − Δ_η) e^(−iw·η) = ⟨w⟩² e^(−iw·η) and (1 − Δ_w) e^(−iw·η) = ⟨η⟩² e^(−iw·η). Integrating by parts k times
in each variable in the regularised integral gives [[eq:i-b-2-2]] with F replaced by χ(ϵw)χ(ϵη)F; the derivatives
falling on the cut-offs are bounded for ϵ ≤ 1 and tend to 0 pointwise, and the integrand is dominated by
C⟨w⟩^(M_F−2k)⟨η⟩^(M_F−2k), which is integrable. Dominated convergence gives the limit and [[eq:i-b-2-2]]. The identity
w^γ e^(−iw·η) = (i∂_η)^γ e^(−iw·η) gives I(w^γ F) = I(D_η^γ F). If F = F(η), then
(2π)^(−n) ∫ e^(−iw·η) χ(ϵw) dw = ϵ^(−n) χ̌(η/ϵ) with ∫ χ̌ = χ(0) = 1, an approximate identity, so I(F) = F(0). ∎

**Theorem {#thm:i-b-2-4}** (Composition.) For a ∈ S^𝐨 and b ∈ S^(𝐨′), Op_h(a) Op_h(b) = Op_h(a#b) with

    a#b(x, ζ) = I(F_(x,ζ)),     F_(x,ζ)(w, η) := a_h(x, ζ + η) b_h(x + hw, ζ).                          {#eq:i-b-2-3}

a#b ∈ S^(𝐨+𝐨′), and for every M ≥ 1

    a#b − Σ_(|α|<M) (h^(|α|)/α!) ∂_ζ^α a D_x^α b ∈ S^(𝐨+𝐨′−(M/2)𝟏).                                      {#eq:i-b-2-4}

Each seminorm of a#b and of the remainder is bounded by a product of seminorms of a and b. The term with α lies in
S^(𝐨+𝐨′−|α|𝟏+ϵ𝟏) for every ϵ > 0.

*Proof.* The kernel of Op_h(a) Op_h(b) is (2πh)^(−2n) ∫ e^(i(x−y)·ζ′/h + i(y−x′)·ζ/h) a(x, ζ′) b(y, ζ) dy dζ′ dζ.
Writing e^(i(y−x′)·ζ/h) = e^(i(x−x′)·ζ/h) e^(−i(x−y)·ζ/h), it is the kernel of Op_h(c) with
c(x, ζ) = (2πh)^(−n) ∫∫ e^(i(x−y)·(ζ′−ζ)/h) a(x, ζ′) b(y, ζ) dy dζ′, and ζ′ = ζ + η, y = x + hw (so
dy dζ′ = h^n dw dη) give [[eq:i-b-2-3]]. On u ∈ 𝒮 the manipulations are justified by inserting χ(ϵw)χ(ϵη) and
letting ϵ → 0.

*The expansion.* By Taylor's formula,

    b(x + hw, ζ) = Σ_(|α|<M) ((hw)^α/α!) ∂_x^α b(x, ζ)
                   + M Σ_(|α|=M) ((hw)^α/α!) ∫_0^1 (1 − t)^(M−1) ∂_x^α b(x + thw, ζ) dt.

[[lem:i-b-2-3]] gives I(w^α a(x, ζ + η) ∂_x^α b(x, ζ)) = (D_ζ^α a)(x, ζ) ∂_x^α b(x, ζ), and
D_ζ^α a ∂_x^α b = ∂_ζ^α a D_x^α b: these are the terms of [[eq:i-b-2-4]]. The remainder is
R_M = M Σ_(|α|=M) (h^M/α!) ∫_0^1 (1 − t)^(M−1) I(G_(α,t)) dt with
G_(α,t)(w, η) := (D_ζ^α a)(x, ζ + η) (∂_x^α b)(x + thw, ζ).

*The remainder, with constant orders.* Let 𝐨_+, 𝐨′_+ be the componentwise suprema. Since
⟨x + y⟩^t ≤ 2^(|t|/2) ⟨x⟩^t ⟨y⟩^(|t|) (Peetre's inequality) and L_h(x + y, ζ + η) ≤ 2L_h(x, ζ) ⟨y⟩ ⟨η⟩ (as
log⟨x + y⟩ ≤ log⟨x⟩ + log(1 + |y|) ≤ log⟨x⟩ + |y|, likewise in ζ, and
|y| + |η| ≤ 2⟨y⟩⟨η⟩ − 1 ≤ (2⟨y⟩⟨η⟩ − 1)L_h(x, ζ)), and using
(th)^(|γ|) ≤ 1, ⟨x + thw⟩^(−|γ|) ≤ 1 and ⟨ζ + η⟩^(−|γ′|) ≤ 1, for |γ|, |γ′| ≤ 2k

    |∂_w^γ ∂_η^(γ′) G_(α,t)| ≤ C w_(𝐨_++𝐨′_+)(x, ζ) ⟨x⟩^(−M) ⟨ζ⟩^(−M) L_h(x, ζ)^μ ⟨w⟩^(M_F) ⟨η⟩^(M_F),
    M_F := |𝗋′_+ − M| + |s_+ − M| + μ + 1,

with μ depending on M and k. By [[eq:i-b-2-2]] with 2k > M_F + n, |I(G_(α,t))| obeys the same bound without the last
two factors. A derivative of R_M in x or ζ falls on a or b inside I; it gains ⟨x⟩⁻¹ or ⟨ζ⟩⁻¹ up to a factor
L_h⟨w⟩⟨η⟩, which [[eq:i-b-2-2]] absorbs with a larger k. So R_M ∈ S^(𝐨_++𝐨′_+−M𝟏+ϵ𝟏) for every ϵ > 0, the factor
h^M being the gain in the semiclassical order.

*Variable orders.* Let ω be the sum over the three components of sup 𝐨 + sup 𝐨′ − inf(𝐨 + 𝐨′). For M ≥ 2ω + 2,
𝐨_+ + 𝐨′_+ − M𝟏 + ϵ𝟏 ≤ 𝐨 + 𝐨′ − (M/2)𝟏 pointwise, so R_M ∈ S^(𝐨+𝐨′−(M/2)𝟏) by [[lem:i-b-2-2]] (c). The terms
with |α| < M lie in S^(𝐨+𝐨′−|α|𝟏+ϵ𝟏) by [[lem:i-b-2-2]] (b), (d). Applying this with M′ := max(M, 2ω + 2) and moving
the terms with M ≤ |α| < M′ into the remainder gives [[eq:i-b-2-4]] for every M, and a#b ∈ S^(𝐨+𝐨′). ∎

**Theorem {#thm:i-b-2-5}** (Adjoints.) For a ∈ S^𝐨, the formal adjoint in L²(ℝ^n; ℂ^(N_E)) is Op_h(a)* = Op_h(a^♮)
with a^♮(x, ζ) = I(a_h(x + hw, ζ + η)*), and a^♮ − Σ_(|α|<M) (h^(|α|)/α!) ∂_ζ^α D_x^α a* ∈ S^(𝐨−(M/2)𝟏).

*Proof.* The kernel of Op_h(a)* is (2πh)^(−n) ∫ e^(i(x−x′)·ζ/h) a(x′, ζ)* dζ, the kernel of Op_h(c) with
c(x, ζ′) = (2πh)^(−n) ∫∫ e^(iy·(ζ−ζ′)/h) a(x − y, ζ)* dy dζ; substitute ζ = ζ′ + η, y = −hw. The expansion follows
as in [[thm:i-b-2-4]]. ∎

*Consequences.* (i) Op_h is injective on symbols (the symbol is a partial Fourier transform of the kernel).

(ii) For a ∈ S^𝐨, b ∈ S^(𝐨′) and every ϵ > 0,

    (i/h)[Op_h(a), Op_h(b)] − Op_h((i/h)(ab − ba) + {a, b}) ∈ Ψ^(𝐨+𝐨′−(2,2,1)+ϵ𝟏),                       {#eq:i-b-2-5}

with {a, b} := Σ_j (∂_(ζ_j)a ∂_(x_j)b − ∂_(ζ_j)b ∂_(x_j)a) (products in the written order). If a = p Id is scalar, the
symbol is H_p b, H_p := ∂_ζ p · ∂_x − ∂_x p · ∂_ζ. If a is scalar only modulo lower order, a = p Id + a_1 with p
scalar and a_1 ∈ S^(𝐨−𝟏+ϵ𝟏) for every ϵ > 0, then

    (i/h)[Op_h(a), Op_h(b)] − Op_h(H_p b) ∈ Ψ^(𝐨+𝐨′−(1,1,0)+ϵ𝟏)     for every ϵ > 0,

since (i/h)(ab − ba) = (i/h)(a_1b − ba_1) ∈ S^(𝐨+𝐨′−(1,1,0)+ϵ𝟏) and {a, b} − H_p b = {a_1, b} lies in
S^(𝐨+𝐨′−(2,2,1)+ϵ𝟏).

(iii) If Op_h(a) is self-adjoint, then a − a* ∈ S^(𝐨−𝟏+ϵ𝟏).

(iv) If a vanishes on an open set U, then a#b and b#a, restricted to any open U′ with closure in U, obey the bounds of
S^(−M𝟏) for every M: every term of [[eq:i-b-2-4]] vanishes there, and the remainder lies in S^(𝐨+𝐨′−(M/2)𝟏) for every
M.

*Fibre inner products.* For a fibre inner product h = ⟨H·,·⟩ (H smooth on the compactification, so H^(±1/2) ∈ S^0),
u ↦ H^(1/2)u is unitary from L²_h to L², and A ↦ H^(1/2) A H^(−1/2) preserves every Ψ^𝐨, conjugates principal
symbols, and maps A^(*h) to (H^(1/2) A H^(−1/2))*. So everything in this section holds with ⟨·,·⟩_h and ^(*h) in place
of ⟨·,·⟩ and ^*.

#### Boundedness and Sobolev spaces {#sec:i-b-2-3}

**Lemma {#lem:i-b-2-6}** (Schur.) Let β ∈ ℝ and c ∈ S^((−n−1,−ϵ_0,β)) for some ϵ_0 > 0. Then
‖Op_h(c)‖_(L²→L²) ≤ C h^(−β), with C a seminorm of c.

*Proof.* The kernel is k(x, x′) = (2πh)^(−n) ∫ e^(i(x−x′)·ζ/h) c(x, ζ) dζ, and
(1 − h²Δ_ζ) e^(i(x−x′)·ζ/h) = ⟨(x − x′)/h⟩² e^(i(x−x′)·ζ/h), so

    |k(x, x′)| ≤ (2πh)^(−n) ⟨(x − x′)/h⟩^(−2n−2) ∫ |(1 − h²Δ_ζ)^(n+1) c(x, ζ)| dζ.

(1 − h²Δ_ζ)^(n+1) c is c plus terms h^(2j) Δ_ζ^j c, j ≥ 1, bounded by
C h^(2j−β) ⟨x⟩^(−ϵ_0) ⟨ζ⟩^(−n−1−2j) L_h^μ ≤ C h^(−β) ⟨ζ⟩^(−n−1−j), since h^(2j) ⟨x⟩^(−ϵ_0) ⟨ζ⟩^(−j) L_h^μ is bounded.
Hence |k(x, x′)| ≤ C h^(−n−β) ⟨(x − x′)/h⟩^(−2n−2), so sup_x ∫ |k| dx′ and sup_(x′) ∫ |k| dx are at most C h^(−β),
and Schur's test gives the claim. ∎

**Theorem {#thm:i-b-2-7}** (L² bound.) Let a ∈ S^0 (all orders 0) and ϵ > 0. There is C with

    ‖Op_h(a)u‖ ≤ (sup |a| + ϵ) ‖u‖ + C h^(1/4) ‖u‖,     u ∈ 𝒮,

the supremum over (x, ζ) and h. In particular Ψ^0 acts on L², uniformly in h.

*Proof.* Put c_a := sup |a|² + ϵ² and e := c_a − a*a ≥ ϵ², a Hermitian symbol in S^0. Its positive square root
b_0 := e^(1/2) = (2πi)⁻¹ ∮_𝒞 τ^(1/2) (τ − e)⁻¹ dτ, with 𝒞 a circle in {Re τ > 0} around [ϵ², c_a], lies in S^0
(differentiate under the integral; each derivative of (τ − e)⁻¹ is a sum of products of resolvents and derivatives of
e), as does b_0⁻¹. By [[thm:i-b-2-4]] and [[thm:i-b-2-5]],
Op_h(b_0)* Op_h(b_0) + Op_h(a)* Op_h(a) = c_a + Op_h(r_1) with r_1 ∈ S^(−½𝟏) and Op_h(r_1) self-adjoint. Given
b_0 + ⋯ + b_(j−1) with self-adjoint remainder Op_h(r_j), r_j ∈ S^(−(j/2)𝟏), put b_j := −¼ b_0⁻¹ (r_j + r_j*); then
b_0* b_j + b_j* b_0 = −½(r_j + r_j*) and, by (iii) and [[thm:i-b-2-4]], the new remainder lies in
S^(−((j+1)/2)𝟏+ϵ𝟏) (we absorb the ϵ by taking two steps per half order). With J := 4n + 8 and
B := Op_h(b_0 + ⋯ + b_J),

    ‖Op_h(a)u‖² = c_a‖u‖² − ‖Bu‖² + ⟨Op_h(r_(J+1))u, u⟩ ≤ (c_a + C h^(1/2)) ‖u‖²

by [[lem:i-b-2-6]] with β = −½, since r_(J+1) ∈ S^(−(n+1)𝟏) ⊂ S^((−n−1,−1,−½)). Take square roots. ∎

*Sobolev spaces.* For orders 𝐨 let W_𝐨 := Op_h(w_𝐨 Id). By [[lem:i-b-2-2]] and [[thm:i-b-2-4]],
Op_h(w_(−𝐨)) W_𝐨 = I + Op_h(e) and W_𝐨 Op_h(w_(−𝐨)) = I + Op_h(e′) with e, e′ ∈ S^(−½𝟏), so by [[thm:i-b-2-7]] there
is h_0 > 0 such that for h < h_0 both are invertible on L² with inverses bounded uniformly. For h < h_0 define
H_h^𝐨 := {u ∈ 𝒮′ : W_𝐨 u ∈ L²}, ‖u‖_𝐨 := ‖W_𝐨 u‖_(L²). For constant orders H_h^𝐨 = h^𝖻 ⟨x⟩^(−𝗋) ⟨hD⟩^(−s) L²
with uniformly equivalent norm. For each fixed h, when s is constant, H_h^𝐨 is the scattering Sobolev space
H^(s,𝗋_h) of [[sec:i-a-2-2]], with the decay order 𝗋_h(x, ξ) := 𝗋(x, hξ) in the variable ξ = ζ/h and the regularity
order s, with a norm equivalent for that h: h^(−𝖻(x,hξ)) is a symbol of order 0 at fixed h. This is how the
fixed-frequency results of [[ch:s01]] are used.

**Proposition {#prop:i-b-2-8}** (Mapping.) For A ∈ Ψ^𝐦 and orders 𝐨, ‖Au‖_(𝐨−𝐦) ≤ C ‖u‖_𝐨 for h < h_0.

*Proof.* ‖Au‖_(𝐨−𝐦) = ‖W_(𝐨−𝐦) A W_𝐨⁻¹ (W_𝐨 u)‖, W_𝐨⁻¹ = Op_h(w_(−𝐨)) (I + Op_h(e′))⁻¹, and
W_(𝐨−𝐦) A Op_h(w_(−𝐨)) ∈ Ψ^0 by [[thm:i-b-2-4]]. ∎

The L² pairing extends to H_h^𝐨 × H_h^(−𝐨) with |⟨u, v⟩| ≤ C ‖u‖_𝐨 ‖v‖_(−𝐨):
⟨u, v⟩ = ⟨W_𝐨 u, (W_𝐨⁻¹)* v⟩, and (W_𝐨⁻¹)* maps H_h^(−𝐨) to L² by [[prop:i-b-2-8]] and [[thm:i-b-2-5]].

#### Microlocalisation {#sec:i-b-2-4}

𝒫 := ℝ̄^n × ℝ̄^n is the semiclassical scattering phase space (the face of [Hin26c, (3.34)] at h = 0, identified with
the compactified scattering cotangent bundle of ℝ̄^n as in [Hin26c, (3.36)]). Its boundary faces are fibre infinity
ℝ̄^n × ∂ℝ̄^n and the face ∂ℝ̄^n × ℝ̄^n over spatial infinity.

**Definition {#def:i-b-2-9}** For A = Op_h(a) ∈ Ψ^𝐨: ϖ ∈ 𝒫 is *not* in WF′_h(A) if it has a neighbourhood U in 𝒫 on
which a obeys the bounds of S^(−M𝟏) for every M; it is in Ell_h(A) if it has a neighbourhood U and h_0 > 0 with a_h
invertible and |a_h⁻¹| ≤ C w_𝐨⁻¹ on U ∩ ℝ^(2n) for h < h_0.

By (iv), WF′_h(AB) ⊂ WF′_h(A) ∩ WF′_h(B). Ellipticity at ϖ depends only on a modulo symbols that are small compared
with w_𝐨 near ϖ: modulo S^(𝐨−(0,0,½)) anywhere (for small h), modulo S^(𝐨−(0,½,0)) near the face over spatial
infinity, and modulo S^(𝐨−(½,0,0)) near fibre infinity. The *principal symbol* of A ∈ Ψ^𝐨 is its symbol modulo
S^(𝐨−𝟏+ϵ𝟏) for small ϵ > 0; by [[eq:i-b-2-4]] it is multiplicative.

**Proposition {#prop:i-b-2-10}** (Microlocal elliptic estimate.) Let A ∈ Ψ^𝐦 and B, G ∈ Ψ^0 with
WF′_h(B) ⊂ Ell_h(A) ∩ Ell_h(G). Then for all orders 𝐨 and all M, ‖Bu‖_𝐨 ≤ C(‖GAu‖_(𝐨−𝐦) + ‖u‖_(−M𝟏)).

*Proof.* Let φ ∈ S^0 equal 1 near WF′_h(B), supported where a and g are uniformly invertible. Then
q_0 := φ a⁻¹ g⁻¹ ∈ S^(−𝐦) by [[lem:i-b-2-2]] (e), and Op_h(q_0) G A = Op_h(φ) + Op_h(r) with r ∈ S^(−½𝟏) near
WF′_h(B). Corrections q_j ∈ S^(−𝐦−(j/2)𝟏) supported in supp φ remove the error to any order: QGA = Op_h(φ) + R with
R ∈ S^(−M𝟏) near WF′_h(B). Then B = BQGA − BR + B(I − Op_h(φ)), the last term in Ψ^(−M𝟏) by (iv), and
[[prop:i-b-2-8]] bounds the rest. ∎

**Lemma {#lem:i-b-2-11}** (Positivity.) Let A = A* ∈ Ψ^(2𝐦) with principal symbol 𝖺, and B ∈ Ψ^0. Suppose
𝖺 ≥ c w_𝐦² Id, c > 0, on a neighbourhood of WF′_h(B). Then for all M and small ϵ > 0,
⟨ABu, Bu⟩ ≥ (c/2) ‖Bu‖²_𝐦 − C ‖Bu‖²_(𝐦−½(1−ϵ)𝟏) − C ‖u‖²_(−M𝟏).

*Proof.* Let 𝖺̃ ∈ S^(2𝐦) be Hermitian, equal to 𝖺 near WF′_h(B) and ≥ ¾ c w_𝐦² everywhere. Put
q := w_𝐦 (w_𝐦^(−2) 𝖺̃ − c/2)^(1/2) ∈ S^𝐦 (positive square root, as in [[thm:i-b-2-7]]). Then
A = Op_h(q)* Op_h(q) + (c/2) W_𝐦* W_𝐦 + E with E ∈ Ψ^(2𝐦−(1−ϵ)𝟏) near WF′_h(B), so
⟨ABu, Bu⟩ ≥ (c/2) ‖Bu‖²_𝐦 + ⟨EBu, Bu⟩, and [[prop:i-b-2-8]] bounds the last term. ∎

**Lemma {#lem:i-b-2-12}** (Square roots with logarithmic growth.) Let Q_0 ∈ S^0 be Hermitian with Q_0 ≥ c_Q Id,
c_Q > 0, and let κ ≥ 0 be a real scalar function with κ ≤ C L_h and
|∂_x^α ∂_ζ^β κ| ≤ C_αβ ⟨x⟩^(−|α|) ⟨ζ⟩^(−|β|) L_h^(μ_αβ) for (α, β) ≠ 0. Let Q := Q_0 + κ Id. Then Q^(1/2) ∈ S^(ϵ𝟏)
for every ϵ > 0 and Q^(−1/2) ∈ S^0. If b := w_𝐨 φ Q^(1/2) with φ ∈ S^0 scalar, then b ∈ S^(𝐨+ϵ𝟏) for every ϵ, and
wherever φ ≥ c > 0 on an open set U, φ′ b⁻¹ ∈ S^(−𝐨) for φ′ ∈ S^0 supported in U; [[prop:i-b-2-10]] then holds with
A := Op_h(b), at the order 𝐨, on U.

*Proof.* Q = (1 + κ) Q̃ with Q̃ := (Q_0 + κ)/(1 + κ), whose values lie in [min(c_Q, 1), max(sup |Q_0|, 1)] and whose
derivatives obey [[eq:i-b-2-1]] with order 0. So Q̃^(±1/2) ∈ S^0 by the Cauchy formula of the proof of
[[thm:i-b-2-7]] over a fixed contour. (1 + κ)^(1/2) ≤ C L_h^(1/2) ≤ C_ϵ w_(ϵ𝟏), and its derivatives
½(1 + κ)^(−1/2) ∂κ and higher obey [[eq:i-b-2-1]]; (1 + κ)^(−1/2) ≤ 1 likewise. This gives the first two claims, and
b⁻¹ = w_(−𝐨) φ⁻¹ Q^(−1/2) on U. In the proof of [[prop:i-b-2-10]] with q_0 := φ′ b⁻¹ ∈ S^(−𝐨), q_0#b − φ′ lies in
S^(−½𝟏) near supp φ′, since each term of [[eq:i-b-2-4]] with |α| ≥ 1 gains |α|𝟏 up to logarithms and the
logarithmic growth of b is one factor L_h^(1/2); the iteration is unchanged. ∎

### The positive commutator scheme {#sec:i-b-3}

All operators below have Schwartz kernels supported in {r > r_0 − (3/2)δ_0}². The coefficients of P_(h,z) on X̃° are
extended to ℝ⁴ arbitrarily (smoothly); no estimate below sees the extension. Orders are triples 𝐨 = (s, 𝗋, 𝖻) with s
constant, and 𝐦 := (2, 0, 0) is the order of P_(h,z). For a fibre inner product h, pairings and adjoints are those of
L²_h ([[sec:i-b-2-2]]).

#### A priori estimates {#sec:i-b-3-1}

The commutants of [[ch:s01]] are regularised because the estimates there are also regularity statements: they are
applied to u known only in a weaker space. Here every estimate is proved for Schwartz u, and is then extended by
density to the spaces where it is used.

**Lemma {#lem:i-b-3-1}** (Density.) Fix h ∈ (0, h_0), z, and orders 𝐨. Let
𝒢 := {u ∈ H_h^𝐨 : P_(h,z) u ∈ H_h^(𝐨−𝐦+(1,1,0))} with the graph norm. Then 𝒮 is dense in 𝒢. The same holds with the
b-regular norms of [[eq:i-b-1-5]] and for P_(h,z)^(*h) with 𝐨 replaced by −𝐨 + 𝐦 − (1, 1, 0).

*Proof.* At fixed h, H_h^𝐨 is the space H^(s,𝗋_h) of [[sec:i-a-2-2]] with 𝗋_h(x, ξ) := 𝗋(x, hξ), with an equivalent norm
([[sec:i-b-2-3]]), and P_(h,z) = h² P̂(z/h) ∈ Ψ_sc^(2,0). With T_t from (C8) of [[sec:i-a-2-1]], T_t u → u in H_h^𝐨,
and P_(h,z) T_t u = T_t P_(h,z) u + [P_(h,z), T_t] u. Here T_t P_(h,z) u → P_(h,z) u, and [P_(h,z), T_t] is bounded
in Ψ_sc^(1,−1) and tends to 0 in Ψ_sc^(1+δ,−1+δ) for every δ > 0 ([[lem:i-a-2-1]] (c) and (C8) of [[sec:i-a-2-1]]).
So it is uniformly bounded from H^(s,𝗋_h) to H^(s−1,𝗋_h+1) and tends to 0 on the dense subspace H^(s+δ,𝗋_h+δ), hence
strongly. T_t u is Schwartz. For the b-regular norms, [⟨x⟩D_x, T_t] is likewise bounded in Ψ_sc^(0,0) and tends to 0
strongly. ∎

Every term of the estimates below (‖Bu‖_𝐨, h⁻¹‖G P_(h,z) u‖_(𝐨−𝐦+(1,1,0)), ‖Eu‖_𝐨, ‖u‖_(−M𝟏), with B, G, E ∈ Ψ^0) is
continuous on 𝒢. So an estimate proved for Schwartz u holds on 𝒢, with the same constant, for each h. Near ∂_♯X the
estimates are applied to χu with χ ∈ C_c^∞({r > r_0 − δ_0}); then P_(h,z)(χu) = χ P_(h,z) u + [P_(h,z), χ] u with
[P_(h,z), χ] = h · Diff¹_h.

#### The identity and one step {#sec:i-b-3-2}

**Lemma {#lem:i-b-3-2}** (The commutator identity; cf. [Hin26c, (9.66)].) Let P ∈ Ψ^𝐦 and Ǎ = Ǎ^(*h). For Schwartz u,

    (2/h) Im⟨ǍPu, Ǎu⟩_h = ⟨Cu, u⟩_h,     C := (i/h)[Re_h P, Ǎ²] + (1/h)(Ǎ² Im_h P + Im_h P Ǎ²).          {#eq:i-b-3-1}

*Proof.* 2i Im⟨Ǎ²Pu, u⟩ = ⟨(Ǎ²P − P^(*h)Ǎ²)u, u⟩, and
Ǎ²P − P^(*h)Ǎ² = [Ǎ², Re_h P] + i(Ǎ² Im_h P + Im_h P Ǎ²). Divide by ih. ∎

We use XǍ² + Ǎ²X = 2ǍXǍ + [[X, Ǎ], Ǎ]. If Re_h P has principal symbol p Id with p real, Ǎ has principal symbol ǎ Id
with ǎ real, and h⁻¹ Im_h P ∈ Ψ^(𝐦−(1,1,0)) has principal symbol p_I (an h-self-adjoint endomorphism), then by
[[eq:i-b-2-5]] and [[thm:i-b-2-4]] the principal symbol of C is H_p(ǎ²) Id + 2ǎ² p_I, and the remainders lie in
Ψ^(𝐦+2𝐤−(2,2,1)+ϵ𝟏), where Ǎ ∈ Ψ^𝐤. With

    𝐤 := 𝐨 − ½(𝐦 − (1, 1, 0)) = 𝐨 − (½, −½, 0),                                                         {#eq:i-b-3-2}

C ∈ Ψ^(2𝐨) and the remainders lie in Ψ^(2𝐨−𝟏+ϵ𝟏).

**Lemma {#lem:i-b-3-3}** (One step.) Let P ∈ Ψ^𝐦, 𝐨 an order and 𝐤 as in [[eq:i-b-3-2]]. Let K_1 be a closed subset
of 𝒫 and G ∈ Ψ^0 elliptic on K_1. Suppose Ǎ = Ǎ^(*h) ∈ Ψ^𝐤 and that, for a sign ς and C as in [[eq:i-b-3-1]],

    ςC = −B^(*h)B − F + E^(*h)E + JP + R,                                                               {#eq:i-b-3-3}

where: B ∈ Ψ^𝐨 and Ǎ = ZB + Y with Z ∈ Ψ^(−½(𝐦−(1,1,0))), Y ∈ Ψ^(𝐤−½𝟏); ⟨Fw, w⟩_h ≥ −C_F‖w‖²_(−M𝟏) for Schwartz
w; E ∈ Ψ^𝐨 is microsupported in a closed set K_E; J ∈ Ψ^(2𝐨−𝐦) with WF′_h(J) ⊂ Ell_h(P); R ∈ Ψ^(2𝐨−½𝟏); and
Ǎ, B, E, J, R are microsupported in K_1. Let E′ ∈ Ψ^0 be elliptic on K_E. Then for Schwartz u and h < h_0,

    ‖Bu‖² ≤ C(h⁻² ‖GPu‖²_(𝐨−𝐦+(1,1,0)) + ‖E′u‖²_𝐨 + ‖Gu‖²_(𝐨−¼𝟏) + ‖u‖²_(−M𝟏)).                      {#eq:i-b-3-4}

C depends on C_F and on seminorms of the operators involved.

*Proof.* By [[eq:i-b-3-1]] and [[eq:i-b-3-3]],
‖Bu‖² = −ς(2/h) Im⟨ǍPu, Ǎu⟩ − ⟨Fu, u⟩ + ‖Eu‖² + ⟨JPu, u⟩ + ⟨Ru, u⟩. Microlocalise first: let Φ ∈ Ψ^0 be
microlocally the identity near K_1, with WF′_h(Φ) ⊂ Ell_h(G); then Ǎ(I − Φ) and (I − Φ)^(*h)Ǎ are residual, and
‖Φf‖_𝐭 ≤ C(‖Gf‖_𝐭 + ‖f‖_(−M𝟏)) by [[prop:i-b-2-10]].

(a) ⟨ǍPu, Ǎu⟩ = ⟨Z^(*h)ǍPu, Bu⟩ + ⟨ǍPu, Yu⟩, and Z^(*h)Ǎ ∈ Ψ^(𝐨−𝐦+(1,1,0)), Ǎ maps H^(𝐨−𝐦+(1,1,0)) to
H^(−½(𝐦−(1,1,0))), and Y maps H^(𝐨−½𝟏) to H^(½(𝐦−(1,1,0))). So
(2/h)|⟨ǍPu, Ǎu⟩| ≤ ½‖Bu‖² + C h⁻² ‖GPu‖²_(𝐨−𝐦+(1,1,0)) + C ‖Gu‖²_(𝐨−½𝟏) + C ‖u‖²_(−M𝟏).

(b) −⟨Fu, u⟩ ≤ C_F ‖u‖²_(−M𝟏).

(c) ‖Eu‖ ≤ C(‖E′u‖_𝐨 + ‖u‖_(−M𝟏)) by [[prop:i-b-2-10]].

(d) Let Φ_J ∈ Ψ^0 be microlocally the identity near WF′_h(J) with WF′_h(Φ_J) ⊂ Ell_h(P) ∩ Ell_h(G); then
⟨JPu, u⟩ = ⟨JPu, Φ_J u⟩ + O(‖u‖²_(−M𝟏) + ‖GPu‖²), ‖JPu‖_(−𝐨) ≤ C(‖GPu‖_(𝐨−𝐦) + ‖u‖_(−M𝟏)), and
‖Φ_J u‖_𝐨 ≤ C(‖GPu‖_(𝐨−𝐦) + ‖u‖_(−M𝟏)) by [[prop:i-b-2-10]]; and
‖GPu‖_(𝐨−𝐦) ≤ C ‖GPu‖_(𝐨−𝐦+(1,1,0)) ≤ C h⁻¹ ‖GPu‖_(𝐨−𝐦+(1,1,0)) ([[prop:i-b-2-8]]).

(e) |⟨Ru, u⟩| ≤ C ‖Gu‖²_(𝐨−¼𝟏) + C ‖u‖²_(−M𝟏).

Absorb ½‖Bu‖². ∎

#### Iteration in the semiclassical order {#sec:i-b-3-3}

The error term ‖Gu‖_(𝐨−¼𝟏) is at most ‖Gu‖_(𝐨−(0,0,¼)) = h^(1/4) ‖Gu‖_𝐨. Lowering only the semiclassical order keeps
every threshold, because 𝖻 enters a commutant only through the factor h^(−2𝖻), which at an order 𝐨 − (0, 0, β) is
multiplied by the constant h^(2β): a decomposition [[eq:i-b-3-3]] at 𝐨 gives one at 𝐨 − (0, 0, β) by multiplying
every operator by h^β, with the same seminorms in the shifted classes.

**Lemma {#lem:i-b-3-4}** (Iteration.) Let Λ ⊂ 𝒫 be closed and U_0 an open neighbourhood. Suppose that for every open U
with Λ ⊂ U ⊂ U_0 there are Ǎ and a decomposition [[eq:i-b-3-3]] at the order 𝐨, with K_1 ⊂ U, K_E = K_E(U) a closed
subset of Ū_0 ∖ Λ (or no E term), and B elliptic on the closure of an open neighbourhood U′ of Λ. Let G be elliptic on
Ū_0 and M ∈ ℕ. Then there are a neighbourhood U_* of Λ and a closed set K_E^* ⊂ Ū_0 ∖ Λ such that for every
B_* ∈ Ψ^0 microsupported in U_*, every E′ elliptic on K_E^*, and Schwartz u,

    ‖B_* u‖_𝐨 ≤ C(h⁻¹ ‖GPu‖_(𝐨−𝐦+(1,1,0)) + ‖E′u‖_𝐨 + h^M ‖Gu‖_𝐨 + ‖u‖_(−M𝟏)).                       {#eq:i-b-3-5}

*Proof.* Let J := 4M. Choose U_0 ⊃ U_1 ⊃ ⋯ ⊃ U_J ⊃ Λ, U_j the U′ of the hypothesis for U_(j−1), with B^(j) elliptic on
Ū_j and K_E^* := ⋃_j K_E(U_(j−1)). Let G_0 := G and, for j ≥ 1, G_j ∈ Ψ^0 elliptic on Ū_j with
WF′_h(G_j) ⊂ Ell_h(B^(j)), so that ‖G_j u‖_𝐭 ≤ C(‖B^(j)u‖_(𝐭−𝐨) + ‖u‖_(−M𝟏)) (with B^(j) at the shifted order). Apply
[[lem:i-b-3-3]] at the order 𝐨 − (0, 0, (J − j)/4) with (U_(j−1), G_(j−1)), using the scaling above:

    ‖G_j u‖_(𝐨−(0,0,(J−j)/4)) ≤ C(h⁻¹ ‖GPu‖_(𝐨−𝐦+(1,1,0)) + ‖E′u‖_𝐨 + ‖G_(j−1) u‖_(𝐨−(0,0,(J−j+1)/4))
                                 + ‖u‖_(−M𝟏)).

Chaining from j = J down to j = 1 leaves ‖G_0 u‖_(𝐨−(0,0,J/4)) = h^M ‖Gu‖_𝐨. Take U_* := U_J and use
‖B_* u‖_𝐨 ≤ C(‖G_J u‖_𝐨 + ‖u‖_(−M𝟏)). ∎

*Positivity of absorbing terms.* Suppose h⁻¹ Im_h P contains −ℓ𝒜 with ℓ ≥ 0 a constant, ℓ ≤ C h⁻¹, and 𝒜 = 𝒜^(*h)
such that ς𝒜 ∈ Ψ^(2𝐭) has principal symbol ≥ c w_𝐭² on a neighbourhood of WF′_h(Ǎ), for some order 𝐭. Then ςC
contains −ℓς(Ǎ²𝒜 + 𝒜Ǎ²) = −F − ℓς[[𝒜, Ǎ], Ǎ] with F := 2ℓǍ(ς𝒜)Ǎ. The double commutator lies in
ℓΨ^(2𝐤+2𝐭−2𝟏), which for the orders below is in the class of R. And F satisfies the hypothesis of [[lem:i-b-3-3]]:
[[lem:i-b-2-11]], whose proof does not use the order of B, gives
⟨ς𝒜Ǎw, Ǎw⟩ ≥ (c/2) ‖Ǎw‖²_𝐭 − C ‖Ǎw‖²_(𝐭−½(1−ϵ)𝟏) − C ‖w‖²_(−M𝟏), and the middle term is at most
C h^(1−ϵ) ‖Ǎw‖²_𝐭, which the first absorbs for h small. So ⟨Fw, w⟩ ≥ −Cℓ ‖w‖²_(−M𝟏) ≥ −C ‖w‖²_(−(M−1)𝟏). This is
[Hin26c, (9.69)].

In [[lem:i-b-3-3]] we also allow B ∈ ⋂_ϵ Ψ^(𝐨+ϵ𝟏) of the form of [[lem:i-b-2-12]] (a variable order contributes a
factor (1 + κ)^(1/2) with κ logarithmic); the proof is unchanged, and [[lem:i-b-2-12]] gives
‖B_* u‖_𝐨 ≤ C(‖Bu‖ + ‖u‖_(−M𝟏)) for B_* microsupported where the cut-offs of B equal 1, which is what [[lem:i-b-3-4]]
uses.

### Elliptic and real principal type estimates {#sec:i-b-4}

Throughout, Z ⊂ {z ∈ ℂ : |z| ∈ [½, 2], Im z ≥ 0} is compact, P := P_(h,z) with z ∈ Z, ℓ := Im z/h ∈ [0, 2h⁻¹], and
𝐨 = (s, 𝗋, 𝖻) with s constant. Constants are uniform in z ∈ Z unless said otherwise. We write ρ := ⟨x⟩⁻¹,
ρ_∞ := ⟨ζ⟩⁻¹ and μ := ⟨ζ⟩⟨x⟩⁻¹ = w_((1,−1,0)). A function a on ℝ^(2n) is *classical of order* (k, l) if ρ_∞^k ρ^l a
extends smoothly to 𝒫; then a ∈ S^((k,l,0)), as derivatives of a smooth function on 𝒫 gain ⟨x⟩⁻¹ in x and ⟨ζ⟩⁻¹ in ζ
([[sec:i-b-2-1]]). 𝒱_b(𝒫) denotes the smooth vector fields on 𝒫 tangent to both boundary faces.

#### The operator and its Hamilton field {#sec:i-b-4-1}

**Lemma {#lem:i-b-4-1}** Assume (H1), (H2) and (H6).

(a) G_0, τ_1 and g_00 are classical of orders (2, 0), (1, 0) and (0, −2), and Ĝ_z := ρ_∞² G_z ∈ C^∞(𝒫) depends
polynomially on z. P = Op_h(p_(h,z)) with p_(h,z) − G_z Id ∈ S^((1,−1,−1)), seminorms bounded uniformly for z ∈ Z;
Re_h P has principal symbol Re G_z Id.

(b) 𝒫_1(z) ∈ Ψ^((1,−1,0)) and 𝒬 ∈ Ψ^((1,0,0)), both h-self-adjoint and depending only on Re z; their principal symbols
p_1(z) and q_z Id satisfy μ⁻¹ p_1(z) ∈ S^0 and q̂_z := ρ_∞ q_z ∈ C^∞(𝒫). At the face over ∂X, q_z = −2ξ.

(c) If p is real and classical of order (k, 0), k ≤ 2, then μ⁻¹ H_p extends from ℝ^(2n) to an element of
ρ_∞^(2−k) 𝒱_b(𝒫). Hence

    𝖧_z := μ⁻¹ H_(Re G_z) = 𝖧^(0) + (Re z) 𝖧^(1) + ((Re z)² − (Im z)²) 𝖧^(2),                             {#eq:i-b-4-1}

with 𝖧^(0) := μ⁻¹ H_(G_0) ∈ 𝒱_b(𝒫), 𝖧^(1) := μ⁻¹ H_(τ_1) ∈ ρ_∞ 𝒱_b(𝒫) and 𝖧^(2) := μ⁻¹ H_(g_00) ∈ ρ² ρ_∞² 𝒱_b(𝒫).
Thus 𝖧_z is a smooth vector field on 𝒫, tangent to both faces, depending polynomially on (Re z, Im z); at fibre
infinity it does not depend on z, and 𝖧_z − 𝖧_(Re z) = −(Im z)² 𝖧^(2) vanishes at both faces. For a ∈ C^∞(𝒫),
H_(Re G_z) a = μ 𝖧_z a, and 𝖧_z log⟨ζ⟩, 𝖧_z log⟨x⟩ lie in C^∞(𝒫).

Here 𝖧_(Re z) is [[eq:i-b-4-1]] at the real point Re z. On the characteristic set over X̃° and at fibre infinity
𝖧_(z_0) is, up to the positive factor μ⁻¹, resp. ρ⁻¹, the field H_(G_(z_0)), resp. ρ_∞ H_(G_0), of [[sec:i-b-1-3]]
and (H3); over ∂X it is ⟨ζ⟩⁻¹ 𝖵_(G_(z_0)), with H_p = ρ 𝖵_p as in [[lem:i-a-4-4]] (c), so on the characteristic set
over ∂X it vanishes exactly on R_(z_0,in) ∪ R_out ([[lem:i-a-4-5]], read at σ_0 = z_0 in the variable ζ = hξ; the
boundary symbol is homogeneous of degree 2 in (σ, ξ, η)).

*Proof.* (a) By (H2), P̂(0) = ρ² P^(0) with P^(0) ∈ Diff²_b, and a b-vector field is ρ⁻¹ times a scattering vector
field; so G_0 is classical of order (2, 0). Likewise T ∈ ρ Diff¹_b + ρ³ Diff¹_b gives τ_1 of order (1, 0), and
g_00 ∈ ρ² C^∞. The rest is [[lem:i-b-1-1]] (a) and [[thm:i-b-2-5]]: the h-adjoint of Op_h(G_z Id) is Op_h(Ḡ_z Id)
modulo S^((1,−1,−1)).

(b) σ_1(T) = τ_1 Id is real and scalar (H1), so Im_h T has differential order 0: by [[lem:i-a-4-4]] (b) it is the
matrix function −ρ(S + S^(*h)) + T_2, T_2 ∈ ρ² C^∞, of order (0, −1, 0). Im_h P̂(0) ∈ ρ² Diff¹_b ⊂ ρ Diff¹_sc, so
h Im_h P̂(0) ∈ Ψ^((1,−1,0)). 𝒬 = −h Re_h T − 2(Re z) g_00 has order (1, 0, 0) and principal symbol
−τ_1 − 2(Re z) g_00, which is −2ξ at the face by [[lem:i-a-4-4]] (a) and g_00 ∈ ρ² C^∞.

(c) Near the face over ∂X, in polar coordinates x = ω/ρ, ∂_(x_j) ∈ ρ 𝒱_b(ℝ̄^n); near fibre infinity
∂_(ζ_j) ∈ ρ_∞ 𝒱_b(ℝ̄^n). For p = ρ_∞^(−k) p̂ with p̂ smooth, ∂_ζ p ∈ ρ_∞^(1−k) C^∞(𝒫) and
∂_x p = ρ_∞^(−k) ∂_x p̂ ∈ ρ_∞^(−k) ρ C^∞(𝒫), since b-vector fields preserve C^∞(𝒫). So
H_p ∈ ρ_∞^(1−k) ρ 𝒱_b = μ ρ_∞^(2−k) 𝒱_b. For g_00 ∈ ρ² C^∞ the x-derivative gains a further ρ². Finally
𝖧_z log⟨ζ⟩ = −ρ_∞⁻¹ 𝖧_z ρ_∞ is smooth since 𝖧_z ρ_∞ ∈ ρ_∞ C^∞, and likewise for log⟨x⟩ = −log ρ. ∎

The *characteristic set* of P is Σ_z := {Ĝ_z = 0} ⊂ 𝒫, closed. Over X̃° at finite frequencies, Σ_z = ∅ for Im z > 0
([[lem:i-b-1-1]] (d)); at fibre infinity Σ_z = ∂Σ_0 for every z; over ∂X, with G_z = 2zξ + ξ² + |η|²
([[lem:i-a-4-4]] (a)), Σ_z ∩ {ρ = 0} is the sphere {(ξ + z_0)² + |η|² = z_0²} if z = z_0 ∈ ℝ, and the zero section
R_out := {ρ = 0, ζ = 0} alone if Im z > 0 (the imaginary part 2(Im z)ξ forces ξ = 0, and then |η| = 0). For
z_0 ∈ {±1} the radial sets over ∂X are R_(z_0,in) := {ρ = 0, ξ = −2z_0, η = 0} and R_out, and q̂_(z_0) has the sign
of z_0 on Σ_(z_0) ∩ {ρ = 0} ∖ R_out and vanishes at R_out.

#### The elliptic estimate {#sec:i-b-4-2}

**Proposition {#prop:i-b-4-2}** Let K_0 ⊂ 𝒫 be compact with Ĝ_z ≠ 0 on K_0 for every z ∈ Z, and B, G ∈ Ψ^0 with
WF′_h(B) ⊂ K_0 and G elliptic on K_0. Then for all orders 𝐨 and all M, uniformly for z ∈ Z and h < h_0,

    ‖Bu‖_𝐨 ≤ C(‖GPu‖_(𝐨−𝐦) + ‖u‖_(−M𝟏)) ≤ C(‖GPu‖_(𝐨−𝐦+(1,1,0)) + ‖u‖_(−M𝟏)).                         {#eq:i-b-4-2}

The same holds for P^(*h).

*Proof.* By compactness of K_0 × Z there are a neighbourhood U of K_0 and c > 0 with |Ĝ_z| ≥ c on U for z ∈ Z. Since
p_(h,z) − G_z Id ∈ S^((1,−1,−1)) is bounded by C h w_𝐦, p_(h,z) is invertible on U with
|p_(h,z)⁻¹| ≤ 2c⁻¹ w_𝐦⁻¹ for h < h_0. [[prop:i-b-2-10]] applies, with constants depending on seminorms and on c only.
The second inequality is ‖f‖_(𝐨−𝐦) ≤ C ‖f‖_(𝐨−𝐦+(1,1,0)) ([[prop:i-b-2-8]]). For P^(*h) the symbol is Ḡ_z modulo
S^((1,−1,−1)). ∎

The second form is better by a factor h than the estimates below, whose first term is h⁻¹ ‖GPu‖_(𝐨−𝐦+(1,1,0)).

#### Flow boxes with a parameter, and cut-offs {#sec:i-b-4-3}

**Lemma {#lem:i-b-4-3}** Let Π ⊂ ℝ^d be open and (V_π)_(π∈Π) a family in 𝒱_b(𝒫) depending smoothly on π (jointly
smooth on 𝒫 × Π). Let ϖ_0 ∈ 𝒫, π_* ∈ Π and V_(π_*)(ϖ_0) ≠ 0. Then there are neighbourhoods Π_0 of π_* and U of ϖ_0,
τ > 0, and functions t, y_1, …, y_(2n−1) smooth on U × Π_0 such that for each π ∈ Π_0: (t, y)(·, π) is a
diffeomorphism of U onto (−τ, τ) × Y_π with Y_π open in [0, ∞)^k × ℝ^(2n−1−k), where k ∈ {0, 1, 2} is the number of
faces through ϖ_0 and the first k components of y are defining functions of those faces; V_π t = 1 and V_π y = 0; and
t(ϖ_0, π) = 0, y(ϖ_0, π) = y_0 independent of π. The same coordinates serve every point ϖ ∈ U with
|t(ϖ, π)| < τ/2, after translation in t, with τ/2 in place of τ.

*Proof.* Choose coordinates (ϱ_1, …, ϱ_k, w) near ϖ_0 with ϱ_i defining the faces through ϖ_0, and extend V_π smoothly
to a neighbourhood of ϖ_0 in ℝ^(2n) (allowing ϱ_i < 0). Tangency gives V_π ϱ_i = ϱ_i f_i with f_i smooth, so
V_(π_*)(ϖ_0) lies in the span of the ∂_w; after a linear change of w, V_(π_*)(ϖ_0) = ∂_(w_1). Let S := {w_1 = 0} and
Φ(t, ϖ′, π) := exp(tV_π)(ϖ′) for ϖ′ ∈ S near ϖ_0. Φ is smooth, and (t, ϖ′) ↦ Φ has invertible differential at
(0, ϖ_0, π_*); the inverse function theorem applied to (t, ϖ′, π) ↦ (Φ(t, ϖ′, π), π) gives a smooth inverse on a
neighbourhood. Take y := (ϱ_1, …, ϱ_k, w_2, …) of ϖ′. Along the flow ϱ_i(Φ(t, ϖ′, π)) = ϱ_i(ϖ′) exp ∫_0^t f_i, so
the flow preserves each face and each side of it: the inverse maps 𝒫 to {ϱ_i(ϖ′) ≥ 0}, and y_i = ϱ_i(ϖ′) is a
positive smooth multiple of ϱ_i. V_π t = 1 and V_π y = 0 by construction. The last statement is the translation
t ↦ t − t(ϖ). ∎

**Lemma {#lem:i-b-4-4}** There is χ ∈ C^∞(ℝ) with χ = 0 on (−∞, 0], χ = 1 on [1, ∞), χ′ ≥ 0, and √(χχ′) ∈ C^∞(ℝ).

*Proof.* Let ψ_1 ∈ C^∞((0, ∞)), ψ_1 ≥ 0, with ψ_1(s) = 1/s on (0, ½] and ψ_1 = 0 on [1, ∞). On (0, ∞) put
φ(t) := ∫_t^1 ψ_1(s)² ds and χ := e^(−φ). Then φ = 1/t + c near 0, so χ and all its derivatives tend to 0 as t → 0⁺;
set χ := 0 on (−∞, 0]. χ′ = ψ_1² χ ≥ 0, χ = 1 on [1, ∞), and √(χχ′) = ψ_1 e^(−φ), whose derivatives are polynomials
in 1/t times e^(−1/t) near 0. ∎

#### Propagation {#sec:i-b-4-4}

For ϵ_♭ ∈ {1, −1} write P_(ϵ_♭) := P if ϵ_♭ = 1 and P^(*h) if ϵ_♭ = −1. Then Re_h P_(ϵ_♭) = Re_h P and, by
[[eq:i-b-1-3]],

    h⁻¹ Im_h P_(ϵ_♭) = ϵ_♭ 𝒫_1(z) − ℓ ϵ_♭ 𝒬.                                                          {#eq:i-b-4-3}

**Proposition {#prop:i-b-4-5}** (Propagation.) Let ϵ_♭, ς ∈ {1, −1}, z_* ∈ Z and ϖ_0 ∈ 𝒫 with 𝖧_(z_*)(ϖ_0) ≠ 0 and
ϵ_♭ ς q̂_(z_*)(ϖ_0) > 0. Let U_0 be a neighbourhood of ϖ_0 such that for z ∈ Z

    ς𝖧_(Re z) 𝖻 ≤ 0 on U_0,     ς𝖧_(Re z) 𝗋 ≤ 0 on U_0 ∩ {ρ = 0}.                                       {#eq:i-b-4-4}

Let γ be the integral curve of ς𝖧_(z_*) with γ(0) = ϖ_0. There is T_0 > 0 such that for every neighbourhood W of
γ(−T_0/2) there are a neighbourhood Z_0 of z_* in Z, a neighbourhood U_* of γ([−T_0/4, 0]) and a compact set
K_E ⊂ W with the following property: for B_* ∈ Ψ^0 microsupported in U_*, E′ ∈ Ψ^0 elliptic on K_E, G ∈ Ψ^0 elliptic
on Ū_0, all M, z ∈ Z_0, h < h_0 and Schwartz u,

    ‖B_* u‖_𝐨 ≤ C(h⁻¹ ‖G P_(ϵ_♭) u‖_(𝐨−𝐦+(1,1,0)) + ‖E′u‖_𝐨 + h^M ‖Gu‖_𝐨 + ‖u‖_(−M𝟏)).                  {#eq:i-b-4-5}

So estimates propagate along ς𝖧 where ς has the sign of ϵ_♭ q: for P, along the future field sgn(q)𝖧 of
[[sec:i-b-1-3]]; for P^(*h), along the past field. The hypothesis [[eq:i-b-4-4]] is stated for 𝖧_(Re z) and not 𝖧_z;
the difference is absorbed in the proof by the term ℓ𝒬, which is where Im z ≥ 0 is used.

*Proof.* *Step 0: the box.* Apply [[lem:i-b-4-3]] to V_π := ς𝖧_z, π = (Re z, Im z), the formula [[eq:i-b-4-1]]
defining it for all π ∈ ℝ². This gives Π_0, U_1 ⊂ U_0 and τ; shrink them so that Ū_1 ⊂ U_0 is compact and
ϵ_♭ ς q̂_z ≥ c_0 > 0 on U_1 for z ∈ Z_0 := Z ∩ Π_0 (q̂_z is continuous in (ϖ, Re z)). Put T_0 := τ/4. In the
coordinates of z_*, γ(t) = (t, y_0).

*Step 1: one commutant.* Fix z ∈ Z_0, numbers t_− < t_+ in (−3T_0, T_0), ϵ ∈ (0, T_0/8] and η_1 > 0 such that
{t ∈ [t_− − ϵ, t_+ + ϵ], |y − y_0| ≤ η_1 + ϵ} ⊂ U_1 in the coordinates of z. With χ from [[lem:i-b-4-4]] put
χ_−(t) := χ((t − t_− + ϵ)/ϵ), χ_+(t) := χ((t_+ + ϵ − t)/ϵ), ψ(y) := χ(((η_1 + ϵ)² − |y − y_0|²)/(2η_1ϵ + ϵ²)), and

    φ := e^(−M_1 t) χ_−(t) χ_+(t) ψ(y),     ǎ := w_𝐤 φ,     Ǎ := ½(Op_h(ǎ Id) + Op_h(ǎ Id)^(*h)),

with 𝐤 from [[eq:i-b-3-2]] and M_1 chosen below. φ ∈ C_c^∞(U_1), so ǎ ∈ S^𝐤 with seminorms uniform in z ∈ Z_0, and
Ǎ = Ǎ^(*h) has principal symbol ǎ Id. Let C be [[eq:i-b-3-1]] for P_(ϵ_♭). By [[eq:i-b-4-3]],
C = C′ − ℓϵ_♭(Ǎ²𝒬 + 𝒬Ǎ²) with C′ := (i/h)[Re_h P, Ǎ²] + ϵ_♭(Ǎ²𝒫_1 + 𝒫_1Ǎ²), and by [[sec:i-b-3-2]] and
[[lem:i-b-4-1]] the principal symbol of ςC′ is ςμ𝖧_z(ǎ²) + 2ςϵ_♭ ǎ² p_1(z), with remainder in Ψ^(2𝐨−𝟏+ϵ′𝟏).
Since μ w_𝐤² = w_(2𝐨), ς𝖧_z t = 1 and 𝖧_z ψ = 0,

    ςμ𝖧_z(ǎ²) + 2ςϵ_♭ ǎ² p_1 = w_(2𝐨) [2φ ∂_t φ + φ² (β + 2(ς𝖧_z 𝗋) log⟨x⟩ + 2(ς𝖧_z 𝖻) log(1/h))],
    β := 2(s − ½) ς𝖧_z log⟨ζ⟩ + 2(𝗋 + ½) ς𝖧_z log⟨x⟩ + 2ςϵ_♭ μ⁻¹ p_1(z),

using log w_𝐤 = (s − ½) log⟨ζ⟩ + (𝗋 + ½) log⟨x⟩ + 𝖻 log(1/h). β is bounded on U_1 uniformly in z ([[lem:i-b-4-1]])
and h-self-adjoint. Next, 2φ ∂_t φ = −2M_1 φ² + e² − f_+² with

    e := e^(−M_1 t) ψ χ_+ √(2χ_−χ_−′),     f_+ := e^(−M_1 t) ψ χ_− √(−2χ_+χ_+′),

smooth by [[lem:i-b-4-4]], e supported in {t ∈ [t_− − ϵ, t_−]} and f_+ in {t ∈ [t_+, t_+ + ϵ]}.

*The decay order.* f_r := ς𝖧_(Re z) 𝗋 is smooth on 𝒫 and ≤ 0 on U_0 ∩ {ρ = 0}, so f_r ≤ C_r ρ on Ū_1, uniformly in
z. By [[lem:i-b-4-1]], ς𝖧_z 𝗋 = f_r − ς(Im z)² 𝖧^(2) 𝗋 with |𝖧^(2) 𝗋| ≤ C ρ². Let χ̃ ∈ C_c^∞(U_1), 0 ≤ χ̃ ≤ 1, equal 1
on a neighbourhood of every supp φ considered. Then on supp φ

    2(ς𝖧_z 𝗋) log⟨x⟩ = −κ_r + β_r,     κ_r := 2χ̃(C_r ρ − f_r) log⟨x⟩ ≥ 0,

with β_r := 2(C_r ρ − ς(Im z)² 𝖧^(2) 𝗋) log⟨x⟩ bounded with all derivatives obeying [[eq:i-b-2-1]].

*The semiclassical order.* f_b := ς𝖧_(Re z) 𝖻 ≤ 0 on U_0; put κ_b := −2χ̃ f_b log(1/h) ≥ 0. The rest is
−2ς(Im z)² (𝖧^(2) 𝖻) log(1/h) = −ℓ c_b with c_b := 2ςh(Im z) log(1/h) 𝖧^(2) 𝖻; note
|c_b| ≤ C h log(1/h) ρ² ρ_∞².

Let Q_0 := 2M_1 − β − β_r on U_1, and choose M_1 with Q_0 ≥ M_1 Id there for z ∈ Z_0; replace Q_0 by
χ̃Q_0 + (1 − χ̃)M_1 Id, which is ≥ M_1 Id everywhere. κ_0 := κ_r + κ_b satisfies the hypotheses of
[[lem:i-b-2-12]] (with κ := κ_0 and c_Q := M_1). With

    b := w_𝐨 φ (Q_0 + κ_0)^(1/2),     B := Op_h(b),     E := Op_h(w_𝐨 e Id),     F_+ := Op_h(w_𝐨 f_+ Id),

the principal symbol of ςC′ is −b² + w_(2𝐨) e² − w_(2𝐨) f_+² − ℓ w_(2𝐨) φ² c_b, and b is h-self-adjoint, as Q_0 is.
So

    ςC′ = −B^(*h)B + E^(*h)E − F_+^(*h)F_+ − ℓ Ǎ Op_h(μ c_b χ̃) Ǎ + R_1,     R_1 ∈ Ψ^(2𝐨−½𝟏):

the principal symbols agree; B ∈ Ψ^(𝐨+ϵ′𝟏) ([[lem:i-b-2-12]]), so B^(*h)B is determined by its principal symbol modulo
Ψ^(2𝐨−𝟏+3ϵ′𝟏); and μ c_b ∈ S^((1,−1,−1+ϵ′)), so Ǎ Op_h(μ c_b χ̃) Ǎ is determined modulo
Ψ^(2𝐤+(1,−1,−1+ϵ′)−𝟏+ϵ′𝟏) = Ψ^(2𝐨−(1,1,2)+2ϵ′𝟏), which ℓ ≤ 2h⁻¹ turns into Ψ^(2𝐨−𝟏+2ϵ′𝟏).

*The absorbing term.* By XǍ² + Ǎ²X = 2ǍXǍ + [[X, Ǎ], Ǎ],
ςC = ςC′ − 2ℓǍ(ςϵ_♭𝒬)Ǎ − ℓς[[ϵ_♭𝒬, Ǎ], Ǎ]. Let 𝒬_♯ be the h-self-adjoint part of
ςϵ_♭𝒬 + ½ Op_h(μ c_b χ̃). Then ςC = −B^(*h)B − F + E^(*h)E + R, where

    F := 2ℓǍ𝒬_♯Ǎ + F_+^(*h)F_+,     R := R_1 − ℓς[[ϵ_♭𝒬, Ǎ], Ǎ] − ℓǍ Op_h(μ c_b χ̃)^a Ǎ,

the last term involving the anti-self-adjoint part Op_h(μ c_b χ̃)^a ∈ Ψ^((0,−2,−2+ϵ′)) of Op_h(μ c_b χ̃) (its symbol is
real, [[thm:i-b-2-5]]), hence in Ψ^(2𝐨−(1,1,1)+(0,0,ϵ′)). 𝒬_♯ ∈ Ψ^((1,0,0)) has principal symbol ϵ_♭ς q_z (the added
term is of lower order), which is ≥ c_0⟨ζ⟩ on U_1; so by the paragraph on positivity of absorbing terms in
[[sec:i-b-3-3]], with 𝐭 = (½, 0, 0), ⟨Fw, w⟩ ≥ −C‖w‖²_(−M𝟏), and the double commutator lies in
ℓΨ^(2𝐤+(1,0,0)−2𝟏+ϵ′𝟏) ⊂ Ψ^(2𝐨−½𝟏). So R ∈ Ψ^(2𝐨−½𝟏). Finally Ǎ = ZB + Y with
Z := Op_h(w_(𝐤−𝐨) χ̃ (Q_0 + κ_0)^(−1/2)) ∈ Ψ^(−½(𝐦−(1,1,0))) ([[lem:i-b-2-12]]) and Y ∈ Ψ^(𝐤−½𝟏), since the principal
symbol of ZB is ǎ. So [[eq:i-b-3-3]] holds with J = 0, K_1 := supp φ and K_E := supp e, and by [[lem:i-b-2-12]], B is
elliptic, in the sense of [[prop:i-b-2-10]], on {φ ≠ 0} ⊃ {t ∈ (t_− − ϵ, t_+ + ϵ), |y − y_0| < η_1 + ϵ}. All
seminorms and C_F are uniform in z ∈ Z_0 and in the parameters t_±, ϵ, η_1 on compact sets of them.

*Step 2: iteration.* Let η > 0, to be fixed by W. In the coordinates of z put Λ_z := {t ∈ [−T_0/2, 0],
|y − y_0| ≤ η}, c_j := 2^(−j) c_0 for j = 0, …, J := 4M, with c_0 ≤ T_0/4, and
U_j(z) := {t ∈ (−T_0/2 − 3c_j, 2c_j), |y − y_0| < η + 2c_j}, a decreasing sequence. The proof of [[lem:i-b-3-4]] uses
its hypothesis only for the sets U_0 ⊃ ⋯ ⊃ U_J it chooses, the j-th being the set U′ for the (j − 1)-st; here Step 1
with t_− := −T_0/2 − 2c_j, t_+ := c_j, ϵ := c_j − c_(j+1), η_1 := η + c_j gives a commutant microsupported in U_j(z)
whose B is elliptic on
{t ∈ (−T_0/2 − 3c_j + c_(j+1), 2c_j − c_(j+1)), |y − y_0| < η + 2c_j − c_(j+1)} ⊃ Ū_(j+1)(z), as c_(j+1) = c_j/2,
with K_E ⊂ {t ∈ [−T_0/2 − 3c_j, −T_0/2 − 2c_j]}, disjoint from Λ_z. So [[eq:i-b-3-5]] holds for B_* microsupported in
U_J(z) and E′ elliptic on K_E^*(z) := ⋃_j K_E ⊂ {t ∈ [−T_0/2 − 3c_0, −T_0/2 − 2c_J], |y − y_0| ≤ η + 2c_0}, uniformly
in z ∈ Z_0.

*Step 3: removing z from the sets.* Given W, choose η and shrink c_0 (all c_j by a common factor) so that, in the
coordinates of z_*, {t ∈ [−T_0/2 − 4c_0, −T_0/2], |y − y_0| ≤ η + 3c_0} ⊂ W. As the coordinates depend continuously on
z in C^∞, there is a neighbourhood Z_0′ ⊂ Z_0 of z_* such that for z ∈ Z_0′ the set K_E^*(z) lies in the compact set
K_E := {t_(z_*) ∈ [−T_0/2 − 4c_0, −T_0/2 − c_J], |y_(z_*) − y_0| ≤ η + 3c_0} ⊂ W, and U_J(z) contains
U_* := {t_(z_*) ∈ (−T_0/4 − c_J, c_J), |y_(z_*) − y_0| < η}, a neighbourhood of γ([−T_0/4, 0]). Then
[[eq:i-b-4-5]] holds for z ∈ Z_0′; rename Z_0′ as Z_0. ∎

**Corollary {#cor:i-b-4-6}** (Propagation along a segment.) Let ϵ_♭, ς be signs, z_* ∈ Z, and γ : [−T, 0] → 𝒫 an
integral curve of ς𝖧_(z_*) with 𝖧_(z_*) ≠ 0 and ϵ_♭ ς q̂_(z_*) > 0 on γ([−T, 0]). Let U_0 be a neighbourhood of
γ([−T, 0]) on which [[eq:i-b-4-4]] holds. Then for every neighbourhood W of γ(−T) there are a neighbourhood Z′ of z_*,
a neighbourhood U_* of γ(0) and a compact K_E ⊂ W such that [[eq:i-b-4-5]] holds for z ∈ Z′, B_* microsupported in
U_*, E′ elliptic on K_E and G elliptic on Ū_0.

*Proof.* U_0 contains γ([−T − δ_γ, δ_γ]) for some δ_γ > 0, and after shrinking δ_γ the hypotheses hold on that longer
segment. The flow boxes of [[lem:i-b-4-3]] at its points have sizes bounded below, since a box at ϖ serves a
neighbourhood of ϖ with half its size ([[lem:i-b-4-3]]); so [[prop:i-b-4-5]] holds at every γ(t) with one T_1 > 0 in
place of T_0, which we may decrease so that T_1 ≤ δ_γ/8 and L := 4(T − T_1/2)/T_1 ∈ ℕ. Let
τ_l := −T + T_1/2 + (l − 1)T_1/4, l = 1, …, L + 1, so τ_(L+1) = 0. Apply [[prop:i-b-4-5]] at γ(τ_1) with W_1 := W, a
neighbourhood of γ(τ_1 − T_1/2) = γ(−T); this gives Z^(1), U_*^(1) ⊃ γ([τ_1 − T_1/4, τ_1]) and K_E^(1) ⊂ W. For l ≥ 2
apply it at γ(τ_l) with W_l := U_*^(l−1), a neighbourhood of γ(τ_l − T_1/2) = γ(τ_(l−1) − T_1/4). The operator E′_l
elliptic on K_E^(l) ⊂ U_*^(l−1) may be taken microsupported in U_*^(l−1), so it is an admissible B_* at step l − 1.
Chaining the L + 1 estimates, with Z′ := ⋂_l Z^(l) and U_* := U_*^(L+1), gives the claim. ∎

**Remark {#rem:i-b-4-7}** Over a compact subset of T*X̃° at finite frequencies, [[prop:i-b-4-5]] and [[cor:i-b-4-6]]
also hold (a) for z = z_0 + iy with y ∈ [−Ch, 0]: then ℓ ∈ [−C, 0], ℓ𝒬 is a bounded term of the class of 𝒫_1 there,
it is put into β, and the condition ϵ_♭ ς q̂ > 0 is not needed (for |ℓ| ≤ C the same holds with either sign of Im z);
and (b) when h⁻¹ Im_h 𝐏 contains a further term −ϵ_W h⁻¹ W^(*h)W, ϵ_W ∈ {1, −1}, with W ∈ Ψ^((1,0,0)) scalar, and a
further bounded term of the class of 𝒫_1, provided ςϵ_W = 1: the first enters ςC as −2h⁻¹ ǍW^(*h)WǍ plus a double
commutator in hΨ, a term −F with ⟨Fw, w⟩ ≥ 0 exactly, as in case (B) of [[lem:i-b-5-1]], and the second is part of
β. Both are used in [[sec:i-b-6]] only.

**Corollary {#cor:i-b-4-6-prime}** (All orders lowered.) In the setting of [[cor:i-b-4-6]], for every J ∈ ℕ the
estimate [[eq:i-b-4-5]] holds with h^M ‖Gu‖_𝐨 replaced by ‖Gu‖_(𝐨−(J/4)𝟏).

*Proof.* In the proof of [[lem:i-b-3-4]] apply [[lem:i-b-3-3]] at the orders 𝐨 − ((J − j)/4)𝟏, j = 1, …, J, in place
of 𝐨 − (0, 0, (J − j)/4). This needs a decomposition [[eq:i-b-3-3]] at each of these orders, with the same sets: in
[[prop:i-b-4-5]] the order enters the commutant only through the constant β of its Step 1, which M_1 absorbs, so the
commutants exist at every order, on sets that do not depend on it. The error term of [[lem:i-b-3-3]] at the j-th step,
‖G_(j−1) u‖_(𝐨−((J−j+1)/4)𝟏), is the left side of the step before, and after J steps what is left is
‖Gu‖_(𝐨−(J/4)𝟏); the terms h⁻¹‖GPu‖ and ‖E′u‖ at lowered orders are bounded by those at 𝐨. The chaining along the
segment is that of [[cor:i-b-4-6]]. ∎

For 𝐨 = (s, 0, 0), s ≥ 0, J ≥ 4s and G microsupported over a compact subset of X̃°, ‖Gu‖_(𝐨−(J/4)𝟏) ≤ C ‖u‖_(L²):
the regularity order is at most 0, the decay order is immaterial over a compact set, and the semiclassical weight is
h^(J/4) ≤ 1.

The admissibility of [[sec:i-b-1-4]] is used through [[eq:i-b-4-4]]: it requires the monotonicity on a
*neighbourhood* U_0 of the curves along which we propagate (for 𝗋, a neighbourhood within the face over ∂X), not only
on the characteristic set. A logarithmic weight log(1/h) multiplies 𝖧𝖻, so a positive value of 𝖧𝖻 off the
characteristic set but on the support of a commutant could not be absorbed. [[sec:i-b-1-4]] is stated in this form.

### Radial estimates {#sec:i-b-5}

The three radial sets are ∂ℛ_± at fibre infinity over the horizon, and R_(z_0,in), R_out over ∂X. One lemma serves all
three, for the operator and its adjoint. Notation is that of [[sec:i-b-4]].

#### A radial estimate {#sec:i-b-5-1}

Let 𝐏 be one of c_z P, (c_z P)^(*h), where c_z ∈ {1, z⁻¹} is fixed, and let ϵ_♭ := 1, resp. −1. Then
Re_h 𝐏 = Re_h(c_z P) and Im_h 𝐏 = ϵ_♭ Im_h(c_z P); since |c_z| ∈ [½, 2], an estimate for 𝐏 is one for P, resp.
P^(*h).

**Lemma {#lem:i-b-5-1}** (Radial estimate.) Let F be one of the two boundary faces of 𝒫, with defining function ϱ (ρ_∞
or ρ), Z′ ⊂ Z compact, Λ ⊂ F compact, U_0 a neighbourhood of Λ with compact closure, and ς ∈ {1, −1}. Suppose,
uniformly for z ∈ Z′:

(i) Re_h 𝐏 − Op_h(p_z Id) ∈ Ψ^((1,−1,−1)), p_z real and classical of order (2, 0), continuous in z;
𝖧_z^𝐏 := μ⁻¹ H_(p_z) ([[lem:i-b-4-1]] (c)) vanishes at every point of Λ, and β_ϱ := ϱ⁻¹ ς𝖧_z^𝐏 ϱ satisfies either
β_ϱ ≥ β_* on U_0 (*source*) or β_ϱ ≤ −β_* on U_0 (*sink*), for some β_* > 0.

(ii) h⁻¹ Im_h 𝐏 = ϵ_♭(𝒫_1^𝐏 − ℓ𝒜) with 𝒫_1^𝐏 ∈ Ψ^((1,−1,0)) h-self-adjoint, of principal symbol p_1^𝐏, and either
(A) ϵ_♭ς𝒜 ∈ Ψ^((1,0,0)) is h-self-adjoint with principal symbol ≥ c_0⟨ζ⟩ Id on U_0; or (B) Ū_0 lies at finite
frequencies, ϵ_♭ς = 1 and 𝒜 = Σ_(j,k) W_j^(*h) M̃_jk W_k + 𝒜_0 + 𝒜_1, where the W_j ∈ Ψ^((1,0,0)) are scalar
semiclassical differential operators acting componentwise, M̃ = (M̃_jk) and 𝒜_0 are matrix functions with M̃ ≥ 0 for
h^(⊕J) and 𝒜_0 ≥ 0 for h everywhere, and 𝒜_1 is a differential operator whose coefficients vanish near the base
projection of Ū_0.

(iii) There are real g, φ ∈ C^∞(𝒫), continuous in z, φ ≥ 0, with Λ = Ū_0 ∩ {ϱ = 0, φ = 0, g = 0},
|ρ_∞² 𝐠_z| ≥ c|g| − Cϱ on U_0 where 𝐠_z is the principal symbol of 𝐏, and on U_0

    ς𝖧_z^𝐏 φ ≥ c_1 φ − C_1(ϱ + g²)  (source),     ς𝖧_z^𝐏 φ ≤ −c_1 φ + C_1(ϱ + g²)  (sink).              {#eq:i-b-5-1}

(iv) 𝗋 and 𝖻 are constant on U_0. Put κ̃ := s − ½ if F is fibre infinity and κ̃ := 𝗋 + ½ if F is the face over ∂X.

(v) (Threshold.) On Λ the h-self-adjoint endomorphism

    𝒯 := 2κ̃ β_ϱ Id − 2ςϵ_♭ μ⁻¹ p_1^𝐏                                                                  {#eq:i-b-5-2}

satisfies 𝒯 ≥ c_𝒯 Id, c_𝒯 > 0.

Then there are a neighbourhood U_* of Λ and a compact set K_E ⊂ Ū_0 ∖ Λ such that for B_* ∈ Ψ^0 microsupported in U_*,
G ∈ Ψ^0 elliptic on Ū_0, E′ ∈ Ψ^0 elliptic on K_E, all M, z ∈ Z′, h < h_0 and Schwartz u,

    ‖B_* u‖_𝐨 ≤ C(h⁻¹ ‖G𝐏u‖_(𝐨−𝐦+(1,1,0)) + δ_sink ‖E′u‖_𝐨 + h^M ‖Gu‖_𝐨 + ‖u‖_(−M𝟏)),                {#eq:i-b-5-3}

where δ_sink := 0 if Λ is a source, and δ_sink := 1 if Λ is a sink.

So at a source, the estimate needs no control near Λ, and at a sink it needs control on a punctured neighbourhood; the
threshold [[eq:i-b-5-2]] decides which orders are allowed. At a source, [[eq:i-b-5-2]] asks κ̃ to be large (a high
regularity or decay order); at a sink, small.

*Proof.* *The cut-offs.* Let χ_0(t) := χ(2 − t) with χ from [[lem:i-b-4-4]]: χ_0 = 1 on (−∞, 1], χ_0 = 0 on [2, ∞),
χ_0′ ≤ 0, √(−χ_0χ_0′) smooth. For δ = (δ_1, δ_2, δ_3) put

    φ_δ := χ_0(ϱ/δ_1) χ_0(φ/δ_2) χ_0(g²/δ_3) on U_0,     K_δ := Ū_0 ∩ {ϱ ≤ 2δ_1, φ ≤ 2δ_2, g² ≤ 2δ_3}.

The compact sets K_δ decrease to Λ as δ → 0, so K_δ ⊂ U_0 for δ small, and then φ_δ, extended by 0, is smooth on 𝒫
with support in K_δ; and every neighbourhood of Λ contains K_δ for δ small. We take
δ_1 ≤ c_δ min(δ_2, √δ_3) and δ_3 ≤ c_δ δ_2, with c_δ := min(c_1/(16C_1), c/(4C), 1); this is preserved by
δ ↦ δ/4. Then: on supp χ_0′(φ/δ_2) ∩ K_δ we have φ ≥ δ_2, so by [[eq:i-b-5-1]]
±ς𝖧_z^𝐏 φ ≥ c_1δ_2 − C_1(2δ_1 + 2δ_3) ≥ ½c_1δ_2 (upper sign at a source, lower at a sink); and on
supp χ_0′(g²/δ_3) ∩ K_δ, |ρ_∞² 𝐠_z| ≥ c√δ_3 − 2Cδ_1 > 0, so 𝐏 is elliptic there.

*The commutant.* ǎ := w_𝐤 φ_δ, Ǎ := ½(Op_h(ǎ Id) + Op_h(ǎ Id)^(*h)), 𝐤 from [[eq:i-b-3-2]]. As in Step 1 of
[[prop:i-b-4-5]], with 𝗋, 𝖻 constant on U_0, the principal symbol of ςC′ (where C = C′ − ℓϵ_♭(Ǎ²𝒜 + 𝒜Ǎ²)) is
w_(2𝐨)[2φ_δ ς𝖧_z^𝐏 φ_δ + φ_δ² β] with

    β := 2(s − ½) ς𝖧_z^𝐏 log⟨ζ⟩ + 2(𝗋 + ½) ς𝖧_z^𝐏 log⟨x⟩ + 2ςϵ_♭ μ⁻¹ p_1^𝐏.

At Λ ⊂ F, one of log⟨ζ⟩, log⟨x⟩ is log ϱ⁻¹, with ς𝖧 log ϱ⁻¹ = −β_ϱ; the other is smooth near Λ, so its derivative
along 𝖧_z^𝐏 vanishes on Λ, where the vector field vanishes. So β = −𝒯 on Λ, and −β ≥ ½c_𝒯 Id on K_δ for δ small,
uniformly in z ∈ Z′. Let Q_0 := χ̃(−β) + (1 − χ̃)½c_𝒯 Id with χ̃ ∈ C_c^∞(U_0) equal to 1 on K_δ, and
b := w_𝐨 φ_δ Q_0^(1/2) ∈ S^𝐨.

*The cut-off terms.* 2φ_δ ς𝖧φ_δ = Σ_(i=1)^3 k_i, where, with a_1 := ϱ, a_2 := φ, a_3 := g² and
φ_i := χ_0(a_i/δ_i), k_i := 2φ_i χ_0′(a_i/δ_i) δ_i⁻¹ (ς𝖧a_i) Π_(j≠i) φ_j². Since χ_0χ_0′ ≤ 0: k_1 has the sign of
−β_ϱϱ, and k_2 that of ∓1, on their supports; k_3 is supported where 𝐏 is elliptic. If Λ is a source, k_1 = −f_1²,
k_2 = −f_2² with

    f_1 := √(−2χ_0χ_0′)(ϱ/δ_1) (β_ϱϱ/δ_1)^(1/2) φ_2 φ_3,     f_2 := √(−2χ_0χ_0′)(φ/δ_2) (ς𝖧φ/δ_2)^(1/2) φ_1 φ_3,

smooth, because β_ϱϱ ≥ β_*δ_1 and ς𝖧φ ≥ ½c_1δ_2 on a neighbourhood of the supports (the square roots of positive
smooth functions there). If Λ is a sink, k_1 = e_1², k_2 = e_2² likewise, with −β_ϱ, −ς𝖧φ under the roots. Let
j_3 := w_(2𝐨) k_3 𝐠_z⁻¹ ∈ S^(2𝐨−𝐦) ([[lem:i-b-2-2]] (e)) and J := Op_h(j_3 Id); WF′_h(J) ⊂ supp k_3 ⊂ Ell_h(𝐏), and
J𝐏 has principal symbol w_(2𝐨) k_3.

*The absorbing term.* In case (A) it is treated exactly as in [[prop:i-b-4-5]] (here c_b = 0): −2ℓǍ(ϵ_♭ς𝒜)Ǎ is a term
−F_abs with ⟨F_abs w, w⟩ ≥ −C‖w‖²_(−M𝟏), and the double commutator is in Ψ^(2𝐨−½𝟏). In case (B),
−ℓ(Ǎ²𝒜 + 𝒜Ǎ²) = −2ℓǍ𝒜Ǎ − ℓ[[𝒜, Ǎ], Ǎ], and for every w

    ⟨Ǎ𝒜Ǎw, w⟩_h = ⟨M̃ WǍw, WǍw⟩_(h^(⊕J)) + ⟨𝒜_0 Ǎw, Ǎw⟩_h ≥ 0

exactly, the integrands being pointwise non-negative, where now 𝒜 stands for 𝒜 − 𝒜_1; so F_abs := 2ℓǍ(𝒜 − 𝒜_1)Ǎ
satisfies ⟨F_abs w, w⟩ ≥ 0. The terms with 𝒜_1, ℓ(Ǎ²𝒜_1 + 𝒜_1Ǎ²), are residual: WF′_h(𝒜_1) lies over the support of
its coefficients, disjoint from WF′_h(Ǎ), and ℓ ≤ 2h⁻¹. As Ǎ is microsupported at finite frequencies, the order of 𝒜
in ζ does not matter, and ℓ[[𝒜, Ǎ], Ǎ] ∈ Ψ^(2𝐤−(2,2,1)+ϵ′𝟏) ⊂ Ψ^(2𝐨−½𝟏) near Ū_0.

*Conclusion.* With B := Op_h(b), F := F_abs + Σ_i F_i^(*h)F_i and E the operators Op_h(w_𝐨 e_i Id) (source:
F_i := Op_h(w_𝐨 f_i Id), no E; sink: no F_i, E from e_1, e_2, with E^(*h)E read as the sum), we get
ςC = −B^(*h)B − F + E^(*h)E + J𝐏 + R with R ∈ Ψ^(2𝐨−½𝟏), since all principal symbols agree. Ǎ = ZB + Y with
Z := Op_h(w_(𝐤−𝐨) χ̃ Q_0^(−1/2)), and B is elliptic on {φ_δ ≠ 0} ⊃ K_(δ/2). The sets supp e_i lie in
{ϱ ≥ δ_1} ∪ {φ ≥ δ_2}, closed and disjoint from Λ. [[lem:i-b-3-3]] applies, and [[lem:i-b-3-4]] with
U_j := K°_(2·4^(−j)δ) and, at the j-th step, the commutant above with δ replaced by 4^(1−j)δ, supported in
K_(4^(1−j)δ) ⊂ U_(j−1) with B elliptic on K_(4^(1−j)δ/2) ⊃ Ū_j (the hypothesis being used only for these sets, as in
[[prop:i-b-4-5]]), gives [[eq:i-b-5-3]] with U_* := K°_(2·4^(−J)δ) and K_E := Ū_0 ∩ ⋃_j supp(e_1 + e_2) at the j-th
step. Uniformity in z ∈ Z′ holds because every symbol above, and every lower bound used, is uniform. ∎

#### The horizon {#sec:i-b-5-2}

**Proposition {#prop:i-b-5-2}** (Cf. [Hin26c, Proposition 9.18] at the horizon and [[prop:i-a-4-2]].) Let
s > ½ + ϑ_ℋ, Z compact as in [[sec:i-b-4]], and 𝗋, 𝖻 constant near ∂ℛ_+ ∪ ∂ℛ_−. For each sign ± there are
neighbourhoods U_* ⊂ U_0 of ∂ℛ_±, with U_0 over {|r − r_h| < δ_0}, and a compact K_E ⊂ Ū_0 ∖ ∂ℛ_±, such that,
uniformly in z ∈ Z, for B_* microsupported in U_* and G elliptic on Ū_0:

    ‖B_* u‖_𝐨 ≤ C(h⁻¹ ‖GPu‖_(𝐨−𝐦+(1,1,0)) + h^M ‖Gu‖_𝐨 + ‖u‖_(−M𝟏)),     𝐨 = (s, 𝗋, 𝖻),                  {#eq:i-b-5-4}

    ‖B_* v‖_(𝐨*) ≤ C(h⁻¹ ‖GP^(*h)v‖_(𝐨*−𝐦+(1,1,0)) + ‖E′v‖_(𝐨*) + h^M ‖Gv‖_(𝐨*) + ‖v‖_(−M𝟏)),
    𝐨* = (1 − s, 𝗋*, 𝖻*),                                                                              {#eq:i-b-5-5}

for any orders 𝗋*, 𝖻* constant near ∂ℛ_±, with E′ elliptic on K_E. The fibre inner product may be chosen near ∂ℛ_±
as in (O3) of [[def:i-a-admissible]]; the adjoint in [[eq:i-b-5-5]] may be taken in any fibre inner product
([[prop:i-a-4-2]]). The band {|r − r_h| < δ_0} may be replaced by {|r − r_h| < δ} for any δ ∈ (0, δ_0]: the
proposition asserts neighbourhoods inside the band, and its proof is local at ∂ℛ_±.

*Proof.* Apply [[lem:i-b-5-1]] with c_z = 1, F fibre infinity, Λ := ∂ℛ_±, and ς := ±ϵ_♭. By (H3) and
[[lem:i-b-1-1]] (e), ±q̂_z > 0 near ∂ℛ_±, uniformly in z (at fibre infinity q̂_z = −ρ_∞τ_1 up to O(ρ_∞)); so (A) holds
with 𝒜 = 𝒬. At fibre infinity 𝖧_z = ρ⁻¹ρ_∞ H_(G_0) does not depend on z, and ±𝖧_z is ρ⁻¹ times the future field 𝖧 of
(H3); so β_ϱ = ϵ_♭ β_0′ with β_0′ := ρ⁻¹β_0 > 0 on ∂ℛ_±, hence on a neighbourhood: for P it is a source; for
P^(*h), a sink. 𝖧_z vanishes on ∂ℛ_± as a vector field on 𝒫: it is tangent to fibre infinity, vanishes on ∂ℛ_± within it
(radial points), and 𝖧_z ρ_∞ = β_ϱ ρ_∞ = 0 there.

For (iii) take g := Ĝ_0, and φ := q_± ∘ π, where q_± is the quadratic defining function of (H3) and π a smooth
retraction of a neighbourhood of ∂ℛ_± in 𝒫 onto ∂Σ_0 (projecting along the level sets of a complement of (ρ_∞, Ĝ_0) in
a coordinate system, as in [[lem:i-a-4-1]]). Ellipticity: |Ĝ_z| ≥ |Re Ĝ_z| ≥ |Ĝ_0| − Cρ_∞. For [[eq:i-b-5-1]]: at a
point ϖ, 𝖧_z φ(ϖ) = dq_±(π_*𝖧_z(ϖ)) and π_*𝖧_z(ϖ) = 𝖧_z(πϖ) + O(|Ĝ_0(ϖ)| + ρ_∞(ϖ)); and |dq_±| ≤ C√q_±, as q_± ≥ 0
is smooth (for a non-negative C² function, |∇f|² ≤ 2f sup|∇²f|). With 𝖧q_± ≥ c q_± near ∂ℛ_± in ∂Σ_0 ((H3), 𝖧 the
future field), and ς𝖧_z = ϵ_♭ρ⁻¹𝖧 at fibre infinity,

    ς𝖧_z φ ≥ c ρ⁻¹ φ − C(|g| + ρ_∞)√φ   if ϵ_♭ = 1,     ς𝖧_z φ ≤ −c ρ⁻¹ φ + C(|g| + ρ_∞)√φ   if ϵ_♭ = −1,

and C|g|√φ ≤ (c/4)ρ⁻¹φ + C′g², C ρ_∞ √φ ≤ C′ρ_∞ on U_0; this is [[eq:i-b-5-1]] (for ϵ_♭ = 1 at a source, for
ϵ_♭ = −1 at a sink). (iv) holds by assumption. For (v): μ⁻¹p_1 = ρ⁻¹ρ_∞p_1 and, at fibre infinity,
ρ_∞p_1(z) = ρ_∞σ_1(Im_h P̂(0)), the term (Re z) Im_h T being of lower order there. With ςϵ_♭ = ±1 and
p_(1,±) := ±ρ_∞σ_1(Im_h P̂(0)) ([[eq:i-a-1-5]]),

    𝒯 = 2ρ⁻¹(κ̃ ϵ_♭ β_0 − p_(1,±)) = 2ρ⁻¹β_0(ϵ_♭κ̃ − β_0⁻¹ p_(1,±))

(both β_0 and p_(1,±) evaluated on ∂ℛ_±; β_0⁻¹p_(1,±) is h-self-adjoint). For P, κ̃ = s − ½, and 𝒯 > 0 if and only if
s − ½ > max spec(β_0⁻¹p_(1,±)), which holds as s > ½ + ϑ_ℋ. For P^(*h) at the order 𝐨*, κ̃ = ½ − s and ϵ_♭ = −1: the
same condition. [[lem:i-b-5-1]] gives [[eq:i-b-5-4]] and [[eq:i-b-5-5]]. ∎

#### The incoming radial set {#sec:i-b-5-3}

**Proposition {#prop:i-b-5-3}** (Cf. [[prop:i-a-4-6]].) Let z_0 ∈ {1, −1}, ν_1 > 0 and Z_in := z_0 + i[0, ν_1]. Let
𝗋, 𝖻 be constant near R_(z_0,in), with 𝗋 > ½(−1 + ϑ_in) there, the fibre inner product chosen as in (O3) of
[[def:i-a-admissible]]. Then there are neighbourhoods U_* ⊂ U_0 of R_(z_0,in) at finite frequencies and a compact
K_E ⊂ Ū_0 ∖ R_(z_0,in) such that [[eq:i-b-5-4]] holds for z ∈ Z_in with 𝐨 = (s, 𝗋, 𝖻), and [[eq:i-b-5-5]] holds with
𝐨* = (s*, −𝗋 − 1, 𝖻*) for any s* and any 𝖻* constant near R_(z_0,in).

*Proof.* [[lem:i-b-5-1]] with c_z = 1, F the face over ∂X, Λ := R_(z_0,in), ς := ϵ_♭z_0. At the face q_z = −2ξ = 4z_0
on Λ, so (A) holds on a neighbourhood. At the face 𝖧_z = 𝖧_(z_0) ([[lem:i-b-4-1]] (c)) is ⟨ζ⟩⁻¹𝖵_p,
p = ξ² + 2z_0ξ + |η|², and by [[eq:i-a-4-4]], ρ⁻¹𝖵_p ρ = −∂_ξ p = 2z_0 on Λ, where ⟨ζ⟩ = √5; so
β_ϱ = ς · 2z_0/√5 = 2ϵ_♭/√5 on Λ, and 𝖧_z vanishes on Λ (there 𝖵_p = 2z_0ρ∂_ρ + H_p^(𝕊³) and both vanish at ρ = 0,
η = 0). For P it is a source; for P^(*h), a sink.

For (iii) take g := ξ² + 2z_0ξ + |η|² and φ := |η|² (round norm), extended to a neighbourhood of Λ in 𝒫 as functions of
(ω, ξ, η) in a collar. Λ = Ū_0 ∩ {ρ = 0, φ = 0, g = 0} for U_0 near Λ (the other solution of φ = g = 0 is R_out).
Re G_z = g + O(ρ) near the face, since g_00 ∈ ρ² C^∞; so |Ĝ_z| ≥ c|g| − Cρ. By [[eq:i-a-4-4]],
𝖵_p|η|² = −2(∂_ξ p)|η|² = −4(ξ + z_0)|η|², which near ξ = −2z_0 is 4z_0|η|²(1 + O(|ξ + 2z_0|)); so
ς𝖧_z φ = ϵ_♭ (4/⟨ζ⟩)|η|²(1 + O(|ξ + 2z_0|)) + O(ρ), which gives [[eq:i-b-5-1]] on a small U_0, with no g² term
needed. (iv) holds by assumption. For (v), at Λ, by [[lem:i-b-4-1]] (b),
μ⁻¹p_1 = ⟨ζ⟩⁻¹ρ⁻¹p_1 = (1/√5)(σ(ρ⁻¹ Im_h P̂(0))(−2z_0, 0) − z_0(S + S^(*h))), and the first term is linear in ζ
([[lem:i-a-4-4]] (b)), so it equals z_0 p_in with p_in of [[eq:i-a-1-5]]. Hence
ςϵ_♭μ⁻¹p_1 = z_0μ⁻¹p_1 = (1/√5)(p_in − (S + S^(*h))) for both signs of z_0, and

    𝒯 = (2/√5)(2ϵ_♭κ̃ Id − (p_in − (S + S^(*h)))).

For P, ϵ_♭κ̃ = 𝗋 + ½; for P^(*h) at the decay order −𝗋 − 1, ϵ_♭κ̃ = −(−𝗋 − 1 + ½) = 𝗋 + ½. In both cases 𝒯 > 0 on Λ
if and only if 2𝗋 + 1 > max spec(p_in − (S + S^(*h))) there, which holds as 𝗋 > ½(−1 + ϑ_in). ∎

#### The outgoing radial set {#sec:i-b-5-4}

Near R_out the absorbing term ℓ𝒬 has no sign, as q_z = −2ξ vanishes there. Dividing by z moves the large imaginary
part onto an operator that is non-negative exactly.

**Lemma {#lem:i-b-5-4}** (The semiclassical form of [Hin26c, (9.49)].) Let V_1 := ρ∂_ρ and
Ω_ab := x_a∂_b − x_b∂_a (1 ≤ a < b ≤ 4), and W := (W_0, W_ab) with W_0 := hρV_1, W_ab := hρΩ_ab, acting componentwise;
J := 7. Near ∂X, on {ρ < ρ_1},

    h² Re_h P̂(0) = W^(*h) M̃ W + h R_1^h,     M̃ = Id + ρΞ,                                             {#eq:i-b-5-6}

with Ξ a smooth h^(⊕J)-self-adjoint matrix function, and R_1^h ∈ hρ² Diff¹_b h-self-adjoint, whose semiclassical symbol
divided by ρ vanishes at R_out. With P̃ := z⁻¹P and ℓ = Im z/h,

    h⁻¹ Im_h P̃ = 𝒫̃_1 − ℓ𝒜,     𝒫̃_1 := Re(z⁻¹) h Im_h P̂(0) + Im_h T − (Im z/|z|²) R_1^h,
    𝒜 := W^(*h) M̃ W/|z|² − g_00.                                                                       {#eq:i-b-5-7}

𝒫̃_1 ∈ Ψ^((1,−1,0)) is h-self-adjoint and μ⁻¹σ(𝒫̃_1) = −(S + S^(*h)) at R_out; Re_h P̃ has principal symbol
p̃_z := Re(z⁻¹G_z) = Re(z⁻¹)G_0 + τ_1 + (Re z)g_00.

*Proof.* By (H2), P^(0) − ((ρD_ρ)² + Δ_(𝕊³)) Id ∈ Diff¹_b + ρ Diff²_b, and Δ_(𝕊³) = Σ_(a<b) Ω_ab* Ω_ab, the rotations
being divergence free for dx. Since (ρV_1)* = −ρV_1 + ρC^∞ and [ρ, V_1] ∈ ρC^∞,
h²ρ²(ρD_ρ)² = W_0*W_0 + h²ρ² Diff¹_b and h²ρ²Ω_ab*Ω_ab = W_ab*W_ab + h²ρ² Diff¹_b. An element of h²ρ³ Diff²_b is
Σ W_j* ρΞ′_jk W_k modulo h²ρ³ Diff¹_b, the second order part being spanned by products of the V's. W_j^(*h) − W_j* is a
matrix function times hρ. Take h-self-adjoint parts: the left side of [[eq:i-b-5-6]] is h-self-adjoint, so replacing
Ξ′ by its h^(⊕J)-self-adjoint part Ξ changes only the remainder, which lies in h²ρ² Diff¹_b = h · hρ² Diff¹_b. Its
symbol: hρ² Diff¹_b = ρ · hρ Diff¹_b, and hρ Diff¹_b consists of c · hρV + hρd, with semiclassical symbol linear in ζ
plus O(ρ); so the symbol divided by ρ vanishes at ζ = 0, ρ = 0. For [[eq:i-b-5-7]]: P̃ = z⁻¹h²P̂(0) + hT + zg_00 by
[[eq:i-b-1-2]], and Im_h(cA) = (Re c) Im_h A + (Im c) Re_h A with Im(z⁻¹) = −Im z/|z|². The symbol of 𝒫̃_1 at the
face is ρ times Re(z⁻¹)r_3 − (S + S^(*h)) plus a term vanishing at R_out, r_3 := σ(ρ⁻¹ Im_h P̂(0)) being linear
([[lem:i-a-4-4]] (b)); and μ = ρ at ζ = 0. ∎

**Proposition {#prop:i-b-5-5}** (Cf. [Hin26c, Proposition 9.27] and [[prop:i-a-4-9]].) Let Z be compact as in
[[sec:i-b-4]], 𝗋 and 𝖻 constant near R_out, and h a fibre inner product with
𝗋 < −½ + ½ inf_(∂X) min spec(S + S^(*h)). Then there are neighbourhoods U_* ⊂ U_0 of R_out at finite frequencies over
{ρ < ρ_1} and a compact K_E ⊂ Ū_0 ∖ R_out such that, uniformly in z ∈ Z,

    ‖B_* u‖_𝐨 ≤ C(h⁻¹ ‖GPu‖_(𝐨−𝐦+(1,1,0)) + ‖E′u‖_𝐨 + h^M ‖Gu‖_𝐨 + ‖u‖_(−M𝟏)),     𝐨 = (s, 𝗋, 𝖻),      {#eq:i-b-5-8}

and [[eq:i-b-5-4]] holds for P^(*h) at 𝐨* = (s*, −𝗋 − 1, 𝖻*) for every s* and every 𝖻* constant near R_out, with
B_*, G, E′ as in [[lem:i-b-5-1]]. By (O3) of [[def:i-a-admissible]] and [[lem:i-a-2-4]], h may be chosen so that the
condition reads 𝗋 < −½ + S̄ up to any given margin.

*Proof.* [[lem:i-b-5-1]] with c_z = z⁻¹, F the face over ∂X, Λ := R_out, ς := ϵ_♭, case (B): by [[lem:i-b-5-4]],
h⁻¹ Im_h 𝐏 = ϵ_♭(𝒫̃_1 − ℓ𝒜). Write M̃ = M̃_ext + (1 − χ_1)(M̃ − Id) with M̃_ext := χ_1M̃ + (1 − χ_1)Id, where
χ_1 ∈ C^∞(X̄) is supported in {ρ < ρ_2} and equal to 1 near the base projection of Ū_0, and ρ_2 is so small that
M̃ ≥ ½ Id on {ρ < ρ_2}; then M̃_ext ≥ ½ Id everywhere, and 𝒜_1 := |z|⁻² W^(*h)(1 − χ_1)(M̃ − Id)W (with M̃ extended
arbitrarily off {ρ < ρ_1}, and the identity [[eq:i-b-5-7]] used only near the base projection of Ū_0).
𝒜_0 := −g_00 ≥ 0 by (H6). So (ii)(B) holds. By [[eq:i-a-4-4]], at the face 𝖧_z^𝐏 = ⟨ζ⟩⁻¹𝖵_g̃ with
g̃ := 2ξ + a_z(ξ² + |η|²), a_z := Re(z⁻¹), and ([[eq:i-a-4-11]]) ρ⁻¹𝖵_g̃ ρ = −2(1 + a_zξ), 𝖵_g̃(ξ² + |η|²) = −4|η|²,
𝖵_g̃ g̃ = 0; 𝖵_g̃ vanishes at R_out as a vector field on 𝒫. So β_ϱ = −2ϵ_♭ at R_out, and ϵ_♭β_ϱ ≤ −1 near it: for P it
is a sink; for P^(*h), a source.

For (iii), g := g̃ and φ := ξ² + |η|², extended in a collar. |ρ_∞² z⁻¹G_z| ≥ |Re(z⁻¹Ĝ_z)| ≥ |g̃| − Cρ. On
{φ ≤ a_z^(−2)}, 2ξ = g − a_zφ gives ξ² ≤ ½(g² + a_z²φ²) ≤ ½g² + ½φ, hence |η|² ≥ ½φ − ½g² and
ς𝖧_z^𝐏 φ = −4ϵ_♭⟨ζ⟩⁻¹|η|² + O(ρ), which is [[eq:i-b-5-1]] (for P at a sink; for P^(*h), at a source).
(iv) holds by assumption. For (v), by [[lem:i-b-5-4]], ςϵ_♭μ⁻¹p_1^𝐏 = −(S + S^(*h)) at R_out, so

    𝒯 = −4ϵ_♭κ̃ Id + 2(S + S^(*h)).

For P, κ̃ = 𝗋 + ½, and 𝒯 > 0 if and only if 2𝗋 + 1 < min spec(S + S^(*h)). For P^(*h) at the decay order −𝗋 − 1,
−ϵ_♭κ̃ = −𝗋 − ½, the same condition. ∎

#### b-regularity at the outgoing radial set {#sec:i-b-5-5}

Write 𝒱 := (V_1, Ω_12, …, Ω_34), V^α for ordered products, α_1 the number of factors V_1, A_k := {|α| = k}, and for
α ∈ A_k with α_1 ≥ 1, α′ := α with one factor V_1 removed. Let

    ‖u‖_(𝐨;k) := Σ_(|α|≤k) ‖(hV)^α u‖_𝐨.                                                                {#eq:i-b-5-9}

Then ‖u‖_((s;k),𝗋,𝖻;+) of [[eq:i-b-1-5]] and h^(−k)‖u‖_(𝐨;k) are equivalent uniformly in h: by
V^α = h^(−|α|)(hV)^α, [[eq:i-b-1-5]] is Σ_(j+|α|≤k) h^(−j−|α|) ‖(hV)^α u‖_𝐨, each term is at most
h^(−k)‖(hV)^α u‖_𝐨, and the terms with j = k − |α| are exactly h^(−k)‖(hV)^α u‖_𝐨. Here the V's replace the ⟨x⟩D_(x_j)
of [[eq:i-b-1-5]]; on X̄, where r > 0, both families span the b-vector fields over C^∞(X̄), so the norms are
equivalent.

**Lemma {#lem:i-b-5-6}** (The semiclassical form of [[lem:i-a-4-8]].) On {ρ < ρ_1}, for Schwartz u and k ≥ 1,
u^(k) := ((hV)^α u)_(α∈A_k) satisfies

    P u_α^(k) + Σ_(β∈A_k) hρ 𝒟_αβ u_β^(k)
        = (hV)^α Pu − α_1 h (hV)^(α′) Pu + Σ_(|β|≤k−1) h^(k−|β|) R_αβ^h (hV)^β u,                          {#eq:i-b-5-10}

with 𝒟_αβ ∈ Ψ^((1,0,0)) semiclassical differential operators whose symbols vanish at R_out, and R_αβ^h ∈ Ψ^((1,−1,0));
all depend polynomially on z.

*Proof.* Multiply [[eq:i-a-4-10]], with σ = z/h and f = P̂(σ)u, by h^(2+k): h^(2+k)V^α = h²(hV)^α, h²P̂(σ) = P, and
h^(2+k)V^(α′) = h · h²(hV)^(α′). It remains to place h²P̃_αβ and h^(2+k)R_αβV^β = h^(k−|β|)h²R_αβ(hV)^β, which needs
the dependence on σ that the proof of [[lem:i-a-4-8]] produces. There P̂(σ) = 2iσρV_1 + ℛ,
ℛ = −2iσρ(3/2 + S) + P̂(0) − iσQ + σ²g_00, and the terms are sorted by origin. From P̂(0) = ρ²P^(0): σ-independent,
in ρ² Diff¹_b ∘ V^β; times h² this is hρ · (hρ Diff¹_b), and hρ Diff¹_b has semiclassical symbol linear in ζ plus
O(ρ). From σρ(3/2 + S) and from the commutators of 2iσρV_1 beyond the diagonal term: σρC^∞ times V^β with
|β| ≤ k − 1 only; times h², hzρC^∞ ∈ Ψ^((0,−1,−1)). From σQ, Q ∈ ρ³ Diff¹_b: [V^α, Q] and QV^(α′) lie in
ρ³ Diff^k_b, whose part with |β| = k has coefficients in ρ³C^∞; so σρ³C^∞ on the diagonal level and σρ³ Diff¹_b below
it; times h², hzρ³C^∞ = hρ · zρ²C^∞ and zρ² · hρ Diff¹_b ⊂ Ψ^((1,−2,0)). From σ²g_00, g_00 ∈ ρ²C^∞: only below the
diagonal level, σ²ρ²C^∞; times h², z²ρ²C^∞. Collecting: h²P̃_αβ = hρ𝒟_αβ with 𝒟_αβ having symbol linear in ζ plus
O(ρ) at the face, so vanishing at R_out; and h²R_αβ ∈ Ψ^((1,−1,0)). ∎

**Proposition {#prop:i-b-5-7}** (Cf. [Hin26c, (9.77)].) In the setting of [[prop:i-b-5-5]], for k ∈ ℕ_0 there are B_*
elliptic at R_out, G and a compact K_E ⊂ Ū_0 ∖ R_out such that for E′ elliptic on K_E, uniformly in z ∈ Z,

    ‖B_* u‖_(𝐨;k) ≤ C(h⁻¹ ‖GPu‖_(𝐨−𝐦+(1,1,0);k) + ‖E′u‖_(𝐨+k(1,1,0)) + h^M ‖Gu‖_(𝐨;k) + ‖u‖_(−M𝟏)).      {#eq:i-b-5-11}

*Proof.* Induction on k; k = 0 is [[eq:i-b-5-8]]. Let k ≥ 1. The system [[eq:i-b-5-10]] is 𝐏^(k)u^(k) = f^(k) with
𝐏^(k) := P ⊗ Id + hρ𝒟 on ℂ^(N_E) ⊗ ℂ^(A_k), inner product h^(⊕A_k). Apply [[lem:i-b-5-1]] to 𝐏 := z⁻¹𝐏^(k) exactly
as in [[prop:i-b-5-5]]. The added term changes nothing that the lemma uses: Re_h(z⁻¹hρ𝒟) ∈ Ψ^((1,−1,−1)) is of lower
order (its commutator with Ǎ², divided by h, lies in Ψ^(2𝐨−𝟏+ϵ′𝟏), Ǎ being scalar), and
h⁻¹ Im_h(z⁻¹hρ𝒟) = Im_h(z⁻¹ρ𝒟) ∈ Ψ^((1,−1,0)) is added to 𝒫̃_1 ⊗ Id, with μ⁻¹ times its symbol vanishing at R_out.
So the threshold matrix is 𝒯 ⊗ Id, the same. This gives [[eq:i-b-5-8]] for u^(k), with G𝐏^(k)u^(k) = Gf^(k). Now
‖G(hV)^α Pu‖_𝐭 + ‖G h(hV)^(α′) Pu‖_𝐭 ≤ C‖G̃Pu‖_(𝐭;k) + C‖u‖_(−M𝟏), 𝐭 := 𝐨 − 𝐦 + (1, 1, 0), with G̃ elliptic on
WF′_h(G); and, G being microsupported at finite frequencies,
‖G h^(k−|β|) R_αβ^h (hV)^β u‖_𝐭 ≤ Ch‖G̃(hV)^β u‖_𝐨 + C‖u‖_(−M𝟏), so h⁻¹ times it is bounded by ‖G̃u‖_(𝐨;k−1), which
the induction hypothesis (applied with G̃ in place of B_*, after shrinking) bounds. The term ‖E′u^(k)‖_𝐨 is at most
C‖E″u‖_(𝐨+k(1,1,0)) + C‖u‖_(−M𝟏), since (hV)^α ∈ Ψ^(k(1,1,0)) ([[prop:i-b-2-8]]). Finally
‖B_*′u‖_(𝐨;k) ≤ C(‖B_* u^(k)‖_𝐨 + ‖G̃u‖_(𝐨;k−1) + ‖u‖_(−M𝟏)) for B_*′ microsupported where B_* is elliptic, since
[B_*′, (hV)^α] is a sum of terms (hV)^γ [B_*′, hV] (hV)^(γ′), |γ| + |γ′| = k − 1, with [B_*′, hV] ∈ Ψ^((0,0,−1)) by
[[thm:i-b-2-4]]. ∎

### The trapped set {#sec:i-b-6}

This section is [Hin26c, Section 9.3.4] on E. Fix z_0 ∈ {1, −1} and Γ = Γ_(z_0) of (H7). Near Γ everything happens at
finite frequencies over a compact set K_Γ ⊂ {r_2 < r < ρ_1⁻¹}, where ⟨x⟩ and ⟨ζ⟩ are bounded above and below and an
admissible 𝖻 is constant ([[sec:i-b-1-4]]). So for operators microsupported there, every norm ‖·‖_𝐨 is h^(−𝖻) times a
norm equivalent to that of L², and we state the estimates of this section in L² (that is, with 𝐨 = 0). χ_Γ ∈ C_c^∞
equals 1 near K_Γ, and ‖u‖_(−M) := ‖χ_Γ u‖_(H_h^(−M)). By [[lem:i-b-6-0]] below we take h_Γ to be the standard inner
product of a trivialisation of E over K_Γ. For h_Γ from the base this is the choice of an h_Γ-orthonormal frame, the
adjoint in another fibre inner product being conjugate to this one by a matrix function ([[prop:i-a-4-2]]); for h_Γ on
phase space it is the replacement of P by P_Q, every estimate being carried back by [[lem:i-b-6-0]] (d). Adjoints are
then ordinary adjoints. A small number ε_Γ > 0 and the compact neighbourhoods Γ(δ), 0 < δ ≤ ε_Γ, of Γ, defined through
φ_u, φ_s and G_(z_0), are fixed in [[sec:i-b-6-1]] and used throughout this section.

#### Inner products on phase space {#sec:i-b-6-0}

**Lemma {#lem:i-b-6-0}** (Cf. [Hin26c, (5.9)] and [Hin17, Proposition 3.12].) Let h_Γ be a smooth fibre inner product on
π*E over a neighbourhood of Γ, given in the trivialisation of E over K_Γ by a positive definite Hermitian matrix
function b(x, ζ). At z = z_0, G := G_(z_0) is real, and h⁻¹ Im P and h⁻¹(Re P − Op_h(G)), taken in the standard inner
product, are of order 0 near Γ; let p_1 and r be their symbols (r is Hermitian up to a scalar that depends on the
quantisation and drops out below). Here p_1 is the p_1(z_0) of [[lem:i-b-1-1]] (b), as h⁻¹ Im P = 𝒫_1(z_0) at
Im z = 0 by [[eq:i-b-1-3]]; [[eq:i-b-6-1]] below writes p^♮ = z_0 p_1. Put

    p_1^(h_Γ) := ½(p_1 + b⁻¹p_1b) + (i/2) b⁻¹[r, b] + ½ b⁻¹H_G b,                                       {#eq:i-b-6-0}

which is h_Γ-self-adjoint (b p_1^(h_Γ) is Hermitian, term by term) and equals p_1 when b = Id. Let ψ_Γ ∈ C_c^∞,
0 ≤ ψ_Γ ≤ 1, equal 1 near Γ, supported in Γ(ε_Γ/3) (the set of [[sec:i-b-6-1]] near which the operator of
[[sec:i-b-6-5]] agrees with P) and in the domain of b; let
b̃ := ψ_Γ b + (1 − ψ_Γ) Id, q := b̃^(1/2) (the positive square root) and Q := Op_h(q). Then for h < h_0:

(a) Q is invertible on L² and on every H_h^𝐨, and Q − I and Q⁻¹ − I lie in Ψ^(−∞), microsupported in supp ψ_Γ up to
O(h^∞) smoothing terms.

(b) P_Q := QPQ⁻¹ = P + hX, where X = X(z) := h⁻¹[Q, P]Q⁻¹ ∈ Ψ^(−∞) is microsupported in supp ψ_Γ and holomorphic in z.

(c) Where ψ_Γ = 1, the symbol of h⁻¹ Im P_Q (standard inner product) at z_0 is q p_1^(h_Γ) q⁻¹; at z ∈ z_0 + i[0, ν′]
the symbols of h⁻¹ Im P_Q and h⁻¹ Im P change by the same scalar and, for P_Q, by O(Im z) more. As conjugation preserves
eigenvalues, [[eq:i-b-1-4]] is the same for P in h_Γ and for P_Q in the standard inner product.

(d) If B_1, E_1, G_1 ∈ Ψ^0 and ‖B_1w‖ ≤ C(h^(−a)‖G_1𝐏_Q w‖ + h^(−c)‖E_1w‖ + h^M‖w‖_(−M)) for all w, where
𝐏_Q ∈ {P_Q, P_Q*}, then the same estimate holds for 𝐏 ∈ {P, P*} and all u, with B_1, E_1, G_1 replaced by B_1Q^♭,
E_1Q^♭, G_1Q^♭, Q^♭ := Q for P and Q^♭ := (Q*)⁻¹ for P*; these have the elliptic sets and microsupports of B_1, E_1,
G_1.

*Proof.* (a) q − Id is smooth with compact support in supp ψ_Γ, so Q − I ∈ Ψ^(−∞); as q is invertible, the symbol
calculus gives Q^− with Q^− − I of the same kind and QQ^− − I =: R, Q^−Q − I in h^∞Ψ^(−∞), so for h small Q is
invertible with Q⁻¹ = Q^−(I + R)⁻¹, which is Q^− up to O(h^∞) smoothing terms.

(b) QPQ⁻¹ − P = [Q − I, P]Q⁻¹, and [Q − I, P] is h times an operator in Ψ^(−∞) microsupported in supp ψ_Γ, since the
principal symbol G_z Id of P commutes with q; P is polynomial in z and Q does not depend on z.

(c) With B := Q*Q, (QPQ⁻¹)* = (Q*)⁻¹P*Q*, so, exactly,

    Im(QPQ⁻¹) = (1/2i)(QPQ⁻¹ − (Q*)⁻¹P*Q*) = Q (Im_B P) Q⁻¹,     Im_B P := (1/2i)(P − B⁻¹P*B).

B has symbol q*q = b̃, equal to b where ψ_Γ = 1. At z_0, P − B⁻¹P*B = B⁻¹[B, Re P] + i(Im P + B⁻¹(Im P)B); as b
commutes with G Id, h⁻¹[B, Re P] has symbol −i{b, G} + [b, r] = iH_G b + [b, r], and dividing by 2ih gives
p_1^(h_Γ) as the symbol of h⁻¹ Im_B P (a scalar part of r drops out of [b, r]). For z ≠ z_0, h⁻¹ Im P changes by
h⁻¹ Op_h(Im G_z), a scalar, and X(z) − X(z_0) = O(Im z) in Ψ^(−∞).

(d) P_Q Q = QP and P_Q*(Q*)⁻¹ = (Q*)⁻¹P*; take w := Q^♭u and use ‖Q^♭u‖_(−M) ≤ C‖u‖_(−M) and the ellipticity of
Q^♭. ∎

So an inner product on phase space costs nothing. Of this section only [[prop:i-b-6-1]] and [[prop:i-b-6-4]] (with
[[lem:i-b-6-3]] behind [[prop:i-b-6-4]]) use the threshold structure; we prove them for P_Q and P_Q* in the standard
inner product and carry them to P and P* by (d). Their proofs use 𝐏 on Γ(ε_Γ/3), where P_Q = P + hX, only through its
principal symbol, which X does not change, and through the symbol of ςh⁻¹ Im 𝐏 in [[eq:i-b-6-2]] and [[eq:i-b-6-5]],
which X changes as in [[prop:i-b-6-1]], to p^♮ + ςσ(Im X), that is, by (c), to z_0 q p_1^(h_Γ) q⁻¹ on Γ at z_0. The
proof of [[prop:i-b-6-4]] also uses, for P_Q, [[prop:i-b-4-5]], [[cor:i-b-4-6]] and the commutator of
[[thm:i-b-2-4]], which hold as hX is a bounded addition to the lower-order part ([[rem:i-b-4-7]]) and
h[X, Φ] ∈ h²Ψ. The O(Im z) dependence of X is O(h) where Im z = O(h), so it enters the h^(1/2)Ψ^0 remainders there, and
for Im z ≤ ν′ it is absorbed by the continuity step of [[prop:i-b-6-1]]. [[sec:i-b-6-5]] and [[sec:i-b-6-6]] use
[[prop:i-b-6-1]] and [[prop:i-b-6-4]] only as microlocal estimates near Γ, for P and for P′, which agree there up to
O(h^∞).

#### Set-up {#sec:i-b-6-1}

Let 𝐏 ∈ {P, P*}, ϵ_♭ := ±1 accordingly, and ς := ϵ_♭z_0. We take Re z = z_0 and 0 ≤ Im z ≤ ν′, ν′ small: for
Im z ≥ ν′, 𝐏 is elliptic near Γ by [[lem:i-b-1-1]] (d), and [[prop:i-b-4-2]] gives every estimate below with h⁻¹
replaced by 1. Write H := H_(G_(z_0)), ℓ := Im z/h ≥ 0, and, on a neighbourhood of Γ,

    p^♮ := z_0 p_1(z_0),     q^♮ := z_0 q_(z_0),     V := ςH.                                              {#eq:i-b-6-1}

q^♮ ≥ 2β_0 on Γ by (H7) and [[lem:i-b-1-1]] (e), p^♮ is the endomorphism p_1^Γ of [[eq:i-b-1-4]] on Γ, and both depend
on Re z = z_0 only ([[lem:i-b-1-1]] (b)). For a real scalar a ∈ C_c^∞ near Γ and A = A* quantising a Id, the operator C
of [[eq:i-b-3-1]] for 𝐏, with A in place of Ǎ², satisfies, by [[eq:i-b-4-3]],

    σ(ςC) = ςH_(Re G_z) a + 2a(p^♮ − ℓq^♮),     ςH_(Re G_z) a = Va + O((Im z)²)                           {#eq:i-b-6-2}

([[lem:i-b-4-1]]: H_(Re G_z) − H = −(Im z)² H_(g_00)). V is the field along which estimates for 𝐏 propagate
([[prop:i-b-4-5]]): the future field z_0H for P, the past field for P*. Accordingly put
(φ_u^♮, φ_s^♮, ν_u^♮, ν_s^♮) := (φ_u, φ_s, ν_u, ν_s) if ϵ_♭ = 1 and (φ_s, φ_u, ν_s, ν_u) if ϵ_♭ = −1, and
Γ_(u/s)^♮ := {φ_(u/s)^♮ = 0} ∩ Σ_(z_0) ∩ O. Then by (Γ.2), on Σ_(z_0) ∩ O,

    Vφ_u^♮ = −ν_u^♮ φ_u^♮,     Vφ_s^♮ = ν_s^♮ φ_s^♮,     {φ_u^♮, φ_s^♮} ≠ 0 on Γ,                          {#eq:i-b-6-3}

with min(inf_Γ ν_u^♮, inf_Γ ν_s^♮) = ν_min. Extend φ_(u/s) and ν_(u/s) smoothly to O. As dG_(z_0) ≠ 0 near Γ (Γ.3),
the differences in [[eq:i-b-6-3]] are smooth multiples of G_(z_0) off Σ_(z_0): Vφ_u^♮ = −ν_u^♮φ_u^♮ + j_u^♮G_(z_0),
Vφ_s^♮ = ν_s^♮φ_s^♮ + j_s^♮G_(z_0) on O. For δ ≤ ε_Γ let

    Γ(δ) := {|φ_u| ≤ δ, |φ_s| ≤ δ, |G_(z_0)| ≤ δ} ∩ Ō′,

O′ ⋐ O a neighbourhood of Γ. We take O so small that it does not meet Σ_(z_0) ∖ Σ^♭_(z_0), a closed set disjoint from
Γ (q_(z_0) ≠ 0 on Σ_(z_0), [[lem:i-b-1-1]] (e)); then by (Γ.1), Γ is the common zero set of φ_u, φ_s and G_(z_0) in O.
So Γ = ⋂_δ Γ(δ), and the Γ(δ) are compact neighbourhoods of Γ shrinking to it. Fix χ_(O′) ∈ C_c^∞(O),
0 ≤ χ_(O′) ≤ 1, equal to 1 on Ō′. The set supp χ_(O′) ∖ O′ is compact and disjoint from Γ, so
max(|φ_u|, |φ_s|, |G_(z_0)|) ≥ δ_O on it, for some δ_O > 0. We take ε_Γ < δ_O, and so small that Γ(ε_Γ) ⊂ O′ and that
[[eq:i-b-6-3]] and (Γ.3) hold on Γ(ε_Γ), with

    c_Γ ≤ |{φ_u^♮, φ_s^♮}| ≤ C_Γ  on Γ(ε_Γ),     C_Γ := max_(Γ(ε_Γ)) |{φ_u, φ_s}|,

for a constant c_Γ > 0. C_Γ is finite because Γ(ε_Γ) is compact, and {φ_u^♮, φ_s^♮} = ϵ_♭{φ_u, φ_s} has the constant
sign ϵ_♭ on Γ(ε_Γ).

*Cut-offs.* For δ ≤ ε_Γ, the set {max(|φ_u|, |φ_s|, |G_(z_0)|) ≤ δ} ∩ supp χ_(O′) is compact and lies in O′, where
χ_(O′) = 1; so it is Γ(δ). Hence, if f ∈ C^∞(ℝ³) has support in [−δ, δ]³, then χ_(O′) f(φ_u^♮, φ_s^♮, G_(z_0)),
extended by 0, is smooth on 𝒫, supported in Γ(δ), and equal to f(φ_u^♮, φ_s^♮, G_(z_0)) on the open set O′, which
contains its support; so no derivative falls on χ_(O′). The cut-offs of [[prop:i-b-6-1]] and [[prop:i-b-6-4]] are of
this form.

*Dynamics in Γ(ε_Γ).* Let γ be an integral curve of V in Σ_(z_0) ∩ Γ(ε_Γ). Along it
φ_u^♮(γ(t)) = φ_u^♮(γ(0)) exp(−∫_0^t ν_u^♮) and φ_s^♮(γ(t)) = φ_s^♮(γ(0)) exp ∫_0^t ν_s^♮, with
ν_(u/s)^♮ ≥ ½ν_min on Γ(ε_Γ) after shrinking ε_Γ. So:

- (D1) if γ(0) ∉ Γ_u^♮, then γ leaves Γ(ε_Γ) in finite backward time;
- (D2) if γ(0) ∈ Γ_u^♮, then as long as it stays in Γ(ε_Γ) backward in time it stays in Γ_u^♮, |φ_s^♮| decreases
  exponentially, and γ(t) → Γ as t → −∞ (the ω-limit points lie in Γ_u^♮ ∩ Γ_s^♮ = Γ);
- (D3) if γ(0) ∈ Γ_u^♮ ∖ Γ, then γ leaves Γ(ε_Γ) in finite forward time.

Combined with (H8) (a)–(b): a point of Σ_(z_0) near Γ not on Γ_u^♮ is not on the corresponding global set, so its
backward V-curve leaves Γ(ε_Γ) and tends to the radial sets.

#### The lossless estimate {#sec:i-b-6-2}

**Proposition {#prop:i-b-6-1}** (Cf. [Hin26c, (9.83)].) Let 𝐏′ := 𝐏 + h𝐗 with 𝐗 = 𝐗(z) ∈ Ψ^0 microsupported near Γ
and continuous in z (as the X of [[lem:i-b-6-0]]), and let p′^♮ := p^♮ + ςσ(Im 𝐗(z_0)) (so that ςh⁻¹ Im 𝐏′ has symbol
p′^♮ − ℓq^♮ up to O(Im z)). Let γ ∈ ℝ with sup_(ϖ∈Γ) max spec(p′^♮(ϖ) − γq^♮(ϖ)) < 0. There are ν′ > 0 and, for every
neighbourhood U of Γ, operators B, E, G ∈ Ψ^0 microsupported in U, B elliptic at Γ, WF′_h(E) ∩ Γ_u^♮ = ∅, such that
for z ∈ z_0 + i[hγ, ν′] with Im z ≥ −ν′, h < h_0 and all M,

    ‖Bu‖ ≤ C(h⁻¹‖G𝐏′u‖ + ‖Eu‖ + h^M‖u‖_(−M)).                                                         {#eq:i-b-6-4}

For 𝐗 = 0 the condition is γ > γ_+, with γ_+ of [[eq:i-b-1-4]].

*Proof.* With χ_0 as in the proof of [[lem:i-b-5-1]], let ψ_u := χ_0(M_1(φ_u^♮)²), ψ_s := χ_0(M_1(φ_s^♮)²),
ψ_Σ := χ_0(M_Σ G_(z_0)²) and ǎ := χ_(O′)ψ_uψ_sψ_Σ, with M_Σ ≥ M_1 ≥ M_0 large (M_0 ≥ 2ε_Γ^(−2)); by the cut-offs
paragraph of [[sec:i-b-6-1]], supp ǎ ⊂ Γ(√(2/M_1)) (for M_Σ ≥ M_1), and χ_(O′) = 1 near supp ǎ. Compute
[[eq:i-b-6-2]] with a = ǎ². First, with χ_0χ_0′ ≤ 0,

    Vψ_u² = 4M_1 χ_0χ_0′(M_1(φ_u^♮)²) φ_u^♮ (−ν_u^♮φ_u^♮ + j_u^♮G_(z_0)),
    Vψ_s² = 4M_1 χ_0χ_0′(M_1(φ_s^♮)²) φ_s^♮ (ν_s^♮φ_s^♮ + j_s^♮G_(z_0)).

On supp χ_0′(M_1(φ_u^♮)²) ∩ supp ψ_Σ we have (φ_u^♮)² ≥ M_1⁻¹ and G_(z_0)² ≤ 2M_Σ⁻¹, so
|j_u^♮G_(z_0)| ≤ ¼ν_min|φ_u^♮| once M_Σ ≥ CM_1; then Vψ_u² = e_u² ≥ 0 with
e_u := 2M_1^(1/2) χ_u |φ_u^♮| (ν_u^♮ − j_u^♮G_(z_0)/φ_u^♮)^(1/2), χ_u := √(−χ_0χ_0′)(M_1(φ_u^♮)²), smooth, and
likewise Vψ_s² = −f_s². The O((Im z)²) term of [[eq:i-b-6-2]] changes these by at most
C(Im z)²M_1|φ| · |χ_0χ_0′|, which keeps the signs and smoothness for Im z ≤ ν′, ν′ small depending on M_1. The
derivative of ψ_Σ is supported where G_(z_0)² ≥ M_Σ⁻¹, where G_z is elliptic for ν′ small; it gives a term J𝐏′ as in
[[lem:i-b-5-1]]. Next, on supp ǎ,

    p′_z^♮ − ℓq^♮ = (p′_z^♮ − γq^♮) − (ℓ − γ)q^♮,

where p′_z^♮ := p′^♮ + ςσ(Im 𝐗(z) − Im 𝐗(z_0)) is the symbol at z. p′^♮ − γq^♮ ≤ −c Id there for M_1 large, by the
hypothesis and continuity, and p′_z^♮ − γq^♮ ≤ −(c/2) Id for Im z ≤ ν′, ν′ small depending on M_1; the symbol b below is
built from the symbol at z. So, with b := ǎ(−2(p′_z^♮ − γq^♮))^(1/2) (the positive square root of a positive definite
smooth matrix function, smooth),

    ςC = −B*B − F_s*F_s + E_u*E_u + J𝐏′ − 2(ℓ − γ)Ǎ ςϵ_♭𝒬 Ǎ + R,     R ∈ h^(1/2)Ψ^0,

where ςϵ_♭𝒬 = z_0𝒬 has principal symbol q^♮ ≥ β_0 on supp ǎ; since 0 ≤ ℓ − γ ≤ 3h⁻¹, the paragraph on positivity
of absorbing terms in [[sec:i-b-3-3]] makes 2(ℓ − γ)Ǎz_0𝒬Ǎ a term F of [[lem:i-b-3-3]], with the double commutator in
R. [[lem:i-b-3-3]] and [[lem:i-b-3-4]], with Λ := Γ and the sets Γ(√(2/M_1)) for an increasing sequence of M_1 in
[M_0, 2M_0] (and M_Σ := CM_1), give [[eq:i-b-6-4]] with E elliptic on the union of the sets supp e_u, which lie in
{(φ_u^♮)² ≥ M_0⁻¹ · ½} (as M_1 ≤ 2M_0) and so avoid Γ_u^♮. Here ν′ was chosen depending on M_1, hence on U; for
ν′(U) ≤ Im z ≤ ν′, ν′ the constant of [[sec:i-b-6-1]], 𝐏′ is elliptic near Γ ([[lem:i-b-1-1]] (d)) and
[[prop:i-b-4-2]] gives [[eq:i-b-6-4]] with the same operators, so the ν′ of the statement does not depend on U. ∎

#### Defect measures with values in matrices {#sec:i-b-6-3}

In this section and the next, h_j → 0 is a sequence, the u_j are ℂ^(N_E)-valued, and we drop j. U is an open
precompact set at finite frequencies over the interior of K_Γ. The family is *tempered on U* if
‖u‖_(−M_t) ≤ C h^(−M_t) for some M_t and sup ‖Gu‖ < ∞ for some G ∈ Ψ^0 elliptic on Ū.

**Lemma {#lem:i-b-6-2}** (Cf. [Hin26c, Lemma 9.30], on E.) If (u_j) is tempered on U, a subsequence has a *defect
measure* on U: a positive semidefinite End(ℂ^(N_E))-valued Radon measure μ on U, such that
⟨Bu, u⟩ → ∫_U tr(b dμ) for every B ∈ Ψ^0 with WF′_h(B) a compact subset of U and principal symbol
b ∈ C_c^∞(U; End ℂ^(N_E)). Write ν := tr μ ≥ 0; then μ has a density dμ/dν with respect to ν, with dμ/dν ≥ 0 and
tr(dμ/dν) = 1 ν-almost everywhere, and for every Hermitian continuous p, tr(p dμ) ≤ max spec(p) dν.

*Proof.* (a) For B as stated, limsup |⟨Bu, u⟩| ≤ C_b := sup|b| · sup_Ū |g|^(−2) · sup ‖Gu‖², where the G of the
definition is taken scalar with principal symbol g, |g| ≥ c > 0 on Ū. As in [Hin26c, (9.87)–(9.88)], B = G*QG + R with
Q ∈ Ψ^0 of principal symbol q := b|g|^(−2) ∈ C_c^∞(U) (the construction of [[prop:i-b-2-10]]), so that R ∈ hΨ^0 is
microsupported in Ell_h(G) up to a term in h^∞Ψ^(−∞); then R = G*R′G + R″ with R′ ∈ hΨ^0 and R″ residual. By
[[thm:i-b-2-7]], |⟨QGu, Gu⟩| ≤ (sup|q| + ϵ + Ch^(1/4))‖Gu‖² for every ϵ > 0, and
|⟨Ru, u⟩| ≤ Ch sup‖Gu‖² + C_M h^M ‖u‖²_(−M_t) = o(1) by temperedness.

(b) The value depends only on b: two such B with the same b differ by hΨ^0 plus residual terms, whose pairings tend to
0 by (a).

(c) A diagonal argument over a countable dense subset of C_c^∞(U; End ℂ^(N_E)) (dense in C_c in the supremum norm on
each compact set) gives a subsequence along which L(b) := lim ⟨Op_h(b)u, u⟩ exists for all b in that set, and by (a) L
extends to a linear functional on C_c(U; End ℂ^(N_E)), continuous for the supremum norm on each compact set. By the
Riesz representation theorem applied to each matrix entry, L(b) = ∫ tr(b dμ) for a matrix of complex Radon measures.

(d) Positivity: let b ≥ 0 with supp b ⊂ K_b ⋐ U, and j ∈ C_c^∞(U) scalar, 0 ≤ j ≤ 1, equal to 1 on K_b. For ϵ > 0,
b + ϵj² Id is positive definite on K_b and equal to ϵj² Id off K_b, so it is q_ϵ*q_ϵ with q_ϵ ∈ C_c^∞(U) (on K_b the
positive square root; off K_b, √ϵ j, which is smooth as j ≥ 0); then
Op_h(b) + ϵ Op_h(j)* Op_h(j) = Op_h(q_ϵ)* Op_h(q_ϵ) + hR′, so liminf ⟨Op_h(b)u, u⟩ ≥ −ϵ limsup ‖Op_h(j)u‖² ≥ −Cϵ. Hence L(b) ≥ 0 for b ≥ 0; taking b = φvv* with φ ≥ 0 scalar and
v ∈ ℂ^(N_E) shows v*μv ≥ 0, so μ is Hermitian and positive semidefinite. Each entry is then absolutely continuous with
respect to ν (|μ_ab| ≤ ν for a positive matrix measure), which gives dμ/dν; and
tr(p dμ/dν) ≤ max spec(p) tr(dμ/dν) as dμ/dν ≥ 0. ∎

**Lemma {#lem:i-b-6-3}** (Cf. [Hin26c, Lemmas 9.31–9.32], on E.) Let (u_j) be tempered on U with defect measure μ, and
𝐏_j := 𝐏_(h_j,z_j) with Im z_j/h_j → η ∈ [0, ∞).

(a) If ‖G𝐏_ju_j‖ = o(1) with G elliptic on Ū, then supp μ ⊂ Σ_(z_0).

(b) For real scalar a ∈ C_c^∞(U), and Y ∈ Ψ^0 microsupported in U with WF′_h(I − Y) ∩ supp a = ∅,

    |∫_U (Va dν + 2a tr((p^♮ − ηq^♮) dμ))| ≤ 4 sup|a| limsup h⁻¹‖Y𝐏u‖ ‖Yu‖.                           {#eq:i-b-6-5}

(c) The same holds with 𝐏 replaced by a self-adjoint Φ ∈ Ψ^0 with real scalar principal symbol φ, with Va replaced by
H_φ a and with p^♮ − ηq^♮ replaced by 0.

*Proof.* (a) For b ∈ C_c^∞(U) with supp b ∩ Σ_(z_0) = ∅, 𝐏_j is elliptic on supp b for j large, so
Op_h(b) = Q𝐏_j + R with Q bounded and R ∈ h^∞Ψ^(−∞) near supp b, and ∫ |b|² dν = lim ‖Op_h(b)u‖² = 0.

(b) With A = A* quantising a Id and WF′_h(A) ⊂ supp a, [[eq:i-b-3-1]] gives (2/h) Im⟨𝐏u, Au⟩ = ⟨Cu, u⟩, and by
[[eq:i-b-6-2]] the principal symbol of ςC is Va + 2a(p^♮ − ℓ_jq^♮) + O((Im z_j)²), which converges in C_c^∞ to
Va + 2a(p^♮ − ηq^♮); as ⟨Op_h(c_j − c)u, u⟩ → 0 when c_j → c uniformly ([[lem:i-b-6-2]] (a)),
⟨ςCu, u⟩ → ∫ tr((Va + 2a(p^♮ − ηq^♮)) dμ), and tr(Va dμ) = Va dν for scalar a. The left side is bounded by
(2/h)(‖Y𝐏u‖ + O(h^∞))(‖AYu‖ + O(h^∞)) and ‖AYu‖ ≤ (sup|a| + ϵ + Ch^(1/4))‖Yu‖ by [[thm:i-b-2-7]], with ϵ ≤ sup|a|.

(c) is the same argument with Im Φ = 0. ∎

#### The estimate with loss one {#sec:i-b-6-4}

**Proposition {#prop:i-b-6-4}** (Cf. [Hin26c, Theorem 9.28] with loss one.) Let β > γ_− and U a neighbourhood of Γ.
There are B, E, G ∈ Ψ^0 microsupported in U, B elliptic at Γ, WF′_h(E) ∩ Γ_u^♮ = ∅, with: every backward V-curve from a
point of WF′_h(B) ∖ Γ_u^♮ reaches Ell_h(E) in finite time within Ell_h(G); Γ ∪ WF′_h(B) ⊂ Ell_h(G); and for
z ∈ z_0 + i[hβ, ν′], h < h_0,

    ‖Bu‖ ≤ C(h⁻²‖G𝐏u‖ + h⁻¹‖Eu‖ + h^M‖u‖_(−M)).                                                       {#eq:i-b-6-6}

*Proof.* Fix γ > γ_+. For Im z ≥ hγ, [[eq:i-b-6-6]] follows from [[eq:i-b-6-4]]. Choose B, E, G for the dynamics as
stated, with WF′_h(B) ⊂ Γ(ε_Γ)° ⊂ Ell_h(G); this is possible by (D1)–(D2). Suppose [[eq:i-b-6-6]] fails for every C in
the range hβ ≤ Im z ≤ hγ. Then there are h_j → 0, z_j and u_j with

    ‖Bu‖ = 1,     ‖G𝐏u‖ = o(h²),     ‖Eu‖ = o(h),     h^M‖u‖_(−M) = o(1),                                {#eq:i-b-6-7}

and after passing to a subsequence Im z_j/h_j → η ∈ [β, γ] and (u_j) has a defect measure μ on U_1, an open
neighbourhood of Γ with Ū_1 ⊂ Ell_h(B) (B itself shows that (u_j) is tempered on U_1, and h^M‖u‖_(−M) = o(1) gives the
bound on ‖u‖_(−M)). We use [[prop:i-b-4-5]] and [[cor:i-b-4-6]] (real principal type) for the 𝐏_j, with
constants uniform in j; for Im z_j < 0 they hold near Γ because ℓ_j is bounded, so ℓ_j𝒬 is a bounded term of the class
of 𝒫_1 over the compact set K_Γ, and the absorbing sign is not needed ([[rem:i-b-4-7]]).

*Localisation.* For ϖ ∈ U_1 ∖ Γ_u^♮, the backward V-curve from ϖ reaches Ell_h(E) within Ell_h(G), so
[[cor:i-b-4-6]] gives ‖B′u‖ ≤ C(h⁻¹‖G𝐏u‖ + ‖Eu‖ + h^M‖u‖_(−M)) = o(1) for B′ elliptic at ϖ; so ϖ ∉ supp μ. With
[[lem:i-b-6-3]] (a), supp μ ⊂ Γ_u^♮ ∩ Σ_(z_0). By (D2), backward curves from Γ_u^♮ ∩ WF′_h(B) reach any neighbourhood
of Γ; so with E′ elliptic on Γ, ‖Bu‖ ≤ C(h⁻¹‖G𝐏u‖ + ‖Eu‖ + ‖E′u‖ + h^M‖u‖_(−M)), and it suffices to find such E′
with ‖E′u‖ → 0. Taking WF′_h(E′) ⊂ Γ(δ), ‖E′u‖² → ∫ |e′|² dν, and it suffices to show 𝗆(δ) = 0 for some δ > 0, where

    𝗆(x) := ν(Γ_u^♮ ∩ Γ(ε_Γ) ∩ {|φ_s^♮| < x}).

*Step 1: an auxiliary equation.* Let Φ, N_u, J_u ∈ Ψ^0 be self-adjoint quantisations of φ_u^♮ Id, ν_u^♮ Id,
j_u^♮ Id, cut off to U_1 and equal to the uncut quantisations modulo h^∞ near Γ(ε_Γ). By [[thm:i-b-2-4]] and
[[eq:i-b-6-2]] (the symbols being scalar, the commutator of the matrix-valued lower order part of 𝐏 with Φ is in h²Ψ),
ς(i/h)[𝐏, Φ] = −N_uΦ + J_u𝐏 + hR + R_away, with R ∈ Ψ^0 and R_away microsupported off Γ(ε_Γ), as Im z = O(h). Hence
f := 𝐏u gives

    (𝐏 − iςhN_u)Φu = (Φ − iςhJ_u)f − iςh²Ru + R′_away u.                                               {#eq:i-b-6-8}

The operator 𝐏′ := 𝐏 − iςhN_u is of the form of [[prop:i-b-6-1]] with p′^♮ = p^♮ − ν_u^♮, and
sup_Γ max spec(p^♮ − βq^♮ − ν_u^♮) ≤ sup_Γ max spec(p_1^Γ − βq^♮) − ν_min < 0, because β > γ_− means
sup_Γ max spec(p_1^Γ − βq^♮) < ½ν_min. So [[prop:i-b-6-1]] applies to 𝐏′ with γ := β, on a small neighbourhood of Γ,
with operators B_1, E_1, G_1. Its right side for Φu: h⁻¹‖G_1(…)‖ = O(h) by [[eq:i-b-6-7]] and sup‖G_1u‖ < ∞;
‖E_1Φu‖ ≤ C‖E_1′u‖ + O(h^∞) with E_1′ microsupported off Γ_u^♮ near WF′_h(E_1), and ‖E_1′u‖ = o(h) by
[[cor:i-b-4-6]] as in the localisation; the last term is O(h^∞). So ‖B_1Φu‖ = O(h).

*Step 2.* Fix δ_1 ∈ (0, ε_Γ) with Γ(δ_1) ⊂ U_1 ∩ Ell_h(B_1), possible as U_1 and Ell_h(B_1) are neighbourhoods of Γ.
In Steps 2–4, and in the definition of 𝗆, ε_Γ is replaced by δ_1, so that every function a below is supported in
U_1 ∩ Ell_h(B_1), where μ lives and [[lem:i-b-6-3]] (c) applies. [[lem:i-b-6-3]] (c) with Φ and Y a cut-off elliptic
where B_1 is gives, for real a ∈ C_c^∞(U_1 ∩ Ell_h(B_1)), |∫ H_(φ_u^♮) a dν| ≤ C_1 sup|a|, C_1 independent of a. Take
a := χ_(O′) a_0(φ_u^♮) a_1(φ_s^♮) ψ(G_(z_0)) with a_0, ψ ∈ C_c^∞((−δ_1, δ_1)) equal to 1 near 0, 0 ≤ a_0, ψ ≤ 1 (so
that a ≥ 0 in Step 3), and a_1(t) := Θ(t/δ)χ_c(t), where Θ is smooth, non-decreasing, Θ(s) = ∓1 for ±s ≤ −2,
Θ′ ≥ ½ on [−1, 1], and χ_c ∈ C_c^∞((−δ_1, δ_1)), 0 ≤ χ_c ≤ 1, equals 1 on [−δ_1/2, δ_1/2] with |χ_c′| ≤ 4/δ_1. Then
|a| ≤ 1, and by the cut-offs paragraph of [[sec:i-b-6-1]] a is supported in Γ(δ_1), with χ_(O′) = 1 near its support.
On supp ν ⊂ Γ_u^♮ ∩ Σ_(z_0), H_(φ_u^♮) a = a_1′(φ_s^♮){φ_u^♮, φ_s^♮} on O′ and H_(φ_u^♮) a = 0 off O′ (the other
terms contain H_(φ_u)φ_u = 0, or ψ′(G_(z_0)), which vanishes near Σ_(z_0)). Replace a_1 by ϵ_♭a_1, ϵ_♭ being the sign
of {φ_u^♮, φ_s^♮} on Γ(ε_Γ); the integrand is then a_1′(φ_s^♮)|{φ_u^♮, φ_s^♮}| on O′. For δ < δ_1/4, Θ′(t/δ) = 0 for
|t| ≥ 2δ and χ_c = 1 on [−δ_1/2, δ_1/2], so a_1′ ≥ 1/(2δ) on [−δ, δ], a_1′ ≥ 0 on [−δ_1/2, δ_1/2], and
|a_1′| = |Θ(t/δ)χ_c′(t)| ≤ 4/δ_1 for δ_1/2 < |t| < δ_1. With c_Γ ≤ |{φ_u^♮, φ_s^♮}| ≤ C_Γ on Γ(δ_1) ⊂ Γ(ε_Γ), the
integral over {|φ_s^♮| < δ} is at least (c_Γ/(2δ))𝗆(δ), that over {δ ≤ |φ_s^♮| ≤ δ_1/2} is non-negative, and that
over {δ_1/2 < |φ_s^♮| < δ_1} is at least −(4C_Γ/δ_1)ν(Γ(δ_1)). So

    (c_Γ/(2δ)) 𝗆(δ) ≤ C_1 + (4C_Γ/δ_1) ν(Γ(δ_1)),     so     𝗆(δ) ≤ C_2 δ                               {#eq:i-b-6-9}

with C_2 := (2/c_Γ)(C_1 + 4C_Γν(Γ(δ_1))/δ_1), independent of δ ∈ (0, δ_1/4); ν(Γ(δ_1)) is finite as Γ(δ_1) is a
compact subset of U_1.

*Step 3: propagation for logarithmic times.* [[lem:i-b-6-3]] (b), with ‖G𝐏u‖ = o(h²), gives
∫(Va dν + 2a tr((p^♮ − ηq^♮) dμ)) = 0 for real a ∈ C_c^∞(U_1). Let p_η := max spec(p^♮ − ηq^♮), continuous;
for a ≥ 0 [[lem:i-b-6-2]] gives ∫(Va + 2ap_η) dν ≥ 0. Since η ≥ β and q^♮ > 0, p_η ≤ max spec(p^♮ − βq^♮), and
β > γ_− gives sup_Γ p_η < ½ν_min; so we can fix κ′ with sup_(Γ(δ_1)) p_η^+/ν_s^♮ < κ′ < ½ (shrinking δ_1;
p_η^+ := max(p_η, 0)). Take a := χ_(O′) a_0(φ_u^♮) a_1(φ_s^♮) ψ(G_(z_0)) with a_0, ψ as before and
a_1(t) := |t|^(−2κ′) f(|t|), f ∈ C_c^∞((δ/2, δ_1)), f ≥ 0, f = 1 on [δ, δ_1/2], f′ ≤ 0 on [δ, ∞), |xf′(x)| ≤ 4 on
[δ/2, δ]. On supp ν, by [[eq:i-b-6-3]], V|φ_s^♮|^(−2κ′) = −2κ′ν_s^♮|φ_s^♮|^(−2κ′), so

    Va + 2ap_η = ν_s^♮ |φ_s^♮|^(−2κ′) (−2(κ′ − p_η/ν_s^♮) f + |φ_s^♮| f′(|φ_s^♮|)).

This is ≤ 0 where |φ_s^♮| ≥ δ, ≤ −c_3 on {δ ≤ |φ_s^♮| ≤ δ_1/2} with c_3 > 0 independent of δ, and bounded by
Cδ^(−2κ′) on {δ/2 ≤ |φ_s^♮| ≤ δ}. Hence c_3(𝗆(δ_1/2) − 𝗆(δ)) ≤ Cδ^(−2κ′) 𝗆(δ).

*Step 4.* With [[eq:i-b-6-9]], 𝗆(δ_1/2) ≤ (1 + Cδ^(−2κ′))C_2δ → 0 as δ → 0, since 2κ′ < 1. So 𝗆(δ_1/2) = 0,
contradicting ‖Bu‖ = 1 as explained. ∎

[Hin26c] writes the range in this proof as −β ≤ h⁻¹ Im z and p_z ≤ p_1 + 2ββ_0, while its theorem is stated for
Im(h⁻¹z) ≥ β. With the range η ≥ β the bound used is p_η ≤ max spec(p^♮ − βq^♮), and Steps 1 and 3 need exactly
sup_Γ max spec(p_1^Γ − βq^♮) < ½ν_min, which is the definition of β > γ_− in [[eq:i-b-1-4]]. When β < 0 this
involves the largest value of q^♮ on Γ, not the smallest, which is why [[eq:i-b-1-4]] defines γ_± as these thresholds
and not through β_0 alone ([[rem:i-b-relation]]). The steps and the use of {φ_u, φ_s} follow [Hin26c], which follows
[Dya16]; the matrix-valued measure enters only through tr and max spec ([[lem:i-b-6-2]]).

#### Complex absorption {#sec:i-b-6-5}

To interpolate between [[prop:i-b-6-1]] and [[prop:i-b-6-4]] we need an invertible problem depending holomorphically
on σ, equal to 𝐏 near Γ. As in [Hin26c] the absorbing operator is built by averaging a symbol in the time frequency,
which makes it entire in σ; here it is also written as W*W, so that its sign is exact. We write the construction for
z_0 = 1; for z_0 = −1, q̃_1 below is defined with −τ in place of τ, and the factor z_0 in [[eq:i-b-6-10]] makes the
absorbing sign the right one.

Let χ_Υ ∈ C_c^∞((−1, 1)) equal 1 on [−½, ½] and Υ(σ) := (2π)⁻¹ ∫ e^(−iσs) χ_Υ(s) ds: Υ is entire,
∫_ℝ Υ(τ + iη) dτ = χ_Υ(0) = 1 for every η (shift of contour), and |∂^k Υ(τ + iη)| ≤ C_(k,M) ⟨τ⟩^(−M) e^(|η|)
(Paley–Wiener). Let q̃_0 ∈ C^∞(T*X̃°), 0 ≤ q̃_0 ≤ 1, with q̃_0 = 0 on Γ(ε_Γ/2) and q̃_0 = 1 off Γ(¾ε_Γ). Put

    a(x; τ, ζ) := (1 − χ_Υ(|(τ, ζ)|)) |(τ, ζ)| q̃_1(x; τ, ζ),
    q̃_1 := q̃_0(x, ζ/τ) if τ > 0 and (x, ζ/τ) ∈ Γ(ε_Γ),     q̃_1 := 1 otherwise.

q̃_1 is smooth and homogeneous of degree 0 on (τ, ζ) ≠ 0, because q̃_0 = 1 near the boundary of Γ(ε_Γ) and |ζ/τ| is
large near τ = 0, ζ ≠ 0; so a is a symbol of order 1 in (τ, ζ), homogeneous of degree 1 for |(τ, ζ)| ≥ 1. Let
a_♭(x; σ, ζ) := ∫ Υ(σ − τ) a(x; τ, ζ) dτ, entire in σ; for |Im σ| ≤ C, a_♭ − a(·; Re σ, ·) is a symbol of order 0 in
(Re σ, ζ), uniformly, by Taylor's formula in τ and ∫ Υ = 1. Let χ ∈ C_c^∞(ℝ⁴), 0 ≤ χ ≤ 1, equal 1 near the base
projection of Γ(ε_Γ), and χ_1 ∈ C_c^∞ equal 1 on supp χ, both supported in the interior of K_Γ. With Op the standard
quantisation in x (dual variable ζ, σ a parameter), acting componentwise,

    Q̂_♭(σ) := χ_1 Op(a_♭(·; σ, ·)) χ_1,     Q̂(σ) := Q̂_♭(σ̄)* Q̂_♭(σ),
    P̂′(σ) := χP̂(σ)χ − iz_0(χQ̂(σ)χ + (1 − χ²)(σ² + Δ)),     P′_(h,z) := h² P̂′(z/h),                   {#eq:i-b-6-10}

on ℝ⁴, Δ ≥ 0 the Euclidean Laplacian. All three terms are entire in σ (σ ↦ Q̂_♭(σ̄)* is holomorphic, being
antiholomorphic composed with the antilinear adjoint).

**Lemma {#lem:i-b-6-5}** Let Re z = z_0 and Im z = hη, |η| ≤ C.

(a) W := hQ̂_♭(z/h) ∈ Ψ^((1,0,0)) has principal symbol w := χ_1² |(1, ζ)| q̃_0, and h²Q̂(z/h) = W*W + hR_W with
R_W ∈ Ψ^((1,0,0)).

(b) WF′_h(W) ∩ Γ(ε_Γ/3) = ∅; so P′_(h,z) − P_(h,z) is microlocally O(h^∞) near Γ(ε_Γ/3).

(c) P′_(h,z) is semiclassically elliptic, in the scattering sense on all of 𝒫, outside Γ(¾ε_Γ).

(d) Over {χ = 1}, h⁻¹ Im P′_(h,z) = h⁻¹ Im P_(h,z) − z_0h⁻¹W*W − z_0 Re R_W and
Re P′_(h,z) − Re P_(h,z) = z_0h Im R_W.

*Proof.* (a) For a symbol b of order l in (σ, ζ), h^l b(x; z/h, ζ/h) is a semiclassical symbol of order (l, 0, 0): its
ζ-derivatives of order k are h^(l−k)(∂^k b) at (z/h, ζ/h), bounded by C(|z|² + |ζ|²)^((l−k)/2). Hence
h(a_♭ − a)(x; z/h, ζ/h) ∈ hS^0, and h a(x; 1/h, ζ/h) = |(1, ζ)| q̃_1(x; 1, ζ) = |(1, ζ)| q̃_0(x, ζ) for h ≤ 1
(homogeneity), with q̃_0 := 1 off Γ(ε_Γ); and Op(b(x; σ, ζ)) = Op_h(b(x; σ, ζ/h)). hQ̂_♭(z̄/h) − W ∈ hΨ^0 since
a_♭(σ̄) − a_♭(σ) is of order 0; so h²Q̂ = W*W + hR_W with R_W := (h⁻¹(hQ̂_♭(z̄/h) − W))* W.

(b) If (x, ζ) ∈ Γ(ε_Γ/3) and |hτ − 1| ≤ ϵ, then (x, ζ/(hτ)) ∈ Γ(ε_Γ/2) for ϵ small (uniform continuity of φ_u, φ_s,
G_(z_0) on a compact set), so a(x; τ, ζ/h) = 0; the rest of the integral defining a_♭(x; 1/h + iη, ζ/h) is over
|τ − 1/h| ≥ ϵ/h, where |Υ| ≤ C_M(h/ϵ)^M, and likewise for all derivatives. So the symbol of W is O(h^∞) in S^((1,0,0))
near Γ(ε_Γ/3), and so is R_W (which ends in W). Near the base projection of Γ(ε_Γ), χ = 1 and 1 − χ² = 0.

(c) The principal symbol of P′_(h,z) is χ²G_(z_0) − iz_0(1 + |ζ|²)(χ²q̃_0² + 1 − χ²), as χ_1 = 1 on supp χ and
z² = 1 + O(h). Its imaginary part vanishes only where χ = 1 and q̃_0 = 0, which is inside Γ(¾ε_Γ); at fibre infinity
q̃_0 = 1, and over ∂X, χ = 0 and the symbol is −iz_0(z² + |ζ|²).

(d) W*W is self-adjoint, and Im(−iX) = −Re X, Re(−iX) = Im X. ∎

By (d), in the region 0 < q̃_0 < 1, 𝐏′ ∈ {P′, P′*} has the structure of [[prop:i-b-4-5]] with the additional term
−ϵ_♭z_0h⁻¹W*W in h⁻¹ Im 𝐏′ and a bounded addition to 𝒫_1; since ςϵ_♭z_0 = z_0² = 1, [[rem:i-b-4-7]] (b) applies, and
[[prop:i-b-4-5]] holds for it.

**Lemma {#lem:i-b-6-6}** (Three lines.) Let F be holomorphic near the rectangle ℛ := [a − L, a + L] + i[0, 1], with
values in a Hilbert space, ‖F‖ ≤ A on ℛ, ‖F‖ ≤ A_0 on {Im w = 0} and ‖F‖ ≤ A_1 on {Im w = 1}, where
0 < A_0, A_1 ≤ A. Then for |Re w − a| ≤ L/2 and y := Im w,

    ‖F(w)‖ ≤ A_0^(1−y) A_1^y exp(3Λ e^(−πL/4)),     Λ := log(A/min(A_0, A_1)).

*Proof.* u := log‖F‖ is subharmonic, as the supremum over unit vectors e of the subharmonic functions
log|⟨F, e⟩|, attained at each point, and upper semicontinuous. v := (1 − y) log A_0 + y log A_1 is harmonic, and so is
k(w) := cosh((π/2)(x − a)) cos((π/2)(y − ½))/cos(π/4), x := Re w; k ≥ 1 on ℛ and k ≥ cosh((π/2)L) on its vertical
sides. So u − v − Λk/cosh((π/2)L) ≤ 0 on ∂ℛ (u − v ≤ 0 on the horizontal sides and ≤ Λ on the vertical ones), hence on
ℛ by the maximum principle. For |x − a| ≤ L/2, k/cosh((π/2)L) ≤ √2 cosh((π/4)L)/cosh((π/2)L) ≤ 2√2 e^(−πL/4). ∎

**Proposition {#prop:i-b-6-7}** (Cf. [Hin26c, Lemma 9.33].) Let γ_− < β < γ_+ < β′. There is h_0 such that for
z ∈ z_0 + i[hβ, hβ′] and h < h_0, P′_(h,z) : H_h^((2,0,0)) → L² is invertible, and

    ‖(P′_(h,z))⁻¹‖_(L²→L²) ≤ C h^(−1−(β′−Im(z/h))/(β′−β)).                                              {#eq:i-b-6-11}

Consequently, for every ϵ > 0 and z ∈ z_0 + i[h(γ_− + ϵ), h(γ_+ + ϵ)],
‖(P′_(h,z))⁻¹‖ ≤ C_ϵ h^(−1−δ_Γ(Im(z/h)−ϵ)).

*Proof.* (a) A priori estimates. Let 𝐏′ ∈ {P′, P′*}. Outside Γ(¾ε_Γ), [[prop:i-b-4-2]] bounds u by
‖𝐏′u‖_(H_h^((−2,0,0))). In Γ(ε_Γ): a point of the characteristic set not on Γ_u^♮ has a backward V-curve that leaves
Γ(ε_Γ) (D1), crossing {0 < q̃_0 < 1} into {q̃_0 = 1}, where 𝐏′ is elliptic; [[cor:i-b-4-6]] (with [[rem:i-b-4-7]])
propagates the elliptic bound along it. Near Γ, [[prop:i-b-6-4]] applies, with all its operators microsupported in
Γ(ε_Γ/3), where 𝐏′ = 𝐏 modulo O(h^∞) ([[lem:i-b-6-5]] (b)), its term ‖Eu‖ being bounded by the propagation just
described. Altogether, for z ∈ z_0 + i[hβ, hβ′],

    ‖u‖_(L²) ≤ C h⁻² ‖𝐏′u‖_(L²) + C h^M ‖u‖_(−M𝟏),

and with h⁻¹ in place of h⁻² at Im z = hβ′, using [[prop:i-b-6-1]] there; the last term is absorbed for h < h_0.

(b) Invertibility. For fixed h, P′_(h,z) is elliptic in the scattering sense at fibre infinity and over ∂X
([[lem:i-b-6-5]] (c)), so it has a parametrix modulo an operator with symbol in S^(−M𝟏), M large, which is compact on
L²; so P′_(h,z) : H_h^((2,0,0)) → L² is Fredholm, and by (a) it and its adjoint are injective.

(c) Interpolation. In terms of σ = z/h, (a) gives ‖P̂′(σ)⁻¹‖_(L²→L²) ≤ C for Re σ ≥ h_0⁻¹ and Im σ ∈ [β, β′], and
≤ C|σ|⁻¹ on Im σ = β′ (here ‖P̂′(σ)u‖_(L²) = h⁻²‖P′_(h,z)u‖_(L²) with h := |Re σ|⁻¹; for z_0 = −1 use
Re σ ≤ −h_0⁻¹). For σ_0 ≥ h_0⁻¹ and f ∈ L², apply [[lem:i-b-6-6]] to F(w) := P̂′(3σ_0 + iβ + (β′ − β)w)⁻¹f on
[−2σ_0/(β′ − β), 2σ_0/(β′ − β)] + i[0, 1], with A = A_0 = C‖f‖, A_1 = Cσ_0⁻¹‖f‖, L = 2σ_0/(β′ − β),
Λ = log σ_0; Λe^(−πL/4) → 0, so ‖P̂′(σ)⁻¹f‖ ≤ Cσ_0^(−(Im σ−β)/(β′−β))‖f‖ for Re σ ∈ [2σ_0, 4σ_0], with C independent
of σ_0. With |σ| ≤ 5σ_0 and
(P′_(h,z))⁻¹ = h⁻² P̂′(z/h)⁻¹ this is [[eq:i-b-6-11]]. For the consequence take β := γ_− + ϵ and β′ := γ_+ + ϵ; then
(β′ − η)/(β′ − β) = δ_Γ(η − ϵ) for η ∈ [β, β′]. ∎

#### The precise loss {#sec:i-b-6-6}

**Theorem {#thm:i-b-6-8}** (Cf. [Hin26c, Theorem 9.28], on E.) Let β > γ_− and U a neighbourhood of Γ. There are
B, E, G ∈ Ψ^0 microsupported in U, with B elliptic at Γ, WF′_h(E) ∩ Γ_u^♮ = ∅, Γ ∪ WF′_h(B) ⊂ Ell_h(G), and every
backward V-curve from WF′_h(B) ∖ Γ_u^♮ reaching Ell_h(E) within Ell_h(G), such that for z ∈ z_0 + i[hβ, ν′], h < h_0,
ϵ > 0 and all M, with δ := δ_Γ(Im(z/h) − ϵ),

    ‖Bu‖ ≤ C_ϵ(h^(−1−δ)‖G𝐏u‖ + h^(−δ)‖Eu‖ + h^M‖u‖_(−M)).                                              {#eq:i-b-6-12}

*Proof.* For Im z ≥ h(γ_+ + ϵ) this is [[eq:i-b-6-4]], with δ = 0; for Im z ∈ [hβ, h(γ_− + ϵ)] it is
[[eq:i-b-6-6]], as then δ = 1. Let Im z ∈ [h(γ_− + ϵ), h(γ_+ + ϵ)]. We follow [HV16, Theorem 4.7] as recalled in
[Hin26c]; all operators have kernels supported over {χ = 1}². Fix c ∈ (0, ε_Γ/12). Choose B elliptic at Γ with
WF′_h(B) ⊂ Γ(c/2), and B^♯ ∈ Ψ^0 with WF′_h(B^♯) ⊂ Γ(c) and WF′_h(I − B^♯) ∩ Γ(3c/4) = ∅; Γ(c) ⊂ Γ(ε_Γ/3). Then
B(I − B^♯) is residual and, by [[lem:i-b-6-5]] (b),

    Bu = B(P′_(h,z))⁻¹B^♯𝐏u + B(P′_(h,z))⁻¹[𝐏, B^♯]u + O(h^∞)‖u‖_(−M)

(for 𝐏 = P* use (P′*)⁻¹). The first term is bounded by C_ϵh^(−1−δ)(‖G𝐏u‖ + h^M‖u‖_(−M)) by [[prop:i-b-6-7]]. The
commutator is h times an operator microsupported in Γ(c) ∖ Γ(3c/4). Let X_u ∈ Ψ^0 be microsupported in
Γ(ε_Γ) ∩ {|φ_u^♮| < c/8}, with WF′_h(I − X_u) disjoint from Γ_u^♮ ∩ Γ(c), and such that backward V-curves from
WF′_h(I − X_u) ∩ Γ(c) reach Ell_h(E) ((D1), choosing E elliptic on Γ(ε_Γ) ∩ {|φ_u^♮| ≥ c/16}).

(i) By [[cor:i-b-4-6]], ‖(I − X_u)[𝐏, B^♯]u‖ ≤ Ch(h⁻¹‖G𝐏u‖ + ‖Eu‖ + h^M‖u‖_(−M)), and [[prop:i-b-6-7]] turns this
into a bound C_ϵh^(−δ)(h⁻¹‖G𝐏u‖ + ‖Eu‖ + h^M‖u‖_(−M)) for B(P′)⁻¹(I − X_u)[𝐏, B^♯]u.

(ii) f_u := X_u[𝐏, B^♯]u is microsupported in K_f := Γ(c) ∖ Γ(3c/4) ∩ {|φ_u^♮| < c/8}, where |φ_s^♮| ≥ 3c/4 or
|G_(z_0)| ≥ 3c/4. Let W̃ := Op_h(w̃) Id with w̃ ∈ C_c^∞ real and scalar, w̃ ≠ 0 on Γ(c/4) and supp w̃ ⊂ Γ(c/2), and
Q̃ := W̃*W̃. Then every backward bicharacteristic of the characteristic set in Γ(ε_Γ) reaches Ell_h(Q̃) (if on Γ_u^♮,
by (D2)) or the region q̃_0 = 1, so the argument of part (a) of the proof of [[prop:i-b-6-7]] (with −iz_0Q̃ as a
further absorbing term: [[rem:i-b-4-7]] (b) with ϵ_W := z_0 for P′, and with ϵ_W := −z_0 for the adjoint
P′* + iz_0Q̃, so ςϵ_W = 1 as in [[sec:i-b-6-5]]) gives ‖(P′ − iz_0Q̃)⁻¹‖ ≤ Ch⁻¹, and [[lem:i-b-6-9]] applies to
P′ − iz_0Q̃. The factor z_0 in the absorbing term is needed: without it the absorbing sign is wrong for z_0 = −1. The
forward V-flowout of K_f ∩ Σ_(z_0) stays in {|φ_s^♮| ≥ 3c/4} while it remains in Γ(ε_Γ) (as |φ_s^♮| increases
forward), and the part of K_f off Σ_(z_0) is elliptic; so the flowout misses WF′_h(Q̃) ∪ WF′_h(B) ⊂ Γ(c/2). By
[[lem:i-b-6-9]], Q̃(P′ − iz_0Q̃)⁻¹f_u and B(P′ − iz_0Q̃)⁻¹f_u are O(h^∞)‖u‖_(−M). Since
v := (P′)⁻¹f_u − (P′ − iz_0Q̃)⁻¹f_u satisfies P′v = −iz_0Q̃(P′ − iz_0Q̃)⁻¹f_u, [[prop:i-b-6-7]] gives
‖v‖ ≤ C_Mh^M‖u‖_(−M); so ‖B(P′)⁻¹f_u‖ ≤ C_Mh^M‖u‖_(−M).

Summing (i) and (ii) gives [[eq:i-b-6-12]]. ∎

**Lemma {#lem:i-b-6-9}** (Direction of propagation.) Let 𝐏″ be P′ − iz_0Q̃ (or its adjoint, with forward replaced by
backward) with ‖(𝐏″)⁻¹‖ ≤ Ch⁻¹. Let X ∈ Ψ^0 be microsupported in a compact K_X ⊂ T*X̃°, and let ϖ ∉ K_X not lie in the
closure of the forward V-flowout of K_X ∩ Σ_(z_0) inside Γ(ε_Γ). Then there is B_ϖ elliptic at ϖ with
‖B_ϖ(𝐏″)⁻¹Xf‖ ≤ C_Mh^M‖f‖_(−M𝟏).

*Proof.* If ϖ is in the elliptic set of 𝐏″, [[prop:i-b-2-10]] gives ‖B_ϖw‖ ≤ C(‖G𝐏″w‖ + h^M‖w‖) with G microsupported
near ϖ, off K_X. Otherwise the backward V-curve from ϖ reaches the elliptic set of the absorption without meeting K_X, and
[[cor:i-b-4-6]] gives ‖B_ϖw‖ ≤ C(h⁻¹‖G𝐏″w‖ + h^M‖w‖) with G microsupported near that curve, again off K_X. Take
w := (𝐏″)⁻¹Xf: G𝐏″w = GXf = O(h^∞) and ‖w‖ ≤ Ch⁻¹‖Xf‖. ∎

### The artificial boundary {#sec:i-b-7}

This is [Hin26c, Proposition 9.35], the semiclassical form of [[sec:i-a-6]]. [Hin26c] proves the energy estimate for
h⁻¹ Im z large and cites [Hin25a, Theorem 9.44] for bounded h⁻¹ Im z; here one argument covers every z with Im z ≥ 0,
the exponential weight in r of [[prop:i-a-6-3]] supplying the positivity that the weight in t supplies there only for
h⁻¹ Im z large. The slab spaces H^s(Ω_(a,b))^(•,−) (supported at r = b, extendible at r = a) and H^s(Ω_(a,b))^(−,•) are those of
[[sec:i-a-6-1]], with the semiclassical norms ‖u‖_(H_h^s) := ‖⟨hD⟩^s u‖; over the compact slabs used here the decay
order plays no role, and an admissible 𝖻 is constant ([[sec:i-b-1-4]]), so it enters only as the factor h^(−𝖻).

#### The H¹_h estimate {#sec:i-b-7-1}

On ℳ := ℝ_t × {r_0 − 2δ_0 < r < r_2} let g be the metric of (H6), time-oriented so that −∇t is future directed, and
□_g := −∇^μ∇_μ componentwise. dr has no dt-component, and g⁻¹(dr, dr) = G_0(dr) < 0 (H4), so dr is g-timelike; the
future direction decreases r, so X := ∇^g r is future directed timelike. For ℂ^(N_E)-valued u′ on ℳ let
T[u′](Y, Z) := Re(⟨Yu′, Zu′⟩ − ½g(Y, Z) g⁻¹(⟨du′, du′⟩)) and ^(Y)K[u′] := ½T[u′]^(μν)(ℒ_Y g)_μν. [[lem:i-a-6-2]]
holds on ℳ with the same proof: div_g(T[u′](W, ·)^♯) = −Re⟨□_g u′, Wu′⟩ + ^(W)K[u′], and
^(wX)K = w ^(X)K + T(∇w, X). For future causal Y, Z, T(Y, Z) ≥ 0, and on a compact set T[u′](X, X) ≥ c_0|du′|²_R for a
fixed Riemannian metric R on ℳ.

**Proposition {#prop:i-b-7-1}** Let r_0 − 2δ_0 < a < b < r_2 and Z as in [[sec:i-b-4]]. There is C such that for
z ∈ Z, h ∈ (0, 1],

    ‖u‖_(H¹_h(Ω_(a,b))) ≤ C h⁻¹ ‖P_(h,z) u‖_(L²(Ω_(a,b))),     u ∈ H²(Ω_(a,b))^(•,−),                    {#eq:i-b-7-1}

and ‖v‖_(H¹_h(Ω_(a,b))) ≤ C h⁻¹ ‖P_(h,z)^(*h) v‖_(L²(Ω_(a,b))) for v ∈ H²(Ω_(a,b))^(−,•). C depends on bounds for
the coefficients, on inf(−G_0(dr)) over the slab and on Z.

*Proof.* By density ([[lem:i-a-6-1]] (c), and smooth approximation up to the extendible side) take u smooth on
Ω̄_(a,b) and vanishing near r = b. P_0 − □_g Id =: L_1 is first order with t-independent coefficients ([[sec:i-b-1-2]]), so L̂_1(σ) = L̂_1(0) + σY_0 with Y_0 a matrix
function and |L̂_1(z/h)u| ≤ C(|du| + h⁻¹|u|). Let u′(t, x) := e^(−izt/h) u(x) on D := [0, 1]_t × Ω_(a,b), so that
□_g u′ = e^(−izt/h)(P̂(z/h) − L̂_1(z/h))u, and let W := wX with w := e^(−2(Im z)t/h) e^(ℓr). Then

    ^(W)K[u′] = w(^(X)K[u′] + 2h⁻¹(Im z) T[u′](−∇t, X) + ℓ T[u′](X, X)) ≥ w(ℓc_0 − C_0)|du′|²_R,

using Im z ≥ 0, T(−∇t, X) ≥ 0 and |^(X)K| ≤ C_0|du′|²_R. Since du′ = e^(−izt/h)(du − ih⁻¹z u dt) and
|α + β dt|²_R ≥ c(|α|²_R + |β|²) for α without dt-component, w|du′|²_R ≥ c e^(ℓr)(|du|² + ¼h⁻²|u|²), a function of x
only. Apply the divergence theorem to J := T[u′](W, ·)^♯ on D. At r = b nothing contributes. At r = a the outward
conormal is −dr, and the flux is −∫ wT[u′](X, X) ≤ 0. At t = 1 and t = 0 the fluxes are −E(1) and E(0),
E(t) := ∫_({t}×Ω_(a,b)) T[u′](W, −∇t); as T[u′] carries the factor |e^(−izt/h)|² = e^(2(Im z)t/h), which w cancels,
and g is t-independent, E(1) = E(0). Hence

    ∫_D ^(W)K[u′] ≤ ∫_D Re⟨□_g u′, Wu′⟩,

and as Wu′ = we^(−izt/h)(Xu − ih⁻¹z(Xt)u) and the integrands are t-independent,

    c(ℓc_0 − C_0) ∫_Ω e^(ℓr)(|du|² + ¼h⁻²|u|²) ≤ C ∫_Ω e^(ℓr)(|P̂(z/h)u| + |du| + h⁻¹|u|)(|du| + h⁻¹|u|).

For ℓ large the terms without P̂ on the right are absorbed, and then
∫ e^(ℓr)(|du|² + h⁻²|u|²) ≤ Cℓ^(−2) ∫ e^(ℓr)|P̂(z/h)u|². With e^(ℓa) ≤ e^(ℓr) ≤ e^(ℓb) and P̂(z/h) = h⁻²P_(h,z),
multiplying by h² gives [[eq:i-b-7-1]]. For v: P_(h,z)^(*h) = h²P̂(z/h)^(*h), and P̂(σ)^(*h) is the spectral family at
σ̄ of the formal adjoint P_0^(*h) (with respect to dt dx and h), a stationary operator of the same form with principal
symbol G. Under t ↦ −t, with the time orientation reversed, it becomes a stationary operator of this form at the
spectral parameter −z̄/h, Im(−z̄) = Im z ≥ 0, for which −∇t is again future directed while −∇r is now future directed,
the future increasing r. The argument above with X replaced by −∇r, e^(ℓr) by e^(−ℓr), and the roles of r = a and
r = b exchanged gives the second estimate. ∎

#### All orders {#sec:i-b-7-2}

**Proposition {#prop:i-b-7-2}** For every s ∈ ℝ and slab Ω_(a,b) with r_0 − δ_0 < a < b < r_2 − δ_0, uniformly for
z ∈ Z and h < h_0:

(i) ‖u‖_(H_h^s(Ω_(a,b))^(•,−)) ≤ C h⁻¹ ‖P_(h,z) u‖_(H_h^(s−1)(Ω_(a,b))^(•,−)) for u ∈ H^s(Ω_(a,b))^(•,−);

(ii) ‖v‖_(H_h^s(Ω_(a,b))^(−,•)) ≤ C h⁻¹ ‖P_(h,z)^(*h) v‖_(H_h^(s−1)(Ω_(a,b))^(−,•)) for v ∈ H^s(Ω_(a,b))^(−,•).

*Proof.* As in [[prop:i-a-6-4]], with the semiclassical estimates in place of the fixed-frequency ones; we prove (i).
Fix a′ ∈ (r_0 − δ_0, a) and Ω′ := Ω_(a′,b).

*Uniqueness* at each fixed h is [[prop:i-a-6-4]] (iii) at σ = z/h.

*Existence with bounds, s ≥ 0.* For f ∈ H_h^(s−1)(Ω′)^(•,−) ⊂ H_h^(−1)(Ω′)^(•,−) = (H¹_h(Ω′)^(−,•))*, the functional
P_(h,z)^(*h)φ ↦ ⟨f, φ⟩ on {P_(h,z)^(*h)φ : φ ∈ H²(Ω′)^(−,•)} ⊂ L² is bounded by
C h⁻¹‖f‖_(H_h^(−1)) ‖P_(h,z)^(*h)φ‖, by [[prop:i-b-7-1]] for the adjoint. The Hahn–Banach and Riesz theorems give
w ∈ L²(Ω′) with ‖w‖ ≤ C h⁻¹‖f‖_(H_h^(−1)) and P_(h,z)w = f, the extension W of w by 0 beyond b satisfying
P_(h,z)W = F (the supported extension of f) on {r > a′}.

*Regularity.* (α) At each h. W is in L²(Ω′)^(•,−) and solves P_(h,z)W = f; by [[prop:i-a-6-4]] (iii) at σ = z/h, at
the orders s and 0, the solution in H^s(Ω′)^(•,−) ⊂ L²(Ω′)^(•,−) is the unique one in L²(Ω′)^(•,−), so
W ∈ H^s(Ω′)^(•,−), and the estimates of [[sec:i-b-3]] and [[sec:i-b-4]] apply to its cut-offs by [[lem:i-b-3-1]].

(β) Uniformly in h. Over {a′ < r < b + δ_0} every characteristic point of P_(h,z), at finite frequencies or at fibre
infinity, lies on a bicharacteristic along which r is strictly monotone: H_G r = 2g⁻¹(ν, dr) ≠ 0 for null ν ≠ 0, dr
being timelike; and for Im z > 0 there is no characteristic point at finite frequencies there ([[lem:i-b-1-1]] (d);
[[lem:i-b-1-1]] (e), stated for z_0 = ±1, holds for every real z ≠ 0 by homogeneity). Its backward direction (in the
sense of [[prop:i-b-4-5]] for P) increases r and reaches {r > b}, where W = 0. Fix a″ ∈ (a′, a).
[[cor:i-b-4-6-prime]] at the order (s, 0, 0) with J ≥ 4s, finitely many times (compactness), with all its operators
microsupported over {r > a″}, and [[prop:i-b-4-2]] off the characteristic set, give
‖W‖_(H_h^s({r>a})) ≤ C(h⁻¹‖F‖_(H_h^(s−1)) + ‖W‖_(L²)). ([[cor:i-b-4-6]] itself would leave h^M‖GW‖_(H_h^s) with G
elliptic on a neighbourhood of the curves, which reaches below r = a, a term on a larger set than the left side
controls, and no enlargement of the cover absorbs it.) So ‖w‖_(H_h^s(Ω_(a,b))) ≤ C h⁻¹‖f‖_(H_h^(s−1)(Ω′)).

*Conclusion for s ≥ 0.* For u ∈ H^s(Ω_(a,b))^(•,−) extend Pu to f ∈ H_h^(s−1)(Ω′)^(•,−) with at most twice its norm,
solve as above, and use uniqueness on Ω_(a,b): w|_(Ω_(a,b)) = u.

*s < 0.* By (ii) for P^(*h) at the order 1 − s > 0, the duality argument of [[prop:i-a-6-4]] with
(H_h^(1−s)(Ω′)^(−,•))* = H_h^(s−1)(Ω′)^(•,−) gives a solution w ∈ H_h^s(Ω′)^(•,−) with ‖w‖ ≤ C h⁻¹‖f‖; uniqueness
concludes. (ii) is the same with the ends exchanged. ∎

**Corollary {#cor:i-b-7-3}** (The semiclassical form of [[cor:i-a-6-5]].) Let b′, b″, χ, χ_1 be as in
[[cor:i-a-6-5]]. For z ∈ Z, h < h_0 and all s,

    ‖χu‖_(H̄_h^s) ≤ C(h⁻¹‖P_(h,z) u‖_(H̄_h^(s−1)({r_0<r<b″})) + ‖χ_1 u‖_(H_h^s)),     u ∈ H̄_h^s,           {#eq:i-b-7-2}

    ‖v|_(Ω_(r_0,b″))‖_(H_h^(1−s)(Ω_(r_0,b″))^(−,•))
        ≤ C h⁻¹ ‖(P_(h,z)^(*h) v)|_(Ω_(r_0,b″))‖_(H_h^(−s)(Ω_(r_0,b″))^(−,•)),     v ∈ Ḣ_h^(1−s).   {#eq:i-b-7-3}

*Proof.* P_(h,z)(χu) = χP_(h,z)u + [P_(h,z), χ]u and [P_(h,z), χ] = h · Diff¹_h is supported in supp dχ, so
h⁻¹‖[P_(h,z), χ]u‖_(H_h^(s−1)) ≤ C‖χ_1 u‖_(H_h^s). Apply [[prop:i-b-7-2]] (i) on Ω_(r_0,b″); [[eq:i-b-7-3]] is
[[prop:i-b-7-2]] (ii). ∎

### Proof of the high-energy theorem {#sec:i-b-8}

Fix z_0, α_+, s and admissible 𝗋, 𝖻, and write 𝐨 := (s, 𝗋 + α_+, 𝖻),
𝐨′ := 𝐨 − 𝐦 + (1, 1, 0) = (s − 1, 𝗋 + α_+ + 1, 𝖻). The decay order of u is 𝗋 + α_+, and the thresholds of
[[sec:i-b-1-4]] are conditions on it.

#### Splitting off the artificial boundary {#sec:i-b-8-1}

Choose r_0 < b′_0 < b′_1 < b′_2 < b′ < b″ < r_2 − δ_0 and χ, χ_1 as in [[cor:i-b-7-3]] for b′, b″, and ψ ∈ C^∞ with
ψ = 0 on {r ≤ b′_0} and ψ = 1 on {r ≥ b′_1}. Over {r_0 − 2δ_0 < r < r_2} the bicharacteristics move strictly
monotonically in r, the future direction decreasing it ([[sec:i-b-7-2]]). So a backward bicharacteristic from a point
over {r ≥ b′_2} stays over {r ≥ b′_2}: it increases r while r < r_2, and it cannot re-enter {r < r_2}, which it could
only do with r decreasing backward. Every estimate of [[sec:i-b-4]] to [[sec:i-b-6]] used below at points over
{r ≥ b′_2} for the direct problem is therefore taken with all its operators microsupported over {r > b′_1}, where
ψ = 1 (each estimate is local near its curves, and its neighbourhoods are chosen inside {r > b′_1}); applied to ψu,
extended by 0 to ℝ⁴, it has GPψu = GPu modulo a residual term. The points over {r ≥ b′_1} could not be covered in
this way, since their estimates reach below b′_1.

#### The direct estimate at k = 0 {#sec:i-b-8-2}

**Proposition {#prop:i-b-8-1}** Let ϵ > 0.

(a) There are ν_1 > 0, h_0 and C such that for z ∈ z_0 + i[0, ν_1], h < h_0 and u ∈ H̄_h^𝐨 with
P_(h,z)u ∈ H̄_h^(𝐨′), with δ := δ_Γ(Im(z/h) − ϵ),

    ‖u‖_(H̄_h^𝐨) ≤ C h^(−1−δ) ‖P_(h,z) u‖_(H̄_h^(𝐨′)).                                                  {#eq:i-b-8-1}

(b) For ν ≥ ν_1, [[eq:i-b-8-1]] holds for z ∈ z_0 + i[ν_1, ν] with δ = 0.

(c) In the setting of [[thm:i-b-1-3]] (2), [[eq:i-b-8-1]] holds with δ = 0.

*Proof.* By [[lem:i-b-3-1]] (applied to ψu, and on the slab by [[lem:i-a-6-1]]) it suffices to take u smooth up to
∂_♯X and Schwartz at ∂X, the constants being independent of the approximation.

(a) *The cover.* Let K_Σ := Σ_(z_0) ∩ {r ≥ b′_2} ⊂ 𝒫, compact. Each ϖ ∈ K_Σ is of one of the following kinds, by
(H8), (H4) at fibre infinity and [[lem:i-a-4-5]] over ∂X.

- (R) ϖ ∈ ∂ℛ_+ ∪ ∂ℛ_− ∪ R_(z_0,in): [[prop:i-b-5-2]] and [[prop:i-b-5-3]] give a neighbourhood U_ϖ and
  ‖B_* u‖_𝐨 ≤ C(h⁻¹‖GPu‖_(𝐨′) + h^M‖Gu‖_𝐨 + ‖u‖_(−M𝟏)) for B_* microsupported in U_ϖ, with no a priori term; here
  s > ½ + ϑ_ℋ and 𝗋 + α_+ > ½(−1 + ϑ_in) at R_(z_0,in) are used.
- (A) ϖ is not of kind (R), not in Γ̄_u and not R_out: its backward curve tends to a set of kind (R) ((H8) (a)), so
  after finite time enters a neighbourhood U_* given by (R); on the segment, 𝖧_(z_0) ≠ 0, q̂_(z_0) ≠ 0
  ([[lem:i-b-1-1]] (e), and [[sec:i-b-4-1]] over ∂X away from R_out), and [[eq:i-b-4-4]] holds by admissibility.
  [[cor:i-b-4-6]] gives an estimate at ϖ with a priori term on a compact subset of U_*, which (R) bounds.
- (Γ) ϖ ∈ Γ: [[thm:i-b-6-8]] (with β := ½γ_− < 0, so that Im z ≥ 0 ≥ hβ) gives an estimate near Γ with loss h^(−1−δ)
  and a priori term h^(−δ)‖Eu‖, E microsupported off Γ_u near Γ; the points of WF′_h(E) are off Γ̄_u by (H8) (b), so
  of kind (A), or elliptic.
- (U) ϖ ∈ Γ̄_u ∖ Γ: its backward curve tends to Γ, so for large negative times it lies on Γ_u ((H8) (b)) inside the
  neighbourhood given by (Γ); [[cor:i-b-4-6]] from there.
- (O) ϖ = R_out: [[prop:i-b-5-5]] with a priori term on a compact K_E ⊂ Ū_0 ∖ R_out, whose points are of kinds (A),
  (U) or elliptic (a backward curve from near R_out leaves every small neighbourhood of it, R_out being a sink); here
  𝗋 + α_+ < −½ + ½ inf min spec(S + S^(*h)) is used.

Each kind is used only after the kinds its a priori terms need, and the order (R), (A), (Γ), (U), (O) is acyclic. By
compactness, finitely many of these neighbourhoods cover K_Σ, and each estimate holds for z in a neighbourhood of z_0
([[cor:i-b-4-6]]; [[prop:i-b-5-2]], [[prop:i-b-5-3]], [[prop:i-b-5-5]] for all z in the sets stated;
[[thm:i-b-6-8]] for z ∈ z_0 + i[hβ, ν′]). The complement in 𝒫|_({r≥b′_2}) of the union of the neighbourhoods is
compact and elliptic for P_(h,z_0), hence for P_(h,z), |z − z_0| small ([[prop:i-b-4-2]]). Take ν_1 so small that all
of this holds for z ∈ z_0 + i[0, ν_1]. For φ ∈ {1 − χ, χ_1}, both supported in {r > b′_2}, a microlocal partition of
unity Σ_j B_j = φ, modulo a residual operator, subordinate to the cover, and the chain of estimates give, with δ ≤ 1
and h^(−δ) · h⁻¹ ≤ h^(−1−δ),

    ‖φu‖_(H_h^𝐨) ≤ C(h^(−1−δ)‖Pu‖_(H̄_h^(𝐨′)) + h^M‖u‖_(H̄_h^𝐨) + ‖u‖_(H̄_h^(−M𝟏))).

*The artificial boundary.* By [[eq:i-b-7-2]], ‖χu‖_(H̄_h^𝐨) ≤ C(h⁻¹‖Pu‖_(H̄_h^(𝐨′)) + ‖χ_1 u‖_(H_h^𝐨)), the orders
being constant there apart from s; the last term is the previous display with φ = χ_1, and
‖u‖ ≤ ‖χu‖ + ‖(1 − χ)u‖, the second by the previous display with φ = 1 − χ.

*Absorption.* ‖u‖_(H̄_h^(−M𝟏)) ≤ Ch‖u‖_(H̄_h^𝐨) for M ≥ max(1, −s, −min(𝗋 + α_+), 1 − min 𝖻), since
w_(−M𝟏)/w_𝐨 ≤ Ch, and h^M ≤ h; so for h < h_0 the last two terms are absorbed, which is [[eq:i-b-8-1]].

(b) For Im z ≥ ν_1, P_(h,z) is elliptic at finite frequencies over X̃° ([[lem:i-b-1-1]] (d)) and over ∂X except at
R_out ([[sec:i-b-4-1]]), uniformly for Im z ∈ [ν_1, ν] by compactness. The characteristic set over {r ≥ b′_2} is
∂Σ_0 ∪ R_out. On ∂Σ_0 the kinds are (R) at ∂ℛ_± and (A) along the curves of (H4); at R_out, kind (O), whose a priori
set K_E is now elliptic. No trapping estimate enters, so δ = 0.

(c) The same as (b), with Re z varying in [−2, 2]: at fibre infinity 𝖧_z does not depend on z, 𝖻 is constant, and only
the constancy of 𝗋 near R_out and the threshold there are used. ∎

#### The adjoint estimate {#sec:i-b-8-3}

**Proposition {#prop:i-b-8-2}** In the settings of [[prop:i-b-8-1]], for v ∈ Ḣ_h^(−𝐨′) with
P_(h,z)^(*h)v ∈ Ḣ_h^(−𝐨),

    ‖v‖_(Ḣ_h^(−𝐨′)) ≤ C h^(−1−δ) ‖P_(h,z)^(*h) v‖_(Ḣ_h^(−𝐨)).                                          {#eq:i-b-8-2}

*Proof.* The same argument for ϵ_♭ = −1: estimates propagate along the past field. The kinds without a priori term are
now R_out (the adjoint half of [[prop:i-b-5-5]], above threshold at the order −𝗋 − α_+ − 1) and the artificial
boundary ([[eq:i-b-7-3]], with nothing on the right but P^(*h)v); Γ is handled by [[thm:i-b-6-8]] for P*, with a priori
term off Γ_u^♮ = Γ_s; ∂ℛ_± and R_(z_0,in) are sinks for the past field, handled by [[eq:i-b-5-5]] and [[prop:i-b-5-3]]
with a priori terms on punctured neighbourhoods. By (H8), the forward (future) curve of a characteristic point not on
Γ̄_s tends to R_out or reaches {r < r_0 − δ_0}, and at fibre infinity reaches {r < r_0 − δ_0} (H4); so the chains
start at the sets without a priori term. The orders −𝐨′ satisfy the reversed monotonicity, −𝗋 and −𝖻 being
non-increasing along the past field. Near ∂_♯X, v restricted to Ω_(r_0,b″) is bounded by [[eq:i-b-7-3]]; beyond, the
microlocal estimates apply to (1 − χ)v, whose commutator term [P^(*h), χ]v is supported where [[eq:i-b-7-3]] already
bounds v. ∎

*Proof of [[thm:i-b-1-3]] (1) and (2).* By [[prop:i-b-8-1]] and [[prop:i-b-8-2]], as δ_Γ ≤ 1. For Im z ∈ [ν_1, ν]
and in (2) the loss is h⁻¹. ∎

#### Invertibility {#sec:i-b-8-4}

*Proof of [[thm:i-b-1-3]] (3).* Let σ with Im σ ≥ 0 and |σ| ≥ C_0. If Im σ ≥ ν′|σ|, put h := |σ|⁻¹ and z := hσ, so
|z| = 1 and Im z ≥ ν′ (part (2)). Otherwise |Re σ| ≥ |σ|√(1 − ν′²) and Im σ < ν′|σ| ≤ 2ν′|Re σ|; put
h := |Re σ|⁻¹, z := hσ ∈ z_0 + i[0, 2ν′] with z_0 = sgn Re σ (part (1) with ν := 2ν′). In both cases h < h_0 for C_0
large. At this fixed h, H_h^𝐨 is the space H^(s,(𝗋+α_+)_h) of [[ch:s01]] with 𝗋_h(x, ξ) := 𝗋(x, hξ), up to an
equivalent norm ([[sec:i-b-2-3]]; h^(−𝖻(x,hξ)) is a symbol of order 0 at fixed h), and in the case of part (1) 𝗋_h is
admissible for Re σ in the sense of (O2)–(O3) of [[def:i-a-admissible]] (the characteristic set over ∂X at σ in the
variable
ξ is that at z in ζ = hξ, and [[sec:i-b-1-4]] asks more than (O2)); in the case of part (2) it is constant near R_out
with the threshold there, which is what [[thm:i-a-7-2]] (2) asks, for every real part including 0. So 𝒳_σ and 𝒴_σ of
[[thm:i-a-7-2]] are the spaces of [[eq:i-b-1-6]], and [[eq:i-b-1-6]] shows that P̂(σ) = h⁻²P_(h,z) is injective on
𝒳_σ and P̂(σ)^(*h) injective on 𝒴_σ*. By [[thm:i-a-7-2]] (3), P̂(σ) is Fredholm, so it is invertible. ∎

#### b-regularity {#sec:i-b-8-5}

*Proof of [[thm:i-b-1-3]] (4).* By the equivalence after [[eq:i-b-5-9]], [[eq:i-b-1-7]] is

    ‖u‖_(𝐨;k) ≤ C h^(−1−δ) ‖P_(h,z) u‖_(𝐨′;k)                                                           {#eq:i-b-8-3}

for 𝐨 and 𝐨′ read on X̄ (the norm [[eq:i-b-5-9]] with H̄ in place of H). Induction on k; k = 0 is [[eq:i-b-8-1]]. Let
k ≥ 1.

(i) Over {r ≤ b″}, the V's are smooth vector fields spanning TX̃ (there r > 0), so ‖χu‖_(𝐨;k) is equivalent to
‖χu‖_(H̄_h^(𝐨+(k,0,0))), and [[eq:i-b-7-2]] at regularity s + k bounds it by
h⁻¹‖Pu‖_(H̄_h^(𝐨′+(k,0,0))) + ‖χ_1 u‖_(H_h^(𝐨+(k,0,0))), the first term being at most Ch⁻¹‖Pu‖_(𝐨′;k).

(ii) Away from R_out and the zero section: the symbols of the hV_j are ρ⁻¹ times the components of ζ in a frame
([[lem:i-a-4-4]]), so Σ_(|α|=k) ((hV)^α)*(hV)^α is elliptic of order 2k(1, 1, 0) wherever |ζ| ≥ c > 0, including fibre
infinity; there ‖Bu‖_(𝐨;k) and ‖Bu‖_(𝐨+k(1,1,0)) bound each other modulo ‖B̃u‖_(𝐨;k−1) + ‖u‖_(−M𝟏), by
[[prop:i-b-2-10]]. At the zero section over X̃°, G_z(x, 0) = z²g_00 ≠ 0, so P is elliptic there, and every order is
controlled by ‖Pu‖ ([[prop:i-b-4-2]]); at finite frequencies over a compact set all orders are equivalent.

(iii) So the chain of [[sec:i-b-8-2]] at the shifted order 𝐨_k := 𝐨 + k(1, 1, 0) bounds u microlocally on the cover
except near R_out, with ‖GPu‖_(𝐨_k−𝐦+(1,1,0)) ≤ C(‖Pu‖_(𝐨′;k) + ‖u‖_(−M𝟏)) for the G that occur (all microsupported
where (ii) applies). 𝐨_k satisfies every condition the chain uses away from R_out: s + k > ½ + ϑ_ℋ, 𝗋 + α_+ + k is
above the threshold at R_(z_0,in), and the monotonicity is unchanged by adding constants.

(iv) Near R_out, [[prop:i-b-5-7]], whose term ‖E′u‖_(𝐨+k(1,1,0)) is supported on K_E, bounded by (iii).

(v) The error terms h^M‖Gu‖_(𝐨_k) and h^M‖Gu‖_(𝐨;k) are bounded by h^M‖u‖_(𝐨;k) and h^M‖Pu‖ by (ii), and absorbed for
h small; the terms ‖B̃u‖_(𝐨;k−1) are bounded by the induction hypothesis.

This gives [[eq:i-b-8-3]], uniformly in the settings of (1) and (2). ∎

#### Regularity in the spectral parameter {#sec:i-b-8-6}

*Proof of [[thm:i-b-1-3]] (5).* For σ as in (3), P̂(σ)⁻¹ is C^∞ in σ as a map between the spaces of [[thm:i-a-7-2]] (6)
(holomorphic for Im σ > 0), and on the overlaps the inverses at different admissible orders agree, kernels and
cokernels being trivial for all of them. So ∂_σP̂⁻¹ = −P̂⁻¹(∂_σP̂)P̂⁻¹, and (σ∂_σ)^j P̂⁻¹ is a sum, with integer
coefficients, of products

    P̂⁻¹ 𝒯_(i_1) P̂⁻¹ ⋯ 𝒯_(i_l) P̂⁻¹,     𝒯_i := (σ∂_σ)^i P̂(σ) = σT + 2^i σ² g_00,
    i_1 + ⋯ + i_l = j,  1 ≤ l ≤ j.                                                                    {#eq:i-b-8-4}

By (H2), σT = 2iσρ(V_1 − 3/2 − S) − iσQ, so 𝒯_i = σρ𝒱 + σρc + σρ³ Diff¹_b + 2^i σ² g_00 with 𝒱 = 2iV_1 and c a
matrix function. Write ‖·‖_((s;k),𝗋;+) for [[eq:i-b-1-5]] at decay order 𝗋 (and 𝖻 fixed), so that
‖u‖_((s;k),𝗋;+) ≍ h^(−k)‖u‖_((s,𝗋,𝖻);k), with h as in [[thm:i-b-1-3]] (3), so that ½|σ| ≤ h⁻¹ ≤ |σ|. Then:

(a) 𝒯_i maps (s′; k′ + 1), 𝗋′ to (s′; k′), 𝗋′ + 1 with norm ≤ C|σ|, for all s′, k′ and decay orders 𝗋′: with
σ = zh⁻¹, σρV_1 = h⁻²zρ(hV_1), and ‖h⁻²ρ(hV_1)u‖_((s′,𝗋′+1,𝖻);k′) ≤ Ch⁻²‖u‖_((s′,𝗋′,𝖻);k′+1) (hV_1 is one of the
module operators of [[eq:i-b-5-9]], and ρ raises the decay order by 1), so the norm is h^(−k′)h⁻²h^(k′+1) = h⁻¹; the
other terms are smaller or equal: σρc and σρ³ Diff¹_b likewise, and σ²g_00 = h⁻²z²g_00 with g_00 ∈ ρ²C^∞ raises the
decay order by 2 and costs h⁻² from (s′; k′), which is h⁻¹ from (s′; k′ + 1) as
‖·‖_((s′;k′+1);+) ≥ h⁻¹‖·‖_((s′;k′);+).

(b) P̂(σ)⁻¹ = h²P_(h,z)⁻¹ maps (s′ − 1; k′), 𝗋 + α_+ + 1 to (s′; k′), 𝗋 + α_+ with norm ≤ C|σ|^(−1+δ), for every
s′ ≥ s and k′, by [[eq:i-b-8-3]] (s′ is admissible since s′ > ½ + ϑ_ℋ).

(c) (s′; k′ + 1); + embeds in (s′ + 1; k′); + with norm ≤ C: at fibre infinity the module operators are elliptic of
order (1, 1, 0) (as in (ii) of [[sec:i-b-8-5]]), which gives one order of regularity, and at finite frequencies the
regularity order is immaterial.

In a product [[eq:i-b-8-4]] with l factors 𝒯, apply (b) l + 1 times, at the regularity orders s, s + 1, …, s + l, and
(a) l times, starting from f in (s − 1; k + j), after converting j − l module orders into regularity by (c) where
needed: each P̂⁻¹ raises the regularity by one, each 𝒯 lowers the module order by one and leaves the regularity, and
the target (s + j; k) is reached after j − l uses of (c). The norm is at most
C|σ|^((l+1)(−1+δ)+l) ≤ C|σ|^(−1+(j+1)δ), as l ≤ j and |σ| ≥ 1. This is [[eq:i-b-1-8]]. ∎

### Uniformity in the operator {#sec:i-b-9}

Let P̂ depend on b ∈ ℬ as in (H5)–(H8). Every constant above depends on finitely many seminorms of the symbols involved
and on finitely many lower bounds: ellipticity constants, β_*, c_1 and c_𝒯 in [[lem:i-b-5-1]], the margins in the
thresholds, c_0 in [[prop:i-b-4-5]], ν_min, β_0, c_Γ and the thresholds γ_± in [[sec:i-b-6]], the lengths of the curves
in the chains of [[sec:i-b-8]], and the constants of [[prop:i-b-7-1]]. Each depends continuously on b, by (H5)–(H8),
and the constructions (flow boxes by [[lem:i-b-4-3]] with b among the parameters; the commutants; the absorbing
operator of [[sec:i-b-6-5]], with Γ(δ) defined through φ_(u/s), which depend continuously on b) can be made with b in a
neighbourhood of each b_0; by compactness of ℬ, finitely many suffice. The two arguments by contradiction
([[prop:i-b-6-4]] and the absorption in part (a) of the proof of [[prop:i-b-6-7]]) are run with sequences
(h_j, z_j, b_j), b_j → b_∞ after passing to a subsequence, every operator of the argument (the B, E, G, the
quantisations Φ, N_u, J_u of Step 1 of the proof of [[prop:i-b-6-4]], and the cut-offs) being built from the data of
b_j, which converge in C^∞ to those of b_∞ by (H5)–(H8). So [[eq:i-b-6-8]] holds with remainders O(h) uniformly in j,
[[lem:i-b-6-3]] holds with the limit symbols (its proof uses only their convergence in C_c^∞), and the dynamics
(D1)–(D3) of b_∞ give the contradiction. Quantising the symbols of the limit b_∞ instead would make [[eq:i-b-6-8]] exact
only up to o(1). Hence [[thm:i-b-1-3]] holds with constants uniform in b ∈ ℬ. As in [[sec:i-a-8]], (H5)–(H8) are not
verified in this chapter; for the operators of the stability theory they are verified in [[ch:s12]] and the chapters
that treat each operator.

**Remark {#rem:i-b-comparison}** (Comparison with [Hin26c, Section 9.3].) Besides the changes of statement in
[[rem:i-b-relation]], the following points differ from [Hin26c]. (a) [Hin26c, Theorem 9.28] states that B is
semiclassically elliptic "at ∂ℛ_+"; the estimate is at the trapped set, and B is elliptic at Γ ([[thm:i-b-6-8]]). (b)
In the proof of [Hin26c, (9.83)] a constant is fixed in (inf_Γ p_1/(2β_0), γ); positivity of −2p_1 + 4β_0γ_0 on Γ
needs γ_0 > sup_Γ p_1/(2β_0) = γ_+. [[prop:i-b-6-1]] avoids the constant by writing p − ℓq = (p − γq) − (ℓ − γ)q. (c)
[Hin26c, Theorem 9.28 (2)] states the adjoint estimate for z ∈ 1 + i[−hβ, ν]. For β < 0 that range misses the real
axis, which the adjoint estimate at Im z = 0 in [Hin26c, (9.59)] needs. The symbol calculus gives the same threshold for
P* as for P ([[sec:i-b-6-1]] defines p^♮ and q^♮ with the field of each, and [[eq:i-b-1-4]] reads the same), so the
range z_0 + i[hβ, ν′] of [[thm:i-b-6-8]] serves both. (d) The second step of the b-regular estimate at R_out in
[Hin26c, (9.77)] carries the diagonal term −2kihzρδ_(α,(k,0,…,0)) of [Hin26c, (9.45)], whose sign and index set differ
from those of the commutator computed in [[lem:i-a-4-8]] (there the diagonal term is +2iα_1σρ, for every α with
α_1 ≥ 1; see [[rem:i-a-4-8-sign]]); [[lem:i-b-5-6]] moves the term to the right side through Pu, as [[lem:i-a-4-8]] does at fixed
σ, and [[prop:i-b-5-7]] then needs no sign of it. (e) [Hin26c, (3.35)] defines H_(sc,h)^(s,𝗋,𝖻) = ρ^𝗋 h^𝖻 H_(sc,h)^s,
which gives ‖u‖ = h^(−𝖻)‖⟨hD⟩^s(⟨x⟩^𝗋 u)‖ on ℝ^n, while the parenthesis after it prints ⟨x⟩^(−𝗋)u; we use
w_𝐨 = ⟨ζ⟩^s⟨x⟩^𝗋h^(−𝖻), as (3.35) does. (f) The method differs in these points: one positive commutator scheme
without regularisation, a priori estimates being proved for Schwartz functions and extended by density
([[sec:i-b-3]]); propagation with flow boxes depending on z, the difference 𝖧_z − 𝖧_(Re z) absorbed by ℓ𝒬
([[prop:i-b-4-5]]), in place of the three regimes of [Hin26c, Propositions 9.19, 9.22, 9.23]; one radial lemma for all
three radial sets ([[lem:i-b-5-1]]); at R_out the large imaginary part written as W*M̃W − g_00, non-negative exactly
([[lem:i-b-5-4]]), which needs the remainder R_2 of [Hin26c, (9.49)] to be put into that form; matrix-valued defect
measures, entering through tr and max spec ([[lem:i-b-6-2]]); the complex absorption written as Q̂_♭(σ̄)*Q̂_♭(σ),
entire and of exact sign ([[sec:i-b-6-5]]); a three lines lemma with its proof ([[lem:i-b-6-6]]) in place of
[DZ19, Lemma D.1]; and the energy estimate at the artificial boundary for every Im z ≥ 0 through the weight e^(ℓr)
([[prop:i-b-7-1]]), in place of [Hin25a, Theorem 9.44] for bounded h⁻¹ Im z.
