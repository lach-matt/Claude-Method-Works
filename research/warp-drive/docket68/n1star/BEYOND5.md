# BEYOND5 -- the solution beyond D_T and Ω: the black-hole interior after the shell, up to the curvature boundary

Status: written (D360); read by verifier 167 (D362), findings seated; r_0 census and Proposition 6.2 added (D363);
read by verifier 168, whose major finding (Lemma 0.5 (6) below r_h/2) and minor findings are seated (D366). The
record's radius mismatch found by verifiers 170-171 is stated in section 1. Propositions 6.1-6.2 assume its repair
(D372), which is now made in proof5 Part VI (D373). Proposition 6.2 is re-proved Part by Part in BEYOND5-R0-PROOF.md
(D368-D378, batches 1-4 read by verifiers 169-173).
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
  is globally hyperbolic with Cauchy surface Σ (D388). Both are vacuum, so both are globally hyperbolic developments of
  (Σ, γ, k) in the sense of [Sbi15] Definition 2.1.
  - *Global hyperbolicity.* [Chr11] Theorem 2.9.9: for an achronal hypersurface S without boundary in a C² spacetime,
    with D̊_I(S) non-empty, D̊_I(S) with the induced metric is globally hyperbolic. Σ is a smooth spacelike graph over
    the open shell, so it has no boundary; it need not be closed, which [Min19] Theorem 3.45 would require.
  - *Σ ⊂ D̊_I(Σ).* [Chr11] states this after Corollary 2.9.8, for achronal C¹ spacelike hypersurfaces without boundary
    ("transversality considerations"), without proof.
  - *Σ is a Cauchy surface of D̊ := D̊_I(Σ).* Let γ be an inextendible timelike curve in D̊. By achronality it meets Σ at
    most once. Suppose it misses Σ.
    - D̊ ∖ Σ lies in I⁺(Σ) ∪ I⁻(Σ), which are open and disjoint by achronality. So γ lies in one of them, say I⁺(Σ).
    - Fix p on γ, let γ₋ be its past part, and pick p′ ∈ I⁺(p) ∩ D̊ ∩ I⁺(Σ), non-empty as D̊ ∩ I⁺(Σ) is an open
      neighbourhood of p. Then p′ ∈ D⁺_I(Σ), not D⁻_I(Σ), as D⁻_I(Σ) ∖ Σ lies in I⁻(Σ), which is disjoint from
      I⁺(Σ). Let c be a timelike curve from p′ to p. It lies in I⁺(p) ⊂ I⁺(Σ) by transitivity of ≪, and γ₋ lies in
      I⁺(Σ) by the case, so c·γ₋ misses Σ. As p′ ∈ D⁺_I(Σ), it is not past-inextendible in M. So γ₋ has a past
      endpoint q, with q ∈ J⁻(p) ⊂ I⁻(p′) (push-up, I ∘ J ⊂ I).
    - If q ∈ I⁺(Σ): [Chr11] Proposition 2.9.7 (I⁻(p′) ∩ J⁺(S) ⊂ D⁺_I(S)) puts the open set I⁻(p′) ∩ I⁺(Σ) inside
      D⁺_I(Σ). So q ∈ D̊ and γ₋ extends in D̊.
    - If q ∉ I⁺(Σ): continue c·γ₋ past q as a past-inextendible timelike curve (the concatenation is a curve of
      [Chr11]'s class, section 2.3, which is not read here). It meets Σ, at some s ∈ J⁻(q). Either s = q ∈ Σ ⊂ D̊, and
      γ₋ extends in D̊; or q ∈ I⁺(s) ⊂ I⁺(Σ), against the case.
    - Either way γ is extendible in D̊, a contradiction. ∎
  - The push-up used is I ∘ J ⊂ I, in J⁻(p) ⊂ I⁻(p′). [Chr11] invokes its Lemma 2.4.14 for a step of this kind in the
    proof of Proposition 2.9.7; the lemma's statement is not read here (D395, verifier 178).
  - "Without boundary" is [Chr11]'s convention (p. 44): a hypersurface is an embedded submanifold of codimension one,
    assumed to have no boundary. Σ, the graph over the open shell, is one. Whether the convention also excludes an
    edge in the sense of achronal sets is not read here.
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
(pp. 11-12), Theorem 3.4 (p. 14), Theorem 3.13 (p. 20). READ ([Chr11] = P. T. Chruściel, "Elements of causality
theory", arXiv:1110.6706v1, read 2026-10-31 through alphaXiv): the definitions of section 2.9 (p. 44), Proposition 2.9.7
(pp. 45-46), the remark after Corollary 2.9.8 and Theorem 2.9.9 (p. 46), Lemma 2.9.11 (p. 47); the page numbers are the
notes' own. READ ([Min19] = E. Minguzzi, "Lorentzian causality theory", Living Rev. Relativ. 22 (2019) 3, read
2026-10-31 through a web-fetch connector, text extracted from the PDF): Theorem 3.45 (Int D(S) globally hyperbolic for S
closed and achronal) and Theorem 3.46; not used, as Σ is not closed.
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

**Lemma 6.4 ((b)'s first step located; deduced, D400).** Let Ω′ be the domain of the record's form (1.1) that Part VII
Lemma 1.2 chooses, with V′ := v_end + T′ and τ′_end, and P′ the supplement's domain (9.1) for those parameters, with
V′_P := V′ + 1 + (τ′_end − τ0) + κ (N1STAR-PROOF.md (1.1), (9.1)).

- (i) *Where the record's g_λ is.* Theorem 1 gives g_λ on Ω′ and Theorem P on P′, and both lie in {v ≤ V′_P}: on Ω′,
  v ≤ V′ + 1 + τ′_end − τ ≤ V′_P − κ, as τ ≥ τ0; on P′, v ≤ V′_P − h(τ).
- (ii) *Σ_IVP leaves it.* For r ≥ R_3, Σ_IVP = {t_KS = c_IVP − T_μend(|x|)} (Part VII 162-163), and it ends at spatial
  infinity I_0 (III.B 253-254), so v → ∞ along it. Hence Σ_IVP ∩ {v > V′_P} is non-empty and contains the whole end
  of Σ_IVP. The record gives no data there at all. Part VII's Theorem 0.2 replaces them, beyond R_3, by the data of
  exact Tangherlini metrics g^KS_(m,0) (Part VII 163-165, Proposition 2.2).
- (iii) *Neither construction reaches further at a fixed λ.* Theorem 1's λ_1 depends on T′. Theorem P's constants
  depend on P (section 9.2, first line), and through V_P:
  - the annuli A_P(τ) have thickness up to d1 = V_P − v_start and outer radius up to t + a2, a2 = V_P − τ0 − 1 (Lemma
    9.1 (d));
  - Lemma 9.3 (b)'s Poincaré constant grows with d1 (an integral over a length up to d1, with r³ varying along the
    ray by a factor up to (1 + d1)³);
  - Lemma 9.6 carries the weight (t + a2)^γ when γ ≤ 0;
  - the decay classes E_p of section 9.3 are bounds whose constants are taken on P+.

  Nothing in the proof gives a λ_P uniform in V_P. So at a fixed λ the record's data exist on a bounded part of
  Σ_IVP: on Σ_IVP ∩ {r ≤ 4R} for λ small depending on R, which is what Part VII Corollary 2.3 uses.
- (iv) *What the rest needs.* Let S := Σ_IVP ∩ {r ≥ 4R} with 4R ≥ R_3, and v1 the value of v on its inner edge ∂S;
  v1 ≥ v_end + 2 (Part VII 151).
  - In g0 = g^KS_(μend,0) (v ≥ v_end), the past domain of dependence W := D⁻(S) is bounded by S, by the ingoing null
    hypersurface N := {v = v1} through ∂S, and by past null infinity at v ≥ v1. For g_λ the same holds up to the
    O(λ) displacement of its null hypersurfaces against g0's.
  - N lies in Ω′ ∪ P′. From ∂S, which is in the interior of Ω′_+ (Lemma 1.2 (b)), N runs to the past in Ω′: τ
    decreases, so v + (τ − τ′_end) ≤ V′ + 1 is kept, and r = v1 − τ grows. At τ0 it meets Σ_τ0 ∩ Ω′ = Σ_τ0 ∩ P′
    (Lemma 9.1 (c)), so v1 ≤ V′_P − κ, and below τ0 it stays in P′, as h ≤ κ.
  - At past null infinity, for v ≥ v1 > v_end, the record's radiation field λ[W_TT] (P-ii) vanishes, as every
    oscillating profile does on {v > v_end} (Part VII 125-129).

  So (b)'s first step is a characteristic problem on W: the data of g_λ on N, nothing incoming at past null infinity,
  solved up to S and uniformly up to I_0, in the wave-map gauge relative to g^KS_(μend,0). It is a scattering problem
  near spatial infinity without incoming radiation, for a perturbation that is O(λ) on N. The record's data near I_0
  are not needed: past null infinity carries nothing there.
- (v) *What N carries.* On N ∩ P′, |g_λ − g_app| ≤ C λ^(K−3) t^(−2) with t ≈ r (P-iii). After the shell, g_app − g0 =
  Σ_j λ^j m_j, the means alone (Part VII 125-131). Theorem A_P's classes (9.6) give m_m ∈ L_2: a leading term
  r^(−2) M_m(v, x̂), M_m := 2 ∫_(−∞)^v S_(m,3) dv′, plus a remainder in E_(5/2) (N1STAR-PROOF.md 1265-1268,
  1296-1298). That is a leading term and a bound, not an expansion.
  - Lemma 0.1's sufficient condition asks for ρ²C^∞ and ρ³C^∞, expansions in integer powers of ρ = 1/r. III.K's class
    is polyhomogeneous with terms of orders r^(−2) and r^(−3) (paper section 8.4).
  - An E_(5/2) bound neither gives such an expansion nor excludes one. III.K's data index set admits half-integer
    exponents (D467, read; reframed D469). ℰ_0 is restricted by min Re ℰ_0 > 3/2 + 2γ_Υ, jℰ_0 ⊂ ℰ_0, ℓ_0 > 3 and ℓ_0 ∉ Re
    π_1ℰ_0 (III.K 53-57, III.C′ Theorem 3.1), where j ranges over ℕ and jℰ_0 is the j-fold sum (III.C Lemma 3.2 (b)):
    closure under addition, so 5/2 ∈ ℰ_0 forces 5, 15/2, …, and none of these conditions is integrality (an inference
    from their absence; the index sets' definition, III.A2 (2.2), is not read). Near I_0, ρ_0 = 1/(2 − x¹) (III.C 36),
    about 1/r. At 𝓘⁺, a different face, the expansion is in ρ_I, functions smooth on M_(1/2) are polyhomogeneous there
    with index set ½ℕ_0, and each slot's index set satisfies ℰ_s + ½ ⊂ ℰ^C_I ⊂ ℰ_s (PART-III-K-NONLINEAR.md 361-377,
    III.C Lemma 3.2 (a)); that bears on 𝓘⁺, not on I_0 (verifier 200). So Lemma 0.1's integer powers
    (PART-VII-ASSEMBLY.md 56-60) are a sufficient condition, not the class. Not read: whether a ρ^(5/2) term, such as the
    cross terms of the sources below could produce (D456), keeps ‖·‖_(d_1) finite, which depends on that norm's weights.

So (b) now consists of three steps:

- (b1) the scattering problem of (iv), with r-weighted estimates in place of Lemma 9.3's annuli of bounded thickness;
- (b2) the expansion of its solution at I_0, to put the data on S in III.K's class;
- (b3) Part VII Proposition 3.2 on g_λ's own data, as above.

**Lemma 6.5 (the Coulomb part, carried to I_0; computed, D406).** On five-dimensional Minkowski space in the chart
(v, r), ds² = −dv² + 2 dv dr + r² dΩ₃², let N = {v = v1} and let Y_l be a harmonic of S³. Expand φ = Σ_j a_j(v)
r^(−2−j) Y_l. Then □φ = 0 is (1 + 2j) a_j′ = −(l + 1 − j)(l + 1 + j) a_(j−1). The recursion stops at j = l + 1,
because in four space dimensions the radial order is the integer l + 1. With a_0 = M and a_j(v1) = 0 for j ≥ 1,

    φ_l = M r⁻² ₂F₁(−l, l + 2; 3/2; (v − v1)/(2r)) Y_l = M r⁻² U_l(1 − (v − v1)/r) Y_l / (l + 1),

U_l the Chebyshev polynomial of the second kind (the Gegenbauer polynomial of S³).

- φ_l is the solution with data M r⁻² Y_l on N and no incoming radiation (r^(3/2) φ_l → 0 at fixed v).
- On a slice t = const (v = t + r), r² φ_l is a polynomial in ρ = 1/r, so φ_l ∈ ρ²C^∞ there.
- Its value at ρ = 0 is M cos(πl/2)/(l + 1), and |r² φ_l| ≤ M wherever 0 ≤ (v − v1)/r ≤ 2, uniformly in l.

Checked by `checks/coulomb5.py` K1-K4 (exact, l ≤ 10). Control: flipping the cross term's sign gives no solution,
and the limit then grows (2, 5, 14, ...).

What it gives for (b2):

- By (v) the means carry on N the leading term r⁻² M_m(v, x̂).
- M_m := 2∫^v S_(m,3) dv′ is constant in v wherever its source has no r⁻³ part. Section 9.3's count suggests that is
  so after the shell: it puts products of means, and the background's Christoffels times means, at r⁻⁴ and below,
  so only the oscillating products reach r⁻³. This is not checked term by term here.
- In wave gauge the principal part of each Cartesian component's equation is the flat □.
- So, at the principal level and for the leading term, the means' data on S are Σ_l M_(m,l) r⁻² U_l(1 − (v − v1)/r)
  Y_l/(l + 1).
- On S, s := (v − v1)/r = 1 − (v1 − t)ρ. The coefficient of ρ^(2+k) is then M_(m,l) (t − v1)^k/k! times the k-th
  derivative of U_l/(l + 1) at s = 1, which is at most a power of l by Markov's inequality (wording corrected D413).
- So when M_m is smooth on S³ (its M_(m,l) decay faster than any power), the sum is in ρ²C^∞ (Lemma 0.1's condition
  for this term).
- The r⁻² coefficient at I_0 is Σ_l cos(πl/2)/(l + 1) M_(m,l) Y_l. The odd harmonics drop out at that order.

*On Tangherlini (D411; `checks/coulomb5.py` K5-K6).* In the ingoing chart ds² = −f dv² + 2 dv dr + r² dΩ₃²,
f = 1 − μ/r², the wave operator gains exactly −μ r⁻³ ∂_r(r ∂_r F). The recursion becomes

    (1 + 2j) a_j′ = −(l + 1 − j)(l + 1 + j) a_(j−1) − μ (j − 1)² a_(j−3).

- The factor 1 + 2j never vanishes, so no logarithm enters at any order.
- The μ terms have degree at most j − 2 in v − v1. So the top degrees, and with them the flat polynomial above, are
  unchanged, and μ enters r²φ at fixed t only from ρ² on.
- The series no longer terminates. Summed on t = const (v1 − t = 1, μ = 1, exact rationals), 40 and 60 terms agree
  to 10⁻¹² at r = 5, 10 and 40 for l = 0, ..., 3 (6.4 × 10⁻¹³ at l = 0, r = 5). r²φ approaches the flat value
  cos(πl/2)/(l + 1): for l = 0 it is 0.95823, 0.98542 and 0.99884 at r = 5, 10, 40. r²(1 − r²φ) is 1.044, 1.458,
  1.855, 1.963 and 1.991 at r = 5, 10, 40, 160 and 640, so the correction tends to 2.0/r² (corrected D420, verifier
  182: "about 1.86/r²" was the r = 40 value).
- Not proved: the convergence for every l and the radius of convergence in s, though the recursion's ratio for
  j ≫ l (about s/2) suggests |s| < 2.

**Lemma 6.5′ (the record's full flat operator; deduced, with `checks/coulombL5.py` Q1-Q4, D417).** On 4+1 Minkowski
the record's operator is L = D Ric + δ*_(E^C) δ_(E^Υ) G, with E^Υ built on c_Υ = r⁻¹ dt and E^C on
c = r⁻¹(dt − v dr) (lin5.py's L̄, [Hin26] (8.1)). Both 1-forms are homogeneous of degree −1, so L is homogeneous of
degree −2. Data r⁻² F(0) on N, with v1 = 0, therefore give the self-similar solution r⁻² F(s), s := v/r, if the
characteristic problem's solution is unique (not given here; see the list below, D429). On a slice
t = const, s = 1 + tρ, so the expansion at I_0 is F's Taylor series at s = 1.

- *Q1-Q2 (exact).* In the spherically symmetric sector, h = r⁻²(a dt² + 2b dt dr + c dr² + d r² g_S³), L reduces to
  a 4 × 4 system in s with second-order part −½ s(s − 2) F″ in every row, the principal symbol at ds. All other
  coefficients are polynomials in s. So its only singular points are s = 0 (N) and s = 2 (the cone u = 0), and I_0,
  at s = 1, is an ordinary point. The other angular components agree with χχ (φφ = sin²θ θθ), and the off-diagonal
  ones outside (t, r) vanish (checked since D429).
- *So r²h is smooth in ρ at I_0, with no logarithm, for every value of γ_Υ, e_Υ, γ_C, e_C and v* (an ODE with
  polynomial coefficients at an ordinary point). The argument uses only the principal symbol and the homogeneity, so its
  ordinary-point part holds for every harmonic, one at a time (D429). The computation covers the l = 0 sector and, since
  D421, the l = 1 scalar-type sector
  (Q5).
- *Q5 (exact, D421).* The l = 1 scalar-type sector, h = r⁻² Y(a dt² + 2b dt dr + c dr² + d r² g_S³) + 2r⁻¹(e dt +
  f dr) ⊗_s dY with Y = cos χ, has six functions. On S³ the traceless Hessian of an l = 1 harmonic vanishes, so there
  is no seventh. The result:
  - r, t and the angles drop out, and the seven components outside the sector vanish, with φφ = sin²θ θθ (all seven
    checked since D427).
  - The second-order part is −½ s(s − 2) times the identity, and the other coefficients are polynomials in s.
  - At the record's point the exponents at s = 0, besides 0, are −0.5099, −0.51, −0.52, −1.5 × 10⁶ (twice) and
    −3 × 10⁶, all negative.
- *Q6, Tangherlini to first order in μ (exact, D426).* Static t, f = 1 − μ/r², with c_Υ and c built on that t (the
  record fixes c_Υ only as |x|⁻¹ dt for large |x|; a t_* there changes the coefficients by terms of the same
  polynomial type; deduced, not computed). In the l = 0 sector, h = r⁻² F(s) + μ r⁻⁴ G(s).
  - The μ⁰ part is Q1's system.
  - The μ¹ part is an ODE system for G with a source in F, depending on s only.
  - Its second-order part is −½ s(s − 2) I, and its coefficients and source are polynomials in s.
  - G's exponents at s = 0, besides 0, are −2.5099, −2.52, −1.5 × 10⁶ and −3 × 10⁶ (the first two are Q4's shifted by
    −2), all negative. So there is no resonance: the regular branch at N exists for every G(0) with the polynomial
    source, and it is the only solution continuous at N.
  - s = 1 is an ordinary point of G's system (second-order part ½ I there, polynomial coefficients and source), so G is
    analytic at s = 1 whatever the exponents at N, and r²h = F(s) + μρ² G(s) + O(μ²) is smooth at I_0, with no
    logarithm at first order in μ. Higher orders in μ and the other sectors are not computed.
- *Q3 (exact control).* With the damping off, Lemma 6.5's polynomials solve the system: a = a_0, b = b_0(1 − s),
  c − d = e_0 U_2(1 − s)/3 and (c + 3d)/4 = p_0, the Cartesian harmonics l = 0, 1, 2, 0. The transfer from N to I_0
  multiplies them by 1, 0, −1/3, 1, which is cos(πl/2)/(l + 1). With U_1 in place of U_2 it fails.
- *Q4.* At s = 0 the Frobenius exponents are 0, for the regular branch the data fix, and 1 − eig(m1_0). At the
  record's point (lin5's: e_Υ = γ_Υ = 1/100, e_C = 1/102400, γ_C = 10⁶, v = 1/2) the latter are −0.5099, −0.52,
  −1.5 × 10⁶ and −3 × 10⁶, all negative. So the regular branch is the only solution continuous at N.
  - With the damping on, the r⁻² coefficient at I_0 is no longer Lemma 6.5's. At γ_C = 1 the transfer matrix
    (regular series, 400 terms, radius 2) agrees with a stiff integrator to 1.6 × 10⁻¹⁴ and mixes the components, for
    instance a(1) = 1.032 a(0) + ….
  - *At the record's γ_C = 10⁶ (D434; `checks/transfer5.py` T1-T3, computed, not certified).* The regular series
    summed at s = 1 with 400 and 600 terms agree to 30 digits (a 60-digit run differs by 5 × 10⁻²⁶; the largest
    coefficient is 2.0 at n = 1, with no transient) for γ_C = 1, 10², 10⁴, 10⁵ and 10⁶, and the stiff
    integrator agrees with it to 10⁻¹² up to γ_C = 10⁴ (at 10⁶ it did not finish in 25 minutes). The exponents at N
    besides 0 are −0.5099, −0.52, −1.5 γ_C and −3 γ_C: the stiff modes are the singular ones at N, and the regular
    branch is not stiff.
    - The transfer converges as γ_C → ∞. The successive differences, 10² to 10⁴, 10⁴ to 10⁵ and 10⁵ to 10⁶, are
      1.3 × 10⁻², 1.2 × 10⁻⁴ and 1.2 × 10⁻⁵, falling like 1/γ_C, so 10⁶ is within about 10⁻⁶ of the limit
      (extrapolated; verifier 186 ran on to γ_C = 10¹², where γ_C(T − T(10¹²)) stays at 1.363 from 10⁵ to 10⁸, so
      T(10⁶) is 1.36 × 10⁻⁶ from the limit, D435).
    - In the basis a, b, c − d, (c + 3d)/4, where Lemma 6.5's transfer is diag(1, 0, −1/3, 1), the record's point
      departs from it by up to 1.22: b(1) = −0.601 a(0) + 0.627 b(0) − 0.304 (c − d)(0) + 1.217 ((c + 3d)/4)(0), where
      the undamped b(1) is 0, and a(1) = 0.976 a(0) + 0.024 b(0) − 0.012 (c − d)(0) + 0.047 ((c + 3d)/4)(0).
    - So at the record's point the l = 0 part of the r⁻² coefficient at I_0 is this transfer applied to F(0), given
      uniqueness; each other harmonic has its own transfer (corrected D435, verifier 186), computed for l ≤ 12 in Q7.
- *Q7, every harmonic at the record's γ_C = 10⁶ (D436; `checks/harmonics5.py` S1-S3, T and G).*
  - *S1-S2 (exact).* With the harmonic kept abstract (a zonal Y with ΔY = −κY, κ = l(l + 2), and an axial
    divergence-free V with ∇^A∇_A V = −(κ − 1)V, the rough Laplacian), the scalar type reduces to a 7 × 7 system in s (6
    × 6 at l = 1) and the
    vector type to 3 × 3 (2 × 2 at l = 1). Each has second-order part −½ s(s − 2) I and polynomial coefficients, the
    off-sector components vanish and χ drops out (15 and 17 checks). At κ = 0 and κ = 3 the scalar system is
    coulombL5's l = 0 and l = 1 system exactly.
  - *S3 (exact).* For any angular, traceless h the gauge 1-form w = δGh + E^Υ Gh is −(div_(S³) h)/r² on the sphere and
    0 in t and r. So on the tensor type w = 0 and L h = D Ric h: its transfers do not depend on γ_C or γ_Υ.
  - *T (computed, not certified).* For l = 1, ..., 12 every scalar- and vector-type transfer at γ_C = 10⁶ is finite.
    The series agree to 30 digits at 400 and 600 terms, and the exponents at N besides 0 do not depend on l: M1 carries
    no κ (exact), and they are −1/2, −1/2 − γ_Υ(1 − e_Υ), −1/2 − γ_Υ, −1/2 − 2γ_Υ, −1/2 − γ_C(1 + v)(1 − e_C), −1/2 −
    γ_C(1 + v) and −1/2 − 2γ_C(1 + v) (−0.5, −0.5099, −0.51, −0.52, −1.499986 × 10⁶, −1.5 × 10⁶ and −3 × 10⁶ at the
    record's point), a subset at l = 1 and on the vector type. So no harmonic is resonant at N, for any l (verifier 187,
    D438). The change
    from γ_C = 10⁵ to 10⁶ grows with l, from 2.5 × 10⁻⁵ at l = 1 to 3.4 × 10⁻² at l = 12 (scalar type, raw components).
  - *G (computed).* In the basis normalised by each harmonic's L²(S³) size, the norms of F(0) ↦ F^(k)(1) at l = 12
    are 10.75, 15.7, 18.1 and 148 for k = 0, ..., 3 on the scalar type (b counted twice, corrected D438), and 1.04, 1.00,
    9.4 and 176 on the vector type.
    They grow roughly like l, l, l and l² (scalar) and 1, 1, l and l² (vector), with an even-odd alternation in l.
  - So up to l = 12 the first four Taylor coefficients at I_0 (k ≤ 3) grow no faster than about l², the local exponent of
    k = 3 still rising towards 2, which is what Lemma 0.1's condition needs
    for the sum over l when the data's harmonics decay faster than any power. That is evidence; the l-uniform bound is
    proved in Q8 (D437). The tensor type's transfer is the undamped one and is not computed here.
- *Q8, Lemma 6.5‴: the transfer bounded uniformly in l (D437; `checks/uniform5.py` U1-U6).* At the record's point, for
  every scalar- and vector-type harmonic l ≥ 2, write x := κ^(1/2) and the reduced system of Q7 in the basis normalised
  by a basis equivalent, uniformly in l, to the harmonic's L²(S³) size (ratios in [0.55, 0.82], verifier 188), W =
  diag(1, 1, 1, 1, x, x, x²) on (a, …, k) and diag(1, 1, x) on (p, q, k), as
  m₂F″ + M₁F′ + M₀F = 0, m₂ = s − s²/2.
  - *Structure (exact, U1-U2).* M₂ = m₂ I; M₀ = (x²/2) I + N with every entry of N of degree at most 1 in x; M₁ of
    degree at most 0. A(s) := M₁(s) − (1 − s) I/2 has A(0) independent of x, with eigenvalues 1, 1.0099, 1.01, 1.02,
    1.49999 × 10⁶, 1.5 × 10⁶ and 3 × 10⁶ (scalar) and 1, 1.01 and 1.5 × 10⁶ (vector), all positive.
  - *The metric (exact, U3).* The H with H A(0) + A(0)ᵀ H = I is positive definite (every leading minor positive), with
    λ(H) in [1.62 × 10⁻⁷, 1.117] (scalar) and [3.33 × 10⁻⁷, 0.551] (vector). Control: with −A(0) no positive H exists.
  - *The equation in T.* With T := ∫₀^s m₂^(−1/2), so that s = 1 − cos(T/√2), N lies at T = 0, I_0 at T = π/√2 and
    s = 3/2 at T = 2√2π/3. Since F_s = T_s F_T and m₂T_ss = −(1 − s)T_s/2,
        F_TT + T_s A(s) F_T + M₀ F = 0,   T_s = m₂^(−1/2).
    The regular branch at N (no resonance for any l ≥ 2: A(0) is independent of l with positive eigenvalues, U2) is
    smooth in T with F_T(0) = 0, since s is even and analytic in T.
  - *The energy.* E := ⟨F_T, H F_T⟩ + (x²/2 + 1)⟨F, H F⟩. The (x²/2) I part of M₀ cancels against the derivative of
    the second term, and H A(0) + A(0)ᵀ H = I, so
        dE/dT = −T_s |F_T|² − 2T_s ⟨F_T, H (A(s) − A(0)) F_T⟩ − 2⟨F_T, H N F⟩ + 2⟨F_T, H F⟩.
    The first term is at most 0. On [0, s₁], |A(s) − A(0)| ≤ a₁ s and T_s s ≤ (s₁/(1 − s₁/2))^(1/2), and |N| ≤ n₀ + n₁ x
    for x² ≥ 8 (U4, from the coefficients' absolute values). With μ = λ_min(H) and 2x|F_T||F| ≤ √2(|F_T|² + x²|F|²/2),
        dE/dT ≤ C_E E,   C_E = (|H|/μ)(2 (s₁/(1 − s₁/2))^(1/2) a₁ + n₀ + 1 + √2 n₁),
    independent of l. So E(T) ≤ e^(C_E T) E(0), where E(0) = (x²/2 + 1)⟨F(0), H F(0)⟩, and on [0, s₁]
        |F(s)| ≤ K₀ |F(0)|,   |F_T| ≤ K₀ (x²/2 + 1)^(1/2) |F(0)|,   K₀ = (|H|/μ)^(1/2) e^(C_E T(s₁)/2).
    U5: ln K₀ = 1.22 × 10¹⁴ at s₁ = 1 and 2.26 × 10¹⁴ at s₁ = 3/2 (scalar); 1.33 × 10¹³ and 2.34 × 10¹³ (vector).
  - *Derivatives.* On [1/2, 3/2] the equation is regular (m₂ ≥ 3/8). Differentiated k times it gives F^(k+2) in terms of
    lower derivatives, with coefficients bounded by C (from M₁) and C(1 + x²) (from M₀) together with their
    s-derivatives. By induction |F^(k)(s)| ≤ K_k (1 + x²)^(k/2) |F(0)| there, with K_k independent of l.
  - *Tensor type.* There w = 0 (Q7, S3); as h is traceless and divergence-free on S³, δGh = δh = 0 as well, so L h = D
    Ric h = −½ □_L h, which on Minkowski acts on each Cartesian component as □. Each component is r⁻² k(s) times a
    harmonic of degree l, k analytic at N (the scalar equation's exponents there are 0 and −½), so it is Lemma 6.5's
    solution, k = k(0) U_l(1 − s)/(l + 1), and Markov's inequality on s ∈ [0, 2] bounds |k^(m)| by l^(2m)|k(0)|
    (corrected D439, verifier 188).
  - *The low harmonics* l = 0, 1 are finitely many, each smooth at s = 1 (an ordinary point), its regular branch fixed by
    the negative exponents at N of Q4, Q5 and Q7.
  - *Consequence.* For smooth data on N the normalised harmonic coefficients F_l(0) decay faster than any power of l,
    and the normalised harmonics' C^m norms on S³ grow at most polynomially. So r²h = Σ_l F_l(s) H_l(ω), with all its
    derivatives, converges uniformly on [1/2, 3/2] × S³: r²h is smooth in (s, ω) near s = 1, that is in ρ²C^∞ at I_0.
    Lemma 0.1's condition for the Coulomb term holds at leading order in flat space, for the full operator at the
    record's point, given uniqueness.
  - The constant is finite and independent of l, which is all the condition needs; it is not a good constant. The
    record's γ_C = 10⁶ enters through |H|/μ ≈ 7 × 10⁶ and coefficients of size 10⁶. On the computed harmonics the energy
    ratio E(T₁)/E(0) on coordinate data F(0) = e_j is at most 3.6 and falls with l (U6, l = 2, …, 6); over all F(0) its
    supremum is 2.85 × 10⁶, 2.25 × 10⁶ and 1.35 × 10⁶ (scalar, l = 2, 3, 4) and 3.1 × 10⁵, 1.5 × 10⁵ and 6.3 × 10⁴
    (vector), reached on data with small ⟨F(0), H F(0)⟩ (verifier 188, D439), far below e^(C_E T₁).

So at leading order in flat space, and for the full operator, each harmonic of the Coulomb part lies in ρ²C^∞ at
I_0, given uniqueness. Whether their sum does, Lemma 0.1's condition for this term, needs a bound uniform in l on the
transfer's Taylor coefficients at s = 1 in place of Lemma 6.5's Markov step. That bound is Lemma 6.5‴ (Q8, D437), so the
condition holds for the full operator at the record's point, when M_m is smooth on S³, given uniqueness (open from D429,
verifier 183, until D437). On the scalar and vector types the coefficient is the transfer matrix's, not cos(πl/2)/(l +
1); on the tensor type it is cos(πl/2)/(l + 1).

What it does not give:

- Tangherlini's corrections beyond the scalar model (the curvature couplings of the tensor equation);
- the structure beyond the principal part (the gauge terms and the trace couplings) on Tangherlini; on Minkowski it is
  Lemma 6.5′ (D417);
- the remainder in E_(5/2) of (v), and the remainder g_λ − g_app (its sources lie in a strip of bounded v along N and
  enter at ρ³ or later in the scalar model, l ≤ 4: D464, D474);
- uniqueness in W beyond the expansion (an energy identity on W would give it); Lemma 6.5′'s self-similar reduction
  assumes it;
- the condition on the sources between N and S (D413, verifier 181). An r^(−q) source there contributes at ρ^(q−2), so
  the r⁻² coefficient at I_0 above needs those sources to be o(r⁻⁴). For l = 0, □φ = f r⁻⁴ Y_0 with zero data on N gives
  φ = r⁻² G(s) with s(s − 2)G″ + 3(s − 1)G′ = f, and G(1) = −f/2, which shifts the ρ² coefficient. After the shell the
  leading means are static, and their products are r⁻⁶ (D447, `checks/sources5.py` Q1-Q3): every term of P quadratic in a
  static h homogeneous of degree −2 has derivative order plus c-order two, so it is homogeneous of degree −6 on
  Minkowski, and higher orders of degree −8 or less (computed at p and 2p for Ric and for δ*_(E_C) Υ⁰ with random static
  h and the record's c_C = r⁻¹(dt − v_C dr), 30 digits; a non-static h breaks it; D449), and Tangherlini's corrections
  lower the degree. So they are o(r⁻⁴), as needed. The cross terms with the means' remainder in E_(5/2) are o(r⁻⁴) too
  (D454, corrected D456; `checks/sources5.py` Q4-Q5). E_(5/2) bounds every Cartesian derivative and every rotation
  derivative by r^(−5/2) (N1STAR-PROOF.md, the classes before Lemma 9.7), so a tangential derivative gains r⁻¹ but a
  radial or time derivative need not. The largest is h ∂_r²ρ, O(r^(−9/2)), which a remainder oscillating in r attains
  (fitted exponent within 0.08 of −9/2 over r = 8-128); the others are O(r^(−11/2)) or less, and the remainder's own
  products O(r⁻⁵). A remainder whose derivatives all gain would give O(r^(−13/2)). The margin over r⁻⁴ is only r^(−1/2):
  by the rule above an r^(−9/2) source contributes at ρ^(5/2), a half-integer power, which bears on (v)'s open question
  whether half-integer exponents occur. The sources from e := g_λ − g_app (D461, corrected D464 and D468). (P-iii) bounds
  e and ∂e by C t⁻² with no gain (N1STAR-PROOF.md 1041-1042), and (9.8) with Lemma 9.3(a) bounds the higher derivatives
  of w_n on the far region (τ ≤ τ_T, t ≥ λ⁻²), |∂ʲw_n| ≲ λ^(K′−2−j) t⁻² for 1 ≤ j ≤ k − 2 uniformly in n, again with no
  gain (verifier 198; one power of λ better than D464 stated, verifier 199; the passage from w_n to e is not checked). So
  where they act, the terms quadratic in e and h ∂²e are of order r⁻⁴, attained for an e in that class
  (`checks/sources5.py` Q6). But e is bounded only on P′, which has v ≤ V′_P, while I_0 lies at v → ∞: these sources sit
  in a strip of bounded v along N. In the scalar l = 0 model on flat 5D, r²φ → −1/2 for r⁻⁴ on all of v ≥ 0 (the G(1) =
  −f/2 above), but r · r²φ → about −0.785 for r⁻⁴ on the strip v ∈ [0, 1] (−0.784 at r = 400 and still drifting;
  `checks/strip5.py`). So in that model a strip source enters at ρ³, not ρ², and, the l = 0 kernel being positive, the
  model bounds every |S| ≤ r⁻⁴ on the strip; in that model these sources do not reach the r⁻² coefficient, and D461's
  conclusion that the record needs a stronger remainder bound is withdrawn. Beyond V′_P, g_λ − g_app is not defined and
  the remainder there is (b1)'s unknown, which nothing above bounds (verifier 199). In the same model at l = 1-4 (D474,
  `checks/strip5.py` T4), with the potential (l(l + 2) + 3/4)/r², the strip enters at ρ³ at l = 1 and 3 (r · r²φ → −1/3
  and 1/15) and at ρ⁴ at l = 2 and 4: the ρ³ coefficient is C_l = −π/(4Γ(1 − l/2)Γ(2 + l/2)), −π/4, −1/3, 0, 1/15, 0 for
  l = 0-4, zero at every even l ≥ 2 (verifier 202's Riemann-function computation, D481; `checks/strip5.py` T5), so in no
  harmonic computed does it reach ρ²; for l ≥ 1 these are values for S = r⁻⁴Y_l, not bounds, as the kernel changes sign.
  Not computed: the strip for the full operator, and whether its r⁻³ term, which carries no structure, is compatible with
  Lemma 0.1's ρ³C^∞.
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

**Proposition 6.2 (deduced from the census, D363; repaired D366, D372; re-proved Part by Part, D368-D378).** Let r_♭ ∈
(0, ½R_1] and replace III.B's r_0 by r_♭ and its ε_param by min(1/20, r_♭/(4R_1)). Put Part I's artificial boundary
there too, r_0^A := r_♭, with the collar δ_0 := min(R_1/16, r_♭/4) (BEYOND5-R0-PROOF.md section 0). Then each of the 214
matched lines that use the inner radius (DEF, SPC, CON, VAL) holds with r_♭, the constants then depending on r_♭. The
Part-by-Part re-proof is BEYOND5-R0-PROOF.md. So with r_♭ := ½ min(R_1, r_q(μ_end)), Proposition 6.1's conclusion holds
for every μ_end, without (1.1).

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
BEYOND5-R0-PROOF.md (D368-D378): Parts I-IX in four batches, each read by its own verifier (169-173), the findings
seated. It found the record's radius mismatch (D372, repaired in Part VI at D373) and the inner-boundary input of II.F
Lemma 1.3 (D378), and no step that fails at r_♭. A use that names the inner radius by none of the eight strings would be
missed; verifier 168 searched for the names above and found them harmless. [Hin26a] Proposition 5.1's conditions at m
are IV6-SOLV Lemma 0.5's (1)-(6); of these only (1) and (6) involve m, and both hold on (0, r_h) (C2 and the sign
argument above). The source itself is not read at m here. Part VII's record domain Ω′ reaches r ≥ a′ = q_0 − δ′_0, below
the record's q_0; with r_♭ it must reach further, through δ′_0 alone. The region r_♭ ≤ r < r_q, covered too, lies beyond
the curvature boundary, where the paper's premise has the classical description stop.

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
