# FAMILIES5-FULL -- two crossing families in full; several families in the class; Vlasov

Status (2026-11-02). Part I: the two-family counterpart of the record's Theorem 1 (Theorem 1₂) is **deduced** here, from
the record's proof (N1STAR-PROOF.md sections 1-6), FAMILIES5.md sections 4b-4i, and six new programs; it has **not been
read by an independent verifier**, and items 6-7 of the record's Theorem 1 (horizon, mean mass) are not claimed for it.
Part II: which null phases the T² class permits is **computed**; that angular separation in Huneau and Luk's sense fails
at the axes for any two families of the same orientation is **computed**; the background for more than two (necessarily
non-round) families is **open**, with the obstruction stated. Part III: the literature is **READ** at source; the 5D
T²-class reduction of the Vlasov passage to Part I is **deduced** with its identities computed; the non-round case is
**open** and stops at Part II's obstruction. Nothing in FAMILIES5.md, the paper or the log is changed.

Labels as in the record: **computed** (a program `checks/<name>5.py` with a `.out` and a negative control that the
program must reject), **deduced** (argued here, a standard step named as such), **READ** (verbatim, identifier and page,
read at source through alphaXiv, 2026-11-02). New programs: `checks/twobg5.py`, `checks/twoslice5.py`,
`checks/nonres5.py`, `checks/twotransport5.py`, `checks/axisphase5.py`, `checks/torusstress5.py`, each with its `.out`.

---

# Part I. Two crossing families: one ingoing, one outgoing

## 1. The statement

**Data (stated).** Let l5, μ0 ≥ √72 l5², A > 0, env ∈ C_c^∞([v_start, v_end]) and τ0 with v_start − τ0 > √μ0 + 1 be the
record's. Add an outgoing family: A₂ > 0 and env₂ ∈ C_c^∞((u1, u2)). The **background's characteristic data** are
explicit Vaidya data on two null cones, both in the past of Σ_τ0:

- on the ingoing cone N′ = {v = v0}, v0 < τ0 + a, before the shell: Tangherlini of mass μ0 (the seed) for u ≥ u2,
  outgoing Vaidya g = −(1 − m(u)/r²) du² − 2 du dr + r² dΩ₃² across the packet [u1, u2], with dm/du = −(2/9) A₂²
  env₂(u)² (the record's Isaacson law (2.6) for the outgoing wave, u the retarded Eddington–Finkelstein time there), and
  Tangherlini of mass μ0 + E₂, E₂ := (2/9) A₂² ∫ env₂², for u ≤ u1; the packet is required to lie where N′ is
  untrapped (r² > m). In double-null form these are the solutions along N′ of the Raychaudhuri constraint with K_out R³
  = ℬ(u) = (1/3) A₂² env₂² in that normalisation (twodust5 B1, B3);
- on the outgoing cone N = {u = u0}, u0 < u1, outside the packet: **ingoing Vaidya** with dμ/dv = (2/9) A² env²,
  μ = μ0 + E₂ before the shell.

Equivalently (deduced from Proposition B(a)): the Cauchy data on Σ_τ0 are the seed's for R < r1, outgoing Vaidya on the
packet [r1, r2], Tangherlini of mass μ0 + E₂ between the packet and the shell, and the record's shell outside; the packet
is chosen with √μ0 < r1 < r2 < v_start − τ0, so that it lies **between the seed's horizon and the shell** on Σ_τ0 and the
two families cross in the future of Σ_τ0 (computed example: `checks/twobg5.py` G2 (vi)). The outgoing family's waves are
the record's W_TT with phase u/λ and envelope env₂, posed on Σ_τ0 (their rays, traced back, run inward to the past
horizon, so they cannot be posed at past null infinity: FAMILIES5.md 4i, D568).

**Theorem 1₂ (deduced; sections 2-6).** With these data and K ≥ 6 there are λ0 > 0 and C, independent of λ, such that
for every λ ∈ (0, λ0] there is a smooth T² × Z2 × Z2-invariant metric g_λ on the two-dust domain Ω₂ (section 2) with:

1. Ric(g_λ) = 0 on Ω₂;
2. on Σ_τ0 the data satisfy the vacuum constraints exactly, equal the seed's on R < r1, and differ from those of the
   two-phase approximant g_app by O(λ^K) in the record's norm (E4);
3. g_λ = g_app + w, |w| ≤ C λ^(K−3), |∂w| ≤ C λ^(K−4) on Ω₂;
4. |g_λ − g0| ≤ C λ, |∂g_λ| ≤ C, and ∂g_λ − ∂g0 = dv ⊗ [∂_(s1) g1^in] + du ⊗ [∂_(s2) g1^out] + O(λ), so ∂g_λ → ∂g0
   weakly in L² and not strongly where env or env₂ is nonzero; g0 is the **two-null-dust background** of section 2,
   Ric(g0) = K_in dv² + K_out du² with K_in R³ and K_out R³ the two families' Isaacson fluxes;
5. D(g_λ) = 0 (the record's wave-map gauge relative to g0) and g_λ is the only C² solution of Ric^H(g) = 0 on Ω₂ with
   data within ε1 of g0.

*How it follows* (deduced): exactly as the record's Theorem 1 (N1STAR-PROOF.md 0.7) from Proposition B (the background
and the domain, section 2), Theorem A₂ (the approximant, section 4), Theorem E₂ (the uniform estimate, section 5) and
Theorem D₂ (the data, section 6). D(g_λ) = 0 and the symmetry follow from the record's argument word for word: the
contracted Bianchi identity is an identity in g and g0 (`paper/response5.py` R14), and Ric^H, D are built from g and the
O(4)-invariant g0 (the two-dust background is round: twodust5 B1).

