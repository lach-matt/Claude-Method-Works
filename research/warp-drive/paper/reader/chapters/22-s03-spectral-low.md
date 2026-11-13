## The spectral family at zero and low frequencies {#ch:s03}

This chapter studies the spectral family P̂(σ) of [[ch:s01]] at σ = 0 and at small σ ≠ 0 with Im σ ≥ 0.
[[thm:i-c-3-1]] is the Fredholm theory of the zero energy operator P̂(0) on weighted b-Sobolev spaces. [[thm:i-c-4-3]]
is that of the transition face normal operator N_tf(σ̂), the model of P̂(σ) in the regime |x| ∼ |σ|⁻¹.
[[def:i-c-5-1]] defines tf-admissibility, [[cor:i-c-5-2]] draws its consequences, and [[prop:i-c-5-3]] verifies it for
asymptotically Minkowski operators, with the help of Hankel functions. [[thm:i-c-6-4]] gives estimates for P̂(σ) and
for its augmentations by finite-rank terms, uniform as σ → 0, together with an estimate for the adjoint;
[[cor:i-c-6-6]] deduces that P̂(0) has index 0. [[thm:i-c-7-1]] makes all of this uniform in the operator.

These are [Hin26c, Theorem 9.36, Theorem 9.38, Corollary 9.39, Proposition 9.40, Theorem 9.41 with Remark 9.42,
Corollary 9.43] in dimension 4 + 1, for operators on a trivial bundle of any rank. The dimensional changes are these.
The shift of [Hin26c, Lemma 3.11] is n/2 = 2, so α + 3/2 becomes α + 2 in Theorems 9.36 and 9.41 and in Corollary 9.43
of [Hin26c], and H_b^(∞,β−3/2) becomes H_b^(∞,β−2). In [Hin26c, Section 9.5], which is stated for every n,
(n − 1)/2 = 3/2, n/2 = 2 and −n + 2 + β = −2 + β. The Bessel order in Proposition 9.40 is ℓ + 1 and its weights are
(0, 2). [[thm:i-c-6-4]] carries an estimate for the adjoint that [Hin26c] does not state; the proof of [[cor:i-c-6-6]]
needs it, because the augmented operator used there has an index that is not known in advance (see the remarks at the
end of the chapter). The smallness of |σ| in [[thm:i-c-6-4]] may depend on the b-regularity order ([[rem:i-c-6-7]]).

Every input is proved here or in [[ch:s01]]–[[ch:s02]], from the classical facts of [[sec:i-c-2-1]], the scattering
calculus of [HJS] as used in [[ch:s01]], and the facts about Hankel functions from [DLMF] stated in [[sec:i-c-5-2]].
The radii 0 < r_0 − 2δ_0 < r_0 < r_2 < r_h of [[sec:i-a-1-1]] enter only through these inequalities, and the radius R_1
of [[sec:i-c-2-6]] is chosen above r_e + 1 whatever r_0 is; so every result below holds with the inner radius r_0 as a
parameter.

[[sec:i-c-1]] fixes the setting and the hypotheses. [[sec:i-c-2]] proves the b-analysis used at the two conic ends, at
infinity and at the origin of the transition face. [[sec:i-c-3]] treats the zero energy operator, [[sec:i-c-4]] the
transition face normal operator, [[sec:i-c-5]] tf-admissibility and the asymptotically Minkowski case, [[sec:i-c-6]]
the low-energy estimates and the index, and [[sec:i-c-7]] their uniformity in the operator.

*Notation.* As in [[ch:s02]], the rank of the bundle is N_E, and large integers that bound orders of Sobolev spaces
are written M. Δ := Δ_(𝕊³) ≥ 0 is the Laplacian of the round metric on 𝕊³. The variable of the Mellin transform and of
indicial families is ι ∈ ℂ, and an indicial root is a value of ι. Variable decay orders are written 𝗋, as in
[[sec:i-a-1-4]], and r = |x|. For an operator A on 𝕊³ with End ℂ^(N_E)-valued coefficients (in particular for an
endomorphism-valued function), A^† denotes its adjoint for the standard inner product of ℂ^(N_E) and the round density,
and A^(*h) := H_0⁻¹ A^† H_0, with H_0 as in [[sec:i-c-1-1]].

