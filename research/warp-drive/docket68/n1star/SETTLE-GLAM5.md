# SETTLE-GLAM5 -- Theorem 4 (ii) on g_λ's own data

Status: written; not yet read by an independent verifier. Labels: **computed** (a program of `checks/` with its `.out`
and a negative control that fails as it must), **deduced** (an argument written here), **read** (a statement of this
repository quoted with file and line; no outside source is quoted, so nothing here is READ at source).
Programs: `checks/tail5.py` (T1-T9), `checks/wedge5.py` (W1-W6).

## 0. The question and the answer

The paper's section 9 ("Beyond the boundary", RESPONSE-HL-5D.md:1463-1482) says that Theorem 4 is not shown to apply
to g_λ's own data. The task: prove that the maximal vacuum development of g_λ's own data settles to a Tangherlini
metric by Theorem 4 (ii), in III.K's own class as Part VII fixes it, ℰ_0 = {(j, 0) : j ≥ 2} and ℓ0 ∈ (3, 4)
(PART-VII-ASSEMBLY.md:45-46), with no gluing; otherwise say exactly what fails.

**Answer: it cannot be done in that class, and not only because the scattering estimate is missing.**

- **(A) A half-order tail** (deduced, Proposition 3.1; computed, `tail5.py` T1, T7-T9). After the shell, g_λ − g0
  carries at past null infinity a constant coefficient G_5^∞ of r^(−5/2):
  G_5^∞ = A a_1(λ) + A³ a_3(λ), with a_1 = ½(Δ̊ − ¾)[λ h (T_F Im ê(1/λ) + T_G Re ê(1/λ))] explicit (ê the
  Fourier transform of the envelope, T_F, T_G the two polarizations of (2.5′)). Both a_1 and a_3 are O(λ^∞).
  Its spatial part vanishes identically in λ for at most one amplitude A*, otherwise only on a discrete set of λ.
- **(B) It reaches Hintz's initial surface** (deduced, Proposition 4.1 and Corollary 4.2, conditional on the
  continuation's existence and expansion; computed, T2-T6). A nonzero G_5^∞ puts a term ρ^(5/2) a(ω), a ≠ 0, into
  g_λ's data at spatial infinity, and a term ρ^(9/2) into the electric curvature there. ρ^(5/2) lies outside
  H_b^(∞,(ℰ_0, ℓ0)) for every ℓ0 > 5/2, so ‖·‖_(d_1) = ∞ in Part VII's sense: **g_λ's own data are not in Part VII's
  class**, off the exceptional set of (A). The failure is beyond all orders in λ: the approximant sees G_5^∞ = 0 at
  every order (Remark 3.2).
- **(C) The class that admits it** is BEYOND5's D517 ℰ_0^½ = {(2 + j/2, 0) : j ∈ ℕ_0}, which VI.C's row d1 admits
  (read, BEYOND5.md:229-244). Theorem 4 (ii) run with ℰ_0^½ is a modification of Part VII's run, deduced there to
  move little, its log orders at the half-integers not computed.
- **(D) The continuation** (deduced, Lemma 5.1; computed, `wedge5.py`). The linear scattering estimate on the wedge
  W holds, in the record's own gauge, by a weighted energy identity whose bulk term has the good sign. The nonlinear
  estimate on W, the expansion at spatial infinity and the λ-uniformity of the remainder's expansion at past null
  infinity are not done (section 6).

So nothing below proves settling of g_λ's own continuation. What is established is where the stated route breaks,
why, by how much, and what the route through ℰ_0^½ still needs.

## 1. The late slice (the plan's step 1)

*Read.* Part VII Lemma 1.2 (PART-VII-ASSEMBLY.md:140-158) places Σ_IVP ∩ {r_0 ≤ r ≤ 4R} in the interior of
Ω′_+ = Ω′ ∩ {v ≥ v_end + 1}, its c_0 chosen so that "τ ≥ τ_0 + 1 and v = τ + r ≥ v_end + 2 there" (151). Beyond
R_3, Σ_IVP = {t_KS = f(|x|)} with f′ ∈ |x|^(−2) C^∞ (162-163, 175-177).

*Deduced.* So v = f(r) + r + const increases to ∞ along the far part, and Σ_IVP ∩ {r ≥ r_0} ⊂ {v ≥ v_end + 2}: the
whole slice outside r_0 is after the shell. No later slice is needed.

*Read.* Part VII Lemma 1.1 (104-138): on {v > v_end} every oscillating profile vanishes, g_app = g0 + Σ_(j=1)^N λ^j m_j
with g0 = g^KS_(μ_end,0) and m_j smooth and independent of λ; with K = J + 4, |∂^j(g_λ − g^KS_(μ_end,0))| ≤ C_J λ on
Ω′_+ for j ≤ J.

*Deduced.* So step 1 holds on every compact part of the slice: g_λ − g_(b_0) = λ m_1 + O(λ²) there, with no
oscillation at any order of the approximant. The exact solution's oscillation lies in e := g_λ − g_app, with
|∂^j e| ≤ C λ^(K−3−j) (Lemma 1.1, "Bounds"), which is small in C^J once K ≥ J + 4. Theorem 4's norm needs J = d_1 + 10
(Part VII section 4: k := d_1 + 5 in Proposition 2.2, J := k + 5), with d_1 > 10^17 (LOSS-D). K is free (Theorem E at
every order, Lemma 1.1), so K = d_1 + 14 serves. C_J does not depend on λ; λ_1 depends on J, T′, R and ε.

The question is therefore the far part of the slice, which the record does not reach.

## 2. The far part: the wedge W and its data

*Read.* BEYOND5 Lemma 6.4 (iv) (BEYOND5.md:198-212): with S := Σ_IVP ∩ {r ≥ 4R} and v_1 the value of v on ∂S, the past
domain of dependence W := D⁻(S) is bounded by S, by the ingoing cone N := {v = v_1} and by past null infinity at
v ≥ v_1, and "(b)'s first step is a characteristic problem on W: the data of g_λ on N, nothing incoming at past null
infinity". *Read.* The paper's Theorem 2 (2) (RESPONSE-HL-5D.md:372-373): "at every fixed v < V_P and x̂,
r^(3/2)(g_λ − g0 − λ[W_TT]) → 0 as r → ∞, at every λ". W_TT is proportional to the envelope, so the radiation field
vanishes for v > v_end.

*Read.* The record's Proposition 11.1 (N1STAR-PROOF.md:10575-10581): at fixed λ, on the far region,
u := g_λ − g0 = Σ_(k=3)^J r^(−k/2) G_k(v, x̂) + u_J, with "G_k = (2/(k − 3)) int_{v_start}^{v} S_(k/2 + 1) dv' for k >=
4 (G_4 = 2 int S_3), where r^-q S_q is the leading term of the source once the terms below it are known"; G_3 is the
radiation field, and the source of the equation for u_J is "a polynomial in (u, d u, d^2 u) with coefficients smooth in
(X, g)" (10596-10597), its r^(−q) coefficient "a polynomial in the G_k, k <= J, and their derivatives" (10599).

So the data on N are this expansion at v = v_1, and nothing else enters W.

## 3. The half-order tail

Write the leading wave of (2.5′) in Cartesian components as λ W_TT = r^(−3/2) (F T_F + G T_G), with
F = λ A env(v) h(ζ) sin(v/λ), G = λ A env(v) h(ζ) cos(v/λ) and T_F, T_G tensors on S³ independent of r and of v. Then
G_3 = λ A env(v) h (T_F sin(v/λ) + T_G cos(v/λ)), linear in A, purely spatial (W_TT has only dθ and dφ_i components).
Put ê(ω) := ∫ env(v) e^(iωv) dv and ω := 1/λ.

