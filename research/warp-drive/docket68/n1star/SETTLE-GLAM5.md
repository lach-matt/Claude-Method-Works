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
