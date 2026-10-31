# BEYOND5-R0-PROOF -- each Part re-proved with the lowered inner radius r_♭ (Proposition 6.2)

Status: batch 1 written (D368): sections 0-3 (common facts, Parts I and II, III.B); batch 2 written (D369): section 4
(III.C-III.I3). Batches 3-4 (III.I4-III.K and IV-IV7; V-IX) to follow. Each batch is read by its own verifier.
Labels as marked; "re-proved" means the Part's argument was re-read at every step that touches the inner region, and
each such step re-derived with r_♭.

BEYOND5.md Proposition 6.2 was deduced from a census of lines (`checks/r0census5.py`). This note does what the census
does not: it goes through each Part's proofs and re-derives the steps that use the inner radius or the region next to
it. That covers Parts I and II as well, which the census left out because their radii are abstract. Their hypotheses
are instantiated in Part VI by radii built from the inner radius.

## 0. The setting

- **Choices.** r_♭ ∈ (0, ½R_1], R_1 = μ_0^(1/2), μ_0 = μ_end (Part VII). ε_♭ := min(1/20, r_♭/(4R_1)), and
  ℬ_♭ := {(μ, A) : |μ − μ_0| < ½μ_0, ‖A‖ < ε_♭ R_1}. So ‖A‖ < r_♭/4 on ℬ_♭.
- **III.B's radius.** r_♭ replaces III.B's r_0 = ½R_1 everywhere: M_♭ := cl{|x| ≥ r_♭, t ≥ −½|x|}, Σ^int := {|x| = r_♭},
  X_♭ := cl{|x| ≥ r_♭}.
