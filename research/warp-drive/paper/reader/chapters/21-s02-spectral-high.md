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

*Notation.* Three letters that the edition reserves elsewhere are replaced in this chapter: the rank of the bundle is
N_E; the largest eigenvalue of an endomorphism A that is self-adjoint for a fibre inner product is written max spec A;
and ℓ denotes Im z/h, except in [[prop:i-b-7-1]], where ℓ is the exponent of the weight e^(ℓr). Large integers that
bound orders of Sobolev spaces are written M.

### Setting, hypotheses and the theorem {#sec:i-b-1}

#### Data from the bounded-frequency theory {#sec:i-b-1-1}

The space X̄ ⊂ ℝ̄⁴, the radii r_0, δ_0, r_2, r_h, the bundle E = X̃ × ℂ^(N_E), fibre inner products h = ⟨H·,·⟩ and
h-adjoints A^(*h) = H⁻¹A*H, and the family P̂(σ) = P̂(0) + σT + σ²P_2 are those of [[sec:i-a-1]], and (H1)–(H5) of
[[sec:i-a-1-3]] are assumed. The radii enter only through 0 < r_0 − 2δ_0 < r_0 < r_2 < r_h; no result below depends on
their values. We write ρ = |x|⁻¹ near ∂X, scattering covectors as ξ dr + r η, and use [[lem:i-a-4-4]]: at the boundary
face T has principal symbol 2ξ Id, and Im_h T = −ρ(S + S^(*h)) + T_2 with T_2 ∈ Ψ^(1,−2).

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
compactification near ∂X; its principal symbol, modulo S^(1,−1,−1), is G_z Id with G_z(x, ζ) := G(−z dt + ζ).

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
Im_h P̂(0) has order 1 (remark (a) on the hypotheses in [[sec:i-a-1-3]]).

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
stronger than (O2) of [[sec:i-a-1-4]], so 𝗋_h(x, ξ) := 𝗋(x, hξ) satisfies (O2)–(O3) of [[sec:i-a-1-4]] at
σ_0 = z_0/h ([[sec:i-b-8-4]]).

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
Γ_(u/s): a point of Γ_u ∖ Γ leaves O forward, so its curve is not contained in Γ_u.

(H5) is extended to (H6)–(H8): g, Γ, φ_(u/s), ν_(u/s) and h_Γ may depend continuously on the parameter b ∈ ℬ (into
C^∞), with ν_min, β_0, γ_± and the convergence in (H8) uniform. For the operators to which the stability theory applies
this chapter, (H6)–(H8) are verified in [[ch:s12]] and the chapters that treat each operator; they are not verified
here.

*Notation.* h is the semiclassical parameter; as an index (^(*h), Re_h, Im_h, h_Γ) it denotes a fibre inner product,
as in [[ch:s01]]. ℓ is Im z/h, except in [[prop:i-b-7-1]]. 𝖧_(z_0) = z_0 H_(G_(z_0)) in (H7) is the future field; the
field 𝖧_z of [[eq:i-b-4-1]] is a positive multiple of H_(G_z), and the future field is ς𝖧_z ([[rem:i-b-1-4]]).

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
is proved for Im(h⁻¹z) ≥ β > γ_−; at Im z = 0 this needs γ_− < 0, which holds in the applications of [Hin26c] and is
part of (H7) here.

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

The best constants with |α| + |β| ≤ k (and fixed exponents) are the seminorms. S^(−∞) := ⋂_K S^(−K𝟏). Note
h^K S^𝐨 = S^(𝐨−(0,0,K)).

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
|x^γ ∂_x^κ Op_h(a)u(x)| ≤ C_γκ ⟨x⟩^(sup 𝗋+|κ|) L_h(x, 0)^μ for some μ and every γ.

