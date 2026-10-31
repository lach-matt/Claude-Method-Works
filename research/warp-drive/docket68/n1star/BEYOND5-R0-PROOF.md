# BEYOND5-R0-PROOF -- each Part re-proved with the lowered inner radius r_♭ (Proposition 6.2)

Status: batch 1 written (D368): sections 0-3 (common facts, Parts I and II, III.B); batch 2 written (D369): section 4
(III.C-III.I3); batch 3 written (D370): sections 5-6 (III.I4-III.K, Part IV). Verifiers 169-171 read batches 1-3;
their findings, among them the radius mismatch of section 0, are seated (D372), and its repair is made in proof5
Part VI (D373), with verifier 172's findings seated (D375). Batch 4 written (D374-D375): sections 7-11 (Parts V-IX),
read by verifier 173, whose findings are seated (D378: the inner-boundary input of II.F Lemma 1.3 named in Part VIII and
III.K, the dependences in Part VII, five nits). Each batch
is read by its own verifier. Labels as marked; "re-proved" means the Part's argument was re-read at every step that
touches the inner region, and each such step re-derived with r_♭.

BEYOND5.md Proposition 6.2 was deduced from a census of lines (`checks/r0census5.py`). This note does what the census
does not: it goes through each Part's proofs and re-derives the steps that use the inner radius or the region next to
it. That covers Parts I and II as well, which the census left out because their radii are abstract. Their hypotheses
are instantiated in Part VI by radii built from the inner radius.

## 0. The setting

- **Choices.** r_♭ ∈ (0, ½R_1], R_1 = μ_0^(1/2), μ_0 = μ_end (Part VII). ε_♭ := min(1/20, r_♭/(4R_1)), and
  ℬ_♭ := {(μ, A) : |μ − μ_0| < ½μ_0, ‖A‖ < ε_♭ R_1}. So ‖A‖ < r_♭/4 on ℬ_♭.
- **III.B's radius.** r_♭ replaces III.B's r_0 = ½R_1 everywhere: M_♭ := cl{|x| ≥ r_♭, t ≥ −½|x|}, Σ^int := {|x| = r_♭},
  X_♭ := cl{|x| ≥ r_♭}.
