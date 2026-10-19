# N1*: what is proved, what is reduced, what is open (2026-10-19)

N1* (named at item 520; `lemmas/counterpart5.py` P5): for lam <= lam0 the vacuum solution with the record's data
exists on D_T = D cap {v <= v_end + T}, and its remainder after the geometric-optics approximant obeys energy
estimates uniform in lam, in a formulation that loses no derivatives, is regular across the T^2 axes and works on the
large background g0 (five-dimensional Vaidya with its black hole, inside to x = 1).

**Verdict: N1* is not proved.** Route W (the instructions' recommended route) was followed. Its exact pieces are
computed and seated (`ansatz5.py`, `foliation5.py`); the analytic core is audited against Touati's proof and stays
OPEN. Huneau and Luk's review (arXiv:2404.07659v1, April 2024; no later literature checked) lists the problem as open,
section 8.5, p. 28, READ
2026-10-19: "The only construction that we have which allows for large data is in the angularly regular setting of
Section 2. In particular, the constructions discussed in Sections 5, 6 and 7.2 all used that the solutions are close
to Minkowski." and "Problem 8.6. Construct local high-frequency solutions as in Sections 5, 6 and 7.2 but such that
the limiting solution is far away from Minkowski spacetime." No response paper is written (instructions sections 7
and 9).

Labels: computed (an instrument here, with selftest and mutants), READ (verbatim at source, 2026-10-19), deduced
(a standard argument, stated with its basis), OPEN.

## 1. What this session computed

- **A1** Touati's weak polarized null identities (3.17), (3.18) hold in 4+1 dimensions for general symmetric T, S; with
  Pol(T) = 0, Q(T,T) = E(T,T) du du and E(T,T) = -1/2 |T_AB|^2 over the three transverse directions. Evidence:
  `ansatz5.py` A1.
- **A2** 5D Vaidya: Ric(g0) = F0^2 dv dv, F0^2 = 3 mu'/(2 r^3); v eikonal; L0 = -d_r null geodesic; box v = 3/r.
  Evidence: `ansatz5.py` A2.
- **A3** The record's first-order wave is Touati-polarized (traceless, transverse), transported as r^(-3/2) by (2.29);
  the linear axis-matching conditions hold at both axes (necessary for smoothness, not a proof of it). Evidence:
  `ansatz5.py` A3.
- **A4** The ansatz to order lam^2: R^(-1) = 0; R^(0) = 0 exactly when mu' = (2/9) A^2 env^2 (F3's dust identity, now
  from the wave-type ansatz: the 4+1 analogue of Touati's energy condition (2.28), derived here as the R^(0) = 0
  condition mu' = (2/9) A^2 env^2 H^2 (c^4 + s^4), averaged over the two quadratures)
  and g2 carries two explicit, axis-regular polarization terms. Evidence: `ansatz5.py` A4.
- **A5** R^(1)'s structure: tangential components first harmonics only (the transport of g2's
  transverse-traceless part, Touati's (5.2)); one non-oscillating
  term, new: R^(1)_v th = F0^2 d_th phi with phi = (1/2) arctan(cos 2th), the averaged dust tilted at O(lam) toward
  grad(v + lam phi); zero for Touati's single-cosine ansatz; zero angular mean on S^3. Evidence: `ansatz5.py` A5.
- **B1** For mu >= 0 the slices tau = v - r are spacelike everywhere (g0^-1(dtau, dtau) = -1 - mu/r^2), L0(tau) = 1:
  Touati's
  (5.48) without smallness. Evidence: `foliation5.py` B1.
- **B2** Touati's background null frame on Vaidya, explicit; the leaves are round 3-spheres (no planar condition (2.10)
  needed). Evidence: `foliation5.py` B2.