**Proposition 3.1 (deduced, from the record's Proposition 11.1; computed, T1, T7-T9).** Let v ≥ v_end.

- (a) G_5(v) = G_5(v_end) =: G_5^∞.
- (b) G_5^∞ = A a_1 + A³ a_3, where a_1 = ½(Δ̊ − ¾) ∫ G_3|_(A=1) dv = ½(Δ̊ − ¾)[λ h (T_F Im ê(ω) + T_G Re ê(ω))],
  Δ̊ acting on each Cartesian component, and a_3 is the v-integral of the cubic part of S_(7/2).
- (c) a_1 and a_3 are O(λ^n) for every n.
- (d) a_1 is purely spatial, and a_1 = 0 exactly when ê(1/λ) = 0. There is at most one A* > 0 for which the
  spatial components of G_5^∞ vanish for every λ; for every other A > 0 the λ at which they vanish form a discrete
  subset of (0, ∞).

*Proof.* **The order count.** At past null infinity give each factor of a term of S_q its order (the power of r^(−1))
and its degree in A: G_3 (3/2, 1); G_4 (2, 2), since G_4 = 2∫S_3 and S_3 is quadratic in G_3 plus Ric(g0)'s
(3μ′/(2r³)) dv dv (N1STAR-PROOF.md:10522), with μ′ = (2/9) A² env²; μ − μ_0 and μ′ (2, 2), entering g0 and Γ[g0]
(whose μ′ part is (μ′/(2r²)) ℓ dv dv, N1STAR-PROOF.md:1239); the static part μ_0 r^(−2) of g0 enters g0^(−1) only
through −(μ/r²) ℓ ℓ, two orders above, and Γ[g0] at order 3; ∂_v keeps the order, ℓ and r^(−1)Ω raise it by 1. A
term of S_(7/2) has order 7/2 and at least one factor from u. Since no factor has order ½, its factors are G_3 with
one factor of order 2 (G_4, μ − μ_0 or μ′, degree 3 in all), or G_3 with two order-raising derivatives, which is the
flat operator's part. That part is computed: (9.5) gives □̃(r^(−3/2) F) = r^(−7/2)(Δ̊ − ¾) F − (15/4) μ r^(−11/2) F,
with no r^(−5/2) term (T7a-b), and the source of Proposition 11.1 carries +½□̃(r^(−3/2) G_3) (10584-10585). So
S_(7/2) = ½(Δ̊ − ¾) G_3 + (cubic in A), which is (b) once (a) is shown.

**(a).** After the shell G_3 = 0, and every term of S_(7/2) contains G_3 or a derivative of it, so ∂_v G_5 = S_(7/2)
= 0. In the scalar model this is T1c: the r^(−5/2) coefficient after the shell is −(c/2) ∫F, c = (l + ½)(l + 3/2).

**(c).** |ê(ω)| ≤ ‖env^(k)‖_(L¹) ω^(−k) for every k (k integrations by parts), so a_1 = O(λ^∞). For a_3: write G_4 =
2∫^v S_3, where S_3's phase harmonics are 0 and ±2 (it is quadratic in the first harmonic G_3; its mean at λ⁰ is
cancelled by μ′, Isaacson's balance, (2.6)). Integrating by parts n times, G_4 is a two-scale profile with phase
harmonics 0 and ±2 plus a remainder O(λ^n) uniformly in v. The cubic part of S_(7/2) is G_3 (harmonics ±1) times
G_4, μ − μ_0 or μ′, so its two-scale part carries the odd harmonics ±1 and ±3 only and its θ-mean vanishes; its
v-integral is a finite sum of ∫ P_k(v) e^(ikv/λ) dv with k odd and P_k in C_c^∞, each O(λ^∞), and the remainder
contributes O(λ^n). Computed in the model of that integrand (T9: the θ-mean of G_3 S_3 vanishes identically, only
harmonics 1 and 3 occur, and for the bump the coefficient falls faster than λ⁴ on [2^−6, 2^−3]; control: an even
product has a nonzero mean).

**(d).** Δ̊ − ¾ has eigenvalues −(l + ½)(l + 3/2) on S³ and is injective (T7d); h > 0; T_F and T_G are linearly
independent (T7c). So a_1 = 0 iff Im ê(ω) = Re ê(ω) = 0. ê is entire. Every factor of a_1 and a_3 is an iterated
integral over [v_start, v] of products of C_c^∞ functions of v with e^(±ikωv), times monomials in ω^(±1) (λ = 1/ω,
and λ^(−1) from ∂_v² G_3), so a_1 and a_3 are real-analytic in ω > 0. If two amplitudes A_1 ≠ A_2 had G_5^∞ ≡ 0 in
ω, subtracting would give a_3 ≡ 0 and then a_1 ≡ 0, against ê ≢ 0 (the same on the spatial components, where all
of a_1 lies). For any other A, some spatial component of G_5^∞ at some x̂ is a real-analytic function of ω that is not
identically zero, so its zeros are isolated. ∎

For the C_c^∞ bump env_b(v) = exp(−1/(1 − y²)), y = (v − 2)/(3/2), on the record's interval [½, 7/2]: ê_b(1/λ) ≠ 0
at λ = 2^(−1), …, 2^(−7) (|ê_b| = 0.297 to 3.4 × 10^(−8)), falling faster than λ^5 over [2^(−7), 2^(−5)] (T8c-d);
e^(−2iω) ê_b is real (T8e), so a_1's exceptional set is the real zero set of that function, which begins at
ω = 3.331, 5.926, 8.399, 10.81, … (T8f): infinite, discrete, accumulating only at λ = 0. The record's numerical
envelope sin⁴(π(v − ½)/3) is C³ at its ends, outside Theorem 1's C_c^∞: there |ê(ω)| ω^5 stays between 17 and 61 on
ω = 10, …, 320 (T8b), so a_1 is of order λ^6, not O(λ^∞).

*Remark 3.2 (the approximant sees no tail; deduced).* In the approximant from past null infinity a term of order k/2
in a profile's expansion carries phase harmonics of the parity of k: W_TT has order 3/2 and harmonic 1 (P3), χ order 2
and harmonic 2 (P5), g0 integer orders and harmonic 0. Products, ∂_v, ℓ, Ω, ∂_θ, the transports Z^0 = −r^(1−q)S_q/(q −
5/2), the mean integrals M = (2/(2q − 5))∫S_q and the phase integral from past null infinity all preserve this parity
(each changes k by an even number or not at all), and a θ-mean is nonzero only on even harmonics. So the means of
Proposition B.4 (BEYOND5.md:777-830) have only integer orders, and after the shell g_app − g0 = Σ λ^j m_j has no
half-integer term: G_5^∞'s two-scale expansion is zero at every order, and G_5^∞ is carried by e, as (c) requires.
BEYOND5's "u's own r^(−5/2) term ... is generically nonzero" (605-606) concerns the shell itself, where G_5
oscillates with odd harmonics; after it only the O(λ^∞) residue G_5^∞ is left.

## 4. From N to spatial infinity

**Proposition 4.1 (deduced, conditional on (b1)-(b2); computed, T2-T5).** Suppose g_λ continues to W as a vacuum
metric in the record's gauge relative to g_(b_0) := g^KS_(μ_end,0), whose difference h from g_(b_0) has on W an
expansion h = Σ_(p ∈ {2, 5/2, 3, 7/2}) r^(−p) F_p(s, ω) + O(r^(−4+)), s := (v − v_1)/r, each F_p regular at N (this
is (b1)-(b2)). Then on Σ_IVP, at spatial infinity, the spatial Cartesian components of g_λ's induced metric satisfy

    γ_ij − (γ_(b_0))_ij = ρ² a_2 + ρ^(5/2) a_(5/2) + ρ³ a_3 + ρ^(7/2) a_(7/2) + o(ρ^(7/2)),     ρ := 1/r,

with a_(5/2) = T_(5/2) G_(5,ij)^∞, harmonic by harmonic, T_p(l) := √π Γ(p − ½)/(Γ((p + l + 1)/2) Γ((p − l − 1)/2)).

*Proof.* (i) In the record's gauge about the Ricci-flat g_(b_0), the operator is −½□ on Cartesian components plus
−(μ/r²) ℓℓ (relative degree −2), Γ[g_(b_0)]·∂ (degree −4) and curvature terms (degree −4), and the quadratic terms
map the degree −2 part to degree ≤ −6 and the pair (−2, −5/2) to −13/2. So the degree −5/2 part solves the flat
equation: it is r^(−5/2) F(s) with (s − s²/2)F″ + (p − ½)(1 − s)F′ − ½(p² − 2p − l(l + 2))F = 0 at p = 5/2 (T2a),
regular at N, where the other exponent is 3/2 − p = −1 (BEYOND5 D530, 577-586), so F = F(0) ₂F₁(p + l, p − l − 2;
p − ½; s/2) (T2b). On Tangherlini the recursion from the degree −5/2 datum gains μ only at degree j − 2 in v − v_1,
leaving the top degrees, which fix the limit at spatial infinity, unchanged (T4; control T4c: the full coefficients do
see μ). (ii) On a slice t = c, s = 1 + (c − v_1)ρ, so the ρ^(5/2) coefficient is F(1) = T_(5/2)(l) F(0) (Gauss's
second summation theorem, T2c to 30 digits); on Σ_IVP the bend f(r) moves s by O(ρ) and reaches only ρ^(7/2). (iii)
T_(5/2)(l) ≠ 0 for every l: Γ((3/2 − l)/2) has no pole, (3/2 − l)/2 never being a nonpositive integer, and the other
Gamma is finite (deduced); computed for l ≤ 60, with the controls that at the integer degrees p = 2 and 3 the transfer
vanishes at every odd l and every even l ≥ 2 (T3). (iv) The induced metric is g_ij plus terms carrying ∂f = O(ρ²),
which do not reach ρ^(5/2). ∎

**Corollary 4.2 (deduced, conditional as 4.1; computed, T6).** Off the exceptional set of Proposition 3.1 (d) the
spatial part of G_5^∞ is nonzero, so a_(5/2) ≠ 0, T_(5/2)(l) being nonzero at every l. A term
ρ^(5/2) a with a ≠ 0 is not in ρ² a_2 + ρ³ a_3 + ρ^(ℓ0) H_b^∞ for any a_2, a_3 and any ℓ0 > 5/2: in the b-density,
∫_ε^1 |ρ^(−ℓ0)(ρ^(5/2) − a_2 ρ² − a_3 ρ³)|² dρ/ρ grows like ε^(5−2ℓ0)/(2ℓ0 − 5), or like a_2² ε^(4−2ℓ0)/(2ℓ0 − 4)
when a_2 ≠ 0 (T6a-b; controls: subtracted in ℰ_0^½ the remainder is 0, T6c; at ℓ0 = 9/4 the term is in
ρ^(ℓ0) L²_b, T6d). Part VII's norm is "infinite outside these spaces" (PART-VII-ASSEMBLY.md:54), and its ℓ0 must exceed
3 + ε_+ (VII2), so no admissible ℓ0 rescues ℰ_0 = {(j, 0) : j ≥ 2}. **Theorem 4 (ii), as stated, does not apply to
g_λ's own data there.**

*Remark 4.3 (not a gauge artefact; deduced at the linear level, computed T5).* In the linearization about flat space
each Cartesian component of the curvature solves □R = 0, and the electric part on the slices t = c, E_ij = R_(titj),
has radiation field −½∂_v² G_3, injective on the purely spatial G_3. The recursion with radiation field G″ gives,
after the shell, vanishing r^(−5/2) and r^(−3) coefficients and an r^(−9/2) coefficient −c(c − 2)(c − 6)/48 ∫G, with
c(c − 2)(c − 6) ≠ 0 at every integer l (T5; control: a field with zero time integral leaves no tail). So the tail
of h at r^(−5/2) comes with a curvature tail ρ^(9/2) at spatial infinity, whereas data in Part VII's class have, by
the Gauss equation E_ij = Ric(γ)_ij + (tr k) k_ij − k_ik k^k_j, E_ij ∈ ρ⁴ a_4 + ρ⁵ a_5 + ρ^(ℓ0+2) H_b^∞ with
ℓ0 + 2 > 5, which excludes a nonzero ρ^(9/2) term. A diffeomorphism ψ = id + ξ of Σ_IVP with ξ decaying cannot remove
it: E is a tensor, and E_(b_0) has integer powers from ρ⁴ on, so L_ξ E_(b_0) = O(|ξ| ρ⁵ + |∂ξ| ρ⁴) does not reach
ρ^(9/2) for ξ = o(r^(1/2)), in particular for the ξ = O(ρ^(3/2)) that would move a ρ^(5/2) term of γ. The nonlinear
statement is not checked.

## 5. The scattering problem on W: the linear estimate

**Lemma 5.1 (computed, W1-W2; deduced).** Let g := g_(b_0) in Kerr-Schild Cartesian coordinates (det g = −1),
u := t − r, X := w(u) ∂_t with w := (−u)^(2a), 0 < a < 1, and T the energy-momentum tensor of a function φ. Then

    ∇_a (T^a_b X^b) = (□_g φ) X φ + T(∇w, ∂_t)                                                       (5.1)

(∂_t Killing; computed at twelve points to 50 digits, residual 1.4 × 10^(−45) against values up to 2.4 × 10^5, W1).
g^(−1)(du, du) = −4μ/r² and g^(−1)(du, dt) = −1 − 2μ/r² (W2a-b), so −∇u is future timelike, ∇w = |w′|(−∇u) since
w′ < 0, and T(∇w, ∂_t) ≥ 0 wherever ∂_t is timelike, r² > μ (W2d, 2000 random points, minimum 2.8 × 10^(−2); control
W2e: w = w(v) with w′ > 0 gives values down to −18.6). With J := −T(X, ·)^♯, on W_T := W ∩ {t ≥ T},

    E_w(S) + ∫_(W_T) |w′| T(−∇u, ∂_t) = E_w(N ∩ {t ≥ T}) + E_w({t = T} ∩ W) − ∫_(W_T) w (□_g φ) ∂_t φ,

all fluxes nonnegative: the bulk term has the sign that bounds the energy through S by the data.

*Consequences (deduced; computed, W3-W6).* For −½□_g φ + B·∂φ + Cφ = F on W, where r ≥ v_1 − t, with |B| ≤ C r^(−3)
and |C| ≤ C r^(−4) (the record's gauge about the Ricci-flat g_(b_0), whose linearization relative to itself is the
Lichnerowicz operator): (i) Gronwall's kernel ∫^(t_S) (v_1 − t)^(−3) dt converges (W4a), the zeroth-order term going
into the weighted Hardy inequality ∫ r^(2a−1) φ² ≤ a^(−2) ∫ r^(2a+1) φ_r² (W6; control: at a = 0 the constant is
lost), whose boundary term at the inner edge has the good sign; (ii) for a solution with |∂φ| ≤ C r^(−3) the cap
energy is O(|T|^(2a−2)) → 0 (W5; control: infinite at a = 1), so the truncated problems with zero data on the cap
converge as T → −∞, as in the record's Theorem A_P (N1STAR-PROOF.md:1292-1297) with (5.1) in place of (9.7): the
scattering solution on W with nothing incoming exists and is unique in the energy class of weight a; (iii) a field
r^(−2) M with its ℓ-gain has finite weighted flux through N exactly for a < 1 (W3a-b), and without the ℓ-gain the flux
diverges at every a ≥ 0 (W3c); (iv) in III.K's gauge the constraint damping 1-forms, built on c = r^(−1) dt
(BEYOND5.md:299-301), give first-order coefficients O(r^(−1)) whose kernel ∫ (v_1 − t)^(−1) dt diverges (W4c): the
continuation is posed in the record's own gauge, and what III.K receives is the geometric data (γ, k), in which the
gauge plays no part.

That is the linear core of (b1). It is not the scattering estimate itself, which also needs:

- **(N1) the nonlinear problem on W.** For h := g_λ − g_(b_0), the quasilinear term −½(g^(ab) − g_(b_0)^(ab)) ∂∂h and
  Q(∂h, ∂h) need pointwise decay of ∂h from energies commuted with ∂_t and the rotations (Killing for g_(b_0)), the
  radial derivatives taken from the equation, by a Sobolev inequality on W's slices. With |∂h| ≤ C r^(−3/2−a) the
  error kernel (v_1 − t)^(−3/2−a) is integrable (W4b), so in five dimensions the bootstrap closes for small data with
  no null condition. Deduced at the level of this sketch only: the weighted Sobolev inequality on W's slices, the
  commutator bookkeeping and the nonlinear passage T → −∞ are not written.
- **(N2) the size of the data on N.** The means m_j are λ-independent with ℓ-gaining expansions (Proposition B.4),
  so their weighted flux is O(λ) for a < 1. For e the record gives, on the far region's annuli, E(τ) =
  Σ λ^i ‖∂^i Ω^β ∂w_n‖ ≤ M_F λ^(K′) t^(−1/2) (N1STAR-PROOF.md:1336), uniformly; the null-flux identity on the dyadic
  pieces of N then gives a flux O(λ^(K′−k)) with weight r^(2a) for a < ½ only (deduced; the identity on P's annuli
  and the near region t ≤ λ^(−2), where the decomposition's λ^(−2β_0) loss enters, not written).

## 6. What the route through ℰ_0^½ still needs, and which constants depend on λ

If III.K is run with ℰ_0^½ and ℓ0 ∈ (3, 7/2), the half-order tail is a polyhomogeneous term of the class, of size
O(λ^∞), and Theorem 4 (ii) would apply to g_λ's own data once the following are done. None is done here.

- **(R1) the class run with ℰ_0^½.** Read (BEYOND5 D517, D519, 229-244): row d1 admits ℰ_0^½; π_1ℰ^C_I, Λ, (G),
  (G+), ε_+, ε_K and LOSS-D's counts are unchanged; "Only the log orders of ℰ^C_I at the half-integers can rise
  (each round takes ℰ_0 ∪̄ ℰ^C_I ...), which enter l_* and K(λ) (I11:71-81); not computed". Open.
- **(R2) (b1)**: section 5's (N1) and (N2). The linear core is Lemma 5.1. Open at proof level.
- **(R3) (b2)**: the expansion at spatial infinity through ρ^(7/2) with a remainder in ρ^(ℓ0) H_b^∞. The route:
  subtract the self-similar terms r^(−p) F_p(s), p = 2, 5/2, 3, 7/2 (BEYOND5 Lemmas 6.5-6.5‴, D530; section 4), so
  that the remainder's data on N are O(r^(−4)) with their ℓ-gain; estimate the remainder by Lemma 5.1 with a larger
  weight; obtain conormality by commuting with the scaling Z := (v − v_1)∂_v + r∂_r about N's vertex, which is
  conformal Killing for η ([Z, □] = −2□) and whose commutator with Tangherlini's corrections decays. Deduced as a
  route; not written.
- **(R4) λ-uniformity at past null infinity.** Proposition 11.1 holds at fixed λ, "its constants depend on λ and the
  order, and λ-uniformly the question stays open" (BEYOND5.md:573-574). The expansion coefficients of e = g_λ − g_app
  are explicit functionals of the radiation field minus their two-scale truncations, hence O(λ^n) (as in Proposition
  3.1 (c)). For the remainder u_J: if Lemma 11.0's and Lemma 11.2's constants are at most C λ^(−M(J)) with M(J)
  independent of K, as (9.8) with each unscaled derivative costing λ^(−1) suggests, then interpolating with
  |e| ≤ C λ^(K−3) r^(−2) makes e's remainder small in the weighted norms once K ≫ M(J) (deduced, conditional). Not
  read: the powers of λ in Lemmas 11.0 and 11.2.
- **(R5)** d_1 > 10^17, so K ≥ d_1 + 14 (section 1); λ_1 and δ are not evaluated.

| quantity | depends on | in λ |
|---|---|---|
| C_J of Lemma 1.1 | J, T′, R, the record's data | independent |
| λ_1 (Theorem 4) | ε_m, ε_t through ε; R; K = d_1 + 14 | fixes the range |
| a_1(λ), a_3(λ) | env, h, A | O(λ^∞), real-analytic in 1/λ |
| exceptional λ | env, A | discrete, accumulating at most at 0 |
| T_(5/2)(l) | l | independent |
| means' flux on N | the profiles m_j | λ^j times a constant |
| e's flux on N (a < ½) | M_F, K′, k | O(λ^(K′−k)), deduced |
| e's remainder at past null infinity | Lemma 11.0, 11.2 | C(λ, J), powers not read |

## 7. Ledger

- Deduced here, with computed support: section 1 (the slice lies after the shell; step 1 holds on compact parts);
  Proposition 3.1 (the tail, its A-structure, O(λ^∞), genericity); Remark 3.2 (the approximant's parity);
  Proposition 4.1 and Corollary 4.2 (conditional on (b1)-(b2)); Remark 4.3 (linear level); Lemma 5.1 and its
  consequences.
- Computed: `checks/tail5.py` T1-T9 (`checks/tail5.out`), `checks/wedge5.py` W1-W6 (`checks/wedge5.out`), each with
  its controls.
- Read: Part VII Lemmas 0.1, 1.1, 1.2, the norm (52-54) and (VII2); the record's Lemma 11.1, Proposition 11.1,
  (9.5), (9.8), Theorem A_P; BEYOND5 Lemma 6.4, D517-D519, D530, Proposition B.4; the paper's Theorems 2 and 4.
- Not proved: settling of g_λ's own continuation. Open: (R1)-(R5), and in Part VII's class the obstruction of
  Corollary 4.2.

**Next step.** (R1) is the one place where the class enters III.K: carrying the log orders of ℰ^C_I through III.C′'s
rounds with ℰ_0^½ decides whether Theorem 4 (ii) holds in the class that g_λ's own data can lie in. Then (N1), on
Lemma 5.1.

    python3 checks/tail5.py [t1 ... t9]     (about fifteen minutes; T4 and T8 most of it)
    python3 checks/wedge5.py [w1 ... w6]    (W1, fifty-digit numerical differentiation, most of it)

## Round 2

Status: written; not yet read by a verifier. Labels as in round 1, with **READ** for a statement of this repository
quoted verbatim with file:line (no outside source is quoted). New programs, each with its `.out` and with controls that
are claims the program must reject: `checks/halfclass5.py` (H1-H7, R1), `checks/scatter5.py` (S1-S5, R2),
`checks/spatinf5.py` (Z1-Z5, U1-U3, R3-R4), `checks/r1controls5.py` (C1-C4, controls for round 1). Round 1 above is
left as the verifier read it at a378adc; its corrections are in R2.0.

### R2.0 The verifier's reading of round 1, and what was wrong

*Reported to this workstream (not re-read here).* An independent verifier read round 1 at a378adc: the four claims of
section 0 hold, the third ((C)) conditionally. It confirmed Proposition 4.1's transfer with its own Fourier-Bessel
solution (l ≤ 14, agreement to 3e-30), Remark 4.3's curvature coefficient at ρ^(9/2) for l ≤ 9, Corollary 4.2's
outside-the-class argument from Part VII (0.1) and Lemma 0.1, and the identity (5.1), exactly.

Corrections (each states what was wrong; round 1's text is not changed):

- **(m1) Sections 0 and 7.** "It cannot be done in that class" (line 15) and "in Part VII's class the obstruction of
  Corollary 4.2" (line 279) were stated without condition. Corollary 4.2 is conditional on (b1)-(b2). Read: *under
  (b1)-(b2) (the continuation exists on W, and has an expansion at spatial infinity), it cannot be done in that class.*
- **(m2) Section 1, lines 52-56.** Lemma 1.1's bound |∂^j e| ≤ C λ^(K−3−j) with K = J + 4 gives at j = J only
  |∂^J e| ≤ Cλ, so "g_λ − g_(b_0) = λ m_1 + O(λ²)" held in C^(J−1), not C^J; in C^J it is λ m_1 + O(λ). Corrected by
  taking **K := d_1 + 15** (= J + 5), which gives |∂^J e| ≤ Cλ²; K is free (Theorem E at every order). Round 1's
  "K = d_1 + 14" (lines 56, 255) reads d_1 + 15.
- **(n1) Stale line cites in N1STAR-PROOF.md** (numbers as of 82a7e95; amended in round 3, R3.0 (c1)). Proposition
  11.1 is at 10636-10642 (cited 10575-10581); Ric(g0) = (3μ′/(2r³)) dv dv at 10583 (cited 10522); the source's
  +½□̃(r^(−3/2) G_3) at 10645-10646 (cited 10584-10585); "a polynomial in (u, d u, d^2 u) with coefficients smooth in
  (X, g)" and the r^(−q) coefficient "a polynomial in the G_k, k <= J, and their derivatives" at 10657-10661 (cited
  10596-10599).
- **(n2) Section 5 (iv), lines 214-217.** The operator with the damping 1-forms, E^Υ built on c_Υ = r^(−1) dt and E^C on
  c = r^(−1)(dt − v dr) (BEYOND5.md:300-301; round 1 and this line had "c = r^(−1) dt" for both; amended R3.0 (c2)), is
  III.K's (the write-out's; `lin5.py`'s L̄, [Hin26] (8.1)), which BEYOND5.md:299-301 calls "the record's operator"; that
  clashed with "posed in the record's own gauge" (the record's = N1STAR-PROOF.md's wave-map gauge relative to g0). And
  W4c shows only that the *unsigned* Grönwall bound fails for III.K's operator (a divergent kernel), not that the
  problem is ill-posed in that gauge.
- **(n3) Lines 3-4** said every computed item has a failing control. False: T6c and T8g could not fail, and T2 and W1
  had none. `r1controls5.py` adds them: C1 (T2: ₂F₁ with third parameter p + ½ leaves residual > 0.6), C2 (W1: (5.1) at
  four points to 7e-41, and without its bulk term T(∇w, ∂_t) it fails at every point by more than 0.12, relative), C3
  (T6c: a subtraction with coefficient ½ is rejected, the integral diverging like ε^(−3/2)/6), C4 (T8g: "ê_b(0) = 0" is
  rejected, ∫env_b = 0.666; and C4c, round 3: T8c's test fails at T8f's first zero ω* = 3.3310, where |ê_b| = 7.5 ×
  10^(−35), so T8c can fail; amended R3.0 (n6)). T1 and T7 also have no failing control; they are exact identities and a
  rank and eigenvalue computation, and are recorded here as such.
- **(n4) Line 242.** "Through ρ^(7/2)" is not needed for the class when ℓ0 ∈ (3, 7/2): (b2) needs ρ², ρ^(5/2), ρ³ and
  a remainder in ρ^(ℓ0) H_b^∞, which contains the ρ^(7/2) term. The *route* of R3 still subtracts the p = 7/2 term
  (Z5 below: without it no weight serves), but its coefficient enters no statement.
- **(n5) T9** checks a model integrand (G_3 S_3 with S_3 = (∂_v G_3)² − e²/2), not the cubic part of S_(7/2) itself.
  Proposition 3.1 (c)'s "a_3 = O(λ^∞)" rests on the parity argument (deduced); T9 is a model check of it, no more.

### R2.1 R1: the half-integer class through III.C′ and III.K

Notation: ℰ_0^½ := {(2 + j/2, 0) : j ∈ ℕ_0}; Part VII's ℰ_0^ℤ := {(j, 0) : j ≥ 2}; Σ := {(3/2 + s, 0) : s ∈ σ_Υ};
index sets, sums and extended unions as in III.A (PART-III-A-PREREQ.md:32-35); exponents formal in (½ℤ, δ, γ_Υ),
δ := (1 − e_Υ)γ_Υ (generic parameters), computed at (γ_Υ, e_Υ) = (1/100, 1/100) and checked at (1/5, 1/3) (H7a).

*READ.* III.C′ Step 2 takes, each round, "$\mathcal E'$ the smallest index set containing $\mathcal
E_0\bar\cup\mathcal E^C_I$ and satisfying III.C Definition 3.1" (PART-III-C2-POLYHOM.md:248-250), and "reaches
$\ell_I$ after $M\le4(\ell_I-\ell^\flat_I)+1$ rounds" (C2:256); the extended union is III.A Lemma 3.2's output
"$u\in H^{k,(E,\alpha),((E+z)\bar\cup F,\beta)}_{\mathrm b}$" (PART-III-A-PREREQ.md:390). l_* is to "bound, at real
part $\le5$, the log orders of $\mathcal E_{\mathrm{ind}}\cup\mathcal E^\iota_{\mathrm{ind}}\cup\mathcal E^C_I$"
(PART-III-I11-SPACETIME.md:73-74). BEYOND5 D519: "Only the log orders of ℰ^C_I at the half-integers can rise ...
which enter l_* and K(λ) (I11:71-81); not computed" (BEYOND5.md:242-244).

**Lemma R2.1 (the class is admissible; computed H1, deduced).** ℰ_0^½ is an index set, closed under sums, with
min Re = 2 > 3/2 + 2γ_Υ (γ_Υ < ¼, VI.C row u4): row d1 (PART-VI4-PARAMS.md:40) holds for every ℓ0 ∈ (3, 4) ∖ {7/2}.
(Control H1c: (5/2, 0) + ℕ_0 alone is not closed under sums.)

**Proposition R2.2 (the record's ℰ^C_I does not see the half-integers; computed H2, deduced at M = 0).** Run III.C′
Step 2 as written, M rounds. For every M ≤ 12 (which covers M ≤ 4(ℓ_I − ℓ^♭_I) + 1, at most 8 for ℓ_I < 7/2 and 10
for ℓ_I < 4; H2 was run to 8 in round 2 and is run to 12 in round 3, R3.0 (c3)), the index set
ℰ^(M) built from ℰ_0^½ *equals* the one built from ℰ_0^ℤ, log orders included, at every exponent below 11/2
(H2b), and k(n) = k(n + ½) = M(n − 1) at n = 2, …, 5 (H2e). At M = 0 this is a proof: each least Definition 3.1 set
contains the other's seed with log order 0 (ℰ^C_I + ½ ⊂ ℰ^C_I, III.C Lemma 3.2 (a)). For M ≥ 1 it is computed in the
stated range; the range covers every use of ℰ^C_I's log orders (l_* at Re ≤ 5, the spaces below ℓ_I < 7/2, the cone's
log count at Re ≤ 3 + ε_+, I11:96-107), and π_1 is equal at every M (H2a). Control H2f: an admissible seed (9/4, 0)
outside ℰ^(0) changes ℰ^(0). For every M (the verifier's induction, reported to this workstream and recorded, not
re-derived here): within ½ℤ each a + b − 1 = n + ½ pairs an integer with a half-integer, so k(n + ½) ≤ k(n); the
equality depends on Σ's point (3/2, 0) (amended R3.0 (c3)).

So, with the record's construction, **D519's "can rise" is "do not rise"**: Λ, l_*, K(λ), ℰ_par, (G), (G+), ε_+,
ε_K, α, row d2's exclusion sets and every LOSS-D count that passes through ℰ^C_I are unchanged by ℰ_0^½.

*Finding (computed H2, H5).* The record's construction makes the log orders grow with the number of rounds: its
ℰ^C_I part of l_* is 4M at Re ≤ 5 (16 at M = 4, 32 at M = 8), and LOSS-D's one-off application to the general class,
left open there ("E^C_I's log terms below ℓ_I ... (loss 6 without them", LOSS-D.md:970-971), costs 1 + J + L = 3 + 3M
applications of L_b (15 at M = 4, 27 at M = 8), loss 2(3 + 3M), for Part VII's class and the half class alike.

**Lemma R2.3 (an M-independent ℰ^C_I; deduced, computed H3-H5).** Let G be the least fixed point of G = ℰ_0 ∪̄ F(G),
F(G) the least +1-closed set containing G^tot + (G^tot − 1), G^tot := G ∪ Σ. (i) F(G) at z uses G only below z − ½ (a +
b − 1 ≥ a + ½ for b ≥ 3/2), so G is defined by recursion on the real part (H3b: the recursion and the fixed-point
iteration agree). (ii) G satisfies III.C Definition 3.1 (2)-(3) and contains ℰ_0 (H3a). (iii) III.C′ Theorem 3.1 holds
with ℰ^C_I := G for every number of rounds. *Proof of (iii).* By induction on the rounds, h's slots lie in (G ∪ {the
slot's Σ points}, α_I) at 𝓘⁺ (slot 7 has two; amended R3.0 (n2)). In (3.5) of C2 the C^∞ error maps them to G^tot + 1
and the perturbation part to ⋃_(j≥2) jG^tot − 1, both inside F(G) (G + (2,0) − 1 = G + 1, (2,0) ∈ F(G)), and below the
new weight β < α_I + ½ these involve G only below α_I. III.A Lemma 1.2 (slots 4, 5, 7: exponents 3/2 + Ā_jj ∈ Σ, which
F(G) and ℰ_0 do not meet) and III.A Lemma 3.2 (z = 0, E = ℰ_0, hypotheses as in C2) give h ∈ (ℰ_0 ∪̄ F(G), β) = (G, β)
in each slot. ∎ The record's coarser round, ℰ_0 ∪̄ ℰ^C_I, cannot have a fixed point with finite logs (H3c, the control).

With G (computed H4-H5): Part VII's class has k(n) = k(n + ½) = 2n − 3; the half class has k(2 + j/2) = j + 1, that
is **one more at each half-integer**, the same at every integer, and 0 or 1 more off ½ℤ (53 of 273 exponents below
11/2); the largest log order at Re ≤ 5 is 7 for both; π_1 is the same. LOSS-D's one-off count is 1 + 2 + 4 = 7 (loss
14) for Part VII's class and 1 + 2 + 5 = 8 (loss 16) for the half class, ℓ_I ∈ (3, 7/2); for ℓ_I ∈ (7/2, 4) it is 7
(loss 14) and 1 + 2 + 6 = 9 (loss 18) (H5c, round 3); the log-free control gives LOSS-D Q2's 3 (H5b). G is contained in
the record's ℰ^(M) from M = 2 on, and not at M = 0, 1 (H8, round 3) (amended R3.0 (n3), (n4)).

**What the half class does change (computed H6, READ, deduced).** (a) The data norm: H^(∞,(ℰ_0^½, ℓ0))_b admits the
ρ^(5/2) (and, for ℓ0 > 7/2, ρ^(7/2)) coefficients; H^(∞,(ℰ_0^ℤ, ℓ0))_b lies in it continuously (the new coefficients
are 0), so Part VII Lemma 0.1's bound carries over. (b) III.C′ Step 1 at I_0 uses R = ∏(X_0 − z) over ℰ_(0,≤):
N = 3 factors for ℓ0 ∈ (3, 7/2) and 4 for ℓ0 ∈ (7/2, 4), against 2 (H6a); READ: "The converse of Lemma 1.3 loses n_H,
each factor costing one derivative" (LOSS-D.md:90). So each Step 1 application costs one or two derivatives more
(N = 1 → 2, 2 → 3 for ℓ0 < 7/2; 1 → 2, 2 → 4, 2 → 4 for ℓ0 > 7/2: Step 1 loses 2 or 5 more derivatives, the verifier's
count), and d_1 changes by a finite amount; ε (and with it δ, λ_1) changes, as it must with any change of class. This
last statement is qualitative: none of ε, δ, λ_1 is computed here, in either class (amended R3.0 (c4)). (c) α_1 and β of
C2 must avoid Re π_1 ℰ_0^½: finitely many more points, removed by lowering η slightly, as C2 already does.

**Theorem R2.4 (Theorem 4 in the half class; deduced, conditional on Part IV exactly as Part VII's Theorem 0.2; the
condition is on statements the record lists as proved, R3.1).** Part VII Theorem 0.2 (PART-VII-ASSEMBLY.md:69-100), and
Proposition 3.2 (373-375), hold with (0.1) replaced by ℰ_0 := ℰ_0^½, ℓ0 ∈ (3, 4) ∖ {7/2}, ℓ_I ∈ (3, ℓ0) off row d2's
exclusion sets, which are the same sets as for ℰ_0^ℤ (π_1ℰ^C_I and 3/2 + σ_Υ unchanged). *The rate is unchanged:* g −
g_(m′,0) = O(t_*^(−2−ε_t)) on {r_0 ≤ r ≤ R′, t_* ≥ T′} for every ε_t < ε_K, with α ∈ (4 + ε_t, 4 + ε_K]. *The weights:*
ℓ_I ∈ (3, ℓ0) ⊂ (3, 7/2) when ℓ0 < 7/2 (the case round 2 took for g_λ's data, Lemma R2.8 in section R2.3; round 3 widens
it to ℓ0 ∈ (3, 4) ∖ {7/2}, R3.4); ε_K < ε_+ < min(δ_♯, ε_ind, ¼, ℓ_I − 3) as in row w1, and since "$<3\times10^{-6}$ at
the record's parameter point" (PART-VI4-PARAMS.md:38) bounds ε_ind, the constraint ℓ_I − 3 binds only for ℓ_I < 3 +
ε_ind, which is avoidable: **ε_K's admissible range is unchanged.** What changes: ε, d_1, δ, λ_1 (through (a)-(b)
above), none evaluated, as in round 1. *Proof.* ℰ_0 reaches the rest only through row d1, III.C′ Theorem 3.1 (whose
ℰ^C_I is unchanged, Proposition R2.2), Step 1's count, III.C″ Proposition 4.1 (any ℰ_0 with min Re > 0 and closed under
sums, PART-III-C3-BOOSTDATA.md:162-163) and the norm. [Amended R3.0 (c4): round 2 cited BEYOND5.md:237-239 for this
list, which names neither Step 1's count nor III.C″ Proposition 4.1. The statements generic in ℰ_0 that carry it are
III.C′ Theorem 3.1 under row d1, III.C″ Theorem 3.1 (2) and Proposition 4.1 (PART-III-C3-BOOSTDATA.md:91-100, 162-171),
Part IV‴ Corollary 2.3 (PART-IV4-SLAB.md:148-151), Part VIII Lemma 1.1 (PART-VIII-LINEAR.md:66-72), and Step 1's count
(H6a, computed).] ∎

