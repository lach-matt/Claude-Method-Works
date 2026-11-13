## The boost parameter, almost boundedness and the extraction of parameters {#ch:s20}

This chapter studies forward solutions of the linearised gauge-fixed Einstein operator at a base point near the
Schwarzschild–Tangherlini parameter b₀, for sources with more than one order of decay at K⁺, and reads off from them
the parameters of the linearised Myers–Perry family. It has three steps. First ([[prop:iii-i3-2-1]]), for sources of
K⁺-weight α_K ∈ (1, 3/2) the forward solution is a cut-off generalised zero energy state of the boosts,
χ^H_K h^(≤1)_b(Ṡ), plus a remainder of K⁺-weight α_K − 2 > −1; the vector Ṡ ∈ 𝒮_1 is the *boost parameter* of the
solution. Second ([[sec:iii-i4-1]]–[[sec:iii-i4-4]]), a correction term added to the operator lets a right-hand side
generate the boost term, and the map from the parameter of that term to the boost parameter of the forward solution is
invertible ([[prop:iii-i4-4-1]], [[prop:iii-i15-2-8]]); so a forward solution with no boost term, growing at most like
t_*^(2−α_K) = o(t_*) in compact spatial sets, can be found ([[cor:iii-i4-4-3]]). Third, once the boost term is
eliminated, the forward solution has K⁺-weight α_K − 2 for every α_K < 2 ([[prop:iii-i5-2-1]]); and for sources with
a little more than t_*^(−2) decay at K⁺ it is a cut-off linearised Myers–Perry metric, plus a cut-off constant
centre-of-mass shift, plus a remainder that decays at K⁺ ([[prop:iii-i6-2-1]]). These are [Hin26, Proposition 11.20,
Proposition 11.30, (11.95), Proposition 11.32, Proposition 11.34] in dimension 4 + 1.

The scheme is that of [Hin26]. The dimension changes it in five places. The states decay one order faster, and the
correction terms carry no logarithm, so nothing has to be cancelled at ι⁺. The formal solution at null infinity has
ι⁺-exponents beginning at λ_♯ := 3/2 + (1 − e_Υ)γ_Υ, not at 1, so the step that removes a t_*^(−3) term at ι⁺ is not
needed below α_K = 3/2, and later it removes finitely many terms with no pole. The zero energy window is (0, 1), as
no indicial root of L̂_b(0) has real part in (0, 1]. The remainders keep the ι⁺-weight min(α_+, 3/2, min Re ℰ_+) − ε
in place of 1 − ε; the cap 3/2 is the transport of the radiation order from 𝓘⁺. And there is no logarithmic
centre-of-mass motion: the motions that the exponents at ι⁺ create decay at K⁺.

The chapter is written at a general base point b near b₀. The operator is taken at b and the corrections are tensors
built from b₀-objects. The one identity that is exact only at b₀, the boost identity [[lem:iii-i4-2-4]], acquires an
error at b ([[lem:iii-i15-2-7]]), and the invertibility of the boost parameter map is proved at b by a direct bound
([[prop:iii-i15-2-8]]).

### The setting at a base point {#sec:s20-setting}

The notation is that of [[ch:s11]]–[[ch:s19]]; n = 4 throughout. The black hole parameters are b = (m, A), with
tangent space 𝔟 := ℝ ⊕ 𝔰𝔬(4), and b₀ = (m₀, 0); R₁ = m₀^(1/2). ℬ_* is the open ball about b₀ fixed in
[[sec:iii-h2-0]], with ℬ̄_* ⊂ ℬ_1. It is shrunk finitely many times below, each time to a smaller ball about b₀. 𝒮_1
is the space of the s1 parameters: S = S_w ∈ 𝒮_1 has |x|S = w · x with w ∈ ℝ⁴, so 𝒮_1 ≅ ℝ⁴.

*Spaces.* M, Ω_* = cl_M{t^♭_* ≥ 1}, the faces 𝓘⁺, ι⁺, K⁺ with their defining functions ρ_I, ρ_+, ρ_K, and the
unweighted b-density μ_b are those of [[sec:iii-i-1]]. Weights and index sets are listed at (𝓘⁺, ι⁺, K⁺); a single
number at a face is a plain weight there. H^(k,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_+,ℓ_+),ℓ_K)_b(Ω_*) and the spaces of
right-hand sides H^(k,(⟨ℰ^C_I+1⟩′,ℓ_I+1),(ℰ_++2,ℓ_++2),ℓ_K)_b(Ω_*) are those of [[def:iii-i-1-1]], with the
index sets ℰ_+ and ℰ^C_I there; the superscript (•, −) marks distributions supported in {t^♭_* ≥ 1} and extendible
at the artificial boundary. ℰ^tot_I, π_1 and the other index sets of [[ch:s17]] keep their meaning. The class of
perturbations is 𝒳^k of [[eq:iii-i-1-4]], with parameters a_I > 3/2, a_+ > 1, a_K > 2, and

    m_+ := min(a_+, min Re ℰ_+).

The constants γ_Υ, e_Υ, the set σ_Υ and ℓ_I^max are those of [[ch:s19]] and [[sec:iii-i1-1]], and

    λ_♯ := 3/2 + (1 − e_Υ)γ_Υ

is the exceptional exponent of [[prop:iii-i1-3-1]]; as 0 < γ_Υ < 1/4 ([[eq:iii-c-1-1]]), λ_♯ ∈ (3/2, 7/4). On the
spectral side, M′, Ω_− := cl_(M′){t_* ≤ 1}, Ω_<, the faces I, ι = ι⁺ ∪ ι⁻ and K = K⁺ ∪ K⁻ of M′, X̄ = {r ≥ r_0} and
the spaces on M′ are those of [[sec:iii-i2-1]]; H̄ denotes restrictions. X^±_(sc-b) over ±[0, c] is the space of
[[sec:ii-g1-3-1]], with faces scf, tf, zf, weights listed in that order and the defining functions [[eq:ii-g1-3-2]];
ρ = ⟨x⟩⁻¹, μ_X = |dx|/⟨x⟩⁴, r̂ := |σ|⟨x⟩, and χ_zf := χ_1(r̂) is the cut-off of [[sec:ii-g1-3-1]], equal to 1 for
r̂ ≤ 1/8 and to 0 for r̂ ≥ 1/4. ℱ is the Fourier transform in t_*, under which ∂_(t_*) becomes −iσ. The
inner radius r_0 of the artificial boundary {r = r_0}, at which every space is extendible, is a parameter of the
setting ([[ch:s12]]); no step of this chapter uses its value.

*The operator at the base point.* A base point is a pair (h, S), with S ∈ 𝒮_1 small and h ∈ 𝒳^∞ small in 𝒳^d,
together with a black hole parameter b ∈ ℬ̄_*. Its background is

    g_(b₀,b,−S) = (1 − χ_K)φ*_(−S) g_(b₀) + χ_K g_b

of [[eq:iii-i-1-1]], equal to g_b near K⁺, and its operator is L^(g,g_0), g_0 := g_(b₀,b,−S), g := g_0 + h, where
L^(g,g_0) := D_1P(·, g_0) at g is the linearised gauge-fixed Einstein operator of [[ch:s11]]. L_b := L^(g_b,g_b) is the
stationary model at b, and L̂_b(σ) = L_0 − iσL_1 − σ²L_2 its spectral family ([[sec:iii-h-1]]). The following
properties of the base point are used.

(B1) [[lem:iii-i-3-6]], [[prop:iii-i-3-4]], [[prop:iii-i-4-1]] and [[cor:iii-i-5-2]] are stated for the background
g_(b₀,b,−S) with |b − b₀| and |S| small: g_(b₀,b,−S) − g_b lies in the class of h, vanishes near K⁺, and
L^(g,g_0) − L_b gains a_K at K⁺. [[thm:iii-i-5-3]] holds at every b ∈ ℬ̄_*, with constants uniform in b and with
continuity in (b, S, h) ([[cor:iii-h2-5-1]]).

(B2) The models do not depend on b. N_ι⁺(2L_b) = N_ι⁺(2L̄) ([[lem:iii-h2-3-2]]), so the ι⁺-spectrum and
[[thm:iii-g1-3-1]] are those at b₀, and [[thm:iii-g2-4-2]] and [[cor:iii-g2-4-3]] hold at b with the K⁺-towers of L_b.
The tf-normal operator does not depend on b ([[lem:iii-g4-1-1]]). The indicial roots of L̂_b(0) do not depend on b,
the normal operator of L̂_b(0) at ∂X̄ being that of 2L̄ ([[lem:iii-f-2-1]] (3)); by [[prop:iii-f1-2-3]] (a) none of
them has real part in (0, 1], so (0, 1) lies in the indicial gap of L̂_b(0) for μ_b.

(B3) The states at b are those of [[sec:iii-h-1]]: for ḃ ∈ 𝔟 and S ∈ 𝒮_1, ġ_b(ḃ) is the gauge-corrected linearised
metric of [[eq:iii-f3-2-1]], h_b(S) := h_(b,s1)(S) = δ*_(g_b) ω^(0)_(b,s1)(S) and h̆_b(S) := h̆¹_(b,s1)(S), with the
1-forms ω^(0)_(b,s1)(S), ω̆^((0),1)_(b,s1)(S) of [[prop:iii-d2-3-1]]. They are stationary, linear in their arguments,
real on real arguments and smooth in b; their index sets at ∂X̄ are those at b₀, with ℰ_ind independent of b:
ġ_b(ḃ) ∈ 𝒜², h_b(S) ∈ 𝒜^((3,0)∪(3+ℰ_ind)), h̆_b(S) ∈ 𝒜^((2,0)∪(2+ℰ_ind)). Their seminorms in 𝒜^(q−δ) are bounded
uniformly in b for every δ > 0 ([[rem:iii-h-2-6]]), a loss absorbed below, where every weight is used with room. The
generalised state of the boosts

    h^(≤1)_b(S) := t_* h_b(S) + h̆_b(S) = δ*_(g_b)(t_* ω^(0)_(b,s1)(S) + ω̆^((0),1)_(b,s1)(S))

lies in the kernels of D_(g_b)Ric and of δ_(g_b,E_Υ)G_(g_b) ([[prop:iii-d2-3-1]] (2)), so L_b h^(≤1)_b(S) = 0; and
L_b ġ_b(ḃ) = 0. These results use the dynamical hypotheses (Dyn) of [[ch:s13]], which hold for b near b₀
([[ch:s12]]).

(B4) The results of [[ch:s18]] that we use — [[def:iii-h-2-1]], [[def:iii-h-3-1]], [[lem:iii-h-2-2]]–[[lem:iii-h-2-5]],
[[prop:iii-h-3-2]], [[thm:iii-h-4-1]] and [[cor:iii-h-4-2]]–[[cor:iii-h-4-4]] — are stated for b near b₀ and hold on
ℬ̄_* with constants uniform in b, by [[thm:iii-h2-2-1]]. So do [[prop:iii-g4-5-1]] and [[lem:iii-g4-4-3]], whose inputs
are the tf-normal operator (B2), the zero energy states (B3) and [[ch:s18]].

(B5) S ↦ h_b(S) is injective, uniformly in b ([[lem:s20-injective]] below).

The results of [[ch:s19]] that we use — [[prop:iii-i1-2-1]], [[prop:iii-i1-3-1]], [[lem:iii-i2-2-1]],
[[lem:iii-i2-3-1]], [[lem:iii-i2-4-1]]–[[lem:iii-i2-4-3]] and [[prop:iii-i2-5-1]] — are used at b: L_(b₀), g_(b₀) near
K⁺ and the states at b₀ are replaced by L_b, g_b and the states at b, and the background g_(b₀,b₀,−S) by
g_(b₀,b,−S). In this form they hold at every b ∈ ℬ̄_*, with constants uniform in b ([[thm:iii-i15-3-1]])
[[pending:issue-1]].

