# FAMILIES5-FULL -- two crossing families in full; several families in the class; Vlasov

Status (2026-11-02, round 1; the next paragraph updates it). Part I: the two-family counterpart of the record's
Theorem 1 (Theorem 1₂) is **deduced** here, from
the record's proof (N1STAR-PROOF.md sections 1-6), FAMILIES5.md sections 4b-4i, and six new programs; it has **not been
read by an independent verifier**, and items 6-7 of the record's Theorem 1 (horizon, mean mass) are not claimed for it.
Part II: which null phases the T² class permits is **computed**; that angular separation in Huneau and Luk's sense fails
at the axes for any two families of the same orientation is **computed**; the background for more than two (necessarily
non-round) families is **open**, with the obstruction stated. Part III: the literature is **READ** at source; the 5D
T²-class reduction of the Vlasov passage to Part I is **deduced** with its identities computed; the non-round case is
**open** and stops at Part II's obstruction. Nothing in FAMILIES5.md, the paper or the log is changed.

Round 2 (2026-11-02, Part V). An independent verifier read this note at commit 169c9b5 and found no major gap; its seven
findings are seated (section 11, each with its disposition, the text corrected in place where it stood). Theorem E₂'s
Lemma 3.3₂ and Steps 4-6 are written in full (section 8), every identity behind them computed (`checks/twodecomp5.py`,
from the reduced Ricci tensor, whose principal part is what J1-J7 exercise [R5]) and the power counting computed term by term (`checks/twoledger5.py`): Theorem E₂,
and with it Theorem 1₂ items 1-5, is **deduced**. The record's item 6 (one zero per column of the outgoing expansion) is
**deduced for two families**, with no condition on where the outgoing packet lies: the outgoing wave's would-be O(1)
contribution to ∂_R θ⁺ along a column is computed to vanish at stage 0 (section 9) [R5: and proved for every function,
section 9, `checks/h3proof5.py`]; item 7 (the mean mass) is **deduced** with the outgoing family's parity base computed
(section 10). [R5: read by an independent verifier at commit 9872bb3, findings in section 12.]

Round 5 (2026-11-06). The independent verifier of Part V (sections 8-11, commit 9872bb3) found Lemma 3.3₂, Steps 4-7 (the
94 ledger rows), item 7, section 2 (d)-(e) and V3's Schur argument sound, reran all eight programs to their `.out`
files, and showed H3 provable. Its findings (one major, five minor, notes and nits) are repaired in place, each marked
[R5], with their dispositions in section 12; H3's structural proof is banked as `checks/h3proof5.py` and section 11 (i)
is withdrawn.

Labels as in the record: **computed** (a program `checks/<name>5.py` with a `.out` and a negative control that the
program must reject), **deduced** (argued here, a standard step named as such), **READ** (verbatim, identifier and page,
read at source through alphaXiv, 2026-11-02). New programs: `checks/twobg5.py`, `checks/twoslice5.py`,
`checks/nonres5.py`, `checks/twotransport5.py`, `checks/axisphase5.py`, `checks/torusstress5.py`, each with its `.out`;
round 2: `checks/twodecomp5.py`, `checks/twoledger5.py`, `checks/twohorizon5.py`, `checks/twoparity5.py`, and
`twobg5.py`, `twotransport5.py`, `axisphase5.py`, `torusstress5.py` amended (section 11).

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
4. |g_λ − g0| ≤ C λ, |∂g_λ| ≤ C, and ∂g_λ − ∂g0 = dv̂ ⊗ [∂_(s1) g1^in] + du ⊗ [∂_(s2) g1^out] + O(λ), so ∂g_λ → ∂g0
   weakly in L² and not strongly where env or env₂ is nonzero; g0 is the **two-null-dust background** of section 2,
   Ric(g0) = K_in dv² + K_out du² with K_in R³ and K_out R³ the two families' Isaacson fluxes;
