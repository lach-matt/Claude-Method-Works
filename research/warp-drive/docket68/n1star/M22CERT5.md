# M22CERT5 -- the attempt at a certified lower bound m_lo on |M_22| (workstream D, after LAMBDA0-DATA5.md section 13)

*Status (2026-11-06).* New; not yet read by a verifier. The task: supply the certified stability constant of the
coupled stage-1 system on X*'s past, certify the residual of the numerical solution, and conclude |M_22 - M_22^num|
<= C_stab x residual, hence m_lo = M_22^num - that bound; if C_stab x residual cannot be brought below about 2 at a
resolution that can be run, report the certified numbers reached, and the resolution and cost the bound would need.
Labels as in LAMBDA0-DATA5.md: **proved**, **computed** (exact unless it says floating point; **certified** for Arb
balls or exact rationals), **deduced**, **READ**. Program: `checks/m22cert5.py` (`--selftest`; output
`checks/m22cert5.out`, **10/10**), which imports `checks/m22evol5.py` and changes nothing in it. LAMBDA0-DATA5.md,
CONSTANTS5.md, N1STAR-PROOF.md and the paper are not edited by this file.

## 0. Summary

- **What m_lo would buy** (computed, X5): lambda0 < 0.0022636 / 0.0019042 / 0.0011329 (operator norm / Frobenius /
  largest entry) at m_lo = 1, and 0.0023500 / 0.0019070 / 0.0011761 at m_lo = 1/2. The certified 0.0024433 /
  0.0019079 / 0.0012228 stand either way.
- **m_lo is not reached.** The estimate is written out (Section 2, proved). The certified numbers it yields are lower
  bounds on its own constants, and they suffice to decide it at every resolution that can be run:
  - its Gronwall factor for the energy is at least e^32.84 = 1.83 x 10^14 (certified, X3), from one coefficient of
    one row of the lower-order operator (X1). Half of that exponent is gathered after tau = 1.51, near X*;
  - so the estimate certifies m_lo > 0 only if int e^(Lambda(s)) ||rho(s)|| ds < 17.32 (deduced), Lambda(s) the
    exponent gathered from s to tau*, rho the residual;
  - the solver's residual (its tau-tau component alone, measured off the nodes; floating point, X4) gives that
    integral as 9.5 x 10^8, 5.1 x 10^8, 2.0 x 10^7 and 7.2 x 10^5 at 32 x 12, 40 x 12, 48 x 16 and 64 x 20: a factor
    4.2 x 10^4 too large at the finest grid. Extrapolated, it would fall below 17.32 at about 128 x 36, a run of about
    8 hours here. That is a necessary condition only: it uses X3's lower bound, the residual measured and not
    certified, and one component of it.
