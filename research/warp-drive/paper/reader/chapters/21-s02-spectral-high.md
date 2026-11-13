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

*Proof.* At fixed h, H_h^𝐨 is the space H_sc^(s,𝗋_h) of [HJS] with 𝗋_h(x, ξ) := 𝗋(x, hξ), with an equivalent norm
([[sec:i-b-2-3]]), and P_(h,z) = h² P̂(z/h) ∈ Ψ_sc^(2,0). With T_t from (C8) of [[sec:i-a-2-1]], T_t u → u in H_h^𝐨,
and P_(h,z) T_t u = T_t P_(h,z) u + [P_(h,z), T_t] u. Here T_t P_(h,z) u → P_(h,z) u, and [P_(h,z), T_t] is bounded
in Ψ_sc^(1,−1) and tends to 0 in Ψ_sc^(1+δ,−1+δ) for every δ > 0 ([[lem:i-a-2-1]] (c) and (C8) of [[sec:i-a-2-1]]).
So it is uniformly bounded from H^(s,𝗋_h) to H^(s−1,𝗋_h+1) and tends to 0 on the dense subspace H^(s+δ,𝗋_h+δ), hence
strongly. T_t u is Schwartz. For the b-regular norms, [⟨x⟩D_x, T_t] is likewise bounded in Ψ_sc^(0,0) and tends to 0
strongly. ∎

Every term of the estimates below (‖Bu‖_𝐨, h⁻¹‖G P_(h,z) u‖_(𝐨−𝐦+(1,1,0)), ‖Eu‖_𝐨, ‖u‖_(−K𝟏), with B, G, E ∈ Ψ^0) is
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

