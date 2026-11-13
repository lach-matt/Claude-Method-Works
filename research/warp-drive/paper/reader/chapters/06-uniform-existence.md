## Uniform existence {#ch:uniform-existence}

This chapter proves the existence theorem on which the main theorem rests: given an approximate solution of high order
and Cauchy data close to it, the solution of the reduced equations exists on the fixed domain Ω for every small λ, and
its departure from the approximate solution obeys estimates uniform in λ. The proof turns on one decision. The
approximate solution is carried to high order K, so that the remainder is O(λ^K) and every nonlinear term is beaten by a
power of λ rather than by the size of the data. What then has to be uniform in λ is a linear estimate on the large
background. Its only coefficient of size 1/λ couples one scalar component of the remainder to the wave; that component's
own equation has no such coefficient; and the coupling is absorbed by a phase shift of the wave ([[lem:phase-shift]]).
This is the mechanism of [Tou23a, Section 3.2.3, p. 21], with a compactly supported mollifier adapted to the slices in
place of his Fourier cut-off.

Throughout, g0, L0 = ∂_τ − x̂·∂_x, ℓ = g0⁻¹dv = −L0 and □̃ := g0^(ab) ∂_a ∂_b (acting componentwise) are those of
[[prop:vaidya]], with the commutator identity [[eq:commutator]]. D and Ric^H are the gauge vector and the reduced Ricci
tensor of [[eq:gauge]], so that Ric^H(g) = −(1/2) g^(ab) ∂_a ∂_b g + Q(X; g)(∂g, ∂g), with second derivatives of g
entering only through the first term. The domain Ω of [[eq:omega]], its slices Σ_τ = A(τ) = {a ≤ |x| ≤ b(τ)}, the times
τ0 < τ_end and the properties (a)–(f) of Ω are those of [[lem:domain]]. Profiles f(X, θ) on Ω × S¹, their evaluations
[f](X) := f(X, v(X)/λ), their θ-means ⟨f⟩, the scaled norms |f|_j of [[eq:scaled-norm]] and the chain rule ∂_a [f] = λ⁻¹
(∂_a v) [∂_θ f] + [∂_a f] are those of [[sec:profiles]]. The number ε1, with 0 < ε1 < min(s0, μ0/a² − 1), is the one
fixed after [[lem:eigen]]: every g̃ with |g̃ − g0| ≤ ε1 on Ω is Lorentzian, satisfies the conclusions of [[lem:domain]]
(e), and has |g̃⁻¹| ≤ (s0 − ε1)⁻¹ ([[lem:lorentz-margin]]). All constants below depend on Ω and not on λ, and 0 < λ ≤ λ1
:= min(1, δ0)/10 ([[eq:lambda-one]]). The inequalities on the slices used below are the Sobolev and product bounds of
[[lem:sobolev]], the compactly supported mollifier 𝒫 adapted to the annuli with its properties (M1)–(M6)
([[lem:mollifier]]), the energy inequality [[eq:energy]] of [[lem:energy]] for −(1/2) g̃^(ab) ∂_a ∂_b u = f with |g̃ −
g0| ≤ ε1, and the transport estimate [[eq:transport]] of [[lem:transport]] along L0.

### The theorem {#sec:ue-theorem}

