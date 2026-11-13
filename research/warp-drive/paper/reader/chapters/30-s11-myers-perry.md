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
D := ρ∂_ρ. The variable of an indicial family, written λ in [Hin26], is written ι; in [[sec:iii-a-4]] the letter ι
also names a boundary face, as in [[sec:ii-g1-3-1]], and no indicial variable occurs there. In [[sec:iii-b-1]] to
[[sec:iii-b-6]] the letter m is the mass parameter of the family; in [[sec:iii-a-1]] to [[sec:iii-a-4]] it is the order
of a differential operator. The spacetime dimension is written 5.

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

*Proof.* Contracting the Ricci identity, ∇̸^d∇̸_a ω_d = ∇̸_a∇̸^d ω_d + (ν − 1)ω_a. (a) With ω = dS and the symmetry of the
Hessian, −(Δ̸dS)_a = ∇̸^d∇̸_d∇̸_a S = ∇̸^d∇̸_a∇̸_d S = ∇̸_a∇̸^d∇̸_d S + (ν − 1)∇̸_a S. (b)
2(δ̸δ̸*ω)_b = −∇̸^a∇̸_a ω_b − ∇̸^a∇̸_b ω_a = (Δ̸ω)_b − ∇̸_b∇̸^a ω_a − (ν − 1)ω_b. (c) For a 2-tensor S_eb the Ricci
identity gives ∇̸_d∇̸_a S_eb − ∇̸_a∇̸_d S_eb = −g̸_ae S_db + g̸_de S_ab − g̸_ab S_ed + g̸_db S_ea; contracting d with e and
taking S_db := ∇̸_d ω_b, so that ∇̸^d S_db = −(Δ̸ω)_b and tr S = −δ̸ω,

    ∇̸^d∇̸_a∇̸_d ω_b = −∇̸_a(Δ̸ω)_b + (ν − 1)∇̸_a ω_b + ∇̸_b ω_a + g̸_ab δ̸ω.

With ∇̸_d∇̸_a ω_b = ∇̸_a∇̸_d ω_b + g̸_db ω_a − g̸_ab ω_d this yields

    −(Δ̸∇̸ω)_ab = ∇̸^d∇̸_d∇̸_a ω_b = −∇̸_a(Δ̸ω)_b + (ν − 1)∇̸_a ω_b + 2∇̸_b ω_a + 2g̸_ab δ̸ω,

and symmetrising in a, b gives (c). (d) are the formal adjoints of (a) and (c): the adjoint of d on functions is δ̸, of
δ̸* is δ̸, of g̸· is tr, Δ̸ is formally self-adjoint, and two differential operators agree if and only if their formal
adjoints do. ∎

**Lemma {#lem:iii-a1-1-2}** (Ambient identities.) For a function f, a tangential vector field V and a tangential
symmetric matrix field Q on 𝕊^ν:

    Δᵉ(f x̂) = (Δ̸f + νf) x̂ − 2∇̸f,                                                                     {#eq:iii-a1-1-2a}

    ΔᵉV = (Δ̸ + 1)V − 2(δ̸V) x̂,                                                                         {#eq:iii-a1-1-2b}

    Δᵉ(f x̂ ⊗ x̂) = (Δ̸f + 2νf) x̂ ⊗ x̂ − 2fP − 2x̂ ⊙ ∇̸f,                                                {#eq:iii-a1-1-2c}

    Δᵉ(x̂ ⊙ V) = x̂ ⊙ (Δ̸ + ν + 3)V − 4(δ̸V) x̂ ⊗ x̂ − 4δ̸*V,                                            {#eq:iii-a1-1-2d}

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
a(dx̄⁰)² + 2b dx̄⁰dx̄¹ + 2dx̄⁰ ⊗_s rc + e(dx̄¹)² + 2dx̄¹ ⊗_s rf + r²q, with 2α ⊗_s β := α ⊗ β + β ⊗ α and αβ := α ⊗_s β. In
Cartesian terms, rω̸ is the tangential field V with V♭|_(𝕊³) = ω̸ of the ambient picture, extended homogeneously of
degree 0, and r²q is likewise the tangential matrix field of q: dxⁱ pulls back to r ∂_a x̂ⁱ dyᵃ on the sphere of radius
r. Neither identification depends on (t, r). The Minkowski metric and its dual are

    ḡ = −dt² + dr² + r²g̸ = −dx̄⁰dx̄¹ + r²g̸,
    ḡ⁻¹ = −4∂₀ ⊗_s ∂₁ + r⁻²g̸⁻¹ = 2ρ∂_(t_*) ⊗_s ρ∂_ρ + ρ²((ρ∂_ρ)² + g̸⁻¹),                                  {#eq:iii-a1-2-3}

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
    Γ̄⁰_(ab) = −r g̸_ab,     Γ̄¹_(ab) = r g̸_ab,     Γ̄^c_(ab) = Γ̸^c_(ab),                                    {#eq:iii-a1-2-5}

as in [Hin26, (2.40)]: ḡ_01 = −½, ḡ^01 = −2, ḡ_ab = r²g̸_ab, and for example Γ̄⁰_(ab) = ½ḡ^01(−∂₁ḡ_ab) = −r g̸_ab,
Γ̄^c_(0b) = ½r⁻²g̸^cd ∂₀(r²) g̸_bd. The scalar wave operator □̄u = −ḡ^μκ u_(;μκ) is

    □̄ = 4∂₀∂₁ + (3/r)(∂₁ − ∂₀) + r⁻²Δ̸ = −2∂_(t_*)ρ(ρ∂_ρ − 3/2) + ρ²(−(ρ∂_ρ)² + 2ρ∂_ρ + Δ̸).              {#eq:iii-a1-2-6}

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
□_c = −2∂_(t_*)ρ(D − ν/2) + ρ²(−D² + (ν − 1)D + Δ̸). Write α := dt = ½(dx̄⁰ + dx̄¹) and β := dr = ½(dx̄⁰ − dx̄¹) = x̂ · dx.

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
    T_Q = (□_c + 2r⁻²)q − 2r⁻²𝖡g̸ − 4r⁻²δ̸*𝖴.

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

*The divergence.* (δ̄h)_κ = −ḡ^μσ ∇̄_μ h_σκ = 2(∇̄₀h_1κ + ∇̄₁h_0κ) − r⁻²g̸^ab ∇̄_a h_bκ, with h_00 = a, h_01 = b,
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
real. In Cartesian coordinates a 1-form with ∂_μω_κ + ∂_κω_μ = 0 satisfies ∂_σ∂_μω_κ = 0 (the identity
∂_σ∂_μω_κ = ∂_σ s_μκ + ∂_μ s_σκ − ∂_κ s_σμ, s := δ̄*ω), so on the connected set ℝ_t × (ℝ⁴ ∖ 0) it is affine,
ω_μ = a_μ + B_μκ x^κ with B antisymmetric. The splitting [[eq:iii-a1-2-2]] does not depend on t, so ω is independent of
t, which forces B_μ0 = 0: ω is a combination of dt, the dxⁱ and the rotation forms B_ij xʲ dxⁱ. These are homogeneous
of degree 0, 0 and 1 in x and, in [[eq:iii-a1-2-2]], of the types s0 (dt = ½(dx̄⁰ + dx̄¹)), s1
(dxⁱ = x̂_i dr + r dx̂_i = ½x̂_i(dx̄⁰ − dx̄¹) + r dx̂_i) and v1 (by [[def:iii-a1-1-7]]). A nonzero ρ^ι u of a single type
and degree is therefore one of these, with ι = 0, 0 and −1 respectively. ∎