- **Part I's radii.** Part VI fixes them (VI-DYN 88-89) as r_0^A − 2δ_0 := ½R_1, δ_0 := (r_h − ½R_1)/8 = R_1/16,
  r_0^A := ½R_1 + 2δ_0 and r_2 := r_h − 2δ_0, with r_h = R_1 the horizon of b_0 = (μ_0, 0). Here δ_0 is kept at the
  record's value R_1/16, and only the inner radius moves: r_0^A − 2δ_0 := r_♭, r_0^A := r_♭ + R_1/8, r_2 := r_h −
  R_1/8 = 7R_1/8 as before. Then 0 < r_0^A − 2δ_0 < r_0^A < r_2 < r_h, since r_♭ + R_1/8 < 7R_1/8 for r_♭ < 3R_1/4.
  So everything Part I places near the horizon is unchanged: U_0 over {|r − r_h| < δ_0} (I.B:1067), the time step
  T_1 ≤ δ_0/8 (I.B:906). Letting δ_0 = (r_h − r_♭)/8 grow instead would have moved those. (I write r_0^A for Part I's
  r_0, to keep it apart from III.B's.)
- **What may change.** Every constant chosen from the inner radius is chosen again from r_♭, and so are the smallness
  parameters downstream (the neighbourhood U of b_0, λ_1, ε, ε_m). Nothing is claimed uniform in r_♭; μ_end, and so
  r_♭, is fixed.

## 1. Common facts

**F1 (Kerr-Schild domain).** For b = (μ, A) ∈ ℬ_♭ and |x| ≥ ½r_♭, the condition of III.B Lemma 3.3 (c) holds. So
g^KS_b is defined, smooth, Lorentzian and Ricci-flat (III.B Proposition 3.4), with H_b > 0, smoothly in b.

*Proof.* s = −½ tr A² = a² + b² ≤ 2‖A‖² in the rotated frame A = aJ_12 + bJ_34 (III.B Lemma 3.1's proof), and
‖A‖² < r_♭²/16. So |x|² ≥ r_♭²/4 > r_♭²/8 > 2‖A‖² ≥ s. By Lemma 3.1 (b), r_A² ≥ |x|² − ‖A‖² > r_♭²/4 − r_♭²/16 =
3r_♭²/16 > 3‖A‖². Hence ‖A‖²(r_A² + ‖A‖²) < (r_A²/3)(4r_A²/3) = (4/9) r_A⁴ < r_A⁴, which is (c). Lorentzian: g^KS_b =
η + H k ⊗ k with k null for η (Lemma 3.3 (a)), and Lemma 3.3 (d) gives the inverse, so g^KS_b is non-degenerate; it
has signature (1, 4) by continuity in H ≥ 0 from η, the determinant not vanishing along the path. ∎

**F2 (inside the horizon, at b_0).** On {|x| ≤ 2R_1}, Φ_μ is a time translation (III.B Lemma 3.5 (c)), so
g_(b_0) = g^KS_(μ_0, 0) there. With f := 1 − μ_0/r², its inverse has g^(−1)(dr, dr) = f, g^(−1)(dt, dr) = μ_0/r² and
g^(−1)(dt, dt) = −(1 + μ_0/r²). On 0 < r < r_h = R_1, f < 0, so dr is timelike. dt is past timelike (the time
orientation of III.B and Part I), and g^(−1)(dt, dr) > 0, so dr lies in the opposite cone: dr is future timelike, and
the future direction decreases r.

*Proof.* k = dt + dr, k^♯ = η^(−1)(k, ·) = −∂_t + ∂_r, H = μ_0/r² at A = 0, and Lemma 3.3 (d): g^(−1) = η^(−1) −
H k^♯ ⊗ k^♯. Then g^(−1)(dr, dr) = 1 − H, g^(−1)(dt, dr) = −H(−1)(1) = H and g^(−1)(dt, dt) = −1 − H. Two timelike
covectors lie in the same cone iff their g^(−1)-product is negative. ∎

**F3 (near b_0).** For every compact interval [a, b] ⊂ (0, r_h) there is a neighbourhood U of b_0 in ℬ_♭ such that for
b ∈ U, on {a ≤ r ≤ b}: g_b^(−1)(dr, dr) ≤ ½ max_[a,b] f < 0 and g_b^(−1)(dt, dr) > 0. So dr is future timelike there,
uniformly. *Proof.* F1 makes g_b^(−1) continuous in b on {|x| ≥ ½r_♭} (Lemma 3.3 (d), smoothly in b). The two strict
inequalities hold at b_0 on the compact set (F2), so they persist on a neighbourhood. ∎

**F4 (the flow inside the horizon).** Let [a, b] ⊂ (0, r_h), U as in F3, and Σ the characteristic set of a
t_*-invariant operator with principal symbol G(ν) = g_b^(−1)(ν, ν), b ∈ U, over {a ≤ r ≤ b}. On each of its two
components the future-directed field H satisfies H r = ±2 g_b^(−1)(ν, dr). This is non-zero and of one sign, because ν
is null, non-zero and in a fixed cone while dr is timelike. Rescaled to fibre infinity it is bounded away from 0
uniformly, by compactness of the sphere bundle over {a ≤ r ≤ b}. So every integral curve entering {a ≤ r ≤ b} leaves it
through {r = a}, forward, within a bounded parameter, and r increases backward. ∎

**F5 (the time functions).** For b ∈ ℬ_♭, dt_* (with ψ from r_♭, (3.6)) and dt_IVP are timelike for g_b on
{|x| ≥ r_♭}, and t_* ≤ t, t_IVP ≤ t. This is III.B Lemma 3.7 at r_♭, re-proved in section 3. ∎

## 2. Parts I and II

**What they use.** Part I (I.A-I.C) and Part II (II.A-II.G2) are proved for abstract radii
0 < r_0^A − 2δ_0 < r_0^A < r_2 < r_h and for any spectral family and metric satisfying (H1)-(H8) (I.A section 1.3,
I.B sections 1.2 and 1.5) and (K1)-(K4) (II.B section 1.1). I listed every line of Parts I and II that names r_0,
δ_0, r_2, ∂_♯X, the artificial boundary or the inner region: 490 lines, by the pattern in the footnote. Of these, 314
are domain or slab notation of a fixed form ({r > r_0 − 2δ_0}, {r ≥ r_0}, Ω_(a,b), "the artificial boundary").
I read the other 176 one by one. Several use δ_0 as a local constant of their own section, unrelated to the radii:
the trapped-set neighbourhoods Γ(δ_0/3) in I.B section 6, the orders s − ½ + δ_0 in II.A2 and II.D, ρ_sf ≥ δ_0 in II.F,
and x_I ≤ δ_0 in II.E section 2. The radii are used in three ways only:

- as the domains of the hypotheses, {r_0^A − 2δ_0 < r < r_2} in (H4) and X̃° = {r > r_0^A − 2δ_0} in (H6), (H8);
- through slabs Ω_(a,b) with r_0^A − 2δ_0 < a < b < r_2 (I.A Propositions 6.3-6.4, I.B Propositions 7.1-7.2), on which
  the energy estimates use only that dr is future timelike (I.A section 6.2);
- through constants chosen from them, each by an inequality that a smaller r_0^A does not make harder:
  - II.F2 Lemma 2.3: Ω_♮ = {t_* ≥ ½, r_0^A − 2δ_0 < r ≤ r_0^A + 4}, with ε_I² < (2r_0^A + 9)^(−1) and
    (ε_ι δ_ι)^(−1) > r_0^A + 4. Both are choices of small constants, easier for smaller r_0^A. Ω_♮ is used only as the
    set where the order function is the constant s_in (II.F2:221-243, 261, 313, 332, 468). It is not asked to contain
    the horizon.
  - II.F2 (before Lemma 2.4): κ ∈ (0, ¼] with r_0^A − 2κ > r^♯ and r_0^A + 4κ ≤ r^♮. Here r^♯ ∈ (r_0^A − δ_0, r_0^A)
    (II.E Lemma 1.2) and r^♮ > r_0^A (II.D (1.2)), so κ exists.
  - II.E:565, (ε_ι δ)^(−1) > r_h + 1; II.C:459, c_1 from compactness of {r_0^A ≤ r ≤ r^♮} with (H4); II.A:1050,
    ⟨x⟩ ∼ r on {r ≥ r_0^A > 0}; I.C:443, the interior chain over {r < 4R_1}. Each is a constant, or a region that
    contains the inner one whatever r_0^A is.
  - I.A:1304-1320 (cut-offs on {|x| ≤ 3/2 r_0^A}, {|x| < 5/4 r_0^A}, dilations D_λ, λ ∈ [1, 2], mollifiers of radius
    below (λ − 1) r_0^A) and II.C:380 (r^♮ := ½(r_0^A + r_2)): proportional to the radii.
  - II.F:2115 (T_+ := max(2, 2r_0^A)) and II.G:542 (r′_0 − 1 > r_0^A, r′_0 > r_2 being free in II.C Lemma 3.2):
    constants, easier for smaller r_0^A.

None uses a number tied to ½R_1. So Parts I and II hold at the new radii once their hypotheses do.

**The hypotheses at the new radii.** Part VI checks them for the record's metrics (I.B section 1.5's last
paragraph); that check is re-proved in batch 4. Here, the hypotheses that involve the inner region and why they hold:

- (H1) and (H6): G_0 is g_b^(−1) restricted to the annihilator of ∂_(t_*), and g_b is defined, smooth and Lorentzian on
  X̃° = {r > r_♭} (F1). dt_* is past timelike there (F5).
- (H4) on {r_♭ < r < r_2}: G_0 is Lorentzian, dr is timelike for it, and H r < 0 on ∂Σ_0 (F2, F3 with [a, b] =
  [½r_♭, r_2 + δ_0]; r_2 + δ_0 = 15R_1/16 < r_h). G_0 contains the timelike dr, and the restriction of a Lorentzian
  form to a hyperplane containing a timelike covector is Lorentzian (I.A's remark under (H4)). Every curve reaches
  {r < r_0^A − δ_0} at a finite parameter: F4 on [r_0^A − δ_0, r_h − ε], with the record's own argument near the
  horizon unchanged, since nothing there moves.
- (H8) (a) forward: curves not trapped tend to R_out or reach {r < r_0^A − δ_0} in finite time. This is F4 inside the
  horizon; outside, nothing has moved. Backward: inside the horizon r increases (F4), so a curve from the new part of
  the region reaches the old region in a bounded parameter and then behaves as before.
- (H2), (H3), (H5), (H7), (K1)-(K4) concern infinity, the horizon, the trapped set (which lies in {r > r_2}; for
  Tangherlini it is at r = (2μ_0)^(1/2) > r_h) and uniformity. None involves the inner region, and none changes.

*Status:* Parts I and II re-proved in the sense above, given Part VI's checks (batch 4).

## 3. III.B

Read in full at sections 2, 3 and 5 and at every statement of 3.4 and 6 (statement list at its headings). Each use
of the inner radius, re-derived:

- **Definition 2.1, (2.1).** M_♭ and Σ^int are defined for every r_♭ > 0. The blow-ups are at infinity.
- **Lemma 2.2.** The diffeomorphism cl_M′{t_0 ≥ 1} → cl_M{t_0 ≥ 1} is built from the charts (2.2), all at infinity. It
  holds for X_♭ as for X.
- **Lemmas 3.1, 3.3, Definition 3.2, Proposition 3.4** are stated on {|x|² > s}. On {|x| ≥ ½r_♭} and ℬ_♭ they apply by
  F1.
- **The parameter set (157-161).** ℬ_♭ replaces ℬ, and F1 replaces the line's computation. The horizon of g^KS_(μ,0) is
  at |x| = μ^(1/2) ∈ (R_1/√2, √(3/2) R_1), inside {|x| > r_♭}, since r_♭ ≤ ½R_1 < R_1/√2.
- **Lemma 3.5 (c).** T_μ is smooth and bounded, with T′_μ = −2χ_∞ μ/(ρ² − μ) supported in ρ ≥ 2R_1. So Φ_μ is a
  diffeomorphism of ℝ_t × {|x| ≥ r_♭}, a time translation on {|x| ≤ 2R_1}. The extension to M̃ is at infinity.
- **Proposition 3.6.** Its proof is at infinity, plus smoothness of g^KS_b on M_♭, which is F1.
- **(3.6) and Lemma 3.7.** ψ(ρ) := ∫_(r_♭)^ρ (1 − χ_∞(s) 8μ_0/s²) ds.
  - (a) β = 1 off supp χ_∞ ⊂ [2R_1, ∞), and on it the record's computation, which does not involve the inner radius,
    gives β ∈ (−1, 1). So β ∈ (−1, 1] on [r_♭, ∞), and Lemma 3.3 (e), valid there by F1, makes dt_* timelike.
  - t_* ≤ t: ψ = ρ − r_♭ ≥ 0 on [r_♭, 2R_1], and ψ(2R_1) = 2R_1 − r_♭ ≥ 3/2 R_1. On [2R_1, 3R_1], ψ′ ≥ 1 − 8μ_0/(4μ_0)
    = −1, so ψ ≥ ½R_1 > 0. On [3R_1, ∞), ψ′ ≥ 1 − 8/9 > 0. So ψ ≥ 0.
  - (b) unchanged: ψ_IVP′ := ψ′ on [r_♭, 5R_1], then non-negative and at most ψ′, vanishing beyond R_3, and
    ψ_IVP(r_♭) = 0. The β-bounds on [5R_1, ∞) do not involve the inner radius; ψ_IVP ≥ 0 as before.
  - The constant C′ in ψ(ρ) = ρ − C′ + 8μ_0/ρ (ρ ≥ 3R_1) changes; it is used only as a constant (the form of [Hin26]
    (3.13)).
- **Lemma 3.9 (data on Σ_IVP).** The induced data need Σ_IVP ∩ M_♭ spacelike, which is F5.
- **Lemma 5.1 (cut-off boosts).** V(S_w) vanishes on {|x| ≤ 5R_1}, which contains Σ^int for every r_♭ ≤ ½R_1. It is
  unchanged.
- **Section 6.** c_Υ ∈ |x|^(−1) C^∞(X_♭; T*) must be smooth and stationary on X_♭. The record's c (10.49; IV6-SOLV Lemma
  0.2 (d)) is, up to positive factors, dt + (v/2) dr on r ≤ r_c/2: smooth for r > 0. The trace-weight Lemma 6.2 and
  Lemma 6.3 are algebraic.

*Status:* III.B re-proved at r_♭.

## 4. III.C to III.I3

**Which r_0.** Part III writes r_0 for two radii:

- in its stationary Parts (III.D-III.G), which work on Part I's X̄ (I.A section 1.1) and cite I.A Theorem 7.2, it is
  Part I's r_0^A, now r_♭ + R_1/8, with Part I's δ_0 = R_1/16;
- from III.H on (the spacetime spaces of II.A and III.H section 1, and III.K, which says "r_0 the inner radius (III.B
  (3.6))"), it is the spacetime inner radius, now r_♭ (III.K) or Part II's r_0^A.

Each step below is checked at both values where the reading is not plain. Where r_0 − δ_0 occurs (III.F3 Lemma 2.3,
III.F4 (iii), III.H2:99), it is Part I's: r_0^A − δ_0 = r_♭ + R_1/16 > 0. Verifier 168's A2 read F3's r_0 as III.B's,
for which r_♭ − R_1/16 can be negative. With Part I's radii that does not arise, and D366's free choice of δ_0 is not
needed.

**Parts with no inner-boundary step.** III.A, A2, C, D3, D4, E2, F, F2, G-G5 and I2 name no r_0. III.C-III.C″ work with
their own exterior radius "r_0 large" (census class OTHER). The rest reach the inner boundary only through Part I's
spaces and theorems, which hold at the new radii (section 2).

**III.D (Proposition 6.2).**

- (a)-(c) are on {r > r_h} and do not change.
- (d), inside the horizon: in the ingoing chart the harmonic coefficients solve −fU″ + AU′ + BU = 0 with A, B smooth on
  (0, ∞), and (r − r_h)Y′ = MY with M smooth on (0, ∞) (III.D:409-416). The Gronwall bound on [r_1, r_h) holds for
  every r_1 ∈ (r_0, r_h), whatever r_0 > 0 is. So u = 0 on {r > r_0}.
- "u smooth up to {|x| = r_0}" is I.A Theorem 7.2 (5) at the new radii.

**III.D2 (d)** repeats III.D (d) at σ = 0.

**III.E (b)** (vanishing inside the horizon, III.E:118-123; used by III.E Proposition 3.1 and III.F4 Steps 1-2).

- On {r_0 < |x| < r_h}, ∂_(t_*) is spacelike: g_(b_0)(∂_t, ∂_t) = −f > 0 there. The quotient metric is Lorentzian with
  |x| timelike (F2), and both persist for b near b_0 on compacta (F3).
- The Cauchy problem runs on the spacelike {|x| = c} from {|x| < r_0}, where the solution vanishes by the supported
  character, across {|x| = r_0}. That needs the operator hyperbolic in |x| just inside r_0. It is: dr is timelike on
  {½r_♭ ≤ r ≤ r_h − ε} (F2, F3), and the operator is defined on Part I's X̃° ⊃ {r > r_♭} (F1).

**III.F3 (modes).**

- Lemma 2.1 (b): the chart (t_*, r, z) and so the system's coefficients are smooth on (r_0, ∞), for every r > 0
  (III.B's t_* at r_♭).
- Lemma 2.3: the radial system's coefficients are smooth on (r_0 − δ_0, ∞), and on (r_0 − δ_0, r_h − ε] f < 0, so the
  system is regular there. r_0 − δ_0 = r_♭ + R_1/16 > 0.
- Proposition 3.1 (*the interior*): III.D (d) as above.

**III.F4 (zero energy).** Theorem 3.1:

- Steps 1-6 are on {r > r_h}.
- Step 1's H is an angular component, the same in every chart, so smooth on {r > r_0}.
- Step 7 solves the r-row system on (r_0, ∞) in the chart (t_*, r, z), smooth there.
- Section 4: (iii) is F3 Lemma 2.3 at σ = 0, and (vi) is III.D (d).
- Step 2 of the independence proof: a Killing 1-form vanishing on {r_0 < |x| < r_h} vanishes on the connected X°.
  {|x| ≥ r_0} is connected for every r_0 > 0.

**III.F5 (pairings, :33-34, 87-88).** Every pairing has one factor vanishing on {r_0 < |x| < r_h} (III.E (b)), so the
integrations by parts on X produce no boundary term at {|x| = r_0}. That holds at any r_0.

**III.H, III.H2, III.H3.**

- III.H:29: r ≥ r_0 > 0 on X.
- III.H2 section 1: the spaces are extendible at {r = r_0}, a construction for any radius (I.A section 6.1).
- III.H2 Lemma 6.2:
  - the order is constant on {r ≤ r_0 + δ_1}, δ_1 ∈ (0, 1], as II.C Definition 2.4 (3) gives: constant on
    {r ≤ r_Γ}, r_Γ > r_2 > r_0;
  - the defining functions ρ_sf = r^(−1), ρ_K = r/t are bounded factors apart on {r ≥ r_0}, with constants depending
    on r_0;
  - the step *near r = r_0* cuts off with χ_1, vanishing on {r ≥ min(r_0 + δ_1, 3/2 r_0)}, and extends by Seeley's
    reflection in r into {r > ½r_0}. The extension acts on functions in x only and needs no metric there, and ½r_0 > 0;
  - ⟨x⟩ ≤ C r on {r ≥ r_0}, C = C(r_0).
- III.H2:99: constancy over {r_0 − δ_0 ≤ r ≤ r_2 − δ_0}, Part I's radii, as in section 2.
- III.H3 Theorem 4.1: convergence on compact subsets of M° ∩ {r > r_0}.

**III.I3 (:24-28, 90-92, 97, 211-213).**

- The artificial boundary {r = r_0} carries extendible spaces.
- Where a chart near infinity meets {r < r_0}, u is first extended by II.G′ Remark 3.7's Seeley extension in the
  spatial variable. That commutes with ∂_(t_*), and "nothing propagates across {r = r_0}".
- The density argument at 211-213 uses that the forward solution on {r ≥ r_0} depends on f there only, {r = r_0} being
  spacelike: F2, F3 at r_♭.

*Status:* III.C-III.I3 re-proved at r_♭.

Footnote (reading pattern for section 2): lines of PART-I-*.md and PART-II-*.md matching
`r_0(?![0-9])|r_\{0\}|\delta_0|r_2(?![0-9])|\partial_\sharp|artificial|inner`, then filtered for R_1, r_h, μ,
Tangherlini, Myers and numerical relations among the radii.