**Lemma {#lem:s20-injective}** (The s1 states at b.) After shrinking ℬ_*, there are a compact set 𝒦_0 ⊂ X° and c > 0
such that

    sup_(𝒦_0) |h_b(S)| ≥ c|S|        for all b ∈ ℬ̄_* and S ∈ 𝒮_(1,ℂ).

In particular S ↦ h_b(S) is injective, and h_b(Ṡ) determines Ṡ, with |Ṡ| ≤ c⁻¹ sup_(𝒦_0)|h_b(Ṡ)|.

*Proof.* At b₀ the map S ↦ h_(b₀)(S) is injective ([[prop:iii-f3-4-1]] (1)). Let S lie on the unit sphere of
𝒮_(1,ℂ) ≅ ℂ⁴. Then h_(b₀)(S) is a nonzero smooth tensor on X°, so it does not vanish at some point x_S, and by linearity
and continuity |h_(b₀)(S′)(x_S)| > 0 for S′ in a neighbourhood of S on the sphere. Finitely many such neighbourhoods
cover the sphere; let 𝒦_0 be the finite set of their points x_S. The function S ↦ max_(𝒦_0)|h_(b₀)(S)| is continuous
and positive on the sphere, so it is at least 2c for some c > 0, and by homogeneity sup_(𝒦_0)|h_(b₀)(S)| ≥ 2c|S|.
h_b(S) is smooth in b and linear in S ((B3)), so |h_b(S) − h_(b₀)(S)| ≤ C|b − b₀||S| on 𝒦_0, and the bound with c
holds for |b − b₀| ≤ c/C. ∎

### Profiles at zero energy {#sec:iii-i3-1}

This section and the next are [Hin26, Section 11.4.1] in dimension 4 + 1.

For γ_zf ∈ (0, 1), H^(k,(γ_scf,γ_tf,((0,0),γ_zf)))_b(X^±_(sc-b)) is the space of χ_zf v_0 + ũ with
v_0 ∈ H^(k,γ_tf)_b(X), its *zf-coefficient* (the same for both signs when so stated), and ũ ∈ H^(k,γ)_b(X^±_(sc-b))
([[sec:ii-g1-3-1]]). Throughout, c ≤ 1/(8√5), so that χ_zf = 1 on {r ≤ 2} for |σ| ≤ c (there ⟨x⟩ ≤ √5, so
r̂ ≤ 1/8); and c is also below the k-independent bound of [[sec:iii-i3-2]] (χ_zf = 1 on supp f*_j).

**Lemma {#lem:iii-i3-1-1}** (Profiles independent of σ.) Let a ∈ ℝ, P ∈ ρ^p Diff^m_b(X̄) with smooth coefficients,
p ≥ 0, j ∈ ℕ₀, and u_0 ∈ H^(∞,a)_b(X). Then

(a) σ^j χ_zf P u_0 ∈ H^(∞,(∞,a+p+j,γ_zf))_b(X^±_(sc-b)) for every γ_zf < j;

(b) [P, χ_zf]u_0 (for m ≥ 1) and (χ′ − χ_zf)u_0, χ′ any other function of r̂ equal to 1 near 0 and with compact
support, lie in H^(∞,(∞,a+p,∞))_b, resp. H^(∞,(∞,a,∞))_b.

*Proof.* On supp χ_zf, |σ| ≤ ρ/4, so by [[eq:ii-g1-3-2]] ρ_tf ∼ ρ, ρ_zf ∼ r̂ = |σ|/ρ and ρ_scf ∼ 1, and the weight is
w_γ ∼ ρ^(γ_tf−γ_zf) |σ|^(γ_zf). (a) By Fubini,

    ∬ |σ|^(2j) |Pu_0|² ρ^(−2(γ_tf−γ_zf)) |σ|^(−2γ_zf) 1_(|σ|≤ρ/4) |dσ/σ| μ_X = C ∫ |Pu_0|² ρ^(−2(γ_tf−j)) μ_X,

the inner integral ∫_0^(ρ/4) σ^(2(j−γ_zf)) dσ/σ = (ρ/4)^(2(j−γ_zf))/(2(j − γ_zf)) converging as γ_zf < j. This is
finite for γ_tf ≤ a + p + j, as Pu_0 ∈ H^(∞,a+p)_b(X). The fields σ∂_σ and ⟨x⟩∂_x fall on σ^j, on χ_zf (bounded
derivatives, [[sec:ii-g1-3-1]]) and on Pu_0, with the same bound. (b) The coefficients of [P, χ_zf] and of χ′ − χ_zf
are supported in r̂ ∈ [δ, δ⁻¹] for some δ ∈ (0, 1), a compact subset of the interior of tf, where w_γ ∼ ρ^(γ_tf).
Fubini with ∫_(δρ)^(ρ/δ) dσ/σ = 2 log δ⁻¹ bounds the norm by C‖ρ^(−γ_tf) · ‖_(L²(μ_X)) of terms of the form ρ^p times
b-derivatives of u_0, resp. of u_0 itself, finite for γ_tf ≤ a + p, resp. γ_tf ≤ a. ∎

**Lemma {#lem:iii-i3-1-2}** (The augmented operator near zero energy; [Hin26, Lemma 11.21] in dimension 4 + 1.) For
u_0 ∈ H^(∞,a)_b(X) and |σ| ≤ c:

(a) (L̂_b(σ) − L̂_b(0))(χ_zf u_0) ∈ H^(∞,(∞,a+2,γ_zf))_b for every γ_zf < 1;

(b) for ḃ ∈ 𝔟, S ∈ 𝒮_1 and the columns f̂_ḃ, f̂_S of [[def:iii-h-2-1]] and [[def:iii-h-3-1]], f̂_ḃ(σ) − χ_zf f̂_ḃ(0)
and f̂_S(σ) − χ_zf f̂_S(0) lie in H^(∞,(N,3−ε,1−ε))_b(X^±_(sc-b)) for every N and ε > 0, and
f̂_ḃ(0), f̂_S(0) ∈ 𝒜³ ⊂ H^(∞,3−ε)_b(X).

[Hin26, (11.64)] has ρ_tf² ρ_zf Diff¹_b in (a) and, from [Hin26, Lemma 10.5], the tf-weight 2 + ε_ind − ε for the
columns. In dimension 4 + 1 the columns are one order better at tf, and the rows of L̃_b(σ) do not depend on σ
([[def:iii-h-3-1]]).

*Proof.* (a) L̂_b(σ) − L̂_b(0) = −iσL_1 − σ²L_2, with L_1 ∈ ρ Diff¹_b and L_2 ∈ ρ² C^∞ near ∂X̄ and with smooth
coefficients on compact sets ([[sec:iii-h-1]]). Write L_1χ_zf = χ_zf L_1 + [L_1, χ_zf]. [[lem:iii-i3-1-1]] (a) with
(p, j) = (1, 1) and (2, 2) puts σχ_zf L_1u_0 and σ²χ_zf L_2u_0 in the space stated, and [[lem:iii-i3-1-1]] (b) gives
[L_1, χ_zf]u_0 ∈ H^(∞,(∞,a+1,∞))_b, which the factor σ, of tf-order 1 on the interior of tf, brings to a + 2.

(b) By [[lem:iii-h-2-4]] (a), f̂ = f̂_c + f̂_∞ with f̂_c entire in σ and supported in {r ≤ 2}, and f̂_∞ = r⁻³G(σr, x)
on {r ≥ 1}, with G entire and |(ζ∂_ζ)^j (r∂_r)^i ∂^β_ω G| ≤ C⟨ζ⟩^(−N) for Im ζ ≥ 0. For |σ| ≤ c, χ_zf = 1 on
{r ≤ 2}, so f̂_c(σ) − χ_zf f̂_c(0) = f̂_c(σ) − f̂_c(0) = O(|σ|) in C^∞, supported in {r ≤ 2}, where ρ_zf ∼ |σ|: this
gives the zf-weight 1 − ε and no condition at tf or scf. On {r ≥ 1}, H := G(σr, x) − χ_1(|σ|⟨x⟩)G(0, x) satisfies
|VH| ≤ C min(|σ|r, 1)⟨σr⟩^(−N) for products V of σ∂_σ, r∂_r, ∂_ω: G(ζ) − G(0) = O(|ζ|) where χ_1 = 1, G decays
rapidly where χ_1 = 0, and |σ|⟨x⟩ ∼ |σ|r in between. On {r̂ ≤ 1}, where w_γ ∼ ρ^(γ_tf−γ_zf) |σ|^(γ_zf), Fubini bounds
that part of the squared norm of r⁻³H by

    C ∫ ⟨x⟩^(−4+2(γ_tf−γ_zf)) ∫_0^(1/⟨x⟩) σ^(2−2γ_zf) (dσ/σ) μ_X = C′ ∫ ⟨x⟩^(2γ_tf−6) μ_X,

finite for γ_zf < 1 and γ_tf < 3. On {r̂ ≥ 1} the rapid decay in r̂ and r⁻³ ≤ (ρ_scf ρ_tf)³ give the bound, as in the
proof of [[lem:iii-h-2-4]] (b). f̂(0) ∈ 𝒜³ is [[lem:iii-h-2-3]]. ∎

**Lemma {#lem:iii-i3-1-3}** (The cut-off states near zero energy.) Let G_1, G_2 and the cut-off χ be those of
[[eq:iii-i2-4-1]] and [[sec:iii-i2-4]]:

    G_1(σ)(ḃ) := Ψ(σ, ·) ġ_b(ḃ),      G_2(σ)(S) := (Ψ − σ∂_σΨ) h_b(S) − iσΨ h̆_b(S),

with Ψ of [[lem:iii-h-2-5]]. For ḃ_0 ∈ 𝔟 and S_0 ∈ 𝒮_1,

    χ(|σ|)G_1(σ)(ḃ_0) − χ_zf ġ_b(ḃ_0) ∈ H^(∞,(N,2−ε,1−ε))_b,     χ(|σ|)G_2(σ)(S_0) − χ_zf h_b(S_0) ∈ H^(∞,(N,3−ε,1−ε))_b

for every N and ε > 0; and ġ_b(ḃ_0) ∈ H^(∞,2−ε)_b(X), h_b(S_0) ∈ H^(∞,3−ε)_b(X).

*Proof.* As for [[lem:iii-i3-1-2]] (b). For r ≥ 1, Ψ = Φ(σr) with Φ(0) = 1 ([[lem:iii-h-2-5]] (b)); so, with
ζ := σr,

    G_1(ḃ_0) − χ_zf ġ_b = (Φ(ζ) − χ_1(|σ|⟨x⟩)) ġ_b,
    G_2(S_0) − χ_zf h_b = ((Φ − ζΦ′)(ζ) − χ_1(|σ|⟨x⟩)) h_b − iζΦ(ζ) r⁻¹h̆_b,

both O(min(|ζ|, 1)⟨ζ⟩^(−N)) times states in 𝒜², resp. 𝒜³ ((B3); r⁻¹h̆_b ∈ 𝒜³). For r ≤ 1, Ψ − 1 = O(|σ|) with its
derivatives ([[lem:iii-h-2-5]] (d) and its proof). And χ(|σ|) − 1 vanishes for |σ| ≤ c/2; on supp χ_zf the remaining
term is supported in a compact set of x away from tf and zf. The Fubini count of [[lem:iii-i3-1-2]] (b), with ⟨x⟩⁻² in
place of ⟨x⟩⁻³ for G_1, gives γ_tf < 2 there. ∎

### The boost parameter {#sec:iii-i3-2}

Let h^(≤1)_b(S) = t_* h_b(S) + h̆_b(S) be the generalised state of the boosts at b ((B3); [Hin26, (6.37), (6.32b)]),
and χ^H_K the cut-off of [[eq:iii-h-1-2]]: smooth, vanishing for t_* ≤ 1 and for |x| ≥ t_*/2, and equal to 1 on
{t_* ≥ 2, |x| ≤ t_*/4}.

**Proposition {#prop:iii-i3-2-1}** (The boost parameter; [Hin26, Proposition 11.20] in dimension 4 + 1.) Let
b ∈ ℬ̄_* and L := L^(g,g_0), with g_0 := g_(b₀,b,−S), g := g_0 + h, |S| < ε_0, h ∈ 𝒳^∞ and ‖h‖_(𝒳^d) < ε_0, ε_0 and d
those of [[thm:iii-i-5-3]]. Let ℓ_I satisfy [[eq:iii-i2-5-1]], α_K ∈ (1, min(a_K − 1, 3/2)) and α_+ > α_K. For
f ∈ H^(∞,(⟨ℰ^C_I+1⟩′,ℓ_I+1),α_++2,α_K)_b(Ω_*; S²T*)^(•,−), the forward solution of Lu = f is

    u = χ^H_K h^(≤1)_b(Ṡ) + ũ,     Ṡ ∈ 𝒮_1,
    ũ ∈ H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β_+,α_K−2)_b(Ω_*)^(•,−)  for every β_+ < min(α_+, 3/2, min Re ℰ_+),           {#eq:iii-i3-2-1}

with Ṡ and ũ depending continuously on f, uniformly in b ∈ ℬ̄_*.

Ṡ is determined by u: ũ has K⁺-weight α_K − 2 > −1, so h_b(Ṡ) is the coefficient of t_* in u at K⁺, and S ↦ h_b(S)
is injective ([[lem:s20-injective]]). [Hin26, (11.63)] has the ι⁺-weight 1 − ε and α_K ∈ (1, 1 + ε_K).

*Proof.* *Step 0* ([Hin26, (11.65)]). Fix α′_K ∈ [1/2, 1) with α′_K ≥ α_K − (a_K − 2), possible as α_K < a_K − 1,
and β′_+ ∈ (1, min(α_+, 3/2, min Re ℰ_+)). [[prop:iii-i2-5-1]], with α′_K for α_K (α_+ > α′_K), gives
u ∈ H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β′_+,α′_K−2)_b. [[eq:iii-i-4-2]] of [[prop:iii-i-4-1]] (3/2 < ℓ_I < a_I + 1/2,
β′_+ < min Re ℰ_+) gives (L − L_b)u the ι⁺-weight β′_+ + 2 + m_+ − ε > 4 (with no expansion term, as
β′_+ + m_+ < 2 min Re ℰ_+) and the K⁺-weight α′_K − 2 + a_K ≥ α_K. Fix

    α^♯_+ ∈ (α_K, min(α_+, λ_♯)),     α^♯_+ ≥ min(α_+, 3/2) − ε,                                         {#eq:iii-i3-2-2}

for a given small ε > 0. Then α^♯_+ ∈ (1, 7/4) ⊂ (1, 2), α^♯_+ − 1 ∈ (0, 1) and α^♯_+ − α_K ∈ (0, 1). So

    L_b u = f′ := f − (L − L_b)u ∈ H^(∞,(⟨ℰ^C_I+1⟩′,ℓ_I+1),α^♯_++2,α_K)_b(Ω_*)^(•,−).

*Step 1* (null infinity; [Hin26, (11.66a)]). [[prop:iii-i1-3-1]] with ℰ̆_+ := ∅ and ℓ̆_+ := α^♯_+ applies, as
α^♯_+ < λ_♯ < min Re ℰ^C_I ([[def:iii-c-3-1]] (2)), so α^♯_+ ∉ Re π_1ℰ^C_I and α^♯_+ ≠ λ_♯. It gives u_I, supported
near 𝓘⁺ and vanishing for t_* < 1, with ι⁺-data (ℰ^♯_+, α^♯_+) and f′ − L_b u_I ∈
H^(∞,ℓ_I+1,(ℰ^♯_++2,α^♯_++2),α_K)_b. As min Re ℰ^♯_+ = λ_♯ > α^♯_+ ([[eq:iii-i1-3-2]] with ℰ̆_+ = ∅; min Re ℰ^C_I is
larger), both are plain weights:

    u^♭ := u − u_I :     L_b u^♭ = f^♭ := f′ − L_b u_I ∈ H^(∞,ℓ_I+1,α^♯_++2,α_K)_b(Ω_*)^(•,−).

In [Hin26] the set ℰ^♯_+ contains (1, 0), which leaves a t_*^(−3) term at ι⁺ in f^♭, removed there by [Hin26,
Proposition 9.11] at λ = 1; in dimension 4 + 1 there is no such term. u^♭ vanishes for t_* < 1, so it is the forward
solution of L_b u^♭ = f^♭ ([[prop:ii-e-3-4]]).

*Step 2* (the decomposition). As in [[sec:iii-i2-4]], u^♭ = u_hi + u_reg + u_sing, with ℱu_hi =
(1 − χ(|σ|))L̂_b(σ)⁻¹ f̂^♭(σ), ℱu_reg = χ(|σ|)û_(reg,1)(σ), (û_(reg,1), b̂_1, Ŝ_1) := L̃_b(σ)⁻¹(f̂^♭(σ), 0, 0), and
u_sing = u_(sing,1) + u_(sing,2) with

    ℱ(∂_(t_*) u_(sing,1)) = χ(|σ|)G_1(σ)(b̂_1(σ)),        ℱ(∂²_(t_*) u_(sing,2)) = χ(|σ|)G_2(σ)(Ŝ_1(σ))

([[eq:iii-i2-4-1]]). The memberships [[eq:iii-i3-2-3]]–[[eq:iii-i3-2-13]] are read as there: at order k, with the c of
that order and of the weight α of [[eq:iii-h-1-1]] with α + 2 = α^♯_+ − α_K. The functions u, u_I, u^♭ and ũ and the
parameter Ṡ = S_0 (obtained from L̃_b(0)⁻¹) do not depend on c, so their memberships hold at every order.
[[lem:iii-i2-4-1]] (β^f_I = ℓ_I, β_ι = α^♯_+, β_K = α_K ∈ (1, 2); ℓ_I + 1 ≥ α^♯_+ + 2 − (1 − ε_1), as ℓ_I ≥ 2) gives
u_hi ∈ H^(∞,(3/2−ε,N,N))_b(M′). [[prop:ii-g1-3-3]] (1), with β_K = α_K ∈ (1, 2), gives

    f̂^♭|_(±(0,c]) ∈ H^(∞,(3−ε,α^♯_++1,((0,0),α_K−1)))_b(X^±_(sc-b))                                     {#eq:iii-i3-2-3}

(its scf-weight is min(ℓ_I + 1, α^♯_+ + 2) − ε ≥ 3 − ε), with zf-coefficient f̂^♭(0) = ∫ f^♭ dt_* ∈
H^(∞,α^♯_++1)_b(X), the same for both signs (f^♭(·, x) is integrable, its K⁺-weight being α_K > 1).

*Step 3.1* (zero energy; [Hin26, (11.68)–(11.70)]). By [[prop:iii-h-3-2]] at the weight α := α^♯_+ − 3, so that
α + 2 = α^♯_+ − 1 ∈ (0, 1) and 𝒴_0 = H̄^(s−1,α+2)_b has the μ_b-weight α^♯_+ + 1 ([[sec:ii-g1-4-1]]), at every
regularity s,

    (û_0, ḃ_0, S_0) := L̃_b(0)⁻¹(f̂^♭(0), 0, 0),     û_0 ∈ H^(∞,α^♯_+−1)_b(X),   ḃ_0 ∈ 𝔟,   S_0 ∈ 𝒮_1.   {#eq:iii-i3-2-4}

The rows of L̃_b(σ) do not depend on σ, and ⟨χ_zf û_0, f*_j⟩ = ⟨û_0, f*_j⟩ = 0 once c is so small that χ_zf = 1 on
supp f*_j; and χ_zf û_0 ∈ 𝒳_σ for σ ≠ 0, having compact support in x. So, for 0 < |σ| ≤ c,

    L̃_b(σ)(χ_zf û_0, ḃ_0, S_0) = (f̂^♭(σ) − f̂_2(σ), 0, 0),                                             {#eq:iii-i3-2-5}

    f̂_2 := (f̂^♭ − χ_zf f̂^♭(0)) − [L̂_b(0), χ_zf]û_0 − (L̂_b(σ) − L̂_b(0))(χ_zf û_0)
             − (f̂_(ḃ_0)(σ) − χ_zf f̂_(ḃ_0)(0)) − (f̂_(S_0)(σ) − χ_zf f̂_(S_0)(0)),

using L̂_b(0)û_0 + f̂_(ḃ_0)(0) + f̂_(S_0)(0) = f̂^♭(0), which is [[eq:iii-i3-2-4]]. The first term of f̂_2 lies in
H^(∞,(3−ε,α^♯_++1,α_K−1))_b by [[eq:iii-i3-2-3]] and the definition of the space; the second in
H^(∞,(∞,α^♯_++1,∞))_b ([[lem:iii-i3-1-1]] (b), p = 2, a = α^♯_+ − 1); the third in H^(∞,(∞,α^♯_++1,γ_zf))_b for every
γ_zf < 1 ([[lem:iii-i3-1-2]] (a)); the last two in H^(∞,(N,3−ε,1−ε))_b ([[lem:iii-i3-1-2]] (b)). As α^♯_+ < 2 − ε and
α_K − 1 < 1 − ε for ε small,

    f̂_2|_(±(0,c]) ∈ H^(∞,(5/2−ε,α^♯_++1,α_K−1))_b(X^±_(sc-b)).                                          {#eq:iii-i3-2-6}

*Step 3.2* (the rest; [Hin26, (11.71)]). By [[eq:iii-i3-2-5]],

    (û_(reg,1), b̂_1, Ŝ_1) = (χ_zf û_0, ḃ_0, S_0) + L̃_b(σ)⁻¹(f̂_2(σ), 0, 0).

[[lem:iii-i2-4-2]] with β_scf := 3/2 − ε, β_tf := α^♯_+ − 1, β_zf := α_K − 1 (α + 2 := α^♯_+ − α_K ∈ (0, 1)) applies
to [[eq:iii-i3-2-6]], so

    û_(reg,1) ∈ H^(∞,(3/2−2ε,α^♯_+−1,((0,0),α_K−1)))_b,
    b̂_1 ∈ H^(∞,((0,0),α_K−1))_b(±(0, c], |dσ/σ|; 𝔟),      Ŝ_1 ∈ H^(∞,((0,0),α_K−1))_b(±(0, c], |dσ/σ|; 𝒮_1),
                                                                                                         {#eq:iii-i3-2-7}

with the coefficients û_0, ḃ_0, S_0 at σ = 0, the same for both signs (û_0 ∈ H^(∞,α^♯_+−1)_b(X) being the
zf-coefficient of the tf-weight α^♯_+ − 1). By [[prop:ii-g1-3-5]] (1), applied to χ(|σ|)û_(reg,1), which is
supported where the cut-off of [[prop:ii-g1-3-5]] is 1 as c ≤ 1/2, with β_K = α_K ∈ (1, 2) and the one Taylor
coefficient, of order 0 < α_K − 1, the same for the two signs,

    u_reg ∈ H^(∞,(min(3/2,α^♯_+)−3ε,α^♯_+,α_K))_b(M′).                                                   {#eq:iii-i3-2-8}

*Step 3.3* (the singular part; [Hin26, (11.72)–(11.74)]). By [[eq:iii-i2-4-1]], [[lem:iii-i3-1-3]] and
[[lem:iii-i2-4-3]] with a = α_K − 1, applied to b̂_1 − ḃ_0 and Ŝ_1 − S_0,

    ℱ(∂_(t_*) u_(sing,1)) ∈ H^(∞,(N,2−ε,((0,0),α_K−1)))_b,     ℱ(∂²_(t_*) u_(sing,2)) ∈ H^(∞,(N,3−ε,((0,0),α_K−1)))_b,

with zf-coefficients ġ_b(ḃ_0) and h_b(S_0): the tf-weights α_K + 1 − ε and α_K + 2 − ε of the remainders exceed 2 − ε
and 3 − ε, and 1 − ε > α_K − 1. Multiplication by −iσ takes the first to H^(∞,(N,3−ε,α_K−1))_b with zero
zf-coefficient ([[lem:iii-i3-1-1]] (a) with j = 1 for σχ_zf ġ_b(ḃ_0); α_K − 1 < 1), so

    ℱ(∂²_(t_*) u_sing) ∈ H^(∞,(N,3−ε,((0,0),α_K−1)))_b(X^±_(sc-b)),   with zf-coefficient h_b(S_0) for both signs.
                                                                                                         {#eq:iii-i3-2-9}

This is [Hin26, (11.72a)–(11.72b)], with the tf-weight 3 − ε in place of 2 − ε. As u^♭ = 0 for t_* < 1,
u_sing = −(u_hi + u_reg) there, so by [[eq:iii-i3-2-8]]

    u_sing|_(Ω_−) ∈ H̄^(∞,min(3/2,α^♯_+)−3ε,α^♯_+,α_K)_b,
    ∂_(t_*)u_sing|_(Ω_−) ∈ H̄^(∞,min(3/2,α^♯_+)−3ε,α^♯_++1,α_K+1)_b,                                    {#eq:iii-i3-2-10}

∂_(t_*) raising the ι- and K-weights by 1 ([[sec:iii-i2-1]]).

*First integration.* [[lem:iii-i2-3-1]] applies to v := ∂_(t_*)u_sing with β_I := 3/2, β_ι := α^♯_+ + 1 and
β_K := α_K − 1 ∈ (0, 1/2): β_ι > β_I; β_K ≤ β_ι − β_I = α^♯_+ − 1/2, as α^♯_+ > α_K; β_K ∈ (−1, 1) ∖ {0}; the
zf-restrictions of the two signs agree by [[eq:iii-i3-2-9]]; v|_(Ω_<) has weights at least (∞, β_ι, β_K) by
[[eq:iii-i3-2-10]]; ℱv is supported in a compact subset of (−c, c), c ≤ 1/2, as [[lem:iii-i2-3-1]] asks (as in the
proof of [[prop:iii-i2-5-1]]); and the tf-weight 3 − ε of [[eq:iii-i3-2-9]] is at least β_ι = α^♯_+ + 1. So

    ∂_(t_*)u_sing ∈ H^(∞,3/2,α^♯_++1−ε,((0,0),α_K−1))_b(M′).                                            {#eq:iii-i3-2-11}

*Second integration.* [[lem:iii-i2-2-1]] (1) applies to u_sing with (β_I, β_ι, β_K) := (min(3/2, α^♯_+) − 3ε,
α^♯_+ − ε, α_K − 2) and ℰ_K := {(−1, 0)}, so that ℰ_K + 1 = {(0, 0)} (α_K − 2 ∈ (−1, −1/2) is not 0). Its hypotheses
are [[eq:iii-i3-2-10]] (at K⁻ the weight α_K, with no expansion) and [[eq:iii-i3-2-11]]. So

    u_sing ∈ H^(∞,min(3/2,α^♯_+)−3ε,min(3/2,α^♯_+)−4ε,({(−1,0),(0,0)},α_K−2))_b(M′),                    {#eq:iii-i3-2-12}

in which only (−1, 0) lies below the weight α_K − 2 ∈ (−1, −1/2): u_sing = t_* χ u_(K⁺) + O(α_K − 2) at K⁺, for some
u_(K⁺) on K⁺ and a cut-off χ equal to 1 near K⁺.

*Step 3.4* (the coefficient; [Hin26, (11.75)]). u_(K⁺) is the (0, 0)-coefficient of ∂_(t_*)u_sing at K⁺ in
[[eq:iii-i3-2-11]], that is, lim_(t_*→∞) ∂_(t_*)u_sing(t_*, x). As ∂_(t_*)u_sing tends to 0 as t_* → −∞ (its
K⁻-weight is α_K + 1 > 0), and ∂²_(t_*)u_sing(·, x) is integrable (its K⁺-weight is α_K > 1 by [[eq:iii-i3-2-9]] and
[[prop:ii-g1-3-5]] (1), and ⟨t_*⟩^(−α_K) L²(dt_*/⟨t_*⟩) ⊂ L¹ for α_K > 1),

    u_(K⁺) = ∫_ℝ ∂²_(t_*)u_sing dt_* = ℱ(∂²_(t_*)u_sing)(0) = h_b(S_0)

by [[eq:iii-i3-2-9]]. So, with Ṡ := S_0 = Ŝ_1(0),

    u_sing − χ^H_K t_* h_b(Ṡ) ∈ H^(∞,min(3/2,α^♯_+)−3ε,min(3/2,α^♯_+)−4ε,α_K−2)_b(M′),                  {#eq:iii-i3-2-13}

χ^H_K t_* h_b(Ṡ) itself being ρ_K⁻¹ρ_ι² times a bounded conormal function near ι⁺ ∩ K⁺ (h_b ∈ 𝒜³, and χ^H_K = 0 near
𝓘⁺), so of ι⁺-weight 2 − ε. Replacing t_* h_b by h^(≤1)_b = t_* h_b + h̆_b changes this by χ^H_K h̆_b(Ṡ), of weights
(∞, 2 − ε, −ε) (h̆_b ∈ 𝒜² is stationary), which lies within [[eq:iii-i3-2-13]] as α_K − 2 < −ε. In [Hin26], (10.13)
identifies the total integral of ∂²_(t_*) applied to the augmented generalised state with h_(b,s1); here the augmented
state is χ^H_K h^(≤1)_b(S) ([[def:iii-h-2-1]]), and G_2(0)(S) = Ψ(0, ·)h_b(S) = h_b(S) directly.

*Step 4* (null infinity). So u = χ^H_K h^(≤1)_b(Ṡ) + ũ with ũ := u_I + u_hi + u_reg + (u_sing − χ^H_K h^(≤1)_b(Ṡ)), of
ι⁺-weight ℓ′_+ := min(3/2, α^♯_+) − 4ε and K⁺-weight α_K − 2 (Steps 1–3; u_I is supported near 𝓘⁺). Near 𝓘⁺,
χ^H_K = 0, so Lũ = f there, and [[prop:iii-i1-2-1]] with ℓ_+ := min(ℓ′_+, min Re ℰ_+ − ε) gives the 𝓘⁺-data
(⟨ℰ^C_I⟩, ℓ_I). Its hypotheses hold: ℓ_+ ∉ Re π_1ℰ_+, and lowering the a priori weight is free;
3/2 < ℓ_I < min(a_I + 1/2, ℓ_I^max) by [[eq:iii-i2-5-1]]; ℓ_+ < min(ℓ_I, a_+ + min Re ℰ_+); and ℓ_+ lies below
min Re ℰ_+, so that (ℰ_+, ℓ_+) is the weight ℓ_+, and below min Re ℰ^tot_I = 3/2. As α^♯_+ ≥ min(α_+, 3/2) − ε and
ε is arbitrary, [[eq:iii-i3-2-1]] holds for every β_+ < min(α_+, 3/2, min Re ℰ_+); Ṡ does not depend on these
choices, being determined by u.

*Continuity.* f′ depends continuously on f ([[prop:iii-i2-5-1]] and [[eq:iii-i-4-2]]), and u_I, f̂^♭(0),
(û_0, ḃ_0, S_0), f̂_2, the pieces of Step 2 and the integrations are linear maps bounded between the spaces above (the
construction of [[prop:iii-i1-3-1]], [[prop:iii-h-3-2]], [[lem:iii-i3-1-1]]–[[lem:iii-i3-1-3]], [[lem:iii-i2-2-1]],
[[lem:iii-i2-3-1]], [[lem:iii-i2-4-1]]–[[lem:iii-i2-4-3]], [[prop:ii-g1-3-3]] (1) and [[prop:ii-g1-3-5]] (1)). So
Ṡ = S_0 and ũ depend continuously on f; Step 4 does by the closed graph theorem, L being fixed, or by the
constructive bound of [[prop:iii-i1-2-1]]. Every input is uniform on ℬ̄_* by (B1)–(B5), and so are the bounds. ∎

### Undoing the boost: the setting {#sec:iii-i4-1}

[[sec:iii-i4-1]]–[[sec:iii-i4-4]] are [Hin26, Section 11.4.2] in dimension 4 + 1. They construct the correction terms
that let a right-hand side generate the boost term of [[prop:iii-i3-2-1]] ([Hin26, Definition 11.23, Lemma 11.24]),
the identity behind them ([Hin26, (11.76)–(11.78b)]), the augmented gauge-fixed Einstein operator ([Hin26, Definition
11.25]) and its linearisation in the boost parameter ([Hin26, Lemma 11.28]), and they eliminate the boosts ([Hin26,
Proposition 11.30, (11.95)]). Four things differ from [Hin26]. There are no logarithms: the correction h^(−1) has the
index set (2, 0) ∪ (2 + ℰ_ind) at ι⁺ and its linearised curvature (4, 0) ∪ (4 + ℰ_ind), with nothing to cancel,
where [Hin26, (11.82)] cancels a (3, 1)-coefficient. The parameter derivatives begin at order 4 at ι⁺, above every
weight that [[prop:iii-i3-2-1]] uses, so the splitting of [Hin26, (11.86), Remark 11.29] and the special treatment of
(3, 0)-terms are not needed. The boosts of [[sec:iii-b-5]] are centred at t = 0 and the model states of
[[prop:iii-d2-3-1]] at t̄ = 0, with t̄ − t → C′, a translation, so the generalised state is re-centred
([[lem:iii-i4-1-2]]). And the augmented operator is taken in the form of [Hin26, Remark 11.27], so that its
linearisation is exactly the operator of [[thm:iii-i-5-3]] with a shifted perturbation.

*Cut-offs.* χ^♭_K, χ_K, χ^♯_K, χ_IVP, χ^♯_IVP and χ_r are the cut-offs of [[sec:iii-b-5]], with [[eq:iii-i-1-2]].
From here on χ_K is this cut-off: smooth on M, equal to 1 near K⁺ (on supp χ^♭_K ⊃ {|x| < t/10, t > 60R₁}) and to 0
near 𝓘⁺ (supp χ_K ⊂ {|x| < t/2}), supported in {t^♭_* ≥ 10}, with Cartesian derivatives ∂χ_K ∈ ρ_+C^∞ near (ι⁺)°
(the proof of [[lem:iii-i-4-3]]). χ^H_K := χ_+(t_*)χ_c(|x|/t_*) is the cut-off of [[eq:iii-h-1-2]], the one in
[[prop:iii-i3-2-1]]. Put

    𝒞 := supp χ_K ∩ supp(1 − χ_K),

whose closure meets ∂M only in a compact subset of (ι⁺)° (the proof of [[lem:iii-i-4-3]]). Every derivative of χ_K
is supported in 𝒞, and χ^♭_K = 0 on 𝒞, as supp χ^♭_K ⊂ int χ_K⁻¹(1).

*Boosts.* For S = S_w ∈ 𝒮_1 let ω̄(S) := t d(|x|S) − |x|S dt = t w · dx − (w · x)dt, η := −dt² + dx²,
X_S := η⁻¹ω̄(S), Θ := χ_r(|x|)χ^♯_IVP(1 − χ^♭_K), V(S) := ½ΘX_S and φ_S := exp V(S) ([[lem:iii-b-5-1]]). For the
fixed b ∈ ℬ̄_*, the background of the base point is

    g_S := g_(b₀,b,−S) = (1 − χ_K)φ*_(−S) g_(b₀) + χ_K g_b                                               {#eq:iii-i4-1-1}

([[eq:iii-i-1-1]]). Θ = 1 on 𝒞 ∩ {t ≥ T_1} for some T_1: there χ^♭_K = 0, |x| ≥ t/10 (so χ_r = 1 once t ≥ 60R₁),
and t_IVP = t − C″ > −|x|/10 (so χ^♯_IVP = 1). Put

    w(S) := g_(b₀)(X_S, ·) = g_(b₀)η⁻¹ω̄(S),        so that        g_(b₀)(V(S), ·) = ½Θ w(S).

*Conventions.* δ*_g is the symmetrised covariant derivative and δ_g h = −∇^κ h_(κμ) ([[sec:iii-b-6]]), so
ℒ_X g = 2δ*_g(g(X, ·)); with a ⊗_s b := ½(a ⊗ b + b ⊗ a),

    [δ*_g, χ]ω = dχ ⊗_s ω,        [δ_g, χ]h = −ι_(g⁻¹dχ) h.                                              {#eq:iii-i4-1-2}

P(g, g_0), Υ^(E_Υ)(g, g_0), δ*_(g_0,E_C) and δ_(g_0,E_Υ) are those of [[def:iii-b-6-1]]; L^(g,g_0) := D_1P(·, g_0) at
g, and L_b = L^(g_b,g_b) = D_(g_b)Ric + δ*_(g_b,E_C)δ_(g_b,E_Υ)G_(g_b) ([[eq:iii-b-6-8]]). Three identities are used
throughout.

(i) Υ^(E_Υ)(g, g) = 0 for every g ([[eq:iii-b-6-3]]), so (D_1 + D_2)Υ^(E_Υ)(g, g) = 0 and P(g, g) = Ric(g).

(ii) D_1Υ^(E_Υ)(g, g) = −δ_(g,E_Υ)G_g. Indeed Υ⁰(g, g_0) = g g_0⁻¹δ_gG_g g_0 ([[sec:iii-b-6]]), so by
[[eq:iii-b-6-3]] D_1Υ⁰(g, g)k = D(δ_gG_g)(k) g = −δ_gG_g k, as δ_gG_g g = 0 for every g; the E^Υ-term contributes
−E^Υ_g G_g k, which is [[eq:iii-b-6-6]] at g_0 = g.

(iii) If Ric(g) = 0, then D_gRic(ℒ_Y g) = ℒ_Y Ric(g) = 0 for every smooth vector field Y (differentiate
Ric(ψ_ε^* g) = ψ_ε^* Ric(g) along the flow ψ_ε of Y); in particular D_gRic ∘ δ*_g = 0.

*The boost states at b₀.* The corrections below are built from b₀-objects. By [[prop:iii-d2-3-1]] at b₀, with
ω_s1(S) := ω^(0)_(b₀,s1)(S) and ω̆(S) := ω̆^((0),1)_(b₀,s1)(S), stationary and linear in S,

    ω_s1(S) − ω̄_s1(S) ∈ 𝒜^((2,0)∪(2+ℰ_ind)),        ω̆(S) − ω̄̆_s1(S) ∈ 𝒜^((1,0)∪(1+ℰ_ind)),

where ω̄_s1(S) = d(|x|S), ω̄̆_s1(S) = |x| d(|x|S) − |x|S dt̄ and t̄ = t_* + |x| are the Minkowski 1-forms of
[[sec:iii-d2-1]]. h(S) := δ*_(g_(b₀))ω_s1(S) ∈ 𝒜^((3,0)∪(3+ℰ_ind)), and

    h^(≤1)(S) = t_* h(S) + h̆(S) = δ*_(g_(b₀))(t_* ω_s1(S) + ω̆(S)),        h̆(S) ∈ 𝒜^((2,0)∪(2+ℰ_ind)),

is the generalised state h^(≤1)_(b₀) of (B3); h(S) and h^(≤1)(S) lie in the kernels of D_(g_(b₀))Ric and of
δ_(g_(b₀),E_Υ)G_(g_(b₀)). Near infinity t̄ = t + C′ − 8m₀|x|⁻¹ ([[sec:iii-d2-1]], from [[eq:iii-b-3-6]]) and
g_(b₀) − η ∈ |x|⁻²C^∞ ([[eq:iii-b-3-5]], [[prop:iii-b-3-6]]); C′ is that constant.

**Definition {#def:iii-i4-1-1}** (The re-centred states.) At b₀,

    ω^(≤1)_♮(S) := (t_* − C′)ω_s1(S) + ω̆(S),        h^(≤1)_♮(S) := δ*_(g_(b₀))ω^(≤1)_♮(S) = h^(≤1)(S) − C′h(S),

and at b ∈ ℬ̄_*, with the same constant C′,

    ω^(≤1)_(b,♮)(S) := (t_* − C′)ω^(0)_(b,s1)(S) + ω̆^((0),1)_(b,s1)(S),
    h^(≤1)_(b,♮)(S) := δ*_(g_b)ω^(≤1)_(b,♮)(S) = h^(≤1)_b(S) − C′h_b(S).

Each lies in the kernels of D Ric and of δ_(E_Υ)G at its own metric, being a linear combination of the generalised
state and the state of (B3). At b₀, h^(≤1)_(b₀,♮) = h^(≤1)_♮.

**Lemma {#lem:iii-i4-1-2}** (The time origin.) (a) Near infinity,

    (t_* − C′)ω̄_s1(S) + ω̄̆_s1(S) − ω̄(S) = −8m₀|x|⁻¹(d(|x|S) + S d|x|) ∈ |x|⁻¹C^∞(X̄; T*).

(b) Let ℓ_I ∈ ℝ, β_+ < 2 and α_K < 2. If u = χ^H_K h^(≤1)_b(Ṡ) + ũ with ũ ∈
H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β_+,α_K−2)_b(Ω_*)^(•,−), then u = χ_K h^(≤1)_(b,♮)(Ṡ) + ũ′ with ũ′ in the same space, linear and
continuous in (Ṡ, ũ).

*Proof.* (a) As t_* = t̄ − |x|,

    (t_* − C′)d(|x|S) + |x| d(|x|S) − |x|S dt̄ − t d(|x|S) + |x|S dt = (t̄ − C′ − t)d(|x|S) − |x|S d(t̄ − t),

and t̄ − C′ − t = −8m₀|x|⁻¹, d(t̄ − t) = 8m₀|x|⁻²d|x|. The Cartesian components of |x|⁻¹d(|x|S) = |x|⁻¹w · dx and of
S d|x| lie in |x|⁻¹C^∞, resp. C^∞, homogeneous of degree −1, resp. 0.

(b) ũ′ := u − χ_K h^(≤1)_(b,♮)(Ṡ) vanishes near {t^♭_* = 1}, as u does and χ_K = 0 for t^♭_* < 10, and

    ũ′ − ũ = (χ^H_K − χ_K)h^(≤1)_b(Ṡ) + C′χ_K h_b(Ṡ).

Both cut-offs are smooth on M, equal to 1 near K⁺ (χ^H_K = 1 on {|x| ≤ t_*/4, t_* ≥ 2}) and to 0 near 𝓘⁺; so
χ^H_K − χ_K is supported in a set whose closure meets ∂M in a compact subset of (ι⁺)°. There |x| ∼ t_*, and functions
in 𝒜^ℰ(X̄) are in 𝒜^ℰ at ι⁺, ⟨x⟩⁻¹ being ρ_+ times a positive smooth function; so h^(≤1)_b(Ṡ) = t_* h_b(Ṡ) + h̆_b(Ṡ)
lies in 𝒜^((2,0)∪(2+ℰ_ind)) ((B3)), hence in H^(∞,2−ε)_b at ι⁺, with no condition at 𝓘⁺ or K⁺; the compact part is
smooth. And χ_K h_b(Ṡ) vanishes near 𝓘⁺, is bounded and stationary near K⁺ (K⁺-weight −ε for every ε > 0, above
α_K − 2 < 0), and is O(⟨x⟩⁻³) with its b-derivatives near ι⁺ (ι⁺-weight 3 − ε). As β_+ < 2, both terms lie in the
space of ũ. ∎

### The correction terms and the augmented operator {#sec:iii-i4-2}

This section is [Hin26, (11.76)–(11.85)] in dimension 4 + 1.

**Definition {#def:iii-i4-2-1}** (The correction terms; [Hin26, Definition 11.23] in dimension 4 + 1.) For S ∈ 𝒮_1,

    h^(−1)(S) := −[δ*_(g_(b₀)), χ_K](ω^(≤1)_♮(S) − Θw(S)) = −dχ_K ⊗_s (ω^(≤1)_♮(S) − Θw(S)),
    ϑ^(−1)(S) := [δ_(g_(b₀),E_Υ)G_(g_(b₀)), χ_K]h^(≤1)_♮(S) = −ι_(g_(b₀)⁻¹dχ_K) G_(g_(b₀)) h^(≤1)_♮(S),
    ϑ_♯(S) := ϑ^(−1)(S) + D_1Υ^(E_Υ)(g_(b₀), g_(b₀))h^(−1)(S) = ϑ^(−1)(S) − δ_(g_(b₀),E_Υ)G_(g_(b₀))h^(−1)(S).

All three are linear in S, and they are the same tensors at every base point. In [Hin26] h^(−1) is built from
ω̄^((0),≤1)_s1 without the factor Θ. Here w(S) is the 1-form of the boost family of [[sec:iii-b-5]], so that
[[eq:iii-i4-2-3]] below is exact, and Θ = 1 where it matters ([[lem:iii-i4-2-2]]); ϑ_♯ carries the counterterm of
[Hin26, Remark 11.27].

**Lemma {#lem:iii-i4-2-2}** ([Hin26, Lemma 11.24] in dimension 4 + 1.) h^(−1)(S), ϑ^(−1)(S) and ϑ_♯(S) are supported
in 𝒞 and smooth, and, with 𝒢 := (2, 0) ∪ (2 + ℰ_ind), near (ι⁺)°

    h^(−1)(S) ∈ 𝒜^𝒢,      D_(g_0)Ric(h^(−1)(S)) ∈ 𝒜^(𝒢+2),      ϑ^(−1)(S), ϑ_♯(S) ∈ 𝒜^(𝒢+1),             {#eq:iii-i4-2-1}

for every metric g_0 smooth on M near (ι⁺)° with g_0 − η ∈ ρ_+C^∞ there; the seminorms are O(|S|).

*Proof.* Each is a differential expression with a factor dχ_K, so it is supported in 𝒞; it is smooth, as
ω^(≤1)_♮, w, Θ and h^(≤1)_♮ are. Near (ι⁺)°, on 𝒞 ∩ {t ≥ T_1}, Θ = 1 and |x| ≥ t/10, and, omitting S,

    ω^(≤1)_♮ − w = (t_* − C′)(ω_s1 − ω̄_s1) + (ω̆ − ω̄̆_s1) + ((t_* − C′)ω̄_s1 + ω̄̆_s1 − ω̄) + (η − g_(b₀))η⁻¹ω̄.

With t_* ∈ ρ_+⁻¹C^∞ there, the four terms lie in 𝒜^((1,0)∪(1+ℰ_ind)), 𝒜^((1,0)∪(1+ℰ_ind)), ρ_+C^∞
([[lem:iii-i4-1-2]] (a)) and ρ_+²C^∞ · ρ_+⁻¹C^∞ = ρ_+C^∞ (the components of ω̄ are tw and −w · x). So
ω^(≤1)_♮ − w ∈ 𝒜^((1,0)∪(1+ℰ_ind)), with no logarithm, and dχ_K ∈ ρ_+C^∞ gives h^(−1) ∈ 𝒜^𝒢. D_(g_0)Ric is a
second-order operator whose coefficients are smooth functions of g_0⁻¹, g_0 and its first two Cartesian derivatives,
and Cartesian derivatives lie in ρ_+𝒱_b, so D_(g_0)Ric ∈ ρ_+²Diff²_b with smooth coefficients near (ι⁺)°, and it maps
𝒜^𝒢 into 𝒜^(𝒢+2). h^(≤1)_♮ = (t_* − C′)h + h̆ ∈ 𝒜^𝒢 near (ι⁺)°, and ι_(g_(b₀)⁻¹dχ_K) has coefficients in ρ_+C^∞, so
ϑ^(−1) ∈ 𝒜^(𝒢+1). δ_(g_(b₀),E_Υ)G_(g_(b₀)) ∈ ρ_+Diff¹_b there: δ by the Cartesian count, and E^Υ_(g_(b₀)) has
coefficients c_Υ ∈ |x|⁻¹C^∞ and c_(Υ,H), which vanishes for |x| ≥ 5R₁ ([[eq:iii-b-6-1]]); so ϑ_♯ ∈ 𝒜^(𝒢+1). ∎

[Hin26, (11.79)–(11.81)] have the index sets (1, 1) ∪ (1 + ℰ_ind), (3, 0) ∪ (3 + ℰ_ind) and (2, 0) ∪ (2 + ℰ_ind),
and the middle membership there needs the vanishing of a (3, 1)-coefficient ([Hin26, (11.82)]). The absence of a
logarithm here comes from [[prop:iii-d2-3-1]] (1).

**Definition {#def:iii-i4-2-3}** (The augmented operator; [Hin26, Definition 11.25] in dimension 4 + 1, in the form of
[Hin26, Remark 11.27].) For small S ∈ 𝒮_1, b ∈ ℬ̄_* and h ∈ 𝒳^∞ with small 𝒳^d-norm, with g_0 := g_(b₀,b,−S) and
g′ := g_0 + h^(−1)(S) + h, put

    P_1(h, S, b) := Ric(g′) − δ*_(g_0,E_C)(Υ^(E_Υ)(g′, g_0) − ϑ_♯(S)),     L_(h,S) := D_hP_1(·, S, b) at h.
                                                                                                         {#eq:iii-i4-2-2}

P_1(0, 0, b₀) = P(g_(b₀), g_(b₀)) = 0. For b ≠ b₀, P_1(0, 0, b) does not vanish in 𝒞, where the background
interpolates between g_(b₀) and g_b; the linear theory uses only D_hP_1 and D_SP_1. [Hin26, (11.83)] has
Υ^(E_Υ)(g_0 + h, g_0) and ϑ^(−1); [Hin26, Remark 11.27] notes that the present form makes the linearisation in h
exactly a gauge-fixed linearised Einstein operator ([[lem:iii-i4-2-5]]). With the form of [Hin26, (11.83)] one needs in
addition that D_(g′)Ric − D_(g_0+h)Ric is of the error class.

**Lemma {#lem:iii-i4-2-4}** (The boost identity at b₀; [Hin26, (11.76)–(11.78b)] in dimension 4 + 1.) At b = b₀, for
Ṡ ∈ 𝒮_1,

    D_SP_1(0, S, b₀)|_(S=0)(Ṡ) = L_(b₀)(χ_K h^(≤1)_♮(Ṡ))
                               = −D_(g_(b₀))Ric([δ*_(g_(b₀)), χ_K]ω^(≤1)_♮(Ṡ)) + δ*_(g_(b₀),E_C)ϑ^(−1)(Ṡ).
                                                                                                         {#eq:iii-i4-2-3}

Its form at b ∈ ℬ̄_* is [[lem:iii-i15-2-7]].

*Proof.* In this proof b = b₀, g_S = g_(b₀,b₀,−S), and δ*, D Ric, δ*_(E_C), δ_(E_Υ), G are taken at g_(b₀).
*The background.* s ↦ φ_(−sṠ) = exp(−sV(Ṡ)) is the flow of −V(Ṡ), so ∂_S φ*_(−S)g_(b₀)|_(S=0)(Ṡ) =
−ℒ_(V(Ṡ))g_(b₀) = −δ*(Θw(Ṡ)), and with [[eq:iii-i4-1-2]]

    k′ := ∂_S g_S|_(S=0)(Ṡ) = −(1 − χ_K)δ*(Θw) = −δ*((1 − χ_K)Θw) − [δ*, χ_K](Θw).

*The curvature term.* At S = 0, g′ = g_(b₀) (h = 0 and h^(−1)(0) = 0), and ∂_S g′ = k′ + h^(−1)(Ṡ). By (iii),
D Ric(k′) = −D Ric([δ*, χ_K](Θw)), and adding D Ric(h^(−1)(Ṡ)) = −D Ric([δ*, χ_K](ω^(≤1)_♮ − Θw)) gives
∂_S Ric(g′) = −D Ric([δ*, χ_K]ω^(≤1)_♮(Ṡ)).

*The gauge term.* At S = 0 the bracket in [[eq:iii-i4-2-2]] is Υ^(E_Υ)(g_(b₀), g_(b₀)) − 0 = 0, so only its
derivative counts. With D_jΥ := D_jΥ^(E_Υ)(g_(b₀), g_(b₀)), by (i) and the definition of ϑ_♯,

    D_1Υ(k′ + h^(−1)(Ṡ)) + D_2Υ(k′) − ϑ_♯(Ṡ) = D_1Υ h^(−1)(Ṡ) − ϑ^(−1)(Ṡ) − D_1Υ h^(−1)(Ṡ) = −ϑ^(−1)(Ṡ),

so the gauge term contributes +δ*_(E_C)ϑ^(−1)(Ṡ). This is the right side of [[eq:iii-i4-2-3]].

*The left side.* h^(≤1)_♮ = δ*ω^(≤1)_♮ lies in both kernels, so with [[eq:iii-i4-1-2]] and (iii),

    L_(b₀)(χ_K h^(≤1)_♮) = D Ric(δ*(χ_K ω^(≤1)_♮) − [δ*, χ_K]ω^(≤1)_♮)
                           + δ*_(E_C)(χ_K δ_(E_Υ)G h^(≤1)_♮ + [δ_(E_Υ)G, χ_K]h^(≤1)_♮),

which is −D Ric([δ*, χ_K]ω^(≤1)_♮) + δ*_(E_C)ϑ^(−1). ∎

As in [Hin26], [[eq:iii-i4-2-3]] says that the right-hand side D_SP_1(0, 0, b₀)(Ṡ), supported in 𝒞, generates the
forward solution χ_K h^(≤1)_♮(Ṡ): the final black hole boosted along −Ṡ, without an initial boost.

**Lemma {#lem:iii-i4-2-5}** (The linearisation in h; [Hin26, (11.84)–(11.85)] in dimension 4 + 1.) Assume

    2 + ℰ_ind ⊂ ℰ_+.                                                                                     {#eq:iii-i4-2-4}

(ℰ_ind is the index set of [[prop:iii-d2-3-1]], independent of b by (B3) and fixed once, so [[eq:iii-i4-2-4]] is a
condition on ℰ_+.) Then h^(−1)(S) ∈ 𝒳^∞ with ‖h^(−1)(S)‖_(𝒳^k) ≤ C_k|S|, and, at b ∈ ℬ̄_*,

    L_(h,S) = L^(g′,g_0),       g′ = g_0 + h′,     h′ := h^(−1)(S) + h,     g_0 = g_S.

So for |S| and ‖h‖_(𝒳^d) small, L_(h,S) is the operator of [[thm:iii-i-5-3]] at b with (S, h′) in place of (S, h),
and [[prop:iii-i-3-4]], [[prop:iii-i-4-1]], [[cor:iii-i-5-2]], [[thm:iii-i-5-3]], [[prop:iii-i1-2-1]],
[[prop:iii-i1-3-1]], [[prop:iii-i2-5-1]] and [[prop:iii-i3-2-1]] hold for it, with their constants for (S, h′).

*Proof.* ϑ_♯(S) does not depend on h, so D_hP_1 = D_(g′)Ric − δ*_(g_0,E_C)D_1Υ^(E_Υ)(g′, g_0) = L^(g′,g_0)
([[eq:iii-b-6-8]]). By [[lem:iii-i4-2-2]], h^(−1)(S) vanishes near 𝓘⁺ and K⁺ and for t^♭_* < 10, is smooth, and near
(ι⁺)° lies in 𝒜^𝒢; 𝒢 ⊂ ℰ_+ by (2, 0) ∈ ℰ_+ ([[eq:iii-i-1-3]]) and [[eq:iii-i4-2-4]], so h^(−1)(S) lies in
H^(∞,(ℰ_+,a_+))_b at ι⁺ for every a_+, with norms O(|S|). ∎

[Hin26] asks ℰ_+ ⊃ 1 + ℰ_ind and j(ℰ_+ ∪ (1, 1)) ⊂ ℰ_+ ∪ (1, 1) ([Hin26, (11.85)]), the latter for its logarithm; in
dimension 4 + 1, [[eq:iii-i4-2-4]] and [[eq:iii-i-1-3]] suffice.

### The linearisation in the boost parameter {#sec:iii-i4-3}

This section is [Hin26, Lemma 11.28] in dimension 4 + 1. Let

    𝒦 := H^(∞,(⟨(3,0)⟩_0,∞),((2,0),∞),∞)_b(Ω_*),

the class of [[lem:iii-i-3-6]], contained in 𝒳^∞ (the proof of [[prop:iii-i-3-4]]). By [[lem:iii-i-3-6]],
k_S := g_S − g_b ∈ 𝒦. Its proof rests on [[eq:iii-b-5-3]] of [[lem:iii-b-5-2]], with h_(S_w) smooth in w, and on the
pullbacks of [[lem:iii-b-5-1]], smooth in w; so S ↦ k_S ∈ 𝒦 is smooth, and k′ := ∂_S k_S(S′) = ∂_S g_S(S′) ∈ 𝒦 with
seminorms O(|S′|). k′ = −(1 − χ_K)∂_S(φ*_(−S)g_(b₀))(S′) does not depend on b, and it vanishes on int χ_K⁻¹(1), a
neighbourhood of K⁺.

**Lemma {#lem:iii-i4-3-1}** (The derivative of the operator family.) Let |S| and ‖h‖_(𝒳⁵) be small, h ∈ 𝒳^k, k ≥ 5,
s ∈ [0, 1], S′ ∈ 𝒮_1, and L̇ := ∂_S[L^(g_S+sh, g_S)](S′), the derivative of the coefficients. Then L̇ vanishes near
K⁺, lies in the class [[eq:iii-i-3-6]], and for 3/2 < ℓ_I < a_I + 1/2, 0 < ℓ_+ ≤ max(a_+, min Re ℰ_+),
ℓ_+ < a_+ + min Re ℰ_+ and every ε > 0,

    L̇ : H^(k,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_+,ℓ_+),ℓ_K)_b → H^(k−2,(⟨ℰ^C_I+1⟩′,ℓ_I+1),(2ℰ_++2,ℓ_++2+m_+−ε),∞)_b,      {#eq:iii-i4-3-1}

with norm O(|S′|), uniformly in s.

*Proof.* g_S + sh − g_b = k_S + sh and g_S − g_b = k_S, both in 𝒳^k. In the proof of [[prop:iii-i-3-4]],
L^(g,g_0) − L_b is a sum of terms in which smooth functions of g⁻¹, g_0⁻¹ and of the background multiply Cartesian
derivatives, of total order two with the operator's own, of the differences g − g_b, g_0 − g_b
([[eq:iii-b-6-6]]–[[eq:iii-b-6-8]]), at least one factor in each term being a difference; [[lem:iii-c-4-3]] counts
them. L̇ is the sum of the same terms with one factor replaced by k′ or one of its derivatives (or g⁻¹ by
−g⁻¹k′g⁻¹), and k′ ∈ 𝒦 ⊂ 𝒳^∞ is counted as a difference. So L̇ lies in the class [[eq:iii-i-3-6]]. Near 𝓘⁺, in the
proof of [[eq:iii-i-4-1]] of [[prop:iii-i-4-1]], L^(g,g_0) is the leading part ρ_+²ρ_I(X_+ − X_I)(X_I − 3/2 − Ā),
which does not depend on (g, g_0), plus the C^∞ error of L_b, plus the perturbation error, in which the background
difference k_S ∈ 𝒦 ⊂ 𝒳^∞ is counted with h, as in the proof of [[prop:iii-i-3-4]]. The first two do not depend on S.
L̇ is the S-derivative of the perturbation error, which is of the same kind, and the counts given there for the
perturbation error (2ℰ^tot_I ⊂ ℰ^C_I + 1 at the weight ℓ_I + 1, and 2ℰ_+ + 2 at the weight ℓ_+ + 2, by
[[lem:iii-c-2-1]]) apply to it. Away from 𝓘⁺, the count of [[eq:iii-i-4-2]], from [[eq:iii-i-3-6]] and
[[lem:iii-c-2-1]], gives the ι⁺-data; and L̇ = 0 near K⁺, as g_S = g_b there. Linearity in k′ gives the bound O(|S′|).
∎

**Lemma {#lem:iii-i4-3-2}** ([Hin26, Lemma 11.28] in dimension 4 + 1.) Assume [[eq:iii-i4-2-4]]. Let |S| and
‖h‖_(𝒳⁵) be small, h ∈ 𝒳^k, k ≥ 5, b ∈ ℬ̄_*, and f_(h,S)(S′) := D_SP_1(h, S, b)(S′), S′ ∈ 𝒮_1. Put

    ℰ̃_+ := 𝒢 ∪ (ℰ_+ + 𝒢),        𝒢 = (2, 0) ∪ (2 + ℰ_ind).                                              {#eq:iii-i4-3-2}

Then f_(h,S)(S′) is linear in S′ and vanishes on int χ_K⁻¹(1), a neighbourhood of K⁺; if h vanishes for t^♭_* < c,
c ≤ 10, so does f_(h,S)(S′); and for every ε > 0

    f_(h,S)(S′) ∈ H^(k−2,(⟨ℰ^C_I+1⟩′,a_I+1),((ℰ̃_+∪2ℰ_+)+2, a_++2+min(2,m_+)−ε),∞)_b(Ω_*),               {#eq:iii-i4-3-3}

with norm O(|S′|), continuous in (h, S) with h ∈ 𝒳^k. In particular its ι⁺-weight is 4 − ε at worst. f_(0,0)(S′) is
supported in 𝒞, and at b = b₀ it is L_(b₀)(χ_K h^(≤1)_♮(S′)) ([[lem:iii-i4-2-4]]).

*Proof.* Write g_0 = g_S, g′ = g_0 + h^(−1)(S) + h, k′ = ∂_S g_S(S′), h^(−1)′ := h^(−1)(S′) and ϑ′ := ϑ_♯(S′), and
Υ := Υ^(E_Υ). Differentiating [[eq:iii-i4-2-2]],

    f = D_(g′)Ric(k′ + h^(−1)′) − (∂_S δ*_(g_0,E_C))(Υ(g′, g_0) − ϑ_♯(S))
        − δ*_(g_0,E_C)(D_1Υ(g′, g_0)(k′ + h^(−1)′) + D_2Υ(g′, g_0)k′ − ϑ′).                              {#eq:iii-i4-3-4}

Cover Ω_* by the open sets U_K := int χ_K⁻¹(1), U_I := int χ_K⁻¹(0), a neighbourhood U_ι of 𝒞 ∩ {t ≥ T_1} near
(ι⁺)° on which |x| ≥ t/20 and Θ = 1, and a set with compact closure in M°; multiplication by a subordinate partition
of unity of functions smooth on M preserves the spaces.

*On U_K:* g_0 = g_b, h^(−1)(S) = 0 and ϑ_♯(S) = 0 near each point, so P_1(h, S, b) does not depend on S, and f = 0.

*On U_I:* g_0 = φ*_(−S)g_(b₀) is Ricci flat and h^(−1), ϑ_♯ vanish, so by (i) P_1(h, S, b) = P(g_0 + h, g_0) =
P(g_0 + h, g_0) − P(g_0, g_0) = ∫_0^1 L^(g_0+sh, g_0)h ds, and

    f = ∫_0^1 L̇_s h ds,        L̇_s := ∂_S[L^(g_S+sh, g_S)](S′),

which vanishes where h vanishes on a neighbourhood. [[lem:iii-i4-3-1]] with u = h and (ℓ_I, ℓ_+, ℓ_K) =
(a_I, a_+, a_K) (its hypotheses hold: 3/2 < a_I < a_I + 1/2, 0 < a_+ ≤ max(a_+, min Re ℰ_+) and
a_+ < a_+ + min Re ℰ_+) gives the 𝓘⁺-data (⟨ℰ^C_I+1⟩′, a_I + 1) and the ι⁺-data (2ℰ_+ + 2, a_+ + 2 + m_+ − ε),
uniformly in s.

*On U_ι,* every term of [[eq:iii-i4-3-4]] is counted near (ι⁺)°, where Cartesian derivatives lie in ρ_+𝒱_b. The
inputs: φ_(−S) is the exact boost on supp(1 − χ_K) near (ι⁺)° (the proof of [[lem:iii-i-3-6]]), so
g_0 − η ∈ ρ_+²C^∞ and k′ ∈ ρ_+²C^∞, as g_(b₀) − η and g_b − η lie in |x|⁻²C^∞ and |x| ≥ t/20; h^(−1)(S),
h^(−1)′ ∈ 𝒜^𝒢 and ϑ_♯(S), ϑ′ ∈ 𝒜^(𝒢+1) ([[lem:iii-i4-2-2]]); and h ∈ H^(k,(ℰ_+,a_+))_b. So
g′ − η ∈ H^(k,(ℰ_+,a_+))_b (ρ_+²C^∞ ⊂ 𝒜^((2,0)), and [[eq:iii-i4-2-4]]), and products stay in this class
(2ℰ_+ ⊂ ℰ_+). There are three counts, with 𝒜^𝒢 ⊂ 𝒜² (no logarithm at order 2), so that multiplication by an element
of 𝒜^𝒢 raises H_b-weights by 2.

(1) D_(g′)Ric ∈ ρ_+²(C^∞ + H^(k−2,(ℰ_+,a_+))_b)Diff²_b, applied to k′ + h^(−1)′ ∈ 𝒜^𝒢: the index set
(𝒢 + 2) ∪ (ℰ_+ + 𝒢 + 2) and the weight a_+ + 4.

(2) ∂_S δ*_(g_0,E_C) is of order zero with coefficients in ρ_+³C^∞: ∂_S Γ(g_0) involves g_0⁻¹∂k′ and k′∂g_0, and
∂_S E^C_(g_0) involves k′ and c_C ∈ |x|⁻¹C^∞ ([[eq:iii-b-6-2]]). Υ(g′, g_0) is a smooth function of g′, g_0 times
Γ(g′) − Γ(g_0), plus −E^Υ_(g_0)G_(g_0)(g′ − g_0), so with g′ − g_0 = h^(−1)(S) + h it lies in
H^(k−1,(ℰ_++1,a_++1))_b, as does ϑ_♯(S) (𝒢 + 1 ⊂ ℰ_+ + 1). The product: (ℰ_+ + 4, a_+ + 4).

(3) By (i), D_1Υ(g′, g_0)k′ + D_2Υ(g′, g_0)k′ = [(D_1 + D_2)Υ(g′, g_0) − (D_1 + D_2)Υ(g_0, g_0)]k′, a smooth function
of (g′, ∂g′) vanishing at g′ = g_0, hence, by Taylor's formula in g′, linear in (g′ − g_0, ∂(g′ − g_0)) with smooth
coefficients, applied to (k′, ∂k′), of total derivative order one (c_Υ counting as one): (ℰ_+ + 3, a_+ + 3). By the
definition of ϑ_♯,

    D_1Υ(g′, g_0)h^(−1)′ − ϑ′ = [D_1Υ(g′, g_0) − D_1Υ(g_(b₀), g_(b₀))]h^(−1)′ − ϑ^(−1)(S′),

which is linear in (g′ − g_(b₀), g_0 − g_(b₀)) and their first derivatives (both in H^(k,(ℰ_+,a_+))_b) times
ρ_+𝒜^𝒢, plus 𝒜^(𝒢+1): the index set (ℰ_+ + 𝒢 + 1) ∪ (𝒢 + 1) and the weight a_+ + 3. δ*_(g_0,E_C) ∈ ρ_+Diff¹_b
adds 1.

So on U_ι, f has the ι⁺-index set (𝒢 + 2) ∪ (ℰ_+ + 𝒢 + 2) ∪ (ℰ_+ + 4) = ℰ̃_+ + 2 (ℰ_+ + 4 ⊂ ℰ_+ + 𝒢 + 2, as
(2, 0) ∈ 𝒢) at the weight a_+ + 4, and no 𝓘⁺ or K⁺ condition. On the compact part f lies in H^(k−2). Together these
give [[eq:iii-i4-3-3]], with min Re(2ℰ_+ + 2) > 4, min Re(ℰ̃_+ + 2) = 4 and a_+ + 2 + min(2, m_+) > 4. Each term of
[[eq:iii-i4-3-4]] and of ∫_0^1 L̇_s h ds is linear in S′ and a product of factors continuous in (h, S), with the
bounds of [[lem:iii-c-2-1]], so f is continuous in (h, S). If h = 0 for t^♭_* < c, c ≤ 10, then {t^♭_* < c} ⊂ U_I
(supp χ_K ⊂ {t^♭_* ≥ 10}), and f = ∫_0^1 L̇_s h ds = 0 there. For h = 0, S = 0, f vanishes on U_K and on U_I, so it
is supported in 𝒞; at b₀ it is [[eq:iii-i4-2-3]]. ∎

[Hin26, (11.86)–(11.87)] split f into f¹, with the ι⁺-index set ℰ_+ + 3, and a term with ℰ̃_+ + 2 ∋ (3, 0)
supported where (1 − χ^♭_K)χ^♯_K ≠ 0, to keep (3, 0)-terms away from 𝓘⁺ ([Hin26, Remark 11.29]). In dimension 4 + 1
the least exponent is 4 and the weight needed below is α_+ + 2 < 4, so no splitting is made. The finer index sets of
[[eq:iii-i4-3-3]] are recorded for later use.

### Elimination of boosts {#sec:iii-i4-4}

This section is [Hin26, Proposition 11.30 and (11.95)] in dimension 4 + 1. Fix ℓ_I with [[eq:iii-i2-5-1]], that is,
2 ≤ ℓ_I < min(a_I + 1/2, ℓ_I^max) and ℓ_I ∉ Re π_1ℰ^C_I ∪ (3/2 + σ_Υ), and with ℓ_I ≤ a_I, which needs a_I ≥ 2; and
fix α_K ∈ (1, min(a_K − 1, 3/2)) and α_+ ∈ (α_K, 2). [[prop:iii-i3-2-1]] needs ℓ_I ≥ 2, and the parameter derivative
has the 𝓘⁺-weight a_I + 1; the choice a_I = 3 + ε_I of [Hin26] meets a_I ≥ 2. When the parameter b ∈ ℬ̄_* of the base
point is to be named, we write L_(h,S;b), f_(h,S;b), Ṡ_(h,S;b) and S^(−1)_(h,S;b) for the objects below.

**Proposition {#prop:iii-i4-4-1}** (Elimination of boosts; [Hin26, Proposition 11.30] in dimension 4 + 1.) Assume
[[eq:iii-i4-2-4]]. There are d ∈ ℕ and ε_1 > 0 such that for b ∈ ℬ̄_*, |S| < ε_1 and h ∈ 𝒳^∞ vanishing near
{t^♭_* = 1} ([Hin26, (11.91)]) with ‖h‖_(𝒳^d) < ε_1:

(1) (*Asymptotics.*) For f ∈ H^(∞,(⟨ℰ^C_I+1⟩′,ℓ_I+1),α_++2,α_K)_b(Ω_*; S²T*)^(•,−), the forward solution of
L_(h,S)u = f is

    u = χ_K h^(≤1)_(b,♮)(Ṡ(f)) + ũ,     Ṡ(f) ∈ 𝒮_1,
    ũ ∈ H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β_+,α_K−2)_b(Ω_*)^(•,−)    for every β_+ < min(α_+, 3/2, min Re ℰ_+),         {#eq:iii-i4-4-1}

with Ṡ(f) and ũ depending linearly and continuously on f.

(2) (*The boost parameter.*) The map S^(−1)_(h,S) ∈ ℒ(𝒮_1), S′ ↦ Ṡ(f_(h,S)(S′)), with f_(h,S) of [[lem:iii-i4-3-2]]
(which lies in the space of (1) by [[eq:iii-i4-3-3]], as ℓ_I ≤ a_I and α_+ < 2), is invertible, with inverse of norm
at most 2.

The constants, d and ε_1 do not depend on b ∈ ℬ̄_* (after the shrinking of ℬ_* in [[prop:iii-i15-2-8]]). (2) is
proved in [[sec:iii-i15-2-6]], with the bound [[eq:iii-i15-2-5]].

[Hin26, (11.92)] admits f = f¹ + (1 − χ^♭_K)f² with f² of ι⁺-index set (3, 0), and [Hin26, Remark 11.31] a further
f² with K⁺-weight 1 + ε_K; in dimension 4 + 1 both kinds of term have ι⁺-order 4 and lie in the space of (1). [Hin26,
(11.93)] has the ι⁺-weight 1 − ε and α_K ∈ (1, 1 + ε_K).

*Proof of (1).* [[lem:iii-i4-2-5]] and [[prop:iii-i3-2-1]] (its hypotheses: ℓ_I with [[eq:iii-i2-5-1]],
α_K ∈ (1, min(a_K − 1, 3/2)), α_+ > α_K) give u = χ^H_K h^(≤1)_b(Ṡ) + ũ with ũ in the space of [[eq:iii-i4-4-1]],
continuously in f, for ‖h′‖_(𝒳^d) and |S| small; [[lem:iii-i4-1-2]] (b) (β_+ < 3/2 < 2, α_K < 2) gives
[[eq:iii-i4-4-1]]. Ṡ(f) is determined by u: ũ has K⁺-weight α_K − 2 > −1, so h_b(Ṡ) is the coefficient of t_* in u
at K⁺, and S ↦ h_b(S) is injective ([[lem:s20-injective]]). ∎

**Lemma {#lem:iii-i4-4-2}** (The boost parameter depends continuously on the operator.) Write Ṡ_(h,S)(f) for the Ṡ(f)
of [[eq:iii-i4-4-1]]. There are k_0 ∈ ℕ and C such that, for b ∈ ℬ̄_* and (h, S) as in [[prop:iii-i4-4-1]],

(a) |Ṡ_(h,S)(f)| ≤ C‖f‖_(H^(k_0,(⟨ℰ^C_I+1⟩′,ℓ_I+1),α_++2,α_K)_b);

(b) if ℓ_I > 2, or if f vanishes near 𝓘⁺, then for fixed f and b the map (h, S) ↦ Ṡ_(h,S)(f) is continuous, h in
the 𝒳^d-topology with d ≥ k_1 + d_T + 7, d_T the d of [[thm:iii-i-5-3]] and k_1 below.

*Proof.* In the proof of [[prop:iii-i3-2-1]] with L := L_(h,S), Ṡ = S_0 is obtained from f′ := f − (L − L_b)u alone:
u_I by the construction of [[prop:iii-i1-3-1]] for L_b, f^♭ := f′ − L_b u_I, and S_0 the 𝒮_1-component of
L̃_b(0)⁻¹(f̂^♭(0), 0, 0) ([[eq:iii-i3-2-4]]). So Ṡ = Π_b f′ with a linear map Π_b that depends on L_b only and is
bounded on H^(k_1,(⟨ℰ^C_I+1⟩′,ℓ_I+1),α^♯_++2,α_K)_b for some k_1: the construction of [[prop:iii-i1-3-1]] loses
finitely many derivatives, and so do [[prop:ii-g1-3-3]] (1) and [[prop:iii-h-3-2]], which give f̂^♭(0) and
L̃_b(0)⁻¹. The bound of Π_b is uniform in b ∈ ℬ̄_* by (B1) and (B4). Moreover Ṡ is determined by u, so it does not
depend on the auxiliary weights (α′_K, β′_+, α^♯_+, ℓ_I) of that proof, which may therefore be taken with room:
α′_K > α_K − (a_K − 2) strictly and ℓ_I > 2 strictly, so that lowering the weights of u by a small ς > 0 keeps f′ in
a space on which some such Π_b is bounded. If ℓ_I = 2 and f vanishes near 𝓘⁺, f lies in the space for any
ℓ″_I ∈ (2, min(a_I + 1/2, ℓ_I^max)) off the set excluded in [[eq:iii-i2-5-1]], and the argument runs there; Ṡ is the
same, being determined by u.

(a) ‖f′‖ ≤ ‖f‖ + ‖(L − L_b)u‖ ≤ ‖f‖ + C‖u‖, by [[eq:iii-i-4-2]] with the coefficient bounds of [[prop:iii-i-3-4]],
uniform for small (S, h′); and ‖u‖ ≤ C‖f‖ in the space [[eq:iii-i2-5-2]] of [[prop:iii-i2-5-1]], whose constant is
locally uniform in (S, h′). With ‖h′‖_(𝒳^d) ≤ ‖h‖_(𝒳^d) + C|S| ([[lem:iii-i4-2-5]]) this gives (a), k_0 being the
sum of the losses.

(b) For (h_1, S_1) near (h, S), let L_1 := L_(h_1,S_1) and u_1 its forward solution with right-hand side f. Then

    Ṡ_(h_1,S_1)(f) − Ṡ_(h,S)(f) = −Π_b((L_1 − L)u_1 + (L − L_b)(u_1 − u)),                                 {#eq:s20-diff}

as Π_b(f − (L_1 − L_b)u_1) − Π_b(f − (L − L_b)u) is this. The coefficients of L^(g,g_0) − L_b are polynomial in the
differences and their derivatives, with coefficients smooth in g⁻¹, g_0⁻¹ (the proof of [[lem:iii-i4-3-1]]), so
L_1 − L has coefficients in the class [[eq:iii-i-3-6]] of norm o(1) as (h_1, S_1) → (h, S) (h′_1 → h′ in 𝒳^d,
[[lem:iii-i4-2-2]]), and the bound [[eq:iii-i-4-2]] is linear in the coefficient norms ([[lem:iii-c-2-1]]); u_1 is
bounded in [[eq:iii-i2-5-2]] by the argument of (a). So (L_1 − L)u_1 → 0. The continuity in [[prop:iii-i2-5-1]] gives
u_1 → u in [[eq:iii-i2-5-2]] with the weights lowered by ς, at the regularity k_1 + 2 that Π_b needs once
d ≥ k_1 + d_T + 7 (the continuity in [[thm:iii-i-5-3]], through [[eq:iii-i-3-7]]); and [[eq:iii-i-4-2]] gives
(L − L_b)(u_1 − u) → 0 in the space of f′ with the weights lowered by ς, on which Π_b is bounded by the choice of
room. ∎

(b) is a continuity at fixed (h, S, b), and it is not used for [[prop:iii-i4-4-1]] (2): the proof in
[[sec:iii-i15-2-6]] is a direct bound, into which only the identity [[eq:s20-diff]] enters.

#### The boost parameter at b {#sec:iii-i15-2-6}

[[lem:iii-i4-2-4]] is an identity at b₀. It uses that g_(b₀) is Ricci flat in 𝒞 and that the correction and the
leading term are built from the same b₀-state. At b the background in 𝒞 interpolates between g_(b₀) and g_b, so the
identity acquires an error, and [[prop:iii-i4-4-1]] (2) is proved by a bound that is uniform in b, not by continuity
at fixed b.

**Lemma {#lem:iii-i15-2-7}** (The boost identity at b.) Let b ∈ ℬ̄_*, G := g_(b₀,b,0) = (1 − χ_K)g_(b₀) + χ_K g_b
([[eq:iii-i-1-1]]), P_1(h, S, b) as in [[eq:iii-i4-2-2]], with g_0 := g_(b₀,b,−S), and
f_(0,0;b)(Ṡ) := D_SP_1(0, S, b)|_(S=0)(Ṡ). Let h^(≤1)_(b,♮)(Ṡ) = δ*_(g_b)ω^(≤1)_(b,♮)(Ṡ) be the re-centred s1 state
at b ([[def:iii-i4-1-1]]; at b₀ it is h^(≤1)_♮). Then

    f_(0,0;b)(Ṡ) = L^(G,G)(χ_K h^(≤1)_(b,♮)(Ṡ)) + E^S_b(Ṡ),                                             {#eq:iii-i15-2-4}

where E^S_b(Ṡ) is supported in 𝒞, vanishes at b = b₀, and, near (ι⁺)°, lies in 𝒜^(𝒢+2−δ) for every δ > 0,
𝒢 = (2, 0) ∪ (2 + ℰ_ind), with seminorms O(|b − b₀||Ṡ|) uniformly on ℬ̄_*.

*Proof.* *Support.* By [[eq:iii-i-1-1]], g_(b₀,b,−S) = (1 − χ_K)φ*_(−S)g_(b₀) + χ_K g_b, and the corrections h^(−1),
ϑ_♯ of [[def:iii-i4-2-1]] are supported in 𝒞 ([[lem:iii-i4-2-2]]). In the interior of χ_K⁻¹(0),
g′ = g_0 = φ*_(−S)g_(b₀) is Ricci flat for every S, and Υ^(E_Υ)(g_0, g_0) = 0 by (i) of [[sec:iii-i4-1]]; so
P_1(0, S, b) = 0 there for all S, and f_(0,0;b) = 0. In the interior of χ_K⁻¹(1), g′ = g_0 = g_b does not depend on S,
so again f_(0,0;b) = 0. On both sets L^(G,G)(χ_K h^(≤1)_(b,♮)) vanishes as well. On the first it vanishes trivially.
On the second it is L_b h^(≤1)_(b,♮), which is 0: h^(≤1)_(b,♮) = δ*_(g_b)ω^(≤1)_(b,♮) lies in ker D_(g_b)Ric by (iii),
and in ker δ_(g_b,E_Υ)G_(g_b) because ω^(≤1)_(b,♮) is a generalised zero energy state of the gauge potential operator
□^Υ_b ([[prop:iii-d2-3-1]]). So E^S_b is supported in 𝒞.

*At b₀.* G = g_(b₀), L^(G,G) = L_(b₀) and h^(≤1)_(b₀,♮) = h^(≤1)_♮, so [[eq:iii-i15-2-4]] with E^S_(b₀) = 0 is
[[eq:iii-i4-2-3]].

*Size.* Every term of E^S_b(Ṡ) is linear in Ṡ and a smooth function of b on 𝒞. Its ingredients are
G − g_(b₀) = χ_K(g_b − g_(b₀)), which lies in |b − b₀|ρ_+²C^∞ near (ι⁺)° (on 𝒞, |x| ≥ t/10, and
g_b − g_(b₀) = O(|b − b₀||x|⁻²) with all Cartesian derivatives, [[prop:iii-b-3-6]]); the state h^(≤1)_(b,♮), smooth in
b in 𝒜^(𝒢−δ) ((B3), with the loss of [[rem:iii-h-2-6]]); the b-independent corrections; and
k′ := ∂_S g_S(Ṡ) = −(1 − χ_K)δ*_(g_(b₀))(Θw(Ṡ)), which does not depend on b and lies in ρ_+²C^∞ near (ι⁺)° (the proof
of [[lem:iii-i4-3-2]]), and which enters because w itself has order ρ_+⁻¹. The count of [[lem:iii-i4-2-2]], that
D_(g_0)Ric and δ*δG lie in ρ_+²Diff²_b near (ι⁺)°, takes 𝒜^(𝒢−δ) into 𝒜^(𝒢+2−δ), uniformly for b ∈ ℬ̄_*. So
∂_b E^S_b(Ṡ) is bounded there by C|Ṡ|, and E^S_b = E^S_b − E^S_(b₀) is O(|b − b₀||Ṡ|) by the mean value theorem along
the segment from b₀ to b, which lies in the ball ℬ̄_*. ∎

**Proposition {#prop:iii-i15-2-8}** ([[prop:iii-i4-4-1]] (2) and [[cor:iii-i4-4-3]] at b.) In [[prop:iii-i4-4-1]] (1)
at b ∈ ℬ̄_*, the leading term is built at b and Ṡ(f) is read from the coefficient h_b(Ṡ(f)) of t_* at K⁺, which
determines it by [[lem:s20-injective]]. There are C and a smallness of (h, S), uniform on ℬ̄_*, with

    |S^(−1)_(h,S;b) − id| ≤ C(‖h‖_(𝒳^d) + |S| + |b − b₀|).                                              {#eq:iii-i15-2-5}

So, after shrinking ℬ_* and the smallness of (h, S), S^(−1)_(h,S;b) is invertible with inverse of norm at most 2, and
[[cor:iii-i4-4-3]] and [[cor:iii-i5-2-2]] hold at b, with constants uniform in b.

*Proof.* At b, the map of [[lem:iii-i4-4-2]] is Ṡ_(h,S;b)(f) = Π_b f′, with f′ := f − (L_(h,S;b) − L_b)u. Here Π_b is
built from the construction of [[prop:iii-i1-3-1]] for L_b and from L̃_b(0)⁻¹ ([[prop:iii-h-3-2]] at b, (B4)), and
its bound [[lem:iii-i4-4-2]] (a) holds with C uniform in b, by (B1) and (B4). χ_K h^(≤1)_(b,♮)(S′) vanishes for
t^♭_* < 10, as supp χ_K ⊂ {t^♭_* ≥ 10}. By [[lem:iii-i15-2-7]] it is therefore the forward solution
([[prop:ii-e-3-4]]) of the operator L_(0,0;b) = L^(G,G) ([[lem:iii-i4-2-5]] at h = 0, S = 0) with the right-hand side
f_(0,0;b)(S′) − E^S_b(S′), and it has the form [[eq:iii-i4-4-1]] with Ṡ = S′ and ũ = 0. Hence, for S′ in a basis of
𝒮_1,

    S^(−1)_(h,S;b)(S′) − S′ = Ṡ_(h,S;b)(f_(h,S;b)(S′) − f_(0,0;b)(S′)) + (Ṡ_(h,S;b) − Ṡ_(0,0;b))(f_(0,0;b)(S′))
                              + Ṡ_(0,0;b)(E^S_b(S′)).

*The first term.* f_(h,S;b) := D_SP_1(h, S, b) depends smoothly on (h, S). The bounds of [[lem:iii-i4-3-2]] hold for
small (h, S) and depend on b only through finitely many seminorms of g_(b₀,b,−S); the derivative of f_(h,S;b) in h is
bounded by [[eq:iii-i4-3-1]], and that in S by the count of [[eq:iii-i4-3-4]], for d as in [[prop:iii-i4-4-1]]. So
‖f_(h,S;b)(S′) − f_(0,0;b)(S′)‖ ≤ C(‖h‖_(𝒳^d) + |S|)|S′| in the norm of [[lem:iii-i4-4-2]] (a), and the first term
is at most C(‖h‖_(𝒳^d) + |S|)|S′|.

*The second term.* By [[eq:s20-diff]], with (h_1, S_1) := (h, S) and (0, 0) in place of (h, S), it is

    −Π_b((L_(h,S;b) − L_(0,0;b))u_(h,S) + (L_(0,0;b) − L_b)(u_(h,S) − u_(0,0))),

where u_(h,S), u_(0,0) are the forward solutions with the right-hand side f := f_(0,0;b)(S′), which vanishes near 𝓘⁺
(it is supported in 𝒞). The coefficients of L_(h,S;b) − L_(0,0;b) lie in the class [[eq:iii-i-3-6]] with norm at most
C(‖h‖_(𝒳^d) + |S|): they are polynomial in the differences of the metrics, with coefficients smooth in their inverses
(the proofs of [[lem:iii-i4-3-1]] and [[lem:iii-i4-2-5]]). So [[eq:iii-i-4-2]] gives
‖(L_(h,S;b) − L_(0,0;b))u_(h,S)‖ ≤ C(‖h‖_(𝒳^d) + |S|)‖f‖. Since L_(0,0;b)(u_(h,S) − u_(0,0)) =
−(L_(h,S;b) − L_(0,0;b))u_(h,S), [[prop:iii-i2-5-1]], with the weights lowered by the room ς of the proof of
[[lem:iii-i4-4-2]], gives ‖u_(h,S) − u_(0,0)‖ ≤ C(‖h‖_(𝒳^d) + |S|)‖f‖, and [[eq:iii-i-4-2]] bounds the second summand
in the same way. Π_b is bounded on the space with that room, uniformly in b. So the second term is at most
C(‖h‖_(𝒳^d) + |S|)|S′|.

*The third term.* By [[lem:iii-i15-2-7]], E^S_b(S′) is supported in 𝒞. It vanishes near 𝓘⁺ and K⁺, and its
ι⁺-order is at least 4 − δ > α_+ + 2 for δ < 2 − α_+, as α_+ < 2. So it lies in the space of [[lem:iii-i4-4-2]] (a)
with norm at most C|b − b₀||S′|, and the third term is at most C|b − b₀||S′|.

This proves [[eq:iii-i15-2-5]], and the Neumann series gives the inverse once the right side of [[eq:iii-i15-2-5]] is
at most 1/2. The proofs of [[cor:iii-i4-4-3]] and [[cor:iii-i5-2-2]] use the invertibility alone, so they hold at
b. ∎

The same pattern, a direct bound in place of a continuity at fixed base point, serves for the parameter columns of
[[ch:s21]].

**Corollary {#cor:iii-i4-4-3}** ([Hin26, (11.95)] in dimension 4 + 1.) For b ∈ ℬ̄_* and (h, S) and f as in
[[prop:iii-i4-4-1]] (1), put S″ := (S^(−1)_(h,S))⁻¹Ṡ(f). The forward solution u of

    D_((h,S))P_1(·, ·, b)(u, S″) = L_(h,S)u + f_(h,S)(S″) = f                                            {#eq:iii-i4-4-2}

lies in H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β_+,α_K−2)_b(Ω_*)^(•,−) for every β_+ < min(α_+, 3/2, min Re ℰ_+); in compact spatial sets
it grows at most like t_*^(2−α_K) = o(t_*), by b-Sobolev embedding at K⁺.

*Proof.* f − f_(h,S)(S″) lies in the space of [[prop:iii-i4-4-1]] (1) ([[lem:iii-i4-3-2]]), so
u = χ_K h^(≤1)_(b,♮)(Ṡ) + ũ with Ṡ = Ṡ(f) − S^(−1)_(h,S)(S″) = 0 by linearity. ∎

[Hin26] then introduces P′(h, S, b) := P(χ_− h_(−S) + h, S, b) ([Hin26, (11.90)]), which carries the initial data,
and works with h vanishing for t_* < 1 ([Hin26, (11.91)]), restoring χ_− h_(−S) only at [Hin26, Definition 11.63,
Corollary 11.66]. The same is done here: every statement above is for h vanishing near {t^♭_* = 1}, and the initial
data enter with the augmented operators of [[ch:s23]].