**Theorem {#thm:uniform-existence}** (Uniform existence.) Fix k = 6 and K ≥ 6. Let g_app be an approximant with N stages
of order K at regularity k ([[def:approximant]]): g_app is [[eq:approximant]], with profiles g_j bounded with all their
derivatives independently of λ, and it satisfies (E1)–(E3) there, (E3) with the constant C_R. Suppose moreover:

- (E4) *The data*: g is a Cauchy datum on Σ_τ0 for Ric^H(g) = 0 with w := g − g_app satisfying

      Data(w) := ‖w‖ + Σ_(1≤j≤k+1) λ^(j−1) ‖∂_x^j w‖ + Σ_(j≤k) λ^j ‖∂_x^j ∂_τ w‖ ≤ C_D λ^K   on Σ_τ0.

Then there are λ0 > 0 and M, depending on Ω, k, K, C_R, C_D and the bounds on the profiles but not on λ, such that for 0
< λ ≤ λ0 the solution g of Ric^H(g) = 0 with these data exists on Ω, is unique there among C² solutions with |g − g0| ≤
ε1 on Ω, is smooth if the data are, and

    w = h + φ [∂_θ g1],     with     𝒩(τ) ≤ M λ^K   on [τ0, τ_end],                                   {#eq:ue-remainder}

𝒩 the quantity [[eq:ue-energy]] (energies of h, of φ and of □̃φ to order k, scaled). In particular ‖w(τ)‖ + ‖∂w(τ)‖ ≤ M
λ^(K−1), |w| ≤ M λ^(K−3) and |∂w| ≤ M λ^(K−4) on Ω, and |g − g0| ≤ C λ, |∂g| ≤ C.

The proof occupies the rest of the chapter: the linear structure in [[sec:ue-linearisation]] and
[[sec:ue-decomposition]], the bootstrap in [[sec:ue-bootstrap]], existence, continuation and uniqueness in
[[sec:ue-existence]].

### The linearisation and its one large coefficient {#sec:ue-linearisation}

Let R = R_v be the two-scale operator of [[def:two-scale]], so that Ric^H([G]) = [R[G]] for a profile G; by
[[lem:phase-shift-symmetry]] (a) it satisfies the translation identity [[eq:phase-equivariance]], R[G(·, · + c)](X, θ) =
R[G](X, θ + c) for every constant c.

For the profile of g_app, R = λ⁻¹ R^(−1) + R^(0) + λ R^(1) + …, with R^(−1) = −(1/2) g0⁻¹(dv, dv) ∂_θ² g1 = 0.

Let P(w) := (d/ds) Ric^H(g_app + s w) at s = 0. Then

    P(w) = −(1/2) g_app^(ab) ∂_a ∂_b w + (1/2) λ⁻¹ s(w) [∂_θ² g1] + B·∂w + C·w,  s(w) := w(ℓ, ℓ), {#eq:ue-linearisation}

with B and C profiles (bounded with all X- and θ-derivatives; here C is a coefficient, not a constant). Indeed, expand
g_app⁻¹ to second order in the reduced equations. Second derivatives of g_app enter P only through (1/2) w^(ab) ∂_a ∂_b
g_app, where w^(ab) := g_app^(ac) g_app^(bd) w_cd, because second derivatives of g enter Ric^H(g) only through −(1/2)
g^(ab) ∂_a ∂_b g. By the chain rule ∂_a ∂_b [λ g1] = λ⁻¹ ∂_a v ∂_b v [∂_θ² g1] + O(1), and w^(ab) ∂_a v ∂_b v = w(ℓ_app,
ℓ_app) with

    ℓ_app := g_app⁻¹ dv = ℓ − λ ⟨g1⟩(ℓ, ·)^♯ + O(λ²),

by (E1): the oscillating part of g1 drops out of the O(λ) term, since (g1 − ⟨g1⟩)(ℓ, ·) = 0. So w(ℓ_app, ℓ_app) = s(w) +
O(λ)|w|, and that difference times λ⁻¹ goes into C. All other terms are linear in w or ∂w with coefficients built from
g_app and ∂g_app, which are bounded.

For a profile Y, P([Y]) = [λ⁻¹ T Y + P_0 Y], with

    T Y = −(ℓ_app·∂_X ∂_θ Y) − (1/2)(g_app^(ab) ∂_a ∂_b v) ∂_θ Y + B·(dv ⊗ ∂_θ Y)
          + (1/2) Y(ℓ, ℓ) ∂_θ² g1 − (1/2) n1 ∂_θ² Y,

where λ n1 := g_app⁻¹(dv, dv) = −λ ⟨g1⟩(ℓ, ℓ) + O(λ²) by (E1): the λ⁻² part of the principal term, −(1/2) λ⁻²
g_app⁻¹(dv, dv) ∂_θ² Y, is of size λ⁻¹ and is kept in T. The coefficient (1/2) λ⁻¹ s(w) [∂_θ² g1] is the only one of
size λ⁻¹, and it couples the single scalar s = w(ℓ, ℓ) to the wave. This is the five-dimensional form of the quasilinear
coupling described in [Tou23a, Section 3.2.2, p. 20].

**Lemma {#lem:phase-shift}** (The phase-shift identity.) Under (E2), T(∂_θ g1) = λ T1 with T1 a profile.

*Proof.* Differentiate [[eq:phase-equivariance]] for G the profile of g_app at c = 0: the linearisation of R at G in the
direction ∂_θ G equals ∂_θ R[G]. Now ∂_θ G = λ ∂_θ g1 + λ² ∂_θ g2 + …, and P([Y]) = [D_G R[Y]], so the left side is λ⁻¹
T(λ ∂_θ g1 + λ² ∂_θ g2 + …) + P_0(λ ∂_θ g1 + …) = T(∂_θ g1) + O(λ). The right side is ∂_θ(λ⁻¹ R^(−1) + R^(0)) + O(λ) =
O(λ), since R^(−1) = 0 and R^(0) = 0 by (E2). Both sides are expansions in powers of λ with profile coefficients, the
remainders λ times bounded profiles. ∎

A constant shift of the phase is a symmetry of the leading equation, so its generator ∂_θ g1 is annihilated by the λ⁻¹
part of the linearised operator. This one line is the analytic content of Touati's transport and polarization conditions
at first order.

### The decomposition and the regained derivative {#sec:ue-decomposition}

Write G1 := [∂_θ g1] and G2 := [∂_θ² g1]. By (E1), G1(ℓ, ·) = G2(ℓ, ·) = 0; differentiating g1(ℓ, ·) − ⟨g1⟩(ℓ, ·) = 0,
also (∂_X ∂_θ g1)(ℓ, ℓ) = 0, and (∂_X ∂_X ∂_θ g1)(ℓ, ℓ) is bounded.

**Lemma {#lem:ue-decomposition}** For φ(X) (independent of θ) and the metric g = g_app + w,

    −(1/2) g^(ab) ∂_a ∂_b (φ G1) + B·∂(φ G1) + C·(φ G1)
        = −λ⁻¹ (ℓ_app·∂φ) G2 + λ⁻¹ φ [T(∂_θ g1)] − (1/2)(□̃_app φ) G1 + B1·∂φ + C1 φ + 𝒬_φ,              {#eq:ue-phi-g1}

with □̃_app := g_app^(ab) ∂_a ∂_b, B1·∂φ and C1 φ with bounded profile coefficients, and 𝒬_φ collecting the terms with a
factor of w:

    |𝒬_φ| ≤ C |w| (λ⁻² |φ| + λ⁻¹ |∂φ| + |∂²φ|),

and likewise for derivatives, in scaled norms; the second derivatives ∂²φ in 𝒬_φ multiply G1 only.

*Proof.* Expand ∂_a ∂_b (φ G1) by the chain rule. The λ⁻² term carries g⁻¹(dv, dv) = g_app⁻¹(dv, dv) + O(|w|), whose
first part is λ n1 and belongs to φ T(∂_θ g1). The λ⁻¹ terms are the cross term −λ⁻¹ g^(ab) ∂_a φ ∂_b v G2, with g^(ab)
∂_b v = ℓ_app^a + O(|w|), and φ times the λ⁻¹ part of P(G1), which is φ T(∂_θ g1) by the definition of T. The second
derivatives of φ appear only as −(1/2) g^(ab) ∂_a ∂_b φ G1 = −(1/2)(□̃_app φ) G1 + (a term with a factor w, multiplying
G1). The rest has bounded coefficients. ∎

Let s := s(w) and define φ by the transport

    L0 φ = −(1/2) 𝒫 s,      φ = 0 on Σ_τ0,                                                            {#eq:ue-transport}

that is ℓ·∂φ = (1/2) 𝒫 s. It exists on Ω, because the integral curves of L0 followed to the past stay in Ω and meet Σ_τ0
([[lem:domain]] (d)). Put h := w − φ G1. Then s(h) = s(w) = s, since G1(ℓ, ℓ) = 0. Write F := −Ric^H(g_app) and 𝒬(w) for
the terms of Ric^H(g_app + w) of second and higher order in (w, ∂w) other than the principal part. The equation
Ric^H(g_app + w) = 0 reads −(1/2) g^(ab) ∂_a ∂_b w + (1/2) λ⁻¹ s G2 + B·∂w + C·w = F + 𝒬(w), and by [[eq:ue-phi-g1]],
[[eq:ue-transport]] and [[lem:phase-shift]] it becomes

    −(1/2) g^(ab) ∂_a ∂_b h + B·∂h + C·h = F + 𝒬(w) − 𝒬_φ − (1/2) λ⁻¹ ((1 − 𝒫) s) G2
          + λ⁻¹ ((ℓ_app − ℓ)·∂φ) G2 − φ [T1] + (1/2)(□̃_app φ) G1 − B1·∂φ − C1 φ.                         {#eq:ue-h}

Indeed, the λ⁻¹ terms of [[eq:ue-phi-g1]] are −λ⁻¹ (ℓ_app·∂φ) G2 = −λ⁻¹ (ℓ·∂φ) G2 − λ⁻¹ ((ℓ_app − ℓ)·∂φ) G2 = −(1/2) λ⁻¹
(𝒫 s) G2 − λ⁻¹ ((ℓ_app − ℓ)·∂φ) G2 and λ⁻¹ φ [T(∂_θ g1)] = φ [T1]; subtracting from the equation for w leaves (1/2) λ⁻¹
s G2 − (1/2) λ⁻¹ (𝒫 s) G2 = (1/2) λ⁻¹ ((1 − 𝒫) s) G2 on the left, which is moved to the right.

Every coefficient on the right of [[eq:ue-h]] is a bounded profile. The one coefficient of size 1/λ left multiplies (1 −
𝒫) s, which is O(λ ∂s) by (M3), and |ℓ_app − ℓ| ≤ C λ. Two things remain: □̃_app φ has two derivatives of φ, and φ is
driven by s.

**Lemma {#lem:ell-ell}** (The ℓℓ component.) The component s satisfies

    □̃ s = c1·∂h + c0·h + c2·∂φ + c3 φ − 2q F(ℓ, ℓ) − 2q 𝒬(w)(ℓ, ℓ) + 2q 𝒬_φ(ℓ, ℓ) + Σ_(b,i) c^(bi) ∂_b ∂_i h,

where c0, …, c3 are bounded coefficients (profiles, and profiles times the function q of the proof, which depends on w
and so is not a profile; the terms 2 g0^(ab) ∂_a(ℓ ⊗ ℓ)·∂_b h and h·□̃(ℓ ⊗ ℓ) carry no q), the sum runs over pairs with
i spatial, |c^(bi)| ≤ C(λ + |w|) and |∂c^(bi)| ≤ C(1 + |∂w|), and 𝒬_φ(ℓ, ℓ) contains no second derivative of φ. There is
no coefficient of size 1/λ.

*Proof.* □̃ s = (□̃ h)(ℓ, ℓ) + 2 g0^(ab) ∂_a(ℓ ⊗ ℓ)·∂_b h + h·□̃(ℓ ⊗ ℓ). Write g0^(ab) ∂_a ∂_b = q g^(ab) ∂_a ∂_b + Σ
c^(bi) ∂_b ∂_i with q := g0^(ττ)/g^(ττ); here g^(ττ) ≠ 0, since the slices stay spacelike for g ([[lem:domain]] (e)),
and c^(bi) = O(|g⁻¹ − g0⁻¹|) = O(λ + |w|). Contract [[eq:ue-h]] with ℓ ⊗ ℓ: G2(ℓ, ℓ) = G1(ℓ, ℓ) = 0 removes the 1/λ
terms and the □̃_app φ term exactly; B1·∂φ and C1 φ stay of first order; the second derivatives of φ in 𝒬_φ multiply G1
and also drop. ∎

**Lemma {#lem:commutator-transport}** (The commutator transport.) Ψ := □̃ φ satisfies

    L0 Ψ − (2/r) Ψ = −(1/2) □̃ 𝒫 s − (1/r)(∂_τ + ∂_r) 𝒫 s − (3/r²) ∂_r φ,                                 {#eq:ue-psi}

and □̃_app φ = Ψ + c^(ab) ∂_a ∂_b φ with |c| ≤ C λ. Every second derivative of φ is a combination, with bounded
coefficients, of L0 𝒫 s, ∂_x 𝒫 s, ∂φ and the spatial Hessian ∂_x² φ, which satisfies the transport

    L0(∂_x² φ) = −(1/2) ∂_x² 𝒫 s + (∂_x x̂) * ∂_x² φ + (∂_x² x̂) * ∂_x φ,

where * denotes contractions with bounded coefficients.

*Proof.* Apply [[eq:commutator]] to φ: L0 Ψ = □̃ L0 φ + (2/r)(Ψ + (∂_τ + ∂_r) L0 φ) − (3/r²) ∂_r φ, and substitute L0 φ
= −(1/2) 𝒫 s. Next, g_app⁻¹ − g0⁻¹ = O(λ) gives □̃_app φ − Ψ = c^(ab) ∂_a ∂_b φ with |c| ≤ C λ. For the second
derivatives, ∂_τ = L0 + x̂·∂_x, L0 L0 φ = −(1/2) L0 𝒫 s and L0 ∂_i φ = ∂_i L0 φ + (∂_i x̂^m) ∂_m φ; the commutator [L0,
∂_i] = (∂_i x̂^m) ∂_m involves spatial derivatives only, since the ∂_τ coefficient of L0 is the constant 1. Applying ∂_i
∂_j to L0 φ = −(1/2) 𝒫 s and commuting gives the transport of ∂_x² φ. ∎

### The energy and the bootstrap {#sec:ue-bootstrap}

On [τ0, τ] (wherever the solution exists) put

    𝒩(τ) := Σ_(j≤k) λ^j ( ‖∂^j ∂h‖ + ‖∂^j Ψ‖ + ‖∂^j ∂φ‖ + λ ‖∂^j ∂_x² φ‖ ) + ‖h‖ + ‖φ‖.                  {#eq:ue-energy}

*Proof of [[thm:uniform-existence]].* The proof is in eight steps; the first seven are an a priori bound, the eighth
gives existence.

**Step 1** (what 𝒩 controls). |w|_(k+1) ≤ C 𝒩. Indeed w = h + φ G1. For h, ‖h‖ ≤ 𝒩 and, for 1 ≤ i ≤ k + 1, λ^i ‖∂^i h‖ ≤
λ · λ^(i−1) ‖∂^(i−1) ∂h‖ ≤ 𝒩. For φ G1, the Leibniz rule writes λ^j ∂^j (φ G1) as a sum of λ^i ∂^i φ · λ^(j−i) ∂^(j−i)
G1, and λ^(j−i) |∂^(j−i) G1| ≤ C by the chain rule (each derivative of the evaluation costs at most λ⁻¹); moreover ‖φ‖ ≤
𝒩 and λ^i ‖∂^i φ‖ = λ · λ^(i−1) ‖∂^(i−1) ∂φ‖ ≤ λ 𝒩 for 1 ≤ i ≤ k + 1. Hence, by the Sobolev bound ‖∂^i f‖_(L^∞) ≤ C
λ^(−3−i) |f|_(i+3) of [[eq:sobolev]], ‖∂^i w‖_(L^∞) ≤ C λ^(−3−i) 𝒩 for i ≤ 4, and |∂w|_k ≤ λ⁻¹ |w|_(k+1) ≤ C λ⁻¹ 𝒩.

**Step 2** (data). φ = 0 on Σ_τ0, so h = w there. The derivatives of h, φ and Ψ on Σ_τ0 of order up to k + 1 in τ are
fixed by [[eq:ue-transport]], [[eq:ue-h]] and the equation for w, whose coefficients obey the scaled bounds of the chain
rule; solving for ∂_τ² by induction gives 𝒩(τ0) ≤ C (Data(w) + C_R λ^K) ≤ C (C_D + C_R) λ^K. (On Σ_τ0, ∂_τ φ = −(1/2) 𝒫
s, and ∂_x 𝒫 s = 𝒫 ∂_x s + O(λ) 𝒫 ∂_x s by (M4): no 1/λ enters.)

**Step 3** (the bootstrap). Suppose 𝒩 ≤ 2 M λ^K on [τ0, τ*], with M to be fixed. Then by Step 1 |w| ≤ C M λ^(K−3) and
|∂w| ≤ C M λ^(K−4) ≤ C M λ², so for λ ≤ λ0(M) the metric g = g_app + w satisfies |g − g0| ≤ ε1 (so that the domain lemma
and the energy inequality apply to it) and |∂g| ≤ M1 with M1 independent of M.

**Step 4** (h). Apply ∂^α, |α| = j ≤ k, to [[eq:ue-h]], apply the energy inequality to each component, and multiply by
λ^j. The commutator [∂^α, g^(ab)] ∂_a ∂_b h has terms ∂^i g · ∂^(j−i+1) ∂h with i ≥ 1. With ‖∂^i g_app‖_∞ ≤ C λ^(1−i),
λ^j times each is at most C λ^(j−i+1) ‖∂^(j−i+1) ∂h‖ ≤ C 𝒩; the w part is at most C M λ^(K−4) 𝒩 (for i ≤ 4 with ∂^i w in
L^∞; for i ≥ 5 with ∂^i w in L² and the other factor in L^∞ by the Sobolev bound). The right side of [[eq:ue-h]]:

- λ^j ‖∂^α F‖ ≤ C_R λ^K by (E3);
- B·∂h and C·h give C 𝒩 (profile coefficients cost λ⁻¹ per derivative, compensated by the weights);
- the term λ⁻¹ ((1 − 𝒫) s) G2 gives Σ_i λ^(i−1) ‖∂^i (1 − 𝒫) s‖ ≤ C Σ_i λ^i ‖∂^i ∂s‖ ≤ C 𝒩 by (M3), (M4), (M6);
- λ⁻¹ ((ℓ_app − ℓ)·∂φ) G2 and φ [T1] give C 𝒩;
- (1/2)(□̃_app φ) G1 = (1/2) Ψ G1 + (1/2)(c ∂²φ) G1 with |c| ≤ C λ, and by [[lem:commutator-transport]] λ ∂²φ is
  controlled by λ L0 𝒫 s, λ ∂_x 𝒫 s, λ ∂φ and λ ∂_x² φ, each at most C 𝒩 at every level j ≤ k (no Bernstein inequality
  is needed: λ^(j+1) ‖∂^j L0 𝒫 s‖ ≤ C λ^(j+1) ‖∂^j ∂s‖ by (M4), (M6));
- B1·∂φ and C1 φ give C 𝒩;
- the nonlinear terms 𝒬(w) and 𝒬_φ are at most C λ⁻⁵ 𝒩² + C λ⁻³ 𝒩² by the product bound and Step 1 (the worst is
  quadratic in ∂w: |∂w ∂w|_k ≤ C λ⁻³ |∂w|_k² ≤ C λ⁻⁵ 𝒩²), hence at most C M² λ^(2K−5) ≤ C M² λ^(K+1), as K ≥ 6.

So

    Σ_(j≤k) λ^j ‖∂^j ∂h(τ)‖ + ‖h(τ)‖ ≤ C ( 𝒩(τ0) + ∫_(τ0)^(τ) (𝒩 + C_R λ^K + C M² λ^(K+1)) ).

**Step 5** (φ). Apply ∂^α to [[eq:ue-transport]]: L0 ∂^α φ = −(1/2) ∂^α 𝒫 s + [L0, ∂^α] φ, where [L0, ∂^α] has smooth
λ-independent coefficients and involves derivatives of φ of lower or equal order; λ^j ‖∂^α 𝒫 s‖ ≤ C Σ_(i≤j) λ^i ‖∂^i s‖
≤ C 𝒩 by (M1), (M4), (M6). The same holds for ∂φ (with ∂𝒫 s ≤ C 𝒫 ∂s). For λ ∂_x² φ use the transport of
[[lem:commutator-transport]]: λ^(j+1) ‖∂^α ∂_x² 𝒫 s‖ = λ^(j+1) ‖∂_x 𝒫(∂^α ∂_x s)‖ + (commutators) ≤ C λ^j ‖∂^j ∂s‖, by
the Bernstein bound (M2) in the one spatial derivative. The transport estimate then bounds the φ-part of 𝒩(τ) by C
(𝒩(τ0) + ∫_(τ0)^(τ) 𝒩) (∂_τ φ does not vanish on Σ_τ0).

**Step 6** (Ψ). Apply ∂^α to [[eq:ue-psi]] and the transport estimate (with c = 2/r ≤ 2/a). Write □̃ 𝒫 s = 𝒫 □̃ s + [□̃,
𝒫] s. By [[lem:ell-ell]], □̃ s is of first order in (h, φ) up to F, the nonlinear terms and Σ c^(bi) ∂_b ∂_i h. For the
last, 𝒫(c ∂_b ∂_i h) = 𝒫 ∂_i(c ∂_b h) − 𝒫((∂_i c) ∂_b h) and ‖𝒫 ∂_i f‖ ≤ C λ⁻¹ ‖f‖ by (M2), (M4), with |c| ≤ C(λ + |w|):
at most C ‖∂h‖ at level 0, and at level j

    λ^j ‖∂^α 𝒫 ∂_i (c ∂h)‖ ≤ C λ^(j−1) Σ_i ‖∂^i c‖_∞ ‖∂^(j−i) ∂h‖ ≤ C 𝒩,

since ‖∂^i c‖_∞ ≤ C λ^(1−i) (for the w-part of c only for i ≤ 4; for i ≥ 5 its ∂^i w is in L² and the other factor in
L^∞ by the Sobolev bound, as in Step 4; the restriction to i ≤ 4 applies likewise to c0, …, c3 through q). For the
commutator, [g0^(ab), 𝒫] ∂_a ∂_b s with at least one spatial index is bounded by C ‖∂s‖ by (M5). The ττ term is
rewritten with

    ∂_τ² s = (□̃ s − 2 g0^(τi) ∂_τ ∂_i s − g0^(ij) ∂_i ∂_j s)/g0^(ττ),      g0^(ττ) = −1 − μ/r²,

after which (M5) applies to the spatial terms. In □̃ s ([[lem:ell-ell]]) the first-order terms gain the factor λ of
(M5)'s second form, and the terms c^(bi) ∂_b ∂_i h are written ∂_i(c ∂_b h) − (∂_i c) ∂_b h, so that (M5)'s first form
bounds them by C ‖c ∂h‖ + C ‖∂c‖_∞ ‖∂h‖ ≤ C 𝒩 (at level j likewise; applying the second form to them would cost a
derivative at j = k). The terms of g0^(ab)(∂_a ∂_b 𝒫 − 𝒫 ∂_a ∂_b) s carry, by (M4) and (M6), a factor λ and a spatial
derivative inside 𝒫, so they are at most C ‖∂s‖ by (M4); likewise at level j. The other terms of [[eq:ue-psi]] are of
first order in 𝒫 s and φ. So the Ψ-part of 𝒩(τ) is at most C (𝒩(τ0) + ∫ (𝒩 + C_R λ^K + C M² λ^(K+1))).

**Step 7** (closing). Steps 4–6 give

    𝒩(τ) ≤ C2 ( 𝒩(τ0) + ∫_(τ0)^(τ) 𝒩 + (τ_end − τ0)(C_R λ^K + C M² λ^(K+1)) ),

with C2 independent of M and λ. Gronwall's lemma and Step 2 give 𝒩(τ) ≤ C3 ((C_D + 1 + C_R) λ^K + C M² λ^(K+1)), with C3
:= C2 e^(C2 (τ_end − τ0)) (1 + τ_end − τ0) C. Take M := C3 (C_D + 1 + C_R) + 1 and λ0 so small that C3 C M² λ0 ≤ 1 and
Step 3 holds. Then 𝒩 ≤ (M − 1) λ^K + λ^K = M λ^K < 2 M λ^K on [τ0, τ*], which improves the bootstrap assumption. 𝒩 is
continuous in τ for a smooth solution, so the set of τ* for which the assumption holds is open and closed in the
interval of existence.

### Existence, continuation and uniqueness {#sec:ue-existence}

**Step 8** (existence and continuation). The local theory needs the time lines timelike as well as the slices spacelike.
[AO14, Theorem 1.1, p. 2] ([[thm:std-ao-existence]]), for the divergence-form equation ∂_μ(A^(μν)(U) ∂_ν U) = F on
[0, T] × R^n, asks in its hypothesis (1.3) that (1/γ)|ξ|² ≤ A^(ij) ξ_i ξ_j ≤ γ|ξ|² and A^(00) ≤ −κ for all (U, ξ),
with constants γ, κ > 0; and in the first-order form the eigenvalue 0
of the symbol meets a characteristic speed wherever g^(ij) ξ_i ξ_j = 0, against [DS23, (A4)], which asks that the
distinct eigenvalues of the symbol never meet. In the coordinates (τ, x) this fails on part of Ω: g0^(ij) ξ_i ξ_j = |ξ|²
− (μ/r²)(x̂·ξ)² < 0 for radial ξ where r² < μ, and Ω reaches r = a < √μ0. So the local theorems are applied in other
coordinates, in four steps. The results used are the following.

- [DS23, Theorem 2.4]: for a system ∂_t u + A^i(t, x, u) ∂_i u = R(t, x, u) on the torus T^n, with A^i and R smooth and
  bounded with their derivatives uniformly in t (their (A1)–(A2)), A^i(t, x, u) ξ_i diagonalizable with real eigenvalues
  (A3) whose distinct values do not meet each other (A4), and r > n/2 + 1: for every u0 ∈ H^r whose values stay at
  positive distance from the boundary of the admissible set of states, there is T > 0, depending on ‖u0‖_r and that
  distance, such that the system has a unique solution u ∈ C([−T, T]; C¹) ∩ C¹([−T, T]; C⁰).
- [DS23, Theorem 2.6]: for the maximal solution, exactly one of the following holds: it exists for all time; its values
  approach the boundary of the admissible set of states; its norm in C([0, T]; C¹) ∩ C¹([0, T]; C⁰) is unbounded as T
  tends to the maximal time.
- [LY22, Theorem 26]: a bounded smooth domain in R^n has an extension operator E, one operator, bounded from W^(m,p) of
  the domain to compactly supported W^(m,p) functions on a neighbourhood, for every m and 0 < p ≤ ∞; it maps smooth
  functions to smooth functions. [LY22, Lemma 27] ([[thm:std-ly-extension]]): for χ ∈ C_c^∞(R^n) and a
  bijection Φ of R^n whose derivatives of positive order and those of its inverse are bounded, f ↦ (χ f) ∘ Φ is
  bounded on every W^(m,p)(R^n).
- [SY21, Sections 1 and 2.1]: a bounded Lipschitz domain in R^n has a universal extension operator (Stein's, or
  Rychkov's), one operator bounded from W^(m,p) of the domain to W^(m,p)(R^n) for every m and every 1 ≤ p ≤ ∞.

(i) *The coefficients.* On Ω the system for w is Ric^H(g_app + w) = 0, relative to g0, and the profiles of g_app are
defined on Ω × S¹. Extend them to R⁵ × S¹ by one universal extension operator acting in X, the same for every order
(Stein's or Rychkov's, for the bounded Lipschitz domain Ω, a convex polygon in (τ, r) times S³ [SY21, Sections 1, 2.1]):
g_app extends smoothly with bounded derivatives of every order, for all τ, and is unchanged on Ω. Outside a
neighbourhood U of Ω, replace g_app and g0 by g_ext and g0_ext, obtained by interpolating lapse, shift and spatial
metric (relative to τ) convexly to (1, 0, δ) on {r ≤ a/4} and on {r ≥ R2 + 1}, R2 := b(τ0) + 1. Every such combination
is a Lorentzian metric with each Σ_τ spacelike: a convex combination of positive lapses is positive and a convex
combination of positive definite spatial metrics is positive definite, and a metric −ν² dτ² + γ_ij (dx^i + β^i
dτ)(dx^j + β^j dτ) with ν > 0 and γ positive definite is Lorentzian with dτ timelike. So the system keeps its form, with
coefficients smooth in X and equal to Minkowski's outside a compact set in x; on U nothing changes.

(ii) *The coordinates.* Write g_ext = −ν² dτ² + γ_ij (dx^i + β^i dτ)(dx^j + β^j dτ), with lapse ν ≥ ν_min > 0, shift
β_ext = β^i ∂_i and spatial metric γ. Put Z := ∂_τ − β_ext. Then Z(τ) = 1 and, since dx^i(Z) + β^i dτ(Z) = −β^i + β^i =
0,

    g_ext(Z, Z) = −ν² ≤ −ν_min² < 0;

and Z = ∂_τ outside a compact set. Put X = (τ, Φ_Z(τ, y)), Φ_Z the flow of Z from τ0. The slices are unchanged and ∂_τ
at fixed y is Z. For a vector Y tangent to a slice, g_ext(Z, Y) = g_ext(∂_τ, Y) − γ(β, Y) = γ(β, Y) − γ(β, Y) = 0,
because g_ext(∂_τ, ∂_i) = γ_ij β^j. So in (τ, y) the metric g_ext has zero shift, g_ext = −ν² dτ² + γ̃_ab dy^a dy^b with
γ̃ the spatial metric in the coordinates y, and its inverse has g_ext^(00) = −ν⁻², g_ext^(0a) = 0 and g_ext^(ab) =
γ̃^(ab), the inverse spatial metric, uniformly positive definite. Only the independent variables change: the unknowns
stay the Cartesian arrays of the coordinates (τ, x), the principal part stays −(1/2) g^(ab) ∂_a ∂_b with g^(ab)
transformed as a tensor, and the system stays quasilinear with coefficients smooth in (τ, y).

(iii) *The cut-off.* Let χ be a smooth map of the components, the identity on |w| ≤ ε2/2 and with values in |w| ≤ ε2,
with ε2 so small that every metric within ε2 of g_ext keeps the conditions g^(00) ≤ −c_0 and g^(ab) ξ_a ξ_b ≥ c_0 |ξ|²
with a fixed constant c_0 > 0 in (τ, y). Put χ(w) for w in the coefficients and lower-order terms. The modified system
agrees with the original where |w| ≤ ε2/2, which holds on Ω (|w| ≤ C M λ^(K−3), Step 3). The coefficients and the
forcing term are taken at time τ̄(τ), τ̄ smooth, equal to τ on [τ0 − 1, τ_end + 1] and constant outside [τ0 − 2, τ_end +
2]: the coordinates of (ii) degenerate as |τ| grows (the flow lines of Z pile up where β_ext vanishes), and [DS23, (A1)]
asks for bounds uniform in t; on [τ0, τ_end] nothing changes. The coefficients and the forcing term equal Minkowski's
outside a compact set in y, so the system is posed on a torus T⁴_L of large period L.

Write the modified system as −(1/2) g^(μν) ∂_μ ∂_ν w = F̃(τ, y, w, ∂w), with μ, ν running over (τ, y) and a, b, c below
over y alone. In V := (w, u_0, u_a), with u_0 := ∂_τ w and u_a := ∂_(y^a) w, it is the first-order system

    ∂_τ w = u_0,
    −g^(00) ∂_τ u_0 − 2 g^(0a) ∂_a u_0 − g^(ab) ∂_a u_b = 2 F̃(τ, y, w, u),
    g^(ab) ∂_τ u_b − g^(ab) ∂_b u_0 = 0,

the second line being the equation with the first derivatives of w replaced by (u_0, u_b). Its coefficient of ∂_τ is A⁰
= diag(1, −g^(00), g^(ab)) (acting on each of the fifteen components of w), symmetric and positive definite, and its
coefficient of ∂_c is

    A^c = [[0, 0, 0], [0, −2 g^(0c), −g^(cb)], [0, −g^(ac), 0]]

in the blocks (w, u_0, u_b), symmetric. So the system is symmetric hyperbolic. Its eigenvalues ζ, defined by A^c ξ_c V =
ζ A⁰ V for ξ ≠ 0, are as follows. If ζ ≠ 0, the last rows give u_b = −(ξ_b/ζ) u_0, the first gives w = 0, and the second
gives

    g^(00) ζ² − 2 g^(0c) ξ_c ζ + g^(ab) ξ_a ξ_b = 0,

whose two roots ζ_− < 0 < ζ_+ are real with product g^(ab) ξ_a ξ_b/g^(00) < 0. If ζ = 0, then u_0 = 0 and g^(ab) ξ_a u_b
= 0, with w free: a space of dimension four for each component. So (A⁰)⁻¹ A^c ξ_c is diagonalizable with the real
eigenvalues ζ_− < 0 < ζ_+ and 0, which never meet; ζ_± are simple roots of a quadratic with smooth coefficients and 0 is
constant, so all three are smooth in (τ, y, V, ξ) for ξ ≠ 0, as (A4) of [DS23] ([[thm:std-ds-existence]]) also requires,
and the system satisfies (A1)–(A4) of [DS23] on all of the state space, the cut-off keeping the coefficients defined for
every value of w. The relation u_a = ∂_a w propagates, since ∂_τ(u_a − ∂_a w) = ∂_a(u_0 − ∂_τ w) = 0.

(iv) *The restarts.* At τ_i extend the data from Σ_(τ_i) ∩ Ω = A(τ_i), in x, by the universal Seeley-type operator of
[LY22, Theorem 26] for the smooth annulus (one operator bounded on every H^m, so smooth data extend to smooth data), cut
off, and compose with Φ_Z(τ_i, ·) to pass to y. The constants are uniform in τ, the annuli being images of a fixed one
under radial diffeomorphisms with bounded derivatives: [LY22, Lemma 27] states the composition bounded, and its proof,
by the chain and product rules and a change of variables, gives a bound through finitely many derivatives of the
diffeomorphism and its inverse. [DS23, Theorem 2.4] with r = k > 4/2 + 1 (k = 6) gives a solution on [τ_i, τ_i + δ], δ
depending only on the norm of the data, which Steps 1 and 7 bound for each fixed λ (|w|_(k+1) ≤ C 𝒩 ≤ C M λ^K). The data
are smooth; by [DS23, Theorem 2.6] at every r ≥ k, the solution with data in H^r continues as long as its C¹ norm stays
bounded, so it lies in every H^r on the same interval, and it is smooth. On Ω ∩ {τ_i ≤ τ ≤ τ_i + δ} it solves the
original system while |w| ≤ ε2/2.

It is the only C² solution there with the data on Σ_(τ_i) ∩ Ω and |g − g0| ≤ ε1, the class in which the energy
inequality applies; the solution here is in it by Step 3, and so is its image under an isometry of g0, which fixes g0
and acts on Cartesian arrays by an orthogonal matrix. For let g_(1) := g_app + w1 and g_(2) := g_app + w2 be two such.
Then

    −(1/2) g_(1)^(ab) ∂_a ∂_b (w1 − w2) = (1/2)(g_(1)^(ab) − g_(2)^(ab)) ∂_a ∂_b w2 + F(X, w1, ∂w1) − F(X, w2, ∂w2) =: f,

where F(X, w, ∂w) := −Ric^H(g_app + w) − (1/2) g^(ab) ∂_a ∂_b w, g = g_app + w, contains no second derivative of w (and
F(X, 0, 0) = F). Then ‖f‖ ≤ C (‖w1 − w2‖ + ‖∂(w1 − w2)‖), because ∂²w2 is bounded and |g_(i)⁻¹| ≤ (s0 − ε1)⁻¹. The
energy inequality from τ_i and Gronwall's lemma give w1 = w2. This is the finite speed of propagation the proof uses,
obtained from the energy inequality with no further input, and the same argument, run from τ0 over all of Ω, gives the
uniqueness stated in the theorem. With Step 7 the bootstrap continues, so the solution exists on all of Ω with
[[eq:ue-remainder]].

Finally the bounds after [[eq:ue-remainder]]. By Step 1, |w|_(k+1) ≤ C 𝒩 ≤ C M λ^K, so ‖w‖ ≤ C M λ^K and ‖∂w‖ ≤ λ⁻¹
|w|_(k+1) ≤ C M λ^(K−1); |w| ≤ C λ⁻³ 𝒩 ≤ C M λ^(K−3) and |∂w| ≤ C λ⁻⁴ 𝒩 ≤ C M λ^(K−4) (M renamed to absorb C). Then |g −
g0| ≤ |λ [g1] + Σ_(j≥2) λ^j [g_j]| + |w| ≤ C λ, and |∂g| ≤ |∂g_app| + |∂w| ≤ C, since ∂[λ g1] = dv ⊗ [∂_θ g1] + λ [∂_X
g1] is bounded. ∎

### The theorem at every order {#sec:ue-every-order}

The proof fixes k = 6. Some uses of the theorem need the remainder small in H^d for a large d.

**Remark {#rem:ue-every-order}** [[thm:uniform-existence]] holds at every order k ≥ 6 with K ≥ 6: with 𝒩_k the quantity
[[eq:ue-energy]] at order k, 𝒩_k(τ) ≤ M_k λ^K on [τ0, τ_end], given (E3) and (E4) at order k. The inputs hold at every
order for the approximant of [[thm:approximant]] with the data of [[thm:data]], and the remainder is O(λ) in H^d once k
≥ d and K ≥ d + 1.

*Proof.* (a) *Where k = 6 enters.* Step 1: the scaled Sobolev bound ‖∂^i w‖_∞ ≤ C λ^(−3−i) 𝒩 needs i + 3 ≤ k + 1, so i ≤
4 at k = 6 and i ≤ k − 2 in general. Step 4: the commutator terms ∂^i g · ∂^(j−i+1) ∂h are split with ∂^i w in L^∞ for i
≤ 4 and in L² for i ≥ 5, the other factor then of order j − i + 1 ≤ 2 in L^∞; at order k the split is at k − 2, the L^∞
factor needing at most 2 + 1 + 3 ≤ k + 1 derivatives of 𝒩's quantities. The nonlinear terms use |∂w ∂w|_k ≤ C λ⁻³
|∂w|_k², the scaled product bound in four space dimensions, valid at every k ≥ 3 with C = C_k. Step 8: [DS23, Theorem
2.4] with r = k > 4/2 + 1. Steps 2, 5, 6 and 7 do not use k = 6.

(b) *The closing.* The bootstrap closes when 2K − 5 ≥ K + 1 (Step 4's C M² λ^(2K−5) ≤ C M² λ^(K+1)), that is when K ≥ 6,
whatever k is; the constants C, C2, M and λ0 then depend on k. So 𝒩_k(τ) ≤ M_k λ^K on [τ0, τ_end], given (E3) and (E4)
at order k.

(c) *The inputs at order k.* (E3) at order k: the residual of the approximant of [[thm:approximant]] is λ^N times a
profile bounded with all its derivatives ([[sec:approximant]]), so |Ric^H(g_app)|_k ≤ C_k λ^N for every k: the
approximant of [[thm:approximant]] is of order N − 1 at every regularity k. (E4) at order k: [[prop:exact-correction]]
bounds the correction at every order, sup_r ‖∂_r^j U(r)‖_(H^s(S³)) ≤ C_(j,s) λ^(N−2−j), with λ0 independent of the
order, so Data(w) at order k is O(λ^(N−3)) = O(λ^K) with N = K + 3, as in the proof of [[thm:data]].

(d) *Unscaled norms.* 𝒩_k ≤ M_k λ^K gives ‖∂^j ∂h‖ ≤ M_k λ^(K−j) for j ≤ k, and likewise for φ G1 by Step 1, so the
remainder is O(λ) in H^d once k ≥ d and K ≥ d + 1. ∎
