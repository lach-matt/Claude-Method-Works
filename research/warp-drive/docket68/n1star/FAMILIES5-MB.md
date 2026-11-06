# FAMILIES5-MB -- the sign of the charge on configuration seeds: M_b decided

Status (2026-11-06, workstream C, the missing input M_b of FAMILIES5-R6.md section 1.5). This note settles M_b. It
does not edit the paper, N1STAR-PROOF.md, FAMILIES5-R6.md or any proof5 Part; its proposed text for the paper is in
section 7. Program: `checks/mbsign5.py` (E1-E9, with controls), its run in `checks/mbsign5.out`.

**The quantity whose sign is decided.** With the record's constraint map (H = R + (tr K)² − |K|², M_i = D_jK^j_i −
D_i tr K, K = ½ L_n γ, n the future unit normal; bandconst5) and its KID (N_s, 2Y_s), ξ = N_s n + Y_s the static
Killing field, the pairing is N_s H + 2Y_s·M = 2G(ξ, n) (qsign5 Q5 (b)). For a compactly supported invariant
linearised vacuum seed δ in a vacuum band U,

    Q(δ) := ½ ∫_U (N_s D²H + 2Y_s·D²M)[δ, δ] dvol = 2 ∫_U G^(2)[δ](ξ, n) dvol,      E(δ) := −Q(δ),

