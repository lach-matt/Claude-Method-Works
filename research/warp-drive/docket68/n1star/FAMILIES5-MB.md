# FAMILIES5-MB -- the sign of the charge on seeds that perturb the metric: M_b decided

Status (2026-11-06, workstream C, the missing input M_b of FAMILIES5-R6.md section 1.5). This note settles M_b, both
ways: it fails on every vacuum band that meets the black-hole region and holds on every vacuum band outside the horizon.
It does not edit the paper, N1STAR-PROOF.md, FAMILIES5-R6.md or any proof5 Part; its proposed text for the paper is in
section 7. Program: `checks/mbsign5.py` (E1-E9, seven controls), its full run in `checks/mbsign5.out` (all PASS). [R8:
"its default run"; this note's round-8 review by an independent verifier is seated in bracketed [R8] notes
(FAMILIES5-R8.md R8.9), the old text kept.] [R10 (Major 1 of the round-8 confirming reader): "the black-hole region" and
"outside the horizon" in this note's summaries say more than the theorems. Theorem X needs a band meeting {f < 0},
inside the apparent horizon R² = μ; Theorem P needs a band in {f > 0}. The black-hole region (inside the event horizon)
also contains bands with √μ3 < R < R_EH, where f > 0 and Theorem P gives E > 0: there no such data exist at second
order. Read every "meets the black-hole region" as "meets {f < 0}", every "outside the horizon" as "where f > 0", and
"every perturbation" as "every invariant (class) perturbation", the class of Theorem P. The event horizon's location is
not computed in the record and nothing uses it. FAMILIES5-R10.md.] [R11 (nit 4): that bands with √μ3 < R < R_EH exist is
deduced -- on Σ_τ0 the point R = √μ3 = 0.9067 lies in region III, its outgoing ray is marginal (R_v = 0) until the
ingoing shell arrives, where A > 0 makes e^(−2s)R_v strictly decrease, so the ray ends trapped and, A ≥ 0, stays
trapped; trappedness after the shell is open in the starting radius, so nearby rays with f > 0 at the start are trapped
too -- and computed on the computed background, `checks/ehband5.py` H1: every row crossing Σ_τ0 between √μ3 and R_x =
1.000 (n = 80 and 160) ends trapped, every row above 1.005 does not; control, no ingoing shell: none is trapped.
FAMILIES5-R11.md.] [R11-nits: "ends trapped, so it lies in the black-hole region" is the standard result that a trapped
surface lies inside the black-hole region of a strongly asymptotically predictable spacetime satisfying the null
convergence condition: Wald, General Relativity (1984), Proposition 12.2.2; Hawking and Ellis, The Large Scale Structure
of Space-Time (1973), Proposition 9.2.1. Not READ at source: neither book is reachable from this container; it is cited
as Wald's Proposition 12.2.2 in arXiv:1909.02001 and in doi:10.1007/s10714-024-03245-5, Appendix A. Its proof uses only
the Raychaudhuri equation for the null congruence orthogonal to the surface and the causal structure of J⁻(I⁺), so it
holds in five dimensions; vacuum and null dust satisfy the null convergence condition (R_ab k^a k^b = 8π ρ (l·k)² ≥ 0
for dust T = ρ l l). In this SO(4)-symmetric class the direct argument also suffices: e^(−2s)R_v never increases, so R
decreases along the trapped outgoing ray for good, it cannot reach I⁺, and no future causal curve from its start does
(deduced).]

**The quantity whose sign is decided.** With the record's constraint map (H = R + (tr K)² − |K|², M_i = D_jK^j_i −
D_i tr K, K = ½ L_n γ, n the future unit normal; bandconst5) and its KID (N_s, 2Y_s), ξ = N_s n + Y_s the static
Killing field, the pairing is N_s H + 2Y_s·M = 2G(ξ, n) (qsign5 Q5 (b)). For a compactly supported invariant
linearised vacuum seed δ in a vacuum band U,

    Q(δ) := ½ ∫_U (N_s D²H + 2Y_s·D²M)[δ, δ] dvol = 2 ∫_U G^(2)[δ](ξ, n) dvol =: −E(δ),

