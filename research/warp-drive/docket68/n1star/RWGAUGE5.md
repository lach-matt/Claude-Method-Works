# RWGAUGE5: the Regge-Wheeler-type gauge uniformly in r

*Status.* Written (this note, workstream G). Not verified by a second reader. Labels as in the supplement:
*proved* (the argument is complete here, given the statements it cites), *computed* (`checks/rwgauge5u.py` with
`checks/rwgauge5u.out`, exact, each check with a control that mutates the code under test and must fail), *READ*
(verbatim, with identifier and page, read at source on 2026-11-06 through the alphaXiv reader). The program is not
`checks/rwgauge5.py`: that name belongs to GAUGEDECAY5.md section 1's program, which this note does not touch.

*The item.* The paper (RESPONSE-HL-5D.md section 8.2) and the supplement (Proposition 10.1 (iv)) state that in the
gauge f_a = 0 = H_T of [KI03], with the l = 0 gauge fixed to the mass change, every metric component settles to a
change of mass at [HKW18]'s rate on each region r <= R, uniformly in l with a constant growing as a power of R, and
"uniformly in r it is not shown". This note decides the uniform statement.

*The decision: outcome (b), with the sharp weighted statement.*
- **Uniformly in r it is false** for the scalar type's orbit-space components. In the frame of the static observers,
  for every leaf Sigma_tau1 of [HKW18]'s decay foliation there is a single-mode perturbation of the class, with finite
  [HKW18] data of every order, whose component h(e0, e0) is exactly B r^(1/2) f^-1 S on the outgoing part of that
  leaf (Theorem 1: proved, the identities computed). So no bound sup_{Sigma_tau}|h(e_a, e_b)| <= C(tau) D^(1/2) holds
  for any tau, nor the same with the L^2 norm of r^-1 h(e_a, e_b) along the leaf.
- **The angular components and the tensor type settle uniformly in r**, and the orbit-space components do with the
  weight r^(-1/2), which is the exact growth: r^(-1/2)|h(e_a, e_b)| + r^(1/2)|h(e_i, e_j)| <= C delta^(-1/2) D^(1/2)
  tau^(delta - 1/2) on every leaf, uniformly in r >= R_1 and in l; with one more power, r^-1 |h(e_a, e_b)| + |h(e_i,
  e_j)| <= C D^(1/2) tau^-1; and the squared L^2 norm along the leaf of r^(-3/2) h(e_a, e_b) and r^(-1/2) h(e_i, e_j)
  decays at [HKW18]'s rate tau^-2 (Theorem 2: proved from [HKW18]'s Theorems 2, 16 and 18 READ, applied as stated;
  every coefficient and exponent computed). D is [HKW18]'s data norm for the master field commuted with at most two of T
  and the rotations. The exponents 1/2 and -1/2 of the weights are attained (Theorem 1), so they cannot be improved.
  [R2.0 M1: Theorem 2 (b)-(c) bound the L^2(S^3) norm at fixed (tau, r); the pointwise |.| written here is Theorem 2'
  (R2.0.1), with D' (two more rotations) in place of D. R2.0 M2: "the squared L^2 norm along the leaf" is the
  integral against dr dsigma, dsigma the unit sphere's measure, which is Theorem 2 (a); against the leaf's own volume
  form it is false (R2.0.2).]