where G^(2)[δ] is the ε² coefficient of the Einstein tensor of g + εh, h any linearised vacuum solution with data δ
(section 4.1 shows the two expressions agree). Q is the coefficient of Proposition L′ (FAMILIES5-VLASOV section 4:
the KID's coefficient is ε²Q(δ) + O(ε³)), the quantity Theorem Q's dichotomy needs. M_b reads: Q(δ) < 0 (E(δ) > 0)
for every non-gauge δ. This note decides the sign of Q; E is used only as −Q. No identification of E with the
Hollands–Wald canonical energy is used or claimed (that identification is standard, not READ here). What is computed
instead is the identification that matters: in the tensor sector, on every slice, E = 2|T|² times the flux of the
conserved current of the tensor master field (E2); in the scalar sector, on a static slice, E is Kodama and Ishibashi's
master energy (E6, E9). [The verifier of FAMILIES5-R6 (finding m2) noted that R6 section 1.5's parenthetical "the
second-order quantity ∫G^(2)(ξ, n)" read literally gives Q = +2E; the definition above is the one adopted.]

**Verdict.**

1. **M_b is false as stated: it fails on every vacuum band that meets the black-hole region (Theorem X).** Inside the
   horizon ξ is spacelike and Q takes both signs on seeds of tensor type. On every class slice the tensor sector's
   charge is exactly Q = −2|T|² ∫ T_m(ξ, n) dℓ, T_m the stress of the tensor master field (computed, E2), and with the
   normal derivative chosen as P = −(Y_s^R/N_s) ∂_R H it is Q = −|T|² ∫ (R³ f H′² + (k_T² + 2) R H²) dR on every slice,
   positive for radially oscillating H where f < 0 (computed exactly on Part I's seed region, E3). **Exactly localised
   vacuum data with a non-gauge first-order part therefore exist on every vacuum band of Part I's slice that meets {f <
   0}** (deduced: Proposition L′'s intermediate-value clause along a family of tensor seeds on which Q changes sign).
2. **M_b holds on every vacuum band outside the horizon (Theorem P).** For every compactly supported invariant
   linearised vacuum seed δ supported in {f > 0}, Q(δ) ≤ 0, with equality only for gauge seeds. In the class, E is the
   sum over the class's harmonics (scalar l = 2, 4, …; tensor l = 2, 4, …) of master energies with positive potentials:
   the scalar ones are Kodama–Ishibashi's, potential f Qp/(16R²H_KI²) with Qp > 0 on the whole exterior for every
   class mode (computed exactly: the reduction E4-E6, the positivity certificate E7), the tensor ones are manifestly
   positive (E2). The passage from Part I's slice to a static slice is deduced (conservation, section 4.1). **So on
   exterior bands no exactly localised vacuum data background + εδ + O(ε²) with δ non-gauge exist**, and a smooth
   family of exactly localised data there is, to every order in ε, a re-slicing of the background (deduced, section 5).
3. **No third-order question arises.** Q = 0 on a non-gauge seed occurs only inside the horizon (at the zero of the
   family in item 1), where existence is already decided by the sign change; outside, Q = 0 only on gauge seeds.
4. **For the paper's "More families" bullet:** exact compact support — **yes** for vacuum data on bands meeting the
   black-hole region (Theorem X), **no** at second order on bands outside the horizon (Theorem P with Proposition L′).
   The replacement sentence is in section 7.

Labels: **computed** (a check of `checks/mbsign5.py`, exact unless stated, each with a control it must reject),
**deduced** (argued here; the standard facts used are named), **proved** (deduced, every identity it uses computed),
**READ** (as quoted in the record). Nothing in this note is "reduced to" an unproved input.

---

## 0. The setting

- *Vacuum regions.* Every vacuum region of Part I's spacetime is Tangherlini, g = −f dv² + 2 dv dR + R² dΩ₃², f = 1 −
  μ/R², v = ∫e^(ψ_P) dv̂ (Part I's chart, ψ_P = ψ_P(v̂), qsign5 Q2), and Part I's slice is there the round slice v =
  V(R), w := V′ = e^(ψ_P(τ0 + R)), spacelike: 0 < f w < 2. ξ = ∂_v. Inside the horizon (the seed region R < R_h =
  0.9067, μ0 = 0.8221; the slice's inner edge 0.683; qsign5 Q3) ξ is spacelike.
- *The class* (FAMILIES5-R6 section 1.1): T² × Z2 × Z2-invariant data on a band U = {R1 < R < R2} of a vacuum region,
  compactly supported in U.
- *Gauge seeds* (R6 section 1.5): the data of L_Z g, Z compactly supported near the band (or equal on the inner side to
  a constant multiple of ξ, a translation along the Killing flow). Their charge is zero. On a slice with K0 = 0 they are
  (L_X γ, D²ψ − ψ Ric), X spatial, ψ the normal displacement (E4 (b)).

## 1. The class harmonics (computed E1; the scalar part the record's GAUGEDECAY5 Lemma 1.2)

**Lemma H.** (a) Class functions on S³ are the expansions in P_j(cos 2θ), Δ = −l(l + 2), l = 2j. (b) Class 1-forms
are exact (no vector type; the record's Lemma 1.2 (c)). (c) For each n ≥ 0 the tensor

    T_n = A dθ² + B sin²θ dφ1² + C cos²θ dφ2²,  A = C_n^(3/2)(u), u = cos 2θ,  B = (3u − 1)A/2 − (1 − u²) ∂_u A,  C = −A − B,

is trace-free, divergence-free, regular at both axes and satisfies (Δ + k_T²)T_n = 0 with k_T² = l(l + 2) − 2, l =
2n + 2. The divergence condition determines B from A uniquely, so the class TT tensors are spanned by these, one for
each even l ≥ 2; |T_0|² := ∫(A² + B² + C²) sin θ cos θ dθ = 3/2. (d) A class symmetric 2-tensor on S³ is the sum of a
trace part, a scalar-derived trace-free part (D̂D̂ − ⅓γ̂Δ̂)τ and a TT part, mutually orthogonal (the record's Lemma
1.2 (b)-(c)).

*Proof.* (a), (b), (d): the record. (c): computed E1 for n = 0, …, 3 (exact), with the uniqueness of B; the general n
follows since the θθ eigen-equation is the Gegenbauer equation 4(1 − u²)A_uu − 16uA_u + (k_T² − 6)A = 0 and the
other two components follow from it and the divergence condition (E1 checks all three). Control: B with the derivative
term's sign reversed is not divergence-free (rejected). ∎

Orthogonality between harmonics of different type or different l in every quadratic form below is Schur's lemma for
SO(4) (the background is round; scalar harmonics of level l span the irreducible (l/2, l/2), TT tensors of level l
span ((l + 2)/2, (l − 2)/2) ⊕ its conjugate), or directly by integration by parts on S³ (deduced).

## 2. The tensor sector on every slice (Theorem T; computed E2)

**Theorem T.** On every class slice v = V(R) of Tangherlini (any w = V′ with 0 < fw < 2; Part I's vacuum slices are
these), let δγ = 2R²H(R) T, δK = (R² P(R) + 2R n^R H) T, T a class TT harmonic of level l. Then:
(i) the linearised constraints vanish identically;
(ii) N_s √γ_RR = 1 and N_s² − γ_RR (Y_s^R)² = f;
(iii) Q(δ) = −2|T|² ∫ T_m(ξ, n) √γ_RR dR, with

    T_m(ξ, n) = R³ (ξ(H) P − ½ g(ξ, n)|dH|²) − ½ g(ξ, n)(k_T² + 2) R H²,   ξ(H) = N_s P + Y_s^R H_R,  g(ξ, n) = −N_s,

the flux through the slice of the current T_ab ξ^b of the tensor master field, T_ab = R³(∂_aH ∂_bH − ½ g_ab |dH|²) −
½ g_ab (k_T² + 2) R H², which is conserved on solutions of the tensor equation D_a(R³ D^a H) = (k_T² + 2) R H
(ξ Killing, ξ(R) = 0);
(iv) the quadratic form of T_m in (P, H_R) is R³ [[N/2, Y/2], [Y/2, N/(2γ_RR)]] with determinant R⁶ f/(4γ_RR):
positive definite exactly where f > 0.

*Proof.* Computed E2, exact and symbolic in w(R) and μ (the square root √(w(2 − fw)) carried as a function whose
derivatives are eliminated, the identity tested in Q(R, μ, w-jets)[√] by reduction modulo its square): (i) for a
generic class A (B, C from Lemma H); (iii) the Euler operator of (θ-integrated Q-density) + 2|T|²T_m√γ_RR vanishes in
H and in P, for l = 2 and l = 4; the angular integrals exact. Control: |T|² replaced by |T|²/2 (rejected). (ii), (iv)
exact. That the tensor field h = 2R²H T is a linearised vacuum solution iff H solves the tensor equation is the
record's static5 S1 and gmodes5 G1 (computed there). ∎

So in the tensor sector E = 2|T|² ∫T_m(ξ, n): positive on every nonzero tensor seed supported where f > 0, and
indefinite where f < 0, on Part I's slice itself (no transfer to another slice is needed here).

## 3. Inside the horizon: M_b fails (Theorem X)

**Lemma X1 (computed E3).** On every class slice, the tensor seeds with P = −(Y_s^R/N_s) H_R have

    Q = −|T|² ∫ (R³ f H_R² + (k_T² + 2) R H²) dR                                                               (X1)

(independent of w), and those with H = 0 have Q = −|T|² ∫ R³ P² dR < 0. *Computed:* both from Theorem T by the Euler
test (E3 (a)). On [R1, R2] = [0.72, 0.89], with H = (R − R1)²(R2 − R)² and l = 2 (|T|² = 3/2, k_T² = 6), Q is
affine in μ and Q = 1.1843 × 10⁻⁸ at μ = 0.80 and 1.5618 × 10⁻⁸ at μ = 0.84 (exact rationals printed): Q > 0 for
every μ in [0.80, 0.84], an interval containing Part I's μ0 = 0.8221; R2² = 0.7921 < 0.80, so the band is inside the
horizon for every such μ, and 0.72 > 0.683 puts it inside Part I's seed region. Control: the same construction on
[0.92, 1.09], outside the horizon for every μ in the interval, gives Q = −2.79 × 10⁻⁸ and −2.32 × 10⁻⁸ (no E < 0
seed; rejected).

For any band [R1, R2] in {f < 0} and any l, H_ω = β(R) sin(ωR) with β a bump gives, by (X1), Q(H_ω) = ½|T|²ω² ∫R³|f|β²
dR + O(ω) > 0 for ω large (deduced, Riemann–Lebesgue). The polynomial H is C¹ with compact support; Q is continuous
on H¹_0 in (H, P), so smooth compactly supported seeds with Q > 0 are obtained by approximation (deduced).

**Theorem X.** Let U be a vacuum band of Part I's slice meeting {f < 0}. Then (a) there are invariant, compactly
supported, non-gauge linearised vacuum seeds in U with Q > 0 (E < 0) and with Q < 0; (b) there are exact vacuum
constraint data on Part I's slice, invariant, equal to Part I's outside a compact subset of U, of the form background
+ εδ_(s(ε)) + c(ε), c = O(ε²), δ_s non-gauge, for every small ε > 0.

*Proof.* (a) Lemma X1 on a sub-band of U ∩ {f < 0}; tensor seeds are non-gauge, since a gauge seed's angular parts are
built from scalars (2fK0 ∝ γ̂, L_Xγ and L_X K0 from X^R and the exact X^θ, D²f and the curvature terms from scalars and
γ̂), so its TT projection vanishes (Lemma H (d)). (b) Take δ_s = (sH, −s(Y_s^R/N_s)H_R + (1 − s)P0), s ∈ [0, 1], H and
P0 bumps in U ∩ {f < 0}: every δ_s is a nonzero tensor seed, hence non-gauge; Q(δ_s) is continuous (quadratic) in s
with Q(δ_0) < 0 < Q(δ_1). Proposition L′ (FAMILIES5-VLASOV section 4, from [CS06] Theorem 2 and [CD03] Theorem 5.6,
READ in the record) gives c(ε, s) supported in U with the KID coefficient m(ε, s) = ε²Q(δ_s) + O(ε³) uniformly in s,
continuous in s; m(ε, 0) < 0 < m(ε, 1) for ε small, so m(ε, s(ε)) = 0 for some s(ε). ∎ (This is R6 section 1.5 (i)
with the momentum seed replaced by a tensor one, so no band-by-band argument for non-gauge-ness is needed.)

Physically: inside the horizon ξ is spacelike and Q is a momentum; an outgoing tensor packet carries it with the sign
opposite to the momentum seeds', as R6 section 1.5 anticipated and Theorem Q′ (ii) found for outgoing null dust. Seeds
localised in angle as well exist: a class TT field H(R, θ)-dependent with B, C determined pointwise from A (Lemma H
(c)) solves the linearised constraints for any R- and θ-dependence, and (X1) holds mode by mode (deduced).

## 4. Outside the horizon: M_b holds (Theorem P)

### 4.1 From Part I's slice to a static slice (Lemma TR; deduced)

**Lemma TR.** Let δ be a compactly supported invariant linearised vacuum seed in a band U ⊂ {f > 0} of Part I's slice.
Let h be the linearised vacuum solution of Tangherlini (mass of U's region) with data δ, in a harmonic gauge with
compactly supported gauge data, so supp h ⊂ J(K), K = supp δ. Then for a static slice {t = t1} (t = v − r*),
h|_{t = t1} has compact support in the exterior and Q(δ) = Q_static(h|_{t = t1}).

*Proof.* (1) Q is a flux. For g_ε = g + εh, H(γ_ε, K_ε) = 2G_ε(n_ε, n_ε) and M_i = G_ε(n_ε, e_i) (the pairing qsign5
Q5 (b)); expanding at second order with G = 0 and G^(1)[h] = 0, the ε² coefficient of N_s H + 2Y_s·M is 2G^(2)[h](ξ, n),
and the second-order part K2 of the data contributes ∫(N_s, 2Y_s)·DΦ(0, K2) = 0 (KID; K2 compactly supported). So Q(δ)
= 2∫_Σ G^(2)[h](ξ, n). (2) J^a := G^(2)[h]^ab ξ_b is conserved: expanding ∇^(ε)_a G_ε^ab = 0 at second order with G^(1) =
0 gives ∇_a G^(2)ab = 0, and ∇_a(G^(2)ab ξ_b) = G^(2)ab ∇_(a ξ_b) = 0. (3) The slice: in Kruskal coordinates (U, V)
of region I (both future-increasing), the slice is a spacelike curve along which U decreases and V increases with R;
K occupies U ∈ [U(R2), U(R1)], V ∈ [V(R1), V(R2)]; J⁺(K) ⊂ {U ≥ U(R2), V ≥ V(R1)}, J⁻(K) ⊂ {U ≤ U(R1), V ≤ V(R2)}. The
rectangles S_in = {U(R1) < U < 0, 0 < V < V(R1)} and S_out = {U < U(R2), V > V(R2)} meet neither. A static slice is a
ray V = c|U|; choose c with V(R_a)/|U(R1)| < c < V(R1)/|U(R1)| (R_a < R1 on the slice), so the ray meets S_in at
points with U slightly above U(R1); it meets S_out at |U| large. Let Σ′ coincide with Part I's slice outside [R_a,
R_b], follow straight (spacelike: ΔU ΔV < 0) segments inside S_in and S_out to the ray, and the ray between them;
R_b is taken large enough that V(R_b) > c|U_s′| and |U(R_b)| > |U_s′| at the outer junction U_s′. Σ′ is a spacelike
graph equal to the slice outside a compact set, so by Stokes and (2) the flux of J through Σ′ equals Q(δ); h vanishes
on the two connectors (they lie in S_in, S_out), so the flux is that through the ray, whose part outside the ray
segment carries no support (J(K) ∩ ray ⊂ {|U| ∈ [min(|U(R1)|, V(R1)/c), max(|U(R2)|, V(R2)/c)]}, inside the segment).
The flux through a full static slice is Q_static of h's data there, by (1) on that slice; the support is compact and
avoids the bifurcation sphere (near U = V = 0 a point is in neither J⁺(K) nor J⁻(K)). ∎ Standard facts used:
existence, uniqueness up to gauge and finite propagation for the linearised equations in harmonic gauge; Stokes.
*Computational support:* in the tensor sector Theorem T verifies the conclusion on every slice of the family directly
(Q equals the conserved master flux, slice by slice), and in the scalar sector E9 shows that Q on static slices is the
conserved master energy.

δ is gauge iff h is iff h|_{t = t1} is (uniqueness up to gauge).

### 4.2 The static slice

On γ = dR²/f + R² dΩ₃², N = √f, K0 = 0, Y = 0: D²H[(h, k), (h, k)] = D²R[h, h] + 2((tr k)² − |k|²), the mixed terms
vanishing at K0 = 0, and the linearised constraints decouple: DR[h] = 0, D^i(k_ij − tr k γ_ij) = 0. So

    E = E_V(h) + E_K(k),   E_V := −½ ∫ N D²R[h, h] dvol,   E_K := ∫ N (|k|² − (tr k)²) dvol.

**Lemma G (gauge invariance; computed E4 (c), deduced).** E_V(h + L_Xγ) = E_V(h) when DR[h] = 0 and E_K(k + k_ψ) =
E_K(k) when M[k] = 0, k_ψ := D²ψ − ψ Ric, for X, ψ with compact support. *Proof.* From R(φ*γ) = φ*R(γ):
DR[L_Xγ] = X(R) = 0 and D²R[h, L_Xγ] = X(DR[h]) − DR[L_X h]; then −∫N X(DR[h]) = ∫div(NX) DR[h] = 0, and ∫N DR[v]
dvol = ∫⟨(DR)*N, v⟩ = 0 for compactly supported v, as (DR)*N = D²N − ΔN γ − N Ric = 0 (static vacuum); the quadratic
term vanishes the same way. For E_K the bilinear form B(k, k_ψ) = ∫ψ · Euler_ψ[N(⟨k, k_ψ⟩ − tr k tr k_ψ) dvol] and
Euler_ψ[…] = √γ(2 dN·M[k] + N div M[k]), which vanishes when M[k] = 0; and M[k_ψ] = 0, so B(k_ψ, k_ψ) = 0. Computed
(mode-free, class fields of (R, θ), exact at three rational points with free jets): DR[L_Xγ] = 0; the Euler operator
of N DR[h] √γ vanishes in all five class components of h; M[k_ψ] = 0; the Euler identity for B. ∎

### 4.3 Modes and gauge-fixing (computed E4 (a), (b); deduced)

Expand a class seed on the static slice in Lemma H's harmonics: h = Σ_l scalar modes (h_RR = aS, h_Rθ = R b S′, h_ij =
R²(c S γ̂ + e Ŝ), Ŝ := D̂D̂S + (k²/3)γ̂S, k² = l(l + 2)) + Σ tensor modes + an l = 0 part, and k likewise ((p, q, w, z) in
place of (a, b, c, e)). By Lemma H (d) and orthogonality, E_V, E_K and the constraints split mode by mode. The spatial
gauge X = αS∂_R + βS′∂_θ shifts (a, b, c, e) by ((1/f)′α + 2α′/f, α/(Rf) + Rβ′, 2α/R − (2k²/3)β, 2β), so β = −e/2, α =
−Rf(b − Re′/2) reach b = e = 0 (the record's Regge–Wheeler-type gauge, GAUGEDECAY5 Lemma 1.3, on the slice), leaving
the invariants

    A = a + (1/f)′α + 2α′/f,    F = c/2 − f b + k² e/6 + f R e′/2;

the lapse direction k_ψS shifts z by ψ/R², so ψ = −R²z reaches z = 0. Both gauges are local in R and so compactly
supported. In this gauge (E4 (a), every coefficient computed free of θ) the radial densities per ∫S² sin θ cos θ dθ
are exact rational expressions in (R, μ, k²): C(A, F) the Hamiltonian constraint, M_R, M_θ the momentum ones, E_V(A, F),
E_K(p, q, w) (printed in the run).

### 4.4 The kinetic energy (Lemma K; computed E5)

With H_KI := m + 6μ/R², m := k² − 3, and Z := R³(w − f q):

    Z′ + (R²H_KI/3) q + R² M_θ + (R³/3) M_R = 0 identically,
    E_K = 6k² m Z² / (R³ H_KI²) + d/dR(…)  on the momentum constraint,

and Z ↦ (q, w, p) = (−3Z′/(R²H_KI), Z/R³ + f q, ((4 − 3x)q + R f q′ − 2w)/f), x := μ/R², parametrises every solution of
both constraints (onto: q = −3Z′/(R²H_KI) on the constraint). Control: R³w in place of Z (a gauge-variant variable)
fails the identity (rejected).

### 4.5 The potential energy (Lemma V; computed E6)

(i) E_V = E_red + R⁴F′C + d/dR, E_red = 24R³fF′² + (14k² − 24)RF² − R²f(k² + 12f)AF′ + (k²/2)Rf²A² + 3k²RfAF. (ii) ℓ :=
A − (2R/f)F′ + (2H_KI/(3f²))F satisfies ℓ′ + κℓ − (2k²H_KI/(9Rf³))F = (R/(3f²)) C, κ := (k² + 6 + 6x)/(3Rf); so on the
constraint F = 9Rf³(ℓ′ + κℓ)/(2k²H_KI), A = ℓ + (2R/f)F′ − (2H_KI/(3f²))F, and this map ℓ ↦ (A, F) solves C
identically. (iii) With Φ := R^(3/2) f² ℓ/H_KI,

    E_V = (27m/(2k²)) ( f Φ′² + Qp Φ²/(16 R² H_KI²) ) + d/dR,
    Qp = 1296x³ + (624m − 144)x² + 36m(m − 12)x + 16m³ + 60m²,

i.e. ∫ (27m/(2k²)) ((∂_r*Φ)² + V_S Φ²) dr*, V_S = f Qp/(16R²H_KI²): Kodama and Ishibashi's scalar potential at n = 3
(the record's gmodes5 G3, READ [KI03] (3.1)-(3.7)); here it is recomputed from the record's constraint map, not taken
from [KI03]. ℓ is the five-dimensional Moncrief variable (in four dimensions the same construction gives Moncrief's
K + (f/Λ)(H2 − rK′)). The principal parts cancel: E_V(ℓ) has no ℓ″² term. Controls: ℓ without its F-term fails (ii)
(rejected); Φ with R^(1/2) in place of R^(3/2) fails (iii) (rejected).

### 4.6 Positivity (computed E7, E8, E2)

Class modes have l = 2j, so m = 4j(j + 1) − 3 ∈ {5, 21, 45, …}. **Qp > 0 for x ∈ [0, 1]**: at m = 5, Qp = 1296x³ +
2976x² − 1260x + 3500 with the quadratic's discriminant −40075200 < 0 and no root in [0, 1]; for m = 21 + t, t ≥ 0,
every coefficient of Qp in (x, t) is ≥ 0 and Qp(0, 0) > 0. H_KI > 0; f > 0 on R > √μ; 27m/(2k²) > 0, 6k²m/(R³H_KI²) > 0.
So E_V,l ≥ 0 and E_K,l ≥ 0, with E_V,l = 0 iff Φ = 0 iff ℓ = 0 iff (A, F) = 0 (by (ii)), and E_K,l = 0 iff Z = 0 iff
(p, q, w) = 0 (Lemma K, f > 0). Control (the wrong sign): the potential of the ℓ-form before the S-deformation is
negative near the horizon at m = 5 (computed: it changes sign on r > 1 at μ = 1), so the positivity is not automatic
(rejected). l = 0 (E8): on the constraint E_V and E_K are d/dR's; a compactly supported l = 0 h is L_(RF∂_R)γ, the
other solution of the l = 0 constraint being the mass change A = μ/(R²f²), nowhere zero. Tensor modes: Theorem T at w
= 1/f (the static slice), E_T = |T|² ∫(R³P² + R³fH′² + (k_T² + 2)RH²) dR > 0.

**Remark (E9, computed).** On the momentum constraint the configuration map applied to h = 2Nk gives Φ[2Nk] = (2k²/3)
√f Z/(R^(3/2)H_KI); since ∂_t h = 2Nk + L_βγ on a static slice, this is ∂_tΦ, and E_K = (27m/(2k²))∫Φ_t²/f dR. So
on the static slice E = (27m/(2k²)) |S|² ∫(Φ_t² + (∂_r*Φ)² + V_SΦ²) dr*, the energy of the Kodama–Ishibashi master
equation, conserved by it.

### 4.7 Theorem P

**Theorem P.** For every compactly supported invariant linearised vacuum seed δ in a vacuum band U ⊂ {f > 0} of Part
I's slice, Q(δ) ≤ 0, with equality iff δ is gauge.

*Proof.* Lemma TR moves Q to a static slice; there Q = −E_V − E_K (4.2), unchanged by the compactly supported gauge of
4.3 (Lemma G); the modes separate (orthogonality); each scalar mode has E_V,l + E_K,l ≥ 0 with equality iff its gauge-
fixed data vanish (4.4-4.6); tensor modes likewise (Theorem T); l = 0 contributes 0 and is gauge (E8). So Q ≤ 0, and Q
= 0 iff every mode is gauge iff δ is gauge (uniqueness up to gauge, Lemma TR). ∎ **Status: deduced**, with every
identity computed (E2, E4-E8); the standard facts are those of Lemma TR.

## 5. What follows for exact compact support

- **Inside the horizon (Theorem X): yes.** On every vacuum band of Part I's slice meeting {f < 0}, exact invariant
  vacuum data equal to Part I's outside the band exist, with a non-gauge (tensor-type) first-order part. With the
  outgoing null dust of R6 Theorem Q′ (ii), the band inside the horizon admits exact localisation both in vacuum and
  with matter.
- **Outside the horizon (Theorem P with Proposition L′): no, at second order.** No data background + εδ + O(ε²) with δ
  non-gauge satisfy the vacuum constraints and equal the background outside U, for ε small. *To every order (deduced):*
  if D_ε is a family of such data smooth in ε with D_0 the background, its first nonzero order after removing a
  re-slicing is a linearised seed δ_j with Q(δ_j) = 0 (the KID coefficient at order ε^(2j)), hence gauge by Theorem P;
  re-slicing the development by that gauge generator and repeating, D_ε agrees with a re-slicing of the background to
  every order in ε. Whether such a D_ε can be a non-trivial family that is flat at ε = 0 is not decided (no analyticity
  is claimed); the second-order statement is what Proposition L′ gives and what the paper uses.
- **The third order.** Q = 0 on a non-gauge seed happens only inside the horizon (δ_(s*) of Theorem X), where the sign
  change already gives existence; outside it happens only on gauge seeds. No question moves to third order.

## 6. Status

| item | status | support |
|---|---|---|
| Lemma H (class TT harmonics) | computed (n ≤ 3), deduced (all n) | E1 |
| Theorem T (tensor sector, every slice) | computed | E2 |
| Lemma X1, the exact Q > 0 seed on Part I's seed region | computed | E3 |
| Theorem X (exact localisation inside the horizon) | deduced | E3, Proposition L′ (READ in the record) |
| Lemma TR (passage to a static slice) | deduced | Theorem T, E9 (support) |
| Lemma G (gauge invariance on the static slice) | proved | E4 (c) |
| Lemmas K, V (the reductions) | computed | E5, E6 |
| positivity of the master potentials on the class spectrum | computed | E7 |
| l = 0 | computed | E8 |
| Theorem P (M_b outside the horizon) | deduced (every identity computed) | E2, E4-E8 |
| the static-slice E is the master energy | computed | E9 |
| HW canonical-energy identification | not used, not claimed | -- |

Not independently read: this note.

## 7. Proposed replacement for the M_b sentence of FAMILIES5-R6 section 8's proposed paper block

In FAMILIES5-R6.md section 8, "New:", the last sentence of the proposed bullet. (FAMILIES5-R6.md itself is not edited.)

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
  tensor type (computed exactly on the slice), so exactly localised vacuum data with a perturbation of the metric as
  first-order part exist on every vacuum band of the slice that meets the black-hole region (deduced, by intermediate
  values). Outside the horizon E is positive on every perturbation that is not a gauge one: in the class it is the sum,
  over the even harmonics, of the energies of Kodama and Ishibashi's master equations, whose potentials are positive in
  five dimensions (the reduction and the positivity computed exactly, the passage to a static slice deduced), so on
  bands outside the horizon no exactly localised vacuum data with a non-gauge first-order part exist.
```

## Files

`FAMILIES5-MB.md` (this note); `checks/mbsign5.py` (E1-E9, controls in E1, E2, E3, E5, E6, E7), `checks/mbsign5.out`
(its full run).
