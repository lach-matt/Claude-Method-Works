# BEYOND5 -- the solution beyond D_T and Ω: the black-hole interior after the shell, up to the curvature boundary

Status: written (D360); read by verifier 167 (D362), findings seated; r_0 census and Proposition 6.2 added (D363);
read by verifier 168, whose major finding (Lemma 0.5 (6) below r_h/2) and minor findings are seated (D366). The
record's radius mismatch found by verifiers 170-171 is stated in section 1. Propositions 6.1-6.2 assume its repair
(D372), which is now made in proof5 Part VI (D373).
Labels as marked; nothing here is computed beyond the census.

The paper's open item "beyond the boundary" (RESPONSE-HL-5D.md section 9) reads: Theorems 1-3 are made on D_T and Ω,
and beyond them only Theorem 4 is stated, outside the black hole. Two regions lie beyond.

- **Inside x_K = 1** (r < r_q): curvature above the scale l5, where the paper's premise is that the classical
  description stops. Nothing is attempted there.
- **The interior after the time T** (r_q ≤ r < √μ_end, v > v_end + T): below the event horizon, above the curvature
  boundary, for all later times. This note is about that region.

## 1. What Theorem 4's development already covers

Part VII (proof5/PART-VII-ASSEMBLY.md) builds Theorem 4 (i) on III.B's domain M = {|x| ≥ r_0, t ≥ −|x|/2}, with
r_0 := ½R_1 = ½√μ_end (PART-III-B-FAMILY.md:49-55, with III.B's μ_0 set to μ_end at PART-VII-ASSEMBLY.md:39-41).
The surface r = r_0 lies inside the horizon and is spacelike; the level sets of t_* are spacelike for all r > 0 there
(in Kerr-Schild form g^(−1)(dt − dr, dt − dr) = −4μ/r²). The
metric g of Theorem 0.2 (i) is defined on Ω_* ∪ 𝒟_0, the future of Σ_IVP within M (PART-III-K-NONLINEAR.md:21-30,
96-110), which is M ∩ {t_IVP ≥ 0}. It satisfies Ric(g) = 0, and on {r_0 ≤ r ≤ R', t_* ≥ T'} it decays at the rates
(0.2) to g_(m',0), Tangherlini of a mass m' with |m' − μ_end| < ε_m.

**The radius the development reaches (D372, D373).** This holds on all of M only if Part I's artificial boundary,
where Part II's spaces and III.D-III.J‴'s estimates end, is at III.B's r_0. Until D373 it was not. Part VI put it at
r_0^A = ½R_1 + 2δ_0 = ⅝R_1 (VI-DYN 88-89 as it stood), while III.K and Part VII use ½R_1 (BEYOND5-R0-PROOF.md
section 0; verifiers 170-171). So the record's g was controlled on {r ≥ ⅝R_1}. The repair puts Part I's artificial
boundary at r_0 itself, with the inward collar δ_0 = R_1/16, where the Kerr-Schild family is still defined (down to
¼R_1, IV6-SOLV:28-30). It is now made in Part VI (D373: VI-DYN section 2, Lemma 1.1 and finding (VI.A7); VI2 and VI3
read on {|x| ≥ ⅜R_1}). Re-proving the Parts at that choice is BEYOND5-R0-PROOF.md, with r_♭ = r_0 = ½R_1 as one
case. Without the repair, Proposition 6.1's condition would read r_q ≥ ⅝R_1, which is
μ_end ≤ (8/5)⁴ √72 l5² ≈ 55.61 l5².

**Proposition 6.1 (deduced; with the repair of D372, made in Part VI at D373).** Let r_q := (√72 μ_end l5²)^(1/4)
be the curvature boundary after the shell, a radius in the background's coordinates. If

    μ_end ≤ 16√72 l5² ≈ 135.76 l5²,                                                                             (1.1)

then r_q ≥ r_0. So the development g of Theorem 0.2 (i) is defined on the whole coordinate region {r ≥ r_q} to the
future of Σ_IVP: the interior up to the background's x_K = 1, for all later times. g's own x_K = 1 surface lies within
O(λ + ε_m) of r = r_q. So with strict inequality in (1.1), and λ_1 and ε_m small, it also lies in {r > r_0}. g is
G-invariant and vacuum, its data are within C λ of Tangherlini's in III.K's norm, and it settles there at the rate of
Theorem 4.

*Proof.* r_q ≥ ½√μ_end ⇔ √72 μ_end l5² ≥ μ_end²/16 ⇔ (1.1). The rest is Theorem 0.2 (i) on {r ≥ r_0} ⊃ {r ≥ r_q}. ∎

For the paper's two seeds (μ0 = 100 l5² and 1000 l5², log D38), (1.1) holds for the first whenever the wave adds at
most 35.76 l5² of mass, and fails for the second. Theorem 0.2 is a small-λ statement, so the gain to use is its λ → 0
limit (2.6), (2/9) A² ∫ env². For the record's envelope sin⁴(π(v − ½)/3) on [½, 7/2], ∫ env² = 3 · 35/128 ≈ 0.820.
With A = 1 in seed units, which is still to be confirmed, the gain is ≈ 0.182 μ0. Then μ_end ≈ 118 l5² at the first
seed, and (1.1) holds with a margin of about 18 l5² (verifier 167's B2). Without D372's repair the first seed
would fail the condition μ_end ≤ 55.61 l5², and only Proposition 6.2 would cover it.

## 2. Whose continuation it is

g is the development of the glued data (γ_λ, k_λ). These equal g_λ's data on Σ_IVP ∩ {r ≤ R} and exact Tangherlini
data beyond 4R. Two facts follow.

- *On the domain of dependence of Σ_IVP ∩ {r < R}* g and g_λ agree up to a diffeomorphism. They are vacuum
  developments of the same data, so this is geometric uniqueness on a domain of dependence. Part VII's Remark 4.1
  records this as finding (VII4), "not written"; it is written as Lemma 6.3 (section 3 (a), D367). The two give one
  vacuum spacetime N: g_λ on the past domain of dependence of Σ := Σ_IVP ∩ {r_0 < r < R} near Σ, and g to the future of
  Σ_IVP in {r ≥ r_0}. On the future side they are identified on their maximal common development. Elsewhere in Ω' they
  need not agree, because on R < r < 4R the glued data differ from g_λ's. This still covers the hole's interior after
  the time T.
- *At late times near the hole* that domain of dependence does not reach (finding (VII1): "K^+ at late times is not
  in the domain of dependence of any bounded part of the slice"). So the interior covered by Proposition 6.1 belongs to
  *a* vacuum continuation of g_λ, fixed by the gluing. It is not *the* continuation of the record's data, because
  the record's g_λ is constructed on the compact Ω' only.

## 3. What remains

- **(a) Write (VII4).** The change of gauge on a compact region identifying the two developments on their common
  domain of dependence. This is standard and only needs writing out. Written below as Lemma 6.3 (D367).

**Lemma 6.3 ((VII4), deduced, D367).** Let Σ := Σ_IVP ∩ {r_0 < r < R}, with the data (γ, k) that g_λ and g both
induce on it (Part VII: the glued data equal g_λ's on Σ_IVP ∩ {r ≤ R}). In Part VII's chart (Lemma 1.2) Σ is one set
for both metrics. Let V ⊂ Ω′_+ ∩ {v > v_end} be an open neighbourhood of Σ̄ on which t_IVP, extended below r_0 with
ψ′_IVP = 1, is a time function for g_λ (see the proof). Let A := int D⁻_V(Σ) ∪ Σ, the past domain of dependence of Σ in
V with g_λ, and B := M ∩ {t_IVP ≥ 0} with g.

- (i) The space N := A ⊔ B / ~, gluing along Σ by the identity, is a smooth, Hausdorff, time-oriented vacuum spacetime:
  g_λ on A and g on B.
- (ii) In N and in V, int D(Σ) are globally hyperbolic developments of (Σ, γ, k). Their maximal common globally
  hyperbolic development U contains a neighbourhood of Σ. On U, g and g_λ agree up to a time-orientation-preserving
  isometry that is the identity on Σ, and the two glue along U into one development, Hausdorff.

*Proof.*

- *(i), smoothness.* Take K ⊂ Σ compact and the Gaussian normal maps E_λ(s, x) := exp^(g_λ)_x(s n_λ) for s ≤ 0 and
  E(s, x) := exp^g_x(s n) for s ≥ 0, n_λ and n the future unit normals; for some ε(K) > 0 both are diffeomorphisms on
  [−ε, 0] × K and [0, ε] × K. There E_λ^* g_λ = −ds² + h^λ_s and E^* g = −ds² + h_s, with h^λ_0 = h_0 = γ and
  ∂_s h^λ_0 = ∂_s h_0 = ±2k (one convention for both).
  - In this gauge Ric = 0 is ∂_s² h = F(h, ∂_s h, ∂_x h, ∂_x² h), a universal expression. Differentiating m times in s
    makes ∂_s^(m+2) h at s = 0 a universal expression in the ∂_s^j h, j ≤ m + 1, and their x-derivatives.
  - By induction every ∂_s^m h^λ and ∂_s^m h agree at s = 0. So H := h^λ on s ≤ 0 and h on s ≥ 0 has continuous
    one-sided partial derivatives of every order that agree at s = 0, and is C^∞.
  - −ds² + H is then a smooth metric, Ricci-flat on each side and so on both. These charts, over a cover of Σ by such
    K, give N its smooth structure near Σ; away from Σ it is A's and B's.
- *(i), Hausdorff.* A contains no point of the edge ∂Σ = Σ_IVP ∩ ({r = r_0} ∪ {r = R}), since the edge is not in
  int D(Σ). So a point of B on Σ_IVP ∖ Σ and any point of A have disjoint neighbourhoods. Two half-spaces glued along
  half their common boundary, edge included, would fail exactly there; with A as defined they do not.
- *V exists.* Σ̄ lies in the interior of Ω′_+ (Part VII Lemma 1.2 (b)), where v ≥ v_end + 2. dt_IVP is timelike for
  g_(b_0) on {|x| ≥ ½r_0} with ψ_IVP extended by ψ′_IVP = 1 below r_0 (III.B Lemma 3.7 (b) and Lemma 3.3 (e): β = 1).
  g_λ = g_(b_0) + O(λ) in C⁰ on Ω′_+ ∩ {v ≥ v_end} (Part VII Lemmas 1.1, 1.2 (a)). So for λ small, dt_IVP is
  timelike for g_λ on a neighbourhood V of the compact Σ̄.
- *(ii).* Σ is a level set of a time function, t_IVP in V and in B and hence in N, so it is acausal there. Then int D(Σ)
  is globally hyperbolic with Cauchy surface Σ (standard causality theory; not read at source here). Both are vacuum,
  so both are globally hyperbolic developments of (Σ, γ, k) in the sense of [Sbi15] Definition 2.1.
  - [Sbi15] Theorem 2.6 gives a common development near Σ (Choquet-Bruhat's local uniqueness).
  - Theorem 3.4 gives the maximal one, U ⊂ int_N D(Σ) with an isometric embedding ψ into Ω′. As a common development
    of two developments of the same data, ψ preserves the time orientation and the embedding of Σ (Definitions
    2.2, 2.4).
  - Theorem 3.13 (no corresponding boundary points) makes the gluing along U Hausdorff, and Theorem 2.7 is the
    resulting common extension. ∎

What it does and does not say:

- N is the one vacuum spacetime of section 2: the record's g_λ just before Σ, near the hole, and the development g
  after Σ_IVP, everywhere in {r ≥ r_0}. Across Σ_IVP ∩ {r ≥ R} nothing is glued, since the data differ there.
- The identification of g with g_λ to the future of Σ holds on U, the largest region on which the two developments are
  isometric. How far U reaches into int D⁺(Σ) of each is not decided here. It is as far as both are determined by
  (Σ, γ, k) alone, with no corresponding boundary points.
- The g_λ side is taken in V, not in all of Ω′, because Σ is acausal in V by construction. Whether it is acausal in Ω′,
  which would enlarge the development on that side, is not decided here.
- [Sbi15] works with smooth vacuum data on a connected Riemannian manifold satisfying the constraints (Definition 2.1),
  not necessarily complete. Σ is one: in the chart (t, x) it is the graph over the shell {r_0 < |x| < R} ⊂ ℝ⁴, which is
  connected, and its data satisfy the constraints because both metrics are vacuum.

READ ([Sbi15] = J. Sbierski, "On the existence of a maximal Cauchy development for the Einstein equations - a
dezornification", arXiv:1309.7591v3, read 2026-10-31 through alphaXiv): Definitions 2.1-2.4 and Theorems 2.6-2.8
(pp. 11-12), Theorem 3.4 (p. 14), Theorem 3.13 (p. 20).
- **(b) The continuation of the record's own data.**
  - The record would first have to construct g_λ on the whole of Σ_IVP, to spatial infinity. The region there lies
    after the shell (v > v_end), where g_λ is Tangherlini plus smooth means times powers of λ (paper section 8.7) plus
    the remainder of Part VII Lemma 1.1.
  - Those data would then have to be shown to lie in III.K's class: polyhomogeneous at spatial infinity with terms of
    orders r^(−2) and r^(−3) (Lemma 0.1).
  - Then the class run behind (i), Part VII Proposition 3.2 with S = 0 and b = (m', 0) and now on g_λ's own data,
    gives the development of those data, with the interior of section 1 at late times. Without the symmetry, (ii) would.
  - The first step needs the record's estimates on a domain reaching spatial infinity at the time of Σ_IVP. The
    supplement's construction from past null infinity (the region before Σ_τ0) is the natural start.
- **(c) Masses above (1.1).** Proposition 6.1 needs r_0 ≤ r_q.
  - III.B fixes r_0 = ½R_1 as a choice. Every Tangherlini metric g^KS_μ is regular on r > 0 with spacelike t_* slices,
    and a Myers-Perry metric of small spin has its inner horizon near r = 0. So any fixed r_0 ∈ (0, R_1) above the
    inner horizons of the parameter family should serve.
  - With r_0 < r_q, Proposition 6.1 then holds for every μ_end.
  - Proving this means a census of r_0's uses in proof5 (III.B-III.K and Parts IV-VII), among them Part VII Lemma 1.2
    (a' < r_0/2) and III.K Proposition 1.2 (R_ν = (r_0 + R)/2). Each use must be through constants, or through
    "r = r_0 is spacelike, inside every horizon of the family, outside every inner horizon".
  - **The census (D363; `checks/r0census5.py`, `BEYOND5-R0.tsv`).** 322 lines of Parts III-VII in 25 files name
    r_0, the inner radius or boundary, ½R_1, r_♯, ⅝R_1, ¾R_1 or, since D373, ⅜R_1 (308 lines before Part VI's
    amendment). Each is classed at its line, by reading, not by proof:
    - 108 are another r_0 (OTHER): III.C′'s exterior radius "r_0 large" (C2-POLYHOM, C3-BOOSTDATA, IV-EB,
      IV3-NM, IV4-SLAB; III.K says so at 134-135), the source's r_0 = r_c (IV5-CDMODES, IV6-SOLV), and r_A at A = 0
      (III.B 102, 117);
    - 19 are the definition and the domain (DEF): III.B 49-79, 177-178 and 224-251 ((2.1), (3.6), Lemma 3.7);
      III.K 43-44; Part VII 40, 195, 258;
    - 120 use only that {r = r_0} is spacelike with dr future timelike, inside the horizon (SPC): the artificial
      boundary, vanishing inside the horizon (III.E), the radial ODEs on (r_0 − δ_0, ∞) (D-GAUGEPOT, F3-MODES,
      F4-ZERO). IV6-SOLV's finding (IV′′′′′5) says its cut-offs and energy estimates near Σ^♯ need only "the future
      timelike character of dr on [r_♯, r̂]";
    - 61 go through a constant chosen from it (CON; 48 before D373, the thirteen added being Part VI's amended lines):
      δ_0 of I.A's radii and the collar below r_0 (VI-DYN to VI3-TRAPPING),
      ν_0 = min(¼, r_0/8) and R_ν (III.K), δ_1 and the weights (H2-ADMISS), δ′_0 (Part VII Lemma 1.2);
    - 14 rest on a value (VAL), 13 of them on ½R_1, and VI-DYN 81 (since D375) on the collar's ⅜R_1 ≥ ¼R_1.
      III.B 157-159: ‖A‖ < ε_param R_1 with |x|² ≥ ¼R_1² > 2‖A‖². III.B 244: ψ(2R_1) = 2R_1 − r_0 ≥ 3/2 R_1.
      VI3-TRAPPING 375: r_0 − δ_0 = 7/16 R_1 < ⅝R_1 (D373). And 8 lines of IV6-SOLV
      (192, 428, 532-533, 679-680, 882, 884) use Lemma 0.5 (6), record 10.14 (ii), which was checked on [r_h/2, ∞)
      only (`cform5.py` C3; (IV′′′′′6): "not known ... below r_♯"; verifier 168's A1).
    - Read by verifier 168 and harmless, though no pattern matches them: Σ^♯ (15 lines of IV6-SOLV), Σ^int (III.B 57,
      358, 361, 374; III.C 112; III.I8 61) and 7/16 R_1 (VI3-TRAPPING 376; 9/16 R_1 before D373). Part IX, the gauge
      comparison, is outside the census; Theorem 0.2 does not use it.

**Proposition 6.2 (deduced from the census, D363; repaired D366, D372).** Let r_♭ ∈ (0, ½R_1] and replace III.B's
r_0 by r_♭ and its ε_param by min(1/20, r_♭/(4R_1)). Put Part I's artificial boundary there too, r_0^A := r_♭, with
the collar δ_0 := min(R_1/16, r_♭/4) (BEYOND5-R0-PROOF.md section 0). Then each of the 214 matched lines that use the
inner radius (DEF, SPC, CON, VAL) holds with r_♭, the constants then depending on r_♭. The Part-by-Part re-proof is
BEYOND5-R0-PROOF.md. So with r_♭ := ½ min(R_1, r_q(μ_end)), Proposition
6.1's conclusion holds for every μ_end, without (1.1).

*Proof (from the census).*

- **The five VAL sites hold at r_♭.**
  - III.B 157-159: ‖A‖ < r_♭/4. For |x| ≥ ½r_♭ (IV6-SOLV extends to {r ≥ ½r_♯}), |x|² ≥ ¼r_♭² > r_♭²/8 > 2‖A‖² ≥ s
    and r_A² ≥ |x|² − ‖A‖² > 3r_♭²/16 > 3‖A‖², so ‖A‖²(r_A² + ‖A‖²) < (4/9) r_A⁴ < r_A⁴: Lemma 3.3 (c)'s condition.
  - III.B 243-244: ψ(2R_1) = 2R_1 − r_♭ ≥ 3/2 R_1 and ψ′ ≥ −1 on [2R_1, 3R_1], so ψ ≥ ½R_1 > 0 there as before.
  - VI-DYN 81 (Lemma 1.1's collar): ⅜R_1 ≥ ¼R_1, where Lemma 3.3 (c) holds on III.B's ℬ. At r_♭ the collar ends at
    r_♭ − 2δ_0 ≥ ½r_♭, where F1 gives (c) on ℬ_♭.
  - VI3-TRAPPING 375: r_0 − δ_0 < ⅝R_1 for Part I's radii. With D372's choice r_0^A = r_♭ and δ_0 ≤ R_1/16
    (BEYOND5-R0-PROOF.md section 0), r_0^A − δ_0 < r_♭ ≤ ½R_1 < ⅝R_1.
  - IV6-SOLV's Lemma 0.5 (6) below r_h/2 (exact, by hand; D366). On r ≤ r_0/2 the record's c is the inner piece
    dt + (v/2) dr up to a positive factor (`cform5.py`:17), v = ½. In Kerr-Schild Tangherlini, g^(−1)(dr, dr) = f,
    g^(−1)(dt, dr) = 1 − f and g^(−1)(dt, dt) = −(2 − f), with f = 1 − μ/r². So ⟨c, dr⟩ = 1 − ¾f = ¼ + ¾μ/r² > 0 and
    G(c) = −3/2 + (9/16) f < 0 for every r > 0 (C2's formula). On (0, r_h), f < 0, so Lemma 3.8's form
    f e G(c) + 2(1 − e)⟨c, dr⟩² is positive, and −ℓ(−dr) is positive definite there, as (6) asks. It is strict on the
    compact {r_♭ ≤ r ≤ r_h/2}, so it persists for b near b_0, with uniform lower bounds, on shrinking U as Lemma 0.5's
    proof does. Proposition 5.1 and 5.3 (1) then run on {r ≥ r_♭}, the extension below r_♭ as in (IV′′′′′6).
- **SPC.** For Tangherlini, g^(−1)(dr, dr) = 1 − μ/r² < 0 on 0 < r < r_h, and the radial systems' coefficients are
  smooth on (0, ∞), r_h aside (III.D 417; F3-MODES 204-212). Where F3-MODES 196-212 and F4-ZERO 361 work on
  {r > r_0 − δ_0}, δ_0 is not fixed there, and any δ_0 ∈ (0, r_♭) serves (verifier 168's A2). For b near b_0 this
  persists on the compact
  {½r_♭ ≤ r ≤ ¾R_1} on shrinking the neighbourhood. So dr is future timelike there, as IV6-SOLV Lemma 0.3 (c) needs.
- **CON.** Each constant is then chosen from r_♭. For Part VII Lemma 1.2, take δ′_0 ∈ (max(0, q_0 − ½r_♭), q_0),
  which the lemma allows (δ′_0 ∈ (0, q_0), q_0 = r_q(μ0), N1STAR-PROOF.md:145-149).
- **DEF.** The definitions and domains read with r_♭ for r_0, as the three VAL sites allow.
- So Theorem 0.2 (i) holds on {r ≥ r_♭} ⊃ {r ≥ r_q}, with λ_1, ε_m and ε depending on r_♭, so on μ_end. ∎

What this rests on: the census is a reading at 322 lines, not a re-proof of each Part. The re-proof, Part by Part, is
BEYOND5-R0-PROOF.md (D368-), in batches, each read by its own verifier. A use that names the inner
radius by none of the eight strings would be missed; verifier 168 searched for the names above and found them harmless.
[Hin26a] Proposition 5.1's conditions at m are IV6-SOLV Lemma 0.5's (1)-(6); of these only (1) and (6) involve m, and
both hold on (0, r_h) (C2 and the sign argument above). The source itself is not read at m here. Part VII's record
domain Ω′ reaches r ≥ a′ = q_0 − δ′_0, below the record's q_0; with r_♭ it must reach further, through δ′_0 alone.
The region r_♭ ≤ r < r_q, covered too, lies beyond the curvature boundary, where the paper's premise has the classical
description stop.

- **(d) The slab, if (c) fails somewhere.** The region r_q ≤ r ≤ r_0 after Σ_IVP is a slab of finite r-time: inside
  the hole r is a time function, and every point's causal past meets {r = r_0} in a set of bounded t-extent. Points
  whose causal past meets r = r_0 before Σ_IVP also need g_λ and (a). Alternatively, restrict the slab to
  D⁺({r = r_0} ∩ {t_IVP ≥ 0}).
  - Data on {r = r_0} are small and decay in t_* (Theorem 0.2 (i), (0.2)).
  - The background is t-translation invariant on the slab.
  - Cauchy stability with constants uniform in t then extends g across the slab for λ small. Writing this out is the
    alternative to (c).

## 4. Sources

proof5/PART-VII-ASSEMBLY.md: Theorem 0.2, (0.2), Remark 4.1, findings (VII1), (VII4). The census: checks/r0census5.py
(--selftest, --show) and BEYOND5-R0.tsv. proof5/PART-III-B-FAMILY.md:49-55
(r_0, M). proof5/PART-III-K-NONLINEAR.md:21-30, 96-110 (Ω_*, 𝒟, N). RESPONSE-HL-5D.md sections 2.3, 8.7, 8.8, 9.