5. D(g_λ) = 0 (the record's wave-map gauge relative to g0) and g_λ is the only C² solution of Ric^H(g) = 0 on Ω₂ with
   data within ε1 of g0.

The record's items 6 (the horizon) and 7 (the mean mass) for two families: sections 9 and 10 (round 2).

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
(v̂, R) after reparametrising v̂, and where 𝒜 = 0 (and R_v ≠ 0) outgoing Vaidya: the only region where it is not Vaidya
is the compact crossing diamond Q× = [u1, u2] × [v_start, v_end]. (Corrected in round 2, the verifier's nit 7.) Off Q×
the background is Vaidya, but explicit from the data only in u ≤ u1 (ingoing Vaidya with the mass function of the data
on N) and in v ≤ v_start (outgoing Vaidya with that of the data on N′); in u ≥ u2 and in v ≥ v_end it is Vaidya with
the mass functions μ(u2, ·) and μ(·, v_end) read from the diamond's solution on its edges, not explicit from the data.
In the example the departures from Vaidya off Q× fall with resolution (1.8 × 10⁻⁵, 5.2 × 10⁻³, 5.2 × 10⁻³, 2.2 × 10⁻⁴
at n = 160 in the four regions, each falling with n).

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
{u ≥ u2}, so {R ≥ a, v ≤ V1} has u bounded, and by the same bound {R ≥ a′, v ≤ V1} for every a′ > 0 [R5: stated with
a′ before step (1), which uses a uniform K_0 on {R ≥ a′}]. *The first exit* (written in round 2, the verifier's item 1: (c) assumes the
solution on J⁻(p), so Ω₂ ⊂ Q_(a′) needs an argument). Fix a′ < a, K > K_0 (the chain's bound on {R ≥ a′}), the truncated
fixed point Ũ on Q (F_K, G_K equal to F, G on {|U| ≤ K, R ≥ a′}) and Q_(a′) := {p ∈ Q : R̃ > a′ on J⁻(p) ∩ Q}. (1) Ũ
solves the true system on Q_(a′): for p ∈ Q_(a′), if |Ũ| ≥ K somewhere on the compact J⁻(p) ∩ Q, let q be such a point
with u + v least; on J⁻(q) ∖ {q}, |Ũ| < K and R̃ > a′, so Ũ solves the true system there, the chain gives |Ũ| ≤ K_0
there and, by continuity, at q: a contradiction. (2) Q_(a′) is a past set, open in Q (the least of R̃ over J⁻(p) is
continuous in p), and the development D := ∪_(a″>0) Q_(a″) is a past set carrying one smooth solution (two truncations
agree where both solve B1, by the contraction). (3) For p ∈ D with R(p) ≥ a, (c) applies, J⁻(p) ⊂ D, and gives R ≥
min(R(p), √μ0) ≥ a > a′ on J⁻(p): p ∈ Q_(a′). (4) So G := {p ∈ D : R ≥ a on J⁻(p)} ⊂ Q_(a′), and G is not cut by the
edge of the development: G is closed in Q [R5: G ⊂ Q_(a′) and R̃ is continuous on Q_(a′)], and at p ∈ ∂G the least of R over J⁻(p) is a (were it larger, a neighbourhood of
p would lie in G), so (c) at p gives min(R(p), √μ0) ≤ a < √μ0, i.e. R(p) = a: ∂G ⊂ {R = a}. Ω₂ ⊂ G below, and the
background exists, smooth, on all of it.

(e) *The domain and the record's Lemma 1.1 (deduced; computed twodomain5 D1-D2, twodt5 T1-T2, twotransport5, twobg5
G3).* Define Ω₂ ⊂ G by the record's (1.1) with v̂, τ = v̂ − R and R in place of v, τ, r, the outer data cone N = {u =
u0} being chosen with **N ∩ {τ ≥ τ0} ⊂ {R > b(τ)}** (round 2, the verifier's item 1: if N met Σ_τ0 at R < b(τ0), {u =
u0} would be a null boundary of Ω₂ through which the ingoing waves enter, and Lemma 2.3 and (e) would fail there). The
condition costs nothing: u ≤ u1 is explicit ingoing Vaidya with the data's mass function (a), so N can be moved outward
without changing the background elsewhere (uniqueness on the smaller rectangle). Computed (twobg5 G3, the example, T =
1, δ0 = 0.05): the example's own N (R = 5 at v = 0) meets Σ_τ0 at R − b = −4.09, inside the domain, which is the
verifier's case; the outgoing ray of region I from R = 7.505 at v = 0 keeps R − b ≥ 1.01 on all of [τ0, τ_end] (along it
R and τ increase while b decreases), so with that N the condition holds. Then Lemma 1.1 (a)-(f) hold:
(a), (c), (d), (e) as FAMILIES5.md 4i (D533, D537) shows, with at least the record's margins (ψ ≤ 0, f ≤ 1); (b) by (c)
above; (f) with r_q^♭ := r_q(μ) ≥ r_q(μ0) = q0 by (b), the curvature boundary being {K ≤ l5⁻⁴}, K = 72μ²/R⁸ + (8/3)
e^(−4s) 𝒜ℬ/R⁶ (twodt5 T1), which gives R ≥ r_q(μ) ≥ q0 when 𝒜ℬ ≥ 0. Every past causal curve from Ω₂ meets Σ_τ0 inside
Ω₂ (record's (d)-(e)), so both generators reach Σ_τ0 transversally (they are null, dτ timelike). Compactness is (d).

(f) *The computed example (twobg5 G2, floating point).* Corner mass 1.5 at R = 5; packet ℬ = 1.7 b(u; 5.7, 7.2) on N′;
shell 𝒜 = 3.6 b(v; 3, 4.5) on N (b a C^∞ bump); seed μ0 = 0.82211; outer mass after the shell 3.6058. At n = 40, 80,
160: structure, mass bound, trapped R = a, past-closedness as above; the diamond lies at R ≥ 2.59 and is untrapped; on
Σ_τ0 (τ0 = −a + 0.02) the packet lies at R ∈ [1.861, 3.431] between the seed's horizon 0.907 and the shell's inner edge
3.825, which meets the record's rule. The rectangle stops at v = 5: inside the hole the double-null grid thins
exponentially (FAMILIES5.md 4i, D3), and there the background is region III's ingoing Vaidya (a), whose mass and ψ
are read on u = u2 + 0.1 from the diamond's solution (nit 7); twobg5 G4 integrates its outgoing rays (round 2).

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
- *The constant on Ω₂* (computed, twobg5 G2 (vii) and G4; corrected in round 2, the verifier's nit 5): |g0⁻¹(dv̂, du)|
  off the trapped region (R² ≥ 1.5μ) has least value 0.181, 0.138, 0.148 at n = 40, 80, 160 (stable to 10 %, not
  monotone in n; round 1 quoted the n = 160 value alone), and on R = a it equals 0.892, 0.446, 0.240 at v = 0.5, 1, 1.5
  (converged to 1 %). Its least value over every computed cell, 0.131, 0.071, 0.042 at n = 40, 80, 160, is **not
  converged**: each finer grid reaches further into the strip near R = a at late v (v ≈ 4.5-4.9), where the double-null
  grid thins. G4 resolves it along region III's outgoing rays, where ψ and μ depend on v alone and d ln|R_u|/dv = v̂′
  e^ψ μ/R³: on R = a the symbol is 0.892, 0.446, 0.240, 0.134, 0.0758, 0.0434, 0.0266, 0.0212, 0.0183, 0.0156 at v =
  0.5, 1, 1.5, ..., 4.5, 4.9 (agreeing with the grid at v = 0.5, 1, 1.5 to 1 %, with n = 80 and 160 coefficients to 2
  %), decreasing in v, at a rate per unit v of 1.4 falling to 1.1 by v = 3 and 0.3-0.5 once the shell has raised the
  mass. Its value at v = 4.9, about 0.016, is below the grid's least value at every n, which is what the grids were
  approaching. Analytically d ln(sym)/dv̂ = −ψ′ − e^ψ μ/R³ ≥ −ψ′ − μ_max/a³ (= −ψ′ − 10.5 here) on R ≥ a. So the
  non-resonance constant is a positive constant on the compact Ω₂ that **degenerates exponentially with the time spent
  in the hole** (the redshift at the horizon). Theorem 1₂'s constants depend on it; this is harmless for a fixed T, and
  is the quantitative cost of the black hole for the two-family problem.
- *Stage data on Σ_τ0* (deduced): on Σ_τ0 the two families' supports are disjoint (section 1); the pure harmonics are
  transported along their own generators, so they keep their supports in v and in u, and the mixed harmonics are
  algebraic in products of the two families' profiles, so they vanish near Σ_τ0. So the mixed harmonics take no data
  (FAMILIES5.md 4h (d)) **and** vanish on Σ_τ0, which is what the data construction (section 6) needs.

The stage system of Lemma 5.3′ ((a) mean: a wave equation; (b) two phase transports; (c) two pure-harmonic transports;
(d) mixed division) closes on Ω₂ by the record's Picard argument, both generators reaching Σ_τ0 inside Ω₂ (Proposition
B(e)). The mixed division costs one derivative per stage (FAMILIES5.md 4h, verifier 227's correction), harmless for
smooth data and finitely many stages.

## 5. The uniform linear estimate and the bootstrap (Theorem E₂)

**Theorem E₂ (deduced; round 1 gave it in outline, the verifier's item 3; Lemma 3.3₂ and Steps 4-6 are written in full
in section 8, round 2).** The record's Theorem E (N1STAR-PROOF.md 0.4) holds on Ω₂ for a two-phase approximant with
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
- *Lemma 3.3₂* (deduced, 4g; written in full and computed in section 8): contracting with ℓ_in ⊗ ℓ_in kills family
  in's λ⁻¹ term and its □̃φ_in term exactly;
  family out's survive through χ′ alone: ½ λ⁻¹ ((1 − 𝒫) s_out(h)) e^(−4σ) F2² χ′ = O(∂ s_out(h)), λ⁻¹ ((ℓ_app^out −
  ℓ_out) · dφ_out) G2^out(ℓ_in, ℓ_in) = O(|dφ_out|) [R5: listed], and −q c_in Ψ_out, a bounded coefficient at the top
  order of Ψ_out; N_φ^out(ℓ_in, ℓ_in) keeps |w||∂²φ_out|, at most C M λ^(K−4) N₂ in the
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
- *Steps 4-7* (written term by term in section 8, the counting computed in `checks/twoledger5.py`): every new term is a
  bounded two-phase profile times a quantity N₂ controls at the same scaled order; the
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