The rest of this note is: 1. what is READ; 2. the components on the outgoing chart (Lemma 1); 3. Theorem 1; 4.
Theorem 2; 5. remarks (the region r <= R_1 and a reading of [HKW18]'s energies); 6. the replacement text; 7. files.

## 1. What is READ

[HKW18] P.-K. Hung, J. Keller and M.-T. Wang, arXiv:1809.05144v1 (read 2026-11-06).

- (R1) [R2.0 m8: the p. 67 quote below is corrected in place to the source's wording.] The decay estimate, p. 4,
  Theorem 2: "With further specification of an initial data slice Σ_0 and a decay
  foliation Σ_τ := φ_τ(Σ_0) formed by flowing along the static Killing vector field, a symmetric traceless two-tensor
  Ψ solving any one of the equations (134, 149, 153, 174) satisfies the uniform boundedness estimate Ě^N_Ψ(Σ_τ) ≤
  C(n, M) Ě^N_Ψ(Σ_0), (6) and, in spacetime dimension six and below, the uniform decay estimate Ě^N_Ψ(Σ_τ) ≤ C(n, M)
  I_Ψ(Σ_0)/τ^2, (7)". The same estimate for the summed scalar quantity, (186), p. 69; the uniformity in l, p. 67: "The
  estimates for the Q^(+)_{ℓm_s(n,ℓ),αβ} in the previous subsection are uniform in the angular mode numbers ℓ and m,
  owing to convergence of the potentials V^(+)_ℓ to the limiting potential V^(+) (178)."
- (R2) Pointwise bounds are not proved there, p. 4 (and again p. 69): "We remark that further pointwise uniform
  boundedness and uniform decay estimates can be derived from those above by means of commutation with the angular
  Killing fields and application of Sobolev estimates on the orbit spheres."
- (R3) The foliation, p. 30, section 7.3: "Σ_0 ∩ {R_1 ≤ r} = {u = −½(R_1)_*} ∩ {R_1 ≤ r}", with u = ½(t − r_*), v =
  ½(t + r_*) ((13), p. 5), and "L := ∂/∂v = ∂/∂t + ∂/∂r_*" ((92), p. 30); "We define n_Στ as the unit timelike normal
  vector for Σ_τ for r ≤ R_1 and n_Στ := L for r > R_1." So the part of Σ_τ in r >= R_1 is one outgoing null cone.
- (R4) The energies, p. 39: "We define the strictly timelike red-shift multiplier N := T + Y, in addition to the
  current J^N_a[Ψ] := T_ab[Ψ]T^b + Ť_ab[Ψ]Y^b, (114) and energies E^N_Ψ(Σ_τ) := ∫_Στ J^N_a[Ψ] n^a_Στ dVol_Στ, Ě^N_Ψ(Σ_τ)
  := ∫_Στ Ť_ab[Ψ] n^a_Στ N^b dVol_Στ. (115)"; "We extend Y to the exterior region such that Y is causal and Y = 0 for
  r ≥ r_1" (p. 39); the virtual stress tensor, p. 29: "Ť_ab[Ψ] := ∇_aΨ · ∇_bΨ − ½ g_ab (∇_cΨ · ∇^cΨ). (89)".
- (R5) The r^p hierarchy, p. 43, "Φ := r^(n/2) Ψ (124)", and p. 46: "E^p_Ψ(Σ_τ) := ∫_{Στ∩{r≥R_1}} r^(p−n) (1 − μ)^k
  |∇_L Φ|^2 (1 − μ) r^n dv dVol_S^n" (127), and Theorem 16: "For 1 ≤ p ≤ 2 and τ_1 < τ_2, we have the r^p-estimate:
  E^p_Ψ(Σ_τ2) + (1/C) ∫_τ1^τ2 (E^(p−1)_Ψ(Σ_τ) + (2 − p) A^(p−1)_Ψ(Σ_τ)) dτ ≤ E^p_Ψ(Σ_τ1) + C Ě^N_Ψ(Σ_τ1). (128)"
- (R6) Theorem 18, p. 47: "Ě^N_Ψ(Σ_τ) ≲ I_Ψ(Σ_0)/τ^2, (130) where I_Ψ(Σ_0) := E^2_{Ψ,L_K Ψ}(Σ_0) + E^N_{Ψ,L_K Ψ,
  L^2_K Ψ}(Σ_0). (131)", K = {T, Ω_i} (p. 47); and in its proof, with τ_k = 2^k: "there exist τ̃_k ∈ [τ_(k−1), τ_k]
  such that E^1_Ψ(Σ_τ̃k) ≤ (C/τ_k)(E^2_Ψ(Σ_τ(k−1)) + Ě^N_Ψ(Σ_τ(k−1))) ≤ (C/τ_k)(E^2_Ψ(Σ_τ0) + Ě^N_Ψ(Σ_τ0))" (p. 47).
- (R7) The scalar master quantity and its normalisation, as the supplement READ it (Proposition 10.1 (iii)-(iv)):
  [HKW18]'s Q^(+) is [KI03]'s master field Phi (their (169)) carried as (r^(1/2) Phi) times a tensor harmonic ((173),
  pp. 60-61), so its pointwise norm is r^(-3/2) |Phi| and the r^p energies (124), (127) are of Phi itself.

[KI03] (H. Kodama and A. Ishibashi, arXiv:hep-th/0305147v3) is used only through the supplement's Proposition 10.1
(ii)-(iii), the gauge and the reconstruction (10.1), READ there; at l = 2 and 4 the reconstruction, with the
potential below, is also checked here against the linearised Einstein equations (U3 (b)). The scalar potential is
[CLY03b]'s, as `settle5.py` T2 READ it.

## 2. The components on the outgoing chart

*Notation.* f = 1 - mu/r^2, r_h = mu^(1/2), r* = r + (r_h/2) log((r - r_h)/(r + r_h)), u = t - r*, v = t + r* (twice
[HKW18]'s u and v). The outgoing chart (u, r): g = -f du^2 - 2 du dr + r^2 gamma, in which T = d_t = d_u. A scalar mode
of the class has harmonic S = P_j(cos 2 theta), l = 2j >= 2, k^2 = l(l + 2), m = k^2 - 3, H = m + 6 mu/r^2 (5 <= m <=
H <= m + 6 on r >= r_h), master field P(u, r) (the Phi of [KI03] and of (R7)), and in the gauge f_a = 0 = H_T the
mode is h = F_ab S dy^a dy^b + 2 r^2 F S gamma with F, F_ab given by the supplement's (10.1). The static orthonormal
frame on r > r_h is e0 = f^(-1/2) d_t = f^(-1/2) d_u, e1 = f^(1/2) d_r|_t = f^(1/2) d_r - f^(-1/2) d_u, and the
unit frame e_i of the sphere of radius r, in which h(e_i, e_j) = 2 F S delta_ij. The master equation (d_t^2 - d_r*^2 +
V) P = 0, V = f Q/(16 r^2 H^2) ([CLY03b], `settle5.py` T2), is in the outgoing chart

    2 f d_r T P = f d_r (f d_r P) - V P                                                                        (2.1)

(computed: U3 (a), box_2 = -2 d_u d_r + d_r(f d_r) there). Jets: P, TP, T^2 P, d_r P, d_r TP, d_r^2 P (d_r at fixed u).

**Lemma 1 (computed: U1, U2, U4).** (i) (10.1) computed in the outgoing chart is the supplement's ingoing-chart (10.1)
(`checks/kirecon5.py`) carried by v = u + 2r*. (ii) The frame components are exact linear combinations of the jets.
The coefficient of T^2 P in h(e0, e0), h(e0, e1), h(e1, e1) is r^(1/2)/f, -r^(1/2)/f, r^(1/2)/f, and T^2 P does not
occur in h(e_i, e_j); the coefficient of TP in 2F is -r^(-1/2). (iii) With d_r^2 P eliminated by (2.1), every
coefficient of r^(-1/2) h(e_a, e_b) (a, b in {0, 1}) and of r^(1/2) 2F is f^(-K) times a finite sum of monomials
H^alpha r^beta with alpha <= 0, except that the coefficient of P carries alpha <= 1 (the factor m of Proposition 10.1
(iii), two angular derivatives), and

    jet          T^2 P   d_r TP   TP    d_r P   P
    orbit block  0       0        -1    -1      -2        (largest beta in r^(-1/2) h(e_a, e_b))
    angular      absent  absent   0     0       -1        (largest beta in r^(1/2) 2F)

with the 0's attained by T^2 P in h(e0, e0) and by TP in 2F. On r >= R_1 > r_h, f^(-K) <= (1 - mu/R_1^2)^(-K), so
r^(-1/2) h(e_a, e_b) and r^(1/2) h(e_i, e_j) are bounded by the jets with weights r^beta, uniformly in r >= R_1 and in
l (H >= 5, H <= (11/8) k^2).

(The full table, coefficient by coefficient, is printed by U4 in `checks/rwgauge5u.out`. Once d_r^2 P is eliminated,
d_r TP survives only in h(e0, e1).)

## 3. Theorem 1: it fails uniformly in r

Fix R_1 and [HKW18]'s foliation (R3). In the coordinates of section 2 the part of Sigma_tau in r >= R_1 is the cone
C_tau := {u = u_tau, r >= R_1}, u_tau = u_0 + tau.

**Theorem 1 (proved; the identities computed: U2, U3, U5, U6).** For every tau_1 >= 0, every even l >= 2 and every
(A, B) in R^2 there is a smooth linearised vacuum solution h about five-dimensional Tangherlini, on the future of
Sigma_0 in the exterior and up to the future horizon, of the class (T^2-invariant and even under both reflections),
consisting of the single scalar mode l in the gauge f_a = 0 = H_T (no l = 0 part, no tensor part), such that

(i) its master field has I_{X Psi}(Sigma_0) < oo for every X a product of T and the rotations Omega_i (all orders);

(ii) on C_tau1, with P_uu(r) := T^2 P(u_tau1, r) = B + (A/2) int_r^oo (V/f) dr',

    h(e_i, e_j) = -A r^(-1/2) S delta_ij,    h(e0, e0) = r^(1/2) f^-1 P_uu(r) S + c_A(r) A S,

c_A = -(2 m r^4 - 3 m mu r^2 - 6 mu^2)/(r^(1/2) (r^2 - mu)(m r^2 + 6 mu)) = O(r^(-1/2)) (computed: U5), and for A = 0:

    h(e0, e0) = B r^(1/2) f^-1 S,   h(e0, e1) = -B r^(1/2) f^-1 S,   h(e1, e1) = B r^(1/2) f^-1 S,   h(e_i, e_j) = 0.

In particular, for B != 0, sup_{Sigma_tau1} |h(e0, e0)| = oo and int_{R_1}^oo r^-2 ||h(e0, e0)||^2 dr = oo on that leaf,
while I_Psi(Sigma_0) < oo: no estimate sup_{Sigma_tau} |h(e_a, e_b)| <= C(tau) D^(1/2), and no estimate of int r^-2
||h(e_a, e_b)||^2 dr along the leaf, holds at any tau, whatever the data norm D built from (R1)-(R6). For A != 0,
r^(1/2) |h(e_i, e_j)| = |A| |S| on C_tau1, so the weight r^(1/2) of Theorem 2 (c) on the angular block is attained.

*Proof.* Step 1 (Kruskal form of the master equation). Put U = -e^(-u/r_h), W = e^(v/r_h) (Kruskal's V, renamed to
keep V for the potential); the surface gravity is 1/r_h. Then -UW = e^(2 r*/r_h) = e^(2r/r_h) (r - r_h)/(r + r_h),
whose r-derivative at r_h is e^2/(2 r_h) != 0 [R2.0 m4: and 2 r^2 e^(2r/r_h)/(r_h (r + r_h)^2) > 0 at every r > 0,
from -1 at r = 0, so r is a smooth function of UW on all of {UW < 1}], so r is a smooth function of UW near the
horizons; d_u d_v = -(UW/r_h^2) d_U d_W, and the master equation 4 d_u d_v P + V P = 0 becomes d_U d_W P = c P with

    c = -(r_h^2/4) (V/f) (f/(-UW)) = -(r_h^2/4) (V/f) (r + r_h)^2 e^(-2r/r_h)/r^2,

smooth wherever r > 0 (computed: U5). The past horizon is W = 0, the future horizon U = 0, and C_tau1 lies on {U =
U_1}, U_1 := -e^(-u_tau1/r_h).

Step 2 (the Goursat problem). [R2.0 m4: U_0' is unnecessary, and the domain is the union of the rectangles Q =
[U_-, U_+] x [0, W_+] with U_- <= U_1 <= U_+ and U_+ W_+ < 1, which covers the whole exterior and the future horizon;
see R2.0.3.] Let U_0' be at most the least value of U on Sigma_0 (finite: Sigma_0 ∩ {r <= R_1} is
compact in the Kruskal chart, and U = U_0 := -e^(-u_0/r_h) on C_0), so that the future of Sigma_0 lies in {U >= U_0'},
U increasing along causal curves. Let g(U) := alpha (U - U_1) + (beta/2)(U - U_1)^2 and consider, on each compact
rectangle Q = [U_0', U_+] x [0, W_+] with 0 < U_+ small enough that r > 0 on Q, the integral equation

    P(U, W) = g(U) + int_{U_1}^U int_0^W c(U', W') P(U', W') dW' dU'                                           (3.1)

(signed integrals). Its n-th Picard iterate is bounded by sup_Q |g| M_Q^n/n!, M_Q := int int_Q |c|, because the
iterated integrand lives on chains ordered in both coordinates; so (3.1) has a unique continuous solution on Q, which is
smooth (differentiate (3.1)), and the solutions on nested rectangles agree. This gives a smooth P on [U_0', U_+] x
[0, oo) with d_U d_W P = c P, P(U, 0) = g(U), P(U_1, W) = 0 (proved).

Step 3 (the jets on C_tau1). On U = U_1, P = 0, so d_W^k P = 0, and d_W d_U P = c P = 0 gives d_U P = g'(U_1) = alpha;
d_W d_U^2 P = d_U(c P) = c alpha. In the outgoing chart (d_u = -(U/r_h) d_U, d_u^2 = (U^2 d_U^2 + U d_U)/r_h^2,
computed: U5) this is: P = d_r P = d_r^2 P = 0 and TP = A := -U_1 alpha/r_h along C_tau1, d_r TP = 0 by (2.1), and
d_r T^2 P = -A V/(2f) (the u-derivative of (2.1)), so T^2 P = B + (A/2) int_r^oo (V/f) dr', the integral finite
(computed: U5; at l = 2 it is int_{r_h}^oo (V/f) dr = 11/(2 r_h) exactly), B its limit at null infinity. A = -U_1
alpha/r_h, and B = (U_1^2 (beta + alpha int_0^oo c(U_1, W) dW) + U_1 alpha)/r_h^2 is affine in beta with slope U_1^2/
r_h^2 != 0, so every (A, B) is reached by choosing alpha and then beta.

Step 4 (the metric). With S = P_(l/2)(cos 2 theta), the supplement's (10.1) applied to P S gives h in the gauge f_a = 0
= H_T; it is a linearised vacuum solution (Proposition 10.1 (iii), [KI03] (3.13)-(3.14) READ there; at l = 2, 4
[R2.0 m5: and 6] computed here: U3 (b), DRic(h) = 0 modulo the master equation), smooth up to the future horizon
because P is smooth in (U, W) and (U, W) are smooth functions of the ingoing chart (v, r) there, T^2-invariant and even
under both reflections because S depends on theta alone. Lemma 1 (ii) and the jets of Step 3 give (ii) of the theorem
(computed: U5).

Step 5 (the data). On the part of Sigma_0 in r <= R_1 the solution is smooth on a compact set, so every energy there is
finite. On C_0 = Sigma_0 ∩ {r >= R_1} (u_0 <= u_tau1): the rotations act within the mode, so it suffices to take X =
T^a; T^a P solves the master equation (T is Killing, T = (W d_W - U d_U)/r_h), with Goursat data on W = 0 and on U =
U_1 that are bounded (on U = U_1 they are the T^a P of U6, bounded along the cone). On the strip u_0 <= u <= u_tau1,
int int |c| dU dW = (1/4) int int V du dv = (1/2)(u_tau1 - u_0) int_{r_h}^oo (V/f) dr < oo (dU dW = (UW/r_h^2) du dv
in absolute value; v = u + 2r*), so the Picard bound of Step 2 gives sup |T^a P| < oo on the strip. Then, along u =
u_0, d_v T^a P(u_0, v) = d_v T^a P(u_tau1, v) + (1/4) int_{u_0}^{u_tau1} V T^a P du', where the first term is (f/2)
d_r T^a P on C_tau1, O(r^-2) for a <= 4 (computed: U6, from the expansion at null infinity), and the second is O(r^-2)
because V = O(r^-2) uniformly for u in a compact interval at fixed v. So d_r T^a P = O(r^-2) and T^a P = O(1) on C_0,
and every energy in I_{X Psi}(Sigma_0) -- int r^p (d_r T^a P)^2 dr with p <= 2 and int ((d_r T^a P)^2 + k^2 (T^a P)^2
/r^2) dr, U7 (ii) -- is finite. For tau_1 = 0 the strip is empty and U6 alone suffices. Every order a: along C_tau1 the
T^a P are determined by P = 0 and T P = A through the u-derivatives of (2.1), d_r P_j = (1/2) d_r(f d_r P_(j-1)) -
(1/2) r^-2 q P_(j-1), q = r^2 V/f analytic in 1/r at null infinity; if P_(j-1) = c + O(1/r) and d_r P_(j-1) = O(r^-2)
as power series in 1/r, then d_r P_j = O(r^-2) and P_j = c_j + O(1/r), so the induction runs through every a (U6
computes a <= 4, which is what X in {1, T, T^2, Omega, T Omega, Omega^2} with [HKW18]'s L_K^2 asks of Theorem 2). []

*What it shows.* The obstruction is not a defect of the estimates: on [HKW18]'s leaves, which run out to null infinity,
the gauge f_a = 0 = H_T puts T^2 P, the radiation of the master field, into the orbit-space components with the weight
r^(1/2) (Lemma 1 (ii)). The family is the cleanest such solution: P vanishes along the cone and only T^2 P (and, for A
!= 0, TP) survives there.

## 4. Theorem 2: what holds uniformly in r

Let h be a perturbation of the class in the gauge of the paper (f_a = 0 = H_T for every mode l >= 2, h_0 = c K), and
let Psi_l be the master quantities of its modes (scalar and tensor). Write h_(ab) := h(e_a, e_b) - c K(e_a, e_b), h_(ij)
:= h(e_i, e_j) - c K(e_i, e_j) (the frame components of h - c K) on r >= R_1, ||.|| the L^2(S^3) norm, and

    D := sum over the modes of sum_X I_{X Psi_l}(Sigma_0),   X in {1, T, T^2, Omega, T Omega, Omega^2}

(Omega standing for the six rotations, summed), [HKW18]'s data norm (R6) with at most two more commutations.

**Theorem 2 (proved from (R1)-(R7) READ, applied as stated; the coefficients and exponents computed: U4, U7).** With C
depending on mu and R_1 only, for tau >= 1 and every 0 < delta <= 1/2:

    (a)  int_{R_1}^oo ( r^-3 ||h_(ab)||^2 + r^-1 ||h_(ij)||^2 )(tau, r) dr  <=  C D tau^-2,
    (b)  sup_{r >= R_1} ( r^-1 ||h_(ab)|| + ||h_(ij)|| )(tau, r)  <=  C D^(1/2) tau^-1,
    (c)  sup_{r >= R_1} ( r^(-1/2) ||h_(ab)|| + r^(1/2) ||h_(ij)|| )(tau, r)  <=  C delta^(-1/2) D^(1/2) tau^(delta-1/2),

the arguments meaning the point of Sigma_tau at radius r (on C_tau). The weights in (c) are the exact growth and
decay of Theorem 1 and cannot be raised; in (a), r^-3 cannot be replaced by r^-2 (Theorem 1). [R2.0: (a) is against
dr dsigma, dsigma the unit sphere's measure (R2.0.2); ||.|| is the L^2(S^3) norm at fixed (tau, r), and the pointwise
bounds are Theorem 2' (R2.0.1); the proof below uses the class only through three properties (no vector type, no l = 1,
h_0 = c K), which is what lets Theorem 2' apply it to rotated perturbations.]

*Proof.* Step 1 (the energies on the cone; computed: U7 (ii)). On C_tau, n = L = f d_r|_u (R3), the v-measure is
dr/f, Y = 0 (R4: r >= R_1 > r_1), and Ť(L, T) = (1/2)(L Psi)^2 + (1/2) f r^-2 |∇̊Psi|^2 (computed from (89)). With
Psi = r^(1/2) Phi Y_l (R7), |Y_l|_g = r^-2 |Y_l|_gamma, so r^3 |∇_r Psi|^2 = (d_r Phi - 3 Phi/(2r))^2 |Y_l|^2; the ratio
||Y_l||/||S_l|| is bounded below uniformly in l (1 for unit harmonics; (2/3) k^2 (k^2 - 3) >= 80/3 in square for Y_l =
(D D - gamma Lap/3) S_l, `checks/rwgauge5.py` R3 (e)); and int_{S^3} |∇̊Y_l|^2 = (k^2 - 6) ||Y_l||^2 >= (k^2/4)
||Y_l||^2 for the scalar-derived tensor harmonics (k^2 >= 8; the least value 2 is [HKW18]'s lambda = 2, p. 31) [R2.0
m9: for every l this is [HKW18] (36), p. 8, "˚∆Y_αβ = (2n − ℓ(ℓ + n − 1)) Y_αβ", at n = 3]. So

    int_{R_1}^oo ( (d_r Phi)^2 + k^2 Phi^2/r^2 ) dr  <=  C_1 Ě^N_Psi(Sigma_tau)/||Y_l||^2,   C_1 = 9/(2 f_1) + 8

(f_1 = f(R_1); computed: U7 (ii)-(iii)); the same for X Psi with X Phi in place of Phi, and sum_i Ě^N[Omega_i Psi_l] =
k^2 Ě^N[Psi_l] mode by mode (the Casimir of so(4) on the mode, l(l + 2) = k^2, commutes with the energy densities).
By (R6) applied to X Psi, each Ě^N[X Psi](Sigma_tau) <= C I_{X Psi}(Sigma_0) tau^-2.

Step 2 (a). By Lemma 1 (iii) and (2.1), r^(-3/2) h_(ab) and r^(-1/2) h_(ij) are combinations of T^2 P, TP and P with
coefficients O(r^-1) (times H <= (11/8) k^2 for P) and of d_r TP, d_r P with coefficients O(1), uniformly in l
(computed: U4, the weights of (a)). So the left side of (a) is bounded by sum_{X in {1, T, T^2, Omega}} of Step 1's
left sides, hence by C D tau^-2 (the factor H^2 on P^2 by the Omega-commuted energy, k^4 Phi^2/r^2).

Step 3 (b). Lemma S (proved; U7 (i)): if int_R^oo (w^2/s^2 + w'^2) ds < oo then

    sup_{r >= R} w(r)^2/r  <=  2 (int_R^oo w^2/s^2)^(1/2) (int_R^oo w'^2)^(1/2) + int_R^oo w^2/s^2,

since d_s(w^2/s) = 2 w w'/s - w^2/s^2 and liminf w^2/s = 0 (else w^2/s^2 >= c/s is not integrable); and sup w^2 <= 2
(int w^2)^(1/2) (int w'^2)^(1/2) when int w^2 < oo (then liminf |w| = 0). Applied with Step 1, each for every mode:
w = T^a P (a <= 2) gives sup r^(-1/2) |T^a P| <= C (Ě^N[T^a Psi])^(1/2); w = k^2 P gives sup r^(-1/2) k^2 |P| <= C
(Ě^N[Omega Psi] + Ě^N[Omega^2 Psi])^(1/2); w = d_r T^a P (a <= 1), with w' = d_r^2 T^a P = 2 d_r T^(a+1) P/f - (f'/f)
d_r T^a P + V T^a P/f^2 from (2.1) and |V| <= C k^2 r^-2, gives sup |d_r T^a P| <= C (Ě^N[T^a Psi] + Ě^N[T^(a+1)
Psi] + Ě^N[T^a Omega Psi])^(1/2). Each is <= C D^(1/2) tau^-1 by (R6). Lemma 1 (iii), with the weight r^-1 on the
orbit block and r^0 on the angular block, puts every term under one of these sups with a bounded coefficient
(computed: U4, the weights of (b)).

Step 4 (c). The new input is sup |T^2 P| and sup |TP| (the terms of weight r^0 in Lemma 1 (iii); the others are
handled by Step 3). For w = T^a P (a = 1, 2) on C_tau and p = 1 + 2 delta: |w(r)| <= |w(R_1)| + int_{R_1}^oo |w'| <=
R_1^(1/2) sup r^(-1/2) |w| + (int s^p w'^2)^(1/2) (R_1^(1-p)/(p - 1))^(1/2). The first is <= C D^(1/2) tau^-1 (Step 3);
for the second, int s^p w'^2 <= f_1^-(k+2) E^p[T^a Psi] [R2.0 m9: k here is [HKW18]'s exponent in (127), written
k_H in R2.0, not the k of k^2 = l(l + 2)], and E^p <= (E^1)^(2-p) (E^2)^(p-1) (Hoelder with s^p = s^(2-p)
(s^2)^(p-1)), where E^2[T^a Psi](tau) <= E^2(0) + C Ě^N(0) ((128) at p = 2; [R2.0 m1: Ě^N(0) <= C E^N(0) <= C I
by [HKW18] Lemma 11, p. 39, (R8) in R2.0]) and E^1[T^a Psi](tau) <= C D/tau:
for tau in [tau~_k, tau~_(k+1)], (128) at p = 1 from tau~_k and (R6)'s bound at tau~_k give E^1(tau) <= C (tau_k^-1 +
tau~_k^-2) D, and tau <= tau_(k+1) = 2 tau_k. So the second term is <= C delta^(-1/2) D^(1/2) tau^(-(2-p)/2) = C
delta^(-1/2) D^(1/2) tau^(-1/2 + delta) (computed: U7 (iv)). []

*The tensor type.* Its components in the frame are 2 H_T T_(ij) = 2 r^(-3/2) Phi_T T_(ij) (Proposition 10.1 (iii)),
three powers of r^(1/2) better than the angular block of the scalar type [R2.0 m9: two powers: r^(-3/2) against
r^(-1/2)], and Step 1 and Lemma S give (a)-(c) for it
directly; it is included in h_(ij) above.

*The l = 0 part.* h_0 - c K = 0 by the gauge condition, and K's frame components are O(r^-2): c K is the change of mass
to which h settles. *The mode sum.* Every constant above is uniform in l, and ||h_(ab)||^2 = sum_l ||h_(ab), l||^2 with
sup_r of a sum at most the sum of the sups, so (a)-(c) for the modes add up to (a)-(c) for h.

## 5. Remarks

1. *Sharpness.* The weights are sharp in the strongest sense available: Theorem 1's family realises r^(-1/2) h(e0, e0)
   = B f^-1 S and r^(1/2) h(e_i, e_j) = -A S delta_ij on a whole cone. The rates in (b)-(c) are what [HKW18]'s energy
   decay gives by Lemma S and (128); they are not claimed sharp (the measured tail is t^-7 at l = 2, section 10.3 of
   the supplement).
2. *What the frame means.* A bounded change of frame (any frame uniformly comparable to the static one on r >= R_1)
   leaves the conclusions unchanged. The statements are on r >= R_1, where the static frame is regular; on r <= R_1 the
   paper's statement (each region r <= R) is unchanged by this note.
3. *A reading of [HKW18]'s energies (outside this item, recorded).* (R4) shows that Ě^N is the energy of the red-shift
   multiplier N = T + Y, a first-order energy; the supplement's proof of Proposition 10.1 (iv) calls these "the N-th
   order red-shift energies". The difference does not touch r >= R_1 (where Y = 0 and the radial second derivatives
   come from (2.1)). Near r = r_h, where (2.1) degenerates (the coefficient of d_r^2 P in the ingoing chart is f), the
   non-degenerate control of d_r^2 Phi that the ingoing components' "two orbit-space derivatives" ask for is not an
   energy [HKW18] commute with (their K = {T, Omega_i}, (R6)); it is the red-shift commutation of Dafermos and
   Rodnianski, which [HKW18] do not carry. Whether the paper's region r <= R statement, taken up to the horizon, is to
   be read with that commutation or through GAUGEDECAY5.md's Theorem 1.5 (Part VIII's rate, the horizon included) is
   for the author; this note proposes no change to it.
4. *Not claimed.* Nothing here concerns the harmonic gauge or the passage to it (sections 10.4 onward of the supplement).

## 6. Proposed replacement for the paper (RESPONSE-HL-5D.md, section 8.2, lines 793-796)

The old text occurs exactly once in the paper and the new text not at all (computed: U8). [R2.0: the block below is
the round-2 text, for M1, M2 and the wording of the verifier's minor 3; the round-1 block is kept in R2.0.4.]

```old
So in
that Regge–Wheeler-type gauge, with the l = 0 gauge fixed to the mass change, every metric component of a perturbation
in the class settles to a change of mass at [HKW18]'s rate on each region r ≤ R, uniformly in l with a constant growing
as a power of R (uniformly in r it is not shown), with the loss of two derivatives so counted.
```

```new
So in
that Regge–Wheeler-type gauge, with the l = 0 gauge fixed to the mass change, every metric component of a perturbation
in the class settles to a change of mass at [HKW18]'s rate on each region r ≤ R, uniformly in l with a constant growing
as a power of R, with the loss of two derivatives so counted. Uniformly in r it fails, and what holds instead is sharp
(supplement RWGAUGE5, `docket68/n1star/checks/rwgauge5u.py`). In the frame of the static observers, on the outgoing
part of [HKW18]'s leaves (r ≥ R_1, their radius), the orbit-space components of the scalar type can grow as, and no
faster than, r^(1/2): for every leaf there is a single-mode perturbation of the class, with finite [HKW18] data of
every order, whose component h(e_0, e_0) is B r^(1/2) f^(−1) S on the outgoing part of that leaf, B ≠ 0 a constant,
f = 1 − μ/r² and S its harmonic (Theorem 1, proved; the components computed exactly). With that weight they settle,
and the angular components and the tensor type settle without it, pointwise and uniformly in r ≥ R_1 and in l:
r^(−1/2)|h(e_a, e_b)| and r^(1/2)|h(e_i, e_j)| decay at least as τ^(δ−1/2) for every δ ∈ (0, 1/2], and
r^(−1)|h(e_a, e_b)| and |h(e_i, e_j)| at least as τ^(−1), for data with [HKW18]'s I_{XΨ}(Σ_0) finite for X = T^a Ω^b,
a ≤ 2, b ≤ 4, Ω the rotations; and, for b ≤ 2, the integral of r^(−3)|h(e_a, e_b)|² + r^(−1)|h(e_i, e_j)|² over
r ≥ R_1 and the unit sphere, against dr dσ, decays at least as τ^(−2), [HKW18]'s rate (Theorems 2 and 2′, proved from
[HKW18]'s Theorems 2, 16 and 18 as READ and a Sobolev inequality on S³; every coefficient and exponent computed). The
powers r^(±1/2) are attained, so the weights cannot be improved.
```

## 7. Files

- `RWGAUGE5.md` (this note).
- `checks/rwgauge5u.py` with `checks/rwgauge5u.out`: U1-U8 (U8 the replacement's uniqueness and the line widths),
  exact, each with a control that mutates the code under test and fails. Imports `checks/kirecon5.py` (U1, U3),
  `checks/rwgauge5.py`'s tensor calculus (U3 (b), U7) and `settle5.py`'s potentials (U3, U5); writes nothing.

## R2.0 Round 2: the verifier's findings, re-derived and seated

*Status.* Round 2, 2026-11-06, after an independent verifier's reading of this note and of `checks/rwgauge5u.py`.
Its verdict: the mathematics holds. It recomputed Lemma 1, Theorem 1 and the vacuum check at l = 2 and 4 by its own
code (a static-chart reconstruction and its own linearised Ricci), confirmed Theorem 2 as stated in section 4, and
agreed with Remark 3. The text above is kept; where a finding corrects it, a bracketed note [R2.0 ...] points here.
Each finding below was re-derived before it was seated. The verifier's minor 2 (the supplement's Proposition 10.1 (iv)
at N1STAR-PROOF.md:1730 and :1805) is being repaired elsewhere, with the merged text of the paper's section 8.2; this
note edits neither.

(R8) READ, [HKW18] p. 39: "Lemma 11. Assume the T-energy comparison (111) holds. Defining the red-shift multiplier N as
above, we have the pointwise density estimate [...] in addition to the energy comparison E^N_Ψ(Σ_τ) ≈ Ě^N_Ψ(Σ_τ)".
(R9) READ, [HKW18] (36), p. 8: the tensors Y_αβ := ˚∇_α˚∇_βY − (1/n) ˚σ_αβ ˚∆Y of (35) satisfy "˚∆Y_αβ = (2n −
ℓ(ℓ + n − 1)) Y_αβ", with ℓ ≥ 2.

### R2.0.1 M1: the bounds of Theorem 2 (b)-(c) are L^2(S^3) norms; the pointwise statement, proved

*Finding (agreed).* (b)-(c) bound ||.||, the L^2(S^3) norm at fixed (tau, r); the summary and the round-1
replacement wrote |.|, which reads pointwise, and a zonal harmonic's sup over L^2 ratio grows with l. Of the two fixes
the stronger is taken: the pointwise statement is proved below with two more rotations in the data.

**Lemma A (proved; computed: U9).** Let Omega_i, i = 1, ..., 6, be the rotations x_a d_b - x_b d_a (a < b) of R^4 on
S^3. For a function w on S^3,

    sup |w|^2  <=  (1/12) ||(1 - Lap) w||^2  <=  (1/6) ( ||w||^2 + sum_{i,j} ||Omega_i Omega_j w||^2 ),

and for a symmetric 2-tensor T on S^3, with L_i the Lie derivative along Omega_i,

    sup |T|^2  <=  (1/6) ( 2305 ||T||^2 + 192 sum_i ||L_i T||^2 + 4 sum_{i,j} ||L_i L_j T||^2 ).

*Proof.* The degree-l harmonics on S^3 have dimension (l + 1)^2. For an L^2-orthonormal basis Y_m of them, sum_m
|Y_m(omega)|^2 does not depend on the basis and is carried to itself by the rotations, so it is constant, equal to
(l + 1)^2/vol(S^3) = (l + 1)^2/(2 pi^2); hence |w_l(omega)| <= (l + 1) ||w_l||/(2 pi^2)^(1/2) for w_l of degree l.
By Cauchy-Schwarz, sup |w| <= sum_l (l + 1) ||w_l||/(2 pi^2)^(1/2) <= (sum_l (l + 1)^-2)^(1/2) (sum_l (l + 1)^4
||w_l||^2)^(1/2)/(2 pi^2)^(1/2), and (l + 1)^2 = 1 + l(l + 2), sum_l (l + 1)^-2 = pi^2/6: the first inequality, with
the constant (pi^2/6)/(2 pi^2) = 1/12. Then (a + b)^2 <= 2a^2 + 2b^2 and ||Lap w||^2 = sum_{i,j} ||Omega_i Omega_j w||^2,
since sum_i Omega_i^2 = Lap on S^3 and each Omega_i is skew and commutes with Lap. For T: extend T to R^4 by T(PX, PY),
P = 1 - x x^T/|x|^2; its Cartesian components T_AB are functions on S^3 with sum_AB T_AB^2 = |T|^2. L_Omega P = 0, so
the Lie derivative of the extension is the extension of L_Omega T, and in Cartesian components Omega(T_AB) = (L_Omega
T)_AB - (omega^T T + T omega)_AB with omega the generator's constant matrix, of operator norm 1. So |Omega_i T|_F <=
|L_i T| + 2 |T| and |Omega_i Omega_j T|_F <= |L_i L_j T| + 2 |L_j T| + 2 |L_i T| + 4 |T|; summing the scalar
inequality over A, B, with (a + b + c + d)^2 <= 4 (a^2 + b^2 + c^2 + d^2) and six rotations, gives 4, 4 x 4 x 6 + 4 x 4 x
6 = 192 and 4 x 16 x 36 = 2304, plus the ||T||^2 of the first term. []

*U9 computes:* the dimensions (l + 1)^2 (l <= 20), vol(S^3) = 2 pi^2, 1 + l(l + 2) = (l + 1)^2, sum (l + 1)^-2 =
pi^2/6 and the constant 1/12; the reproducing kernel ((l + 1)/(2 pi^2)) U_l(cos psi) (Chebyshev U) with norm^2 =
value at its centre = (l + 1)^2/(2 pi^2) and eigenvalue -l(l + 2), l <= 6; sum_i Omega_i^2 = Lap on four test
functions in Hopf coordinates (three zonal, one not); ||Lap w||^2 = sum ||Omega_i Omega_j w||^2 on a test function by
exact integration; operator norm 1 of the six generators; L_Omega P = 0; the inequality (a + b + c + d)^2 <= 4 sum and
the constants. Controls: the Casimir summed over ordered pairs (twice Lap) fails, and the series with (1 - Lap)^(3/4)
in place of (1 - Lap) diverges.

**Theorem 2' (proved from Theorem 2 and Lemma A).** With h as in Theorem 2, let

    D' := sum_{Y in {1, Omega_i, Omega_i Omega_j}} D[L_Y h]   (the I_{X Psi} with X = T^a Omega^b, a <= 2, b <= 4).

Then for tau >= 1 and 0 < delta <= 1/2, with C depending on mu and R_1 only, |h_(ab)| the components as functions on
S^3 and |h_(ij)| the norm of the angular block in the unit sphere's metric:

    (b')  sup_{r >= R_1, omega} ( r^-1 |h_(ab)| + |h_(ij)| )(tau, r, omega)  <=  C D'^(1/2) tau^-1,
    (c')  sup_{r >= R_1, omega} ( r^(-1/2) |h_(ab)| + r^(1/2) |h_(ij)| )  <=  C delta^(-1/2) D'^(1/2) tau^(delta-1/2).

*Proof.* At fixed (tau, r), h_(ab) is a function on S^3 and h_(ij) is the symmetric tensor r^-2 h restricted to the
sphere, in the unit metric. The rotations commute with e0, e1 and with the restriction to the sphere, so Omega_i
Omega_j (h_(ab)) = (L_i L_j h)_(ab) and L_i L_j (h_(ij)) = (L_i L_j h)_(ij). L_Y h is a linearised vacuum solution in
the same gauge (the gauge f_a = 0 = H_T and the decomposition into types are SO(4)-equivariant), of scalar and tensor
type only, with modes l >= 2 only and no l = 0 part (L_Y (c K) = 0). Theorem 2's proof uses the class only through
these three properties: Lemma 1 holds for every scalar harmonic, its frame formulas seeing S only through k^2, and
[HKW18]'s estimates are for every perturbation. So (b)-(c) hold for L_Y h with the data D[L_Y h], and Lemma A gives
(b')-(c'). []

So the pointwise |.| of the summary is Theorem 2' with D', and section 6 now says pointwise with the data stated.

### R2.0.2 M2: the measure in (a)

*Finding (agreed), re-derived.* Theorem 2 (a) is int_{R_1}^oo int_{S^3} ( ... ) dr dsigma, dsigma the unit sphere's
measure: that is how Step 2 bounds it, by int (...) dr of Step 1's energies. Against the leaf's own volume form, r^3 dv
dsigma = r^3 dr dsigma/f ([HKW18] p. 30, (127)), the bound is false: for Theorem 1's family on C_tau1, int r^-3
|h(e0, e0)|^2 r^3 dr/f = ||S||^2 B^2 int r f^-3 dr = oo. The summary's "squared L^2 norm along the leaf" is meant in
dr dsigma; section 6 now writes the integral and its measure out.

### R2.0.3 The minor findings

1. *Lemma 11.* Agreed: Ě^N(Sigma_0) <= C E^N(Sigma_0) <= C I, used in Step 4 of Theorem 2, is [HKW18] Lemma 11
   ((R8)); cited there now.
2. *The supplement.* Handled elsewhere (see the status paragraph).
3. *Wording of the replacement.* Agreed; section 6 now reads "can grow as, and no faster than", "decay at least as",
   "on the outgoing part of that leaf", "B != 0 a constant" and "delta in (0, 1/2]".
4. *The Goursat domain.* Agreed, re-derived. F(r) := e^(2r/r_h)(r - r_h)/(r + r_h) = -UW has F' = 2 r^2
   e^(2r/r_h)/(r_h (r + r_h)^2) > 0 on (0, oo) and F(0) = -1 (computed: U5), so r is a smooth function of UW on {UW <
   1} and c is smooth there. The domain of (3.1) is the union of the rectangles Q = [U_-, U_+] x [0, W_+] with U_- <=
   U_1 <= U_+ and U_+ W_+ < 1, on each of which the Picard bound holds; their union contains the exterior {U < 0, W >
   0}, the future horizon and a neighbourhood of it inside. So the solution exists on the whole exterior and U_0' is
   not needed; Step 5 is unchanged.
5. *General even l.* The vacuum property for every even l rests on [KI03] as Proposition 10.1 (iii) READ it; U3 (b)
   now computes l = 6 as well (l = 2, 4, 6).
6. *The constant between [HKW18] (169)'s Phi and (10.1)'s P.* See R2.0.5.
7. *The program.* Every item taken: U4's weights for (a), (b) and (c) are now computed from the measured powers of
   every entry, not from the tables; U7's two tautologies are replaced by an exact check of the interpolation E^p <=
   (E^1)^(2-p) (E^2)^(p-1) on three test functions at p = 6/5, 3/2, 9/5 (control: without the E^2 factor it fails);
   U5 derives the cone relations from (2.1) order by order in u - u_1 (no longer restating them) and asserts c_A and
   int V/f dr = 11/2 exactly; U3 (a) asserts that potential_general is settle5.py's potential at l = 2, 4, 6, 8 and
   that U4's elimination of d_r^2 P satisfies (2.1) identically; U6 asserts the leading coefficients -(m + 15/4)/2
   times A, B, C3 and re-checks the recursion by r-differentiation of the series; U8's label now says what it prints.
   The verifier's surviving mutants M4 (V/f^2 -> V/f), M8 (potential_general's Q) and M11 (U6's d_r sign) and its
   U5 survivors M3 and M9 are re-run against the new program in R2.0.6.
8. *The (R1) quote.* Corrected in place to p. 67's wording ("ℓ and m, owing to convergence ...").
9. *Nits.* "Two powers" (noted at the tensor type); the exponent k of [HKW18] (127) is k_H, not the k of k^2 = l(l + 2);
   (k^2 - 6) for every l is [HKW18] (36), p. 8, (R9) (U7 computes it at l = 2, 4).

### R2.0.4 The round-1 replacement block, kept for the record

[Superseded by section 6's block; it wrote |.| where Theorem 2 bounds L^2(S^3) norms (M1), left the measure of the
leaf norm unstated (M2), and is worded as the verifier's minor 3 records.]

```round1-new
So in
that Regge–Wheeler-type gauge, with the l = 0 gauge fixed to the mass change, every metric component of a perturbation
in the class settles to a change of mass at [HKW18]'s rate on each region r ≤ R, uniformly in l with a constant growing
as a power of R, with the loss of two derivatives so counted. Uniformly in r it fails, and what holds instead is sharp
(supplement RWGAUGE5, `docket68/n1star/checks/rwgauge5u.py`). In the frame of the static observers, along the
outgoing part of [HKW18]'s leaves, the orbit-space components of the scalar type grow as r^(1/2): for every leaf there
is a single-mode perturbation of the class, with finite [HKW18] data of every order, whose component h(e_0, e_0) is
B r^(1/2) f^(−1) S on that leaf, f = 1 − μ/r² and S its harmonic (Theorem 1, proved; the components computed
exactly). With that weight they settle, and the angular components and the tensor type settle without it, uniformly in
r and l along the outgoing part of the leaves: r^(−1/2)|h(e_a, e_b)| and r^(1/2)|h(e_i, e_j)| decay as τ^(δ−1/2) for
every δ > 0, r^(−1)|h(e_a, e_b)| and |h(e_i, e_j)| as τ^(−1), and the squared L² norms along the leaf of r^(−3/2)
h(e_a, e_b) and r^(−1/2) h(e_i, e_j) as τ^(−2), [HKW18]'s rate, for data with two more commutations with T and the
rotations (Theorem 2, proved from [HKW18]'s Theorems 2, 16 and 18 as READ; every coefficient and exponent computed).
The powers r^(±1/2) are attained, so the weights cannot be improved.
```

### R2.0.5 [HKW18] (169)'s Phi against (10.1)'s P

*Finding (agreed: not re-derived in round 1).* (R7) is the supplement's READ, and the constant between [HKW18]'s
master field and the P of (10.1) was not re-derived; an l-dependent constant would touch only Theorem 2's uniformity
in l. *Re-derived (computed: U10).* [HKW18] (159)-(162) give, in the gauge f_a = 0 = H_T (H_A = 0, H_2 = 0, e_A = 0),
hcheck_AB = r F_AB and Hcheck = r F, the H of (55) being the coefficient of the unit-sphere metric, 2 r^2 F. With
(163) read with mixed indices, X = hcheck^t_t - 2 Hcheck, Y = hcheck^r_r - 2 Hcheck, Z = hcheck^r_t (the reading
(164)'s inversion through the traceless equation requires: hcheck^t_t + hcheck^r_r = -6 Hcheck at n = 3), and
(168)-(169) at n = 3,

    Ztilde = ( f (d_r X + d_r Y) - (f/r + f'/2) X + (2f/r - f'/2) Y ) / (k^2/r^2 - f'' - 3 f'/r),
    Phi_HKW = ( 3 Ztilde - r (X + Y) ) / ( r^(1/2) (k^2 - 3 + 6 mu/r^2) ),

applied to the perturbation that (10.1) builds from P give, once the master equation removes d_t^2 P,

    Phi_HKW = P   exactly, at general l (every other jet of P cancels).

So the constant is 1 for every l, and [HKW18]'s scalar quantity is Q^(+) = (r^(1/2) P) Y_αβ with Y_αβ of (35)
unnormalised, ||Y_αβ||^2 = (2/3) k^2 (k^2 - 3) ||Y||^2 >= (80/3) ||Y||^2: Theorem 2's uniformity in l stands as
written (Step 1's ratio ||Y_l||/||S_l|| bounded below). The control (V multiplied by 1 + mu/r^2) leaves a non-constant
coefficient.

### R2.0.6 Mutants re-run

PLACEHOLDER-MUT
