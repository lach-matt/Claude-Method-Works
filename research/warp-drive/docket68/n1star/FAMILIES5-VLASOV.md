# FAMILIES5-VLASOV -- restricted Vlasov limits in the T² class; Rácz's split on the whole slice; standard results

Status (2026-11-06, workstream C, round 5). This note takes up the five items FAMILIES5-AXIS.md left open, (a)-(e). It
does not edit the paper, N1STAR-PROOF.md or any proof5 Part. FAMILIES5-AXIS.md is amended by bracketed [R5 …]
amendments, which also seat the findings of the verifier of round 4 (section 8 here). FAMILIES5-FULL.md is repaired in
place for the verifier of its Part V (its section 12).

**Verdict.**

1. **(d) The Vlasov limit is decided (Theorem V, deduced; every identity computed).** Uniformity in N is not needed, and
   N-dependence was not the obstruction: [HL25] itself fixes λ_N far below λ0(N) along a diagonal (READ, section 2).
   In the class the part that must be uniform in N is the background, and it is (Proposition U: the N-dust
   approximants of a Vlasov field labelled by initial direction differ from it by the label quadrature's residual,
   with constants independent of N). The high-frequency step may depend on N, and there round 4 named the wrong
   difficulty: the least pairwise symbol c/N² is harmless along a diagonal; what defeats the record's every-order
   scheme is resonance among three or more phases (k_a + k_antipode − k_c is exactly null, H4), which pairwise
   separation does not exclude. [HL25]'s own device removes it: frequencies 1, Λ, …, Λ^(N−1) make every combination
   non-null (Lemma C). With torus-polarised waves (Lemma P), the orbit space's absence of shear (Lemma Ψ) and
   separation kept by the flow (Lemma S), FAMILIES5-FULL Part II's extension applies at each N, and:
   **every smooth class Einstein–restricted-massless-Vlasov solution whose field is a caustic-free family of dusts
   labelled by initial direction, off the axes, on a domain of the record's type, with data meeting the record's open
   conditions, is a weak limit of class vacuum metrics.** The axes are not an extra hypothesis: restricted particles
   that reach an axis off the axial directions focus there with density ~ 1/ρ2 (Proposition Ax, H7), so a smooth
   solution's field never does; at an axis at most one ingoing and one outgoing family are separated (O1).
   [R6 (FAMILIES5-R6.md, the round-5 verifier). "Uniformity in N is not needed" reads: the high-frequency step need not
   be uniform in N; what [HL25] need uniform, and which of it is needed here, is in R6.0 (Minor 1). "Data meeting the
   record's open conditions" is replaced by stated hypotheses, with (V2′), an angle between the labels and any radial
   dust, added (R6 section 3, Lemma O, Proposition NE); D₂ with overlapping families is proved and N is taken odd (R6
   section 4); Theorem V is deduced with the N-family step as there.]
2. **(a) Rácz's split on the whole slice (computed).** On Part I's Σ_τ0 the algebraic-hyperbolic split is hyperbolic
   everywhere except a band R ∈ [4.30, 4.53] inside the shell (R1; converged, max N_k = 1.79 × 10⁻³ at R = 4.40), where
   the shell's flux exceeds 2μ(2 + μ/R²)/R (R2, exact). There K is negative definite and **no foliation** makes the
   split hyperbolic (R2, exact). Replacement: Proposition L holds for every perturbation whose radial support avoids the
   band; data meeting the band are posed on the cone N, where localisation is exact (B6). [R6. The band is [4.29, 4.53]
   (interpolated edges 4.2914, 4.5284 at n = 160; racglobal5 R1 repaired); "no foliation" holds for foliations of Σ_τ0
   and is now proved from [Rac16] (4.22) (R2 repaired); a slice bent by 0.00145 is hyperbolic everywhere and carries
   band-localised data across the band (R6 section 2, Theorem L″).] [R8: with the lobe moved, 0.00116, and certified for
   the background itself (FAMILIES5-R8.md R8.2-R8.3).]
