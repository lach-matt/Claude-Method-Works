# Part. The stability theory, III: the Myers–Perry family and the linear theory at low energy {#part:stability-linear}

## Harmonics on 𝕊³, the Myers–Perry family, the gauge-fixed Einstein equation and partial polyhomogeneity {#ch:s11}

This chapter sets up the objects on which the linear theory of the following chapters is built, and the tools for
proving partial expansions. It writes out [Hin26, Sections 2–4] in dimension 4 + 1, in three parts.

[[sec:iii-a1-1]] and [[sec:iii-a1-2]] carry [Hin26, Section 2.4, pp. 63–67]: the decomposition of functions, 1-forms
and symmetric 2-tensors on the sphere at infinity into harmonics of scalar, vector and tensor type; the identities
between the geometric operators on each type and the special low degrees; the Minkowski wave operator, symmetric
gradient and divergence in the null splittings near infinity ([Hin26, Lemma 2.29]); the types these operators preserve;
the indicial roots by type; and the indicial families of the symmetric gradient with their kernels. On 𝕊³ the constants
of [Hin26, Lemma 2.29] change, and one type is new: trace-free divergence-free symmetric 2-tensors, which 𝕊² does not
carry. Every statement is proved on the unit sphere 𝕊^ν and on ℝ^(1+(ν+1)) for general ν ≥ 2, from the Ricci identity
and the Gauss formula, and then read at ν = 3. At ν = 2 each formula is the corresponding one of [Hin26], entry by
entry.

[[sec:iii-b-1]] to [[sec:iii-b-6]] carry [Hin26, Sections 3 and 4, pp. 68–83]: the compactified spacetime and its
charts; the black hole family, here the Myers–Perry family, as smooth metrics on it with their decay at infinity; time
functions, linearised metrics and initial data; null coordinates near null infinity; cut-off Lorentz boosts and the
pullback of the family by them; and the gauge-fixed Einstein equation with its linearisation. In five dimensions the
family can be written for every spin at once in Kerr–Schild form, and the ingoing and outgoing Eddington–Finkelstein
times of the family differ by a function in |x|⁻¹C^∞, where in four dimensions they differ by 4m log r. So the
Kerr–Schild coordinates, in which the family is regular across the future event horizon, are smooth coordinates on the
compactification, and a change of time function that is the identity near the horizon puts the family into the outgoing
form used at null infinity. The causal character of every time function is read off from one algebraic inequality
([[lem:iii-b-3-3]] (e)), and the boost lemma is proved with the exact Lorentz boost. The inner radius r_♭ of the
spacetime is a parameter: every result of these sections holds for every r_♭ ∈ (0, ½R₁], with R₁ the radius fixed by
the mass in [[sec:iii-b-2]].

[[sec:iii-a-1]] to [[sec:iii-a-4]] carry [Hin26, Sections 2.1–2.3, pp. 44–63]: b-analysis and partial
polyhomogeneity, the scattering and 3b-notions in dimension 4 + 1, the integration of the b-vector fields x∂_x and
x∂_x − y∂_y, and the Fourier transform with partial expansions. The first, third and fourth are stated in [Hin26] for
manifolds with corners of any dimension or for ℝⁿ with any n; their proofs are given here in full. The Fourier
transform statements rest on [[prop:ii-g1-3-3]] and [[prop:ii-g1-3-5]], which hold in dimension 4 + 1.

*Notation.* In [[sec:iii-a1-1]] and [[sec:iii-a1-2]] the letter ν ≥ 2 is the dimension of the sphere 𝕊^ν, and
D := ρ∂_ρ. The variable of an indicial family, written λ in [Hin26], is written ι, and the Mellin variable of the
normal operator at sf in [[sec:iii-a-2]], also written λ in [Hin26], is written ϰ, as in [[ch:s16]]. The letter ι also
names two boundary faces, future timelike infinity ι⁺ from [[sec:iii-b-2]] on, and the face ι of [[sec:iii-a-4]], as in
[[sec:ii-g1-3-1]], where no indicial variable occurs; in [[sec:iii-b-6]], ι_V h := h(V, ·) is the interior product. In
[[sec:iii-b-1]] to [[sec:iii-b-6]] the letter m is the mass parameter of the family; in [[sec:iii-a-1]] to
[[sec:iii-a-4]] it is the order of a differential operator. The spacetime dimension is written 5. The letter σ is the
spectral parameter of [[sec:iii-a-2]] and [[sec:iii-a-4]] only.

### Harmonics on the sphere {#sec:iii-a1-1}