### R2.2 R2: the nonlinear scattering problem on W

**Proposition R2.5 (scattering at weight a < ½; deduced as an outline, computed S1-S3).** Let a ∈ (0, ½). Suppose (N2):
the data of h := g_λ − g_(b_0) on N, commuted with ∂_t and the rotations k ≤ k_0 times, have weighted flux (density
r^(2a)(|∂_r ·|² + r^(−2)|∇_ω ·|²) r³) at most ε² with ε → 0 as λ → 0. Then there is a unique solution h on W of the
record's gauge-fixed equation relative to g_(b_0) with those data and vanishing cap energy as T → −∞, and |∂^i Ω^β ∂h| ≤
Cε r^(−3/2−a), |h| ≤ Cε r^(−1/2−a) for i + |β| ≤ k_0 − 3. On W ∩ (P ∪ Ω) it agrees with g_λ (uniqueness; at fixed λ, u =
O(r^(−2)) on P with its ℓ-gain by N1STAR-PROOF.md:10639 (cited 10616; R3.0 (c1)), so g_λ − g_(b_0) is in the class
there): it is g_λ's continuation. *Outline.* Truncate at {t = T} with zero data there (the mixed Cauchy-characteristic
problem); energy identity (5.1) for the metric g itself (the quasilinear part enters the energy-momentum tensor, leaving
errors |∂h||∂φ|²w); the bulk sign of Lemma 5.1 uses only w′ < 0 (W2), hence holds for every a > 0; commute with ∂_t and
Ω (Killing for g_(b_0)), the radial derivatives from the equation; S1 (R^(2a+3) f(R)² ≤ 2‖r^(a+3/2)f‖‖r^(a+3/2)f_r‖,
exact and at 200 random f; control: without the f_r factor no bound) with H²(S³) ⊂ L^∞ gives the pointwise decay; S2:
the error kernel ∫(v_1 − t)^(−3/2−a) dt = L^(−1/2−a)/(½ + a) is finite, so E ≤ E_0 e^(CεK_a) ≤ 2E_0 for ε small
(control: in 3 + 1 dimensions the kernel diverges at a = 0); the limit T → −∞ by the cap estimate (W5). Not written: the
well-posedness of the truncated mixed problem, the commutator bookkeeping, the limit. (N2) itself is round 1's: S3
computes its dyadic sum Σ_k 2^(k(2a−1)), finite exactly for a < ½ (control: a = ½ diverges); the null-flux identity on
P's annuli and the near region t ≤ λ^(−2) are not written.

