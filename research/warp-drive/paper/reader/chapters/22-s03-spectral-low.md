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

#### The Mellin transform {#sec:i-c-2-3}

For v supported in {t > t_0} with e^(c_0 t)v ∈ L²(μ_b) define the L²(𝕊³)-valued function

    (ℳv)(ι) := ∫_ℝ e^(ιt) v(t, ·) dt = ∫_0^∞ ϱ^(−ι) v dϱ/ϱ.

For Re ι < c_0 the integral converges absolutely (Cauchy–Schwarz with e^((Re ι − c_0)t) ∈ L²((t_0, ∞))), and ℳv is
holomorphic there. On the line Re ι = x ≤ c_0, ℳv(x + iτ) = ℱ_t(e^(xt)v)(−τ), so by (K6)

    ∫_ℝ ‖ℳv(x + iτ)‖² dτ = 2π‖e^(xt)v‖² ≤ 2π e^(2(x−c_0)t_0) ‖e^(c_0 t)v‖²,     x ≤ c_0,                  {#eq:i-c-2-1}

the last bound because e^(xt) ≤ e^((x−c_0)t_0) e^(c_0 t) for t > t_0. As x ↑ c_0, e^(xt)v → e^(c_0 t)v in L² by
dominated convergence, so the values on Re ι = c_0 are the L² limits of those on nearby lines. Integration by parts
gives ℳ((ϱ∂_ϱ)v) = ℳ(−∂_t v) = ι ℳv, and operators on 𝕊³ commute with ℳ. By [[lem:i-c-2-2]] (h), for integers m,

    ‖v‖²_(H_(b,c)^m)  is equivalent to  ∫_ℝ ‖ℳv(c + iτ)‖²_(H_⟨τ⟩^m) dτ.                                    {#eq:i-c-2-2}

**Lemma {#lem:i-c-2-3}** (Moving the line.) Let v be supported in {t > t_0} with e^(c_0 t)v ∈ L², and suppose that
ℳv extends holomorphically from {Re ι < c_0} to {Re ι < c_1}, c_1 > c_0, with
Ξ := sup_(c_0≤x<c_1) ∫ ‖ℳv(x + iτ)‖² dτ < ∞. Then e^(c_1 t)v ∈ L² and ‖e^(c_1 t)v‖² ≤ Ξ/2π.

*Proof.* The extension is continuous on Re ι = c_0, so it agrees there with the L² limits above. Let
φ ∈ C_c^∞(ℝ × 𝕊³) and Ψ(ι) := ∫ e^(−ιt) φ̄(t, ·) dt, which is entire, with ‖Ψ(x + iτ)‖_(L²(𝕊³)) ≤ C_X ⟨τ⟩⁻² for
|x| ≤ X (integrate by parts twice in t). Put g(ι) := ∫_(𝕊³) ℳv(ι) · Ψ(ι) dω, with a · b := Σ_k a_k b_k the bilinear
pairing on ℂ^(N_E); g is holomorphic on {Re ι < c_1}. For x ≤ c_0, Parseval for e^(xt)v and e^(−xt)φ gives
⟨v, φ⟩_(μ_b) = (2π)⁻¹ ∫_ℝ g(x + iτ) dτ. Fix x_0 < c_0 and x_1 ∈ [c_0, c_1). Then
∫_(x_0)^(x_1) ∫_ℝ |g(s + iT)| dT ds < ∞ by Cauchy–Schwarz, [[eq:i-c-2-1]] and the definition of Ξ, so there are
T_j → +∞ and T′_j → −∞ with ∫_(x_0)^(x_1) |g(s + iT_j)| ds → 0, and likewise at T′_j. Cauchy's theorem on the
rectangles [x_0, x_1] × [T′_j, T_j] then gives ∫ g(x_1 + iτ) dτ = ∫ g(x_0 + iτ) dτ, so

    |⟨v, φ⟩_(μ_b)| ≤ (2π)⁻¹ (∫ ‖ℳv(x_1 + iτ)‖² dτ)^(1/2) (∫ ‖Ψ(x_1 + iτ)‖² dτ)^(1/2) ≤ (Ξ/2π)^(1/2) ‖e^(−x_1 t)φ‖,

by (K6) for Ψ(x_1 + iτ) = ℱ_t(e^(−x_1 t)φ̄)(τ). So ‖e^(x_1 t)v‖² ≤ Ξ/2π; let x_1 ↑ c_1 (monotone convergence on
{t > 0}, dominated convergence on {t_0 < t ≤ 0}). ∎

#### The indicial family {#sec:i-c-2-4}

**Lemma {#lem:i-c-2-4}** Let J(ι) = −ι² + a_J ι + Δ + V_J + b_J, with a_J, b_J ∈ C^∞(𝕊³; End ℂ^(N_E)) and
V_J ∈ Diff¹(𝕊³; End ℂ^(N_E)), and let m be an integer.

(a) For X > 0 there is μ_X such that for |Re ι| ≤ X and |Im ι| ≥ μ_X, J(ι): H^m(𝕊³) → H^(m−2)(𝕊³) is invertible with
‖J(ι)⁻¹‖_(H_μ^(m−2) → H_μ^m) ≤ 2, where μ := Im ι.

(b) spec_J := {ι : ker J(ι) ∩ C^∞ ≠ 0} is discrete, with finitely many points in each strip {|Re ι| ≤ X}; off it
J(ι): H^m → H^(m−2) is invertible, and J⁻¹ is meromorphic on ℂ.

(c) If [x_0, x_1] ∩ Re spec_J = ∅, then sup{‖J(ι)⁻¹‖_(H_μ^(m−2) → H_μ^m) : x_0 ≤ Re ι ≤ x_1} < ∞, μ = Im ι.

*Proof.* (a) Write ι = x + iμ, so −ι² = μ² − x² − 2ixμ and J(ι) = (1 + μ² + Δ) + R with
R := −1 − x² − 2ixμ + a_J(x + iμ) + V_J + b_J. By (K4) and the spectral theorem, 1 + μ² + Δ is an isometry
H_μ^m → H_μ^(m−2), and ‖w‖_(H_μ^(m−j)) ≤ (1 + μ²)^(−j/2) ‖w‖_(H_μ^m) for j ≥ 0. Multiplication by a smooth function is
bounded on H_μ^k uniformly in μ, for every integer k: for k ≥ 0 because ‖w‖²_(H_μ^k) is equivalent, uniformly, to
Σ_(j≤k) μ^(2(k−j)) ‖w‖²_(H^j), by Leibniz's rule; for k < 0 by duality. Likewise V_J maps H_μ^k to H_μ^(k−1)
boundedly, uniformly in μ (for k ≥ 1 directly, for k ≤ 0 by duality with V_J^†). So

    ‖Rw‖_(H_μ^(m−2)) ≤ C(1 + |μ|) ‖w‖_(H_μ^(m−2)) + C‖w‖_(H_μ^(m−1)) ≤ C′(1 + |μ|)⁻¹ ‖w‖_(H_μ^m),

and a Neumann series inverts J(ι) with the stated bound once C′(1 + |μ|)⁻¹ ≤ ½. (b) J(ι) = (1 + Δ)(Id + F(ι)) on
H^m, with F(ι) := (1 + Δ)⁻¹(J(ι) − 1 − Δ) compact on H^m (it maps H^m to H^(m+1), and (K3)–(K4) give compactness on
𝕊³) and polynomial in ι. By (a), Id + F(ι) is invertible for some ι, so (K5) applies on D = ℂ. Id + F(ι) is Fredholm
of index 0, so it fails to be invertible exactly when it has a kernel; a kernel element of J(ι) in H^m is smooth by
(K4), so the exceptional set is spec_J for every m. In a strip it lies in {|Im ι| ≤ μ_X} by (a), a compact set, which
meets the discrete set in finitely many points. (c) On the part with |Im ι| ≥ μ_X, X := max(|x_0|, |x_1|), the bound is
2. The rest is compact, J⁻¹ is continuous there, and the μ-weighted norms are equivalent to the unweighted ones for
|μ| ≤ μ_X. ∎

For the end at ∞ the operator is P⁽⁰⁾, with ϱ∂_ϱ = ρ∂_ρ, and ℳ turns N(P⁽⁰⁾) into multiplication by I(ι), which has
the form of [[lem:i-c-2-4]] with spec_I = spec_b.

#### The model estimates {#sec:i-c-2-5}

Let L = Σ_(j=0)^2 B_j(ϱ)(ϱ∂_ϱ)^j on {t > t_0}, with B_j ∈ C^∞([0, e^(−t_0)); Diff^(2−j)(𝕊³; End ℂ^(N_E))), and with
*normal operator* N(L) := Σ_j B_j(0)(ϱ∂_ϱ)^j, whose Mellin symbol J(ι) := Σ_j B_j(0) ι^j has the form of
[[lem:i-c-2-4]]. Then L ∈ Diff_b^2 and L − N(L) ∈ ϱ Diff_b^2. Assume that L is *b-elliptic*: in the coordinates
(t, ω) its principal symbol is p Id with |p| ≥ c|(τ, η)|² on {t > t_0}, uniformly. (For N(L) the principal symbol is
that of −∂_t² + Δ.) Cut-offs below are functions of t, with χ̃ = 1 near the support of χ.

**Lemma {#lem:i-c-2-5}** (The b-elliptic estimate.) For all s, c and M there is C with

    ‖χv‖_(H_(b,c)^s) ≤ C(‖χ̃Lv‖_(H_(b,c)^(s−2)) + ‖χ̃v‖_(H_(b,c)^(−M))).

*Proof.* Under Φ_k the operator L becomes L^(k) on a neighbourhood of Ā, with coefficients bounded in C^∞ uniformly in
k and principal symbols elliptic with a uniform bound, as ϱ∂_ϱ and Z_i are dilation invariant and on A they are
combinations of ∂_(y_j) with fixed smooth coefficients. Apply (K2) to the family {L^(k)} and to v ∘ Φ_k itself, with
φ := (ψ_k χ) ∘ Φ_k and φ̃ equal to 1 near a compact neighbourhood of supp φ and supported in a fixed neighbourhood of
Ā where χ̃ ∘ Φ_k = 1. This is possible as χ̃ = 1 near supp χ, and only finitely many distinct pairs (φ, φ̃) are
needed, χ being constant outside a compact set of t. Then φ̃ (Lv) ∘ Φ_k = φ̃ (χ̃Lv) ∘ Φ_k, so
‖(ψ_k χ v) ∘ Φ_k‖_(H^s) is bounded by the pieces of χ̃Lv and of χ̃v on the neighbouring k, uniformly, and no commutator
with χ arises. Multiply by e^(2ck) and sum, using [[lem:i-c-2-2]] (a)–(c). ∎

**Lemma {#lem:i-c-2-6}** (The normal operator estimate; [Hin26c, (3.47)].) Let c ∉ Re spec_J and m ∈ ℤ. Then
‖v‖_(H_(b,c)^m) ≤ C‖N(L)v‖_(H_(b,c)^(m−2)) for v supported in {t > t_0}, and

    ‖χv‖_(H_(b,c)^m) ≤ C(‖χ̃Lv‖_(H_(b,c)^(m−2)) + ‖χ̃v‖_(H_(b,c−1)^m)).                                   {#eq:i-c-2-3}

*Proof.* By [[eq:i-c-2-2]], [[lem:i-c-2-2]] (h) and ℳ(N(L)v)(c + iτ) = J(c + iτ) ℳv(c + iτ), the first estimate is
[[lem:i-c-2-4]] (c) with x_0 = x_1 = c. For [[eq:i-c-2-3]] apply it to χv:
N(L)χv = χLv + [L, χ]v + (N(L) − L)χv. The commutator has coefficients supported in supp dχ, a compact set of t, where
all weights are equivalent; N(L) − L ∈ ϱ Diff_b^2 maps H_(b,c−1)^m to H_(b,c)^(m−2) by [[lem:i-c-2-2]] (b)–(c). The
transform of [[sec:i-c-2-3]] is defined for e^(c_0 t)v ∈ L²; so the first estimate is proved for v ∈ C_c^∞, whose
transform is entire, and extends by density ([[lem:i-c-2-2]] (d)) to every v ∈ H_(b,c)^m supported in {t > t_0}, both
sides being continuous on H_(b,c)^m. This covers m < 0, where it is used. ∎

**Lemma {#lem:i-c-2-7}** (Improving the weight.) Let (c_−, c_+) contain no real part of a point of spec_J, let
c ∈ (c_−, c_+), and suppose χ̃v ∈ H_(b,c)^∞ and χ̃Lv ∈ H_(b,c′)^∞ for every c′ < c_+. Then χv ∈ H_(b,c′)^∞ for every
c′ < c_+, so χv ∈ ∩_(c′<c_+) 𝒜^(c′).

*Proof.* Take nested cut-offs χ̃ = χ_0, χ_1, …, χ_p = χ, each equal to 1 near the support of the next. Suppose
χ_i v ∈ H_(b,c_i)^∞ with c_i ∈ (c_−, c_+), and fix x_1 < min(c_i + 1, c_+). Then

    f := N(L)χ_(i+1)v = χ_(i+1)Lv + [L, χ_(i+1)]v + (N(L) − L)χ_(i+1)v

lies in H_(b,c″)^∞ with c″ := min(c_i + 1, ½(x_1 + c_+)) > x_1: the first term by hypothesis, the second because it is
supported in a compact set of t inside {χ_i = 1}, the third by [[lem:i-c-2-2]] (b)–(c). So ℳf is holomorphic on
{Re ι < c″} with line norms bounded by [[eq:i-c-2-1]], and J(ι) ℳ(χ_(i+1)v)(ι) = ℳf(ι) for Re ι < c_i. The strip
{c_i − ϵ ≤ Re ι ≤ x′_1}, x_1 < x′_1 < c″, contains no root for ϵ small, so J⁻¹ℳf is holomorphic on its interior,
agrees with ℳ(χ_(i+1)v) near Re ι = c_i − ϵ, and has line norms bounded by [[lem:i-c-2-4]] (c) and [[eq:i-c-2-1]].
[[lem:i-c-2-3]], with c_0 := c_i − ϵ and c_1 := x′_1, gives χ_(i+1)v ∈ H_(b,x_1)^0; [[lem:i-c-2-5]] at the weight x_1,
with Lv ∈ H_(b,x_1)^∞ on the support of χ_(i+1), gives χ_(i+2)v ∈ H_(b,x_1)^∞. Each two steps raise the weight by any
amount less than min(1, c_+ − c_i), so finitely many reach every c′ < c_+. The last claim is [[lem:i-c-2-2]] (f). ∎

#### The spaces on X̄ {#sec:i-c-2-6}

Fix R_1 > r_e + 1 so large that {r ≥ R_1} ⊂ {ρ < ρ_1} and P⁽⁰⁾ is b-elliptic on {r ≥ ½R_1} (possible by (H2), its
b-principal symbol being that of (ρD_ρ)² + Δ plus O(ρ)), and let χ_∂ = χ_∂(r) with χ_∂ = 0 on {r ≤ R_1} and χ_∂ = 1
on {r ≥ 2R_1}.

**Definition {#def:i-c-2-8}** (The spaces of [Hin26c, (3.72)] in dimension 4 + 1.) For s, a ∈ ℝ,

    ‖u‖²_(H̄_b^(s,a)) := ‖(1 − χ_∂)u‖²_(H̄^s) + ‖χ_∂ u‖²_(H_(b,a+2)^s),

with H̄^s extendible at ∂_♯X ([[sec:i-a-6-1]]) and H_(b,a+2)^s of [[def:i-c-2-1]] at the end at ∞; Ḣ_b^(s,a) is
defined with Ḣ^s (supported at ∂_♯X) in the first term. H̄_b^((s;k),a) := H̄_b^(s+k,a) (for b-spaces, b-regularity is
regularity).

By [[lem:i-c-2-2]], near ∂X the norm is that of ρ^a H_b^s(|dx|) = ρ^(a+2) H_b^s(μ_b), as |dx| = ρ⁻⁴μ_b; the b-weight is
a + 2. The space does not depend on R_1 or χ_∂, up to equivalent norms.

**Lemma {#lem:i-c-2-9}** (a) The L²(|dx|) pairing identifies the dual of H̄_b^(s,a) with Ḣ_b^(−s,−a).
(b) For s′ > s and a′ > a, the inclusion H̄_b^(s′,a′) ↪ H̄_b^(s,a) is compact.
(c) ([Hin26c, (3.72)] in dimension 4 + 1.) H̄_b^(d+3,a) ⊂ ρ^(a+2) C_b^d near ∂X; in particular
H̄_b^(∞,β−2) ⊂ 𝒜^β near ∂X, and 𝒜^β ⊂ H̄_b^(∞,β−2−ϵ) near ∂X for ϵ > 0.
(d) P̂(0) maps H̄_b^(s,a) to H̄_b^(s−2,a+2) and Ḣ_b^(s,a) to Ḣ_b^(s−2,a+2).

*Proof.* (a) Near ∂X, ⟨u, v⟩_(|dx|) = ⟨u, ρ⁻⁴v⟩_(μ_b), and v ↦ ρ⁻⁴v maps H_(b,−a+2)^(−s) (the b-weight of
Ḣ_b^(−s,−a)) onto H_(b,−a−2)^(−s), the dual of H_(b,a+2)^s ([[lem:i-c-2-2]] (b), (d)); in the interior it is
[[lem:i-a-6-1]] (b); glue with χ_∂. (b) [[lem:i-c-2-2]] (e) and (K3). (c) [[lem:i-c-2-2]] (f) with d + 3 > d + 2.
(d) Near ∂X, P̂(0) = ρ²P⁽⁰⁾, and [[lem:i-c-2-2]] (b)–(c). ∎

### The zero energy operator {#sec:i-c-3}

With s and α as in [[sec:i-c-1-2]] let

    𝒳_0 := {u ∈ H̄_b^(s,α) : P̂(0)u ∈ H̄_b^(s−1,α+2)},     𝒴_0 := H̄_b^(s−1,α+2),
    𝒳_0^* := {v ∈ Ḣ_b^(1−s,−α−2) : P̂(0)^(*h)v ∈ Ḣ_b^(−s,−α)},                                           {#eq:i-c-3-1}

Hilbert spaces with the graph norms; 𝒳_0 → 𝒴_0 is [Hin26c, (9.108)], and 𝒴_0^* = Ḣ_b^(1−s,−α−2) by
[[lem:i-c-2-9]] (a).

**Theorem {#thm:i-c-3-1}** (The zero energy operator.) Assume (H1)–(H4) and (G), with s > ½ + ϑ_ℋ constant.

(1) (*Fredholm estimates.*) For every M there is C with

    ‖u‖_(H̄_b^(s,α)) ≤ C(‖P̂(0)u‖_(H̄_b^(s−1,α+2)) + ‖u‖_(H̄_b^(−M,−M))),     u ∈ 𝒳_0,                      {#eq:i-c-3-2}

    ‖v‖_(Ḣ_b^(1−s,−α−2)) ≤ C(‖P̂(0)^(*h)v‖_(Ḣ_b^(−s,−α)) + ‖v‖_(Ḣ_b^(−M,−M))),     v ∈ 𝒳_0^*.             {#eq:i-c-3-3}

P̂(0): 𝒳_0 → 𝒴_0 is Fredholm, and the annihilator of its range in 𝒴_0^* is ker_(𝒳_0^*) P̂(0)^(*h).

(2) (*Kernel.*) Every u ∈ H̄_b^(s,α) with P̂(0)u = 0 is smooth up to ∂_♯X and lies in 𝒜^β near ∂X for every
β < β_+.

(3) (*Independence.*) The kernel and the annihilator of the range depend neither on s > ½ + ϑ_ℋ nor on α with
α + 2 ∈ I; nor, therefore, does the index.

(4) (*Invertibility.*) If (Z) holds for one such pair (s, α), it holds for all, and then [[eq:i-c-3-2]]–[[eq:i-c-3-3]]
hold without their last terms.

This is [Hin26c, Theorem 9.36] in dimension 4 + 1, on E. The weight on P̂(0)^(*h)v in [[eq:i-c-3-3]] is −α, the dual
of the weight α of the domain; [Hin26c, (9.107)] prints −α − 2 (see [[sec:s03-remarks]]).

#### Proof of (1) {#sec:i-c-3-1}

*Proof of [[thm:i-c-3-1]] (1).* *The interior.* Let χ, χ_1 and b′ < b″ be as in [[cor:i-a-6-5]], χ_far := 1 − χ,
and φ_j ∈ C_c^∞({r < jR_1}) equal to 1 on {r ≤ (j − 1)R_1}, j = 3, 4, 5. Run the pieces (A), (B) and (F) of
[[sec:i-a-7-1]] at σ = 0 for φ_3 χ_far u: [[prop:i-a-4-2]] (1) at the horizon (σ = 0 lies in its compact sets
𝒟 ⊂ {Im σ ≥ 0}), [[prop:i-a-5-2]] along the curves of (H4), which lie over {r ≤ r_e}, and [[prop:i-a-5-1]] on the
rest of fibre infinity over {r < 3R_1}; at finite frequencies over a compact set every operator of order −∞ is bounded
by ‖u‖_(H^(−M)) there. With [[eq:i-a-6-1]] at σ = 0 for χu this gives, with s > s_0 > ½ + ϑ_ℋ,

    ‖(1 − χ_∂)u‖_(H̄^s) ≤ C(‖P̂(0)u‖_(H̄^(s−1)({r<4R_1})) + ‖φ_4 u‖_(H̄^(s_0)) + ‖φ_4 u‖_(H̄^(−M))),

as 1 − χ_∂ = (1 − χ_∂)(χ + φ_3 χ_far). By (K3) and Ehrling's lemma,
‖φ_4 u‖_(H̄^(s_0)) ≤ δ‖φ_5 u‖_(H̄^s) + C_δ‖φ_5 u‖_(H̄^(−M)), and over {r < 5R_1} the norms of H̄_b^(s,α) and H̄^s are
equivalent. So

    ‖(1 − χ_∂)u‖_(H̄^s) ≤ C‖P̂(0)u‖_(H̄_b^(s−1,α+2)) + Cδ‖u‖_(H̄_b^(s,α)) + C_δ‖u‖_(H̄_b^(−M,−M)).          {#eq:i-c-3-4}

*Near ∂X.* Let χ̃_∂ be supported in {r > ½R_1} and equal to 1 near supp χ_∂. [[lem:i-c-2-5]] for L = P⁽⁰⁾ at the
b-weight α + 2, with χ̃_∂P⁽⁰⁾u = χ̃_∂ρ⁻²P̂(0)u, gives

    ‖χ_∂ u‖_(H_(b,α+2)^s) ≤ C(‖P̂(0)u‖_(H̄_b^(s−2,α+2)) + ‖χ̃_∂ u‖_(H_(b,α+2)^(−M))),

the b-weight of H̄_b^(s−2,α+2) being α + 4 and [[lem:i-c-2-2]] (b) moving ρ⁻². Choose M ∈ ℕ. By [[lem:i-c-2-6]] at
c = α + 2 (not a real part of a root, by (G)), with cut-offs χ̃_∂ and χ̃′, and [[lem:i-c-2-2]] (g),

    ‖χ̃_∂ u‖_(H_(b,α+2)^(−M)) ≤ C‖P̂(0)u‖_(H̄_b^(−M−2,α+2)) + Ce^(−k_0)‖χ̃′u‖_(H_(b,α+2)^(−M))
                                 + C_(k_0)‖χ̃′u‖_(H_(b,−M)^(−M)).

Here χ̃′ − χ̃_∂ has compact support in {r > ¼R_1}, where all weights are equivalent, so
‖χ̃′u‖_(H_(b,α+2)^(−M)) ≤ ‖χ̃_∂ u‖_(H_(b,α+2)^(−M)) + C‖u‖_(H̄_b^(−M,−M)), and
‖χ̃′u‖_(H_(b,−M)^(−M)) ≤ C‖u‖_(H̄_b^(−M,−M)). Take k_0 with Ce^(−k_0) ≤ ½; the left side is finite because
u ∈ H̄_b^(s,α), so it absorbs the middle term. With [[eq:i-c-3-4]], and δ small, this proves [[eq:i-c-3-2]].

*The adjoint.* Let v ∈ 𝒳_0^*. In the interior run the adjoint chain of [[sec:i-a-7-1]] at σ = 0 over {r < 4R_1}:
[[eq:i-a-6-2]] at the artificial boundary, which needs nothing but P̂(0)^(*h)v; (B*), [[prop:i-a-5-2]] for
P̂(0)^(*h) with the backward field from there to the horizon; (A*), [[prop:i-a-4-2]] (2), whose E-term lies in the
region of (B*); and (F). No a priori term arises. Near ∂X,

    ρ⁻²P̂(0)^(*h) = H⁻¹ ρ² (P⁽⁰⁾)^(†_b) ρ⁻² H,

where †_b denotes the adjoint for μ_b and the standard inner product. It is b-elliptic, with (ρ∂_ρ)^(†_b) = −ρ∂_ρ,
and its normal operator has the Mellin symbol

    I^♯(ι) := H_0⁻¹ I(2 − ῑ)^† H_0 = −ι² + (4 − a^(*h))ι + Δ + V^(*h) + b^(*h) + 2a^(*h) − 4,               {#eq:i-c-3-5}

which is of the form of [[lem:i-c-2-4]] once Δ in [[eq:i-c-3-5]] is read as H_0⁻¹ΔH_0, which differs from Δ by a
first-order operator; and spec_(I^♯) = {2 − μ̄ : μ ∈ spec_b}.

These facts are verified as follows. For an operator A, ⟨Au, v⟩_(|dx|) = ⟨Au, ρ⁻⁴v⟩_(μ_b) =
⟨u, ρ⁴A^(†_b)ρ⁻⁴v⟩_(|dx|), so the adjoint for |dx| = ρ⁻⁴μ_b is A^† = ρ⁴A^(†_b)ρ⁻⁴; for A = ρ²P⁽⁰⁾ this is
ρ⁴(P⁽⁰⁾)^(†_b)ρ⁻², and as A^(*h) = H⁻¹A^†H with ρ commuting with H, ρ⁻²P̂(0)^(*h) = H⁻¹ρ²(P⁽⁰⁾)^(†_b)ρ⁻²H. Its
normal operator is H_0⁻¹ρ²N(P⁽⁰⁾)^(†_b)ρ⁻²H_0, and N(P⁽⁰⁾)^(†_b) = Σ_j (−ρ∂_ρ)^j A_j(0)^† = Σ_j A_j(0)^†(−ρ∂_ρ)^j,
the A_j(0) not depending on ρ. For w ∈ C^∞(𝕊³; ℂ^(N_E)),

    ρ² N(P⁽⁰⁾)^(†_b) ρ⁻² (ρ^ι w) = ρ^ι Σ_j A_j(0)^† (2 − ι)^j w = ρ^ι (Σ_j A_j(0)(2 − ῑ)^j)^† w = ρ^ι I(2 − ῑ)^† w,

which gives the first equality in [[eq:i-c-3-5]]. For the second, I(2 − ῑ) = −(2 − ῑ)² + a(2 − ῑ) + Δ + V + b, and
taking adjoints, with Δ self-adjoint and scalar factors conjugated,

    I(2 − ῑ)^† = −(2 − ι)² + (2 − ι)a^† + Δ + V^† + b^† = −ι² + (4 − a^†)ι + Δ + V^† + b^† + 2a^† − 4;

conjugation by H_0 turns a^†, V^†, b^† into a^(*h), V^(*h), b^(*h) and Δ into H_0⁻¹ΔH_0. Finally, by the proof of
[[lem:i-c-2-4]] (b), I(κ): H^m → H^(m−2) is Fredholm of index 0 for every κ ∈ ℂ, so I(κ)^† has a nontrivial kernel
exactly when I(κ) has, that is, when κ ∈ spec_b (kernel elements being smooth by (K4)); with κ = 2 − ῑ this is
ι ∈ {2 − μ̄ : μ ∈ spec_b}. Thus conjugation by ρ^(±2) shifts the roots by 2, and the †_b-adjoint reflects them.

v has b-weight −α − 2 + 2 = −α, and −α ∉ Re spec_(I^♯) if and only if α + 2 ∉ Re spec_b, which (G) gives.
[[lem:i-c-2-5]], [[lem:i-c-2-6]] and [[lem:i-c-2-2]] (g) for this operator, as above, give [[eq:i-c-3-3]], the target
weight being −α: ρ⁻²P̂(0)^(*h)v ∈ H_(b,−α)^(−1−s) is P̂(0)^(*h)v in the b-weight −α + 2, which is that of
Ḣ_b^(−s,−α).

*Fredholm.* By [[lem:i-c-2-9]] (b) the inclusion 𝒳_0 ↪ H̄_b^(−M,−M) is compact for M > max(−s, −α), so
[[eq:i-c-3-2]] gives a finite-dimensional kernel and closed range (Peetre's lemma), and [[eq:i-c-3-3]] does the same
for P̂(0)^(*h) on 𝒳_0^*. *Green's formula*: ⟨P̂(0)u, v⟩ = ⟨u, P̂(0)^(*h)v⟩ for u ∈ 𝒳_0, v ∈ 𝒳_0^*, with the
h-weighted L²(|dx|) pairings of [[sec:i-a-7-3]]. Split with χ_∂. For (1 − χ_∂)u it is the proof in [[sec:i-a-7-3]].
Near ∂X, [[lem:i-c-2-5]] gives χ_∂u ∈ H_(b,α+2)^(s+1) and χ̃_∂v ∈ H_(b,−α)^(2−s); both sides of the formula are
continuous in χ_∂u ∈ H_(b,α+2)^(s+1) for fixed v ([[lem:i-c-2-9]] (a), (d)), and for χ_∂u ∈ C_c^∞ the formula is the
definition of P̂(0)^(*h)v as a distribution; [[lem:i-c-2-2]] (d) gives the density. *Cokernel*: an element of 𝒴_0^*
annihilating the range annihilates P̂(0)C_c^∞(X̄°), so it solves P̂(0)^(*h)v = 0 and lies in 𝒳_0^*; conversely use
Green's formula. ∎

#### Proof of (2) {#sec:i-c-3-2}

*Proof of [[thm:i-c-3-1]] (2).* Let u ∈ H̄_b^(s,α) with P̂(0)u = 0. In the interior the estimates of [[sec:i-c-3-1]]
hold in the strong sense ([[rem:i-a-7-3]]: [[prop:i-a-4-2]] (1), [[prop:i-a-5-1]], [[prop:i-a-5-2]] and
[[cor:i-a-6-5]] do), with the a priori term at the horizon given by the order s of u, so u ∈ H̄^(s′) on {r < 3R_1}
for every s′: u is smooth up to ∂_♯X. Near ∂X, [[lem:i-c-2-5]] at every order gives χ_∂u ∈ H_(b,α+2)^∞, and
[[lem:i-c-2-7]] for L = P⁽⁰⁾, with (c_−, c_+) = I and c = α + 2, gives χ_∂u ∈ 𝒜^β for every β < β_+. In [Hin26c]
this step is a contour shift through (9.109); here it is done by [[lem:i-c-2-3]] and [[lem:i-c-2-7]]. ∎

#### Proof of (3) and (4) {#sec:i-c-3-3}

*Proof of [[thm:i-c-3-1]] (3) and (4).* *Kernel.* By (2), every kernel element u for (s, α) is smooth up to ∂_♯X and
in 𝒜^β near ∂X for all β < β_+; by [[lem:i-c-2-9]] (c) it lies in H̄_b^(s′,α′) for every s′ and every α′ with
α′ + 2 < β_+, so it is a kernel element for every pair (s′, α′).

*Annihilator.* Let v ∈ ker_(𝒳_0^*) P̂(0)^(*h) for (s, α). Near ∂X, [[lem:i-c-2-5]] gives χ̃_∂v ∈ H_(b,−α)^∞, and
[[lem:i-c-2-7]] for ρ⁻²P̂(0)^(*h), whose gap containing −α is (2 − β_+, 2 − β_−), gives χ_∂v ∈ H_(b,c′)^∞ for every
c′ < 2 − β_−; this is the b-weight −α′ of Ḣ_b^(1−s′,−α′−2) whenever α′ + 2 > β_−. In the interior, the adjoint
estimates of [[sec:i-c-3-1]] hold in the strong sense ([[rem:i-a-7-3]]) at every order 1 − s′ with s′ > ½ + ϑ_ℋ: at the
horizon the adjoint estimate is below threshold and needs no a priori condition beyond v ∈ H^(−M), and [[eq:i-a-6-2]]
and propagation hold at every order. So v is an annihilator for every pair (s′, α′).

So kernels and annihilators do not depend on the pair, and neither does the index. (4) follows: if one pair has
trivial kernel and annihilator, all do. Without the last terms: if ‖u_j‖_(H̄_b^(s,α)) = 1 and ‖P̂(0)u_j‖ → 0, then by
[[lem:i-c-2-9]] (b) a subsequence converges in H̄_b^(−M,−M), by [[eq:i-c-3-2]] it is Cauchy in 𝒳_0, and its limit is a
kernel element of norm 1, a contradiction; likewise for [[eq:i-c-3-3]]. ∎

**Remark {#rem:i-c-3-2}** ([Hin26c, Remark 9.37].) [Hin26c] notes that the error term of [[eq:i-c-3-2]] may be taken
at orders s^♭ < s and α^♭ < α with α^♭ + 2 in the same gap, and that the kernel is polyhomogeneous. Neither is used
below, and neither is proved here.