Let ν ≥ 2, let g̸ be the round metric of the unit sphere 𝕊^ν ⊂ ℝ^(ν+1), and use the conventions of [Hin26, Notation
2.26]: Δ̸ := −tr ∇̸² is the non-negative rough Laplacian on tensors, δ̸ω := −∇̸^a ω_a, (δ̸h)_a := −∇̸^b h_ab,
(δ̸*ω)_ab := ½(∇̸_a ω_b + ∇̸_b ω_a), and

    δ̸*₀ := δ̸* + (1/ν) g̸ δ̸,                                                                           {#eq:iii-a1-1-1}

the trace-free part of δ̸* (tr δ̸*ω = −δ̸ω); at ν = 2 this is the operator δ̸* + ½g̸δ̸ of [Hin26]. On functions
Δ̸ = δ̸d. The curvature is R̸(X, Y)Z = ⟨Y, Z⟩X − ⟨X, Z⟩Y, so that on 1-forms
∇̸_a∇̸_b ω_c − ∇̸_b∇̸_a ω_c = g̸_ac ω_b − g̸_bc ω_a, and Ric(g̸) = (ν − 1)g̸.

*Ambient picture.* Write x̂ for the position on 𝕊^ν. A 1-form on 𝕊^ν is identified, through g̸, with a tangential vector
field V : 𝕊^ν → ℝ^(ν+1), V · x̂ = 0, and a symmetric 2-tensor with a tangential symmetric matrix field Q, Q x̂ = 0; g̸
itself is P := I − x̂ ⊗ x̂. Put x̂ ⊙ V := x̂ ⊗ V + V ⊗ x̂. D_X denotes the flat derivative along X of ℝ^(ν+1)- or
matrix-valued functions on 𝕊^ν, and Δᵉ is Δ̸ applied to each Cartesian component as a function.

**Lemma {#lem:iii-a1-1-1}** (Commutators on the unit sphere.) For every function S, 1-form ω and symmetric 2-tensor h
on 𝕊^ν:

(a) Δ̸ dS = dΔ̸S − (ν − 1) dS;

(b) 2δ̸δ̸*ω = dδ̸ω + Δ̸ω − (ν − 1)ω;

(c) Δ̸δ̸*ω = δ̸*Δ̸ω − (ν + 1)δ̸*ω − 2g̸ δ̸ω;

(d) δ̸Δ̸ω = Δ̸δ̸ω − (ν − 1)δ̸ω and δ̸Δ̸h = Δ̸δ̸h − (ν + 1)δ̸h − 2d tr h.

*Proof.* Contracting the Ricci identity, ∇̸^d∇̸_a ω_d = ∇̸_a∇̸^d ω_d + (ν − 1)ω_a. (a) With ω = dS and the symmetry of
the Hessian, −(Δ̸dS)_a = ∇̸^d∇̸_d∇̸_a S = ∇̸^d∇̸_a∇̸_d S = ∇̸_a∇̸^d∇̸_d S + (ν − 1)∇̸_a S. (b)
2(δ̸δ̸*ω)_b = −∇̸^a∇̸_a ω_b − ∇̸^a∇̸_b ω_a = (Δ̸ω)_b − ∇̸_b∇̸^a ω_a − (ν − 1)ω_b. (c) For a 2-tensor S_eb the Ricci
identity gives ∇̸_d∇̸_a S_eb − ∇̸_a∇̸_d S_eb = −g̸_ae S_db + g̸_de S_ab − g̸_ab S_ed + g̸_db S_ea; contracting d with e
and taking S_db := ∇̸_d ω_b, so that ∇̸^d S_db = −(Δ̸ω)_b and tr S = −δ̸ω,

    ∇̸^d∇̸_a∇̸_d ω_b = −∇̸_a(Δ̸ω)_b + (ν − 1)∇̸_a ω_b + ∇̸_b ω_a + g̸_ab δ̸ω.

With ∇̸_d∇̸_a ω_b = ∇̸_a∇̸_d ω_b + g̸_db ω_a − g̸_ab ω_d this yields

    −(Δ̸∇̸ω)_ab = ∇̸^d∇̸_d∇̸_a ω_b = −∇̸_a(Δ̸ω)_b + (ν − 1)∇̸_a ω_b + 2∇̸_b ω_a + 2g̸_ab δ̸ω,

and symmetrising in a, b gives (c). (d) are the formal adjoints of (a) and (c): the adjoint of d on functions is δ̸, of
δ̸* is δ̸, of g̸· is tr, Δ̸ is formally self-adjoint, and two differential operators agree if and only if their formal
adjoints do. ∎

**Lemma {#lem:iii-a1-1-2}** (Ambient identities.) For a function f, a tangential vector field V and a tangential
symmetric matrix field Q on 𝕊^ν:

    Δᵉ(f x̂) = (Δ̸f + νf) x̂ − 2∇̸f,                                                                    {#eq:iii-a1-1-2a}

    ΔᵉV = (Δ̸ + 1)V − 2(δ̸V) x̂,                                                                        {#eq:iii-a1-1-2b}

    Δᵉ(f x̂ ⊗ x̂) = (Δ̸f + 2νf) x̂ ⊗ x̂ − 2fP − 2x̂ ⊙ ∇̸f,                                              {#eq:iii-a1-1-2c}

    Δᵉ(x̂ ⊙ V) = x̂ ⊙ (Δ̸ + ν + 3)V − 4(δ̸V) x̂ ⊗ x̂ − 4δ̸*V,                                           {#eq:iii-a1-1-2d}

    ΔᵉQ = (Δ̸ + 2)Q − 2x̂ ⊙ δ̸Q − 2(tr Q) x̂ ⊗ x̂.                                                      {#eq:iii-a1-1-2e}

*Proof.* By the Gauss formula of the unit sphere, D_X x̂ = X, D_X V = ∇̸_X V − ⟨X, V⟩x̂, and, writing
Q = Σ q_bc e_b ⊗ e_c in a frame, D_X Q = ∇̸_X Q − x̂ ⊙ Q(X) with Q(X) := Σ q_bc X^b e_c. At a point take an orthonormal
frame (e_a) with ∇̸e_a = 0 there; then D_(e_a)e_a = −x̂ and Δᵉ = −Σ_a D_(e_a)D_(e_a) there; write D_a := D_(e_a).
[[eq:iii-a1-1-2b]]: e_a⟨e_a, V⟩ = ⟨e_a, ∇̸_a V⟩ there, so
Σ_a D_aD_aV = Σ_a(∇̸_a∇̸_a V − 2⟨e_a, ∇̸_a V⟩x̂ − ⟨e_a, V⟩e_a) = −Δ̸V + 2(δ̸V)x̂ − V. [[eq:iii-a1-1-2a]],
[[eq:iii-a1-1-2c]]: the product rule Δᵉ(uv) = (Δᵉu)v + uΔᵉv − 2Σ_a(D_a u)(D_a v) with Δᵉx̂ = νx̂, Σ_a(e_a f)e_a = ∇̸f and
Σ_a e_a ⊗ e_a = P. [[eq:iii-a1-1-2d]]: by the product rule and [[eq:iii-a1-1-2b]],
Δᵉ(x̂ ⊗ V) = νx̂ ⊗ V + x̂ ⊗ ((Δ̸ + 1)V − 2(δ̸V)x̂) − 2Σ_a e_a ⊗ (∇̸_a V − ⟨e_a, V⟩x̂); adding the transpose and using
Σ_a(e_a ⊗ ∇̸_a V + ∇̸_a V ⊗ e_a) = 2δ̸*V gives [[eq:iii-a1-1-2d]]. [[eq:iii-a1-1-2e]]:
Σ_a D_aD_aQ = Σ_a(∇̸_a∇̸_a Q − x̂ ⊙ (∇̸_a Q)(e_a) − e_a ⊙ Q(e_a) − x̂ ⊙ D_a(Q(e_a))) with
D_a(Q(e_a)) = (∇̸_a Q)(e_a) − Q(e_a, e_a)x̂, Σ_a(∇̸_a Q)(e_a) = −δ̸Q and Σ_a e_a ⊙ Q(e_a) = 2Q. As a check,
[[eq:iii-a1-1-2e]] at Q = P and [[eq:iii-a1-1-2c]] at f = 1 give ΔᵉP = −Δᵉ(x̂ ⊗ x̂) = 2P − 2νx̂ ⊗ x̂. ∎

**Definition {#def:iii-a1-1-3}** (Spherical harmonics; [Hin26, Definition 2.27] in dimension 4 + 1.) For l ∈ ℕ₀ let
k_l² := l(l + ν − 1).

(1) 𝒮_l := ker(Δ̸ − k_l²) ⊂ C^∞(𝕊^ν).

(2) For l ≥ 1, 𝒱_l := {V ∈ C^∞(𝕊^ν; T*𝕊^ν) : δ̸V = 0, Δ̸V = (k_l² − 1)V}. A 1-form is of *scalar type* l if it is dS,
S ∈ 𝒮_l, and of *vector type* l if it lies in 𝒱_l.

(3) For l ≥ 2, 𝒯_l := {T ∈ C^∞(𝕊^ν; S²T*𝕊^ν) : tr T = 0, δ̸T = 0, Δ̸T = (k_l² − 2)T}. A symmetric 2-tensor is of
*scalar type* l if it is δ̸*₀dS + S′g̸ with S, S′ ∈ 𝒮_l; of *vector type* l if it is δ̸*V, V ∈ 𝒱_l; of *tensor type*
l if it lies in 𝒯_l.

On 𝕊² there are no nonzero trace-free divergence-free symmetric 2-tensors, and 𝒱_l = {⋆dS : S ∈ 𝒮_l} ([Hin26, p. 64],
from [Hig87]); this is not used below. On 𝕊³ the tensor type is not empty. With z := x₁ + ix₂, w := x₃ + ix₄ and
β := z dw − w dz, a tangential 1-form, T := z^(l−2) β ⊗ β restricted to 𝕊³ lies in 𝒯_l ⊗ ℂ for every l ≥ 2. Indeed,
with the Euclidean product extended bilinearly, dz · dz = dw · dw = dz · dw = 0, so β · β = 0, β · dz = β · dw = 0 and
β · x = 0; and ∂_iβ_i = 0. Hence T is tangential (Tx = z^(l−2)β(β · x) = 0) and trace-free, its Euclidean divergence
β(β · ∇z^(l−2)) + z^(l−2)((∂_iβ_i)β + (β · ∇)β) vanishes, and its Cartesian components are holomorphic polynomials in
(z, w), so harmonic and homogeneous of degree l. By [[lem:iii-a1-1-4]] (1) each component restricted to 𝕊³ lies in
𝒮_l ⊗ ℂ, so ΔᵉT = k_l²T, and [[eq:iii-a1-1-2e]] with tr T = 0 gives k_l²T = (Δ̸ + 2)T − 2x̂ ⊙ δ̸T. The first term on the
right is tangential and the second has no tangential part, so δ̸T = 0 and Δ̸T = (k_l² − 2)T.

**Lemma {#lem:iii-a1-1-4}** (Spectra.) (1) 𝒮_l consists of the restrictions of the harmonic homogeneous polynomials of
degree l on ℝ^(ν+1), these exhaust the eigenfunctions of Δ̸, and dim 𝒮_l = (l + 1)² at ν = 3.

(2) If ω ≠ 0 is a co-closed 1-form with Δ̸ω = μω, then μ = k_l² − 1 for some l ≥ 1, and the Cartesian components of ω
lie in 𝒮_l. 𝒱_1 consists of the duals of the Killing fields of 𝕊^ν, which are the rotation fields x ↦ Ax,
A ∈ 𝔰𝔬(ν + 1), restricted to 𝕊^ν; dim 𝒱_1 = ν(ν + 1)/2.

(3) If h ≠ 0 is trace-free, divergence-free and Δ̸h = μh, then μ = k_l² − 2 for some l ≥ 2, and the Cartesian
components of h lie in 𝒮_l.

(4) Δ̸ maps co-closed 1-forms to co-closed 1-forms and trace-free divergence-free tensors to such tensors. Every smooth
co-closed 1-form is a sum Σ_(l≥1) V_l, V_l ∈ 𝒱_l, and every smooth trace-free divergence-free tensor a sum
Σ_(l≥2) T_l, T_l ∈ 𝒯_l, converging in C^∞.

*Proof.* (1) This is classical. On ℝ^(ν+1), Δ_(ℝ^(ν+1)) = ∂_r² + (ν/r)∂_r − r⁻²Δ̸ (in our sign convention for Δ̸), so a
harmonic homogeneous polynomial p of degree l restricts to an element of 𝒮_l. Every polynomial restricted to 𝕊^ν is a
sum of restricted harmonic ones (the decomposition 𝒫_l = ℋ_l ⊕ |x|²𝒫_(l−2) of the homogeneous polynomials of degree
l), polynomials are dense in C(𝕊^ν), and eigenfunctions with distinct eigenvalues are orthogonal; so an eigenfunction
with eigenvalue μ is orthogonal to a dense set unless μ = k_l² for some l, and then it is orthogonal to every
restricted harmonic polynomial of degree ≠ l, hence lies in the restrictions of ℋ_l. In four variables
dim ℋ_l = dim 𝒫_l − dim 𝒫_(l−2) = C(l + 3, 3) − C(l + 1, 3) = (l + 1)², C(·, ·) the binomial coefficient.

(2) By [[eq:iii-a1-1-2b]] with δ̸V = 0, ΔᵉV = (μ + 1)V: every Cartesian component of V is an eigenfunction with
eigenvalue μ + 1, which by (1) is k_l² for some l ≥ 0, the components lying in 𝒮_l. If l = 0 the components are
constant, and V · x̂ = 0 for every x̂ forces V = 0; so l ≥ 1. For V ∈ 𝒱_1, [[lem:iii-a1-1-1]] (b) gives
2δ̸δ̸*V = (k_1² − 1 − (ν − 1))V = 0, as k_1² = ν, so ‖δ̸*V‖² = 0 and V is Killing. Conversely a Killing V has
δ̸V = −tr δ̸*V = 0 and, by [[lem:iii-a1-1-1]] (b), Δ̸V = (ν − 1)V = (k_1² − 1)V. The rotation fields restrict to Killing
fields, A ↦ (Ax)|_(𝕊^ν) is injective, and the Killing fields of a connected Riemannian ν-manifold form a space of
dimension at most ν(ν + 1)/2 (a Killing field is determined by its value and its covariant derivative at one point); so
they are all.

(3) By [[eq:iii-a1-1-2e]] with tr Q = 0 and δ̸Q = 0, every Cartesian component is an eigenfunction with eigenvalue
μ + 2 = k_l², the components lying in 𝒮_l. If l = 0, Q is constant with Qx̂ = 0 for every x̂, so Q = 0. If l = 1,
Q_ij = Σ_k c_ijk x̂_k with c symmetric in i, j, and Q(x̂)x̂ = 0 for every x̂ makes c antisymmetric in j, k; a 3-tensor
symmetric in its first two indices and antisymmetric in its last two vanishes
(c_ijk = −c_ikj = −c_kij = c_kji = c_jki = −c_jik = −c_ijk). So l ≥ 2.

(4) The first sentence is [[lem:iii-a1-1-1]] (d), with tr Δ̸h = Δ̸ tr h as g̸ is parallel. Δ̸ is elliptic and
self-adjoint on the compact 𝕊^ν, so L² is the orthogonal sum of its finite-dimensional eigenspaces E_μ of smooth
sections, and a smooth section's expansion converges in C^∞ (the spectral theorem and elliptic regularity for
self-adjoint elliptic operators on a compact manifold). For a co-closed ω = Σ_μ ω_μ, [[lem:iii-a1-1-1]] (d) makes δ̸ω_μ
an eigenfunction with eigenvalue μ + ν − 1; these are mutually orthogonal for distinct μ and sum to δ̸ω = 0, so each ω_μ
is co-closed and, by (2), lies in 𝒱_l with μ = k_l² − 1. For a trace-free divergence-free h = Σ_μ h_μ the same argument
applies to tr h_μ (eigenvalue μ) and then to δ̸h_μ (eigenvalue μ + ν + 1 by [[lem:iii-a1-1-1]] (d)), and (3)
concludes. ∎

**Lemma {#lem:iii-a1-1-5}** (The identities; [Hin26, (2.34)–(2.35)] in dimension 4 + 1.) For S ∈ 𝒮_l, V ∈ 𝒱_l (l ≥ 1),
T ∈ 𝒯_l (l ≥ 2) and k² := k_l²:

    δ̸dS = k²S,     Δ̸dS = (k² − ν + 1) dS,     δ̸*dS = δ̸*₀dS − (k²/ν) g̸S,     Δ̸(g̸S) = k² g̸S,
    δ̸(g̸S) = −dS,     tr(g̸S) = νS,     tr δ̸*₀dS = 0,
    δ̸(δ̸*₀dS) = ((ν − 1)/ν)(k² − ν) dS,     Δ̸(δ̸*₀dS) = (k² − 2ν) δ̸*₀dS,
    Δ̸V = (k² − 1)V,     δ̸δ̸*V = ½(k² − ν)V,     tr δ̸*V = 0,     Δ̸δ̸*V = (k² − ν − 2) δ̸*V,
    tr T = 0,     δ̸T = 0,     Δ̸T = (k² − 2)T;                                                       {#eq:iii-a1-1-2}

and

    δ̸*₀dS = 0  (S ∈ 𝒮_1),     δ̸*V = 0  (V ∈ 𝒱_1).                                                {#eq:iii-a1-1-3}

At ν = 3: Δ̸dS = (k² − 2)dS, δ̸*dS = δ̸*₀dS − (k²/3)g̸S, δ̸(δ̸*₀dS) = (2/3)(k² − 3)dS, Δ̸(δ̸*₀dS) = (k² − 6)δ̸*₀dS,
δ̸δ̸*V = ½(k² − 3)V, Δ̸δ̸*V = (k² − 5)δ̸*V, and k² = l(l + 2). At ν = 2 the list is [Hin26, (2.35)].

*Proof.* δ̸dS = Δ̸S; Δ̸dS is [[lem:iii-a1-1-1]] (a). δ̸*dS = ∇̸²S has trace −k²S, which with [[eq:iii-a1-1-1]] is the
third identity; the next three hold as g̸ is parallel. By [[lem:iii-a1-1-1]] (b), 2δ̸δ̸*dS = k²dS + (k² − ν + 1)dS −
(ν − 1)dS, so δ̸δ̸*dS = (k² − ν + 1)dS, and δ̸(δ̸*₀dS) = (k² − ν + 1 − k²/ν)dS = ((ν − 1)/ν)(k² − ν)dS. By
[[lem:iii-a1-1-1]] (c) with ω = dS, Δ̸δ̸*dS = (k² − 2ν)δ̸*dS − 2k²g̸S, and adding (k²/ν)Δ̸(g̸S) = (k⁴/ν)g̸S gives
Δ̸δ̸*₀dS = (k² − 2ν)δ̸*₀dS, the g̸S terms cancelling. For V: the first identity is the definition;
[[lem:iii-a1-1-1]] (b) gives δ̸δ̸*V = ½(k² − 1 − ν + 1)V; tr δ̸*V = −δ̸V = 0; [[lem:iii-a1-1-1]] (c) gives
(k² − 1 − ν − 1)δ̸*V. The T line is the definition. [[eq:iii-a1-1-3]]: S ∈ 𝒮_1 is the restriction of a linear function
L, and by the Gauss formula ∇̸²S(X, Y) = D²L(X, Y) − ⟨X, Y⟩dL(x̂) = −⟨X, Y⟩S, so δ̸*₀dS = −Sg̸ + (1/ν)g̸ νS = 0; and
V ∈ 𝒱_1 is Killing by [[lem:iii-a1-1-4]] (2). ∎

**Lemma {#lem:iii-a1-1-6}** (Decomposition; [Hin26, p. 64] in dimension 4 + 1.) (1) Every S ∈ C^∞(𝕊^ν) is a sum
Σ_(l≥0) S_l, S_l ∈ 𝒮_l. (2) Every smooth 1-form is a sum of scalar type l ≥ 1 and vector type l ≥ 1 1-forms. (3) Every
smooth symmetric 2-tensor is a sum of scalar type l ≥ 0, vector type l ≥ 2 and tensor type l ≥ 2 tensors; in the scalar
type, δ̸*₀dS is absent for l ≤ 1 by [[eq:iii-a1-1-3]]. All sums converge in C^∞.

*Proof.* (1) is [[lem:iii-a1-1-4]] (1) with the spectral decomposition of Δ̸. (2) δ̸ω has mean zero; let S be the
mean-zero solution of Δ̸S = δ̸ω, so that V := ω − dS is co-closed, and expand S by (1) and V by [[lem:iii-a1-1-4]] (4).
(3) Write h = (1/ν)(tr h)g̸ + h₀ with h₀ trace-free. On trace-free tensors the adjoint of δ̸*₀ is δ̸, and δ̸*₀ has
injective principal symbol (ξ ⊗_s ω − (1/ν)g̸⟨ξ, ω⟩ = 0 forces ω = 0 for ξ ≠ 0 as ν ≥ 2), so δ̸δ̸*₀ is elliptic and
self-adjoint; solving δ̸δ̸*₀ω = δ̸h₀, which is possible as δ̸h₀ is orthogonal to ker δ̸δ̸*₀ = ker δ̸*₀, gives
h₀ = δ̸*₀ω + T with ω smooth and T trace-free and divergence-free. Expand ω by (2), using δ̸*₀V = δ̸*V for co-closed V
and [[eq:iii-a1-1-3]] for l = 1, T by [[lem:iii-a1-1-4]] (4), and tr h by (1). ∎

**Definition {#def:iii-a1-1-7}** ([Hin26, Definition 2.28] in dimension 4 + 1.) For a ∈ ℝ⁴, S(a) := a · x/|x| ∈ 𝒮_1;
for A ∈ 𝔰𝔬(4), V(A) := (Ax) · dx, which restricted to 𝕊³ lies in 𝒱_1 (the dual of the rotation field Ax · ∂_x), and
A ↦ V(A) is an isomorphism 𝔰𝔬(4) → 𝒱_1 by [[lem:iii-a1-1-4]] (2) (both are six-dimensional). Conversely, for S ∈ 𝒮_1
and V ∈ 𝒱_1 (or their complexifications) a(S) and A(V) denote the unique a and A with S = S(a), V = V(A). As in
[Hin26], S(a) is homogeneous of degree 0 and V(A) is dual, with respect to the Euclidean metric, to a rotation field.
The forms V(a) = (a × x) · dx, a ∈ ℝ³, of [Hin26] are the case 𝔰𝔬(3) ≅ ℝ³.

### The Minkowski operators in dimension 4 + 1 {#sec:iii-a1-2}

This section is [Hin26, Section 2.4.1] in dimension 4 + 1.

#### Coordinates, splittings and the metric {#sec:iii-a1-2-1}

On ℝ^(1+4) use t ∈ ℝ, r = |x| > 0, ω = x/|x| ∈ 𝕊³ for 0 ≠ x ∈ ℝ⁴, and

    t_* := t − r,     ρ := r⁻¹,     x̄⁰ := t + r,     x̄¹ := t − r.                                      {#eq:iii-a1-2-1}

The level sets of x̄⁰, x̄¹ are null. The bundle splittings are those of [Hin26, (2.37b)] with 𝕊³ in place of 𝕊²:

    T*ℝ^(1+4) = ⟨dx̄⁰⟩ ⊕ ⟨dx̄¹⟩ ⊕ rT*𝕊³,
    S²T*ℝ^(1+4) = ⟨(dx̄⁰)²⟩ ⊕ ⟨2 dx̄⁰dx̄¹⟩ ⊕ (2 dx̄⁰ ⊗_s rT*𝕊³) ⊕ ⟨(dx̄¹)²⟩ ⊕ (2 dx̄¹ ⊗_s rT*𝕊³)
                  ⊕ r²S²T*𝕊³;                                                                            {#eq:iii-a1-2-2}

that is, (ω₀, ω₁, ω̸) is the covector ω₀ dx̄⁰ + ω₁ dx̄¹ + rω̸, and (a, b, c, e, f, q) the symmetric tensor
a(dx̄⁰)² + 2b dx̄⁰dx̄¹ + 2dx̄⁰ ⊗_s rc + e(dx̄¹)² + 2dx̄¹ ⊗_s rf + r²q, with 2α ⊗_s β := α ⊗ β + β ⊗ α and αβ := α ⊗_s β.
In Cartesian terms, rω̸ is the tangential field V with V♭|_(𝕊³) = ω̸ of the ambient picture, extended homogeneously of
degree 0, and r²q is likewise the tangential matrix field of q: dxⁱ pulls back to r ∂_a x̂ⁱ dyᵃ on the sphere of radius
r. Neither identification depends on (t, r). The Minkowski metric and its dual are

    ḡ = −dt² + dr² + r²g̸ = −dx̄⁰dx̄¹ + r²g̸,
    ḡ⁻¹ = −4∂₀ ⊗_s ∂₁ + r⁻²g̸⁻¹ = 2ρ∂_(t_*) ⊗_s ρ∂_ρ + ρ²((ρ∂_ρ)² + g̸⁻¹),                               {#eq:iii-a1-2-3}

with ∂₀ := ∂_(x̄⁰), ∂₁ := ∂_(x̄¹) in the coordinates (x̄⁰, x̄¹, ω); ∂₀ = −½ρ²∂_ρ, ∂₁ = ∂_(t_*) + ½ρ²∂_ρ,
∂₀r = −∂₁r = ½. In the splitting [[eq:iii-a1-2-2]], ḡ = (0, −½, 0, 0, 0, g̸), tr := tr_ḡ = (0, −4, 0, 0, 0, tr), and
G := I − ½ḡ tr (the operator G_g = I − ½g tr_g of [Hin26], defined the same way in every dimension) is

         [ 1    0     0   0   0   0       ]
         [ 0    0     0   0   0   ¼ tr    ]
    G =  [ 0    0     1   0   0   0       ],     G̸ := I − ½g̸ tr,                                       {#eq:iii-a1-2-4}
         [ 0    0     0   1   0   0       ]
         [ 0    0     0   0   1   0       ]
         [ 0    2g̸   0   0   0   G̸       ]

as in [Hin26, (2.39b)]: tr h = −4b + tr q, so Gh = (a, ¼ tr q, c, e, f, q + 2bg̸ − ½g̸ tr q). The Christoffel symbols of
ḡ in the coordinates x̄⁰, x̄¹ and coordinates yᵃ on 𝕊³ vanish except for

    Γ̄^c_(0b) = Γ̄^c_(b0) = ½r⁻¹δ^c_b,     Γ̄^c_(1b) = Γ̄^c_(b1) = −½r⁻¹δ^c_b,
    Γ̄⁰_(ab) = −r g̸_ab,     Γ̄¹_(ab) = r g̸_ab,     Γ̄^c_(ab) = Γ̸^c_(ab),                              {#eq:iii-a1-2-5}

as in [Hin26, (2.40)]: ḡ_01 = −½, ḡ^01 = −2, ḡ_ab = r²g̸_ab, and for example Γ̄⁰_(ab) = ½ḡ^01(−∂₁ḡ_ab) = −r g̸_ab,
Γ̄^c_(0b) = ½r⁻²g̸^cd ∂₀(r²) g̸_bd. The scalar wave operator □̄u = −ḡ^μκ u_(;μκ) is

    □̄ = 4∂₀∂₁ + (3/r)(∂₁ − ∂₀) + r⁻²Δ̸ = −2∂_(t_*)ρ(ρ∂_ρ − 3/2) + ρ²(−(ρ∂_ρ)² + 2ρ∂_ρ + Δ̸).            {#eq:iii-a1-2-6}

Indeed ḡ^ab Γ̄⁰_(ab) = −ν/r and ḡ^ab Γ̄¹_(ab) = ν/r at ν = 3; and with D := ρ∂_ρ, ρ²∂_ρ ρ²∂_ρ = ρ²(D + 1)D, so
4∂₀∂₁ = −2ρD∂_(t_*) − ρ²(D² + D) and (ν/r)(∂₁ − ∂₀) = νρ∂_(t_*) + νρ²D. For general ν, [[eq:iii-a1-2-6]] reads
−2∂_(t_*)ρ(D − ν/2) + ρ²(−D² + (ν − 1)D + Δ̸); at ν = 2 it is [Hin26]'s. Equivalently
□̄ = ∂_t² − ∂_r² − (ν/r)∂_r + r⁻²Δ̸.

#### The operators in the splittings {#sec:iii-a1-2-2}

**Lemma {#lem:iii-a1-2-1}** ([Hin26, Lemma 2.29] in dimension 4 + 1.) In the coordinates t_*, ρ, ω and the splittings
[[eq:iii-a1-2-2]], with Δ̸ the tensor Laplacian acting componentwise on the summands and D := ρ∂_ρ:

(1) (1-forms.) □̄ = −2∂_(t_*)ρ(D − 3/2) + ᵇ□̄(0), where

                                             [  3/2   −3/2   −δ̸ ]
    ᵇ□̄(0) = ρ²(−D² + 2D + Δ̸ + B₁),    B₁ := [ −3/2    3/2    δ̸ ];
                                             [ −2d     2d     1  ]

and δ̄* = E₁∂_(t_*) + ᵇδ̄*(0), where, with rows ordered as in [[eq:iii-a1-2-2]] and columns as (ω₀, ω₁, ω̸),

          [ 0   0   0 ]                      [ −½D    0      0         ]
          [ ½   0   0 ]                      [  ¼D   −¼D     0         ]
    E₁ := [ 0   0   0 ],     ᵇδ̄*(0) = ρ ·  [  ½d    0     −¼(D + 1)  ].
          [ 0   1   0 ]                      [  0     ½D     0         ]
          [ 0   0   ½ ]                      [  0     ½d     ¼(D + 1)  ]
          [ 0   0   0 ]                      [  g̸   −g̸     δ̸*        ]

(2) (Symmetric 2-tensors.) □̄ = −2∂_(t_*)ρ(D − 3/2) + ᵇ□̄(0), where ᵇ□̄(0) = ρ²(−D² + 2D + Δ̸ + B₂) with, in the order
(a, b, c, e, f, q),

          [  3     −3     −2δ̸     0     0     −½tr ]
          [ −3/2    3      δ̸    −3/2   −δ̸     ½tr ]
    B₂ := [ −2d    2d     7/2     0    −5/2   −δ̸   ];                                                   {#eq:iii-a1-2-7}
          [  0     −3      0      3     2δ̸    −½tr ]
          [  0    −2d    −5/2    2d    7/2     δ̸   ]
          [ −2g̸   4g̸   −4δ̸*   −2g̸   4δ̸*    2    ]

and δ̄ = E₂∂_(t_*) + ᵇδ̄(0), with rows (ω₀, ω₁, ω̸),

          [ 2  0  0  0  0  0 ]
    E₂ := [ 0  2  0  0  0  0 ],
          [ 0  0  2  0  0  0 ]
                   [ D − 3   −D + 3    δ̸       0        0        ½tr ]
    ᵇδ̄(0) = ρ ·  [ 0        D − 3    0       −D + 3   δ̸       −½tr ].                                  {#eq:iii-a1-2-8}
                   [ 0        0        D − 4   0        −D + 4   δ̸   ]

For general ν the same holds with 3/2 and 2D in the scalar part replaced by ν/2 and (ν − 1)D; with the 1-form matrix
entries ±3/2 replaced by ±ν/2; with the entries 3, −3, −3/2, 7/2, −5/2 of [[eq:iii-a1-2-7]] replaced by ν, −ν, −ν/2,
(ν + 4)/2, −(ν + 2)/2; and with 3, 4 in [[eq:iii-a1-2-8]] replaced by ν, ν + 1; δ̄* does not depend on ν. At ν = 2 this
is [Hin26, Lemma 2.29], entry by entry.

*Proof.* We prove the general-ν statement.

*The wave operator.* In Cartesian coordinates the Christoffel symbols of ḡ vanish, so □̄ acts on each Cartesian
component of a tensor as the scalar operator ∂_t² − ∂_r² − (ν/r)∂_r + r⁻²Δ̸, which on a Cartesian component, regarded as
a function of (t, r) with values in functions on 𝕊^ν, is L₀ + r⁻²Δᵉ, L₀ := ∂_t² − ∂_r² − (ν/r)∂_r. Write
□_c := L₀ + r⁻²Δ̸ acting componentwise in the splitting; by the calculation of [[eq:iii-a1-2-6]],
□_c = −2∂_(t_*)ρ(D − ν/2) + ρ²(−D² + (ν − 1)D + Δ̸).
Write α := dt = ½(dx̄⁰ + dx̄¹) and β := dr = ½(dx̄⁰ − dx̄¹) = x̂ · dx.

1-forms: ω₀dx̄⁰ + ω₁dx̄¹ + rω̸ = (ω₀ + ω₁)α + (ω₀ − ω₁)x̂ · dx + V · dx with V the field of ω̸. By [[eq:iii-a1-1-2a]] and
[[eq:iii-a1-1-2b]],

    □̄ω = Aα + Bβ + W · dx,     A = □_c(ω₀ + ω₁),     B = □_c(ω₀ − ω₁) + νr⁻²(ω₀ − ω₁) − 2r⁻²δ̸ω̸,
    W = (□_c + r⁻²)ω̸ − 2r⁻²d(ω₀ − ω₁),

and Aα + Bβ = ½(A + B)dx̄⁰ + ½(A − B)dx̄¹, which is (1).

2-tensors: in terms of α and β, h = (a, b, c, e, f, q) is h = 𝖠α² + 2𝖷αβ + 𝖡β² + 2α ⊗_s 𝖶 + 2β ⊗_s 𝖴 + 𝖰, where
𝖠 = a + 2b + e, 𝖷 = a − e, 𝖡 = a − 2b + e, 𝖶 = c + f, 𝖴 = c − f (as tangential fields) and 𝖰 the field of q; in
Cartesian components, h_tt = 𝖠, (h_ti) = 𝖷x̂ + 𝖶, (h_ij) = 𝖡x̂ ⊗ x̂ + x̂ ⊙ 𝖴 + 𝖰. By [[lem:iii-a1-1-2]],

    (□̄h)_tt = □_c𝖠,     (□̄h)_(t·) = T_X x̂ + T_W,     (□̄h)_(··) = T_B x̂ ⊗ x̂ + x̂ ⊙ T_U + T_Q,
    T_X = □_c𝖷 + νr⁻²𝖷 − 2r⁻²δ̸𝖶,     T_W = (□_c + r⁻²)𝖶 − 2r⁻²d𝖷,
    T_B = □_c𝖡 + 2νr⁻²𝖡 − 4r⁻²δ̸𝖴 − 2r⁻² tr q,     T_U = (□_c + (ν + 3)r⁻²)𝖴 − 2r⁻²d𝖡 − 2r⁻²δ̸q,
    T_Q = (□_c + 2r⁻²)q − 2r⁻²𝖡g̸ − 4r⁻²δ̸*𝖴.                                                             {#eq:s11-box-tensors}

Inverting, the components of □̄h in [[eq:iii-a1-2-2]] are a′ = ¼(□_c𝖠 + T_B) + ½T_X, b′ = ¼(□_c𝖠 − T_B),
e′ = ¼(□_c𝖠 + T_B) − ½T_X, c′ = ½(T_W + T_U), f′ = ½(T_W − T_U), q′ = T_Q. Substituting:

    a′ = □_c a + r⁻²(νa − νb − 2δ̸c − ½ tr q),
    b′ = □_c b + r⁻²(−(ν/2)a + νb − (ν/2)e + δ̸c − δ̸f + ½ tr q),
    e′ = □_c e + r⁻²(−νb + νe + 2δ̸f − ½ tr q),
    c′ = □_c c + r⁻²(−2da + 2db + ((ν + 4)/2)c − ((ν + 2)/2)f − δ̸q),
    f′ = □_c f + r⁻²(−2db + 2de − ((ν + 2)/2)c + ((ν + 4)/2)f + δ̸q),
    q′ = □_c q + r⁻²(−2g̸a + 4g̸b − 4δ̸*c − 2g̸e + 4δ̸*f + 2q),

which is (2) for □̄. (For instance, in c′ the coefficient of c is ½ + (ν + 3)/2, from ½(□_c + r⁻²)𝖶 and
½(□_c + (ν + 3)r⁻²)𝖴; the coefficient of da is −1 − 1, from −r⁻²d𝖷 and −r⁻²d𝖡.)

*The symmetric gradient.* From [[eq:iii-a1-2-5]], for a 1-form with coordinate components ω₀, ω₁, ω_b = rω̸_b:
∇̄₀ω₀ = ∂₀ω₀, ∇̄₁ω₁ = ∂₁ω₁, ∇̄₀ω₁ = ∂₀ω₁, ∇̄₁ω₀ = ∂₁ω₀, ∇̄₀ω_b = r∂₀ω̸_b, ∇̄₁ω_b = r∂₁ω̸_b,
∇̄_bω₀ = ∂_bω₀ − ½ω̸_b, ∇̄_bω₁ = ∂_bω₁ + ½ω̸_b, ∇̄_aω_b = r∇̸_aω̸_b + r g̸_ab(ω₀ − ω₁). Symmetrising and reading off the
components of [[eq:iii-a1-2-2]]: a = ∂₀ω₀, b = ½(∂₀ω₁ + ∂₁ω₀), c = ½∂₀ω̸ + (ρ/2)(dω₀ − ½ω̸), e = ∂₁ω₁,
f = ½∂₁ω̸ + (ρ/2)(dω₁ + ½ω̸), q = ρ(δ̸*ω̸ + g̸(ω₀ − ω₁)); with ∂₀ = −½ρD, ∂₁ = ∂_(t_*) + ½ρD this is the stated δ̄*.
No trace over the sphere occurs, so ν does not enter.

*The divergence.* (δ̄h)_κ = −ḡ^μπ ∇̄_μ h_πκ = 2(∇̄₀h_1κ + ∇̄₁h_0κ) − r⁻²g̸^ab ∇̄_a h_bκ, with h_00 = a, h_01 = b,
h_0b = rc_b, h_11 = e, h_1b = rf_b, h_ab = r²q_ab. From [[eq:iii-a1-2-5]]: ∇̄₀h_10 = ∂₀b, ∇̄₁h_00 = ∂₁a,
g̸^ab ∇̄_a h_b0 = −rδ̸c + rν(a − b) − (r/2) tr q; ∇̄₀h_11 = ∂₀e, ∇̄₁h_01 = ∂₁b,
g̸^ab ∇̄_a h_b1 = −rδ̸f + rν(b − e) + (r/2) tr q; ∇̄₀h_1c = r∂₀f_c, ∇̄₁h_0c = r∂₁c_c,
g̸^ab ∇̄_a h_bc = r²(−δ̸q + (ν + 1)(c − f))_c, the ν + 1 being g̸^ab g̸_ab + 1. Hence
(δ̄h)₀ = 2∂_(t_*)a + ρ((D − ν)a + (−D + ν)b + δ̸c + ½ tr q),
(δ̄h)₁ = 2∂_(t_*)b + ρ((D − ν)b + (−D + ν)e + δ̸f − ½ tr q), and the rT*𝕊^ν component is
2∂_(t_*)c + ρ((D − ν − 1)c + (−D + ν + 1)f + δ̸q).

Setting ν = 2 reproduces every entry of [Hin26, Lemma 2.29] ([Hin26, (2.41), (2.42)] and the 1-form statements);
setting ν = 3 gives (1)–(2). ∎

#### Types, and the indicial roots by type {#sec:iii-a1-2-3}

Applying [[lem:iii-a1-1-6]] to each component of a tensor in the splittings [[eq:iii-a1-2-2]] at each sphere of
constant (t_*, ρ) gives the types of [Hin26, (2.43)–(2.44)], with 𝕊³ harmonics, and one more:

    s0 1-forms: (aS, bS, 0), S ∈ 𝒮_0;     sl 1-forms, l ≥ 1: (aS, bS, c dS), S ∈ 𝒮_l;
    vl 1-forms, l ≥ 1: (0, 0, cV), V ∈ 𝒱_l;                                                             {#eq:iii-a1-2-9}

and, writing the last component of [[eq:iii-a1-2-2]] as pSg̸ + qδ̸*₀dS, qδ̸*V or τT,

    s0: (aS, bS, 0, eS, 0, pSg̸), S ∈ 𝒮_0;     s1: (aS, bS, c dS, eS, f dS, pSg̸), S ∈ 𝒮_1;
    sl, l ≥ 2: (aS, bS, c dS, eS, f dS, pSg̸ + qδ̸*₀dS), S ∈ 𝒮_l;     v1: (0, 0, cV, 0, fV, 0), V ∈ 𝒱_1;
    vl, l ≥ 2: (0, 0, cV, 0, fV, qδ̸*V), V ∈ 𝒱_l;     tl, l ≥ 2: (0, 0, 0, 0, 0, τT), T ∈ 𝒯_l,          {#eq:iii-a1-2-10}

with a, b, c, e, f, p, q, τ functions of (t_*, ρ). The tensor type tl is new in dimension 4 + 1. The operators of
[[lem:iii-a1-2-1]] are built from d, δ̸, δ̸*, tr, g̸·, Δ̸ and constants, and by [[eq:iii-a1-1-2]]–[[eq:iii-a1-1-3]] each
of these maps the components of a type to components of the same type, degree and harmonic; so the operators of
[[lem:iii-a1-2-1]] preserve the type, the degree l and the particular S, V or T, and act on each type by a matrix of
operators in (t_*, ρ). For example, on sl 1-forms, l ≥ 1, ᵇ□̄(0) is ρ² times

                  [ k²  0    0      ]   [  3/2   −3/2   −k² ]
    −D² + 2D +    [ 0   k²   0      ] + [ −3/2    3/2    k² ],     k² = l(l + 2),                       {#eq:iii-a1-2-11}
                  [ 0   0    k² − 2 ]   [ −2      2      1   ]

the analogue of [Hin26, (2.45)].

**Definition {#def:iii-a1-2-2}** ([Hin26, Definition 2.30] in dimension 4 + 1.) On X := [0, ∞)_ρ × 𝕊³, for
A ∈ ρ^α Diff^m_b(X) acting on one of the bundles above, ι ∈ ℂ is a *scalar*, *vector* or *tensor type l indicial
root* of A if there is a nonzero u of that type and degree with N(A)(ρ^ι u) = 0, N(A) the normal operator of
[[def:s11-b-analysis]].

Replacing D by ι in [[eq:iii-a1-2-11]], the determinant is
−(ι + l + 1)(ι + l)(ι + l − 1)(ι − l − 1)(ι − l − 2)(ι − l − 3) (the type sl of 1-forms in [[lem:iii-a1-2-3]] below),
so −l − 1, −l, −l + 1, l + 1, l + 2, l + 3 are the scalar type l indicial roots of ᵇ□̄(0) on 1-forms (in dimension
3 + 1 the six numbers of [Hin26] are −l − 1, −l, −l + 1, l, l + 1, l + 2).

**Lemma {#lem:iii-a1-2-3}** (Indicial roots of ᵇ□̄(0) by type in dimension 4 + 1.) For a finite list 𝒟 of integers
write R(𝒟) for the list of −d and d + 2, d ∈ 𝒟, with multiplicity. The indicial roots of ᵇ□̄(0), as the zeros of the
determinant of its type-wise indicial matrix with multiplicity, are R(𝒟) with: on functions of degree l, 𝒟 = (l); on
1-forms, s0: (0, 1); sl, l ≥ 1: (l − 1, l, l + 1); vl: (l); on symmetric 2-tensors, s0: (0, 0, 1, 2); s1:
(0, 1, 1, 1, 2, 3); sl, l ≥ 2: (l − 2, l − 1, l, l, l, l + 1, l + 2); v1: (1, 2); vl, l ≥ 2: (l − 1, l, l + 1); tl,
l ≥ 2: (l). In particular every indicial root is an integer, the roots on scalar functions are −l and l + 2 (in
dimension 3 + 1, −l and l + 1), and none lies in the open interval (0, 2).

*Proof.* We prove the statement for general ν, with −d and d + ν − 1 in place of −d and d + 2; ν = 3 gives the
lemma. The list 𝒟 is the list of degrees of the harmonic polynomials that make up the Cartesian components of a tensor
of the given type.

*Step 1: reduction to Cartesian components.* Write a 1-form as ω_t dt + Σ_i ω_i dxⁱ and a symmetric 2-tensor by its
Cartesian components h_tt, h_ti, h_ij. As dt and dxⁱ are parallel for ḡ, □̄ acts on each Cartesian component as the
scalar operator, which by [[eq:iii-a1-2-6]] for general ν is −2∂_(t_*)ρ(D − ν/2) + ρ²(−D² + (ν − 1)D + Δ̸); on a
Cartesian component, regarded as a function on 𝕊^ν depending on (t_*, ρ), Δ̸ is Δᵉ. So in Cartesian components
ᵇ□̄(0) = ρ²(−D² + (ν − 1)D + Δᵉ). Let C be the passage from the components of [[eq:iii-a1-2-2]] to the Cartesian
ones, given by dx̄⁰ = dt + x̂ · dx, dx̄¹ = dt − x̂ · dx and rω̸ ↔ V · dx, and for 2-tensors by the formulas for h_tt,
(h_ti), (h_ij) in the proof of [[lem:iii-a1-2-1]]; C is a pointwise isomorphism and does not depend on (t_*, ρ).

Fix a type and a degree l, and let J : ℂ^k → C^∞(𝕊^ν; ·) be the map from the k constant coefficients to the tensor of
that type in [[eq:iii-a1-2-9]]–[[eq:iii-a1-2-10]], with S, V or T fixed. By the paragraph before [[eq:iii-a1-2-11]]
there is a type-wise indicial matrix I(ι) ∈ ℂ^(k×k) with ᵇ□̄(0)(ρ^ι J(u)) = ρ^(ι+2) J(I(ι)u). The map J is injective:
the summands of [[eq:iii-a1-2-2]] are independent; S ↦ dS is injective on 𝒮_l for l ≥ 1; pSg̸ + qδ̸*₀dS = 0 forces
p = q = 0 for l ≥ 2, the two terms being pure trace and trace-free, and δ̸*₀dS ≠ 0 as its divergence
((ν − 1)/ν)(k_l² − ν)dS is nonzero; and δ̸*V ≠ 0 for V ∈ 𝒱_l, l ≥ 2, as δ̸δ̸*V = ½(k_l² − ν)V ≠ 0. Let W := CJ(ℂ^k), a
k-dimensional space of Cartesian component vectors. Applying C, which commutes with ρ and D,

    CJ(I(ι)u) = (−ι² + (ν − 1)ι + Δᵉ) CJ(u),     u ∈ ℂ^k,

so W is invariant under Δᵉ and I(ι) is similar to the restriction of −ι² + (ν − 1)ι + Δᵉ to W. If W has a basis of
Δᵉ-eigenvectors with eigenvalues k_d², d ∈ 𝒟, then, as −ι² + (ν − 1)ι + d(d + ν − 1) = −(ι + d)(ι − d − ν + 1),

    det I(ι) = Π_(d∈𝒟) (−ι² + (ν − 1)ι + k_d²) = Π_(d∈𝒟) (−(ι + d)(ι − d − ν + 1)),

whose zeros with multiplicity are −d and d + ν − 1, d ∈ 𝒟. It remains to exhibit such a basis for each type.

*Step 2: harmonic polynomials.* Write ℋ_d for the harmonic homogeneous polynomials of degree d on ℝ^(ν+1), with
values in ℂ, in ℂ^(ν+1) or in matrices. By [[lem:iii-a1-1-4]] (1), the restriction to 𝕊^ν of an element of ℋ_d is a
Δᵉ-eigenvector with eigenvalue k_d². For f ∈ ℋ_d and j ≥ 1,

    Δ(|x|^(2j) f) = 2j(2j + ν − 1 + 2d) |x|^(2j−2) f,     Δ(xⁱ f) = 2∂_i f,

by Δ|x|^(2j) = 2j(2j + ν − 1)|x|^(2j−2), Euler's identity x · ∇f = df and the harmonicity of f. For p ∈ ℋ_l with
S := p|_(𝕊^ν), on 𝕊^ν

    (∇p)| = ∇̸S + lSx̂,     (∇²p)| = ∇̸²S + lSP + (l − 1)x̂ ⊙ ∇̸S + l(l − 1)S x̂ ⊗ x̂,

with ∇̸S the tangential field of dS and ∇̸²S = δ̸*dS the tangential matrix field of the Hessian on 𝕊^ν: the first is
Euler's identity; for the second, ∇p is homogeneous of degree l − 1, so D_(x̂)(∇p) = (l − 1)(∇̸S + lSx̂), and for
tangential X, D_X(∇̸S + lSx̂) = ∇̸_X∇̸S − ⟨X, ∇̸S⟩x̂ + l(XS)x̂ + lSX by the Gauss formula.

*Step 3: the bases.* In each case below W is spanned by the restrictions listed, which are Δᵉ-eigenvectors by Step 2,
and their number is k = dim W; so they form a basis.

*Functions:* W = span{S}; 𝒟 = (l).

*1-forms*, in Cartesian components (ω_t; ω_i). s0: S is constant and W = span{(1; 0), (0; x̂)}, x̂ the restriction of
x ∈ ℋ_1; 𝒟 = (0, 1). sl, l ≥ 1: W is the sum of span{(S; 0)} and of the spatial span{(0; Sx̂), (0; ∇̸S)}. Let
H := xp − (ν + 2l − 1)⁻¹|x|²∇p; by Step 2, Δ(xp) = 2∇p and Δ(|x|²∇p) = 2(ν + 2l − 1)∇p as ∇p ∈ ℋ_(l−1), so
H ∈ ℋ_(l+1). On 𝕊^ν, H| = Sx̂ − (ν + 2l − 1)⁻¹(∇p)| and (∇p)| = ∇̸S + lSx̂, so the spatial span is span{H|, (∇p)|};
𝒟 = (l − 1, l, l + 1). vl: W = span{(0; V)}, and the Cartesian components of V lie in 𝒮_l by [[lem:iii-a1-1-4]] (2);
𝒟 = (l).

*2-tensors*, in Cartesian components (h_tt; h_ti; h_ij). As (𝖠, 𝖷, 𝖡) and (a, b, e), and (𝖶, 𝖴) and (c, f), determine
each other linearly, W = W_tt ⊕ W_tx ⊕ W_xx, with W_tt spanned by the values of 𝖠, W_tx by those of 𝖷x̂ + 𝖶 and W_xx
by those of 𝖡x̂ ⊗ x̂ + x̂ ⊙ 𝖴 + 𝖰, over the type.

s0: W_tt = span{1}, W_tx = span{x̂}, and W_xx = span{x̂ ⊗ x̂, P} = span{I, x̂ ⊗ x̂ − (ν + 1)⁻¹I}, the restrictions of the
constant I and of x ⊗ x − (ν + 1)⁻¹|x|²I ∈ ℋ_2; 𝒟 = (0, 1, 0, 2).

sl, l ≥ 1 (this includes s1): W_tt = span{S}, and W_tx = span{Sx̂, ∇̸S} = span{H|, (∇p)|} as for 1-forms. W_xx is
spanned by Sx̂ ⊗ x̂, x̂ ⊙ ∇̸S and SP, and, for l ≥ 2, by the field of δ̸*₀dS. By Step 2 and [[eq:iii-a1-1-2]]
(∇̸²S = δ̸*₀dS − (k_l²/ν)SP),

    (∇²p)| = δ̸*₀dS + (l − k_l²/ν)SP + (l − 1)x̂ ⊙ ∇̸S + l(l − 1)S x̂ ⊗ x̂,     (x ⊙ ∇p)| = x̂ ⊙ ∇̸S + 2lS x̂ ⊗ x̂,

and Sδ = SP + Sx̂ ⊗ x̂, δ the identity matrix; for l = 1, ∇²p = 0 and δ̸*₀dS = 0 by [[eq:iii-a1-1-3]]. So
W_xx = span{Sx̂ ⊗ x̂, (x ⊙ ∇p)|, Sδ, (∇²p)|}, without the last for l = 1. Now ∇²p ∈ ℋ_(l−2) and pδ ∈ ℋ_l. With
Q := x ⊙ ∇p, ΔQ = 4∇²p and Δ(|x|²∇²p) = 2(ν + 2l − 3)∇²p, so Q^h := Q − 2(ν + 2l − 3)⁻¹|x|²∇²p ∈ ℋ_l. With
K := p x ⊗ x, ΔK = 2pδ + 2Q = 2pδ + 2Q^h + 4(ν + 2l − 3)⁻¹|x|²∇²p; and Δ(|x|²pδ) = 2(ν + 2l + 1)pδ,
Δ(|x|²Q^h) = 2(ν + 2l + 1)Q^h, Δ(|x|⁴∇²p) = 4(ν + 2l − 1)|x|²∇²p. Hence

    H₂ := K − (ν + 2l + 1)⁻¹|x|²(pδ + Q^h) − (ν + 2l − 3)⁻¹(ν + 2l − 1)⁻¹|x|⁴∇²p ∈ ℋ_(l+2).

On 𝕊^ν, Sx̂ ⊗ x̂ and (x ⊙ ∇p)| are combinations of H₂|, Q^h|, Sδ and (∇²p)|, so W_xx = span{H₂|, Q^h|, Sδ, (∇²p)|}
(without the last for l = 1), with eigenvalues k_(l+2)², k_l², k_l², k_(l−2)². So 𝒟 = (l) ∪ (l − 1, l + 1) ∪
(l − 2, l, l, l + 2) for l ≥ 2, and (1) ∪ (0, 2) ∪ (1, 1, 3) = (0, 1, 1, 1, 2, 3) for l = 1.

v1 and vl: W_tt = 0, W_tx = span{V}, and W_xx = span{x̂ ⊙ V} for l = 1, span{x̂ ⊙ V, δ̸*V} for l ≥ 2. By
[[lem:iii-a1-1-4]] (2) there is v ∈ ℋ_l with values in ℝ^(ν+1) and v| = V; v is homogeneous of degree l, so x · v = 0
everywhere and D_(x̂)v = lV on 𝕊^ν. By the Gauss formula D_X V = ∇̸_X V − ⟨X, V⟩x̂ for tangential X, the Jacobian
J_v := (∂_i v_j) is lx̂ ⊗ V + ∇̸V − V ⊗ x̂ on 𝕊^ν, with ∇̸V := Σ_a e_a ⊗ ∇̸_(e_a)V; so

    (∂ ⊙ v)| := (J_v + J_vᵀ)| = (l − 1)x̂ ⊙ V + 2δ̸*V,     ∂ ⊙ v ∈ ℋ_(l−1).

Also Δ(x ⊙ v) = 2∂ ⊙ v, so H₁ := x ⊙ v − (ν + 2l − 1)⁻¹|x|²∂ ⊙ v ∈ ℋ_(l+1). For l = 1, v = Ax with A antisymmetric,
∂ ⊙ v = A + Aᵀ = 0, and x̂ ⊙ V = H₁|; for l ≥ 2, W_xx = span{H₁|, (∂ ⊙ v)|}. So 𝒟 = (1, 2) for v1 and
(l − 1, l, l + 1) for vl.

tl: W = span{T}, whose Cartesian components lie in 𝒮_l by [[lem:iii-a1-1-4]] (3); 𝒟 = (l).

Every d in these lists is ≥ 0, so −d ≤ 0 and d + 2 ≥ 2 at ν = 3. ∎

#### The symmetric gradient's indicial families {#sec:iii-a1-2-4}

Reading off [[lem:iii-a1-2-1]] (1) on the types s0, s1 and v1 (for s1 the entry −1 in the last row comes from
δ̸*dS = −Sg̸ at l = 1, which holds for every ν by [[eq:iii-a1-1-2]]–[[eq:iii-a1-1-3]], as k_1² = ν):

                         [ −ι/2    0   ]                         [ −ι/2   0     0          ]
                         [  ι/4   −ι/4 ]                         [  ι/4  −ι/4   0          ]
    N_s0(ᵇδ̄*(0), ι) =  [  0      ι/2 ],    N_s1(ᵇδ̄*(0), ι) =  [  1/2   0    −¼(ι + 1)  ],
                         [  1     −1   ]                         [  0     ι/2   0          ]
                                                                 [  0     1/2   ¼(ι + 1)   ]
                                                                 [  1    −1    −1          ]

                         [ −¼(ι + 1) ]
    N_v1(ᵇδ̄*(0), ι) =  [  ¼(ι + 1) ].                                                                {#eq:iii-a1-2-12}

(The rows are the components of [[eq:iii-a1-2-2]] that the type carries: a, b, e, q for s0; a, b, c, e, f, q for s1;
c, f for v1.) These are [Hin26, (2.46a)–(2.46c)] unchanged.

**Lemma {#lem:iii-a1-2-4}** (Injectivity; the remark after [Hin26, (2.46)] in dimension 4 + 1.) For every type other
than s0, s1, v1 and every ι ∈ ℂ, N_•(ᵇδ̄*(0), ι) is injective; N_s0 and N_s1 are injective for ι ≠ 0, and N_v1 for
ι ≠ −1. At the exceptional values the kernels are spanned by (1, 1) (from dt), by (1, −1, 2) (from dxⁱ, with
S = x̂_i), and by the rotations V ∈ 𝒱_1.

*Proof.* By [[lem:iii-a1-2-1]] (1), ᵇδ̄*(0) is ρ times an operator with coefficients polynomial in D and independent of
ρ, so for u of one type ᵇδ̄*(0)(ρ^ι u) = ρ^(ι+1) N_•(ᵇδ̄*(0), ι)u, and ρ^ι u does not depend on t_*. So if
N_•(ι)u = 0 then ω := ρ^ι u satisfies δ̄*ω = 0 on ℝ_t × (ℝ⁴ ∖ 0), and so do its real and imaginary parts, as δ̄* is
real. In Cartesian coordinates a 1-form with ∂_μω_κ + ∂_κω_μ = 0 satisfies ∂_π∂_μω_κ = 0 (the identity
∂_π∂_μω_κ = ∂_π s_μκ + ∂_μ s_πκ − ∂_κ s_πμ, s := δ̄*ω), so on the connected set ℝ_t × (ℝ⁴ ∖ 0) it is affine,
ω_μ = a_μ + B_μκ x^κ with B antisymmetric. The splitting [[eq:iii-a1-2-2]] does not depend on t, so ω is independent of
t, which forces B_μ0 = 0: ω is a combination of dt, the dxⁱ and the rotation forms B_ij xʲ dxⁱ. These are homogeneous
of degree 0, 0 and 1 in x and, in [[eq:iii-a1-2-2]], of the types s0 (dt = ½(dx̄⁰ + dx̄¹)), s1
(dxⁱ = x̂_i dr + r dx̂_i = ½x̂_i(dx̄⁰ − dx̄¹) + r dx̂_i) and v1 (by [[def:iii-a1-1-7]]). A nonzero ρ^ι u of a single type
and degree is therefore one of these, with ι = 0, 0 and −1 respectively. ∎

### What changes for the black hole family in dimension 4 + 1 {#sec:iii-b-1}

Throughout [[sec:iii-b-1]] to [[sec:iii-b-6]], spacetime is ℝ^(1+4) with coordinates (t, x), x ∈ ℝ⁴, |x| is the
Euclidean norm, x̂ := x/|x| ∈ 𝕊³, η := −dt² + dx², and X̄ denotes the radial compactification of ℝ⁴_x; C^∞(X̄) near
infinity consists of the smooth functions of (|x|⁻¹, x̂). The changes from [Hin26, Sections 3–4] are these.

(a) The sphere at infinity is 𝕊³, and the angular indices are 2, 3, 4.

(b) The family is g_b, b = (m, A), m > 0, A ∈ 𝔰𝔬(4): seven parameters where Kerr has four, 𝔰𝔬(4) being
six-dimensional. The mass enters at |x|⁻² and the spin at |x|⁻³, where for Kerr they enter at r⁻¹ and r⁻².

(c) There is no logarithm: the ingoing and outgoing times differ by 2∫^r m(s² − m)⁻¹ ds ∈ |x|⁻¹C^∞
([[lem:iii-b-3-5]]).

(d) The boosts are four, S ranging over the restrictions to 𝕊³ of linear functions, and the boosted mass term has the
exponent 4 and the constant 2/π² where [Hin26] has 3 and 3/(4π) ([[lem:iii-b-5-2]]).

(e) The trace weight of the gauge modifications is 2/(5 − 2) = 2/3 where [Hin26] has 1, so that the modifications act
on trace-reversed tensors exactly as in dimension 3 + 1 ([[lem:iii-b-6-2]]).

### The compactification {#sec:iii-b-2}

Fix m₀ > 0 and set R₁ := m₀^(1/2). Fix the *inner radius* r_♭ ∈ (0, ½R₁]. Nothing below is uniform in r_♭: every
constant chosen from the inner radius is chosen from r_♭. (In [[ch:s12]] the radius r₀ of the artificial boundary of
[[sec:i-a-1-1]] is put at r_♭.)

**Definition {#def:iii-b-2-1}** ([Hin26, Definitions 3.1–3.2, (3.2)–(3.3)].) ℝ̄^(1+4) is the radial compactification,
k_± the two points at future and past timelike infinity of the closure of {|x| ≤ C}, and Y_+ ⊂ ∂ℝ̄^(1+4) the 3-sphere
{1/t = 0, (t − |x|)/t = 0} in the closure of {t > 0}. M̃ := [ℝ̄^(1+4); k_+, Y_+], and

    M := cl_(M̃) {|x| ≥ r_♭, t ≥ −½|x|},                                                               {#eq:iii-b-2-1}

with boundary hypersurfaces I₀ (spacelike infinity), ℐ⁺ (the lift of Y_+), ι⁺ (future timelike infinity), K⁺ (the lift
of k_+), Σ^past := {t = −½|x|} and Σ^int := {|x| = r_♭}. M̃_(1/2) and M_(1/2) are obtained by declaring the square root
of a defining function of ℐ⁺ smooth.

Local coordinates, with ω ∈ 𝕊³ and t₀ := t − |x|, are those of [Hin26, (3.4a)–(3.4h)] with r replaced by |x| and 𝕊² by
𝕊³:

    τ = t/|x|, ρ = 1/|x|;     ρ₀ = 1/(|x| − t + 2), ρ_I = (|x| − t + 2)/|x|;     t₀, ρ_I = 1/|x|;
    ρ_I = (t − |x| + 2)/|x|, ρ_+ = 1/(t − |x| + 2);     ρ_+ = 1/|x|, v = t₀/|x|;     ρ_+ = 1/|x|, ρ_K = |x|/t₀;
    ρ_K = t₀⁻¹, x,                                                                                        {#eq:iii-b-2-2}

near the interior of I₀, near I₀ ∩ ℐ⁺, near the interior of ℐ⁺, near ℐ⁺ ∩ ι⁺, near the interior of ι⁺, near ι⁺ ∩ K⁺
and near the interior of K⁺. These are the coordinates of the iterated blow-up of the radial compactification at k_+
and at Y_+ ([[def:ii-a-1-2]] constructs the same blow-ups; nothing in the construction depends on the dimension). ℐ⁺
fibres over Y_+ ≅ 𝕊³ with fibres ℝ_(t₀). Two facts are used repeatedly: the functions in C^∞(X̄) lift to smooth
functions on M (they are smooth functions of ρ = |x|⁻¹ and ω, and ρ = ρ₀ρ_I, ρ_I, ρ_Iρ_+, ρ_+, ρ_+ in the charts
listed, a smooth function on each); and dt and dxⁱ, i = 1, …, 4, form a smooth frame of the scattering cotangent bundle
T* := ˢᶜT*ℝ̄^(1+4) pulled back to M ([Hin26, Notation 3.5]). So a symmetric 2-tensor Σ g_μκ dx^μ dx^κ (x⁰ := t) lies in
C^∞(M; S²T*) when its coefficients are smooth on M, and |x|^(−j)C^∞(M; S²T*) means coefficients in |x|^(−j)C^∞(M).

**Lemma {#lem:iii-b-2-2}** ([Hin26, Lemma 3.4].) Let X := cl_(X̄){|x| ≥ r_♭} and
M′ := [ℝ̄_(t₀) × X; {±∞} × ∂X]. The identity of ℝ^(1+4) extends to a diffeomorphism from cl_(M′){t₀ ≥ 1} onto
cl_M{t₀ ≥ 1}.

*Proof.* Both sides are covered by the charts below, and the transition maps are smooth with smooth inverses. Away from
the front face {+∞} × ∂X of M′: near {+∞} × X°, (t₀⁻¹, x), which are the coordinates [[eq:iii-b-2-2]] near the interior
of K⁺; near ℝ × ∂X, (t₀, |x|⁻¹, ω), the coordinates near the interior of ℐ⁺. Near the front face, M′ has the
coordinates ((t₀ + 2)/|x|, 1/(t₀ + 2), ω) near its intersection with ℝ × ∂X, which are (ρ_I, ρ_+, ω) near ℐ⁺ ∩ ι⁺;
(1/|x|, t₀/|x|, ω) in its interior, the coordinates near the interior of ι⁺; and (1/|x|, |x|/t₀, ω) near its
intersection with {+∞} × X, the coordinates near ι⁺ ∩ K⁺. ∎

### The Myers–Perry family {#sec:iii-b-3}

#### Kerr–Schild form {#sec:iii-b-3-1}

For A ∈ 𝔰𝔬(4) let s := −½ tr(A²), p := Pf(A), ‖A‖ the operator norm, and for r > 0

    Π(r) := r⁴ + sr² + p²,     𝖬(r) := (r² + s)I + A²,     Q(r, x) := Π(r) − xᵀ𝖬(r)x.                    {#eq:iii-b-3-1}

Every A ∈ 𝔰𝔬(4) is O(aJ₁₂ + bJ₃₄)Oᵀ for some O ∈ SO(4) and a, b ∈ ℝ, where J_ij is the elementary rotation generator
with (J_ij)_ij = 1 = −(J_ij)_ji (the normal form of real antisymmetric matrices). In this *rotated frame*
A² = −diag(a², a², b², b²), s = a² + b², p² = a²b² and ‖A‖ = max(|a|, |b|); in particular s ≤ 2‖A‖².

**Lemma {#lem:iii-b-3-1}** (The radial function.) (a) A⁴ + sA² + p²I = 0 and (r²I − A²)𝖬(r) = Π(r)I. (b) For
|x|² > s (note s ≥ ‖A‖²), Q(·, x) has exactly one zero r = r_A(x) in (0, ∞), and it is simple; r_A is smooth in
(x, A), r₀(x) = |x|, r_A(x)² ≤ |x|² ≤ r_A(x)² + ‖A‖², and r_A ∈ |x|(1 + |x|⁻²C^∞(X̄)) near infinity, smoothly in A.

*Proof.* (a) For real antisymmetric 4 × 4 matrices, det(ζI − A) = ζ⁴ + (Σ_(i<j) A_ij²)ζ² + Pf(A)², and
Σ_(i<j) A_ij² = −½ tr(A²) = s; so the first identity is the Cayley–Hamilton theorem. (In the rotated frame it reads
a⁴ − (a² + b²)a² + a²b² = 0 and the same with a, b exchanged.) Then
(r²I − A²)𝖬(r) = r⁴ + sr² + r²A² − (r² + s)A² − A⁴ = r⁴ + sr² − sA² − A⁴ = Π(r)I. (b) With y := r²,
Q = y² + (s − |x|²)y + p² − s|x|² + |Ax|², using −xᵀA²x = |Ax|². In the rotated frame the constant term is
c₀ := a²b² − (a² + b²)|x|² + a²(x₁² + x₂²) + b²(x₃² + x₄²) ≤ a²b² − min(a², b²)|x|², which is negative when
min(a², b²) > 0 and |x|² > max(a², b²), and equals −a²(x₃² + x₄²) ≤ 0 (or the same with the roles exchanged) when b = 0.
So c₀ ≤ 0 on {|x|² > s}. The discriminant is (|x|² − s)² − 4c₀ ≥ (|x|² − s)² > 0, so the two roots are real and
distinct, their product c₀ ≤ 0 and their sum |x|² − s > 0: exactly one is positive, it is simple, and it is smooth in
the coefficients:

    r_A² = ½(|x|² − s + ((|x|² − s)² − 4(p² − s|x|² + |Ax|²))^(1/2)).

With z := |x|⁻² this is |x|² · ½(1 − sz + ((1 − sz)² − 4z(p²z − s + |Ax̂|²))^(1/2)), a smooth function of (z, x̂, A) near
z = 0 with value 1 at z = 0; so r_A² ∈ |x|²(1 + |x|⁻²C^∞(X̄)) and likewise r_A. At A = 0, Q = y(y − |x|²), so
r₀ = |x|. Finally Q = 0 and (a) give xᵀ(r_A²I − A²)⁻¹x = 1; as −A² ≥ 0 with largest eigenvalue ‖A‖², the eigenvalues
of (r_A²I − A²)⁻¹ lie in [(r_A² + ‖A‖²)⁻¹, r_A⁻²], which gives the two bounds on |x|². ∎

**Definition {#def:iii-b-3-2}** (Myers–Perry in Kerr–Schild form.) For m > 0, A ∈ 𝔰𝔬(4) and |x|² > s, with r := r_A(x)
and Π, 𝖬 evaluated at r,

    ℓ_A := (𝖬(rI + A)x/Π) · dx,     k_A := dt + ℓ_A,     F_A := 1 + xᵀA²𝖬²x/Π²,     H_(m,A) := mr²/(ΠF_A),
    g^KS_(m,A) := η + H_(m,A) k_A ⊗ k_A.                                                                 {#eq:iii-b-3-2}

**Lemma {#lem:iii-b-3-3}** (Kerr–Schild algebra.) On {|x|² > s}: (a) |ℓ_A|_eucl = 1, so k_A is null for η;
(b) ℓ_A(x · ∂_x) = r_A(x), so ℓ_A(x̂ · ∂_x) = r_A/|x| ∈ (0, 1]; (c) if ‖A‖²(r_A² + ‖A‖²) < r_A⁴, then F_A ∈ (0, 1] and
H_(m,A) > 0; (d) (g^KS_(m,A))⁻¹ = η⁻¹ − H_(m,A) k_A^♯ ⊗ k_A^♯, k_A^♯ := η⁻¹(k_A, ·); (e) for β ∈ (−1, 1], wherever (c)'s
condition holds, (g^KS_(m,A))⁻¹(dt − β d|x|, dt − β d|x|) < 0.

*Proof.* Put 𝖭 := (r²I − A²)⁻¹, which is 𝖬/Π by [[lem:iii-b-3-1]] (a); 𝖭 is symmetric and commutes with A, so 𝖭A is
antisymmetric. The coefficient vector of ℓ_A is 𝖭(r + A)x, and Q = Π(1 − xᵀ𝖭x). (a), (b): xᵀ𝖭Ax = 0, so
ℓ_A(x · ∂_x) = xᵀ𝖭(r + A)x = r xᵀ𝖭x = r(1 − Q/Π); and, as (r − A)𝖭²(r + A) = 𝖭²(r² − A²) = 𝖭,
|𝖭(r + A)x|² = xᵀ(r − A)𝖭²(r + A)x = xᵀ𝖭x = 1 − Q/Π. Both identities hold for every r > 0, and at r = r_A(x), where
Q = 0, they give (a) and (b); r_A/|x| ∈ (0, 1] by [[lem:iii-b-3-1]] (b). (c) 𝖬 commutes with A, so A𝖬 is antisymmetric
and xᵀA²𝖬²x = −|A𝖬x|²; so F_A ≤ 1. By [[lem:iii-b-3-1]] (a), 𝖬/Π = (r²I − A²)⁻¹ has norm at most r⁻², so
|A𝖬x|/Π ≤ ‖A‖|x|r⁻² ≤ ‖A‖(r² + ‖A‖²)^(1/2)r⁻² < 1 under (c)'s condition ([[lem:iii-b-3-1]] (b)); so F_A > 0, and
H_(m,A) > 0 as Π > 0 for r > 0. (d) η⁻¹(k_A, k_A) = 0 by (a), and then
(η + Hk ⊗ k)(η⁻¹ − Hk^♯ ⊗ k^♯) = I + Hk ⊗ k^♯ − Hk ⊗ k^♯ − H²η⁻¹(k, k)k ⊗ k^♯ = I. (e) With Θ := dt − β d|x|,
η⁻¹(Θ, Θ) = −1 + β² and k_A^♯(Θ) = η⁻¹(k_A, Θ) = −1 − βℓ_A(x̂ · ∂_x) = −1 − βr_A/|x|. So the quantity is
−(1 − β²) − H(1 + βr_A/|x|)²; for β ∈ (−1, 1) the first term is negative and the second non-positive; for β = 1 the
first vanishes and the second is −H(1 + r_A/|x|)² < 0. ∎

**Proposition {#prop:iii-b-3-4}** (The Myers–Perry family.) g^KS_(m,A) is Ricci-flat where it is defined and
H_(m,A) > 0. At A = 0 it is the five-dimensional Schwarzschild–Tangherlini metric η + m|x|⁻²(dt + d|x|)², whose future
event horizon is {|x| = m^(1/2)}.

This is the Myers–Perry family [MP86] in Kerr–Schild form ([ER08, (31), p. 14]). We use the following result as a black
box; it is part of [[thm:std-myers-perry]], restated here because the proof below uses its formulas.

[ER08, Section 4.2, (42) and (44), p. 16] (the general Myers–Perry solution of [MP86] in odd spacetime dimension; here
dimension 5, i = 1, 2, summation over i). For a mass parameter m > 0 and spins a₁, a₂ ∈ ℝ, the metric

    −dt′² + (r² + a_i²)(dμ_i² + μ_i² dφ_i²) + (mr²/(ΠF))(dt′ − a_iμ_i² dφ_i)² + (ΠF/(Π − mr²)) dr²,
    F = 1 − a_i²μ_i²/(r² + a_i²),     Π = (r² + a₁²)(r² + a₂²),     μ₁² + μ₂² = 1,                         {#eq:s11-er08}

is a solution of the vacuum Einstein equations; its event horizon is at the largest root r₀ of Π(r₀) − mr₀² = 0
([ER08, (45), p. 16]).

*Proof.* *The rotated frame.* Let A = aJ₁₂ + bJ₃₄ and put a₁ := −a, a₂ := −b. Then 𝖬/Π = (r²I − A²)⁻¹ is diagonal with
entries (r² + a_i²)⁻¹ on the i-th plane, Π(r) = (r² + a₁²)(r² + a₂²) is the Π of [[eq:s11-er08]], and Q = 0 reads
Σ_i (x²_(2i−1) + x²_(2i))/(r² + a_i²) = 1. On the dense open set where x₁² + x₂² > 0 and x₃² + x₄² > 0 introduce
coordinates (r, μ₁, ψ₁, ψ₂), with μ_i > 0, μ₁² + μ₂² = 1 and r = r_A(x), by

    x_(2i−1) + ix_(2i) = (r² + a_i²)^(1/2) μ_i e^(iψ_i),     i = 1, 2.

These are coordinates: the inverse map is r = r_A(x), μ_i = |(x_(2i−1), x_(2i))|(r_A(x)² + a_i²)^(−1/2),
ψ_i = arg(x_(2i−1) + ix_(2i)), smooth on that set by [[lem:iii-b-3-1]] (b), and μ₁² + μ₂² = 1 is Q(r_A(x), x) = 0. In
the i-th plane, with R_i := (r² + a_i²)^(1/2)μ_i, x dx + y dy = R_i dR_i = rμ_i² dr + (r² + a_i²)μ_i dμ_i and
x dy − y dx = R_i² dψ_i, (x, y) := (x_(2i−1), x_(2i)). Since Σ_i μ_i dμ_i = 0,

    dx² = Σ_i (r² + a_i²)(dμ_i² + μ_i² dψ_i²) + F dr²,     F := Σ_i r²μ_i²/(r² + a_i²) = 1 − Σ_i a_i²μ_i²/(r² + a_i²),

and, as (Ax)_(2i−1) = −a_i x_(2i), (Ax)_(2i) = a_i x_(2i−1),

    ℓ_A = Σ_i (r(x dx + y dy) + a_i(x dy − y dx))/(r² + a_i²) = F dr + Σ_i a_iμ_i² dψ_i.

Also xᵀA²𝖬²x/Π² = xᵀA²(r²I − A²)⁻²x = −Σ_i a_i²R_i²/(r² + a_i²)², so F_A = F. Hence, with U := mr²/(ΠF),

    g^KS_(m,A) = −dt² + Σ_i (r² + a_i²)(dμ_i² + μ_i² dψ_i²) + F dr² + U(dt + F dr + Σ_i a_iμ_i² dψ_i)².

On {Π − mr² ≠ 0} put dt = dt′ + f₀(r) dr and dψ_i = −dφ_i + f_i(r) dr with

    f₀ := mr²/(Π − mr²),     f_i := −a_i mr²/((r² + a_i²)(Π − mr²)),

functions of r alone, so that t′ and φ_i are coordinates. Then k_A = dt′ − Σ_i a_iμ_i² dφ_i + K dr with
K := f₀ + F + Σ_i a_iμ_i² f_i. Put K₀ := FΠ/(Π − mr²); as UF = mr²/Π, UK₀ = mr²/(Π − mr²) = f₀ and
f_i = −UK₀a_i/(r² + a_i²), so, with Σ_i a_i²μ_i²/(r² + a_i²) = 1 − F, K = UK₀ + F − UK₀(1 − F) = F(1 + UK₀) = K₀. In
the new coordinates the coefficients of dr dt′ and dr dφ_i are −2f₀ + 2UK = 0 and −2(r² + a_i²)μ_i² f_i − 2UKa_iμ_i² = 0,
and the coefficient of dr² is

    −f₀² + Σ_i (r² + a_i²)μ_i² f_i² + F + UK² = −U²K² + U²K²(1 − F) + F + UK² = F(1 + UK) = FΠ/(Π − mr²).

So g^KS_(m,A) is the metric [[eq:s11-er08]] with these spins on the set where x₁² + x₂² > 0, x₃² + x₄² > 0 and
Π(r_A) ≠ mr_A², and is Ricci-flat there. This set is dense in the domain: its complement there lies in two 2-planes
and in the level sets {r_A = c} for the finitely many positive roots c of Π(c) − mc², each of which is the quadric
{xᵀ(c²I − A²)⁻¹x = 1} by [[lem:iii-b-3-1]]. Being smooth, g^KS_(m,A) is Ricci-flat on the whole of its domain.

*Every A.* For O ∈ O(4), s and p² are unchanged under A ↦ OAOᵀ, 𝖬(r) becomes O𝖬(r)Oᵀ, Q(r, Ox) for OAOᵀ is Q(r, x) for
A, so r_(OAOᵀ)(Ox) = r_A(x), and the coefficient vector of ℓ, F and H are carried along. So the linear map
L_O(t, x) := (t, Ox) satisfies L_O*g^KS_(m,OAOᵀ) = g^KS_(m,A), and Ricci-flatness passes to every A ∈ 𝔰𝔬(4).

*At A = 0*, ℓ₀ = x̂ · dx = d|x| and H_(m,0) = m|x|⁻², which is the stated metric; at a₁ = a₂ = 0 the largest root of
Π(r₀) − mr₀² = r₀²(r₀² − m) is r₀ = m^(1/2), and r = |x| there. The Ricci-flatness at A = 0 can also be checked directly.
In coordinates (t, |x|, ω), g^KS_(m,0) = −f dt² + 2(1 − f) dt d|x| + (2 − f) d|x|² + |x|²g̸ with f := 1 − m|x|⁻², and on
{f ≠ 0}, with t_s := t − ∫(1 − f)/f d|x|, it is −f dt_s² + f⁻¹ dr² + r²g̸, r := |x| (the cross term is
−2f(1 − f)/f + 2(1 − f) = 0, and the dr² coefficient is −(1 − f)²/f + 2(1 − f)²/f + 2 − f = 1/f). Its Christoffel
symbols are Γ^(t_s)_(t_s r) = f′/(2f), Γ^r_(t_s t_s) = ff′/2, Γ^r_rr = −f′/(2f), Γ^r_ab = −rf g̸_ab, Γ^a_rb = r⁻¹δ^a_b
and those of g̸, and the Ricci tensor is R_(t_s t_s) = f(r³f′)′/(2r³), R_rr = −(r³f′)′/(2fr³),
R_ab = (2(1 − f) − rf′)g̸_ab, the others zero. For f = 1 − mr⁻², r³f′ = 2m is constant and 2(1 − f) − rf′ = 0. ∎

**Definition {#def:s11-parameters}** (The parameter set.) Let ε_♭ := min(1/20, r_♭/(4R₁)) and

    ℬ := {b = (m, A) : |m − m₀| < ½m₀, ‖A‖ < ε_♭R₁},     b₀ := (m₀, 0).

For b = (m, A) write g^KS_b := g^KS_(m,A). On ℬ, ‖A‖ < r_♭/4 and ‖A‖ < R₁/20; at r_♭ = ½R₁, ε_♭ = 1/20. This one set
serves the whole stability theory: every neighbourhood of b₀ used in [[ch:s12]] lies in ℬ. Only b near b₀ is used
below.

**Lemma {#lem:s11-ks-domain}** (The Kerr–Schild domain.) Let b = (m, A) ∈ ℬ and |x| ≥ ½r_♭. Then
|x|² > 2‖A‖² ≥ s, r_A(x)² > 3‖A‖², and the condition of [[lem:iii-b-3-3]] (c) holds, so that F_A ∈ (0, 1]. Hence
g^KS_b is defined and smooth on ℝ_t × {|x| ≥ ½r_♭}, smoothly in b, with H_(m,A) > 0; det g^KS_b = −1 in the
coordinates (t, x); g^KS_b is Lorentzian of signature (1, 4), with inverse η⁻¹ − H_(m,A) k_A^♯ ⊗ k_A^♯; and g^KS_b is
Ricci-flat there. The horizon {|x| = m^(1/2)} of g^KS_(m,0) lies in {|x| > r_♭}. At r_♭ = ½R₁ the domain is
{|x| ≥ ¼R₁}.

*Proof.* ‖A‖ < ε_♭R₁ ≤ r_♭/4, so ‖A‖² < r_♭²/16 and |x|² ≥ r_♭²/4 > r_♭²/8 > 2‖A‖² ≥ s. By [[lem:iii-b-3-1]] (b),
r_A² ≥ |x|² − ‖A‖² > r_♭²/4 − r_♭²/16 = 3r_♭²/16 > 3‖A‖². Hence ‖A‖²(r_A² + ‖A‖²) < (r_A²/3)(4r_A²/3) = (4/9)r_A⁴ < r_A⁴,
which is (c)'s condition, so F_A ∈ (0, 1] and H_(m,A) > 0 by [[lem:iii-b-3-3]] (c); smoothness in (x, b) is that of
r_A ([[lem:iii-b-3-1]] (b)). As k_A is η-null ([[lem:iii-b-3-3]] (a)), the determinant of a rank-one perturbation gives
det(η + H_(m,A) k_A ⊗ k_A) = det η (1 + H_(m,A) η⁻¹(k_A, k_A)) = −1. For c ∈ [0, 1] the metrics
η + cH_(m,A) k_A ⊗ k_A likewise have determinant −1, so their signature is that of η, (1, 4). The inverse is
[[lem:iii-b-3-3]] (d), and Ricci-flatness is [[prop:iii-b-3-4]]. Finally m^(1/2) > (½m₀)^(1/2) = R₁/√2 > ½R₁ ≥ r_♭. ∎

In particular, for b ∈ ℬ and |x| ≥ r_♭, g^KS_b is defined, smooth, with H_(m,A) > 0, on ℝ_t × {|x| ≥ r_♭}, smoothly
in b; and the horizon of g^KS_(m,0) is at |x| = m^(1/2) ∈ (R₁/√2, (3/2)^(1/2)R₁).

#### The outgoing form near infinity {#sec:iii-b-3-2}

Fix χ_∞ ∈ C^∞(ℝ), non-decreasing, equal to 0 on (−∞, 2R₁] and to 1 on [3R₁, ∞). For m ∈ (½m₀, (3/2)m₀) let

    T_m(ϱ) := 2∫_ϱ^∞ χ_∞(s) m/(s² − m) ds,     Φ_m(t, x) := (t − T_m(|x|), x),     g_b := Φ_m*g^KS_b.     {#eq:iii-b-3-3}

(s² − m ≥ 4m₀ − (3/2)m₀ = (5/2)m₀ on supp χ_∞.) Write g_m := g_(m,0) and ḡ := η. Since T_m is constant on [0, 2R₁],
[[eq:iii-b-3-3]] defines g_b on ℝ_t × {|x| ≥ ½r_♭}, and there g_b is g^KS_b translated in time on {|x| ≤ 2R₁}.

**Lemma {#lem:iii-b-3-5}** (No logarithm.) (a) T_m ∈ |x|⁻¹C^∞(X̄) near infinity, with
T_m(ϱ) = m^(1/2) log((ϱ + m^(1/2))/(ϱ − m^(1/2))) = 2m/ϱ + 2m²/(3ϱ³) + O(ϱ⁻⁵) for ϱ ≥ 3R₁, smooth in m. (b) For
|x| ≥ 3R₁,

    g_m = η + (m/|x|²)(dt − d|x|)² = −f dt² − (2m/|x|²) dt d|x| + (2 − f) d|x|² + |x|²g̸,     f := 1 − m/|x|²,
                                                                                                          {#eq:iii-b-3-4}

g̸ the round metric of 𝕊³. (c) Φ_m is a diffeomorphism of ℝ_t × {|x| ≥ r_♭} which equals a time translation on
{|x| ≤ 2R₁}; it extends to a diffeomorphism of M̃ near {|x| ≥ r_♭} preserving every boundary hypersurface, and Φ_m* maps
ρ₀^α ρ_I^β ρ_+^γ ρ_K^δ C^∞(M; S²T*) into itself near I₀ ∪ ℐ⁺ ∪ ι⁺ ∪ K⁺, for all weights.

*Proof.* (a) For ϱ ≥ 3R₁, T_m(ϱ) = 2∫_ϱ^∞ m/(s² − m) ds = 2m^(1/2) artanh(m^(1/2)/ϱ), an odd power series in m^(1/2)/ϱ
convergent for ϱ > m^(1/2). (b) On {|x| ≥ 3R₁}, Φ_m*dt = dt − T_m′ d|x| = dt + (2m/(|x|² − m)) d|x|, and
g^KS_(m,0) = η + (m/|x|²)(dt + d|x|)², whose (t, |x|) block has g_tt = −f, g_(t|x|) = m/|x|² and g_(|x||x|) = 1 + m/|x|².
Substituting, the (t, |x|) block of Φ_m*g^KS_(m,0) has g_tt = −f,
g_(t|x|) = m/|x|² + (−f)(2m/(|x|² − m)) = m/|x|² − 2m/|x|² = −m/|x|², and
g_(|x||x|) = 1 + m/|x|² + 2(m/|x|²)(2m/(|x|² − m)) − f(2m/(|x|² − m))² = 1 + m/|x|², the last two terms cancelling as
f/(|x|² − m) = |x|⁻²; this is [[eq:iii-b-3-4]]. (c) T_m is smooth and bounded, so Φ_m is a diffeomorphism with inverse
(t, x) ↦ (t + T_m(|x|), x), a time translation by −T_m(2R₁) on {|x| ≤ 2R₁}. In each chart of [[eq:iii-b-2-2]] the lift
is smooth with smooth inverse: t₀ ↦ t₀ − T_m with T_m ∈ ρC^∞ near ℐ⁺; ρ₀ ↦ ρ₀(1 + ρ₀T_m)⁻¹, ρ_+ ↦ ρ_+(1 − ρ_+T_m)⁻¹,
ρ_K = t₀⁻¹ ↦ ρ_K(1 − ρ_KT_m)⁻¹, τ ↦ τ − ρT_m, and near ι⁺ ∩ K⁺, ρ_K = |x|/t₀ ↦ ρ_K(1 − ρ_+ρ_KT_m)⁻¹, the other
coordinates fixed; each factor is 1 + O(ρ) or 1 + O(ρ_K) with ρ ∈ ρ₀ρ_Iρ_+C^∞. So the defining functions are multiplied
by positive smooth functions and the weighted spaces are preserved. On the bundle, Φ_m*dt = dt − T_m′(|x|)x̂ · dx and
Φ_m*dxⁱ = dxⁱ, with T_m′x̂ⁱ ∈ C^∞(X̄): a smooth bundle map of T*. ∎

**Proposition {#prop:iii-b-3-6}** ([Hin26, Proposition 3.10] in dimension 4 + 1.) For b = (m, A) ∈ ℬ:
g_b ∈ C^∞(M; S²T*) and g_b⁻¹ ∈ C^∞(M; S²T), smoothly in b; and

    g_b − g_m ∈ |x|⁻³C^∞(M; S²T*),     g_m − ḡ ∈ |x|⁻²C^∞(M; S²T*),                                       {#eq:iii-b-3-5}

with g_m − ḡ = m|x|⁻²(dt − d|x|)² on {|x| ≥ 3R₁}; the same for the dual metrics, with
g_m⁻¹ − ḡ⁻¹ = −m|x|⁻²(∂_t + ∂_|x|)^(⊗2) there.

*Proof.* By [[lem:iii-b-3-5]] (c) it suffices to prove the statements for g^KS_b, with g^KS_m := g^KS_(m,0) in place of
g_m. By [[lem:iii-b-3-1]] (b), r := r_A ∈ |x|(1 + |x|⁻²C^∞(X̄)); so Π, r² + s ∈ |x|⁴(1 + |x|⁻²C^∞), resp. |x|²(…), and
𝖬/Π = (r² − A²)⁻¹ ∈ |x|⁻²(I + |x|⁻²C^∞(X̄)). Hence the coefficient vector of ℓ_A is
r𝖬x/Π + 𝖬Ax/Π = x̂ + |x|⁻¹Ax̂ + |x|⁻²C^∞(X̄); F_A ∈ 1 + |x|⁻²C^∞ and H_(m,A) ∈ m|x|⁻²(1 + |x|⁻²C^∞(X̄)), all smooth in
b. As dt, dxⁱ form a smooth frame of T* on M and C^∞(X̄) lifts into C^∞(M) ([[sec:iii-b-2]]),
g^KS_b = η + H(dt + ℓ_A)² ∈ C^∞(M; S²T*). At A = 0, ℓ₀ = x̂ · dx = d|x| and H_(m,0) = m|x|⁻², so
g^KS_m − η = m|x|⁻²(dt + d|x|)² ∈ |x|⁻²C^∞; and H_(m,A) − H_(m,0) ∈ |x|⁻⁴C^∞, ℓ_A − ℓ₀ ∈ |x|⁻¹C^∞(X̄; T*), so
g^KS_b − g^KS_m ∈ |x|⁻³C^∞. The dual metrics are η⁻¹ − Hk^♯ ⊗ k^♯ ([[lem:iii-b-3-3]] (d)), and the same argument
applies. On {|x| ≥ 3R₁} the formula for g_m is [[eq:iii-b-3-4]]; its inverse follows by applying [[lem:iii-b-3-3]] (d)
to the outgoing Kerr–Schild form η + m|x|⁻²(dt − d|x|)², dt − d|x| being η-null with η⁻¹(dt − d|x|, ·) = −∂_t − ∂_|x|.
∎

So the mass of g_b appears in g_b − ḡ at |x|⁻² = ρ₀²ρ_I²ρ_+² (in the charts [[eq:iii-b-2-2]], up to smooth positive
factors), its spin at |x|⁻³: one order of |x|⁻¹ further than for Kerr in each case.

#### Time functions {#sec:iii-b-3-3}

Let

    ψ(ϱ) := ∫_(r_♭)^ϱ (1 − χ_∞(s) 8m₀/s²) ds,     t_* := t − ψ(|x|).                                   {#eq:iii-b-3-6}

For ϱ ≥ 3R₁, ψ(ϱ) = ϱ − C′ + 8m₀/ϱ with a constant C′ (depending on r_♭); so t_* = t₀ + C′ − 8m₀|x|⁻¹ near infinity,
the form of [Hin26, (3.13)] with T̃ = C′ − Cr⁻¹.

**Lemma {#lem:iii-b-3-7}** ([Hin26, Lemmas 3.6–3.7] in dimension 4 + 1.) (a) For every b ∈ ℬ, dt_* is timelike for
g_b on {|x| ≥ r_♭}, and t_* ≤ t there. (b) There is t_IVP = t − ψ_IVP(|x|) with ψ_IVP = ψ on [r_♭, 5R₁], ψ_IVP
constant on [R₃, ∞) for some R₃, such that dt_IVP is timelike for every g_b, b ∈ ℬ, on {|x| ≥ r_♭}, t_IVP ≤ t, and
t_IVP − t_* is a function of |x| alone.

*Proof.* Pull back by Φ_m⁻¹: in the Kerr–Schild coordinates (t_KS, x) = Φ_m(t, x), t = t_KS + T_m(|x|), so a function
t − φ(|x|) has differential dt_KS − β d|x| with β := φ′ − T_m′ = φ′ + 2χ_∞ m/(|x|² − m). By [[lem:iii-b-3-3]] (e),
which applies by [[lem:s11-ks-domain]], it suffices that β ∈ (−1, 1] on [r_♭, ∞).

(a) φ = ψ: β = 1 − χ_∞(8m₀/ϱ² − 2m/(ϱ² − m)). Off supp χ_∞, β = 1. On it, ϱ ≥ 2R₁, that is ϱ² ≥ 4m₀, and
m < (3/2)m₀: (8m₀ − 2m)ϱ² − 8m₀m ≥ 5m₀ · 4m₀ − 12m₀² > 0, so the bracket is positive and β < 1; and
β ≥ 1 − 8m₀/ϱ² > 1 − 2 = −1 for ϱ > 2R₁ (at ϱ = 2R₁, χ_∞ = 0). For t_* ≤ t: ψ = ϱ − r_♭ ≥ 0 on [r_♭, 2R₁] and
ψ(2R₁) = 2R₁ − r_♭ ≥ (3/2)R₁; ψ′ ≥ 1 − 8m₀/(4m₀) = −1 on [2R₁, 3R₁], so ψ ≥ ½R₁ there; and ψ′ ≥ 1 − 8/9 > 0 on
[3R₁, ∞). So ψ ≥ 0 on [r_♭, ∞).

(b) Choose ψ_IVP′ ∈ C^∞ with ψ_IVP′ = ψ′ on [r_♭, 5R₁], 0 ≤ ψ_IVP′ ≤ ψ′ on [5R₁, ∞), and ψ_IVP′ = 0 on [R₃, ∞) (possible
as ψ′ > 0 there), and ψ_IVP(r_♭) = 0. Then β = ψ_IVP′ + 2χ_∞ m/(ϱ² − m) lies in (0, 1) on [5R₁, ∞) (it is positive,
and at most the value for ψ, which is < 1 by (a)) and equals the value for ψ on [r_♭, 5R₁]. ψ_IVP ≥ 0 as ψ ≥ 0 on
[r_♭, 5R₁] and ψ_IVP is non-decreasing after. ∎

The formulas [[eq:iii-b-3-3]] and [[eq:iii-b-3-6]] define g_b and t_* also on ℝ_t × {½r_♭ ≤ |x| ≤ r_♭}, where χ_∞ = 0,
T_m is constant and ψ′ = 1; there β = 1 in the proof of (a), so dt_* is timelike for g_b by [[lem:iii-b-3-3]] (e) and
[[lem:s11-ks-domain]]. The inequality t_* ≤ t is not claimed there, where ψ < 0.

So t_IVP = t − C″ for |x| ≥ R₃: its level set Σ^IVP := t_IVP⁻¹(0) is asymptotically flat and ends at I₀, and the level
sets of t_* end at ℐ⁺.

#### Linearised metrics, and initial data {#sec:iii-b-3-4}

**Definition {#def:iii-b-3-8}** ([Hin26, Definition 3.11].) For b ∈ ℬ and ḃ = (ṁ, Ȧ) ∈ ℝ × 𝔰𝔬(4),
ġ_b(ḃ) := (d/ds) g_(b+sḃ)|_(s=0).

By [[prop:iii-b-3-6]], smoothly in b,

    ġ_b(ḃ) ∈ |x|⁻²C^∞(M; S²T*),     ġ_b(0, Ȧ) ∈ |x|⁻³C^∞(M; S²T*).                                       {#eq:iii-b-3-7}

(For the first: d/ds of g_(m+sṁ) − ḡ ∈ |x|⁻²C^∞, using that Φ_m depends smoothly on m and [[lem:iii-b-3-5]] (c) holds
uniformly; for the second: d/ds of g_((m,A+sȦ)) − g_m ∈ |x|⁻³C^∞.)

**Lemma {#lem:iii-b-3-9}** ([Hin26, Lemma 3.13 and Remark 3.14] in dimension 4 + 1.) Let γ_b, k_b be the metric and
second fundamental form induced by g_b on Σ^IVP, identified with X by (t, x) ↦ x (as in [Hin26, Definition 3.12], with
the future unit normal). Then

    γ_m = (1 + m/|x|²) d|x|² + |x|²g̸  on {|x| ≥ R₃},     γ_b − γ_m ∈ |x|⁻³C^∞(X; S²T*X),                 {#eq:iii-b-3-8}

    k_m, ∂_b k_b ∈ |x|⁻³C^∞(X; S²T*X),     k_b − k_m ∈ |x|⁻⁴C^∞(X; S²T*X).                                {#eq:iii-b-3-9}

*Proof.* On {|x| ≥ R₃}, Σ^IVP = {t = C″} and dt = 0 on it, so by [[eq:iii-b-3-4]] the induced metric of g_m is
η|_(dt=0) + m|x|⁻²d|x|², which is the first formula of [[eq:iii-b-3-8]]; the second follows from [[eq:iii-b-3-5]]
restricted to {t = C″} (restriction maps |x|^(−j)C^∞(M; S²T*) near I₀ into |x|^(−j)C^∞(X; S²T*X), as {t = C″} meets
the boundary of M only in I₀, transversally). Near infinity Σ^IVP = {t = C″}, and as g_b(ν_b, ∂_j) = 0,
k_b(∂_i, ∂_j) = g_b(∇_(∂_i)ν_b, ∂_j) = −g_b(ν_b, ∇_(∂_i)∂_j) = −ν_b^α Γ(g_b)_(αij),
Γ_(αij) := ½(∂_i g_(αj) + ∂_j g_(αi) − ∂_α g_ij), with ν_b the future unit normal. Since g_b − η ∈ |x|⁻²C^∞, the
Christoffel symbols Γ(g_b)_(αij) in the coordinates (t, x) are first derivatives ∂_x of |x|⁻²C^∞(X̄) (the coefficients
are t-independent), hence in |x|⁻³C^∞(X̄), and ν_b ∈ ∂_t + |x|⁻²C^∞; so k_b ∈ |x|⁻³C^∞, and the same with
g_b − g_m ∈ |x|⁻³C^∞ gives k_b − k_m ∈ |x|⁻⁴C^∞, and smoothness in b gives the derivative. ∎

The data class of the stability theory is then that of [Hin26, Remark 3.14] shifted by one order: γ_m modulo
O(|x|^(−2−ε)), k_m modulo O(|x|^(−3−ε)). Which data lie in it is shown in [[ch:s27]].

### Null coordinates near null infinity {#sec:iii-b-4}

On {|x| ≥ 3R₁} let r_* := |x| − ½T_m(|x|) = |x| + ½m^(1/2) log((|x| − m^(1/2))/(|x| + m^(1/2))), so dr_*/d|x| = f⁻¹,
and ([Hin26, (3.29)])

    x¹ := t − |x| = t₀,     x⁰ := t + 2r_* − |x| = t + |x| − T_m(|x|).                                   {#eq:iii-b-4-1}

**Lemma {#lem:iii-b-4-1}** ([Hin26, (3.30)–(3.33) and Lemma 3.15] in dimension 4 + 1.) On {|x| ≥ 3R₁}:

    g_m = −f dx⁰dx¹ + |x|²g̸,     dx⁰ = dt + ((2 − f)/f) d|x|,     dx¹ = dt − d|x|,                       {#eq:iii-b-4-2}

with ab := ½(a ⊗ b + b ⊗ a); dx⁰, dx¹ ∈ C^∞(M; T*) near I₀ ∪ ℐ⁺ ∪ ι⁺; ∂₀|x| = f/2, ∂₁|x| = −f/2; and

    ∂₀ = (f/2)(∂_t + ∂_|x|) ∈ ρ₀ρ_Iρ_+ 𝒱_b(M),     ∂₁ = (f/2)(((2 − f)/f)∂_t − ∂_|x|) ∈ ρ₀ρ_+ 𝒱_b(M).     {#eq:iii-b-4-3}

*Proof.* With c := (2 − f)/f = (|x|² + m)/(|x|² − m) = 1 − T_m′, dx⁰ = dt + c d|x| by [[eq:iii-b-4-1]]. Then
−f(dt + c d|x|)(dt − d|x|) = −f dt² − f(c − 1) dt d|x| + fc d|x|² with f(c − 1) = 2m/|x|² and fc = 2 − f, which is
[[eq:iii-b-3-4]]. c − 1 = 2m/(|x|² − m) ∈ |x|⁻²C^∞(X̄) and d|x| = x̂ · dx, so dx⁰, dx¹ are smooth sections of T*.
Inverting (dx⁰, dx¹) on the (t, |x|)-plane, d|x| = (1 + c)⁻¹(dx⁰ − dx¹) = (f/2)(dx⁰ − dx¹) (as 1 + c = 2/f) and
dt = (f/2)(dx⁰ + c dx¹), which give ∂₀|x|, ∂₁|x| and the formulas for ∂₀, ∂₁ in [[eq:iii-b-4-3]]. For the memberships
let u := t − |x|, v′ := t + |x|, so ∂_t + ∂_|x| = 2∂_(v′) and ∂_t − ∂_|x| = 2∂_u at fixed ω. Near ℐ⁺ ∩ ι⁺,
ρ_+ = (u + 2)⁻¹ and ρ_I = 2(u + 2)/(v′ − u), and |x|⁻¹ = ρ_Iρ_+; so ∂_(v′)ρ_+ = 0,
∂_(v′)ρ_I = −ρ_I/(v′ − u) = −½ρ_I²ρ_+, and ∂_(v′) = −½ρ_Iρ_+ ρ_I∂_(ρ_I) ∈ ρ_Iρ_+𝒱_b; ∂_uρ_+ = −ρ_+²,
∂_uρ_I = ρ_Iρ_+ + ½ρ_I²ρ_+, and ∂_u = −ρ_+ ρ_+∂_(ρ_+) + ρ_+(1 + ½ρ_I)ρ_I∂_(ρ_I) ∈ ρ_+𝒱_b. Near I₀ ∩ ℐ⁺,
ρ₀ = (2 − u)⁻¹, ρ_I = 2(2 − u)/(v′ − u), and the same calculation gives ∂_(v′) = −½ρ₀ρ_I ρ_I∂_(ρ_I) ∈ ρ₀ρ_I𝒱_b and
∂_u ∈ ρ₀𝒱_b. In the interior of ℐ⁺, with (t₀, ρ_I = |x|⁻¹), ∂_(v′) = −½ρ_I ρ_I∂_(ρ_I) ∈ ρ_I𝒱_b and
∂_u = ∂_(t₀) + ½ρ_I²∂_(ρ_I) ∈ 𝒱_b. In the interiors of I₀ and ι⁺ both lie in |x|⁻¹𝒱_b, linear fields with constant
coefficients being |x|⁻¹ times b-vector fields there. As ((2 − f)/f)∂_t − ∂_|x| = 2∂_u + (c − 1)(∂_u + ∂_(v′)) with
c − 1 ∈ |x|⁻²C^∞, [[eq:iii-b-4-3]] follows; the dimension enters nowhere. ∎

Correspondingly ([Hin26, (3.34)–(3.37)]), on {|x| ≥ 3R₁}, where [[eq:iii-b-4-1]] defines x⁰,

    T* = ⟨dx⁰⟩ ⊕ ⟨dx¹⟩ ⊕ |x|T*𝕊³,
    S²T* = ⟨(dx⁰)²⟩ ⊕ ⟨2dx⁰dx¹⟩ ⊕ (2dx⁰ ⊗_s |x|T*𝕊³) ⊕ ⟨(dx¹)²⟩ ⊕ (2dx¹ ⊗_s |x|T*𝕊³) ⊕ ⟨|x|²g̸⟩
           ⊕ |x|² ker tr_g̸,                                                                              {#eq:iii-b-4-4}

and in this splitting g_m = (0, −f/2, 0, 0, 0, 1, 0). *Rescaled components* ([Hin26, Definition 3.16]): with x², x³, x⁴
local coordinates on 𝕊³ and s(μ₁, …, μ_n) := #{j : μ_j ∈ {2, 3, 4}}, the rescaled components of a tensor T are
T^(ν̄₁…ν̄_p)_(μ̄₁…μ̄_q) := |x|^(s(ν)−s(μ)) T^(ν₁…ν_p)_(μ₁…μ_q). By [[prop:iii-b-3-6]],
(g_b)_(μ̄κ̄) − (g_m)_(μ̄κ̄) ∈ |x|⁻³C^∞(M), where [Hin26] has r⁻².

### Cut-off Lorentz boosts {#sec:iii-b-5}

Let 𝒮_1 := {S_w : w ∈ ℝ⁴}, S_w(ω) := w · ω on 𝕊³, the restrictions of linear functions (the space 𝒮_1 of [Hin26],
three-dimensional there, is four-dimensional here). Let ([Hin26, (3.38)])

    ω̄(S_w) := t d(|x|S_w) − |x|S_w dt = t w · dx − (w · x) dt,     X_w := ḡ⁻¹(ω̄(S_w), ·) = t w · ∂_x + (w · x)∂_t,

the generator of the Lorentz boosts in the direction w; X_w is Killing for ḡ, so δ*_ḡ ω̄(S_w) = 0. The time-s flow of
X_w is the boost of rapidity s|w|: with ŵ := w/|w|, t ↦ t cosh(s|w|) + (x · ŵ) sinh(s|w|),
x · ŵ ↦ (x · ŵ) cosh(s|w|) + t sinh(s|w|), the orthogonal components fixed. The cut-offs χ^♭_K, χ_K, χ^♯_K, χ_IVP,
χ^♯_IVP ∈ C^∞(M) are those of [Hin26, Definition 3.17] with the mass 𝔪 of the Kerr base point there replaced by R₁,
chosen consistently as follows: χ^♭_K, χ_K, χ^♯_K are supported in {t > 50R₁}; χ^♭_K = 1 on {|x| < t/10, t > 60R₁}; supp
χ^♯_K ⊂ {|x| < t/2}; χ_IVP = 1 on {t_IVP > −|x|/10}; supp χ^♯_IVP ⊂ {t_IVP > −|x|/2}; and each later function equals 1 on
a neighbourhood of the support of the earlier, with strict nesting: supp χ_IVP ⊂ int{χ^♯_IVP = 1}, supp χ^♭_K ⊂ int{χ_K =
1}. In addition fix χ_r ∈ C^∞(ℝ) equal to 0 on (−∞, 5R₁], to 1 on [6R₁, ∞), and less than 1 on (−∞, 6R₁).

**Lemma {#lem:iii-b-5-1}** ([Hin26, Lemma 3.18] in dimension 4 + 1.) V(S_w) := ½χ_r(|x|)χ^♯_IVP(1 − χ^♭_K)X_w is a
b-vector field on ℝ̄^(1+4) near its support, tangent to Y_+; its lift to M is a b-vector field vanishing near
Σ^past ∪ K⁺ ∪ Σ^int and on {|x| ≤ 5R₁}, tangent to every boundary hypersurface. Hence φ_(S_w) := exp(V(S_w)) is a
diffeomorphism of M restricting to diffeomorphisms of I₀, ℐ⁺ and ι⁺, equal to the identity near Σ^past ∪ K⁺ ∪ Σ^int and
on {|x| ≤ 5R₁}, and φ_(S_w)* maps ρ₀^α ρ_I^β ρ_+^γ C^∞(M; S²T*) to itself for all weights.

*Proof.* With ρ = |x|⁻¹, v = t₀/|x|, ω = x̂ (coordinates near Y_+ = {ρ = v = 0}): X_w|x| = tS_w, X_w t = |x|S_w,
X_w ω = (t/|x|)(w − (w · ω)ω) = (1 + v)∇̸S_w, so X_w ρ = −ρ(1 + v)S_w and X_w v = S_w − (t²/|x|²)S_w = −S_w v(2 + v):

    X_w = −S_w(1 + v)ρ∂_ρ − S_w(2 + v)v∂_v + (1 + v)∇̸S_w,                                               {#eq:iii-b-5-1}

[Hin26, (3.40)], a b-vector field tangent to {ρ = 0} and {v = 0}, the dimension entering only through ∇̸ on 𝕊³. Away
from Y_+, X_w is linear with constant coefficients, hence a b-vector field on the radial compactification, tangent to its
boundary; and the blow-up of a submanifold to which a b-vector field is tangent lifts it to a b-vector field. The cut-off
factor is smooth on M and vanishes near Σ^past (as χ^♯_IVP = 0 for t_IVP ≤ −|x|/2), near K⁺ (as 1 − χ^♭_K = 0 on
{|x| < t/10, t > 60R₁}, a neighbourhood of K⁺ in M) and on {|x| ≤ 5R₁}, which contains Σ^int (as χ_r = 0 there and
r_♭ ≤ ½R₁). The factor χ_r equals 1 near I₀ ∪ ℐ⁺ ∪ ι⁺, so it changes nothing at infinity. A complete b-vector field
tangent to all boundary hypersurfaces has a flow by diffeomorphisms preserving each of them, and its pullback preserves
each weighted space, the defining functions being multiplied by smooth positive functions. ∎

**Lemma {#lem:iii-b-5-2}** ([Hin26, Lemma 3.19] in dimension 4 + 1.) Let w ∈ ℝ⁴ be so small that every integral curve
of V(S_w) starting in supp(χ_IVP(1 − χ_K)) stays, for times in [0, 1], in {χ_r χ^♯_IVP(1 − χ^♭_K) = 1} (a subset of
{|x| ≥ 6R₁}), or in a fixed compact subset of M disjoint from I₀ ∪ ℐ⁺ ∪ ι⁺ ∪ K⁺; [[eq:iii-b-5-3]] concerns the former,
the statement on the latter being smoothness only. Such w ≠ 0 exist: with the strict nesting above, the first set has a
neighbourhood margin around supp(χ_IVP(1 − χ_K)) near I₀ ∪ ℐ⁺ ∪ ι⁺, M is compact, and as V(S_w) is linear in w its
time-[0, 1] flow converges uniformly to the identity as w → 0; so the hypothesis holds for |w| < w₀. Let c := |w|, so
that

    c² = (2/π²)‖S_w‖²_(L²(𝕊³)),     a(ω) := (cosh(c/2) + (S_w(ω)/c) sinh(c/2))⁻¹,     h_(S_w) := m(a⁴ − 1) ∈ C^∞(𝕊³).
                                                                                                         {#eq:iii-b-5-2}

((S_w/c) sinh(c/2) = S_w sinh(c/2)/c and cosh(c/2) are smooth in w, so h_(S_w) is smooth in w and vanishes at w = 0.)
Then for b = (m, A) ∈ ℬ,

    χ_IVP(1 − χ_K)(φ_(S_w)*g_b − (g_b + |x|⁻²h_(S_w)(dx¹)²)) ∈ ρ₀²ρ_I³ρ_+² C^∞(M; S²T*).                  {#eq:iii-b-5-3}

[Hin26, (3.43)–(3.44)] have r⁻¹, 2m(a³ − 1), 3/(4π) and the remainder class ρ₀ρ_I²ρ_+.

*Proof.* By symmetry ∫_(𝕊³) ω_i ω_j = δ_ij |𝕊³|/4, and |𝕊³| = 2π², so
‖S_w‖²_(L²(𝕊³)) = c² ∫_(𝕊³)(ŵ · ω)² = c²|𝕊³|/4 = π²c²/2. On the set in question the flow of V(S_w) = ½X_w for time 1
is the boost Λ of rapidity β := c/2 in the direction ŵ; so φ_(S_w)* = Λ* there. As Λ*ḡ = ḡ,

    Λ*g_b − g_b = Λ*(g_b − g_m) − (g_b − g_m) + Λ*(g_m − ḡ) − (g_m − ḡ).

By [[lem:iii-b-5-1]], φ_(S_w)*, which equals Λ* there, maps |x|⁻³C^∞(M; S²T*) into itself, and the first two terms lie
in |x|⁻³C^∞ ⊂ ρ₀³ρ_I³ρ_+³C^∞. For the last two, g_m − ḡ = m|x|⁻²(dt₀)² on {|x| ≥ 3R₁} ([[prop:iii-b-3-6]]),
t₀ = x¹. Write t = |x|(1 + v), x = |x|ω. By homogeneity, t′ := t ∘ Λ = |x|L(v, ω) and |x′| := |x ∘ Λ| = |x|G(v, ω),
with L, G smooth for bounded v, G > 0 on the region, and L(0, ω) = G(0, ω) = a(ω)⁻¹: at v = 0, with cos ϑ := ω · ŵ =
S_w/c, t′ = |x|(cosh β + cos ϑ sinh β), and
|x′|² = |x|²((cos ϑ cosh β + sinh β)² + sin²ϑ) = |x|²(cosh β + cos ϑ sinh β)², the difference of the two right sides
being |x|²(cos²ϑ(cosh²β − sinh²β) + sin²ϑ − 1) = 0. As Λ preserves t² − |x|²,

    t₀′ := t′ − |x′| = (t² − |x|²)/(t′ + |x′|) = |x|K_Λ(v, ω),     K_Λ := v(2 + v)/(L + G) = a(ω)v(1 + O(v)),

with L + G > 0 on the region (no point of it is mapped to the past light cone of the origin by a small boost). Using
|x| dv = dt₀ − v d|x|,

    dt₀′ = K_Λ d|x| + |x|(∂_v K_Λ dv + ∂_ω K_Λ dω) = ∂_v K_Λ dt₀ + (K_Λ − v∂_v K_Λ) d|x| + ∂_ω K_Λ · |x|dω,

with ∂_v K_Λ = a + O(v), K_Λ − v∂_v K_Λ = O(v²), ∂_ω K_Λ = O(v), and d|x|, |x|dω smooth sections of T*. So
dt₀′ = a dt₀ + vΞ with Ξ ∈ C^∞(M; T*), and |x′|⁻² = |x|⁻²G⁻² = |x|⁻²(a² + O(v)). Hence

    Λ*(m|x|⁻²(dt₀)²) − m|x|⁻²(dt₀)² = m|x|⁻²(a⁴ − 1)(dt₀)² + m|x|⁻²v C^∞(M; S²T*).

On the region v is bounded (as 1 − χ_K vanishes near K⁺), and v ∈ ρ_I C^∞ near ℐ⁺: v = ρ_I(1 − 2ρ_+) near ℐ⁺ ∩ ι⁺,
v = −ρ_I(1 − 2ρ₀) near I₀ ∩ ℐ⁺, v = t₀ρ_I in the interior of ℐ⁺; and |x|⁻² ∈ ρ₀²ρ_I²ρ_+²C^∞. So the last term lies in
ρ₀²ρ_I³ρ_+²C^∞, which is [[eq:iii-b-5-3]] (away from ℐ⁺, ρ_I is bounded below and |x|⁻²C^∞ ⊂ ρ₀²ρ_+²C^∞). ∎

### The gauge-fixed Einstein equation {#sec:iii-b-6}

This section is [Hin26, Section 4] in spacetime dimension 5. Throughout, G_g h := h − ½g tr_g h, δ_g is the divergence
((δ_g h)_μ = −∇^κ h_κμ), δ*_g the symmetrised covariant derivative, and ι_V h := h(V, ·).

**Definition {#def:iii-b-6-1}** ([Hin26, Definitions 4.1–4.2] in spacetime dimension 5.) Let c_Υ be a stationary 1-form
in |x|⁻¹C^∞ with c_Υ = |x|⁻¹dt for large |x|, c_(Υ,H) a stationary 1-form in C_c^∞({|x| < 5R₁}), c_C a stationary
1-form in |x|⁻¹C^∞ with c_C = |x|⁻¹(dt − v_C d|x|) for large |x|, v_C ∈ (0, 1), all three smooth on
{|x| ≥ ½r_♭} ∪ ∂X̄ (the domain of [[lem:s11-ks-domain]]), and e_Υ, γ_Υ, γ_(Υ,H), e_C, γ_C ∈ ℝ. For a metric g₀,

    E^Υ_(g₀,∞)h := −γ_Υ(2ι_(g₀⁻¹c_Υ)h − (2/3)(1 − e_Υ) c_Υ tr_(g₀)h),
    E^Υ_(g₀,H)h := γ_(Υ,H)(2ι_(g₀⁻¹c_(Υ,H))h − (2/3) c_(Υ,H) tr_(g₀)h),                                   {#eq:iii-b-6-1}

E^Υ_(g₀) := E^Υ_(g₀,∞) + E^Υ_(g₀,H), δ_(g₀,E_Υ) := δ_(g₀) + E^Υ_(g₀);

    E^C_(g₀)ω := γ_C(2c_C ⊗_s ω − (2/3)(1 − e_C) g₀ ι_(g₀⁻¹c_C)ω),     δ*_(g₀,E_C) := δ*_(g₀) + E^C_(g₀);
                                                                                                          {#eq:iii-b-6-2}

    Υ⁰(g, g₀)_μ := g_μκ g^ατ (Γ(g)^κ_ατ − Γ(g₀)^κ_ατ),     Υ^(E_Υ)(g, g₀) := Υ⁰(g, g₀) − E^Υ_(g₀)G_(g₀)(g − g₀),
                                                                                                          {#eq:iii-b-6-3}

    P(g, g₀) := Ric(g) − δ*_(g₀,E_C)Υ^(E_Υ)(g, g₀),     □^Υ_(g,E_Υ) := 2δ_(g,E_Υ)G_g δ*_g,
    □^C_(g,E_C) := 2δ_g G_g δ*_(g,E_C),                                                                  {#eq:iii-b-6-4}

and L_(g,g₀) := D_((g,g₀))P(·, 0), L_g := L_(g,g).

Υ⁰(g, g₀) = g g₀⁻¹ δ_g G_g g₀ ([Hin26, (4.3)–(4.4)]): (δ_g G_g g₀)^κ = −∇^α(g₀)_α^κ + ½∇^κ tr_g g₀, and in g-normal
coordinates at a point, where ∇ = ∂, both g^ατ(Γ(g)^κ_ατ − Γ(g₀)^κ_ατ) and (g₀⁻¹δ_g G_g g₀)^κ equal
(g₀⁻¹)^κπ(−g^ατ ∂_α(g₀)_τπ + ½g^ατ ∂_π(g₀)_ατ). This is the wave map gauge identity, valid in every dimension.

**Lemma {#lem:iii-b-6-2}** (The trace weight.) In spacetime dimension 5: tr_g G_g h = −(3/2) tr_g h; G_g is
invertible, G_g⁻¹h = h − (1/3)g tr_g h; and

    E^Υ_(g₀,∞)G_(g₀)h = −γ_Υ(2ι_(g₀⁻¹c_Υ)h − e_Υ c_Υ tr_(g₀)h),     E^Υ_(g₀,H)G_(g₀)h = 2γ_(Υ,H) ι_(g₀⁻¹c_(Υ,H))h,
    G_(g₀)E^C_(g₀)ω = γ_C(2c_C ⊗_s ω − e_C g₀ ι_(g₀⁻¹c_C)ω).                                              {#eq:iii-b-6-5}

These are the expressions that [Hin26, (4.1), (4.2) and (4.7)] give in spacetime dimension 4 with the trace weight 1.

*Proof.* tr_g g = 5, so tr_g G_g h = tr_g h − (5/2) tr_g h; and
(I − (1/3)g tr)(I − ½g tr) = I − (½ + 1/3 − 5/6)g tr = I. With ι_c G_g h = ι_c h − ½c tr h (c standing for the vector
g₀⁻¹c and the covector c): 2ι_c G_g h − (2/3)(1 − e)c tr G_g h = 2ι_c h − c tr h + (1 − e)c tr h = 2ι_c h − e c tr h,
which gives the first identity; the second, where (2/3) stands in place of (2/3)(1 − e), is the same calculation with
e = 0 in that place: 2ι_c h − c tr h + c tr h = 2ι_c h. For E^C: tr_(g₀)E^Cω = γ_C⟨c, ω⟩(2 − (10/3)(1 − e_C)), so
G_(g₀)E^Cω = γ_C(2c ⊗_s ω − g₀⟨c, ω⟩((2/3)(1 − e_C) + 1 − (5/3)(1 − e_C))) = γ_C(2c ⊗_s ω − e_C g₀⟨c, ω⟩). In spacetime
dimension 4 with weight 1, tr G = −tr, and the same lines give the same right sides. ∎

The operators that enter the following chapters, □^Υ = 2δ_g G_g δ*_g + 2E^Υ G_g δ*_g and
□^C = 2δ_g G_g δ*_g + 2δ_g G_g E^C, contain E^Υ and E^C only through E^Υ G and G E^C; so [[eq:iii-b-6-5]] is why the
weight is 2/(5 − 2): the modifications act as in spacetime dimension 4, and their parameters e, γ keep their roles.

**Lemma {#lem:iii-b-6-3}** ([Hin26, Lemma 4.4] in spacetime dimension 5.) With C(g, g₀)^τ_μκ := Γ(g)^τ_μκ −
Γ(g₀)^τ_μκ, C_(g,g₀)(ġ)^κ := g^κτ C(g, g₀)_τμα ġ^μα and Y_(g,g₀)(ġ)^κ := Υ⁰(g, g₀)^τ ġ^κ_τ (indices moved with g):

    D¹|_((g,g₀))Υ⁰ = −δ_g G_g − C_(g,g₀) + Y_(g,g₀),
    D¹|_((g,g₀))Υ^(E_Υ) = −δ_g G_g − C_(g,g₀) + Y_(g,g₀) − E^Υ_(g₀)G_(g₀);                                {#eq:iii-b-6-6}

    D_g Ric = ½□_g − δ*_g δ_g G_g + R_g,     (□_g ġ)_μκ := −g^ατ ġ_(μκ;ατ),                               {#eq:iii-b-6-7}

with R_g the zeroth order term of [Hin26, (4.12)], (R_g ġ)_τκ = Riem(g)^ρ_τκ^α ġ_ρα + ½(Ric(g)^ρ_κ ġ_τρ +
Ric(g)^ρ_τ ġ_κρ) in the curvature convention of [Hin26]; and

    L_(g,g₀) = ½□_g + E^C_(g₀)δ_g G_g + (δ*_(g₀) − δ*_g)δ_g G_g + R_g
               + δ*_(g₀,E_C)(C_(g,g₀) − Y_(g,g₀) + E^Υ_(g₀)G_(g₀)),
    L_g = D_g Ric + δ*_(g,E_C)δ_(g,E_Υ)G_g.                                                               {#eq:iii-b-6-8}

*Proof.* The proof of [Hin26, p. 83] is an index calculation in which the dimension does not appear; we give it.
[[eq:iii-b-6-6]]: from [[eq:iii-b-6-3]],
D¹Υ⁰(ġ)^μ = ġ^μκ Υ⁰_κ − g^μκ ġ^ατ C_κατ + ½g^μκ g^ατ(ġ_ακ;τ + ġ_τκ;α − ġ_ατ;κ), using
DΓ(ġ)^κ_ατ = ½(ġ^κ_α;τ + ġ^κ_τ;α − ġ_ατ^;κ) and Dg^ατ = −ġ^ατ; the first term is Y, the second −C, and the third is
ġ^μκ_;κ − ½∇^μ tr ġ = −(δ_g G_g ġ)^μ, the coefficient ½ being that of G_g, the same in every dimension. The last term of
[[eq:iii-b-6-3]] is linear in g − g₀ with g₀ fixed, with linearisation −E^Υ_(g₀)G_(g₀). [[eq:iii-b-6-7]]:
DRiem(ġ)^κ_τμα = (DΓ(ġ)^κ_τα)_;μ − (DΓ(ġ)^κ_τμ)_;α; contracting,
2DRic(ġ)_τα = (ġ_τ^κ_;ακ − ġ_τ^κ_;κα) − ġ_τα;κ^κ + ġ_α^κ_;τκ − ġ^κ_κ;τα + ġ_τκ^;κ_α. The commutator term is a curvature
term ([Hin26, (4.14)]); the second term is (□_g ġ)_τα; and −2δ*_g δ_g G_g ġ differs from the remaining terms by another
commutator, a curvature term; the two curvature terms sum to 2R_g ġ. Each step is the Ricci identity, valid in every
dimension. [[eq:iii-b-6-8]]: L_(g,g₀) = D_g Ric − δ*_(g₀,E_C)D¹Υ^(E_Υ), and substituting
[[eq:iii-b-6-6]]–[[eq:iii-b-6-7]] and δ*_(g₀,E_C) − δ*_g = (δ*_(g₀) − δ*_g) + E^C_(g₀) gives the first formula; at g₀ =
g, C_(g,g) = 0 = Y_(g,g), and the second follows. ∎

*Remarks on [Hin26, Sections 3–4].* The Boyer–Lindquist apparatus of [Hin26, Section 3.2] ((3.9)–(3.18), (3.22),
(3.25)–(3.26)) is not needed here: Kerr–Schild coordinates and the time change [[eq:iii-b-3-3]] replace it, which five
dimensions allow and four do not ([[lem:iii-b-3-5]]). Where [Hin26] constructs T̃ with T̃ = C′ − Cr⁻¹ by an estimate,
[[eq:iii-b-3-6]] gives it explicitly with C = 8m₀. The proof of [[lem:iii-b-5-2]] uses the exact boost and homogeneity
in place of the expansion [Hin26, (3.45)–(3.49)] of the cut-off flow; in dimension 4 + 1 the expansion has no O(ρ)
terms, the coordinate t₀ = t − |x| of the compactification being the Minkowski retarded time. The cut-offs of
[[sec:iii-b-5]] differ from those of [Hin26, Definition 3.17] in two respects, neither of which changes anything near
I₀ ∪ ℐ⁺ ∪ ι⁺ ∪ K⁺. [Hin26, Definition 3.17] asks χ^♭_K to be supported in {t > 50𝔪} and equal to 1 on {r < t/10}, and
on {𝔪 ≤ r < t/10, 10𝔪 < t ≤ 50𝔪}, which meets the spacetime, the two conditions conflict; here χ^♭_K = 1 is asked only
on {|x| < t/10, t > 60R₁}. And [Hin26, Lemma 3.18] asserts that the lift of V(S) vanishes for r ≤ 5𝔪, which with the
cut-offs of [Hin26, Definition 3.17] needs χ^♯_IVP(1 − χ^♭_K) = 0 on {r ≤ 5𝔪}, which fails at t ≤ 50𝔪 where χ^♭_K = 0
and t_IVP > −r/2; here the radial factor χ_r gives it.

### Manifolds with corners, blow-ups and b-analysis {#sec:iii-a-1}

We use the following notions of [Hin26, pp. 44–48]: manifolds with corners M of any dimension, boundary hypersurfaces
H (embedded, with defining functions ρ_H and collar neighbourhoods [0, ε)_(ρ_H) × H), local defining functions, the
radial compactification ℝ̄^d, and real blow-ups of boundary faces and of boundary submanifolds ([Hin26, Notation 2.1,
Examples 2.2–2.3]; [Mel96]). None of the definitions below mentions the dimension except as the generic dimension n of
the model [0, ∞)^k × ℝ^(n−k).

**Definition {#def:s11-b-analysis}** (b-analysis and partial polyhomogeneity; [Hin26, Definitions 2.4–2.8 and Notation
2.9].) Let M be a manifold with corners.

(1) (b-vector fields, b-operators, b-densities.) 𝒱_b(M) consists of the smooth vector fields on M tangent to ∂M;
Diff^m_b(M) of the locally finite sums of up to m-fold compositions of elements of 𝒱_b(M), 0-fold compositions being
multiplication by elements of C^∞(M); a b-density μ is a smooth positive density on M° such that (Π_H ρ_H)μ is a smooth
positive density on M. In local coordinates x^j ∈ [0, ∞), j ≤ k, and y^l ∈ ℝ, b-vector fields are the smooth
combinations of x^j∂_(x^j) and ∂_(y^l), and b-densities are a dx¹/x¹ ⋯ dx^k/x^k dy¹ ⋯ dy^(n−k), a > 0 smooth.

(2) (Normal operators, indicial roots.) On a manifold with boundary with a collar [0, ε)_ρ × ∂M, A ∈ Diff^m_b(M) is
A = Σ_(j≤m) A_j(ρ)(ρ∂_ρ)^j, A_j ∈ C^∞([0, ε); Diff^(m−j)(∂M)). The b-normal operator and the indicial family are
N(A) := Σ_j A_j(0)(ρ∂_ρ)^j on [0, ∞)_ρ × ∂M and N(A, ι) := Σ_j A_j(0)ι^j ∈ Diff^m(∂M), ι ∈ ℂ. ι is an *indicial root*
if N(A, ι)u = 0 for some 0 ≠ u ∈ C^∞(∂M), equivalently N(A)(ρ^ι u) = 0 (an *indicial solution*); the *boundary
spectrum* spec_b(A) is the set of indicial roots; ι is *simple* if there are no indicial solution u and u′ ∈ C^∞(∂M)
with N(A)(ρ^ι(log ρ)u + ρ^ι u′) = 0. For A ∈ ρ^α Diff^m_b(M), N(A) := ρ^α N(ρ^(−α)A), and its indicial roots are those
of ρ^(−α)A. A is *elliptic* near ∂M if, writing A = Σ_(j+|β|≤m) a_jβ(ρ, y)(ρ∂_ρ)^j ∂_y^β, the polynomial
Σ_(j+|β|=m) a_jβ(ρ, y)ξ^j η^β has no real zeros (ξ, η) ≠ (0, 0).

(3) (Weighted spaces.) Let M be compact with boundary hypersurfaces H_1, …, H_p and defining functions ρ_1, …, ρ_p, and
for α⃗ ∈ ℝ^p let ρ⃗^(α⃗) := Π_j ρ_j^(α_j). 𝒜^(α⃗)(M) is the space of smooth u on M° such that ρ⃗^(−α⃗)Au is bounded for
every A ∈ Diff_b(M). For a b-density μ and k ∈ ℕ₀, H^(k,α⃗)_b(M) is the space of u ∈ L²_loc(M°) with
ρ⃗^(−α⃗)Au ∈ L²(M, μ) for all A ∈ Diff^k_b(M), normed by Σ_(A∈𝒜_k) ‖ρ⃗^(−α⃗)Au‖_(L²(M,μ)) for a finite spanning set 𝒜_k
of Diff^k_b(M); different choices give equivalent norms. On M = [0, ∞)^k_x × ℝ^(n−k)_y × S, S closed, the same spaces
are defined with μ = |dx¹/x¹ ⋯ dx^k/x^k dy¹ ⋯ dy^(n−k)| ⊗ μ_S and the testing operators the compositions of x^j∂_(x^j),
∂_(y^l) and vector fields on S.

(4) (Index sets.) An *index set* is a subset E ⊂ ℂ × ℕ₀ with

    (z, k) ∈ E ⟹ (z + j, k) ∈ E for all j ∈ ℕ₀, and (z, j) ∈ E for all j ≤ k,                         {#eq:s11-index-set}

and with only finitely many (z, k) ∈ E with Re z ≤ C, for every C ∈ ℝ. We write min Re E := inf{Re z : (z, 0) ∈ E}
(min Re ∅ := ∞); π₁ : ℂ × ℕ₀ → ℂ for the projection and Re π₁E := {Re z : z ∈ π₁E}; k(E, z) := max{k : (z, k) ∈ E} if
z ∈ π₁E and k(E, z) := −1 otherwise; E + F := {(z + w, k + l) : (z, k) ∈ E, (w, l) ∈ F} and
E + q := {(z + q, k) : (z, k) ∈ E}; the *extended union* E ∪̄ F := E ∪ F ∪ {(z, k + l + 1) : (z, k) ∈ E, (z, l) ∈ F};
for z ∈ ℂ and k ∈ ℕ₀, E ∪̄ {(z, k)} := the smallest index set G ⊃ E with k(G, z) = k(E, z) + k + 1; and (z, k) also
denotes the index set {(z + j, l) : j ∈ ℕ₀, 0 ≤ l ≤ k}, the smallest one containing the pair (z, k).

(5) (Partial polyhomogeneity.) Let M be compact, and for each boundary hypersurface H let E_H be an index set and
α_H ∈ ℝ; let ℋ(H) be the set of boundary hypersurfaces H′ ≠ H with H ∩ H′ ≠ ∅. If min Re E_H > α_H for all H, put
H^(k,(E⃗,α⃗))_b(M) := H^(k,α⃗)_b(M) and 𝒜^((E⃗,α⃗))(M) := 𝒜^(α⃗)(M). Otherwise, by induction on the number of H with
min Re E_H ≤ α_H, H^(k,(E⃗,α⃗))_b(M) is the space of u such that for every H with min Re E_H ≤ α_H there are
u^((z,ℓ)) ∈ H^(k,(E⃗(H),α⃗(H)))_b(H), (E⃗(H), α⃗(H)) := (E_(H′), α_(H′))_(H′∈ℋ(H)), with, in a collar
[0, ε)_(ρ_H) × H and for χ ∈ C_c^∞([0, ε)) equal to 1 on [0, ε/2],

    u − χ(ρ_H) Σ_((z,ℓ)∈E_H, Re z≤α_H) ρ_H^z (log ρ_H)^ℓ u^((z,ℓ)) ∈ H^(k,(E⃗′,α⃗))_b(M),               {#eq:s11-partial}

where E′_H := ∅ and E′_(H′) := E_(H′) for H′ ≠ H. 𝒜^((E⃗,α⃗))(M) is defined in the same way. Another defining function
ρ′_H = a⁻¹ρ_H, a > 0 smooth, gives the same space: ρ_H^z = a^z(ρ′_H)^z and log ρ_H = log ρ′_H + log a, with a and log a
Taylor expanded at ρ′_H = 0, turn [[eq:s11-partial]] into the analogous expansion in ρ′_H, by [[eq:s11-index-set]].

(6) (Notation.) With the boundary hypersurfaces ordered, H^(k,(E⃗,α⃗))_b(M) is written H^(k,(E_1,α_1),…,(E_p,α_p))_b(M);
(∅, α) is written α; and H^(k,E_1,(E_2,α_2))_b(M) := ⋂_(α_1∈ℝ) H^(k,(E_1,α_1),(E_2,α_2))_b(M), with the obvious variants
and the same for 𝒜-spaces. 𝒜^(E⃗)(M) is the space of polyhomogeneous functions, and on a manifold with boundary
H^(∞,(E,α))_b(M) = 𝒜^E(M) + H^(∞,α)_b(M).

Two facts used throughout are immediate from the definitions. (F1) A b-vector field V maps H^(k,(E⃗,α⃗))_b(M) to
H^(k−1,(E⃗,α⃗))_b(M): in a collar of H, V = aρ_H∂_(ρ_H) + W with W tangent to the slices, and
V(ρ_H^z(log ρ_H)^ℓ u) = ρ_H^z(log ρ_H)^ℓ(az + W)u + ℓa ρ_H^z(log ρ_H)^(ℓ−1)u for u independent of ρ_H in the collar (as
expansion coefficients are), and a and W, which depend on ρ_H, are re-expanded in their Taylor series at ρ_H = 0, adding
terms at z + 1 + ℕ₀ with the same powers of log ρ_H, which [[eq:s11-index-set]] allows. (F2) Two memberships of the
same function in spaces with the same data at a face H and different data elsewhere combine by a partition of unity
subordinate to neighbourhoods of the faces, as in the proof of [[prop:ii-g1-3-3]].

A b-vector field V is *b-normal at H* if V − χ(ρ_H)ρ_H∂_(ρ_H) ∈ ρ_H𝒱_b(M) for a collar [0, ε)_(ρ_H) × H and
χ ∈ C_c^∞([0, ε)) equal to 1 near 0. The notion does not depend on the collar: if ρ′_H = aρ_H with a > 0 smooth and
(ρ_H, y) ↦ (ρ′_H, y′) is the change of collar, then ρ_H∂_(ρ_H) applied to ρ′_H gives ρ′_H(1 + ρ_H∂_(ρ_H) log a) and
applied to y′ gives ρ_H∂_(ρ_H)y′, which vanishes at ρ_H = 0 since y′ = y there; so
ρ_H∂_(ρ_H) − ρ′_H∂_(ρ′_H) ∈ ρ_H𝒱_b ([Hin26, p. 49]).

**Lemma {#lem:iii-a-1-1}** ([Hin26, Lemma 2.10], normal form.) Let V be b-normal at the compact boundary hypersurface
H. There are a defining function ρ_H and an adapted collar [0, ε)_(ρ_H) × H in which V = ρ_H∂_(ρ_H).

*Proof.* In a collar [0, ε′)_x × H, V = x∂_x + x(a(x, y)x∂_x + V_∂(x)) with a smooth and V_∂(x) a smooth family of
b-vector fields on H; so x⁻¹V = (1 + ax)∂_x + V_∂(x) is smooth, tangent to the boundary hypersurfaces
[0, ε′) × ∂_jH (as V_∂(x) is tangent to ∂H) and transversal to H. Its flow Φ(s, y) := e^(sx⁻¹V)(0, y) is defined for
small s ≥ 0 (tangency keeps it inside M), and Φ is a diffeomorphism from [0, ε″)_s × H onto a neighbourhood of H, as
Φ(0, y) = (0, y) and ∂_sΦ is transversal to H there. In these coordinates x⁻¹V = ∂_s, so V = x∂_s = (x/s)s∂_s, and
x/s = 1 + sb(s, y) with b smooth, as x = s + O(s²) (∂_s x = 1 + ax = 1 at s = 0). Put ρ_H := s(1 + c(s, y)) with c
smooth and c(0, y) = 0; then s∂_s = s(1 + c + s∂_s c)∂_(ρ_H) at fixed y, so
V = ((1 + sb)(1 + c + s∂_s c)/(1 + c))ρ_H∂_(ρ_H), which is ρ_H∂_(ρ_H) if and only if ∂_s c = −b(1 + c)/(1 + sb), an
ordinary differential equation in s with y as a parameter, solvable with c(0, y) = 0 for small s. Then
(s, y) ↦ (ρ_H, y) is a diffeomorphism near s = 0, giving the collar. ∎

**Lemma {#lem:iii-a-1-2}** ([Hin26, Lemma 2.12], a Fuchsian ordinary differential equation.) On [0, 1)_x × H, H a
compact manifold with corners, with b-Sobolev spaces defined by x∂_x and |dx/x| in the first factor, let
χ ∈ C_c^∞([0, ¾)) equal 1 on [0, ½], z ∈ ℂ, α ≠ Re z. If (x∂_x − z)u = f ∈ H^(k,(E,α),(F⃗,β⃗))_b and
(1 − χ(x))u ∈ H^(k,∞,(F⃗,β⃗))_b, where (E, α) refers to {0} × H and (F⃗, β⃗) to [0, 1) times the boundary hypersurfaces
of H, then u ∈ H^(k,(E ∪̄ {(z,0)},α),(F⃗,β⃗))_b.

*Proof.* x∂_x(x^(−z)u) = x^(−z)f, and multiplication by x^(−z) shifts (E, α) to (E − z, α − Re z) and commutes with
everything else; so let z = 0, α ≠ 0. By

    x∂_x(x^w(log x)^ℓ v(y)) = w x^w(log x)^ℓ v(y) + ℓ x^w(log x)^(ℓ−1) v(y)                               {#eq:iii-a-1-1}

a term χ(x)x^w(log x)^ℓ v of f with w ≠ 0 is the image of χ(x)w⁻¹x^w(log x)^ℓ v up to a term with one log fewer and a
term w⁻¹x^w(log x)^ℓ v x∂_xχ supported in x ∈ [½, ¾]; descending in ℓ and ascending in Re w removes all terms of f with
(w, ℓ) ∈ E, w ≠ 0, Re w ≤ α, from the equation, the subtracted terms lying in H^(k,(E,α),(F⃗,β⃗)). A term
χ(x)Σ_(j≤ℓ)(log x)^j v_j (the exponent w = 0, present only if 0 ∈ π₁E with Re 0 ≤ α) is the image of
χ(x)Σ_j (j + 1)⁻¹(log x)^(j+1) v_j up to a term supported in [½, ¾]; this raises the log power at 0 by one, which is
E ∪̄ {(0, 0)}. It remains to treat f ∈ H^(k,α,(F⃗,β⃗)) (E = ∅). Subtracting ψ(x)u, ψ ∈ C_c^∞((¾, 1]) equal to 1 near 1,
which lies in H^(k,∞,(F⃗,β⃗)) by hypothesis, we may assume u = f = 0 near x = 1. The operator x∂_x commutes with x∂_x and
with b-derivatives on H, so the case k = 0 applied to derivatives gives every k. The solution operators below act in x
alone, commute with multiplication by functions of y and with ρ^w(log ρ)^j for defining functions ρ of the faces of H,
and are bounded on x^α L²(|dx/x|; 𝓗) for any Hilbert space 𝓗; applied to the terms and the remainders of the
expansions [[eq:s11-partial]] at the faces [0, 1) × ∂_jH (inductively on the number of faces), they preserve (F⃗, β⃗).
So we drop y. If α < 0: u(x) = −∫_x^1 f(s) ds/s, and by Cauchy–Schwarz with ∫_x^1 s^α ds/s ≤ |α|⁻¹x^α and
∫_0^s x^(−α) dx/x = |α|⁻¹s^(−α),

    ∫_0^1 x^(−2α)|u|² dx/x ≤ |α|⁻¹ ∫_0^1 x^(−α) ∫_x^1 s^(−α)|f(s)|² (ds/s) (dx/x) ≤ |α|⁻² ∫_0^1 s^(−2α)|f(s)|² ds/s.

If α > 0: u(0) := −∫_0^1 f ds/s converges absolutely (|u(0)|² ≤ (2α)⁻¹ ∫ s^(−2α)|f|² ds/s), u(x) − u(0) = ∫_0^x f ds/s,
and with ∫_0^x s^α ds/s = α⁻¹x^α, ∫_s^1 x^(−α) dx/x ≤ α⁻¹s^(−α),

    ∫_0^1 x^(−2α)|u(x) − u(0)|² dx/x ≤ α⁻¹ ∫_0^1 x^(−α) ∫_0^x s^(−α)|f|² (ds/s) (dx/x)
                                     ≤ α⁻² ∫_0^1 s^(−2α)|f(s)|² ds/s;                                    {#eq:iii-a-1-2}

the constant u(0) is the term (0, 0) of E ∪̄ {(0, 0)} (here E = ∅). ∎

**Lemma {#lem:iii-a-1-3}** ([Hin26, Lemma 2.11], testing for partial polyhomogeneity.) In the notation of
[[def:s11-b-analysis]] (5), let H be a boundary hypersurface with α_H ∉ Re π₁E_H, V b-normal at H,
E_(H,≤) := {(z, ℓ) ∈ E_H : Re z ≤ α_H} (a finite set), and E⃗′ as in [[eq:s11-partial]]. If
(1 − χ(ρ_H))u ∈ H^(k,(E⃗′,α⃗))_b(M) and

    (Π_((z,ℓ)∈E_(H,≤)) (V − z)) u ∈ H^(k,(E⃗′,α⃗))_b(M),                                                  {#eq:iii-a-1-3}

then u ∈ H^(k,(E⃗,α⃗))_b(M). Conversely, u ∈ H^(k,(E⃗,α⃗))_b implies [[eq:iii-a-1-3]] with k − |E_(H,≤)| in place of k.

*Proof.* By [[lem:iii-a-1-1]] take a collar with V = ρ_H∂_(ρ_H) near H (the defining function changes by a smooth
positive factor, which by [[def:s11-b-analysis]] (5) does not change the spaces). Conversely: by [[eq:iii-a-1-1]] the
product annihilates Σ_((z,ℓ)∈E_(H,≤)) ρ_H^z(log ρ_H)^ℓ u^((z,ℓ)), the factor V − z being taken once for each (z, ℓ),
ℓ ≤ k(E_H, z), so k(E_H, z) + 1 times; derivatives falling on the cut-off are supported away from H; and each factor
costs one derivative (F1). Directly: order the factors as (z_1, ℓ_1), …, (z_p, ℓ_p) with Re z_1 ≥ ⋯ ≥ Re z_p and put
w_i := Π_(j>i)(V − z_j)u, so that w_0 is the left side of [[eq:iii-a-1-3]], w_p = u and (V − z_i)w_i = w_(i−1). Apply
[[lem:iii-a-1-2]] for i = 1, …, p, peeling the outermost factor first (its hypothesis α_H ≠ Re z_i is ours): by
[[def:s11-b-analysis]] (4) it raises the logarithmic order at z_i by one and completes by [[eq:s11-index-set]], which
adds pairs only at z_i + j, j ≥ 1. In this order those points have real part above that of every later factor, so no
later raise meets a completion; the count at each z ∈ π₁E_(H,≤) starts at −1 (the index set of w_0 at H, that of E⃗′,
being empty) and is raised k(E_H, z) + 1 times, to k(E_H, z), while completions reaching z from z − j carry at most
k(E_H, z − j) ≤ k(E_H, z). So the index set of u at H is E_(H,≤) completed by [[eq:s11-index-set]], contained in E_H,
and the expansion terms with Re z > α_H are absorbed in the remainder. (In another order a raise can meet a completion:
for V(V − 1) with V peeled first, the completion (1, 0) of (0, 0) is then raised to (1, 1).) The a priori hypothesis of
[[lem:iii-a-1-2]] holds for each w_i by (F1), but only at the order k − (p − i), so this gives the index set with u of
order k − p + 1. For the order k: the solution operators of [[lem:iii-a-1-2]] act in ρ_H alone, commute with
derivatives along H and preserve H^k, so their composition applied to the left side of [[eq:iii-a-1-3]] gives u_p of
order k with the same index set; u − u_p is annihilated by the product near H, so it is Σ ρ_H^z(log ρ_H)^ℓ c_(z,ℓ)
there (the solutions of the ordinary differential equation in ρ_H), and its coefficients are read off u − u_p on
{ρ_H ≥ ¾}, where both are of order k, by pairing in ρ_H against test functions, so c_(z,ℓ) ∈ H^k(H). ∎

#### Normal operator arguments {#sec:iii-a-1-1}

Let ∂M be a compact manifold without boundary, M := [0, ρ₀)_ρ × ∂M, with the b-density |dρ/ρ| ⊗ μ, μ a smooth
positive density on ∂M, and let N_E ≥ 1 be an integer. The operators of this section act on ℂ^(N_E)-valued functions.
Diff^m_b(M; ℂ^(N_E)) is the space of N_E × N_E matrices with entries in Diff^m_b(M): in the collar and in local
coordinates y on ∂M, A = Σ_(j+|β|≤m) a_jβ(ρ, y)(ρ∂_ρ)^j∂_y^β with smooth matrix-valued coefficients a_jβ, and
A = Σ_(j≤m) A_j(ρ)(ρ∂_ρ)^j with A_j ∈ C^∞([0, ρ₀); Diff^(m−j)(∂M; ℂ^(N_E))), the operators on ∂M being matrices of
differential operators in the same way. A is *elliptic* near ρ = 0 if its *principal symbol*, the matrix
Σ_(j+|β|=m) a_jβ(ρ, y)ξ^jη^β, is invertible for all real (ξ, η) ≠ (0, 0) and all (ρ, y) with ρ near 0; for N_E = 1
this is the ellipticity of [[def:s11-b-analysis]] (2). The normal operator, the indicial family, the indicial roots and
the boundary spectrum are defined as in [[def:s11-b-analysis]] (2), with ℂ^(N_E)-valued u and u′. A ℂ^(N_E)-valued
function lies in one of the spaces of [[def:s11-b-analysis]] (3), (5) and (6), or in H^k(∂M) below, when each of its
components does, and these spaces are written as those of functions: H^k(∂M) stands for H^k(∂M; ℂ^(N_E)), and so on.
A b-differential operator on the sections of a vector bundle of rank N_E over M with a frame smooth up to ρ = 0 is,
written in that frame, an element of Diff^m_b(M; ℂ^(N_E)); the bundles of the later chapters are trivialised in this
way ([[sec:i-a-1-2]]).

Fix smooth vector fields X₁, …, X_q on ∂M spanning T∂M at every point. For an integer k ≥ 0, H^k(∂M) is normed by
‖u‖_(H^k) := Σ ‖X_(i₁)⋯X_(i_l)u‖_(L²(∂M,μ)), the sum over l ≤ k and all indices, the fields acting on each component
and ‖u‖²_(L²(∂M,μ)) := ∫ |u|² μ with |·| the Euclidean norm of ℂ^(N_E); this is the usual Sobolev norm up to
equivalence ([Hin26d, Definition 3.14 and Remark 3.15, pp. 34–35], for each component), and
‖u‖_(H^k) = ‖u‖_(L²) + Σ_i ‖X_iu‖_(H^(k−1)) for k ≥ 1. For A ∈ Diff^m_b(M; ℂ^(N_E)) elliptic near ρ = 0,
N(A, ι) = Σ_j A_j(0)ι^j depends polynomially on ι and is elliptic on ∂M: its principal symbol, the matrix
Σ_(|β|=m) a_0β(0, y)η^β, which is that of A at ρ = 0 and ξ = 0, is invertible for η ≠ 0. We use three facts about it.

(E1) *Large-parameter ellipticity.* For every strip {c₁ ≤ Re ι ≤ c₂} and every integer s ≥ 0 there are R and C such
that N(A, ι) : H^(s+m)(∂M) → H^s(∂M) is invertible for |Im ι| ≥ R in the strip, with

    Σ_(j≤m) |ι|^(m−j)‖N(A, ι)⁻¹g‖_(H^(s+j)(∂M)) ≤ C‖g‖_(H^s(∂M)).

(E2) *Analytic Fredholm theory.* N(A, ι)⁻¹ : L²(∂M) → H^m(∂M) is meromorphic in ℂ. Let s ≥ 0 be an integer. At every
ι that is not a pole, N(A, ι)⁻¹ maps H^s(∂M) to H^(s+m)(∂M), with norm bounded uniformly on every compact set of such
ι. Every coefficient of its Laurent expansion at any point of ℂ maps H^s(∂M) to H^(s+m)(∂M), so C^∞(∂M) to C^∞(∂M);
the coefficients of the negative powers have finite rank.

(E3) *Poles and indicial roots.* Let Π be a bounded projection on L²(∂M) that maps H^s(∂M) into itself for every
integer s ≥ 0 and satisfies ΠN(A, ι)u = N(A, ι)Πu for all u ∈ H^m(∂M) and ι ∈ ℂ (Π = Id is allowed); so
ΠH^s(∂M) = {u ∈ H^s(∂M) : Πu = u}. Then N(A, ·)⁻¹Π : L²(∂M) → H^m(∂M) has a pole at ι₁ ∈ ℂ if and only if
N(A, ι₁)u = 0 for some 0 ≠ u ∈ ΠC^∞(∂M). If it has no pole at ι₁, N(A, ι₁) maps ΠH^(s+m)(∂M) bijectively onto
ΠH^s(∂M) for every integer s ≥ 0, and ΠC^∞(∂M) bijectively onto itself. In particular (Π = Id), the poles of
N(A, ·)⁻¹ are exactly the indicial roots; N(A, ι) : H^(s+m)(∂M) → H^s(∂M) and N(A, ι) : C^∞(∂M) → C^∞(∂M) are
bijective if ι ∉ spec_b(A) and not injective if ι ∈ spec_b(A); and spec_b(A) has finitely many points in every strip
{c₁ ≤ Re ι ≤ c₂}.

The three facts rest on the following results of the literature. All three use the elliptic estimate on a compact
manifold without boundary, quoted below, and the equivalence of the norms of this section with the usual Sobolev
norms, [Hin26d, Definition 3.14 and Remark 3.15]. The proof of (E2), on which that of (E3) builds, also uses the
compact inclusion H^(m+1)(∂M) ↪ H^m(∂M), [Hin26d, Theorem 3.21], and analytic Fredholm theory,
[[thm:std-analytic-fredholm]]; (E2) and (E3) also use the Sobolev embedding theorem on the compact ∂M, by which
C^∞(∂M) is the intersection of the H^s(∂M). In the following quotation the letters A, X, E, F, m, s, t, p, u and C are
the source's. [Shu92, Appendix 1, Lemma 1.4, pp. 69–70] states: "Let A be a C^∞-bounded uniformly elliptic differential
operator acting as in (1.2) between spaces of sections of vector bundles of bounded geometry. Then for every
s, t ∈ ℝ, p ∈ (1, +∞) there exists C > 0 such that (1.5) ‖u‖_(s,p) ≤ C(‖Au‖_(s−m,p) + ‖u‖_(t,p)), u ∈ C_0^∞(X, E).
Moreover if u ∈ W_p^(−∞)(X, E) and Au ∈ W_p^(s−m)(X, F) then u ∈ W_p^s(X, E)." There (p. 69) the principal symbol
a_m(x, ξ) of A is a matrix in local trivialisations, A "is called elliptic if this matrix is invertible for every
(x, ξ) with ξ ≠ 0. It is called uniformly elliptic if there exists C > 0 such that (1.4) |a_m⁻¹(x, ξ)| ≤ C|ξ|^(−m),
(x, ξ) ∈ T*X, ξ ≠ 0", with |ξ| the length in the Riemannian metric of X; W_p^(−∞)(X, E) is the union of the
W_p^s(X, E), s ∈ ℝ; and W_2^s(X, E) is the Sobolev space of order s, the completion of C_0^∞(X, E) in a norm built
from a partition of unity subordinate to coordinate balls and Sobolev norms in the coordinates, with
W_2^0(X, E) = L²(X, E) (pp. 67–69).

Let Z be a compact manifold without boundary, fix a Riemannian metric on it, and let P be a differential operator of
order m on Z with smooth coefficients, acting on ℂ^(N_E)-valued functions, whose principal symbol is invertible at every
point of T*Z ∖ o. The quotation applies to P on the trivial bundle Z × ℂ^(N_E). Z is of bounded geometry: the coverings
of compact manifolds are among the examples of [Shu92, Appendix 1, p. 64], and Z covers itself. The trivial bundle, with
its global trivialisation, has constant transition functions, so it is of bounded geometry (p. 65). In canonical
coordinates of a fixed radius r below the injectivity radius, which are defined by a point of Z and an orthonormal frame
there, the coefficients of P are smooth functions of the frame and of the point of the closed ball of radius r, and
these range over a compact set (the orthonormal frame bundle times the closed ball); so the coefficients are bounded with
all their derivatives, uniformly, and P is C^∞-bounded. The function |a_m⁻¹(x, ξ)||ξ|^m is continuous on T*Z ∖ o and
homogeneous of degree 0 in ξ, so it is bounded by its maximum on the compact set {|ξ| = 1}; this is (1.4). On the
compact Z, W_2^k, k ∈ ℕ₀, is the usual Sobolev space of ℂ^(N_E)-valued functions, so it is H^k(Z) with an equivalent
norm: the norms of this section, built from smooth fields spanning TZ, are equivalent to the usual one by
[Hin26d, Definition 3.14 and Remark 3.15], as on ∂M above. So (1.5) with s + m in
place of s, t = 0 and p = 2, extended from C^∞(Z) to H^(s+m)(Z) by density and by the continuity of both of its sides
in H^(s+m)(Z) (P maps H^(s+m)(Z) continuously to H^s(Z), p. 69), and the last sentence of the quotation give, for
every integer s ≥ 0, a constant C with

    ‖v‖_(H^(s+m)(Z)) ≤ C(‖Pv‖_(H^s(Z)) + ‖v‖_(L²(Z))),     v ∈ H^(s+m)(Z),                                (EE)

and v ∈ H^(s+m)(Z) whenever v ∈ L²(Z) and Pv ∈ H^s(Z), Pv being taken in the sense of distributions.

*Proof of (E1).* Let 𝕋 := ℝ/2πℤ and Z := 𝕋_x × ∂M, with the density |dx| ⊗ μ and the norms H^k(Z) defined as above
with the fields ∂_x, X₁, …, X_q. For c ∈ ℝ and κ ∈ [0, 1] let P_(c,κ) := Σ_j A_j(0)(∂_x + c + iκ)^j. In local
coordinates y on ∂M, with A = Σ_(j+|β|≤m) a_jβ(ρ, y)(ρ∂_ρ)^j∂_y^β, P_(c,κ) = Σ a_jβ(0, y)(∂_x + c + iκ)^j∂_y^β, whose
principal symbol at (ξ, η) is the matrix i^m Σ_(j+|β|=m) a_jβ(0, y)ξ^jη^β; it is invertible on T*Z ∖ o, by the
ellipticity of A. So (EE) holds for each P_(c,κ). It holds with one constant C₁ for all (c, κ) ∈ K := [c₁, c₂] × [0, 1]:
the difference P_(c,κ) − P_(c′,κ′) has order at most m − 1, with coefficients bounded by C_K(|c − c′| + |κ − κ′|) on K,
so ‖(P_(c,κ) − P_(c′,κ′))v‖_(H^s) ≤ C_K(|c − c′| + |κ − κ′|)‖v‖_(H^(s+m)); for (c, κ) close to (c′, κ′) this term is
absorbed, and (EE) holds there with twice the constant of (c′, κ′); finitely many such neighbourhoods cover K.

Now let u ∈ H^(s+m)(∂M), ι = c + iτ with c ∈ [c₁, c₂], n := ⌊τ⌋, κ := τ − n and v := e^(inx)u. Then
P_(c,κ)v = e^(inx)N(A, ι)u. As ∂_x commutes with the X_i, every product of at most k of the fields ∂_x, X_i applied to
v is e^(inx)(in)^l X_(i₁)⋯X_(i_p)u with l + p ≤ k; so ‖v‖_(H^k(Z)) is bounded above and below, with constants
depending only on k, by [u]_(k,τ) := Σ_(l≤k) ⟨τ⟩^l ‖u‖_(H^(k−l)(∂M)), ⟨τ⟩ := (1 + τ²)^(1/2) (the term l = 0 dominates
the others where |n| ≤ 1). So (EE) gives [u]_(s+m,τ) ≤ C₂([N(A, ι)u]_(s,τ) + ‖u‖_(L²)), and as
‖u‖_(L²) ≤ ⟨τ⟩^(−s−m)[u]_(s+m,τ),

    [u]_(s+m,τ) ≤ 2C₂[N(A, ι)u]_(s,τ)     for ⟨τ⟩^(s+m) ≥ 2C₂.                                           (E1′)

*Invertibility.* Fix R with ⟨R⟩^m ≥ 2C₂ for s = 0. By (E1′) at s = 0, N(A, ι) : H^m → L² is injective with closed
range for |Im ι| ≥ R. Its formal adjoint with respect to μ and the Euclidean inner product of ℂ^(N_E) is
Σ_j A_j(0)*ῑ^j = N(A′, ῑ) with A′ := Σ_j A_j(0)*(ρ∂_ρ)^j, which is elliptic near ρ = 0, as its principal symbol at
ρ = 0 is (−1)^m times the conjugate transpose of that of A at (−ξ, η); and Re ῑ = Re ι. So, after enlarging R,
N(A′, ῑ) is injective on H^m as well. If g ∈ L² is orthogonal to the range of N(A, ι), then N(A′, ῑ)g = 0 in the
sense of distributions; (EE) for the operator P′ built from A′ as P_(c,κ) from A, applied to e^(in′x)g with
n′ := ⌊−τ⌋, gives g ∈ H^m, so g = 0. Hence N(A, ι) : H^m → L² is bijective. For g ∈ H^s, u := N(A, ι)⁻¹g lies in H^m
and P_(c,κ)(e^(inx)u) = e^(inx)g ∈ H^s(Z), so u ∈ H^(s+m) by (EE).

*The estimate.* We show, by induction on s,

    Σ_(l≤m) ⟨τ⟩^l ‖u‖_(H^(s+m−l)) ≤ C‖N(A, ι)u‖_(H^s)     (u ∈ H^(s+m), ι = c + iτ, c ∈ [c₁, c₂], |τ| ≥ R),

which is (E1), as |ι| ≤ C⟨τ⟩ in the strip. At s = 0 it is (E1′). Let s ≥ 1 and g := N(A, ι)u. Then
N(A, ι)X_iu = X_ig + [N(A, ι), X_i]u, where [N(A, ι), X_i] = Σ_j ι^j[A_j(0), X_i] and [A_j(0), X_i] has order at
most m − j; so ‖[N(A, ι), X_i]u‖_(H^(s−1)) ≤ C Σ_(l≤m) ⟨τ⟩^l‖u‖_(H^(s−1+m−l)) ≤ C′‖g‖_(H^(s−1)), by the case s − 1.
The case s − 1 applied to X_iu ∈ H^(s−1+m) then gives Σ_l ⟨τ⟩^l‖X_iu‖_(H^(s−1+m−l)) ≤ C(‖X_ig‖_(H^(s−1)) +
C′‖g‖_(H^(s−1))) ≤ C″‖g‖_(H^s), and ‖u‖_(H^k) ≤ ‖u‖_(H^(k−1)) + Σ_i ‖X_iu‖_(H^(k−1)) at k = s + m − l gives the
case s. ∎

*Proof of (E2).* Fix ι₀ at which N(A, ι₀) is invertible, by (E1). On the Hilbert space H^m(∂M) let
B(ι) := N(A, ι₀)⁻¹(N(A, ι) − N(A, ι₀)) = Σ_(j≥1) (ι^j − ι₀^j)N(A, ι₀)⁻¹A_j(0). For j ≥ 1, A_j(0) has order at most
m − 1 and maps H^m to H^1, and N(A, ι₀)⁻¹ maps H^1 to H^(m+1) by (E1); and the inclusion H^(m+1)(∂M) ↪ H^m(∂M) is
compact ([Hin26d, Theorem 3.21, p. 38], [[thm:std-sbg-calculus]] (S3), on the compact ∂M with w = w′ = 1, for each
component). So B is an entire family of compact operators on H^m, and Id + B(ι) = N(A, ι₀)⁻¹N(A, ι) is invertible
wherever N(A, ι) is, in particular at ι₀. By [[thm:std-analytic-fredholm]], W(ι) := (Id + B(ι))⁻¹ exists off a
discrete set S and is meromorphic on ℂ; so is N(A, ι)⁻¹ = W(ι)N(A, ι₀)⁻¹ : L² → H^m, with the same poles and
orders, as N(A, ι₀)⁻¹ : L² → H^m is bijective. Every point of S is a pole: if W extended holomorphically to ι₁ ∈ S,
the identities (Id + B(ι))W(ι) = Id = W(ι)(Id + B(ι)) would extend to ι₁ by continuity, and Id + B(ι₁) would be
invertible, whereas by the theorem it has a nonzero kernel. So S is the set of poles, and
N(A, ι) = N(A, ι₀)(Id + B(ι)) : H^m → L² is invertible exactly off S. At a pole ι₁ of order p write
W(ι) = Σ_(k≥−p) W_k(ι − ι₁)^k and B(ι) = Σ_(k≥0) B_k(ι − ι₁)^k. From (Id + B)W = Id, (Id + B₀)W_(−p) = 0 and
(Id + B₀)W_(−p+k) = −Σ_(1≤l≤k) B_lW_(−p+k−l) for 1 ≤ k < p. The kernel of Id + B₀ is finite-dimensional, as B₀ acts
on it as −Id and B₀ is compact; so W_(−p) has finite rank, and inductively each W_(−p+k), k < p, maps into the
preimage under Id + B₀ of a finite-dimensional space, which is finite-dimensional. So the coefficients of the negative
powers of N(A, ι)⁻¹ = W(ι)N(A, ι₀)⁻¹ have finite rank.

*Bounds off the poles.* Let s ≥ 0 be an integer and Ω ⊂ ℂ a compact set containing no pole. Choose c₁ ≤ c₂ and T ≥ 0
with Ω ⊂ {c₁ ≤ Re ι ≤ c₂, |Im ι| ≤ T}, and let C₁ be the constant of (EE) at the order s for the P_(c,κ),
(c, κ) ∈ [c₁, c₂] × [0, 1], found in the proof of (E1). As a function with values in the operators L² → H^m, N(A, ·)⁻¹
is holomorphic on a neighbourhood of Ω, hence continuous in norm there; so ‖N(A, ι)⁻¹‖_(L²→H^m) ≤ C_Ω for ι ∈ Ω. For
ι = c + iτ ∈ Ω and g ∈ H^s let u := N(A, ι)⁻¹g ∈ H^m, and let n, κ and v := e^(inx)u be as in the proof of (E1). Then
v ∈ L²(Z) and P_(c,κ)v = e^(inx)g ∈ H^s(Z), so v ∈ H^(s+m)(Z) by (EE), and u ∈ H^(s+m)(∂M) by the comparison of
‖v‖_(H^k(Z)) with [u]_(k,τ) in that proof. That comparison, (EE), ‖u‖_(H^k) ≤ [u]_(k,τ) and, as |τ| ≤ T,
[g]_(s,τ) ≤ (s + 1)⟨T⟩^s‖g‖_(H^s) give ‖u‖_(H^(s+m)) ≤ C(‖g‖_(H^s) + ‖u‖_(L²)), with C depending on s, m, T and C₁
only. As ‖u‖_(L²) ≤ C_Ω‖g‖_(L²) ≤ C_Ω‖g‖_(H^s),

    ‖N(A, ι)⁻¹g‖_(H^(s+m)) ≤ C′_Ω‖g‖_(H^s)     (ι ∈ Ω, g ∈ H^s),

which is the bound of (E2). For ι, ι′ ∈ Ω, on H^s,
N(A, ι)⁻¹ − N(A, ι′)⁻¹ = N(A, ι)⁻¹(N(A, ι′) − N(A, ι))N(A, ι′)⁻¹, and N(A, ι′) − N(A, ι) = Σ_j (ι′^j − ι^j)A_j(0)
maps H^(s+m) to H^s with norm at most C″_Ω|ι′ − ι|, as A_j(0) has order at most m − j and
ι′^j − ι^j = (ι′ − ι)Σ_(a+b=j−1) ι′^aι^b. So, in the norm of operators H^s → H^(s+m),
‖N(A, ι)⁻¹ − N(A, ι′)⁻¹‖ ≤ (C′_Ω)²C″_Ω|ι − ι′| on Ω.

*The Laurent coefficients.* Let ι₁ ∈ ℂ, and let r₁ > 0 be so small that the closed disc of radius r₁ about ι₁ contains
no pole other than ι₁. The coefficient of (ι − ι₁)^k, k ∈ ℤ, in the Laurent expansion of N(A, ι)⁻¹ at ι₁ is (2πi)⁻¹
times the integral of (ι − ι₁)^(−k−1)N(A, ι)⁻¹ over the circle |ι − ι₁| = r₁, taken in the operators L² → H^m. Take
for Ω that circle, which contains no pole. By the last paragraph the integrand is continuous on it in the norm of
operators H^s → H^(s+m), so the integral converges in that norm too, to an operator that agrees on H^s with the
coefficient (the Riemann sums are the same, and convergence in H^(s+m) implies convergence in H^m). So the coefficient
maps H^s to H^(s+m), with norm at most r₁^(−k)C′_Ω. As s is arbitrary, it maps C^∞(∂M), the intersection of the
H^s(∂M), to itself. ∎

*Proof of (E3).* Let S be the set of poles of N(A, ·)⁻¹. By the proof of (E2), S is the discrete set of
[[thm:std-analytic-fredholm]] there, and N(A, ι) : H^m → L² is invertible exactly for ι ∉ S. S is also closed: its
complement is open, as B is continuous in norm and a Neumann series inverts every small perturbation of an invertible
operator. So S has finitely many points in every compact set. For ι ∉ S, Π commutes with N(A, ι)⁻¹: for g ∈ L² and
u := N(A, ι)⁻¹g, Πu ∈ H^m and N(A, ι)Πu = ΠN(A, ι)u = Πg, so ΠN(A, ι)⁻¹g = N(A, ι)⁻¹Πg.

Fix ι₁ ∈ ℂ and r₁ > 0 such that the closed disc of radius r₁ about ι₁ contains no point of S other than ι₁. On the
punctured disc write N(A, ι)⁻¹ = Σ_(k≥−p) R_k(ι − ι₁)^k, with p ≥ 0 and R_k : L² → H^m, and
N(A, ι) = Σ_(j≤m) 𝒩_j(ι − ι₁)^j, with 𝒩_j : H^m → L² bounded and 𝒩_0 = N(A, ι₁). R_k is (2πi)⁻¹ times the integral
of (ι − ι₁)^(−k−1)N(A, ι)⁻¹ over the circle |ι − ι₁| = r₁, on which Π commutes with N(A, ι)⁻¹; so ΠR_k = R_kΠ for
every k, as operators on L². The Laurent coefficients of N(A, ·)⁻¹Π at ι₁ are the R_kΠ.

*A pole gives a kernel.* Suppose that N(A, ·)⁻¹Π has a pole at ι₁, and let q ≥ 1 be the largest integer with
R_(−q)Π ≠ 0. For 0 < |ι − ι₁| < r₁, N(A, ι)N(A, ι)⁻¹Π = Π. The coefficient of (ι − ι₁)^(−q) on the left is
𝒩_0R_(−q)Π, as R_kΠ = 0 for k < −q, and on the right it is 0; so N(A, ι₁)R_(−q)Π = 0. Take g ∈ L² with
u := R_(−q)Πg ≠ 0. Then u ∈ H^m, N(A, ι₁)u = 0, and u = R_(−q)ΠΠg = ΠR_(−q)Πg = Πu. Write ι₁ = c + iτ, n := ⌊τ⌋,
κ := τ − n and v := e^(inx)u ∈ L²(Z), as in the proof of (E1). Then P_(c,κ)v = e^(inx)N(A, ι₁)u = 0, so (EE), which
holds for P_(c,κ) (proof of (E1)), gives v ∈ H^(s+m)(Z) for every s, and the comparison of ‖v‖_(H^k(Z)) with
[u]_(k,τ) in the proof of (E1) gives u ∈ H^(s+m)(∂M) for every s. So u ∈ C^∞(∂M), and u = Πu ∈ ΠC^∞(∂M) is a nonzero
solution of N(A, ι₁)u = 0.

*No pole gives invertibility.* Suppose that N(A, ·)⁻¹Π has no pole at ι₁: R_kΠ = 0 for k < 0, and N(A, ι)⁻¹Π → R_0Π
in the norm of operators L² → H^m as ι → ι₁. For u ∈ ΠH^m and 0 < |ι − ι₁| < r₁,
N(A, ι)⁻¹ΠN(A, ι)u = N(A, ι)⁻¹N(A, ι)Πu = u, and letting ι → ι₁ (N(A, ·) : H^m → L² is continuous) gives
R_0ΠN(A, ι₁)u = u. So N(A, ι₁) is injective on ΠH^m, and in particular N(A, ι₁)u = 0 has no solution
0 ≠ u ∈ ΠC^∞(∂M); with the last paragraph this proves the equivalence. Letting ι → ι₁ in N(A, ι)N(A, ι)⁻¹Π = Π gives
N(A, ι₁)R_0Π = Π on L². Let s ≥ 0 be an integer and g ∈ ΠH^s. Then u := R_0Πg = R_0g lies in H^(s+m) by (E2), R_0
being a Laurent coefficient, and u = ΠR_0g = Πu; and N(A, ι₁)u = Πg = g. So N(A, ι₁) maps ΠH^(s+m) onto ΠH^s, and
injectively, as ΠH^(s+m) ⊂ ΠH^m. As s is arbitrary and C^∞(∂M) is the intersection of the H^s(∂M), it maps ΠC^∞(∂M)
bijectively onto itself.

*The case Π = Id.* By the equivalence, ι₁ is a pole of N(A, ·)⁻¹ if and only if N(A, ι₁)u = 0 for some
0 ≠ u ∈ C^∞(∂M), that is, if and only if ι₁ ∈ spec_b(A) ([[def:s11-b-analysis]] (2)). Off spec_b(A) the bijectivity
was just shown, and on spec_b(A), N(A, ι) has a nonzero kernel in C^∞(∂M). By (E1), for every strip
{c₁ ≤ Re ι ≤ c₂} there is R such that N(A, ι) : H^m → L² is invertible, that is ι ∉ S, for |Im ι| ≥ R in the strip.
So the indicial roots in the strip lie in S ∩ {c₁ ≤ Re ι ≤ c₂, |Im ι| ≤ R}, the intersection of S with a compact set,
and there are finitely many. ∎

Define

    Spec_b(A) := {(ι, k) : N(A, ζ)⁻¹ has a pole of order ≥ k + 1 at ζ = ι}

(this set contains all smaller k, as an index set must; the smallest index set containing it, as [[lem:iii-a-1-4]]
uses, is the same whether "of order ≥ k + 1" or "of order k + 1" is used). By (E3), π₁Spec_b(A) = spec_b(A), and, the
pole orders being finite, Spec_b(A) has finitely many elements (ι, k) with c₁ ≤ Re ι ≤ c₂, for all c₁ ≤ c₂.

The Mellin transform is ℳg(ι) := ∫_0^∞ ρ^(−ι) g(ρ) dρ/ρ. In the variable s = −log ρ it is the Fourier–Laplace transform
∫ e^(ιs) g(e^(−s)) ds, so Plancherel's theorem gives (M1): for g supported in ρ < ρ₀, g ∈ ρ^γ L²(|dρ/ρ|; 𝓗) if and only
if ℳg is holomorphic in Re ι < γ with sup_(c<γ) ∫ |ℳg(c + iη)|² dη < ∞, and then 2π‖ρ^(−γ)g‖² equals the integral on
Re ι = γ; ℳ(ρ∂_ρ g) = ιℳg; and g = (2πi)⁻¹ ∫_(Re ι=c) ρ^ι ℳg(ι) dι for c ≤ γ. So g ∈ H^(k,γ)_b(M) if and only if
Σ_(j+|β|≤k) ∫_(Re ι=γ) |ι|^(2j) ‖ℳg(ι)‖²_(H^(|β|)(∂M)) |dι| < ∞ (with the same bound for Re ι < γ). (M2)
([Hin26, Remark 2.14]) For χ ∈ C_c^∞([0, 1)) equal to 1 near 0,
ℳ(χρ^z(log ρ)^k a)(ι) = (−1)^k k!(z − ι)^(−k−1) a + e(ι)a with e entire, since ∫_0^1 ρ^(w−ι) dρ/ρ = (w − ι)⁻¹ for
Re ι < Re w and k derivatives in w give the first term, while (χ − 1_[0,1])ρ^z(log ρ)^k is supported away from 0 and of
compact support. Hence for g ∈ H^(∞,(F,β))_b supported in ρ < 1, ℳg is holomorphic in Re ι < min(β, min Re F) and
meromorphic in Re ι < β with poles only at ι ∈ π₁F, of order at most k(F, ι) + 1, and on vertical lines in Re ι < β
away from the poles |ι|^J ‖ℳg(ι)‖_(H^J(∂M)) is square-integrable for every J, uniformly on compact sets of real parts.

**Lemma {#lem:iii-a-1-4}** ([Hin26, Lemma 2.13], boundary spectrum and polyhomogeneity.) Let
A ∈ Diff^m_b(M; ℂ^(N_E)) be elliptic near ρ = 0, χ ∈ C_c^∞([0, ½ρ₀)) equal 1 on [0, ¼ρ₀] and χ̃ ∈ C_c^∞([0, ρ₀))
equal 1 on [0, ½ρ₀]. Suppose χ̃u ∈ H^(∞,α)_b(M) and χAu ∈ H^(∞,(F,β))_b(M) with β ≠ Re ι for all ι ∈ spec_b(A). Let
E(α) be the smallest index set containing the (ι, k) ∈ Spec_b(A) with Re ι > α, E_0 := E(α) ∪̄ F,
E_(k+1) := E(α) ∪̄ (F ∪̄ (E_k + 1)), E := ⋃_k E_k. Then χ̃u ∈ H^(∞,(E,β))_b(M).

*Proof.* If β ≤ α there is nothing to prove (H^(∞,α)_b ⊂ H^(∞,(E,β))_b), so let β > α. If some exponent of F has real
part β, remove those finitely many terms χρ^z(log ρ)^j f_(z,j) of χAu first: N(A, ·)⁻¹ is holomorphic on Re ι = β, by
(E3), so the circle integral [[eq:iii-a-1-4]] of [[lem:iii-a-1-5]] (whose proof does not use the present lemma) gives
u_(z,j) = ρ^z Σ_(i≤j)(log ρ)^i u_i, u_i ∈ C^∞(∂M), with N(A)u_(z,j) = ρ^z(log ρ)^j f_(z,j); then A(χu_(z,j)) is that term
up to (A − N(A))(χu_(z,j)), whose exponents lie in z + 1 + ℕ₀, above β, and up to terms supported in ρ ≥ ¼ρ₀.
Replacing u by u − Σ χu_(z,j) keeps the hypotheses (Re z = β > α) and the conclusion ((z, j) ∈ F ⊂ E) and removes these
terms, so we may assume β ∉ Re π₁F. Write v := χ̃u and N(A) = Σ_j A_j(0)(ρ∂_ρ)^j in the collar. Then N(A)v = f′ with
f′ := χAu + (χ̃ − χ)Au + [A, χ̃]u − (A − N(A))v. The sum of the second and third terms is w := A(χ̃u) − χAu. It vanishes
on ρ < ¼ρ₀, where χ̃ − χ = 0 and [A, χ̃] = 0, as χ̃ = χ = 1 there, and it is supported in supp χ̃, a compact subset of
[0, ρ₀); so its support is a compact subset of (0, ρ₀) × ∂M. There all derivatives of w are square integrable. Indeed
A(χ̃u) ∈ H^(∞,α)_b(M), as A maps H^(∞,α)_b(M) into itself on functions supported in supp χ̃, where its coefficients are
bounded with all their derivatives, and χAu ∈ H^(∞,(F,β))_b(M); and on a compact subset of (0, ρ₀) × ∂M membership in
either space implies that all derivatives are square integrable, since there b-derivatives are combinations of ordinary
ones with smooth coefficients, the weights are bounded above and below, and the expansion terms of [[eq:s11-partial]]
are smooth. So w is smooth with compact support in (0, ρ₀) × ∂M, and ℳw is entire, with |ι|^n‖ℳw(ι)‖_(H^J(∂M)) bounded
on every strip {c₁ ≤ Re ι ≤ c₂} for all n and J, as ℳ((ρ∂_ρ)^n w) = ι^nℳw. And A − N(A) ∈ ρ Diff^m_b near ρ = 0, so f′ ∈
H^(∞,(F,β))_b + H^(∞,α+1)_b after cutting off. Let γ := min(β, α + 1), decreased slightly if necessary so that no Re ι,
ι ∈ spec_b(A) ∪ π₁F, equals γ (possible as spec_b(A) ∪ π₁F has finitely many points in every strip, by (E3) and
[[def:s11-b-analysis]] (4); β itself is excluded, by the hypothesis and the reduction above, when γ = β). By (M1), ℳv is
holomorphic in Re ι < α and N(A, ι)ℳv = ℳf′ there; by (M2) and (E2), N(A, ι)⁻¹ℳf′ is meromorphic in Re ι < γ and
continues ℳv. Its poles with Re ι < α cancel (as ℳv is
holomorphic there), and there are none on Re ι = α: a pole ι₀ there would make ∫|ℳv(c + iη)|² dη grow at least like
(α − c)⁻¹ as c ↑ α, against the uniform bound of (M1); at ι with α < Re ι < γ the pole order is at most the order of
N(A, ·)⁻¹ plus that of ℳf′. Now v = (2πi)⁻¹ ∫_(Re ι=c) ρ^ι ℳv dι for c < α, and we move the contour to Re ι = γ. This
is justified by (E1) and (M2): on the horizontal segments {c ≤ Re ι ≤ γ, Im ι = ±T}, along a sequence T → ∞,
∫_c^γ ‖N(A, s ± iT)⁻¹ℳf′(s ± iT)‖²_(H^J) ds → 0 for every J (by Fubini, the square-integrability in Im ι of
|ι|^(J′)‖ℳf′‖_(H^(J′)), uniform in the strip, makes T ↦ ∫_c^γ ‖ℳf′(s ± iT)‖²_(H^(J′)) ds integrable, hence small along
a sequence, which a diagonal choice makes one for all J; (E1) bounds N(A, ·)⁻¹ there). This is a statement in L² on the
segments, not a pointwise one, and it is what the contour shift uses. The residues at the finitely many poles in
α < Re ι < γ are of the form ρ^ι Σ_(j≤q)(log ρ)^j a_j, with q + 1 the pole order and a_j ∈ C^∞(∂M) (the Laurent
coefficients of N(A, ·)⁻¹ that enter, of negative and of non-negative powers, map C^∞(∂M) to itself by (E2)): by the
order count these lie in H^(∞,(E(α)∪̄F,γ′)) for every γ′ < γ (the extended union E ∪̄ F of [[def:s11-b-analysis]] (4)
is precisely the addition of pole orders, (z, k + l + 1) from orders k + 1 and l + 1). The integral on Re ι = γ lies in
H^(∞,γ)_b by (M1), for all |ι|-weighted norms, as N(A, ·)⁻¹ is bounded from H^s to H^(s+m) uniformly on that line: by
(E1) where |Im ι| ≥ R, and by (E2) on the compact rest, which contains no pole by (E3). So v ∈ H^(∞,(E_0,γ)) near ρ = 0.
If γ = β we are done. Otherwise γ < β (and γ ≤ α + 1); repeat with α replaced by γ − δ′ for small δ′ > 0 and the
expansion found so far moved into the right side: (A − N(A)) applied to ρ^ι(log ρ)^j a is, by Taylor expansion of the
coefficients A_j(ρ) at ρ = 0, an expansion with exponents in ι + 1 + ℕ₀ and the same log powers, which is E_0 + 1; so f′
∈ H^(∞,(F∪̄(E_0+1),β)) + H^(∞,γ+1−δ′), and the same argument gives E_1 up to the weight min(β, γ + 1 − δ′). Each step
raises the weight by almost 1 until β is reached; finitely many steps suffice, the index sets being contained in E. (The
poles of N(A, ·)⁻¹ that enter at a later step are those with real part above the previous weight, all in E(α).) ∎

**Lemma {#lem:iii-a-1-5}** ([Hin26, Lemma 2.15], formal solutions.) Let A ∈ Diff^m_b(M; ℂ^(N_E)) be elliptic, F an
index set, β ∈ ℝ, ord(z) the order of the pole of N(A, ·)⁻¹ at z (0 if none), and
E := {(ι + j, k + m′) : (ι, k) ∈ F, j ∈ ℕ₀, m′ ≤ Σ_(q=0)^j ord(ι + q)}. There is a continuous linear map
S = S_(A,F,β) : 𝒜^F(M) → 𝒜^E(M), also bounded H^(k,(F,β))_b → H^(k+m,(E,β))_b for every k, such that f − ASf ∈ 𝒜^G(M),
G := {(ι, k) ∈ E : Re ι ≥ β}, resp. f − ASf ∈ H^(k,β)_b. If A depends smoothly on a finite-dimensional parameter b with
b-independent N(A), S can be chosen smooth in b; for β = ∞ the statement on 𝒜-spaces holds with S continuous but
non-linear.

*Proof.* Consider one term χ(ρ)ρ^ι(log ρ)^ℓ f₀ of f, f₀ ∈ H^k(∂M), with Re ι minimal and ℓ = k(F, ι). By Cauchy's formula
ρ^ι(log ρ)^ℓ = (ℓ!/(2πi)) ∮_ι ρ^ζ(ζ − ι)^(−ℓ−1) dζ over a small circle around ι enclosing no other pole of N(A, ·)⁻¹;
put

    u := (ℓ!/(2πi)) ∮_ι ρ^ζ (ζ − ι)^(−ℓ−1) N(A, ζ)⁻¹f₀ dζ.                                                {#eq:iii-a-1-4}

As N(A)(ρ^ζ g) = ρ^ζ N(A, ζ)g, N(A)u = ρ^ι(log ρ)^ℓ f₀ exactly. By the residue theorem
u = ρ^ι Σ_(j≤ℓ+q)(log ρ)^j u_j, q = ord(ι), where u_j is ℓ!/j! times the coefficient of (ζ − ι)^(ℓ−j) in the Laurent
expansion of N(A, ζ)⁻¹ at ι, applied to f₀; so u_j ∈ H^(k+m)(∂M), as every Laurent coefficient gains m derivatives by
(E2). Then χu ∈ H^(k+m,(ι,ℓ+q)) and f − A(χu) has the term removed, up to (A − N(A))(χu), an expansion with
exponents in ι + 1 + ℕ₀ and log powers ≤ ℓ + q (Taylor expansion of the coefficients; this term depends smoothly on b
when A does), and up to commutator terms supported away from ρ = 0, which are 𝒜^∞ near ∂M. Iterating over the finitely
many terms with Re ι ≤ β (new terms with exponents ι + j and log powers raised by the pole orders met, which is the
definition of E) gives u with f − Au ∈ H^(k,β)_b resp. 𝒜^G; for β = ∞, take an asymptotic (Borel) sum of the infinitely
many terms, which is continuous but not linear. Each step is a fixed linear operation, the circle integral
[[eq:iii-a-1-4]] involving no choice (adding an indicial solution ρ^ι u₀ ∈ ker N(A) would be a choice); hence S is
linear, continuous, and smooth in b. ∎

### Scattering and 3b-notions in dimension 4 + 1 {#sec:iii-a-2}

**Definition {#def:iii-a-2-1}** ([Hin26, Definition 2.16, Example 2.17].) For d ∈ ℕ, ˢᶜT*ℝ^d := ℝ̄^d × ℝ^d with (z, ζ)
the covector ζ_μ dz^μ, and 𝒱_sc(ℝ̄^d) is the C^∞(ℝ̄^d)-span of ∂_(z⁰), …, ∂_(z^(d−1)). In {z⁰ > 0}, with ρ_∞ := 1/z⁰ and
ẑ^j := z^j/z⁰,

    ∂_(z⁰) = −ρ_∞(ρ_∞∂_(ρ_∞) + Σ_(j=1)^(d−1) ẑ^j ∂_(ẑ^j)),     ∂_(z^j) = ρ_∞∂_(ẑ^j),

since ∂_(z⁰)ρ_∞ = −ρ_∞² and ∂_(z⁰)ẑ^j = −ρ_∞ẑ^j; so 𝒱_sc(ℝ̄^d) = ρ_d𝒱_b(ℝ̄^d) for a boundary defining function ρ_d. In
dimension 4 + 1 the Minkowski metric ḡ = −dt² + Σ_(j=1)^4 (dx^j)² is an element of C^∞(ℝ̄⁵; S² ˢᶜT*ℝ⁵).

**Definition {#def:iii-a-2-2}** ([Hin26, (2.10) and Definition 2.18] in dimension 4 + 1.) Write ℝ̄⁵ for the radial
compactification of ℝ^(1+4)_(t_*,x), let k_± ∈ ∂ℝ̄⁵ be the limits of (t_*, 0) as t_* → ±∞, and
M̃₀ := [ℝ̄⁵; k_+, k_−], with boundary hypersurfaces sf (the lift of ∂ℝ̄⁵) and K_± (the lifts of k_±);
ρ_sf := ⟨x⟩⁻¹ and ρ_K := ⟨x⟩(1 + t_*² + |x|²)^(−1/2) are defining functions. 𝒱_3sc(M̃₀) is the C^∞(M̃₀)-span of
∂_(t_*), ∂_(x¹), …, ∂_(x⁴). (1) ³ᵇT*M̃₀ := M̃₀ × ℝ⁵, (t_*, x; τ, ξ) being τ dt_*/⟨x⟩ + Σ_(j=1)^4 ξ_j dx^j/⟨x⟩; dually
(v, w) ↦ v⟨x⟩∂_(t_*) + Σ_(j=1)^4 w^j⟨x⟩∂_(x^j). (2) 𝒱_3b(M̃₀) is the C^∞(M̃₀)-span of ⟨x⟩∂_(t_*), ⟨x⟩∂_(x^j),
j = 1, …, 4, equivalently ρ_sf⁻¹𝒱_3sc(M̃₀). (3) Diff^m_3b(M̃₀) and Diff^(m,(α_sf,α_K))_3b := ρ_sf^(−α_sf)ρ_K^(−α_K)
Diff^m_3b, and H^(s,(α_sf,α_K))_3b = ρ_sf^(α_sf)ρ_K^(α_K)H^s_3b (with variable orders as in [[sec:ii-a-2-2]]).

A t_*-translation-invariant A ∈ Diff^(m,(α_sf,0))_3b(M̃₀) has the form

    A = Σ_(j+|α|≤m) ⟨x⟩^(α_sf) a_jα(x) (⟨x⟩∂_(t_*))^j (⟨x⟩∂_x)^α,     a_jα ∈ C^∞(ℝ̄⁴),                    {#eq:iii-a-2-1}

α ∈ ℕ₀⁴, and its spectral family, with (ℱu)(σ, x) := ∫ e^(iσt_*) u(t_*, x) dt_*, is

    Â(σ) = Σ_(j+|α|≤m) ⟨x⟩^(α_sf) a_jα(x) (−iσ⟨x⟩)^j (⟨x⟩∂_x)^α.                                          {#eq:iii-a-2-2}

(The wave operator of a stationary metric of [[sec:iii-b-3]] is of this form with m = 2, α_sf = −2: ⟨x⟩⁻² times a
combination of (⟨x⟩∂)², as in [[ch:s05]].)

**Definition {#def:iii-a-2-3}** ([Hin26, Definition 2.19] in dimension 4 + 1.) X̃ := ℝ⁴,
X̃_sc-b := [[0, 1]_ς × X̃̄; {0} × ∂X̃̄], X̃̄ the radial compactification of X̃, with the faces scf (the lift of
[0, 1] × ∂X̃̄), tf (the front face) and zf (the lift of {0} × X̃̄) and, with ρ := ⟨x⟩⁻¹, the defining functions
ρ_scf = ρ/(ς + ρ), ρ_tf = ς + ρ, ρ_zf = ς/(ς + ρ). 𝒱_sc-b(X̃) is the C^∞(X̃_sc-b)-span of ρ_scf⟨x⟩∂_(x^j),
j = 1, …, 4; Diff^(m,(α_scf,α_tf,α_zf))_sc-b := ρ_scf^(−α_scf)ρ_tf^(−α_tf)ρ_zf^(−α_zf) Diff^m_sc-b; and
‖u‖_(H^(m,(α_scf,α_tf,α_zf))_(sc-b,ς)) := Σ_(|α|≤m) ‖ρ_scf^(−α_scf)ρ_tf^(−α_tf)ρ_zf^(−α_zf)(ρ_scf⟨x⟩∂_x)^α u‖_(L²(X̃,μ))
for a fixed weighted b-density μ (below μ = |dx|), with the variant H^((m;k)) with b-regularity as in [Hin26]. As
ς⟨x⟩ = ρ_zf/ρ_scf and ⟨x⟩∂_(x^j) ∈ ρ_scf⁻¹𝒱_sc-b, [[eq:iii-a-2-2]] gives, for fixed σ̂ with |σ̂| = 1,
{Â(σ̂ς)}_(ς∈[0,1]) ∈ Diff^(m,(α_sf+m,α_sf,0))_sc-b(X̃), as in dimension 3 + 1.

**Lemma {#lem:iii-a-2-4}** ([Hin26, Lemma 2.20] in dimension 4 + 1.) For u ∈ H^(m,(α_sf,0))_3b(M̃₀, |dt_*dx|),

    ∫_(−1)^1 ‖û(σ)‖²_(H^(m,(m+α_sf,α_sf,0))_(sc-b,|σ|)(X̃,|dx|)) dσ ≤ C‖u‖²_(H^(m,(α_sf,0))_3b(M̃₀,|dt_*dx|)),
                                                                                                          {#eq:iii-a-2-3}

and the reverse inequality holds if supp û ⊂ [−1, 1].

*Proof.* The norm on the right is equivalent to Σ_(j+|β|≤m) ‖⟨x⟩^(α_sf)(⟨x⟩∂_(t_*))^j(⟨x⟩∂_x)^β u‖_(L²(|dt_*dx|)), the
weight commuting with the fields up to lower-order terms with bounded coefficients
(⟨x⟩∂_x⟨x⟩^c = c⟨x⟩^c x/⟨x⟩), and the weight ρ_K⁰ being trivial. By Plancherel in t_* this is
Σ_(j+|β|≤m) ∫ ‖⟨x⟩^(α_sf)(σ⟨x⟩)^j(⟨x⟩∂_x)^β û(σ)‖²_(L²(dx)) dσ/(2π), up to constants. For |σ| ≤ 1:
ρ_scf^(−α_sf)ρ_tf^(−α_sf) = ρ^(−α_sf) = ⟨x⟩^(α_sf), ρ_scf⁻¹ = 1 + |σ|⟨x⟩, and
ρ_scf^(−m)(ρ_scf⟨x⟩∂_x)^β = ρ_scf^(−(m−|β|))(⟨x⟩∂_x)^β modulo terms of the same form with fewer derivatives and
bounded coefficients (⟨x⟩∂_x log ρ_scf is bounded); and (1 + |σ|⟨x⟩)^(m−|β|) is comparable to
Σ_(j≤m−|β|) |σ⟨x⟩|^j. So the integrand of [[eq:iii-a-2-3]] is comparable to
Σ_(j+|β|≤m) ‖⟨x⟩^(α_sf)(σ⟨x⟩)^j(⟨x⟩∂_x)^β û(σ)‖² at each |σ| ≤ 1, which gives both inequalities. ∎

*The normal operator at sf* ([Hin26, (2.14)–(2.15)] in dimension 4 + 1). For A as in [[eq:iii-a-2-1]], with
a^∞_jα(ω) := a_jα|_(∂ℝ̄⁴), ω = x/|x| ∈ 𝕊³,

    N_sf(A) := r^(α_sf) Σ_(j+|α|≤m) a^∞_jα(ω)(r∂_(t_*))^j (r∂_x)^α                                        {#eq:iii-a-2-4}

is homogeneous of degree α_sf under (t_*, x) ↦ (ct_*, cx), c > 0, and A − N_sf(A) ∈ Diff^(m,(α_sf−1,0))_3b on
{r ≥ 1}, as a_jα − a^∞_jα and ⟨x⟩ − r are O(r⁻¹) with all b-derivatives. In ρ = r⁻¹, ω, v := ρt_* (so
sf° = ℝ_v × 𝕊³), N_sf(r^(−α_sf)A) = Σ a_jkγ(ω) ∂_v^j (ρ∂_ρ + v∂_v)^k ∂_ω^γ, since ρ⁻¹∂_(t_*) = ∂_v and
ρ∂_ρ|_(t_*) = ρ∂_ρ|_v + v∂_v; and the Mellin transform in ρ gives

    N_sf(r^(−α_sf)A, ϰ) := Σ_(j+k+|γ|≤m) a_jkγ(ω) ∂_v^j (ϰ + v∂_v)^k ∂_ω^γ ∈ Diff^m_b(sf),                {#eq:iii-a-2-5}

so that N_sf(r^(−α_sf)A)(ρ^ϰ u) = ρ^ϰ N_sf(r^(−α_sf)A, ϰ)u for u = u(v, ω).

The only change from dimension 3 + 1 is 𝕊³ in place of 𝕊².

*Extendible and supported spaces* ([Hin26, Section 2.1.5, Notation 2.21]). For a compact submanifold with corners Ω of
a compact manifold with corners, H̄^s_b(Ω) is the space of restrictions to Ω° of elements of H^s_b, with the quotient
norm; Ḣ^s_b(Ω) is the space of elements of H^s_b supported in Ω; H^s_b(Ω)^(•,−) is supported at some faces and
extendible at the others, defined through the δ-enlargement Ω_δ; the same with weights and partial expansions; and
H^s_b := H̄^s_b when every face is extendible. These definitions do not involve the dimension; they are the
constructions of [[sec:ii-a-7]] in the b-setting.

### Integration along x∂_x and x∂_x − y∂_y {#sec:iii-a-3}

This section is [Hin26, Section 2.2]. On [0, 2)_x × [0, 2)_y × (−2, 2)^d_q with the density |dx/x dy/y dq|, write
H^(k,(E,α),(F,β))_b for the b-Sobolev space with partial expansions at x = 0 and y = 0, and fix χ ∈ C_c^∞([0, ¾)) equal
to 1 on [0, ½] ([Hin26, (2.16)]).

**Lemma {#lem:iii-a-3-1}** ([Hin26, Lemma 2.22].) Let Re z < min(α, min Re E) and f ∈ H^(k,(E,α),(F,β))_b. Then
(x∂_x − z)u = f has a unique solution u ∈ H^(k,(E,α),(F,β))_b.

*Proof.* Multiplication by x^(−z) reduces to z = 0, α > 0, min Re E > 0. The terms χ(x)x^w(log x)^ℓ v of f with
Re w ≤ α have w ≠ 0 and are removed by [[eq:iii-a-1-1]] as in [[lem:iii-a-1-2]], by terms in H^(k,(E,α),(F,β)). For
f ∈ H^(k,α,(F,β)), u(x) := ∫_0^x f(s) ds/s solves the equation, and [[eq:iii-a-1-2]] with u in place of u − u(0) shows
u ∈ H^(k,α,(F,β)) (y, q being parameters and the expansion at y = 0 preserved as in [[lem:iii-a-1-2]]). Uniqueness: a
solution of x∂_x u = 0 is a function c(y, q) of the other variables, which lies in H^(k,(E,α)) at x = 0 only if c = 0,
as α > 0 and (0, 0) ∉ E. ∎

**Lemma {#lem:iii-a-3-2}** ([Hin26, Lemma 2.23], with the hypothesis α + Re z > β.) Let z ∈ ℂ, α + Re z > β, and
Re(w + z) ≠ β for all (w, 0) ∈ E. If (x∂_x − y∂_y + z)u = f ∈ H^(k,(E,α),(F,β))_b and
(1 − χ(y))u ∈ H^(k,(E,α),∞)_b, then u ∈ H^(k,(E,α),((E+z)∪̄F,β))_b.

*Proof.* (x∂_x − y∂_y)(x^z u) = x^z f; replacing (u, f, E, α) by (x^z u, x^z f, E + z, α + Re z) reduces to z = 0 with
α > β, which is where α + Re z > β is used.

*Step 1, at x = 0.* Let (w, ℓ), ℓ = k(E, w), with Re w = min Re E ≤ α, and x^w(log x)^ℓ v(y, q),
v ∈ H^(k,(F,β))_b([0, 2) × (−2, 2)^d), the corresponding term of f. By

    (x∂_x − y∂_y)(x^w(log x)^ℓ a(y, q)) = x^w(log x)^ℓ(w − y∂_y)a + ℓx^w(log x)^(ℓ−1)a,                   {#eq:iii-a-3-1}

the coefficient a of x^w(log x)^ℓ in u on {y ≥ ¾} (which exists by the a priori hypothesis) solves (w − y∂_y)a = v
there. Extend a to (0, 2) by solving this equation; (y∂_y − w)a = −v, and [[lem:iii-a-1-2]] in the variable y, whose
hypothesis β ≠ Re w is ours, gives a ∈ H^(k,(F∪̄{(w,0)},β))_b. Then ũ := u − χ(x)x^w(log x)^ℓ a satisfies the hypotheses
with E replaced by E ∖ {(w, ℓ)} at x = 0 and F by F ∪̄ {(w, 0)} at y = 0 (the cut-off contributes terms supported in
x ∈ [½, ¾], where the spaces of u and f have no condition at x = 0). Repeating over the finitely many (w, ℓ) ∈ E with
Re w ≤ α produces u₀ ∈ H^(k,E,(F∪̄E,β))_b near x = 0 with

    ũ := u − u₀:     (x∂_x − y∂_y)ũ =: f̃ ∈ H^(k,α,(E∪̄F,β))_b,     (1 − χ(y))ũ ∈ H^(k,α,∞)_b.            {#eq:iii-a-3-2}

*Step 2, at y = 0.* For (w, ℓ), ℓ = k(E ∪̄ F, w), Re w ≤ β < α, let y^w(log y)^ℓ v(x, q), v ∈ H^(k,α)_b, be the term of
f̃. As (x∂_x − y∂_y)(y^w(log y)^ℓ a(x, q)) = y^w(log y)^ℓ(x∂_x − w)a − ℓy^w(log y)^(ℓ−1)a, [[lem:iii-a-3-1]]
(Re w < α, empty index set at x = 0) gives a ∈ H^(k,α)_b with (x∂_x − w)a = v; subtract χ(y)y^w(log y)^ℓ a, descend in ℓ
and ascend in Re w. This produces ũ₀ ∈ H^(k,α,(E∪̄F,β))_b with (1 − χ(y))ũ₀ = 0 near y ≥ ¾ and u^♭ := ũ − ũ₀
satisfying

    (x∂_x − y∂_y)u^♭ =: f^♭ ∈ H^(k,α,β)_b,     (1 − χ(y))u^♭ ∈ H^(k,α,∞)_b.                               {#eq:iii-a-3-3}

*Step 3, the remainder.* It suffices to show u^♭ ∈ H^(k,α,β)_b, and to do so for k = 0: x∂_x, y∂_y, ∂_q commute with
x∂_x − y∂_y. With ψ ∈ C_c^∞([0, 1)) equal to 1 on [0, ¾],
(x∂_x − y∂_y)(ψ(y)u^♭) = ψf^♭ + yψ′(y)(1 − χ(y))u^♭ still lies in H^(0,α,β) and ψu^♭ vanishes near y = 1; and
(1 − ψ)u^♭ ∈ H^(0,α,∞). Multiplication by (xy)^(−α) commutes with x∂_x − y∂_y, so let α = 0 > β. Drop q. The solution
vanishing near y = 1 is, by integration along the characteristics xy = const,

    u^♭(x, y) = ∫_y^1 f^♭(xy/s, s) ds/s

(indeed x∂_x and y∂_y of the integral agree except for the boundary term −f^♭(x, y) from y∂_y). By Cauchy–Schwarz with
∫_y^1 s^β ds/s ≤ |β|⁻¹y^β, then t := xy/s at fixed (x, s) (so y ∈ (0, s) becomes t ∈ (0, x), dy/y = dt/t), and
∫_t^2 x^β dx/x ≤ |β|⁻¹t^β:

    ∬ y^(−2β)|u^♭|² (dx/x)(dy/y) ≤ |β|⁻¹ ∬ s^(−β) ∫_0^s y^(−β)|f^♭(xy/s, s)|² (dy/y)(ds/s)(dx/x)
        = |β|⁻¹ ∬ s^(−2β) ∫_0^x t^(−β)x^β |f^♭(t, s)|² (dt/t)(ds/s)(dx/x) ≤ |β|⁻² ∬ s^(−2β)|f^♭(t, s)|² (dt/t)(ds/s),

with x ranging over (0, 2). ∎

**Lemma {#lem:iii-a-3-3}** (A product of such operators.) Let z_1, …, z_p ∈ ℂ, repetitions allowed, and let Z be the
smallest index set with k(Z, z) ≥ #{j : z_j = z} − 1 for every z. Let E be an index set without logarithms
(k(E, w) = 0 for w ∈ π₁E), and suppose α + Re z_j > β and Re(w + z_j) ≠ β for all w ∈ π₁E and all j. If

    Pu = f ∈ H^(k,(E,α),(F,β))_b,     (1 − χ(2y))u ∈ H^(k+p,(E,α),∞)_b,     P := Π_(j=1)^p (x∂_x − y∂_y + z_j),
                                                                                                          {#eq:iii-a-3-4}

then u ∈ H^(k,(E,α),((E+Z)∪̄F,β))_b, with E + Z the sum of [[def:s11-b-analysis]] (4).

For p = 1 this is [[lem:iii-a-3-2]] for log-free E (Z = {(z_1 + j, 0) : j ∈ ℕ₀} and E + Z = E + z_1). Iterating
[[lem:iii-a-3-2]] instead loses: once z and z + 1 both occur, the factor z + 1 meets the pair (z + 1, 0) that E + z has
put into the index set at y = 0 and returns (z + 1, 1), which (E + Z) ∪̄ F need not contain. The cure is to solve for
each coefficient in x at once.

*Proof.* Order the factors so that Re z_1 ≥ ⋯ ≥ Re z_p, and let G := (E + Z) ∪̄ F.

*Step 1, at x = 0, one coefficient at a time.* As E has no logarithms, [[eq:iii-a-3-1]] gives
P(x^w a(y, q)) = x^w Π_j(w + z_j − y∂_y)a exactly. For w ∈ π₁E with Re w ≤ α, let v_w ∈ H^(k,(F,β))_b be the
coefficient of x^w in f, and a_w that of u on {y ≥ 3/8}, which lies in H^(k+p) there by [[eq:iii-a-3-4]] and solves
Π_j(w + z_j − y∂_y)a_w = v_w there. Extend a_w to y ∈ (0, 2) as the solution of this ordinary differential equation (with
constant coefficients in log y, q a parameter). Put b_p := a_w and b_(i−1) := (w + z_i − y∂_y)b_i, so that b_0 = v_w and
(y∂_y − (w + z_i))b_i = −b_(i−1). Apply [[lem:iii-a-1-2]] in y for i = 1, …, p in this order: its hypothesis
β ≠ Re(w + z_i) is ours, and (1 − χ(y))b_i ∈ H^k because b_i is p − i derivatives of a_w on {y ≥ 3/8}. It gives
b_i ∈ H^(k,(G_i,β))_b with G_0 := F and G_i := G_(i−1) ∪̄ {(w + z_i, 0)} ([[def:s11-b-analysis]] (4)). The completion by
[[eq:s11-index-set]] at step i adds pairs only at w + z_i + j, j ≥ 1, whose real parts exceed those of every later
w + z_(i′). So no later raise meets a completion: the count at c is raised from k(F, c) once for each j with
w + z_j = c, to at most k(F, c) + k(Z + w, c) + 1 = k((Z + w) ∪̄ F, c), and a completion reaching c from c − j carries
at most the final count at c − j. By induction on Re c, G_p ⊂ (Z + w) ∪̄ F ⊂ G, the extended union being monotone in
each argument and Z + w ⊂ E + Z. Moreover (y∂_y)^i a_w, i ≤ p, is a linear combination of b_p, …, b_(p−i), so it too
lies in H^(k,(G,β))_b.

Let u₀ := Σ_w χ(x)x^w a_w, summed over w ∈ π₁E with Re w ≤ α; then u₀ ∈ H^(k,(E,α),(G,β))_b near x = 0, and
Pu₀ = Σ_w χ(x)x^w v_w + Σ_w [P, χ(x)](x^w a_w). Each commutator term is supported in x ∈ [½, ¾] and applies at most
p − 1 of the fields x∂_x, y∂_y to x^w a_w, so it lies in H^(k,∞,(G,β))_b by the last remark. Hence ũ := u − u₀
satisfies Pũ =: f̃ ∈ H^(k,α,(G,β))_b (f less its expansion at x = 0 lies in H^(k,α,(F,β))_b, and F ⊂ G), and
(1 − χ(2y))ũ ∈ H^(k+p,α,∞)_b, since the a_w are the coefficients of u on {y ≥ 3/8}, and on {¼ < y < 3/8}, where
1 − χ(2y) ≠ 0 too, the coefficient of u solves the same equation and equals a_w by uniqueness.

*Step 2, the factors one at a time with nothing at x = 0.* Put w̃_p := ũ and w̃_(i−1) := (x∂_x − y∂_y + z_i)w̃_i, so
that w̃_0 = f̃. For i = 1, …, p, [[lem:iii-a-3-2]] with the empty index set at x = 0 (its hypothesis on E is then void,
α + Re z_i > β is ours, and (1 − χ(y))w̃_i ∈ H^(k,α,∞)_b by the order k + p in [[eq:iii-a-3-4]]) gives
w̃_i ∈ H^(k,α,(∅∪̄G,β))_b = H^(k,α,(G,β))_b. So u = u₀ + w̃_p ∈ H^(k,(E,α),(G,β))_b. ∎

### The Fourier transform with partial expansions {#sec:iii-a-4}

This section is [Hin26, Section 2.3] in dimension 4 + 1. In it ι names a boundary face, not an indicial root.

Let X := ℝ⁴_x (radially compactified), M := [ℝ̄_(t_*) × X̄; {±∞} × ∂X̄] with faces ℐ (the lift of ℝ̄ × ∂X̄), ι (the front
face) and K (the lift of ∂ℝ̄ × X̄), the b-densities |dt_*/⟨t_*⟩|, |dx/⟨x⟩⁴| and their product, and the spaces
H^(k,(E_I,β_I),(E_ι,β_ι),(E_K,β_K))_b(M) of [[def:s11-b-analysis]] (5) (orders and index sets at ℐ, ι, K, in this
order); the testing fields are compositions of ∂_(t_*), t_*∂_(t_*), ⟨x⟩∂_(x^j), j ≤ 4. These are the manifold and the
spaces of [[sec:ii-g1-3-1]]. At high frequencies H^(k,β,γ)_(b+)(±[½, ∞) × X) is the space of [[sec:ii-g1-3-1]]; at low
frequencies X^±_sc-b := [±[0, 1]_σ × X̄; {0} × ∂X̄] with faces scf, tf, zf, as in [[sec:ii-g1-3-1]], carries the spaces
of [[def:s11-b-analysis]] (5) with partial expansions (index set (0, 0) at zf, coefficients in H_b(X), as in
[[eq:s10-zf]]).

*The inputs in dimension 4 + 1.* The four statements [Hin26, (2.25a)–(2.26b)], called (T1)–(T4) here, are proved in
dimension 4 + 1 in [[ch:s10]]:

(T1) ([Hin26, (2.25a)] and the matching statement of [Hin26, (2.25b)]): by [[prop:ii-g1-3-3]] (1), for β_K ∈ (0, ∞) ∖ ℕ,
ε ∈ (0, 1), β_I ≥ β_ι − min(β_K, 1 − ε) and u ∈ H^(k+1,(β_I,β_ι,β_K))_b(M),
(ℱu)|_(±(0,1]) ∈ H^(k,(min(β_I,β_ι)−ε,β_ι−1,((0,0),β_K−1)))_b(X^±_sc-b), with the σ-Taylor coefficients of order
< β_K − 1 of the two signs equal.

(T2) ([Hin26, (2.25b)]): [[prop:ii-g1-3-3]] (2), with the loss ℓ = ⌈(½ − min(β_K, β_ι − β_I))_+⌉.

(T3) ([Hin26, (2.26a)]): by [[prop:ii-g1-3-5]] (1), with ℓ := ⌈(max(β_ι − β_scf, β_K) + ε − ½)_+⌉, if
v^± ∈ H^(k+ℓ,(β_scf,β_ι−1,((0,0),β_K−1)))_b(X^±_sc-b) have the same σ-Taylor coefficients, then
ℱ⁻¹v ∈ H^(k,(min(β_scf,β_ι)−ε,β_ι,β_K))_b(M), v := χ(σ)Σ_± 1_(±σ>0)v^±.

(T4) ([Hin26, (2.26b)]): [[prop:ii-g1-3-5]] (2), whose high-frequency space carries the weight δ − 1 where that of
[Hin26] carries δ; the statement of [Hin26], with any δ, follows by renaming δ.

We also use, from the same proofs, that ℱ ∘ t_*∂_(t_*) = (−σ∂_σ − 1) ∘ ℱ (integration by parts:
∫ e^(iσt_*) t_*∂_(t_*)u = −∫(iσt_* + 1)e^(iσt_*)u, and ∂_σℱu = ℱ(it_*u)), and that ℱ commutes with operators in x. As
σ∂_σ commutes with 1_(±σ>0) and [σ∂_σ, χ(σ)] = σχ′(σ) is supported in ½ ≤ |σ| ≤ 1, we have, for v as in (T3) and any
z,

    ℱ⁻¹((σ∂_σ − (z − 1))w) = (−t_*∂_(t_*) − z)ℱ⁻¹w                                                       {#eq:iii-a-4-1}

for every tempered w, and (σ∂_σ − (z − 1))v = χ(σ)Σ_± 1_(±σ>0)(σ∂_σ − (z − 1))v^± + r with r supported in
½ ≤ |σ| ≤ 1. Such an r, if of class H^(k′,β_scf) there, has ℱ⁻¹r ∈ H^(k′−ℓ′,(β_scf−ε,J,J))_b(M) for every J, with a
loss ℓ′ = ℓ′(J) that grows with J ([[prop:ii-g1-3-5]] (1)) and is finite for the finitely many J used, by (T3)
with the tf- and zf-weights taken arbitrarily large (r vanishes near tf and zf); we call such terms *harmless*.

**Lemma {#lem:iii-a-4-1}** ([Hin26, Lemma 2.24].) Let χ ∈ C_c^∞((−1, 1)) equal 1 near 0. The following are b-normal
vector fields: (1) −t_*∂_(t_*) at K; (2) −t_*∂_(t_*) − χ(r⁻¹)r∂_r at ι (defined as −t_*∂_(t_*) near r = 0);
(3) −χ(r⁻¹)r∂_r at ℐ; (4) σ∂_σ at zf; (5) σ∂_σ + χ(ρ)ρ∂_ρ at tf; (6) χ(ρ)ρ∂_ρ at scf; here r = |x|, ρ = |x|⁻¹,
ω = x/|x| ∈ 𝕊³.

*Proof.* In t_* > 1 let τ := t_*⁻¹, so −t_*∂_(t_*) = τ∂_τ. Near ι ∩ K: ρ_ι = ρ, ρ_K = τ/ρ; then τ∂_τ = ρ_K∂_(ρ_K)
and ρ∂_ρ = ρ_ι∂_(ρ_ι) − ρ_K∂_(ρ_K), so −t_*∂_(t_*) − r∂_r = τ∂_τ + ρ∂_ρ = ρ_ι∂_(ρ_ι), and near K° (coordinates τ, x)
−t_*∂_(t_*) = τ∂_τ with τ defining K. Near ι ∩ ℐ: ρ_ι = τ, ρ_I = ρ/τ; τ∂_τ = ρ_ι∂_(ρ_ι) − ρ_I∂_(ρ_I),
ρ∂_ρ = ρ_I∂_(ρ_I), so the field in (2) is ρ_ι∂_(ρ_ι) and −r∂_r = ρ_I∂_(ρ_I), and near ℐ° (coordinates t_*, ρ, ω)
−r∂_r = ρ∂_ρ. The same holds for t_* < −1. On X^±_sc-b near zf ∩ tf: ρ_zf = |σ|/ρ, ρ_tf = ρ, and
σ∂_σ = ρ_zf∂_(ρ_zf), ρ∂_ρ = ρ_tf∂_(ρ_tf) − ρ_zf∂_(ρ_zf), so σ∂_σ + ρ∂_ρ = ρ_tf∂_(ρ_tf); near zf°, σ∂_σ = ρ_zf∂_(ρ_zf)
with ρ_zf = |σ|. Near tf ∩ scf: ρ_scf = ρ/|σ|, ρ_tf = |σ|; ρ∂_ρ = ρ_scf∂_(ρ_scf) and
σ∂_σ = ρ_tf∂_(ρ_tf) − ρ_scf∂_(ρ_scf), so (5) is ρ_tf∂_(ρ_tf) there too, and (6) holds. In each case the field equals
the normal field of an adapted chart exactly, and the cut-offs act only away from the face. ∎

**Proposition {#prop:iii-a-4-2}** ([Hin26, Proposition 2.25] in dimension 4 + 1.) Let β_K ∈ (0, ∞) ∖ ℕ,
β_I, β_ι ∈ ℝ, and E_I, E_ι, E_K index sets with β_I, β_ι − 1 ∉ Re π₁E_I, β_ι ∉ Re π₁E_ι, β_K ∉ Re π₁E_K and
min Re E_K > 0.

(1) (Fourier transform.) Suppose

    β_I ≥ β_ι − β_K,     β_I > β_ι − min(1, min Re E_K).                                                 {#eq:iii-a-4-2}

Let ε > 0 be small and β̃_ι := min(β_ι, min Re E_ι − ε). There is l ∈ ℕ₀, depending only on the weights and index sets,
such that for u ∈ H^(k+l,(E_I,β_I),(E_ι,β_ι),(E_K,β_K))_b(M),

    (ℱu)|_(σ∈±[0,1]) ∈ H^(k, (E_I, min(β_I,β̃_ι)−ε), ((E_ι−1)∪̄E_I, β_ι−1), ((0,0)∪̄(E_K−1), β_K−1))_b(X^±_sc-b).
                                                                                                          {#eq:iii-a-4-3}

(2) (Inverse Fourier transform.) Let χ ∈ C_c^∞((−1, 1)) equal 1 near [−½, ½], β_scf ∈ ℝ, and ε and β̃_ι as in (1).
There is l ∈ ℕ₀ such that if v^± ∈ H^(k+l, β_scf, (E_ι−1,β_ι−1), ((0,0)∪̄(E_K−1),β_K−1))_b(X^±_sc-b) satisfy, at zf,

    (σ∂_σ)^(ℓ_j+1)∂_σ^j v⁻ = (σ∂_σ)^(ℓ_j+1)∂_σ^j v⁺,     j = 0, …, ⌊β_K − 1⌋,     ℓ_j := k(E_K, j + 1),   {#eq:iii-a-4-4}

then for v := χ(σ)Σ_± 1_(±σ>0)v^±,

    ℱ⁻¹v ∈ H^(k, min(β_scf,β̃_ι)−ε, (E_ι,β_ι), (E_K,β_K))_b(M).                                           {#eq:iii-a-4-5}

The meaning of [[eq:iii-a-4-4]]: by (σ∂_σ)∂_σ^j = ∂_σ^j(σ∂_σ − j), it says that the coefficient of σ^j in
(σ∂_σ − j)^(ℓ_j+1)v^±, which is log-free, is the same for both signs. The factor σ∂_σ − j occurs k(E_K, j + 1) + 1
times in R_zf below, as (z, m′) ∈ E_K with z − 1 = j.

*Proof.* We take ε so small, and decrease it if necessary, that none of min(β_I, β̃_ι) − ε,
β̃_K := min(β_K, min Re E_K − ε) and min Re E_ι − ε is an integer or the real part of an element of π₁E_I, π₁E_K
(finitely many conditions below any bound). We write E_(ι,≤) := {(z, m′) ∈ E_ι : Re z ≤ β_ι} and similarly E_(K,≤),
E_(I,≤).

*Part (1), E_I = ∅.* Then u ∈ H^(k+l,(β_I,β̃_ι,β̃_K))_b(M), and the hypotheses of (T1) hold for these weights:
β_I ≥ β̃_ι − β̃_K (if β̃_K = β_K by [[eq:iii-a-4-2]], and otherwise because
β_I > β_ι − min Re E_K ≥ β̃_ι − β̃_K − ε strictly, so for small ε), and β_I ≥ β̃_ι − (1 − ε) for small ε, as
β_I > β_ι − 1. They remain true when β̃_K is increased up to β_K or β̃_ι up to β_ι. So (T1) gives

    ℱu ∈ H^(k,(min(β_I,β̃_ι)−ε, β̃_ι−1, ((0,0),β̃_K−1)))_b(X^±_sc-b).                                     {#eq:iii-a-4-6}

Let R_ι := Π_((z,m′)∈E_(ι,≤)) (−t_*∂_(t_*) − χ(r⁻¹)r∂_r − z). By the converse in [[lem:iii-a-1-3]] at ι
([[lem:iii-a-4-1]] (2)) and (F1) at ℐ and K, R_ιu ∈ H^(k+l−|E_(ι,≤)|,(β_I,β_ι,β̃_K))_b, so for l large (T1) gives
ℱ(R_ιu) ∈ H^(k,(min(β_I,β_ι)−ε,β_ι−1,((0,0),β̃_K−1))). As ℱ(−t_*∂_(t_*)u) = (σ∂_σ + 1)ℱu and −r∂_r = ρ∂_ρ commutes
with ℱ, ℱ(R_ιu) = Π_(E_(ι,≤)) (σ∂_σ + χ(ρ)ρ∂_ρ − (z − 1))ℱu. Weakening its scf-weight to min(β_I, β̃_ι) − ε,
[[lem:iii-a-1-3]] at tf ([[lem:iii-a-4-1]] (5); its hypothesis is β_ι − 1 ∉ Re π₁(E_ι − 1); its a priori hypothesis
away from tf is [[eq:iii-a-4-6]]) gives

    ℱu ∈ H^(k,(min(β_I,β̃_ι)−ε, (E_ι−1,β_ι−1), ((0,0),β̃_K−1)))_b.                                        {#eq:iii-a-4-7}

Now let R_K := Π_((z,m′)∈E_(K,≤)) (−t_*∂_(t_*) − z). By the converse in [[lem:iii-a-1-3]] at K ([[lem:iii-a-4-1]] (1))
and (F1), R_Ku ∈ H^(k+l−|E_(K,≤)|,(β_I,(E_ι,β_ι),β_K))_b, with the full weight β_K at K; [[eq:iii-a-4-7]] applied to it
(with β̃_K replaced by β_K, allowed above) gives

    Π_((z,m′)∈E_(K,≤)) (σ∂_σ − (z − 1)) ℱu = ℱ(R_Ku) ∈ H^(k,(min(β_I,β̃_ι)−ε, (E_ι−1,β_ι−1), ((0,0),β_K−1)))_b.

Apply in addition Π_(j≤⌊β_K−1⌋)(σ∂_σ − j), which annihilates the zf-terms of index set (0, 0) with real part ≤ β_K − 1,
so that the right side has empty index set at zf and weight β_K − 1; then integrate one factor at a time, in decreasing
order of real part as in [[lem:iii-a-1-3]], by [[lem:iii-a-1-2]] at zf ([[lem:iii-a-4-1]] (4); its hypotheses are
β_K − 1 ≠ j, true as β_K ∉ ℕ, and β_K − 1 ≠ Re(z − 1), true as β_K ∉ Re π₁E_K; the a priori hypothesis away from zf is
[[eq:iii-a-4-7]]). The index set obtained at zf is (0, 0) ∪̄ (E_K − 1) (below the weight β_K − 1): in this order each
exponent c is raised once per factor, from −1 to k((0, 0), c) + k(E_K − 1, c) + 1, and the completions by
[[eq:s11-index-set]] stay below that. Each one-factor step costs at most one derivative (as in [[lem:iii-a-1-3]]),
absorbed in l. With [[eq:iii-a-4-7]] at tf and scf this is [[eq:iii-a-4-3]].

*Part (1), general E_I.* Let χ_K ∈ C^∞(M) equal 1 near K and 0 near ℐ. χ_Ku vanishes near ℐ, so it lies in the space
with E_I = ∅ and any ℐ-weight β′_I ≥ β_I; the case just proved, with β′_I so large that
min(β′_I, β̃_ι) = β̃_ι, gives [[eq:iii-a-4-3]] for it (its tf index set E_ι − 1 lies in (E_ι − 1) ∪̄ E_I). So assume u
vanishes near K; then E_K = ∅ and the K-weight is arbitrary: fix β_K ∉ ℕ, at least its given value (so
[[eq:iii-a-4-2]] persists), with β_K > β_ι + max(0, −min Re E_I), so that β_K − 1 + Re z > β_ι − 1 for every
z ∈ π₁E_I, as [[lem:iii-a-3-3]] needs. Let χ̃ ∈ C_c^∞(X) equal 1 on {|x| ≤ 8}. As u vanishes near K, χ̃u has compact
support in (t_*, x), so ℱ(χ̃u) is entire in σ with values in H^(k+l)_b of compact support in x: it lies in
H^(k+l,(∞,∞,((0,0),β_K−1)))_b(X^±_sc-b). Let R_I := Π_((z,m′)∈E_(I,≤)) (−χ(r⁻¹)r∂_r − z); by the converse in
[[lem:iii-a-1-3]] at ℐ ([[lem:iii-a-4-1]] (3)) and (F1), R_Iu ∈ H^(k+l−|E_(I,≤)|,(β_I,(E_ι,β_ι),β_K))_b, and the case
E_I = ∅ gives

    Π_((z,m′)∈E_(I,≤)) (χ(ρ)ρ∂_ρ − z) ℱu = ℱ(R_Iu) ∈ H^(k+l′, (min(β_I,β̃_ι)−ε, (E_ι−1,β_ι−1), ((0,0),β_K−1)))_b,

l′ := l − |E_(I,≤)| − l₀, l₀ the loss of the case E_I = ∅. Integrate from ρ ≥ 1/8, where ℱu = ℱ(χ̃u), towards ρ = 0.
Near zf, in ρ_zf = |σ|/ρ, ρ_tf = ρ, each factor ρ∂_ρ − z equals −(ρ_zf∂_(ρ_zf) − ρ_tf∂_(ρ_tf) + z), so the product is
± the operator of [[lem:iii-a-3-3]] with x = ρ_zf, y = ρ_tf, one z_j for each (z, m′) ∈ E_(I,≤) (so z occurs
k(E_I, z) + 1 times and Z is E_(I,≤) completed by [[eq:s11-index-set]], contained in E_I), (E, α) = ((0, 0), β_K − 1),
which has no logarithms, and (F, β) = (E_ι − 1, β_ι − 1). Its hypotheses hold: β_K − 1 + Re z > β_ι − 1 by the choice of
β_K; Re(w + z) ≠ β_ι − 1 for w ∈ ℕ₀, as β_ι − 1 ∉ Re π₁E_I and index sets are closed under adding ℕ₀; and on ρ ≥ ¼,
where 1 − χ(2ρ) ≠ 0, the a priori condition is ℱu = ℱ(χ̃u), of order k + l ≥ k + l′ + |E_(I,≤)|. As (0, 0) + Z = Z,
[[lem:iii-a-3-3]] gives the index sets ((0, 0), β_K − 1) at zf and (Z ∪̄ (E_ι − 1), β_ι − 1) ⊂ (E_I ∪̄ (E_ι − 1), β_ι −
1) at tf. Near scf, in ρ_scf = ρ/|σ|, ρ_tf = |σ|, ρ∂_ρ − z = ρ_scf∂_(ρ_scf) − z, and [[lem:iii-a-1-2]] at scf, one factor
at a time in decreasing order of Re z as in [[lem:iii-a-1-3]] (with min(β_I, β̃_ι) − ε ≠ Re z by the choice of ε; the a
priori condition on ρ_scf ≥ ½ holds in the zf chart, and the tf index set found there is carried as the data at the
other face), gives the index set (E_I, min(β_I, β̃_ι) − ε) there, the derivatives lost one factor at a time absorbed
in l. This is [[eq:iii-a-4-3]].

*Part (2), E_K = ∅.* Then [[eq:iii-a-4-4]] is the equality of the σ-Taylor coefficients of v^± of orders
≤ ⌊β_K − 1⌋ (as ℓ_j = −1), and v^± ∈ H^(k+l,(β_scf,β̃_ι−1,((0,0),β_K−1))), so (T3) gives

    u := ℱ⁻¹v ∈ H^(k+l−l₁,(β′_I,β̃_ι,β_K))_b(M),     β′_I := min(β_scf, β̃_ι) − ε,                        {#eq:iii-a-4-8}

l₁ the loss of (T3). Let R_tf := Π_((z,m′)∈E_(ι,≤)) (σ∂_σ + χ(ρ)ρ∂_ρ − (z − 1)). By the converse in
[[lem:iii-a-1-3]] at tf ([[lem:iii-a-4-1]] (5)), R_tf v^± ∈ H^(k+l−|E_(ι,≤)|,(β_scf,β_ι−1,((0,0),β_K−1)))_b, and the
σ-Taylor coefficients of R_tf v^± still agree: near zf, σ∂_σ multiplies the coefficient of σ^j by j and χ(ρ)ρ∂_ρ acts
on the coefficients in x, the same on both sides. By [[eq:iii-a-4-1]],
ℱ⁻¹(R_tf v) = Π(−t_*∂_(t_*) − χ(r⁻¹)r∂_r − z)u, while R_tf v equals χ(σ)Σ_± 1_(±σ>0)R_tf v^± up to harmless terms; so
(T3) gives

    Π_((z,m′)∈E_(ι,≤)) (−t_*∂_(t_*) − χ(r⁻¹)r∂_r − z) u ∈ H^(k+l−|E_(ι,≤)|−l₁,(β′_I,β_ι,β_K))_b(M),

and [[lem:iii-a-1-3]] at ι ([[lem:iii-a-4-1]] (2); β_ι ∉ Re π₁E_ι; a priori hypothesis [[eq:iii-a-4-8]]) gives
[[eq:iii-a-4-5]] with E_K = ∅.

*Part (2), general E_K.* Weakening the zf data to ((0, 0), β̃_K − 1) (the terms of E_K − 1, and their extended union
with (0, 0), have real part ≥ min Re E_K − 1 > β̃_K − 1) and using [[eq:iii-a-4-4]] for j ≤ ⌊β̃_K − 1⌋, where it is
the plain matching (as j + 1 < min Re E_K gives ℓ_j = −1), the case just proved gives
u ∈ H^(k+l−l₂,(β′_I,(E_ι,β_ι),β̃_K))_b(M). Let R_zf := Π_((z,m′)∈E_(K,≤)) (σ∂_σ − (z − 1)). It annihilates the zf-terms
of E_K − 1 below β_K − 1, so R_zf v^± ∈ H^(k+l−|E_(K,≤)|,(β_scf,(E_ι−1,β_ι−1),((0,0),β_K−1)))_b. Its coefficient of
σ^j, j ≤ ⌊β_K − 1⌋, is a nonzero constant (the product of j − (z − 1) over the factors with z − 1 ≠ j, the same for
both signs) times the coefficient of σ^j in (σ∂_σ − j)^(ℓ_j+1)v^±, so [[eq:iii-a-4-4]] is exactly the matching of the
Taylor coefficients of R_zf v^±. By [[eq:iii-a-4-1]] and the case E_K = ∅ (harmless terms aside),

    Π_((z,m′)∈E_(K,≤)) (−t_*∂_(t_*) − z) u = ℱ⁻¹(R_zf v) ∈ H^(k′,(β′_I,(E_ι,β_ι),β_K))_b(M),

and [[lem:iii-a-1-3]] at K ([[lem:iii-a-4-1]] (1); β_K ∉ Re π₁E_K) gives the index set (E_K, β_K) at K. With l the sum
of the losses met, this is [[eq:iii-a-4-5]]. ∎

*Use in the following chapters.* [[lem:iii-a-1-3]] (testing) and [[lem:iii-a-1-2]] (integration) prove partial
expansions at the faces of M and X_sc-b; [[lem:iii-a-1-4]] and [[lem:iii-a-1-5]] give normal-operator expansions at sf,
where the indicial roots are those of [[sec:iii-a1-2-3]]; [[lem:iii-a-2-4]] and [[eq:iii-a-2-4]]–[[eq:iii-a-2-5]] give
the spectral families and the normal operator at sf of the stationary operators of [[sec:iii-b-3]];
[[lem:iii-a-3-1]]–[[lem:iii-a-3-3]] integrate the transport operators at ι and ℐ; and [[prop:iii-a-4-2]] passes
between the time and the frequency sides. Every statement of [[sec:iii-a-1]]–[[sec:iii-a-4]] is in b-densities, so the
numbers in the hypotheses (β_ι − 1, β_K − 1, [[eq:iii-a-4-2]]) are those of [Hin26]; the dimension enters only through
[[prop:ii-g1-3-3]] and [[prop:ii-g1-3-5]], which hold in dimension 4 + 1.

*Remarks on [Hin26, Sections 2.1–2.3].* Several statements above differ from their counterparts in [Hin26].
(1) [Hin26, (2.29)] uses ℓ = k(E_K, j) in place of ℓ_j = k(E_K, j + 1) in [[eq:iii-a-4-4]]. The logarithmic terms of
v^± at σ^j come from (j + 1, ·) ∈ E_K, and R_zf contains σ∂_σ − j exactly k(E_K, j + 1) + 1 times; already for
E_K = (1, 0), where v^± carries a^± log|σ| at zf, the condition with ℓ = k(E_K, 0) = −1 at j = 0 asks v⁻ = v⁺ at zf,
which is meaningless for a logarithmically divergent function, while the proof needs a⁻ = a⁺. (2) In the proof of
[Hin26, Proposition 2.25 (2)] the zf-weight of R_zf v^± is β_K − 1, not β_K. (3) The commutator of σ∂_σ with χ(σ),
supported in ½ ≤ |σ| ≤ 1, is harmless ([[eq:iii-a-4-1]]). (4) The constant in Cauchy's formula in the proof of
[[lem:iii-a-1-5]] is ℓ!/(2πi). (5) [Hin26, Lemma 2.23] assumes α > β; the reduction to z = 0 needs α + Re z > β, and the
condition is necessary: for α + Re z < c < β, u := x^(−z)χ(xy)(xy)^c solves (x∂_x − y∂_y + z)u = 0, satisfies the a
priori condition with E = ∅, and is not in H^(k,α,β)_b, being y^c times a smooth nonvanishing function near y = 0,
x = ½. In [[prop:iii-a-4-2]] the weight β_K is free in the case where the condition is used (the function vanishes near
K) and is taken large enough. (6) For general E_I the proof of [Hin26, Proposition 2.25 (1)] integrates the factors of
R_I one at a time; once z and z + 1 both occur in E_(I,≤), the extended union returns (z + 1, 1), a logarithm the stated
index set need not contain. The stated set is right, and follows coefficient by coefficient in the zf variable
([[lem:iii-a-3-3]]). (7) The integrations in [[lem:iii-a-1-3]] are carried out in decreasing order of real part, on
which the result depends (for V(V − 1), integrating V first gives (1, 1)); and [[lem:iii-a-1-4]] and [[lem:iii-a-1-5]]
reach the weight β only once the terms of F with real part β are solved first.