## 2. The background on the whole domain (Proposition B)

Notation (FAMILIES5.md 4c, 4i): g0 = −2 e^(2s) du dv + R² dΩ₃², K_in R³ = 𝒜(v), K_out R³ = ℬ(u), 𝒜, ℬ ≥ 0, μ := R²(1 + 2
e^(−2s) R_u R_v) the Misner–Sharp mass; v̂ the ingoing coordinate with ψ = 0 on N (region I), τ := v̂ − R, x := R x̂, and
g0 = −e^(2ψ) f dv̂² + 2 e^ψ dv̂ dR + R² dΩ₃², f = 1 − μ/R² (twodomain5 D1).

**Proposition B.** (a) *Structure (computed: twobg5 G1 (a)-(b), G2 (i)).* μ_u = −(2/3) ℬ e^(−2s) R_v and μ_v = −(2/3) 𝒜
e^(−2s) R_u; ψ_u = ℬ/(3R² R_u), and the mirror ψ̃_v = 𝒜/(3R² R_v). So where ℬ = 0 the background is ingoing Vaidya in
(v̂, R) after reparametrising v̂, and where 𝒜 = 0 (and R_v ≠ 0) outgoing Vaidya: the only region where it is not explicit
Vaidya is the compact crossing diamond Q× = [u1, u2] × [v_start, v_end]. In the example the departures from Vaidya off Q×
fall with resolution (1.8 × 10⁻⁵, 5.2 × 10⁻³, 5.2 × 10⁻³, 2.2 × 10⁻⁴ at n = 160 in the four regions, each falling with
n).

(b) *The mass bound μ ≥ μ0 on the whole development (deduced; computed G1 (c), G2 (ii)).* μ_uv = (2/9) 𝒜ℬ e^(−2s)/R² ≥ 0
(twoext5 X2, recomputed G1 (c)), so μ(u, v) ≥ μ(u, v0) + μ(u0, v) − μ(u0, v0). The second difference is ∫ μ_v ≥ 0, R_u
being negative (c). On N′, μ(·, v0) = m(u) decreases from μ0 + E₂ to μ0 across the untrapped packet and is μ0 inside
it. Hence μ ≥ μ0. (Computed: the least of μ − μ0 over R ≥ a is −4.0 × 10⁻², −9.9 × 10⁻³, −2.3 × 10⁻³ at n = 40, 80, 160,
a discretisation deficit falling at second order. Control: with ℬ → −ℬ, 𝒜ℬ < 0, the deficit is −0.648 at both n, so the
bound fails.) This is where the choice of data matters: FAMILIES5.md 4i (D546-D549, D4) had the packet *outside* a hole
of fixed mass, which lowers the interior mass and can untrap R = a; with the packet inside the shell and outside the seed
the interior mass is the seed's and the outgoing dust can only add to it.

