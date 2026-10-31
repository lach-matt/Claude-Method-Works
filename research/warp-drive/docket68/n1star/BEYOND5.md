# BEYOND5 -- the solution beyond D_T and Ω: the black-hole interior after the shell, up to the curvature boundary

Status: written (D360); read by verifier 167 (D362), findings seated; r_0 census and Proposition 6.2 added (D363).
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
  - **The census (D363; `checks/r0census5.py`, `BEYOND5-R0.tsv`).** 308 lines of Parts III-VII in 25 files name
    r_0, the inner radius or boundary, ½R_1, r_♯, ⅝R_1 or ¾R_1. Each is classed at its line, by reading, not by proof:
    - 108 are another r_0 (OTHER): III.C′'s exterior radius "r_0 large" (C2-POLYHOM, C3-BOOSTDATA, IV-EB,
      IV3-NM, IV4-SLAB; III.K says so at 134-135), the source's r_0 = r_c (IV5-CDMODES, IV6-SOLV), and r_A at A = 0
      (III.B 102, 117);
    - 19 are the definition and the domain (DEF): III.B 49-79, 177-178 and 224-251 ((2.1), (3.6), Lemma 3.7);
      III.K 43-44; Part VII 40, 195, 258;
    - 128 use only that {r = r_0} is spacelike with dr future timelike, inside the horizon (SPC): the artificial
      boundary, vanishing inside the horizon (III.E), the radial ODEs on (r_0 − δ_0, ∞) (D-GAUGEPOT, F3-MODES,
      F4-ZERO). IV6-SOLV's own finding (IV′′′′′5) says its uses of r_♯ = r_0 need only "the future timelike
      character of dr on [r_♯, r̂]";
    - 48 go through a constant chosen from it (CON): δ_0 of I.A's radii (VI-DYN to VI3-TRAPPING),
      ν_0 = min(¼, r_0/8) and R_ν (III.K), δ_1 and the weights (H2-ADMISS), δ′_0 (Part VII Lemma 1.2);
    - 5 put the value ½R_1 into an inequality (VAL). III.B 157-159: ‖A‖ < ε_param R_1 with
      |x|² ≥ ¼R_1² > 2‖A‖². III.B 244: ψ(2R_1) = 2R_1 − r_0 ≥ 3/2 R_1. VI3-TRAPPING 374: r_0 − δ_0 < ⅝R_1.

**Proposition 6.2 (deduced from the census, D363).** Let r_♭ ∈ (0, ½R_1] and replace III.B's r_0 by r_♭ and its
ε_param by min(1/10, r_♭/(4R_1)). Then every one of the 200 uses of the inner radius (DEF, SPC, CON, VAL) holds with
r_♭, the constants then depending on r_♭. So with r_♭ := ½ min(R_1, r_q(μ_end)), Proposition 6.1's conclusion holds
for every μ_end, without (1.1).

*Proof (from the census).*
- **The three VAL sites hold at r_♭.**
  - III.B 157-159: for |x| ≥ ½r_♭ (IV6-SOLV extends to {r ≥ ½r_♯}), |x|² ≥ ¼r_♭² > r_♭²/8 > 2‖A‖² and
    r_A² ≥ |x|² − ‖A‖² > 0, so Lemma 3.3 (c)'s condition holds.
  - III.B 243-244: ψ(2R_1) = 2R_1 − r_♭ ≥ 3/2 R_1 and ψ′ ≥ −1 on [2R_1, 3R_1], so ψ ≥ ½R_1 > 0 there as before.
  - VI3-TRAPPING 374: r_♭ + (r_h − r_♭)/8 < ⅝R_1 ⇔ 7r_♭ + r_h < 5R_1, which holds as r_h < √(3/2) R_1 (III.B 160)
    and 7r_♭ ≤ 7/2 R_1.
- **SPC.** For Tangherlini, g^(−1)(dr, dr) = 1 − μ/r² < 0 on 0 < r < r_h, and the radial systems' coefficients are
  smooth on (0, ∞), r_h aside (III.D 417; F3-MODES 204-212). For b near b_0 this persists on the compact
  {½r_♭ ≤ r ≤ ¾R_1} on shrinking the neighbourhood. So dr is future timelike there, as IV6-SOLV Lemma 0.3 (c) needs.
- **CON.** Each constant is then chosen from r_♭. For Part VII Lemma 1.2, take δ′_0 ∈ (q_0 − ½r_♭, q_0), which the
  lemma allows (δ′_0 ∈ (0, q_0)).
- **DEF.** The definitions and domains read with r_♭ for r_0, as the three VAL sites allow.
- So Theorem 0.2 (i) holds on {r ≥ r_♭} ⊃ {r ≥ r_q}, with λ_1, ε_m and ε depending on r_♭, so on μ_end. ∎

What this rests on: the census is a reading at 308 lines, not a re-proof of each Part. A use that names the inner
radius by none of the seven strings would be missed. [Hin26a] Proposition 5.1's conditions at m are taken from
IV6-SOLV's finding (IV′′′′′5), not read at source here. Part VII's record domain Ω′ reaches r ≥ a′ = q_0 − δ′_0,
below the record's q_0; with r_♭ it must reach further, through δ′_0 alone. The region r_♭ ≤ r < r_q, covered too,
lies beyond the curvature boundary, where the paper's premise has the classical description stop.

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