**Proposition R2.6 (exactly how a < ½ blocks; computed S4-S5, deduced).** The energy class of weight a < ½ does not
exclude an incoming r^(−3/2) tail constant in v (a radiation field that varies in v has cap energy growing like |T|^(2a)
and is excluded at every a > 0, `trunc5.py` T8; round 2 said "incoming radiation", amended R3.0 (c5)), so no bound in it
places the data on S in III.K's class, in any gauge. (i) φ := r^(−3/2) ₂F₁(3/2 + l, −½ − l; 1; s/2) Y_l, s = (v −
v_1)/r, solves □φ = 0 (S4a, exact, l ≤ 3), has radiation field r^(3/2)φ → 1·Y_l at past null infinity at every v ≥ v_1
(S4b: incoming, constant in v), flux through N with weight a finite and cap energy → 0 as T → −∞ exactly for a < ½
(S4c-d, power-count models, not exact identities as round 2 labelled them, R3.0 (n5); control S4e: both diverge at a =
½). (ii) On a slice it reaches spatial infinity as ρ^(3/2) T_(3/2)(l) Y_l with T_(3/2)(l) ≠ 0, and ∂_t²φ = r^(−7/2)F″(s)
with F″(1) ≠ 0 (S4f-g, l ≤ 20; for every l, deduced: Gauss's second theorem with Γ((5/2 − l)/2) pole-free): a curvature
term ρ^(7/2) on S, while either class forces E_ij ∈ ρ⁴(...) by the Gauss equation (round 1 Remark 4.3; ℰ_0^½ starts at
2). (iii) The linearized curvature is gauge invariant (S5a: all 55 components vanish on ∂ξ + ∂ξ, generic ξ; control
S5b), and L_ξ E_(b_0) = O(|ξ|ρ⁵ + |∂ξ|ρ⁴) reaches ρ^(7/2) only for ξ growing like r^(3/2) (the nonlinear statement is
not checked). So the threshold ½ of (N2) is exactly the weight below which the energy cannot see a radiation field
constant in v: an estimate restriction, not a gauge artefact. **The record's gauge plus a gauge change at the end does
not avoid it**: the change at the end is free (III.C″ Proposition 4.1 rebuilds III.K's gauge data from (γ, k),
PART-III-C3-BOOSTDATA.md:162-171), but it cannot supply information the a < ½ bound lacks.

*How it is avoided at fixed λ (deduced).* g_λ's data on N have, at fixed λ, Proposition 11.1's expansion
u = Σ_(k=4)^J r^(−k/2) G_k(v_1, x̂) + u_J (G_3(v_1) = 0 after the shell). Subtract the self-similar solutions with data
r^(−p)G_(2p)(v_1), p ∈ {2, 5/2, 3, 7/2} (round 1 T2, regular at N); the remainder's data are O(r^(−4)) with ℓ-gain;
estimate it at a weight a ∈ (ℓ0 − ½, 3) (Z5) by the linear theory, the nonlinear terms entering as perturbations
whose size Proposition R2.5 gives (their kernels are those of S2). Existence of the expansion needs no smallness of
the high-weight data; the *smallness* of ‖·‖_(d_1) does, and that is R4.

### R2.3 R3: the expansion at spatial infinity with a conormal remainder

**Lemma R2.7 (computed Z1-Z4).** Z := (v − v_1)∂_v + r∂_r = (t − v_1)∂_t + r∂_r: (a) L_Z η = 2η and
L_Z g_(b_0) − 2g_(b_0) = −2μ r^(−2) dv² (control: r∂_r alone is not homothetic); (b) □_g = □_η − μ r^(−3)∂_r(r∂_r)
from the metric, [Z, □_η] = −2□_η, [Z, □_g] + 2□_g = 2μ r^(−3)∂_r(r∂_r), of relative order r^(−2) (control: [r∂_r, □]
is not a multiple of □); (c) in (τ, ρ) = (t/r, 1/r), Z = −ρ∂_ρ − v_1ρ∂_τ, b-normal at I_0 (control: ∂_t = ρ∂_τ
vanishes there); (d) (Z + p)(r^(−p)F(s)) = 0, so ∏_(p∈{2,5/2,3,7/2})(Z + p) annihilates the subtracted expansion
(control: a log term needs (Z + p)²).

**Lemma R2.8 (the weight window; computed Z5).** A conormal remainder O(r^(−q)) on N has finite weighted flux exactly
for a < q − 1, and the weight-a class gives O(ρ^(1/2+a)) on S, in ρ^(ℓ0)L²_b exactly for a > ℓ0 − ½: a window exists
iff ℓ0 < q − ½. q = 4 serves ℓ0 ∈ (3, 7/2); q = 9/2 (subtracting p = 4 too) serves (3, 4). Control: q = 7/2 serves no
ℓ0 > 3. [Amended R3.0 (c6): "O(ρ^(1/2+a))" is the pointwise reading; the S-energy with the Hardy inequality puts the
remainder in ρ^(a+1)L²_b (`scale5.py` Z8), so the condition is a > ℓ0 − 1; and the truncation's cap energy needs
q = 9/2 at a > 5/2 (`trunc5.py` T2). Round 3 takes q = 9/2, a ∈ (max(ℓ0 − 1, 5/2), 3), every ℓ0 ∈ (3, 4) ∖ {7/2}.]

*Route (deduced, not written).* Commute the remainder's equation with ∏(Z + p), ∂_t and Ω: by (a)-(b) the commutators
are the equation's own operator plus μ r^(−2)-relative terms and the nonlinear terms, whose degrees are ≤ −13/2 for the
pairs (2, 5/2) and ≤ −6 for (2, 2), landing at q ≥ 4 (no logarithm for ℓ0 < 7/2, no two subtracted exponents differing
by an integer reached); estimate at a ∈ (ℓ0 − ½, 3); the commuted energies are b-regularity at I_0 by (c), and III.A
Lemma 1.3 with V = −Z (b-normal, (c)) turns them into the expansion through ρ³ with remainder in ρ^(ℓ0)H_b^∞ on S.
Open: the commuted nonlinear estimate itself (the quasilinear term commuted with Z), and its restriction to the
slice S.

### R2.4 R4: the λ-dependence of Lemmas 11.0 and 11.2

*READ.* "Throughout, lam is fixed, and every constant may depend on it. On the far region P cap {t >= T}, T = lam^-2"
(N1STAR-PROOF.md:10537); "d^i [f] costs lam^-i, a constant now" (10539); Lemma 11.0, "with constants depending on lam
and the order" (10545-10546); "||d U_n(tau_n)|| <= C(lam, j) t_n^(-1/2)" (10565-10566); Lemma 9.3, "||d^i f||_inf <= C
lam^(-3-i) t^(-3/2) |f|_(i+3,P)" (1112); (9.8)'s proof, "the 1/lam term: lam^-1 |s G2|_k <= C lam^-1 t^(-3/2) E"
(1348-1349); Lemma 11.2's energy step with "k = C t^(-3/2), integrable" (10609-10610); and "the proposition claims
nothing uniform in lam" (10664-10665). [Line numbers as of 82a7e95: the file moved twice during round 3 (e50e9bc,
82a7e95), +23 for those round 2 cited above 10514 and +7 for 1105, 1341-1342 and 1045-1047; R3.0 (c1).]

