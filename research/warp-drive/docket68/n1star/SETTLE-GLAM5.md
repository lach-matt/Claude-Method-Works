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
11/2); the largest log order at Re ≤ 5 is 7 for both; π_1 is the same. LOSS-D's one-off count is 1 + 2 + 4 = 7
(loss 14) for Part VII's class and 1 + 2 + 5 = 8 (loss 16) for the half class, ℓ_I ∈ (3, 7/2); for ℓ_I ∈ (7/2, 4) it is 7
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
[R5.0 (r3-m6): "R3.1" here means R3-A; R3-A discharges the Part IV condition, and R2.4 itself remains deduced in this
file.]

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
the scaled Sobolev of Lemma 9.3) or the Grönwall factor of Lemma 9.5, which on t ≥ λ^(−2) is e^(2C) even with the kernel
Cλ^(−1)t^(−3/2) (U1a; control U1b: from t = λ^(−1) the factor e^(2Cλ^(−1/2)) beats every power). If the explicit data
constants C(λ, j) of the approximating solutions and the near part of N (t ≤ λ^(−2), the λ^(−2β_0) loss) are polynomial
in λ^(−1) as well, then (Poly): the constants of (11.7) at order J with N derivatives are O(λ^(−M(J,N))) with M
independent of K, since g_λ is unique ((P-v), 1052-1054 as of 82a7e95) and Theorem P at a fixed K_0 = 6 serves for them.
In the linear model the expansion coefficients lose nothing: sup|I_j| ≤ Cλ^(j+1) for the j-fold integrals of λ env
sin(v/λ), each ∂_v costing λ^(−1) (U3a-b; control U3c: a non-oscillating field loses λ^(−1)).

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

## Round 3 (2026-11-02)

Status: written; not yet read by a verifier. Labels as in round 2. New programs, each with its `.out` and with
controls that are claims the program must reject: `checks/poly5.py` (P1-P9, (Poly) and the verifier's M1),
`checks/scale5.py` (Z1-Z8, (b2)), `checks/trunc5.py` (T1-T8, (b1)). N1STAR-PROOF.md line numbers are as of
82a7e95. Round 2's programs amended (R3.0):
`halfclass5.py` (H2 to M ≤ 12, H5c, H8), `spatinf5.py` (U2), `r1controls5.py` (C4c), `scatter5.py` (docstring); their
`.out` files are regenerated and pass. Round 2's text is amended in place where the verifier's report asked, each
amendment marked "R3.0 (…)" there; round 1 is unchanged. Sections are R3.0 and R3-A … R3-F, statements R3.1 … R3.7,
equations (R3a)-(R3c), so that they do not collide (the verifier's nit).

### R3.0 The verifier's reading of round 2, and what was amended

*Reported to this workstream (the reader's scripts were not re-read here).* R2.0, R2.2, R2.3 sound; R2.4 had a gap for
ℓ0 ∈ (7/2, 4); R2.6 overstated; R2.9 had a major gap (M1). Dispositions:

- **(M1) R2.9-R2.10.** (P-iii) bounds e, not e minus its subtracted coefficients, which were bounded nowhere (round 1
  covers only k = 5), and R2.9 had only the first-derivative flux. *Repaired*: Lemma R3.2 (the coefficients by an
  interpolation lemma, the commuted fluxes from Propositions 9.8-9.9 at order k, R ≥ λ^(−2)) and the threshold K*
  (`poly5.py` P8-P9); R2.9 and R2.10 carry the amendment; R2.10's K − 4 > as does not imply K > K* (P9b).
- **(c1)** Every round-2 cite of N1STAR-PROOF.md above 10514 was 21 lines low after e50e9bc, and the file moved again
  during this round (82a7e95: +2 more there, +7 below): all of them, and 1045-1047, 1105, 1341-1342, are updated to
  82a7e95 at (n1), R2.5, R2.4's READ, the ledger and the next step.
- **(c2) (n2)** said "damping built on c = r^(−1) dt" for both 1-forms: E^Υ is built on c_Υ = r^(−1) dt and E^C on
  c = r^(−1)(dt − v dr) (BEYOND5.md:300-301). Amended.
- **(c3) R2.2** was computed for M ≤ 8; ℓ_I < 4 allows M up to 10. H2 now runs to M ≤ 12, equality holding at every
  M (`halfclass5.out`); the verifier's induction for every M is recorded in R2.2, not re-derived.
- **(c4) R2.4.** The gap for ℓ0 ∈ (7/2, 4) is closed by (c3). The factor counts (2 or 5 more derivatives in Step 1)
  are the verifier's and are recorded; the claims on ε, δ, λ_1 are now stated as qualitative (none is computed); the
  dependency list cites the statements generic in ℰ_0 (III.C″ Theorem 3.1 (2) and Proposition 4.1, Part IV‴
  Corollary 2.3, Part VIII Lemma 1.1, H6a) in place of BEYOND5.md:237-239.
- **(c5) R2.6.** "Does not exclude incoming radiation" overstated: a radiation field varying in v has cap energy
  ~ |T|^(2a) ∫F′² and is excluded at every a > 0; what a < ½ fails to exclude is an r^(−3/2) tail constant in v
  (`trunc5.py` T8a-b, quadrature: the ratio to |T|^(2a) tends to ∫F′² = 1.0895). Reworded.
- **(c6) R2.8** used the pointwise bound O(ρ^(1/2+a)); the S-energy with Hardy gives ρ^(a+1)L²_b (`scale5.py` Z8), so
  the condition is a > ℓ0 − 1. Amended, with a pointer to R3-D.
- **(m1)** `spatinf5.py` U2 cast `sp.Integer(JJ − 1 − 2aa)`, which truncated: s is now exact (22/5, 125/11, 82/11),
  and two failing cases with K − 4 ≤ as (K = 24, 16) give an infinite flux, as they must. **(m2)** R2.10's (b2) now
  names its restriction to S. **(m3)** R ≥ λ^(−2), so s ≥ 2 (in Lemma R3.2). **(m4)** Run times corrected.
- **Nits.** (n1) scatter5's docstring now says 55 components; (n2) slot 7 has two Σ points (R2.3); (n3) for
  ℓ_I ∈ (7/2, 4) the half class costs 9 applications, loss 18 (computed, H5c: (J, L) = (2, 6); Part VII's class 7);
  (n4) G ⊂ ℰ^(M) exactly from M = 2 (computed, H8); (n5) S4c-d are power-count models (R2.6, scatter5); (n6) C4c runs
  T8c's test at T8f's first zero ω* = 3.3310293, where |ê_b| = 7.5 × 10^(−35): T8c can fail; (n7) "R2.3 below" in
  R2.4 now reads "Lemma R2.8 in section R2.3".

### R3-A What "conditional on Part IV" means

*READ.* III.K Theorem 4.3 is "conditional on Part IV" (PART-III-K-NONLINEAR.md:468), and (K2) says what Part IV must
deliver: "(a) III.C′ Theorem 2.1 in the cut-off gauge ... (b) Its continuation on the slab 𝒮 ... (c) III.E Theorem 1.1
(constraint damping) ... Theorem 4.3 is conditional on these" (PART-III-K-NONLINEAR.md:510-518). Part VII Theorem 0.2
uses III.K Theorem 4.3 (PART-VII-ASSEMBLY.md:69-92), and so did Theorem R2.4.
[R5.0 (nit): PART-III-K-NONLINEAR.md:468 and 510-518 read 470 and 512-520.]
[R6 (m7): now 471 and 513-521 (md5 5b0ad3f0), keyed by content: "Theorem 4.3 ([Hin26] Theorem 13.1 at n = 4; conditional
on Part IV)" and (K2) through "Theorem 4.3 is conditional on these".]

*READ, the statements that deliver them and their status (proof5/README.md:77-84).*
- (a): Part IV″ Theorem 2.4 (the linear exterior estimate), Theorem 3.1 (the nonlinear exterior solution) and
  Corollary 4.1 (the cut-off gauge) (PART-IV3-NM.md:229, 321, 382), on Part IV′ and Part IV; status **proved**
  (IV D309; IV′, IV″ D311).
- (b): Part IV‴ Theorems 2.1-2.2 and Corollary 2.3 (PART-IV4-SLAB.md:86, 128, 148); **proved** (D312).
- (c): III.E Theorem 1.1 (1)-(3) is Part IV⁗ Theorem 2.1 (PART-IV5-CDMODES.md:154), with [Hin26a] Theorem 5.2 at
  n = 4 from Part IV′′′′′ Theorem 7.3 (PART-IV6-SOLV.md:742); (4) is Part IV′′′′′′ Theorem 4.1 (PART-IV7-TFACE.md:387)
  through its Theorem 3.1 (348). **Proved** (IV⁗, IV′′′′′ D312; IV′′′′′′ D315).
- III.K itself: **proved** (D312), conditionally on (a)-(c) (README:77).

*READ, the class.* Part IV″ works with conormal data: "ℰ_0 := ∅, ℓ_0 := ℓ^♭_0" (PART-IV3-NM.md:60-61), its Theorem
3.1's data in H_b^(∞,ℓ^♭_0) (321-330). The one output that carries an index set, Part IV‴ Corollary 2.3, takes "the
hypotheses of III.C′ Theorem 3.1 on the data" (PART-IV4-SLAB.md:148-149), which ℰ_0^½ satisfies (row d1, Lemma R2.1).

*Deduced.* "Conditional on Part IV" in Theorems R2.4 and R2.10 means conditional on those seven statements, each listed
as proved in the record, none depending on ℰ_0 beyond row d1. So (P4) is discharged by citation and Theorem R2.4
holds in the record's sense of "proved". This workstream did not re-read Part IV.
[R5.0 (r3-m6): overclaimed. R3-A discharges Theorem R2.4's Part IV condition by citation; R2.4 itself remains deduced
here.]

### R3-B (Poly): the powers of λ, carried

*Setting.* "λ-order p" means a bound C λ^p. K_0 := 6: Theorem P at K = 6 gives the same g_λ as at any K ≥ 6, for λ ≤
min(λ_P(K), λ_P(6)) ((P-v), N1STAR-PROOF.md:1052-1054; the two approximants differ by O(λ²) t^(−2) in C¹). So every
constant below is K-free. u_1 := g_λ − g0 − r^(−3/2)G_3 = a + w, a := g_app − g0 − r^(−3/2)G_3 explicit
(N1STAR-PROOF.md:1436-1440), w = g_λ − g_app.

(a) *The chain rule and the kernels* (computed P1-P3). Each Cartesian derivative of a profile at phase v/λ costs exactly
λ^(−1), attained, and a rotation none (P1a-d; control: x2∂_1 + x1∂_2 costs λ^(−1)). ∂(λ[W_TT]) has order 0 (P2a: λ-order
0), so the kernel ‖∂g_n‖_∞ ≤ C t^(−3/2) of Lemma 9.5 in Lemma 11.0 and of Lemma 11.2's energy step is λ-free, and on t ≥
λ^(−2) its Grönwall factor is e^(2Cλ) (P3a).

(b) **Finding F1 (a gap in Lemma 11.0's written proof; harmless on the far region).** (g^(−1) − g0^(−1))(dv, dv) = −u(ℓ,
ℓ) + O(u²) (P2c, exact first variation at 60 digits; control P2e), so the quasilinear term of S(u) on λ[W_TT] is
½(g^(ab) − g0^(ab))∂_a∂_b(λ[W_TT]) = ½λ^(−1)(g^(−1) − g0^(−1))(dv, dv)[∂_θ²W_TT] + O(λ⁰) (P2d, exact on a profile W sin
θ), i.e. a term −½λ^(−1) u_1(ℓ, ℓ)[∂_θ²W_TT] of F_1, linear in u_1 with coefficient λ^(−1)t^(−3/2). At order |γ| = j + 1
its ∂^γ contains −½λ^(−1)(∂^γ u_1)(ℓ, ℓ)[∂_θ²W_TT], of the top order, not "the orders already controlled"
(N1STAR-PROOF.md:10550-10551). It must enter Lemma 9.5's kernel through Lemma 9.3(b), as Proposition 9.8 (i) does with
λ^(−1)sG2 (1348-1349): on t ≥ λ^(−2) that kernel integrates to 2C (P3a), a λ-free factor e^(2C). On the near region it
would give e^(2C(1/λ − 1)), which beats every power (P3b, the control).
[Withdrawn, R5.0 (r3-M1): the λ^(−1) term multiplies U, which the previous step bounds; the term at the energy's own
order is b . d U, from the Q-difference (R4-B; R5-D). P2c is a central difference, not exact.]

(c) *The data constants C(λ, j)* (computed P4). ‖∂U_n(τ_n)‖ ≤ C(λ, j)t_n^(−1/2) (N1STAR-PROOF.md:10563-10566):
the explicit part a is natural, ∂^(j+2) a has λ-order −(j + 1) (times r^(−2)); for w_n, which vanishes on
Σ_(τ_n) with its first derivatives, the model of (3.2) (oscillating g_app^(−1) − g0^(−1) of size λ, the 1/λ coupling
s(w)G2, quadratic terms, residual λ^(N−1)[R]) gives ∂_τ^m w_n λ-order exactly N + 1 − m (m = 2..6, N = 6; control: "order
N − 1 at every m" fails at m = 3). So C(λ, j) ≤ C_j λ^(−(j+1)): polynomial.
[R5.0 (nit): P4 is a 1+1 model (model-checked, the structure of the record's equation deduced); P4b now mutates the
model's operator.]

(d) *Lemma 11.0 as written* (computed P5). With the sources split as written (the highest-order factor in L², the rest
in sup; sup at order n from energies of order n + 2 by Lemma 9.3, the cost of three; Theorem P at orders ≤ 6), the
energy at order N has λ-order −P(N), P(N) finite at every order and P(N) ≤ 9N/4 for 7 ≤ N ≤ 160 (P(40) = 82, P(160) =
358). The record's split inequality ⌊(N + 2)/2⌋ ≤ max(4, N − 3) holds (P5a); the reverse split needs an uncontrolled
order (P5d).

(e) *The sharp reading* (computed P6; deduced). Proposition 9.8's proof at order k: items (i)-(v) (N1STAR-PROOF.md:
1348-1354) use scaled norms throughout, the nonlinear term is C(k)λ^(−5)t^(−3/2)E², and 10.51's reading of section 4
(6776-6801: Step 4's split at k − 2, "valid at every k ≥ 3 with C = C_k", closing when 2K − 5 ≥ K + 1) applies to
them verbatim. So (9.8) holds at every order k ≥ 6 for λ ≤ λ_F(k) (deduced, not read line by line). With it, w has
λ-order K′_0 − 3 − n ≥ 1 − n at n derivatives, a has λ-order 1 − n, and the recursion of (d) closes at the
natural exponent: |∂^α Ω^β u_1| ≤ C λ^(1−|α|) t^(−2) (P6a; control P6b: at K′ = 5 the scaled bootstrap fails).
[R5.0: P6b is [arithmetic]; the closing condition is computed in order5.py O2.]

(f) *Lemma 11.2 and Proposition 11.1* (computed P7). The coefficient G_k = c∫S_(k/2+1) has λ-order −e(G_k), e(G_k) = k −
4 (k ≥ 4; e(G_3) = −1): S_q's monomials are a linear term on G_(k−2) with at most one ∂_v or products of earlier
coefficients with at most two, and an integral over [v_start, v] costs nothing. Each stage of Proposition 11.1 is Lemma
11.2 with: S̃'s terms linear in u_J (+1: the λ^(−1)u_J(ℓ,ℓ)[∂_θ²W] of F1 and ∂u_J ∂(λ[W])), quadratic in u_J (one factor
bounded crudely, |∂u_J| ≤ λ^(−(J−3)) r^(−2)), S′'s (g^(−1) − g0^(−1))∂²(r^(1−q)G_(J+1)) (e(G_(J+1)) + 1), a λ-free
Grönwall factor (Lemma 9.5 on the far region, P3a), Lemma 9.3 (+2), and the ℓ-transport (11.6) with the λ-free factor
e^(3d1/(2r′))(d1/2) (+1 per ℓ, its forcing containing ∂_v u~~). u_J has λ-order −B_J, B_J = (J² − J)/2 − 3 (J ≥ 4), B_3
= −1 (P7b; control P7c: no bound linear in J with slope 3, B_24 = 273).
[R5.0 (r3-m7): the recursion omits products of three or more coefficients, whose orders grow without bound unless the far
region's r^(−1/2) ≤ λ is used; with it every monomial gives B_J ≤ 3J − 9 (Proposition R5.4, r5settle5 A). P7c checks the
recursion, not the problem: [arithmetic].]

**Proposition R3.1 ((Poly) on the far region; deduced, computed P1-P7).** For J ≥ 3 and n, m ≥ 0 there are C and
λ_0 > 0, depending on J, n, m and the record's data (seed, A, env, angular profile) and not on K, such that for
0 < λ ≤ λ_0, on {t_P ≥ λ^(−2) + d1} (the far region less the collar its ℓ-transport needs, N1STAR-PROOF.md:10625),
for |α| + |β| ≤ n:

    |∂_X^α Ω^β ℓ^m u_J| ≤ C λ^(−(B_J + |α| + m)) r^(−(J+1)/2 − m),    |∂_X^α G_k| ≤ C λ^(−(k − 4 + |α|))  (k ≥ 4),

B_J = (J² − J)/2 − 3. So (Poly) holds with M(J, n, m) = B_J + n + m, polynomial and K-independent. Its inputs: (e),
i.e. Proposition 9.8 at order n + 4 (deduced); without (e), Lemma 11.0 as written gives a larger finite exponent
(P(N) ≤ 9N/4 at the base), still polynomial. ∎
[R5.0 (r3-m7): an upper bound; derived, B_J ≤ 3J − 9 (Proposition R5.4), so this bound holds a fortiori and M(8, n, m) =
15 + n + m serves.]

*Where polynomiality fails, exactly.* Only on the near region and only through the 1/λ coupling: Theorem P's
smoothness argument there ("taken over the bounded interval [tau_T, tau0] on the near region, with no decomposition
needed for fixed lam", N1STAR-PROOF.md:1423-1426) has the kernel C(λ)t^(−3/2) with C(λ) ⊃ λ^(−1) (F1), whose
Grönwall factor over [1, λ^(−2)] is e^(2C(1/λ − 1)) (P3b). (11.7) lives on the far region and does not use it.
[R5.0 (r3-M1): the λ^(−1) of C(λ) is the zero-order coefficient d^2 g_n' of Theorem P's difference system, "at most C
lam^-1 t^(-3/2)" (N1STAR-PROOF.md:1424-1425 now), not F1.]

(g) *The near region* (deduced; computed T6c). It enters only (N2)'s commuted fluxes on N ∩ {1 ≤ t_P ≤ λ^(−2)}.
Proposition 9.9's proof states that "every line holds at every order j ≤ k with c0 unchanged" (N1STAR-PROOF.md:
1404-1405) and that β0 "depends only on the constants C of (9.9) below at the orders j ≤ k" (1371); with 10.51's
reading of section 4 this gives (9.9a) at every order k with β0(k) = max(2, 4C(k) + 1), C(k) not evaluated, the loss
λ^(−2β0(k)) absorbed by K′ = K + 3 + ⌈4β0(k)⌉ (deduced, not read line by line). So (P-iii) holds at order k:
|∂^i(g_λ − g_app)| ≤ C_k λ^(K−3−i) t_P^(−2) on P, i ≤ k − 3. The near-region pieces of N then sum to
O(log(1/λ) λ^(2(K′−1) − 4β0 − 2(2a+1))), → 0 once K′ > 2 + 2β0 + 2a (T6c, exact at β0 = 2, 3).

(h) *The coefficients of e* (the verifier's M1; computed P8). **Lemma (interpolation).** If P(s) = Σ_(i≤d) c_i s^i
and |P| ≤ η on [σ/2, σ], then |c_i| ≤ L_d σ^(−i) η, L_d the largest row sum of the inverse Vandermonde matrix at
d + 1 equally spaced nodes (L_4 = 27136/3; P8a, exact, 100 random polynomials). Apply it on N to r²e = Σ_(k=4)^(J′)
s^(k−4)e_k + s^(−4)(remainder), s = r^(−1/2), with (P-iii)'s |e| ≤ Cλ^(K−3)r^(−2) and (Poly)'s remainder
Cλ^(−M)r^(−(J′+1)/2) (M the order of e's remainder: u_(J′)'s of R3.1 with the approximant's, explicit), at
σ^(J′−3) = λ^(K−3+M): |e_k| ≤ Cλ^((K−3)(1−θ_k) − Mθ_k), θ_k := (k − 4)/(J′ − 3) (P8b), with σ in the far region once
K − 3 + M > J′ − 3 (P8c; control P8d: at a fixed radius the bound is λ^(−M)). The same with K − 3 − i and M + i for
∂_v^i e, from (P-iii) at order k ((g)).
[R5.0: P8c and P8d are [arithmetic]; the optimum is recomputed with mutation controls in r5settle5 C.]

**Lemma R3.2 (the commuted flux of e's remainder on N; deduced, computed P8-P9).** Let J′ ≥ 8, a ∈ (0, (J′ − 1)/2),
j ≥ 0, M as in (h) at j + 1 derivatives, s := max(2, (2M + 1)/(J′ − 1 − 2a)), R := λ^(−s). The flux at weight a
through N of Γ^α(e − Σ_(k=4)^(8) r^(−k/2)e_k), |α| ≤ j, Γ ∈ {∂_t, Ω, Z} (on N, Z = rℓ, tangent, `scale5.py` Z6),
tends to 0 as λ → 0 once K > K*(a, J′, M, j), the largest of 4 + j + s(a + j) (e below R, where the λ-uniform
bounds have no ℓ-gain and Z costs r) and 3 + i + (s·max(0, 2a + 2 − k)/2 + (M + i)θ_k)/(1 − θ_k) for 4 ≤ k ≤ 8,
i ≤ j + 1 (each coefficient up to R); above R, (11.7) with its ℓ-gains gives λ^(−2M)R^(2a+1−J′) → 0 by the choice of
s. Computed exactly at K = ⌊K*⌋ + 1 in three cases (P9a). Control (P9b): a = 11/4, J′ = 8, M = 12: R2.10's K = 50
satisfies K − 4 > as, but K* = 56 and the e_8 term of the flux tends to infinity. ∎
[R5.0 (nit): P9b shows that the interpolation bound on the e_8 term diverges, not the flux.]
[R5.0 (nit): s = 2 puts R at λ^(−2), short of the collar λ^(−2) + d1: s := max(5/2, (2M + 1)/(J′ − 1 − 2a)).]

So the smallness of g_λ's data on N at weight a, with k_0 commutations, needs K > K*(a, 8, M(8, k_0 + 1, k_0 + 1),
k_0); with R3.1's M(8, n, m) = 25 + n + m this is a finite number for each a < 3, k_0, linear in k_0 for a fixed a.
[R5.0 (r3-m5): quadratic in k_0, not linear (r5settle5 B1: K* = 116, 821.5, 2071.5 at k_0 = 0, 10, 20 for a = 11/4).]

### R3-C (b1): the truncated problems as Cauchy problems, and (N2)

**Lemma R3.3 (the truncation; computed T1-T2; deduced).** (i) ∇v = g_b0^(−1)dv = −∂_t + x̂·∂_x is null and past-directed
for every μ (T1b, exact), so dv(Y) ≥ 0 for every future causal Y (T1a, 2000 random points, minimum 5.7 × 10^(−2);
control T1d: dr(Y) has both signs). For g_λ and for any metric with Lemma 9.1(f)'s margin, Φ := v + h(τ) increases along
future causal curves (N1STAR-PROOF.md:1069-1078), and N runs inside Ω′ ∪ P′ with δ_0 := V′_P − κ − v_1 > 0: ∂S lies in
the interior of Ω′_+ and v + (τ − τ′_end) decreases strictly along N to the past (BEYOND5.md:203-205; Part VII Lemma
1.2), so BEYOND5's "v1 ≤ V′_P − κ" is strict. For q ∈ J^−(p) ∩ Σ_T, p ∈ N, τ(p) ≥ T: on the bounded part in Ω′ use v +
ε(τ − τ0), a time function with margin 2ε (T1e, exact; control T1f), with ε(τ′_end − τ0) < δ_0/2, then Φ on P′: v(q) ≤
v_1 + δ_0/2 + κ − h(T) = V′_P − h(T) − δ_0/2 (deduced). (ii) So the *truncated problem* 𝒫_T is a Cauchy problem for the
record's Ric^H(g) = 0 relative to g0 (= g_b0 on v ≥ v_end) with data on Σ_T: g_λ's on {v ≤ V′_P − h(T) − δ_0/2}, a
cut-off over the band {V′_P − h(T) − δ_0/2 ≤ v ≤ V′_P − h(T)} ⊂ P′, and beyond it g_b0 (for (b1)) or g_b0 + Σ (for (b2),
Σ the self-similar terms of R3-D). Its solution equals g_λ on {v ≤ v_1, t ≥ T} ∩ (P′ ∪ Ω′) by uniqueness in the domain
of dependence ((P-v); Step 8), so N ∩ {t ≥ T} carries g_λ's data: **no characteristic problem and no corner condition is
posed**. The strip between N and the band has width κ − h(T) ≥ κ(1 − t_P^(−1/4)) (T1c). (iii) Since v is a time
function, the solution on W ∩ {v ≤ V_*} depends only on the data on Σ_T ∩ {v ≤ V_*}: the problem may be posed with data
equal to g_b0 beyond v = V_* + 2, a compactly supported perturbation, to which the record's local theory (Step 8, READ
there: [DS23] Theorems 2.4, 2.6, [AO14] Theorem 1.1) applies on bounded domains; the solutions for V_* → ∞ agree on
overlaps. (iv) The cap energies: the band costs |T|^(2a_0 − 1) for h ~ r^(−2), → 0 exactly for a_0 < ½ (T2a, control
T2c), and |T|^(2a − 6) for the remainder h_R = O(r^(−9/2)) of R3-D, → 0 exactly for a < 3 (T2b); the subtraction through
p = 7/2 only (h_R = O(r^(−4))) does not tend to 0 at a = 11/4 (T2c). ∎
[R5.0 (r3-m1): in (i) the infimum is 0, attained at Y = −∇v (r5settle5 D2); the sampled minimum is an artefact. (iii) is
withdrawn: v is not a time function (dv is null for g_b0, and g^(−1)(dv, dv) = −h(ℓ, ℓ) + O(h²) has either sign,
r5settle5 D1-D2); the localisation is by Φ_W = v + 1/r (or v + εt on the bounded slab) and does not change the data
(R5-B). (i), (ii) and (iv) stand.]

**The energy identity for the quasilinear metric (computed T3).** For g = g_b0 + h, not stationary, and X = w(u)∂_t,

    ∇_a(T^a_b X^b) = (□_g φ) Xφ + T(∇w, ∂_t) + ½ w T^(ab) ∂_t g_ab,                                           (R3a)

at 40 digits, six cases, relative defect 1.3 × 10^(−40) (T3a; control T3c: without the deformation term it fails);
and g^(ab)∂_a∂_b φ = □_g φ + g^(ab)Γ^c_ab ∂_c φ (T3b): the reduced operator differs from □_g by a first-order term
with coefficient Γ[g_b0] + O(∂h) = O(r^(−3)) + O(|∂h|). The deformation term is bounded by w|∂_t h||∂φ|², a kernel
|∂_t h| ≤ Cε r^(−3/2−a_0), integrable along W (scatter5 S2). Round 1's (5.1) is the case ∂_t h = 0.

**The commutators (computed `scale5.py` Z2, `trunc5.py` T4).** ∂_t P(h) = DP(h)[∂_t h] and L_Ω P(h) = DP(h)[L_Ω h]
exactly for the full gauge-fixed operator (Z2a-b at 40 digits; controls: the rotation on components alone, and the
translation ∂_1, fail): the commuted fields solve the linearised equation at h with no source. The radial second
derivative is solved for from the equation: on φ(t, |x|) the ∂_r² coefficient of g_b0^(ab)∂_a∂_b is 1 − μ/r² > 0
(T4a; with ∂_t² coefficient −(1 + μ/r²), ∂_t∂_r coefficient 2μ/r²), so ∂_r²h is the source plus ∂_t-commuted and
angular terms (control T4b: it vanishes at r² = μ).

**(N2)'s flux identity on a dyadic piece (computed T5-T6).** On D = {τ_− ≤ t ≤ τ_+, v_start ≤ v ≤ v_1}, for φ
vanishing near {v = v_start} (the record's e and m_j do, N1STAR-PROOF.md:1046, (P-i), and 1234),
[R5.0 (nit): 1234 reads 1235.]

    E(τ_+) + ∫_N ½(φ_t − φ_r)² r³ dr = E(τ_−) − ∫∫_D φ_t □φ r³ dr dt,                                         (R3b)

exactly in the flat radial model (T5a; control T5b: with the transverse (φ_t + φ_r)² it fails); on N only the tangential
derivative enters. With the record's operator, the commuted equations and Lemma 9.5's bulk bound in place of the flat
ones, each dyadic piece N_k = N ∩ {2^k ≤ t_P ≤ 2^(k+1)} has flux at most C(E(τ_k^−)² + bulk), the energy at the
earlier slice. Far region (Proposition 9.8 at order k): Σ_k 2^(2a(k+1)) M_F² λ^(2(K′−i)) 2^(−k), finite exactly for
a < ½ (T6a; control T6b). Near region ((g)): T6c. Compact part N ∩ Ω′: Part VII Lemma 1.1 (|∂^j e| ≤ Cλ^(K−3−j)). So
(N2) holds at every a_0 ∈ (0, ½) with k_0 commutations: the weighted commuted flux of h on N is O(λ²) (the means,
λ-independent profiles with their ℓ-gain, W3) plus O(λ^(2(K−3−k_0))) (deduced; every identity computed).

**The limit (computed T7).** For T > T′ → −∞, h_T − h_T′ on W ∩ {t ≥ T} has the caps' data (T2) and the flux of
h_T′ through N ∩ {T′ ≤ t ≤ T} and its sources there, whose tails tend to 0: |T|^(2a_0 − 2) with the ℓ-gain (T7a;
control T7b: without it the tail is infinite). With the integrable kernels (scatter5 S2; W4) the h_T form a Cauchy
sequence in the energy class of weight a_0, and the limit is unique there (R2.5).

**Proposition R3.4 ((b1); deduced, every identity computed).** Under (N2) at a_0 ∈ (0, ½) with k_0 commutations and
data small (λ small, K as in Lemma R3.2 at a_0), g_λ continues to W as a solution of Ric^H = 0 relative to g_b0, the
limit of the truncated problems of Lemma R3.3, unique in the energy class of weight a_0 with vanishing cap energy, and
|∂^i Ω^β ∂h| ≤ Cε r^(−3/2−a_0) for i + |β| ≤ k_0 − 3. What is not written: the bootstrap on W assembled line by line
from (R3a), the commutators, S1 (scatter5), W6 and S2 (that is round 2's outline with each identity now computed);
and **(V)**, that the limit is vacuum: D(g) solves the homogeneous system of N1STAR-PROOF.md section 0.7 with D = 0 on N
(g_λ is vacuum and in gauge on P ∪ Ω) and data of size → 0 on the caps (the band's constraint defect, T2), and the
record's argument for D(g_λ) = 0 on P (N1STAR-PROOF.md:1433-1436, Grönwall with an integrable kernel) then gives D = 0
on W; deduced, not written.

### R3-D (b2): the Z-commuted estimate and the expansion at spatial infinity

**Proposition R3.5 (the scaling identity; computed Z1, Z3).** Let P_μ(h) := Ric^H(g_b0(μ) + h; g_b0(μ)) in Cartesian
components and Z := (t − v_1)∂_t + x·∂_x on components. For every h,

    (Z + 2) P_μ(h) = DP_μ(h)[Z h] − 2μ ∂_μ P_μ(h).                                                          (R3c)

*Proof (deduced).* D_s^* g_b0(μ) = s² g_b0(μ s^(−2)) (Z1d, exact), Ric^H is natural and Ric^H(s²G; s²G0) = Ric^H(G; G0);
so P_(μ s^(−2))(h(s·)) = s² P_μ(h)(s·), and d/ds at s = 1 is (R3c); P is static, which centres the dilation at any
t = v_1. ∎ *Computed*: Z1a, all 15 components at three points, 40 digits, for an explicit h of size 0.3 (not small):
defect 4.7 × 10^(−41) against terms up to 0.44; controls Z1b (without −2μ∂_μP: defect ≥ 0.028) and Z1c (the
non-uniform dilation (t − v_1)∂_t + 2x·∂_x: ≥ 0.065). Z3: the scalar case is round 2's Z2c,
−2μ∂_μ(□_g) = 2μ r^(−3)∂_r(r∂_r).

For a solution, P_μ(h) = 0, so Zh solves the linearised equation at h — with the full quasilinear principal part
−½g^(ab)∂_a∂_b — with source 2μ∂_μ P_μ(h), the μ-derivative at fixed h; P depends on μ only through g_b0, and
∂_μ g_b0 = r^(−2) kk, so every term of the source carries μ r^(−2) relative to P's terms. Differentiating (R3c) in h,
(Z + 2)DP(h)[k] = DP(h)[Zk] + D²P(h)[Zh, k] − 2μ∂_μDP(h)[k], which gives the equations of Z^j h and of mixed
Γ^α h (Γ ∈ {∂_t, L_Ω, Z}) by induction (deduced). In particular the quasilinear term commutes without loss: the
"(Z H)∂∂h" of round 2 is D²P(h)[Zh, h]'s principal part.
[R5.0 (nit): it is DP(h)[Zh]'s zero-order part −½(Dg^(−1)[Zh])^(ab) ∂_a∂_b(g_b0 + h).]

**The identities the weighted estimate uses (computed Z4-Z8).** (i) Every second derivative is a first derivative of
a commuted field: ∂_i = r^(−1)x̂_i(Z − (t − v_1)∂_t) − r^(−2)x_jΩ_ij on every function (Z4a), with |t − v_1| ≤ r on W
(Z4b; control Z4c). (ii) On N, Z(v − v_1) = v − v_1 and Z = r(∂_r − ∂_t) (Z6a-b): the data of Z^j h on N are
tangential and keep the order r^(−q) (Z6c). (iii) Kernels at weight a for the remainder h_R := h − Σ,
Σ := Σ_(p∈{2,5/2,3,7/2,4}) r^(−p)F_p(s), F_p regular at N (round 1 T2; the p = 4 term solves the degree −4 equation with
the quadratic degree −6 source, the other exponent 3/2 − p < 0 excluded as in BEYOND5 D530; deduced): the μ-source and
the Σ-coefficients give r^(−3), the quasilinear h_R-term (Zh_R)∂∂h_R gives (v_1 − t)^(−1/2−a) (integrable for a > ½),
Q's give r^(−3), r^(−3/2−a), and Σ's residual P(Σ) = O(r^(−6)) gives the L² kernel (v_1 − t)^(a−4), integrable
exactly for a < 3 (Z7a; controls Z7b at a = 3, Z7c at a = ½). (iv) On S = {t = f(r)}, r d/dr(h|_S) = (Zh)|_S +
(v_1 − f + rf′)(∂_t h)|_S (Z5a; control Z5b), the coefficient smooth in ρ (f′ ∈ |x|^(−2)C^∞, PART-VII-ASSEMBLY.md:
162-177): the b-derivatives of the data on S are restrictions of commuted fields. (v) The S-flux at weight a with the
Hardy inequality puts φ|_S in ρ^(a+1)L²_b(dρ/ρ) and ∂φ|_S in ρ^(a+2)L²_b (Z8a, exact on ρ^β); Σ|_S has exponents
p + j, all in ℰ_0^½ (Z8c); and a ∈ (ℓ0 − 1, 3) serves ℓ0 = 3.8 (Z8b), where round 2's pointwise reading a > ℓ0 − ½ does
not (Z8d).
[R5.0 (nit): with p = 4 in Σ, P(Σ) = O(λ r^(−13/2)) (B8, r5op5 O2) and the kernel is (v_1 − t)^(a − 9/2), integrable for
a < 7/2; a < 3 is set by the cap (T2b, r5settle5 G2). Z7 and Z8b-d are [arithmetic].]

**Proposition R3.6 ((b2); deduced, every identity computed).** Let ℓ0 ∈ (3, 4) ∖ {7/2},
a ∈ (max(ℓ0 − 1, 5/2), 3), q = 9/2. Run Lemma R3.3 with the data g_b0 + Σ beyond the band (posed on {v ≤ V_*} as in
R3.3 (iii)) and estimate Γ^α h_R, |α| ≤ k_0, Γ ∈ {∂_t, L_Ω, Z}, at weight a by (R3a), with the equations of
Proposition R3.5, the kernels of (iii), the data on N small by Lemma R3.2 at weight a, and the caps by T2b; the
limit is Proposition R3.4's solution (both lie in the weight-a_0 class with vanishing cap energy: Σ's flux and cap
energy are finite and vanishing for a_0 < 1, W3, W5). Then on S: h|_S − Σ|_S ∈ ρ^(ℓ0)H_b^(k_0 − c) and
∂h|_S − ∂Σ|_S ∈ ρ^(ℓ0+1)H_b^(k_0 − c) (c a fixed number of commutations), with Σ|_S polyhomogeneous with exponents in
ℰ_0^½; the data (γ, k) of g_λ on S lie in III.K's half class with ℓ0 ∈ (3, 4) ∖ {7/2}, the coefficients at ρ², ρ³
O(λ), at ρ^(5/2) O(λ^∞) (round 1). What is not written: the bootstrap over |α| assembled line by line, and (V).
[R5.0 (r3-m2, r3-m3): H_b^∞ is delivered by Theorem R4.6's Steps 7 and 9 (with R5-B); the data on N need the means
through r^(−4), Lemma R4.4 at J = 8 (R4-C).]

The window widens round 2's: ℓ0 ∈ (3, 4) ∖ {7/2}, all of Part VII's range, which R2.4 now covers (H2 to M ≤ 12).

### R3-E The theorem that results

**Theorem R3.7 (conditional; deduced).** Fix A, the C_c^∞ envelope of Theorem 1, the angular profile and the seed. Let
ℓ0 ∈ (3, 4) ∖ {7/2}, ℓ_I ∈ (3, ℓ0) off row d2's exclusion sets, ε_m > 0, ε_t < ε_K; let ε, d_1 be III.K Theorem 4.3's in
the half class, k_0 large enough for the H^(d_1) norm, a ∈ (max(ℓ0 − 1, 5/2), 3), a_0 ∈ (0, ½), M := M(8, k_0 + 1,
k_0 + 1) = 27 + 2k_0 (Proposition R3.1), and K > max(d_1 + 14, K*(a, 8, M, k_0), K*(a_0, 8, M, k_0)). Assume:
[R5.0: K*(a_0, ...) is superfluous; the window is a ∈ (ℓ0 − 1, 3); the G-invariance Proposition 3.2 needs is R5.0
(r3-m4). Theorem R5.1 restates this theorem.]

- (Pr) Propositions 9.8 and 9.9 at order k_0 + 4 (deduced from 10.51's reading, R3-B (e), (g); not read line by line);
  [R5.0 (nit): at order k_0 + 5 (R3.1 at n = k_0 + 1).]
- (B) the bootstraps of Propositions R3.4 and R3.6 written out from the identities computed here;
- (V) the limit is vacuum (Proposition R3.4).

Then there is λ_2 ∈ (0, λ_P(K)] such that for every 0 < λ ≤ λ_2 (no exceptional set) g_λ continues to W as a vacuum
metric whose data on Σ_IVP lie in III.K's class with ℰ_0 = ℰ_0^½ and norm < ε in H^(d_1), and the conclusion of
Theorem R2.10 holds: the development of g_λ's own data settles to a Tangherlini metric g_(m′,0),
|m′ − μ_end| < ε_m, at the rate O(t_*^(−2−ε_t)), by Theorem R2.4 (whose Part IV condition is discharged, R3-A), with no
gluing. *Proof.* R3.4 (continuation), R3.6 (the class on S), Lemma R3.2 and R3.1 (smallness), Theorem R2.4 and Part
VII Proposition 3.2 (settling), as in R2.10. ∎

### R3-F Findings, ledger, what remains

Findings:
1. (P4) is discharged by citation: Part IV's seven outputs are listed as proved, and none depends on ℰ_0 beyond row
   d1 (R3-A).
2. (Poly) holds on the far region with M(J, n, m) = (J² − J)/2 − 3 + n + m, K-independent (Proposition R3.1), given
   Proposition 9.8 at order n + 4; with Lemma 11.0 as written, still polynomial (P(N) ≤ 9N/4). The data constants are
   C(λ, j) ≤ C_j λ^(−(j+1)). The only non-polynomial factor in the record's fixed-λ arguments is the near region's
   smoothness argument (e^(C/λ)), which (11.7) does not use.
   [R5.0 (r3-m7): an upper bound; B_J ≤ 3J − 9 derived (Proposition R5.4).]
3. F1: Lemma 11.0's proof treats a top-order term −½λ^(−1)(∂^γ u_1)(ℓ,ℓ)[∂_θ²W_TT] as a lower-order source; it belongs in
   Lemma 9.5's kernel, where on the far region it costs e^(2C). Finding for N1STAR-PROOF.md (not edited here).
   [Withdrawn, R5.0 (r3-M1); see R4-B and R5-D.]
4. M1 repaired: e's coefficients by interpolation, the commuted fluxes from Propositions 9.8-9.9 at order k, and the
   threshold K* (Lemma R3.2), which R2.10's K − 4 > as does not imply.
5. (b1)'s mixed problem is not needed: J^−(N) lies in {v ≤ V′_P − h(T) − δ_0/2} on Σ_T, inside P′, so the
   truncations are Cauchy problems with g_λ's own data there, and N's data are attained by uniqueness (Lemma R3.3).
6. The Z-commuted equation is exact and nonlinear: (R3c), verified at 4.7 × 10^(−41); the commutator defect is the
   μ-derivative of the operator.
7. The window for g_λ's data widens to ℓ0 ∈ (3, 4) ∖ {7/2} (Hardy on S, q = 9/2).

Ledger. Computed: `poly5.py` P1-P9 (28 checks), `scale5.py` Z1-Z8 (25), `trunc5.py` T1-T8 (23), all with failing
controls, and round 2's amended programs. Deduced: Propositions R3.1, R3.4 (outline with computed identities), R3.5,
R3.6 (same), Lemmas R3.2, R3.3, Theorem R3.7 (conditional). READ: PART-III-K-NONLINEAR.md:468, 510-518;
proof5/README.md:77-84; PART-IV3-NM.md:60-61, 229, 321, 382; PART-IV4-SLAB.md:86, 128, 148-149;
PART-IV5-CDMODES.md:154; PART-IV6-SOLV.md:742; PART-IV7-TFACE.md:348, 387; N1STAR-PROOF.md (as of 82a7e95) 1046,
1052-1054, 1069-1078, 1234, 1348-1354, 1371, 1404-1405, 1423-1426, 1433-1440, 6776-6801, 10550-10551, 10563-10566,
10625; BEYOND5.md:203-205, 300-301; PART-VII-ASSEMBLY.md:69-92, 162-177. None from outside sources.
[R6 (m7): PART-III-K-NONLINEAR.md:468, 510-518 is now 471, 513-521 (md5 5b0ad3f0).]

Open, precisely: (B) the two bootstraps on W written line by line (their identities, kernels, data and caps are
computed here); (V) the vacuum condition of the limit (section 0.7's system with D = 0 on N; deduced); (Pr)
Propositions 9.8-9.9 read at order k > 6 (deduced from 10.51); R5 (λ_1, δ not evaluated; another workstream). Not
open any more: (P4), (Poly), the mixed problem, the commutators, (N2)'s identity, the Z-commuted equation.
[R5.0 (r3-m6): read (P4) discharged by citation; (Poly) reduced to (Pr), discharged by R4.1-R4.2; the mixed problem not
needed (R3.3 (ii)).]

N1STAR-PROOF.md moved during this round (e50e9bc, then 82a7e95); every number above is as of 82a7e95.

**Next step.** (V) is the shortest: the system of section 0.7 on W, with the band's constraint defect estimated by T2's
count at the order of D (one derivative more). Then (B) for Proposition R3.4, from round 2's outline and (R3a).

    python3 checks/poly5.py      (about seven minutes; P4 most of it)
    python3 checks/scale5.py     (about three minutes; Z1-Z2 most of it)
    python3 checks/trunc5.py     (about two minutes; T3 most of it)

## Round 4 (2026-11-02)

Status: written; not yet read by a verifier. Labels as in rounds 2-3. New programs, each with its `.out` from a full
run and with controls that mutate the code under test (the rule, the operator, the formula or the field), so that the
claim checked fails under the mutation: `checks/order5.py` (O1-O5, (Pr)), `checks/f1lemma5.py` (F1a-F1e, F1),
`checks/boot5.py` (B1-B13, (B)), `checks/vac5.py` (V1-V2, (V)). N1STAR-PROOF.md is cited as of 2a69924, where it last
changed (from 82a7e95 only lines 631-640 moved, three lines added: numbers below 631 are 82a7e95's, numbers above are
82a7e95's + 3; md5 f436ef75...2fbe2da3b); proof5/ as of 03d4fba. Sections R4.0 and R4-A … R4-G,
statements R4.1 … R4.10, equations (R4a)-(R4e).

What this round settles, in one paragraph. (Pr) holds at every order k: Propositions 9.8 and 9.9 are read line by line
and the order enters only through constants and through the approximant's order N(k) (R4-A). F1 is restated (the term
at the energy's own order is the Q-part's b . dU, not the λ^-1 term, which is one order lower) and repaired by exact
replacement text for N1STAR-PROOF.md (R4-B). The existence bootstrap at weight a_0 < 1/2 planned in R2.5 and R3.4 does
not close (Proposition R4.7: its top-order quasilinear kernel is (1 + |σ|)^(-a_0-1/2), and neither factor of the
estimate can be improved in its class); it is not needed: the continuation, its expansion and the class on S come from
one bootstrap at weight a in (max(ℓ0 - 1, 5/2), 3), written line by line (R4-D), whose data on N also need the
approximant's means expanded through r^-4 at past null infinity, a gap in R3.6 closed by Lemma R4.4; uniqueness holds
in the weight-a_0 class (Proposition R4.8); and the limit is vacuum (R4-F). Theorem R4.10 then states R3.7's conclusion
with (Pr), (B) and (V) discharged. Not done here, by assignment: R5 (λ_1 and δ are not evaluated).

### R4.0 The verifier's reading of round 3

No finding had been forwarded when this round was written. Findings that arrive are seated here as "R4.0 (verifier
...)", each with its disposition.
[R5.0: both readers' findings, round 3's and round 4's, are seated in R5.0.]

### R4-A (Pr): Propositions 9.8 and 9.9 at every order

*Where k enters (READ).* Proposition 9.8 (N1STAR-PROOF.md:1341-1361): E(τ) := sum_(i + |β| ≤ k) λ^i ||d^i
Ω^β d w_n|| ≤ M_F λ^K' t^(-1/2) (9.8), proved for the k of Theorem E (k = 6, section 0.4). Its proof uses k
in (i)-(v) (1350-1358), in Lemma 9.3(a) (1114-1116: the cost of three) and in Step 8 (1360-1361). Proposition 9.9
(1363-1418): N_P at order k, β0 "depends only on the constants C of (9.9) below at the orders j ≤ k" (1374), "every
line holds at every order j ≤ k with c0 unchanged" (1407-1408), N = K + 4 + ceil(4 β0) (1052-1053, 1324).

**Proposition R4.1 (Proposition 9.8 at order k; deduced, computed O1-O2).** For every k ≥ 6 and every K' > 5 there are
λ_F(k) > 0 and M_F(k), independent of τ_n, such that the conclusions of Proposition 9.8 hold with (9.8) at order k.

*Proof.* Each step of 9.8's proof, with its dependence on k. (a) The bootstrap E ≤ 2 M_F λ^K' t^(-1/2) gives, by
Lemma 9.3, |w_n| ≤ C M_F λ^(K'-3) t^-2 and |d w_n| ≤ C M_F λ^(K'-4) t^-2 (orders 0 and 1, which need k ≥ 3),
hence the margin of Lemma 9.1(f) and, by Lemma 9.2, w_n = 0 on {v ≤ v_start}: independent of k. (b) The commuted
equation λ^i d^i Ω^β [P(w) = F + N(w)], i + |β| ≤ k: (i) λ^-1 |s G2|_(k,P) ≤ C_k λ^-1 t^(-3/2) E by
Leibniz, every factor λ^(i2) d^(i2) Ω^(β2) G2 being bounded by C_k t^(-3/2) (G2 = [∂_th^2 g1], a profile in
E_(3/2), the chain rule (0.3)), and every factor λ^(i1) ||d^(i1) Ω^(β1) s|| by C E (for i1 = 0 through Lemma
9.3(b): s = w(ℓ, ℓ) vanishes on {v = v_start}, [Ω, ∂_r] = 0 and Ω^β(ℓ ℓ) is bounded); (ii) B . d w,
C . w: C_k t^(-3/2) E (profile coefficients in E_(3/2)); (iii) the commutators [λ^i d^i Ω^β, g^(ab) ∂_a ∂_b]:
the g_app part as in the record (λ^i d^i g_app in λ E_(3/2) for i ≥ 1; [Ω_ab, □̃] = 0, O4d), the w part a
sum of products d^(i') w . d^(j - i' + 1) d w; (iv) the nonlinear terms N(w), monomials of total w-order at most j + 2
with no factor of order j + 2 (that is the principal part). For (iii)-(iv) the split "factor of highest w-order in L^2,
every other factor in sup through Lemma 9.3(a)" exists exactly when k ≥ 5 (O1a: enumerated for k = 5..200, the
second-largest w-order being at most floor((k + 2)/2) ≤ k - 2, O1b); so both are at most C_k λ^-5 t^(-3/2) E^2 at
every k ≥ 6 (the record's λ^-5 is an upper bound: the scaled product costs λ^-3, the 1/λ monomial λ^-1 w w G2
one more). Control: with the cost of four in place of three the minimal k is 7 (O1c); with the split reversed no k
works (O1d). (v) |F|_(k,P) ≤ C_R(k) λ^K' t^(-3/2): Theorem A_P's residual λ^(N-1) [R_N] + λ^N [R'_N] with R
in E_3 with all derivatives (1243-1245), in the scaled norm by (0.3). (c) Lemma 9.5 with the kernels C_k t^(-3/2) and
C_k λ^-1 t^(-3/2): over t ≥ λ^-2 they integrate to 2 C_k λ and 2 C_k (O2a); the data at τ_n are E(τ_n) ≤
C_k |F|_(k,P)(τ_n) (w_n = ∂_τ w_n = 0 there, the higher τ-derivatives from the equation); Gronwall gives E(τ)
≤ C_k e^(2 C_k (1 + λ)) (2 C_R(k) λ^K' + C_k M_F^2 λ^(2K'-5)) t^(-1/2) ≤ M_F(k) λ^K' t^(-1/2) with M_F(k) :=
4 C_k e^(6 C_k) C_R(k) + 1 and λ ≤ λ_F(k), since K' > 5 (O2b-O2d; control O2c: K' = 5 does not close). (d)
Existence and continuation: Step 8 with [DS23] Theorem 2.4 at r = k > 3 (10.51(a), 6786-6791). Nothing else depends on
k. ∎

**Proposition R4.2 (Proposition 9.9 at order k; deduced, computed O1, O3-O4).** For every k ≥ 6 let C(k) be the sum of
the constants of the lines of (9.9) at the orders j ≤ k, β0(k) := max(2, 4 C(k) + 1), and let the approximant have
order N = K + 4 + ceil(4 β0(k)), K ≥ 6. There are λ_N(k) > 0 and M_N(k) such that (9.9a) holds at order k:
N_P(τ) ≤ M_N(k) λ^K' t^(-1/2) (T/t)^β0(k) on [τ_T, τ0], and N_P(τ0) ≤ M_N(k) λ^(K' - 2 β0(k)).

*Proof.* 9.9's proof (1379-1418) at order k. (a) The data: N_P(τ_T) ≤ C' E(τ_T) by Proposition R4.1 at order k.
(b) Lemma 9.4b is stated for every j ≤ k (1143). (c) The transports keep c0 at every order: [Z, L0] = 0 for Z in
{∂_τ, ∂_r, Ω} and [∂_r, r^-c] = -c r^(-c-1), [Ω, r^-c] = [∂_τ, r^-c] = 0 (O4a-O4b; control O4c: the
Cartesian ∂_1 does not commute with L0, which is why N_P's Z are these). (d) The bootstrap integrals: for β > 1 and
a > -β, ∫_t^T t'^(-1-a) (T/t')^β dt' = T^β (t^(-a-β) - T^(-a-β))/(a + β) ≤ t^(-a) (T/t)^β /
(β + a), and log(T/t) ≤ (T/t)^β/β (O3a-O3b; control O3b': without the factor (T/t)^β the log of the
Q'-line is unbounded), so each integral returns C(k)/(β0(k) - 1) ≤ 1/4 of its bound (O3c). (e) The nonlinear terms
R_nl at order k by Lemma 9.3(a) and the split of R4.1 (b) (O1): C_k λ^-5 t^(-3/2) (B λ^(-2 β0 - 1))^2, whose
contribution C B^2 λ^(-8 - 4 β0) is below B/2 for λ small exactly because K' = N - 1 > 8 + 4 β0(k), which N
= K + 4 + ceil(4 β0(k)) gives for every K ≥ 6 (O3d; control O3e: with ceil(2 β0) in place of ceil(4 β0) it
fails at K = 6, β0 = 4). (f) The margin of Lemma 9.1(f) as in R4.1 (a). ∎

**Corollary R4.3 (Theorem P at order k; deduced, computed O5).** For every k ≥ 6 and K ≥ 6, with N(k) := K + 4 +
ceil(4 β0(k)), there is λ_P(K, k) > 0 such that for λ ≤ λ_P(K, k) Theorem P's g_λ satisfies (9.8) at order
k on the far region and (P-iii) at order k: |d^i(g_λ - g_app^(N(k)))| ≤ C_k λ^(K-3-i) t_P^-2 on P, i ≤ k - 3.

*Proof.* The proof of Theorem P (1419-1449) at order k: Data(w_n) at τ0 by R4.2; Theorem E at order k (10.51); the
limit n → ∞, the bounds at order k inherited by weak lower semicontinuity (for each τ the family λ^i d^i
Ω^β d w_n(τ), i + |β| ≤ k, is bounded in L^2(A_P(τ)) uniformly in n; a subsequence converges weakly; its
limit is the distributional derivative of the C^(k-5) limit, and norms do not increase). The solution built at order k
is g_λ: g_app^(N(k)) - g_app^(N(6)) = sum_(j > N(6)) λ^j [g_j] is λ^N(6) (1 + O(λ)) t^(-3/2) in C^1 (O5b),
inside the uniqueness class of (P-v) (1055-1057). ∎

*So (Pr) is discharged at every order.* No order fails; what grows with k is the approximant's order N(k) (O5a: N =
22, 30, 62, 174 at C(k) = 1/2, 1, 3, 10, K = 6) and λ_P(K, k) shrinks. Proposition R3.1's input "Proposition 9.8 at
order n + 4" (R3-B (e)) and R3-B (g)'s "(9.9a) at every order k" are now Propositions R4.1-R4.2, no longer "deduced, not
read line by line".

### R4-B F1: what is at the top order in Lemma 11.0, and the replacement text

*R3-B (b) corrected.* Lemma 11.0's induction (N1STAR-PROOF.md:10551-10579) controls, at the step |γ| = j + 1, the
energy ||d U|| of U := d^γ u_1, the derivatives of u_1 of order j + 2; the energies of the lower steps already
control those of order ≤ j + 1, U itself among them. F_1 = S(u) - (1/2)(g_λ^(ab) - g0^(ab)) ∂_a ∂_b u_1 + (1/2) □̃
(r^(-3/2) G_3) equals -Ric^H(g_λ) - (1/2) g_λ^(ab) ∂_a ∂_b u_1 by (0.2), so (computed on the full five-dimensional
operator, `f1lemma5.py`, 80 digits): (F1a) it has no second derivative of u_1 (the Hessian coefficient vanishes to 6e-53
relative; control: in the □̃ form the coefficient remains); (F1b) its coefficient of u_1 is c = -(1/2) λ^-1
(.)(ℓ, ℓ) [∂_th^2 W_TT] + O(1) (the remainder stays bounded at λ = 1e-2, 1e-3, 1e-4 while the λ^-1 term reaches
4.6 x 10^3; the λ^-1 part is exactly the ℓ-ℓ one; control: with a non-oscillating wave the test fails); (F1c) its
coefficient of d u_1 is b, of λ-order 0 and nonzero (control: b = 0 for g0 = η without the wave). By the chain rule
(F1d), d^γ F_1 = b . d U + c U + (derivatives of u_1 of order ≤ j + 1). So: **the term at the energy's own order is
b . d U, from Q, which the written proof counts among "the orders already controlled"**: that is the gap. The term
-(1/2) λ^-1 U(ℓ, ℓ)[∂_th^2 W_TT] that R3-B (b) and R3-F (3) named is one order lower: the energies of the lower
steps bound ||U||, and the written proof closes with it in the source, at the cost of one λ^-1 per order (F1e''). The
repair puts both in Lemma 9.5's kernel: k = C(1 + λ^-1) t^(-3/2), whose integral over the far region is 2C(1 + λ)
(F1e; control F1e': over [1, λ^-2] it is exp(2C(1 + λ^-1)(1 - λ))). That also makes Proposition R3.1's count "+1
per order for F1" (P7) an overcount; R3.1's exponent stays an upper bound.
[R5.0 (r4-m1, r4-m8): with an envelope on the wave c's remainder is in E_(3/2), not O(1) E_2 (cclass5 C1-C2); F1c shows
only b ≠ 0, the λ^0 wave part of b is cclass5 C3.]
[R6 (nit): R5-D's mechanism is the one written, through the source of (9.3) before Gronwall's lemma; "kernel" here means
the Gronwall exponent, and the factor is the same (R6.0, nits).]

*The replacement text* (for N1STAR-PROOF.md, not edited here; two edits, old strings quoted exactly from the file as of
2a69924, each new string ending so that the unchanged continuation of its last line stays within 121 characters).
[Superseded by R5-D (the round-4 reader's m1, m2).]

Edit 1, old (lines 10551-10560, up to "in L^2."; it occurs once):

```text
*Proof.* By Lemma 11.1 below, u_1 = u - r^(-3/2) G_3 solves -(1/2) g_lam^{ab} d_a d_b u_1 = F_1 := S(u) - (1/2)
(g_lam^{ab} - g0^{ab}) d_a d_b u_1 + (1/2) box~ (r^(-3/2) G_3), and F_1 is in E_3 with all derivatives (S(u) by Lemma
11.1; the second term is E_(3/2) E_2; the third is in E_(7/2) by Lemma 9.7(c) and P2), where "all derivatives" of a term
containing u_1 means the orders already controlled. Induction on the order: for |gamma| = j + 1, U := d^gamma u_1 solves
-(1/2) g_lam^{ab} d_a d_b U = d^gamma F_1 + sum_{0 < gamma' <= gamma} (d^{gamma'} g_lam^{ab}) d^{gamma - gamma'} d_a d_b
u_1. The terms with |gamma'| = 1 are (d g_lam) d U with d g_lam in E_(3/2), of the kind Lemma 9.5's kernel k absorbs; a
term with |gamma'| >= 2 is a product of a derivative of g_lam of order <= j + 1 with one of u_1 of order <= j + 1, and is
estimated in L^2(Sigma_tau) with the factor of higher order in L^2 (the energies of the lower steps, at most C t^(-1/2))
and the other in sup norm (E_2 by the induction hypothesis, through Lemma 9.3 for the orders it costs, and by Theorem P
for the lowest), so the source is at most C(lam, j) t^(-3/2) in L^2.
```

Edit 1, new:

```text
*Proof.* By Lemma 11.1 below, u_1 = u - r^(-3/2) G_3 solves -(1/2) g_lam^{ab} d_a d_b u_1 = F_1 := S(u) - (1/2)
(g_lam^{ab} - g0^{ab}) d_a d_b u_1 + (1/2) box~ (r^(-3/2) G_3). By (0.2), F_1 = -Ric^H(g_lam) - (1/2) g_lam^{ab} d_a
d_b u_1 with g_lam = g0 + r^(-3/2) G_3 + u_1, so F_1 contains no second derivative of u_1 (`checks/f1lemma5.py` F1a):
it is a smooth function of (X, u_1, d u_1), in E_3 with all derivatives at u_1 = 0 (the terms of Lemma 11.1 in G_3 and
g0, and the third term, in E_(7/2) by Lemma 9.7(c) and P2), and along g_lam its partial derivatives are b := dF_1/d(d
u_1), in E_(3/2) and of lam-order 0 (Q's derivative, linear in d g0 + d u, with d u = dv [d_th W_TT] + O(lam)), and c :=
dF_1/d u_1 = -(1/2) lam^-1 (.)(ell_lam, ell_lam) [d_th^2 W_TT] + E_2, ell_lam := g_lam^-1 dv (from -(1/2)(g_lam^-1 u_1
g_lam^-1)^{ab} d_a d_b (lam [W_TT]), as in (3.2); F1b-F1c). Induction on the order: for |gamma| = j + 1, U := d^gamma
u_1 solves

    -(1/2) g_lam^{ab} d_a d_b U - b . d U - c U
        - sum_{|gamma'| = 1} (d^{gamma'} g_lam^{ab}) d^{gamma - gamma'} d_a d_b u_1 = R_gamma,

where, by the chain rule (F1d), R_gamma := d^gamma F_1 - b . d U - c U + sum_{|gamma'| >= 2} (d^{gamma'} g_lam^{ab})
d^{gamma - gamma'} d_a d_b u_1 contains derivatives of u_1 of order <= j + 1 only. On the left, b . d U is of the order
this step estimates and is not a source; the terms with |gamma'| = 1 are (d g_lam) d U' with d g_lam in E_(3/2) and U'
in the same family {d^gamma u_1 : |gamma| = j + 1}; and c U is one order lower. Lemma 9.5's identity, summed over the
family, takes all three into its kernel: ||b . d U|| <= C t^(-3/2) ||d U||, and ||c U|| <= C lam^-1 t^(-3/2) ||U|| <= C
lam^-1 t^(-3/2) ||d U|| by Lemma 9.3(b) (U vanishes on {v = v_start}); the kernel is k = C(1 + lam^-1) t^(-3/2), whose
integral over the far region t >= lam^-2 is at most 2C(1 + lam) (F1e), a lam-free factor. (With c U taken as a source,
through the energies of the lower steps, the step also closes at fixed lam, at one lam^-1 per order.) Each term of
R_gamma is a product of a derivative of g_lam or of F_1's coefficients of order <= j + 1 with derivatives of u_1 of order
<= j + 1, estimated in L^2(Sigma_tau) with the factor of higher order in L^2 (the energies of the lower steps, at most C
t^(-1/2)) and the others in sup norm (E_2 by the induction hypothesis, through Lemma 9.3 for the orders it costs, and
by Theorem P for the lowest), so ||R_gamma|| <= C(lam, j) t^(-3/2).
```

Edit 2, old (lines 10569-10570, from "Lemma 9.5's identity" to "uniformly in n."; it occurs once):

```text
Lemma 9.5's identity then gives ||d U_n(tau)|| <= ||d U_n(tau_n)|| +
C int_{tau_n}^tau t'^(-3/2) dtau' <= C(lam, j) t^(-1/2) at every order, uniformly in n.
```

Edit 2, new:

```text
Lemma 9.5's identity with that kernel and Gronwall's
lemma give sum_{|gamma| = j + 1} ||d U_n(tau)|| <= C e^(2C(1 + lam)) sum_{|gamma| = j + 1} (||d U_n(tau_n)|| +
int_{tau_n}^tau ||R_gamma^n|| dtau') <= C(lam, j) t^(-1/2) at every order, uniformly in n.
```

(Edit 1's last line is followed by " The identity is not run on the region between {v =" of line 10560; Edit 2's first
line continues "U_n(τ_n)|| ≤ C(λ, j) t_n^(-1/2) with t_n ≥ t. " of line 10569 and its last is followed by " The
bookkeeping of sup against" of line 10570. Applied to a copy of the file both edits leave every line within 121
characters and nothing else changed (checked). R_γ^n is R_γ for u_1^n.)

### R4-C The means at past null infinity: a gap in R3.6's data, closed

R3.6 takes "the data on N small by Lemma R3.2 at weight a". Lemma R3.2 bounds e = g_λ - g_app only. On N, h_R :=
g_λ - g_b0 - Σ is, by linearity of the coefficients, the sum of e's remainder and sum_j λ^j (m_j minus its
coefficients through r^-4): its weighted flux at a > 5/2 is finite only if the means m_j (λ-independent, Part VII
Lemma 1.1) have expansions through r^-4 with remainders O(r^(-9/2)) and their ℓ-gain. Theorem A_P gives m_j in L_2,
the leading term only (1235-1246).

**Lemma R4.4 (the means; deduced, computed B9, B13).** For every stage j ≥ 1 and J ≥ 4 there are smooth
λ-independent tensors M_(j,k)(v, x̂), k = 4, ..., J, vanishing for v ≤ v_start, with m_j = sum_(k=4)^J r^(-k/2)
M_(j,k) + m_(j,J) and ∂_X^α Ω^β ℓ^m m_(j,J) in E_((J+1)/2 + m) on the far part of P+, with constants
independent of λ; no logarithm occurs; for v ≥ v_end every M_(j,k) is a polynomial in v, and for k ≤ 9 the
M_(j,k) satisfy there the flat recursion (2q - 3) M_(j,2q)' = (Δ̊ + (q - 1)(q - 3)) M_(j,2q-2), so M_(j,k) has degree
at most floor((k - 4)/2).
[R5.0 (r4-m7): "no logarithm" rests on Theorem A_P's coefficient classes (N1STAR-PROOF.md:1266-1269 now), computed in
r5settle5 H; B13 is [arithmetic].]

*Proof.* Induction on the stage j and, within it, on J, as Proposition 11.1, for the stage system (a)-(c) of Lemma 5.3
(N1STAR-PROOF.md:521-540) on P (Theorem A_P), whose coefficients and sources are polynomials in the earlier stages'
profiles (expanded by the induction) and in W_TT, χ, g0 (exact: W_TT = r^(-3/2) F, χ = r^-2 X(v, th, s), g0 - η
= μ r^-2 dv dv; 1235-1268). (a) is Lemma 11.2 with g0 in place of g_λ (no quasilinear term): u~ = m_j, the source
r^-q S_q + S~ with q ≥ 3 (Theorem A_P's count: every monomial of the stage sources lies in L_3, 1248-1268), (H_m) from
the induction. (c) is the transport of Lemma 9.7(d), iterated: at each order the leading term -r^(1-q) S_q/(q - 5/2)
and a remainder whose source gains 1/2. (b) is L0 φ_j = -(1/2) m_j(ℓ, ℓ) - (1/2) q_j, integrated along ℓ from
past null infinity: r^-q S → -r^(1-q) S/(q - 1). The thresholds q = 5/2 (Lemma 11.2: 2/(2q - 5); Lemma 9.7(d):
1/(q - 5/2)) and q = 1 ((b)) are never met: the sources of (a) and (c) start at q = 3 and those of (b) at q = 2, and
each order adds 1/2 (B13a, to exponent 12; control B13b). After the shell every oscillating profile vanishes (Part VII
Lemma 1.1, PART-VII-ASSEMBLY.md:122-130) and μ = μ_end; the stage sources are then products of earlier means and
μ-terms, every one O(r^-6) (two factors r^-2 and two derivatives, ∂_v of a leading coefficient vanishing by
induction; -(μ/r^2) ℓ ℓ and Γ[g0] d each add r^-2 and r^-3 to r^-2), so they enter only from q = 6 (k = 10):
through k = 9 the coefficients obey the flat recursion of Lemma 11.2, which raises the degree in v by one every second
order (B9b), and from q = 6 on products of polynomials and the constant μ keep them polynomial. ∎
[R5.0 (r4-m11): Part VII Lemma 1.1 concerns Ω'; on P the transfer is the transport from past null infinity at fixed v >
v_end, with zero data and zero sources there (R5.0).]

**Lemma R4.5 (the data on N at weight a; deduced, computed B9, B12).** Let a in (5/2, 7/2), k1 ≥ 0 and Γ in {∂_t,
L_Ω, Z}. (i) At fixed λ the commuted flux of h_R through N at weight a, |α| ≤ k for any k, is finite. (ii) It
is at most C(λ^2 + ν(λ)) with ν(λ) → 0 as λ → 0 for |α| ≤ k1, once K > K*(a, 8, M, k1) of Lemma
R3.2, M := M(8, k1 + 1, k1 + 1) of Proposition R3.1.

*Proof.* On N, s = 0 and Σ = sum_(k=4)^8 r^(-k/2) G_k(v1); ∂_t^i Σ = sum_(p) r^(-p-i) F_p^(i)(0), and the
fixed-v expansion of r^-p F_p((v - v1)/r) is sum_m r^(-p-m) F_p^(m)(0)(v - v1)^m/m!, which is the solution of the flat
recursion with data G_(2p)(v1) (B9a: the 2F1 coefficient ratio equals the recursion's, symbolically in p, l, m; control
B9a'': third parameter p + 1/2). After the shell G_k obeys the flat recursion for k ≤ 9 (B9b; Lemma R4.4 for the means,
and the same count for g_λ - g0, whose sources after the shell are O(r^-6) too), so the r^(-k/2) coefficients of ∂_t^i
(g_λ - g_b0) and of ∂_t^i Σ agree on N for k ≤ 8 and every i: h_R and every ∂_t^i h_R are O(r^(-9/2)) on N with
their ℓ-gain, Z = r ℓ and Ω being tangent (scale5 Z6). (i): Proposition 11.1 at fixed λ; flux at weight a
finite for a < 7/2 (R2.8, Z5); the N-flux for the metric g = g_b0 + H, H = O(λ r^-2), contains besides (ℓ φ)^2 and
|r^-1 Ω φ|^2 (exact for g_b0, the null hypersurface) the term |H| |d φ|^2, whose weighted integral is ∫ λ
r^(2a - 8) dr < ∞. (ii): the means' part is sum_j λ^j (m_j's remainder), λ-independent per j by Lemma R4.4,
O(λ^2) in flux; e's part tends to 0 by Lemma R3.2, its inputs (P-iii) and (9.9a) at order k1 + 4 now being Corollary
R4.3 and Proposition R4.2. ∎
[R5.0 (r4-m12, nit): off N the band also carries Σ's terms beyond r^(−4), O(λ r^(−9/2)), not λ-independent per j (the
O(λ^2) bound stands); the order is k1 + 5.]
[R6 (m3): the lemma holds for every a in (0, 7/2); nothing in its proof uses a > 5/2 (R6-B).]

### R4-D (B): the bootstrap on W at weight a, line by line

*Setting.* μ := μ_end; R ≥ R_3 so large that on r ≥ 4R, |f'| ≤ 1/2 and μ/r^2 ≤ 1/16 (R is free in Part VII
Lemma 1.2, PART-VII-ASSEMBLY.md:140; f' in |x|^-2 C^∞, 177). Kerr-Schild Cartesian (t, x), g_b0 = η + μ r^-2 k k.
W = {v ≥ v1, t ≤ f(r)} (BEYOND5 Lemma 6.4 (iv), BEYOND5.md:198-205). t̃ := t - f(r), Σ̃_σ := {t̃ = σ}
cap W (σ ≤ 0; Σ̃_0 = S); on it v increases along the rays r → (f(r) + σ, r ω) (B4c), Σ̃_σ cap
W = {r ≥ r_σ}, r_σ ≥ |σ| - C, and |t - v1| ≤ r on W (B4e). Fix ℓ0 in (3, 4) ∖ {7/2}, a in (max(ℓ0 - 1,
5/2), 3), k1 := max(8, d_1 + 4). Σ := sum_(p in Pi) r^-p F_p(s, x̂), Pi := {2, 5/2, 3, 7/2, 4}, s := (v - v1)/r,
with F_p(0, .) = G_(2p)(v1, .) (Proposition 11.1): for p ≤ 7/2 the regular solution of the flat degree -p equation,
harmonic by harmonic sum_l G_(2p,l)(v1) 2F1(p + l, p - l - 2; p - 1/2; s/2) Y_l (round 1 T2; at s = 0 the other
exponent is 3/2 - p < 0, BEYOND5 D530), convergent with all derivatives on s in [0, 3/2] (the 2F1 grow at most like a
power of l there, B9c, and G_(2p)(v1, .) is smooth), W lying in {s ≤ 1 + C/r} subset {s ≤ 3/2}; F_4 the regular
solution of the degree -4 equation with the degree -6 source of μ r^-2 F_2 and of the quadratic terms in r^-2 F_2.
Weight w := (u* - u)^(2a), u := t - r, u* := 2 sup f - v1 + 1, so r ≤ u* - u ≤ 2r + C on W. Commutators Γ in
{∂_t, L_Ω_ij, Z}, Z := (t - v1) ∂_t + x.∂_x on components; for a multi-index α, Γ^α their product. H :=
Σ + h_R, g := g_b0 + H, P(h) := Ric^H(g_b0 + h; g_b0).
[R5.0 (r4-m3): r ≤ u* − u fails for this u*; u* := sup_W f + 1 (r5settle5 E1). eps here is eps_B (r4-m10).]
[R5.0 (window): a ∈ (ℓ0 − 1, 3); nothing needs a > 5/2 (r5settle5 G5).]

*The truncations.* For T ≤ T_1 the Cauchy problem on Σ̃_T with data (g, ∂_t g) equal to g_λ's on {v ≤ V_T},
V_T := V'_P - h(T) - δ_0/2, to (1 - χ_T) g_λ + χ_T (g_b0 + Σ) on the band {V_T ≤ v ≤ V_T + δ_0/2},
and to g_b0 + Σ beyond (χ_T smooth, 0 below the band, 1 above). Lemma R3.3 holds with Σ̃_T in place of
{t = T} (its proof uses only that the slice is spacelike with margin and lies in P' ∪ Ω' ∪ W, and the time
functions Φ_P = v + h(τ) and v + ε(τ - τ0)): the solution g_T equals g_λ on {v ≤ v1, t̃ ≥ T} cap (P' cup
Ω'), so N cap {t̃ ≥ T} carries g_λ's data. On W, Φ_W := v + 1/r is a time function for every g with |g^-1 -
g_b0^-1| ≤ r^-2/2 (g_b0^-1(dΦ_W, dΦ_W) = -2 r^-2 + r^-4 (1 - μ r^-2), B2d), which localises the problem as in
R3.3 (iii): data equal to g_b0 beyond v = V_* + 2, the record's local theory (Step 8, 412-456) on bounded pieces, the
solutions for V_* → ∞ agreeing on overlaps.
[R5.0 (r4-M4): these data make h_R = −Σ beyond V_* + 2, of infinite weighted energy for a ≥ 1 (r5settle5 F4); the
localisation is replaced in R5-B, which leaves the data unchanged and localises the energy identity.]

*The quantities.* For σ in [T, 0], with T_g[φ] the energy-momentum tensor of a function φ for g,

    E_σ[φ] := ∫_(Σ̃_σ) √|g| T_g[φ](X, -∇ t̃) d^4x,   X := w ∂_t,                        (R4a)
    F_N[φ; T, σ] := ∫_(N cap {T ≤ t̃ ≤ σ}) √|g| T_g[φ](X, -∇ v),
    𝔈_k(σ) := sum_(|α| ≤ k) sum_(i ≤ j) E_σ[(Γ^α h_R)_ij],   𝔉_k likewise with F_N.

**Step 1 (the margins; computed B1-B2).** If |H| ≤ 1/50, then on r ≥ 4R: c1 w |d φ|^2 ≤ √|g| T_g[φ](X, -∇
t̃) ≤ c2 w |d φ|^2 with c1 = 0.24, c2 = 0.76 for X = ∂_t (B1a; control B1c: |f'| = 3/2 gives a negative value),
√|det g| in [0.9, 1.1] (B1b). If |H| ≤ μ/(2 r^2), -∇ u and ∂_t are future timelike (B2a-b; control B2c), so the
bulk term T(∇ w, ∂_t) = |w'| T(-∇ u, ∂_t) of (R3a) is ≥ 0.
[R5.0 (nit): c1, c2 bound T without √|g|, which B1b bounds; B1a also passes at |H| ≤ 1/5.]

**Step 2 (the bootstrap assumption and the pointwise bounds; deduced, computed B3-B4).** (BA): 𝔈_k1(σ) ≤ 4 ε^2 on
[T, σ*]. Under (BA), for σ in [T, σ*] and r ≥ r_σ:

    |d Γ^β h_R| ≤ C_S ε r^(-3/2-a) (|β| ≤ k1 - 3),   |d d Γ^β h_R| ≤ C_S ε r^(-3/2-a)
    (|β| ≤ k1 - 4),   |Γ^β h_R| ≤ C_S ε r^(-1/2-a) (|β| ≤ k1 - 3).                                (R4b)

*Proof.* Along a ray of Σ̃_σ, d/dr = x̂.∂_x + f' ∂_t (B4b) and x̂.∂_x = r^-1 (Z - (t - v1) ∂_t) (B4a), with
|t - v1| ≤ r (B4e): every r-derivative of d Γ^β h_R along the ray, and every second derivative of Γ^β h_R,
is a combination with coefficients bounded by 1 + 4/r of first derivatives of Γ Γ^β h_R (Γ in {∂_t, Z,
Ω}; scale5 Z4a) and of r^-1 Γ Γ^β h_R. Round 2's S1 (R^(2a+3) F(R)^2 ≤ 2 ||r^(a+3/2) F|| ||r^(a+3/2)
F_r||, scatter5) on each ray, applied to Ω^γ d Γ^β h_R, |γ| ≤ 2, with H^2(S^3) in L^∞(S^3), gives
the first bound with 𝔈_(|β|+3); the undifferentiated terms enter through the Hardy inequality of the slice,
∫_(r_σ)^∞ r^(2a+1) φ^2 dr ≤ (a + 1)^-2 ∫ r^(2a+3) φ_r^2 dr, whose boundary term at the inner edge has
the good sign and whose constant is sharp (B3a-B3c; control B3d); the second bound is the first with one more
commutation; the third integrates the first from r = ∞ (the Hardy integral finite, the limit 0). ∎
[R5.0 (r4-M4): S1 and Hardy to r = ∞ need the full-slice energies finite; shown in R5-B, the boundary terms vanishing
along a sequence (r5settle5 F3).]

So under (BA), with ε ≤ ε_2 and λ ≤ λ_2: |H| ≤ C λ r^-2 + C_S ε r^(-1/2-a) ≤ min(1/50, μ/(2 r^2),
r^-2/2) on W (a > 3/2), and Step 1 applies.
[R7 (nit): a >= 3/2 suffices (C_S eps r^(-1/2-a) <= r^-2/4 for eps small; r6sigma5 W6); the window is open and lies
above 2, so nothing changes.]
[R8 (nit 4): take |H| <= r^-2/4 in place of r^-2/2 here (it holds for lam <= lam_2, eps_B <= eps_2, a >= 3/2), so that
|g^-1 - g_b0^-1|_op <= 0.2845 r^-2 < r^-2/2, the margin D4-D5 (B2d) assume (r7settle5 K6; R8-A).]

**Step 3 (the commuted equations; computed B5, scale5 Z1-Z2).** With c_Γ := 2 and M_Γ := -2 μ ∂_μ for Γ =
Z, c_Γ := 0 and M_Γ := 0 otherwise, the identity (Γ + c_Γ) P(h) = DP(h)[Γ h] + M_Γ P(h) holds
for every h ((R3c), scale5 Z1a; Z2a-b), and differentiating it in h,

    (Γ + c_Γ) DP(h)[k] = DP(h)[Γ k] + D^2P(h)[Γ h, k] + M_Γ DP(h)[k]                           (R4c)

(B5a-b at 60 digits for Γ = Z and ∂_t; controls B5c-d: without D^2P they fail). Applied |α| times to P(Σ +
h_R) = 0, and subtracting the same expansion of P(Σ) (which is not 0): Γ^α h_R solves

    DP(H)[Γ^α h_R] = S^α := -R^α + (A) + (B) + (C),                                                (R4d)

R^α the commuted residual of Σ (products of (Γ_i + c_i) and M_i applied to P(Σ)); (A) the terms linear
in one Γ^β h_R, |β| ≤ |α|, with explicit coefficients built from Γ^γ Σ (from D^mP(H)
[Γ^(α_1) ., ..., Γ^(α_m) .], m ≥ 2, one slot h_R and the others Σ, and from DP(H) - DP(Σ) on
Γ^α Σ); (B) the terms with at least two slots h_R (m ≥ 2, every |α_i| ≥ 1, sum |α_i| ≤ |α|);
(C) (μ ∂_μ)^j DP(H)[Γ^β h_R], j ≥ 1, |β| < |α|. Componentwise, DP(H)[k] = -(1/2) g^(ab) ∂_a ∂_b k +
B(H) . d k + C(H) k with |B(H)| ≤ C(μ r^-3 + |d H|), |C(H)| ≤ C(μ r^-4 + |d d H| + |d H|^2) ((0.2): Q is quadratic
in d g with coefficients rational in g and smooth through Γ[g_b0], and -(1/2)(Dg^-1[k])^(ab) ∂_a ∂_b (g_b0 + H) is
the zero-order part).
[R5.0 (r4-m5): R^α = Π_i (Γ_i + c_i) P(Σ), with no M_i on P(Σ); the M_i P(Σ) terms cancel.]

**Step 4 (the energy identity; computed trunc5 T3).** For φ := (Γ^α h_R)_ij, (R3a) on W_T cap {t̃ ≤ σ},
whose boundary is Σ̃_σ (future), Σ̃_T cap W (past) and N cap {T ≤ t̃ ≤ σ} (past), with the co-area
d^5x = dt̃ d^4x:

    E_σ[φ] + ∫ ∫ √|g| |w'| T(-∇ u, ∂_t) = E_T[φ] + F_N[φ] - ∫ ∫ √|g| w (□_g φ) ∂_t φ
                                                          - (1/2) ∫ ∫ √|g| w T^(ab) ∂_t g_ab,              (R4e)

□_g φ = g^(ab) ∂_a ∂_b φ - g^(ab) Γ^c_ab[g] ∂_c φ (trunc5 T3b) = -2 S^α + 2 B(H) . d φ + 2 C(H) φ -
g^(ab) Γ^c_ab ∂_c φ. The bulk term on the left is ≥ 0 (Step 1) and is dropped.
[R5.0 (r4-M4): (R4e) is run on the bounded domains W_T ∩ {t̃ ≤ σ} ∩ {Φ_W ≤ V_*}, whose extra boundary has flux ≥ 0, and
V_* → ∞ (R5-B).]

**Step 5 (the error terms; computed B6-B8, B3).** Each error is ∫_T^σ ||w^(1/2) Y||_(L^2(Σ̃_σ')) E^(1/2)
dσ' / c1^(1/2) for a term Y of □_g φ, and on Σ̃_σ' every r ≥ r_σ' ≥ |σ'| - C:

| term | bound of ||w^(1/2) Y|| | kernel q in (1 + abs(σ))^-q |
|---|---|---|
| R^α (P(Σ) = O(λ r^(-13/2)), B8a; degree -6 cancelled by F_4) | C λ r_σ^(a - 9/2) (B8b) | 9/2 - a |
| (A), coefficient on d Γ^β h_R (λ r^-3) | C λ r_σ^-3 𝔈^(1/2) | 3 |
| (A), on d d Γ^β h_R, abs(β) < abs(α) (λ r^-2; Z4a) | C λ r_σ^-2 𝔈^(1/2) | 2 |
| (A), on Γ^β h_R (λ r^-4, Hardy) | C λ r_σ^-3 𝔈^(1/2) | 3 |
| (C) (μ r^-2 d d Γ^β h_R) | C μ r_σ^-2 𝔈^(1/2) | 2 |
| B(H) . d φ, Γ[g] . d φ | C (μ + λ) r_σ^-3 + C ε r_σ^(-3/2-a) | 3, 3/2 + a |
| C(H) φ (Hardy: r abs(d d h_R) ≤ C_S ε r^(-1/2-a)) | C (μ + λ) r_σ^-3 + C ε r_σ^(-1/2-a) | 3, a + 1/2 |
| (B) (B7's split, (R4b)) | C ε r_σ^(-1/2-a) 𝔈^(1/2) | a + 1/2 |
| deformation (1/2) w T^(ab) ∂_t g_ab | C (λ r_σ^-3 + ε r_σ^(-3/2-a)) | 3, 3/2 + a |

(B6a: every kernel integrable on a in (5/2, 3); B6b: exactly on (1/2, 7/2); controls B6c-d: at a = 1/2 the C(H) φ
kernel fails, at a = 7/2 the residual's.) (B): every multilinear term has one slot in L^2 (energy order ≤ k1: an
undifferentiated slot through Hardy, a twice differentiated one through Z4a) and the others in sup by (R4b) (order + 3,
or + 4 with two derivatives, ≤ k1), for every k1 ≥ 6 (B7a, enumerated to 30, minimal k1 = 6; control B7c: k1 = 5
fails; B7d: with the smallest slot in L^2 it fails at every k1). Summing over |α| ≤ k1 and the components:
[R5.0 (r4-m6, nits): boot5.py's multilinear row now has the table's a + 1/2 and B6c expects both rows; the B(H) and
deformation rows carry the factors 𝔈^(1/2) and 𝔈; the coefficients' exponents are measured in r5op5 O1.]

    𝔈_k1(σ) ≤ C_E [ 𝔈_k1(T) + 𝔉_k1 + ∫_T^σ κ 𝔈_k1 + ∫_T^σ ρ 𝔈_k1^(1/2) ],

κ := C(μ + λ)(1 + |σ|)^-2 + C ε (1 + |σ|)^(-1/2-a), ρ := C λ (1 + |σ|)^(a - 9/2), with
∫ κ ≤ C(μ + 1) =: K_κ and ∫ ρ ≤ C λ/(7/2 - a) =: ρ_∞, independent of T (μ is fixed, the kernels
integrable whatever their size).

**Step 6 (closing; deduced).** With y(σ) := sup_[T, σ] 𝔈_k1^(1/2), Gronwall gives y^2 ≤ C_E e^(C_E K_κ)
(𝔈_k1(T) + 𝔉_k1 + 2 y ρ_∞), so 𝔈_k1 ≤ C_* (𝔈_k1(T) + 𝔉_k1 + λ^2) on [T, σ*], C_* independent of T, λ,
ε. Put ε^2 := C_* (sup_(T ≤ T_1) 𝔈_k1(T) + 𝔉_k1 + λ^2). 𝔉_k1 ≤ C(λ^2 + ν(λ)) (Lemma R4.5); 𝔈_k1(T),
the cap, is at most C(λ) |T|^(2a - 6) (trunc5 T2b; B12a), below λ^2 for T ≤ T_1(λ). So ε ≤ ε_2 for λ ≤
λ_2, and 𝔈_k1 ≤ ε^2 < 4 ε^2: (BA) is improved. 𝔈_k1 is continuous in σ for the smooth truncated solution,
so (BA) holds on the whole interval of existence, and with Step 2's bounds the local theory continues g_T (Step 8 with
Φ_W): g_T exists on all of W_T with 𝔈_k1 ≤ ε^2.
[R5.0 (r4-M4): smoothness does not give the finiteness and continuity of 𝔈_k1; finite speed of propagation and P(Σ) = O(λ
r^(−13/2)) do (R5-B, r5settle5 F2, F5).]

**Step 7 (every order at fixed λ; computed B7b).** For k > k1, induction on k: the terms of order k are linear in the
order-k quantities with coefficients bounded by (R4b) at orders ≤ k - 1 (B7b: with the sup factors at energy order ≤
k - 1 every term splits, k = 9..30), so Step 5's inequality holds at order k with ε replaced by C_(k-1)(λ) in the
sup factors and Gronwall closes without smallness: 𝔈_k ≤ C_k(λ) (𝔈_k(T) + 𝔉_k + λ^2), finite by Lemma R4.5 (i)
and the cap. So no smallness is needed above k1.

**Step 8 (the limit T → -∞; computed B11-B12).** For T' < T ≤ T_1, δ := g_T' - g_T on W_T solves the linear
system obtained by subtracting the two equations, written with g_T' as principal part: -(1/2) g_T'^(ab) ∂_a ∂_b δ =
(1/2)(g_T'^(ab) - g_T^(ab)) ∂_a ∂_b g_T + (Q(g_T') - Q(g_T)), linear in (δ, d δ) with zero-order coefficient d d
H_T and first-order coefficients d H_T, d H_T' (Step 5's kernels). δ = 0 on N cap W_T. On Σ̃_T, δ =
h_R,T' - h_R,T(T): the second is the cap; the first is bounded by Step 5 run on W_T' cap {t̃ ≤ T}, whose data are tails:
𝔈[h_R,T'](T) ≤ C(𝔈(T') + 𝔉_k1(T', T) + (∫_(-∞)^T ρ)^2) =: ϑ(T), with 𝔉(T', T) ≤ C |T|^(2a-7), the cap
≤ C |T|^(2a-6), ∫_(-∞)^T ρ ≤ C λ |T|^(a - 7/2) (B12a; control B12b: at a = 7/2 the residual tail is
infinite). So E[δ] ≤ C ϑ(T) → 0 on W_T uniformly in T' < T: (g_T) is Cauchy in the weight-a energy on every
W_T0, and with the uniform bounds at every order (Step 7) it converges in C^k on compact subsets of W for every k.
The limit g is smooth on W, solves Ric^H(g) = 0, has h_R := g - g_b0 - Σ with 𝔈_k1 ≤ ε^2 and 𝔈_k ≤ C_k(λ)
(lower semicontinuity), and E_σ[Γ^α h_R] ≤ C ϑ(σ) → 0 as σ → -∞ (vanishing cap energy);
since every g_T equals g_λ on {v ≤ v1, t̃ ≥ T} near N, g_λ on P ∪ Ω and g on W join smoothly across N.

**Step 9 (the class on S; computed scale5 Z5, Z8).** On S = Σ̃_0, r d/dr (h_R|_S) = (Z h_R)|_S + (v1 - f + r f')
(∂_t h_R)|_S with a coefficient smooth in ρ := 1/r (scale5 Z5a; f' in |x|^-2 C^∞): every (ρ d_ρ)^j Ω^β
(h_R|_S) is a restriction of commuted fields with smooth bounded coefficients, and by the Hardy inequality (Z8a, B3)
h_R|_S lies in ρ^(a+1) H_b^k and d h_R|_S in ρ^(a+2) H_b^k (dρ/ρ dω) for every k, a + 1 > ℓ0. Σ|_S =
sum_p ρ^p F_p(1 + ρ(f_∞ - v1) + ρ^2 C^∞, x̂) is polyhomogeneous with exponents p + j, all in ℰ_0^½
(Z8c), its coefficients O(λ) (F_p(0) = G_(2p)(v1) = O(λ): Lemma R4.4 for the means, Lemma R3.2 for e; the
ρ^(5/2) one O(λ^∞), round 1). The induced (γ, k) are smooth functions of (g, d g) on S and of (d f, d^2 f) in
ρ^2 C^∞, ρ^3 C^∞ (Part VII Lemma 2.1's computation, 175-180), and ℰ_0^½ is closed under sums: γ -
γ_b0 in H_b^(∞,(ℰ_0^½, ℓ0)), k - k_b0 in H_b^(∞,(ℰ_0^½ + 1, ℓ0 + 1)), with ||.||_(d_1) ≤ C(λ + ε)
on S, since k1 ≥ d_1 + 4 covers the d_1 derivatives and the commutations of Steps 2 and 9.

**Theorem R4.6 (the continuation; deduced, every identity and exponent computed).** Under the setting above there are
λ_2 > 0 and T_1(λ) such that for 0 < λ ≤ λ_2: g_λ continues to W as a smooth metric g with Ric^H(g) = 0, the
limit of the truncated problems, with g - g_b0 - Σ in the weight-a class with vanishing cap energy and 𝔈_k1 ≤ ε^2,
ε → 0 as λ → 0, and 𝔈_k ≤ C_k(λ) at every k; its data on S are in III.K's half class with ||.||_(d_1) ≤
C(λ + ε). *Proof.* Steps 1-9. ∎

### R4-E (b1): the weight-a_0 bootstrap does not close; uniqueness holds at a_0

**Proposition R4.7 (the scheme of R2.5 and R3.4 does not close; deduced, computed B10, B3).** Let a_0 in (0, 1/2], and
consider the existence bootstrap of R2.5/R3.4: the energies (R4a) at weight a_0 of Γ^α h, h := g - g_b0 (no
subtraction), Γ in {∂_t, L_Ω} (or with Z), |α| ≤ k0, pointwise bounds by S1 and H^2(S^3) as in Step 2.
Its commuted equation contains, through C(H) of Step 3, the top-order term -(1/2)(Dg^-1[Γ^α h])^(ab) ∂_a ∂_b h,
undifferentiated in Γ^α h. With the quantities that scheme controls, it is bounded only as ||w^(1/2) r^-1
Γ^α h|| . sup r |d d h| ≤ C 𝔈^(1/2) ε r^(-1/2-a_0) (Hardy, Sobolev), a kernel (1 + |σ|)^(-a_0-1/2),
not integrable for a_0 ≤ 1/2 (B10a); the energy inequality then carries the factor exp(C ε |T|^(1/2 - a_0)) (log T
at a_0 = 1/2), unbounded as T → -∞, and the improvement step fails. Neither factor can be improved in the class: the
Hardy constant is attained (B3a, B10c), and Sobolev's bound |d d h| ≤ C ε r^(-3/2-a_0) is attained by the band
family R^(-a_0-3/2) ψ(r - R), of bounded weighted energy with R^(a_0+3/2) |φ| = ψ(1/2) at r = R + 1/2 (B10b).
Control (B10d): the same chain at a = 11/4 is integrable. ∎
[R5.0 (r4 verdict): restated as Proposition R5.3: the written chain does not close; each inequality is sharp separately,
no single field is shown to make the product sharp.]

This corrects round 1's (N1) and R2.5's "the bootstrap closes for small data with no null condition" (they counted
the first-order kernel (v1 - t)^(-3/2-a), not the undifferentiated top-order one); R3-C's identities and R3.3's
Cauchy problems stand. It is a statement about a scheme: the continuation of Theorem R4.6 has d d h = O(r^-4) on W and
lies in the a_0-class. (b1)'s existence is not needed: Theorem R4.6 constructs the continuation, and (N2)'s dyadic
identity at a_0 < 1/2 (R3-C) is no longer used. (b1)'s class enters only through uniqueness.

**Proposition R4.8 (uniqueness at weight a_0; deduced, computed B11).** Let a_0 in (0, 1/2) and let g' = g_b0 + h' be a
smooth metric on W with Ric^H(g') = 0, g' = g_λ on N with its first derivatives, |h'| ≤ 1/50, Γ^α h' (|α|
≤ 3, Γ in {∂_t, L_Ω, Z}) of finite weight-a_0 energy on every Σ̃_σ, and E_σ[h'] → 0 as σ →
-∞. Then g' = g of Theorem R4.6.
[R5.0 (r4-M3): finiteness per slice does not suffice; Proposition R5.2 assumes the energies bounded uniformly in σ, and
its zero-order bound carries (μ + λ) r^(−3).]

*Proof.* (R4b) at weight a_0 gives |d h'| ≤ C r^(-3/2-a_0) and |h'| ≤ C r^(-1/2-a_0). δ := g' - g solves
-(1/2) g'^(ab) ∂_a ∂_b δ = (1/2)(g'^(ab) - g^(ab)) ∂_a ∂_b g + (Q(g')(d g', d g') - Q(g)(d g, d g)): zero-order
coefficient d d g of the constructed solution (r |d d H| ≤ C λ r^-3 + C ε r^(-1/2-a), a > 5/2) and |d g'|^2;
first-order coefficients |d g| + |d g'|. (R4e) for δ with the metric g', weight a_0: the deformation |∂_t h'| and the
bulk-sign error (T_g'(-∇_(g_b0) u, ∂_t) ≥ -C |h'| |d δ|^2, a kernel |w'| |h'| / w ≤ C r^(-3/2-a_0)) have q =
3/2 + a_0; the zero-order term through Hardy has q = min(3, a + 1/2); all > 1 (B11a; control B11c: with the zero-order
coefficient d d h' the kernel is q = a_0 + 1/2 ≤ 1). δ = 0 on N; on Σ̃_σ1 its energy is at most
2 E[h'] + 2 E[h], both → 0 as σ1 → -∞ (Σ: |σ|^(2a_0 - 2), B11b; h_R: weight a > a_0). Gronwall from
σ1 and σ1 → -∞: δ = 0. ∎

So the continuation is the only one in the record's gauge with nothing incoming in the weight-a_0 sense, a class that
contains every candidate with a radiation-free r^-2 approach; R2.6's r^(-3/2) tail constant in v has nonzero data on N
and is no counterexample.

### R4-F (V): the limit is vacuum

**Proposition R4.9 (deduced, computed V1-V2).** The metric g of Theorem R4.6 has D(g) = 0 on W, hence Ric(g) = 0; with
Theorem P, g_λ on P ∪ Ω ∪ W is vacuum, and its data (γ, k) on Σ_IVP satisfy the constraints.

*Proof.* (i) The identity (V1, 60 digits, three points, for a g that solves nothing; controls V1b-c): for every g,

    (1/2)(□_g D_n + Ric(g)_n^d D_d) + ∇^m Ein(C)_mn + ∇^m Ein(Ric^H(g))_mn = 0,

Ein(X) := X - (1/2) g tr_g X, C_mn := (1/2)(g_(m ρ)(Γ[g_b0] - Γ[g])^ρ_(n s) + (m ↔ n)) D^s (the
contracted Bianchi identity with Ric = Ric^H + Sym(g Dh D); READ in the record's 0.7 at [LR05], [CBCL06]). Where Ric^H
= 0, D_n solves -(1/2) g^(ab) ∂_a ∂_b D_n = b . d D + c D, linear and homogeneous, with |b| ≤ C(μ r^-3 + |d H|) and
|c| ≤ C(μ r^-4 + |d d H| + |d H|^2) (Ric(g) is a known coefficient). (ii) Each g_T solves Ric^H = 0 on W_T, so D_T :=
D(g_T) solves (i)'s system there. Its weight-a_D energy, a_D in (0, 2), has the kernels of V2a (q = 3, 3/2 + a, a + 1/2;
control V2e), all integrable. On N, D_T = D(g_λ) = 0 with its tangential derivatives (g_T = g_λ on {v ≤ v1}, its
one-sided jet on N being g_λ's). On Σ̃_T: D_T = 0 on {v ≤ V_T}; on the band g_T = g_λ + χ_T (g_b0 + Σ -
g_λ) with g_b0 + Σ - g_λ = O(r^(-9/2)) with derivatives (Lemma R4.5's proof), so D_T and d D_T are
O(r^(-9/2)) there, energy ~ |T|^(2a_D - 6) (V2c); beyond, D_T = D(g_b0 + Σ) = O(λ r^-3) and d D_T = O(λ r^-4)
(the second time derivative from Ric^H(g_T) = 0 differs from (g_b0 + Σ)'s by P(Σ) = O(λ r^(-13/2))), energy
≤ C λ^2 |T|^(2a_D - 4) (V2b; control V2d: a_D = 2). So E_σ[D_T] ≤ C(λ^2 |T|^(2a_D - 4) + |T|^(2a_D - 6)) for
every σ in [T, 0], with C independent of T. (iii) As T → -∞, g_T → g in C^2 on compact sets, so D(g_T) → D(g)
there, and E_σ[D(g)] restricted to any compact set is 0: d D(g) = 0 on W, and D(g) = 0 on N gives D(g) = 0.
Then Ric(g) = Ric^H(g) + Sym(g Dh D) = 0. g_λ is vacuum on P ∪ Ω (Theorem P), and the join across N is smooth
(Step 8). ∎

III.K receives (γ, k) only; its gauge data are rebuilt from them (III.C'' Proposition 4.1,
PART-III-C3-BOOSTDATA.md:162-171), so D = 0 is needed only for the vacuum property, which it gives.

### R4-G The theorem, the ledger, what remains

**Theorem R4.10 (deduced; conditional only on statements the record lists as proved).** Fix A, the C_c^∞ envelope of
Theorem 1, the angular profile and the seed. Let ℓ0 in (3, 4) ∖ {7/2}, ℓ_I in (3, ℓ0) off row d2's exclusion sets,
ε_m > 0, ε_t < ε_K; let ε, d_1 be III.K Theorem 4.3's in the half class (Theorem R2.4); a in (max(ℓ0 - 1,
5/2), 3); k1 := max(8, d_1 + 4); M := M(8, k1 + 1, k1 + 1) = 27 + 2 k1 (Proposition R3.1); K > max(d_1 + 14, K*(a, 8,
M, k1)) (Lemma R3.2) and the approximant of order N(K, k1 + 4) (Corollary R4.3). Then there is λ_2 > 0 such that for
every 0 < λ ≤ λ_2 (no exceptional set):
[R5.0 (nit): N(K, k1 + 5), λ_2 ≤ λ_F(k1 + 5); M = 17 + 2 k1 suffices (Proposition R5.4); a ∈ (ℓ0 − 1, 3).]
[R5.0 (r4-M1): the label is wrong: the theorem also rests on N1STAR-PROOF.md section 11.1 (deduced, its D44 repair
unread), on Lemma 11.0's repair (R5-D) and on this file's own deductions; Theorem R5.1 restates it with its status.]

- (1) g_λ continues to W as a smooth vacuum metric in the record's gauge (Theorem R4.6, Proposition R4.9), the only
  such continuation with nothing incoming in the weight-a_0 sense, a_0 in (0, 1/2) (Proposition R4.8);
- (2) its data (γ, k) on Σ_IVP lie in III.K's class with ℰ_0 = ℰ_0^½ and ||.||_(d_1) < ε (Step 9 on S;
  Part VII Lemma 1.1 with K ≥ d_1 + 15 on Σ_IVP cap {r ≤ 4R});
- (3) the maximal vacuum development of (γ, k) settles to a Tangherlini metric g_(m',0), |m' - μ_end| < ε_m, at the
  rate |(t_* d_(t_*))^i ∂_x^β (g - g_(m',0))| ≤ C t_*^(-2-ε_t) on {r_0 ≤ r ≤ R', t_* ≥ T'}, by Theorem R2.4
  (III.K Theorem 4.3 in the half class) and Part VII Proposition 3.2, with no gluing.

*Proof.* Theorem R4.6 and Proposition R4.9 give (1) and the class on S; R4.8 the uniqueness; Part VII Lemma 1.1 the
compact part of Σ_IVP; Theorem R2.4, whose Part IV condition is discharged by citation (R3-A), and Part VII
Proposition 3.2 give (3), as in Theorem R2.10. ∎

*What the theorem rests on.* (P4): Part IV's seven outputs, listed as proved in the record (R3-A). Theorem R2.4: R2.2
computed for M ≤ 12 and the verifier's induction for every M (recorded in R2.2, not re-derived), Lemma R2.3. (Pr):
Propositions R4.1-R4.2. (Poly): Proposition R3.1 with R4.1. (B): Theorem R4.6. (V): Proposition R4.9. The constant
λ_2 is not evaluated (R5, another workstream): the theorem is qualitative in λ.

*Changes to round 3, recorded.* R3.7's hypotheses (Pr), (B), (V) are discharged; its K*(a_0, ...) is dropped (no
existence at a_0); R3.6's data need Lemma R4.4 (R4-C); R3-B (b) and R3-F (3) are corrected (R4-B); R3.4's bootstrap is
replaced by Proposition R4.7 (it does not close) and Theorem R4.6; R2.5's and round 1's (N1) "closes with no null
condition" is withdrawn.

Ledger. Computed: `order5.py` O1-O5 (22 checks), `f1lemma5.py` F1a-F1e (12), `boot5.py` B1-B13 (48), `vac5.py`
V1-V2 (8), every check with a control that mutates the code under test and fails as it must. Deduced: Propositions
R4.1, R4.2, Corollary R4.3, Lemmas R4.4, R4.5, Theorem R4.6 (Steps 1-9), Propositions R4.7, R4.8, R4.9, Theorem R4.10.
READ: N1STAR-PROOF.md (2a69924) 135-148, 366-411, 412-456, 521-540, 1043-1061, 1091-1102, 1114-1116, 1143,
1170-1179, 1235-1268, 1324, 1341-1361, 1363-1418, 1419-1449, 6779-6804, 10548-10579, 10593-10668; PART-VII-ASSEMBLY.md
122-130, 140, 175-180; BEYOND5.md 198-205; PART-III-C3-BOOSTDATA.md 162-171. None from outside sources.
[R5.0: not every one: the checks marked [arithmetic] in round 5 cannot fail under a mutation of the operator.]

Open: nothing in (Pr), (B), (V) or F1. R5 (λ_1 and δ not evaluated) belongs to another workstream.

*Proposed text for the paper's section 9, "Beyond the boundary"* (RESPONSE-HL-5D.md, replacing the sentences from "It is
not shown that Theorem 4 applies to g_λ's own data" to "The scattering estimate itself is not done."; not edited here):
[Superseded by R5-E (the round-4 reader's M2, m13).]

```text
  Theorem 4 does apply to g_λ's own data, in the half-integer class ℰ_0^½ = {(2 + j/2, 0)} (supplement
  `docket68/n1star/SETTLE-GLAM5.md`, rounds 1–4; deduced, every identity, exponent and kernel computed under
  `checks/`). After the shell g_λ − g_b0 has at past null infinity an r^(−5/2) coefficient, O(λ^∞) but nonzero off a
  discrete set of λ, which puts a ρ^(5/2) term into the data at spatial infinity, outside Part VII's integer class;
  with ℰ_0^½, III.K's class run changes only by finitely many derivatives (conditional, as Part VII, on Part IV's
  outputs, listed as proved). g_λ continues to the past domain of dependence of the far initial slice as a vacuum
  metric with nothing incoming, by a weighted energy bootstrap after subtracting its self-similar terms through r^(−4);
  it is the only such continuation, and its data lie in that class with small norm. So for every 0 < λ ≤ λ_2, with no
  exceptional set, the maximal development of g_λ's own data settles to a Tangherlini metric at Theorem 4's rate, with
  no gluing. λ_2 is not evaluated.
```

    python3 checks/order5.py     (about two minutes)
    python3 checks/f1lemma5.py   (about five minutes)
    python3 checks/boot5.py      (about three minutes; B5 most of it)
    python3 checks/vac5.py       (about half an hour; V1 most of it)

## Round 5 (2026-11-06)

Status: written; not yet read by a verifier. Labels as in rounds 2-4; a check marked **[arithmetic]** computes a
consequence of exponents or rules entered by hand, and its control cannot fail under a mutation of the operator. New
programs, each with its `.out` from a full run and with controls that mutate the code under test (the operator, the
field, the rule or the formula) so that the claim fails: `checks/r5settle5.py` (A-H), `checks/r5op5.py` (O1-O3, on the
full five-dimensional gauge-fixed operator), `checks/cclass5.py` (C1-C3, the same), `checks/r5edits5.py` (E1-E3: R5-D's
text applied to a copy of N1STAR-PROOF.md, and the facts it states) and `checks/zinv5.py` (ZI1-ZI2: the round-3
verifier's scratch check of (R3c), copied with a driver). Rerun after the relabelling and repairs below:
`poly5.py`, `scale5.py`, `trunc5.py`, `scatter5.py` (its `.out` was older than its source), `boot5.py`, `order5.py`,
`f1lemma5.py`, `vac5.py`. N1STAR-PROOF.md is cited as of md5 709c63be (D616: two lines added after line 631, so every
round-4 citation above 631 is +2; Lemma 11.0 is at 10550-10581); numbers from round 3 stay in 82a7e95's numbering. Rounds
1-4 are left as their verifiers read them; where a finding below withdraws or corrects a sentence, a bracketed note
"[R5.0 (...)]" is inserted at the end of the paragraph or item that contains it, and the sentence is not changed.
Sections R5.0 and R5-A … R5-E, statements R5.1 … R5.4.
[R6 (m8): zinv5's .out was empty when this was read: its run never finished, for two reasons in its evaluation;
repaired, it passes ZI1-ZI3 (R6.0 (m8)). F3, F3', F4, F5 and G5 are [arithmetic].]

What this round settles, in one paragraph. Every finding of both readers is re-derived and seated (R5.0). Two of the
round-4 reader's majors change the mathematics: Theorem R4.6 never met spatial infinity (M4), and is repaired by
running the energy identity on bounded domains of dependence cut by the time function v + 1/r, whose boundary flux has
a sign, with the full-slice energies shown finite by finite speed of propagation (R5-B); and Proposition R4.8's
uniqueness needs energies bounded uniformly in the slice (M3, R5-C). The weight window is (l0 - 1, 3), the lower bound
5/2 of rounds 3-4 being needed by nothing (R5-C, computed G5). The lam-orders of Proposition R3.1 are derived from every
monomial of the source: B_J <= 3J - 9, below what rounds 3-4 used (R5-A, computed A). The exponents that rounds 3-4
typed by hand are now measured on the operator or on explicit fields where it matters (O1, O2, G1-G3, H), and the rest
are marked [arithmetic]. Theorem R5.1 restates R4.10 with every condition and its exact status (R5-E); the replacement
texts for N1STAR-PROOF.md's Lemma 11.0 and for the paper's section 9 are R5-D and R5-E.

### R5.0 The verifiers' readings, and their dispositions

**(a) The round-3 reader** (its findings arrived after round 4 was written; each re-derived here).

- **(r3-M1) F1 is false as round 3 stated it.** Re-derived: at the step |gamma| = j + 1 the energy controlled is ||d U||,
  U := d^gamma u_1; the term -(1/2) lam^-1 U(ell, ell)[d_th^2 W_TT] is lam^-1 t^(-3/2) U, and ||U|| is already bounded by
  step j (whose energies bound every derivative of u_1 of order j + 1, U among them, through Lemma 9.3(b)), so it is a
  lower-order source (`f1lemma5.py` F1b; F1e'' [arithmetic]). The terms at the energy's own order are the Q-difference's
  d(lam [W_TT]) . d U and Gamma[g0] . d U, lam-free and of the kernel's kind (F1c; their lam^0 wave part `cclass5.py`
  C3). This is round 4's R4-B, which already corrected F1: it agrees. Round 3's R3-B (b) and R3-F finding 3 are withdrawn
  (notes inserted). The near region's e^(C/lam) (R3-B, "Where polynomiality fails") comes from the zero-order coefficient
  d^2 g_n' of Theorem P's difference system, "at most C lam^-1 t^(-3/2)" (N1STAR-PROOF.md:1424-1425), integrated over [1,
  lam^-2], not from F1; it enters neither (11.7) nor Corollary R4.3 (whose bounds come from (9.8)-(9.9) at order k
  directly). Note inserted.
- **(r3-m1) v is not a time function.** Re-derived and computed: g_b0^-1(dv, dv) = 0 and the first variation is
  -h(ell, ell), so for g_b0 + eps h the sign of g^-1(dv, dv) is that of -h(ell, ell), and both occur (`r5settle5.py`
  D1); for g_b0 itself the infimum of dv(Y) over future causal Y is 0, attained at Y = -grad v (D2): T1a's sampled
  minimum 5.7e-2 is an artefact, and its label is corrected (`trunc5.py` T1a, rerun). R3.3 (iii) is withdrawn as
  written. Its replacements: v + eps t on the bounded slab, a time function with uniform margin 2 eps (D3) under
  |g^-1 - g_b0^-1|_op <= eps/4; or Phi_W := v + 1/r on all of W, with g_b0^-1(dPhi, dPhi) = -2 r^-2 + r^-4 (1 - mu r^-2)
  and (g_b0^-1 + delta)(dPhi, dPhi) <= -r^-2 + r^-4 < 0 for every |delta|_op <= r^-2/2, because |dPhi|_E^2 =
  1 + (1 - r^-2)^2 <= 2 (D4, exact; D5 sampled; control D5'). Round 4's Theorem R4.6 does not use v: it localises by
  Phi_W (B2d). But its localisation had a different gap, the round-4 reader's M4, repaired in R5-B.
- **(r3-m2) Persistence of regularity.** R3.6 delivered rho^l0 H_b^(k0 - c); III.K's class needs H_b^oo. Round 4 already
  supplies it: Theorem R4.6's Step 7 bounds 𝔈_k <= C_k(lam) at every k at fixed lam, whose inputs are Lemma R4.5 (i) (the
  N-flux at every order at fixed lam, from (11.7) at every order, which Lemma 11.0 and Proposition 11.1 give at fixed
  lam, and from Theorem P's smoothness on the compact part of N, N1STAR-PROOF.md:1428-1431) and the cap at every order
  at fixed lam (C(lam) |T|^(2a - 6), r5settle5 G2); Step 9 turns every k into H_b^k. So R3.6's conclusion holds with
  H_b^oo, by R4.6 Steps 7 and 9 (as repaired in R5-B). Note inserted.
- **(r3-m3) The approximant through r^-4.** Supplied by round 4's Lemma R4.4 at J = 8: on N (v1 > v_end) g_app - g_b0
  = sum_j lam^j m_j, and Lemma R4.4 gives each m_j = sum_(k=4)^8 r^(-k/2) M_(j,k) + m_(j,8) with m_(j,8) in E_(9/2)
  with its ell-gains, lam-independent; R4-C is that repair (with R5.0 (r4-m11), (r4-m12) below). Note inserted.
- **(r3-m4) G-invariance for Part VII Proposition 3.2.** Part VII's G = O(2) x O(2) acts by (t, x) -> (t, sigma x)
  (PART-VII-ASSEMBLY.md:31-38); it preserves W, N, every Sigma~_sigma, Phi_W, the weights w(u), the commutator set
  {d_t, Z, Omega_ij} (Omega_ij up to a rotation of the indices), g_b0, and g_lam ((P-v)). The gauge-fixed operator is
  natural: P(sigma^* h) = Lambda^T P(h)(Lambda .) Lambda (`r5op5.py` O3, for the reflection x2 -> -x2 and a rotation;
  control O3': a shear fails). Sigma's coefficients G_(2p)(v1, .) are those of g_lam's unique expansion, so Sigma is
  G-invariant, and so are the truncated data (g_lam, chi_T(v), Sigma). Hence each truncated solution is G-invariant by
  uniqueness of its Cauchy problem, and so is the limit; independently, for sigma in G, sigma^* g satisfies every
  hypothesis of Proposition R5.2 (R5-C) and equals g. So (gamma, k) on Sigma_IVP is G-invariant (Sigma_IVP = {t_KS =
  f(|x|)} is), as Proposition 3.2 needs, and its conclusion gives b = (m', 0), S = 0 (PART-VII-ASSEMBLY.md:403-406).
  [R6 (m7): the paragraph *The metric.* ending "So b = (m',0) and S = S^(0)_1 = 0" is now at 420-423 (md5 500c085b).]
- **(r3-m5) K* is quadratic in k0, not linear** (line 738). Computed, `r5settle5.py` B1: a = 11/4, M = 27 + 2 k0:
  K* = 116, 821.5, 2071.5 at k0 = 0, 10, 20, and for k0 >= 400 the second differences are those of s (a + k0) with
  s = (2M + 1)/(7 - 2a) growing linearly in k0; control B4: with s held fixed K* is linear. Finite in every case,
  which is all R3.7 and R4.10 use. Note inserted.
- **(r3-m6) R3-A overclaims.** Corrected: R3-A discharges Theorem R2.4's Part IV condition by citation; R2.4 itself
  remains this file's deduction. R3-F's "Not open any more: (P4), (Poly), the mixed problem" reads: (P4) discharged by
  citation; (Poly) reduced to (Pr) (then discharged by R4.1-R4.2); the mixed problem not needed (R3.3 (ii)). Notes
  inserted, and the heading of Theorem R2.4, which cites "R3.1" for R3-A, is noted.
- **(r3-m7) M(J, n, m) was an upper bound from a crude recursion.** Re-derived from every monomial of (11.4)
  (`r5settle5.py` A): products of m >= 1 factors from {G_3, ..., G_J, u_J}, coefficients of degree 0, -2, -3, -4, -6,
  two derivatives each a d_v (costing lam^-1) or an r-derivative (gaining r^-1). Round 3's recursion took only products
  of two or three coefficients; without the far region's trade r^-1/2 <= lam (r >= lam^-2) the m-fold products' orders
  grow with m (control A2'': 18 at m_max = 4, 30 at m_max = 7), so it was not a derivation. With the trade every
  monomial is bounded: e(G_k) = k - 4 (A1) and B_(J+1) = 2 + max(B_J + 1, J - 2), hence **B_J = 3J - 9** (J >= 4; A2,
  the same at m_max = 6 and 7). The round-3 reader's 4J - 13 is the same recursion with B_J + 2 for the multilinear
  remainder terms, whose extra factor's r^-1/2 the trade turns into lam. Both, and R3.1's (J^2 - J)/2 - 3, are >= 3J - 9
  for J >= 4 (A2'), so R3.1's stated bound holds a fortiori; the sharper M(8, n, m) = 15 + n + m serves, and every K*
  computed with a larger M is still valid (K* increases with M). P7c checked the recursion's output, not the problem:
  marked [arithmetic]. Note inserted.
- **Controls that could not fail.** P4b now mutates the model's operator (its coupling lam^-1 replaced by lam^-3, and
  P4a's claim then fails; a coupling lam^-2 has the natural order of two derivatives and changes nothing; `poly5.py`,
  rerun); P6b, P7c, P8c, P8d are marked [arithmetic], P8c-P8d recomputed with mutation controls in `r5settle5.py` C (the
  optimum over sigma = lam^beta found on an exact grid; controls: the remainder exponent mutated, and beta held at 0); Z7
  is [arithmetic], its kernels' coefficient exponents measured in `r5op5.py` O1 and its residual's degree in O2; T2, T6,
  T7 are [arithmetic], the cap and tail exponents measured on explicit fields in `r5settle5.py` G2-G3 (T6 belongs to
  (N2), no longer used since R4.7); Z8b-Z8d are [arithmetic], Z8c recomputed by series in G6 (control: a p = 9/4 term)
  and the window in G5.
- **Nits.** (Pr) is needed at order k0 + 5, not k0 + 4 (R3.1 at n = k0 + 1 uses Proposition 9.8 at order n + 4); the
  same holds for R4.5 (ii) and R4.10 at k1 + 5 (and lam_2 <= lam_F(k1 + 5), the round-4 reader's unstated condition).
  PART-III-K-NONLINEAR.md:468 and 510-518 read 470 and 512-520; N1STAR-PROOF.md "1234" (R3-C, 82a7e95) reads 1235.
  P(Sigma) is O(lam r^(-13/2)) once p = 4 is in Sigma (B8, r5op5 O2), so R3-D (iii)'s kernel (v1 - t)^(a - 4) is
  (v1 - t)^(a - 9/2), integrable for a < 7/2, and a < 3 is set by the cap (T2b, G2). K*(a_0, ...) in R3.7 is
  superfluous (round 4 dropped it). s = 2 gives R = lam^-2, short of the collar lam^-2 + d1: s := max(5/2, (2M + 1)/
  (J' - 1 - 2a)) (`poly5.py` P9, r5settle5 B3: K* unchanged in every case computed). P2c is a central difference, not
  exact (label corrected); P4 is a 1+1 model (model-checked, the structure of the record's equation deduced); P9b shows
  that the interpolation bound on the e_8 term diverges, not the flux (label corrected). The "(Z H) d d h" of R3.5 is
  DP(h)[Z h]'s zero-order part -(1/2)(Dg^-1[Z h])^(ab) d_a d_b (g_b0 + h), not D^2P(h)[Z h, h]'s principal part.
  `scatter5.out` is regenerated (rerun, 2026-11-06; all checks pass).
  [R6 (m7): "read 470 and 512-520" is now 471 and 513-521 (md5 5b0ad3f0).]
- **The window.** Re-derived: nothing requires a > 5/2. The kernels allow (1/2, 7/2) (B6b; their coefficients'
  exponents measured, O1), the cap a < 3 (G2), the N-flux a < 7/2 (G3), the class on S a + 1 >= l0 (G4), uniqueness
  a > a_0 (R5.2), and Step 2 a > 3/2. Computed (G5): the admissible set on the grid is (l0 - 1, 3) for l0 = 3.1, 3.3,
  3.6, 3.9; controls: p = 4 dropped (cap 2a - 5), or the pointwise reading of the class on S (a > l0 - 1/2), leave no
  weight for l0 >= 7/2. Theorem R4.6's window (max(l0 - 1, 5/2), 3) is replaced by (l0 - 1, 3); the restriction was
  harmless but unneeded. The 5/2 of R2.8's note marked where the subtraction must reach p = 4 (it must, for every
  a > 5/2, and it does).
  [R6 (m3, nit): G5 is [arithmetic]; it now carries Lemma R4.5's hypothesis, widened to (0, 7/2), Step 2's and R5.2's,
  and the window is computed in r6sigma5 W. "a + 1 >= l0" is the inclusion's exact condition; the window is open, a +
  1 > l0, as in Step 9.]

**(b) The round-4 reader** (verdicts: R4.1-R4.3 hold, with lam_2 <= lam_F(k1 + 5) unstated; the F1 correction holds;
R4.4 holds as deduced; R4.5 holds; R4.6 has a gap (M4); R4.7 holds only about the written chain; R4.8 has a gap (M3);
R4.9 holds given R4.6; R4.10 holds given its inputs, its label wrong (M1)).

- **(r4-M1) R4.10's label.** Accepted: R4.4 (through Lemma 11.2), R4.5 (i), Step 9's F_p(0) = G_(2p)(v1), and R3.1-R3.2
  use N1STAR-PROOF.md section 11.1, which the record lists as deduced with the D44 repair not yet read
  (N1STAR-PROOF.md:29-34); Lemma 11.0 carries F1's gap until R5-D's text is applied; Theorem R2.4 is this file's own
  deduction; and rounds 2-5 are this file's. The label of Theorem R5.1 (R5-E) names exactly what must be read.
- **(r4-M2) The proposed paper text overclaimed.** Accepted; R5-E replaces it: "Theorem 4 does apply" becomes a
  deduction with its conditions; the computational claim is stated as what was computed (the identities on the full
  operator; the coefficient decays and the degrees of the self-similar residuals measured on it, O1-O2; the caps, tails
  and window measured on explicit fields, G; the remaining kernel exponents counted by hand, their integrability
  checked); "the only such continuation" carries R5.2's qualifiers.
- **(r4-M3) R4.8's uniformity.** Accepted: with C(sigma) the Gronwall kernels need not integrate. Proposition R5.2
  (R5-C) assumes sup_sigma E_sigma[Gamma^alpha h'] < oo for |alpha| <= 3, which gives (R4b) at weight a_0 uniformly.
- **(r4-M4) R4.6 at spatial infinity.** Accepted, and repaired in R5-B: the identity is run on W_T cap {t~ <= sigma}
  cap {Phi_W <= V_*}, a bounded domain of dependence whose extra boundary {Phi_W = V_*} is spacelike with flux >= 0
  (D4-D5, F1; control F1': a timelike cut-off {r = R} has a flux of either sign), and dropped; the full-slice energies
  are finite and continuous by finite speed of propagation and P(Sigma) = O(lam r^(-13/2)) (F2, F5); S1 and Hardy are
  used on finite intervals with their boundary terms, which vanish along a sequence R' -> oo once the energy is finite
  (F3); and V_* -> oo by monotone convergence. The data are no longer localised: round 4's "data equal to g_b0 beyond
  V_* + 2" made h_R = -Sigma there, with infinite weighted energy for a >= 1 (F4).
- **(r4-m1) c's remainder class is E_(3/2).** Accepted and computed: with an envelope on the wave the remainder of c
  decays like r^(-3/2), its lam^0 part containing -(.)(ell, ell)[d_v d_th W_TT] (`cclass5.py` C2: fitted slope 1.40;
  2.62 once that term is subtracted; 2.50 without the envelope; control C2': with the opposite sign the slope stays
  1.45), and F1b holds with the envelope (C1). The kernel is unaffected (c's remainder is lam^0 E_(3/2) and enters
  through Lemma 9.3(b) as t^(-3/2)). R5-D writes "+ E_(3/2)".
- **(r4-m2) Edits 1-2.** Accepted: R5-D defines R_gamma^n in its text, writes d u's lam^0 E_2 terms (dv [d_th chi]
  dv dv and the phase shift's), names the u_1-free source d_X^gamma F_1(X, 0, 0) in E_3, and restores the factor 1/2 and
  the binomial coefficients C(gamma, gamma') in the Leibniz sums (both missing in the original line 10556-10558 too).
- **(r4-m3) u*.** Accepted: with u* := 2 sup f - v1 + 1 and v1 = f(4R) + 4R, r <= u* - u fails. R5-C sets u* :=
  sup_W f + 1, so that r + 1 <= u* - u <= 2r + |u* - v1| on W (`r5settle5.py` E1, sampled; control E1').
- **(r4-m4) Invariance.** As (r3-m4) above.
- **(r4-m5) R^alpha.** Accepted, re-derived: for a solution, (Gamma + c_Gamma) P(H) = 0, so DP(H)[Gamma h_R] =
  -DP(H)[Gamma Sigma] - M_Gamma P(H), and for Sigma itself (Gamma + c_Gamma) P(Sigma) = DP(Sigma)[Gamma Sigma] +
  M_Gamma P(Sigma); subtracting, the M_Gamma P(Sigma) terms cancel and DP(H)[Gamma h_R] = -(Gamma + c_Gamma)
  P(Sigma) - (DP(H) - DP(Sigma))[Gamma Sigma] + M_Gamma(P(H) - P(Sigma)) at fixed arguments, the last two linear in h_R
  (rows (A) and (C)). So R^alpha = prod_i (Gamma_i + c_i) P(Sigma), with no M_i applied to P(Sigma): otherwise mu d_mu
  P(Sigma) = O(lam r^-6) (Sigma_4 cancels degree -6 only at mu = mu_end) would give the kernel 4 - a. The residual's
  kernel stays 9/2 - a.
  [R6 (nit): the last term is -M_Gamma(P(H) - P(Sigma)) (R6.0, nits); it is bounded in absolute value, so nothing
  changes.]
- **(r4-m6) The multilinear row (B).** The text's q = a + 1/2 is right (an undifferentiated slot through Hardy, the
  other in sup with r |d d h_R| <= eps_B r^(-1/2-a)); `boot5.py` had 3/2 + a. Corrected there, and B6c now expects the
  two rows with exponent a + 1/2 (rerun; it passes).
- **(r4-m7) B13.** Accepted: B13a passed a transport input at exactly q = 5/2 through "or q < 3" (`b13probe.py` of the
  reader, re-derived: min(prods) = 5/2). The "no logarithm" of Lemma R4.4 rests on Theorem A_P's coefficient classes
  (N1STAR-PROOF.md:1266-1269): in (c) the unknowns enter as E_(3/2) m_m, E_(3/2) Psi_m, E_(3/2) ell phi_m, E_(5/2)
  d_v phi_m and E_(5/2) r^-1 Omega phi_m; in (a) as E_2 m_m, E_3 d phi_m and E_(3/2) gh_(m+1); the known sources lie in
  L_3. With m_m, ell phi_m, Psi_m, r^-1 Omega phi_m in L_2, phi_m, d_v phi_m in L_1 and gh in O_2, every input of (a)
  and (c) has exponent >= 3 and of (b) >= 2 (`r5settle5.py` H1, to order 20; control H1': with d_v phi_m's class E_(3/2)
  an input at 5/2 appears). B13 is marked [arithmetic], superseded by H.
- **(r4-m8) F1c.** Accepted: it passes with the amplitude lam^2, showing only b != 0. `cclass5.py` C3 shows the wave's
  part b(g0 + U3) - b(g0) of lam-order 0 (its largest value over four phases bounded and bounded away from 0 for
  lam = 1e-2, 1e-3, 1e-4), and fails under the amplitude lam^2 (C3'). F1c's label is corrected.
- **(r4-m9) B10b** now tests R^(a+3/2) phi_R''(R + 1/2) = psi''(1/2) = -1, with the weighted energies of phi_R and of
  phi_R' bounded (rerun).
- **(r4-m10) eps.** From here on eps_B denotes the bootstrap's size (round 4's eps in R4-D-R4-F), and eps III.K's
  threshold.
- **(r4-m11) R4.4's citation.** Part VII Lemma 1.1 concerns Omega'. The transfer to P: on P the oscillating profiles of
  stage m are the transport solutions from past null infinity along ell at fixed v (Theorem A_P, N1STAR-PROOF.md:1237-
  1239; Lemma 5.3 (c)), with data the envelope-multiplied radiation field and sources products of earlier stages'
  profiles at the same v; for v > v_end both vanish (by induction on the stage), so the profile does, by uniqueness of
  the transport with nothing incoming.
- **(r4-m12) R4.5's means.** On N, s = 0 and Sigma = sum_p r^-p G_(2p)(v1) has no Taylor terms; off N, on the band,
  h_R contains Sigma's Taylor terms beyond r^-4, of size O(lam r^(-9/2)), which are not lam-independent per j: R4.5's
  sentence should read "sum_j lam^j (m_j's remainder), each lam-independent, and Sigma's terms beyond r^-4, O(lam)".
  The O(lam^2) flux bound is unaffected.
- **(r4-m13) The paper text.** R5-E excludes the amplitude A* of Proposition 3.1 (d) and says that eps, delta and
  lam_1 change with the class (R2.4), none evaluated.
- **R4.7** is restated in R5-C: what is shown is that the written chain does not close; each of its two inequalities is
  sharp in the class separately (B3a, B10c; B10b), but no single field is shown to make their product sharp.
- **Nits.** R4.8's zero-order coefficient bound reads r |d d H| <= C (mu + lam) r^-3 + C eps_B r^(-1/2-a) (d d g_b0's
  mu r^-3 term). Step 1's c1 = 0.24, c2 = 0.76 bound T(d_t, -grad t~) without sqrt|g| (B1b bounds that factor, in [0.9,
  1.1]; B1a also passes at |H| <= 1/5, so its margin is loose). The table's B(H) and deformation rows carry the factors
  𝔈^(1/2) and 𝔈 respectively, omitted there. Run times (measured by the reader, in parallel): order5 1.7 min, f1lemma5
  2.3, boot5 6, vac5 9 (round 4 stated "about half an hour" for vac5).
- **Checks that cannot fail given hand-entered inputs.** Marked [arithmetic], with a note in each docstring: `order5.py`
  O1b (its first clause), O1d, O2b-O2d, O3c, O3e, O5a-O5c; `f1lemma5.py` F1e, F1e', F1e''; `boot5.py` B4c-B4e, B6a-B6d,
  B8a, B8c, B10a, B10d, B11a-B11c, B12a, B12b, B13a, B13b; `vac5.py` V2a-V2e. What they take as input is now measured
  where it carries the argument: the coefficient rows of B6 and V2a on the operator (O1), the degrees behind B8 on the
  operator (O2: P(g_b0 + Sigma_2) decays like r^-6 and P(g_b0 + Sigma_(5/2)) like r^(-13/2), the flat part cancelling
  exactly; control: a non-solution leaves degree -4), the caps and tails of B12, T2, T7 and V2b-V2c on explicit fields
  (G2-G3), B13 by H.
- **Unexercised claims**, each now: R4.6 at spatial infinity and the continuity of 𝔈 (R5-B; D4-D5, F1-F5); u* (E1); the
  sizes of the (A) and (C) coefficients (O1); P(Sigma)'s degree (O2 for its inputs; with Sigma_4 it is deduced, below)
  and F_4's existence (deduced, R5-C); R4.8's uniformity (R5.2); the class of c (C2); R4.3's uniqueness step (deduced:
  g_app^(N(k)) - g_app^(N(6)) = sum_(j > N(6)) lam^j [g_j] is lam^N(6) t^(-3/2) in C^1, inside (P-v)'s class, O5b
  [arithmetic]; not computable beyond that); invariance (O3).

**(c) The reader of N1STAR-PROOF.md section 11** (its Major 1, on Lemma 11.0; its other findings, on (9.10), Theorem
M (c), past5.py P7 and section 11's minors, belong to another repair and are left alone here). Its Major 1 is the gap
R4-B named: b . d U is of the order the step estimates, and R4-B closes it once its notes are repaired. Each note is
folded into R5-D's text and given computational support:

- (s11-1) c's remainder is E_(3/2), its lam^0 term -(.)(ell, ell)[d_v d_th W_TT] from the envelope: as (r4-m1);
  `cclass5.py` C1-C2.
- (s11-2) R_gamma^n is defined inside Edit 2 ("R_gamma^n being R_gamma with g_n and u_1^n in place of g_lam and u_1");
  `r5edits5.py` E1 checks that it is defined there, and R_gamma before it (control: the current text fails both).
- (s11-3) d u's lam^0 terms: dv [d_th chi] dv dv in E_2 and the phase shift's term in E_(5/2), besides dv [d_th W_TT]:
  `r5edits5.py` E2 (two-scale chain rule, exact: the lam^0 part of d(lam [W_TT(. + phi_1)]) - dv [d_th W_TT] decays like
  r^(-5/2) for phi_1 in L_1, and that of d(lam [chi dv dv]) like r^-2; control: with phi_1 not decaying the first term
  is E_(3/2), and the class claim fails). The class of b is unchanged.
- (s11-4) the u_1-free source d_X^gamma F_1(X, 0, 0), in E_3: named in R_gamma; `r5edits5.py` E3 measures
  |F_1(X, 0, 0)| = |Ric^H(g0 + U3)| along a ray on the full operator, decaying like r^-3 (control: an amplitude r^-1 in
  place of r^(-3/2), not a radiation field, decays like r^-2).
- (s11-5) the factor 1/2 and the binomial coefficients C(gamma, gamma') in both Leibniz sums: E1 checks them in the text
  (control: the original lacks them).
- (s11-6) b . d U, c U and the |gamma'| = 1 terms enter through the source f of Lemma 9.5's energy inequality, before
  Gronwall's lemma, with ||f|| <= C(1 + lam^-1) t^(-3/2) sum ||d U'|| + ||R_gamma||, not through its kernel ||d gt||:
  R5-D says so (E1 checks the sentence; the inequality's structure is the energy identity of the reader's
  `energy_kernel.py`, bulk linear in (d g, b); the factor's integral, `f1lemma5.py` F1e [arithmetic]).
  [R6 (nit): energy_kernel.py is the section-11 reader's and is not in checks/; the structure is Lemma 9.5's proof, and
  the factor and Gronwall's lemma are computed in r6edits5 E2d-E2e.]
- (s11-7) "by Theorem P for the lowest" reads "by (9.8) for u_1^n at the lowest": E1 checks it.

### R5-A The round-3 corrections, re-derived

**Proposition R5.4 ((Poly) on the far region, R3.1 corrected; deduced, computed A1-A2).** For J >= 4 and n, m >= 0
there are C and lam_0 > 0, depending on J, n, m and the record's data and not on K, such that for 0 < lam <= lam_0 on
{t_P >= lam^-2 + d1}, for |alpha| + |beta| <= n,

    |d_X^alpha Omega^beta ell^m u_J| <= C lam^(-(3J - 9 + |alpha| + m)) r^(-(J+1)/2 - m),
    |d_X^alpha G_k| <= C lam^(-(k - 4 + |alpha|))  (k >= 4).

*Proof.* As R3.1 (R3-B (f)), with the stage rule re-derived from every monomial: the source of u_J's equation is
S~ (r-order >= (J + 4)/2) plus r^-q S_q (q = (J + 3)/2, which defines G_(J+1)); its monomials are products of
m >= 1 factors from {G_3, ..., G_J, u_J} with a coefficient of degree 0, -2, -3, -4 or -6 (eta, mu r^-2, Gamma[g0],
d d g0, (d g0)^2) and two derivatives, each a d_v (lam^-1) or an r-derivative (r^-1). On r >= lam^-2, |d^d u_J| <=
C lam^-d r^-2 (u_1's bound |d^alpha u_1| <= C lam^(1-|alpha|) t^-2 and r^(-k/2) lam^(-(k-4)) <= r^-2 there), and every
excess half-power of decay beyond (J + 4)/2 is a power of lam (r^(-1/2) <= lam). The explicit monomials of S~ then have
order <= J - 2 (an m-fold product has lam-order minus twice its r-order at most 2 - 4m, so m = 1 with a coefficient of
degree 2 and m = 2 bound it), the terms with one u_J factor at most B_J + 1 (u_J times d d (r^(-3/2) G_3) and
d u_J . d(r^(-3/2) G_3): the coefficients c and b of F1), those with two or more at most B_J + 1 after the trade, and S'
adds e(G_(J+1)) + 1 = J - 2. The energy step is lam-free (Lemma 9.5's kernel on the far region, R4-B), Lemma 9.3 adds
2 and each ell 1. So B_(J+1) = 2 + max(B_J + 1, J - 2), B_3 = -1, B_J = 3J - 9. ∎ (A1: e(G_k) = k - 4, k = 4..13; A2:
B_J = 3J - 9, J = 4..12, the same at m_max = 6 and 7; A2'': without the trade no bound.)
[R6 (nits): "a coefficient of degree 2" reads "degree -2"; "Lemma 9.5's kernel" means the Gronwall exponent (R6.0); the
"+2 for Lemma 9.3" is measured in r6settle5 L, and the coefficient list is computed from g_b0 in A0.]

The inputs of R3.1 are unchanged: (e), i.e. Proposition 9.8 at order n + 4, which is R4.1.

### R5-B Theorem R4.6 at spatial infinity (the round-4 reader's M4)

The following replaces R4-D's paragraph "*The truncations.*" from "On W, Phi_W := v + 1/r" to its end, and adds to
Steps 2, 4 and 6; everything else in R4-D stands, with eps_B for its eps and u* := sup_W f + 1.

*The localisation (replacing round 4's).* For V_* > v1 let D_*(sigma) := W cap {T <= t~ <= sigma} cap {Phi_W <= V_*}.
It is bounded (on it v1 <= v <= V_* and T <= t - f(r) <= 0, so r <= V_* - T + sup|f|). For every metric g with
|g^-1 - g_b0^-1|_op <= r^-2/2, Phi_W is a time function (D4-D5), so the truncated solution on D_*(sigma) is determined
by its data on Sigma~_T cap {Phi_W <= V_*} together with the data of Lemma R3.3 on the part of {t~ = T} in P' cup
Omega' that the past of D_*(sigma) meets; it is obtained from the record's local theory on bounded domains (Step 8,
N1STAR-PROOF.md:412-456) with the data extended smoothly and arbitrarily beyond, the extension not seen in D_*(sigma).
The data themselves are not changed: on Sigma~_T they are g_lam's, the band's and g_b0 + Sigma, so h_R vanishes beyond
the band. (Round 4 set them to g_b0 beyond V_* + 2, which makes h_R = -Sigma there, of infinite weighted energy for
a >= 1: F4.) The solutions for different V_* agree on overlaps; the local existence time is uniform in V_*, the data
beyond the band being g_b0 + Sigma, smooth with bounded derivatives.

*Finite energies (added to Step 6).* On the existence interval [T, sigma_1), every 𝔈_k(sigma) of the full slice is finite
and continuous in sigma. On the part of Sigma~_sigma inside the domain of influence of the band and of N's data (where r
<= C(|T| + 1): v grows at most at rate 2 + O(eps_B) along causal curves) it is the integral of a smooth function over a
compact set. Beyond it, Gamma^alpha h_R solves its commuted equation (R4d) with the source -prod (Gamma_i + c_i) P(Sigma)
= O(lam r^(-13/2)) (R5.0 (r4-m5); every Gamma keeps the degree, Z (r^-p F_p(s)) = -p r^-p F_p(s)) and data at T of the
same size (h_R and d_t h_R vanish beyond the band, the higher time derivatives are given by the equation). On the
exterior region {r >= R + 2(t~ - T) + C}, whose inner boundary moves outward faster than light and so is a future
boundary with flux >= 0 (the identity F2, computed in the flat radial model for the null case), the unweighted energy is
at most C |T|^2 lam^2 R^-9 by Gronwall over the bounded interval, and summed over dyadic R the weighted energy converges
for a < 9/2 (F5; control F5': with the source O(r^-6) of a Sigma without F_4, only for a < 4). Continuity in sigma
follows by dominated convergence. So 𝔈_k1(sigma) is finite and continuous, as Step 6's continuity argument needs.
[R6 (m1): this paragraph ran the identity on an unbounded region and cited dominated convergence; it is written out in
R6-A (i)-(iv), on bounded regions cut by {Phi_W <= V_*}, with the continuity from a dyadic tail bound uniform in sigma
(r6settle5 X1-X4).]

*The pointwise bounds (added to Step 2).* With 𝔈(sigma) finite, int^oo r^(2a+3) F^2 dr < oo for F = d Gamma^beta h_R
and for its r-derivative (the latter by Z4a, as in Step 2), so liminf_(R' -> oo) R'^(2a+4) F(R')^2 = 0 (F3'), and S1
on [R, R'] with its boundary term R'^(2a+3) F(R')^2 (F3: the identity) gives S1 on [R, oo) in the limit along that
sequence; Hardy's inequality likewise (its outer boundary term R'^(2a+2) phi(R')^2/(2a+2) vanishes along a sequence).
So (R4b) holds as written.
[R6 (m2): Hardy's outer boundary term needs the field to vanish at infinity first, and S1 needs no Hardy; written out in
R6-A (v)-(vi) (r6settle5 Y1-Y2).]

*The energy identity (added to Step 4).* (R4e) is applied on D_*(sigma). Its boundary has, besides Sigma~_sigma cap
{Phi_W <= V_*}, Sigma~_T cap {Phi_W <= V_*} and N cap D_*(sigma), the piece {Phi_W = V_*} cap {T <= t~ <= sigma},
spacelike (D4-D5) and to the future of D_*(sigma), whose flux T_g[phi](X, -grad Phi_W) is >= 0 because X = w d_t and
-grad Phi_W are future timelike (F1, sampled; control F1': for the normal grad r of a timelike cut-off it is negative
somewhere). Dropping it, (R4e) holds with E_sigma restricted to {Phi_W <= V_*} on the left and every integral on the
right taken over D_*(sigma). As V_* -> oo the left side increases to E_sigma (monotone convergence), and the right side
converges to its full-slice value, each integrand being integrable by the finite energies above and Step 5's kernels.
So (R4e) holds on the full slices as an inequality, which is all Steps 5-6 use.
[R6 (m4): F1 now takes the minimum over the covector exactly, and F1x computes the sign exactly.]

**Theorem R5.1′ (= Theorem R4.6 with the window (l0 - 1, 3) and R5-B; deduced, every identity computed, the
coefficients' and residuals' degrees measured on the operator, the caps and tails on explicit fields).** Under R4-D's
setting with a in (l0 - 1, 3), u* := sup_W f + 1 and eps_B for the bootstrap's size, the conclusions of Theorem R4.6
hold. *Proof.* R4-D Steps 1-9 with the additions of R5-B. ∎

### R5-C The other repairs of round 4

**Proposition R5.2 (uniqueness at weight a_0; replaces R4.8; deduced, computed B11).** Let a_0 in (0, 1/2) and let
g' = g_b0 + h' be a smooth metric on W with Ric^H(g') = 0, g' = g_lam on N with its first derivatives, |h'| <= 1/50,
sup_(sigma <= 0) E_sigma[Gamma^alpha h'] < oo for |alpha| <= 3 and Gamma in {d_t, L_Omega, Z} (energies of weight a_0),
and E_sigma[h'] -> 0 as sigma -> -oo. Then g' = g of Theorem R5.1′.
*Proof.* As R4.8, with (R4b) at weight a_0 now uniform in sigma: |d h'| <= C r^(-3/2-a_0), |h'| <= C r^(-1/2-a_0) with
C independent of sigma (S1 and Hardy on [r_sigma, oo) by R5-B's sequence argument, the energies bounded uniformly), so
the kernels q = 3/2 + a_0 and q = min(3, a + 1/2) of B11 are integrable with sigma-independent constants; the
zero-order coefficient is r |d d H| <= C (mu + lam) r^-3 + C eps_B r^(-1/2-a). ∎ The class contains every candidate
with a radiation-free r^-2 approach and bounded commuted energies.
[R6 (m2): the uniformity in sigma needs the limit of h' at spatial infinity to be shown to vanish before Hardy is used;
the proof is rewritten in R6-A (r6settle5 Y1-Y3).]

**Proposition R5.3 (R4.7 restated; deduced, computed B3, B10).** In the existence scheme of R2.5/R3.4 as written
(energies of weight a_0 <= 1/2 of Gamma^alpha h, h := g - g_b0, pointwise bounds by S1 and H^2(S^3)), the top-order
term -(1/2)(Dg^-1[Gamma^alpha h])^(ab) d_a d_b h is bounded only through Hardy for Gamma^alpha h and Sobolev for
d d h, giving the kernel (1 + |sigma|)^(-a_0-1/2), not integrable (B10a [arithmetic]). Each of the two inequalities is
sharp in the class separately (Hardy's constant, B3a and B10c; Sobolev's bound on d d h by the band family, B10b), but
no single field is shown to make their product sharp. So the written chain does not close; nothing is claimed about
other estimates in that class. Theorem R5.1′ does not use the scheme.

*Smaller repairs.* (i) Step 3's residual is R^alpha = prod_i (Gamma_i + c_i) P(Sigma) (R5.0 (r4-m5)). (ii) The table's
multilinear row has q = a + 1/2 (R5.0 (r4-m6)). (iii) Lemma R4.4's transfer to P and Lemma R4.5's means as in R5.0
(r4-m11), (r4-m12). (iv) (Pr) at order k1 + 5: R4.5 (ii)'s "(9.9a) at order k1 + 4" and R4.10's "N(K, k1 + 4)" read
k1 + 5, and lam_2 <= lam_F(k1 + 5). (v) F_4 exists: harmonic by harmonic, the degree -4 equation with the degree -6
source of mu r^-2 F_2 and of the quadratic terms in r^-2 F_2 (present: O2) is (s - s^2/2) F'' + (7/2)(1 - s) F' -
(1/2)(8 - l(l + 2)) F = S_l(s), S_l smooth on [0, 3/2]; s = 0 is a regular singular point with exponents 0 and
3/2 - 4 = -5/2, whose difference is not an integer, so there is a unique solution analytic at 0 (Frobenius), and the
next singular point is s = 2, so it extends smoothly to [0, 3/2]; the sum over l converges with all derivatives as for
F_p (B9c), S_l decaying rapidly in l for smooth G_4(v1). With it P(Sigma) = O(lam r^(-13/2)) (B8's degree count
[arithmetic], its inputs measured in O2).
[R6 (r6-F4): F_4 is constructed on the full operator in r6sigma5 S1-S4; and it is not needed: with F_4 the flat
solution, P(Sigma) = O(lam r^-6) and every estimate still closes on the window (R6.0).]

### R5-D The replacement text for N1STAR-PROOF.md's Lemma 11.0 (final)

Two edits, for N1STAR-PROOF.md as of md5 709c63be (not edited here). They supersede R4-B's Edits 1-2 and incorporate
the round-4 reader's m1 and m2 and the section-11 reader's notes 1-7 (R5.0 (c)). Each old string occurs exactly once in
the current file; applied to a copy, the file gains 23 lines and every line stays within 121 characters
(`checks/r5edits5.py` E1, which applies the blocks below as printed here). Edit 1's new text is followed on its last
line by the unchanged " The identity is not run on the region between {v =", Edit 2's new text is preceded on its
first line by "U_n(tau_n)|| <= C(lam, j) t_n^(-1/2) with t_n >= t. " and followed by " The bookkeeping of sup against".
[R6 (m7): the line numbers given as "now" below are stale against the live file; R6-D, keyed by content, with the
reader's four nits, supersedes this section.]

Edit 1, old (lines 10553-10562 now):

```text
*Proof.* By Lemma 11.1 below, u_1 = u - r^(-3/2) G_3 solves -(1/2) g_lam^{ab} d_a d_b u_1 = F_1 := S(u) - (1/2)
(g_lam^{ab} - g0^{ab}) d_a d_b u_1 + (1/2) box~ (r^(-3/2) G_3), and F_1 is in E_3 with all derivatives (S(u) by Lemma
11.1; the second term is E_(3/2) E_2; the third is in E_(7/2) by Lemma 9.7(c) and P2), where "all derivatives" of a term
containing u_1 means the orders already controlled. Induction on the order: for |gamma| = j + 1, U := d^gamma u_1 solves
-(1/2) g_lam^{ab} d_a d_b U = d^gamma F_1 + sum_{0 < gamma' <= gamma} (d^{gamma'} g_lam^{ab}) d^{gamma - gamma'} d_a d_b
u_1. The terms with |gamma'| = 1 are (d g_lam) d U with d g_lam in E_(3/2), of the kind Lemma 9.5's kernel k absorbs; a
term with |gamma'| >= 2 is a product of a derivative of g_lam of order <= j + 1 with one of u_1 of order <= j + 1, and is
estimated in L^2(Sigma_tau) with the factor of higher order in L^2 (the energies of the lower steps, at most C t^(-1/2))
and the other in sup norm (E_2 by the induction hypothesis, through Lemma 9.3 for the orders it costs, and by Theorem P
for the lowest), so the source is at most C(lam, j) t^(-3/2) in L^2.
```

Edit 1, new:

```text
*Proof.* By Lemma 11.1 below, u_1 = u - r^(-3/2) G_3 solves -(1/2) g_lam^{ab} d_a d_b u_1 = F_1 := S(u) - (1/2)
(g_lam^{ab} - g0^{ab}) d_a d_b u_1 + (1/2) box~ (r^(-3/2) G_3). By (0.2), F_1 = -Ric^H(g_lam) - (1/2) g_lam^{ab} d_a
d_b u_1 with g_lam = g0 + r^(-3/2) G_3 + u_1, so F_1 contains no second derivative of u_1 (`checks/f1lemma5.py` F1a):
it is a smooth function F_1(X, u_1, d u_1), and F_1(X, 0, 0) is in E_3 with all derivatives (the terms of Lemma 11.1
in G_3 and g0, and the third term, in E_(7/2) by Lemma 9.7(c) and P2; `checks/r5edits5.py` E3). Along g_lam its partial
derivatives are b := dF_1/d(d u_1), in E_(3/2) and of lam-order 0 (the derivative of the Q-difference, linear in d g0 +
d u; d u is of lam-order 0: dv [d_th W_TT], plus dv [d_th chi] dv dv in E_2 and the phase shift's term in E_(5/2), plus
O(lam); `checks/cclass5.py` C3, r5edits5.py E2), and c := dF_1/d u_1 = -(1/2) lam^-1 (.)(ell_lam, ell_lam) [d_th^2
W_TT] + E_(3/2), ell_lam := g_lam^-1 dv (the first term from -(1/2)(g_lam^-1 u_1 g_lam^-1)^{ab} d_a d_b (lam [W_TT]), as
in (3.2); the E_(3/2) part contains -(.)(ell_lam, ell_lam) [d_v d_th W_TT], from the envelope's dependence on v; F1b,
cclass5.py C1-C2). Induction on the order: for |gamma| = j + 1, by Leibniz's rule U := d^gamma u_1 solves

    -(1/2) g_lam^{ab} d_a d_b U = f_gamma := b . d U + c U
        + (1/2) sum_{|gamma'| = 1} C(gamma, gamma') (d^{gamma'} g_lam^{ab}) d^{gamma - gamma'} d_a d_b u_1 + R_gamma,

C(gamma, gamma') := gamma!/(gamma'! (gamma - gamma')!), where R_gamma := d^gamma F_1 - b . d U - c U + (1/2)
sum_{|gamma'| >= 2} C(gamma, gamma') (d^{gamma'} g_lam^{ab}) d^{gamma - gamma'} d_a d_b u_1 contains derivatives of
u_1 of order <= j + 1 only (the chain rule, F1d). In f_gamma, b . d U is of the order this step estimates and is not
known; the terms with |gamma'| = 1 are (d g_lam) d U' with d g_lam in E_(3/2) and U' in the same family {d^gamma u_1 :
|gamma| = j + 1}; and c U is one order lower. They enter through f in Lemma 9.5's energy inequality, before Gronwall's
lemma, not through its kernel ||d gt||: ||b . d U|| <= C t^(-3/2) ||d U||, ||c U|| <= C lam^-1 t^(-3/2) ||U|| <= C
lam^-1 t^(-3/2) ||d U|| by Lemma 9.3(b) (U vanishes on {v = v_start}), so ||f_gamma|| <= C(1 + lam^-1) t^(-3/2)
sum_{|gamma'| = j + 1} ||d d^{gamma'} u_1|| + ||R_gamma||; summed over the family, Gronwall's lemma then costs the
factor exp(int C(1 + lam^-1) t^(-3/2)), at most e^(2C(1 + lam)) over the far region t >= lam^-2, a lam-free factor.
(With c U taken as a source, through the energies of the lower steps, the step also closes at fixed lam, at one lam^-1
per order.) R_gamma is the sum of d_X^gamma F_1(X, 0, 0), the u_1-free source, in E_3, and of products of a derivative
of g_lam or of F_1's coefficients of order <= j + 1 with derivatives of u_1 of order <= j + 1, each estimated in
L^2(Sigma_tau) with the factor of higher order in L^2 (the energies of the lower steps, at most C t^(-1/2)) and the
others in sup norm (E_2 by the induction hypothesis, through Lemma 9.3 for the orders it costs, and by (9.8) for u_1^n
at the lowest), so
||R_gamma|| <= C(lam, j) t^(-3/2).
```

Edit 2, old (lines 10571-10572 now):

```text
Lemma 9.5's identity then gives ||d U_n(tau)|| <= ||d U_n(tau_n)|| +
C int_{tau_n}^tau t'^(-3/2) dtau' <= C(lam, j) t^(-1/2) at every order, uniformly in n.
```

Edit 2, new:

```text
Lemma 9.5's energy inequality with that f and
Gronwall's lemma give sum_{|gamma| = j + 1} ||d U_n(tau)|| <= C e^(2C(1 + lam)) sum_{|gamma| = j + 1} (||d
U_n(tau_n)|| + int_{tau_n}^tau ||R_gamma^n|| dtau'), R_gamma^n being R_gamma with g_n and u_1^n in place of g_lam
and u_1, so ||d U_n(tau)|| <= C(lam, j) t^(-1/2) at every order, uniformly in n.
```

### R5-E The theorem, its status, and the paper's text

**Theorem R5.1 (Theorem R4.10 restated with every condition).** Fix A, the C_c^∞ envelope of Theorem 1, the angular
profile and the seed. Let l0 in (3, 4) \ {7/2}, l_I in (3, l0) off row d2's exclusion sets, eps_m > 0, eps_t < eps_K;
let eps, d_1 be III.K Theorem 4.3's in the half class ℰ_0^½ = {(2 + j/2, 0) : j in ℕ_0} (Theorem R2.4), below Part VII
Proposition 3.2's equivariant threshold; let a in (l0 - 1, 3), k1 := max(8, d_1 + 4), M := 15 + 2(k1 + 1) (Proposition
R5.4; any larger M serves), K > max(d_1 + 14, K*(a, 8, M, k1)) (Lemma R3.2 with s := max(5/2, (2M + 1)/(7 - 2a))), and
the approximant of order N(K, k1 + 5) (Corollary R4.3). Then there is lam_2 > 0, lam_2 <= min(lam_P(K, k1 + 5),
lam_F(k1 + 5)), not evaluated, such that for every 0 < lam <= lam_2 (no exceptional set):

- (1) g_lam continues to the past domain of dependence W of Sigma_IVP cap {r >= 4R} as a smooth vacuum metric in the
  record's wave-map gauge relative to g_b0 (Theorem R5.1′, Proposition R4.9), G-invariant (R5.0 (r3-m4)), and it is the
  only continuation in that gauge with |h'| <= 1/50, uniformly bounded commuted energies of weight a_0 in (0, 1/2) and
  energy tending to 0 toward past null infinity (Proposition R5.2);
- (2) its data (gamma, k) on Sigma_IVP lie in III.K's class with ℰ_0 = ℰ_0^½ and ||.||_(d_1) < eps (Step 9 on S, with
  R5-B; Part VII Lemma 1.1 with K >= d_1 + 15 on Sigma_IVP cap {r <= 4R});
- (3) the maximal vacuum development of (gamma, k) settles to a Tangherlini metric g_(m',0), |m' - mu_end| < eps_m, at
  the rate |(t_* d_(t_*))^i d_x^beta (g - g_(m',0))| <= C t_*^(-2-eps_t) on {r_0 <= r <= R', t_* >= T'}, by Theorem
  R2.4 and Part VII Proposition 3.2, with no gluing.

*Proof.* As R4.10, with R5.1′ for R4.6, R5.2 for R4.8, Proposition R5.4 for R3.1, and the invariance of R5.0 (r3-m4).
∎

*Status (the round-4 reader's M1).* **Deduced**, in this file (rounds 1-5; rounds 1-4 read by verifiers, every finding
seated in R5.0; round 5 not yet read), and **conditional on**: Part IV's seven outputs, III.K Theorem 4.3, Part VII
Lemma 1.1 and Proposition 3.2 (all listed as proved in proof5/README.md; R3-A); Theorem P (proved, N1STAR-PROOF.md:24-27;
used at every order through Corollary R4.3, deduced here from Propositions R4.1-R4.2); and **N1STAR-PROOF.md section
11.1** (Lemmas 11.0-11.2 and Proposition 11.1: deduced, its D44 repair not yet read, N1STAR-PROOF.md:29-34), which
Proposition R5.4, Lemma R3.2, Lemma R4.4, Lemma R4.5 (i) and Step 9 use. It rests on no statement of Part IX. What has
to be read for the label "proved": (a) section 11.1 of N1STAR-PROOF.md with R5-D's two edits applied (the D44 repair
included); (b) this file's statements that the theorem uses: Lemma R2.1, Proposition R2.2 (computed for every round
count III.C′ uses, M <= 12, exactly below 11/2) and Theorem R2.4, Lemmas R3.2-R3.3 (as amended), Propositions R4.1-R4.2,
Corollary R4.3, Lemmas R4.4-R4.5, R4-D with R5-B (Theorem R5.1′), Propositions R4.9, R5.4 and R5.2, and Theorem R5.1;
(c) the programs they cite. Nothing else is open in the theorem; lam_2, eps, delta and lam_1 are not evaluated (R5,
another workstream), in either class.
[R6 (m5): superseded by R6-E's status: the D44 clause is stale (D45 and D47 read that repair), and the list omitted
statements the deduction uses.]

*Computational support, stated as what was computed.* The operator identities ((5.1), (R3a), (R3c) in Cartesian and in
invariant form, (R4c), the contracted Bianchi identity, the localised energy identity) are computed, on the full
operator where the operator enters; the coefficients of DP(H) and the degrees of P(g_b0 + Sigma_p) are measured on the
full operator (O1-O2); the class of c and the lam-order of b on it (C1-C3); h_R's decay, the caps, the null-hypersurface
tails, the class on S and the weight window on explicit fields (G1-G6); the lam-orders of the expansion from every
monomial (A); the remaining kernel exponents (the residual's after F_4, the bulk-sign error, the deformation, the
uniqueness kernels and the D-system's) are counted by hand, their integrability checked ([arithmetic]).
[R6 (m6, m8): the weight window here was G5, [arithmetic]; it is computed in r6sigma5 W, and R6-E restates this
paragraph.]

*The text for the paper's section 9* (RESPONSE-HL-5D.md, not edited here; the old texts occur exactly once in the
current file, checked).
[R6 (m6): superseded by R6-E's blocks.]

Block 1, in "Settling", old:

```text
  not evaluated. Theorem 4 (i) concerns glued data that agree with g_λ's on a ball; settling of g_λ's own continuation
  is not shown. Evaluating λ1 and δ would need every constant of the write-out made explicit, and several come from
```

Block 1, new:

```text
  not evaluated. Theorem 4 (i) concerns glued data that agree with g_λ's on a ball. That the development of g_λ's own
  data settles, with no gluing, is deduced in a data class wider than (ii)'s by half-integer orders, conditional on the
  supplement's section 11.1, whose repairs are not yet read (Beyond the boundary, below). Evaluating λ1 and δ would need
  every constant of the write-out made explicit, and several come from
```

Block 2, in "Beyond the boundary", old:

```text
  6.3, deduced). It is not shown that Theorem 4 applies to g_λ's own data: g_λ is given on Ω, which does not contain the
  whole initial slice, and continuing it to spatial infinity asks for a scattering problem from past null infinity and an
  expansion of its solution at spatial infinity. Parts of that are done (deduced, with exact computations, all under
  `docket68/n1star/`): the leading Coulomb part carried to spatial infinity with no logarithm (`checks/coulomb5.py`, and
  under the full operator `checks/coulombL5.py`), the map from data on the initial null hypersurface to the leading
  coefficient at spatial infinity, under the write-out's full operator on Minkowski space, bounded uniformly in the
  harmonic (reduced for every harmonic, `checks/harmonics5.py`; bounded, `checks/uniform5.py`), the remainder's sources,
  supported where v is bounded along the initial null hypersurface, entering one order later at every harmonic computed
  (l ≤ 12) (`checks/sources5.py`, `checks/stripfull5.py`), and the approximant's stage profiles expanded in powers of
  r^(−1/2) at past null infinity, with the closure properties of that expansion shown (deduced, with an exact check,
  `checks/closure5.py`). The scattering estimate itself is not done. Below the inner boundary the theorems are not
```

Block 2, new:

```text
  6.3, deduced). It is deduced, with no gluing, that Theorem 4 applies to g_λ's own data in a data class wider than
  (ii)'s by half-integer orders (supplement `docket68/n1star/SETTLE-GLAM5.md`, rounds 1–5, Theorem R5.1; conditional on
  Part IV, III.K and Part VII, proved, on Theorem P, proved, and on the supplement's section 11.1, deduced, whose repairs
  are not yet read). After the shell g_λ − g_b0 has at past null infinity an r^(−5/2) coefficient, O(λ^∞), which for a
  C_c^∞ envelope and every amplitude but at most one is nonzero off a discrete set of λ (computed for a bump envelope,
  `docket68/n1star/checks/tail5.py`); it puts an r^(−5/2) term into g_λ's data at spatial infinity, outside the integer
  orders of (ii)'s class. With the orders r^(−2), r^(−5/2), r^(−3), … below r^(−ℓ0) admitted in the metric (ℓ0 ∈ (3, 4),
  ℓ0 ≠ 7/2, and one order more in the second fundamental form), Hintz's construction runs with the same index sets for
  its iterates and finitely many more derivatives lost; its thresholds, and with them λ1 and δ, change and are not
  evaluated, in either class. g_λ continues to the past domain of dependence of the far part of Hintz's initial surface
  as a vacuum metric in the record's wave-map gauge, by one weighted energy estimate at a weight a ∈ (ℓ0 − 1, 3), run on
  bounded domains of dependence, after its self-similar terms through r^(−4) are subtracted; it is the only continuation
  in that gauge near Tangherlini whose commuted energies of weight a0 ∈ (0, ½) stay bounded, its energy vanishing toward
  past null infinity, and its data lie in the widened class with small norm. So for every 0 < λ ≤ λ2, λ2 not evaluated,
  with no exceptional set, the maximal vacuum development of g_λ's own data on Hintz's initial surface settles to
  five-dimensional Tangherlini of a mass m′ with |m′ − μ_end| < ε_m at Theorem 4's rate (deduced; the operator identities
  computed, the coefficient decays and the residuals' degrees measured on the write-out's full operator, the caps, tails
  and weight window measured on explicit fields, the remaining kernel exponents counted by hand with their integrability
  checked, all under `docket68/n1star/checks/`, `r5settle5.py`, `r5op5.py`, `cclass5.py` among them). Below the inner
  boundary the theorems are not
```

Block 3 (optional, section 8.1, for consistency with blocks 1-2), old:

```text
replaced by a gluing (section 8.7), and Theorem 4 is not shown to apply to g_λ's own data.
```

Block 3, new:

```text
replaced by a gluing (section 8.7); that Theorem 4 applies to g_λ's own data, with no gluing, in a class wider by
half-integer orders, is deduced in section 9 (Beyond the boundary).
```

Ledger. Computed: `r5settle5.py` A-H (43 checks), `r5op5.py` O1-O3 (7), `cclass5.py` C1-C3 (6), `r5edits5.py` E1-E3 (10),
`zinv5.py` ZI1-ZI2 (2; still running when this was written, its `.out` written by the program on completion; (R3c) is
computed independently in `scale5.py` Z1 and `boot5.py` B5), each with controls that mutate the code under test; rerun:
`poly5.py`, `scale5.py`, `trunc5.py`, `scatter5.py`, `boot5.py`, `order5.py`, `f1lemma5.py`, `vac5.py`, all passing (28,
25, 23, 16, 48, 22, 12 and 8 checks). Deduced: Propositions R5.2, R5.3, R5.4, Theorem R5.1′ (R4-D with R5-B), Theorem
R5.1. READ: N1STAR-PROOF.md (709c63be) 24-27, 29-34, 412-456, 1172-1184 (Lemma 9.5), 1237-1239, 1266-1269, 1424-1425,
1428-1431, 10550-10581; PART-VII-ASSEMBLY.md 31-38, 403-406; PART-III-K-NONLINEAR.md 470, 512-520. None from outside
sources. The verifiers' scratch scripts relied on are in `checks/` as `zinv5.py` (copied with a driver); their other
computations (K*, B_J, the class of c, B13's probe) are recomputed by this round's own programs (B, A, C2, H).
[R6 (m7, m8): zinv5 finished in round 6 (ZI1-ZI3), its m4 not a control; PART-VII-ASSEMBLY.md 403-406 is now 420-423
(md5 500c085b) and PART-III-K-NONLINEAR.md 470, 512-520 is now 471, 513-521 (md5 5b0ad3f0), by content.]

Open in the theorem: nothing beyond its status (the readings named above). Not evaluated: lam_2, eps, delta, lam_1.

    python3 checks/r5settle5.py   (about four minutes on a loaded machine)
    python3 checks/r5op5.py       (about seven minutes)
    python3 checks/cclass5.py     (about nine minutes)
    python3 checks/r5edits5.py    (about half a minute)
    python3 checks/zinv5.py       (five processes in parallel; over two hours on this loaded machine)
[R6 (m8, nit): measured run times are with round 6's run lines.]

## Round 6 (2026-11-06)

Status: written; not yet read by a verifier. Labels as in rounds 2-5: a check marked **[arithmetic]** computes a
consequence of exponents or rules entered by hand, and its control cannot fail under a mutation of the operator. New
programs, each with its `.out` from a full run, byte-identical on a second run, and with controls that mutate the code
or the text under test: `checks/r6settle5.py` (X, Y, M, L, A0, T), `checks/r6sigma5.py` (S1-S4: F_4 on the full
operator; W: the window computed as a whole), `checks/r6edits5.py` (E1-E4: R6-D applied to a copy of the live
N1STAR-PROOF.md, and the mathematics it states read from the text and checked). Changed and rerun: `r5settle5.py` (F1
exact, F1x; G5 with Lemma R4.5 widened, G5c; [arithmetic] labels), `r5edits5.py` (E1f: R5-D's mathematics read from its
text), `zinv5.py` (its evaluation repaired; its first complete run; control m5 in place of m4, which is a no-op, ZI3).
N1STAR-PROOF.md is cited here by quoted content, not by line number: another workstream (D625) is editing it while this
is written; every R6-D old text is checked by r6edits5 E1a to occur exactly once in the file as it stood at the final
run (md5 223e1749; also at fb2fbf06 and 7400212b, earlier states of that file while it was being edited). Rounds 1-5 are
left as their verifiers read them; where a finding below withdraws or corrects a sentence, a bracketed note "[R6 (...)]"
is inserted at the end of the paragraph or item that contains it, and the sentence is not changed. Sections R6.0 and
R6-A ... R6-E.

What this round settles, in one paragraph. The round-5 reader found no major gap and eight minors; each is re-derived
and seated (R6.0), and every claim its list names as exercised by no check now has a computation or, where it is not
computable, a complete proof. The two repairs of R5-B that the reader found incomplete are written out in full (R6-A):
the exterior energy estimate is run on bounded regions cut by {Phi_W <= V_*}, both of whose lateral boundaries are
future boundaries with a positive definite flux (computed, X1-X2), and the continuity of the energy follows from a
dyadic tail bound uniform in sigma (X4); Hardy's inequality is used only after the field is shown to vanish at spatial
infinity, which for h_R follows from its data and for Proposition R5.2's h' from the uniform bound on d h' (Y1-Y3), and
the boundary term then vanishes at every radius, not along a sequence. Lemma R4.5 holds on (0, 7/2) (M), the window
(l0 - 1, 3) is computed as a whole from exponents measured on the fields and on the operator (r6sigma5 W), and F_4 is
constructed on the full five-dimensional operator, which then decays two orders faster (S1-S4). F_4's source term turns
out not to be needed: without it P(Sigma) = O(lam r^-6) and every estimate still closes on the window (R6.0 (r6-F4)).
The flux sign is checked by an exact minimum over the covector (F1, F1x), and R6-D's mathematics is read from its text
and checked (r6edits5 E2), so the reader's four surviving mutants die. zinv5 never finished in round 5 for two reasons
that are not in the identity; repaired, it runs in 13 to 25 minutes and shows that one of its four controls could not
fail (R6.0 (m8)). R6-D is the final replacement text for N1STAR-PROOF.md's Lemma 11.0, with the reader's four nits; R6-E
restates Theorem R5.1's status with a complete conditional list and gives the paper's texts.

### R6.0 The round-5 reader's findings, and their dispositions

**(m1) R5-B's exterior energy ran on an unbounded region.** Accepted. Re-derived and repaired in R6-A (i)-(iv): the
identity is run on X_(rho, V_*) := W cap {T <= t~ <= sigma} cap {r - 2(t~ - T) >= rho} cap {Phi_W <= V_*}, which is
bounded; its two lateral boundaries are spacelike, with the region to their past (the inner one by r6settle5 X2: with
|f'| <= 1/4, g_b0^-1(alpha, alpha) <= -7/4 for alpha := d(r - 2 t~) and alpha(d_t) = -2 < 0; the outer one by D4-D5), so
their fluxes are >= 0 (F1x) and are dropped; Gronwall on the bounded interval with constants independent of V_* and rho,
then V_* -> oo by monotone convergence (X3). The identity with both lateral fluxes is computed exactly on the flat
radial model (X1; control X1': a timelike inner boundary, speed 1/2, gives a flux form with the eigenvalue -1/4). The
continuity of 𝔈 comes from the weighted tail bound C lam^2 rho^(2a - 9), uniform in sigma, summed over dyadic shells (X4
[arithmetic]), not from dominated convergence: 𝔈 is a uniform limit of continuous functions. Notes inserted at R5-B.
[R7 (minor 1): the outer cut is the cone {r + 2(t~ - T) <= V_*} since round 7; R7-A.]

**(m2) Hardy's outer boundary term needs a priori decay.** Accepted. Re-derived in R6-A (v)-(vi) and R6-A's proof of
Proposition R5.2. (a) S1 for F := Omega^gamma d Gamma^beta h needs no Hardy: along a ray of Sigma~_sigma, d/dr F is r^-1
d(Z Gamma^beta h) - r^-1 (t - v1) d(d_t Gamma^beta h) + f' d(d_t Gamma^beta h) plus first derivatives of Gamma^beta h
with coefficients O(1/r), exactly (r6settle5 Y1; Z4a); no undifferentiated term occurs, so the energies of first
derivatives of commuted fields bound it. (b) For h_R, Gamma^beta h_R(sigma, .) -> 0 at spatial infinity: its data at t~
= T vanish beyond the band except for time derivatives, which are O(lam r^(-13/2)), and |d_t Gamma^beta h_R| <= C
r^(-3/2-a) on [T, sigma] by (a); integrated in time at fixed x. (c) For Proposition R5.2's h', (a) gives |d h'| <= C_0
r^(-3/2-a_0) with C_0 independent of sigma; the limit c(sigma, xhat) of h' at spatial infinity exists, does not depend
on sigma (|d_t h'| <= C_0 r^(-3/2-a_0), the time segments lying in W), and |c| <= |g_lam - g_b0|(r_sigma) + C
r_sigma^(-1/2-a_0) -> 0 as sigma -> -oo, the inner edge of Sigma~_sigma cap W lying on N where h' = g_lam - g_b0 =
O(r^-2): c = 0. (d) Then phi = -int_r^oo d_s phi and Cauchy-Schwarz give r^(2a+2) phi(r)^2 <= (2a + 2)^-1 int_r^oo
s^(2a+3) (d_s phi)^2 ds -> 0 (Y2, 24 random fields that are not power laws), so Hardy's outer boundary term vanishes at
every radius and Hardy holds on [r_sigma, oo). Control Y2': phi = c + r^(-a-2) has finite derivative energy and a
nonzero limit, and Hardy fails for it. A model of (c) with its two controls (a constant added; a sigma-dependent limit):
Y3. Notes inserted at R5-B and Proposition R5.2.

**(m3) Lemma R4.5 is stated for a in (5/2, 7/2).** Accepted. Re-derived: its proof uses a only in (i) the finiteness of
the N-flux, ∫ r^(2a) r^-9 r^3 dr, and of the |H| |d phi|^2 term, ∫ lam r^(2a-8) dr, both finite exactly for a < 7/2
(r6sigma5 W2, W7), and in (ii) Lemma R3.2, stated for a in (0, (J' - 1)/2) = (0, 7/2) at J' = 8; nothing uses a > 5/2.
So Lemma R4.5 holds for every a in (0, 7/2), with K > K*(a, 8, M, k1). Independently, its fluxes are monotone in a,
since u* - u >= 1 on W (r5settle5 E1) gives w_a <= w_a' for a <= a' (r6settle5 M1; control M1'). G5 now includes R4.5's
hypothesis with Step 2's a >= 3/2 and Proposition R5.2's a > 1/2, and is marked [arithmetic]; its control G5c shows that
R4.5's round-4 hypothesis would give (max(l0 - 1, 5/2), 3). The window is computed as a whole in r6sigma5 W. Note
inserted at Lemma R4.5.
[R7 (nit): r^-9 reads r^-11: the flux density is |d h_R|^2 ~ r^-11 for h_R = O(r^(-9/2)), and int r^(2a) r^-11 r^3 dr is
finite exactly for a < 7/2, as stated.]

**(m4) F1 could not fail.** Accepted. F1 now takes the minimum over the covector exactly, as the least eigenvalue of the
quadratic form p -> T_g[p](X, n) (the minimum of r^2 lambda_min over 2000 points is 0.2678 > 0); the verifier's
mutations Phi = v - 1/r and |H| = 6 r^-2 now fail it (R6.0, mutants). The sign itself is computed exactly in F1x: for X
= e_0 and n = (cosh s, sinh s, 0, 0, 0) the form has the characteristic roots e^s/2, e^-s/2 and cosh(s)/2 (three times),
so it is positive definite for any two future timelike vectors (a g-orthonormal frame puts them in this position, and
congruence keeps definiteness); for n spacelike it has the root -e^-s/2.

**(m5) R5.1's conditional list.** Accepted; R6-E (status) replaces it. (a) The D44 clause was stale: D45 read the D44
repairs and found that "Lemma 11.0's new argument closes the thirteenth verifier's gap rather than moving it", and D47
found Lemma 11.0 "sound as repaired" (N1STAR-LOG.md, entries D45 and D47); the section-11 reader of D618 then found
Lemma 11.0's top-order gap (its Major 1), which R5-D, now R6-D, repairs: written, not applied. (N1STAR-PROOF.md's status
paragraph, as edited today, records the D45 and D47 reads and names R5-D as the pending replacement; R6-D supersedes
R5-D.) (b) The list now names what the deduction also uses: N1STAR-PROOF.md's Theorem E with Step 8's local theory
(R5-B, Step 6); Part VII Lemma 1.2 (R4-D's setting: R is free) and Lemma 2.1 (Step 9's computation of (gamma, k));
III.C'' Proposition 4.1 (III.K's gauge data rebuilt from (gamma, k), R4-F); BEYOND5 Lemma 6.4 (iv) (W and N); R5-C (v),
F_4's existence, in this file's list (now computed, and not needed: (r6-F4)); and N1STAR-PROOF.md's Lemma 11.2 as
amended by D618's repair. (c) Theorem P's uses of Lemma 1.1 (e) and Lemma 2.3 after D623 (and D625, D627), checked
against the live 0.3 and Lemma 2.3: they stand. On P the margin of Lemma 9.1 (f) is a bound on the inverse metric,
|g^-1 - g0^-1| <= eps_P t^(-5/4); Lemma 9.1 (f) says "the causal claim follows as in Lemma 1.1(e)", which uses Lemma 1.1
(e)'s argument (open conditions, past causal curves cannot cross the boundaries), not its eps1; and Lemma 9.5 says
"Lemma 2.3's proof on P cap {tau1 <= s <= tau}", whose constants need |gt^-1| and |gt| bounded and Y = -gt^-1 dtau
uniformly timelike. Those follow from the inverse margin: g0^-1(dtau, dtau) = -1 - m with m := mu/r^2, so
(g0^-1 + delta)(dtau, dtau) <= -1 + eps_P; the least absolute eigenvalue of g0^-1 is s(m) = (1 + m^2)^(1/2) - m, so for
eps_P < s(m*) (m* := sup_P+ m) every such g^-1 is invertible with |g| <= (s(m*) - eps_P)^-1 by Weyl's inequality; and {r
= a} stays spacelike for eps_P < mu0/a^2 - 1 (r6settle5 T, exact and 2000 samples; control T': |delta|_op = s(m) makes
g^-1 singular). These are D623's two thresholds, in the form the inverse margin takes (g0 and g0^-1 have the same least
absolute eigenvalue s(m), the (tau, r) block having determinant -1, so s0 of 0.3 is s(m*)); Lemma 9.1 (f)'s "There is
eps_P > 0" allows them, and nothing in Theorem P's proof needs eps1 of 0.3. (A clarifying clause in Lemma 9.1 (f),
naming eps_P < min(s(m*), mu0/a^2 - 1), would make this explicit; that is for the record's own session to decide.)
[R7 (nit): on Omega, Theorem P's (P-iv) rests on Theorem E, which uses eps1 of 0.3 as D623 amended it; that use is
inside Theorem E, proved, and the inverse margin of Lemma 9.1 (f) concerns P only.]

**(m6) The paper texts.** Accepted; R6-E's blocks replace R5-E's. They name condition (b) (rounds 5-6 of this file not
yet read), say that R6-D is written and not applied, separate what is measured (the coefficient decays and the residual
degrees on the operator, the caps and the N-flux tails on explicit fields) from what is computed from those measurements
(the window) and from what is counted by hand, write "supplement section 11.1" as the paper's Theorem 3 does, name eps
among the thresholds not evaluated, and cite the r^(-5/2) coefficient as "deduced, SETTLE Proposition 3.1; computed for
a bump envelope".

**(m7) R5-D's line citations.** Accepted. R6-D keys every citation of N1STAR-PROOF.md by quoted content; its old texts
are R5-D's, checked to occur exactly once in the live file (E1a). Re-keyed by the same rule, at the coordinator's report
and verified against the current files (by content): PART-III-K-NONLINEAR.md's "Theorem 4.3 ([Hin26] Theorem 13.1 at n =
4; conditional on Part IV)" is at its line 471 (cited as 468, and as 470 in R5.0's nit), and its (K2) "What Part IV must
deliver here" through "Theorem 4.3 is conditional on these" at 513-521 (cited as 510-518 and 512-520), at md5 5b0ad3f0
(after D628 and a later edit, neither touching those lines); PART-VII-ASSEMBLY.md's paragraph *The metric.* ending "So b
= (m',0) and S = S^(0)_1 = 0" is at 420-423 (cited as 403-406), at md5 500c085b, and its *The group.* paragraph is still
at 31-38 (31-37 and the blank line after it). Notes inserted at the citing lines.

**(m8) Labels, and zinv5.** Accepted. F3 (the product rule), F3' (a power law), F4 and F5 (typed exponents) and G5 (a
typed list) are marked [arithmetic] in r5settle5's output and docstring; what they stood for is now computed in
r6settle5 X-Y and r6sigma5 W. zinv5: the round-5 run, started 07:59, had printed nothing after 2 h 58 min and was
stopped (its processes identified by their command line and start time, killed by PID). Two causes, neither in the
identity. (1) Each jet was substituted into the unsimplified defect with sympy's Expr.subs, which walks and rebuilds the
whole tree at every key; one component took hours. Expr.xreplace replaces each Derivative node and each A(t, r) node
structurally, before its arguments are reached, and then the symbols; the expression and the substituted values are
unchanged, so the defect is the same exact algebraic number, now evaluated in under a second per component. (2) In mode
m3 the mu term was the Python integer 0, which has no .doit(): that process died at once, so ZI2 could never have
passed. With both repaired (and three random draws, not one), the first complete run found that mode m4, the gauge term
contracted with g0^ab in place of g^ab, is not a control: that operator is still built covariantly from (g, g0) and is
still invariant under (g, g0) -> (c g, c g0), which is all (R3c) uses (R3-D: the dilation pulls g0(mu) back to kappa^2
g0(mu/kappa^2)), so the identity holds for it too (defect 1.4e-188, ZI3). Its place is taken by m5, the gauge background
held at a fixed mass 1/2 (Gamma[g0(1/2)] in D and in its covariant derivative), which breaks the mu-scaling and fails
(defect 0.53). Result: ZI1 (mode none, defect 1.4e-188 against terms up to 1.5e3), ZI2 (m1, m2, m3, m5 fail with defects
87, 46, 0.39, 0.53), ZI3; 13 to 25 minutes for the six modes on this machine (load about 25 on four cores). Notes
inserted at the round-5 header and ledger.
[R7 (nit): "died at once" is not exact: the m3 process ran its slow evaluations of the first component's other terms and
died with an AttributeError at its first evaluation of the mu term, before any RESULT line.]

**(r6-F4) F_4's source is not needed** (found in this round, computed). R5-C (v)'s F_4 solves the degree -4 equation
with the degree -6 source, which makes P(Sigma) = O(lam r^(-13/2)) (r6sigma5 S4). If instead F_4 is the regular flat
solution with data G_8(v1) (it exists as the other F_p do: the 2F1 with p = 4), h_R on N is unchanged (on N, s = 0 and
Sigma's coefficients are G_(2p)(v1) whatever F_4's equation; off N, F_4's Taylor terms enter at r^-5 and beyond, so h_R
= O(r^(-9/2)) still, G1), and P(Sigma) = O(lam r^-6) (measured without Sigma_4 in S4, where Sigma_2 + Sigma_(5/2) decays
like r^-6; a flat Sigma_4 adds nothing at degree -6, the flat operator annihilating it, and its mu and quadratic terms
are of degree -8). Every use of the residual then still closes on the window: the residual's kernel is 4 - a > 1 (W3: a
< 3), rho_inf = C lam/(3 - a), Step 8's tail ∫_(-oo)^T rho <= C lam |T|^(a - 3) -> 0, the exterior estimate of R6-A
gives rho^(2a - 8), finite for a < 4 (X4'), and R4.9's d D_T = O(lam r^-4) is unchanged; the window is unchanged (W'').
So R5-C (v) is not a condition of Theorem R5.1; it is kept, computed, as the sharper statement.

**Nits.**
- R5.0 (r4-m5): the last term is -M_Gamma(P(H) - P(Sigma)), not +. Re-derived: 0 = DP(H)[Gamma H] + M_Gamma P(H) and
  DP(H)[Gamma Sigma] = (DP(H) - DP(Sigma))[Gamma Sigma] + (Gamma + c_Gamma) P(Sigma) - M_Gamma P(Sigma), so DP(H)[Gamma
  h_R] = -(Gamma + c_Gamma) P(Sigma) - (DP(H) - DP(Sigma))[Gamma Sigma] - M_Gamma(P(H) - P(Sigma)). The term is bounded
  in absolute value, so nothing changes. Note inserted.
- R5-D's text: the sums lacked "gamma' <= gamma"; gamma' was reused as the family index; f^n, b^n, c^n were not defined;
  ||R_gamma^n|| <= C t^(-3/2) uniformly in n was implicit. All four are repaired in R6-D, and checked (E1d (g)-(j)); the
  uniformity in n is proved there: d_X^gamma F_1(X, 0, 0) does not depend on n, and every other factor of R_gamma^n is
  bounded by the induction hypothesis for u_1^n, which is uniform in n, with (9.8) at the lowest orders.
- R4-B ("puts both in Lemma 9.5's kernel") and R5.4 ("Lemma 9.5's kernel on the far region") against R5-D (s11-6) ("not
  through its kernel"): R5-D's mechanism is the one written: b . d U, c U and the |gamma'| = 1 terms enter (9.3) through
  its source f, and Gronwall's lemma, applied to the inequality summed over the family, turns their coefficient C(1 +
  lam^-1) t^(-3/2) into the exponent; the factor is the same e^(2C(1 + lam)) either way, and "kernel" in R4-B and R5.4
  means that exponent. Notes inserted.
- (s11-6) cited the section-11 reader's `energy_kernel.py`, which is not in checks/. The structure of (9.3) is Lemma
  9.5's proof ("Lemma 2.3's proof on P cap {tau1 <= s <= tau} ... the bulk is at most C k ||d u||^2 + ||f|| ||d u||.
  Gronwall"); the factor's integral and Gronwall's lemma in integral form are computed in r6edits5 E2d-E2e. Note
  inserted.
- "a + 1 >= l0" (R5.0, the window) against Step 9's "a + 1 > l0": the inclusion rho^(a+1) L^2_b in rho^(l0) L^2_b holds
  exactly for a + 1 >= l0 (G4 tests that), and the window is taken open, a + 1 > l0, as Step 9 says (r6sigma5 W5). Note
  inserted.
- R5.4's proof: "m = 1 with a coefficient of degree 2" reads "degree -2" (r-power 2 in A's list). Note inserted.
- The count of bracketed notes in rounds 1-4 is 44: 40 "[R5.0", 2 "[Withdrawn, R5", 2 "[Superseded".
- Run times, measured on this machine under load (about 25 on four cores), are given with the run lines below; the
  round-5 figures were optimistic.

**The reader's surviving mutants, rerun on the code and text as they now stand** (its scripts, applied to scratch copies
of the current files, unchanged except for the path; outputs in this round's scratch, mutout/): F-m1 (Phi = v - 1/r in
F1) and F-m2 (|H| = 6 r^-2 in F1) now fail F1 (the minimum of r^2 lambda_min is -0.7322 and -2.2860 against 0.2678
unmutated). E-m6 (the factor -> e^(2C/lam)) now fails r5edits5 E1f (its E2d). E-m5 (c U's bound lam^-1 -> lam^-3), as
its mutE.py applies it, replaces the first occurrence of its string in the file, and that is R4-B's superseded
replacement text (line 1106 of the round-5 file), not R5-D: the mutant never reached the code under test, in round 5 or
now, and no check of R5-D could have caught it; the same script's E-m4 has the same defect (R4-B's line 1075), which its
mutE2.py avoided by working inside R5-D's section. Applied inside R5-D, E-m5 fails E1f (E2b, E2c) and E-m4 fails E1a;
applied inside R6-D, E-m5, E-m6 and E-m4 fail r6edits5 (E2b-E2c, E2d, E1a), and r6edits5 E3 carries E-m5 and E-m6 among
its own six controls. Every other mutant rerun fails as before: A-m1 and A-m3 (A2), A-m2 (by assertion), D-m1 (D5), F-m3
(F1), E-m1, E-m2, E-m3, E-m7 (E1d, and E1f for E-m2 and E-m7), E-m8 (E1a); A-m4 is still a no-op of the model; G-m1's
anchor (G5's condition line) has changed, and its content is now G5c, a control in the program that fails as it must;
C-m1 (cclass5, unchanged) was not rerun.
[R7 (nit): E-m4's first occurrence is at line 1074 of the round-5 file, not 1075.]

**The claims the reader found exercised by no check**, each now: R5-D's mathematics and the uniformity in n (r6edits5
E2a-E2h, E1d (j), with mutation controls E3); the exterior energy identity and the continuity of 𝔈 (r6settle5 X1-X4);
the a priori decay behind Hardy (Y1-Y2); R5.2's uniformity in sigma (Y3, and the proof in R6-A); F_4's existence and
P(Sigma) = O(lam r^(-13/2)) with Sigma_4 (r6sigma5 S1-S4, on the full operator); the window as a whole (W, from measured
exponents); the "+2 for Lemma 9.3" (r6settle5 L) and part A's coefficient list (A0, computed from g_b0); the flux sign
(F1, F1x); the completeness of the conditional list (R6-E, by hand: every statement outside this file that R4-D, R5-B,
R5-C, R6-A and R6-B cite is listed); ZI1-ZI2 (zinv5, finished, with ZI3).
[R7 (minor 2): from measured and hand-counted exponents; R7.0 (minor 2).]

### R6-A Theorem R4.6 at spatial infinity, written out (R5-B's two paragraphs and Proposition R5.2's proof)

R5-B's localisation and its energy identity on D_*(sigma) stand. Throughout, g_T is the truncated solution on its
interval of existence [T, sigma_1), which here means: g_T exists on W_T cap {t~ <= sigma'} with every derivative bounded
there, for every sigma' < sigma_1. Beyond the band its data are g_b0 + Sigma, smooth with every derivative bounded, so
the record's local theory (Step 8), applied on the balls of a fixed radius beyond the band, gives such a solution on a
time interval that does not depend on the ball (finite speed of propagation); within [T, sigma_1') every coefficient of
the commuted equations (R4d), which are built from Sigma, h_R and their derivatives, is bounded on W_T cap {t~ <=
sigma_1'} for every sigma_1' < sigma_1. Fix such a sigma_1'. R is the radius of R4-D's setting; enlarging it, |f'| <=
1/4 on r >= 4R (f' is in |x|^-2 C^oo).

*(i) The exterior regions.* For rho >= rho_0 (rho_0 so large that {t~ = T, r >= rho_0} lies beyond the band and in {v >
v1}) and V_* > 0 let X_(rho, V_*) := W cap {T <= t~ <= sigma} cap {r - 2(t~ - T) >= rho} cap {Phi_W <= V_*}, sigma <=
sigma_1'. It is bounded (r <= V_* - T + sup|f| on it) and does not meet N. Its boundary consists of the bottom Sigma~_T
cap {r >= rho} cap {Phi_W <= V_*}, the top Sigma~_sigma cap {r >= rho + 2(sigma - T)} cap {Phi_W <= V_*}, the inner
piece {r - 2(t~ - T) = rho} and the outer piece {Phi_W = V_*}. The inner piece is spacelike with the region to its past:
its conormal alpha := d(r - 2 t~) = (1 + 2 f') dr - 2 dt has g_b0^-1(alpha, alpha) = -4 + (1 + 2 f')^2 - mu r^-2 (3 + 2
f')^2 <= -7/4 for |f'| <= 1/4, |alpha|_E^2 <= 25/4, so (g_b0^-1 + delta)(alpha, alpha) < 0 for every |delta|_op <=
r^-2/2 at r >= 2, and alpha(d_t) = -2 < 0, so r - 2 t~ decreases along future causal curves (r6settle5 X2, exact, and
2000 samples; control X2': at f' = 1/2 alpha is null for eta). The outer piece is spacelike with the region to its past
by D4-D5. So X_(rho, V_*) is a domain of dependence of its bottom for every metric of the bootstrap class, and its
solution is the one with data g_b0 + Sigma there.
[R7 (minor 1): "by D4-D5" holds only for |g^-1 - g_b0^-1|_op <= r^-2/2, the bootstrap's margin, which Step 6's openness
cannot assume at sigma*; R7-A cuts with the cone {r + 2(t~ - T) <= V_*} instead, which needs only |g^-1 - g_b0^-1|_op <
7/25 (r7settle5 K1-K4).]
[R9 (nit 8): rho_0 is also taken >= 4R (enlarging it), so that the exterior regions lie in r >= 4R, where |f'| <= 1/4
and m <= 1/16; R8-A uses it.]

*(ii) The unweighted estimate.* For phi := (Gamma^alpha h_R)_ij, |alpha| <= k, the energy identity (R3a) with X := d_t
(w = 1) on X_(rho, V_*) has, besides the top and the bottom, the fluxes of the two lateral pieces, which are
T_g[phi](d_t, n) with n future timelike, >= 0 (r5settle5 F1x), and are dropped. The flat radial model of this identity,
with both lateral fluxes and their quadratic forms (eigenvalues 1/2, 3/2 and (c -+ 1)/2, c = (1 - r^-2)^-1), is computed
exactly in X1. Put e(sigma) := sum_(|alpha| <= k) (energy of Gamma^alpha h_R on the top + ||Gamma^alpha h_R||^2 on the
top); the L^2 part obeys d/dsigma ||phi||^2 <= 2 ||phi|| ||d_t phi||, both lateral edges of the top moving so as to
shrink it. The bulk terms are -int int sqrt|g| (box_g phi) d_t phi and the deformation term, with box_g phi = -2
S^alpha + (terms linear in d phi, phi), S^alpha = -R^alpha + (A) + (B) + (C) (R4d), every coefficient bounded on X_(rho,
V_*) by the choice of sigma_1', and R^alpha = O(lam r^(-13/2)) (r6sigma5 S4). So e(sigma) <= e(T) + C int_T^sigma
(e + ||R^alpha||_(L^2(top)) e^(1/2)), C independent of V_* and of rho >= rho_0, and by Gronwall's lemma e(sigma)^(1/2)
<= e^(C(sigma - T)) (e(T)^(1/2) + int_T^sigma ||R^alpha||). At t~ = T beyond the band h_R and d_t h_R vanish and the
higher time derivatives contained in Gamma^alpha are given by Ric^H(g_T) = 0, where g_T = g_b0 + Sigma: they are O(lam
r^(-13/2)). Hence e(T) <= C lam^2 int_rho^oo r^-13 r^3 dr = C lam^2 rho^-9 and ||R^alpha||_(L^2(r >= rho)) <= C lam
rho^(-9/2), so e(sigma) <= C(sigma_1' - T) lam^2 rho^-9 for every sigma in [T, sigma_1'] and every V_*. As V_* -> oo the
left side increases to the unweighted energy of Sigma~_sigma cap {r >= rho + 2(sigma - T)} (monotone convergence; X3),
which is therefore at most C lam^2 rho^-9.
[R7 (nits): S4 measures that degree for one static l = 0 example; the general statement is R5-C (v)'s deduction with
S1-S2 and the degree count, and (r6-F4) makes it unnecessary. In (iv), continuity holds on every interval on which
|g^-1 - g_b0^-1|_op < 7/25, with R7-A's cut; Step 6's openness at sigma* is R7-A.]
[R9 (m1): round 8's rewrap had moved this note's last words into the paragraph above; they are put back, the break
before "|g^-1" so that no line begins with "- " (word sequence checked against round 7's file, R9.0).]

*(iii) The weighted tail.* On Sigma~_sigma, w <= (2r + C)^(2a). For rho >= max(rho_0, 4(sigma_1' - T)) the shell {2^j
rho <= r <= 2^(j+1) rho} of Sigma~_sigma lies in {r >= rho_j + 2(sigma - T)} with rho_j := 2^(j-1) rho, so its weighted
energy is at most C (2^(j+1) rho)^(2a) lam^2 (2^(j-1) rho)^-9, and summing over j >= 0, the weighted energy of
Sigma~_sigma cap {r >= rho} is at most C lam^2 rho^(2a - 9) for a < 9/2 (X4, the exact sum 2^(2a+9) rho^(2a-9)/(1 -
2^(2a-9)) [arithmetic]), with C independent of sigma in [T, sigma_1'].
[R7 (nit): the shell argument needs rho_j = 2^(j-1) rho >= rho_0 at j = 0, so rho >= max(2 rho_0, 4(sigma_1' - T)).]

*(iv) Finite and continuous.* 𝔈_k(sigma) is the energy of Sigma~_sigma cap {r <= rho}, the integral of a smooth function
over a compact set varying continuously with sigma, hence continuous in sigma, plus the weighted tail beyond rho, at
most C lam^2 rho^(2a - 9) uniformly in sigma. So 𝔈_k is finite and is the uniform limit, as rho -> oo, of continuous
functions on [T, sigma_1']: it is continuous there, for every sigma_1' < sigma_1, as Step 6's continuity argument needs.
(With F_4 the flat solution, (r6-F4), the same holds with rho^-8 and a < 4.)

*(v) The pointwise bounds, first order (S1).* Fix sigma in [T, sigma_1). For F := Omega^gamma d Gamma^beta h_R, |gamma|
<= 2, S1 on [r_sigma, R'] holds with its boundary term R'^(2a+3) F(R')^2 (F3). Its right side involves F and d/dr F
along the ray, and d/dr F is a combination, with coefficients bounded on W, of first derivatives of Gamma Gamma^beta h_R
(Gamma in {d_t, Z, Omega}) and of r^-1 times first derivatives of Gamma^beta h_R (exactly: d/dr (d_c psi) = r^-1 d_c(Z
psi) - r^-1 (t - v1) d_c(d_t psi) + f' d_c(d_t psi) - r^-1 d_c psi, r6settle5 Y1); no undifferentiated term occurs, so 𝔈
bounds it without Hardy. Since 𝔈(sigma) < oo by (iv), int^oo r^(2a+3) (F^2 + (d_r F)^2) dr < oo, and so liminf_(R' ->
oo) R'^(2a+4) F(R')^2 = 0 (were R'^(2a+4) F^2 >= c > 0 beyond some R'_0, int r^(2a+3) F^2 >= c int dr/r = oo). Letting
R' -> oo along that sequence gives S1 on [r_sigma, oo): the first two bounds of (R4b).

*(vi) The a priori decay, and Hardy.* Every Gamma^beta h_R(sigma, .) tends to 0 at spatial infinity along Sigma~_sigma:
at fixed x with r beyond the band, |Gamma^beta h_R(sigma, x)| <= |Gamma^beta h_R(T, x)| + (sigma - T) sup_[T, sigma]
|d_t Gamma^beta h_R(., x)|; the first term is 0 or O(lam r^(-13/2)) (the time derivatives of the data), and the second
is at most (sigma - T) C r^(-3/2-a) by (v), with C = C(sup_[T, sigma] 𝔈) finite by (iv); the time segment {x} x [f(r) +
T, f(r) + sigma] lies in W_T. So phi := Gamma^beta h_R satisfies phi(r) = -int_r^oo d_s phi along the ray, and by
Cauchy-Schwarz r^(2a+2) phi(r)^2 <= (2a + 2)^-1 int_r^oo s^(2a+3) (d_s phi)^2 ds, which tends to 0 as r -> oo (the tail
of a convergent integral; r6settle5 Y2, 24 fields that are not power laws). Hardy's inequality on [r_sigma, R'] has the
outer boundary term R'^(2a+2) phi(R')^2/(2a + 2), which therefore tends to 0 for every R' -> oo, and its inner one has
the good sign: Hardy holds on [r_sigma, oo) as stated in Step 2, and the third bound of (R4b) is phi = -int_r^oo d_s phi
with the first. So (R4b) holds as written. (Without the decay Hardy fails: Y2', phi = c + r^(-a-2).)

**Proposition R5.2's proof (replacing R5-C's).** As R4.8, with (R4b) at weight a_0 uniform in sigma, in four steps. (1)
S1 for F := Omega^gamma d Gamma^beta h', |gamma| + |beta| <= 2, needs only the energies of first derivatives of
Gamma^alpha h', |alpha| <= 3 (Y1, as in (v)), and these are bounded uniformly in sigma by hypothesis; the sequence
argument of (v) applies on each slice. So |d h'| <= C_0 r^(-3/2-a_0) on every Sigma~_sigma, C_0 independent of sigma.
(2) For fixed sigma and xhat, h'(sigma, r xhat) has a limit c(sigma, xhat) as r -> oo along Sigma~_sigma, since |d/dr
h'| <= (1 + |f'|) C_0 r^(-3/2-a_0) is integrable. (3) c does not depend on sigma: for sigma_1 < sigma_2 <= 0 and r large
the time segment from (f(r) + sigma_1, r xhat) to (f(r) + sigma_2, r xhat) lies in W, and |h'(sigma_2, r xhat) -
h'(sigma_1, r xhat)| <= (sigma_2 - sigma_1) C_0 r^(-3/2-a_0) -> 0. (4) c = 0: the inner edge of Sigma~_sigma cap W lies
on N, where h' = g_lam - g_b0 (g' = g_lam on N), which is O(r^-2) there (u_1 in E_2, Theorem P; the radiation field
vanishes on {v > v_end}); so |c(xhat)| <= |g_lam - g_b0|(r_sigma xhat) + 2 C_0 int_(r_sigma)^oo r^(-3/2-a_0) dr <= C
r_sigma^-2 + C r_sigma^(-1/2-a_0), and r_sigma -> oo as sigma -> -oo. Hence h'(sigma, r xhat) = -int_r^oo d/ds h' ds,
|h'| <= C r^(-1/2-a_0) with C independent of sigma, and Hardy holds on [r_sigma, oo) with sigma-independent constants,
its outer boundary term vanishing as in (vi). The kernels q = 3/2 + a_0 and q = min(3, a + 1/2) of B11 are then
integrable with sigma-independent constants; the zero-order coefficient is r |d d H| <= C (mu + lam) r^-3 + C eps_B
r^(-1/2-a). ∎ (A model of (2)-(4), r6settle5 Y3: the limit is the same at three sigma and is 0; controls: a constant
added keeps every derivative bound and |h'| <= 1/50 but violates g' = g_lam on N, and its limit is that constant; a
sigma-dependent limit makes |d_t h'| fail to decay. The hypothesis |h'| <= 1/50 is used for Step 1's margins only.)

### R6-B Lemma R4.5 on (0, 7/2), F_4 on the operator, and the window computed

**Lemma R4.5 (widened).** Lemma R4.5 holds for every a in (0, 7/2), with K > K*(a, 8, M, k1) of Lemma R3.2. *Proof.*
R4.5's proof, read at such a: (i) uses the N-flux of the commuted h_R, O(r^(-9/2)) on N with its ell-gains, at weight a,
finite exactly for a < 7/2 (R2.8, Z5; r6sigma5 W2: the tail exponent is 2a - 7, computed at thirteen a in [1/2, 7/2]),
and the term |H| |d phi|^2 of the N-flux for g, ∫ lam r^(2a - 8) dr, finite exactly for a < 7/2 (W7, sympy's own
convergence condition); (ii) uses Lemma R4.4, which has no a, and Lemma R3.2, stated for a in (0, (J' - 1)/2) = (0, 7/2)
at J' = 8. ∎ (Independently, the fluxes are monotone in a, since u* - u >= 1: r6settle5 M1.)

**F_4 on the full operator** (R5-C (v), computed in r6sigma5). S1: for every F and every harmonic polynomial h_l of
degree l = 0..4, -(1/2) box_eta (r^-4 F(s) h_l r^-l) = r^-6 h_l r^-l L_l[F] with L_l[F] = (s - s^2/2) F'' + (7/2)(1 - s)
F' - (1/2)(8 - l(l + 2)) F, exactly R5-C (v)'s operator (control: 7/2 -> 3 fails). S2: the indicial roots at s = 0 are 0
and -5/2; the recursion (n + 1)(n + 7/2) f_(n+1) = S_n + (n(n - 1)/2 + 7n/2 + kappa_l) f_n has a nonvanishing leading
factor, so the solution analytic at 0 is unique given F(0) = G_(8,l)(v1), and f_(n+1)/f_n -> 1/2: radius 2, covering s
in [0, 3/2] (the sources S_l are polynomials in s, F_2 = 2F1(2 + l, -l; 3/2; s/2) being one). S3: for the l = 0 field
Sigma_2 = (3/10) r^-2 P of r5op5 O2, the degree -6 part Q_6 of P(g_b0 + Sigma_2) is computed exactly, by the
second-order expansion of Ric^H(eta + e m + d sigma; eta + e m) as polynomials in (x, 1/r) restricted to S^3 harmonic by
harmonic; the e, e^2 and d parts vanish (Tangherlini is vacuum; r^-2 is harmonic in R^4), Q_6 has the harmonics l = 0,
1, 2, and it agrees with the full operator's r^6 P(g_b0 + Sigma_2) on a ray to 4.5e-11 (Richardson). S4: with Sigma_4 :=
r^-4 sum_l F_l(s) H_l(xhat), F_0 = 1/4, F_1 = 2/5 and F_2 = -(2/7) s 3F2(1, 1, 7; 2, 9/2; s/2) (the l = 2 piece needs s:
a constant is a homogeneous solution there), the full operator's |P| decays along the ray (s = 1/2, r = 8 .. 2048) like
r^-6 for Sigma_2, r^-8 for Sigma_2 + Sigma_4 and r^(-13/2) for Sigma_2 + Sigma_(5/2) + Sigma_4; controls: the l = 2
piece constant, -Sigma_4, and Sigma_2 + Sigma_(5/2) without Sigma_4 each decay like r^-6. So F_4 exists and P(Sigma) =
O(lam r^(-13/2)) with Sigma_4, on the operator; and, by (r6-F4), neither is needed.

**The window, computed** (r6sigma5 W). Each condition of the bootstrap is an exponent computed from a field or from the
operator, not typed: the cap's exponent measured at thirteen a in [1/2, 7/2] on the exact h_R of G1 is the affine law
2a - 6 (fit residual below 2e-3), so the cap vanishes exactly for a < 3 (W1); the N-flux tail of h_R(v1, .) has exponent
2a - 7 (exact, W2); the residual's kernel from the degree measured in S4 is integrable exactly for a < q_R - 3 = 7/2
(W3; with q_R = 6, a < 3); S1's pointwise exponent a + 3/2 and its integral a + 1/2 give the h_R rows, integrable for
a > 1/2 (W4; the coefficient rows of r5op5 O1 do not depend on a); r = 1/rho gives the class exponent a + 1 on S (W5);
Step 2 needs a >= 3/2, Lemma R4.5 (0, 7/2), Proposition R5.2 a > 1/2 (W6-W8). Their intersection, as sympy intervals, is
(l0 - 1, 3) for l0 = 3.1, 3.3, 3.6, 3.9 (W). Controls: p = 4 dropped from Sigma, with W1-W2 recomputed on that field
(exponents 2a - 5 and 2a - 6), gives (l0 - 1, 5/2) and nothing for l0 >= 7/2; Lemma R4.5 on (5/2, 7/2) gives
(max(l0 - 1, 5/2), 3) (W'); and q_R = 6 leaves the window unchanged (W'').
[R7 (minor 2): not "every condition computed": the cap's and the N-flux tail's exponents are measured and the residual's
degree is measured; the rows', the class's and Step 2's exponents are counted by hand from typed scaling rules
([arithmetic], W4-W8), and in round 6 the class's lower end l0 - 1 was typed in the window and W5's result unused. Since
round 7 the window's lower end is W5's exponent (control W''').]

### R6-D The replacement text for N1STAR-PROOF.md's Lemma 11.0 (final; supersedes R5-D)

Two edits, for N1STAR-PROOF.md as it stands (not edited here; another workstream is editing other sections of it, and
the main session seats these after that). Every citation is by quoted content. The old texts are R5-D's: Edit 1's begins
at Lemma 11.0's "*Proof.* By Lemma 11.1 below, u_1 = u - r^(-3/2) G_3 solves" and ends with its sentence "so the source
is at most C(lam, j) t^(-3/2) in L^2."; Edit 2's begins "Lemma 9.5's identity then gives ||d U_n(tau)|| <= ||d
U_n(tau_n)|| +" and ends "uniformly in n.", just before "The bookkeeping of sup against". `checks/r6edits5.py` E1 reads
the four blocks below as printed here and applies them to a copy of the live file: each old text occurs there exactly
once (md5 fb2fbf06 when written, 7400212b and 223e1749 as the file was edited since, the last at the final run), the
file gains 31 lines, every line stays within 121 characters, nothing outside Lemma 11.0 changes, and the edited lemma
satisfies E1d's ten predicates (r5edits5's six and the reader's four nits) and E2's eight mathematical checks; E3's six
mutations of the text each fail. Edit 1's new text is followed on its last line by the unchanged " The identity is not
run on the region between {v ="; Edit 2's is preceded on its first line by "U_n(tau_n)|| <= C(lam, j) t_n^(-1/2) with
t_n >= t. " and followed by " The bookkeeping of sup against".
[R7 (minor 3): E2 checks R6-D's exponents, bounds and Gronwall factor; the induction's structure (which terms are
unknown, R_gamma's order, Gronwall on the family, Lemma 9.3(b)'s hypothesis, b^n and c^n with b's and c's constants) is
a read proof, which the round-6 reader read and found correct and non-circular; since round 7, E1d's predicates (k)-(o)
check that the text states each of those steps (r6edits5).]
[R8 (the section-9.5/11 reader's mutants): E1d's predicates (r)-(t) read Edit 2 too, E2d reads Edit 2's factor as well,
and E3 carries ten mutations; R6-D's text is unchanged, the rotation case included (R8-F).]

What changed against R5-D: the Leibniz sums carry "gamma' <= gamma"; the family is indexed by delta, so gamma' is not
reused; f_gamma^n, b^n, c^n and R_gamma^n are defined, with the reason that b^n and c^n obey the bounds of b and c
(Lemma 11.1 applies to u_1^n verbatim); ||R_gamma^n|| <= C(lam, j) t^(-3/2) uniformly in n is stated and proved
(d_X^gamma F_1(X, 0, 0) does not depend on n, and every other factor is bounded by the induction hypothesis for u_1^n,
uniform in n, with (9.8) at the lowest orders); the L^2 count behind ||R_gamma|| is written (E_3 on a slice of volume at
most C t^3 gives C t^(-3/2), a product at most C t^(-2)); and Edit 2 closes with the two inequalities it uses, ||d
U_n(tau_n)|| <= C(lam, j) t^(-1/2) and int_(tau_n)^tau t'^(-3/2) dtau' <= 2 t^(-1/2). Why the induction closes at the
top order is R5-D's argument, read by the round-5 reader and unchanged: b . d U and the |gamma'| = 1 terms are linear in
the unknown family with coefficient C t^(-3/2); c U <= C lam^-1 t^(-3/2) ||d U|| by Lemma 9.3(b), since U vanishes on {v
= v_start}; Gronwall's lemma applied to the inequality summed over the family costs exp(int_(lam^-2)^oo C(1 + lam^-1)
t^(-3/2) dt) = e^(2C(1 + lam)) (E2d); and R_gamma contains only orders <= j + 1.

Edit 1, old:

```text
*Proof.* By Lemma 11.1 below, u_1 = u - r^(-3/2) G_3 solves -(1/2) g_lam^{ab} d_a d_b u_1 = F_1 := S(u) - (1/2)
(g_lam^{ab} - g0^{ab}) d_a d_b u_1 + (1/2) box~ (r^(-3/2) G_3), and F_1 is in E_3 with all derivatives (S(u) by Lemma
11.1; the second term is E_(3/2) E_2; the third is in E_(7/2) by Lemma 9.7(c) and P2), where "all derivatives" of a term
containing u_1 means the orders already controlled. Induction on the order: for |gamma| = j + 1, U := d^gamma u_1 solves
-(1/2) g_lam^{ab} d_a d_b U = d^gamma F_1 + sum_{0 < gamma' <= gamma} (d^{gamma'} g_lam^{ab}) d^{gamma - gamma'} d_a d_b
u_1. The terms with |gamma'| = 1 are (d g_lam) d U with d g_lam in E_(3/2), of the kind Lemma 9.5's kernel k absorbs; a
term with |gamma'| >= 2 is a product of a derivative of g_lam of order <= j + 1 with one of u_1 of order <= j + 1, and is
estimated in L^2(Sigma_tau) with the factor of higher order in L^2 (the energies of the lower steps, at most C t^(-1/2))
and the other in sup norm (E_2 by the induction hypothesis, through Lemma 9.3 for the orders it costs, and by Theorem P
for the lowest), so the source is at most C(lam, j) t^(-3/2) in L^2.
```

Edit 1, new:

```text
*Proof.* By Lemma 11.1 below, u_1 = u - r^(-3/2) G_3 solves -(1/2) g_lam^{ab} d_a d_b u_1 = F_1 := S(u) - (1/2)
(g_lam^{ab} - g0^{ab}) d_a d_b u_1 + (1/2) box~ (r^(-3/2) G_3). By (0.2), F_1 = -Ric^H(g_lam) - (1/2) g_lam^{ab} d_a
d_b u_1 with g_lam = g0 + r^(-3/2) G_3 + u_1, so F_1 contains no second derivative of u_1 (`checks/f1lemma5.py` F1a):
it is a smooth function F_1(X, u_1, d u_1), and F_1(X, 0, 0) is in E_3 with all derivatives (the terms of Lemma 11.1
in G_3 and g0, and the third term, in E_(7/2) by Lemma 9.7(c) and P2; `checks/r5edits5.py` E3). Along g_lam its partial
derivatives are b := dF_1/d(d u_1), in E_(3/2) and of lam-order 0 (the derivative of the Q-difference, linear in d g0 +
d u; d u is of lam-order 0: dv [d_th W_TT], plus dv [d_th chi] dv dv in E_2 and the phase shift's term in E_(5/2), plus
O(lam); `checks/cclass5.py` C3, r5edits5.py E2), and c := dF_1/d u_1 = -(1/2) lam^-1 (.)(ell_lam, ell_lam) [d_th^2
W_TT] + E_(3/2), ell_lam := g_lam^-1 dv (the first term from -(1/2)(g_lam^-1 u_1 g_lam^-1)^{ab} d_a d_b (lam [W_TT]), as
in (3.2); the E_(3/2) part contains -(.)(ell_lam, ell_lam) [d_v d_th W_TT], from the envelope's dependence on v; F1b,
cclass5.py C1-C2). Induction on the order: for |gamma| = j + 1, by Leibniz's rule U := d^gamma u_1 solves

    -(1/2) g_lam^{ab} d_a d_b U = f_gamma := b . d U + c U + R_gamma
        + (1/2) sum_{gamma' <= gamma, |gamma'| = 1} C(gamma, gamma') (d^{gamma'} g_lam^{ab})
              d^{gamma - gamma'} d_a d_b u_1,

C(gamma, gamma') := gamma!/(gamma'! (gamma - gamma')!), where R_gamma := d^gamma F_1 - b . d U - c U + (1/2)
sum_{gamma' <= gamma, |gamma'| >= 2} C(gamma, gamma') (d^{gamma'} g_lam^{ab}) d^{gamma - gamma'} d_a d_b u_1 contains
derivatives of u_1 of order <= j + 1 only (the chain rule, F1d). In f_gamma, b . d U is of the order this step
estimates and is not known; the terms with |gamma'| = 1 are (d g_lam) d U' with d g_lam in E_(3/2) and U' in the same
family {d^delta u_1 : |delta| = j + 1}; and c U is one order lower. They enter through f_gamma in Lemma 9.5's energy
inequality (9.3), before Gronwall's lemma, not through its kernel k: ||b . d U|| <= C t^(-3/2) ||d U||, ||c U|| <= C
lam^-1 t^(-3/2) ||U|| <= C lam^-1 t^(-3/2) ||d U|| by Lemma 9.3(b) (U vanishes on {v = v_start}), so ||f_gamma|| <=
C(1 + lam^-1) t^(-3/2) sum_{|delta| = j + 1} ||d d^delta u_1|| + ||R_gamma||; summed over the family, Gronwall's lemma
then costs the factor exp(int C(1 + lam^-1) t^(-3/2)), at most e^(2C(1 + lam)) over the far region t >= lam^-2, a
lam-free factor. (With c U taken as a source, through the energies of the lower steps, the step also closes at fixed
lam, at one lam^-1 per order.) R_gamma is the sum of d_X^gamma F_1(X, 0, 0), the u_1-free source, in E_3, and of
products of a derivative of g_lam or of F_1's coefficients of order <= j + 1 with derivatives of u_1 of order <= j + 1,
each estimated in L^2(Sigma_tau) with the factor of higher order in L^2 (the energies of the lower steps, at most C
t^(-1/2)) and the others in sup norm (E_2 by the induction hypothesis, through Lemma 9.3 for the orders it costs, and by
(9.8) for u_1^n at the lowest): d_X^gamma F_1(X, 0, 0), in E_3, has L^2 norm at most C t^(-3/2) on Sigma_tau, whose
volume is at most C t^3, and each product at most C t^(-2) (a coefficient in E_(3/2), or a second factor of u_1 in
E_2, times the L^2 factor), so
||R_gamma|| <= C(lam, j) t^(-3/2).
```

Edit 2, old:

```text
Lemma 9.5's identity then gives ||d U_n(tau)|| <= ||d U_n(tau_n)|| +
C int_{tau_n}^tau t'^(-3/2) dtau' <= C(lam, j) t^(-1/2) at every order, uniformly in n.
```

Edit 2, new:

```text
Lemma 9.5's energy inequality (9.3) for U_n
with f = f_gamma^n, and Gronwall's lemma, give sum_{|gamma| = j + 1} ||d U_n(tau)|| <= C e^(2C(1 + lam)) sum_{|gamma|
= j + 1} (||d U_n(tau_n)|| + int_{tau_n}^tau ||R_gamma^n|| dtau'), where f_gamma^n, b^n, c^n and R_gamma^n are
f_gamma, b, c and R_gamma with g_n and u_1^n in place of g_lam and u_1 (Lemma 11.1 applies to u_1^n verbatim, so b^n
and c^n obey the bounds on b and c above with the same constants), and ||R_gamma^n|| <= C(lam, j) t^(-3/2) uniformly in
n: d_X^gamma F_1(X, 0, 0) does not depend on n, and every other factor of R_gamma^n is bounded by the induction
hypothesis for u_1^n, which is uniform in n, with (9.8) at the lowest orders. Since ||d U_n(tau_n)|| <= C(lam, j)
t_n^(-1/2) <= C(lam, j) t^(-1/2) and int_{tau_n}^tau t'^(-3/2) dtau' <= 2 t^(-1/2), ||d U_n(tau)|| <= C(lam, j)
t^(-1/2) at every order, uniformly in n.
```

### R6-E Theorem R5.1's status, and the paper's text

Theorem R5.1 stands as stated in R5-E, with Proposition R5.2's proof as in R6-A and Lemma R4.5 as widened in R6-B; R5-C
(v) is no longer among its conditions ((r6-F4)).

*Status (replacing R5-E's).* **Deduced**, in this file (rounds 1-6; rounds 1-5 read by verifiers, every finding seated
in R5.0 and R6.0; round 6 not yet read), and **conditional on**:

- (a) statements the record lists as proved: Part IV's seven outputs (R3-A); III.K Theorem 4.3, with III.C' Theorem 3.1
  under row d1 and III.C'' Theorem 3.1 (2) and Proposition 4.1 through Theorem R2.4, III.C'' Proposition 4.1 also
  rebuilding III.K's gauge data from (gamma, k) (R4-F); Part VII Lemmas 1.1, 1.2 (R4-D's setting: R is free) and 2.1
  (Step 9's computation of (gamma, k)) and Proposition 3.2 (all listed as proved in proof5/README.md); BEYOND5 Lemma 6.4
  (iv) (W, N and their placement in Omega' cup P'); N1STAR-PROOF.md's Theorem E (sections 1-4, proved), whose Step 8
  local theory R4-D Step 6, R5-B and R6-A use; and Theorem P (proved), used at every order through Corollary R4.3, its
  uses of Lemma 1.1 (e) and Lemma 2.3 standing after D623 (R6.0 (m5) (c));
- (b) N1STAR-PROOF.md section 11.1 (Lemmas 11.0, 11.1, 11.2 and Proposition 11.1), which the record lists as deduced,
  with: its D44 repair read by D45 and D47 and found to close the thirteenth verifier's gap; Lemma 11.0's top-order gap
  found by D618's section-11 reader (its Major 1), repaired by R6-D, written and not applied; and Lemma 11.2 as amended
  by D618's repair, which another workstream is seating. Section 11.1 is used by Proposition R5.4, Lemma R3.2, Lemma
  R4.4, Lemma R4.5 (i) and Step 9;
- (c) this file's statements: Lemma R2.1, Proposition R2.2 (computed for every round count III.C' uses, M <= 12, exactly
  below 11/2), Theorem R2.4, Lemmas R3.2-R3.3 (as amended), Propositions R4.1-R4.2, Corollary R4.3, Lemma R4.4, Lemma
  R4.5 (as widened, R6-B), R4-D with R5-B and R6-A (Theorem R5.1′), Propositions R4.9, R5.4 and R5.2 (its proof as in
  R6-A), and Theorem R5.1; rounds 5 and 6 are not yet read by a verifier;
  [R7 (nits, minor 4): round 5 was read (vB5) and round 6 was read (vB6); the list is completed in R7-E: Part VIII Lemma
  1.1, III.A Lemmas 1.2, 1.3 and 3.2, III.C Definition 3.1 and Lemma 3.2 (a), Part VII Lemma 0.1 and Theorem 0.2 among
  the proved statements, BEYOND5 Lemma 6.4 (iv) moved to the deduced ones, and (b)'s Lemma 11.2 clause updated.]
- (d) the programs they cite.

It rests on no statement of Part IX. What has to be read for the label "proved": (b) with R6-D applied; (c), rounds 5
and 6; (d). Not evaluated: lam_2, eps, delta, lam_1 (another workstream), in either class. The list was made by reading
every statement outside this file that R4-D, R5-B, R5-C, R6-A and R6-B cite; nothing else is open in the theorem.

*Computational support, stated as what was computed.* The operator identities ((5.1), (R3a), (R3c) in Cartesian form and
in invariant form (zinv5, finished), (R4c), the contracted Bianchi identity) are computed on the full operator, and the
localised and the exterior energy identities on the flat radial model (F2, X1); the coefficients of DP(H), the degrees
of P(g_b0 + Sigma_p) and the degree after Sigma_4 are measured on the full operator (O1-O2, S4), and Q_6, which F_4
cancels, is computed exactly (S3); the class of c and the lam-order of b on it (C1-C3); h_R's decay, the caps, the
null-hypersurface tails and the class on S on explicit fields (G1-G4, G6, W1-W2); the weight window from those measured
exponents (W); the lam-orders of the expansion from every monomial, with the coefficient list computed from g_b0 and
Lemma 9.3's cost measured (A, A0, L); the flux signs exactly (F1x, X1-X2); R6-D's mathematics read from its text
(r6edits5 E2). The remaining kernel exponents (the bulk-sign error, the deformation, the uniqueness kernels and the
D-system's) are counted by hand, their integrability checked ([arithmetic]).
[R7 (minor 2): the window from the measured exponents and from hand-counted ones (the rows', the class's, Step 2's);
R7-E restates this paragraph.]

*The text for the paper's section 9* (RESPONSE-HL-5D.md, not edited here; it supersedes R5-E's blocks; each old text
occurs exactly once in the current file, md5 7d9fc1be at the final run (7193c56e when written), checked by r6edits5 E4;
the new lines are within 121 characters).
[R7 (minor 2, minor 4, nits): superseded by R7-E's blocks.]

Block 1, in "Settling", old:

```text
  not evaluated. Theorem 4 (i) concerns glued data that agree with g_λ's on a ball; settling of g_λ's own continuation
  is not shown. Evaluating λ1 and δ would need every constant of the write-out made explicit, and several come from
```

Block 1, new:

```text
  not evaluated. Theorem 4 (i) concerns glued data that agree with g_λ's on a ball. That the development of g_λ's own
  data settles, with no gluing, is deduced in a data class wider than (ii)'s by half-integer orders, conditional on
  supplement section 11.1, deduced, whose Lemma 11.0 has a repair written and not yet applied, and on the last two
  rounds of that deduction, not yet read by a verifier (Beyond the boundary, below). Evaluating λ1 and δ would need
  every constant of the write-out made explicit, and several come from
```

Block 2, in "Beyond the boundary", old:

```text
  6.3, deduced). It is not shown that Theorem 4 applies to g_λ's own data: g_λ is given on Ω, which does not contain the
  whole initial slice, and continuing it to spatial infinity asks for a scattering problem from past null infinity and an
  expansion of its solution at spatial infinity. Parts of that are done (deduced, with exact computations, all under
  `docket68/n1star/`): the leading Coulomb part carried to spatial infinity with no logarithm (`checks/coulomb5.py`, and
  under the full operator `checks/coulombL5.py`), the map from data on the initial null hypersurface to the leading
  coefficient at spatial infinity, under the write-out's full operator on Minkowski space, bounded uniformly in the
  harmonic (reduced for every harmonic, `checks/harmonics5.py`; bounded, `checks/uniform5.py`), the remainder's sources,
  supported where v is bounded along the initial null hypersurface, entering one order later at every harmonic computed
  (l ≤ 12) (`checks/sources5.py`, `checks/stripfull5.py`), and the approximant's stage profiles expanded in powers of
  r^(−1/2) at past null infinity, with the closure properties of that expansion shown (deduced, with an exact check,
  `checks/closure5.py`). The scattering estimate itself is not done. Below the inner boundary the theorems are not
```

Block 2, new:

```text
  6.3, deduced). It is deduced, with no gluing, that Theorem 4 applies to g_λ's own data in a data class wider than
  (ii)'s by half-integer orders (supplement `docket68/n1star/SETTLE-GLAM5.md`, rounds 1–6, Theorem R5.1), conditional
  on Part IV, III.K and Part VII, proved; on Theorem P, proved; on supplement section 11.1, deduced, whose Lemma 11.0
  has a repair written in SETTLE-GLAM5.md (R6-D) and not yet applied; and on rounds 5–6 of SETTLE-GLAM5.md, not yet
  read by a verifier. After the shell g_λ − g_b0 has at past null infinity an r^(−5/2) coefficient, O(λ^∞), which for
  a C_c^∞ envelope and every amplitude but at most one is nonzero off a discrete set of λ (deduced, SETTLE-GLAM5.md
  Proposition 3.1; computed for a bump envelope, `docket68/n1star/checks/tail5.py`); it puts an r^(−5/2) term into
  g_λ's data at spatial infinity, outside the integer orders of (ii)'s class. With the orders r^(−2), r^(−5/2),
  r^(−3), … below r^(−ℓ0) admitted in the metric (ℓ0 ∈ (3, 4), ℓ0 ≠ 7/2, and one order more in the second fundamental
  form), Hintz's construction runs with the same index sets for its iterates and finitely many more derivatives lost;
  its threshold ε, and with it λ1 and δ, change and are not evaluated, in either class. g_λ continues to the past
  domain of dependence of the far part of Hintz's initial surface as a vacuum metric in the record's wave-map gauge, by
  one weighted energy estimate at a weight a ∈ (ℓ0 − 1, 3), run on bounded domains of dependence, after its
  self-similar terms through r^(−4) are subtracted; it is the only continuation in that gauge near Tangherlini whose
  commuted energies of weight a0 ∈ (0, ½) stay bounded, its energy vanishing toward past null infinity, and its data
  lie in the widened class with small norm. So for every 0 < λ ≤ λ2, λ2 not evaluated, with no exceptional set, the
  maximal vacuum development of g_λ's own data on Hintz's initial surface settles to five-dimensional Tangherlini of a
  mass m′ with |m′ − μ_end| < ε_m at Theorem 4's rate (deduced, with the conditions above). Computed, all under
  `docket68/n1star/checks/`: the operator identities, on the write-out's full operator; the coefficient decays and the
  residuals' degrees, measured on that operator (`r5op5.py`, `r6sigma5.py`, which also builds the r^(−4) term there);
  the caps and the null-hypersurface tails, measured on explicit fields; the weight window, computed from those
  measured exponents (`r6sigma5.py`); the remaining kernel exponents, counted by hand with their integrability
  checked. Below the inner boundary the theorems are not
```

Block 3 (section 8.1, for consistency with blocks 1-2), old:

```text
replaced by a gluing (section 8.7), and Theorem 4 is not shown to apply to g_λ's own data.
```

Block 3, new:

```text
replaced by a gluing (section 8.7); that Theorem 4 applies to g_λ's own data, with no gluing, in a class wider by
half-integer orders, is deduced, conditionally, in section 9 (Beyond the boundary).
```

Ledger. Computed (new): `r6settle5.py` X, Y, M, L, A0, T (21 checks), `r6sigma5.py` S1-S4, W (20), `r6edits5.py` E1-E4
(23), each with controls that mutate the code or the text under test. Changed and rerun: `r5settle5.py` (45),
`r5edits5.py` (11), `zinv5.py` (3). The other round-5 programs are unchanged and their `.out` files stand (r5op5 7,
cclass5 6, poly5 28, scale5 25, trunc5 23, scatter5 16, boot5 48, order5 22, f1lemma5 12, vac5 8 checks). Every new or
changed `.out` is from a full run and byte-identical on a second run. The reader's surviving mutants, rerun: F-m1 and
F-m2 fail F1; E-m6 fails r5edits5 E1f; E-m5 and E-m4, applied inside R5-D, fail E1f and E1a, and inside R6-D r6edits5
E2b-E2d and E1a (R6.0). Deduced: R6-A (i)-(vi), Proposition R5.2's proof, Lemma R4.5 widened, (r6-F4). READ:
N1STAR-PROOF.md by quoted content (0.3's eps1 sentences and their D623 note; Lemma 1.1 (e); Lemma 2.3; Lemma 9.1 (f)
"the causal claim follows as in Lemma 1.1(e)"; Lemma 9.5 "Lemma 2.3's proof on P cap {tau1 <= s <= tau}"; section 11.1
and Lemma 11.0); N1STAR-LOG.md entries D45, D47, D618-D620, D619/D623/D624; PART-III-K-NONLINEAR.md 471, 513-521 (md5
5b0ad3f0); PART-VII-ASSEMBLY.md 31-38, 420-423 (md5 500c085b); RESPONSE-HL-5D.md (md5 7d9fc1be). None from outside
sources.

Open in the theorem: nothing beyond its status (the readings named above). Not evaluated: lam_2, eps, delta, lam_1.

    python3 checks/r6settle5.py   (4 minutes alone, 27 beside the five others)
    python3 checks/r6sigma5.py    (18 to 29 minutes, beside the others; S4 most of it)
    python3 checks/r6edits5.py    (one to two minutes)
    python3 checks/r5settle5.py   (14 to 25 minutes, beside the others)
    python3 checks/r5edits5.py    (5 to 8 minutes)
    python3 checks/zinv5.py       (six processes in parallel; 13 to 25 minutes)
    python3 checks/r5op5.py       (unchanged; 21 minutes as the round-5 reader measured it)
    python3 checks/cclass5.py     (unchanged; 17 minutes, likewise)
    python3 checks/vac5.py        (unchanged; 45 minutes, likewise)

The times are wall-clock on this machine with the load at about 25 on four cores; round 5's figures (four, seven, nine
and half a minute, and "about half an hour" for vac5) were optimistic.

## Round 7 (2026-11-06)

Status: written; not yet read by a verifier. The round-6 reader (vB6) found no major gap and re-derived the mathematics
wherever it went: m1's identity and fluxes, m2, F_4 on the full operator (with (r6-F4): the window (l0 - 1, 3) stands),
and R6-D's Lemma 11.0, correct and non-circular; all six programs reproduced byte for byte. It found four minors and ten
nits; each is re-derived and seated here (R7.0), with "[R7 (...)]" notes at the lines they correct, the old text kept.
R6-D is seated into N1STAR-PROOF.md by the coordinator as D630, not by this file, and its text is unchanged; only its
label here changes (minor 3). New program: `checks/r7settle5.py` (K1-K4: the cone cut of R7-A). Changed and rerun:
`r6sigma5.py` (the window's lower end is W5's computed exponent, control W'''; W4-W8 marked [arithmetic]),
`r6settle5.py` (X3, M1 and T marked [arithmetic]), `r6edits5.py` (predicates (k)-(o) on R6-D's induction, E2g reading
the text's own product bound, E4 on R7-E's blocks). Each `.out` is from a full run and byte-identical on a second run.
Sections R7.0, R7-A, R7-E.

### R7.0 The round-6 reader's findings, and their dispositions

**(minor 1) The exterior continuity was proved only inside the bootstrap class.** Accepted. Step 6 closes by openness:
at sigma*, where (BA) holds on [T, sigma*], 𝔈_k1 must be continuous on some [T, sigma* + delta'], where the class is not
yet known. R6-A (i) made the outer cut {Phi_W = V_*} a future boundary "by D4-D5", which needs |g^-1 - g_b0^-1|_op <=
r^-2/2, a margin of order r^-2 that only the bootstrap gives; at |delta|_op = 3 r^-2 the flux form is negative somewhere
(r7settle5 K2', the reader's computation reproduced). Repaired in R7-A, as the reader proposed: the outer cut is the
cone {r + 2(t~ - T) <= V_*}, whose conormal beta = d(r + 2 t~) has g_b0^-1(beta, beta) = (2f' - 3)(2f' + 1) - m(1 +
2f')^2 <= -7/4 and beta(d_t) = 2 (K1, exact), so it needs only |g^-1 - g_b0^-1|_op < 7/25, a margin of order 1, sharp at
f' = -1/4 (K1'); the inner cut already needed no more (alpha = d(r - 2 t~), the same bound). The flux forms on both
pieces are positive definite at |delta|_op = 0.27 (K2: least eigenvalue 0.0355 over 4000 points), |H|_op <= 1/25 gives
|delta|_op <= 0.0473 (K3), and the identity with the cone's flux is exact on the flat radial model (K4; control: an
outer piece at speed 1/2 has an indefinite flux form). On [T, sigma*] Step 4's localisation by Phi_W stays as it was,
the class giving its margin there.
[R8 (nits 1, 5): 0.0473 reads <= 0.0474 (the bound 0.0473378 is attained, K3); 7/25 is sharp for the hypotheses |f'| <=
1/4, m >= 0, attained only as m -> 0 (R8.0).]

**(minor 2) The window was not "computed as a whole from measured exponents".** Accepted. Re-derived: of the window's
conditions, the cap's exponent (W1) and the N-flux tail's (W2) are measured on explicit fields and the residual's degree
(W3's input) on the operator (S4); the h_R rows' exponents (W4), the class's (W5), Step 2's, Lemma R4.5's and
Proposition R5.2's (W6-W8) are consequences of scaling rules entered by hand, and so [arithmetic]; and in round 6 the
class's lower end l0 - 1 was typed inside window(), W5's computed exponent unused (the reader's mutation of W5 failed W5
alone). Now the window's lower end is the solution set of W5's exponent > l0, and a control (W''') mutates that exponent
to a + 1/2 and moves the lower end to l0 - 1/2; W4-W8 are labelled [arithmetic], and X3, M1 and T in r6settle5 likewise.
The statement, in R6-B, R6.0, R6-E and the paper's Block 2 (notes inserted; R7-E): the cap and tail exponents and the
residual's degree are measured; the window is computed from them and from the class's, Step 2's and the rows' exponents,
counted by hand.
[R8 (nit 6): the hand-counted exponents include Lemma R4.5's and Proposition R5.2's thresholds, which do not bind
(R8-E's Block 2).]

**(minor 3) r6edits5 E2 checks R6-D's exponents and Gronwall factor, not the induction's structure.** Accepted. The
structure (b . d U unknown and of the step's order; R_gamma of order <= j + 1 only, so the induction is not circular;
Gronwall's lemma on the inequality summed over the family; Lemma 9.3(b)'s hypothesis that U vanishes on {v = v_start};
b^n and c^n with b's and c's constants) is a read proof, which the round-6 reader read and found correct; it is labelled
so (note at R6-D). Five predicates now check that the text states each step ((k)-(o), E1d), and E2g reads the text's own
"each product at most C t^(-2)" and compares it with the computed power; the reader's six text mutants that passed
(R_gamma of order j + 2; Lemma 9.3(b)'s hypothesis dropped; Gronwall per gamma; b . d U called known; "with the same
constants" dropped; the product bound t^-1) now fail (mutants, below). These remain checks of the text, not computations
of the induction.

**(minor 4) R6-E's conditional list was incomplete.** Accepted; R7-E's list replaces it. Added to the statements the
record lists as proved (proof5/README.md): Part VIII Lemma 1.1 (D336), used in Theorem R2.4; III.A Lemmas 1.2, 1.3 and
3.2 (D231) and III.C Definition 3.1 and Lemma 3.2 (a) (D245), used in Lemma R2.1, Proposition R2.2 and Theorem R2.4;
Part VII Lemma 0.1 and Theorem 0.2 (D324), used in Theorem R2.4. BEYOND5 Lemma 6.4 (iv) moves to the deduced conditions
(deduced at D400, read by verifier 180 at D405), and the paper's Block 2 names it. Section 11.1's clause is updated:
D618's amendment of Lemma 11.2 is already in the file, R6-D is seated as D630, and sections 9.5 and 11 await a
confirming read that starts after D630.
[R8 (m1, nit 7): "used in Lemma R2.1, Proposition R2.2 and Theorem R2.4" is made exact in R8.0 (nit 7) and R8-E (a);
BEYOND5 Lemma 6.4 (iv) is also in Block 1 and in what must be read for "proved" (R8.0 (m1)).]

**Nits.**
- "Rounds 5 and 6 not yet read": round 5 was read (vB5), round 6 is read (vB6); round 7 is not. Note inserted; R7-E.
- R6-A (iii): with rho_j = 2^(j-1) rho the shells need rho_0 <= rho/2, so rho >= max(2 rho_0, 4(sigma_1' - T)). Note
  inserted.
- R6-A (ii) cites S4 for R^alpha = O(lam r^(-13/2)); S4 measures one static l = 0 example, and the general statement is
  R5-C (v)'s deduction with S1-S2 and the degree count (and, by (r6-F4), unnecessary). Note inserted; the paper's Block
  2 says "for one example, the general case being deduced".
- zinv5's narrative, "died at once": the m3 process ran its slow evaluations of the first component's other terms and
  died at its first evaluation of the mu term, with an AttributeError, before any RESULT line. Note inserted.
- R6.0 (m5) (c): on Omega, Theorem P's (P-iv) rests on Theorem E, which uses eps1 of 0.3 as D623 amended it; that use is
  inside Theorem E, proved. Note inserted.
- Step 2's "(a > 3/2)" against W6's a >= 3/2: a >= 3/2 suffices (C_S eps r^(-1/2-a) <= r^-2/4 for eps small), and the
  window lies above 2. Note inserted.
- E-m4's first occurrence is at line 1074 of the round-5 file. Note inserted.
- R6.0 (m3): "∫ r^(2a) r^-9 r^3 dr" reads r^-11 (|d h_R|^2 for h_R = O(r^(-9/2))); finite exactly for a < 7/2, as
  stated. Note inserted.
- The prose md5 pins of PART-III-K-NONLINEAR.md are updated to 5b0ad3f0 (the pinned lines 471 and 513-521 read as cited,
  checked); PART-VII-ASSEMBLY.md is still 500c085b.
- The paper's R6-E texts are superseded by R7-E's, which name BEYOND5 Lemma 6.4 (iv) and the window's two kinds of
  exponent.

**The reader's mutants, rerun** (its scripts on scratch copies; outputs in this round's scratch, mutout7/): its mutation
of W5's weight (r^(2a+1) -> r^(2a+3)) now fails W, W' and W''' as well as W5, since the window uses W5's exponent; its
Step 2 threshold 2 -> 3 fails W6-W8, W and W'; its typed-bound mutation no longer applies, the bound no longer being
typed. Its six text mutants of R6-D that passed now fail: R_gamma's orders j + 2, Lemma 9.3(b)'s hypothesis dropped,
Gronwall per gamma, b . d U called known and "with the same constants" dropped fail E1d ((k)-(o)), and the product bound
t^-1 fails E2g. The flux check K2' reproduces its computation that R6-A's cut fails at |delta|_op = 3 r^-2.

### R7-A Step 6's openness: the exterior regions cut by a cone (replacing R6-A (i)'s outer cut; completing (iv))

For rho >= rho_0 and V_* > 0 let X'_(rho, V_*) := W cap {T <= t~ <= sigma} cap {r - 2(t~ - T) >= rho} cap {r + 2(t~ - T)
<= V_*}. It is bounded (r <= V_* on it) and does not meet N. Its lateral pieces are {r - 2(t~ - T) = rho}, with conormal
alpha := d(r - 2 t~) = (1 + 2f') dr - 2 dt, and {r + 2(t~ - T) = V_*}, with conormal beta := d(r + 2 t~) = (1 - 2f')
dr + 2 dt. With m := mu r^-2 >= 0, g_b0^-1(alpha, alpha) = (2f' - 1)(2f' + 3) - m(3 + 2f')^2 and g_b0^-1(beta, beta) =
(2f' - 3)(2f' + 1) - m(1 + 2f')^2, both at most -7/4 for |f'| <= 1/4; |alpha|_E^2, |beta|_E^2 <= 25/4; alpha(d_t) = -2
and beta(d_t) = 2 (r7settle5 K1, exact). So for every metric g with |g^-1 - g_b0^-1|_op < 7/25 both pieces are
spacelike, r - 2 t~ decreases and r + 2 t~ increases along future causal curves, and X'_(rho, V_*) lies to the past of
both: it is a domain of dependence of its bottom, and the fluxes T_g[phi](d_t, n) through its lateral pieces, n = g^-1
alpha and n = -g^-1 beta future timelike, are >= 0 (r5settle5 F1x; K2: least eigenvalue 0.0355 at |delta|_op = 0.27;
control K2': at 0.30 beta can be spacelike, and 7/25 is sharp, K1'). R6-A (ii)-(iv) then hold verbatim with X'_(rho,
V_*) in place of X_(rho, V_*) (the exhaustion V_* -> oo is the same, by monotone convergence), on every interval [T,
sigma'] with sigma' < sigma_1 on which |g^-1 - g_b0^-1|_op < 7/25 on W_T cap {t~ <= sigma'}: 𝔈_k is finite and
continuous there, whether or not (BA) holds. (The flat radial model of the identity with the cone's flux, exact: K4.)
[R8 (nits 3, 5): the claim holds under "sup |g^-1 - g_b0^-1|_op <= c < 7/25", with d_t future timelike and the slices
spacelike exactly (|g - g_b0|_op <= 0.4520, g(d_t, d_t) < -0.485, g^-1(dt~, dt~) <= -0.64; r7settle5 K5), the margins
uniform in c; "sharp" as in the note above (R8-A).]

*Openness at sigma*.* Let (BA) hold on [T, sigma*], sigma* < sigma_1. Step 2 gives |H| <= 1/50 on W_T cap {t~ <=
sigma*}, hence |g^-1 - g_b0^-1|_op <= s^2 |H|/(1 - s |H|) <= 0.0232 there, s := |g_b0^-1|_op <= 1/16 + (1 + 1/256)^(1/2)
(K3, exact). By the definition of the interval of existence (R6-A), d_t H is bounded on W_T cap {t~ <= sigma_1'} for any
sigma_1' in (sigma*, sigma_1), so |H(t~, x)| <= |H(sigma*, x)| + (t~ - sigma*) sup |d_t H| <= 1/25 for t~ in [sigma*,
sigma* + delta'], delta' > 0 small, uniformly in x; there |g^-1 - g_b0^-1|_op <= 0.0473 < 7/25 (K3) and g(d_t, d_t) <=
-1 + m + |H| < 0. So 𝔈_k1 is finite and continuous on [T, sigma* + delta'] by the above, and Step 6's improvement
𝔈_k1(sigma*) <= eps^2 < 4 eps^2 extends (BA) to [T, sigma* + delta''] for some delta'' > 0: the set where (BA) holds is
open in [T, sigma_1), as well as closed, and Step 6 closes as stated. On [T, sigma*] Step 4's energy identity on
D_*(sigma) keeps its cut {Phi_W <= V_*}, the class giving the margin r^-2/2 there (Step 2).
[R8 (nits 1, 2, 4): 0.0473 reads <= 0.0474; the segments from sigma* are taken only on the exterior regions, where they
stay in W_T and where alone R6-A (ii)-(iv) need the margin, the compact part needing none; and Step 2's bound is |H| <=
r^-2/4, which gives the margin r^-2/2 of D4-D5 for Step 4's cut (r7settle5 K6). R8-A.]

### R7-E Theorem R5.1's status (final), and the paper's text (final)

Theorem R5.1 stands as stated in R5-E, with Proposition R5.2's proof as in R6-A, Lemma R4.5 as widened in R6-B, Step 6's
openness as in R7-A, and R5-C (v) not among its conditions ((r6-F4)).

*Status (replacing R6-E's).* **Deduced**, in this file (rounds 1-7; rounds 1-6 read by verifiers, round 5 by vB5 and
round 6 by vB6, every finding seated in R5.0, R6.0 and R7.0; round 7 not yet read), and **conditional on**:

- (a) statements the record lists as proved (proof5/README.md): Part IV's seven outputs (R3-A); III.A Lemmas 1.2, 1.3
  and 3.2 (D231) and III.C Definition 3.1 and Lemma 3.2 (a) (D245), in Lemma R2.1, Proposition R2.2 and Theorem R2.4;
  III.C' Theorem 3.1 under row d1, III.C'' Theorem 3.1 (2) and Proposition 4.1, through Theorem R2.4, Proposition 4.1
  also rebuilding III.K's gauge data from (gamma, k) (R4-F); III.K Theorem 4.3; Part VII Lemmas 0.1, 1.1, 1.2 (R4-D's
  setting: R is free) and 2.1 (Step 9's computation of (gamma, k)), Theorem 0.2 and Proposition 3.2 (D324); Part VIII
  Lemma 1.1 (D336), in Theorem R2.4; N1STAR-PROOF.md's Theorem E (sections 1-4), whose Step 8 local theory R4-D Step 6,
  R5-B, R6-A and R7-A use; and Theorem P (D35), used at every order through Corollary R4.3, its uses of Lemma 1.1 (e)
  and Lemma 2.3 standing after D623 (R6.0 (m5) (c));
- (b) statements outside this file that the record lists as deduced: N1STAR-PROOF.md section 11.1 (Lemmas 11.0, 11.1,
  11.2 and Proposition 11.1), its D44 repair read by D45 and D47, Lemma 11.0's top-order repair (R6-D) read by the
  round-6 reader and seated as D630, D618's amendment of Lemma 11.2 already in the file, and D618's edits to sections
  9.5 and 11 awaiting a confirming read that starts after D630 (section 11.1 is used by Proposition R5.4, Lemma R3.2,
  Lemma R4.4, Lemma R4.5 (i) and Step 9); and BEYOND5 Lemma 6.4 (iv) (W, N and their placement in Omega' cup P'),
  deduced at D400 and read by verifier 180 at D405;
- (c) this file's statements: Lemma R2.1, Proposition R2.2 (computed for every round count III.C' uses, M <= 12, exactly
  below 11/2), Theorem R2.4, Lemmas R3.2-R3.3 (as amended), Propositions R4.1-R4.2, Corollary R4.3, Lemma R4.4, Lemma
  R4.5 (as widened, R6-B), R4-D with R5-B, R6-A and R7-A (Theorem R5.1′), Propositions R4.9, R5.4 and R5.2 (its proof as
  in R6-A), and Theorem R5.1; rounds 1-6 read, round 7 not yet;
- (d) the programs they cite.

It rests on no statement of Part IX. What has to be read for the label "proved": section 11.1 after D630 (the confirming
read of sections 9.5 and 11); round 7 of this file; the programs. Not evaluated: lam_2, eps, delta, lam_1 (another
workstream), in either class. The list was made by reading every statement outside this file that rounds 2-7 cite on the
theorem's chain (R2.1-R2.4, R3-A, R4-D, R4-F, R5-B, R5-C, R6-A, R6-B, R7-A) and the reader's list (minor 4); nothing
else is open in the theorem.
[R8 (m1, nit 7): BEYOND5 Lemma 6.4 (iv) is added to what must be read for "proved", with the reason; (a)'s "in Lemma
R2.1, Proposition R2.2 and Theorem R2.4" is made exact (R8-E).]

*Computational support, stated as what was computed.* The operator identities ((5.1), (R3a), (R3c) in Cartesian form and
in invariant form (zinv5), (R4c), the contracted Bianchi identity) are computed on the full operator; the localised and
exterior energy identities on the flat radial model (F2, X1, K4), with the flux forms' signs exact (F1x, X1-X2, K1) and
sampled on the perturbed metrics (F1, K2); the coefficients of DP(H) and the degrees of P(g_b0 + Sigma_p) are measured
on the full operator (O1-O2), and so is the degree after Sigma_4 for one static l = 0 example, whose degree -6 part Q_6
is computed exactly (S3-S4; the general case is R5-C (v)'s deduction, and unnecessary by (r6-F4)); the class of c and
the lam-order of b on it (C1-C3); h_R's decay, the caps, the null-hypersurface tails and the class on S on explicit
fields (G1-G4, G6, W1-W2); the weight window computed from the measured cap and tail exponents and residual degree and
from the rows', the class's and Step 2's exponents, counted by hand ([arithmetic], W4-W8); the lam-orders of the
expansion from every monomial, with the coefficient list computed from g_b0 and Lemma 9.3's cost measured (A, A0, L);
R6-D's exponents, bounds and Gronwall factor read from its text and checked (r6edits5 E2), its induction's structure a
read proof whose stated steps are checked as text (E1d (k)-(o)). The remaining kernel exponents (the bulk-sign error,
the deformation, the uniqueness kernels and the D-system's) are counted by hand, their integrability checked
([arithmetic]).

*The text for the paper* (RESPONSE-HL-5D.md, not edited here; final, superseding R5-E's and R6-E's blocks). Each old
text is located by content and occurs exactly once in the current file (md5 5930486d at the final run), every line of
the edited file is within 121 characters, and the new texts state what the round-5 and round-6 readers asked (r6edits5
E4).
[R8 (m1, nit 6): superseded by R8-E's blocks.]

Block 1, in "Settling", old:

```text
  not evaluated. Theorem 4 (i) concerns glued data that agree with g_λ's on a ball; settling of g_λ's own continuation
  is not shown. Evaluating λ1 and δ would need every constant of the write-out made explicit, and several come from
```

Block 1, new:

```text
  not evaluated. Theorem 4 (i) concerns glued data that agree with g_λ's on a ball. That the development of g_λ's own
  data settles, with no gluing, is deduced in a data class wider than (ii)'s by half-integer orders, conditional on
  supplement section 11.1, deduced, whose Lemma 11.0 repair is seated and, with D618's edits to sections 9.5 and 11,
  awaits a confirming read, and on the last round of that deduction, not yet read by a verifier (Beyond the
  boundary, below). Evaluating λ1 and δ would need every constant of the write-out made explicit, and several come from
```

Block 2, in "Beyond the boundary", old:

```text
  6.3, deduced). It is not shown that Theorem 4 applies to g_λ's own data: g_λ is given on Ω, which does not contain the
  whole initial slice, and continuing it to spatial infinity asks for a scattering problem from past null infinity and an
  expansion of its solution at spatial infinity. Parts of that are done (deduced, with exact computations, all under
  `docket68/n1star/`): the leading Coulomb part carried to spatial infinity with no logarithm (`checks/coulomb5.py`, and
  under the full operator `checks/coulombL5.py`), the map from data on the initial null hypersurface to the leading
  coefficient at spatial infinity, under the write-out's full operator on Minkowski space, bounded uniformly in the
  harmonic (reduced for every harmonic, `checks/harmonics5.py`; bounded, `checks/uniform5.py`), the remainder's sources,
  supported where v is bounded along the initial null hypersurface, entering one order later at every harmonic computed
  (l ≤ 12) (`checks/sources5.py`, `checks/stripfull5.py`), and the approximant's stage profiles expanded in powers of
  r^(−1/2) at past null infinity, with the closure properties of that expansion shown (deduced, with an exact check,
  `checks/closure5.py`). The scattering estimate itself is not done. Below the inner boundary the theorems are not
```

Block 2, new:

```text
  6.3, deduced). It is deduced, with no gluing, that Theorem 4 applies to g_λ's own data in a data class wider than
  (ii)'s by half-integer orders (supplement `docket68/n1star/SETTLE-GLAM5.md`, rounds 1–7, Theorem R5.1), conditional
  on the write-out's Parts III, IV, VII and VIII, proved; on Theorem P, proved; on supplement section 11.1, deduced,
  whose Lemma 11.0 repair (SETTLE-GLAM5.md R6-D) is seated and, with D618's edits to sections 9.5 and 11, awaits a
  confirming read; on BEYOND5 Lemma 6.4 (iv), deduced and read by a verifier; and on round 7 of SETTLE-GLAM5.md, not
  yet read by a verifier. After the shell g_λ − g_b0 has at past null infinity an r^(−5/2) coefficient, O(λ^∞), which
  for a C_c^∞ envelope and every amplitude but at most one is nonzero off a discrete set of λ (deduced, SETTLE-GLAM5.md
  Proposition 3.1; computed for a bump envelope, `docket68/n1star/checks/tail5.py`); it puts an r^(−5/2) term into
  g_λ's data at spatial infinity, outside the integer orders of (ii)'s class. With the orders r^(−2), r^(−5/2),
  r^(−3), … below r^(−ℓ0) admitted in the metric (ℓ0 ∈ (3, 4), ℓ0 ≠ 7/2, and one order more in the second fundamental
  form), Hintz's construction runs with the same index sets for its iterates and finitely many more derivatives lost;
  its threshold ε, and with it λ1 and δ, change and are not evaluated, in either class. g_λ continues to the past
  domain of dependence of the far part of Hintz's initial surface as a vacuum metric in the record's wave-map gauge, by
  one weighted energy estimate at a weight a ∈ (ℓ0 − 1, 3), run on bounded domains of dependence, after its
  self-similar terms through r^(−4) are subtracted; it is the only continuation in that gauge near Tangherlini whose
  commuted energies of weight a0 ∈ (0, ½) stay bounded, its energy vanishing toward past null infinity, and its data
  lie in the widened class with small norm. So for every 0 < λ ≤ λ2, λ2 not evaluated, with no exceptional set, the
  maximal vacuum development of g_λ's own data on Hintz's initial surface settles to five-dimensional Tangherlini of a
  mass m′ with |m′ − μ_end| < ε_m at Theorem 4's rate (deduced, with the conditions above). Computed, all under
  `docket68/n1star/checks/`: the operator identities, on the write-out's full operator; the coefficient decays and the
  residuals' degrees, measured on that operator (`r5op5.py`, and `r6sigma5.py`, which also builds the r^(−4) term
  there for one example, the general case being deduced); the caps and the null-hypersurface tails, measured on
  explicit fields; the weight window, computed from those measured exponents and from the exponents of the data class
  and of the pointwise bound, which are counted by hand; the remaining kernel exponents, counted by hand with their
  integrability checked. Below the inner boundary the theorems are not
```

Block 3 (section 8.1, for consistency with blocks 1-2), old:

```text
replaced by a gluing (section 8.7), and Theorem 4 is not shown to apply to g_λ's own data.
```

Block 3, new:

```text
replaced by a gluing (section 8.7); that Theorem 4 applies to g_λ's own data, with no gluing, in a class wider by
half-integer orders, is deduced, conditionally, in section 9 (Beyond the boundary).
```

Ledger (round 7). Computed (new): `r7settle5.py` K1-K4 (8 checks), with controls that mutate the code under test.
Changed and rerun: `r6sigma5.py` (21), `r6settle5.py` (21), `r6edits5.py` (24, E1s among them (the coordinator's: R6-D
is seated, and E1-E3 run on the live file with R6-D undone in memory)). Every new or changed `.out` is from a full run
and byte-identical on a second run; the other programs are unchanged and their `.out` files stand (r5settle5 45,
r5edits5 11, zinv5 3, r5op5 7, cclass5 6, poly5 28, scale5 25, trunc5 23, scatter5 16, boot5 48, order5 22, f1lemma5 12,
vac5 8 checks). Deduced: R7-A. READ: proof5/README.md's rows for III.A, III.C, VII and VIII and its Part VIII sentence
(D231, D245, D324, D336); N1STAR-LOG.md D400, D405; BEYOND5.md Lemma 6.4; PART-III-K-NONLINEAR.md 471, 513-521 (md5
5b0ad3f0); RESPONSE-HL-5D.md (md5 5930486d). None from outside sources.

Open in the theorem: nothing beyond its status (the readings named above). Not evaluated: lam_2, eps, delta, lam_1.

    python3 checks/r7settle5.py   (8 to 30 seconds)
    python3 checks/r6sigma5.py    (about eight minutes, beside the others; S4 most of it)
    python3 checks/r6settle5.py   (about six minutes)
    python3 checks/r6edits5.py    (8 to 35 seconds)

The times are wall-clock on this machine under the load of the other workstreams (about 25 on four cores).

## Round 8 (2026-11-06)

Status: written; not yet read by a verifier. The round-7 reader (vB7) confirmed round 7 with no major finding: R7-A
re-derived by hand, sound and not circular; R6-D's induction read line by line and correct, its "read proof" label
justified; the four programs byte-identical. It found one minor and ten nits; each is re-derived and seated here (R8.0),
with "[R8 (...)]" notes at the lines they correct, the old text kept. The only edits to earlier rounds' lines are of
form, recorded in R8.0 (nit 8): two round-7 notes that had been inserted inside their paragraphs are moved to the
paragraphs' ends, and five paragraphs are rewrapped so that no line begins with "- " (the words of the file are
unchanged, checked). Changed and rerun: `r7settle5.py` (K2's worst directions, K3's extremal H, K4's flux form derived,
K5 and K6 new), `r6edits5.py` (E2a with the text's own C(gamma, gamma'), E2g reading the slice's volume, predicates
(p)-(q), E4 on R8-E's blocks with the status words), and `r6sigma5.py` (its stated run time only). Each `.out` is from a
full run and byte-identical on a second run. Sections R8.0, R8-A, R8-E.

### R8.0 The round-7 reader's findings, and their dispositions

**(m1) BEYOND5 Lemma 6.4 (iv) was handled inconsistently.** Accepted. R7-E's list (b) and the paper's Block 2 named it
as a deduced condition; Block 1 did not, and R7-E's list of what must be read for "proved" omitted it. Block 1 of R8-E
now reads "on BEYOND5 Lemma 6.4 (iv), deduced and read by a verifier," (E4c checks it). R8-E's list of what must be read
now includes it, and says why it is there: BEYOND5.md labels the lemma "deduced, D400"; verifier 180 read the entries
containing it (D405), and its one serious finding concerned the loss's gap condition, not Lemma 6.4; whether that read
promotes the lemma to "proved" is the record's own decision, recorded in BEYOND5.md, and until it is made the lemma
stays among the deduced conditions.

**Nits.**
- (1) The bound of K3 at |H| = 1/25 is 0.0473378, attained (H along g_b0's eigenvector of least |eigenvalue|, K3 now
  checks it), so "0.0473" reads "<= 0.0474" at R7.0 (minor 1), R7-A and r7settle5's docstring and K3 (the check itself
  tested < 0.0474). Notes inserted.
- (2) The openness step at sigma* took the time segment from (sigma*, x) for every point of W_T with t~ in (sigma*,
  sigma* + delta']; near N such a segment can leave W_T. Re-derived in R8-A: the margin is needed only on the exterior
  regions X'_(rho, V_*), rho >= rho_0, which is all R6-A (ii)-(iv) use (the part r <= rho of a slice needs only the
  smoothness of g_T), and there the segment stays in W_T. Note inserted.
- (3) R7-A's general claim used facts only sampled (d_t future timelike, the slices spacelike). Now exact (r7settle5
  K5): for sup |g^-1 - g_b0^-1|_op <= c < 7/25, |g - g_b0|_op <= s^2 c/(1 - s c) <= 0.4520, so g(d_t, d_t) <=
  -1 + 1/16 + 0.4520 < -0.485, and g^-1(dt~, dt~) <= -15/16 + c (17/16) <= -0.64; the "sup ... <= c < 7/25" gives R6-A
  (ii)'s Gronwall constants their uniform margin. R8-A; note inserted.
- (4) Step 4's margin: Step 2 bounds |H| <= r^-2/2, but D4-D5 (B2d) assume |g^-1 - g_b0^-1|_op <= r^-2/2, and |H| <=
  r^-2/2 gives only 0.571 r^-2 (r7settle5 K6'). Step 2's bound is taken as |H| <= r^-2/4 (it holds for lam <= lam_2,
  eps_B <= eps_2 small, as Step 2's other bounds do), which gives |g^-1 - g_b0^-1|_op <= 0.2845 r^-2 < r^-2/2 (K6, at
  r >= 8, m <= 1/16). R8-A; notes inserted at Step 2 and R7-A.
- (5) "Sharp": 7/25 is sharp for the hypotheses |f'| <= 1/4, m >= 0, attained only as m -> 0 (the conormal's exact
  threshold is (3 + 4f' - 4f'^2)/(5 - 4f' + 4f'^2) at m = 0, least at f' = -1/4; 3/5 at f' = 0). Notes inserted;
  r7settle5's K1' and docstring say so.
- (6) The window's hand-counted exponents include Lemma R4.5's and Proposition R5.2's thresholds (neither binds). R8-E's
  Block 2: "from exponents counted by hand (those of the data class, of the pointwise bound, and of two further
  thresholds, which do not bind)". Note inserted.
- (7) "Used in Lemma R2.1, Proposition R2.2 and Theorem R2.4" was imprecise. Exactly: Lemma R2.1 cites none of them;
  III.C Definition 3.1 and Lemma 3.2 (a), and III.A Lemma 3.2 (the extended union), are cited in Proposition R2.2 (its
  READ of III.C' Step 2 and its M = 0 proof); III.A Lemmas 1.2 and 3.2 and III.C Definition 3.1 in Lemma R2.3 (iii),
  which is not on the theorem's chain (they stay in the list, conservatively); III.A Lemma 1.3 through LOSS-D's READ in
  R2.4's count of what the half class changes, (b), and in the route of round 2's section R2.3; Part VII Lemma 0.1 in
  that count, (a), and Theorem 0.2 in Theorem R2.4; Part VIII Lemma 1.1 in R2.4's amended list of statements generic in
  E_0. R8-E (a); notes inserted.
- (8) Markdown: lines that began with "- " inside paragraphs rendered as list items (round 6's opening paragraph, two
  round-6 paragraphs, R7-A, a round-7 note), and two round-7 notes had been inserted inside their paragraphs (the
  inserting script took such a line for a list item). The notes are moved to their paragraphs' ends and the paragraphs
  rewrapped, binding "a - b" so that no line begins with "- "; the file's words are unchanged (their multiset compared
  before and after). A scan of the whole file for every line that would open a block inside a paragraph or a list item
  (a line beginning, after its indent, with "- ", "+ ", "* ", ">" or "1)"/"N.") found seven more, from rounds 2 to 8:
  "14) for" (round 2), "1) = 27 + 2k_0" (round 3, Theorem R3.7), "- h_R,T(T)" (round 4, Step 8), "- (DP(H)" (round 5,
  (r4-m5)), "> l0" (a round-6 note in round 5), "> 1/2" (round 6, the window) and ">= 8" (round 8, nit (4)); at each the
  break is moved by one or two words, the words unchanged, and the scan now finds only intended list items.
- (9) Run times: the docstrings now say what was measured (r7settle5 5 to 30 seconds, r6edits5 5 to 35 seconds, r6sigma5
  3 to 29 minutes with the load); the run lines below give this round's.
- (10) The program gaps the reader's surviving mutants showed, each closed: K2 now also takes delta along beta beta^T at
  f' = -1/4 and along alpha alpha^T at f' = 1/4, m = 0, at the size actually drawn, where the conormals' thresholds
  attain 7/25 (kills M5: at 0.29 beta is spacelike there); K3 takes the extremal H, which attains the bound (kills M12:
  one factor s dropped gives 0.0445 < 0.0473); K4 derives the outer flux form from the identity's boundary term,
  -rout'(t) e - phi_t phi_r, and checks the typed form against it (kills M17); E2a evaluates the text's own definition
  of C(gamma, gamma') (kills "gamma!/gamma'!"); E2g reads "whose volume is at most C t^3" and compares it with the
  computed power (kills "t^4"); E1d's predicates (p) "and c U is one order lower." and (q) "(Lemma 11.1 applies to u_1^n
  verbatim" (kill "c U of the top order" and "Lemma 11.2 applies"); E4c checks the status words on all three blocks:
  "conditional on", "It is deduced", "on Theorem P, proved", Block 3's "is deduced, conditionally", and no "independent
  of", "unconditionally", "It is proved" or "is proved in section 9" (kills the four status mutants).

**The reader's mutants, rerun** (its scripts on scratch copies; the paper-block mutants applied to R8-E's blocks, which
E4 now reads; outputs in this round's scratch, mutout8/): of its 21 r7settle5 mutants 20 are killed (M1-M19 and M21; M5
by K2's extremal directions, M12 by K3's attained bound, M17 by K4's derived form, the three that survived round 7), and
M20, its own control of the worst direction at 0.27, below 7/25, passes, as it should (mutout8/r7mut.out); its 21
r6edits5 text mutants (T1-T10 on R6-D and the seated Lemma 11.0, P1-P9 with P1' and P8' on R8-E's blocks) are all killed
and the unmutated copy passes (mutout8/textmut2.out: T3 by E2g, T6 and T7 by E1d's (p) and (q), T8 by E2a, P1' by E4c's
BEYOND5 predicate on Block 1, P4, P5, P7, P8' and P9 by E4c's status words); and its two r6sigma5 mutant runs, which had
not finished when round 7 was read, have finished since and are both killed, as R7.0 claimed (the W5 weight r^(2a+1) ->
r^(2a+3) fails W5, W, W' and W'''; Step 2's threshold 2 -> 3 fails W6-W8, W and W').

### R8-A The openness step, exactly (R7-A amended)

*The general claim.* Let c < 7/25 and let g be a metric on a region of W with sup |g^-1 - g_b0^-1|_op <= c there (m <=
1/16, |f'| <= 1/4). Then (r7settle5 K1, K5, exact): both conormals alpha and beta are timelike for g, with g^-1(beta,
beta), g^-1(alpha, alpha) <= -7/4 + (25/4) c < 0; |g - g_b0|_op <= s^2 c/(1 - s c) <= 0.4520 (g - g_b0 = g
(g_b0^-1 - g^-1) g_b0, |g_b0|_op = s = m + (1 + m^2)^(1/2)), so g(d_t, d_t) <= -1 + 1/16 + 0.4520 < -0.485; and
g^-1(dt~, dt~) <= -15/16 + (17/16) c <= -0.64, so the slices Sigma~ are spacelike. All these margins depend on c only,
so R6-A (ii)'s Gronwall constants are uniform on such a region. This is the hypothesis under which R7-A's first
paragraph holds; its "|g^-1 - g_b0^-1|_op < 7/25" reads "sup ... <= c < 7/25".
[R9 (nits 2-3): K5 and K6 now state and test these numbers, 0.4520 and 0.2845 r^-2, and test that each bound is attained
(R9.0).]

*The openness step, restricted to the exterior regions.* R6-A (ii)-(iv) use the margin only on the exterior regions
X'_(rho, V_*) with rho >= rho_0 (on the part r <= rho of a slice the energy is the integral of a smooth function over a
compact set, continuous with no margin). For (t~, x) in X'_(rho, V_*) with t~ in [sigma*, sigma* + delta'], the time
segment from (sigma*, x) to (t~, x) lies in W_T: r >= rho >= rho_0 >= 4R, and v(sigma*, x) >= v(T, x) > v1 by the choice
of rho_0 ({t~ = T, r >= rho_0} lies in {v > v1}), v increasing with t~ at fixed x. So |H(t~, x)| <= |H(sigma*,
x)| + (t~ - sigma*) sup |d_t H| <= 1/25 there for delta' small (Step 2 at sigma*, the bound on d_t H on the interval of
existence), hence sup |g^-1 - g_b0^-1|_op <= 0.0474 =: c < 7/25 on the exterior regions over [T, sigma* + delta'], and
the general claim applies. The points of W_T near N, where a segment from sigma* could leave W_T, lie in the compact
part and need no margin. The rest of R7-A's openness step stands.

*Step 4's margin.* Step 2's bound is taken as |H| <= min(1/50, mu/(2 r^2), r^-2/4) (it holds for lam <= lam_2 and eps_B
<= eps_2 as before: C lam r^-2 + C_S eps_B r^(-1/2-a) <= r^-2/4 for a >= 3/2), so that |g^-1 - g_b0^-1|_op <= 0.2845
r^-2 < r^-2/2 on r >= 8 (r7settle5 K6; with r^-2/2 it would be 0.571 r^-2, K6'), the margin under which D4-D5 make
{Phi_W = V_*} a future boundary for Step 4's identity on D_*(sigma), sigma <= sigma*.

### R8-E Theorem R5.1's status (final), and the paper's text (final)

Theorem R5.1 stands as stated in R5-E, with Proposition R5.2's proof as in R6-A, Lemma R4.5 as widened in R6-B, Step 6's
openness as in R7-A with R8-A, and R5-C (v) not among its conditions ((r6-F4)).

*Status (replacing R7-E's).* **Deduced**, in this file (rounds 1-8; rounds 1-7 read by verifiers, round 7 by vB7, every
finding seated in R5.0-R8.0; round 8 not yet read), and **conditional on**:

- (a) statements the record lists as proved (proof5/README.md): Part IV's seven outputs (R3-A); III.C Definition 3.1 and
  Lemma 3.2 (a) (D245) and III.A Lemma 3.2 (D231), in Proposition R2.2; III.A Lemma 1.3 (D231), through LOSS-D's READ,
  in R2.4's count of what the half class changes; III.A Lemma 1.2 (D231), only in Lemma R2.3, which is not on the
  theorem's chain (listed conservatively); III.C' Theorem 3.1 under row d1, III.C'' Theorem 3.1 (2) and Proposition 4.1,
  in Theorem R2.4, Proposition 4.1 also rebuilding III.K's gauge data from (gamma, k) (R4-F); III.K Theorem 4.3; Part
  VII Lemma 0.1 (in R2.4's count), Lemmas 1.1, 1.2 (R4-D's setting: R is free) and 2.1 (Step 9's computation of (gamma,
  k)), Theorem 0.2 (in Theorem R2.4) and Proposition 3.2 (D324); Part VIII Lemma 1.1 (D336), in Theorem R2.4's list of
  statements generic in E_0; N1STAR-PROOF.md's Theorem E (sections 1-4), whose Step 8 local theory R4-D Step 6, R5-B,
  R6-A, R7-A and R8-A use; and Theorem P (D35), used at every order through Corollary R4.3, its uses of Lemma 1.1 (e)
  and Lemma 2.3 standing after D623 (R6.0 (m5) (c));
- (b) statements outside this file that the record lists as deduced: N1STAR-PROOF.md section 11.1 (Lemmas 11.0, 11.1,
  11.2 and Proposition 11.1), its D44 repair read by D45 and D47, Lemma 11.0's top-order repair (R6-D) read by the
  round-6 and round-7 readers and seated as D630, D618's amendment of Lemma 11.2 already in the file, and D618's edits
  to sections 9.5 and 11 awaiting a confirming read that starts after D630 (section 11.1 is used by Proposition R5.4,
  Lemma R3.2, Lemma R4.4, Lemma R4.5 (i) and Step 9); and BEYOND5 Lemma 6.4 (iv) (W, N and their placement in Omega' cup
  P'), labelled deduced at D400 and read by verifier 180 at D405;
  [R9 (m2): superseded by R9-E: the confirming read of sections 9.5 and 11 is done and seated (D632), section 11 is
  marked proved (D633), and BEYOND5 Lemma 6.4 (iv) is replaced on the chain by Lemma R9.1.]
- (c) this file's statements: Lemma R2.1, Proposition R2.2 (computed for every round count III.C' uses, M <= 12, exactly
  below 11/2), Theorem R2.4, Lemmas R3.2-R3.3 (as amended), Propositions R4.1-R4.2, Corollary R4.3, Lemma R4.4, Lemma
  R4.5 (as widened, R6-B), R4-D with R5-B, R6-A, R7-A and R8-A (Theorem R5.1′), Propositions R4.9, R5.4 and R5.2 (its
  proof as in R6-A), and Theorem R5.1; rounds 1-7 read, round 8 not yet;
- (d) the programs they cite.

It rests on no statement of Part IX. What has to be read for the label "proved": section 11.1 after D630 (the confirming
read of sections 9.5 and 11); BEYOND5 Lemma 6.4 (iv): its label is "deduced" (D400), verifier 180 read the entries
containing it (D405) and its one serious finding concerned the loss's gap condition, so the lemma is promoted to
"proved" only by the record's own decision on that read, recorded in BEYOND5.md, or by a further read; round 8 of this
file; the programs. Not evaluated: lam_2, eps, delta, lam_1 (another workstream), in either class. The list was made by
reading every statement outside this file that rounds 2-8 cite on the theorem's chain and the round-6 and round-7
readers' lists; nothing else is open in the theorem.
[R9 (m2): the confirming read of sections 9.5 and 11 is done (D632) and section 11 is marked proved (D633); what remains
to be read is round 9 of this file (R9-E).]

*Computational support, stated as what was computed.* As R7-E's, with: the general claim of R7-A exact (K5) and Step 4's
margin (K6); the window computed from the measured cap and tail exponents and residual degree and from exponents counted
by hand, those of the rows, of the data class, of Step 2's pointwise bound and of Lemma R4.5's and Proposition R5.2's
thresholds ([arithmetic], W4-W8).

*The text for the paper* (RESPONSE-HL-5D.md, not edited here; final, superseding R5-E's, R6-E's and R7-E's blocks). Each
old text is located by content and occurs exactly once in the current file (md5 4c121081 at the final run, 5930486d, its
committed state, when written: the two differ in the paper's md5 table only), every line of the edited file is within
121 characters, and the new texts state what the round-5 to round-7 readers asked, status words included (r6edits5 E4).

Block 1, in "Settling", old:

```text
  not evaluated. Theorem 4 (i) concerns glued data that agree with g_λ's on a ball; settling of g_λ's own continuation
  is not shown. Evaluating λ1 and δ would need every constant of the write-out made explicit, and several come from
```

Block 1, new:

```text
  not evaluated. Theorem 4 (i) concerns glued data that agree with g_λ's on a ball. That the development of g_λ's own
  data settles, with no gluing, is deduced in a data class wider than (ii)'s by half-integer orders, conditional on
  supplement section 11.1, deduced, whose Lemma 11.0 repair is seated and, with D618's edits to sections 9.5 and 11,
  awaits a confirming read, on BEYOND5 Lemma 6.4 (iv), deduced and read by a verifier, and on the last round of that
  deduction, not yet read by a verifier (Beyond the boundary, below). Evaluating λ1 and δ would need every constant of
  the write-out made explicit, and several come from
```
[R9 (m2): superseded by R9-E's Block 1: "whose Lemma 11.0 repair is seated and, with D618's edits to sections 9.5 and
11, awaits a confirming read" reads "... has been read by a confirming reader (D632)", section 11.1 is proved (D632,
D633), BEYOND5 Lemma 6.4 (iv) is Lemma R9.1, and the conditions are separated by semicolons.]

Block 2, in "Beyond the boundary", old:

```text
  6.3, deduced). It is not shown that Theorem 4 applies to g_λ's own data: g_λ is given on Ω, which does not contain the
  whole initial slice, and continuing it to spatial infinity asks for a scattering problem from past null infinity and an
  expansion of its solution at spatial infinity. Parts of that are done (deduced, with exact computations, all under
  `docket68/n1star/`): the leading Coulomb part carried to spatial infinity with no logarithm (`checks/coulomb5.py`, and
  under the full operator `checks/coulombL5.py`), the map from data on the initial null hypersurface to the leading
  coefficient at spatial infinity, under the write-out's full operator on Minkowski space, bounded uniformly in the
  harmonic (reduced for every harmonic, `checks/harmonics5.py`; bounded, `checks/uniform5.py`), the remainder's sources,
  supported where v is bounded along the initial null hypersurface, entering one order later at every harmonic computed
  (l ≤ 12) (`checks/sources5.py`, `checks/stripfull5.py`), and the approximant's stage profiles expanded in powers of
  r^(−1/2) at past null infinity, with the closure properties of that expansion shown (deduced, with an exact check,
  `checks/closure5.py`). The scattering estimate itself is not done. Below the inner boundary the theorems are not
```

Block 2, new:

```text
  6.3, deduced). It is deduced, with no gluing, that Theorem 4 applies to g_λ's own data in a data class wider than
  (ii)'s by half-integer orders (supplement `docket68/n1star/SETTLE-GLAM5.md`, rounds 1–8, Theorem R5.1), conditional
  on the write-out's Parts III, IV, VII and VIII, proved; on Theorem P, proved; on supplement section 11.1, deduced,
  whose Lemma 11.0 repair (SETTLE-GLAM5.md R6-D) is seated and, with D618's edits to sections 9.5 and 11, awaits a
  confirming read; on BEYOND5 Lemma 6.4 (iv), deduced and read by a verifier; and on round 8 of SETTLE-GLAM5.md, not
  yet read by a verifier. After the shell g_λ − g_b0 has at past null infinity an r^(−5/2) coefficient, O(λ^∞), which
  for a C_c^∞ envelope and every amplitude but at most one is nonzero off a discrete set of λ (deduced, SETTLE-GLAM5.md
  Proposition 3.1; computed for a bump envelope, `docket68/n1star/checks/tail5.py`); it puts an r^(−5/2) term into
  g_λ's data at spatial infinity, outside the integer orders of (ii)'s class. With the orders r^(−2), r^(−5/2),
  r^(−3), … below r^(−ℓ0) admitted in the metric (ℓ0 ∈ (3, 4), ℓ0 ≠ 7/2, and one order more in the second fundamental
  form), Hintz's construction runs with the same index sets for its iterates and finitely many more derivatives lost;
  its threshold ε, and with it λ1 and δ, change and are not evaluated, in either class. g_λ continues to the past
  domain of dependence of the far part of Hintz's initial surface as a vacuum metric in the record's wave-map gauge, by
  one weighted energy estimate at a weight a ∈ (ℓ0 − 1, 3), run on bounded domains of dependence, after its
  self-similar terms through r^(−4) are subtracted; it is the only continuation in that gauge near Tangherlini whose
  commuted energies of weight a0 ∈ (0, ½) stay bounded, its energy vanishing toward past null infinity, and its data
  lie in the widened class with small norm. So for every 0 < λ ≤ λ2, λ2 not evaluated, with no exceptional set, the
  maximal vacuum development of g_λ's own data on Hintz's initial surface settles to five-dimensional Tangherlini of a
  mass m′ with |m′ − μ_end| < ε_m at Theorem 4's rate (deduced, with the conditions above). Computed, all under
  `docket68/n1star/checks/`: the operator identities, on the write-out's full operator; the coefficient decays and the
  residuals' degrees, measured on that operator (`r5op5.py`, and `r6sigma5.py`, which also builds the r^(−4) term
  there for one example, the general case being deduced); the caps and the null-hypersurface tails, measured on
  explicit fields; the weight window, computed from those measured exponents and from exponents counted by hand
  (those of the data class, of the pointwise bound, and of two further thresholds, which do not bind); the remaining
  kernel exponents, counted by hand with their integrability checked. Below the inner boundary the theorems are not
```
[R9 (m2): superseded by R9-E's Block 2, which states section 11.1 proved (D632, D633), R6-D read by the confirming
reader (D632), and round 9 (Lemma R9.1) as the round not yet read.]

Block 3 (section 8.1, for consistency with blocks 1-2), old:

```text
replaced by a gluing (section 8.7), and Theorem 4 is not shown to apply to g_λ's own data.
```

Block 3, new:

```text
replaced by a gluing (section 8.7); that Theorem 4 applies to g_λ's own data, with no gluing, in a class wider by
half-integer orders, is deduced, conditionally, in section 9 (Beyond the boundary).
```

Ledger (round 8). Changed and rerun: `r7settle5.py` (12 checks), `r6edits5.py` (24, E1s among them; 29 since R8-F),
`r6sigma5.py` (21; only its stated run time changed). Every changed `.out` is from a full run and byte-identical on a
second run; the other programs are unchanged and their `.out` files stand (r6settle5 21, r5settle5 45, r5edits5 11,
zinv5 3, r5op5 7, cclass5 6, poly5 28, scale5 25, trunc5 23, scatter5 16, boot5 48, order5 22, f1lemma5 12, vac5 8
checks). r5edits5 and r6edits5, which read this file's R5-D, R6-D and R8-E, were rerun after its last edit of this round
(the line-break moves of nit (8) included): both .out files unchanged. Deduced: R8-A. READ: BEYOND5.md Lemma 6.4's
label; N1STAR-LOG.md D400, D405; SETTLE-GLAM5.md round 2 (R2.1-R2.4) for the citations of nit 7; RESPONSE-HL-5D.md (md5
4c121081; 5930486d when written). None from outside sources.

Open in the theorem: nothing beyond its status (the readings named above). Not evaluated: lam_2, eps, delta, lam_1.

    python3 checks/r7settle5.py   (7 to 12 seconds)
    python3 checks/r6edits5.py    (7 to 14 seconds)
    python3 checks/r6sigma5.py    (about five minutes, 304 and 311 seconds, beside the others; S4 most of it)

The times are wall-clock on this machine under the load of the other workstreams.

### R8-F The section-9.5/11 reader's findings on R6-D (added to round 8)

The independent reader of N1STAR-PROOF.md sections 9.5 and 11 (the coordinator's report-vN95) confirmed R6-D seated
byte-exact (D630) and its induction correct, and reported two things for this file, both re-derived here. Its other nits
(n1, n2, n4-n8) are on N1STAR-PROOF.md outside R6-D's blocks and are D632's.

*Its four surviving text mutants.* M10 (Edit 2's factor e^(2C(1 + lam)) -> e^(2C/lam)), M14 (Edit 2's f = f_gamma^n ->
R_gamma^n, which treats b . d U as known there), M19 (Edit 2's sums removed, so Gronwall acts per gamma) and M12 (the
family's |delta| = j + 1 -> j) passed r6edits5 as it stood in rounds 7 and 8: predicates (m) and (n) read only Edit 1,
and E2d only Edit 1's factor. Accepted. r6edits5 now reads Edit 2 structurally (`read_edit2`): the forcing of its energy
inequality, the index sets of the two sums of its Gronwall bound, and its factor's exponent. E1d gains three predicates:
(r) the forcing is f_gamma^n, and the definition of f_gamma read from Edit 1 contains b . d U (R_gamma's subtracts it);
(s) both sides of the Gronwall bound are sums over the family; (t) the step's |gamma|, the family's |delta|, the sum in
||f_gamma||'s bound and Edit 2's two sums read one index. E2d now also requires Edit 2's factor, read, to equal the
computed exp(int_(lam^-2)^oo C(1 + lam^-1) t^(-3/2) dt) = e^(2C(1 + lam)); for R5-D's text, which r5edits5 E1f reads
through E2d and which states no second factor, the requirement is off, and r5edits5's output is unchanged. E1e's control
still fails every predicate, (r)-(t) included, on the unedited Lemma 11.0. E3 carries the four as controls, each caught
(M10 by E2d, M14 by (r), M19 by (s) and (t), M12 by (t)), and E3 now reports, instead of stopping, when the text under
test lacks a control's target, so that E1's and E2's verdicts are printed. On scratch copies, each mutant applied to
R6-D's printed block and to the seated text together (mutout8/textmut3.out), the four and five variants (M10', the
factor e^(C(1 + lam)); M14', f = c^n U_n + R_gamma^n; M19' and M19'', one sum removed; M12', Edit 2's sums at |gamma| =
j) are killed 9 of 9 by the new r6edits5 (by E2d for M10 and M10', by E1d for the rest; M14' also by E2d), against 1 of
9 by the round-8 version (M14', by E1b's line length only). The round-7 reader's 21 text mutants are still killed, 21 of
21 (mutout8/textmut4.out).
[R9 (nit 6): (r) now also reads the signs of f_gamma's and R_gamma's definitions and composes them, b . d U and c U
cancelling (R9.0).]

*n3, the rotation case.* R6-D's printed text needs no wording change. Its induction is over coordinate derivatives (Edit
1: "for |gamma| = j + 1, by Leibniz's rule U := d^gamma u_1"), where each product is at most C t^(-2) (E2g; the |gamma'|
= |gamma| term, (d g^{ab}/d g . d^gamma u_1) d_a d_b u_1, is t^(-1/2) t^(-2) = t^(-5/2)). Rotations enter only in the
unchanged text after Edit 2, the bookkeeping paragraph's "(with Omega^beta among the derivatives the same way: ...)" in
N1STAR-PROOF.md, which R6-D does not edit. There the reader's point holds, computed in the new E2i (exact): a rotation
keeps a field's class while a coordinate derivative raises it (r^-q x_1/r along a ray: r^(-q) against r^(-q-1)), and
|Omega f| <= r |d f| (Lagrange's identity), so for pure-rotation gamma the lower steps' energies bound ||Omega^gamma
u_1|| only by C t^(1/2), and that product is C t^(-3/2), not at most C t^(-2). It is not above the source's C t^(-3/2),
so ||R_gamma|| <= C(lam, j) t^(-3/2) and Edit 2's integral stand as printed; alternatively, since Omega v = 0,
Omega^gamma u_1 vanishes on {v = v_start} and Lemma 9.3(b) puts the term into the family, with kernel C t^-2, whose
integral over t >= lam^-2 is C lam^2, a lam-free factor. Edit 1's aside "(With c U taken as a source, through the
energies of the lower steps, the step also closes at fixed lam, at one lam^-1 per order.)" is right as printed, for
coordinate derivatives (lam^-1 t^(-3/2) t^(-1/2) is integrable over t >= lam^-2); with rotations it is not (lam^-1
t^(-3/2) t^(1/2) = lam^-1 t^-1), and c U goes into the family by Lemma 9.3(b), as Edit 1's main route does. So the note
belongs at the rotation parenthetical, not in R6-D, and D632 has seated one there since (N1STAR-PROOF.md md5 5043cedf,
"for pure rotations gamma the |gamma'| = |gamma| Leibniz term of R_gamma has the L^2 factor ||Omega^gamma u_1^n||, which
the lower steps' energies bound only by C t^(1/2) ... and the aside on c U taken as a source is for Cartesian gamma"):
it states what E2i computes, with the constant 2 r where Lagrange's identity gives r, which is harmless.

Ledger (R8-F). Changed and rerun: `r6edits5.py` (29 checks: E2i and four E3 controls added, E1d and E2d widened; FAILED
none), byte-identical on two runs; `r5edits5.py`, which imports it, rerun: its .out unchanged. Deduced: n3's disposition
(with E2i). READ: the section-9.5/11 reader's report (mutants and n3); N1STAR-PROOF.md's bookkeeping paragraph after
Edit 2 (md5 88179da4 when read, 5043cedf with D632's note at the final run, on which r6edits5 and the mutants were run).
None from outside sources.

    python3 checks/r6edits5.py    (9 to 11 seconds)

## Round 9 (2026-11-06)

### R9.0 The round-8 reader's findings, and their dispositions

The round-8 reader confirmed round 8: no major finding; R8-A and R8-F correct line by line; r7settle5 and r6edits5
byte-identical on its runs. Its findings are two minor ones (m1, m2) and eight nits, and the commission asks for one
promotion: no open item in Theorem R5.1's conditions that this workstream can close. Each is re-derived below; the
amended sites carry [R9] notes, the old text kept. New programs: `checks/r9beyond5.py` (Lemma R9.1) and
`checks/r9text5.py` (the file's own text); changed: `r7settle5.py` and `r6edits5.py`.

**(m1) The nit-8 rewrap corrupted R6-A (ii) and its "[R7 (nits)]" note.** Accepted. The round-8 script that moved two
notes and rewrapped three paragraphs took the note's continuation line, which began "- g_b0^-1|_op", for part of the
paragraph above, so the paragraph ended "...at most C lam^2 rho^-9. - g_b0^-1|_op < 7/25, with R7-A's cut; Step 6's
openness at sigma* is R7-A.]" and the note stopped at "on which |g^-1". The fragment is put back at the note's end, the
break before "|g^-1", so that no line begins with "- ". Verified by word sequence, not by multiset: the rounds 1-7
region of the file, with the [R8] and [R9] notes removed (bracket-matched) and the two R7 notes that round 8 moved
compared as notes, is word for word the round-7 file (git 54c8634, md5 8235b0a9), 46111 words in the same order
(`r9text5.py` T1; control T1': round 8's misplacement re-created in memory fails). The same comparison run before the
repair finds exactly this one displacement and nothing else; round 8's seven line-break moves change no word's position.

**(m2) R8-E's status was behind D632.** Accepted. D632 (N1STAR-LOG.md; N1STAR-PROOF.md lines 55-61 and 10941-10952 at
md5 5043cedf) seats the confirming read of sections 9.5, 9.10 and 11: R6-D byte-exact in Lemma 11.0, its induction
holding line by line, one minor finding and eight nits seated; D633 (landed: N1STAR-PROOF.md md5 5c1a186a, 11402 lines;
section 9.5 and Theorem M, section 11, now "proved (D632)", amended in place, the header saying sections 9.1-9.5, lines
1-962 keeping their numbers) marks section 11 proved. R8-E (b), its list of what must be read for "proved", and its
Blocks 1 and 2 ("whose Lemma 11.0 repair is seated and, with D618's edits to sections 9.5 and 11, awaits a confirming
read") are superseded by R9-E, where the repair "has been read by a confirming reader (D632)" and section 11.1 is
"proved (D632, D633)". [R9] notes are inserted at the four sites. E4 now reads R9-E's blocks, and E4c' checks that
R8-E's blocks fail exactly the eight predicates round 9 adds.

**Nits.**
- (1) The paper's md5 is now b21cd7ca; it differs from 4c121081 in md5-table rows only. R9-E's old texts are located by
  content and each occurs once in it (r6edits5 E4a).
- (2) R8-A's 0.4520 and 0.2845 against K5's printed 0.4521 and K6's 0.2847: K5 and K6 now state and test the same
  numbers, |g - g_b0|_op <= 0.4520 (0.451961 at delta = 7/25) and <= 0.2845 r^-2 (0.2844468).
- (3) K5 and K6 test attainment (the reader's N1, N8, one factor s dropped, survived): K5 takes delta = -sign(w) c e e^T
  along g_b0^-1's eigenvector e of least |eigenvalue| w at c = 0.2797, m = 1/16, and finds |g - g_b0|_op = 0.4512716,
  the bound's value (the reader's 0.4513176 is the same bound at c = 0.27972); K6 takes H along g_b0's eigenvector of
  least |eigenvalue| at r = 8 and finds 0.2844468342 r^-2, the bound's value.
- (4) K2's worst directions are computed, not typed (N9, N10 changed the typed 1.5 to 1.0 and survived): `worst_fp`
  finds exactly the f' in [-1/4, 1/4] at which each conormal's threshold -g_b0^-1(c, c)/|c|_E^2 (m = 0) is least, f' =
  -1/4 for beta and 1/4 for alpha, both 7/25, and the new K2'' checks that along them delta of size 7/25 makes the
  conormal null and 0.27 keeps it timelike.
- (5) E4c checks the status words "(deduced, with the conditions above)" in Block 2 and "is deduced in a data class" in
  Block 1 (the reader's P12, P13, changing them to "(proved)" and "is proved", survived), in outcome A, and their proved
  forms in outcome B.
- (6) Predicate (r) reads R_gamma's signs (V-X1, "- b . d U" -> "+ b . d U" in R_gamma's definition, was caught only
  through another predicate): `signed_terms` reads f_gamma's and R_gamma's definitions as signed sums of b . d U, c U,
  R_gamma and d^gamma F_1, and `definitions_consistent` composes them: f_gamma must be d^gamma F_1 plus the sums, b . d
  U and c U cancelling (Leibniz's rule).
- (7) Block 1's conditions are separated by semicolons (R9-E; E4c checks it).
- (8) R8-A uses rho_0 >= 4R, which R6-A (i) did not state. Added there by an [R9] note: rho_0 is also taken >= 4R, so
  that the exterior regions lie in r >= 4R, where |f'| <= 1/4 and m <= 1/16.

**The promotion.** (a) Section 11 of N1STAR-PROOF.md has been read by an independent confirming reader with its findings
seated (D632) and is marked proved by D633; Theorem R5.1's condition on it is stated "proved (D632, D633)" (R9-E). (b)
BEYOND5 Lemma 6.4 (iv) (BEYOND5.md:198-212, "deduced, D400", read by verifier 180 at D405) is written out in full as
Lemma R9.1 (R9-B), with the past domain of dependence for g_b0 exact, the O(lam) displacement of its null boundary under
a nearby metric explicit and bounded, the placement of N in Omega' cup P' with its inequalities proved from Part VII
Lemma 1.2's, and the radiation field's vanishing read; `r9beyond5.py` computes every inequality, with controls that
fail. It is placed in this file, where it is used; BEYOND5.md is not edited. Theorem R5.1 stays "deduced" until an
independent reader has read round 9; R9-E gives the paper's blocks for both outcomes.

**The reader's surviving mutants, rerun** (its scripts or their equivalents on the round-9 code, on scratch copies;
outputs in this round's scratch, mutout9/): @@MUT9@@

### R9-B Lemma R9.1: BEYOND5 Lemma 6.4 (iv), written out

BEYOND5 Lemma 6.4 (iv) is on Theorem R5.1's chain through W, N and their placement in Omega' cup P', and through the
radiation field's vanishing at past null infinity (R4-D's setting, Lemma R3.3, R4-D's truncations, Proposition R5.2
(4)). It is written out here in full.

*Setting.* The record's chart (tau, x), r = |x|, xhat = x/r, v = tau + r (N1STAR-PROOF.md 0.1). On {v >= v_end}, mu =
mu_end and g0 = eta + m dv dv, g0^-1 = eta^-1 - m L0 L0, L0 = d_tau - xhat.d_x, m := mu_end r^-2; there g0 = g_b0 (Part
VII Lemma 1.2 (a)). R >= R_3 is R4-D's: on r >= 4R, m <= 1/16. In Part VII's chart (t, x) = (tau + T_mu_end(|x|) + c_0,
x), Sigma_IVP cap {r >= R_3} = {t_KS = f(|x|)} with t_KS = t - T_mu_end = tau + c_0 (PART-VII-ASSEMBLY.md 162-163), that
is {tau = F(r)} with F := f - c_0, F' = f' in |x|^-2 C^oo (177) and |F'| <= 1/4 on r >= 4R (R6-A), so tau_max :=
sup_(r >= 4R) F is finite. Put S := Sigma_IVP cap {r >= 4R}, tau_S := F(4R), v1 := 4R + tau_S (the value of v on dS), t~
:= tau - F(r), W := {v >= v1, t~ <= 0, r >= 4R}, N := W cap {v = v1} = {v = v1, tau <= tau_S} and Zb := {v <= v1, r >=
4R}. In R4-D's notation t = tau + c_0 and f = F + c_0, so t~ and W are R4-D's ("t <= f(r)"; r >= 4R is stated here, and
is implied where Sigma_IVP is spacelike for g0 on [R_3, 4R], that is F' > -1 there). Omega', P', V', tau'_end, V'_P,
kappa and h are BEYOND5 Lemma 6.4's (Part VII Lemma 1.2's Omega' and the supplement's (9.1) for its parameters);
tau_top, q_end, r_0 and a' are Part VII Lemma 1.2's.

**Lemma R9.1 (BEYOND5 Lemma 6.4 (iv), written out; deduced, every inequality computed).**
- (i) *The domain of dependence for g0.* t~ is a time function on {r >= 4R}, g0^-1(dt~, dt~) = -1 + F'^2 - m(1 + F')^2
  <= -15/16, and v is nondecreasing along future causal curves (dv is null). W = D^-(S; g0) in (R x (R^4 \ 0), g0). Its
  boundary is S, N and past null infinity at v >= v1 (tau -> -oo at fixed v >= v1 and xhat, r -> oo), and r >= v1 - tau
  on W.
- (ii) *The placement.* m_Omega := V' + 1 - (v1 + tau_S - tau'_end) >= q_end + 3 >= 3, and v1 >= v_end + 2. Every point
  of {v <= v1 + 1/2, r >= 4R} lies in Omega' if tau >= tau0 (with tau <= tau'_end - 1/2, v + (tau - tau'_end) <= V' - 1
  and r > a') and in P' if tau <= tau0 (with v + h(tau) <= V'_P - 3). So N and a strip of v-width 1/2 beyond it lie in
  Omega' cup P', and v1 = V'_P - kappa - (tau_S - tau0) - m_Omega <= V'_P - kappa - 1 - m_Omega.
- (iii) *The displacement under a nearby metric.* Let g be a smooth Lorentzian metric on an open set M containing W cup
  Zb, and eps a continuous function of tau, 0 <= eps <= 1/8, with |g - g0|_op, |g^-1 - g0^-1|_op <= eps(tau) at the
  points of W cup Zb (Euclidean operator norms of the component matrices), and I(tau) := 2 int_tau^(tau_max) eps finite.
  Then d_tau is g-timelike and taken future-directed, and: (a) W_+ := {v >= v1 + I(tau), t~ <= 0, r >= 4R} lies in
  D^-(S; g); (b) from every p in {r >= 4R} with v(p) < v1 - I(tau(p)) a future g-timelike curve along which r decreases
  reaches {r = 4R} at a point q with v(q) < v1, meeting no point of S; so p is not in D^-(S; g) whenever q has a
  future-inextendible causal continuation along which r keeps decreasing (for g0, the ingoing null ray; for g, the curve
  of Y below while |g - g0|_op <= 1/8 along it), and then D^-(S; g) cap {r >= 4R} lies in W_- := {v >= v1 - I(tau), t~
  <= 0, r >= 4R}. The null boundary of D^-(S; g) through dS therefore lies in {|v - v1| <= I(tau)}: N displaced by at
  most I(-oo).
- (iv) *The size of the displacement.* For the record's g_lam on Zb, |g_lam - g0| <= C lam on the compact Omega'
  (Theorem 1: g_lam - g_app = O(lam^K) and g_app - g0 = O(lam) there) and |g_lam - g0| <= C lam^(K-3) t^-2 + C lam
  t^(-3/2) on P' ((P-iii) and (P-v)'s margin |g_app - g0| <= C lam t^(-3/2)), g_lam = g0 on {v <= v_start} (P-i); so
  eps_lam := C_1 lam min(1, t^(-3/2)) (t = 1 + tau0 - tau) bounds both norms on Zb for lam small (the inverse by K3's
  Neumann bound), and its I(-oo) = 2 C_1 lam (tau_S - tau0 + 2) = O(lam). For Theorem R5.1's continuation g on W,
  |g - g0| <= C lam r^-2 + C_S eps r^(-1/2-a) <= C (lam + eps)(v1 - tau)^-2 (Step 2 as R8-A takes it, a >= 3/2, r >=
  v1 - tau), eps Theorem R4.6's, which tends to 0 with lam; its integral is C (lam + eps)/(v1 - tau_max). So I(-oo) <= C
  (lam + eps): the null boundary of D^-(S; g) is N displaced by O(lam + eps), by O(lam) on the record's side.
- (v) *Nothing incoming.* At past null infinity, for v >= v1 >= v_end + 2, the record's radiation field lam [W_TT]
  (P-ii) vanishes: W_TT is proportional to the envelope, which vanishes for v >= v_end, and every oscillating profile
  vanishes on {v > v_end} (PART-VII-ASSEMBLY.md 123-129). By (P-ii), r^(3/2)(g_lam - g0) -> 0 as r -> oo at every fixed
  v in [v1, V'_P) and xhat.

*Proof.* (i) The contractions are B1's (exact): g0^-1(dv, dv) = 0, g0^-1(dv, dtau) = -1, g0^-1(dtau, dtau) = -1 - m,
g0^-1(dr, dr) = 1 - m, g0^-1(dtau, dr) = m, so g0^-1(dt~, dt~) = -1 + F'^2 - m(1 + F')^2, at most -15/16 on |F'| <= 1/4
(its maximum at m = 0, decreasing in m). dt~(d_tau) = 1 and dv(d_tau) = 1, so t~ increases and v does not decrease along
future causal curves. beta = d(r + 2t~) and alpha = d(r - 2t~) have g0^-1 <= -7/4 (K1), beta(d_tau) = 2 and alpha(d_tau)
= -2, so |dr(Y)| < 2 dt~(Y) for future causal Y. L0 is future null with L0(v) = 0, L0(tau) = 1, L0(r) = -1; along its
rays t~ = v - r - F(r) increases as r decreases, and d(r + F)/dr = 1 + F' >= 3/4. *D^-(S; g0) lies in W.* For p in
D^-(S; g0), the ingoing null ray from p (v = v(p), r decreasing to 0) meets S, at r* >= 4R with tau = F(r*); so v(p) =
r* + F(r*) >= 4R + F(4R) = v1, r(p) >= r* >= 4R, and t~(p) <= 0, t~ increasing along the ray to 0 at r*. *W lies in
D^-(S; g0).* Let p be in W and gamma a future-inextendible causal curve from p; v >= v1 along it. If gamma reaches {r =
4R}, at a first point q, then t~(q) = tau(q) - tau_S = v(q) - v1 >= 0, so gamma meets {t~ = 0} at or before q, at a
point with r >= 4R and v >= v1: a point of S. Otherwise gamma stays in {r >= 4R}, where t~ increases and |dr| < 2 dt~;
while t~ <= 0 it lies in the compact set {t~(p) <= t~ <= 0, 4R <= r <= r(p) + 2|t~(p)|}, where, since dt~ is uniformly
timelike, its coordinate velocity parametrised by t~ is bounded; if t~ stayed below 0, gamma would have an endpoint and
be extendible. So gamma reaches t~ = 0, at a point with r >= 4R and v >= v1: a point of S. In the chart, W's boundary is
{t~ = 0} cap W = S, {v = v1} cap W = N and the end tau -> -oo at fixed v and xhat; r = v - tau >= v1 - tau on W. (ii)
From Part VII Lemma 1.2's proof (PART-VII-ASSEMBLY.md 150-159, proved): on Sigma_IVP cap {r_0 <= r <= 4R}, which
contains dS, tau >= tau0 + 1, v >= v_end + 2 and tau <= tau_top, so tau_S >= tau0 + 1, tau_S <= tau_top and v1 >=
v_end + 2; V' >= tau_top + 2R + q_end + 1; tau'_end >= V' - q_end and tau'_end >= tau_top + 1; r_0 > a' and 4R > r_0.
Then m_Omega = V' + 1 + tau'_end - 2 tau_S - 4R >= 2V' + 1 - q_end - 2 tau_top - 4R >= q_end + 3. For v <= v1 + 1/2 and
r >= 4R, tau = v - r <= tau_S + 1/2 <= tau'_end - 1/2; if tau >= tau0, v + (tau - tau'_end) <= v1 + tau_S + 1 - tau'_end
= V' + 2 - m_Omega <= V' - 1; if tau <= tau0, v + h(tau) <= v1 + 1/2 + kappa = V'_P - (tau_S - tau0) - m_Omega + 1/2 <=
V'_P - 3, as h <= kappa and V'_P = V' + 1 + (tau'_end - tau0) + kappa. B3 proves each implication in linear real
arithmetic (z3) from these hypotheses, which are satisfiable in each case; B3' finds a counterexample with V' three
smaller; B3n checks one instance of Lemma 1.2's construction on a grid of 24321 points (control: V' five smaller,
m_Omega < 0, leaves points out). (iii) (B2, exact.) g(d_tau, d_tau) <= -1 + m + eps < 0 and g^-1(dtau, dtau) <=
-1 - m + eps < 0, so dtau(Y) > 0 for future g-causal Y. *The cone of dv.* omega := dv + 2 eps dtau has g^-1(omega,
omega) <= g0^-1(omega, omega) + eps |omega|_E^2 = -2 eps - 4m eps^2 + 4 eps^3 < 0 for 0 < eps <= 1/8, and omega(d_tau) =
1 + 2 eps > 0, so omega(Y) > 0 for every future g-causal Y: dv(Y) >= -2 eps dtau(Y). Along a future g-causal curve
parametrised by tau, v - I(tau) is then nondecreasing. *The ingoing curve.* Y := L0 + 2 eps d_tau has g(Y, Y) <= g0(Y,
Y) + eps |Y|_E^2 = -2 eps + 4m eps^2 + 4 eps^3 < 0, dtau(Y) = 1 + 2 eps, dv(Y) = 2 eps and dr(Y) = -1: along its
integral curves r decreases at unit rate and dv/dtau <= 2 eps. t~ stays a g-time function on {r >= 4R} with |dr(Y)| < 2
dt~(Y) for future g-causal Y (K1, K5: eps <= 1/8 < 7/25). (a) For p in W_+ and gamma a future-inextendible g-causal
curve from p, v >= v1 + I(tau) >= v1 along gamma while it is in W (v - I nondecreasing), and the argument of (i) applies
verbatim: gamma meets S. (b) Along Y's integral curve from p, v(tau) <= v(p) + I(tau(p)) - I(tau) < v1 - I(tau) <= v1
while r >= 4R (by continuity, the bound holding where v < v1); so its points have v < v1 and r >= 4R, hence tau = v - r
< tau_S: they lie in Zb, where the bound holds, and none is on S (on S, v >= v1). r decreases at unit rate, so the curve
reaches {r = 4R} at q with v(q) < v1, and any continuation along which r keeps decreasing stays in {r < 4R}, disjoint
from S. The displacement bound follows: points of W_+ are in D^-(S; g), points below W_- are not. (iv) is the record's
bounds read ((P-i), (P-iii), (P-v)'s margin, Theorem 1 on the compact Omega', Step 2's pointwise bound as R8-A takes it,
Theorem R4.6's eps), with B4's integrals, exact: int_(-oo)^(tau0) (1 + tau0 - tau)^(-3/2) dtau = 2 and
int_(-oo)^(tau_max) (v1 - tau)^-2 dtau = 1/(v1 - tau_max). (v) is READ (PART-VII-ASSEMBLY.md 123-129: "the leading wave,
proportional to the envelope, vanishes on {v > v_end}", "every oscillating profile vanishes on {v > v_end}"; (P-ii)); B6
finds each quoted passage by content. ∎

*Computed (r9beyond5).* B1-B2 and B4's integrals exact (sympy, z3 with the vacuity guard); B3 in linear real arithmetic
(z3); B2' samples 3000 perturbations of each kind and finds the sharp constant of the cone comparison in (1/2, 2] (so
the factor 2 is not loose by more than 4); B4' integrates the past g-null generator from dS on a radial model, g^-1 =
g0^-1 + eps(tau) n n^T for eight directions n with eps = 0.05 min(1, t^(-3/2)), down to tau_S - 3000, and finds |v - v1|
<= I(tau) throughout, while along n proportional to dv it leaves |v - v1| <= I(tau)/4 (B4'', control); B5 samples (i) on
the model F = 3 + 64/r (from 300 points of W, 40 random future causal curves each meet S; at 600 random points the
ingoing null ray meets S exactly on W; control: {v >= v1 - 2, t~ <= 0, r >= 4R} has points whose ray misses S) and (iii)
on the perturbed model.

*What Theorem R5.1 uses.* R4-D's setting uses (i): W, N, t~ and r >= v1 - tau on W. Lemma R3.3 and R4-D's truncations
use (ii): g_lam's data on N, and on a strip beyond it, are the record's (V_T = V'_P - h(T) - delta_0/2 > v1 + 3 by
(ii)). Proposition R5.2 (4) and the data beyond the band use (v). Theorem R5.1 (1)'s name, "the past domain of
dependence W", is (i) for g_b0 and (iii)-(iv) for the continued metric: W and D^-(S; g) differ by a strip of v-width
O(lam + eps) along N. The last step of (iii) (b), that a curve entering {r < 4R} can be continued inward, concerns the
glued spacetime inside r < 4R; it holds for g0 and along the record's g_lam, and Theorem R5.1 does not use it.

### R9-E Theorem R5.1's status (final), and the paper's text (final, two outcomes)

Theorem R5.1 stands as stated in R5-E, with Proposition R5.2's proof as in R6-A, Lemma R4.5 as widened in R6-B, Step 6's
openness as in R7-A with R8-A, R5-C (v) not among its conditions ((r6-F4)), and BEYOND5 Lemma 6.4 (iv) replaced on its
chain by Lemma R9.1.

*Status (replacing R8-E's).* **Deduced**, in this file (rounds 1-9; rounds 1-8 read by verifiers, round 8 by its reader,
confirmed, every finding seated in R5.0-R9.0; round 9 not yet read), and **conditional on**:
- (a) statements the record lists as proved: R8-E's list (a), unchanged, and N1STAR-PROOF.md section 11.1 (Lemmas 11.0,
  11.1, 11.2 and Proposition 11.1, R6-D seated at D630), read by an independent confirming reader of sections 9.5, 9.10
  and 11 with its findings seated (D632) and marked proved (D633): "proved (D632, D633)";
- (b) statements outside this file that the record lists as deduced: none. BEYOND5 Lemma 6.4 (iv), which was the one, is
  replaced on the chain by Lemma R9.1, which writes it out in full (R9-B); BEYOND5.md is not edited;
- (c) this file's statements: R8-E's list (c), and Lemma R9.1; rounds 1-8 read, round 9 not yet;
- (d) the programs they cite, `r9beyond5.py` and `r9text5.py` among them.

What has to be read for the label "proved": round 9 of this file (Lemma R9.1 with `r9beyond5.py`, and the repairs of
R9.0). When an independent reader has read it and confirmed it, Theorem R5.1 is **proved**, conditional on supplement
section 11.1, proved (D632, D633): outcome B below; until then outcome A. Both outcomes rest on D633, which has landed
(N1STAR-PROOF.md md5 5c1a186a: Theorem M, section 11, "proved (D632)" [amended D633]). Not evaluated: lam_2, eps, delta,
lam_1 (another workstream), in either class. The list was made by reading every statement outside this file that rounds
2-9 cite on the theorem's chain and the round-6 to round-8 readers' lists; nothing else is open in the theorem.

*Computational support, stated as what was computed.* As R8-E's, with: the past domain of dependence, its placement and
its displacement (Lemma R9.1, `r9beyond5.py` B1-B6); K5 and K6 attained, K2's worst directions computed (r7settle5);
predicate (r) on the signs of f_gamma's and R_gamma's definitions (r6edits5); the file's own text against the round-7
file, word by word (`r9text5.py`).

*The text for the paper* (RESPONSE-HL-5D.md, not edited here; final, superseding R5-E's to R8-E's blocks). The three old
texts are the same in both outcomes; each is located by content and occurs exactly once in the current file (md5
@@PAPERMD5@@ at the final run), every line of the edited file is within 121 characters in either outcome, and the new
texts state what the round-5 to round-8 readers asked, status words included (r6edits5 E4). Outcome A is for round 9 not
yet read by an independent reader; outcome B for round 9 read and confirmed.

*Outcome A (round 9 not yet read).*

Block 1, in "Settling", old:

```text
  not evaluated. Theorem 4 (i) concerns glued data that agree with g_λ's on a ball; settling of g_λ's own continuation
  is not shown. Evaluating λ1 and δ would need every constant of the write-out made explicit, and several come from
```

Block 1, new:

```text
  not evaluated. Theorem 4 (i) concerns glued data that agree with g_λ's on a ball. That the development of g_λ's own
  data settles, with no gluing, is deduced in a data class wider than (ii)'s by half-integer orders, conditional on
  supplement section 11.1, proved (D632, D633); on BEYOND5 Lemma 6.4 (iv), now written out in full with every
  inequality computed (SETTLE-GLAM5.md Lemma R9.1); and on the last round of that deduction, which contains it and is
  not yet read by a verifier (Beyond the boundary, below). Evaluating λ1 and δ would need every constant of the
  write-out made explicit, and several come from
```

Block 2, in "Beyond the boundary", old:

```text
  6.3, deduced). It is not shown that Theorem 4 applies to g_λ's own data: g_λ is given on Ω, which does not contain the
  whole initial slice, and continuing it to spatial infinity asks for a scattering problem from past null infinity and an
  expansion of its solution at spatial infinity. Parts of that are done (deduced, with exact computations, all under
  `docket68/n1star/`): the leading Coulomb part carried to spatial infinity with no logarithm (`checks/coulomb5.py`, and
  under the full operator `checks/coulombL5.py`), the map from data on the initial null hypersurface to the leading
  coefficient at spatial infinity, under the write-out's full operator on Minkowski space, bounded uniformly in the
  harmonic (reduced for every harmonic, `checks/harmonics5.py`; bounded, `checks/uniform5.py`), the remainder's sources,
  supported where v is bounded along the initial null hypersurface, entering one order later at every harmonic computed
  (l ≤ 12) (`checks/sources5.py`, `checks/stripfull5.py`), and the approximant's stage profiles expanded in powers of
  r^(−1/2) at past null infinity, with the closure properties of that expansion shown (deduced, with an exact check,
  `checks/closure5.py`). The scattering estimate itself is not done. Below the inner boundary the theorems are not
```

Block 2, new:

```text
  6.3, deduced). It is deduced, with no gluing, that Theorem 4 applies to g_λ's own data in a data class wider than
  (ii)'s by half-integer orders (supplement `docket68/n1star/SETTLE-GLAM5.md`, rounds 1–9, Theorem R5.1), conditional
  on the write-out's Parts III, IV, VII and VIII, proved; on Theorem P, proved; on supplement section 11.1, proved
  (D632, D633), whose Lemma 11.0 repair (SETTLE-GLAM5.md R6-D) is seated and has been read by a confirming reader
  (D632); and on round 9 of SETTLE-GLAM5.md, not yet read by a verifier, which writes out BEYOND5 Lemma 6.4 (iv) in
  full (Lemma R9.1, every inequality computed). After the shell g_λ − g_b0 has at past null infinity an r^(−5/2)
  coefficient, O(λ^∞), which for a C_c^∞ envelope and every amplitude but at most one is nonzero off a discrete set of
  λ (deduced, SETTLE-GLAM5.md Proposition 3.1; computed for a bump envelope, `docket68/n1star/checks/tail5.py`); it
  puts an r^(−5/2) term into g_λ's data at spatial infinity, outside the integer orders of (ii)'s class. With the
  orders r^(−2), r^(−5/2), r^(−3), … below r^(−ℓ0) admitted in the metric (ℓ0 ∈ (3, 4), ℓ0 ≠ 7/2, and one order more in
  the second fundamental form), Hintz's construction runs with the same index sets for its iterates and finitely many
  more derivatives lost; its threshold ε, and with it λ1 and δ, change and are not evaluated, in either class. g_λ
  continues to the past domain of dependence of the far part of Hintz's initial surface as a vacuum metric in the
  record's wave-map gauge, by one weighted energy estimate at a weight a ∈ (ℓ0 − 1, 3), run on bounded domains of
  dependence, after its self-similar terms through r^(−4) are subtracted; it is the only continuation in that gauge
  near Tangherlini whose commuted energies of weight a0 ∈ (0, ½) stay bounded, its energy vanishing toward past null
  infinity, and its data lie in the widened class with small norm. So for every 0 < λ ≤ λ2, λ2 not evaluated, with no
  exceptional set, the maximal vacuum development of g_λ's own data on Hintz's initial surface settles to
  five-dimensional Tangherlini of a mass m′ with |m′ − μ_end| < ε_m at Theorem 4's rate (deduced, with the conditions
  above). Computed, all under `docket68/n1star/checks/`: the operator identities, on the write-out's full operator; the
  far part's past domain of dependence, the place of its inner null boundary in the record's domains and that
  boundary's displacement under g_λ, small with λ (`r9beyond5.py`); the coefficient decays and the residuals' degrees,
  measured on that operator (`r5op5.py`, and `r6sigma5.py`, which also builds the r^(−4) term there for one example,
  the general case being deduced); the caps and the null-hypersurface tails, measured on explicit fields; the weight
  window, computed from those measured exponents and from exponents counted by hand (those of the data class, of the
  pointwise bound, and of two further thresholds, which do not bind); the remaining kernel exponents, counted by hand
  with their integrability checked. Below the inner boundary the theorems are not
```

Block 3 (section 8.1, for consistency with blocks 1-2), old:

```text
replaced by a gluing (section 8.7), and Theorem 4 is not shown to apply to g_λ's own data.
```

Block 3, new:

```text
replaced by a gluing (section 8.7); that Theorem 4 applies to g_λ's own data, with no gluing, in a class wider by
half-integer orders, is deduced, conditionally, in section 9 (Beyond the boundary).
```

*Outcome B (round 9 read and confirmed).*

Block 1, in "Settling", old:

```text
  not evaluated. Theorem 4 (i) concerns glued data that agree with g_λ's on a ball; settling of g_λ's own continuation
  is not shown. Evaluating λ1 and δ would need every constant of the write-out made explicit, and several come from
```

Block 1, new:

```text
  not evaluated. Theorem 4 (i) concerns glued data that agree with g_λ's on a ball. That the development of g_λ's own
  data settles, with no gluing, is proved in a data class wider than (ii)'s by half-integer orders (Beyond the
  boundary, below), conditional on supplement section 11.1, which is proved (D632, D633). Evaluating λ1 and δ would
  need every constant of the write-out made explicit, and several come from
```

Block 2, in "Beyond the boundary", old:

```text
  6.3, deduced). It is not shown that Theorem 4 applies to g_λ's own data: g_λ is given on Ω, which does not contain the
  whole initial slice, and continuing it to spatial infinity asks for a scattering problem from past null infinity and an
  expansion of its solution at spatial infinity. Parts of that are done (deduced, with exact computations, all under
  `docket68/n1star/`): the leading Coulomb part carried to spatial infinity with no logarithm (`checks/coulomb5.py`, and
  under the full operator `checks/coulombL5.py`), the map from data on the initial null hypersurface to the leading
  coefficient at spatial infinity, under the write-out's full operator on Minkowski space, bounded uniformly in the
  harmonic (reduced for every harmonic, `checks/harmonics5.py`; bounded, `checks/uniform5.py`), the remainder's sources,
  supported where v is bounded along the initial null hypersurface, entering one order later at every harmonic computed
  (l ≤ 12) (`checks/sources5.py`, `checks/stripfull5.py`), and the approximant's stage profiles expanded in powers of
  r^(−1/2) at past null infinity, with the closure properties of that expansion shown (deduced, with an exact check,
  `checks/closure5.py`). The scattering estimate itself is not done. Below the inner boundary the theorems are not
```

Block 2, new:

```text
  6.3, deduced). It is proved, with no gluing, that Theorem 4 applies to g_λ's own data in a data class wider than
  (ii)'s by half-integer orders (supplement `docket68/n1star/SETTLE-GLAM5.md`, rounds 1–9, Theorem R5.1), conditional
  on the write-out's Parts III, IV, VII and VIII, proved; on Theorem P, proved; and on supplement section 11.1, proved
  (D632, D633), whose Lemma 11.0 repair (SETTLE-GLAM5.md R6-D) has been read by a confirming reader (D632). BEYOND5
  Lemma 6.4 (iv) is written out in full there (Lemma R9.1, every inequality computed) and read. After the shell
  g_λ − g_b0 has at past null infinity an r^(−5/2) coefficient, O(λ^∞), which for a C_c^∞ envelope and every amplitude
  but at most one is nonzero off a discrete set of λ (deduced, SETTLE-GLAM5.md Proposition 3.1; computed for a bump
  envelope, `docket68/n1star/checks/tail5.py`); it puts an r^(−5/2) term into g_λ's data at spatial infinity, outside
  the integer orders of (ii)'s class. With the orders r^(−2), r^(−5/2), r^(−3), … below r^(−ℓ0) admitted in the metric
  (ℓ0 ∈ (3, 4), ℓ0 ≠ 7/2, and one order more in the second fundamental form), Hintz's construction runs with the same
  index sets for its iterates and finitely many more derivatives lost; its threshold ε, and with it λ1 and δ, change
  and are not evaluated, in either class. g_λ continues to the past domain of dependence of the far part of Hintz's
  initial surface as a vacuum metric in the record's wave-map gauge, by one weighted energy estimate at a weight a ∈
  (ℓ0 − 1, 3), run on bounded domains of dependence, after its self-similar terms through r^(−4) are subtracted; it is
  the only continuation in that gauge near Tangherlini whose commuted energies of weight a0 ∈ (0, ½) stay bounded, its
  energy vanishing toward past null infinity, and its data lie in the widened class with small norm. So for every
  0 < λ ≤ λ2, λ2 not evaluated, with no exceptional set, the maximal vacuum development of g_λ's own data on Hintz's
  initial surface settles to five-dimensional Tangherlini of a mass m′ with |m′ − μ_end| < ε_m at Theorem 4's rate
  (proved, with the conditions above). Computed, all under `docket68/n1star/checks/`: the operator identities, on the
  write-out's full operator; the far part's past domain of dependence, the place of its inner null boundary in the
  record's domains and that boundary's displacement under g_λ, small with λ (`r9beyond5.py`); the coefficient decays
  and the residuals' degrees, measured on that operator (`r5op5.py`, and `r6sigma5.py`, which also builds the r^(−4)
  term there for one example, the general case being deduced); the caps and the null-hypersurface tails, measured on
  explicit fields; the weight window, computed from those measured exponents and from exponents counted by hand (those
  of the data class, of the pointwise bound, and of two further thresholds, which do not bind); the remaining kernel
  exponents, counted by hand with their integrability checked. Below the inner boundary the theorems are not
```

Block 3 (section 8.1, for consistency with blocks 1-2), old:

```text
replaced by a gluing (section 8.7), and Theorem 4 is not shown to apply to g_λ's own data.
```

Block 3, new:

```text
replaced by a gluing (section 8.7); that Theorem 4 applies to g_λ's own data, with no gluing, in a class wider by
half-integer orders, is proved in section 9 (Beyond the boundary), conditional on the supplement's section 11.1, proved.
```

Ledger (round 9). New: `r9beyond5.py` (@@N_B@@ checks) and `r9text5.py` (@@N_T@@). Changed and rerun: `r7settle5.py`
(@@N_K@@ checks), `r6edits5.py` (@@N_E@@). Every new or changed `.out` is from a full run and byte-identical on a second
run; the other programs are unchanged and their `.out` files stand (@@OTHERS@@); r5edits5, which reads R5-D and imports
r6edits5, was rerun after this round's last edit of the file: its `.out` unchanged. Deduced: Lemma R9.1. READ:
PART-VII-ASSEMBLY.md 123-129, 150-159, 162-163, 177 (Lemma 1.2's proof, the radiation field after the shell, Sigma_IVP's
form); N1STAR-PROOF.md 0.1, (1.1), (9.1), Lemma 9.1 (c), Theorem P (P-i)-(P-v), at md5 @@PROOFMD5@@ (5043cedf at D632;
D633's edits since are to status lines); N1STAR-LOG.md D632; BEYOND5.md 177-212 (md5 b67a56b2, not edited);
RESPONSE-HL-5D.md (md5 @@PAPERMD5@@); git 54c8634's SETTLE-GLAM5.md. None from outside sources.

Open in the theorem: nothing beyond its status (the readings named above). Not evaluated: lam_2, eps, delta, lam_1.

    python3 checks/r9beyond5.py   (@@T_B@@)
    python3 checks/r9text5.py     (@@T_T@@)
    python3 checks/r7settle5.py   (@@T_K@@)
    python3 checks/r6edits5.py    (@@T_E@@)

The times are wall-clock on this machine under the load of the other workstreams.