- Background on Ω₂, outgoing data stated: deduced (via D552/D558, §2 (d)); identities computed; example computed on the
  rectangle v ≤ 5 only (§2, twobg5, twoext5 X1-X2) [R5: label].
- μ ≥ μ0, R = a trapped, past-closed: deduced; computed (G2) with a failing control (§2 (b)-(c)).
- Regularity step of D558: deduced (written) (§2 (d)).
- Constraints on the slice: deduced; S1 symbolic, S2-S4 exact at random points (§6, twoslice5).
- Dynamic outgoing null phase: settled: exact eikonal, and not used by the data (S4) (§3, §6).
- Approximant every order, interactions, non-resonance: deduced; symbol computed; constant computed on Ω₂ (§4, nonres5,
  twobg5).
- Energy estimate, bootstrap: deduced; Lemma 3.3₂ and Steps 4-6 written in full in round 2 (§8), the identities
  computed (twodecomp5 J0-J9), the counting computed (twoledger5 T1-T2), each with failing controls.
- Transport on Ω₂ for both generators: computed (twotransport5).
- Theorem 1₂ items 1-5: **deduced** (§1); read by an independent verifier at commit 169c9b5 with no major gap; round 2's
  sections 8-10 not yet read.
- Theorem 1 item 6 (horizon) for two families: **deduced**, with no placement condition (§9; round 1: not claimed); its
  decisive cancellation proved structurally (h3proof5) [R5].
- Theorem 1 item 7 (mean mass) for two families: **deduced** (§10; round 1: not claimed).