3. **(b) Exact compact support (READ, computed).** [CS06]/[CD03] give vacuum data equal to Part I's outside a band up
   to the invariant KIDs; in Part I's vacuum regions there is exactly one, the static one (R3), so one charge. On the
   stream-function seeds the charge is negative (R4, 45 seeds), so they do not complete to exactly localised vacuum
   data, nor with dust added in the band (dust energy is nonnegative and enters with the same sign). Not obtained;
   what replaces it is localisation in a band widened by Δ (Proposition L), and exact localisation on cones.
   [R6. Decided: every momentum seed has Q < 0 (R6 Theorem Q, identity computed); with matter (Q′) the KID pairs with
   ∫T(ξ, n), which the dominant energy condition makes nonnegative only outside the horizon: "nor with dust added" is
   withdrawn for bands inside the horizon, where exactly localised Einstein–null-dust data exist (R6 Theorem Q′, the
   round-5 verifier's Major 4). The dust energy term 2∫N_s δe dropped Y_s·J.]
4. **(c) Part II.** (ii) at the axes is decided by (O1); for three or more families (ii) is replaced by (ii′),
   separation with hierarchical frequencies (Lemma C). (iii) is settled: non-radial families carry the torus
   polarisation, which is transported, cancels the constraints' λ⁻¹ term on every class slice, and realises every
   stress; the other polarisation fails the record's radial correction by a computed λ⁻¹ term (H2), and is not needed.
5. **(e) The standard results.** Kato 1975 (Arch. Rational Mech. Anal. 58, 181–205) and a textbook elliptic
   regularity theorem could not be read at source here (paywalled); the needed versions are proved (section 6):
   Theorem K (Kato's iteration with a non-local source bounded on H^s balls and L²-Lipschitz there; model computed,
   `katonl5.py`) and Lemma E (interior H^(k+2) estimates in two variables), with Lemma A′ (Lemma A in the two forms
   Theorem N′ uses). [Rac16] (READ, pp. 12, 14) and [CS06], [CD03] (READ) are quoted where used.

Labels as in the record: **computed** (a program `checks/<name>5.py` with a `.out` and a control it must reject),
**deduced** (argued here), **READ** (verbatim, identifier and page, read at source through alphaXiv, 2026-11-06). New
programs: `checks/vlasovhf5.py` (H1-H7) with `checks/twoscale5.py` (exact two-scale jets, T1), `checks/racglobal5.py`
(R1-R4), `checks/katonl5.py` (K1), `checks/h3proof5.py` (FAMILIES5-FULL item 6), each with its `.out`, all PASS.
Repaired, `.out` regenerated: `axisellip5.py`, `bandconst5.py`, `twotransport5.py`, `torusstress5.py`, `twobg5.py`,
`twodecomp5.py`.

---

## 1. The literature at source (READ)

- [HL25] C. Huneau, J. Luk, arXiv:2506.21779v1.
  - P. 3: "(1) First, we approximate the solution to Einstein-Vlasov equation by solutions to Einstein equations coupled
    to N dust (Proposition 4.7). (2) Then, we approximate the solution to Einstein-null dust equations by high frequency
    solutions to Einstein vacuum equations, with a frequency 1/λ very large compared to the number of dust N (Theorem
    5.1)." And: "in [14], the smallness parameter ε for the amplitude of f is allowed to depend on N, but now the
    dependence on N becomes important as we pass to the N → ∞ limit."
  - P. 2, (1.2): the Vlasov field is the family f(t, x, ω), u(t, x, ω), ω ∈ S¹, with "2Lf + (□_g u)f = 0 ∀ω ∈ S¹",
    "g⁻¹(du, du) = 0, u↾Σ0 = x¹ cos ω + x² sin ω": a continuum of dusts labelled by initial direction.
  - P. 11, Lemma 4.1: "ω_A^(N) = 2πA/N on S¹, and N coefficients α_A^(N) = m([2πA/N, 2π(A+1)/N))".
  - P. 18, Lemma 4.15: angular separation "with constant η′ in Definition 4.14 bounded below by η′ ≳ 1/N²". Lemma 4.16:
    "choosing the a_A bigger and bigger to ensure that there is a term in each expression which dominate the other ...
    a_0 = 1, a_A = cN² a_(A−1)". Theorem 5.1: "There exist ε2 > 0 and N0 ∈ Z>0 such that for any odd N ≥ N0, there
    exists λ0^(N) > 0 such that the following holds."
  - P. 19, proof of Theorem 3.1: "We choose our sequence (g_i, U_i) to be (g^(N_i, λ_N_i), U^(N_i, λ_N_i)) given by
    Theorem 5.1, with N_i ≥ N0 odd, N_i → ∞, and λ_N_i ∈ (0, λ0^(N_i)) chosen to be suitably small."
  - P. 5, footnote 5: "Going through the proof gives that C(N) = c^N N^N works for some large c ≥ 1".
  - Indices, fractions and superscripts restored from the extraction.
- [Rac16] I. Rácz, arXiv:1508.01810v3. P. 12: "the above outlined process guarantee that solutions κ, k_i, K^l_l to the
  system comprised by (4.16) and (3.2), along with the freely specifiable part of the data N̂, N̂^i, γ̂_ij, K̊_ij, in
  virtue of the relations (2.1) and (2.4) determine solutions to the full constraint system (1.1)-(1.2)." P. 14: "As
  for symmetrizable hyperbolic systems the initial value problem is known to be well-posed in the smooth setting",
  and Theorem 4.3: "there exists a unique smooth (local) solution (k_i, K^l_l) to (4.16) and (3.2)" for data making the
  system "symmetrizable hyperbolic in a sufficiently small neighborhood of S_ρ0".
- [CS06] J. Corvino, R. M. Schoen, arXiv:gr-qc/0301071v1. P. 13, Theorem 2: "Let Ω ⊂ M³ be a compactly contained
  C^(k+2)-domain, and let g0 be a C^(k+4,α)-metric and π0 a C^(k+3,α)-symmetric (2,0)-tensor. Suppose that the
  linearization DΦ_(g0,π0) of the constraint map ... has an injective formal L²-adjoint ... Then ... there is a
  C^(k+2,α)-metric g and a C^(k+2,α)-symmetric tensor π on M with Φ(g, π) = (v, W) in Ω and (g, π) = (g0, π0) outside
  Ω. Moreover, (g, π) depends continuously on (v, W). ... If the adjoint of the linearization has nontrivial kernel,
  then the analogous theorem holds for solving Φ(g, π) = (v, W) up to a finite-dimensional error."
- [CD03] P. T. Chruściel, E. Delay, arXiv:gr-qc/0301073v2. P. 4: "These are the general relativistic constraint
  equations whatever the space-dimension n". P. 24, Theorem 5.6: on a compact manifold with boundary, the constraint
  map is solved "up to kernel" with a projection π_(K⊥) on the orthogonal of the kernel of P*, with data and solutions
  vanishing at the boundary (Proposition 5.7). P. 33: "Elements in the kernel of P* are called Killing initial data
  (KIDs). Existence of non-zero KIDs implies existence of non-zero Killing vectors in the associated vacuum
  space-time".
- Not read at source (paywalled, by any route available here): T. Kato, *The Cauchy problem for quasi-linear symmetric
  hyperbolic systems*, Arch. Rational Mech. Anal. 58 (1975) 181–205; and the interior regularity theorems of the
  standard texts. Their needed versions are proved in section 6.

## 2. Theorem V: restricted massless Vlasov limits in the class

**Setting.** In the class a Burnett limit is restricted (FAMILIES5-FULL Part III V(b)): its momenta are tangent to the
2+1 orbit space, on which the Vlasov equation is the orbit space's (vlasov5 V1). Following [HL25] (1.2), a smooth
restricted field is written as a family of dusts labelled by ω ∈ S¹: T_V = ∫ q(·, ω) du_ω ⊗ du_ω dω, each u_ω an
eikonal of g with initial gradient of direction-label ω on Σ_τ0, q(·, ω) transported by 2ℓ_ω(√q) + (□u_ω)√q = 0.

**Theorem V (deduced; identities computed in vlasovhf5, twoscale5, racglobal5 and the record's programs).** Let (g, q,
u) be a smooth class solution of the Einstein–restricted-massless-Vlasov system on a compact domain Ω of the record's
type (N1STAR-PROOF.md Lemma 1.1 (a)-(f) for g), possibly with Part I's two radial dusts as well, such that:

- (V1) (q, u) are smooth in (x, ω); every u_ω has no caustic on a neighbourhood of the tube D_ω of supp q(·, ω) in Ω;
  distinct labels have nowhere-parallel initial gradients: ∂_ω β0 ≥ b > 0, β0 the gradient's angle on Σ_τ0;
- (V2) every D_ω lies at distance ≥ 2δ > 0 from the axes (for a smooth solution this is automatic: Proposition Ax);
  the radial dusts, if present, satisfy Theorem N′'s (H2′) with Corollary N′1's adapted boundaries;
- (V3) Σ_τ0 ∩ Ω carries a foliation by invariant 3-spheres on which the record's corrected constraint map satisfies
  Lemma 6.3 (a)-(c) (open conditions; they hold on every round slice, twoslice5 S1, so near Part I's).

Then there are smooth T² × Z2 × Z2-invariant metrics g_n on Ω with Ric(g_n) = 0, g_n → g uniformly and ∂g_n ⇀ ∂g weakly
in L²(Ω).

*Proof.* Proposition U gives, for N ≥ N0, the class Einstein–(N-dust)-solution g^(N) with labels ω_A = 2πA/N, and
|g^(N) − g|_(C¹(Ω)) ≤ C_k N^(−k) for every k. For each such N: (i) g^(N) satisfies Lemma 1.1 on Ω (open, inherited from
g); (ii′) its families are pairwise separated with constant c0/N² (Lemma S) and, with the frequencies a_A = Λ^A, every
combination with |n|₁ ≤ K + 2 has |g⁻¹(K_n, K_n)| ≥ c(N) > 0 on the overlaps (Lemma C); (iii) the non-radial waves are
torus-polarised (Lemma P), and the transport of Ψ_A = □̃φ_A closes (Lemma Ψ). Then FAMILIES5-FULL Part II's extension of
Theorems A₂, E₂ and D₂ (deduced, conditional on (i)-(iii); here its (ii) is (ii′), see Lemma C) gives vacuum metrics
g^(N)_λ on Ω, λ ≤ λ0(N), with |g^(N)_λ − g^(N)| ≤ C(N) λ and ∂g^(N)_λ − ∂g^(N) = Σ_A (bounded profiles in a_A u_A/λ) +
O(C(N) λ). Diagonal ([HL25] p. 19, Steps 1-3): fix a countable dense set (η_j) of L² test fields; choose λ_N ≤ λ0(N) with
C(N) λ_N ≤ 1/N, |∫ η_j (∂g^(N)_λN − ∂g^(N))| ≤ 1/N for j ≤ N (non-stationary phase: each harmonic's integral is O(λ) at
fixed N, its phase being non-null, hence non-constant), and ‖∂g^(N)_λN‖_(L²) ≤ ‖∂g^(N)‖ + (Σ_A ∫ F_A² |du_A|²)^(1/2)
+ 1 (the cross terms of distinct harmonics vanish as λ → 0 at fixed N, and the diagonal terms are the label quadrature
of the Vlasov energy, bounded uniformly). Then g_N := g^(N)_λN → g uniformly and ∂g_N, bounded in L² and convergent
against a dense set, converges weakly to ∂g. ∎

**Corollary V1 (Part I with a restricted Vlasov field; deduced).** Part I's background on the adapted Ω₂ (FAMILIES5-AXIS
Corollary N′1), carrying a small restricted Vlasov field in label form whose tubes stay off the axes and have no
caustic on Ω₂, is a weak limit of class vacuum metrics. (The background exists by Proposition U's argument with the
continuum of labels, Theorem N′ for the radial pair; (V3) holds by openness.)

### 2.1 Proposition U: the background is uniform in N (deduced; computed H6)

Let g^(N) be the class Einstein–N-dust solution whose families are the labels ω_A = 2πA/N with weights 2π/N: data q_A =
(2π/N) q(·, ω_A) and u_A = u_(ω_A) on Σ_τ0, the metric data corrected to satisfy the constraints with T^(N) := (2π/N) Σ_A
q_A du_A ⊗ du_A [R6 nit: one weight only, T^(N) := Σ_A q_A du_A ⊗ du_A] (the record's solve under (V3); the
correction is of the size of T^(N) − T_V on Σ_τ0). Then for N ≥ N0,
g^(N) exists on Ω and ‖g^(N) − g‖_(H^(m+1)(Σ_τ)) + ((2π/N) Σ_A ‖(p_A, θ_A, q_A/(2π/N)) − (p, θ, q)(·, ω_A)‖²_(H^m))^(1/2)
≤ C_k N^(−k), C_k independent of N.

*Proof.* The sampled continuum (p, θ, q)(·, ω_A), with g, solves the N-system's transports (A2)-(A4) exactly and (A1)
up to the residual E_N := T_V − T^(N)[g], the periodic trapezoid rule's error for an integrand smooth in ω: |∂^j E_N| ≤
C_(j,k) N^(−k) (computed H6 (a): faster than any power; a kink gives N⁻², rejected). Theorem N's energy for the
difference, with the family norms weighted by 2π/N (an ℓ² sum), closes with N-independent constants: the source of the
metric equation is (2π/N) Σ_A (ς_A p_A p_A + q_A(π_A p_A + p_A π_A)), bounded by Cauchy–Schwarz by C times the
weighted family norm; each family's transport depends on the others only through the metric and through Ric(P_A, P_A) =
(2π/N) Σ_B q_B g⁻¹(p_A, p_B)², a quadrature bounded the same way; every other term is Theorem N's, per family, with
constants uniform in A because the sampled families are uniformly smooth in ω. Gronwall and the bootstrap give the
bound for N ≥ N0. ∎ (Computed, a model, H6 (b): in a mean-field wave–transport model the N-label solution's error
falls with N and its ratio to the quadrature residual stays below 0.02 for N = 4, 8, 16; weights 2π/(N + 1) are
rejected.)

### 2.2 Lemma S: separation is kept by the flow (deduced; computed H5)

Under (V1), at every point y of Ω where labels ω, ω′ are present, |g⁻¹(du_ω, du_ω′)| ≥ c0 (ω − ω′)², c0 > 0 depending
on Ω and the family, not on N. *Proof.* Let Φ be the flow map (x0, ω) ↦ (y, α) of the null geodesics on the orbit
space's projectivised null bundle, α the momentum's angle in a frame. For fixed y the label's angle α(y; ω) has
∂_ω α|_y = det DΦ / det(∂y/∂x0) (Schur complement). DΦ is invertible (a flow composed with the initial section, ∂_ω β0 ≥
b) and det(∂y/∂x0) is bounded and nonzero (no caustic, compact Ω), so |∂_ω α| ≥ c1 > 0 with a fixed sign, and in 2+1,
g⁻¹(du_ω, du_ω′) = −E E′ (1 − cos(α − α′)). ∎ Computed (H5, the orbit space of Tangherlini): the Schur formula agrees
with shooting to 1.1 × 10⁻⁹, d α/d ω ≥ 0.80, and the least symbol/(Δω)² over adjacent labels is 0.2923, 0.2926, 0.2927,
0.2927 at N = 8, 16, 32, 64; control: ∂_ω α at fixed x0 disagrees. So the families of Proposition U are separated with
c = c0 (2π/N)², [HL25]'s η′ ≳ 1/N² (READ p. 18).

### 2.3 Lemma C: coherence after hierarchical rescaling (deduced; computed H4)

Pairwise separation is not enough for the every-order scheme. At stage m the residual carries the harmonics e^(i n·s),
|n|₁ ≤ m + 2, and a harmonic with two or more nonzero entries is divided by Q_n := g⁻¹(K_n, K_n), K_n = Σ n_A du_A. For
an antipodal pair and any third phase, K = k_a + k_b − k_c is exactly null in flat space (computed, H4's control): no
division removes it, and pairwise separation holds there. **Lemma C.** Let k_1, …, k_N be future null covectors at a
point of a 2+1 Lorentzian space with |g(k_A, k_B)| ≥ c (A ≠ B) and frame norms |k_A|² ≤ M², and a_A := Λ^(A−1). For
every n with two or more nonzero entries, |n|₁ ≤ m, T > S its two largest indices,

    |g(K_n, K_n)| ≥ 2 a_T a_S (c − 2m M²/Λ − m² M²/(2Λ)),        K_n = Σ_A n_A a_A k_A.

*Proof.* g(k_T, k_T) = 0, so g(K, K) = 2 n_T a_T g(k_T, V) + g(V, V), V the rest; g(k_T, V) = n_S a_S g(k_T, k_S) +
(terms with a_B ≤ a_S/Λ), each ≤ m M² a_S/Λ, and |g(V, V)| ≤ m² M² a_S² ≤ m² M² a_T a_S/Λ. ∎ So Λ > (2m + m²/2) M²/c
makes every combination non-null with margin; with c = c0/N² (Lemma S) this is [HL25]'s a_A = cN² a_(A−1) (READ p. 18).
The phases a_A u_A are eikonals, so the two-scale scheme is unchanged, the profile of family A carrying the amplitude
λ F_A/a_A. Computed (H4, exact): over every n with |n|₁ ≤ 5 (N ≤ 4) for four random rational configurations the bound
holds; control (Λ = 1): the antipodal resonance g(K, K) = 0.

### 2.4 Lemma P: the torus polarisation (deduced; computed H1, H2)

A family's wave is torus-polarised when it oscillates only in ψ1 − ψ2: δψ1 = −δψ2 = λ a cos(u/λ), h unperturbed.
(a) For any phase, the λ⁻¹ part of Ric on the orbit block is (a1 + a2) cos(s) du ⊗ du, the mixed components vanish, and
the λ⁻¹ part of E_i := −Ric_ii/g_ii is −a_i g⁻¹(du, du) cos s (H1 (a)-(b), exact at three random points of a general
class metric). So with u null and a2 = −a1 the whole λ⁻¹ part of Ric vanishes with h unperturbed. (b) The sin s part of
E_i at λ⁰ is −[2⟨da_i, du⟩ + a_i(□_h u + ⟨du, dσ0⟩) + A⟨dψ_i0, du⟩], A = a1 + a2 (H1 (c)); summed over i, A obeys the
homogeneous transport 2ℓ(A) + A(□_g u + ℓ(σ0)) = 0: A = 0 is kept (deduced). (c) The constraints' λ⁻¹ coefficient is,
for every slow (h, k), on a non-round class slice with a non-radial phase and for a generic wave, the record's formula
dρ⁽⁻¹⁾ = −2⟨h, p ⊗ W″p⟩ + h(p, p) tr W″ + |p|²⟨h, W″⟩, dJ_i⁽⁻¹⁾ = 2(h^jk p_j K1′_ki − p_i h^jk K1′_jk) (H2, exact);
for torus-polarised waves and the record's corrections (h = a dR², any k) both vanish, since W″ lives on the torus
block and h, p on the orbit block. (d) The mean of the quadratic term is ½(a1² + a2²) du ⊗ du = a² du ⊗ du: every
density F_A² is realised. Control (H2): the other polarisation (an orbit component α q ⊗ q, q ⊥ p) gives dρ⁽⁻¹⁾ =
|p|² a α (q^R)² ≠ 0 for h = a dR² whenever the phase is not radial; the formula with its first sign flipped is rejected.

### 2.5 Lemma Ψ: the orbit space has no shear (deduced; computed H3)

For u null to first order on a 2+1 Lorentzian h, ⟨Hess_h u, S⟩_h = (□_h u) tr_h S for every symmetric S with S(ℓ, ·) = 0
(H3, exact at three random jets; the transverse space is one-dimensional). So the map S ↦ ⟨Hess u, S⟩ − θ_h tr S
factors through S ↦ S(ℓ, ·), and for invariant φ, whose torus Hessian is first order (classchi5 C1),
[□, ℓ·∂]φ = 2θ_h □φ + (derivatives of ℓφ) + (first order in φ). This is FAMILIES5-FULL (F6) with a_K = 2θ_h for a
non-radial family on a non-round background; the record's derivation used shear-free generators. Controls: in 3+1 the
identity fails (shear); with the Christoffel term dropped it fails.

### 2.6 Proposition Ax and the obstructions (computed; deduced)

**Proposition Ax.** If a restricted Vlasov field, smooth on the orbit space's null bundle off the axes, has in its
support a momentum whose orbit geodesic reaches an axis at a point of Ω transversally (not along the axis), its
five-dimensional density is ≥ c/ρ2 near that point, so T and Ric are unbounded and the solution is not C² there.
*Proof.* √|g5| = √|h| e^(ψ1+ψ2), so a restricted current J is conserved in five dimensions iff e^(ψ1+ψ2) J is conserved
on the orbit space (H7 (a), exact); the orbit-space density is transported by a flow smooth across the edge (the
meridional plane's flow, the metric even in ρ2), so it is bounded below near the arrival, while e^(ψ2) = √a ρ2 (1 +
O(ρ2²)) (axisloss5 X1 (a)). In the plane of the axis the restricted momenta are radial, and the planar continuity
equation gives r n(r, t) → v t n0(v t) > 0 as r → 0 (H7 (b), exact), with the non-smooth x̂ ⊗ x̂ stress (vlasov5 V2's
control); axial momenta (control) stay bounded. ∎ So (V2) is necessary for smooth solutions; with V2-V3 of vlasov5, the
axes enter a smooth restricted field only through the two radial (axial) dusts.

**Obstructions (each proved).** (O1) At an axis point every invariant null phase has gradient along ±x̂ (axisphase5 A1,
computed): among the families present there at most one is ingoing and one outgoing, and two of one orientation have
g⁻¹(du_A, du_B) = 0 there. (O2) Proposition Ax. (O3) Without the frequency hierarchy, three families with an antipodal
pair resonate exactly (H4). (O4) With the record's radial correction a non-radial family in the second polarisation
leaves a λ⁻¹ coefficient (H2). Theorem V is built so that none applies: labels off the axes, radial pair at them,
frequencies 1, Λ, …, Λ^(N−1), torus polarisation.

## 3. (a) Rácz's split on Part I's whole slice (computed: racglobal5 R1, R2)

- **R1.** From twobg5's double-null solution at n = 40, 80, 160 (ψ_R = ℬ/(3R²R_u²), ψ_v̂, μ_R, μ_v̂ through twobg5 G1
  (a)-(c)), N_k on all of Σ_τ0 ∩ Ω₂ (R from 0.683 to the grid's edge 5.882; beyond it Tangherlini of mass 3.6057, N_k =
  (μ/R³)(f − 3) < 0): N_k < 0 except on R ∈ [4.2956, 4.5264] at n = 160 ([4.3017, 4.5204] at n = 80), max N_k = 1.7925
  × 10⁻³ at R = 4.3994; E f ≤ 0.9052 < 1 throughout. Controls: with the flux term −E f_v/2 dropped max N_k = −0.036;
  with half the shell's amplitude −0.017. The region-I formula agrees with the grid to an error falling at second
  order.
- **R2 (exact).** In ingoing Vaidya N_k = (μ/R³)(f − 3) + μ′(v̂)/(2R²): hyperbolic iff μ′ < 2μ(2 + μ/R²)/R. Where N_k >
  0, κ < 0 and K^l_l < 0 with K round, so K is negative definite; for every unit normal n̂ of every foliation, κ′ =
  K(n̂, n̂) < 0 and K′^l_l = tr K − κ′ = sin²β κ + (3 − sin²β) K^l_l/3 < 0, so κ′K′^l_l > 0: [Rac16] Lemma 4.1 fails
  for every foliation. Control: a K of mixed sign has a hyperbolic tilt.

**Proposition L (amended [R5]).** [R7 (the round-6 verifier's m6): superseded by FAMILIES5-R6 Theorem L″, which has no
radial restriction.] As FAMILIES5-AXIS Proposition L, for a perturbation supported in {R1 < R < R2, θ1 < θ < π/2 − θ1}
with [R1, R2] disjoint from the band B = [4.29, 4.53]: solved inward from R2 to a when R2 < 4.29, outward from R1 to
b(τ0) when R1 > 4.53 (the split is hyperbolic on those intervals, R1). Existence on the whole interval: Theorem K's
Cauchy stability [R7: Theorem K′, FAMILIES5-R6 section 5] around the background, which solves the system there ([Rac16]
Theorem 4.3 is local in existence only); the constraints hold identically ([Rac16] p. 12: the system and (4.17) are the
constraints); the support widens by Δ(R) = ∫c dR + O(ε) (finite speed). **Perturbations meeting B** are posed on the
outgoing cone N (B6: exact localisation, any amplitude) [R6: the localisation holds for any amplitude; carrying the cone
data to Σ_τ0 is Cauchy stability and needs small data], evolved by the characteristic problem ([Wu26] Theorem 2.1, READ
in the record) to Σ_τ0, where they are supported in the band widened by the angular light-cone spread, R|dΩ/dτ| ≤ 1
(augment5 S7).

## 4. (b) Exact compact support (READ; computed: racglobal5 R3, R4)

**Proposition L′ (deduced from [CS06] Theorem 2 and [CD03] Theorem 5.6, READ, with R3).** Let U be an invariant band
compactly contained in a vacuum region of Part I's Σ_τ0 (seed, gap, outside the shell) and εδ a small invariant seed
supported in U. There is an invariant correction c = O(ε²), supported in U, such that background + εδ + c satisfies
the vacuum constraints up to a multiple m(ε) of the (weighted) static KID; m(ε) = ε² Q(δ) + O(ε³). *Proof.* [CD03]
solves up to the projection on ker P* ("whatever the space-dimension n", p. 4). Equivariance: the variational solution
is unique and the problem invariant under the isometries T² × Z2 × Z2 of the background data, so the solution is
invariant and only invariant KIDs project. In a vacuum region KIDs are Killing fields ([CD03] p. 33); the invariant
Killing fields of Tangherlini are the multiples of ∂_t (R3, exact: X^R = X^θ = 0 from the torus components, then X^t
constant; ∂_φi are odd under the reflections), with lapse N_s = e^(−ψ)/√(2e^(−ψ) − f) > 0 on Part I's slice (R3). For
any compactly supported perturbation, ⟨(N_s, Y_s), DΦ(·)⟩ = ⟨P*(N_s, Y_s), ·⟩ = 0, so the projection of Φ(background +
εδ + c) − Φ(background) is ½ ε² ⟨(N_s, Y_s), D²Φ[δ, δ]⟩ + O(ε³) = ε² Q(δ) + O(ε³). ∎ The same computation shows: **if
Q(δ) ≠ 0, no data of the form background + εδ + O(ε²), supported in U, satisfy the vacuum constraints for ε small**;
if Q changes sign on a one-parameter family of seeds, exactly localised data exist (intermediate values, the solution
depending continuously on the seed, [CS06] Theorem 2).

**The charge (computed, R4).** For bandconst5 B4's compactly supported linear data (δγ = 0, a stream function), the
momentum constraint is linear in K at fixed γ and contributes nothing, so Q = ∫_U N_s((tr δK)² − |δK|²) dvol. Pointwise
on Tangherlini (exact) (tr δK)² − |δK|² = (2/(3(2 − f))) δKt² − 2δp² − 2δs2², and the momentum constraint's δs2 makes Q
negative: Q < 0 for all 45 seeds (three bands, one inside the horizon; frequencies 2, 6, 24; five directions); without
the −2δs2² term a θ-seed gives Q > 0 (control). So none of these seeds completes to exactly localised vacuum data, and
adding dust in U does not help: the condition becomes ε²Q = 2∫N_s δe with δe ≥ 0. [R6: withdrawn inside the
horizon; Theorem Q′ (FAMILIES5-R6 section 1.4): the pairing is ∫T(ξ, n), which outgoing null dust makes negative
inside the horizon; marker added in round 7, the round-6 verifier's m5.] Exact compact support is therefore
not obtained here; band localisation (Proposition L) and exact localisation on cones (B6) are what this note proves.
(The sign is what positive energy of a localised perturbation would give; that interpretation is not used.)

## 5. (c) Part II's (ii) and (iii)

- **(ii) at the axes, any number of families (deduced from A1, computed):** (O1). A family set is separated at the axes
  iff, at each axis point, its families present there consist of at most one ingoing and one outgoing family; every
  other family must vanish near that point. A smooth restricted Vlasov field meets this automatically (Proposition Ax).
- **(ii) for three or more families (correction to FAMILIES5-FULL Part II, [R5]):** pairwise separation does not give
  the every-order division (O3); the condition is (ii′): pairwise separation on the overlaps and the frequency hierarchy
  of Lemma C, which then gives |Q_n| ≥ c(N) for every combination up to the order needed.
- **(iii) (computed H1, H2; deduced):** settled by Lemma P. The second polarisation is obstructed for the record's
  radial correction (O4) and is not needed.

## 6. (e) The standard results, proved in the needed versions

**Theorem K (Kato's iteration with a non-local source).** Let s > d/2 + 1 be an integer, A^0, A^j smooth symmetric
matrix functions of (t, x, u) with A^0 ≥ c0 I, and F a map from H^s(R^d) to H^s(R^d) such that (K1) ‖F(t, u)‖_(H^s) ≤
C(M) for ‖u‖_(H^s) ≤ M, (K2) ‖F(t, u) − F(t, v)‖_(L²) ≤ L(M) ‖u − v‖_(L²) for ‖u‖_(H^s), ‖v‖_(H^s) ≤ M, (K3) t ↦ F(t,
u(t)) is continuous into L² when u ∈ C([0, T]; L²) ∩ L^∞H^s. Then for u0 ∈ H^s there is T* > 0, depending only on
‖u0‖_(H^s), and a unique u ∈ L^∞([0, T*]; H^s) ∩ Lip([0, T*]; L²) with A^0(u)∂_t u + A^j(u)∂_j u = F(t, u), u(0) = u0;
the solution continues as long as ‖u(t)‖_(H^s) stays bounded; and the same holds on a domain of the record's type with
spacelike lateral boundaries (the record's Step 8 (i), (iv) extension).
*Proof.* Iterate A^0(u^n)∂_t u^(n+1) + A^j(u^n)∂_j u^(n+1) = F(t, u^n), u^(n+1)(0) = u0. (Boundedness) The H^s energy
of the linear symmetric hyperbolic problem obeys d/dt E_s(u^(n+1)) ≤ C(M)(E_s(u^(n+1)) + ‖F(u^n)‖_(H^s) E_s^(1/2)), the
commutators [∂^α, A^j(u^n)]∂_j bounded by Moser's estimate (s > d/2 + 1); with (K1), ‖u^n‖_(H^s) ≤ M on [0, T*] for all
n. (Contraction) w := u^(n+1) − u^n solves the same linear problem with source −(A^0(u^n) − A^0(u^(n−1)))∂_t u^n −
(A^j(u^n) − A^j(u^(n−1)))∂_j u^n + F(u^n) − F(u^(n−1)), whose L² norm is ≤ C(M)‖u^n − u^(n−1)‖_(L²) by (K2): the L²
energy estimate gives a contraction for T* small. (Limit) u^n → u in C([0, T*]; L²), hence in C H^(s′) for s′ < s
by interpolation, u ∈ L^∞H^s by weak-* compactness, and the limit solves the equation, F(u^n) → F(u) in L² by (K2).
Uniqueness is the same L² estimate; continuation because T* depends only on M. Locality of F is used nowhere. ∎
[R6 (the round-5 verifier's Major 3): true on R^d; the domain version needs F on Σ_t ∩ Ω to depend on u there only,
and the uses need Cauchy stability over the background's interval, which needs a tame bound: Theorem K′, FAMILIES5-R6
section 5.]
([IT20] Theorem 1, READ in the record, is the case A^0 = I, F = 0.) Computed (a model, katonl5 K1): for u_t + (1 +
u)u_x = −(1 − ∂_x²)⁻¹(u²) the iteration's differences fall by ratios ≤ 0.11 and the H² norms stay at 2.40 ± 5 %;
control: the source 0.5 u_xx (not L²-Lipschitz) makes the H² norms grow from 2.07 to 230.

**Lemma E (interior regularity, two variables).** Let L = a^ij ∂_ij + b^i ∂_i + c on the disc D_2δ, a^ij, b^i, c ∈
C^∞(D̄_2δ), a^ij ξ_iξ_j ≥ λ|ξ|². For w ∈ H¹(D_2δ) with Lw = f ∈ H^k(D_2δ), ‖w‖_(H^(k+2)(D_δ)) ≤ C(‖f‖_(H^k(D_2δ)) +
‖w‖_(L²(D_2δ))). *Proof.* For k = 0: test the equation against −∂_h^(−e)(ζ² ∂_h^e w), ζ a cut-off and ∂_h^e the
difference quotient, use ellipticity and Cauchy–Schwarz to bound ‖ζ ∂_h^e ∇w‖ uniformly in h, so ∇²w ∈ L²(D_(3δ/2))
(Nirenberg's method). For k ≥ 1: ∂w solves L(∂w) = ∂f − (∂a^ij)∂_ij w − (∂b^i)∂_i w − (∂c)w, whose right side is in
H^(k−1) by the case k − 1; induction on nested discs. ∎ Computed support: axisellip5 E2, which measures the leaf map's
L²- and H¹-ratios on a curved metric.

**Lemma A′ (Lemma A in the two forms Theorem N′ uses; deduced from Lemma E and E0-E1).** Let ů's leaves be h̊ and U be in
an H^m ball (m ≥ 6) near ů. (a) ‖∂^α(s[U] − s[ů])‖ ≤ C N_m for |α| ≤ m: the difference δh of the leaves solves L_ů δh =
δH2 − (δγ3 terms, first derivatives of δg) + Q(δh), L_ů the linearised mean curvature operator at h̊ (smooth, uniformly
elliptic on the disc, the axis interior: E1 (b)), Q quadratic; Lemma E with k = m. The shift of the foliation δc enters
as (∂_c s[ů]) δc, the derivative falling on ů. (b) ‖s[U] − s[U′]‖_(L²) ≤ C(M) ‖U − U′‖_(L²) on the ball: Lemma E with k
= 0 for the difference, the foliation shift costing ∂_c s, bounded on the ball. These are (K1)-(K2) for Step 9's
source, and the bound Step 6 needs. The constant uses C¹ norms of u and L^∞ of θ, not C² of u (h′ from H2 by (V)), so it
is not circular (the verifier's minor 5).

## 7. What is proved, and what is not

- Theorem V and Corollary V1: deduced; every identity computed (H1-H7, R-checks, twoscale5); the N-family extension of
  Theorems A₂, E₂, D₂ is FAMILIES5-FULL Part II's, deduced at the level of its sections 4-6, with (ii) replaced by (ii′)
  and (F6) by Lemma Ψ.
- Proposition U: deduced; the rate computed (H6 (a)); N-independence computed in a model (H6 (b)).
- Lemmas S, C, P, Ψ: deduced; computed (H5, H4, H1-H2, H3). Proposition Ax and (O1)-(O4): computed (H7, A1, H4, H2).
- (a): computed (R1, R2); Proposition L amended: deduced.
- (b): Proposition L′ deduced from READ statements and R3; the charge's sign on the stream-function seeds computed (R4).
  Exact compact support of nonlinear vacuum data is not obtained.
- (e): Theorem K, Lemma E, Lemma A′: proved here (deduced; the iteration computed in a model, katonl5). Kato 1975 and
  the textbook regularity theorems: not READ.
- Not independently read: this note.

## 8. The verifier of round 4: findings and dispositions [R5 verifier of round 4]

Re-derived before seating. Confirmed by the verifier: the five programs rerun byte-identically, mutations caught; E0
(the Gauss formula, any u; tr χ̸ = θ − κ1 for u null to first order); (V) regular at the axis, indicial root −2; Lemma
A's lossless count; [Rac16] quotes; Corollary N′1's geometry; the fifteen NONROUND amendments. Each finding is seated
in FAMILIES5-AXIS.md as an [R5 verifier of round 4] amendment at the place it concerns.

- *MAJOR 1 (Vlasov "axes included" not shown).* Accepted and proved the other way: Proposition Ax (H7) shows restricted
  particles reaching an axis focus there; FAMILIES5-AXIS's claim for Vlasov is withdrawn and replaced by Theorem V's
  hypothesis (V2), which smooth solutions satisfy.
- *MAJOR 2 (the proposed §9 overclaims).* Accepted: the replacement text below says "Cauchy-stable on compact domains
  of the record's type", states no caustics, the adapted lateral boundaries with one family at each boundary–axis point
  and the support conditions, "the adapted domain", the labels, localised data only where shown, "restricted" only for
  limits, and drops the N² remark.
- *Minor 1 (Theorem N′ Step 6, families B ≠ A at an adapted boundary).* Accepted (re-derived: the leaves of family B
  can cross B's adapted boundary at O(ε)): χ_B = 0 near boundary–axis points for B ≠ A ((H2′) puts no B-dust there), and
  Step 10's d_B energy is taken on a leaf-saturated set inside {χ_B = 1}.
- *Minor 2 (Step 9).* Accepted: Lemma A′ (b) gives (K2), Lemma A (a) (K1), Theorem K the existence; [IT20] Theorem 1 is
  READ for ∂_t u = A^j(u)∂_j u with no source (corrected); the source on the R⁴ extension is χ_A S^ax with the near-axis
  leaves defined by u_A's values on the axis (transported along it) and (V) from θ_A, so p_A need not be closed.
- *Minor 3 (Corollary N′1's support conditions; R_H).* Accepted: supp F_shell ⊂ {v̂ ≤ v_end + η} near the outer
  boundary's axis points and the packet's support in R ≥ R_H + 0.6 near the inner one are added; R_H ≥ 0.906
  (μ_III ≥ 0.82207, √0.82207 = 0.9067).
- *Minor 4 ([Rac16] Theorem 4.3 local; B1, B2 wording).* Accepted: section 3 and the bandconst5 docstring (B1's real
  speeds are the θ-only symbol's; B2's equivalence needs E f < 1).
- *Minor 5 (Lemma A's circular constant).* Accepted: Lemma A′'s constant uses C¹ of u and L^∞ of θ.
- *Minor 6 (E2).* Accepted: E2's ratios are frozen-coefficient limits (1/(2√3) is the flat Gaussian value); the
  reconstruction now starts from h′(r0) = 0 and recovers h′ to 4.1 × 10⁻¹¹ and σ to 8.0 × 10⁻¹⁰ (axisellip5 rerun).
- *Minor 7 (why curvature drops out).* Accepted: on a surface of revolution k_φ = ν(log √g_φφ), the Killing identity
  (as Proposition C), so the recovery avoids Codazzi and Ric_M3; E0 (the Gauss formula) alone does not exclude them.
- *Nits.* Accepted: B5's 4.0 × 10⁻⁹ is qualitative (ten implicit-Euler steps); X3's ‖Af‖ = ‖f‖/√2 holds for the
  Gaussian family, only ‖s‖ = ‖f‖ is an identity; ‖χ̸̂‖ = |s|/√2 counted once; "K_rr − K_φφ" has r the leaf tangent; B6's
  "no smallness" concerns localisation, not existence of cone data; Lemma A takes m ≥ 5 within Theorem N's m ≥ 6;
  (H2′) is vacuous where no dust meets a boundary–axis point.

## 9. Proposed replacement for the paper's section 9 item "More families" (14 lines)

[R6: superseded by FAMILIES5-R6.md section 8, which folds in the round-5 verifier's Minor 10.]

> - **More families.** In the class each family's null second fundamental form is diag(θ_h, κ1, κ2), the torus terms
>   first order, and at an axis the remaining planar shear is recovered elliptically from the expansion. So the
>   Einstein–null-dust system in the class is Cauchy-stable on compact domains of the record's type, without
>   smallness, for dusts without caustics whose lateral boundaries are adapted (one family) where they meet an axis
>   (deduced; supplement `docket68/n1star/FAMILIES5-AXIS.md`). A restricted massless Vlasov field, the only kind a
>   limit in the class can carry, never reaches an axis off the axial directions in a smooth solution: there its
>   density grows like 1/ρ2. Every smooth class solution of Einstein–restricted massless Vlasov whose field is a
>   caustic-free family of dusts labelled by initial direction, off the axes, on such a domain with data meeting the
>   record's open conditions, is a weak limit of class vacuum metrics (deduced: N-dust approximants uniform in N, then
>   torus-polarised waves at frequencies 1, Λ, …, Λ^(N−1), which leave no combination of phases resonant, and a
>   diagonal choice of λ_N, as Huneau and Luk do; supplement `FAMILIES5-VLASOV.md`, identities computed, not yet
>   read independently). At an axis point at most one ingoing and one outgoing family are separated. Data localised
>   in an angle exist on cones exactly, and on Part I's slice in a widened band where Rácz's split is hyperbolic: all
>   of it but a band inside the shell, where the extrinsic curvature is negative definite and no foliation is (computed).

## Files

`FAMILIES5-VLASOV.md` (this note). New, each with its `.out`: `checks/vlasovhf5.py` (H1-H7, a few minutes),
`checks/twoscale5.py` (T1, seconds), `checks/racglobal5.py` (R1-R4, a few minutes), `checks/katonl5.py` (K1, seconds),
`checks/h3proof5.py` (about a minute). Repaired, `.out` regenerated: `checks/axisellip5.py` (E2 from h′(r0) = 0),
`checks/bandconst5.py` (docstring), `checks/twotransport5.py` (T1 compared), `checks/torusstress5.py` (V3, V4),
`checks/twobg5.py` (G3's independent check), `checks/twodecomp5.py` (wording). FAMILIES5-AXIS.md: [R5] amendments.
FAMILIES5-FULL.md: repaired in place, its section 12.

## 10. Round 6

In `FAMILIES5-R6.md`: R6.0 (the round-5 verifier's findings, each re-derived and seated), the charge's sign (Theorem
Q, Q′), the band crossed (Theorem L″), Theorem V's hypotheses (Lemma O, Proposition NE), the N-family step (D₂_N),
Theorem K′, and the proposed section 9 text.