G^(2)[δ] the ε² coefficient of the Einstein tensor of g + εh, h a linearised vacuum solution with data δ (the second
equality is Lemma TR (1)). Q is Proposition L′'s coefficient (FAMILIES5-VLASOV section 4: the KID's coefficient is
ε²Q(δ) + O(ε³) [R8 (nit): with this Q the matter balance of FAMILIES5-R7 R7.2 reads ε²Q/2 + O(ε³) = ∫T(ξ, n), the factor
2 being the pairing's 2G(ξ, n); the two normalisations agree]), the quantity Theorem Q's dichotomy needs; M_b reads
Q(δ) < 0 (E(δ) > 0) for every non-gauge δ. This note decides the sign of Q; E is only −Q. **No identification of E with
the Hollands–Wald canonical energy is used or claimed** (it is standard, not READ here). What is computed instead is the
identification the proof needs: in the tensor sector, on every slice, E is 2|T|² times the flux of the conserved current
of the tensor master field (E2); in the scalar sector, on a static slice, E is Kodama and Ishibashi's master energy (E6,
E9). [This is the definition the verifier of FAMILIES5-R6 proposed (finding m2): R6 section 1.5's parenthetical "the
second-order quantity ∫G^(2)(ξ, n)", read literally, gives Q = +2E.]

**Verdict.**

1. **M_b fails on every vacuum band that meets the black-hole region (Theorem X).** [R10 (Major 1): every vacuum band
   meeting {f < 0}; the status note above.] Inside the horizon ξ is spacelike and Q takes both signs on seeds of tensor
   type. On every class slice the tensor sector's charge is Q = −2|T|² ∫ T_m(ξ, n) dℓ, T_m the flux of the tensor master
   field's conserved current (computed, E2 [R8 (minor 1): at three slice points; on every slice exactly in
   `checks/mbslice5.py` (R9, R10), section 2's note]); with the normal derivative P = −(Y_s^R/N_s) ∂_R H it is Q = −|T|²
   ∫ (R³ f H′² + (k_T² + 2) R H²) dR on every slice, positive for radially oscillating H where f < 0 (computed exactly
   on Part I's seed region, E3). **Exactly localised vacuum data with a non-gauge first-order part therefore exist on
   every vacuum band of Part I's slice that meets {f < 0}** (deduced: Proposition L′'s intermediate-value clause on a
   family of tensor seeds on which Q changes sign). [R8 (Major 1): as Theorem X (b) states, these are data near Part
   I's, background + εδ + O(ε²), for small amplitude ε; item 2's non-existence is likewise a statement at second order,
   for small amplitude, about such families.]
2. **M_b holds on every vacuum band outside the horizon (Theorem P).** [R10 (Major 1): every vacuum band in {f > 0}, for
   invariant perturbations.] For every compactly supported invariant linearised vacuum seed δ supported in {f > 0}, Q(δ)
   ≤ 0, with equality only for gauge seeds. In the class, E is the sum, over the class's harmonics (scalar l = 2, 4, …;
   tensor l = 2, 4, …; l = 0 contributes nothing), of master energies with positive potentials: the scalar ones
   Kodama–Ishibashi's, potential V_S = f Qp/(16R²H_KI²) with Qp > 0 on the whole exterior for every class mode (the
   reduction computed, E4-E6, E9; the positivity certified, E7 [R8 (nit): computed exactly, not certified -- E7 is exact
   algebra; it now also covers every l ≥ 2]), the tensor ones manifestly positive (E2). The passage from Part I's slice
   to a static slice is deduced (Lemma TR). **So on exterior bands no exactly localised vacuum data background + εδ +
   O(ε²) with δ non-gauge exist**, and a smooth family of exactly localised data there agrees to every order in ε with a
   re-slicing of the background (deduced, section 5). [R10 (nit): with section 5's qualifier -- only where each order's
   re-slicing generator can be chosen with the allowed support.]
3. **No third-order question arises.** Q = 0 on a non-gauge seed occurs only inside the horizon (the zero of the family
   in item 1), where existence is already decided by the sign change; outside, Q = 0 only on gauge seeds.
4. **For the paper's "More families" bullet:** exact compact support of vacuum data — **yes** on bands meeting the
   black-hole region (Theorem X), **no** at second order on bands outside the horizon (Theorem P with Proposition L′).
   The replacement sentence is in section 7. [R8 (Major 1): superseded; the single M_b paper text, rebased onto
   FAMILIES5-R7 R7.6 with its qualifiers, is in FAMILIES5-R8.md R8.8.]

Labels: **computed** (a check of `checks/mbsign5.py`, exact, each with a control it must reject [R8 (minor 4): true
since R8 -- E4, E8 and E9 had none and now have one each]), **deduced** (argued here; the standard facts used are
named), **READ** (as quoted in the record). Nothing here is reduced to an unproved input; what is not claimed is listed
in section 5.

---

## 0. The setting

- *Vacuum regions.* Every vacuum region of Part I's spacetime is Tangherlini, g = −f dv² + 2 dv dR + R² dΩ₃², f = 1 −
  μ/R², with v = ∫e^(ψ_P) dv̂ (Part I's chart, ψ_P = ψ_P(v̂); qsign5 Q2), and Part I's slice is there the round slice v
  = V(R), w := V′ = e^(ψ_P(τ0 + R)) > 0, γ_RR = w(2 − f w) > 0. ξ = ∂_v. Inside the horizon (the seed region R < R_h =
  0.9067, μ0 = 0.8221; the slice's inner edge 0.683; qsign5 Q3 [R8 (nit): the inner edge 0.683 is FAMILIES5-VLASOV
  section 3's (racglobal5); the horizon and μ0 are qsign5 Q3's]) ξ is spacelike.
- *The class* (FAMILIES5-R6 section 1.1): T² × Z2 × Z2-invariant data on a band U = {R1 < R < R2} of a vacuum region,
  compactly supported in U.
- *Gauge seeds* (R6 section 1.5): the data of L_Z g with Z compactly supported near the band (or equal on the inner
  side to a constant multiple of ξ). Their charge is 0. On a slice with K0 = 0 they are (L_X γ, D²ψ − ψ Ric), X the
  tangential part of Z, ψ its normal part (E4 (b)).

## 1. The class harmonics (computed E1; the scalar part the record's GAUGEDECAY5 Lemma 1.2)

