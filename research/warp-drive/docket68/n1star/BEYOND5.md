# BEYOND5 -- the solution beyond D_T and Ω: the black-hole interior after the shell, up to the curvature boundary

Status: written (D360); read by verifier 167 (D362), findings seated. Labels as marked; nothing here is computed.

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

**Proposition 6.1 (deduced).** Let r_q := (√72 μ_end l5²)^(1/4) be the curvature boundary after the shell, a radius in
the background's coordinates. If

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
seed, and (1.1) holds with a margin of about 18 l5² (verifier 167's B2).

## 2. Whose continuation it is

g is the development of the glued data (γ_λ, k_λ). These equal g_λ's data on Σ_IVP ∩ {r ≤ R} and exact Tangherlini
data beyond 4R. Two facts follow.

- *On the domain of dependence of Σ_IVP ∩ {r < R}* g and g_λ agree up to a diffeomorphism. They are vacuum
  developments of the same data, so this is local geometric uniqueness on a domain of dependence (standard; not read at
  source here). Part VII's Remark 4.1 records this as finding (VII4), "not written". With it the two give one vacuum
  spacetime: g_λ on Ω' to the past of Σ_IVP ∩ {r < R} and on that set's domain of dependence, and g to the future of
  Σ_IVP in {r ≥ r_0}. Elsewhere in Ω' they need not agree, because on R < r < 4R the glued data differ from g_λ's.
  This still covers the hole's interior after the time T.
- *At late times near the hole* that domain of dependence does not reach (finding (VII1): "K^+ at late times is not
  in the domain of dependence of any bounded part of the slice"). So the interior covered by Proposition 6.1 belongs to
  *a* vacuum continuation of g_λ, fixed by the gluing. It is not *the* continuation of the record's data, because
  the record's g_λ is constructed on the compact Ω' only.

## 3. What remains

- **(a) Write (VII4).** The change of gauge on a compact region identifying the two developments on their common
  domain of dependence. This is standard and only needs writing out.
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
- **(d) The slab, if (c) fails somewhere.** The region r_q ≤ r ≤ r_0 after Σ_IVP is a slab of finite r-time: inside
  the hole r is a time function, and every point's causal past meets {r = r_0} in a set of bounded t-extent. Points
  whose causal past meets r = r_0 before Σ_IVP also need g_λ and (a). Alternatively, restrict the slab to
  D⁺({r = r_0} ∩ {t_IVP ≥ 0}).
  - Data on {r = r_0} are small and decay in t_* (Theorem 0.2 (i), (0.2)).
  - The background is t-translation invariant on the slab.
  - Cauchy stability with constants uniform in t then extends g across the slab for λ small. Writing this out is the
    alternative to (c).

## 4. Sources

proof5/PART-VII-ASSEMBLY.md: Theorem 0.2, (0.2), Remark 4.1, findings (VII1), (VII4). proof5/PART-III-B-FAMILY.md:49-55
(r_0, M). proof5/PART-III-K-NONLINEAR.md:21-30, 96-110 (Ω_*, 𝒟, N). RESPONSE-HL-5D.md sections 2.3, 8.7, 8.8, 9.