- **B3** The structure of Touati's Lemma 3.1, exactly: for the principal part box~ = g0^{mn} d_m d_n,
  [L0, box~] u = (2/r)(d_r(L0 u) + 2 d_v(L0 u) + box~ u), the mass dropping out; for the covariant wave operator of g0
  (Touati's operator, equal to box~ only under his wave condition (2.7), which these coordinates do not satisfy)
  [L0, box_g0] u = (2/r)(d_r(L0 u) + 2 d_v(L0 u) + box_g0 u) - (3/r^2) d_v u - (3/r^2 + mu/r^4) d_r u, a first-order
  remainder within the ||d u|| term of (3.32). Evidence: `foliation5.py` B3.
- **B4** On D_T cap {tau >= tau0}, r_q(mu0) <= r <= V - tau0 (Z3, mu nondecreasing, mu0 > 0), and the slices'
  induced metric is bounded there. Evidence: `foliation5.py` B4. Deduced from it and `lemmas/hf_theorem5.py` F2: the
  region is compact, bounded by a spacelike past slice, a null and a spacelike future boundary.

A5 is the one structural difference this session found between the record's problem and Touati's: the record's
data need both polarizations a quarter turn apart for a round average (F3), and with both, the order-lam Ricci has a
non-oscillating meridional term. Deduced (not computed): no oscillating corrector absorbs it, since an oscillating
term of g2 or g3 enters the mean of R^(1) only through its products with g1, which are fixed once g1 and the
polarization of g2's first harmonic are. Closing the hierarchy at order lam therefore
needs a mean O(lam) metric correction lam m1, solving the linearized equations on Vaidya with that source, which
Touati's ansatz never needs. Its zero angular mean is consistent with the record's runs (F4: the mean mass converges at
O(lam^2), the horizon at O(lam)).

## 2. Prior art, READ at source

- Huneau and Luk, Duke Math. J. 167(18) (2018) 3315-3402, **arXiv:1706.09501** (the instructions' arXiv:1706.09499 is
  their companion elliptic-gauge paper, Comm. Math. Phys. 361 (2018) 873-949; N1STAR-LOG D2). Theorem 4.2: "Let
  k >= 10, -1/2 < delta < 0, R > 0 and A be a finite set. Given an admissible free initial data set ... such that
  |grad u_A| > 1/2; u_A is angularly separated; (Smallness condition) ... <= eps; (Genericity condition on initial
  data) ... Then, there exists eps0 > 0 such that if eps < eps0, a unique solution (g0, phi0, (F0)_A, (u0)_A) to
  (1.4) ... exists on a time interval [0, 1], and there exists a one-parameter family of solutions (g_lam, phi_lam)
  to (1.3) for lam in (0, lam0) ... such that (g_lam, phi_lam) -> (g0, phi0) uniformly on compact sets and
  (dg_lam, dphi_lam) -> (dg0, dphi0) weakly in L^2". Setting: polarized U(1) on I x R^3, reduced to 2+1 Einstein-scalar
  on I x R^2, elliptic gauge (maximal slices, conformally flat), small data, [0, 1].
- Touati, Commun. Math. Phys. 402 (2023) 3109-3200, arXiv:2206.12318: Theorem 2.2, under (2.9) "||g0 - m|| ... <= eps"
  and (2.10) "||grad u0 - z|| ... <= eps": "There exists lam0 > 0 and eps0 = eps0(delta, R) > 0 such that if
  0 < eps <= eps0, there exists for all lam in (0, lam0] a solution g_lam of the form g_lam = g0 + lam g(1)(u0/lam)
  + lam^2 g(2)(u0/lam) + lam^2 h~_lam, (2.25) to (1.1) on [0, 1] x R^3 in generalised wave gauge." The derivative loss
  (section 3.2.2: "Performing energy estimates on (3.28) implies schematically that dF ~ dh while the energy estimate
  for (3.29) gives dh ~ d^2 F. Therefore, there is an a priori loss of one derivative") and its cure (3.2.3: the
  commutator Lemma 3.1 and the Fourier cut-off; Remark 3.5: "It actually replaces the loss of one derivative by the
  loss of one power of lam ... A careful bootstrap argument is still required to regain this power of lam").
- Touati, arXiv:2402.17530v2 (journal reference not read here): Theorem 1.3 under (1.15), "We assume that the metric
  g0 is close to Minkowski".
- Luk and Rodnianski, arXiv:2009.08968: Theorem 1.9 (from their Camb. J. Math. 5(4) 2017 paper): existence on
  [0, u*] x [0, ub*] x S^2 for ub* in (0, eps] with "eps > 0 sufficiently small depending only on C" -- large data,
  angularly regular, local in one null direction; 3+1.
- Huneau and Luk, arXiv:2404.07659: section 8.5, Problem 8.6 (quoted above).

None treats 4+1 dimensions, a background far from Minkowski, fixed points of the symmetry, or a domain reaching
inside a black hole.

## 3. The audit: where Touati's proof uses smallness, and what replaces it on D_T

Touati's eps measures the background's distance from Minkowski and the waves' amplitude together. The sites found
(READ, arXiv:2206.12318v4, in the text as retrieved 2026-10-19):

- **1. (2.9)-(2.11).** Use: background near Minkowski; grad u0 near a constant, no critical points. On D_T: dv
  restricted to Sigma_tau is dr, nonzero on r > 0; leaves compact (B1, B2). Status: computed.
- **2. (5.48).** Use: "Taking eps small enough ... ensures that |1/L^t_0| + |L0| + |dL0| <= C(C0)". On D_T: L0^tau = 1,
  L0 = -d_r exactly (B1). Status: computed.
- **3. (5.52).** Use: energy equivalence. On D_T: spacelike slices with induced metric (1 + mu/r^2) dr^2 + r^2 dOmega^2
  on a compact region (B1, B4). Status: deduced.
- **4. Theorem 6.1 (p. 39).** Use: background transport system solvable "if eps is small enough". On D_T: transport
  along -d_r
  on explicit smooth Vaidya; g1 solved exactly (A3); g2's polarization terms explicit (A4). Status: computed (to order
  lam^0).
- **4'. --.** Use: (no counterpart in Touati). On D_T: the mean O(lam) correction m1 (A5). Status: OPEN.
- **5. Prop. 7.1, (7.9)-(7.11).** Use: the coupling L0 F = Pi<=(h) F(1) with ||F(1)|| ~ eps gives A3 eps^2 << A1 eps.
  On D_T: on a slab of lam-independent length delta the coupling enters as delta C A3, a time integral. Status: deduced
  sketch, OPEN.
- **6. Lemmas 7.3, 7.7, 7.8 (pp. 45-49).** Use: "A1 eps + A3 eps^2 / lam^r"; "Since we can assume lam <= eps" (proof
  of Lemma 7.8, p. 49; the verifier could not retrieve it through its route; it is in the text read here). On D_T:
  these feed
  the transport estimate (7.22) for box_g0 F, a time integral; lam <= eps becomes lam <= 1. Status: deduced sketch,
  OPEN.
- **7. Prop. 7.3, (7.45).** Use: fixed-time products, e.g. "lam^2 ||grad^4 h|| ||d^2 F||_Loo ... <~ A1 A3 eps^2 /
  lam^4". On D_T: **the crux**: with eps ~ 1 this is A1 A3 at the BA2 level, not small and not under a time integral;
  see below. Status: OPEN.
- **8. Prop. 7.5, (7.47).** Use: e^(1 + C(A_i) eps). On D_T: e^(C(A_i) delta) on a slab. Status: deduced sketch, OPEN.
- **9. section 7.6.** Use: "eps and lam small enough compared to 1 (but with eps still independent from lam)". On D_T:
  slabs of fixed length, constants growing per slab, lam0 chosen last. Status: OPEN.
- **10. Theorem 2.1 ([Tou23b]: Comm. Math. Phys. 402(1) (2023) 97-140, as arXiv:2404.07659 ref. [122] prints it).**
  Use: constraint data "if 0 < eps <= eps0". On D_T: data on Sigma_tau0 with tau0 very negative lie where the shell is
  far out: the waves' strength A r^(-3/2) and mu/r^2 are small there, so a smallness parameter exists for the data
  problem; a 4D version of [Tou23b], and the scattering from past null infinity to Sigma_tau0 that makes the data equal
  to the record's, are not done. Status: OPEN.
- **11. section 8.** Use: propagation of polarization and gauge by the contracted Bianchi identities. On D_T:
  dimension-independent argument. Status: deduced (not checked line by line), OPEN.
- **12. Appendix C.** Use: the Fourier cut-off on R^3. On D_T: D_T has a spacelike inner boundary; the nonlocal cut-off
  must be localized. Status: OPEN.
- **13. section 3.2.4.** Use: "This shows why K >= 2 is necessary" (H^2 in L^oo in three space dimensions). On D_T: in
  four space dimensions H^2 is not in L^oo; T^2-invariant functions on {r > 0} live on quotients of dimension <= 3 near
  the axes, so H^2 in L^oo for them. Status: deduced.

**The crux (item 7).** The natural replacement of eps is a slab argument: bootstrap on slabs of a length delta fixed
by the background alone, with constants growing by a fixed factor per slab, and lam0 chosen after the last slab.
Every term that sits under a time integral (items 5, 6, 8) is then multiplied by delta. The argument closes on a
lam-independent domain only if the reduced problem for (F, h) is linear up to terms carrying a positive power of lam;
otherwise a quadratic fixed-time term can make the constants grow doubly exponentially from slab to slab, the slab
lengths shrink with them, and their sum need not reach T. Touati's (7.45) as printed is <~ A1 A3 eps^2 / lam^4; at
the weight lam^4 of (7.39) (p. 50) that is lam^0, harmless only because eps is small. A Gagliardo-Nirenberg
refinement of the L^oo factor (in three space
dimensions ||u||_Loo <~ ||u||_L2^(1/4) ||u||_H2^(3/4); here the T^2 quotient) gains lam^(1/2) for that term; the
arithmetic is checked, its validity on the 4+1 T^2-quotient (dimension,
weights, measure) is not yet established, so the gain is conditional. Whether
every fixed-time product in sections 7.2-7.5 gains a positive power of lam is the precise analytic statement left,
together with items 4', 10, 11 and 12.

## 4. What is left, by size

1. The 4+1, large-background version of Touati's sections 5-8 on D_T with slabs (items 5-9, 11, 12, 13), including the
   term-by-term lam-gain of item 7: the size of [Tou23a].
2. The data (item 10): a 4D, weak-field version of [Tou23b] on Sigma_tau0, and the scattering from past null infinity
   that identifies it with the record's run data.
3. The order-lam hierarchy for two-quadrature data (item 4'): g2's transported parts, g3's polarization, and the mean
   correction m1 of A5, whose solvability is expected from the contracted Bianchi identity and is not shown.

Until these are done THM-HF5's part (i) and the rates of (ii)-(iii) stay OPEN; part (iv) and the limit stay as
`lemmas/hf_theorem5.py` proves them. The application at physical wavelengths (10 l5) and the settling for all later v
(the nonlinear stability of five-dimensional Tangherlini in the class) are outside N1*, as the instructions say.

## 5. What a response paper would say, when there is a theorem to report

Carried over from Huneau and Luk: the reduction to 2+1 gravity with scalars whose target form is flat and positive
definite (`lemmas/kn_gauge.py` K1-K2: two scalars here, one there); the weak polarized null structure (A1, now in 4+1).
Changed: one more dimension; the T^2-mirror class with its axes (regular in 5D coordinates; A3, A4); a large
black-hole background instead of small data (B1-B4 remove the geometric uses of smallness; item 7 is what remains);
data at past null infinity; the interior to a spacelike boundary (F2, B4); and, new here, the O(lam) mean tilt of the
averaged waves (A5), which single-polarization constructions never meet.

