# FAMILIES5-R6 -- round 6: the charge's sign, the band crossed, Theorem V's hypotheses and its N-family step

Status (2026-11-06, workstream C, round 6). This note continues FAMILIES5-VLASOV.md (round 5) and is its section 10 in
all but file: round 5's text stays as it was, with bracketed [R6 …] notes pointing here where a finding of the
round-5 verifier, or of this round, changes it (FAMILIES5-VLASOV.md, FAMILIES5-AXIS.md, FAMILIES5-FULL.md). It does not
edit the paper, N1STAR-PROOF.md or any proof5 Part. Section R6.0 seats the round-5 verifier's report, each finding
re-derived before it is accepted.

**Verdict.**

1. **(b) Exact compact support is settled for momentum seeds, and decided with matter (Theorem Q, Theorem Q′).** Every
   momentum seed (δγ = 0, any δK solving the linearised constraints, compactly supported in a vacuum band U of Part
   I's slice) is a pair (ψ, s1) of compactly supported functions, and its charge is, up to a divergence, minus two
   squares minus Γψ²/sin 2θ, where Γ = 4μ/R exactly wherever Part I's ψ_P vanishes and Γ > 0 on the seed region
   (computed): **Q < 0 for every nonzero momentum seed**, inside the horizon as well as outside. Hence no exactly
   localised vacuum data with such a first-order part exist. With matter the charge must equal ∫T(ξ, n), ξ the static
   Killing field (its KID is (N_s, 2Y_s), computed): where ξ is future causal (outside the horizon) the dominant energy
   condition makes this impossible; **inside the horizon outgoing null dust has T(ξ, n) < 0 and exactly localised
   Einstein–null-dust data exist** (constructed, the sign computed). Round 5's "nor with dust added" holds outside the
   horizon and fails inside it (the round-5 verifier's Major 4, decided). Gauge seeds have Q = 0 and give re-slicings.
   For seeds that perturb the metric the sign of Q is the canonical energy's; that is the one missing input, and
   nothing weaker settles exact vacuum localisation at second order (section 1.5).
2. **(a) The band is crossed (Theorem L″).** The obstruction is a property of the slice: a slice equal to Σ_τ0
   outside R ∈ [3.0, 5.75], bent by at most 0.00145 in τ, is spacelike and has Rácz's split hyperbolic at every point
   (computed, max κ′K′^l_l = −3.08 × 10⁻⁴). Data localised in an angle are posed there, for any radial support, and
   carried across the thin lens to Σ_τ0, widening their angular support by at most 4.8 × 10⁻⁴ rad. So band-localised
   data exist on all of Part I's slice. R2's "no foliation is hyperbolic" holds for foliations of Σ_τ0 itself, now
   proved from [Rac16] (4.22) (the verifier's correction).
3. **Theorem V's hypotheses are stated, open, and met (Lemma O, Proposition NE).** "The record's open conditions" are
   written out: the domain conditions of Lemma 1.1 (a)-(d) for g, and the two sign conditions of Lemma 6.3 (a) on the
   slice (positive mean curvature of the spheres, positive symmetrizer); (b)-(c) of Lemma 6.3 are properties of the
   approximant, not hypotheses. All hypotheses are strict inequalities of continuous functionals on a compact set,
   hence open, and an explicit label family on Tangherlini meets them with margins (computed): the class of solutions
   Theorem V covers is a nonempty open set. A hypothesis is added, (V2′): an angle η between the labels and any radial
   dust on its support (the verifier's Major 2; without it a mixed harmonic is exactly resonant, computed).
4. **The N-family step is written out (section 4).** The data with overlapping families (D₂_N) are proved: the λ⁻¹
   coefficient is linear in the waves and vanishes family by family with every mixed harmonic present (computed with
   three overlapping waves), and the only divisors are spacetime symbols, so [HL25]'s need for N odd (a spatial
   divisor, READ p. 28) does not arise; N is taken odd anyway. A₂_N and E₂_N are listed change by change. Theorem V is
   **deduced**, its N-family energy estimate by the two-family ledger applied family by family (not recomputed for N).
5. **Theorem K′ (Cauchy stability, the verifier's Major 3)** is proved with a tame source bound and a locality
   hypothesis for the domain version; both uses (Proposition L, Theorem N′ Step 9) satisfy them; computed in a model.
6. **Round 5's deduced steps have programs** (section 6): Proposition L′'s expansion and dichotomy, Theorem V's
   diagonal, Lemma A′ (b), each as a model (`checks/r5models5.py`), besides the programs above.

Labels as in the record: **computed** (a program `checks/<name>5.py` with a `.out` and a control it must reject),
**deduced** (argued here), **READ** (verbatim, identifier and page, read at source through alphaXiv, 2026-11-06). New
programs, each with its `.out`, all PASS: `checks/qsign5.py` (Q1-Q6), `checks/racslice5.py` (S1-S3),
`checks/vlasovex5.py` (X1-X3), `checks/nfamily5.py` (N1-N5), `checks/r5models5.py` (M1-M3). Repaired after the round-5
verifier, `.out` regenerated, PASS: `checks/racglobal5.py` (R1 edges, R2 proof, R4 note), `checks/vlasovhf5.py` (H4
resonant configuration, H6 (b) stability constant), `checks/katonl5.py` (K2, the control's label), `checks/twobg5.py`
(G3 margin).

---

## R6.0 The round-5 verifier: findings and dispositions

The verifier read round 5 at commit be6ad77, reran all eleven programs to their `.out` (timings aside), read [HL25],
[Rac16] and [CD03] at source, and ran its own scripts (copied in substance into the repairs below; its scratch is not
relied on). Each finding was re-derived before it was accepted.

- **Major 1 (D₂ for overlapping families; N odd).** *Re-derived.* Part I's data (FAMILIES5-FULL section 4, "Stage data
  on Σ_τ0", and section 6, Lemma 6.2₂) use that the two families' supports are disjoint on Σ_τ0, so the mixed
  harmonics vanish there; a Vlasov field's approximants overlap everywhere. [HL25] use N odd once (READ, p. 28: "since
  N is odd¹⁰, we also have |ω_B − ω_C ± π| ≥ π/N"; footnote 10: "We remark that this is the only place in the proof
  where we used that N is odd"), to bound below the divisors (7.31)-(7.32), a_B² sin²(ω_A − ω_B), which arise when
  they prescribe the eikonal's data ũ_A (7.11) and divide by the symbol of Δ − (cos ω_A ∂1 + sin ω_A ∂2)² (READ,
  p. 27, (7.24)-(7.29)). *Accepted and proved the first way:* D₂_N is proved with the mixed harmonics present
  (section 4.2; computed, nfamily5 N1-N2), the scheme's only divisors are spacetime symbols, nonzero for antipodal
  labels (N3), and N is taken odd along the diagonal. Theorem V is not relabelled conditional; its status is stated in
  section 4.4.
- **Major 2 (radial dusts and labels).** *Re-derived:* where a label's gradient is parallel to dv on the ingoing
  dust's support, g⁻¹(du_A, dv) = 0 and every harmonic supported on the pair (A, in) is null at every Λ (nfamily5 N4
  control). *Accepted:* hypothesis (V2′) (section 3), and Lemma C with c = min(c0/N², c(η)) (N4).
- **Major 3 (Theorem K's Cauchy stability; locality).** *Re-derived:* with the non-tame (K1) the bootstrap over a long
  interval does not close (the H^s bound can grow faster than the interval allows), and the domain version needs F on
  Σ_t ∩ Ω to depend on u there only. *Accepted:* Theorem K′ (section 5); "locality of F is used nowhere" holds for R^d
  only and is withdrawn for the domain version.
- **Major 4 (the dust clause).** *Re-derived exactly* (qsign5 Q5): the KID is (N_s, 2Y_s) for the record's (H, M), and
  it pairs the constraint map with 2T(ξ, n); |Y_s|² − N_s² = −f > 0 inside the horizon. *Accepted and decided:*
  Theorem Q′ (section 1.4): none outside, they exist inside.
- **Minor 1 ([HL25]'s uniformity).** *Accepted.* VLASOV verdict 1's "uniformity in N is not needed" is replaced by:
  the high-frequency step need not be uniform in N. [HL25] need uniform in N the background estimates (READ, p. 16,
  section 4.5: "Our goal will be to obtain estimates which are independent of N ... All implicit constants are
  independent of N"; p. 15, Proposition 4.7 (4)(a): "C = C(R) > 0 is independent of N"), the smallness ε2 of Theorem
  5.1 (p. 18: "There exist ε2 > 0 and N0 ... such that for any odd N ≥ N0"), and the L⁴ bound of p. 19, Step 3. Here:
  the first is Proposition U; no smallness threshold enters (Theorem V is a large-data statement, its smallness at each
  N being λ alone); the third is not needed, Theorem V's conclusion being weak L² convergence, for which the L² bound
  suffices (computed in a model, r5models5 M2).
- **Minor 2 (band edges).** *Re-derived* (racglobal5 R1, repaired): the interpolated zero crossings of N_k are [4.2916,
  4.5283] at n = 80 and [4.2914, 4.5284] at n = 160; "exactly" is dropped; the band is [4.29, 4.53] with margins 0.0014
  and 0.0016.
- **Minor 3 (twobg5 G3).** *Re-derived:* g3_indep's minimum left out the τ0 endpoint; the certified margin is 0.9951,
  at τ0; the printed "R − b ≥ 1.010 on all of [tau0, tau_end]" was the bisection's RK4 at its samples. Repaired
  (twobg5.py, `.out` regenerated; FULL's figure amended).
- **Minor 4 (Lemma A′).** *Accepted.* (b): the L²-Lipschitz bound holds for U whose components include ∂g (the
  record's first-order variable), on a ball small enough that L_U − L_ů is absorbed; with coefficients depending on a
  derivative that U does not carry it fails (computed, r5models5 M3 and its control). (a): the derivatives transverse
  to the disc commute with L_ů up to operators of lower order with smooth coefficients, so ∂_⊥ δh obeys the same
  equation with a source controlled by the previous step; induction on the number of transverse derivatives gives (a)
  for all |α| ≤ m.
- **Minor 5 (Proposition L′).** *Accepted:* it requires DΦ(δ) = 0; otherwise c = O(ε) (computed, M1's control).
- **Minor 6 (B6, "any amplitude").** *Accepted:* B6 localises cone data exactly for any amplitude; carrying them to
  Σ_τ0 is Cauchy stability, which needs small data.
- **Minor 7 (H6 (b) does not discriminate).** *Re-derived* (with the coupling removed it passes). Repaired: the
  N-system's stability constant is measured directly, 0.603, 0.667, 0.667 at N = 4, 8, 16; a coupling growing with N
  gives 0.603, 0.873, 1.654 and is rejected. Stated: the model has no derivative-loss coupling.
- **Minor 8 (katonl5's control).** *Accepted:* 0.5 u_xx violates (K1) and (K2).
- **Minor 9 (FULL stale).** *Accepted:* [R6] pointers at FULL's status (lines 10-11) and Part III's "Where it stops".
- **Minor 10 (the proposed §9 text).** *Accepted, all five:* "a massless Vlasov limit in the class is restricted"
  replaces "the only kind a limit can carry"; "no combination resonant up to the order the scheme uses"; the 1/ρ2 and
  (O1) sentences carry their labels; "(computed)" is confined to the split's region; the dependences are stated
  (section 8).
- **Mutations not caught.** H4 with a_A = 1: repaired (the resonant configuration in the main loop; with a_A = 1 its
  least |Q|/(a_T a_S) is 0 and H4 fails). H6 (b): repaired as Minor 7.
- **Nits.** *Accepted:* T^(N) is Σ_A q_A du_A ⊗ du_A with q_A = (2π/N) q(·, ω_A), one weight; a_A = Λ^(A−1)
  throughout; "its phase being non-null" should read "du_A ≠ 0 on the support" (non-stationary phase); |du_A|² is a
  Euclidean frame norm; H5 samples labels in [−0.6, 0.6] and adjacent pairs (Lemma S is proved for all); H6 (a)'s
  midpoint nodes are harmless; Lemma C's 2m can be m (nfamily5 uses the sharper constant); dα/dω ≥ 0.80 reads ≥ 0.798.
- **Proposition Ax's "automatic".** *Accepted:* for a smooth solution on compact Ω̄ the set supp q ⊂ Ω̄ × S¹ is
  compact; by Proposition Ax no ray of a non-axial label reaches an axis in Ω, so dist(D_ω, axes) > 0 for each ω, and
  by continuity of the flow and compactness inf_ω dist(D_ω, axes) =: 2δ > 0.
- **Confirmed by the verifier and unchanged:** Lemmas S, C, P, Ψ; R3; R4's pointwise identity and sign on 21 further
  seeds; the [HL25], [Rac16], [CD03] readings; Lemma E; Theorem K's local theory; the round-4 seatings.

## 1. (b) Exact compact support: the sign of the charge

### 1.1 Momentum seeds (deduced; computed qsign5 Q1)

On a vacuum band U of Part I's Σ_τ0 write γ = G dR² + R² dΩ₃², K0 = κ0 n̂n̂ + Y0 R² dΩ₃², and a symmetric invariant δK
by its orthonormal components δK_RR = κ, δK_Rθ = p̂, δK_θθ = Kt/3 + s1, δK_11 = Kt/3 + s2, δK_22 = Kt/3 − s1 − s2.
With δγ = 0 the linearised constraints of the record's map (bandconst5: H = R + (tr K)² − |K|², M_i = D_jK^j_i −
D_i tr K) are, exactly (Q1 (i)):

- δH = 2(3Y0 κ + (κ0 + 2Y0) Kt) = 0, so κ = c Kt, c := −(κ0 + 2Y0)/(3Y0);
- δM_R = −∂_R Kt + (3c − 1)Kt/R + (√G/R)(1/sc) ∂_θ(sc p̂) = 0, sc := sin θ cos θ: a divergence, so (with compact
  support) Kt = E ∂_θψ/sc, p̂ = (R/√G) E ∂_Rψ/sc for a compactly supported stream function ψ, E := e^(∫a), a :=
  (3c − 1)/R = −3(1 − β)/R, β := −κ0/(3Y0);
- δM_θ = (1/(√G R³)) ∂_R(R⁴p̂) − β ∂_θ Kt + ∂_θ s1 + (cot θ − 2 tan θ) s1 − s2/sc = 0, which fixes s2.

So **every momentum seed is a pair (ψ, s1) of compactly supported functions, and every pair is one.** (B4's stream
seeds are s1 = 0.) The quadratic part of H gives Q = ∫ N_s ((tr δK)² − |δK|²) dvol (the momentum constraint is linear
in K at fixed γ), with integrand ν sc [(2β − 2/3) Kt² − 2p̂² − s1² − s2² − (s1 + s2)²], ν := N_s √G R³.

### 1.2 Theorem Q (deduced; the identity computed exactly, qsign5 Q1)

**Theorem Q.** For every momentum seed (ψ, s1) compactly supported in U,

    Q = −(2π)² ∫∫ [ 2ν sc (Z − Eψ/(2 sc²))² + (3/2) ν sc (s1 − 2EX/(3 sc))² + Γ ψ²/sin 2θ ] dθ dR,

    Z := s2 + s1/2,   X := ∂_θψ − (3/2)(cos 2θ/sc) ψ,   Γ := 4νE² − P′,   P := 8νE²R/G − (2νER/√G)′ RE/√G.

*Proof.* Three integrations by parts and two completed squares. (i) With weight 2νE/sc, ∫∫ (2νE/sc) ψ W = ∫∫ ν sc (2β
Kt² − 2p̂²) − ½ ∫∫ P′ψ²/sc, W := s2 at s1 = 0 (the θ-integration by parts produces no derivative of the weight
because the weight times sc depends on R alone). (ii) With s1 present, W = Z − T s1, T s1 := sc ∂_θ s1 + (3/2) cos 2θ
s1, and ∫ (ψ/sc) T s1 dθ = −∫ s1 X dθ. (iii) Completing the square in Z and in s1 leaves (1/sc)[νE²ψ²/(2sc²) + ½ P′ψ²
+ (2/3)νE²(X² − ψ_θ²)], and the θ-integration of the cross term in X² − ψ_θ² gives ∫ (X² − ψ_θ²)/sc dθ = ∫ ψ² (6
cos² 2θ − 12)/sin³ 2θ dθ, which collects the ψ² terms into −Γψ²/sin 2θ. Computed: the Euler operator of (Q-density −
decomposition) vanishes in ψ and in s1, for arbitrary G, κ0, Y0, ν, exactly at three rational points (Q1 (ii));
control: with 4νE² → 3νE² it does not. ∎

**Corollary Q.** Wherever Γ > 0 on U, Q(δ) ≤ −(2π)² ∫∫ Γψ²/sin 2θ < 0 for every nonzero momentum seed; if ψ = 0, Q =
−(2π)² ∫∫ ν sc (2(T s1)² + (3/2) s1²) < 0 unless s1 = 0.

### 1.3 Γ on Part I's slice (computed: qsign5 Q2-Q4)

- On every vacuum region of Part I's chart (g0 = −e^(2ψ_P) f dv̂² + 2e^(ψ_P) dv̂ dR + R² dΩ₃², ψ_P = ψ_P(v̂)), N_s √G
  = 1, so ν = R³; Γ/E² is explicit in (R, μ, ψ_P, ψ_P′, ψ_P″); where ψ_P = 0, E = √G/R and **Γ = 4μ/R** exactly (Q2;
  control: P's coefficient 8 → 6 breaks it). The margin is the mass: on flat space the identity degenerates to Q ≤ 0,
  where gauge directions with δγ = 0 exist.
- ψ_P = 0 on the slice outside the outgoing packet (the gap and outside the shell; twobg5 G1 (b), and to 7.6 × 10⁻⁷
  on 391 slice points at n = 160), so Γ = 4μ/R > 0 there. On the seed region (ψ_P = ψ_III(v̂)), Γ/E² ≥ 0.6247 on R ∈
  [0.70, 1.85], horizon at 0.9067 included, Γ between 0.715 and 2.09 times its ψ_P = 0 value, converged between n =
  80 and 160 (Q3).
- On 99 explicit seeds (R4's 45 stream seeds, 54 with s1 ≠ 0, among them s1 equal to the pointwise maximiser and s1
  alone; three bands, one inside the horizon) Q < 0, the decomposition reproduces Q to 1.2 × 10⁻⁶ of Q and 2.2 × 10⁻²
  of its Γ term, and Q ≤ −∫∫Γψ²/sin 2θ (Q4; control: the decomposition without its Γ term misses Q by that term).

So **Q < 0 on every nonzero momentum seed on every vacuum band of Part I's slice.** By Proposition L′ (with DΦ(δ) = 0,
minor 5), no vacuum data background + εδ + O(ε²), supported in U, with δ a momentum seed, exist for ε small.

### 1.4 Matter: Theorem Q′ (deduced; computed qsign5 Q5-Q6)

**Lemma (the KID's pairing; computed exactly, Q5).** On Tangherlini's slice in Part I's chart, (N_s, 2Y_s), Y_s =
Y_s^R ∂_R, Y_s^R = μ/(G R²), is in the kernel of the adjoint of the linearised constraint map (H, M): the Euler
operator of √γ (N_s DH + 2 Y_s^R DM_R) vanishes in all nine invariant fields (δγ diagonal, δK) (control: (N_s, Y_s)
is not). On ingoing Vaidya data in that chart, N_s H + 2 Y_s^R M_R = 2T(ξ, n), T the Vaidya stress (3μ′/(2R³)) dv̂²,
ξ = e^(−ψ) ∂_v̂ (computed: G_vv of ingoing Vaidya and the pairing). So exact data background + εδ + c with matter
stress T supported in U require

    ε² Q(δ)/2 + O(ε³) = ∫_U T(ξ, n) dvol.                                                                    (Q′)

**Theorem Q′.** (i) If f ≥ 0 on U (ξ future causal) and T obeys the dominant energy condition, T(ξ, n) ≥ 0, so (Q′)
fails for ε small: no exactly localised Einstein–matter data from any momentum seed. (ii) If U meets {f < 0} (inside
the horizon; on the seed region R < 0.9067), there are exactly localised Einstein–null-dust data: for radial null dust
T(ξ, n) = q f √(2 − f)/4 along ℓ_out = ∂_v̂ + (f/2)∂_R and q/√(2 − f) along ℓ_in = −∂_R (ψ_P = 0; exact, Q5 (c)), so
outgoing dust inside the horizon has T(ξ, n) < 0. Fix a momentum seed δ in U and an outgoing dust profile q1 ≥ 0 on U
∩ {f < 0}, with ∫T1(ξ, n) < 0, and put s* := Q(δ)/(2∫T1(ξ, n)) > 0. [CS06] Theorem 2 (READ in round 5) solves Φ(γ, K)
= ε² s (2ρ1, J1)_γ up to the KID, the source depending on (γ, K) only through the dust direction's normalisation in
the unknown metric, an O(ε²) smooth dependence that its implicit-function argument absorbs (deduced); the KID
coefficient is m(ε, s) = ε²(Q/2 − s ∫T1(ξ, n)) + O(ε³) uniformly on s ∈ [0, 2s*], continuous in s ([CS06] Theorem 2:
"(g, π) depends continuously on (v, W)"); m(ε, 0) < 0 < m(ε, 2s*) for ε small, so m(ε, s(ε)) = 0 for some s(ε): exact
Einstein–null-dust data, equal to Part I's outside U, the dust density ε² s(ε) q1 ≥ 0. ∎ Computed (Q6): on R ∈ [0.72,
0.9] (f ∈ [−0.586, −0.015]) a seed with Q = −7.25 × 10⁴ and q1 the seed's envelope give ∫T1(ξ, n) = −4.35 × 10⁻²,
s* = 8.33 × 10⁵ > 0; control: the same dust on R ∈ [1.0, 1.75] (outside the horizon) gives ∫T1 > 0, no s*.

Physically: inside the horizon ξ is spacelike, so its conserved charge is a momentum, which two oppositely moving
contributions can cancel; outside it is an energy, which the dominant energy condition makes positive.

### 1.5 Seeds that perturb the metric: the one missing input

- *Gauge seeds* δ_g = (2fK0 + L_Xγ, …), (f, X) supported in U (or equal to a constant multiple of the KID on the inner
  side, as a deformation of the slice along ξ): background + εδ_g + O(ε²) are exact data (the slice deformed inside the
  background spacetime), so Q(δ_g) = 0 (deduced). They exist, and they are the background itself, re-sliced.
- *Configuration seeds* (δγ ≠ 0, not gauge): every seed is (h, k_h + (ψ, s1)) with h compactly supported and k_h
  found by quadratures (κ and s2 algebraic, (Kt, p̂) from a divergence equation whose source integrates to zero by the
  KID identity; deduced), and Q(δ) = −E(δ), E the canonical energy of the linearised solution relative to ξ (the
  second-order quantity ∫G^(2)(ξ, n), conserved between slices of the vacuum region while the support stays in it).
  Its sign on configuration seeds is not determined here.

**The missing input (M_b).** *E(δ) > 0 for every non-gauge compactly supported invariant linearised vacuum solution δ
supported in U.* Given M_b, Proposition L′ excludes exactly localised non-gauge vacuum data near the background in U.
**Nothing weaker suffices**, and M_b's failure decides the other way: (i) if E(δ+) < 0 for a δ+ in U, take a momentum
seed δ− in U with radial support disjoint from δ+'s; Q is continuous and changes sign on δ_s = (1 − s)δ− + sδ+; at
s* with Q(δ_s*) = 0, δ_s* is not gauge (a gauge generator of δ_s* restricts, band by band, to generators of (1 −
s*)δ− and s*δ+, so Q(δ+) would vanish), and the intermediate-value clause of Proposition L′ gives exactly localised
non-gauge vacuum data; (ii) if E ≥ 0 with E(δ0) = 0 for a non-gauge δ0, the second-order coefficient of m vanishes on
δ0 and the question moves to third order, so no second-order argument decides it. Outside the horizon M_b is the
positivity of Tangherlini's canonical energy (the linear stability of its exterior, not proved or READ here); inside,
the outgoing dust of Theorem Q′ is the geometric-optics limit of an outgoing wave packet, which suggests that M_b
fails there (not claimed).

## 2. (a) Across the band: a deformed slice (Theorem L″)

**What R2 shows, corrected (the verifier).** [Rac16] Lemma 4.1 is sufficient only. The obstruction follows from
[Rac16] (4.22) (READ, p. 13): for a leaf covector ξ_S orthogonal to k′ (the leaves are three-dimensional; a torus
direction serves, k′(e_φ) = 0 for round K) the quadratic K′^l_l ξ_n² − 2ξ_n(k′·ξ_S) + κ′|ξ_S|² has discriminant
−κ′K′^l_l|ξ_S|² < 0 when K is negative definite: complex characteristic roots for every tilted foliation of Σ_τ0
(computed exactly, racglobal5 R2; control: the mixed-sign K's hyperbolic tilt has both discriminants positive). This
concerns foliations of Σ_τ0 only.

**Lemma S1 (computed exactly, racslice5 S1).** On every round slice v̂ = V(R) of Part I's chart, κ′ = K(T, T)/g(T, T)
(T = V′∂_v̂ + ∂_R) and K′^l_l = 3n^R/R are explicit in (E, f, ψ_R, ψ_v̂, f_R, f_v̂, V′, V″); at V′ = 1, V″ = 0 they are
B2's; and κ′ is affine in V″ with ∂κ′/∂V″ = 1/(E V′ √(V′(2 − EV′f)/E)(2 − EV′f)) > 0 on every spacelike round slice.
On Σ_τ0 κ is positive outside the band and of size −1.5 × 10⁻³ inside it, while K^l_l ≈ −0.07: a small bend toward
the future raises κ′ there.

**Theorem L″ (deduced from racslice5 S2-S3, Proposition L and Theorem K′).** Let Σ′ = {v̂ − R − φ(R) = τ0}, φ″ =
0.01 (b(R; 4.1, 4.7) − 0.3 b(R; 3.0, 4.0) − (1/3) b(R; 4.85, 5.75)) (b the C^∞ bump; the weights fix φ = φ′ = 0
outside [3.0, 5.75]). Then:

- Σ′ equals Σ_τ0 outside R ∈ [3.0, 5.75], is spacelike (V′ ≥ 0.9982, E V′ f ≤ 0.9036 < 2), and κ′K′^l_l < 0 at every
  point of Σ′ ∩ Ω₂ (max −3.08 × 10⁻⁴, the same to 0.03 % at n = 80 and 160): Rácz's split is hyperbolic on all of Σ′
  (computed, S2; controls: φ = 0 has the band, φ → −φ widens it to [4.20, 4.62]).
- For every invariant perturbation of Σ′'s free data ([Rac16] (4.28)), ε-small in C^∞, supported in {R1 < R < R2, θ1
  < θ < π/2 − θ1}, any [R1, R2] in [a, b(τ0)] (the band included), Proposition L on Σ′ gives constraint data on Σ′ equal
  to the background's outside {R ≤ R2, |θ − θ-band| ≤ Δ(R)} (solved inward from R2 to a, Theorem K′ on the whole
  interval).
- Their development across the lens between Σ′ and Σ_τ0 (a compact region with no lateral boundary, R ∈ [3.026,
  5.723], τ-thickness 0.00145, inside the computed domain; class Einstein–null-dust Cauchy stability near the smooth
  background, the record's local theory in Theorem K′'s form) induces on Σ_τ0 constraint data equal to Part I's outside
  the domain of influence of the support: the angular support widens by at most 0.00145/R_min = 4.8 × 10⁻⁴ rad and the
  radial by at most 0.0015 (R|dΩ/dτ| ≤ 1, augment5 S7; computed, S3).

So **data localised in an angle exist on all of Part I's slice, the band included** (deduced). Proposition L's
statement (FAMILIES5-VLASOV section 3) is superseded: no radial restriction remains, and the cone route (B6) is no
longer needed for the band.

## 3. Theorem V's hypotheses: stated, open, and met

**Theorem V (restated; deduced, the N-family step as in section 4).** Let (g, q, u) be a smooth class solution of
Einstein–restricted massless Vlasov, possibly with Part I's two radial dusts, on a compact domain Ω such that:

- (Ω) Ω = {τ0 ≤ τ ≤ τ_end, r ≥ a, v + (τ − τ_end) ≤ V + 1} (the record's (1.1)) with, for g: each Σ_τ ∩ Ω spacelike;
  {r = a} spacelike with r decreasing along future causal curves near it; {v + τ = const} spacelike with v + τ
  increasing along future causal curves; every family's generator, followed to the past, stays in Ω and meets Σ_τ0
  (Lemma 1.1 (a)-(d) for g);
- (V1) q and u smooth in (x, ω); for each ω the flow map of u_ω's rays from Σ_τ0 has Jacobian ≥ J0 > 0 on a
  neighbourhood of the tube D_ω of supp q(·, ω) in Ω (no caustic); ∂_ω β0 ≥ b > 0 on Σ_τ0 ∩ supp q;
- (V2) dist(D_ω, axes) ≥ 2δ > 0 for every ω (automatic for smooth solutions, R6.0);
- (V2′) on the support of each radial dust, every label's momentum makes an angle ≥ η > 0 with both radial null
  directions (or the supports are disjoint); the radial dusts satisfy Theorem N′'s (H2′) with Corollary N′1's adapted
  boundaries;
- (V3) on Σ_τ0 ∩ Ω the spheres r = const have positive mean curvature and the record's symmetrizer S = diag(1,
  −1/(2r²)) makes the momentum system's r-coefficient positive definite (Lemma 6.3 (a)'s two signs).

Then there are smooth T² × Z2 × Z2-invariant g_n on Ω with Ric(g_n) = 0, g_n → g uniformly and ∂g_n ⇀ ∂g weakly in
L²(Ω), along odd N_n → ∞. Lemma 6.3 (b)-(c) (no λ⁻¹ coefficient; principal coefficients unchanged) are properties of
the approximant, proved for torus-polarised waves (Lemma P (c), nfamily5 N1-N2), not hypotheses.

**Lemma O (the hypotheses are open; deduced).** Each of (Ω), (V1)-(V3) is a finite set of strict inequalities, on the
compact Ω̄ (or Ω̄ × S¹), between quantities that depend continuously on g in C² and on the slice data (q, u|Σ, ∂u|Σ) in
C¹: the contractions of g⁻¹ in (Ω) are continuous in C⁰; the rays and their first variation (whose determinant is the
Jacobian) solve ODEs whose coefficients are the Christoffel symbols and their first derivatives, so by continuous
dependence on coefficients and data the Jacobian, the tubes, their distance to the axes and the angles in (V2′) are
continuous in C²(g) × C¹(data); β0 and ∂_ωβ0 are continuous in C¹(u|Σ); the mean curvature and S A0 in C¹ of the
slice data. An infimum over a compact set of a continuous positive function is positive and depends continuously on
the parameters, so each condition holds on a neighbourhood. ∎

**Proposition NE (Theorem V is not vacuous; computed vlasovex5, deduced).** For the record's g0 with constant mass
(Tangherlini, μ = 1, Kerr–Schild form) on Ω(τ0 = 0, τ_end = 3, a = 0.8, V = 5), (Ω) and (V3) hold exactly (X1: g0⁻¹(dτ,
dτ) = −1 − μ/r², at r = a g^rr = −9/16 and g^rτ = 25/16, g0⁻¹(d(v + τ), d(v + τ)) = −3 − μ/r², b − a ≥ 2.20, θ³H =
3/(rG²) > 0, S A0 = diag(6, 1/(Gr²)) > 0; control: an untrapped a = 1.2 fails (b)). The labels ω ∈ I1 = [−0.5, 0.5]
(outgoing, leaving through r = b) and I2 = [π − 0.15, π + 0.15] (ingoing, inside the horizon when they leave), with
data u_ω = cos ω ρ(r) + sin ω r_c θ (ρ′ = √(1 + μ/r²), r_c = 3) and density on the ball |r − 3| ≤ 0.3, |θ − π/4| ≤ 0.15,
satisfy (V1)-(V2) with J0 = 1.0000 and 0.8978, δ = 0.157 and 0.098, b = 0.909 (X2, on a 9 × 9 grid of rays over the
ball enlarged by 20 % and 81 labels per interval; (V2′) is vacuous, no radial dust). Control: a family focused at
distance 1 ahead has a Jacobian changing sign (least −0.071) and is rejected; a wider ingoing interval [π − 0.5, π +
0.5] reaches an axis inside the horizon (the focusing of Proposition Ax), so (V2) is a real restriction. Openness
illustrated (X3): with μ = 1.02 and directions tilted by 0.02 sin 2θ, J0 = 1.0000 and 0.8471, δ = 0.152 and 0.072.
For ε small, the class Einstein–restricted-Vlasov solution with these data at amplitude ε (constraints by the
record's radial solve, (V3) open) exists on Ω (FAMILIES5-AXIS item 3: Vlasov off the axes, deduced) and is C²-close
to g0 with C¹-close eikonals, so by Lemma O it satisfies (Ω), (V1)-(V3): **Theorem V covers a nonempty open set of
solutions.** ∎

## 4. The N-family extension of A₂, E₂, D₂, written out

### 4.1 What changes from two families to N (deduced; the computed parts named)

- **A₂_N (the approximant to every order).** The stage system is FULL section 4's with N phases: (a) the mean, a wave
  equation; (b) N phase transports, each along its own generator; (c) each family's pure harmonics transported along
  its own generator; (d) every mixed harmonic e^(i n·s), two or more n_A ≠ 0, |n|₁ ≤ m + 2 at stage m, divided by Q_n
  = g⁻¹(K_n, K_n). On the overlaps |Q_n| ≥ 2 a_T a_S (c − mM²/Λ − m²M²/(2Λ)) with c = min(c0/N², c(η)) (Lemma C,
  sharpened; Lemma S for labels, (V2′) for label–radial pairs; computed H4 with the resonant configuration, nfamily5 N3-N4).
  The phase corrections and the mean change Q_n by O(λ), moved to the next order as in FULL's N2 argument since |n|₁ is
  bounded at each stage; each division costs one derivative, finitely many stages. Every generator reaches Σ_τ0 inside
  Ω ((Ω), (V1), (V2)), so the record's Picard argument closes the stage system.
- **E₂_N (the uniform estimate).** The record's Theorem E with w = h + Σ_A φ_A Y_A and N₂ summed over the N families:
  (i) the decomposition is N transports ℓ_A·dφ_A = ½ 𝒫 s_A(h), φ_A = 0 on Σ_τ0, coupled through the bounded maps φ ↦
  𝒫([Y_B(ℓ_A, ℓ_A)] φ) (M1), a contraction on slabs of length independent of the data, by Picard; (ii) the λ⁻¹ part of
  the linearisation is ½ λ⁻¹ Σ_A s_A G2^A, linear in the waves; (iii) Lemma 3.3_N: contracting with ℓ_A ⊗ ℓ_A kills
  family A's λ⁻¹ term and its □̃φ_A term; every B ≠ A survives exactly as Lemma 3.3₂'s family out does, ½ λ⁻¹((1 −
  𝒫)s_B(h)) G2^B(ℓ_A, ℓ_A) = O(∂ s_B(h)), λ⁻¹((ℓ_app^B − ℓ_B)·dφ_B) G2^B(ℓ_A, ℓ_A) = O(|dφ_B|), a bounded coefficient
  on Ψ_B; for torus-polarised waves the wave part of G2^B vanishes on orbit vectors (W_B(ℓ_A, ℓ_A) = 0), only the
  gauge part χ_B p_B ⊗ p_B remaining, as in two families; (iv) Lemma 3.4_N: Ψ_A := □̃φ_A closes for non-radial
  families by Lemma Ψ; (v) Lemma 2.4_N: every family's boundary terms have the record's sign, since every future null
  direction has dr/dτ ∈ [−1, (r² − μ)/(r² + μ)] (computed exactly, nfamily5 N5); (vi) Steps 4-7: every term of the
  N-family linearisation is a term type of the two-family ledger (twoledger5) with its family labels replaced; the
  ledger's counting (powers of λ, derivatives, which part of N₂ controls it) depends on the term type only; there are
  O(N³) terms and the constants depend on N. So the bootstrap closes at N₂ ≤ M(N) λ^K for λ ≤ λ0(N).
- **D₂_N (the data):** section 4.2.

### 4.2 Theorem D₂_N: the data with overlapping families (deduced; computed nfamily5 N1-N3)

**Theorem D₂_N.** For each N and λ ≤ λ0(N) there is a vacuum Cauchy datum on Σ_τ0 ∩ Ω within O(λ^K) of g_app's, with
the gauge condition imposed through ∂_τ g, the N families overlapping anywhere on Σ_τ0.

*Proof.* The approximant's slice data carry every family's wave and the λ² mixed and second harmonics; the mixed
amplitudes are the spacetime ones (stage (d) above) evaluated on Σ_τ0, algebraic in the pure ones. They satisfy the
constraints to O(λ^(K′)), g_app solving Einstein's equations to that order. The correction is the record's radial solve
(Lemma 6.4, Proposition 6.5), whose hypotheses are: (a) Lemma 6.3 (a) on the slice, which is (V3); (b) no λ⁻¹
coefficient in the linearisation at the approximant's data: that coefficient comes from λ⁻¹ ∂_s²(λ W_A) and from ∂_s
K1_A, so it is linear in the waves, the sum of the single-family ones, each zero for a torus-polarised wave with the
record's correction (Lemma P (c)), while the mixed and second harmonics enter at λ⁰ (computed exactly with three
overlapping non-radial waves on a non-round slice and generic λ² mixed harmonics in every component, N1; controls:
one wave in the second polarisation, or mixed harmonics at order λ, leave a λ⁻¹ coefficient); (c) the principal
coefficients at λ⁰ are the background's (N2: the coefficient of ∂_R a in ρ, the only one that involves ∂γ, does not
oscillate; control: a wave with a trace on the leaves makes it oscillate); (d) the constraint map depends on (γ, K)
only (S4). The gauge hierarchy (Lemma 6.1_N): each order's oscillating part is a transport along each generator for
pure harmonics and algebraic, with divisor Q_n ≠ 0, on mixed ones, which therefore take no data. The stage data (Lemma
6.2_N): Pol is onto for each family's covector; the mixed harmonics take no data and need not vanish on Σ_τ0, which no
step uses. **No division is made on the slice:** the phases are the background's eikonals with corrections φ_A = 0 on
Σ_τ0 (FULL 3.4₂), and Ψ_A's initial value is fixed by the transport, dividing only by ℓ_A(τ) ≠ 0 (a null vector is
never tangent to a spacelike slice); nothing prescribes the eikonal's data against the parametrix, as [HL25] (7.11)-
(7.29) do. The only divisors are the spacetime Q_n, which for an antipodal pair of labels is 2a_A a_B g⁻¹(k_A, k_B) =
−4a_A a_B|k|² ≠ 0; computed (N3): for N = 4 labels 2πA/4 with the hierarchy every Q_n with |n|₁ ≤ 5 has |Q_n|/(a_T
a_S) ≥ 359/216, while [HL25]'s divisor (a_B sin(ω_A − ω_B))² is 0 for the antipodal pair; control: without the
hierarchy some Q_n = 0. ∎ So N odd is not needed here; the diagonal takes N odd, at no cost.

### 4.3 Radial dusts with the labels (Major 2)

(V2′) is necessary for the scheme: where a label is parallel to a radial direction on the radial dust's support,
g⁻¹(du_A, du_rad) = 0 and Q_n = 0 for every n on the pair, at every Λ (nfamily5 N4 control). With an angle η: the
label–radial symbols are ≥ E E′(1 − cos η) (2/5 ≥ c(η) = 1/5 in N4), the hierarchy runs over all N + 2 phases, and every
combination with |n|₁ ≤ 4 has |Q_n|/(a_T a_S) ≥ 35612/609961 ≥ the bound 4/50765 (computed exactly, N4). Corollary
V1 (Part I with a restricted Vlasov field) is restated with (V2′).

### 4.4 Status of Theorem V

**Deduced.** Its ingredients: Proposition U (deduced; rate computed H6 (a); N-uniform stability computed in a model,
H6 (b) repaired); Lemmas S, C, P, Ψ (computed H5, H4, H1-H2, H3, nfamily5 N3-N4); A₂_N (deduced; divisors computed);
D₂_N (deduced; computed N1-N3); E₂_N (deduced: the two-family ledger, written in full and computed for two families
(FULL section 8, twoledger5), applied family by family; not recomputed for N); the diagonal (deduced; computed in a
model, r5models5 M2). Not read by an independent verifier.

## 5. Theorem K′: Cauchy stability (Major 3)

**Theorem K′ (deduced; a model computed, katonl5 K2).** In Theorem K's setting (FAMILIES5-VLASOV section 6) assume
moreover

- (K1′) tame: ‖F(t, u)‖_(H^s) ≤ C(‖u‖_(W^(1,∞)))(1 + ‖u‖_(H^s));
- (K4) for the domain version, locality: on Σ_t ∩ Ω, F(t, u) depends only on u|_(Σ_t ∩ Ω).

Let ū ∈ C([0, T]; H^s) solve the system on [0, T] (on the domain, with its spacelike lateral boundaries). Then there
is ε0 > 0 such that for ‖u0 − ū(0)‖_(H^s) ≤ ε0 the solution exists on [0, T], with sup_t ‖u − ū‖_(L²) ≤ e^(LT)‖u0 −
ū(0)‖_(L²), sup_t ‖u‖_(H^s) ≤ M and sup_t ‖u − ū‖_(H^(s′)) ≤ C ‖u0 − ū(0)‖_(L²)^(1−s′/s) for d/2 + 1 < s′ < s.

*Proof.* Put K := sup_t ‖ū‖_(W^(1,∞)) + 1 and let T* ≤ T be the supremum of the t for which the solution exists on [0,
t] with ‖u − ū‖_(W^(1,∞)) ≤ 1. On [0, T*): (1) ‖u‖_(W^(1,∞)) ≤ K; the H^s energy of the symmetric hyperbolic system,
with Moser's tame commutator bound ‖[∂^α, A(u)]∂u‖ ≤ C(‖u‖_(W^(1,∞)))‖u‖_(H^s) and (K1′), obeys d/dt E_s ≤ C(K)(1 +
E_s), so ‖u(t)‖_(H^s) ≤ (1 + ‖u0‖_(H^s))e^(C(K)T) =: M, uniformly for data within ε0 of ū(0). (2) w := u − ū solves the
linear system with coefficients A(u) and source −(A(u) − A(ū))∂ū + F(u) − F(ū); its L² energy with (K2) on the H^s
ball of radius max(M, sup ‖ū‖_(H^s)) gives ‖w(t)‖_(L²) ≤ e^(L t)‖w(0)‖_(L²). (3) Gagliardo–Nirenberg: ‖w‖_(W^(1,∞)) ≤
C‖w‖_(H^(s′)) ≤ C‖w‖_(L²)^(1−s′/s)‖w‖_(H^s)^(s′/s) ≤ C(2M)^(s′/s)(e^(LT)ε0)^(1−s′/s) < 1/2 for ε0 small. (4) If T* < T,
the solution at T* lies in an H^s ball of radius M, so Theorem K continues it past T*, and by continuity ‖w‖_(W^(1,∞))
< 1 a little beyond: a contradiction; so T* = T. On the domain the energy identities on Σ_t ∩ Ω carry lateral boundary
terms of the good sign (the record's Lemma 2.3), and (K4) makes every estimate of F on Σ_t ∩ Ω depend on u there only. ∎

*Its uses satisfy (K1′) and (K4) (deduced).* Proposition L and Theorem L″: [Rac16]'s system (4.16), (3.2) is a
first-order symmetric hyperbolic system whose zero-order terms are smooth functions of (u, x), local, tame by Moser.
Theorem N′ Step 9: the source χ_A S^ax is tame by Lemma A′ (a) (the verifier's observation) and local, the leaf map
being solved on discs D_2δ ⊂ Σ_t ∩ Ω centred on the axis. *Computed (model, K2):* for u_t + (1 + u)u_x = −(1 −
∂_x²)⁻¹(u²) (tame: ‖F(u)‖_(H²)/(‖u‖_∞‖u‖_(H²)) ≤ 0.263) on [0, 1], inside the background's lifespan, sup_t ‖u_d −
ū‖_(H²)/d = 12.46, 12.45, 12.45 for d = 4, 2, 1 × 10⁻³ (Lipschitz over the whole interval); control: on [0, 3], past
the background's shock, ‖ū‖_(H²) grows by 420 and the check rejects it.

## 6. Round 5's deduced steps, given programs (item 4)

FAMILIES5-VLASOV section 7 listed as deduced without a program: Proposition L′ (the expansion and the dichotomy),
Theorem V's diagonal step, Lemma A′, Proposition U's N-independence in the class, the amended Proposition L, and the
dust clause. Now:

- Proposition L′ (model, r5models5 M1): on Φ(u, v) = u′ + v″ + w(x)(u² − κv′²) with seeds u = −v′ and the KID 1:
  m(ε)∫ζ/ε² = 44.742, 45.400, 45.577 → Q = 45.647 at ε = 0.04, 0.02, 0.01, c = O(ε²); with w > 0 no exactly localised
  solution; with w changing sign the bisection gives exact solutions (m = 3.7 × 10⁻¹⁴, max |Φ| = 1.7 × 10⁻¹³, c
  supported in U); control: DΦ(δ) ≠ 0 gives c = O(ε).
- Theorem V's diagonal (model, M2): odd N = 5, 9, 15, 25, hierarchical frequencies, λ_N chosen by the proof's rule:
  ‖∂g_N‖²_(L²) equals the label quadrature of the Vlasov energy (cross terms vanish) and ∫η ∂g_N → 0 on a test field
  outside the list; control: N = 6 with a_A = 1 keeps the antipodal cross terms (20.13 against 10.86).
- Lemma A′ (b) (model, M3): the leaf map's slope is L²-Lipschitz in U on a small H² ball when the coefficients depend
  on U; control: coefficients in U′ not carried by U lose a derivative (the ratio grows with the frequency).
- Proposition U's N-independence: still computed only in a model (H6 (b), now a discriminating one); in the class it is
  deduced.
- Proposition L amended: superseded by Theorem L″ (computed S1-S3, deduced).
- The dust clause: decided by Theorem Q′ (computed Q5-Q6).
- Theorem K's Cauchy stability: Theorem K′ (computed in a model, K2).

## 7. What is proved, and what is not

- (b): Theorem Q (every momentum seed has Q < 0): deduced, the identity computed exactly, Γ computed; Theorem Q′
  (matter): (i) deduced from the dominant energy condition and the computed pairing, (ii) deduced from [CS06] (READ)
  with the sign computed. Missing for configuration seeds: M_b, the sign of the canonical energy (section 1.5).
- (a): Theorem L″, deduced from computed S1-S3, Proposition L and Theorem K′.
- Theorem V: deduced (section 4.4), hypotheses stated and open (Lemma O, deduced), nonempty (Proposition NE,
  computed and deduced).
- Theorem K′: deduced; model computed.
- Not independently read: this note.

## 8. Proposed replacement for the paper's section 9 bullet "More families"

The old text occurs exactly once in `paper/RESPONSE-HL-5D.md` (section 9, "What is not proved"). It supersedes the
replacements proposed in FAMILIES5-NONROUND, FAMILIES5-AXIS and FAMILIES5-VLASOV.

Old:

```
- **More families.** Angular separation and the passage to Vlasov matter are not attempted. Two crossing null dusts are
  scoped and taken through the leading orders (supplement `docket68/n1star/FAMILIES5.md`): the cross coupling of the two
  families is a gauge artefact at leading order (deduced; stage 0 computed, `docket68/n1star/checks/stage0two5.py`), and
  with two families the core estimate of section 5, its approximant to every order and its lemma on the domain are
  deduced (the lemma's form for the two-dust background computed, `docket68/n1star/checks/twodomain5.py`), the last given
  the two-dust background on the whole domain. That background's existence is deduced with one step sketched, given its
  characteristic data (the outgoing family's are open; the dusts' stress in the characteristic constraints computed,
  `checks/chardust5.py`), and computed on a region that does not reach the initial slice (`checks/twodust5.py` B5,
  floating point). With the outgoing family's characteristic data moved to an earlier cone (a choice, those data being
  open), it is computed on a rectangle reaching Σ_−1.5, every outgoing ray from the inner boundary leaving it at τ ≤
  −1.78, the constraint residuals converging at second order away from the steep inner boundary and the inner boundary
  trapped (computed, floating point, `docket68/n1star/checks/twodomainx5.py`, which also computes the earlier rectangle's
  exit range, τ from −0.960 to −0.702). The linearised constraint map at the approximant's slice data has no 1/λ
  coefficient with both families, on flat space, on Vaidya with an outgoing phase that is not null there, and on a static
  background with both phases null (computed, exactly, `checks/data5two.py`), and with both families' second harmonics as
  well (computed exactly on flat space and on Vaidya; with them the constraint system's principal coefficients are the
  background's, computed), and a wave with a trace on the spheres gives one. Not done: the background on the whole
  domain, the constraints' solution on its slice, the dynamic outgoing null phase, and the proof written out at the level
  of sections 5 and 6. No statement about several families is proved.
```

New:

```
- **More families.** Two crossing radial null dusts, one ingoing and one outgoing, are carried through the record's
  argument: the two-dust background on the whole domain, the approximant to every order, the uniform estimate and the
  data (deduced, every identity computed; supplement `docket68/n1star/FAMILIES5-FULL.md` Part I). In the T² class each
  family's null second fundamental form is diag(θ_h, κ1, κ2), the torus terms first order, and at an axis the planar
  shear is recovered elliptically from the expansion, so the class Einstein–null-dust system is Cauchy-stable on compact
  domains of the record's type, without smallness, for caustic-free dusts whose lateral boundaries are adapted (one
  family) where they meet an axis (deduced; `FAMILIES5-AXIS.md`). A massless Vlasov limit in the class is restricted
  (computed); a smooth restricted field never reaches an axis off the axial directions, its density growing like 1/ρ2
  there (computed, `checks/vlasovhf5.py` H7), and at an axis point at most one ingoing and one outgoing family are
  separated (computed, `checks/axisphase5.py`). Every smooth class Einstein–restricted massless Vlasov solution whose
  field is a family of dusts labelled by initial direction, caustic-free, off the axes and at an angle from any radial
  dust on its support, on a domain of the record's type whose initial spheres have positive mean curvature and a
  hyperbolic momentum system, is a weak limit of class vacuum metrics along odd N (deduced: N-dust approximants uniform
  in N; torus-polarised waves at frequencies 1, Λ, …, Λ^(N−1), which leave no combination of phases resonant up to the
  order the scheme uses; data with overlapping families, whose only divisors are spacetime symbols; the N-family energy
  estimate by the two-family ledger applied family by family; a diagonal choice of λ_N, as Huneau and Luk do;
  `FAMILIES5-VLASOV.md`, `FAMILIES5-R6.md`, the identities, divisors and data step computed). These hypotheses are open
  and an explicit family on Tangherlini meets them (computed, `checks/vlasovex5.py`). Data localised in an angle exist
  on cones exactly (computed) and on all of Part I's slice in a band widened by a computed amount (deduced): Rácz's split
  is hyperbolic on the slice except a band inside the shell, where no foliation of that slice is hyperbolic and a slice
  bent by 0.0015 is (computed, `checks/racglobal5.py`, `checks/racslice5.py`). Exactly localised data built on a
  perturbation of the extrinsic curvature alone do not exist, with or without matter obeying the dominant energy
  condition, outside the horizon: their charge is minus a sum of squares minus a term carrying the mass (deduced;
  computed, `checks/qsign5.py`); inside the horizon they exist with outgoing null dust (deduced; the sign computed). For
  perturbations of the metric itself the charge is the canonical energy, whose sign is not decided here: that is the one
  missing input, and nothing weaker settles exact vacuum localisation at second order.
```

## Files

`FAMILIES5-R6.md` (this note). New, each with its `.out`, all PASS: `checks/qsign5.py` (Q1-Q6, several minutes),
`checks/racslice5.py` (S1-S3, a few minutes), `checks/vlasovex5.py` (X1-X3, a few minutes), `checks/nfamily5.py`
(N1-N5, about half an hour under load), `checks/r5models5.py` (M1-M3, a few minutes). Repaired, `.out` regenerated,
PASS: `checks/racglobal5.py` (R1 interpolated edges and margins, R2 the discriminant of [Rac16] (4.22), R4 a note),
`checks/vlasovhf5.py` (H4's resonant configuration and the mutation flag H4_NOHIER, H6 (b)'s stability constant),
`checks/katonl5.py` (K2, the control's label), `checks/twobg5.py` (G3's τ0 endpoint and its print). Bracketed [R6]
notes: FAMILIES5-VLASOV.md, FAMILIES5-AXIS.md, FAMILIES5-FULL.md.