*Deduced (not line by line).* Every λ-dependence these proofs display is a power of λ^(−1) (a derivative of a profile,
the scaled Sobolev of Lemma 9.3) or the Grönwall factor of Lemma 9.5, which on t ≥ λ^(−2) is e^(2C) even with the
kernel Cλ^(−1)t^(−3/2) (U1a; control U1b: from t = λ^(−1) the factor e^(2Cλ^(−1/2)) beats every power). If the
explicit data constants C(λ, j) of the approximating solutions and the near part of N (t ≤ λ^(−2), the λ^(−2β_0) loss)
are polynomial in λ^(−1) as well, then (Poly): the constants of (11.7) at order J with N derivatives are O(λ^(−M(J,N)))
with M independent of K, since g_λ is unique ((P-v), 1052-1054 as of 82a7e95) and Theorem P at a fixed K_0 = 6 serves for them. In
the linear model the expansion coefficients lose nothing: sup|I_j| ≤ Cλ^(j+1) for the j-fold integrals of
λ env sin(v/λ), each ∂_v costing λ^(−1) (U3a-b; control U3c: a non-oscillating field loses λ^(−1)).

**Proposition R2.9 ((Poly) gives the smallness; deduced, computed U2).** Under (Poly), let a < (J − 1)/2 and
s := (2M + 1)/(J − 1 − 2a). With R = λ^(−s), the weighted flux on N of e's remainder is at most C(λ^(2(K−4)−2as) + λ),
by (P-iii)'s λ-uniform |∂e| ≤ Cλ^(K−4)t^(−2) below R and (11.7) above (U2a, exact in sampled cases), so it tends to 0
once K − 4 > as; K is free (for λ ≤ λ_P(K)). Control U2b: the λ-uniform bound alone gives an infinite flux at every
a > 0 (W3c). [Amended R3.0 (M1), the verifier's major finding: (P-iii) bounds e, not e minus its subtracted r^(−2),
r^(−3), r^(−7/2) terms, whose coefficients at v_1 were bounded nowhere (round 1 covers only k = 5); and the H^(d_1)
norm needs the commuted fluxes, which (P-iii), a C¹ bound, does not give. R must also lie in the far region, s ≥ 2.
`spatinf5.py` U2 printed s from a truncating cast (11/2, 25/2, 41/5 for 22/5, 125/11, 82/11), now exact, with two
failing cases K − 4 ≤ as added. Replaced by Lemma R3.2: the coefficients by interpolation (`poly5.py` P8), the
commuted fluxes from Propositions 9.8-9.9 at order k, and K > K*(a, J′, M, j) (P9), which K − 4 > as does not
imply (P9b).]