where: B ∈ Ψ^𝐨 and Ǎ = ZB + Y with Z ∈ Ψ^(−½(𝐦−(1,1,0))), Y ∈ Ψ^(𝐤−½𝟏); ⟨Fw, w⟩_h ≥ −C_F‖w‖²_(−K𝟏) for Schwartz
w; E ∈ Ψ^𝐨 is microsupported in a closed set K_E; J ∈ Ψ^(2𝐨−𝐦) with WF′_h(J) ⊂ Ell_h(P); R ∈ Ψ^(2𝐨−½𝟏); and
Ǎ, B, E, J, R are microsupported in K_1. Let E′ ∈ Ψ^0 be elliptic on K_E. Then for Schwartz u and h < h_0,

    ‖Bu‖² ≤ C(h⁻² ‖GPu‖²_(𝐨−𝐦+(1,1,0)) + ‖E′u‖²_𝐨 + ‖Gu‖²_(𝐨−¼𝟏) + ‖u‖²_(−K𝟏)).                      {#eq:i-b-3-4}

C depends on C_F and on seminorms of the operators involved.

*Proof.* By [[eq:i-b-3-1]] and [[eq:i-b-3-3]],
‖Bu‖² = −ς(2/h) Im⟨ǍPu, Ǎu⟩ − ⟨Fu, u⟩ + ‖Eu‖² + ⟨JPu, u⟩ + ⟨Ru, u⟩. Microlocalise first: let Φ ∈ Ψ^0 be
microlocally the identity near K_1, with WF′_h(Φ) ⊂ Ell_h(G); then Ǎ(I − Φ) and (I − Φ)^(*h)Ǎ are residual, and
‖Φf‖_𝐭 ≤ C(‖Gf‖_𝐭 + ‖f‖_(−K𝟏)) by [[prop:i-b-2-10]].

(a) ⟨ǍPu, Ǎu⟩ = ⟨Z^(*h)ǍPu, Bu⟩ + ⟨ǍPu, Yu⟩, and Z^(*h)Ǎ ∈ Ψ^(𝐨−𝐦+(1,1,0)), Ǎ maps H^(𝐨−𝐦+(1,1,0)) to
H^(−½(𝐦−(1,1,0))), and Y maps H^(𝐨−½𝟏) to H^(½(𝐦−(1,1,0))). So
(2/h)|⟨ǍPu, Ǎu⟩| ≤ ½‖Bu‖² + C h⁻² ‖GPu‖²_(𝐨−𝐦+(1,1,0)) + C ‖Gu‖²_(𝐨−½𝟏) + C ‖u‖²_(−K𝟏).

(b) −⟨Fu, u⟩ ≤ C_F ‖u‖²_(−K𝟏).

(c) ‖Eu‖ ≤ C(‖E′u‖_𝐨 + ‖u‖_(−K𝟏)) by [[prop:i-b-2-10]].

(d) Let Φ_J ∈ Ψ^0 be microlocally the identity near WF′_h(J) with WF′_h(Φ_J) ⊂ Ell_h(P) ∩ Ell_h(G); then
⟨JPu, u⟩ = ⟨JPu, Φ_J u⟩ + O(‖u‖²_(−K𝟏) + ‖GPu‖²), ‖JPu‖_(−𝐨) ≤ C(‖GPu‖_(𝐨−𝐦) + ‖u‖_(−K𝟏)), and
‖Φ_J u‖_𝐨 ≤ C(‖GPu‖_(𝐨−𝐦) + ‖u‖_(−K𝟏)) by [[prop:i-b-2-10]]; and
‖GPu‖_(𝐨−𝐦) ≤ ‖GPu‖_(𝐨−𝐦+(1,1,0)) ≤ h⁻¹ ‖GPu‖_(𝐨−𝐦+(1,1,0)).

(e) |⟨Ru, u⟩| ≤ C ‖Gu‖²_(𝐨−¼𝟏) + C ‖u‖²_(−K𝟏).

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

    ‖B_* u‖_𝐨 ≤ C(h⁻¹ ‖GPu‖_(𝐨−𝐦+(1,1,0)) + ‖E′u‖_𝐨 + h^M ‖Gu‖_𝐨 + ‖u‖_(−K𝟏)).                       {#eq:i-b-3-5}

*Proof.* Let J := 4M. Choose U_0 ⊃ U_1 ⊃ ⋯ ⊃ U_J ⊃ Λ, U_j the U′ of the hypothesis for U_(j−1), with B^(j) elliptic on
Ū_j and K_E^* := ⋃_j K_E(U_(j−1)). Let G_0 := G and, for j ≥ 1, G_j ∈ Ψ^0 elliptic on Ū_j with
WF′_h(G_j) ⊂ Ell_h(B^(j)), so that ‖G_j u‖_𝐭 ≤ C(‖B^(j)u‖_(𝐭−𝐨) + ‖u‖_(−K𝟏)) (with B^(j) at the shifted order). Apply
[[lem:i-b-3-3]] at the order 𝐨 − (0, 0, (J − j)/4) with (U_(j−1), G_(j−1)), using the scaling above:

    ‖G_j u‖_(𝐨−(0,0,(J−j)/4)) ≤ C(h⁻¹ ‖GPu‖_(𝐨−𝐦+(1,1,0)) + ‖E′u‖_𝐨 + ‖G_(j−1) u‖_(𝐨−(0,0,(J−j+1)/4))
                                 + ‖u‖_(−K𝟏)).

Chaining from j = J down to j = 1 leaves ‖G_0 u‖_(𝐨−(0,0,J/4)) = h^M ‖Gu‖_𝐨. Take U_* := U_J and use
‖B_* u‖_𝐨 ≤ C(‖G_J u‖_𝐨 + ‖u‖_(−K𝟏)). ∎

*Positivity of absorbing terms.* Suppose h⁻¹ Im_h P contains −ℓ𝒜 with ℓ ≥ 0 a constant, ℓ ≤ C h⁻¹, and 𝒜 = 𝒜^(*h)
such that ς𝒜 ∈ Ψ^(2𝐭) has principal symbol ≥ c w_𝐭² on a neighbourhood of WF′_h(Ǎ), for some order 𝐭. Then ςC
contains −ℓς(Ǎ²𝒜 + 𝒜Ǎ²) = −F − ℓς[[𝒜, Ǎ], Ǎ] with F := 2ℓǍ(ς𝒜)Ǎ. The double commutator lies in
ℓΨ^(2𝐤+2𝐭−2𝟏), which for the orders below is in the class of R. And F satisfies the hypothesis of [[lem:i-b-3-3]]:
[[lem:i-b-2-11]], whose proof does not use the order of B, gives
⟨ς𝒜Ǎw, Ǎw⟩ ≥ (c/2) ‖Ǎw‖²_𝐭 − C ‖Ǎw‖²_(𝐭−½(1−ϵ)𝟏) − C ‖w‖²_(−K𝟏), and the middle term is at most
C h^(1−ϵ) ‖Ǎw‖²_𝐭, which the first absorbs for h small. So ⟨Fw, w⟩ ≥ −Cℓ ‖w‖²_(−K𝟏) ≥ −C ‖w‖²_(−(K−1)𝟏). This is
[Hin26c, (9.69)].

In [[lem:i-b-3-3]] we also allow B ∈ ⋂_ϵ Ψ^(𝐨+ϵ𝟏) of the form of [[lem:i-b-2-12]] (a variable order contributes a
factor (1 + κ)^(1/2) with κ logarithmic); the proof is unchanged, and [[lem:i-b-2-12]] gives
‖B_* u‖_𝐨 ≤ C(‖Bu‖ + ‖u‖_(−K𝟏)) for B_* microsupported where the cut-offs of B equal 1, which is what [[lem:i-b-3-4]]
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

**Proposition {#prop:i-b-4-2}** Let K ⊂ 𝒫 be compact with Ĝ_z ≠ 0 on K for every z ∈ Z, and B, G ∈ Ψ^0 with
WF′_h(B) ⊂ K and G elliptic on K. Then for all orders 𝐨 and all K′, uniformly for z ∈ Z and h < h_0,

    ‖Bu‖_𝐨 ≤ C(‖GPu‖_(𝐨−𝐦) + ‖u‖_(−K′𝟏)) ≤ C(‖GPu‖_(𝐨−𝐦+(1,1,0)) + ‖u‖_(−K′𝟏)).                         {#eq:i-b-4-2}

The same holds for P^(*h).

*Proof.* By compactness of K × Z there are a neighbourhood U of K and c > 0 with |Ĝ_z| ≥ c on U for z ∈ Z. Since
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
on Ū_0, all M, K, z ∈ Z_0, h < h_0 and Schwartz u,

    ‖B_* u‖_𝐨 ≤ C(h⁻¹ ‖G P_(ϵ_♭) u‖_(𝐨−𝐦+(1,1,0)) + ‖E′u‖_𝐨 + h^M ‖Gu‖_𝐨 + ‖u‖_(−K𝟏)).                  {#eq:i-b-4-5}

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
[[lem:i-b-2-12]] (with κ := κ_0 and M := M_1). With

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
[[sec:i-b-3-3]], with 𝐭 = (½, 0, 0), ⟨Fw, w⟩ ≥ −C‖w‖²_(−K𝟏), and the double commutator lies in
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