(c) *R_u < 0, the inner sphere and past-closedness (deduced; computed G2 (iii)-(iv)).* (e^(−2s) R_u)_u = −e^(−2s)ℬ/(3R²)
≤ 0 and R_u < 0 on the data, so R_u < 0 everywhere (twodomain5 D1). With a < q0 = r_q(μ0) ≤ √μ0 (the record's seed
condition), μ ≥ μ0 > a² makes {R = a} trapped and spacelike, with Ω₂ to its past (g0⁻¹(dR, dR) = 1 − μ/a² < 0; twodomain5
D2's (b) now holds **unconditionally**). Past-closedness: if R(p) ≥ a then R ≥ min(R(p), √μ0) ≥ a on J⁻(p). *Proof.* For
q = (u_q, v_q) ≤ p, R(q) ≥ R(u_p, v_q) by R_u < 0. If R(u_p, v′) < min(R(p), √μ0) for some v′ < v_p, then there R² < μ0 ≤
μ, so R_v < 0 (trapped, as R_u < 0); let v″ be the supremum of the v ∈ [v′, v_p] up to which this persists: R decreases
on [v′, v″], so R(u_p, v″) < min(R(p), √μ0), and continuity forces v″ = v_p, contradicting R(p) ≥ min(R(p), √μ0). ∎ (On
the grid the margin is 0 at every n; R = a is crossed in every resolved column and trapped there with μ − a² ≥ 0.332; the
mass of region III, read on u = u2 + 0.1, is ≥ μ0 − 10⁻⁴ at n = 160.)

(d) *Existence on the whole domain (deduced).* FAMILIES5.md 4i (D558) solves the integral form of the 1+1 system for U =
(R, s, R_u, R_v) by a truncated Volterra iteration in the Bielecki norm on Q := [u0, ∞) × [v0, V1] (each single integral
divides the Lipschitz constant by γ, the double one by γ², on an unbounded u-interval as well), and shows the fixed point
solves the true system on Q_a := {p : R̃ > a on J⁻(p)}, given D552's a priori chain on {R ≥ a}. With (b) the chain
simplifies: s_uv = (3/2) e^(2s) μ/R⁴ ≥ 0 gives s ≥ D[s] with no hypothesis (D552's m0⁻ = 0), and the upper bounds on μ
and s follow from D552 (iv)-(v) on the bounded part of Q where R ≥ a′. Two points D558 left as sketches are written here.
*Regularity.* Let U be the continuous solution on a past-closed set. From the integral equations, R_u = P and R_v = Q
exactly (differentiate R = R(u0, v) + ∫ P du′ in v and use the Q-equation), P_v = F(U), Q_u = F(U), and s_u, s_v are
continuous; for ∂_u P, the difference quotients δ_h P solve δ_h P(u, v) = δ_h P(u, v0) + ∫_(v0)^v (a_h · δ_h(R, s, Q) +
b_h δ_h P) dv′, with a_h, b_h the mean values of ∇F on the segment, continuous and converging uniformly, and δ_h(R, s, Q)
→ (P, s_u, F) uniformly; Gronwall in v makes δ_h P uniformly Cauchy, so ∂_u P exists and is continuous, and likewise ∂_v
Q. So U ∈ C¹; the k-th derivatives solve linear Volterra equations of the same form with coefficients built from lower
derivatives, so by induction U ∈ C^∞ for smooth data. *Boundedness of the domain.* On N′, in the gauge s = const there
(twodomain5's cone()), R_uu = 0 for u ≥ u2, so R_u(u, v0) = c0 < 0 there; R_uv = −e^(2s) μ/R³ < 0 gives R_u ≤ c0 on
{u ≥ u2}, so {R ≥ a, v ≤ V1} has u bounded. With (c), Ω₂ below lies in Q_(a′) for a′ < a, and the background exists,
smooth, on all of it.

(e) *The domain and the record's Lemma 1.1 (deduced; computed twodomain5 D1-D2, twodt5 T1-T2, twotransport5).* Define
Ω₂ by the record's (1.1) with v̂, τ = v̂ − R and R in place of v, τ, r, inside Q_(a′). Then Lemma 1.1 (a)-(f) hold:
(a), (c), (d), (e) as FAMILIES5.md 4i (D533, D537) shows, with at least the record's margins (ψ ≤ 0, f ≤ 1); (b) by (c)
above; (f) with r_q^♭ := r_q(μ) ≥ r_q(μ0) = q0 by (b), the curvature boundary being {K ≤ l5⁻⁴}, K = 72μ²/R⁸ + (8/3)
e^(−4s) 𝒜ℬ/R⁶ (twodt5 T1), which gives R ≥ r_q(μ) ≥ q0 when 𝒜ℬ ≥ 0. Every past causal curve from Ω₂ meets Σ_τ0 inside
Ω₂ (record's (d)-(e)), so both generators reach Σ_τ0 transversally (they are null, dτ timelike). Compactness is (d).

(f) *The computed example (twobg5 G2, floating point).* Corner mass 1.5 at R = 5; packet ℬ = 1.7 b(u; 5.7, 7.2) on N′;
shell 𝒜 = 3.6 b(v; 3, 4.5) on N (b a C^∞ bump); seed μ0 = 0.82211; outer mass after the shell 3.6058. At n = 40, 80,
160: structure, mass bound, trapped R = a, past-closedness as above; the diamond lies at R ≥ 2.59 and is untrapped; on
Σ_τ0 (τ0 = −a + 0.02) the packet lies at R ∈ [1.861, 3.431] between the seed's horizon 0.907 and the shell's inner edge
3.68, which meets the record's rule. The rectangle stops at v = 5: inside the hole the double-null grid thins
exponentially (FAMILIES5.md 4i, D3), and there the background is the explicit ingoing Vaidya of region III (a).

**What this settles.** FAMILIES5.md left open the background on the whole domain (D561: "Open: the cones' data, that is,
the outgoing family's data at past null infinity") and the condition μ > a² on R = a (D546-D549). Both are settled for
these data: the outgoing family's characteristic data are stated (explicit Vaidya data on N′ and N), the diamond is the
only non-explicit region, the mass bound makes Lemma 1.1′(b) unconditional, and existence on all of Ω₂ is deduced with
the regularity step written. **Not settled:** data in which the packet starts outside the shell (no crossing in the
future of Σ_τ0, so not two crossing families) or inside the seed's horizon (then it is trapped on N′ and m increases
inward there; (b) is then not the bound used, and is not examined).

## 3. The phases

The ingoing phase is v̂ (the record's v in region I: v̂ = τ0 + R on Σ_τ0) and the outgoing phase is the background's
other double-null coordinate u, with any λ-independent normalisation (on N′ by its affine parameter, or on Σ_τ0 by u = τ0
− R). Both are **exact eikonals of g0** (double-null coordinates); this is the **dynamic outgoing null phase** that
data5two.py could not hold (its code fixed ∂_τ(∂_τ u) = 0 on Σ). The ingoing generator ℓ_in = g0⁻¹ dv̂ = e^(−ψ) ∂_R|_(v̂)
satisfies ℓ_in = −e^(−ψ) L0 with L0 = ∂_τ − x̂·∂_x **the record's operator** (deduced from the chart, τ = v̂ − R;
twotransport5 T2: radial speed −1). The outgoing generator has radial speed c_out = y/(1 − y), y = e^ψ f/2 ∈ (−∞, 1/2],
so c_out ∈ (−1, 1], negative where trapped (twotransport5 T2).

## 4. The approximant to every order (Theorem A₂)

**Theorem A₂ (deduced: FAMILIES5.md 4h's Lemmas 5.1′, 5.3′ and Theorem A′, now on Ω₂).** For every N and every smooth
choice of stage data there are means m_j, phase corrections φ_j^in, φ_j^out and zero-mean profiles ĝ_j(X, s1, s2) with
residual Ric^H(g_app) = λ^N × (a bounded profile), (E1) for each family, and (E2) (Stage 0: FAMILIES5.md 4b T1-T5, 4e).

The interaction terms and non-resonance, as computed:

- *Stage 0* (FAMILIES5.md 4b, `stage0two5.py`): R^(−1) = 0; the mean of R^(0) is the two-dust equation with no cross
  term; the mixed harmonics (n1, n2), n1 n2 ≠ 0, of R^(0) are present and are removed by λ² ĝ_2^mix by division (T4).
- *Every order* (`nonres5.py` N1-N2, computed): a term λ^j q e^(i(n1 s1 + n2 s2)) E first meets the reduced operator at
  order j − 2, through −½ g^ab ∂_a ∂_b only, with symbol −e^(−2σ) f′h′ n1 n2 (phases f(v), h(u)): zero exactly on the
  pure harmonics, which are transported along their own generator, and |sym| ≥ e^(−2σ) |f′h′| on **every** mixed
  harmonic. So there are no small divisors and the division loses no derivative: this is the whole of Touati's strong
  coherence condition (READ below, [Tou24] (1.18), p. 9) for all mixed phases at once, because in the (u, v) plane the
  null cone is two lines. The corrected phases and the mean change the symbol by λ times a quadratic form in (n1, n2)
  (N2); at stage m only |n1| + |n2| ≤ m + 2 occur (Lemma 5.1's weight count), so the change is moved to the next order,
  as the record's e_j is. Control: two ingoing phases have symbol 0 on every harmonic (resonant), and commensurate ones a
  zero-frequency combination.
- *The constant on Ω₂* (computed, twobg5 G2 (vii)): |g0⁻¹(dv̂, du)| is positive on every computed cell, ≥ 0.147 off the
  trapped region, and on R = a equals 0.892, 0.446, 0.240 at v = 0.5, 1, 1.5 (converged to 1 %): it halves with each 0.5
  in v. So the non-resonance constant is a positive constant on the compact Ω₂ that **degenerates exponentially with the
  time spent in the hole** (the redshift at the horizon). Theorem 1₂'s constants depend on it; this is harmless for a
  fixed T, and is the quantitative cost of the black hole for the two-family problem.
- *Stage data on Σ_τ0* (deduced): on Σ_τ0 the two families' supports are disjoint (section 1); the pure harmonics are
  transported along their own generators, so they keep their supports in v and in u, and the mixed harmonics are
  algebraic in products of the two families' profiles, so they vanish near Σ_τ0. So the mixed harmonics take no data
  (FAMILIES5.md 4h (d)) **and** vanish on Σ_τ0, which is what the data construction (section 6) needs.

The stage system of Lemma 5.3′ ((a) mean: a wave equation; (b) two phase transports; (c) two pure-harmonic transports;
(d) mixed division) closes on Ω₂ by the record's Picard argument, both generators reaching Σ_τ0 inside Ω₂ (Proposition
B(e)). The mixed division costs one derivative per stage (FAMILIES5.md 4h, verifier 227's correction), harmless for
smooth data and finitely many stages.

## 5. The uniform linear estimate and the bootstrap (Theorem E₂)

**Theorem E₂ (deduced).** The record's Theorem E (N1STAR-PROOF.md 0.4) holds on Ω₂ for a two-phase approximant with
(E1) for each family, (E2), (E3), (E4), with w = h + φ_in Y_in + φ_out Y_out and the energy

    N₂(τ) := Σ_(j≤k) λ^j (‖∂^j ∂h‖ + Σ_K (‖∂^j Ψ_K‖ + ‖∂^j ∂φ_K‖ + λ ‖∂^j ∂_x² φ_K‖)) + ‖h‖ + Σ_K ‖φ_K‖,   K ∈ {in, out}.

The proof is the record's section 4 with these changes (each a statement FAMILIES5.md 4f-4g deduces, now with the
domain, the transports and the mollifier in place):

- *The decomposition.* Given the solution w (Step 8), the phases solve the linear system ℓ_K·dφ_K = ½ 𝒫 s_K(h), h :=
  w − Σ_J φ_J Y_J, φ_K = 0 on Σ_τ0 (FAMILIES5.md (3.4′)), by Picard iteration (φ ↦ 𝒫(c φ) is bounded on L²). The
  estimates must use this form: ‖λ^j ∂^j ∂φ_K‖ ≤ C ‖λ^j ∂^j ∂ s_K(h)‖ ≤ C N₂, as in the record's Step 5. Written through
  s_K(w) instead, the source contains 𝒫(c_in φ_out), c_in = e^(−4σ) F2 χ′ oscillating at the mollifier's own scale, whose
  derivative is of size λ⁻¹ ‖φ_out‖ (Bernstein, (M2)): routing the estimate that way would lose a power of λ (deduced).
  Step 1 (|w|_(k+1) ≤ C N₂) and Step 2 (φ_K = 0 on Σ_τ0, so h = w there) are the record's.
- *The λ⁻¹ structure* (computed, FAMILIES5.md 4d L1-L3, 4f Q2): the λ⁻¹ part of the linearisation is ½ λ⁻¹ Σ_K s_K
  G2^K, once per family and nothing else; after the decomposition the only λ⁻¹ coefficients left are ½ λ⁻¹ ((1 − 𝒫)
  s_K(h)) G2^K, each O(∂ s_K(h)) by (M3).
- *Lemma 3.3₂* (deduced, 4g): contracting with ℓ_in ⊗ ℓ_in kills family in's λ⁻¹ term and its □̃φ_in term exactly;
  family out's survive through χ′ alone: ½ λ⁻¹ ((1 − 𝒫) s_out(h)) e^(−4σ) F2² χ′ = O(∂ s_out(h)) and −q c_in Ψ_out, a
  bounded coefficient at the top order of Ψ_out; N_φ^out(ℓ_in, ℓ_in) keeps |w||∂²φ_out|, at most C M λ^(K−4) N₂ in the
  bootstrap. No large coefficient enters s_in's equation; s_out's is the mirror.
- *Lemma 3.4₂* (computed, 4f Q1): Ψ_K := □̃φ_K obeys L_K Ψ_K + a_K Ψ_K = ½ □̃ 𝒫 s_K(h) − ½ M_K(𝒫 s_K(h)) − N_K φ_K, the
  record's (3.6) form on any round double-null metric, both generators being shear-free; Ψ_in's source contains 𝒫(c_in
  Ψ_out) through □̃ s_in(h), bounded on L² whatever the oscillation, and Ψ_out's the mirror. At level j a derivative on
  c_in costs λ⁻¹, which the weight λ^j absorbs.
- *Lemma 2.4₂ (computed, twotransport5 T1-T2).* For Z = ∂_τ + c x̂·∂_x, d_τ ∫ φ² = 2⟨φ, Zφ⟩ + ∫ div(c x̂) φ² + (b′ −
  c(b)) ∫_(|x|=b) φ² + c(a) ∫_(|x|=a) φ²; for ℓ_in, c = −1 (the record's), for ℓ_out, c_out ∈ (−1, 1], so b′ − c_out(b) ≤
  −1 < 0, and c_out(a) < 0 because R = a is trapped (Proposition B(c)). Both boundary terms have the record's sign.
  Control: an untrapped R = a would give c_out(a) > 0 and the wrong sign.
- *Lemma 2.3 (energy), the mollifier (Lemma 2.2), Step 8 (local theory)*: unchanged. Lemma 2.3 uses only that Σ_τ, {R =
  a} and the outer boundary are spacelike with Ω₂ to their past (Proposition B(e)); the mollifier lives on the annuli
  A(τ) = {a ≤ |x| ≤ b(τ)} in the chart (τ, x = R x̂), which is global on Ω₂ since R_u < 0; Step 8 needs smooth bounded
  coefficients and spacelike slices.
- *Steps 4-7*: every new term is a bounded two-phase profile times a quantity N₂ controls at the same scaled order; the
  nonlinear terms are at most C λ⁻⁵ N₂²; so N₂ ≤ C₃((C_D + 1 + C_R) λ^K + C M² λ^(K+1)) and the bootstrap closes at N₂ ≤
  M λ^K with M := C₃(C_D + 1 + C_R) + 1, the smallness a power of λ, never of the data.

## 6. The data on Σ_τ0 (Theorem D₂)

**Theorem D₂ (deduced).** For λ small there is a vacuum Cauchy datum on Σ_τ0 within O(λ^K) of g_app's, with D = 0
imposed through ∂_τ g, equal to the seed's on R < r1.

The record's proof (N1STAR-PROOF.md section 6) carries over with:

- *Lemma 6.3 on the two-dust slice (computed, `twoslice5.py` S1, exact, symbolic).* On **every** round slice, γ = G(R)
  dR² + R² dΩ₃², K round, G, K arbitrary: the linearised ρ has no ∂_R² a and no ∂_R ∂_θ a, the coefficient of ∂_R a is
  3/(R G²) = θ³H > 0 (θ² = 1/G, H = 3/(R √G)) and that of ∂_θ² a is −1/(G R²), independent of K; J_R = 6 ∂_R w − (2/R²)
  ∂_θ q, J_θ = −(2/G) ∂_R q + 4 ∂_θ w; S = diag(1, −1/(2R²)) gives S A0 = diag(6, 1/(G R²)) > 0 and S A^θ symmetric;
  speeds² = 2G/(3R²). At G = 1 + μ/R² this is the record's (5.6). So the slice need not be Vaidya's, and H > 0 holds on
  every round slice (R is a coordinate on it). Control: the correction h = a γ (conformal) brings ∂_R² a (data5's mutant
  conformal_h).
- *No 1/λ coefficient (computed, S2, exact at random points).* At the approximant's slice data with **both families and
  both second harmonics** (χ_in dv², χ_out du²), on a general round spacetime background (lapse, radial metric and shift
  arbitrary functions of (t, R)), with **arbitrary radial phases** Pv(t, R), Pu(t, R) (null or not, static or dynamic),
  the linearisation of (J_R, J_θ, ρ) in a generic (a, w, q) has no coefficient of order λ⁻¹ in any harmonic e^(i(n1 s1 +
  n2 s2)) (three random draws; fields carried as exact Gaussian-rational jets of degree 2, every harmonic, λ-order ≤ 2,
  which is exact at the point because the constraint map takes at most two derivatives along any path). Control: an
  outgoing wave with an oscillating trace on the spheres gives one (in ρ). The cancellation, deduced by hand and so
  checked: δR^(−1)[h] = −2⟨h, p ⊗ W″p⟩ + h(p, p) tr W″ + |p|² ⟨h, W″⟩ and J^(−1)_i[h] = 2(h^(jk) p_j κ1′_(ki) − p_i
  h^(jk) κ1′_(jk)), p = du|_Σ; with h = a dR², both vanish when W has no R- and no t-component and is traceless on the
  spheres, and the gauge term χ p ⊗ p gives zero for every h.
- *Principal coefficients at the approximant's data (computed, S3).* The order-0 coefficients of ∂_R a, ∂_θ² a, ∂_R ∂_θ
  a, ∂_R² a in ρ and of ∂_R w, ∂_θ q, ∂_R q, ∂_θ w in J equal the background's in every harmonic (control: with the trace
  some differ), so α = θ³H and S A0 keep their signs for λ small (Lemma 6.3(c)).
- *∂_t² of the phase never enters (computed, S4).* The constraint map depends on (γ, K), that is on g and its first
  t-derivatives: the slice data are unchanged under Pu → Pu + c(t − t0)²; control: Pu → Pu + c(t − t0)(R − R0) changes
  K. So the dynamic outgoing null phase is covered, and its eikonal equation is not used by the data.
- *Lemma 6.1₂ (the gauge hierarchy; deduced, FAMILIES5.md 4i D566 (i)).* The oscillating part of (6.1) at each order is a
  transport along each family's own generator for its pure harmonics and algebraic (symbol −e^(−2σ) n1 n2 ≠ 0) on the
  mixed ones, which vanish with the lower orders; the means obey the record's wave equation; both generators reach Σ_τ0
  inside Ω₂ (Proposition B(e)).
- *Lemma 6.2₂ (the stage data; deduced).* Pol is onto for each family's null covector (data5.py S1; GL(5)-equivalence),
  so each family's pure harmonics are fixed as the record's, each on its own support; the mixed harmonics take no data
  and vanish on Σ_τ0 (section 4); the means' constraints are Lemma 6.4's radial problem on the two-dust slice, solved
  outward from a sphere R < r1 where the data are the seed's, through the packet and then the shell.
- *Lemma 6.4 and Proposition 6.5*: verbatim, their hypotheses being S1-S3.

## 7. Part I: what is proved, and what is not

- Background on Ω₂, outgoing data stated: deduced; identities computed; example computed (§2, twobg5, twoext5 X1-X2).
- μ ≥ μ0, R = a trapped, past-closed: deduced; computed (G2) with a failing control (§2 (b)-(c)).
- Regularity step of D558: deduced (written) (§2 (d)).
- Constraints on the slice: deduced; S1 symbolic, S2-S4 exact at random points (§6, twoslice5).
- Dynamic outgoing null phase: settled: exact eikonal, and not used by the data (S4) (§3, §6).
- Approximant every order, interactions, non-resonance: deduced; symbol computed; constant computed on Ω₂ (§4, nonres5,
  twobg5).
- Energy estimate, bootstrap: deduced, at the level of the record's section 4 with the changes listed (§5).
- Transport on Ω₂ for both generators: computed (twotransport5).
- Theorem 1₂ items 1-5: **deduced, not independently verified** (§1).
- Theorem 1 items 6-7 (horizon, mean mass) for two families: **not claimed**.

Item 6 would need the outgoing wave's O(1) oscillating contribution to ∂_R θ⁺ along the columns (the phase u is not
constant along a column) to stay below 3/μ near the horizon; it holds where the outgoing packet stays away from √μ(v)
(no oscillation there), which is not arranged above. Item 7's quarter-turn argument needs both families' first mean
corrections odd; not computed.

---

# Part II. Finitely many families in the T² class

**Which null phases the 2+1 quotient permits (computed, `axisphase5.py` A1-A2).** A family's phase in the class is a
T²-invariant function F(τ, ρ1², ρ2²) on R × R⁴; its rays project to the orbit space, the quarter plane with the axes as
edges. At every axis point the spatial gradient of such a function is along x̂ (A1, on both axes), so a null invariant
phase has, there, the gradient dv or the outgoing radial covector. Non-radial invariant null phases exist: on Minkowski,
w = τ + f, f the distance to the T²-orbit of an ellipse (α ≠ β) in the orbit plane, is an exact eikonal, even in ρ1 and
ρ2, with rays radial **exactly at the axes** and tilted between them (A2). Control: τ − x3 (not invariant) leaves
span(dτ, dr) at an axis point.

**Angular separation (computed, A2; deduced).** Two families both ingoing (or both outgoing) at an axis point have
parallel gradients there. For v = τ + r and w above, g0⁻¹(dv, dw) = −1 + cos β, and near the axis g0⁻¹(dv, dw)/(β²/2) →
−1 with β/θ → 5/31, β the angle between the two rays: the mixed symbol −n1 n2 g0⁻¹(dv, dw) **vanishes like θ²** at the
axes (a small divisor of the division of section 4; semi-axes 1/2, 1/3), and Huneau and Luk's angular separation (READ
below, [HL18] Definition 4.1, p. 10) fails there, its cosine tending to 1. The radial in/out pair has g0⁻¹(dv, du) = −2
everywhere (separated). Hence: **with envelopes that do not vanish at the axes, at most two families can be angularly
separated in the class, one ingoing and one outgoing at each axis** — Part I. Several radial families of one orientation
are resonant (nonres5 control): they are one family with a multi-frequency profile, not separated families.

**More families, with envelopes vanishing near the axes.** Separation then needs only hold on the overlaps of supports,
and any finite number of separated families is possible (e.g. non-radial phases of different ellipses, supported away
from the axes). Their averaged stress Σ F_A² du_A ⊗ du_A has a θθ component wherever w_θ ≠ 0 (A3; control: α = β gives
none), so **the background is not round**: the structure of section 2 (Vaidya off a 1+1 diamond) is lost, and the
background is a T²-invariant, non-SO(4)-invariant Einstein–null dust solution, a 2+1 problem on the orbit space with
the axes as boundary.

**The exact obstruction: the background (open).** No existence theorem for that background on a domain like Ω₂, without
smallness, is available here. What is known is small-data and four-dimensional: Huneau and Luk's background is their
small-data local solution in an elliptic gauge, "smallness is required even for local existence of smooth solution"
(READ, [HL24] p. 28, quoted in the record), and Touati assumes the background "close to Minkowski" and does not construct
it (READ, [Tou24] (1.15) p. 8, and Remark 1.3 p. 11: "In this article, we don't prove that such a background spacetime
(M, g0, uA, FA) can be constructed, this follows from [CBF06] adapted to the null dusts case."). The step that fails
without these is the null dust's own regularity: the dust's density is transported by □_g u_A, one derivative below g,
and coupled back into Einstein it loses a derivative (FAMILIES5.md 4i, `dustloss5.py`, in the characteristic setting);
Huneau and Luk recover it in their Vlasov paper through the Raychaudhuri equation for the null expansions (READ, [HL25]
p. 5: "we use the Raychaudhuri equation that χ_A satisfies"), again for small data. In Part I this never arises: with
round radial dusts the background is 1+1 and the dust densities are functions of one null coordinate.

**Conditions under which the proof extends (deduced, conditional).** Given (i) such a background on a domain Ω with the
record's Lemma 1.1 (spacelike slices and lateral boundaries, every generator reaching Σ_τ0), (ii) pairwise separation on
the overlap of supports, |g0⁻¹(du_A, du_B)| ≥ c > 0 there, and (iii) waves transverse to their own generators with the
radial constraint solve's cancellation (S2 used that each wave has no R- or t-component and is traceless on the spheres;
for a non-radial family a wave transverse to its generator and free of R-components is confined to the torus block, one
polarisation; the other is not examined): then sections 4-6 extend with one transport and one phase per family, the
mixed symbols bounded below by c on all harmonics with n_A n_B ≠ 0, and the extended system (h, φ_1, …, φ_N) with N
bounded cross couplings. Without (i) nothing is proved.

---

# Part III. Vlasov matter

## III.1 The literature, at source (READ, alphaXiv, 2026-11-02)

- [HL18] C. Huneau, J. Luk, *High-frequency backreaction for the Einstein equations under polarized U(1) symmetry*,
  arXiv:1706.09501v1. Abstract, p. 1: "We prove that any generic local-in-time small-data polarized-U(1)-symmetric
  solution to the Einstein–multiple null dust system can be achieved as a weak limit of vacuum solutions. Our
  construction allows the number of families to be arbitrarily large, and appears to be the first construction of such
  examples with more than two families." P. 2: "one may hope to eventually construct more general solutions to the
  Einstein– massless Vlasov system by taking the number of families of null dust to infinity." Definition 4.1, p. 10: "we
  say that the set of eikonal functions {u_A}_(A∈A) is angularly separated if there exists η′ ∈ (0, 1) such that δ^(ij)
  (∂_i u_A1)(∂_j u_A2) / (|∇u_A1||∇u_A2|) (t, x) < 1 − η′, ∀(t, x) ∈ I × R², ∀A1 ≠ A2." (fraction restored from the
  extraction.)
- [HL19] C. Huneau, J. Luk, *Trilinear compensated compactness and Burnett's conjecture in general relativity*,
  arXiv:1907.10743v2. Abstract, p. 1: "In this paper, we prove Burnett's conjecture assuming that {h_n} and h_0 in
  addition admit a U(1) symmetry and obey an elliptic gauge condition." P. 4: "That (1.10) holds is due to the
  divergence structure of the terms." P. 8, section 1.2.1: "Like Conjecture 1.1, in full generality the reverse Burnett
  conjecture remains open." P. 13, before Definition 2.7: "By “restricted”, we mean that we are not considering general
  (3 + 1)-dimensional solutions to the Einstein–massless Vlasov system for which the metric admits a U(1) symmetry, but
  instead we require that massless Vlasov measure to be supported in the cotangent bundle corresponding to the (2 +
  1)-dimensional (instead of the (3 + 1)-dimensional) manifold."
- [HL25] C. Huneau, J. Luk, *High-frequency backreaction for the Einstein equations under U(1) symmetry: from
  Einstein–dust to Einstein–Vlasov*, arXiv:2506.21779v1. Abstract, p. 1: "Given suitable small, localized, U(1)-symmetric
  solutions to the Einstein–massless Vlasov system in an elliptic gauge, we prove that they can be approximated by
  high-frequency vacuum spacetimes." Theorem 1.1, p. 2: "The initial data for (ϕ0, ϖ0, f) are compactly supported,
  sufficiently small and regular." Footnote 2, p. 2: "according to [15], this is the expected class of Vlasov matter that
  arises in the limit of U(1) symmetric spacetimes" ([15] = [HL19]). P. 6: "It is an interesting open problem whether
  this could also be carried out without symmetry, for instance by extending the work [39]" ([39] = [Tou24]).
- [Tou24] A. Touati, *The reverse Burnett conjecture for null dusts*, arXiv:2402.17530v2. Abstract, p. 1: "Given a
  regular solution g0 of the Einstein-null dusts system without restriction on the number of dusts, we construct families
  of solutions (gλ)λ∈(0,1] of the Einstein vacuum equations such that gλ −g0 and ∂(gλ −g0) converges respectively
  strongly and weakly to 0 when λ → 0." P. 4: "More importantly, this article completely leaves open the question of
  sending the number of null dusts to infinity and thus proving the reverse Burnett conjecture with the highest level of
  generality. In particular, our local existence result in generalised wave gauge is not uniform in |A| and obtaining
  such uniformity seems to require ideas beyond the present work." P. 8: "We assume that the metric g0 is close to
  Minkowski in the following sense" ((1.15)). P. 9, the strong coherence assumption: "there exists a constant c_coherence
  > 0 such that min_(v∈I) |g0⁻¹(dv, dv)| ≥ c_coherence. (1.18)". Touati's other two papers, *Geometric optics
  approximation for the Einstein vacuum equations* (arXiv:2206.12318) and *High-frequency solutions to the constraint
  equations* (arXiv:2206.13062), are the record's [Tou23a, Tou23b], single-phase; a search of the paper index (Firecrawl,
  2026-11-02, author Touati) returned no Vlasov paper of his.
- [LR20] J. Luk, I. Rodnianski, *High-frequency limits and null dust shell solutions in general relativity*,
  arXiv:2009.08968v1. Abstract, p. 1: "We show moreover that all sufficiently regular solutions to the Einstein–null dust
  system (with potentially measure-valued null dust) adapted to a double null coordinate system arise locally as weak
  limits of solutions to the Einstein vacuum system in the manner described above." Corollary 1.14, p. 6: "for any p ∈ M,
  there exist p ∈ M′ ⊆ M and a sequence of smooth angularly regular vacuum solutions (M′, g_n) such that g_n → g_∞ in C⁰
  and weakly in W^(1,2) in M′." And [HL18] p. 2 on it: "the oscillations in the metrics are limited to 2 dimensions and
  therefore the effective stress-energy-momentum tensor can represent at most two families of null dust."

**Status (READ).** The reverse direction for massless Vlasov is proved only for small, localised, U(1)-symmetric data in
an elliptic gauge in 3+1 ([HL25]); without symmetry it is open, and Touati's multi-dust theorem is not uniform in the
number of dusts ([Tou24] p. 4). The direct direction (limits are massless Vlasov) is proved under U(1) symmetry in an
elliptic gauge ([HL19]), with the Vlasov measure **restricted** to the cotangent bundle of the 2+1 quotient.

## III.2 A five-dimensional T²-class version (deduced; computed `torusstress5.py`)

**Proposition V.** (a) *Every Burnett limit inside the class has no torus stress (deduced; computed V1).* In the class,
R11 and R22 of g5 are linear combinations of □_h ψ and □_h ω (the paper's Proposition 2.1), the mixed torus components
vanish identically, and √|h| □_h f = ∂_a(√|h| h^ab ∂_b f). For a sequence in the class with g_λ → g0 uniformly and ∂g_λ ⇀
∂g0 weakly, √|h_λ| h_λ^ab → √|h0| h0^ab uniformly and ∂ψ_λ ⇀ ∂ψ0 weakly, so ∂_a(√|h_λ| h_λ^ab ∂_b ψ_λ) = 0 passes to the
limit in distributions: □_h0 ψ0 = □_h0 ω0 = 0, so R11[g0] = R22[g0] = 0 — the 5D form of [HL19]'s "divergence
structure" (READ above). Computed (V1): in the two-scale expansion the λ⁻¹ coefficient of ∂_a(H^ab ∂_b f) vanishes on a
null phase and the mean of its λ⁰ coefficient is ∂_a(H0^ab ∂_b f0) exactly, for any oscillation H1 of H, every
oscillating term being a θ-derivative, while the quadratic term of Ric[h] keeps its Isaacson mean. Control: the
non-divergence operator h^ab ∂_a ∂_b f acquires a mean ⟨h1(du, du) ∂_θ² f1⟩.

(b) *A massless Vlasov limit in the class is restricted (computed V2).* T_(φφ) = ∫ p_φ² dμ = 0 forces the measure onto
p_φ1 = p_φ2 = 0: momenta tangent to the 2+1 orbit space — the 5D T² analogue of [HL19]'s restricted system.

(c) *Round limits are two null dusts (computed V3-V4).* If the limit is moreover SO(4)-invariant (as every background of
Part I is), the isotropy SO(3) at a point rotates the angular momentum, and the line {p_φ = 0} ∩ T*S³ = span(e_θ) is
moved off itself (V3), so an invariant measure supported in it is supported at 0: the momenta are radial. Radial null
momenta at a point of Vaidya are multiples of dv or of k_out, so T = (∫ E² df_in) dv² + (∫ E² df_out) k_out² (V4),
radial momenta stay radial along radial geodesics, and the Einstein–(radial) massless Vlasov system is, for g, the
Einstein–two-null-dust system. Control: a momentum with p_θ ≠ 0 gives T_θθ > 0.

**Consequence (deduced).** Within the round T² class the passage to Vlasov matter adds nothing to Part I: every round
massless Vlasov limit in the class is a two-dust solution, and Theorem 1₂ realises those of section 2's form (a seed, an
ingoing shell, an outgoing packet between them on Σ_τ0) as limits of vacuum metrics. No infinite number of families is
needed: in the round class there are only two null directions to oscillate in (Part II).

**Where it stops (open).** A non-round T²-invariant massless Vlasov field has momenta with p_θ ≠ 0; approximating it by
T²-invariant dusts needs non-radial families, which are radial at the axes (Part II), so either the measure's support
at the axes is radial or the families' envelopes vanish there. Either way the background is non-round and the proof
stops at **Part II's obstruction**: the existence of a non-round, large Einstein–null dust background in the class on the
domain, and, for the limit N → ∞ of [HL25], a construction uniform in the number of families, which neither [HL25] (its
constants C(N) = c^N N^N, p. 5, READ: "Going through the proof gives that C(N) = c^N N^N works for some large c ≥ 1",
exponents restored from the extraction)
nor [Tou24] (p. 4) provides beyond small data.

---

# Part IV. Next step

Have an independent verifier read sections 2 and 5 against N1STAR-PROOF.md sections 1 and 3-4 (the domain, and the
extended (h, φ_in, φ_out) system with Lemmas 3.3₂, 3.4₂ written at the record's level), then write Lemma 3.3₂ and Steps
4-6 for two families out in full; separately, decide item 6 (the horizon) for two families by placing the packet so that
it stays outside √μ(v) + δ, or by bounding the outgoing wave's contribution to ∂_R θ⁺.

## Files

`FAMILIES5-FULL.md` (this note); `checks/twobg5.py` (+ `.out`, about 45 s); `checks/twoslice5.py` (+ `.out`, about twenty
minutes); `checks/nonres5.py`, `checks/twotransport5.py`, `checks/axisphase5.py`, `checks/torusstress5.py` (+ `.out`
each, seconds).