- **The certified residual** (X6): the residual is certified pointwise in Arb balls (6.70000884e-6 +/- 6e-30 at a
  point of the 24 x 12 test, its analogue at 48 x 16 in the output), but on a box of half-width delta its enclosure
  has radius ~ 13 delta (first-order wrapping). An L^2 certificate at the level the estimate needs (~3e-13 at tau =
  -0.8) would take delta ~ 2e-14, about 10^27 boxes per slice; even 1e-6 (a dual-weighted residual's level) takes
  about 10^14 boxes per slice and 10^17 over the run. A certified residual of the needed sharpness needs high-order
  Taylor or Chebyshev models with certified tails, whose cost is not a multiple of the evaluation count.
- **The certified upper bound on C_stab** is not computed: it needs the lower-order operator of the full 4D
  Cartesian system, which the class reduction does not determine (Section 4). It would only raise the bar: X3 is a
  lower bound on it.

## 1. What m_lo buys (computed, X5)

With C_app >= 12.593309 + m_lo (operator norm and largest entry) and C_app >= (16.127552^2 + m_lo^2)^(1/2)
(Frobenius), eps1 < s0 <= 0.030768560 and eps1 < 0.0153989 (largest entry), each bound rounded up (LAMBDA0-DATA5.md
13.6, n1):

| m_lo | operator norm | Frobenius | largest entry |
|---|---|---|---|
| 0 (certified) | 0.0024433 | 0.0019079 | 0.0012228 |
| 1/2 | 0.0023500 | 0.0019070 | 0.0011761 |
| 1 | 0.0022636 | 0.0019042 | 0.0011329 |
| 2.2077367 (the band's lower end) | 0.0020789 | 0.0018902 | 0.0010404 |

## 2. The estimate (proved)

*The error equation.* Let m~ be the solver's interpolant (spectral in (r, x), the time integrator's in tau), phi~,
G~ likewise, and e = m_1 - m~, e_phi, e_G the errors. In the Cartesian components u of e in the Kerr-Schild
coordinates (tau, x^1..x^4) the closed system of LAMBDA0-DATA5.md 12.1 (S3) reads

    -(1/2) box~ u + A . du + B u + K_phi e_phi + K_G e_G = -rho_u,      (transports of e_phi, e_G with rho_phi, rho_G),

box~ = g0^ab d_a d_b componentwise (S2 and the Kerr-Schild form g0 = eta + (mu/r^2) dv dv), and A . d + B := E -
P_eta, P_eta(m) := -(1/2) g0^ab nabla^eta_a nabla^eta_b m, which in Cartesian components is -(1/2) box~ m exactly
(the Christoffel symbols of eta vanish there). rho_u is the residual of (m~, phi~, G~) in the mean equations; the
data errors on Sigma enter as E(tau0).

*The energies.* Lemma 9.1's E(tau) = int T(Y, Y) dx over the slice D_tau = {rho(tau) <= r <= 3 - tau}, summed over
the components of u; F(tau) = int (1 + m) |u|^2 dx, the zero-order current |u|^2 Y; W(tau) the L^2 energies of
e_phi, e_G along their transports. Q, q_lo(x) its least eigenvalue, c_Y = (sup Y^T Q^-1 Y)^(1/2) = 2^(1/2) and kappa~
are as in stage1rate5 K2 and Lemma 9.1.

**Lemma 1.** With alpha(tau) := sup_(D_tau) ||A||_op q_lo^(-1/2) (Euclidean operator norm of A on the derivative
vector), beta(tau) := sup ||B||_op (1 + m)^(-1/2) and gamma(tau) := sup of the coupling norms against W^(1/2),

    (E^(1/2))' <= (1/2) (kappa~ + c_Y alpha) E^(1/2) + (c_Y/2) (beta F^(1/2) + gamma W^(1/2) + ||rho_u||),
    (F^(1/2))' <= sigma E^(1/2) + delta F^(1/2),        W^(1/2) by the transports' own Gronwall bound,

with sigma, delta the sup norms of |Y|/((1 + m) q_lo)^(1/2) and of div Y/(2(1 + m)). *Proof.* Lemma 9.1 gives dE/dtau
<= kappa~ E + c_Y E^(1/2) ||f|| for -(1/2) box~ u = f, the lateral fluxes dropped (their signs are those Lemma 9.1
proves for the null boundaries). Here f = -(A du + B u + K e + rho_u). Pointwise |A du| <= ||A|| |du| <= ||A|| (du^T Q
du / q_lo)^(1/2), so ||A du||_(L^2) <= alpha E^(1/2); |B u| <= ||B|| (1 + m)^(-1/2) ((1 + m)|u|^2)^(1/2), so ||B u|| <=
beta F^(1/2); the couplings likewise. For F: d_a (|u|^2 Y^a) = 2 u . Y(u) + |u|^2 div Y, and its flux through the
null boundaries is >= 0 (Y future timelike, the conormal future causal), so F' <= 2 F^(1/2) sigma' E^(1/2) + ... with
|Y(u)| <= |Y| |du| <= |Y| q_lo^(-1/2) (du^T Q du)^(1/2). Divide by 2 E^(1/2), 2 F^(1/2). []

**Corollary 2 (the comparison).** The vector x = (E^(1/2), F^(1/2), W^(1/2)) satisfies x' <= K(tau) x + g with K's
off-diagonal entries >= 0, g = (c_Y/2)(||rho_u||, 0, ||rho_w||-terms). So x(tau*) <= X(tau*), X the solution of X' =
K X + g, X(tau0) = x(tau0), and the bound the estimate delivers for E^(1/2)(tau*) is X_1(tau*) >= (c_Y/2) int_(tau0)
^(tau*) e^(int_s^(tau*) K_11) ||rho_u(s)|| ds (all terms are >= 0), K_11 = (kappa~ + c_Y alpha)/2.

**Corollary 3 (the point value).** With E_s the energies commuted with the rotations of S^3 and with d_tau up to
order s >= 3 (s > 2 on the four-dimensional slice; the commutators bring the first derivatives of A, B, K), the same
construction gives a vector X_s whose first entry dominates the uncommuted one, and |e(X*)| <= C_pt X_s(tau*), C_pt
the point-evaluation constant of E_s's norm on the tau* slice. Then |M_22 - M~_22| <= C_pt X_s(tau*), and m_lo =
|M~_22| - C_pt X_s(tau*).

*Lower bounds on the estimate's own constants* (deduced). (i) K_11 >= (c_Y/2) alpha and alpha(tau) >= |A_(tautau;
e_r tautau)(tau, r)| q_lo(tau, r)^(-1/2) at any point (tau, r, th) of D_tau, one entry of one row of A bounding its
operator norm from below. (ii) C_pt >= (int_(slice) (1 + m))^(-1/2): the constant field u = e_tau e_tau has |e(X*)| = 1
and E_s^(1/2) = (int (1 + m))^(1/2). Hence the estimate's bound is at least

    C_pt (c_Y/2) int_(tau0)^(tau*) e^(Lambda(s)) ||rho_tautau(s)|| ds,    Lambda(s) = int_s^(tau*) (c_Y/2) alpha_lo,