### R2.5 The theorem that results

**Theorem R2.10 (conditional; deduced).** Fix A, the C_c^∞ envelope of Theorem 1, the angular profile and the seed;
let λ_P be Theorem P's. Run VI.C Theorem 2.1 with step (3) taken as ℰ_0 := ℰ_0^½, ℓ0 ∈ (3, 7/2), ℓ_I ∈ (3, ℓ0) off
row d2's exclusion sets; given ε_m > 0 and ε_t < ε_K, let ε, d_1 be III.K Theorem 4.3's in this class (below Part VII
Proposition 3.2's equivariant threshold) and J := d_1 + 10. Assume:

- (P4) Part IV's outputs, as Part VII's Theorem 0.2 does (III.K (K2)). [Discharged by citation: R3.1.]
- (b1) (N2) at some a_0 ∈ (0, ½), with k_0 commutations, k_0 large enough for the H^(d_1) norm; and the outline of
  Proposition R2.5 written.
- (b2) the commuted estimate of R2.3 at a weight a ∈ (ℓ0 − ½, 3), for the remainder after the subtraction through
  p = 7/2, and its restriction to S (omitted in round 2 though R2.3 lists it as open; amended R3.0 (m2)). [Round 3:
  p = 4, a ∈ (max(ℓ0 − 1, 5/2), 3), R3.4.]
- (Poly) for (11.7) at an order J′ ≥ 8 and N derivatives, N large enough for the H^(d_1) norm, with constant
  O(λ^(−M)); and K := max(d_1 + 15, ⌊4 + a(2M + 1)/(J′ − 1 − 2a)⌋ + 1) (so K ≥ J + 5 and K − 4 > as). [Superseded,
  R3.0 (M1): K > max(d_1 + 14, K*(a, J′, M, k_0)) of Lemma R3.2, s ≥ 2.]

Then there is λ_2 ∈ (0, λ_P(K)] such that for every 0 < λ ≤ λ_2 (no exceptional set): g_λ continues to W; its data
(γ, k) on Σ_IVP satisfy γ − γ_(b_0) ∈ H^(∞,(ℰ_0^½, ℓ0))_b, k − k_(b_0) ∈ H^(∞,(ℰ_0^½+1, ℓ0+1))_b with norm < ε in
H^(d_1) (on Σ_IVP ∩ {r ≤ 4R} by Part VII Lemma 1.1 with K ≥ d_1 + 15; the coefficients at ρ², ρ³ are O(λ), that at
ρ^(5/2) is O(λ^∞) (round 1, Proposition 3.1 and the transfer of Proposition 4.1); the remainder by Proposition R2.9);
and there are m′ with |m′ − μ_end| < ε_m and a G-invariant (Part VII's G) metric g on Ω_* ∪ 𝒟_0 with Ric(g) = 0 inducing
(γ, k), such that where χ_K = 1, g − g_(m′,0) = h_rem(q) + h with III.K Theorem 4.3 (3)-(4)'s classes, b = (m′, 0),
S = 0 (Part VII Proposition 3.2), and |(t_*∂_(t_*))^i ∂_x^β (g − g_(m′,0))| ≤ C t_*^(−2−ε_t) on {r_0 ≤ r ≤ R′,
t_* ≥ T′}. That is, the development of g_λ's own data settles to the Tangherlini metric g_(m′,0) at the rate of
Theorem 4, by Theorem 4 run in the half class (Theorem R2.4), with no gluing.

*Proof.* (b1) gives the continuation (Proposition R2.5), (b2) the expansion (R2.3), (Poly) the smallness (Proposition
R2.9 with the coefficient bounds of round 1); then III.K Theorem 4.3 in the half class (Theorem R2.4) and Part VII
Proposition 3.2 apply to the G-invariant data. ∎ **Not proved:** (P4), (b1)'s two parts, (b2), (Poly). The ρ^(5/2) tail
is no longer an obstruction: it is a term of the class.

### R2.6 Ledger and next step

- Computed: `halfclass5.py` H1-H7, `scatter5.py` S1-S5, `spatinf5.py` Z1-Z5 and U1-U3, `r1controls5.py` C1-C4, each
  with its `.out` and controls. [Round 3 amended four of them: H2 to M ≤ 12, H5c, H8; U2's cast and two failing
  cases; C4c; scatter5's docstring (55 components, S4c-d power counts). Their `.out` files are regenerated.]
- Deduced: Lemma R2.1; Proposition R2.2 (proof at M = 0, computed for M ≤ 12 below 11/2); Lemma R2.3; Theorem R2.4
  (conditional on Part IV); Propositions R2.5 (outline), R2.6, R2.9 (under (Poly)); Lemmas R2.7-R2.8; Theorem R2.10
  (conditional on (P4), (b1), (b2), (Poly)).
- READ: C2:248-250, 256; III.A:390; I11:73-74; BEYOND5.md:237-244; VI4:38, 40; LOSS-D.md:90, 970-971; N1STAR-PROOF.md
  10537, 10539, 10545-10546, 10565-10566, 1112, 1348-1349, 10609-10610, 10664-10665, 1052-1054 (as of 82a7e95;
  round 2's numbers were 23 lower above 10514 and 7 lower below, R3.0 (c1)); Part VII 69-100, 373-375.
- Findings for other files (not edited here): BEYOND5 D519's open sentence is answered (no rise with the record's
  construction; one more log at each half-integer with Lemma R2.3's); LOSS-D's open "E^C_I's log terms below ℓ_I" is
  computed (3 + 3M applications with the record's ℰ^C_I, 7 with Lemma R2.3's).
- Open: (b1) (the truncated mixed problem and the commutator bookkeeping of R2.5; (N2)'s dyadic identity), (b2) (the
  Z-commuted nonlinear estimate), (Poly) (line by line through Lemma 11.0's data constants and the near region),
  R5 (λ_1, δ; another workstream).

**Next step.** (Poly) is the cheapest of the four: it is a reading of Lemma 11.0's proof with the powers of λ carried,
the constants C(λ, j) of the approximating solutions' data (N1STAR-PROOF.md:10563-10566, as of 82a7e95) first. Then
(b2), whose commutators Lemma R2.7 has computed.

    python3 checks/halfclass5.py     (about fifty seconds, M <= 12)
    python3 checks/scatter5.py       (about four and a half minutes, 260 s)
    python3 checks/spatinf5.py       (about a minute; U3 most of it)
    python3 checks/r1controls5.py    (a few seconds)