- **Part I's radii, and a repair of the record (D372).** I write r_0^A for Part I's r_0.
  - *The record, until D373.* Part VI fixed Part I's radii (VI-DYN 88-89 then) as r_0^A − 2δ_0 := ½R_1 (III.B's
    inner radius), δ_0 := (r_h − ½R_1)/8 = R_1/16, r_0^A := ½R_1 + 2δ_0 = ⅝R_1, r_2 := r_h − 2δ_0 and r_e := r_h + δ_0,
    with r_h = R_1.
  - *The mismatch.* Part II, and III.D-III.J‴ after it, put the artificial boundary of every space at Part I's r_0^A
    (II.A:38-39; III.H:29, III.H2:30, III.I3:24; verifier 170). III.K and Part VII take III.B's ½R_1 as the inner
    boundary (III.K:43, 84, 103; VII:40). III.K:157 and 183 cite II.C Lemma 3.2 (1), which covers {r ≥ r_0^A} only.
    So, as the record stood, its development was controlled on {r ≥ ⅝R_1}, not on all of III.B's M.
  - *The repair,* made here at r_♭ and so also at the record's ½R_1. Part I's artificial boundary is put at III.B's
    radius, r_0^A := r_♭, with the collar δ_0 := min(R_1/16, r_♭/4) inward. Then X̃° = {r > r_♭ − 2δ_0} ⊂ {r > ½r_♭},
    inside F1's domain. r_2 := 7R_1/8 and r_e := 17R_1/16 keep the record's values.
  - *Ordering.* ½r_♭ ≤ r_0^A − 2δ_0 < r_0^A = r_♭ < r_2 < r_h. At r_♭ = ½R_1, δ_0 = R_1/16, as the record had.
  - *Made in the record (D373).* Part VI now sets r_0^A := ½R_1 and δ_0 := R_1/16, so the collar reaches ⅜R_1; Lemma 1.1
    defines g_b and t_* there by III.B's own formulas, and VI2-VI3 are read on {|x| ≥ ⅜R_1} (VI-DYN finding (VI.A7)).
  - *Near the horizon* only I.B Proposition 5.2's band {|r − r_h| < δ_0} (I.B:1067) involves δ_0, and only when
    r_♭ < R_1/4 does δ_0 shrink. That proposition asserts neighbourhoods inside the band, and its proof is local at
    ∂ℛ_± (Lemma 5.1, "near ∂ℛ_±", I.B:1078-1097), so it holds in any smaller band. I.B:906's δ_0 is a local
    constant of Corollary 4.6 (verifier 169's n1).
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
g^(−1)(dt, dt) = −(1 + μ_0/r²). On 0 < r < r_h = R_1, f < 0, so dr is timelike. Part I orients by dt_*, which is past
timelike (I.B:44). On {|x| ≤ 2R_1}, ψ′ = 1, so dt_* = dt − dr and g^(−1)(dt, dt_*) = −1 − 2μ_0/r² < 0: dt lies in
the same cone and is past timelike too. g^(−1)(dt, dr) > 0, so dr lies in the opposite cone: dr is future timelike,
and the future direction decreases r. For b ∈ ℬ_♭, g_b^(−1)(dt, dt) = −1 − H_b < 0, as k_A^♯(dt) = −1.

*Proof.* k = dt + dr, k^♯ = η^(−1)(k, ·) = −∂_t + ∂_r, H = μ_0/r² at A = 0, and Lemma 3.3 (d): g^(−1) = η^(−1) −
H k^♯ ⊗ k^♯. Then g^(−1)(dr, dr) = 1 − H, g^(−1)(dt, dr) = −H(−1)(1) = H and g^(−1)(dt, dt) = −1 − H. Two timelike
covectors lie in the same cone iff their g^(−1)-product is negative. ∎

**F3 (near b_0).** For every compact interval [a, b] ⊂ [½r_♭, r_h) there is a neighbourhood U of b_0 in ℬ_♭ such that for
b ∈ U, on {a ≤ r ≤ b}: g_b^(−1)(dr, dr) ≤ ½ max_[a,b] f < 0 and g_b^(−1)(dt, dr) > 0. So dr is future timelike there,
uniformly. *Proof.* F1 makes g_b^(−1) continuous in b on {|x| ≥ ½r_♭} (Lemma 3.3 (d), smoothly in b). The two strict
inequalities hold at b_0 on the compact set (F2), so they persist on a neighbourhood. ∎

**F4 (the flow inside the horizon).** Let [a, b] ⊂ [½r_♭, r_h), U as in F3, and G(ν) = g_b^(−1)(ν, ν), b ∈ U, the
principal symbol of a t_*-invariant operator.

- *The sets.* Its characteristic set over {a ≤ r ≤ b} is the null covectors ν. That covers Part I's ∂Σ_0 at fibre
  infinity and I.B's semiclassical Σ_z at finite covectors, ν = −z dt_* + ζ with |z| ∈ [½, 2]. Each splits into the
  future and the past cone. The future-directed field is 𝖧 on ∂Σ_0 (I.A:88-108) and z_0 H_(G_z_0) on Σ_z_0 (I.B:77-79,
  (H7)); its base projection is a positive multiple of the future-directed null vector V = ±g_b^(−1)(ν, ·).
- *The sign.* dr is future timelike (F3), and a future causal vector V has dr(V) < 0 (IV6-SOLV Lemma 0.3's proof).
  So r decreases along the future-directed flow.
- *The bound.* |dr(V)| ≥ c|V| for null V over {a ≤ r ≤ b}, by compactness of the unit null vectors there, dr being
  timelike. At finite covectors |V| ≥ c′(|z| + |ζ|) ≥ c′/2. At fibre infinity the rescaled field is bounded below in
  the same way. So ṙ ≤ −c″ < 0 on all of the characteristic set over [a, b], uniformly in b ∈ U. For Im z > 0, the
  real part of the symbol is used as in I.B Lemma 1.1 (d).
- So every integral curve entering {a ≤ r ≤ b} leaves it through {r = a}, forward, within the parameter (b − a)/c″,
  and r increases backward. ∎

**F5 (the time functions).** For b ∈ ℬ_♭, dt_* (with ψ from r_♭, (3.6)) and dt_IVP are timelike for g_b on
{|x| ≥ r_♭}, and t_* ≤ t, t_IVP ≤ t. This is III.B Lemma 3.7 at r_♭, re-proved in section 3. ∎

## 2. Parts I and II

**What they use.** Part I (I.A-I.C) and Part II (II.A-II.G2) are proved for abstract radii
0 < r_0^A − 2δ_0 < r_0^A < r_2 < r_h and for any spectral family and metric satisfying (H1)-(H8) (I.A section 1.3,
I.B sections 1.2 and 1.5) and (K1)-(K4) (II.B section 1.1). I listed every line of Parts I and II that names r_0,
δ_0, r_2, ∂_♯X, the artificial boundary or the inner region: 489 lines, by the pattern in the footnote. Of these, 313
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
  X̃° = {r > r_♭ − 2δ_0} ⊂ {r > ½r_♭} (F1). dt_* is past timelike there (F5, with ψ′ = 1 continued below r_♭).
- (H4) on {r_♭ − 2δ_0 < r < r_2}: G_0 is Lorentzian, dr is timelike for it, and H r < 0 on ∂Σ_0 (F2, F3 with
  [a, b] = [½r_♭, 15R_1/16], 15R_1/16 ≥ r_2 + δ_0). G_0 contains the timelike dr, and the restriction of a Lorentzian
  form to a hyperplane containing a timelike covector is Lorentzian (I.A's remark under (H4)). Every curve reaches
  {r < r_0^A − δ_0} at a finite parameter: F4 on the fixed interval [½r_♭, 15R_1/16], and the record's own argument
  between 15R_1/16 and the horizon, which does not move.
- (H8) (a) forward: curves not trapped tend to R_out or reach {r < r_0^A − δ_0} in finite time. This is F4 inside the
  horizon; outside, nothing has moved. Backward: inside the horizon r increases (F4), so a curve from the new part of
  the region reaches the old region in a bounded parameter and then behaves as before.
- (H5): the uniform lengths of the curves in (H4) and the uniform convergence in (H8) (I.A:114-115, I.B:169-170)
  inside the horizon are F4's bound (b − a)/c″, uniform over U (verifier 169's m3).
- (H2), (H3), (H7), (K1)-(K4) concern infinity, the horizon and the trapped set, which lies in {r > r_2}; for
  Tangherlini it is at r = (2μ_0)^(1/2) > r_h. On {r ≥ ½R_1} the new t_* differs from the record's by the constant
  r_♭ − ½R_1, ψ changing only by its lower limit, so none of them moves (verifier 169's n3).
- For b ≠ b_0, Part VI states (H4) for Ψ_b^* g_b, which equals g_b on {|x| ≤ ⅝R_1} (VI2-HORIZON:42-44). That set
  contains the inner collar {r ≤ r_♭}, so the bullets above apply to it unchanged (verifier 169's n6).

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
- **Section 4 (null coordinates)** is on {|x| ≥ 3R_1} and does not change (verifier 169's n4).
- **Lemma 5.1 (cut-off boosts).** V(S_w) vanishes on {|x| ≤ 5R_1}, which contains Σ^int for every r_♭ ≤ ½R_1. It is
  unchanged.
- **Section 6.** Definition 6.1's three forms must be smooth and stationary on X̃ = {r ≥ r_0^A − 2δ_0}, which reaches
  below X_♭ (verifier 172's M1): c_Υ (|x|^(−1) dt for large |x|), c_(Υ,H) (compactly supported in {|x| < 5R_1}) and
  c_C (|x|^(−1)(dt − v_C d|x|) for large |x|).
  - c_Υ and c_(Υ,H) are built from dt̄, dr and cut-offs (III.F3:84-85; c_(Υ,H) = −½χ dr): smooth for r > 0.
  - c_C is 10.14's (10.49; IV6-SOLV Lemma 0.2 (d)), up to positive factors dt + (v/2) dr on r ≤ r_c/2. It is smooth
    and past timelike for every r > 0 (`cform5.py` C2).
  - The record checked c_C's conditions (10.14 (i)-(ii); `solv5.py` Q2-Q3) on [r_h/2, ∞). They extend to (0, r_h/2]:
    (1) by C2's formula, (6) by BEYOND5.md's D366 argument. They are conditions on the construction, not (H)/(K)
    hypotheses (verifier 169's m4).
  - The trace-weight Lemma 6.2 and Lemma 6.3 are algebraic.

*Status:* III.B re-proved at r_♭.

## 4. III.C to III.I3

**Which r_0.** III.D-III.J‴ use one radius, Part I's r_0^A: the artificial boundary of Part I's X̄ and of Part II's
spaces (II.A:38; III.H:29; III.H2:30; III.I3:24; verifier 170's finding 1, which corrects this note's first version).
III.B's radius appears only in III.B, III.K (:43, 84, 103) and Part VII. With section 0's repair the two coincide:
r_0^A = r_♭. Where r_0 − δ_0 occurs (III.F3 Lemma 2.3, III.F4 (iii), III.H2:99), it is r_♭ − δ_0 ≥ ¾r_♭ > 0. That
answers verifier 168's A2, and D366's free choice of δ_0 is not needed.

**Parts with no inner-boundary step.** III.A, A2, C, D3, D4, E2, F, F2, G-G5, I and I2 name no r_0 (III.I-CONE:345's
"inner boundary" is that of Ω_ι). III.C-III.C″ work with
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

- On {r_0 < |x| < r_h}, ∂_(t_*) is spacelike: g_(b_0)(∂_t, ∂_t) = −f > 0 there. The quotient metric is Lorentzian,
  with |x| timelike (F2), and both persist for b near b_0 on compacta (F3).
- The Cauchy problem runs on the spacelike {|x| = c} from {|x| < r_0}, where the solution vanishes by the supported
  character, across {|x| = r_0}. That needs the operator hyperbolic in |x| just inside r_0. It is: dr is timelike on
  {½r_♭ ≤ r ≤ 15R_1/16} (F2, F3; the record's argument above that), and the operator is defined on Part I's
  X̃° = {r > r_♭ − 2δ_0} (F1).
- III.E Theorem 1.1 asks c_C to be past timelike on all of X̄ (III.E:37-39). Its inner piece is, for every r > 0
  (`cform5.py` C2; section 3; verifier 170's finding 3).

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
- Section 4: (iii) is F3 Lemma 2.3 at σ = 0, and (vi) is III.D (d). (ii), (iv) and (v) need the states smooth on X̄,
  which is I.C at the new radii (section 2).
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
- III.H3 Theorem 4.1: convergence on compact subsets of M° ∩ {r > r_0}. Its (B2) (III.H3:46-48) takes ε_G from II.C
  Lemma 3.2 over the inner region, with constants uniform over III.H's B̄_1. That set is taken inside F3's U for
  [½r_♭, 15R_1/16] (verifier 170's finding 4).
- III.H:335 and :592 integrate by parts on X with no inner boundary term. That rests on III.E (b): the dual states
  vanish on {r_0 < |x| < r_h}.

**III.I3 (:24-28, 90-92, 97, 211-213).**

- The artificial boundary {r = r_0} carries extendible spaces.
- Where a chart near infinity meets {r < r_0}, u is first extended by II.G′ Remark 3.7's Seeley extension in the
  spatial variable. That commutes with ∂_(t_*), and "nothing propagates across {r = r_0}".
- The density argument at 211-213 uses that the forward solution on {r ≥ r_0} depends on f there only, {r = r_0} being
  spacelike: F2, F3 at r_♭.

*Status:* III.C-III.I3 re-proved at r_♭.

## 5. III.I4 to III.K

**III.I4-III.J‴.** These name no inner radius (III.I16's r_(0,0) is notation; census class OTHER). They work on
Ω_* := cl_M{t^♭_* ≥ 1} (III.I:31-32) with Part II's spaces, extendible at the inner boundary, and Part II's theorems.
Both hold at the new radii (section 2). Section 0's repair matters here: Ω_* is taken in III.B's M, and Part II's
spaces, t^♭_*, II.C Lemma 3.2 and II.F Lemma 1.3 are built at Part II's r_0^A. They agree only when r_0^A is III.B's
radius, now r_♭ (verifier 171's MAJOR, which found the gap in section 0's first version independently of verifier
170). Verifier 171 read III.I4, I5, I7, I8, I9, I11, I12, I13 and III.J-J4: their fixed radii are scale-free
({r ≤ 2}, {r ≥ 1}) or far out (|x| ≥ 5R_1, |x| ≤ 3R_1). Their loops, levels and windows are fixed by weights at
infinity and at K⁺, not by the inner radius (III.J‴'s table).

**III.K.**

- *Setting (:23-47).* t_*, t_IVP and Σ_IVP are III.B's at r_♭ (section 3). F = ψ − ψ_IVP vanishes on [r_♭, 5R_1], so
  t_* ≤ t_IVP as before. R_5, R_6 and the constant C_ψ are at infinity.
- *Lemma 1.1 (d) (:84-86).* ν_0 := min(¼, r_♭/8). On {|t_IVP| < ν_0}, t_* ≤ t_IVP < ¼, so χ_♮(t_*) = 0;
  also |t_IVP| < ν_0 ≤ r_♭/8 ≤ r/8 for r ≥ r_♭, so χ_0 = 0. Only the constant moves.
- *Proposition 1.2 (:96-112).*
  - R_ν := ½(r_♭ + R), R being III.B section 5's radius inside which φ_(±S) is the identity; R = 5R_1 serves
    (III.B:358-361), and R > r_♭. ν vanishes on [0, R_ν], so N = {t_IVP ≥ 0} near {r = r_♭}.
  - The existence of ν uses only 16R_8/64 ≤ (16R_8 − R_ν)/32, which holds as R_8 ≥ max(2r_1, 8, R) ≥ R > R_ν.
  - {r = r_♭} is an inflow boundary for the backward problem: it is spacelike with dr future timelike (F2, F3), and N
    lies to its past.
- *The compact part (:150-188).* 𝒦's boundary pieces are Σ_IVP, {t_IVP = −ν}, Σ_fut,r_1 ∩ {ρ′_I ≥ c}, {ρ′_I = c},
  {t^♭_* = T̂ + 3} and {r = r_♭}.
  - All are spacelike with 𝒦 to their past. Near r = r_♭ the metric is g_(b_0) + h_S, φ_S being the identity on
    {|x| ≤ 5R_1}. {r = r_♭} is spacelike with dr future timelike for it by F2-F3 and continuity in the data.
  - With section 0's repair, III.K's inner radius is Part II's r_0^A = r_♭, so II.C Lemma 3.2 (1), which the record
    cites (:157, 183), applies there as written. F2-F3 is what it rests on.
  - 𝒟's top {t^♭_* = T̂ + 3} is spacelike by II.C Lemma 3.2 (2) on {r ≥ r_0^A} = {r ≥ r_♭}: the strip
    [r_♭, r_0^A) that the first version left to it is now empty (verifier 171's minor).
  - So 𝒦 is a compact domain of dependence. The quasilinear local theory, II.F Lemma 1.3's uniqueness and Cauchy
    stability apply as before.
- *:559.* ν vanishes near {r = r_♭}, as above.
- III.K Proposition 4.2 and the later steps on Ω_* use the inner region through Part II's estimates (section 2) and,
  for b ≠ b_0, through F3's neighbourhood U (verifier 171's nit).

*Status:* III.I4-III.K re-proved at r_♭.

## 6. Part IV

**IV, IV′, IV″, IV‴, IV⁽⁷⁾** (IV-EB, IV2-TAME, IV3-NM, IV4-SLAB, IV7-TFACE). They work on III.C′'s exterior
Ω_ext,r_0 with its own "r_0 large", on the slab near 𝓘⁺, or at the t-face (census class OTHER, or no radius at all).
None reaches the inner boundary.

**IV⁗ (IV5-CDMODES).** :186: ψ − T_μ is continuous on [r_♭, ∞) and tends to +∞, with ψ from r_♭ (section 3) and T_μ
smooth and bounded. :209: the dual space is supported at the inner boundary, a construction for any radius.
:35-36 is the source's r_0 = r_c (OTHER). :136 needs (H1)-(H4) for □^C at the new radii, which is section 2. :170-203
pass modes and a kernel element from Part I's X̄ = {r ≥ r_0^A} to IV6-SOLV at Σ^♯ = {r = r_♭}: with section 0's
repair the two radii are the same (verifier 171's minor).

**IV⁽⁵⁾ (IV6-SOLV)**, with r_♯ := r_♭ and r̂ = ¾R_1 unchanged:

- *Coordinates (:26-34).* g^KS_b is defined, smooth, with H_b > 0, on {r ≥ ½r_♭} (F1, which replaces the record's run
  at ¼R_1). c is 10.14's 1-form, whose inner piece, up to a positive factor, is dt + (v/2) dr on r ≤ r_c/2. It is
  past timelike for g_(b_0) at every r > 0 (`cform5.py` C2), and for g_b, b ∈ U, on the compact {½r_♭ ≤ r ≤ r_c/2}
  by continuity. So the extension IV6:32-34 asks for is the inner formula itself.
- *Definition 0.1.* M^♭ excludes {r < r_♭}, Σ^♯ = {r = r_♭}, and the charts have ρ_sf ∈ [0, r_♭^(−1)]: the
  construction is the same.
- *Lemma 0.2 (c)-(d).* The coefficients of g and c are smooth on {r ≥ ½r_♭} and lie in the stated 3b classes. Their
  behaviour at sf, which the classes see, is unchanged.
- *Lemma 0.3.*
  - (a): Lemma 3.3 (e) wherever (c)'s condition holds, which is {r ≥ ½r_♭} by F1.
  - (b): (a) at β = τ ∈ [0, ½].
  - (c): at b_0, g^(−1)(dr, dr) = 1 − μ_0/r² ≤ 1 − 16/9 on [½r_♭, ¾R_1] (smaller r makes it more negative), and
    g^(−1)(dr, dt) = μ_0/r² > 0. Both strict inequalities persist for b ∈ U on the compact set, as in its proof.
  - (d) is unchanged.
- *Lemma 0.4* (the fibre algebra) is pointwise: his Lemmas 3.3-3.8 and Corollary 3.6 need only c past timelike at the
  point, which holds for every r > 0 (C2). The uniform constant comes from compactness of the unit sphere bundle over
  Ω, now with the inner part {r_♭ ≤ r} included, and continuity in b.
- *Lemma 0.5 (6)* holds on (0, r_h) (BEYOND5.md, D366). Its conditions (1)-(5) involve the inner radius only through
  (1), past timelike, which holds for every r > 0 (C2).
- *Propositions 5.1-5.3, 6.1, 7.1, Theorem 7.3.* Every radius in them is placed relative to r_♯ and r̂:
  - ε_X ≤ T_0 r_♯/2 and ε_r := (r̂ − r_♯)/10 (:514);
  - r_1 := r_♯ + (2/10)(r̂ − r_♯) (:648), r_2 := r_♯ + (2.75/10)(r̂ − r_♯) (:670);
  - χ_(r,j)'s transitions in [r_♯, r̂] (:226-232), and t_1 < ¼T_0 r_♯ (:721).
  The facts they use near Σ^♯ are Lemma 0.3 (c), Lemma 0.4 and Lemma 0.5 (6), all re-proved above.
- (IV′′′′′5)-(IV′′′′′6): the extension to Ω̃ with ¾r_♯ uses Lemma 0.3 on {r ≥ ½r_♯} (re-proved) and keeps Proposition
  5.1 in {r ≥ r_♯}, which (6) now covers anyway.

*Status:* Part IV re-proved at r_♭.

## 7. Part V

**V (V-GLUING).** One line names the inner radius: Definition 2.1 takes g^KS_(μ,A) on ℝ_t × {|x| ≥ r_0} (:141-142).
Everything after it uses the data of G_p on {y^0 = 0} ∩ {|y| > R_P}, R_P = 100R_1 (:149-150), where the point
Φ_p(0, y) has |x| ≥ ½|y| ≥ 50R_1 (Lemma 2.2's proof, :162-164).

- There III.B Lemma 3.3 (c) holds for every ‖A‖ < R_1, so for Part V's |A| < ε_P: |x|² ≥ 2500R_1² > 2‖A‖² ≥ s, and
  r_A² ≥ |x|² − ‖A‖² > 3‖A‖². So the region Part V uses does not depend on the inner radius. Definition 2.1's domain
  clause may be read on {|x| ≥ 50R_1}, which is all Part V uses; III.B's X̄ (:158-160) enters near infinity only
  (verifier 173's n4). Part VII uses Part V at A = 0.
- Lemma 1.4 (scaling), Proposition 2.3 (the charge map), Corollary 2.4 and Theorem 3.1 (the gluing on Γ(R, 4R)) work
  at |x| ≥ R ≥ R_P and are unchanged.

*Status:* Part V re-proved at r_♭; nothing in it reaches the inner region.

## 8. Part VI

Part VI's checks, re-derived at section 0's radii r_0^A := r_♭, δ_0 := min(R_1/16, r_♭/4), r_2 = 7R_1/8 and
r_e = 17R_1/16, so ½r_♭ ≤ r_♭ − 2δ_0 < r_♭ − δ_0 < r_♭ < r_2 < r_h < r_e. At r_♭ = ½R_1 they are D373's, read by
verifier 172; the parameter set is ℬ_♭.

- **VI.A Lemma 1.1** on ℝ × {|x| ≥ r_♭ − 2δ_0}: g^KS_b is defined, smooth and Lorentzian there for b ∈ ℬ_♭ (F1).
  (3.3) and (3.6) define g_b and t_*, with ψ taken from r_♭ (section 3) and ψ′ = 1, T_μ constant on {|x| ≤ 2R_1}; so
  β = 1 there and Lemma 3.3 (e) makes dt_* timelike. The forms of III.B Definition 6.1 are smooth and stationary for
  r > 0, and c_C past timelike (section 3), so every operator of III.D-III.F and IV⁗ is defined on X̃°. t_* ≤ t is not
  claimed below r_♭; III.K uses it on [r_♭, 5R_1] only. The decay at infinity and (K1) do not involve the inner
  radius.
- **(0.1)** holds on {r > 0} at b_0, Φ_μ being a time translation on {|x| ≤ 2R_1}.
- **VI.A Proposition 2.1, (H3)-(H4) at b_0.** f < 0 on (0, r_h). So on {r_0^A − 2δ_0 ≤ r ≤ r_2}, G_0 = fξ² + r^(−2)C is
  Lorentzian of signature (1, 3), G_0(dr) = f < 0, and 𝖧r = 2f < 0 on ∂Σ_0. Forward, |ṙ| = 2|f| grows as r decreases,
  so every curve reaches {r < r_0^A − δ_0} at a finite parameter. The horizon data (β_0, β, q) are at r = r_h and do
  not change.
- **VI.A sections 3-4** (the trapped set at r_ph = √2 R_1 > r_2, (Γ.1)-(Γ.3), (K3)) do not reach below r_2.
- **VI.A section 5, (H8) at b_0.** Inside the horizon the record uses dr timelike and, on compact subsets of
  Σ_(z_0) ∩ {r_0^A − δ_0 ≤ r ≤ r_h − ε}, ṙ bounded above by a negative constant. Both hold, as f < 0 there and the
  sets are compact (F4). The cover argument for uniformity (VI-DYN:259-272) is unchanged.
- **VI.B Lemma 1.2.** Ψ_b is defined on {|x| ≥ r_♭ − 2δ_0}. χ is supported in (⅝R_1, 7/4 R_1), so λ ↦ r̃_b(λx̂)
  equals λ for λ ≤ ⅝R_1 and is a bijection of [r_♭ − 2δ_0, ∞). Ψ_b is the identity on {|x| ≤ ⅝R_1}, which contains
  the whole collar and the artificial boundary.
- **VI.B Proposition 2.2, (H3)-(H5) near b_0.** sup over [r_♭ − 2δ_0, r_h] of (−fr²) is μ_0 − (r_♭ − 2δ_0)², finite,
  so |ξ| ≥ c|ζ| on ∂Σ_0, and by compactness of S^*{r_♭ − 2δ_0 ≤ r ≤ r_h + ½δ_0} this persists for b near b_0. The
  three strict conditions on {r_0^A − 2δ_0 ≤ r ≤ r_2} hold at b_0 on that compact set and persist. Outside U the
  forward time to {r < r_0^A − δ_0} is at most 2(r_h − r_♭ + 2δ_0)/c′. When r_♭ < R_1/4, δ_0 < R_1/16 and the band
  {r < r_h + ½δ_0} is thinner: ∂Σ̃_(0,b) lies in it for b in a smaller neighbourhood, and I.B Proposition 5.2's band
  is local (section 0).
- **VI.B′.** Lemma 0.1's separation holds on {|x|² > s}, which contains {|x| ≥ ½r_♭} for b ∈ ℬ_♭ by F1's bound
  2‖A‖² ≥ s. In Proposition 4.1, Ψ_b is the identity on {|x| ≤ ⅝R_1} ⊃ {r < r_0^A − δ_0}. Inside the horizon of g̃_b,
  dr is timelike on {r_0^A − 2δ_0 ≤ r < r_h} by VI.B Lemma 1.1 and Proposition 2.2 at the new radii (the record cites
  both, VI3-TRAPPING:436-437; verifier 173's n2), and the rescaled ṙ is
  bounded above by a negative constant on compact subsets of {r_0^A − δ_0 ≤ r ≤ r_1}, r_1 < r_h. The exterior part
  and the trapped set are at r > r_h. Theorem 5.1 follows as in the record.
- **VI.C (VI4-PARAMS)** names no inner radius. Its neighbourhood U of b_0 and the constants downstream are chosen
  again, as section 0 says.

*Status:* Part VI re-proved at r_♭.

## 9. Part VII

Read in full at sections 0-2 and at every radius of sections 3-4 (pattern list at the footnote of section 2, with
Ω′, a′, q_0 added).

- **Setting (:39-43).** III.B's μ_0 is μ_end and its r_0 is r_♭ (BEYOND5.md Proposition 6.2 takes r_♭ :=
  ½ min(R_1, r_q(μ_end))). By section 0, Part I's artificial boundary is at r_♭ as well, so III.K's M_♭ and the spaces
  of Parts I-II start at the same radius.
- **Theorem 0.2 (i), (0.2).** The rate on {r_♭ ≤ r ≤ R′, t_* ≥ T′} comes from III.K Theorem 4.3 (4) at r_♭ (section 5)
  where χ_K = 1. The b-Sobolev step (:415-425) is at K⁺ and does not involve the inner radius.
- **Lemma 1.1 (after the shell).** The record's Theorems A, D and E hold on every domain Ω′ of the form (1.1),
  for every δ′_0 ∈ (0, q_0) (N1STAR-PROOF.md:145-150). {r = a′} stays spacelike (record Lemma 1.1 (b): a′ < q_0 ≤
  √μ_seed, the record's μ0). C_J and λ_1 depend on Ω′ = Ω′(T′, δ′_0) (N1STAR-PROOF.md:177), so on r_♭ through δ′_0,
  c_0 and T′, all fixed once r_♭ is (verifier 173's m2).
- **Lemma 1.2 (placing Σ_IVP).** It needs a′ = q_0 − δ′_0 < ½r_♭. Take δ′_0 ∈ (max(0, q_0 − ½r_♭), q_0), a nonempty
  interval as r_♭ > 0.
  - (a): for v ≥ v_end, g_0 = g^KS_(μ_end,0) in (τ, x), a formula valid for every r > 0. g_(b_0) is its pull-back by
    Φ(t, x) = (t − T_μ(|x|), x), a time translation on {|x| ≤ 2R_1}. So (a) holds on Ω′ ∩ {v ≥ v_end, |x| ≥ r_♭}.
  - (b): θ = ψ_IVP − T_μ is continuous on [r_♭, 4R], with ψ_IVP from r_♭ (section 3). Put c_0 := min_[r_♭,4R] θ −
    max(τ_0 + 1, v_end + 2 − r_♭). The rest of the proof (:151-158) uses r only through r ≥ r_♭ > a′.
- **Section 2 (gluing in the class).** Proposition 2.2 takes data on Σ_IVP ∩ {r_♭ ≤ r ≤ 3R} and changes them only on
  {R ≤ r ≤ 4R}, by Part V (section 7). Corollary 2.3 bounds g_λ's data on Σ_IVP ∩ {r_♭ ≤ r ≤ 4R}, a compact subset of
  Ω′_+ by Lemma 1.2 (b), using Lemma 1.1 there.
- **Section 3 (naturality).** The cut-offs are defined from (t, t_*, t_IVP, t^♭_*, |x|), O(4)-invariant at every
  radius. The forms of (C2) have coefficients that are functions of r, smooth for r > 0 (section 3).
- **Section 4 (the proof).** The choices run in the record's order: k, then R, then c_0 and Ω′ by Lemma 1.2 (with
  δ′_0 from r_♭), then J, then λ_1. They depend on r_♭ through δ′_0, c_0 and T′ (Lemma 1.2) and III.K's constants.
  r_♭ depends on μ_end alone, and every later choice comes after it, so Proposition 6.2 is not circular.
- **Remark 4.1 and (VII4)** are BEYOND5.md Lemma 6.3, with Σ = Σ_IVP ∩ {r_♭ < r < R}.

*Status:* Part VII re-proved at r_♭, given section 8.

## 10. Part VIII

Part VIII linearises III.K at b_0 (U = 0); its M, N = {t_IVP ≥ −ν(|x|)}, Ω_* and 𝒟 are III.K's (section 0 there).

- At r_♭ these are section 5's sets. The inputs are Part IV″ Theorem 2.4, IV‴ Theorem 2.1 and III.C′ Theorem 3.1's
  proof at h = 0, which are exterior (section 6, and III.C′ in section 4), and III.K Lemma 2.3 at U = 0 (section 5).
- Step 4 (:280-286) runs II.F Lemma 1.3 on Ω_*° with τ := t^♭_*. Its compactness hypothesis needs dt^♭_* past
  timelike, which II.C Lemma 3.2 (2) gives at h = 0 at the repaired radii (section 2). Near {r = r_♭} it also needs
  past causal curves to stay in {r ≥ min(r(p), r^♮)}: that is II.C Lemma 3.2 (1) at h = 0, as in II.F Lemma 1.4 (a),
  and at b_0 also F2. The record named only the first input, and cited II.F section 7.4, the ι⁺ model, which does not
  meet the inner boundary. Part VIII and III.K Proposition 4.2 (III.K:459-463) now name the second (D378, verifier
  173's m1).
- (2.3) holds on {r_♭ ≤ r ≤ R′}, as Part VII's (0.2) does.
- Corollary 2.3's G-equivariance (VIII:314-337): G fixes t, t_*, t_IVP, t^♭_* and |x| at every radius.

*Status:* Part VIII re-proved at r_♭.

## 11. Part IX

- **Setting (:20-38).** g := g_(b_0) on M_♭ = {|x| ≥ r_♭}, with interior {|x| > r_♭}. dt_IVP is timelike there by
  III.B Lemma 3.7 (b) at r_♭ (section 3, β ∈ (−1, 1] on [r_♭, ∞)), and past timelike, in the cone of dt_*.
- **Lemma 1.2's compact set (:108-127).**
  - t_IVP decreases to the past, and 0 ≤ ψ_IVP ≤ C_3, since ψ_IVP(r_♭) = 0 and ψ_IVP ≥ 0 (section 3).
  - dr is future timelike on {r_♭ ≤ r ≤ r^♮}, r^♮ = ½(r_0^A + r_2) = ½(r_♭ + 7R_1/8) < r_h, by II.C Lemma 3.2 (1) at
    h = 0 with section 0's radii, and at b_0 directly by F2.
  - The record cites the same lemma from III.B's ½R_1, while it covered {r ≥ ⅝R_1} only. This is a third site of
    section 0's mismatch, besides III.K and Part VII, repaired with it. At h = 0 the claim held anyway, by F2.
  - The far region {|x| ≥ 3R_1} is unchanged. So L_p is compact in N° with |x| ≥ min(|x(p)|, r^♮) > r_♭.
- **Section 2 (the gauge comparison)** is pointwise identities and [BGP]'s Cauchy problem on the globally hyperbolic
  N^𝒟. No radius enters.
- Theorem 0.2 does not use Part IX.

*Status:* Part IX re-proved at r_♭.

Footnote (reading pattern for section 2): lines of PART-I-*.md and PART-II-*.md matching
`r_0(?![0-9])|r_\{0\}|\delta_0|r_2(?![0-9])|\partial_\sharp|artificial|inner`, then filtered for R_1, r_h, μ,
Tangherlini, Myers and numerical relations among the radii.