### Setting and hypotheses {#sec:i-c-1}

#### Data from the bounded-frequency theory {#sec:i-c-1-1}

Everything of [[sec:i-a-1]] is kept: X̄, ∂X, ∂_♯X, X̃, the trivial bundle E = X̃ × ℂ^(N_E), fibre inner products h
(with matrices H) and h-adjoints A^(*h) = H⁻¹A^†H, the family P̂(σ) = P̂(0) + σT + σ²P_2, the hypotheses (H1)–(H5),
the thresholds S̄, ϑ_ℋ, ϑ_in, the order pairs, and the spaces H̄^(s,𝗋), Ḣ^(s,𝗋), 𝒳_σ, 𝒴_σ, 𝒳_σ^* of
[[thm:i-a-7-2]]. By [[eq:i-a-1-1]]–[[eq:i-a-1-2]], on {ρ < ρ_1},

    P̂(σ) = 2iσρ(ρ∂_ρ − 3/2 − S) + ρ²P⁽⁰⁾ − iσQ + σ²g_00,                                               {#eq:i-c-1-1}

which is [Hin26c, (9.4) and (5.10)] in dimension 4 + 1. Every b-differential operator with coefficients smooth up to
ρ = 0 can be written as a polynomial in ρ∂_ρ with coefficients that are operators on 𝕊³; for P⁽⁰⁾,

    P⁽⁰⁾ = Σ_(j=0)^2 A_j(ρ)(ρ∂_ρ)^j,     A_j ∈ C^∞([0, ρ_1); Diff^(2−j)(𝕊³; End ℂ^(N_E))).                  {#eq:i-c-1-2}

By (H2), P⁽⁰⁾ − ((ρD_ρ)² + Δ) Id ∈ Diff_b^1 + ρ Diff_b^2, and the second summand vanishes at ρ = 0. So A_2(0) = −Id,
A_1(0) =: a ∈ C^∞(𝕊³; End ℂ^(N_E)) is of order 0, and A_0(0) = Δ Id + V + b with V ∈ Diff¹(𝕊³; End ℂ^(N_E)) of
order 1 and b ∈ C^∞. The *normal operator* and the *indicial family* are

    N(P⁽⁰⁾) := Σ_j A_j(0)(ρ∂_ρ)^j,     I(ι) := Σ_j A_j(0) ι^j = −ι² + aι + Δ + V + b,     ι ∈ ℂ.        {#eq:i-c-1-3}

Then N(P⁽⁰⁾)(ρ^ι v) = ρ^ι I(ι)v for v ∈ C^∞(𝕊³; ℂ^(N_E)), and P⁽⁰⁾ − N(P⁽⁰⁾) ∈ ρ Diff_b^2. We write S_0 := S(0, ·)
and H_0 := H(0, ·).

**Definition {#def:i-c-1-1}** (Indicial roots and gaps; [Hin26c, Definition 3.12].) The *indicial roots* of P̂(0) are
the points of

    spec_b := {ι ∈ ℂ : ker I(ι) ∩ C^∞(𝕊³; ℂ^(N_E)) ≠ 0},

those of ρ⁻²P̂(0) = P⁽⁰⁾, as [Hin26c] defines them for ρ² Diff_b^2. An *indicial gap* is an open interval
(β_−, β_+) ⊂ ℝ, −∞ ≤ β_− < β_+ ≤ ∞, containing no Re ι with ι ∈ spec_b.

By [[lem:i-c-2-4]] below, spec_b is discrete with finitely many points in each vertical strip, so every real number
that is not the real part of a root lies in an indicial gap ([Hin26c, Remark 3.13]).

#### The hypotheses of this chapter {#sec:i-c-1-2}

(G) (*The gap.*) α ∈ ℝ, and α + 2 lies in an indicial gap I = (β_−, β_+) of P̂(0).

(Z) (*Zero energy.*) P̂(0): 𝒳_0 → 𝒴_0 of [[eq:i-c-3-1]] below is invertible.

(TF) (*Transition face.*) P̂ is tf-admissible with weight α + 2 ([[def:i-c-5-1]]).

The regularity order is a constant s > ½ + ϑ_ℋ throughout ([[rem:i-a-1-1]]).

*Remarks.* (a) (G) is the hypothesis "α + 3/2 lies in an indicial gap" of [Hin26c] in dimension 4 + 1: by
[[lem:i-c-2-2]] and [[def:i-c-2-8]], H̄_b^(0,α) = ρ^α L²(|dx|) = ρ^(α+2) L²(μ_b) near ∂X, so the b-weight is α + 2.
(b) Which operators of the Einstein problem satisfy (G), (Z) and (TF), and with which weights, is established in the
chapters where those operators are studied ([[ch:s13]]–[[ch:s15]]); it is not repeated here. (c) Only (H1)–(H2) near
∂X enter [[sec:i-c-4]] and [[sec:i-c-5]]; (H3)–(H4) enter through the interior estimates of [[sec:i-c-3]] and the
low-energy argument of [[sec:i-c-6]]; (H5) enters in [[sec:i-c-7]].

### b-analysis at a conic end {#sec:i-c-2}

#### The classical facts used {#sec:i-c-2-1}

(K1) *Fourier analysis on ℝ^m.* H^s(ℝ^m) := {w : ⟨ζ⟩^s ŵ ∈ L²}. Three facts, each proved here in a line. (i) For
φ ∈ 𝒮(ℝ^m), ‖φw‖_(H^s) ≤ (2π)^(−m) 2^(|s|/2) ‖⟨·⟩^(|s|) φ̂‖_(L¹) ‖w‖_(H^s), by Peetre's inequality
⟨ζ⟩^s ≤ 2^(|s|/2) ⟨ζ − η⟩^(|s|) ⟨η⟩^s and Young's inequality for the transform (2π)^(−m) φ̂ ∗ ŵ of φw; so the norm of
multiplication by φ is bounded by finitely many derivatives of φ, if φ is supported in a fixed compact set. (ii) For
κ > 0 the transform of w(κ·) is κ^(−m) ŵ(ζ/κ), so ‖w(κ·)‖_(H^s) ≤ κ^(−m/2) max(κ, κ⁻¹)^(|s|) ‖w‖_(H^s). (iii) For
s > d + m/2, sup_(|β|≤d) |∂^β w| ≤ (2π)^(−m) ‖⟨ζ⟩^(d−s)‖_(L²) ‖w‖_(H^s), by Cauchy–Schwarz on ŵ.

(K2) *Interior elliptic estimates, uniformly.* Let ℱ be a family of second-order operators on a neighbourhood Ω′ of a
compact set K ⊂ ℝ⁴, with End ℂ^(N_E)-valued coefficients bounded in C^∞(Ω̄′) and principal symbols p Id with
|p(x, ζ)| ≥ c|ζ|². For φ ∈ C_c^∞(int K), φ̃ ∈ C_c^∞(Ω′) equal to 1 near K, and all s and M, there is C with
‖φu‖_(H^s) ≤ C(‖φ̃Lu‖_(H^(s−2)) + ‖φ̃u‖_(H^(−M))) for all L ∈ ℱ. This is [[prop:i-a-5-1]] over a compact set, where
the scattering calculus is the classical one (last paragraph of [[sec:i-a-2-1]]). The uniformity comes from the proof
of [[prop:i-a-5-1]], whose construction depends continuously on the symbol: by Arzelà–Ascoli the closure of ℱ in the
coefficient topology is compact, the coefficients depend continuously on its points, and the ellipticity bound
persists.

(K3) *Rellich.* [HJS, Proposition 3.13]: for distributions supported in a fixed compact set and s′ > s, the inclusion
H^(s′) ↪ H^s is compact.

(K4) *The sphere.* L²(𝕊³) = ⊕_(ℓ≥0) ℋ_ℓ, with ℋ_ℓ the finite-dimensional spaces of spherical harmonics of degree ℓ,
on which Δ = ℓ(ℓ + 2). For integers m ≥ 0, ‖(1 + Δ)^(m/2) w‖_(L²) is equivalent to the H^m(𝕊³) norm, and H^(−m)(𝕊³)
is the dual of H^m(𝕊³). Distributional solutions of elliptic equations with smooth coefficients on 𝕊³ with smooth
right side are smooth. These are (K2) in charts, with a partition of unity.

(K5) *Analytic Fredholm theorem* ([RS1, Theorem VI.14]). If D ⊂ ℂ is open and connected, F: D → ℒ(ℋ) is analytic with
compact values on a Hilbert space ℋ, and Id + F(z_0) is invertible for one z_0 ∈ D, then (Id + F(z))⁻¹ exists for z
off a discrete set 𝒮 ⊂ D, and is meromorphic on D with finite-rank residues.

(K6) *Plancherel on ℝ and Cauchy's theorem.* ℱ_t w(τ) := ∫ e^(−itτ) w(t) dt, so ‖ℱ_t w‖² = 2π‖w‖² for
L²(ℝ; ℋ)-valued w, ℋ a Hilbert space.

#### Ends and dyadic pieces {#sec:i-c-2-2}

An *end* is a neighbourhood of ∞ or of 0 in ℝ⁴, with *decay variable* ϱ := |x|⁻¹ (the end at ∞, where ϱ = ρ) or
ϱ := |x| (the end at 0, used at the face ztf in [[sec:i-c-4]]). Put t := −log ϱ, so t → +∞ at the end,
ω := x/|x| ∈ 𝕊³, and μ_b := |dϱ/ϱ dω| = |dt dω|. The b-vector fields are spanned over C_b^∞ (below) by
ϱ∂_ϱ = −∂_t and a fixed frame Z_1, …, Z_6 of vector fields on 𝕊³; they are dilation invariant.

Fix ψ ∈ C_c^∞((−1, 1)), 0 ≤ ψ ≤ 1, with Σ_(k∈ℤ) ψ(· − k) = 1 on ℝ, and put ψ_k := ψ(t − k),
A := {e⁻¹ < |y| < e}, and Φ_k the dilation of ℝ⁴ by e^k (end at ∞) or e^(−k) (end at 0), which maps A onto
{k − 1 < t < k + 1}. For a distribution v supported in {t > t_0} let v_k := (ψ_k v) ∘ Φ_k, supported in Ā.

**Definition {#def:i-c-2-1}** For s, c ∈ ℝ and v supported in {t > t_0},

    ‖v‖²_(H_(b,c)^s) := Σ_(k≥⌊t_0⌋) e^(2ck) ‖v_k‖²_(H^s(ℝ⁴)).

c is the *b-weight*: at s = 0 the norm is equivalent to ‖ϱ^(−c) v‖_(L²(μ_b)), because μ_b = |y|⁻⁴|dy| on A pulls back
under Φ_k to itself, ϱ^(−c) = e^(ct) lies between e^(c(k−1)) and e^(c(k+1)) on the k-th piece, and Σ_k ψ_k = 1 with at
most two pieces overlapping. C_b^∞ denotes the functions f with (ϱ∂_ϱ)^j Z^α f bounded for all j, α (equivalently,
f ∘ Φ_k bounded in C^∞ on a neighbourhood of Ā uniformly in k); it contains the functions smooth in (ϱ, ω) up to ϱ = 0.
Diff_b^m denotes the operators Σ_(j+|α|≤m) f_(jα) (ϱ∂_ϱ)^j Z^α with f_(jα) ∈ C_b^∞, End ℂ^(N_E)-valued.
𝒜^c := ϱ^c C_b^∞.

**Lemma {#lem:i-c-2-2}** Let s, c ∈ ℝ; all distributions are supported in {t > t_0}.

(a) Another choice of ψ gives an equivalent norm.

(b) For f ∈ C_b^∞, ‖fv‖_(H_(b,c)^s) ≤ C‖v‖_(H_(b,c)^s), with C depending on finitely many seminorms of f; and
‖ϱ^γ v‖_(H_(b,c+γ)^s) and ‖v‖_(H_(b,c)^s) are equivalent.

(c) B ∈ Diff_b^m maps H_(b,c)^s to H_(b,c)^(s−m), with norm bounded by finitely many seminorms of its coefficients.

(d) The pairing ⟨v, w⟩_(μ_b) := ∫ ⟨v, w⟩_(ℂ^(N_E)) μ_b extends continuously to H_(b,c)^s × H_(b,−c)^(−s) and
identifies H_(b,−c)^(−s) with the dual of H_(b,c)^s; C_c^∞ is dense in both.

(e) For s′ > s and c′ > c the inclusion H_(b,c′)^(s′) ↪ H_(b,c)^s is compact.

(f) For s > d + 2, |(ϱ∂_ϱ)^j Z^α v| ≤ C ϱ^c ‖v‖_(H_(b,c)^s) for j + |α| ≤ d. Hence H_(b,c)^∞ := ∩_s H_(b,c)^s ⊂ 𝒜^c;
conversely 𝒜^c ⊂ H_(b,c−ϵ)^∞ for every ϵ > 0.

(g) For every k_0 ≥ 0 and M, ‖v‖_(H_(b,c−1)^s) ≤ e^(−k_0) ‖v‖_(H_(b,c)^s) + C_(k_0,M) ‖v‖_(H_(b,−M)^s).

(h) For integers m ≥ 0, ‖v‖²_(H_(b,c)^m) is equivalent to Σ_(j+|α|≤m) ‖e^(ct) ∂_t^j Z^α v‖²_(L²(μ_b)), and to
∫_ℝ ‖ℱ_t(e^(ct)v)(τ)‖²_(H_⟨τ⟩^m) dτ, where ‖w‖²_(H_μ^m) := ‖(1 + μ² + Δ)^(m/2) w‖²_(L²(𝕊³)). For m < 0 the second
equivalence holds with H_(b,c)^m normed as the dual of H_(b,−c)^(−m).

*Proof.* (a) For a second choice ψ′, (ψ′_k v) ∘ Φ_k = Σ_(|j−k|≤2) (ψ′_k ∘ Φ_k)(ψ_j v) ∘ Φ_k and
(ψ_j v) ∘ Φ_k = v_j ∘ (Φ_j⁻¹Φ_k), a dilation by e^(±(k−j)), |k − j| ≤ 2; (K1) (i)–(ii) bound each term by C‖v_j‖_(H^s),
uniformly, and the weights e^(2ck), e^(2cj) are comparable. (b) Let χ̃ ∈ C_c^∞({e⁻² < |y| < e²}) equal 1 near Ā. Then
(fv)_k = χ̃ (f ∘ Φ_k) v_k, and χ̃ (f ∘ Φ_k) is bounded in C_c^∞ uniformly in k, so (K1) (i) applies. For ϱ^γ,
ϱ^γ ∘ Φ_k = e^(−γk)|y|^(∓γ), and |y|^(∓γ) is smooth near Ā. (c) The operators ϱ∂_ϱ and Z_i commute with the
dilations, so (Bv)_k = Σ_(|j−k|≤1) (ψ_k ∘ Φ_k) B^(k)(v_j ∘ Φ_j⁻¹Φ_k), with B^(k) the operator with coefficients
f_(jα) ∘ Φ_k, bounded in C^∞ near Ā uniformly in k; a differential operator of order m with such coefficients maps
compactly supported elements of H^s to H^(s−m) boundedly, by (K1) (i) and ‖∂_i w‖_(H^(s−1)) ≤ ‖w‖_(H^s). (d) Let
J: v ↦ (e^(ck) v_k)_k, an isometry of H_(b,c)^s into ℓ²(ℤ; H^s), and L: (w_k)_k ↦ Σ_k e^(−ck)(χ̃ w_k) ∘ Φ_k⁻¹. Then
LJ = Id (as χ̃ = 1 on the support of v_k and Σ_k ψ_k = 1), and L is bounded from ℓ²(H^s) to H_(b,c)^s by (a)–(b), as
each point lies in at most three supports. The pairing: ⟨v, w⟩_(μ_b) = Σ_k ⟨ψ_k v, w⟩_(μ_b) =
Σ_k ∫ ⟨v_k, (χ̃w) ∘ Φ_k⟩ |y|⁻⁴ dy, and ‖(χ̃w) ∘ Φ_k‖_(H^(−s)) ≤ C Σ_(|j−k|≤2) ‖w_j‖_(H^(−s)), so Cauchy–Schwarz gives
|⟨v, w⟩_(μ_b)| ≤ C‖v‖_(H_(b,c)^s) ‖w‖_(H_(b,−c)^(−s)). Conversely a bounded functional ℓ on H_(b,c)^s gives the
functional ℓ ∘ L on ℓ²(H^s), represented by (g_k) ∈ ℓ²(H^(−s)); then ℓ(v) = ℓ(LJv) = ⟨v, w⟩_(μ_b) with
w := Σ_k e^(ck)(|y|⁴ χ̃ g_k) ∘ Φ_k⁻¹, and ‖w‖_(H_(b,−c)^(−s)) ≤ C‖(g_k)‖ by the same estimate. Density: truncate the sum
over k and mollify each piece. (e) For k_1 ∈ ℕ, the pieces with k ≤ k_1 form a compact map by (K3); for the rest,
Σ_(k>k_1) e^(2ck) ‖v_k‖²_(H^s) ≤ e^(−2(c′−c)k_1) ‖v‖²_(H_(b,c′)^(s′)). A norm-limit of compact maps is compact. (f) (K1)
(iii) on each piece gives |∂_y^β v_k| ≤ C e^(−ck) ‖v‖, and on A the fields ϱ∂_ϱ, Z_i are combinations of ∂_(y_j) with
smooth coefficients, the same for every k; ϱ^c is comparable to e^(−ck) there. Conversely, for v ∈ 𝒜^c,
‖v_k‖_(H^m) ≤ C_m e^(−ck), and Σ_k e^(2(c−ϵ)k) e^(−2ck) < ∞. (g) Split the sum at k = k_0: for k ≥ k_0,
e^(2(c−1)k) ≤ e^(−2k_0) e^(2ck); the finitely many k < k_0 give e^(2(c−1)k) ≤ C_(k_0,M) e^(−2Mk). (h) On each piece,
‖w‖_(H^m(ℝ⁴)) is equivalent to Σ_(|β|≤m) ‖∂_y^β w‖_(L²), and on A the coordinate change y ↦ (t, ω) is a fixed
diffeomorphism, which with Leibniz's rule for ψ_k gives the first equivalence. For the second, by Plancherel in t (K6)
and (K4) on 𝕊³, Σ_(j+|α|≤m) ‖∂_t^j Z^α u‖² is equivalent to ∫ Σ_ℓ (1 + τ² + ℓ(ℓ + 2))^m ‖(ℱ_t u)_ℓ(τ)‖² dτ, where
(·)_ℓ is the projection to ℋ_ℓ, u := e^(ct)v and [∂_t, e^(ct)] = c e^(ct); and (1 + τ² + ν)^m is equivalent to
Σ_(j≤m) τ^(2j)(1 + ν)^(m−j) for ν ≥ 0. For m < 0 both sides are the dual norms of the case −m, by (d) and Plancherel. ∎