**Lemma H.** (a) Class functions on S³ are the expansions in P_j(cos 2θ), Δ = −l(l + 2), l = 2j. (b) Class 1-forms
are exact (no vector type; the record's Lemma 1.2 (c)). (c) For each n ≥ 0 the tensor

    T_n = A dθ² + B sin²θ dφ1² + C cos²θ dφ2²,   A = C_n^(3/2)(u), u = cos 2θ,
    B = (3u − 1) A/2 − (1 − u²) ∂_u A,   C = −A − B,

is trace-free, divergence-free, regular at both axes and satisfies (Δ + k_T²)T_n = 0, k_T² = l(l + 2) − 2, l = 2n +
2. The divergence condition determines B from A, so the class TT tensors are the L² span of these, one for each even
l ≥ 2; |T|² := ∫(A² + B² + C²) sin θ cos θ dθ = 3/2, 15/2, 21, 45 for l = 2, 4, 6, 8. (d) A class symmetric 2-tensor
on S³ is the orthogonal sum of a trace part, a scalar-derived trace-free part (D̂D̂ − ⅓γ̂Δ̂)τ and a TT part (the
record's Lemma 1.2 (b)-(c)).

*Proof.* (a), (b), (d): the record. (c) computed E1 for n = 0, …, 3, exact (the trigonometric identities by the
Weierstrass substitution): trace-free, divergence-free, all three components of the eigen-equation, A = B at θ = 0
and A = C at θ = π/2 (with A − B a polynomial in u, divisible by 1 − u = 2 sin²θ, the regularity of a tensor in the
polar plane), and the divergence condition solved uniquely for B. All n (deduced): the θθ component of the eigen-
equation is the Gegenbauer equation 4(1 − u²)A_uu − 16uA_u + (k_T² − 6)A = 0, whose solutions regular at u = ±1 are
the C_n^(3/2) at k_T² − 6 = 4n(n + 3); the rough Laplacian of S³ (constant curvature) maps TT tensors to TT tensors
and preserves the class, so Δ̂T_n + k_T²T_n is a class TT tensor whose A-component vanishes, hence zero by the
uniqueness of B. Control (E1): B with the derivative term's sign reversed is not divergence-free (rejected). ∎

Orthogonality between harmonics of different type or different l, in every quadratic form below, is Schur's lemma
for SO(4) (the background is round; scalar harmonics of level l span the irreducible (l/2, l/2), TT tensors of level
l span ((l + 2)/2, (l − 2)/2) ⊕ its conjugate), or integration by parts on S³ (deduced).

## 2. The tensor sector on every slice (Theorem T; computed E2)

**Theorem T.** On every class slice v = V(R) of Tangherlini (any w = V′ > 0 with fw < 2, inside the horizon as well
as outside; Part I's vacuum slices are these), let δγ = 2R²H(R) T, δK = (R² P(R) + 2R n^R H) T, T a class TT harmonic
of level l (P = n(H) is the normal derivative of the tensor field h = 2R²H T). Then:
(i) the linearised constraints vanish identically;
(ii) N_s √γ_RR = 1 and N_s² − γ_RR (Y_s^R)² = f;
(iii) Q(δ) = −2|T|² ∫ T_m(ξ, n) √γ_RR dR, with

    T_m(ξ, n) = R³ (ξ(H) P − ½ g(ξ, n)|dH|²) − ½ g(ξ, n)(k_T² + 2) R H²,  ξ(H) = N_s P + Y_s^R H_R,  g(ξ, n) = −N_s,

the flux through the slice of J^a = T^a_b ξ^b, T_ab = R³(∂_aH ∂_bH − ½g_ab|dH|²) − ½g_ab(k_T² + 2)RH², whose
divergence is ξ(H) times the tensor equation D_a(R³D^aH) − (k_T² + 2)RH (the condition that h is a linearised vacuum
solution: the record's static5 S1, gmodes5 G1);
(iv) T_m's quadratic form in (P, H_R) is R³ [[N/2, Y/2], [Y/2, N/(2γ_RR)]], determinant R⁶ f/(4γ_RR): positive definite
exactly where f > 0.

*Proof.* Computed E2. The slice quantities (n, K0, N_s, Y_s) are derived from the embedding, symbolic in w(R) and μ,
with the unit, future, normal and decomposition checks; (i) holds identically for a generic class A; (iii): the
θ-integrated Q-density from the record's constraint map plus 2|T|²T_m√γ_RR has zero Euler operator in H and in P, for l
= 2 and l = 4 (angular integrals exact; the Euler coefficients exact at three rational slice points, two outside the
horizon and one inside, every jet of w free and √(w(2 − fw)) rational there, w = 2/(f + q²)); the current's divergence
identity exact and symbolic; (ii), (iv) exact and symbolic. Control: |T|² replaced by |T|²/2 (rejected, l = 2 and 4). ∎
[R8 (minor 1): what E2 and E3 (a)-(b) compute is exact at three rational slice points -- R, μ, w and every jet of w
fixed there, the H and P jets free -- a spot check in the slice; "every jet of w free" above means chosen
arbitrarily (as rationals) at each point. [R9, R10] On every class slice and every μ, (iii) and Lemma X1 are
computed in the record, exactly, for l = 2, 4, 6 and 8 (`checks/mbslice5.py` S1, S2): every slice with w > 0 and
fw < 2 is w = 2/(f + q²), √γ_RR = 2q/(f + q²), with q = √(2/w − f) > 0 a free function; every slice quantity is a
polynomial in (R, μ, q, q′, …) over R^a q^b S^c, S = R² − μ + R²q²; the Euler operators of (iii), and Lemma X1's two
identities, are the zero polynomial; and the θ-integrated density over |T|² at l = 6 and 8 is the affine interpolant
in k_T² of l = 2 and 4, exactly. Every l beyond 8 is the minor-8 deduction (deduced). Controls rejected: |T|²
halved, K_RR's w′ term dropped, k_T² + 3 in place of k_T² + 2, R³P² doubled. The round-8 verifier's symbolic check,
by the same parametrisation, agrees.] [R8
(minor 8): *every l (deduced).* The Q-density of the tensor data is quadratic in T, at most linear in second angular
derivatives of δγ (the scalar curvature is linear in second derivatives) and first order in those of δK. Integrated over
S³ with T trace-free, divergence-free and Δ̂T = −k_T²T, every term reduces, by integration by parts, to a radial
coefficient times ∫T·T = |T|² or ∫D̂T·D̂T = k_T²|T|² (the curvature terms of the round S³ give multiples of |T|²). So
the θ-integrated density is |T|² times a quantity affine in k_T², and so is 2|T|²T_m√γ_RR. Their difference is affine in
k_T² for fixed (H, P) and has zero Euler operator at k_T² = 6 and 22 (l = 2, 4; E2), hence for every k_T², every l.]

So in the tensor sector E = 2|T|² ∫T_m(ξ, n), on Part I's slice itself: positive on every nonzero tensor seed
supported where f > 0, indefinite where f < 0.

## 3. Inside the horizon: M_b fails (Theorem X)

**Lemma X1 (computed E3).** On every class slice the tensor seeds with P = −(Y_s^R/N_s) H_R have

    Q = −|T|² ∫ (R³ f H_R² + (k_T² + 2) R H²) dR,                                                              (X1)

independently of w, and for H = 0 the θ-integrated Q-density is −|T|²R³P² pointwise, so Q < 0. *Computed:* both from
Theorem T (E3 (a)). With l = 2 (|T|² = 3/2, k_T² = 6), [R1, R2] = [0.72, 0.89] and H = (R − R1)²(R2 − R)², Q is
affine in μ, Q = 9.43779 × 10⁻⁸ μ − 6.36595 × 10⁻⁸, and Q = 1.18429 × 10⁻⁸ at μ = 0.80, 1.56180 × 10⁻⁸ at μ = 0.84
(exact rationals in the run): **Q > 0 for every μ ∈ [0.80, 0.84]**, an interval containing Part I's μ0 = 0.8221.
R2² = 0.7921 < 0.80 puts the band inside the horizon for every such μ, and 0.72 > 0.683 inside Part I's seed region.
The momentum-only seed P = (R − R1)²(R2 − R)², H = 0 has Q = −1.4774 × 10⁻¹⁰. Control: the same construction on
[0.92, 1.09], outside the horizon for every μ in the interval (0.92² > 0.84), gives Q = −2.787 × 10⁻⁸ and −2.315 ×
10⁻⁸: no E < 0 seed (rejected).

For any band in {f < 0} and any l, H_ω = β(R) sin(ωR), β a bump, gives by (X1) Q(H_ω) = ½|T|²ω² ∫R³|f|β² dR + O(ω)
> 0 for ω large (deduced, Riemann–Lebesgue). The polynomial H is C¹ with compact support; Q is continuous on H¹_0 ×
L² in (H, P), so smooth compactly supported seeds with Q > 0 follow by approximation (deduced).

**Theorem X.** Let U be a vacuum band of Part I's slice meeting {f < 0}. Then (a) there are invariant, compactly
supported, non-gauge linearised vacuum seeds in U with Q > 0 (E < 0) and with Q < 0; (b) for every small ε > 0 there
are exact vacuum constraint data on Part I's slice, invariant, equal to Part I's outside a compact subset of U, of the
form background + εδ_(s(ε)) + c(ε), c = O(ε²), with δ_(s(ε)) a non-gauge seed.

*Proof.* (a) Lemma X1 on a sub-band of U ∩ {f < 0}. Tensor seeds are not gauge: the angular part of a gauge seed is
built from scalars (2fK0 ∝ γ̂; L_Xγ and L_XK0 from X^R and the exact X^θ; D²f and the curvature terms from scalars and
γ̂), so its TT projection vanishes (Lemma H (d)). (b) Let δ_s = (sH, −s(Y_s^R/N_s)H_R + (1 − s)P0), s ∈ [0, 1], with H
of Lemma X1 (smoothed) and P0 a bump: every δ_s is a nonzero tensor seed, hence not gauge, and Q(δ_s) is a quadratic
polynomial in s with Q(δ_0) < 0 < Q(δ_1). Proposition L′ (FAMILIES5-VLASOV section 4, from [CS06] Theorem 2 and [CD03]
Theorem 5.6, READ in the record) gives c(ε, s) supported in U with KID coefficient m(ε, s) = ε²Q(δ_s) + O(ε³) uniformly
in s and continuous in s; m(ε, 0) < 0 < m(ε, 1) for ε small, so m(ε, s(ε)) = 0 for some s(ε). ∎ This is R6 section 1.5
(i) with the configuration seed and the momentum seed both taken of tensor type, so non-gauge-ness needs no band-by-band
argument. [R8 (the verifier's reading): Q(δ_s) is a quadratic in s with Q(δ_0) < 0 < Q(δ_1), so it has exactly one root
s* in (0, 1), a simple one; hence s(ε) = s* + O(ε) and the data are background + εδ_(s*) + O(ε²), with first-order part
the nonzero tensor seed δ_(s*).]

Inside the horizon Q is a momentum, and an outgoing tensor packet carries it with the sign opposite to the momentum
seeds' — as R6 section 1.5 anticipated and as Theorem Q′ (ii) found for outgoing null dust. Seeds localised in angle as
well exist (deduced): a class TT field with A(R, θ) compactly supported and B, C determined pointwise by A (Lemma H
(c)) solves the linearised constraints, and (X1) holds mode by mode.

## 4. Outside the horizon: M_b holds (Theorem P)

### 4.1 From Part I's slice to a static slice (Lemma TR; deduced)

**Lemma TR.** Let δ be a compactly supported invariant linearised vacuum seed in a band U ⊂ {f > 0} of Part I's slice
(extended by zero to a spacelike round slice of the Tangherlini spacetime M_μ of U's region), and h the linearised
vacuum solution with data δ in a harmonic gauge with compactly supported gauge data, so supp h ⊂ J(K), K = supp δ.
Then for a suitable static slice {t = t1}, h's data there are compactly supported in the exterior, and Q(δ) =
Q_static(h|_{t=t1}); δ is gauge iff h|_{t=t1} is.

*Proof.* (1) *Q is a flux.* For g_ε = g + εh, H(γ_ε, K_ε) = 2G_ε(n_ε, n_ε), M_i(γ_ε, K_ε) = G_ε(n_ε, e_i), and ξ = N_ε
n_ε + Y_ε, so N_sH + 2Y_s·M = 2G_ε(ξ, n_ε) + (N_s − N_ε)H + 2(Y_s − Y_ε)·M; the last two terms are O(ε³) since G_ε =
O(ε²) (G = 0, G^(1)[h] = 0). The ε² coefficient of Φ(γ_ε, K_ε) is ½D²Φ[δ, δ] + DΦ(0, K2), K2 the second-order part of
K_ε (compactly supported), which pairs to 0 with the KID. So Q(δ) = 2∫_Σ G^(2)[h](ξ, n). (2) *Conservation.* Expanding
∇^(ε)_a G_ε^ab = 0 at second order with G^(1)[h] = 0 gives ∇_a G^(2)ab = 0, so J^a := G^(2)ab ξ_b has ∇_a J^a = G^(2)ab
∇_(a ξ_b) = 0. (3) *The slice.* In Kruskal coordinates (U, V) of region I (both future-increasing) the slice is a curve
along which U decreases and V increases with R; K lies in U ∈ [U(R2), U(R1)], V ∈ [V(R1), V(R2)]; J⁺(K) ⊂ {U ≥ U(R2), V
≥ V(R1)} and J⁻(K) ⊂ {U ≤ U(R1), V ≤ V(R2)} (causal curves project to causal curves of the orbit space). The rectangles
S_in = {U(R1) < U < 0, 0 < V < V(R1)} and S_out = {U < U(R2), V > V(R2)} meet neither. A static slice is a ray V = c|U|.
Take R_a < R1 on the slice and c ∈ (V(R_a)/|U(R1)|, V(R1)/|U(R1)|): the ray then meets S_in at a point U_s slightly
above U(R1) with c|U_s| ∈ (V(R_a), V(R1)), and S_out at every U_s′ with |U_s′| > max(|U(R2)|, V(R2)/c); take R_b on the
slice with |U(R_b)| > |U_s′|, V(R_b) > c|U_s′|. Let Σ′ be the slice up to R_a, the segment to (U_s, c|U_s|) (in S_in,
ΔU < 0 < ΔV: spacelike), the ray to U_s′, the segment to the slice at R_b (in S_out, spacelike), and the slice beyond.
Σ′ is a spacelike curve equal to the slice outside a compact set, so by (2) and Stokes its J-flux is Q(δ); h vanishes on
the two segments, and J(K) meets the ray only in |U| ∈ [min(|U(R1)|, V(R1)/c), max(|U(R2)|, V(R2)/c)], inside the ray's
segment; near the bifurcation sphere (U, V → 0) and in region III the static slice is outside J(K). So the flux is that
through the whole static slice, which is Q_static of h's data there by (1). Uniqueness up to gauge gives the last
clause. ∎ [R8 (minor 5): two points of wording. Σ is extended to a Cauchy surface of the maximally extended M_μ, so that
h exists on D(Σ), which contains the static slice. And R1, R2 in (3) are the radial extent of supp δ, not U's edges, and
R_a is taken in (R_h, R1) on the slice: if U's inner edge were R_h itself, "R_a < R1" with R1 = R_h would put R_a
outside S_in.] *Standard facts used:* existence, uniqueness up to gauge and finite propagation for the linearised vacuum
equations in harmonic gauge; Stokes' theorem. *Computational support:* in the tensor sector Theorem T gives Q as the
flux of a conserved current on every slice of the family directly; in the scalar sector E9 identifies Q on static slices
with the conserved master energy.

### 4.2 The static slice

On γ = dR²/f + R² dΩ₃², N = √f, K0 = 0, Y = 0: D²H[(h, k), (h, k)] = D²R[h, h] + 2((tr k)² − |k|²), the mixed terms
vanishing at K0 = 0, and the linearised constraints decouple into DR[h] = 0 and D^i(k_ij − tr k γ_ij) = 0. So

    E = E_V(h) + E_K(k),   E_V := −½ ∫ N D²R[h, h] dvol,   E_K := ∫ N (|k|² − (tr k)²) dvol.

**Lemma G (gauge invariance; deduced, its identities computed E4 (c)).** E_V(h + L_Xγ) = E_V(h) when DR[h] = 0, and
E_K(k + k_ψ) = E_K(k) when M[k] = 0, k_ψ := D²ψ − ψ Ric, for X, ψ of compact support. *Proof.* From R(φ*γ) =
φ*R(γ): DR[L_Xγ] = X(R) = 0 and D²R[h, L_Xγ] = X(DR[h]) − DR[L_Xh]; so the cross term is −∫N X(DR[h]) + ∫N
DR[L_Xh] = ∫div(NX)DR[h] + ∫⟨(DR)*N, L_Xh⟩ = 0, using DR[h] = 0 and (DR)*N = D²N − ΔN γ − N Ric = 0 (static vacuum);
the quadratic term vanishes the same way. For E_K: the bilinear form is B(k, k_ψ) = ∫ψ Euler_ψ[N(⟨k, k_ψ⟩ − tr k tr
k_ψ)dvol], and Euler_ψ[…] = √γ(2dN·M[k] + N div M[k]) = 0 when M[k] = 0; and M[k_ψ] = 0, so B(k_ψ, k_ψ) = 0.
*Computed* (mode-free, class fields of (R, θ), exact at three rational points (R, θ, μ) with every jet free): DR[L_Xγ]
= 0; the Euler operator of N DR[h]√γ vanishes in all five class components of h; M[k_ψ] = 0; the Euler identity for
B. ∎

### 4.3 Modes, gauge-fixing and the free functions (computed E4 (a), (b))

A class seed on the static slice is a sum of scalar modes (h_RR = aS, h_Rθ = R b S′, h_ij = R²(c S γ̂ + e Ŝ), Ŝ :=
D̂D̂S + (k²/3)γ̂S, S = P_j(cos 2θ), k² = l(l + 2); k likewise with (p, q, w, z)), tensor modes and an l = 0 part, and
E_V, E_K and the constraints split mode by mode (Lemma H (d), orthogonality). The spatial gauge X = αS∂_R + βS′∂_θ shifts
(a, b, c, e) by ((1/f)′α + 2α′/f, α/(Rf) + Rβ′, 2α/R − (2k²/3)β, 2β) (computed), so β = −e/2, α = −Rf(b − Re′/2)
reach b = e = 0 (the record's Regge–Wheeler-type gauge, GAUGEDECAY5 Lemma 1.3, on the slice), and

    A := a + (1/f)′α + 2α′/f,    F := c/2 − f b + k² e/6 + f R e′/2

are invariant (computed); the lapse direction k_ψ (ψ → ψS) has trace-free angular part ψ Ŝ^TF (computed), so ψ =
−R²z reaches z = 0. Both gauges are local in R, so compactly supported. In this gauge every density is a radial
coefficient times S, S′, S² or S′², free of θ (computed at three rational angles), and per ∫S² sin θ cos θ dθ (using
∫S′² sin θ cos θ dθ = k² ∫S² sin θ cos θ dθ) the radial Hamiltonian constraint C(A, F), momentum constraints M_R(p, q,
w), M_θ(p, q, w) and energies E_V(A, F), E_K(p, q, w) are explicit rational expressions in (R, μ, k²) (written in the
program; e.g. E_K = 2k²R³f q² − 6R³w² − 6R³f w p, M_θ = (4 − 3x)q − f p + R f q′ − 2w, x := μ/R²).

### 4.4 The kinetic energy (Lemma K; computed E5)

With H_KI := m + 6μ/R², m := k² − 3, and Z := R³(w − f q):

    Z′ + (R²H_KI/3) q + R² M_θ + (R³/3) M_R = 0 identically,
    E_K = 6k² m Z²/(R³ H_KI²) + d/dR(…)   on the momentum constraint,

and Z ↦ (q, w, p) = (−3Z′/(R²H_KI), Z/R³ + f q, ((4 − 3x)q + R f q′ − 2w)/f) solves both constraints identically and is
onto (on the constraint q = −3Z′/(R²H_KI), so Z recovers the data). Control: R³w in place of Z (a lapse-gauge-variant
variable) fails the identity (rejected).

### 4.5 The potential energy (Lemma V; computed E6)

(i) E_V = E_red + R⁴F′C + d/dR, with E_red = 24R³fF′² + (14k² − 24)RF² − R²f(k² + 12f)AF′ + (k²/2)Rf²A² + 3k²RfAF,
algebraic in A. (ii) The Moncrief variable

    ℓ := A − (2R/f)F′ + (2H_KI/(3f²))F   satisfies   ℓ′ + κℓ − (2k²H_KI/(9Rf³)) F = (R/(3f²)) C,
    κ := (k² + 6 + 6x)/(3Rf),

so on the constraint F = 9Rf³(ℓ′ + κℓ)/(2k²H_KI) and A = ℓ + (2R/f)F′ − (2H_KI/(3f²))F, a map ℓ ↦ (A, F) that solves C
identically and is onto. (iii) With Φ := R^(3/2) f² ℓ/H_KI,

    E_V = (27m/(2k²)) ( f Φ′² + Qp Φ²/(16 R² H_KI²) ) + d/dR,
    Qp = 1296x³ + (624m − 144)x² + 36m(m − 12)x + 16m³ + 60m²,

i.e. (27m/(2k²)) ∫((∂_r*Φ)² + V_SΦ²) dr*, V_S = f Qp/(16R²H_KI²): Kodama and Ishibashi's scalar potential at n = 3
(the record's gmodes5 G3, READ there from [KI03] (3.1)-(3.7)); it is recomputed here from the record's constraint map,
not taken from [KI03]. The principal parts cancel (no ℓ″² term). In four dimensions the same construction gives
Moncrief's K + (f/Λ)(H2 − rK′). Controls: ℓ without its F-term fails (ii) (rejected); Φ with R^(1/2) in place of
R^(3/2) fails (iii) (rejected).

### 4.6 Positivity (computed E7, E8, E2)
Class modes have l = 2j, so m = 4j(j + 1) − 3 ∈ {5, 21, 45, …}. **Qp > 0 for x ∈ [0, 1]:** at m = 5, Qp = 1296x³ +
2976x² − 1260x + 3500, the quadratic's discriminant is −40076400 < 0, and Qp has no root in [0, 1]; for m = 21 + t, t ≥
0, every coefficient of Qp in (x, t) is ≥ 0 and Qp(0, 0) > 0. H_KI > 0, f > 0 on R > √μ, 27m/(2k²) > 0,
6k²m/(R³H_KI²) > 0. So E_V,l ≥ 0 with equality iff Φ = 0 iff ℓ = 0 iff (A, F) = 0 (by (ii)), and E_K,l ≥ 0 with equality
iff Z = 0 iff (p, q, w) = 0 (Lemma K, f > 0). Control (the wrong sign): the potential of the ℓ-form before the
S-deformation is negative near the horizon at m = 5 (sign −1 at R = 1.01, +1 at R = 3, μ = 1): positivity is not
automatic (rejected). l = 0 (E8): on the constraint E_V and E_K are d/dR's; a compactly supported l = 0 h is L_(RF∂_R)γ,
the other solution of the l = 0 constraint being the mass change A = μ/(R²f²), nowhere zero; the l = 0 k is p = (Rw′ +
w)/f [R8 (minor 4): this k is the lapse direction k_ψ = D²ψ − ψ Ric with ψ = N(c + ∫Rw/(fN) dR): w_ψ = (fN/R)(ψ/N)′ and
p_ψ = (Rw_ψ′ + w_ψ)/f (E8, computed). For compactly supported w, ψ vanishes on the outer side and equals a constant
times N on the inner side, so the l = 0 kinetic part is gauge in R6's extended sense, not compactly supported. Control:
X = F∂_R in place of RF∂_R does not solve the l = 0 constraint]. Tensor modes: Theorem T at w = 1/f (the static slice),
E_T = |T|² ∫(R³P² + R³fH′² + (k_T² + 2)RH²) dR > 0.

**The master energy (E9, computed).** On the momentum constraint the configuration map applied to h = 2Nk gives
Φ[2Nk] = +(2k²/3)√f Z/(R^(3/2)H_KI); since ∂_t h = 2Nk + L_βγ on a static slice, this is Φ_t, and E_K = (27m/(2k²))
∫Φ_t²/f dR. So on the static slice E = (27m/(2k²)) |S|² ∫(Φ_t² + (∂_r*Φ)² + V_SΦ²) dr*, the energy of the
Kodama–Ishibashi master equation, which that equation conserves.

The radial identities of E5, E6, E8, E9 are exact, symbolic in k² and the jets, at four rational points (R, μ) with R
and f rational squares (the default run, `checks/mbsign5.out`), and symbolic in R and k² at μ = 1 (the `--full` run,
`checks/mbsign5_full.out`, E4-E9 PASS; μ = 1 is general by the homothety (t, R) → (λt, λR), which carries μ to λ²μ); E4
(a) keeps μ symbolic. In development E5 was also run symbolic in R, μ and k² (PASS). [R8 (minor 2): the homothety
argument holds only for weight-homogeneous identities, which the program did not check (a non-homogeneous mutation
passed --full). --full is now fully symbolic in (R, μ, k²): μ = xR² with x a free symbol, a change of variables, so no
homogeneity is assumed; `checks/mbsign5_full.out`, E5-E9 PASS. E9 now enforces the + sign, its opposite sign a control;
E7 also proves Qp > 0 on x ∈ [0, 1] for every l ≥ 2 (m = 12 + t: every coefficient ≥ 0), so the potentials are positive
for the whole spectrum of S³, not only the class's.]

### 4.7 Theorem P

**Theorem P.** For every compactly supported invariant linearised vacuum seed δ in a vacuum band U ⊂ {f > 0} of Part
I's slice, Q(δ) ≤ 0, with equality iff δ is gauge.

*Proof.* Lemma TR moves Q to a static slice; there Q = −E_V − E_K (4.2), unchanged by the compactly supported gauges of
4.3 (Lemma G); the modes separate (orthogonality); each scalar mode has E_V,l + E_K,l ≥ 0, with equality iff its
gauge-fixed data vanish (4.4-4.6); tensor modes likewise (Theorem T); l = 0 contributes 0 and is gauge (E8). So Q ≤
0, and Q = 0 iff every mode is gauge iff δ is gauge (Lemma TR). ∎ **Status: deduced, every identity it uses computed**
(E2, E4-E9); the standard facts are those of Lemma TR, orthogonality, and the convergence of the mode sums for smooth
data.

## 5. What follows for exact compact support, and what is not claimed

- **Inside the horizon (Theorem X): yes.** On every vacuum band of Part I's slice meeting {f < 0} there are exact
  invariant vacuum data equal to Part I's outside the band, with a non-gauge (tensor-type) first-order part. With the
  outgoing null dust of R6 Theorem Q′ (ii), bands inside the horizon admit exact localisation in vacuum and with matter.
- **Outside the horizon (Theorem P with Proposition L′): no, at second order.** No data background + εδ + O(ε²) with δ
  non-gauge satisfy the vacuum constraints and equal the background outside U, for ε small. *To every order (deduced):*
  if D_ε is a family of such data smooth in ε with D_0 the background, its first nonzero order after removing a
  re-slicing is a linearised seed δ_j with Q(δ_j) = 0 (the KID coefficient at order ε^(2j)), hence gauge by Theorem P;
  re-slicing the development by its generator and repeating, D_ε agrees with a re-slicing of the background to every
  order in ε. [R8 (the verifier's section 5 gap): it is not shown that the re-slicing generators keep the allowed
  support -- compactly supported near U, or equal to a constant multiple of ξ on the inner side. The statement "to every
  order" is therefore claimed only for families whose re-slicing generator at each order can be so chosen, and is
  otherwise excluded.]
- **Not claimed.** That such an exterior family, flat at ε = 0 relative to re-slicings, is a re-slicing (no
  analyticity is used); that the interior data of Theorem X are not re-slicings at the nonlinear level beyond their
  first-order part being non-gauge; the scalar-mode formula for E in terms of Part I's own slice data (the sign is
  obtained on a static slice, to which Lemma TR transfers it exactly); any identification with the Hollands–Wald
  canonical energy.
- **The third order.** Q = 0 on a non-gauge seed happens only inside the horizon (δ_(s*) of Theorem X), where the sign
  change gives existence already; outside it happens only on gauge seeds. No question moves to third order. [R8 (minor
  6): corrected. Inside the horizon Q, an indefinite quadratic form, vanishes on a whole cone of non-gauge seeds, not
  only at δ_(s*). For such a δ0 whose bilinear form B(δ0, ·) is not identically zero, take η with B(δ0, η) ≠ 0: Q(δ0 +
  sη) = 2sB(δ0, η) + s²Q(η), and Proposition L′ on the family δ0 + sη gives m(ε, s) = ε²Q(δ0 + sη) + O(ε³) uniformly; at
  s = ±Kε, K > C/|B(δ0, η)|, m has opposite signs, so m(ε, s(ε)) = 0 with s(ε) = O(ε), and the data are background + εδ0
  + O(ε²). Only δ0 in the radical of Q (B(δ0, ·) ≡ 0) is left to third order, and is not claimed. Outside the horizon Q
  = 0 only on gauge seeds, as stated.]

## 6. Status

| item | status | support |
|---|---|---|
| Lemma H (class TT harmonics) | computed (n ≤ 3), deduced (all n) | E1 |
| Theorem T (tensor sector, every slice) | computed | E2 [R10: three points; every slice mbslice5 S1] |
| Lemma X1, the exact Q > 0 seed on Part I's seed region | computed | E3 [R10: every slice mbslice5 S2] |
| Theorem X (exact localisation inside the horizon) | deduced | E3; Proposition L′ (READ in the record) |
| [R10] Theorem T, Lemma X1 on every slice (l = 2, 4, 6, 8; every l deduced) | computed, exact | mbslice5 S1, S2 |
| Lemma TR (passage to a static slice) | deduced | Theorem T, E9 (support) |
| Lemma G (gauge invariance on the static slice) | deduced, identities computed | E4 (c); [R10] mbslice5 S4 |
| modes, gauges, invariants, radial densities | computed | E4 (a), (b); [R10, R11] mbslice5 S4 (a), (b) |
| Lemmas K, V (kinetic, potential reductions; the constraint solved) | computed | E5, E6 |
| positivity of the potentials on the class spectrum | computed | E7 |
| l = 0 | computed | E8 |
| the static-slice E is the master energy | computed | E9 |
| Theorem P (M_b outside the horizon) | deduced, every identity computed | E2, E4-E9; [R10] mbslice5 S1, S4 |
| Hollands–Wald identification | not used, not claimed | -- |

[R11 (nit 1): the table was reflowed into a paragraph by the round-10 edit and is restored here as a table; the
[R10]/[R11] entries name mbslice5's exact checks, which are for every (R, θ, μ) (S4) and every slice (S1, S2).]

Not independently read: this note. [R8: read by an independent verifier in round 8 -- M_b settled both ways, no
mathematical error in Theorem X or Theorem P, every identity re-derived symbolically; its findings are seated here as
[R8] notes.]

## 7. Proposed replacement for the M_b sentence of FAMILIES5-R6 section 8's proposed paper block

[R8 (Major 1): this section targets FAMILIES5-R6 section 8's block, which FAMILIES5-R7 superseded by R7.6, and its "New"
text drops R7.6's qualifiers ("near Part I's data", "for small amplitude", the second-order statement about families
background + εδ + O(ε²)); spliced into R6's block it would also bring back the overclaims R7.6 repaired. It is
superseded by the single M_b paper text, rebased onto R7.6's last sentence with those qualifiers and with the
potentials' positivity computed for every l ≥ 2, in FAMILIES5-R8.md R8.8. The text below is kept as it was.]

The last sentence of the bullet proposed in FAMILIES5-R6.md section 8 ("New:"); FAMILIES5-R6.md itself is not edited.
The old text is quoted with its two preceding half-lines, which stay.

Old:

```
  not exist outside the horizon, and inside it they exist with outgoing null dust (deduced; the sign computed). For
  perturbations of the metric itself the charge is the canonical energy, whose sign is not decided here: that is the one
  missing input, and nothing weaker settles exact vacuum localisation at second order.
```

New:

```
  not exist outside the horizon, and inside it they exist with outgoing null dust (deduced; the sign computed). For
  perturbations of the metric itself the charge is Q = 2 int G^(2)(xi, n) =: -E, and its sign is decided
  (`docket68/n1star/FAMILIES5-MB.md`, `checks/mbsign5.py`). Inside the horizon E takes both signs on perturbations of
  tensor type (computed exactly on the slice), so exactly localised vacuum data whose first-order part perturbs the
  metric, and is not a gauge perturbation, exist on every vacuum band of the slice that meets the black-hole region
  (deduced, by intermediate values). Outside the horizon E is positive on every perturbation that is not a gauge one:
  in the class it is the sum, over the even harmonics, of the energies of Kodama and Ishibashi's master equations,
  whose potentials are positive in five dimensions (the reduction and the positivity computed exactly, the passage to
  a static slice deduced), so on bands outside the horizon no exactly localised vacuum data with a non-gauge
  first-order part exist.
```

## Files

`FAMILIES5-MB.md` (this note); `checks/mbsign5.py` (E1-E9; controls in E1, E2, E3, E5, E6 (two), E7);
`checks/mbsign5.out`, its full run [R8 (nits): "its default run"; both runs were redone in round 8 with every change,
runtimes as printed in the .out files] (`python3 checks/mbsign5.py --selftest`: E1-E9 PASS, seven controls rejected,
about 6 minutes under load); `checks/mbsign5_full.out` (`--selftest --full --only=E5,E6,E7,E8,E9`: E4-E9 PASS with the
radial identities symbolic in R and k², about 6 minutes).
