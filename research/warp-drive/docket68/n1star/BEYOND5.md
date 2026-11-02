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
    exponents (D467, read; reframed D469). ℰ_0 is restricted by min Re ℰ_0 > 3/2 + 2γ_Υ, jℰ_0 ⊂ ℰ_0, ℓ_0 > 3 and ℓ_0 ∉
    Re π_1ℰ_0 (III.K 53-57, III.C′ Theorem 3.1), where j ranges over ℕ and jℰ_0 is the j-fold sum (III.C Lemma 3.2 (b)):
    closure under addition, so 5/2 ∈ ℰ_0 forces 5, 15/2, …, and none of these conditions is integrality (an inference
    from their absence; the index sets' definition, [Hin26] (2.2), cited at PART-III-A-PREREQ.md:33, is not read). Near
    I_0, ρ_0 = 1/(2 − x¹) (III.C 36), about 1/r. At 𝓘⁺, a different face, the expansion is in ρ_I, functions smooth on
    M_(1/2) are polyhomogeneous there with index set ½ℕ_0, and each slot's index set satisfies ℰ_s + ½ ⊂ ℰ^C_I ⊂ ℰ_s
    (PART-III-K-NONLINEAR.md 361-377, III.C Lemma 3.2 (a)); that bears on 𝓘⁺, not on I_0 (verifier 200). So Lemma 0.1's
    integer powers (PART-VII-ASSEMBLY.md 56-60) are a sufficient condition, not the class. Not read: whether a ρ^(5/2)
    term, such as the cross terms of the sources below could produce (D456), keeps ‖·‖_(d_1) finite, which depends on
    that norm's weights. [D517, read and deduced. The norm is H^(d_1) of H^(∞,(ℰ_0,ℓ_0))_b × H^(∞,(ℰ_0+1,ℓ_0+1))_b,
    infinite outside these spaces (PART-VII-ASSEMBLY.md:52-54), so it is finite on a ρ^(5/2) term exactly when (5/2, 0)
    ∈ ℰ_0. Part VII takes ℰ_0 = {(j, 0) : j ≥ 2} and ℓ_0 ∈ (3, 4) (PART-VI4-PARAMS.md:69-70), where it is infinite. Row
    d1's hypotheses (VI4:40; III.C′ Theorem 3.1, PART-III-C2-POLYHOM.md:133-140: min Re ℰ_0 > 3/2 + 2γ_Υ, jℰ_0 ⊂ ℰ_0,
    ℓ_0 > 3, ℓ_0 ∉ Re π_1ℰ_0) admit ℰ_0^½ := {(2 + j/2, 0) : j ∈ ℕ_0}, closed under sums, with ℓ_0 ∈ (3, 4) ∖ {7/2}.
    Lemma 0.1's proof carries over to components in ρ²C^∞ and ρ³C^∞ of the compactification in ρ^(1/2): Taylor's formula
    in ρ^(1/2), whose smooth functions are conormal in ρ (ρ∂_ρ = ½ρ^(1/2)∂_(ρ^(1/2))), the exponents 2 + j/2 < ℓ_0 lying
    in ℰ_0^½ and the remainder in ρ⁴C^∞ ⊂ ρ^(ℓ_0)H^∞_b. So half-integer exponents at I_0 lie in a class row d1 admits,
    with ℰ_0^½ in place of Part VII's choice. What that choice moves (corrected D519, verifier 223): little. ℰ_0 reaches
    the rest of the proof through ℰ^C_I (row d2, III.C′ Theorem 3.1), Λ ⊃ π_1ℰ^C_I (PART-III-I11-SPACETIME.md:66), III.K
    Theorem 4.3's ε and d_1 (row n1) and l_* (I11:71-75). But ℰ^C_I already contains (2 + j/2, 0) for every j and every
    admissible ℰ_0: III.C Lemma 3.2 (a) gives ℰ^C_I + ½ ⊂ ℰ^C_I and (2, 0) ∈ ℰ^C_I (PART-III-C-EXTERIOR.md:189-191), and
    Theorem 3.1's proof starts from the least Definition 3.1 set containing ℰ_0 (PART-III-C2-POLYHOM.md:257-259), the
    same for ℰ_0 and ℰ_0^½. So π_1ℰ^C_I, Λ, (G), (G+), ε_+, ε_K and LOSS-D's counts are unchanged. Only the log orders
    of ℰ^C_I at the half-integers can rise (each round takes ℰ_0 ∪̄ ℰ^C_I, C2:228-230, 247-250), which enter l_* and
    K(λ) (I11:71-81); not computed. D517 had said the choice moves Λ and (G+)'s margin, and had left this unread.]

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
  enter at ρ³ or later in the scalar model, l ≤ 4, and under the full operator at every scalar- and vector-type harmonic
  l ≤ 12, with no logarithm: D464, D474, D487);
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
  The strip for the full operator (D487, corrected D491; `checks/stripfull5.py` P1-P5): at radius r the strip is s = v/r
  ∈ [0, d/r], so for the degree −3 profile h = r⁻³F(s) a source of Cartesian size r⁻⁴ on it acts as σd δ(s) at N (σd = ∫
  r⁴S dv over the strip). With harmonics5's reduction at degree −3 (M2 = (s − s²/2)I), integrating (sF′)′ + (M1(0) − I)F′
  = σd δ over the strip, with F = 0 on N, gives F(0+) = (M1(0) − I)⁻¹σd; beyond it the solution is the regular one with
  that value (distributionally: F = H(s)F_reg and sδ′ = −δ; the delta is the strip's leading term in d). So the strip
  enters at ρ³ with coefficient Kσd, K = T_3(M1(0) − I)⁻¹ and T_3 the degree −3 transfer from N to I_0, when every
  eigenvalue has Re m > 1. In the scalar model this is exact: M1(0) = 5/2, F(0+) = −d/3, the regular solution is ₂F₁(3 +
  l, 1 − l; 5/2; s/2), and Gauss's second summation theorem gives F(1) = C_l, verifier 202's coefficient (P1: to 10⁻³⁰
  for l ≤ 6, through the same series transfer as P3). For the record's full operator at its point (γ_C = 10⁶), at every
  scalar- and vector-type harmonic l ≤ 12: M1(0) at degree −3 is M1(0) at degree −2 plus I (exact, P2); its eigenvalues
  are 2.5, 2.51, 2.52 and the damping's 1.5 × 10⁶ and 3 × 10⁶ (at l = 0 and 1 the least is 2.5099), so every Re m ≥ 2.5;
  and K is finite, its norm in each harmonic's normalised basis at most 2.99 (scalar type 1.97 to 2.99, vector type 0.17
  to 1.14; the series at 400 and 600 terms agree to 30 digits; P3). So for every harmonic computed the strip enters at ρ³
  with no logarithm and does not reach the r⁻² coefficient. Its width corrections are analytic in d, at integer powers
  (D491; verifier 208 corrected D487's ρ^(2+m)): the operator is invariant under t → t + c, so a sheet of source at v =
  v_0 gives r⁻³F(1 − v_0/r) at t = 0, and over a uniform strip r³h(I_0) = dKσ + (d²/r)K4σ + O(d³/r²), K4 = −½T_3′(M1(0) −
  I)⁻¹ with T_3′ the transfer to F′(1): ρ⁴, ρ⁵, …. In the scalar model K4 = 1/2, 0, −1/6, 0, 1/10, 0, −1/14 for l = 0-6
  (P1, to 10⁻³⁰), strip5's ρ⁴ at l = 2 and 4 (D474) and, at l = 0, the drift of −0.784 at r = 400 above (−π/4 + 1/800 =
  −0.78415); for the full operator K4 is nonzero at every harmonic l ≤ 12, normalised norm 1.70 to 3.31 (scalar type) and
  0.063 to 0.58 (vector type). This is for a source r⁻⁴σ(v) with σ independent of r; a source only bounded by r⁻⁴ is not
  covered, the kernel having no sign. Uniformly in l (D492, `checks/uniform3_5.py` V1-V7): Lemma 6.5‴'s steps run on the
  degree −3 matrices. The structure holds (second-order part m2 I, M0 = x²I/2 + O(x), M1 = O(1) in x = κ^(1/2)); A_3(0) =
  A_2(0) + I exactly, independent of x, with eigenvalues 2, 2.0099, 2.01, 2.02 and the damping's (scalar type; 2, 2.01
  and 1.5 × 10⁶ on the vector type), and it has a positive Lyapunov metric; the jump J = M1_3(0) − I is M1_2(0),
  independent of x, with |J⁻¹|_2 ≤ 0.993 (scalar) and 0.698 (vector). So |K|_2 ≤ K0_3 |J⁻¹|_2 in uniform5's normalised
  basis for every l ≥ 2, ln K0_3 = 5.99 × 10¹³ and 5.87 × 10¹²: uniform, not sharp (the computed values at l = 2-6 are
  2.2 to 2.4 and 0.34 to 1.0 there; in harmonics5's weighting, which P3 uses, 2.76 to 2.99 and 0.353 to 1.14, the two
  weightings differing by factors bounded independently of l, in [0.645, 1.732] and [1.118, 1.414], so the bound is
  uniform in either; verifier 212, D500). J's eigenvalues, 1.5, 1.5099, 1.51, 1.52 and the damping's, do not depend on x,
  so M1_3(0) = J + I has every real part > 1 at every l ≥ 2, not only at the l computed (P3's '2.51' at l ≥ 2 is 2.5099
  and 2.51 at four digits; D500). K4 is bounded by the derivative estimate, at most linearly in l. Only uniform5's s_1 =
  1 case is rerun at degree −3; that covers K and K4, which need F(1) and F_s(1), but not, by this run alone, the ρ⁵ and
  later width coefficients, which need the derivative induction (D500); for s ≤ 1 that needs only s_1 = 1 (D508).
  Computed to l = 40 (D496, `checks/stripfull5.py 40`, every check passing): on the scalar type ‖K‖ is 2.74 and ‖K4‖ 2.73
  at l = 40, both flat from about l = 10 (K4 does not grow as the bound allows), and on the vector type both fall (0.054
  and 0.021 at l = 40); K at γ_C = 10⁵ departs from its value at 10⁶ by up to 6.8 at l = 40 (scalar type), so what is
  computed is the record's γ_C = 10⁶, not the limit of large damping. The tensor type (D502, `checks/stripfull5.py`
  P4-P5): on h = r^(2−p)F(s)T_AB with T a TT harmonic of level l ≥ 2 on S³, the gauge 1-form vanishes (harmonics5 S3), so
  L = D Ric, which on flat space is −½□ on each Cartesian component once δGh = 0; and each Cartesian component of T is a
  scalar harmonic of degree l (D439). So the tensor type at degree −3 is the scalar model at κ = l(l + 2), and its K and
  K4 are P1's in L's normalisation. Checked on the record's operator itself, exactly at three points, on random
  combinations of all the level-l harmonics for l = 2, 3 and 4 (built as homogeneous polynomial tensors on ℝ⁴, tangent,
  traceless, divergence-free and harmonic: 10, 24 and 42 of them, 2(l + 3)(l − 1), the full count: the SO(4)
  representations (l, ±2), each of dimension (l + 3)(l − 1) by Weyl's formula, as in Lindblom, Taylor and Zhang,
  arXiv:1709.08020, eqs. (39)-(40), read by verifier 215), every component of L h and of the gauge 1-form as predicted,
  while a wrong κ and an added trace part fail (P4). Verifier 215 (D504) confirmed it by another route: the six
  SU(2)-invariant l = 2 TT tensors with F free, the record's operator at six points, δGh, E^ΥGh and w each zero
  separately; and every one of the 76 basis harmonics at l = 2, 3, 4 traceless, divergence-free and with rough Laplacian
  −(l(l + 2) − 2). By Gauss's second summation theorem K = 2(−1)^((l − 1)/2)/(l(l + 2)) and K4 = 0 at odd l, K = 0 and K4
  = −(−1)^(l/2)/(l + 1) at even l, exactly from the terminating sums for every l ≤ 40 (`stripfull5.py 40`; a plain run
  checks l ≤ 12), the series transfer agreeing for l ≤ 12 to 9.3 × 10⁻²⁷ (P5). So on the tensor type the strip enters at
  ρ³ only at odd l, with |K| ≤ 2/15 (at l = 3), and at even l first at ρ⁴, with |K4| ≤ 1/3 (at l = 2): both fall with l,
  so the bound is uniform without Lemma 6.5‴, and there is no logarithm (M1(0) = 5/2). Every type is now computed.
  *Compatible with Lemma 0.1 (D508; deduced, with `checks/stripderiv5.py` as a computed check).* Lemma 0.1
  (PART-VII-ASSEMBLY.md:56-69) asks only that the Cartesian components lie in ρ²C^∞ (γ̃) and ρ³C^∞ (k̃) of the radial
  compactification; no structure is asked of the coefficients, the class's ℰ_0 = {(j, 0) : j ≥ 2} containing ρ³. On {t =
  0} the strip's term is, harmonic by harmonic, r⁻³ ∫ T_l(1 − vρ) J_l⁻¹ σ_l(v) dv over the strip (time-translation
  invariance; T_l the transfer of the regular degree −3 solution from N, F depending on v through F(0) = J⁻¹σ(v)), and s
  = 1 is an ordinary point (m2(1) = ½); so it is ρ³ times a function of ρ whose k-th derivative is ∫ (−v)^k T_l^(k)(1 −
  vρ) J_l⁻¹ σ_l(v) dv, with 1 − vρ ∈ [½, 1] for ρ ≤ 1/(2d). On [½, 1] the equation is regular (m2 ≥ 3/8), the structure
  M1 = O(1), M0 = x²I/2 + O(x) with entries polynomial in s holds at degree −3 (D492, V1), and the s1 = 1 energy bound
  gives |F| ≤ K0_3|F(0)| and |F_T| ≤ K0_3(x²/2 + 1)^(1/2)|F(0)| there; differentiating the equation then gives |F^(k)| ≤
  K_k(1 + κ)^(k/2)|F(0)| with K_k independent of l (uniform5's induction U5, which for s ≤ 1 needs only s1 = 1; this also
  bounds the ρ⁵ and later width coefficients D500 left open, by polynomials in l). Computed at degree −3 for l = 2-20
  (stripderiv5): |F^(k)(1)|/(1 + κ)^(k/2) in uniform5's basis is about 1.5 l at k = 0 on the scalar type (31.6 at l = 20,
  61.5 at l = 40 by verifier 219; 1.6, flat, on the vector type), about 3.0 at k = 1 (scalar; falling on the vector
  type), and falls with l for k = 2, 3, 4: polynomial and far below the induction's l-independent K_k, a pre-asymptotic
  consistency check at s = 1 only (it does not probe uniformity, x²/2 dominating M0's lower terms only from x ≈ 5 × 10⁶
  on the scalar type; D510). The tensor type has F = F(0) ₂F₁(3 + l, 1 − l; 5/2; s/2) = F(0) C^(2)_(l−1)(1 −
  s)/C^(2)_(l−1)(1), a Gegenbauer polynomial, so |F| ≤ |F(0)| on [0, 2] and Markov's inequality bounds its derivatives
  polynomially (verifier 219: the normalised derivatives on [½, 1] fall like l⁻²); l = 0 and 1 are finitely many, s = 1
  an ordinary point. Lemma 0.1 is posed on Σ_IVP, which far out is {t_KS = f(|x|)} with f′ ∈ |x|⁻²C^∞
  (PART-VII-ASSEMBLY.md:162-163), so there s = 1 − (v + c + O(ρ))ρ: a constant shift (a time translation) and an O(ρ)
  bending (Faà di Bruno), and the argument carries over (D510). So for a source r⁻⁴σ(v, ω) with σ ∈ L¹(dv; C^∞(S³))
  supported in v ∈ [0, d], after N, the sum over harmonics converges with every derivative, and the strip's term lies in
  ρ³C^∞ ⊂ ρ²C^∞ (its t-derivative, of degree −4, in ρ⁴C^∞ ⊂ ρ³C^∞): inside Lemma 0.1's sufficient condition. Not covered:
  sources known only by a bound O(r⁻⁴), which is what the record gives (D464), and half-integer exponents, for which
  Lemma 0.1 is not the class (D467). [D517: Lemma 0.1 extends to data smooth in ρ^(1/2), with the half-integer ℰ_0^½
  that row d1 admits in place of Part VII's ℰ_0; (G+)'s margin does not move with it, (v) (corrected D519).]
  [D520, read and deduced: the sources from e are known by more than a bound. Proposition 9.8's energy carries rotation
  derivatives at no cost in λ, E(τ) = Σ_(i+|β|≤k) λ^i ‖∂^i Ω^β ∂w_n‖ ≤ M_F λ^(K′) t^(−1/2) (N1STAR-PROOF.md:1335), and
  Lemma 9.3(a), Sobolev with rotations on the annuli (1103-1104), turns it into |Ω^γ ∂w_n| ≤ C λ^(K′−3) t^(−2) for |γ| ≤
  k − 3, uniformly on each annulus A_P(τ) of the far region (t ≥ λ⁻², t + a_1 ≤ r ≤ t + a_2, Lemma 9.1(d)), the decay
  carried by t⁻². The sources quadratic in e and h ∂²e therefore have, after the factor r⁴, angular derivatives up to
  order about k − 4 bounded uniformly (h ∈ L_2, its rotation derivatives O(r⁻²); each derivative of ∂e costs one λ⁻¹).
  D508's argument, run at finite regularity, then puts the strip's term in ρ³C^m of the compactification with m equal to
  k − 4 less the Sobolev loss on S³ (more than 3/2), so about k − 6 and zero at k = 6, each ρ-derivative costing (1 +
  κ)^(1/2) (D508). Lemma 0.1 asks for finitely many seminorms, a number set by d_1 = N + k″
  (PART-III-K-NONLINEAR.md:417; more than 10¹⁷, LOSS-D LD12), so what is needed is the far region at an order k above
  that number. Section 9 inherits Theorem E's k = 6 (N1STAR-PROOF.md:92). 10.51 reads section 4 for its dependence on k
  and finds Theorem E at every order k ≥ 6 with K ≥ 6 (6708-6733), but it does not read Proposition 9.8. What remains is
  Proposition 9.8 read at every order (k enters through Lemma 9.3's three rotation derivatives and the commutators) and
  the passage from w_n to e (D464); neither is done here. Corrected D521 (verifier 224): both are done in the record at
  fixed λ, which is all the strip needs. Lemma 11.0 (N1STAR-PROOF.md:10471-10501) runs Proposition 9.8's identity on the
  approximating g_n at every order, rotations included, uniformly in n, and passes to g_λ by Arzelà-Ascoli, so every ∂^α
  Ω^β u_1 is in E_2, u_1 := g_λ − g0 − r^(−3/2)G_3; g_app − g0 − r^(−3/2)G_3 is explicit with all its derivatives, so
  every derivative of e is in E_2, and r⁴ times the sources is C^∞ in the angles uniformly (E_2 E_2 ⊂ E_4, Lemma
  9.7(a)). Lemma 11.0's repair of D44 has not itself been read (10412-10416), its constants depend on λ and the order,
  and λ-uniformly the question stays open. What neither D508 nor this note addresses is the radial dependence: D508
  treats a source r⁻⁴σ(v, ω), while e's Cartesian derivatives gain no power of r, so r⁴ times the sources need not be
  smooth in ρ at fixed v, and the strip's term need not then be polyhomogeneous. That is the open item.]
  [D530, exact in the scalar model and deduced for the full operator; `checks/stripradial5.py` R1-R4: the strip's term
  inherits the sources' radial expansion at fixed v, and needs nothing else. The strip's sources sit at bounded v as r →
  ∞, so their radial dependence is their dependence on u = v − 2r → −∞, toward past null infinity. (i) The scalar model
  at every degree. For φ = r^(−p)F(s)Y_l, −½r^(p+2)□φ = (s − s²/2)F″ + (p − ½)(1 − s)F′ − ½(p² − 2p − l(l + 2))F (R1,
  exact, p and l symbolic), Gauss's equation in s/2 with (a, b, c) = (p + l, p − l − 2, p − ½). A sheet r^(−4−q)σδ(v −
  v_0), q ≥ 0, is the degree −(3 + q) problem: F(0+) = −σ/(2p − 3), the regular branch ₂F₁(a, b; c; s/2) (c = p − ½ > 0;
  the other exponent, 3/2 − p < 0, is excluded as in D487), so there is no logarithm at any p > 3/2, half-integers
  included (at p = 3/2 the two exponents meet and that branch carries one; only p ≥ 3 is used; corrected D535), and
  K_(p,l) := F(1) = −√π Γ(p − ½)/((2p − 3)Γ((p + l + 1)/2)Γ((p − l − 1)/2)) by Gauss's second summation theorem (R2, to
  4 × 10⁻³¹; strip5's C_l at p = 3; at half-integer p it vanishes at no l). strip5's scheme with r^(−4−q) on the strip
  gives r^(3+q)φ → K_(3+q,l) to 0.07 % for q = 0, ½, 1 and l = 0, 1 (R3). So if r⁴S = Σ_q ρ^q σ_q(v, ω) at fixed v, the
  strip's term is Σ_q ρ^(3+q) ∫ F_(3+q)(1 − vρ)σ_q(v) dv, by time translation as in D508: its exponents are 3 plus those
  of r⁴S, with no logarithm, and a remainder |r⁴S| ≤ Cρ^m contributes O(ρ^(3+m)) at l = 0, where the kernel is positive
  (D468; not tested by the script, supported by verifier 230's samples, 37 radial and strip sources all of one sign and
  ∫|K|r′⁻¹dr′ of order R⁻¹; D535). (ii) The full operator, deduced. Its principal part on flat space is −½□ ⊗ I (D502),
  so at degree −p M2 = (s − s²/2)I, and M1(0) depends on p only through ∂_r²: M1_p(0) = M1_2(0) + (p − 2)I, first-order
  terms B·∂ putting p into M0 alone (D487's P2, exact, is the step from p = 2 to 3; verifier 230 ran stripfull5's
  reductions in exact sympy at p = 3, 7/2, 4 and 9/2: M1_p(s) − M1_2(s) − (p − 2)(1 − s)I = 0 identically in both
  sectors, D535). M1_2(0)'s eigenvalues are 1.5, 1.5099, 1.51, 1.52 and the damping's (D492), so J_p := M1_p(0) − I has
  every eigenvalue at least p − 3/2 and the other exponent at N is negative at every p ≥ 3: no logarithm, and K_p = T_p
  J_p⁻¹ is finite in each harmonic. Its size and its uniformity in l are computed only at p = 3 (D487, D492, D496).
  (iii) So the open item is exactly the radial expansion of r⁴ times the sources at fixed v, that is, whether e and h
  are polyhomogeneous at past null infinity along the strip. The record's waves are incoming, with phase v/λ
  (N1STAR-PROOF.md:538, 1040), so their fast dependence is in v, which σ(v, ·) absorbs. What the record does not give is
  the dependence on u at fixed v. Lemma 11.0 commutes with ∂ and Ω only, and the derivative along the strip, ∂_u, gains
  no power of r (D464); neither r∂_u nor the scaling field is used there. [Corrected D540, verifier 233: the expansion
  is in the record for g_λ at each fixed λ. Proposition 11.1 (N1STAR-PROOF.md:10562-10592) gives u = g_λ − g0 =
  Σ_(k=3)^J r^(−k/2)G_k(v, x̂) + u_J with ℓ^m u_J ∈ E_((J+1)/2+m) for every m and J, by Lemma 11.2's induction
  (10516-10560), the sources starting at q = 3, so no r^(−5/2) and no logarithm. (Corrected D548, verifier 237: no
  source at q = 5/2, hence no logarithm; u's own r^(−5/2) term, G_5 = ∫S_(7/2) (10567), is generically nonzero.)] (iv)
  What it would cost (R4). A source oscillating in u at fixed v, r⁴S = cos(2r/λ), which E_2 does not exclude, gives on t
  = 0 no ρ³ term (|r³φ| < 0.05 on [300, 400] at λ = 10, against |K_(3,0)| = 0.785) and a ρ⁴ term ≈ √2 λρ⁴ sin(1/(λρ))
  (amplitude 1.39λ at λ = 10, 1.395λ with t = 0 exact; at λ = 30, 1.31λ on [200, 400] is not converged, 1.38λ on [400,
  800] and 1.40λ on [800, 1200]; √2λ is the leading term by parts in u; D535). As a function of ρ it is C¹ but not C²;
  the class test is stricter (corrected D535, verifier 230): ρ⁻² times it, ρ²sin(1/(λρ)), is differentiable but not C¹,
  its derivative carrying −λ⁻¹cos(1/(λρ)), and its t-derivative, −√2ρ⁴cos(1/(λρ)), is ρ³ times ρcos(1/(λρ)), not
  differentiable at 0: outside Lemma 0.1's ρ²C^m and ρ³C^m from m = 1. (Checked on the flat slice t = 0; the bend of
  Σ_IVP, D510, is not checked for this term.) Whether e has such a part along the strip is not decided; with incoming
  waves, it would come from backscatter or from the remainder's own construction. What remains: for g_λ nothing at fixed
  λ, which is all the strip needs (D521); for e = g_λ − g_app, the approximant's own expansion, and the products that
  form the sources (D536 as corrected by D540).]
  [D536, read and deduced: what the record has toward that expansion. The strip is section 9's far region P: v ∈
  [v_start, V_P] and r = t + O(1) (Lemma 9.1(d)), and at fixed (v, x̂) the radial derivative is ℓ = −L0 (ℓv = 0, ℓr = 1;
  N1STAR-PROOF.md:1190-1191). So ρ³C^m for the strip's term needs (r²ℓ)^j of r⁴ times the sources bounded for j ≤ m
  (D530 (i)-(ii)); on P, rℓ = S − (v − 1 − τ0)∂_v, S the scaling field, with the record's t = 1 + τ0 − τ, and v bounded
  (corrected D540: "S − v∂_v" held only for τ∂_τ + r∂_r). (i) One step is in the record: O_p (1197) asks of the
  remainder ℓf̃ ∈ E_(p+3/2), that is rℓf̃ ∈ E_(p+1/2), Lemma 9.7(d)'s transport solutions are in O_(q−1) (1209-1210),
  and Theorem A_P puts W_TT, χ and gh_(m+1) in O_p (1229-1230). (ii) What is not: m_m ∈ L_2 carries no condition on its
  remainder's ℓ-derivatives and φ_m one (ℓφ_m ∈ L_2); the residual Ric^H(g_app) is in E_3 only (1233). Lemma 11.0
  (10471-10501) runs its identity with Cartesian and rotation derivatives only, but section 11 goes on: Proposition 11.1
  (10562-10592) gives u = g_λ − g0 its full expansion in r^(−1/2) at fixed λ, every ℓ-gain included ((11.7); ℓu_1 ∈ E_3
  at 10577). [Corrected D540, verifier 233: D536 had missed section 11 and said u_1 had no ℓ-gain.] (iii) For g_λ the
  route is the record's own, Lemma 11.2's induction rather than a commutator. For e = g_λ − g_app, the approximant's
  m_m, φ_m and residual need the same expansion; Lemma 11.2 would give it to any part solving such an equation with an
  expanding source (not checked). A commutator route would have been: commute Lemma 11.0's identity on the approximating
  g_n with S, j times. [S, □] = −2□ on flat space, and on P the coefficients' S-derivatives stay in the coefficients'
  classes once the approximant's profiles and residual are in iterated O-classes, (rℓ)^i f̃ ∈ E_(p+1/2) for i ≤ j. Lemma
  9.7(d) gives these one transport at a time, but the record states j = 1, for the transported profiles only; m_m, φ_m
  and R_N need them too. (iv) Conormality is not enough: it puts the strip's term in ρ³ times a function with (ρ∂_ρ)^j
  bounded, which lies in ρ²C^(0,1) and not in ρ²C¹ (ρ³ sin(log ρ) is an example). Lemma 0.1's C^m needs an expansion of
  r⁴ times the sources at fixed v, i.e. of e at past null infinity along the strip, the sources being quadratic in e =
  g_λ − g_app, not in u_1 (corrected D540). For g_λ that expansion is Proposition 11.1, which integrates the ∂_v-part
  2∂_v(ℓ + 3/(2r)) of (9.5) from v_start (Lemma 11.2; it is the ∂_v-part, not the leading part at fixed v, verifier
  233). The q = 5/2 logarithm would multiply the leading order and so can only be excluded, not pushed up; the record's
  sources start at q = 3 and exclude it. The exponents are half-integers, so the class is D517's ρ^(1/2)-smooth
  extension of Lemma 0.1, not Part VII's integer one (corrected D540).]
  [D545, read and deduced: the approximant's parts. Theorem A_P (N1STAR-PROOF.md:1224-1309) builds each stage m on the
  strip as explicit leading terms, m^0 = r⁻²M_m(v, x̂, θ), φ^0 = −½r⁻¹M_m(ℓ, ℓ) and gh^0 from Lemma 9.7(d) at q = 3
  (1265-1267), plus remainders (m̃, φ̃, gh̃) that solve the stage system of Lemma 5.3 ((a) a wave equation −½□̃ m +
  B̄·dm + C̄m = …, (b) the transport L0 φ = −½m(ℓ, ℓ) − ½q, (c) the transport for gh) with every source in E_(7/2)
  (1268-1270), estimated by energy (9.7) into m̃ ∈ E_(5/2), φ̃ ∈ E_(3/2) with ℓφ̃ ∈ E_(5/2), gh̃ ∈ O_(5/2) (1296-1298).
  Proposition 11.1's induction would carry over stage by stage: Lemma 11.2 (10516-10560) for (a), its operator −½□̃ with
  g0 in place of g_λ and B̄·dm̃ + C̄m̃ put in its source S̃ (the coefficients being in E_2, 1253-1256, so these terms
  are in E_(q+1)); Lemma 9.7(d) for (b) and (c), each order's source expanded from the previous orders' (corrected D548:
  for (c) only; (b) is the c0 = 0 transport). The sources start at q = 3 (S_m = r⁻³S_(m,3) + E_(7/2), and r⁻³K_(m,3) for
  (c), 1263-1265), so neither lemma meets its q = 5/2 resonance, and each expansion is in r^(−1/2) with ℓ-gaining
  remainders (corrected D548: for (c), only once its coefficient c is expanded). With the stages so expanded, the
  residual R_N (a polynomial in the profiles, 1300-1304) and the products that form the strip's sources (quadratic in e
  = g_λ − g_app) inherit expansions, and the strip's term is polyhomogeneous in ρ^(1/2) (D530, D540), in D517's class.
  Not written: the induction itself on the coupled system, where (H_m) asks the couplings ⟨W_φ(dφ_m)⟩, ⟨Th gh_(m+1)⟩ and
  the coefficients B̄, C̄ for their ℓ-gains, which their explicit leading terms have and their remainders acquire stage
  by stage; the induction over the stages m ≤ N; and λ-uniformity, which the strip does not need (D521).]
  [D548, verifier 237 on D545 (2 major, 4 minor, 2 nits); read and deduced. (1) The φ-transport (b), L0φ_m = −½m_m(ℓ, ℓ)
  − ½q_m, has c0 = 0 (N1STAR-PROOF.md:1185), not Lemma 9.7(d)'s c0 = 3/2: on ℓφ = ½r⁻²M(ℓ, ℓ) Lemma 9.7(d)'s formula
  gives +r⁻¹M(ℓ, ℓ), the record's φ^0 is −½r⁻¹M(ℓ, ℓ) (1266). (b) expands by itself: its solution vanishing at past null
  infinity is φ = −∫_r^∞ S dr′, and a term r^(−k/2)S_k integrates to −r^(1−k/2)S_k/(k/2 − 1), resonant only at k = 2 (q
  = 1). Its sources start at q = 2 (m_m ∈ L_2, q_m ∈ L_3), and the r^(−5/2) term the gh-coupling gives m_m ((a)'s
  E_(3/2) coefficient of gh, 1255) is a q = 5/2 source here, so no logarithm. (2) Lemma 9.7(d) gives one leading term
  and a remainder in O_(q−1) (1209-1210, 1220-1221), not an expansion. Iterating it needs the transport's coefficient c
  (Lemma 5.2's operator, coefficients in E_(3/2)) expanded in r^(−1/2), which nothing in the record supplies; with c
  expanded the iteration steps q by ½ from q = 3 and never meets q = 5/2. So the expansion of gh, and with it of the
  residual and of the strip's sources, is conditional on c's, not "would carry over". (3) Ψ_m := □̃φ_m obeys a c0 = 2
  transport (525-526), resonant at q = 3, and φ^0 puts an r⁻³ term into its source. But Ψ_m = □̃φ_m holds (530), so
  Ψ_m's expansion is (9.5) applied to φ_m's term by term, □̃(r^(−p)F) = (3 − 2p)r^(−p−1)∂_vF + r^(−p−2)(p(p − 2)F + Δ̊F)
  − μp(p + 1)r^(−p−4)F, powers only; the transport is then satisfied, not solved, and its r⁻³ source coefficient is 0
  (r^(−2) is its homogeneous solution). No logarithm enters (c) through Ψ_m (deduced). (4) Not taken: verifier 237 read
  (11.5)'s −½g^(ab)∂_a∂_b as the principal part alone. In section 11's Cartesian coordinates it is (9.5)'s □̃ exactly at
  g_λ = g0 (g0⁻¹ = η⁻¹ − (μ/r²)ℓ ⊗ ℓ, ℓ straight, so ℓ^aℓ^b∂_a∂_b = ℓℓ), as 10529-10530 use it. (5) D517's class needs
  r⁴ times the strip's sources to start at r⁰ or later on the half-integer lattice (D530: r^(−(4+q)) gives ρ^(3+q)),
  D508's hypothesis, now stated. (6) Line 605's "no r^(−5/2)" was wrong; corrected there. Nits: B̄ and C̄ are defined
  only by (a) (516), their E_2 class read from the count (1237-1256); m̃ ∈ E_(5/2) holds for every J (1272-1275).
  Verified as D545 stated: the leading terms, the steps m = 0 and 1 of Lemma 11.2 for (a) on the stated classes, the
  sources starting at q = 3. Open: c's expansion; (H_m) at m ≥ 2 (the ℓ-gains of m̃, φ̃, gh̃); the induction over the
  stages.]
  [D551, read and deduced: (c)'s coefficient has an exact expansion, which settles D548's (2). Lemma 5.2's Th is section
  3.2's T at λ = 0 (N1STAR-PROOF.md:494, 260-266), T Y = −(ℓ_app · d_X)∂_θY − ½(g_app^(ab)∂_a∂_b v)∂_θY + B · (dv ⊗
  ∂_θY) + ½Y(ℓ, ℓ)∂_θ²g1 − ½n1∂_θ²Y. At λ = 0: ℓ_app = ℓ; g0^(ab)∂_a∂_b v = □̃v = 3/r by (9.5), which is Lemma 9.7(d)'s
  3/(2r); the ∂_θ² terms, with the phase's −(ℓ · dφ1)∂_θ²Y, are −½e_1∂_θ²Y = 0 (509-511; e_1 = 2ℓφ1 − m1(ℓ, ℓ) = 0 is
  (b) at m = 1), so m1 and φ1 drop out; B's coefficients are built from g_app and dg_app (254-258), whose λ⁰ parts are
  g0, dg0 and dv ⊗ ∂_θW (the derivative of λg1's oscillating part); and ∂_θ²g1 = ∂_θ²W at λ = 0. So c is algebraic in
  g0, Γ[g0], ∂_θW and ∂_θ²W, the same at every stage m ≥ 1. Both have exact finite expansions: g0 = η + (μ(v)/r²)dv dv
  and g0⁻¹ = η⁻¹ − (μ/r²)L0L0 (50), so its Cartesian components and Christoffel symbols are finite sums of r^(−p)F(v,
  x̂) (Γ[g0]'s μ′ part (μ′/(2r²))ℓ dv dv, 1238-1239); W_TT's Cartesian components are r^(−3/2)F exactly (P3, 1216;
  O_(3/2) with no remainder, 1229). Hence c = Σ_p r^(−p)c_p over finitely many p ≥ 3/2, and Lemma 9.7(d) iterates: Z^0 =
  −r^(1−q)S_q/(q − 5/2) has (ℓ + 3/(2r))Z^0 = r^(−q)S_q exactly, so Z − Z^0 solves the same transport with source S̃ −
  cZ^0, whose expansion starts at q + ½ and is known from S's and c's; the orders step by ½ from q = 3 and never meet
  5/2. (a)'s B̄ and C̄ and the coupling coefficients of the count (E_2, E_3, E_(3/2), E_(5/2); 1253-1256) are θ-means
  and products of the same g0 and W terms, so they are expanded too. Within a stage the half-order induction is
  triangular: at the source order q, m_m's term r^(1−q) comes first (every coupling in (a)'s source reaches m_m, φ_m,
  gh_(m+1) through a coefficient decaying by at least 3/2, so only terms found at orders ≤ q − ½), then φ_m's r^(2−q) by
  integrating (b), then gh_(m+1)'s r^(1−q) from (c) (its couplings again through coefficients in E_(3/2) or better, Ψ_m
  = □̃φ_m included). Still not written: that induction with its ℓ-gains ((H_m) at m ≥ 2), as Proposition 11.1's proof
  does for u, and over the stages.]
  [D555, verifier 240 on D551 (no break; 3 minor, 3 nits): verified Th = section 3.2's T at λ = 0 (N1STAR-PROOF.md:494,
  262-266), m1 and φ1 entering only through −½e_1∂_θ² = 0 (509-511, 517), B at λ⁰ built from g0, dg0 and dv ⊗ ∂_θW
  (257-258, 477), c Th's part and not Wm's or K_m's (494-496), □̃v = 3/r with Lemma 9.7(d)'s sign (1204, 1207-1209;
  checked numerically), g0's inverse exact (Sherman-Morrison, dv null), W_TT = r^(−3/2)F exactly (past5.py selftest,
  P3-P5), and Z^0 exact. Corrected: (1) "known from S's and c's" holds one step at a time: the record gives S̃ only as a
  class (E_(7/2), 1263-1266), so each further step needs the source's expansion at that order, which is the induction
  still to be written, and the ℓ-gains (H_m) (10525). (2) W is W_TT + χ dv dv (461), and χ is r⁻² times a function with
  no remainder (1258-1260; past5.py P5), so c is exact with χ as well. (3) The expansion is in the profile variables (θ
  = u/λ, no phase shift), where Lemma 5.3 (c) and Lemma 9.7(d) are posed; in section 9.4's fixed-phase variables (W_TT(·
  + φ1), 1302-1303, 1317-1319) c is exact only after φ1's expansion is inserted. (4) B̄ and C̄'s expansions are asserted
  as θ-means and products of g0 and W terms, not shown. Nits: the exponents p lie in ½ℤ, which "never meets 5/2" uses;
  dΓ[g0] enters too (72), and is exact; the record's Lemma 5.2 proof says "the λ⁻¹ part of the principal term on λY(X,
  u/λ)" (509) for formulas that are the [Y] coefficients of 262-263 (a wording slip in the record, recorded, not
  repaired). Established: c's expansion and one step of Lemma 9.7(d); the triangular structure at the level of the
  count.]
  [D559, deduced, at the level of the count, as Proposition 11.1's proof is written (N1STAR-PROOF.md:10576-10587): the
  stage system's expansion with its ℓ-gains, (H_m) included. Write E_p^ℓ for the profiles f with ℓ^j f ∈ E_(p+j) with
  all derivatives for every j. It contains every exact term r^(−p)F(v, x̂, θ) (ℓ(r^(−p)F) = −p r^(−p−1)F), is closed
  under products (Leibniz: E_p^ℓ E_q^ℓ ⊂ E_(p+q)^ℓ), under ∂_v, Ω and ∂_θ (which commute with ℓ and r), and under
  Cartesian derivatives (∂_X = x̂(∂_v + ℓ) + r⁻¹(angular), [ℓ, r⁻¹Ω] = −r⁻²Ω). Fix a stage i ≥ 1 and suppose the earlier
  stages' profiles expanded with every remainder in the E^ℓ class of its order (stage 0: W_TT and χ exact, P3, P5). The
  coefficients of (a)-(c) are exact (D551, D555), hence in E^ℓ. Induct on the number m of ℓ's, at a fixed expansion
  order (the order q of the remainders' sources, D545's half-order steps), in the order m̃, φ̃, gh̃. (a): Lemma 11.2
  with g0 for g_λ, so its (H_m) asks only ℓ^j S̃ ∈ E_(q+1/2+j) for j < m; S̃ is the earlier stages' remainder terms (in
  E^ℓ by hypothesis), the couplings ⟨Th gh̃⟩ (algebraic, coefficient in E_(3/2)) and ⟨Wm_φ(dφ̃)⟩ (coefficient in E_3),
  and B̄·dm̃ + C̄m̃ (coefficients in E_2), with ℓ^j of each needing gh̃ and φ̃ at j < m (found at step j) and, in
  B̄·dm̃, ℓ^(j+1)m̃ ≤ ℓ^m m̃, which at j = m − 1 is ℓ applied to ℓ^(m−1)m̃ ∈ E_(q−1/2+m−1) with all derivatives, so in
  E_(q+m−3/2), and B̄'s E_2 lifts the product to E_(q+m+1/2), above the E_(q+m−1/2) asked: the extra derivative is
  absorbed by the coefficient's decay. So (H_m) holds and Lemma 11.2 gives ℓ^m m̃. (b): ℓφ̃ = ½(m̃(ℓ, ℓ) + q̃), so
  ℓ^(m+1)φ̃ = ½ℓ^m(m̃(ℓ, ℓ) + q̃), with q̃ from earlier stages. (c): the transport (ℓ + 3/(2r) + c)Z = S gives ℓ^(m)Z =
  ℓ^(m−1)(S − (3/(2r))Z − cZ), whose terms need m̃ to ℓ^m, φ̃ to ℓ^(m+1) (Ψ̃ = □̃φ̃ carries two derivatives, ℓℓφ̃ among
  them) and Z to ℓ^(m−1): all found. So every remainder of stage i is in E^ℓ at every order, and the r^(−q) coefficients
  of the next order's sources are polynomials in the expanded terms, as in Proposition 11.1's last step; the stages
  follow in turn, each stage's sources being polynomials in earlier stages' profiles (10579-10586's argument). The
  profile variables pass to the physical ones at fixed v (D555 (3)) by Taylor's formula in θ with remainder (corrected
  D564: the full series need not converge for smooth profiles): Y(X, v/λ + δ) = Σ_(k<K) ∂_θ^kY(X, v/λ)δ^k/k! + O(|δ|^K)
  for each K, δ := φ_1 + … ∈ L_1 expanded, each power adding r⁻¹, the remainder in E_K with its ℓ-gains (ℓ(v/λ) = 0,
  ℓ^jδ ∈ E_(1+j)), as N1STAR-PROOF.md:538-540 writes it. So g_app has an expansion in r^(−1/2) at past null infinity at
  fixed λ with ℓ-gaining remainders, as g_λ has (Proposition 11.1), and so has e = g_λ − g_app; the strip's term is then
  polyhomogeneous in ρ^(1/2) (D530, D540, D548 (5)). Not written at proof level: this induction itself, line by line, as
  Proposition 11.1's proof is; and λ-uniformity, which the strip does not need (D521).]
  [D564, verifier 244 on D559 (no break of the ℓ-gain bookkeeping at the level of the count; 4 minor, 5 nits). Verified:
  E_p^ℓ's closure (Lemma 9.7(a), N1STAR-PROOF.md:1199-1200, 1212), Lemma 11.2 with g0 legitimate ((9.5) is the Cartesian
  principal part g0^(ab)∂_a∂_b, checked numerically to 2.6 × 10⁻¹⁵; the covariant box differs by −(μ/r³)ℓ), the
  exponents of (H_m) with one order to spare, the order m̃, φ̃, gh̃, and the transfer of Proposition 11.1's last step
  (each coupling lowers the source order by at least ½, so no cycle; no source at 5/2). Corrected: (1) the θ-Taylor
  formula, above; (2) the (H_m) step uses ℓ(E_p) ⊂ E_p, which Lemma 9.7(a) does not list but which holds as ℓ = x̂·∂_X −
  ∂_v (1212), the step where the term in m̃ itself closes; (3) D559 takes the coefficients' exactness from D551 and
  D555, and D555 (4) left B̄ and C̄'s expansions asserted, not shown: inherited; (4) the log's "closed" is "deduced at
  the level of the count, open at proof level". Nits: dφ̃ at ℓ^j needs ℓ^(j+1)φ̃, from (b) at step j; q̃ is q_m (1270);
  the record's [ℓ, 3/r] = 3/r² (10554) should be −3/r², class-neutral (a slip in the record, recorded); polyhomogeneity
  needs D548 (5)'s start condition, which holds as every derivative of e is in E_2 (Lemma 11.0, D521), so r⁴ times the
  quadratic sources starts at r⁰; and it follows only once e is expanded to every order at fixed v, which D559 supplies
  at the level of the count.]
  [D569, computed (`checks/bbar5.py` K0-K4 and Ctl, exact) and deduced: B̄ and C̄ shown (D555 (4), D564 (3)). By Lemma
  5.1's weights the terms of Rm^(m) linear in m_m pair it with factors of weight 0, which do not depend on m, so B̄ and
  C̄ are the same at every stage and are read off at stage 1 with φ_1 = 0: the λ¹ε¹ coefficient of Ric^H(g0 + λW + λεh)
  in lead5.py's gauge and coordinates, h a symmetric tensor of 15 arbitrary functions of all five coordinates, W = W_TT
  + χ dv dv with χ = r⁻²(k_a cos 2s + k_b sin 2s), a second harmonic (P5 allows any s-dependence, and lead5.py's L4
  leaves an s-independent zero mode free; with that mode the results are the same, verifier 249's mutant, D577). K0: the
  ε-linear part at λ⁰ is ½h_rr ∂_s²W, the record's −½e_1∂_θ²W with e_1 = −m_1(ℓ, ℓ) (5.2), and nothing else. K4: with
  the wave off, its principal part is −½g0^(ab)∂_a∂_b h_cd component by component, Lemma 5.3 (a)'s □̃. K1: the wave's
  contribution to the θ-mean carries no derivative of h, so B̄ = B0, built from g0 alone. K2: that contribution is
  quadratic in the wave, the means of the linear terms vanishing. K3: in an orthonormal frame, whose order is the
  Cartesian one, it is of order r⁻³, attained at nine entries (vv from h_θθ, h_φ1φ1, h_φ2φ2; vθ, vφ1, vφ2 from h_rθ,
  h_rφ1, h_rφ2; θθ, φ1φ1, φ2φ2 from h_rr), and χ contributes nothing, every quadratic χ term pairing dv with dv through
  g0⁻¹, which is null (χ is in the computation: K0's vv entry carries it). Ctl: the amplitude r^(−1/2) lowers K3's order
  to r⁻¹. So C̄ = C0 + ΔC with ΔC an exact finite sum of r^(−p)F(v, x̂), p ≥ 3; B0 and C0 are polynomials in g0's
  Cartesian components and their first two derivatives, and g0 − η = μ(v)r⁻² dv dv is exact, so they are exact sums with
  p ≥ 2 (deduced). B̄ and C̄ are therefore exact sums of r^(−p)F(v, x̂) with p ≥ 2, and such a term lies in E_p^ℓ
  (ℓ(r^(−p)F) = −p r^(−p−1)F), as D559's induction uses them: D564's (3) is discharged, the wave part by computation and
  B0, C0 by deduction (corrected D577, verifier 249: "in E_2, hence in E_2^ℓ" did not follow from E_2 alone). Not
  computed: the stage-m statement rests on Lemma 5.1's weight count, not on a run at m ≥ 2; the frame-to-Cartesian step
  is a change of basis with x̂-dependent, r-independent coefficients (deduced); and K1 carries over to Cartesian
  components because the wave part is of order zero as a tensor operator, which a change of coordinates keeps (D577).
  Notation: h_θθ above is the polar angle's component, the record's θ being the phase, s in bbar5.py.]
  [D578, deduced, written at the level of Proposition 11.1's proof (N1STAR-PROOF.md:10562-10588), from D559 with D564's
  corrections and D569's coefficients (with D577's). **Proposition B.4 (the stage profiles at past null infinity).**
  Write E_p^ℓ for the profiles f(X, θ) on the strip with d_X^α Ω^β ∂_θ^γ ℓ^j f ∈ E_(p+j) for all α, β, γ and j. For
  every stage i ≥ 1 and every J ≥ 4 there are smooth M_(i,k)(v, x̂), Γ_(i,k)(v, x̂, θ) (k = 4, …, J) and Φ_(i,k)(v, x̂)
  (k = 2, …, J − 2), bounded with all derivatives, vanishing for v ≤ v_start, T²×ℤ2×ℤ2-invariant, with m_i = Σ
  r^(−k/2)M_(i,k) + m_(i,J), gh_(i+1) = Σ r^(−k/2)Γ_(i,k) + gh_(i+1,J), φ_i = Σ r^(−k/2)Φ_(i,k) + φ_(i,J), the
  remainders in E_((J+1)/2)^ℓ, E_((J+1)/2)^ℓ and E_((J−1)/2)^ℓ; each coefficient is determined by the earlier ones, Γ
  and Φ algebraically and M by a v-integral of a polynomial in them and their derivatives (corrected D580, verifier
  252), with stage 0 exact (W_TT = r^(−3/2)F, χ = r⁻² times a function of (v, θ, s): past5.py P3, P5). *Proof.* (0) The
  class: E_p^ℓ contains every exact term r^(−p)F(v, x̂, θ) (ℓ(r^(−p)F) = −p r^(−p−1)F), is closed under products
  (Leibniz), under ∂_v, Ω and ∂_θ, under Cartesian derivatives (∂_X = x̂(∂_v + ℓ) + r⁻¹(angular), [ℓ, r⁻¹Ω] = −r⁻²Ω),
  and ℓ(E_p) ⊂ E_p, ℓ being x̂·∂_X − ∂_v (1212; D564 (2)). (1) The coefficients: (a)'s B̄ = B0 and C̄ = C0 + ΔC are
  exact and in E_2 (D569); (c)'s c is a finite sum Σ r^(−p)c_p, p ≥ 3/2, the same at every stage (D551, D555); the
  couplings ⟨Th gh⟩ and ⟨Wm_φ(dφ)⟩ have exact coefficients in E_(3/2) and E_3, and q_i is a polynomial in the earlier
  stages' profiles (486-487). All lie in E^ℓ of their orders by (0). (2) Induction on i, for fixed i on J, and in each
  step J → J + 1 on the number m of ℓ's. The hypothesis on stage i is at level 0 only: its profiles expanded to order J
  with remainders in E_((J+1)/2) (m̃, gh̃) and E_((J−1)/2) (φ̃), with all Cartesian derivatives, Ω and ∂_θ, which
  Theorem A_P gives at J = 4 (m̃ ∈ E_(5/2), φ̃ ∈ E_(3/2), gh̃ ∈ E_(5/2), 1263-1298; D545); the earlier stages are
  expanded to every order with remainders in E^ℓ. Put q := (J + 3)/2. Each step finds the next coefficients and the
  order-(J+1) remainders m̃′, φ̃′, gh̃′ at level 0 by (a)-(c), and then their ℓ-gains by induction on m in the order
  m̃′, φ̃′, gh̃′, each step using the earlier stages' E^ℓ, the explicit terms' gains by (0) and the gains of m̃′, φ̃′,
  gh̃′ found at lower m, or at the same m earlier in that order (D586, verifier 253); the order-J remainders, explicit
  terms plus these, are then in E^ℓ as well (corrected D580, verifier 252: the hypothesis had stage i's own remainders
  in E^ℓ at order J, which Theorem A_P does not give at J = 4). (a) The mean: Lemma 5.3 (a) reads −½g0^(ab)∂_a∂_b m̃ =
  r^(−q)S_q + S̃, where r^(−q)S_q collects the terms of order q, polynomials in the known coefficients, and S̃ the rest:
  B̄·dm̃ + C̄m̃ (E_2 · E_(q−1) ⊂ E_(q+1)), the couplings with φ̃, gh̃ and the products with a remainder factor, each in
  E_(q+1/2) with all derivatives. Lemma 11.2 applies with g0 for g_λ ((9.5) is the Cartesian principal part
  g0^(ab)∂_a∂_b, D564; the energy step is Lemma 9.5 with g̃ = g0, and (H_m)'s second clause is void, g0 − g0 = 0): m̃ =
  r^(1−q)M + m̃′, M = (2/(2q − 5))∫_(v_start)^v S_q, q ≥ 7/2 ≠ 5/2, and m̃′ ∈ E_(q−1/2) = E_((J+2)/2) with all
  derivatives, which is order J + 1. For its ℓ-gains (H_m) asks ℓ^j S̃ ∈ E_(q+1/2+j) for j < m: the couplings need ℓ^j
  gh̃ and ℓ^(j+1) φ̃ (dφ̃ at ℓ^j), found at step j by (b) and (c); B̄·dm̃ needs ℓ^(j+1)m̃, at j = m − 1 the ℓ of
  ℓ^(m−1)m̃′ ∈ E_(q−1/2+m−1) with all derivatives, in E_(q+m−3/2) by ℓ(E_p) ⊂ E_p, and B̄ ∈ E_2 lifts the product to
  E_(q+m+1/2), above the E_(q+m−1/2) asked; C̄m̃ and the products with remainder factors gain by the lower steps (stage
  i) and the hypothesis (earlier stages), the explicit factors by (0). So Lemma 11.2 gives ℓ^m m̃′ ∈ E_(q−1/2+m). (b)
  The phase: Lemma 5.3 (b) is ℓφ̃ = ½(m̃(ℓ, ℓ) + q̃) with c0 = 0 (1185; D548 (1)), solved from past null infinity as φ̃
  = −∫_r^∞ (½m̃(ℓ, ℓ) + ½q̃) dr′: a term r^(−k/2)S_k of the source ½(m̃(ℓ, ℓ) + q̃) gives −r^(1−k/2)S_k/(k/2 − 1),
  resonant only at k = 2, which the sources (from k = 4) never reach, and a remainder in E_p gives one in E_(p−1); and
  ℓ^(m+1)φ̃ = ½ℓ^m(m̃(ℓ, ℓ) + q̃), with q̃ from the earlier stages. Ψ̃ = □̃φ̃ is then (9.5) applied term by term, powers
  only (D548 (3)): its c0 = 2 transport is satisfied, not solved. (c) The oscillating part: the transport (ℓ + 3/(2r) +
  c)Z = S of Lemma 9.7(d), with Z^0 = −r^(1−q)S_q/(q − 5/2) solving (ℓ + 3/(2r))Z^0 = r^(−q)S_q exactly, so Z − Z^0
  solves the same transport with source S̃ − cZ^0, starting at q + ½ (D551); the orders step by ½ from q = 3 and never
  meet 5/2. Its ℓ-gains: ℓ^m Z = ℓ^(m−1)(S − (3/(2r))Z − cZ), whose terms need m̃ to ℓ^m, φ̃ to ℓ^(m+1) (Ψ̃ carries
  ℓℓφ̃) and Z to ℓ^(m−1), all found. (3) Each source coefficient S_q is a polynomial in the earlier coefficients and
  their derivatives, as in Proposition 11.1's last step (10583-10587), and the new coefficients are M = (2/(2q −
  5))∫S_q, and Φ and Γ algebraic in them, the invariance and the vanishing for v ≤ v_start being inherited by the
  integrals from v_start (and by the integral from past null infinity in (b), where every source vanishes for v ≤
  v_start). (4) The physical variables: g_app(X) = G(X, u/λ) with u = v + Σ_j λ^j φ_j (5.1), so Y(X, v/λ + δ) = Σ_(k<K)
  ∂_θ^kY(X, v/λ)δ^k/k! + O(|δ|^K) for each K, δ := Σ_j λ^(j−1)φ_j ∈ E_1^ℓ expanded by (b), each power of δ adding r⁻¹,
  the Taylor remainder in E_K with its ℓ-gains (ℓ(v/λ) = 0) (538-540; D564 (1)). So g_app, and e = g_λ − g_app with
  Proposition 11.1, has an expansion in r^(−1/2) at fixed λ with ℓ-gaining remainders, and the strip's term is
  polyhomogeneous in ρ^(1/2) (D530, D540, D548 (5)), the start condition holding as every derivative of e is in E_2
  (Lemma 11.0; D521). [] Asserted, not shown here (shown D587, below): E_p's closure under ∂_v (1199, beyond the
  derivatives 1194 displays), the couplings' coefficients exact (as B0 and C0 are, by deduction, D577), and the Taylor
  remainder's ℓ-gains (538-540 writes the remainder, not its gains). Not covered: λ-uniformity, which the strip does not
  need (D521). So 3(b)'s induction is written at the level of the record's own Proposition 11.1, given those three
  (corrected D580: "closes" said more).] [D587, deduced, with `checks/closure5.py` K1-K5 (exact; K4 an enumeration of
  every monomial of order m ≤ 10): the three closures shown. (i) ∂_v at fixed (r, x̂) is ∂_τ at fixed x, a Cartesian
  derivative, and commutes with every d_X, every Ω and ℓ (K2), so ∂_v E_p ⊂ E_p and ∂_v E_p^ℓ ⊂ E_p^ℓ: Lemma 9.7 (a)'s
  clause is shown, not only stated. (ii) A θ-mean of a monomial vanishes unless it holds two oscillating factors (with
  their derivatives), every oscillating profile having mean zero and every other factor (g0, m_i, dφ_i) being
  θ-independent. By Lemma 5.1's weight count (N1STAR-PROOF.md:490-497), the order-m monomials linear in gh_(m+1) with
  two oscillating factors are exactly W gh_(m+1) under two λ⁻¹dv∂_θ, and those carrying dφ_m are exactly W W under
  λ⁻¹dv∂_θ and dφ_m∂_θ (K4, the same at every m: what a monomial linear in gh_(m+1) can spend below m is −1 in all, two
  derivatives of weight at least −1 each and every other factor of weight at least 0). So ⟨Th gh⟩'s coefficients are
  polynomials in g0, g0⁻¹, dv, dd v and W, linear in W, and ⟨Wm_φ(dφ)⟩'s quadratic in W; no m_i or dφ_i enters either.
  g0 = η + μ(v)r⁻²dv ⊗ dv, its inverse η⁻¹ − μ(v)r⁻²V ⊗ V, dv and dd v are exact sums (K3), as W = W_TT + χdv² is (stage
  0); exact sums are closed under products, Cartesian derivatives, Ω, ∂_θ and θ-means (K1); so the coefficients are
  exact, of orders 3/2 and 3. (iii) Taylor's formula with integral remainder, R_K = δ^K/(K − 1)! ∫_0^1 (1 − s)^(K−1)
  ∂_θ^K Y(X, v/λ + sδ) ds. By the chain rule (K5) ℓ and Ω of a profile composed with Θ := v/λ + sδ fall on its
  X-argument or on δ and produce no λ⁻¹, since ℓv = Ωv = 0, while d_X produces λ⁻¹dv, bounded at fixed λ; so the
  composite of a profile in E_q^ℓ is in E_q^ℓ, the constants depending on λ and uniform in s ∈ [0, 1], δ^K ∈ E_K^ℓ by
  Leibniz, and R_K ∈ E_(K+q)^ℓ. So 3(b)'s induction is written at the level of the record's Proposition 11.1 with these
  three shown; λ-uniformity is not covered, and the strip does not need it (D521).]
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