(Round 1 wrote here: item 6 would need the outgoing wave's O(1) oscillating contribution to ∂_R θ⁺ along the columns to
stay below 3/μ near the horizon, which holds where the packet stays away from √μ; item 7 needs both families' first mean
corrections odd. Round 2 computes the O(1) term to vanish at stage 0 (§9, twohorizon5 H3), so no placement is needed,
and computes the outgoing family's parity base (§10).)

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

(c) *Round limits are two null dusts (computed V3-V4; V3 corrected in round 2, the verifier's item 2).* If the limit is
moreover round (as every background of Part I is), what roundness gives is a round stress tensor T, not an invariant
measure, so the argument uses T alone. T's angular block commutes with the isotropy so(3), so it is a multiple of the
round metric (Schur, V3 (a)): T_θθ = T_φ1φ1 = T_φ2φ2 in an orthonormal frame. With (b)'s T_φφ = 0 the multiple is 0, so
∫ p_θ² dμ = T_θθ = 0, and for a positive measure p_θ = 0 on its support (Σ w_i p_θ,i² is positive definite, V3 (b)):
the momenta are radial. Control: without (b) roundness alone does not force this (an isotropic angular measure has a
round block with T_θθ > 0; V3's control, rejected). Radial null
momenta at a point of Vaidya are multiples of dv or of k_out, so T = (∫ E² df_in) dv² + (∫ E² df_out) k_out² (V4),
radial momenta stay radial along radial geodesics, and the Einstein–(radial) massless Vlasov system is, for g, the
Einstein–two-null-dust system. Control (computed, round 2): the V4 measure with one more momentum carrying p_θ ≠ 0 has
T_θθ > 0, so it is not of the two-dust form.

**Consequence (deduced).** Within the round T² class every round massless Vlasov limit is a solution with two radial
null dusts, one ingoing and one outgoing; those of section 2's form (a seed, an ingoing shell, an outgoing packet between
them on Σ_τ0) are realised by Theorem 1₂ as limits of vacuum metrics. [R5, the verifier's major finding: Part III proves
the two radial dusts, not that every round limit has section 2's configuration; the earlier "adds nothing to Part I" is
withdrawn.] No infinite number of families is
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

# Part V. Round 2 (2026-11-02)

Labels as above. Programs added: `checks/twodecomp5.py` (exact rational arithmetic at random points, from the full
reduced Ricci tensor; about three minutes), `checks/twoledger5.py` (seconds), `checks/twohorizon5.py` (H1-H2 exact,
sympy; H3 symbolic up to three sample points, then 30 digits; about half an hour), `checks/twoparity5.py` (exact,
sympy; about ten minutes); amended: `checks/twobg5.py` (G3-G5),
`twotransport5.py` (T3), `axisphase5.py` (A4), `torusstress5.py` (V3, V4's control). Each has its `.out`; every check
has a control that the program must reject, and does.

## 8. Lemma 3.3₂ and Steps 4-6 of Theorem E₂, in full

*Setting.* Ω₂, Σ_τ, A(τ) = {a ≤ |x| ≤ b(τ)} in the chart (τ, x = R x̂), τ = v̂ − R (section 2 (e)); k = 6, K ≥ 6; every
constant depends on Ω₂, k, K and the profiles, never on λ. The phases are ϕ_in := v̂ and ϕ_out := u (section 3), s1 :=
v̂/λ, s2 := u/λ, F_K := ∂_(s_K), k_in := dv̂, k_out := du, ℓ_K := g0⁻¹ k_K; g1^(K) is family K's wave with its second
harmonic (χ_in dv̂², χ_out du²); Y_K := F_K g1^(K) + λ F_K ĝ_2 (a two-phase profile), G1^K := [F_K g1^(K)], G2^K :=
[F_K² g1^(K)], c_in := G1^out(ℓ_in, ℓ_in), c_out := G1^in(ℓ_out, ℓ_out). P is the linearisation of Ric^H at g_app,
written with the principal part −½ g^ab ∂_a ∂_b at the full metric g = g_app + w, as the record's (3.2).

*The facts used, each computed (twodecomp5, at three random points of the general round double-null background with
both families' stage-0 waves and a mixed λ² profile, from Ric^H; controls (a)-(f) rejected). [R5: J1-J7 exercise the
principal part −½ g^ab ∂_a ∂_b of Ric^H, which is what (F1)-(F3) claim (dropping ΓΓ from Ric, or breaking the
tracelessness of the waves, leaves them true); J0 holds for any operator commuting with translations in s.]*

- (F1) λ⁻² and λ⁻¹ of P on a slow h: no λ⁻² term; the λ⁻¹ term is ½ λ⁻¹ Σ_K s_K(h) G2^K, s_K(h) := h(ℓ_K, ℓ_K), in all
  fifteen components (J1, J5; twolin5 L1 had h constant). Control (a), plain Ric: fails.
- (F2) Lemma 3.2₂: for φ(X), P(φ Y_K) = φ P(Y_K) − λ⁻¹ (ℓ_app^K · dφ) G2^K − ½ (□̃_app φ) G1^K − ½ λ (□̃_app φ) [F_K ĝ_2]
  + B1^K · dφ + C1^K φ + N_φ^K, B1^K, C1^K bounded profiles, |N_φ^K| ≤ C |w| (λ⁻² |φ| + λ⁻¹ |dφ| + |d²φ|) with the second
  derivatives of φ in N_φ^K multiplying Y_K. Computed: the commutator P(φ Y_K) − φ P(Y_K) has no λ⁻² term (J1), its λ⁻¹
  term is −(ℓ_K · dφ) G2^K exactly, with no term in the other family's generator (J2), and with φ(p) = dφ(p) = 0 its λ⁰
  term is −½ (g0^ab ∂_a ∂_b φ) Y_K (J3): second derivatives of φ enter only through □̃φ (J3 works in the double-null
  chart; the Cartesian □̃ of section 2 differs from it by first-order terms in φ, which join B1^K · dφ). Control (a):
  fails J2, J3.
- (F3) Lemma 3.1₂: P(Y_K) = [T1^K], a bounded profile. Computed: D Ric^H[G](F_K G) = F_K Ric^H[G] at orders λ⁻², λ⁻¹,
  λ⁰ for G = g0 + λ W + λ² Q, both K (J0), which with (E2) (stage 0 solved: stage0two5 T1-T4) is T(F_K g1^(K)) +
  P_(−2)(F_K ĝ_2) = O(λ). Control (b): the direction λ F_1 W without λ² F_1 Q fails J0, so λ F_K ĝ_2 belongs in Y_K.
- (F4) contractions (J4; twophase5 Q2): G1^in(ℓ_in, ·) = G2^in(ℓ_in, ·) = 0 and G1^out(ℓ_out, ·) = G2^out(ℓ_out, ·) = 0;
  c_in = e^(−4σ) F2 χ_out and G2^out(ℓ_in, ℓ_in) = e^(−4σ) F2² χ_out (double-null normalisation; with v̂ a factor v̂′²),
  bounded profiles oscillating in s2 with no λ⁻¹; ℓ_app^in − ℓ_in = λ e^(−2σ) χ_out ℓ_out + O(λ²) and g_app⁻¹(dv, dv) =
  −λ e^(−4σ) χ_out + O(λ²), and the mirrors. Control (d), χ_out on du dv: fails.
- (F5) (J8) q := g0^ττ/g^ττ, c^ab := g0^ab − q g^ab: c^ττ = 0 and c^ab = (g0^ab (g^ττ − g0^ττ) − g0^ττ (g^ab −
  g0^ab))/g^ττ, so |c| ≤ C |g⁻¹ − g0⁻¹| ≤ C (λ + |w|) (g0^ττ ≤ −1 on Ω₂, Lemma 1.1′ (a), so g^ττ ≤ −1/2 for |g −
g0| small). (J9) □̃ s(h) =
  (□̃h)(ℓ, ℓ) + 2 g0^ab ∂_a(ℓ ⊗ ℓ) · ∂_b h + h · □̃(ℓ ⊗ ℓ). Controls (e) q = 1, (f) without the cross term: fail.
- (F6) Lemma 3.4₂ (twophase5 Q1): Ψ_K := □̃ φ_K obeys L_K Ψ_K + a_K Ψ_K = ½ □̃ P s_K(h) − ½ M_K(P s_K(h)) − N_K φ_K, L_K
  := ℓ_K · ∂, a_K = 2 L_K R/R, M_K, N_K first order with bounded coefficients; every second derivative of φ_K is a
  bounded combination of L_K P s_K, ∂_x P s_K, dφ_K and ∂_x² φ_K, and ∂_x² φ_K obeys L_K(∂_x² φ_K) = ½ ∂_x² P s_K(h) +
  (bounded) ∂_x² φ_K + (bounded) ∂_x φ_K (the commutator [∂_x², L_K] has the smooth λ-independent coefficients ∂_x ℓ_K).
- (F7) transports (twotransport5 T1-T3): in the chart ℓ_in = −e^(−ψ) L0 and ℓ_out = ℓ_out(τ) Z_out, Z_out = ∂_τ + c_out
  x̂ · ∂_x, c_out ∈ (−1, 1], c_out(a) < 0; ℓ_out(τ) ≠ 0 on the compact Ω₂ (a null vector is never tangent to a spacelike
  slice), so |ℓ_out(τ)| ≥ c > 0. Lemma 2.4 holds for both, the boundary terms having the record's sign.

**The phases (3.4₂).** Given w on [τ0, τ*], (φ_in, φ_out) solves ℓ_K · dφ_K = ½ P s_K(h), h := w − Σ_J φ_J Y_J, φ_K = 0
on Σ_τ0. Since s_K(h) = s_K(w) − Σ_J φ_J [Y_J(ℓ_K, ℓ_K)], this is a linear system of two transports along transversal
null generators coupled through the bounded maps φ ↦ ½ P([Y_J(ℓ_K, ℓ_K)] φ) (M1); by (F7) and Lemma 2.4 the solution map
of the transports is a contraction in C([τ0, τ0 + δ]; L²(A(τ)))² for δ small independently of the data, so Picard
iteration on successive slabs gives a unique solution on [τ0, τ*] (deduced); it is smooth (P smooths in x at fixed λ,
(M6) in τ). The estimates below use this form, with s_K(h): N₂ controls h, and the coupling is inside h.

**The equation for h (3.5₂).** With F := −Ric^H(g_app) and N(w) the terms of second and higher order,

    −½ g^ab ∂_a ∂_b h + B·dh + C·h = F + N(w) − Σ_K N_φ^K − ½ λ⁻¹ Σ_K ((1 − P) s_K(h)) G2^K
          + λ⁻¹ Σ_K ((ℓ_app^K − ℓ_K) · dφ_K) G2^K − Σ_K φ_K [T1^K] + ½ Σ_K (□̃_app φ_K) G1^K
          + ½ λ Σ_K (□̃_app φ_K) [F_K ĝ_2] − Σ_K (B1^K · dφ_K + C1^K φ_K).                                      (3.5₂)

*Proof (deduced from F1-F3).* Write w = h + Σ_K φ_K Y_K in Ric^H(g_app + w) = 0, use P(φ_K Y_K) = φ_K P(Y_K) + (F2) and
(F3). The λ⁻¹ terms are ½ λ⁻¹ Σ_K s_K(h) G2^K − λ⁻¹ Σ_K (ℓ_app^K · dφ_K) G2^K; by (3.4₂) this is ½ λ⁻¹ Σ_K ((1 − P)
s_K(h)) G2^K − λ⁻¹ Σ_K ((ℓ_app^K − ℓ_K) · dφ_K) G2^K. Computed (J7): with dφ_K(p) fixed by ℓ_K · dφ_K = ½ (s_K(h) −
ρ_K), ρ_K arbitrary (standing for (1 − P) s_K(h)), the λ⁻¹ coefficient of P(h) + Σ_K (P(φ_K Y_K) − φ_K P(Y_K)) is
exactly ½ Σ_K ρ_K G2^K in all fifteen components. Control (c), φ_in transported along ℓ_out: a λ⁻¹ term remains. ∎

**Lemma 3.3₂ (the ℓ_in ⊗ ℓ_in component; deduced from (3.5₂), F4, F5).** With s := s_in(h),

    □̃ s = c1 · dh + c0 · h + Σ_K (c2^K · dφ_K + c3^K φ_K) − q c_in Ψ_out + q λ⁻¹ ((1 − P) s_out(h)) G2^out(ℓ_in, ℓ_in)
          + Σ_K c4^(K,ab) ∂_a ∂_b φ_K − 2q F(ℓ_in, ℓ_in) − 2q N(w)(ℓ_in, ℓ_in) + 2q Σ_K N_φ^K(ℓ_in, ℓ_in)
          + Σ_(a, i) c^(ai) ∂_a ∂_i h,

with c0, c1, c2^K, c3^K bounded profiles, c_in and G2^out(ℓ_in, ℓ_in) bounded profiles oscillating in s2, |c4^K| ≤ C λ,
|c^(ai)| ≤ C (λ + |w|), |∂ c^(ai)| ≤ C (1 + |∂w|), i spatial. N_φ^in(ℓ_in, ℓ_in) contains second derivatives of φ_in
only with a factor λ |w|; N_φ^out(ℓ_in, ℓ_in) contains |w| |∂²φ_out|. The only coefficient of order λ⁻¹ multiplies
(1 − P) s_out(h), which is O(λ ∂ s_out(h)) by (M3). The mirror statement holds for s_out(h), with ℓ_out ⊗ ℓ_out, c_out
and Ψ_in.

*Proof.* (J9): □̃ s = (□̃h)(ℓ_in, ℓ_in) + (terms c1 · dh + c0 · h, ℓ_in smooth and λ-independent). (F5): (□̃h)(ℓ_in,
ℓ_in) = q (g^ab ∂_a ∂_b h)(ℓ_in, ℓ_in) + Σ c^(ai) ∂_a ∂_i h(ℓ_in, ℓ_in) + (first order), and (g^ab ∂_a ∂_b h)(ℓ_in, ℓ_in)
= −2 × (the right side of (3.5₂) − B·dh − C·h)(ℓ_in, ℓ_in). Contract (3.5₂) with ℓ_in ⊗ ℓ_in using (F4). Family in: G1^in
(ℓ_in, ·) = G2^in(ℓ_in, ·) = 0 remove its λ⁻¹ term, its (ℓ_app − ℓ) term and ½ (□̃_app φ_in) G1^in exactly; ½ λ
(□̃_app φ_in) [F1 ĝ_2](ℓ_in, ℓ_in) is O(λ |∂²φ_in|). Family out: −½ λ⁻¹ ((1 − P) s_out) G2^out(ℓ_in, ℓ_in) survives (the
λ⁻¹ term, times −2q); λ⁻¹ ((ℓ_app^out − ℓ_out) · dφ_out) G2^out(ℓ_in, ℓ_in) is O(|dφ_out|), |ℓ_app^out − ℓ_out| ≤ C λ
(F4); ½ (□̃_app φ_out) c_in = ½ c_in Ψ_out + O(λ |∂²φ_out|) (□̃_app = □̃ + O(λ) ∂², the record's Lemma 3.4); the rest
are first order or N_φ. Computed (J6): the ℓ_in ⊗ ℓ_in contraction of the commutator's λ⁰ term, with φ_in, φ_out
quadratic at p, is −½ (□̃ φ_out) c_in exactly: φ_in drops out and φ_out enters only through □̃ φ_out, with no λ⁻¹;
the mirror for ℓ_out ⊗ ℓ_out. And (J7) the contraction of the λ⁻¹ coefficient is ½ ρ_out G2^out(ℓ_in, ℓ_in). ∎

**The norm, Steps 1-3.** N₂(τ) := Σ_(j≤k) λ^j (‖∂^j ∂h‖ + Σ_K (‖∂^j Ψ_K‖ + ‖∂^j ∂φ_K‖ + λ ‖∂^j ∂_x² φ_K‖)) + ‖h‖ +
Σ_K ‖φ_K‖ (8.1). Step 1: λ^j ∂^j(φ_K Y_K) is a sum of λ^i ∂^i φ_K times bounded profiles, and λ^i ‖∂^i φ_K‖ ≤ λ N₂ (1
≤ i ≤ k + 1), so |w|_(k+1) ≤ C N₂, ‖∂^i w‖_∞ ≤ C λ^(−3−i) N₂ (i ≤ 4), |∂w|_k ≤ C λ⁻¹ N₂. Step 2: φ_K = 0 on Σ_τ0, so h =
w there; ∂_τ φ_K = ½ P s_K(h)/ℓ_K(τ) there (F7, no 1/λ), and the higher τ-derivatives follow from (3.4₂), (3.5₂) and
the equation, so N₂(τ0) ≤ C (C_D + C_R) λ^K. Step 3: if N₂ ≤ 2M λ^K on [τ0, τ*], then |w| ≤ C M λ^(K−3), |∂w| ≤ C M
λ^(K−4), and for λ ≤ λ0(M) g = g_app + w keeps Proposition B (e)'s open conditions (Σ_τ and the lateral boundaries
spacelike, both generators transverse to Σ_τ) and |∂g| ≤ M1.

**Step 4 (h).** Apply ∂^α, |α| = j ≤ k, to (3.5₂), Lemma 2.3 to each component, and multiply by λ^j. Term by term (the
exponent and highest order of each computed in twoledger5 T1, 28 rows for this step):
(a) the commutator [∂^α, g^ab] ∂_a ∂_b h: ‖∂^i g_app‖_∞ ≤ C λ^(1−i), so ≤ C N₂, and the w part ≤ C M λ^(K−4) N₂;
(b) F: ≤ C_R λ^K by (E3); (c) B·dh, C·h: ≤ C N₂ (a derivative on a profile costs λ⁻¹, paid by the weight);
(d) ½ λ⁻¹ ((1 − P) s_K(h)) G2^K: Σ_i λ^(i−1) ‖∂^i (1 − P) s_K‖ ≤ C Σ_i λ^i ‖∂^i ∂ s_K‖ ≤ C N₂ by (M3), (M4), (M6);
(e) λ⁻¹ ((ℓ_app^K − ℓ_K) · dφ_K) G2^K: ℓ_app^K − ℓ_K is λ times a profile (F4), so ≤ C N₂;
(f) φ_K [T1^K], B1^K · dφ_K, C1^K φ_K: ≤ C N₂;
(g) ½ (□̃_app φ_K) G1^K = ½ Ψ_K G1^K + ½ (c^ab ∂_a ∂_b φ_K) G1^K, |c| ≤ C λ: the first ≤ C N₂ because both Ψ's are in
    N₂ at every level; the second by (F6), λ^(j+1) ‖∂^j ∂² φ_K‖ ≤ C N₂ (λ^(j+1) ‖∂^j L_K P s_K‖ ≤ C λ^(j+1) ‖∂^j ∂ s_K‖
    by (M4), (M6); no Bernstein inequality is needed here);
(h) ½ λ (□̃_app φ_K) [F_K ĝ_2] = λ (Ψ_K + O(λ) ∂² φ_K) × profile: ≤ C λ N₂;
(i) N_φ^K: ≤ C M λ^(K−5) N₂ ≤ C M λ N₂ (K ≥ 6; its |w| |∂² φ_K| part ≤ C M λ^(K−4) N₂);
(j) N(w): ≤ C λ⁻⁵ N₂² ≤ C M² λ^(2K−5) ≤ C M² λ^(K+1) (K ≥ 6); at the top derivatives of w this uses Moser's product
    estimate [R5]. (The g0 part of [∂^α, g^ab] in (a) and the commutator [∂_x², L_K] of Step 5 have smooth λ-independent
    coefficients and no ledger row; they are ≤ C N₂ trivially [R5].)
So Σ_(j≤k) λ^j ‖∂^j ∂h(τ)‖ + ‖h(τ)‖ ≤ C (N₂(τ0) + ∫_(τ0)^τ (N₂ + C_R λ^K + C M² λ^(K+1))). Nothing in (a)-(j) has a
coefficient of order λ⁻¹ beyond (d), which (M3) pays for; the two families enter (d)-(i) once each.

**Step 5 (φ_in, φ_out).** Each φ_K obeys its own transport (3.4₂), with source ½ P s_K(h). For φ_in, L0 φ_in = −½ e^ψ
P s_in(h) (F7: the record's (3.4) with the smooth bounded factor e^ψ); for φ_out, Z_out φ_out = ½ P s_out(h)/ℓ_out(τ).
Apply ∂^α, |α| = j ≤ k: [Z_K, ∂^α] has smooth λ-independent coefficients and involves derivatives of φ_K of order at
most j, and λ^j ‖∂^α ∂ P s_K‖ ≤ C λ^j ‖∂^(j+1) s_K(h)‖ ≤ C N₂ by (M1), (M4), (M6), s_K(h) = h(ℓ_K, ℓ_K) with ℓ_K smooth;
for λ ∂_x² φ_K, the transport of (F6) with source ½ ∂_x²(P s_K/ℓ_K(τ)) and Bernstein (M2) on one spatial derivative:
λ^(j+1) ‖∂^j ∂_x² P s_K‖ ≤ C λ^j ‖∂^j ∂_x s_K‖ ≤ C N₂. Lemma 2.4 (Lemma 2.4₂ for φ_out, F7) gives the φ-part of N₂(τ)
at most C (N₂(τ0) + ∫ N₂). The form with s_K(h) is what makes this work: written through s_K(w), the source would
contain P([Y_J(ℓ_K, ℓ_K)] φ_J) with an oscillating coefficient, and λ^j ‖∂^j ∂ P(c φ_J)‖ with every derivative on c
costs λ⁻¹ ‖φ_J‖, a power of λ lost (twoledger5 control (a), exponent −1). Without (M2) the ∂_x² φ transport would need
k + 2 derivatives of s (control (e)).

**Step 6 (Ψ_in, Ψ_out).** Apply ∂^α to (F6)'s transport and Lemma 2.4 (c = a_K bounded). In ½ □̃ P s_in = ½ P □̃ s_in +
½ [□̃, P] s_in, insert Lemma 3.3₂.
(a) P of Lemma 3.3₂'s terms: c1 · dh, c0 · h, c2^K · dφ_K, c3^K φ_K ≤ C N₂; the coupling P(q c_in Ψ_out): ‖P(q c_in
    Ψ_out)‖ ≤ C ‖Ψ_out‖ (M1) and λ^j ‖∂^j P(q c_in Ψ_out)‖ ≤ C Σ_(i≤j) λ^i ‖∂^i Ψ_out‖ ≤ C N₂, each derivative on the
    profile q c_in costing λ⁻¹ and the weight paying for it; q λ⁻¹ ((1 − P) s_out) G2^out(ℓ_in, ℓ_in) ≤ C N₂ by (M3);
    c4^K ∂² φ_K ≤ C N₂ by (F6); F, N(w), N_φ: C_R λ^K, C M² λ^(K+1), C M λ^(K−5) N₂; and Σ c^(ai) ∂_a ∂_i h, written
    P ∂_i(c ∂_a h) − P((∂_i c) ∂_a h) with Bernstein on the ∂_i: ≤ C λ⁻¹ ‖c ∂h‖ + C ‖∂h‖ ≤ C N₂ (|c| ≤ C (λ + |w|)), and
    at level j only k + 1 derivatives of h occur (taken directly it would need k + 2: control (c)).
(b) [□̃, P] s_in: the terms with a spatial index by (M5)'s first form, ≤ C ‖∂ s_in‖; the τ-τ term rewritten through
    ∂_τ² s_in = (□̃ s_in − 2 g0^τi ∂_τ ∂_i s_in − g0^ij ∂_i ∂_j s_in)/g0^ττ, after which (M5)'s second form gains λ on
    every term of Lemma 3.3₂ (the coupling included: ≤ C λ N₂) except Σ c^(ai) ∂_a ∂_i h, written ∂_i(c ∂_a h) − (∂_i c)
    ∂_a h and bounded by the first form (the second form on them would cost a derivative at j = k: control (d), the
    record's own remark); g0^ab (∂_a ∂_b P − P ∂_a ∂_b) s_in ≤ C ‖∂ s_in‖ by (M4), (M6).
(c) −½ M_in(P s_in), −N_in φ_in: first order, ≤ C N₂.
So the Ψ_in-part of N₂(τ) is at most C (N₂(τ0) + ∫ (N₂ + C_R λ^K + C M² λ^(K+1))), and the mirror for Ψ_out, whose
source contains P(q′ c_out Ψ_in). The coupling enters through ∫ N₂: Ψ_in and Ψ_out are estimated together, which is why
both are in N₂. Treated as a generic second derivative of φ_out, the coupling would lose a power of λ (control (b),
exponent −1).

**Step 7 (closing).** Steps 4-6: N₂(τ) ≤ C2 (N₂(τ0) + ∫ N₂ + (τ_end − τ0)(C_R λ^K + C M² λ^(K+1))), C2 independent of M
and λ. Gronwall and Step 2: N₂(τ) ≤ C3 ((C_D + 1 + C_R) λ^K + C M² λ^(K+1)). With M := C3 (C_D + 1 + C_R) + 1 and λ0
with C3 C M² λ0 ≤ 1, N₂ ≤ M λ^K < 2M λ^K, improving the bootstrap (computed: twoledger5 T2, with K = 5 failing the
non-linear row, control (f)). N₂ is continuous in τ for a smooth solution, so the bootstrap set is open and closed in
the interval of existence; Step 8 (local existence, continuation, uniqueness) is the record's, on the polygon Ω₂ ⊂ (τ,
R) with the slices spacelike (Proposition B (e)).

*Labels.* Lemma 3.3₂ and Steps 4-7: **deduced**, written above; every identity behind them **computed** (twodecomp5
J0-J9, twophase5 Q1-Q2, twotransport5 T1-T3), the power counting **computed** (twoledger5: 94 terms, each with its
exponent and highest order, passing at k = K = 6 and on k = 6..12 × K = 6..10; controls (a)-(f) rejected). The energy
estimates themselves (Lemmas 2.2-2.4) are the record's, deduced. Theorem E₂ is therefore **deduced**, with the same
standing as the record's Theorem E; round 2's text has not been read by an independent verifier.

## 9. Item 6 for two families: one zero per column of the outgoing expansion

**Proposition 8.1₂ (deduced; computed twohorizon5 H1-H3).** For a column (v̂ and the angles fixed, R varying, in D_T ∩
{τ ≥ τ0}) let θ⁺_λ(R) be the outgoing expansion of the sphere S_(v̂,R) for g_λ, and R_H(v̂) the zero on the column of
the background's θ⁺, that is of R_v (where R² = μ, μ the Misner-Sharp mass there). There are λ1 ∈ (0, λ0], C, δ1 > 0,
independent of λ, such that for λ ≤ λ1 the record's Proposition 8.1 (a)-(c) hold with √μ(v) replaced by R_H(v̂): at
most one zero per column, θ⁺ > 0 above it and < 0 below it; exactly one, R_λ(v̂, ω), with |R_λ − R_H(v̂)| ≤ C λ, on the
columns with R_H(v̂) ≤ v̂ − τ0 − δ1; the spheres below R_H − C λ trapped, those above R_H + C λ untrapped; no inner
apparent horizon. No condition on where the outgoing packet lies is needed beyond section 1's data.

*Proof.* (i) The background. Along g0⁻¹ du = −e^(−2σ) ∂_v the expansion of the spheres is −3 e^(−2σ) R_v/R (H2,
computed), so the future-directed, n(τ) = 1 normalised θ⁺(g0) is a positive multiple of R_v. On a column R decreases in
u (R_u < 0) and ∂_u R_v = R_uv = −e^(2s) μ/R³ < 0 (twobg5 G1 (c)), so ∂_R R_v = e^(2s) μ/(R³ |R_u|) > 0: θ⁺(g0) has at
most one zero on each column, simple, with ∂_R θ⁺ bounded below near it on the compact domain. Where the outgoing dust
vanishes (region III) this is H1's explicit form, θ⁺ = c 3 (1 − μ/R²)/(2R), c = 2R² e^ψ/(R² (2 − e^ψ) + μ e^ψ) > 0, ∂_R
θ⁺ = 3 e^ψ/μ at the zero (control: the ingoing normal's expansion has no zero there); the ingoing expansion is negative
everywhere (R_u < 0). (ii) The approximant. Neither family's fast derivative enters θ± at order λ⁻¹ or λ⁰ (H2: they
enter only as ½ g0⁻¹(k, dϕ) F tr_S W, and tr_S W_K = 0; control: an outgoing wave with a trace on the spheres gives a λ⁰
oscillation in the ingoing expansion). At order λ the outgoing expansion has **no harmonic depending on s2** (H3,
computed): with both families' stage-0 waves and ĝ_2's mixed harmonics fixed by stage 0's division, the λ¹ coefficient
of the expansion along g⁻¹ du has, at three sample points (concrete smooth functions, 30 digits), mixed harmonics and
pure (0, n2) harmonics below 10⁻³¹, against harmonics in s1 alone of 0.37 to 0.91. Control: with ĝ_2 dropped the mixed
harmonics are 4 × 10⁻³ to 0.12 at the three points, so the cancellation is stage 0's division at work. [R5, the
verifier's proof, computed in `checks/h3proof5.py`:] the λ¹ term of θ_du is (terms in s1 alone, with slow derivatives)
+ g0^uv F1(a2), a2 := ½ tr_γ0 Q_AB − ¼ |W_AB|²_γ0 (non-frozen, symbolic in every function: (T)); the angular trace of
Ric^H at λ⁰ is the λ⁰ form of the colliding-plane-wave identity γ^AB Ric_AB = −α⁻¹ □_h α, α = √det γ, whose gauge term
carries only angular derivatives and so is slow, and the mixed harmonics need two fast derivatives, so γ0^AB
R^(0)_AB|mixed = −2 g0^uv F1 F2 a2|mixed (S1); stage 0's division removes every mixed harmonic of R^(0) (S2), so
a2|mixed = 0 for both sign patterns, (1, 1) and (1, −1), and θ_du's λ¹ term has no harmonic depending on s2, for every
function (S3). Controls: without the division a2 has mixed harmonics; with the angular inverse metric's λ corrections
dropped, (T) leaves an s2-dependent remainder. The stage-1 unknowns add no s2-dependence at order λ (deduced:
ĝ_2's pure harmonics enter as ½ g0⁻¹(du, dϕ) F tr_S ĝ_2, which vanishes for ϕ = u since g0⁻¹(du, du) = 0 and is a
harmonic in s1 alone for ϕ = v̂; φ1 enters through ½ g0⁻¹(du, dφ1) F tr_S W = 0; m1 carries no phase), and normalising
the null covector, k_g = c(g)(du + β dv), adds at order λ only s1-dependence (β ∝ g^uu = −λ e^(−4σ) χ_in + O(λ²), c(g)
through W(ℓ_out, ·) = W_in(ℓ_out, ·)). So θ⁺(g_app) = θ⁺(g0) + λ [Th1] + λ² [E] with Th1 independent of s2 and E a
bounded two-phase profile; along a column s1 = v̂/λ is constant, so ∂_R(λ [Th1]) = λ [∂_R Th1], and ∂_R(λ² [E]) = λ²
[∂_R E] + λ (∂_R u)[F2 E] = O(λ). Hence |θ⁺(g_app) − θ⁺(g0)| + |∂_R(θ⁺(g_app) − θ⁺(g0))| ≤ C λ along every column, the
record's (iii). (iii) The remainder: θ⁺ is smooth in g and linear in ∂g, and ‖∂^i w‖_∞ ≤ C M λ^(K−3−i) (i ≤ 4, section 8
Step 1) give ≤ C λ^(K−5) ≤ C λ. (iv) The zero: the record's (v), with R_H for √μ and D_T's r_q^♭ (section 2 (f)). ∎

*What round 2 first expected, and what was computed.* Round 1 named two routes: keep the packet off the horizon band, or
bound the outgoing wave's O(1) contribution (∂_R u)[F2 Th1] to ∂_R θ⁺ below 3/μ. The O(1) contribution is computed to
be zero at stage 0 (H3), so neither is needed. The placement holds in the example anyway (twobg5 G5: R(u2, v) −
√μ_III(v) ≥ 0.6127 at n = 40, 80, 160, the inner edge untrapped throughout; a heavier shell, amplitude 16, traps it,
gap −0.617), and is no longer a hypothesis.

## 10. Item 7 for two families: the mean mass

**Lemma 8.2₂ (deduced; computed twoparity5 P1-P4 and stage5.py S2, S4).** Let S act as in the record's Lemma 8.2 with
the phase reflection applied to both phases, s_K → 3π/2 − s_K, and λ → −λ. (a) σ is an isometry of the two-dust g0
fixing every sphere (P3: of every round double-null metric; control: a sheared angular metric is not σ-invariant), and
Ric^H is built from g and g0, so R[S G] = S R[G], the record's (a), now with both phases. (b) The base: both families'
stage-0 waves are S-odd (family in: stage5 S2's "g1 = W S-odd"; family out: P1, with χ_out the unique solution of its
transport, on outgoing Vaidya, where the packet is posed), the whole R^(1) of each family is S-odd in every nonzero
component (family in: stage5 S4; family out: P2, the same seven components; control: one quadrature, which fails in
every component), and ĝ_2's mixed harmonics are S-even (P4: R^(0)'s mixed harmonics with both families on the general
round double-null background satisfy J R^(0)_(−n)(σX) J i^(n1+n2) = R^(0)_n(X), 52 entries; division by −e^(−2σ) n1 n2
is even under n → −n; control: family out with one quadrature fails). Every later stage of Theorem A₂ (Lemma 5.3₂
(a)-(d)) and every choice of Lemma 6.2₂ (Pol O(4)-equivariant per family, the division, the means' and phases' data
as the record's) is the unique solution of a problem that S maps to itself. Hence the two-family profiles have parity
(−1)^j and the first mean correction m1 is σ-odd: σ^* m1 = −m1.

**Proposition 8.2₂ (deduced).** For every sphere S_(v̂,R) in D_T ∩ {τ ≥ τ0} with v̂ ∉ (v_start, v_end) and u ∉ (u1, u2)
(neither family oscillating there), |M[S](g_λ) − μ(S)| ≤ C λ², μ(S) the background's Misner-Sharp mass; elsewhere ≤
C λ. Here M[S](g0) = μ (P3: the record's Hawking mass of the round spheres of every round double-null metric is
R²(1 + 2 e^(−2σ) R_u R_v)).

*Proof.* At such a sphere every oscillating profile vanishes (each family's are supported in its own range; the mixed
ones are products), so g_app = g0 + λ m1 + λ² E there, and M[S](g_λ) = μ(S) + λ DM[m1] + O(λ²) + O(|w| + |∂w|).
DM[σ^* m] = DM[m] by naturality (σ fixes g0 and S), so DM[m1] = −DM[m1] = 0 by Lemma 8.2₂; the remainder is ≤ C
λ^(K−4) ≤ C λ². Elsewhere θ± have no λ⁰ oscillation (H2) and the area none (tr_S W_K = 0), so M[S](g_app) − μ(S) =
O(λ). ∎

**Theorem 1₂ items 6-7.** Item 7 follows for Theorem 1₂ as stated above (deduced; its parity base computed for both
families and for the mixed stage-0 harmonics). Item 6 follows (section 9, deduced, its decisive cancellation proved for
every function, h3proof5 [R5]; round 2 had it computed at three sample points).

## 11. The verifier's findings (commit 169c9b5) and their dispositions

1. (Minor) Ω₂ inside Q_(a′) with u0 unconstrained; the first exit. **Repaired** in section 2 (d)-(e): N ∩ {τ ≥ τ0} ⊂
   {R > b(τ)} is now required, at no cost (u ≤ u1 is explicit ingoing Vaidya); computed (twobg5 G3): the example's own
   N fails it (R − b = −4.09 at Σ_τ0, the verifier's case), and the cone from R = 7.505 at v = 0 satisfies it with margin
   1.01. The least-(u + v) first-exit argument is written out, with D, G and ∂G ⊂ {R = a}.
2. (Minor) V3 assumed an SO(3)-invariant measure. **Repaired** in Part III (c) and torusstress5 V3: Schur on T's round
   angular block (computed), with T_φφ = 0 giving ∫ p_θ² dμ = 0 and, by positivity (computed), p_θ = 0; control: an
   isotropic angular measure is round with T_θθ > 0, so without V2 the implication fails.
3. (Minor) Theorem E₂ labelled deduced with Lemma 3.3₂ and Steps 4-6 unwritten. **Resolved** by section 8 (written, the
   identities and the counting computed); the label in section 5 now says so.
4. (Minor) Checks that could not fail. **Repaired**: twobg5's test of the least symbol over every cell (always > 0)
   removed, the quantity reported as not converged and resolved by G4 (with a control that must and does fail);
   torusstress5's (1/2)² > 0 replaced by the computed T_θθ of the V4 measure with a non-radial momentum added;
   twotransport5's sign at a typed y = 0.2 replaced by T3, c_out(a) computed from the mass and the characteristics
   traced back (none reach R = a when R = a is trapped; all 40 do in the untrapped control); axisphase5's typed −2
   replaced by A4, computed from v = τ + r, u = τ − r in R⁴ and on Vaidya, with the control v, 2v rejected.
5. (Nit) The constant's figures. **Repaired** in section 4: 0.181, 0.138, 0.148 off the trapped region at n = 40, 80,
   160; the least over every computed cell (0.131, 0.071, 0.042) reported as not converged; resolved on R = a along
   region III's rays (twobg5 G4).
6. (Nit) dv → dv̂ in Theorem 1₂ item 4. **Repaired**.
7. (Nit) Off the diamond, u > u2 and v > v_end are Vaidya with mass functions from the diamond's solution. **Repaired**
   in section 2 (a).

**What remains open (precisely).** [R5: (i), item 6's decisive cancellation, is withdrawn: proved in section 9
(h3proof5); (iii), an independent reading of sections 8-10, is done (section 12).] (ii) Item 7's induction past the
base (every later stage S-symmetric by uniqueness) is deduced, as in the record, not computed. (iv) The symbol on R = a
beyond the computed rectangle (v > 5) is bounded only by G4's analytic rate μ_max/a³, which is far from the measured
one. (v) J0-J7 of twodecomp5 are exact at three random points of a jet space (strong evidence, not a symbolic
identity), and they exercise the principal part of Ric^H. (vi) Part II's non-round background and Part III's non-round
Vlasov case: [R5] see FAMILIES5-NONROUND.md, FAMILIES5-AXIS.md and FAMILIES5-VLASOV.md.

---

# Part IV. Next step

Round 1's next step (an independent reading of sections 2 and 5, then Lemma 3.3₂ and Steps 4-6 written, then item 6)
is done: the reading found no major gap, and Part V writes the rest. Next: an independent verifier on Part V (sections
8-10 against N1STAR-PROOF.md sections 3-4 and 8, with twodecomp5, twoledger5, twohorizon5 and twoparity5); and a
structural proof of H3's cancellation (section 9).

## Files

`FAMILIES5-FULL.md` (this note); `checks/twobg5.py` (+ `.out`, about ten minutes); `checks/twoslice5.py` (+ `.out`,
about twenty minutes); `checks/nonres5.py`, `checks/twotransport5.py`, `checks/axisphase5.py`, `checks/torusstress5.py`
(+ `.out` each, seconds); round 2: `checks/twodecomp5.py` (+ `.out`, about three minutes), `checks/twoledger5.py`
(+ `.out`, seconds), `checks/twohorizon5.py` (+ `.out`, about half an hour), `checks/twoparity5.py` (+ `.out`, about
ten minutes); round 5: `checks/h3proof5.py` (+ `.out`, about six minutes) [R5].
