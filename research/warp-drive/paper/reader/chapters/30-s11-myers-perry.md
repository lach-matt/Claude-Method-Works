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