**Lemma {#lem:i-b-2-3}** (Oscillatory integrals.) Let F ∈ C^∞(ℝ^(2n)_(w,η); ℂ^(N_E×N_E)) satisfy
|∂_w^γ ∂_η^κ F| ≤ A_γκ ⟨w⟩^M ⟨η⟩^M. Fix χ ∈ C_c^∞(ℝ^n) with χ(0) = 1. Then

    I(F) := lim_(ϵ→0) (2π)^(−n) ∫∫ e^(−iw·η) χ(ϵw) χ(ϵη) F(w, η) dw dη

exists, does not depend on χ, and for 2k > M + n

    I(F) = (2π)^(−n) ∫∫ e^(−iw·η) ⟨η⟩^(−2k) (1 − Δ_w)^k [⟨w⟩^(−2k) (1 − Δ_η)^k F] dw dη,
    |I(F)| ≤ C_(n,M) max_(|γ|,|κ|≤2k) A_γκ.                                                             {#eq:i-b-2-2}

Moreover I(w^γ F) = I(D_η^γ F), and I(F) = F(·, 0) if F does not depend on w.

*Proof.* (1 − Δ_η) e^(−iw·η) = ⟨w⟩² e^(−iw·η) and (1 − Δ_w) e^(−iw·η) = ⟨η⟩² e^(−iw·η). Integrating by parts k times
in each variable in the regularised integral gives [[eq:i-b-2-2]] with F replaced by χ(ϵw)χ(ϵη)F; the derivatives
falling on the cut-offs are bounded for ϵ ≤ 1 and tend to 0 pointwise, and the integrand is dominated by
C⟨w⟩^(M−2k)⟨η⟩^(M−2k), which is integrable. Dominated convergence gives the limit and [[eq:i-b-2-2]]. The identity
w^γ e^(−iw·η) = (i∂_η)^γ e^(−iw·η) gives I(w^γ F) = I(D_η^γ F). If F = F(η), then
(2π)^(−n) ∫ e^(−iw·η) χ(ϵw) dw = ϵ^(−n) χ̌(η/ϵ) with ∫ χ̌ = χ(0) = 1, an approximate identity, so I(F) = F(0). ∎

**Theorem {#thm:i-b-2-4}** (Composition.) For a ∈ S^𝐨 and b ∈ S^(𝐨′), Op_h(a) Op_h(b) = Op_h(a#b) with

    a#b(x, ζ) = I(F_(x,ζ)),     F_(x,ζ)(w, η) := a_h(x, ζ + η) b_h(x + hw, ζ).                          {#eq:i-b-2-3}

a#b ∈ S^(𝐨+𝐨′), and for every K ≥ 1

    a#b − Σ_(|α|<K) (h^(|α|)/α!) ∂_ζ^α a D_x^α b ∈ S^(𝐨+𝐨′−(K/2)𝟏).                                      {#eq:i-b-2-4}

Each seminorm of a#b and of the remainder is bounded by a product of seminorms of a and b. The term with α lies in
S^(𝐨+𝐨′−|α|𝟏+ϵ𝟏) for every ϵ > 0.

*Proof.* The kernel of Op_h(a) Op_h(b) is (2πh)^(−2n) ∫ e^(i(x−y)·ζ′/h + i(y−x′)·ζ/h) a(x, ζ′) b(y, ζ) dy dζ′ dζ.
Writing e^(i(y−x′)·ζ/h) = e^(i(x−x′)·ζ/h) e^(−i(x−y)·ζ/h), it is the kernel of Op_h(c) with
c(x, ζ) = (2πh)^(−n) ∫∫ e^(i(x−y)·(ζ′−ζ)/h) a(x, ζ′) b(y, ζ) dy dζ′, and ζ′ = ζ + η, y = x + hw (so
dy dζ′ = h^n dw dη) give [[eq:i-b-2-3]]. On u ∈ 𝒮 the manipulations are justified by inserting χ(ϵw)χ(ϵη) and
letting ϵ → 0.

*The expansion.* By Taylor's formula,

    b(x + hw, ζ) = Σ_(|α|<K) ((hw)^α/α!) ∂_x^α b(x, ζ)
                   + K Σ_(|α|=K) ((hw)^α/α!) ∫_0^1 (1 − t)^(K−1) ∂_x^α b(x + thw, ζ) dt.

[[lem:i-b-2-3]] gives I(w^α a(x, ζ + η) ∂_x^α b(x, ζ)) = (D_ζ^α a)(x, ζ) ∂_x^α b(x, ζ), and
D_ζ^α a ∂_x^α b = ∂_ζ^α a D_x^α b: these are the terms of [[eq:i-b-2-4]]. The remainder is
R_K = K Σ_(|α|=K) (h^K/α!) ∫_0^1 (1 − t)^(K−1) I(G_(α,t)) dt with
G_(α,t)(w, η) := (D_ζ^α a)(x, ζ + η) (∂_x^α b)(x + thw, ζ).

*The remainder, with constant orders.* Let 𝐨_+, 𝐨′_+ be the componentwise suprema. Since
⟨x + y⟩^t ≤ 2^(|t|/2) ⟨x⟩^t ⟨y⟩^(|t|) (Peetre's inequality) and L_h(x + y, ζ + η) ≤ L_h(x, ζ) ⟨y⟩ ⟨η⟩, and using
(th)^(|γ|) ≤ 1, ⟨x + thw⟩^(−|γ|) ≤ 1 and ⟨ζ + η⟩^(−|κ|) ≤ 1, for |γ|, |κ| ≤ 2k

    |∂_w^γ ∂_η^κ G_(α,t)| ≤ C w_(𝐨_++𝐨′_+)(x, ζ) ⟨x⟩^(−K) ⟨ζ⟩^(−K) L_h(x, ζ)^μ ⟨w⟩^M ⟨η⟩^M,
    M := |𝗋′_+ − K| + |s_+ − K| + μ + 1,

with μ depending on K and k. By [[eq:i-b-2-2]] with 2k > M + n, |I(G_(α,t))| obeys the same bound without the last two
factors. A derivative of R_K in x or ζ falls on a or b inside I; it gains ⟨x⟩⁻¹ or ⟨ζ⟩⁻¹ up to a factor
L_h⟨w⟩⟨η⟩, which [[eq:i-b-2-2]] absorbs with a larger k. So R_K ∈ S^(𝐨_++𝐨′_+−K𝟏+ϵ𝟏) for every ϵ > 0, the factor
h^K being the gain in the semiclassical order.

*Variable orders.* Let ω be the sum over the three components of sup 𝐨 + sup 𝐨′ − inf(𝐨 + 𝐨′). For K ≥ 2ω + 2,
𝐨_+ + 𝐨′_+ − K𝟏 + ϵ𝟏 ≤ 𝐨 + 𝐨′ − (K/2)𝟏 pointwise, so R_K ∈ S^(𝐨+𝐨′−(K/2)𝟏) by [[lem:i-b-2-2]] (c). The terms
with |α| < K lie in S^(𝐨+𝐨′−|α|𝟏+ϵ𝟏) by [[lem:i-b-2-2]] (b), (d). Applying this with K′ := max(K, 2ω + 2) and moving
the terms with K ≤ |α| < K′ into the remainder gives [[eq:i-b-2-4]] for every K, and a#b ∈ S^(𝐨+𝐨′). ∎

**Theorem {#thm:i-b-2-5}** (Adjoints.) For a ∈ S^𝐨, the formal adjoint in L²(ℝ^n; ℂ^(N_E)) is Op_h(a)* = Op_h(a^♮)
with a^♮(x, ζ) = I(a_h(x + hw, ζ + η)*), and a^♮ − Σ_(|α|<K) (h^(|α|)/α!) ∂_ζ^α D_x^α a* ∈ S^(𝐨−(K/2)𝟏).

*Proof.* The kernel of Op_h(a)* is (2πh)^(−n) ∫ e^(i(x−x′)·ζ/h) a(x′, ζ)* dζ, the kernel of Op_h(c) with
c(x, ζ′) = (2πh)^(−n) ∫∫ e^(iy·(ζ−ζ′)/h) a(x − y, ζ)* dy dζ; substitute ζ = ζ′ + η, y = −hw. The expansion follows
as in [[thm:i-b-2-4]]. ∎

*Consequences.* (i) Op_h is injective on symbols (the symbol is a partial Fourier transform of the kernel).

(ii) For a ∈ S^𝐨, b ∈ S^(𝐨′) and every ϵ > 0,

    (i/h)[Op_h(a), Op_h(b)] − Op_h((i/h)(ab − ba) + {a, b}) ∈ Ψ^(𝐨+𝐨′−(2,2,1)+ϵ𝟏),                       {#eq:i-b-2-5}

with {a, b} := Σ_j (∂_(ζ_j)a ∂_(x_j)b − ∂_(ζ_j)b ∂_(x_j)a) (products in the written order). If a = p Id is scalar, the
symbol is H_p b, H_p := ∂_ζ p · ∂_x − ∂_x p · ∂_ζ. If a is scalar only modulo S^(𝐨−𝟏), the left side of
[[eq:i-b-2-5]] is still in Ψ^(𝐨+𝐨′−(1,1,0)+ϵ𝟏).

(iii) If Op_h(a) is self-adjoint, then a − a* ∈ S^(𝐨−𝟏+ϵ𝟏).

(iv) If a vanishes on an open set U, then a#b and b#a, restricted to any open U′ with closure in U, obey the bounds of
S^(−K𝟏) for every K: every term of [[eq:i-b-2-4]] vanishes there, and the remainder lies in S^(𝐨+𝐨′−(K/2)𝟏) for every
K.

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

*Proof.* Put M := sup |a|² + ϵ² and e := M − a*a ≥ ϵ², a Hermitian symbol in S^0. Its positive square root
b_0 := e^(1/2) = (2πi)⁻¹ ∮_𝒞 κ^(1/2) (κ − e)⁻¹ dκ, with 𝒞 a circle in {Re κ > 0} around [ϵ², M], lies in S^0
(differentiate under the integral; each derivative of (κ − e)⁻¹ is a sum of products of resolvents and derivatives of
e), as does b_0⁻¹. By [[thm:i-b-2-4]] and [[thm:i-b-2-5]],
Op_h(b_0)* Op_h(b_0) + Op_h(a)* Op_h(a) = M + Op_h(r_1) with r_1 ∈ S^(−½𝟏) and Op_h(r_1) self-adjoint. Given
b_0 + ⋯ + b_(j−1) with self-adjoint remainder Op_h(r_j), r_j ∈ S^(−(j/2)𝟏), put b_j := −¼ b_0⁻¹ (r_j + r_j*); then
b_0* b_j + b_j* b_0 = −½(r_j + r_j*) and, by (iii) and [[thm:i-b-2-4]], the new remainder lies in
S^(−((j+1)/2)𝟏+ϵ𝟏) (we absorb the ϵ by taking two steps per half order). With J := 4n + 8 and
B := Op_h(b_0 + ⋯ + b_J),

    ‖Op_h(a)u‖² = M‖u‖² − ‖Bu‖² + ⟨Op_h(r_(J+1))u, u⟩ ≤ (M + C h^(1/2)) ‖u‖²

by [[lem:i-b-2-6]] with β = −½, since r_(J+1) ∈ S^(−(n+1)𝟏) ⊂ S^((−n−1,−1,−½)). Take square roots. ∎

*Sobolev spaces.* For orders 𝐨 let W_𝐨 := Op_h(w_𝐨 Id). By [[lem:i-b-2-2]] and [[thm:i-b-2-4]],
Op_h(w_(−𝐨)) W_𝐨 = I + Op_h(e) and W_𝐨 Op_h(w_(−𝐨)) = I + Op_h(e′) with e, e′ ∈ S^(−½𝟏), so by [[thm:i-b-2-7]] there
is h_0 > 0 such that for h < h_0 both are invertible on L² with inverses bounded uniformly. For h < h_0 define
H_h^𝐨 := {u ∈ 𝒮′ : W_𝐨 u ∈ L²}, ‖u‖_𝐨 := ‖W_𝐨 u‖_(L²). For constant orders H_h^𝐨 = h^𝖻 ⟨x⟩^(−𝗋) ⟨hD⟩^(−s) L²
with uniformly equivalent norm. For each fixed h, H_h^𝐨 is the scattering Sobolev space of [HJS, Definition 10.2] with
the decay order 𝗋(x, hζ) and the constant regularity order s, with a norm equivalent for that h: h^(−𝖻(x,hζ)) is a
symbol of order 0 at fixed h. This is how the fixed-frequency results of [[ch:s01]] are used.

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
which a obeys the bounds of S^(−K𝟏) for every K; it is in Ell_h(A) if it has a neighbourhood U and h_0 > 0 with a_h
invertible and |a_h⁻¹| ≤ C w_𝐨⁻¹ on U ∩ ℝ^(2n) for h < h_0.

By (iv), WF′_h(AB) ⊂ WF′_h(A) ∩ WF′_h(B). Ellipticity at ϖ depends only on a modulo symbols that are small compared
with w_𝐨 near ϖ: modulo S^(𝐨−(0,0,½)) anywhere (for small h), modulo S^(𝐨−(0,½,0)) near the face over spatial
infinity, and modulo S^(𝐨−(½,0,0)) near fibre infinity. The *principal symbol* of A ∈ Ψ^𝐨 is its symbol modulo
S^(𝐨−𝟏+ϵ𝟏) for small ϵ > 0; by [[eq:i-b-2-4]] it is multiplicative.

**Proposition {#prop:i-b-2-10}** (Microlocal elliptic estimate.) Let A ∈ Ψ^𝐦 and B, G ∈ Ψ^0 with
WF′_h(B) ⊂ Ell_h(A) ∩ Ell_h(G). Then for all orders 𝐨 and all K, ‖Bu‖_𝐨 ≤ C(‖GAu‖_(𝐨−𝐦) + ‖u‖_(−K𝟏)).

*Proof.* Let φ ∈ S^0 equal 1 near WF′_h(B), supported where a and g are uniformly invertible. Then
q_0 := φ a⁻¹ g⁻¹ ∈ S^(−𝐦) by [[lem:i-b-2-2]] (e), and Op_h(q_0) G A = Op_h(φ) + Op_h(r) with r ∈ S^(−½𝟏) near
WF′_h(B). Corrections q_j ∈ S^(−𝐦−(j/2)𝟏) supported in supp φ remove the error to any order: QGA = Op_h(φ) + R with
R ∈ S^(−K𝟏) near WF′_h(B). Then B = BQGA − BR + B(I − Op_h(φ)), the last term in Ψ^(−K𝟏) by (iv), and
[[prop:i-b-2-8]] bounds the rest. ∎

**Lemma {#lem:i-b-2-11}** (Positivity.) Let A = A* ∈ Ψ^(2𝐦) with principal symbol 𝖺, and B ∈ Ψ^0. Suppose
𝖺 ≥ c w_𝐦² Id, c > 0, on a neighbourhood of WF′_h(B). Then for all K and small ϵ > 0,
⟨ABu, Bu⟩ ≥ (c/2) ‖Bu‖²_𝐦 − C ‖Bu‖²_(𝐦−½(1−ϵ)𝟏) − C ‖u‖²_(−K𝟏).

*Proof.* Let 𝖺̃ ∈ S^(2𝐦) be Hermitian, equal to 𝖺 near WF′_h(B) and ≥ ¾ c w_𝐦² everywhere. Put
q := w_𝐦 (w_𝐦^(−2) 𝖺̃ − c/2)^(1/2) ∈ S^𝐦 (positive square root, as in [[thm:i-b-2-7]]). Then
A = Op_h(q)* Op_h(q) + (c/2) W_𝐦* W_𝐦 + E with E ∈ Ψ^(2𝐦−(1−ϵ)𝟏) near WF′_h(B), so
⟨ABu, Bu⟩ ≥ (c/2) ‖Bu‖²_𝐦 + ⟨EBu, Bu⟩, and [[prop:i-b-2-8]] bounds the last term. ∎

**Lemma {#lem:i-b-2-12}** (Square roots with logarithmic growth.) Let Q_0 ∈ S^0 be Hermitian with Q_0 ≥ M Id, M > 0,
and let κ ≥ 0 be a real scalar function with κ ≤ C L_h and
|∂_x^α ∂_ζ^β κ| ≤ C_αβ ⟨x⟩^(−|α|) ⟨ζ⟩^(−|β|) L_h^(μ_αβ) for (α, β) ≠ 0. Let Q := Q_0 + κ Id. Then Q^(1/2) ∈ S^(ϵ𝟏)
for every ϵ > 0 and Q^(−1/2) ∈ S^0. If b := w_𝐨 φ Q^(1/2) with φ ∈ S^0 scalar, then b ∈ S^(𝐨+ϵ𝟏) for every ϵ, and
wherever φ ≥ c > 0 on an open set U, φ′ b⁻¹ ∈ S^(−𝐨) for φ′ ∈ S^0 supported in U; [[prop:i-b-2-10]] then holds with
A := Op_h(b), at the order 𝐨, on U.

*Proof.* Q = (1 + κ) Q̃ with Q̃ := (Q_0 + κ)/(1 + κ), whose values lie in [min(M, 1), max(sup |Q_0|, 1)] and whose
derivatives obey [[eq:i-b-2-1]] with order 0. So Q̃^(±1/2) ∈ S^0 by the Cauchy formula of the proof of
[[thm:i-b-2-7]] over a fixed contour. (1 + κ)^(1/2) ≤ C L_h^(1/2) ≤ C_ϵ w_(ϵ𝟏), and its derivatives
½(1 + κ)^(−1/2) ∂κ and higher obey [[eq:i-b-2-1]]; (1 + κ)^(−1/2) ≤ 1 likewise. This gives the first two claims, and
b⁻¹ = w_(−𝐨) φ⁻¹ Q^(−1/2) on U. In the proof of [[prop:i-b-2-10]] with q_0 := φ′ b⁻¹ ∈ S^(−𝐨), q_0#b − φ′ lies in
S^(−½𝟏) near supp φ′, since each term of [[eq:i-b-2-4]] with |α| ≥ 1 gains |α|𝟏 up to logarithms and the
logarithmic growth of b is one factor L_h^(1/2); the iteration is unchanged. ∎