and m_lo > 0 requires that this be below |M~_22| = 2.207738.

## 3. What is certified

- **X1** (computed, exact): the tau-tau row of A . d + B on the Cartesian scalar T = m(d_tau, d_tau) (with m_vr =
  m_taur - T, m_rr = m_rr' - 2 m_taur + T, e_tau = d_tau, e_r = d_r at fixed tau): the principal parts cancel, there
  is no d_th T, and

      L_tautau = (mu' r - mu/2)/r^3 e_tau T + (5 mu/2 - mu' r)/r^3 e_r T + (2 mu^3 - mu^2 r^2 + mu mu' r^3 - mu' r^5)/r^8 T
                 + (the other components).

  At X* (r = a, mu ~ 1.1) the e_r entry is about 146 and the zero-order one about 1e5. Control C1: P_eta without its
  factor 1/2 leaves second derivatives (the cancellation fails).
- **X2** (certified, exact rationals): an upper envelope rho^ >= rho of the ray through X*, backwards from (tau*, a^) in
  2000 pieces with slopes (m_hi - 1)/(m_hi + 1), m_hi = mu_end/rho^2, rounded up; rho^(tau0) = 1.067222 (the ray itself
  is at 0.987). Control C2: slopes taken at each piece's end fail the supersolution test.
- **X3** (certified, Arb): on each piece, at r = rho^ (a point of the slice; checked), with mu >= 1, mu' <= (2/9) c^2
  and q_lo bounded above over m in [1/r^2, mu_end/r^2] on 16 sub-intervals:

      int_(tau0)^(tau*) (c_Y/2) alpha dtau >= 32.8392,     so  e^(int K_11) >= 1.828 x 10^14,

  half of it gathered after tau = 1.51. Control C3: the same bound at the outer boundary r = 3 - tau gives e^0.527 =
  1.69, so X3's threshold (10^12) fails there: the factor comes from the inner region near X*.
- **The requirement** (deduced, the numbers certified): C_pt >= (int (1 + m))^(-1/2) >= 0.1803 (vol = 12.806, int m <=
  17.97 with m <= mu_end/r^2), c_Y/2 = 2^(-1/2); so m_lo > 0 needs int e^(Lambda(s)) ||rho(s)|| ds < 17.32.

## 4. What is not certified, and why

*The upper bound on C_stab.* It needs sup over every cell of ||A||_op q_lo^(-1/2), ||B||, the couplings and their
first derivatives, in Cartesian components. The class reduction does not determine them: for T^2-invariant fields the
Cartesian derivatives along the phi directions are zero-order in u (rotation generators), so the extracted equations
fix only A_phi . (Omega u) + B u in combination, and an operator norm needs A and B separately. That requires the
extraction for a general tensor in Cartesian components, not done here. It cannot change the conclusion, since X3 is a
lower bound on it.

*The certified residual.* X6 (certified, Arb) evaluates the tau-tau residual of the 48 x 16 interpolant at the slice
tau ~ -0.8 in Arb balls: the interpolant is the 2D Chebyshev series through the nodal values, mu is enclosed by
certified quadrature of env^2 (python-flint's Petras integrator, the tails beyond |y| = 1 - 10^-4 bounded), c from its
defining integral (1.324087298710302 +/- 5e-28). At collocation nodes it reproduces the solver (|rho| < 1e-12), at the
midpoints it is certified nonzero (values in the output). On a box of half-width delta the enclosure's radius grows as
(slope) delta, the slope ~ 13 in the test; for the radius the estimate needs there (~3e-13) delta ~ 2e-14, about 10^27
boxes per slice and 10^30 over the run's slices; for 1e-6 (a dual-weighted residual's level) about 10^14 boxes per
slice (output). An evaluation takes ~0.03 s, so the first-order interval route is not a cost any machine meets; LAMBDA0-
DATA5.md's R2 counted evaluations, not this sharpness. What would reach it: Taylor or Chebyshev models of high order
in (tau, r, x) with certified remainder bounds, whose cost grows with the order and the number of coefficient
functions (202) and is not a multiple of R2's.

*The resolution* (computed, floating point, X4). The residual's tau-tau component falls with resolution (its L^2
norm at tau = -0.8: 1.7e-5 at 32 x 12, 6.4e-7 at 48 x 16, 2.3e-8 at 64 x 20), and the estimate's integral with it.
From the last two grids one step (+16 in r, +4 in x) divides the integral by 27.4, so it would fall below 17.32 after
3.2 more steps, about 128 x 36, a run of about 8 hours here (scaling Nr^3 Nx (Nr + Nx) from 64 x 20's 1023 s). It
is a necessary condition: X3's factor is a lower bound, rho_tautau one component, and the residual measured.

## 5. What holds

m_lo is not reached: the estimate's own constant is certified to be at least 1.83 x 10^14, the residual it would need
is about 10^-13 where the solution's early growth begins, the solver's residual is 4.2 x 10^4 times too large at 64 x
20, and the residual is certified pointwise only. lambda0's certified bounds, 0.0024433 / 0.0019079 / 0.0012228,
stand; M_22 = 2.207738 (computed, floating point; LAMBDA0-DATA5.md sections 12-13) is unchanged; the 64 x 20 run of X4
gives 2.207737966, 1.1e-7 from it, inside the band.

## 6. Program

`checks/m22cert5.py --selftest` (output `checks/m22cert5.out`, **10/10**): X1 (exact), X2, X3 (certified), X4
(floating point), X5 (computed), X6 (certified); controls C1-C4. Imported, not copied: m22evol5.py (the system, the
solver, the data, the chain). READ: stage1rate5 K2 (Q, c_Y), envelope5.out E1 (c's upper end, used in X3), Lemma 9.1.
md5: program PROGMD5, output OUTMD5.
