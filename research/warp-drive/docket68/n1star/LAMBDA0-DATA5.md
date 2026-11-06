# LAMBDA0-DATA5 -- the stage-1 data on Sigma, the envelope, and X*'s past (workstream D, after round 8)

*Status (2026-11-06).* New; not yet read by a verifier. It takes the three blocks CONSTANTS5.md R8.2 records on
lambda0 (and R9.5 keeps): (a) S_1 and B_1, the second-order constraint expansion of the stage-1 data on Sigma; (b) the
stability constant over X*'s past; (c) an admissible envelope. Labels as in the record: **proved** (an argument
written here, every step checked), **computed** (a program, exact unless it says floating point; **certified** for Arb
balls or exact rationals), **deduced** (an argument from cited lines), **READ** (quoted or cited), **reduced to X**
(what is left, named). One program, `checks/lam0data5.py` (`--selftest`; output `checks/lam0data5.out`), every check
named and printed, six controls that mutate the computed path and fail as they must. CONSTANTS5.md, N1STAR-PROOF.md
and the paper are not edited. [Section 12 adds a second program, `checks/m22evol5.py` (output `checks/m22evol5.out`):
the stage-1 evolution extracted, checked exactly and solved, and M_22's floating value.]

## 0. Summary

- **(a) S_1 and B_1** (computed, exact; D3-D4): closed forms (3.2)-(3.3), the linear part being data5.py's
  linearisation. **Check** (computed, floating point; D6): at lam = 1/32 and 1/64 the true constraint residual minus
  lam <Phi^(1)> falls as lam^2 (orders 1.92-2.03 in all nine cases).
- **The data on Sigma** (reduction exact, D5; solution floating point, D7): the stage-1 constraint system splits into
  three ODEs per harmonic (5.2); solved for round 2's envelope, sup |a| = 9.7e-7 on the slice. **The drop** (D8): with
  those data the residual's mean falls from order lam to lam^2.
- **The Cauchy data of stage 1** (computed, exact, D2, D4; assembled, deduced, Section 6): complete on Sigma, m_1,
  d_tau m_1, phi_1, Psi_1 and gh_2 with both its harmonics.
- **(c) The envelope** (proved; E1): envelope5.py's env is C_c^oo on [1/2, 7/2] with the numerics' integral, and it is
  the envelope the certified lambda0 bounds already use.
- **(b) The constant** (certified; G1-G3): over X*'s past, read by domain of dependence, the principal-part factor
  5.103e10 becomes <= 1391.72.
- **M_22**: not enclosed, 0 not decided; reduced to a validated solve of the stage-1 evolution on X*'s past
  (Section 8). **lambda0**: not lowered; 0.0024433 (operator norm) stands.
  [Section 12: the stage-1 evolution is now extracted (exact, S1-S4) and solved on X*'s past; M_22 = 2.207738
  (computed, floating point; error estimate 1.4e-7), positive, not enclosed. lambda0's three certified bounds stand;
  the floating value would sharpen them to 0.0020789, 0.0018903 and 0.0010404 (not certified).]
  [Section 13: confirmed by an independent reader; n1, 0.0018902; the value pinned by a second discretisation (N4)
  and the mean equations checked by N3b; no certified lower bound on |M_22| is reached (13.3).]

What the round-8 text says that is now false: "neither the record nor this supplement has S_1 or B_1 in closed form or
in a program" (R8.2) and, in R8.7/R9.7 block 3, "whose data on the initial slice are not computed". Section 10 gives
the corrected text as an old/new pair; lambda0 itself is not reached, so it is offered as a correction, not as the
lambda0 replacement the commission asks for if lambda0 is reached.

## 1. Setting (READ N1STAR-PROOF.md 0.1, 5.2, Lemmas 5.3, 6.1, 6.2, by content)

Kerr-Schild coordinates (tau, r, th, phi1, phi2), g0 = eta + (mu(v)/r^2) dv dv, v = tau + r, ell = g0^-1 dv = -d_tau
+ d_r; Sigma = {tau = tau0}, where v = tau0 + r and the phase is s = v/lam. The approximant (5.1) at stage 1:

    g_app = g0 + lam W(X, u/lam) + lam m_1 + lam^2 gh_2(X, u/lam) + (orders lam^2 and higher, means and gh_3),
    u = v + lam phi_1 + ...,   W = W_TT + chi dv dv   (lead5.py's W_TT, amplitude A E(v) H(th) r^(-3/2)).

Lemma 6.2 at m = 1 fixes on Sigma: phi_1 = 0 and (m_1)_(tau .) = 0, h_1 = a dr dr (the spatial part of m_1), so by
Lemma 5.3 (b) d_tau phi_1 = -(1/2) m_1(ell, ell) = -a/2; chi = 0 there with its tangential derivatives (stage 0's
data); gh_2 by step (i) (F1 at order 1); the tau-derivatives of (m_1)_(tau .) by step (ii); and the order-1 mean of
the second fundamental form is the free datum Q_1 = w Pi + q (dr dth + dth dr) ("given h_m, Q_m fixes d_tau of that
spatial part"). The constraint map is (J, rho) = (2(-div K + d tr K), R - |K|^2 + (tr K)^2) as in data5.py, with K =
(d_tau gamma - L_beta gamma)/(2N). In the symmetry class every field is a function of (r, th) (and s), C = cos th,
S = sin th, Lambda := r^2 + mu, and the record's H is H = (C^4 + S^4)^(-1/2) = (2/(1 + cos^2 2th))^(1/2) (D5).

**The method** (computed, `lam0data5.py`). Every field is a series {(k, n): coefficient of lam^k z^n}, z = e^(is),
differentiated along Sigma by d_r -> d_r + d_v + lam^-1 d_s and, for oscillating profiles, in tau by d_v + (lam^-1 +
d_tau phi_1) d_s; products are cut at lam^1, gamma^-1 is kept to lam^2. The cut loses nothing in the order-1 mean
(deduced, printed as DOC): a dropped lam^2 coefficient of Gamma, K or tr K reaches order 1 only through one fast
derivative and is multiplied there by g0^-1, not oscillating, so its mean is zero; gh_2 (lam^2, oscillating) is kept,
because one fast derivative brings it to order 1 against the oscillating d_s W; gh_3 reaches order 1 only through d_s^2
against g0^-1; m_2 and d_tau phi_2 stay at order 2.

## 2. Step (i) at m = 1: gh_2 on Sigma

**Proposition 2.1** (computed, exact; D1-D2). On Sigma: (a) D^(0) = 0; (b) for every gh_2 in the class (harmonics 1
and 2) the gh_2-part of D^(1), lowered by g0, is Pol(d_s gh_2), Pol(Y) = Y(ell, .) - (1/2) dv tr_g0 Y; (c) the first
harmonic of D^(1) at gh_2 = 0 has only a th component and does not depend on h_1: Lambda_1(h_1) = 0 in the class;
(d) Pol^+ = Pol^T (Pol Pol^T)^-1 (Euclidean in the Cartesian (tau, x), the record's choice) maps the class covector
(0, 0, c) (components tau, r, th) to the class tensor whose (tau th) component is -c/2 and (r th) component c/2, every
other component 0. Hence, solving Pol(d_s gh_2) = -(the rest of D^(1)'s oscillating part), gh_2 on Sigma is

    first harmonic:   gh_2(tau th) = -gh_2(r th) = (A E/(6 r^(3/2))) [ (5 H sin 2th + 2 S^2 H') cos s
                                                                       + (5 H sin 2th - 2 C^2 H') sin s ],   (2.1)
    second harmonic:  gh_2 = (A^2 E^2 H^2/(6 r^3)) (cos 2th cos 2s - (1/4) sin^2 2th sin 2s) Pi,              (2.2)

Pi = r^2 (dth^2 + C^2 dphi1^2 + S^2 dphi2^2), every other component 0 (the second harmonic takes chi's d_tau on Sigma
from stage0bd5.py's closed form of chi, READ; d_v of its factor r^-2 - (v - tau0)^(-1/2) r^(-3/2) is (1/2) r^-3 there).

*Proof.* (a)-(b) and (d) are exact identities (sympy), (c) is the computed first harmonic. (c) is also seen directly:
the terms of D^(1) bilinear in (m_1, d_s W) or (d phi_1, d_s W) are contractions of d_s W with ell, with the trace or
with g0^-1(dtau) = (-1 - m, m, 0, 0, 0), and W is angular, transverse (W(ell, .) = 0) and traceless (lead5 L5). []

## 3. The order-1 mean of the constraint map: S_1 and B_1

**Theorem 3.1** (computed, exact; D3-D4). For the slice data of the stage-1 approximant (Section 1 with (2.1)-(2.2)):

(i) the constraint map has no lam^-1 term, and its order-0 mean is proportional, in every component, to mu' - (2/9)
A^2 E^2 H^2 (C^4 + S^4) (it vanishes exactly under stage 0's energy condition, lead5 L2);

(ii) its order-1 mean is

    <Phi^(1)> = P(h_1, Q_1) + B_1 a - S_1,                                                                   (3.1)

with P the linearisation of the constraint map at g0's data on Sigma -- equal, coefficient by coefficient, to data5.py's
lin_0 (40 digits at three rational points) --

    P_rho  = (3 r^3/Lambda^2) d_r a - (1/Lambda) Lap a
             + 3 (2 r^6 + 6 r^4 mu + 4 r^2 mu^2 + 2 mu^3 - 2 mu' r^5 - mu' r^3 mu)/(r^2 Lambda^3) a
             - 3 (mu' r^3 + 2 mu^2)/(r^2 Lambda^(3/2)) w,
    P_Jr   = 6 d_r w + (6/r) w - (2/r^2) div(q dth) - 3 (mu' r^3 - 4 r^2 mu - 2 mu^2)/(r Lambda^(5/2)) a,
    P_Jth  = -(2 r^2/Lambda) d_r q - r (6 r^2 + 8 mu - mu' r)/Lambda^2 q + 4 d_th w
             + r^2 (mu' r - 2 mu)/(2 Lambda^(5/2)) d_th a,

Lap a = d_th^2 a + 2 cot 2th d_th a and div(q dth) = d_th q + 2 cot 2th q on the T^2-invariant fields of S^3, and

    B_1 a = H^2 (C^4 + S^4) A^2 E^2 a ( -(1/3) Lambda^(-3/2),  0,  (2/3) r Lambda^-2 )   in (J_r, J_th, rho),     (3.2)
    S_1   = ( 0,  -A^2 E^2 H^2 sin 2th / (3 r^2 Lambda^(1/2)),  0 ).                                            (3.3)

(iii) B_1 is algebraic in h_1 (no other coefficient of (3.1) carries A); the phase d_tau phi_1 = -a/2 carries the part
(-(1/3) r^-4 Lambda^(1/2), 0, (1/3) r^-3) A^2 E^2 H^2 (C^4 + S^4) a of it; gh_2's first harmonic (2.1), any second
harmonic of gh_2 (generic, in all seven class components that enter the slice data, so (2.2) among them) and chi's
d_tau contribute nothing to (3.1) (each recomputed with it off or on).

So Lemma 6.2 (iii) at m = 1 reads P(h_1, Q_1) + B_1(h_1) = S_1 with these S_1 and B_1. In the record's class and
with the record's H, B_1 is round: H^2 (C^4 + S^4) = 1, and A^2 E^2 = (9/2) mu'. S_1 has only a J_th component; it is
the constraint-side counterpart of stage 1's mean source S = -(4/9) A^2 E^2 H^2 sin 2th r^-3 (dv dth + dth dv) (READ
stage5.out S2): both are momentum along th, odd under th -> pi/2 - th.

*Proof.* (i)-(iii) are the computed series of Section 1 (`lam0data5.py` D3-D4), whose order-1 mean is complete by the
DOC argument; the comparison with data5.py's lin_0 is an independent implementation of P. []

**K's order-1 mean** (computed, exact; D4). With d_tau h_1 = 0 the metric gives K's order-1 mean M1, linear in (a,
d_r a, d_th a), with no W^2 term:

    M1_rr = mu [2 r^5 Lambda d_r a + (2 mu^3 + 4 mu^2 r^2 + 4 mu r^4 - 2 mu' r^5 - mu' mu r^3) a]/(4 r^6 Lambda^(3/2)),
    M1_rth = mu d_th a/(2 r Lambda^(1/2)),   M1 on the spheres = mu (2 r^4 - mu^2) a/(2 r^4 Lambda^(3/2)) Pi;

so the datum Q_1 is reached by d_tau h_1 = 2 N0 (Q_1 - M1), N0 = (1 + mu/r^2)^(-1/2). (The record's phrase "Q_m fixes
d_tau of that spatial part" is this formula.)

## 4. The check at finite lam (D6) and three controls

The evaluation shares nothing with the two-scale series: the slice data of g_app at a fixed lam (gamma, d_tau gamma
with the phase, the shift, the lapse; gh_2 by (2.1); d_tau h_1 = 2 N0 (Q_1 - M1)) are evaluated pointwise as
second-order jets in (r, th), and the constraint map is formed from them by its definition (Christoffel symbols, scalar
curvature, div K), with no series, no cut and no mean. (The data use (2.1) and M1, which the check therefore tests too:
a wrong M1 would leave K's order-1 mean off Q_1 and the remainder of order lam.) With E = 1 + v/4, mu' = (2/9) E^2,
the record's H, A = 1 and test fields a = (1/7 + cos 2th/5)(1 + r/10), w = r cos 2th/9 + 1/11, q = r sin 2th/13, the
weak residual W(lam) := int f(r) Phi_lam(r, th) dr against the Gaussian f of standard deviation 0.3 at r = 3.5 (every
oscillating term contributes O(lam^oo)) is compared with lam I1, I1 := int f <Phi^(1)> from (3.1):

| th | J_r: W - lam I1 at 1/32, 1/64 (p) | J_th (p) | rho (p) |
|---|---|---|---|
| 0.35 | -3.07e-6, -8.10e-7 (1.92) | 1.85e-4, 4.67e-5 (1.99) | 5.44e-4, 1.36e-4 (2.00) |
| 0.80 | 1.02e-5, 2.56e-6 (1.99) | 9.81e-5, 2.49e-5 (1.98) | 2.08e-6, 5.10e-7 (2.03) |
| 1.20 | 6.92e-6, 1.76e-6 (1.97) | -4.78e-5, -1.18e-5 (2.02) | 1.68e-4, 4.20e-5 (2.00) |

(computed, floating point; p = log2 of the ratio). Every remainder is of order lam^2: (3.1) is the order-1 mean of the
true residual. **Controls** (must fail, and do): C1, S_1 with its sign flipped: J_th's orders 1.19, 1.05, 0.94; C2, the
phase d_tau phi_1 = -a/2 dropped from the data: J_r's orders 0.99, 1.10 and rho's 0.97 at some th; C3, B_1 dropped
from the prediction: orders near 1 in J_r and rho. So the sign of S_1, the phase and B_1 are each seen by the check.

## 5. The stage-1 constraint system, mode by mode

**Proposition 5.1** (computed, exact; deduced; D5). With the record's H every coefficient of P + B_1 is independent of
th except the angular operators -(1/Lambda) Lap (in rho) and -(2/r^2) div (in J_r); Lap P_k(cos 2th) = -4k(k + 1)
P_k(cos 2th); and

    H^2 sin 2th = sum_(k >= 1) sigma_k d_th P_k(cos 2th),   sigma_k = -((2k + 1)/2) int_-1^1 atan(x) P_k(x) dx,  (5.1)

exact: sigma_1 = 3/2 - 3 pi/4, sigma_3 = -49/6 + 21 pi/8, sigma_5 = 583/15 - 99 pi/8, sigma_7 = -1371/7 + 1995 pi/32,
..., zero for even k (atan is odd), decaying like (1 + 2^(1/2))^-k (the Bernstein ellipse of atan, whose poles are at
+-i); |sum_(k<=11) sigma_k P_k + atan| <= 4.9e-6 on a 41-point grid of [-1, 1] (floating point). So with a = sum
a_k(r) P_k, w = sum w_k(r) P_k, q = sum q_k(r) d_th P_k (x = cos 2th; the class's covectors q dth are gradients of
class functions), the system P(h_1, Q_1) + B_1 a = S_1 is, mode by mode (e := A^2 E^2 = (9/2) mu'),

    (3 r^3/Lambda^2) a_k' + [4k(k+1)/Lambda + 2 (9 (Lambda^3 - r^2 mu^2) - e r^5)/(3 r^2 Lambda^3)] a_k
                          - 2 (e r^3 + 9 mu^2)/(3 r^2 Lambda^(3/2)) w_k = 0,
    6 w_k' + (6/r) w_k + (8k(k+1)/r^2) q_k - (e r (3 r^2 + mu) - 18 mu (2 r^2 + mu))/(3 r Lambda^(5/2)) a_k = 0,  (5.2)
    -(2 r^2/Lambda) q_k' - 2 r (27 r^2 + 36 mu - e r)/(9 Lambda^2) q_k + 4 w_k + r^2 (e r - 9 mu)/(9 Lambda^(5/2)) a_k
                          + e sigma_k/(3 r^2 Lambda^(1/2)) = 0,

mu = mu(tau0 + r), E = E(tau0 + r), from zero data at r = a; a_0 = w_0 = 0. Lemma 6.4's system is therefore a sequence
of linear 3 x 3 ODE systems in r: the parabolic part is a_k' = -4k(k+1) (Lambda/(3 r^3)) a_k + ..., the hyperbolic
pair (w_k, q_k) has speeds of order k (Lemma 6.3's c^2 = 2 Lambda/(3 r^4)). Lemma 6.4's solution exists, is unique
and smooth; the P_k(cos 2th) are a complete orthogonal basis of the T^2-invariant functions on S^3 (the measure C S dth
is dx/4, x = cos 2th), the d_th P_k one of the class covectors q dth (each the gradient of a class function), the
coefficients are th-free and Lap, div act diagonally, so the projections of that solution satisfy (5.2) with zero data
and are its unique solutions: the modes computed below are Lemma 6.4's solution, harmonic by harmonic (deduced).

**The data for round 2's envelope** (computed, floating point; D7). envelope5.py's env (c = 1.3240872987 by quadrature,
inside envelope5's certified [1.32407110621, 1.3241034918]), A = 1, mu0 = 1; (5.2) for k = 1, 3, ..., 11 by Radau
(rtol 1e-11, checked against 1e-9: differences below 3e-13) from zero data at r = 5/2 (below it E = 0 and the data
vanish) to 11/2, mu integrated beside them reaching 1.1822916666667 = 227/192. Sizes (sup over r and a th grid):

| region | sup \|a\| | sup \|w\| | sup \|q\| |
|---|---|---|---|
| X*'s past on Sigma, r <= 4 | 2.13e-7 | 1.99e-5 | 2.18e-3 |
| the slice, r <= 11/2 | 9.69e-7 | 1.32e-4 | 3.22e-3 |

So h_1 = a dr dr on Sigma is about 1e-6, where the data alone would need |a_1| > 12.37 to move the operator-norm bound
(R8.0 (6), classm5 K3): what R7.3 called implausible is now computed.

**The drop** (computed, floating point; D8). For E = 1 + v/4, (5.2) solved for k <= 11 from zero data at r = 1.1, the
data built from that solution as in Section 4; the weak residual (J_r, J_th, rho):

| th | stage-0 data: W(1/32), p | stage-1 data: W(1/32), p |
|---|---|---|
| 0.35 | (3.48e-6, 2.72e-4, -1.60e-6), (2.00, 1.00, 2.00) | (2.85e-6, -9.24e-7, -2.55e-6), (2.01, 2.10, 2.02) |
| 0.80 | (3.26e-6, 6.64e-4, -3.49e-6), (2.00, 1.00, 2.00) | (1.84e-6, -2.94e-7, -1.00e-5), (2.00, 3.71, 2.00) |
| 1.20 | (3.48e-6, 2.89e-4, -1.66e-6), (2.00, 1.00, 2.00) | (2.74e-6, 7.77e-7, -2.66e-6), (1.99, 1.91, 1.98) |

The stage-0 data carry the order-lam mean -S_1 in J_th (p = 1.00); with the stage-1 data it is gone (p >= 1.91): the
residual drops by the predicted order, and J_r, rho stay of order lam^2 in both.

## 6. The complete stage-1 Cauchy data on Sigma (deduced from Sections 2, 3, 5; D2, D4)

    m_1 = a dr dr,  (m_1)_(tau .) = 0;   d_tau (m_1)_(spatial) = 2 N0 (Q_1 - M1(a));   phi_1 = 0,  d_tau phi_1 = -a/2;
    d_tau (m_1)_(tau .) from step (ii): the mean of D^(1) on Sigma, with T := d_tau (m_1)_(tau .), H := d_tau h_1,
    m := mu/r^2, is
        tau:  -(1/2) [ (1 + m) T_tautau + (1 - m) H_rr + H_thth/r^2 + H_p1p1/(r C)^2 + H_p2p2/(r S)^2 ],
        r:    -(1 + m) T_taur + m H_rr + (1/2)(1 - m) d_r a + (3/r - mu/r^3) a,
        th:   -(1 + m) T_tauth + m H_rth - (1/2)(1 - m) d_th a,
    and (ii) sets these to 0 (coefficient -(1 + m) != 0);
    Psi_1 = box~ phi_1 on Sigma: from L0 phi_1 = -(1/2) m_1(ell, ell), d_tau^2 phi_1 = -(1/2) d_r a - (1/2)(T_tautau -
    2 T_taur + H_rr), so Psi_1 = (1 + m) [ (1/2) d_r a + (1/2)(T_tautau - 2 T_taur + H_rr) ] - m d_r a;
    gh_2 and Z = d_s gh_2 on Sigma: (2.1)-(2.2).

With (a, w, q) from (5.2) these are the data of Lemma 5.3 (a)-(c) at m = 1, all on Sigma, for round 2's envelope:
R8.2's step (S1) is done.

## 7. The envelope (step 2; proved, E1)

*Admissibility, from the record.* N1STAR-PROOF.md 0.1 and Theorem A: mu smooth, nondecreasing, mu >= mu0, constant for
v <= v_start and v >= v_end, mu' = (2/9) A^2 env^2; Theorem 1 asks env in C_c^oo (CONSTANTS5.md 1.1); the certified
lambda0 leaves depend on the envelope through mu_end = mu0 + (2/9) A^2 int env^2 = 227/192 (the numerics' integral
105/128, CONSTANTS5.md 1.1), and the certified C_app through env's peak c at v = 2 (R9.0 minor 2). The numerics'
sin^4 is C^3 and not C^4 at v = 1/2 (its fourth derivative there is 8 pi^4/27 from the right, 0 from the left: C4).

**Lemma 7.1** (proved). env(v) := c beta((2v - 4)/3), beta(y) = cos^12(pi y/2) exp(-y^2/(1 - y^2)) for |y| < 1 and 0
otherwise, c := ((105/128)/((3/2) int beta^2))^(1/2) (envelope5.py), is admissible: env is in C_c^oo with support
[1/2, 7/2], int env^2 = 105/128, max env = env(2) = c, and mu = mu0 + (2/9) A^2 int_(1/2)^v env^2 is smooth,
nondecreasing, constant outside [1/2, 7/2], with mu_end = 227/192.

*Proof.* exp(-y^2/(1 - y^2)) = e exp(-1/(1 - y^2)), so beta = e cos^12(pi y/2) phi(1 - y^2) with phi(t) = exp(-1/t)
for t > 0 and 0 for t <= 0. phi^(k)(t) = P_k(1/t) exp(-1/t) for t > 0 with P_0 = 1, P_(k+1)(x) = x^2 (P_k(x) - P_k'(x))
(induction: d/dt [P(1/t) e^(-1/t)] = t^-2 (P - P')(1/t) e^(-1/t)), and P_k(x) e^(-x) -> 0 as x -> oo, so every
derivative of phi tends to 0 at 0+ and phi is C^oo on R. Composition with 1 - y^2 and the product with the entire
cos^12 keep C^oo; phi(1 - y^2) = 0 exactly for |y| >= 1 and beta > 0 on |y| < 1, so supp beta = [-1, 1], supp env =
[1/2, 7/2]. int env^2 = c^2 (3/2) int beta^2 = 105/128 by the definition of c. beta <= 1 = beta(0), so max env = c at
v = 2. mu' = (2/9) A^2 env^2 >= 0 is smooth and vanishes outside [1/2, 7/2]. [] Computational support (E1): the
recursion for k <= 8 and the limits (sympy); the factorisation (sympy); beta's derivatives 1..8 at y = 1 - 1e-3 are
at most 1.44e-205 (60 digits), while sin^4's at v = 1/2 + 1e-3 reach 1.17e4 (C4); c lies in envelope5's certified
interval and the integrated mu of D7 ends at 227/192.

This envelope is the one every certified lambda0 leaf already uses (lzerotrace5's K_lo = c_lo a^(-3/2), R9.0 minor 2),
so M_22 for it is the number the operator-norm bound needs, and nothing has to be re-certified for the envelope.

## 8. M_22: what is decided, and what is not (step 2)

*The chain* (READ classm5 K1-K2, K4; R8.2). In the class m_1(X*) e_phi1 = M_22 e_phi1, M_22 := (m_1)_phi1phi1(X*)/a^2,
X* = (th = 0, v = 2, r = a, phi1 = phi2 = 0), tau* = 2 - a; C_app >= (4/3) K + |M_22| with (4/3) K >= 12.5934637 >
12.593309 (certified, recomputed in the chain check); an enclosure [lo, hi] of M_22 with 0 not in it would give lambda0
< 0.0024433 x 12.593309/(12.593309 + min(|lo|, |hi|)). C5 (control): at r = a + 1/100 the base fails, (4/3) env(2)
r^(-3/2) <= 11.9248313 < 12.593309, so the chain is tied to X*.

*Decided now.* The data of the evolution on Sigma (Section 6) for the fixed admissible envelope (Section 7); that the
data alone cannot move the bound (|a| ~ 1e-6 against 12.37, Section 5); and that the stability constant of the a
posteriori route over X*'s past is <= 1391.72 for the principal part, not 5.103e10 (Section 9).

*Not decided.* M_22 itself, and so whether 0 is excluded. M_22 is the value at X* of the solution of Lemma 5.3 (a)-(c)
at m = 1 -- the mean m_1 (eight class components, coupled by box~ componentwise, B-bar, C-bar of bbar5.py), phi_1 and
Psi_1 transported along ell, and Z = d_s gh_2 (harmonics 1 to 3) transported along ell with the couplings <Th gh_2>
and <Wm_phi(d phi_1)> -- on X*'s past in Omega, a 2+1-dimensional (tau, r, th) linear system driven by S (stage5.out
S2) and by the data of Section 6. This round extracted none of that system's coefficients as arrays and ran no solve
of it, floating point or validated; a value of M_22 is therefore not claimed even approximately. [Section 12
supersedes these two sentences: the coefficients are extracted and checked exactly (S1-S4), and the solve is done in
floating point, M_22 = 2.207738.]

**Reduced to:** a validated solve of the stage-1 evolution (Lemma 5.3 (a)-(c), m = 1) on X*'s past from the Cauchy
data of Section 6, for envelope5's envelope, with an enclosure of the point value (m_1)_phi1phi1(X*). With the domain
of dependence of Section 9 the tolerance its residual must meet, in the reading of classm5 K5 (principal part only),
is about 7.19e-4 |M_22| in Lemma 2.3's energy, before c_Y q^(1/2) (<= 2^(1/2) x 37.8, stage1rate5 K3), the
lower-order coefficients' rates (not computed: round 6's minor 9) and the Sobolev constant of the point evaluation;
it is not met, since no approximate solution exists here. Nothing weaker suffices (R7.3, R8.2: an upper bound on m_1
cannot raise a lower bound, and the data are too small, Section 5). [Section 12.5: an approximate solution now
exists; carried through c_Y q^(1/2) and any lower-order rate, the tolerance falls below what it reaches.]
[Section 13, m2: not for any rate -- for k <= 3 it stays above 1.1e-7; it does for a rate of the size 12.5
illustrates (k = 10), and k is not bounded, nor are the Sobolev and commuted-energy constants (13.2).]

## 9. Block (b): X*'s past by domain of dependence (step 3; certified, G1-G3)

**Lemma 9.1** (deduced). Let rho~ : [tau0, tau*] -> (0, oo) be continuous and piecewise linear, rho~(tau*) = a, with
rho~'(tau) >= (1 - m)/(1 + m) at (tau, rho~(tau)) wherever it is differentiable, m = mu/rho~^2. Let u solve -(1/2) box~ u
= f on Omega and E_~(tau) := int_(A(tau), r >= rho~(tau)) T(Y, Y) dx with Lemma 2.3's multiplier Y = -g0^-1 dtau (gt =
g0, as stage 1 needs). Then

    d E_~ / d tau <= kappa~(tau) E_~ + c_Y E_~^(1/2) ||f||_(r >= rho~(tau)),
    kappa~(tau) := sup_(r >= rho~(tau)) kappa(r),

kappa(r) the local rate (1/r) sup |lambda(r M, Q)| of stage1rate5 K2 (m in [mu0/r^2, mu_end/r^2], k in [0, (2/9)
c^2/r]), so the principal-part energy at X*'s slice grows from Sigma by at most e^(int_(tau0)^(tau*) kappa~).

*Proof.* Integrate stage1rate5 K2's identity d_a J^a = (1/2) T^(ab) pi_ab + (Y u)(box~ u + Gamma . du) over U =
{tau0 <= tau' <= tau, r >= rho~(tau')} in Omega. Its boundary is the two slices, Omega's lateral boundaries (fluxes
>= 0, dropped as in Lemma 2.3) and the surface r = rho~(tau'), with outward conormal N = rho~' dtau - dr. A future
causal vector P has dtau(P) > 0 and, since g0 = eta + m dv dv, its radial speed P^r/P^tau lies in [-1, (1 - m)/(1 +
m)] (the roots of (1 + m) x^2 + 2 m x + m - 1 <= 0); so N(P) = P^tau (rho~' - P^r/P^tau) >= 0, and the energy flux,
future causal by dominant energy, leaves U through that surface: its flux is >= 0 and is dropped. The bulk is bounded
pointwise by kappa(r) T(Y, Y) + c_Y T(Y, Y)^(1/2) |f| as in stage1rate5 K2, with r >= rho~(tau). Gronwall. []

**The numbers** (certified). G1: rho~ in 2000 pieces backward from (tau*, a) over 4 - a (an upper bound of tau* -
tau0), each slope sigma = (m_lo - 1)/(m_lo + 1) rounded down, m_lo = 1/(rho + dt)^2 (mu >= mu0 = 1 on Omega), checked
exactly piece by piece; rho~ reaches 0.984835 at tau0 (it approaches the horizon from inside, never crossing r = 1).
G2: kappa on 600 r-cells of [a, b(tau0)] in Arb (stage1rate5's forms, imported), 12.9289 at r = a, 6.67 above 1/2,
2.63 above 1, 0.68 above 2. G3: int kappa~ dtau <= 14.4766, so

    e^((1/2) int kappa~) <= 1391.72      against      e^(kappa Dtau*/2) <= 5.103 x 10^10 (classm5 K5),

smaller by 3.67 x 10^7. C6 (control): slopes 1.25 times steeper than the outgoing null rays fail the exact check.

So the record's only stability constant, read on X*'s past instead of the whole slab, is about 1.4 x 10^3 for the
principal part. The whole system's constant needs the lower-order coefficients' rates (B-bar, C-bar, the couplings to
phi_1, Psi_1 and Z), which the record does not compute; Lemma 9.1 applies to them unchanged (the transports, along
L0 = -ell, radial speed -1, leave the region through r = rho~ as well), so their rates add to kappa~ on the same region.

## 10. Step 4, and the replacement text

*Step 4 is not reached:* 0 is not excluded for M_22 by any computation here, so no lambda0 bound follows beyond the
certified 0.0024433 (operator norm), 0.0019079 (Frobenius) and 0.0012228 (largest entry), which stand unchanged (they
are statements about round 2's envelope, which is the envelope of Section 7).

*The replacement text.* The commission asks for an old/new pair for R8.7's "Physical wavelengths (lambda0)" new block
if lambda0 is reached. It is not; but that block's last clause, "whose data on the initial slice are not computed", is
now false, in R8.7 and in R9.7, which replaces R8.7 and carries the same clause. Two pairs follow, one for each; each
old text occurs exactly once in CONSTANTS5.md as it stands (checked by content), and each new text claims only what
this file proves or computes. R9.7's (the current proposal):

```old
needs a validated solve of the first stage for that envelope, whose data on the initial slice are not computed. And
  a high-frequency theorem, whose expansion parameter is λ over the
```

```new
needs a validated solve of the first stage for that envelope. Its data on the initial slice are now computed: the
  second-order constraint expansion in closed form, solved harmonic by harmonic (supplement
  `docket68/n1star/LAMBDA0-DATA5.md`, `checks/lam0data5.py`), and too small to move the bound by themselves; over that
  point's past the energy estimate's growth is at most 1.4 × 10³ by domain of dependence (certified), against 5.1 ×
  10¹⁰ over the whole slab, before the lower-order terms. The solve itself is not done. And
  a high-frequency theorem, whose expansion parameter is λ over the
```

R8.7's (if R8.7 rather than R9.7 is used):

```old
fixed smooth envelope, whose data on the initial slice are not computed. And a high-frequency theorem, whose
  expansion parameter is λ over the
```

```new
fixed smooth envelope, that of supplement `checks/envelope5.py`. Its data on the initial slice are now computed:
  the second-order constraint expansion in closed form, solved harmonic by harmonic (supplement
  `docket68/n1star/LAMBDA0-DATA5.md`, `checks/lam0data5.py`), and too small to move the bound by themselves; over that
  point's past the energy estimate's growth is at most 1.4 × 10³ by domain of dependence (certified), against 5.1 ×
  10¹⁰ over the whole slab, before the lower-order terms. The solve itself is not done. And a high-frequency theorem,
  whose expansion parameter is λ over the
```

"Certified" in the new texts refers to the principal-part factor (G3); "computed" to the closed forms (exact) and the
solved data (floating point), Sections 3 and 5. [CONSTANTS5.md R12.7 pair 3 has since carried this correction; the
final pairs, with M_22's floating value, are in Section 12.6.]

## 11. Programs, pass counts, what remains

`checks/lam0data5.py --selftest` (output `checks/lam0data5.out`, **18/18**; about 11 minutes on the loaded machine):
D1-D8 (Sections 2-6), E1 (Section 7), G1-G3 (Section 9), and controls C1-C6, each mutating the computed path: C1 S_1's
sign (D6 fails), C2 the phase dropped from the data (D6 fails), C3 B_1 dropped from the prediction (D6 fails), C4 the
numerics' sin^4 (E1's smoothness fails), C5 X* moved to r = a + 1/100 (the chain's base fails), C6 slopes 1.25 times too
steep (G1's future-boundary check fails). Imported, not copied: data5.py (lin_0), stage1rate5.py (the energy forms, the
domain constants). READ: envelope5.out E1 (c's interval), lzerotrace5.out T3 (12.593309), classm5.out K5 (5.103e10),
stage0bd5.py (chi's closed form), stage5.out S2 (stage 1's mean source).

*Labels.* Proved: Lemma 7.1. Computed, exact: Proposition 2.1, Theorem 3.1, Proposition 5.1's reduction and sigma_k,
M1, step (ii). Computed, floating point: D6 (the check), D7 (the data), D8 (the drop). Certified: G1-G3, the chain's
base. Deduced: the DOC cut, Section 6's assembly, Lemma 9.1, the tolerance.

*What remains, with its single missing input.* lambda0 below 0.0024433 needs a certified enclosure of M_22, 0
excluded; the single missing input is now **a validated solve of the stage-1 evolution system (Lemma 5.3 (a)-(c), m
= 1) on X*'s past from the Cauchy data of Section 6, for envelope5's envelope** -- the system's coefficient arrays,
an approximate solution, and its residual below about 7.19e-4 |M_22| in the energy of Lemma 9.1 once the lower-order
rates and the point evaluation's Sobolev constant are added. The data on Sigma, the envelope and the principal-part
constant are no longer missing. [Section 12: the coefficient arrays and an approximate solution now exist
(`checks/m22evol5.py`, 13/13); the residual bound is what does not close (12.5), and the route ends at the floating
value.]

## 12. The stage-1 evolution solved, and M_22 (`checks/m22evol5.py`)

*Status (2026-11-06).* New; not yet read by a verifier. It supersedes what Sections 0, 8, 10 and 11 say of M_22 (each
marked there): the stage-1 evolution system is now extracted, checked exactly and solved on X*'s past, and M_22 has a
floating-point value. It is not enclosed: the validated solve does not close at a cost this machine can meet (12.5),
so lambda0's certified bounds stand unchanged, and the sharpened bounds M_22 gives are stated as computed, not
certified. Program: `checks/m22evol5.py` (`--selftest`; output `checks/m22evol5.out`, **13/13**), the companion of
lam0data5.py whose data on Sigma it evolves and whose functions it imports.

### 12.1 The system (computed, exact; S1-S4)

Lemma 5.3 (a)-(c) at m = 1 (READ by content) is read off the two-scale expansion of Ric^H(g_app) in lead5.py's ingoing
Eddington-Finkelstein coordinates (v, r, th, phi1, phi2), g_app = g0 + lam (W + m_1) + lam^2 gh_2(X, u/lam), u = v +
lam phi_1, W = W_TT + chi dv dv (chi stage0bd5.py's closed form): a series in lam^k z^n (z = e^(is)) and in d, the
degree in the unknowns -- m_1's eight class components, phi_1, gh_2's eight components at the harmonics +-1, +-2, +-3
-- cut at k <= 1 and d <= 1. The stage-1 system is the order-1 coefficient's part of degree <= 1 at every harmonic
(its degree-2 part is the e_2 term the lemma leaves to stage 2), with e_1 = 2 ell.d phi_1 - m_1(ell, ell) = 0, ell =
d_r (Lemma 5.3 (b)). The coefficients are extracted as sympy expressions and checked exactly:

- **S1** (stage 0, verified): the six non-class components vanish to order 1, and so does order lam^-1; the order-0
  coefficient's degree-1 part vanishes once e_1 = 0, in every component and harmonic (8 m_rr coefficients are live
  before e_1 is used, so the check is not vacuous); its degree-0 part vanishes except in vv at harmonic 0, where it is
  nonzero for a general mu' and zero under the energy condition mu' = (2/9) A^2 E^2 H^2 (C^4 + S^4).
- **S2** (the structure): each mean equation's principal part is -(1/2) g0^ab d_a d_b = -d_v d_r - (f/2) d_r^2 -
  (1/(2 r^2)) d_th^2 on its own component, with no second derivative of another; each equation at the harmonic n = 1,
  2, 3 carries the transport -i n d_r of its own gh_2 component and no derivative of another; the mean's known source
  is S = -(4/9) A^2 E^2 H^2 sin 2th r^-3 in v th alone (stage5.out S2's, READ, recovered here independently).
- **S3** (the closed subsystem; deduced from the exact structure): the mean equations see gh_2 only through its first
  harmonic in (r th, th th, phi1 phi1, phi2 phi2) and its second in r r; each r r equation (n = 1, 2, 3) is a
  homogeneous transport of gh_2(r r) at its own harmonic, which is zero on Sigma, so gh_2(r r) = 0; and the first-
  harmonic equations of the four see no other gh_2 component but r r. So (m_1, phi_1, those four) is closed: eight wave
  equations, one transport (2 d_r^EF phi_1 = (m_1)_rr) and four complex transports along ell, the rest of gh_2
  slaved to it.
- **S4**: the first harmonic of the gauge vector D^(1), lowered, is algebraic in gh_2's first harmonic, m_1 and d_th
  phi_1; its r component is gh_2(r r) alone, its th component carries the known source and gh_2(r th). It is the
  diagnostic N3: zero on Sigma by (F1) and not imposed by the solve, it propagates by the contracted Bianchi identity,
  so its staying small is a check on the solved equations and their coupling.
  [Section 13, m1: on the four gh_2 transports, (m_1)_rth and d_th phi_1 only; N3 is unchanged under C1 and does
  not see the mean equations, which N3b, the harmonic-0 part, now checks (13.1).]

### 12.2 The solve (computed, floating point; N1-N3)

Kerr-Schild time tau = v - r, from tau0 = -2 to tau* = 2 - a. The region is X*'s past cut at the null surface v = 3: r
between the outgoing null ray through X* (integrated backwards in floating point, DOP853) and 3 - tau. Both boundaries
are null; every null mode of the system leaves through them or runs along them, so no boundary condition is imposed, and
the domain of dependence makes the cut harmless (N2). Discretisation: Chebyshev-Lobatto in r in the frame moving with
the boundaries, the wave equations in first-order form (psi = d_r m_1); Chebyshev-Gauss in x = cos 2th, with the
axis-regular variables h_vth/sin 2th, h_rth/sin 2th, h_thth, (h_thth - h_p2/S^2)/S^2 and (h_thth - h_p1/C^2)/C^2 (and
their counterparts for gh_2), whose th-jets are formed by the product rule from exact factors; RK4 with step L(tau)/Nr^2
(cfl 1), L the domain's width. Data: Section 6 (D2, D4, D5, D7) on the solver's grid, for envelope5's envelope; gh_2's
first harmonic by (2.1).

| Nr x Nx (cfl) | M_22 | | Nr x Nx (cfl) | M_22 |
|---|---|---|---|---|
| 24 x 12 | 2.208069251 | | 32 x 12 (1/2) | 2.207746494 |
| 32 x 12 | 2.207746494 | | 32 x 16 | 2.207741160 |
| 40 x 12 | 2.207743389 | | 48 x 16 | 2.207738078 |
| 48 x 12 | 2.207743412 | | 32 x 20 | 2.207741048 |

Radial refinement changes M_22 by 3.2e-4, 3.1e-6 and 2.3e-8 (Nr 24 to 32 to 40 to 48), angular refinement by 5.3e-6
and 1.1e-7 (Nx 12 to 16 to 20); the angular change is the same at Nr = 32 and 48 to 2e-11, and halving the step changes
M_22 by 7.3e-11: spectral convergence in both directions, the time error negligible. So (**N1**, computed, floating
point)

    M_22 = 2.207738   (48 x 16), error estimate 1.4e-7 (the last radial, angular and time changes summed),

and the band [2.207737, 2.207739], ten times that, lies 1.6 x 10^6 half-widths from 0: M_22 > 0. Each coarser run sits
outside the band by its own truncation in the direction it is coarse in, which is what the band measures. The value is
not an enclosure: the error estimate is the observed change under refinement, not a bound.
[Section 13, n3: the band rounded outward is [2.2077367, 2.2077395]. m4: the value is now pinned by a second
discretisation and an independent readout, N4 (13.4).]

**N2**: with the outer boundary at v = 2.6 instead of 3 (X*'s past lies in v <= 2), M_22 = 2.207743412 against
2.207743389 at 40 x 12, a change of 2.3e-8, inside the band's half-width. **N3**: the gauge diagnostic, zero on Sigma
to 2.2e-16 by (F1), stays below 3.1e-6 of its terms' size at mid-solve (tau = 0.54) and below 2.3e-7 at tau* on 48 x
12, 48 x 16 and 32 x 20, and falls with Nr as M_22's radial error does (1.9e-4, 3.1e-6, 3.2e-9, 1.1e-9 at mid-solve
for Nr = 24, 32, 40, 48): the solution respects a consequence of the Bianchi identity that the solve does not
impose.
[Section 13, n2: N2's 2.3e-8 is Nr = 40's radial truncation; the v = 2.6 run agrees with 48 x 12 at v = 3 to
3e-11. m1: the consequence N3 tests concerns the gh_2 transports only (13.1).]

*The axis.* A first version removed the numerator's interpolated axis value before each division by S^2 or C^2. That
adds a rank-one term ~ (1 - x)/(1 + x) to the semi-discrete operator, and at 48 x 12 that version runs away (C4; a
scratch growth-rate test, not part of the program, put the growing mode at the inner boundary next to the axis). The
numerator is S^2 (C^2) times a regular expression identically in the jets (the jets are exact products), so the
division is now pointwise, and the runs above converge.
[Section 13, n4: the term is ~ 1/S^2 and 1/C^2: (1 + x)/(1 - x) for the S^2 division, (1 - x)/(1 + x) for C^2.]

**Controls** (each mutates the computed path; must fail, and does; at 32 x 12 unless said): C1, S with its sign
flipped: M_22 = -4.289491, outside the band (M_22 is affine in S, so S's share is 3.2486 and the rest -1.0409); C2,
gh_2's coupling into the mean dropped: M_22 = 3.248207, outside the band; C3, gh_2's first harmonic set to zero on
Sigma (violating (F1)): the gauge diagnostic at tau0 is 1.00 of its terms' size, and N3's test fails; C4, the axis
division of the first version, at 48 x 12: M_22 = 9.8 x 10^4, outside the band; C5, M_22 placed off the class (CH below):
the chain's step fails. So the sign of S, the coupling to gh_2, the gh_2 data and the axis treatment are each seen;
the coupling to gh_2 alone moves M_22 by -1.04.
[Section 13, n5: C4's value is not reproducible (7e4 in the rerun, -2.0e5 in the reader's): it runs away, |M_22|
~ 1e5. C1 and C2 now also fail N3b, and C6 (the readout) is new (13.1, 13.4).]

### 12.3 The chain at the floating value (computed, floating point; not certified)

**CH**: at X*, with m_1(X*) = M_22 e_phi1 e_phi1 (the class, READ classm5 K1-K2) and stage 0's W and chi D there, the
supremum over the phase of |g_1|_op exceeds (4/3) K by |M_22| to rounding (the operator-norm step, and the largest
entry's, which uses the same C_app), and that of |g_1|_F^2 exceeds B + M_22^2 (the Frobenius step; r7fixes5 R1-R2,
READ). C5: off the class the excess is 0.2546, not |M_22|. With C_app >= 12.593309 + |M_22| (operator norm, largest
entry) and C_app >= (16.127552^2 + M_22^2)^(1/2) (Frobenius), the floating value would give

    lambda0 < 0.0020789 (operator norm),  < 0.0018903 (Frobenius),  < 0.0010404 (largest entry),

against the certified 0.0024433, 0.0019079 and 0.0012228; the band's two ends give the same figures. These are what a
certified enclosure of the band would deliver. They are not claimed.
[Section 13, n1: from eps1/C_app unrounded and rounded up they are 0.0020789, 0.0018902, 0.0010404 (13.6); m3:
what they need is a certified lower bound m_lo > 0 on |M_22|, not its sign (13.3).]

### 12.4 Step 4: what is certified

M_22 is not certified, so step 4 is not reached: **lambda0 < 0.0024433 (operator norm), < 0.0019079 (Frobenius), <
0.0012228 (largest entry)**, certified for round 2's envelope (READ lzerotrace5 T7, r7fixes5 R2, r6fixes5 F1), stand
unchanged. The M_22 route is a sharpening, computed as far as floating point takes it: the system exact (S1-S4), its
solve converged to about 1e-7, the sharpened numbers above.

### 12.5 The validated enclosure: what it needs, and why it does not close here (deduced; the arithmetic exact)

An a posteriori closure (R8.2 (S3)) bounds |M_22 - M_22^num| by the residual of an approximate solution times the
stability constant of the closed system, through the energy of Lemma 9.1 and a Sobolev embedding for the point value.
In the reading of Section 8 the residual must be below 7.19e-4 |M_22| in the principal-part energy, about 1.6e-3. Then:

- c_Y q^(1/2) <= 2^(1/2) x 37.8 = 53.5 (stage1rate5 K3, READ) brings the tolerance to 3.0e-5;
- the lower-order terms (the couplings to phi_1 and to gh_2, B-bar and C-bar in the record's notation, now explicit in
  S2-S3) add their rate k to kappa~ on the same region (Lemma 9.1); the record bounds none (round 6's minor 9), and for
  any k the factor is e^(k Dtau*/2), Dtau* = 3.7301: k = 10 already costs 1.3 x 10^8, which takes the tolerance to
  2.4e-13;
- the point value needs energies commuted at least twice (the slice is four-dimensional, so s > 2) and the Sobolev
  constant of the evaluation, each with its own, larger rates.

The converged floating solve reaches, by its own refinement, a truncation of about 1e-7 to 1e-8 in M_22; the residual
would have to be pushed at least five orders below that, and bounded in interval arithmetic over every space-time cell
of X*'s past (about 3.4 x 10^6 cells at 48 x 16 over 4479 steps, each with the closed system's coefficient functions
and the commuted equations), with a lower-order rate that is itself not proved. That is not a cost this machine can
meet, and nothing weaker certifies M_22's sign: an upper bound on m_1 cannot raise a lower bound (R7.3, R8.2), and the
data alone are too small (Section 5). So the route stops at the floating value, and the certified bounds of 12.4 are
the result.
[Section 13, m2, m3: "at least five orders" reads "about five orders", and only for a rate of the size k = 10;
the decisive point is that k is not bounded, nor are the point evaluation's constants (13.2). "Nothing weaker
certifies M_22's sign" reads "... a lower bound on |M_22|"; three cheaper routes exist (an L^2 pairing by R7.3's
criterion, a dual-weighted residual, s > 3/2 on the axis), none of which removes the unbounded k (13.3). The
interval evaluation itself is affordable (R2: about 910 s over all cells), so "not a cost this machine can meet"
is overstated: what is missing is the certified rate, not machine time.]

### 12.6 The replacement texts

The paper's lambda0 sentence, and the current proposal for it (CONSTANTS5.md R13.7, which supersedes R12.7 and keeps
its pair 3, the pair that carries Section 10's correction), now say less than is known: "The solve itself is not done"
is false. Five pairs follow: P for the paper, C1-C4 for R13.7 (its pair 3's new text, made P's; the source-map row; the
statuses; the Appendix D rows). Each old text occurs exactly once in its file as it stands, the four in CONSTANTS5.md
are disjoint, and seating them leaves every line at most 121 characters with no continuation line opening a list
(checked by content when this section was written: paper md5 4c121081..., CONSTANTS5.md md5 b9617854...; CONSTANTS5.md
is being edited by another workstream, so C1, whose old text R12.7 also carries, is anchored on the last line of R13.7's
pair 2). Each new text claims only what Sections 1-12 prove, certify or compute: the three certified bounds, the
reduction to one number, the data, the floating value with its observed stability, and the sharpened numbers marked
not certified. The pairs use ~~~ fences, since C1's texts contain the record's own ``` fences.
[Section 13, m6: CONSTANTS5.md R14.7 and R15.7 took up P verbatim as their pair 3; C1-C4 are not to be applied.
The final P, with R13.7's status words restored (m5), is in 13.5 and replaces R15.7's pair 3.]

**Pair P** (`paper/RESPONSE-HL-5D.md`, section 9, "Physical wavelengths", lambda0; old: the bullet's opening words,
to the line's end -- the span of R13.7's pair 3, whose new text this replaces).

~~~old
λ0 is not evaluated, and a high-frequency theorem, whose expansion parameter is λ over the
~~~

~~~new
The threshold λ0 that the proof of Theorem 1 delivers is traced term by term (supplement
  `docket68/n1star/CONSTANTS5.md`): at the numerical point, with the smooth envelope of supplement
  `checks/envelope5.py`, which has the numerics' integral, it is below 0.0024433 in the operator norm, 0.0019079 in the
  Frobenius norm and 0.0012228 in the largest entry (certified), so the wavelength 10 l5 lies more than 400 times
  beyond it. The approximant's first linear stage sharpens these through its mean correction at the point where the
  first-order wave is largest, which the symmetry class reduces to one number (computed, `checks/classm5.py`). That
  stage has been solved for this envelope on the point's past, from its data on the initial slice (the second-order
  constraint expansion in closed form, solved harmonic by harmonic; supplement `docket68/n1star/LAMBDA0-DATA5.md`,
  `checks/lam0data5.py`): the number is 2.207738, stable under refinement to 1.4 × 10⁻⁷ (computed, floating point,
  `checks/m22evol5.py`), and with it the three bounds become 0.0020789, 0.0018903 and 0.0010404. That sharpening is
  computed, not certified; the certified bounds are the ones stated. And a high-frequency theorem, whose expansion
  parameter is λ over the
~~~

**Pair C1** (CONSTANTS5.md, R13.7 pair 3: its new text becomes Pair P's, so that the proposal and the paper agree;
the old text opens with the last line of R13.7's pair 2, which makes it occur once, since R12.7 carries the same
pair 3).

~~~old
  those choices made numerically. This is a limit of the explicit computation, not a gap in Theorem 4.
```

```old
λ0 is not evaluated, and a high-frequency theorem, whose expansion parameter is λ over the
```

```new
λ0 is not evaluated. The threshold the proof of Theorem 1 delivers is traced term by term
  (supplement `docket68/n1star/CONSTANTS5.md`): at the numerical point, with the smooth envelope of supplement
  `checks/envelope5.py`, which has the numerics' integral, it is below 0.0025 in the operator norm, 0.0020 in the
  Frobenius norm and 0.00123 in the largest entry (certified), so the wavelength 10 l5 lies more than 400 times beyond
  it. A value, or a lower certified bound, needs the approximant's linear stages solved. The first can lower the
  operator-norm bound, for example through its mean correction at the point where the first-order wave is largest, which
  the symmetry class reduces to one number (computed, `checks/classm5.py`); a certified value of that number needs a
  validated solve of the first stage for that envelope. Its data on the initial slice are now computed: the second-order
  constraint expansion in closed form (exact), solved harmonic by harmonic (floating point; supplement
  `docket68/n1star/LAMBDA0-DATA5.md`, `checks/lam0data5.py`), and too small to move the bound by themselves; over that
  point's past the energy estimate's growth is at most 1.4 × 10³ by domain of dependence (certified), against 5.1 × 10¹⁰
  over the whole slab, before the lower-order terms. The solve itself is not done. And a high-frequency theorem, whose
  expansion parameter is λ over the
```
~~~

~~~new
  those choices made numerically. This is a limit of the explicit computation, not a gap in Theorem 4.
```

```old
λ0 is not evaluated, and a high-frequency theorem, whose expansion parameter is λ over the
```

```new
The threshold λ0 that the proof of Theorem 1 delivers is traced term by term (supplement
  `docket68/n1star/CONSTANTS5.md`): at the numerical point, with the smooth envelope of supplement
  `checks/envelope5.py`, which has the numerics' integral, it is below 0.0024433 in the operator norm, 0.0019079 in the
  Frobenius norm and 0.0012228 in the largest entry (certified), so the wavelength 10 l5 lies more than 400 times
  beyond it. The approximant's first linear stage sharpens these through its mean correction at the point where the
  first-order wave is largest, which the symmetry class reduces to one number (computed, `checks/classm5.py`). That
  stage has been solved for this envelope on the point's past, from its data on the initial slice (the second-order
  constraint expansion in closed form, solved harmonic by harmonic; supplement `docket68/n1star/LAMBDA0-DATA5.md`,
  `checks/lam0data5.py`): the number is 2.207738, stable under refinement to 1.4 × 10⁻⁷ (computed, floating point,
  `checks/m22evol5.py`), and with it the three bounds become 0.0020789, 0.0018903 and 0.0010404. That sharpening is
  computed, not certified; the certified bounds are the ones stated. And a high-frequency theorem, whose expansion
  parameter is λ over the
```
~~~

**Pair C2** (CONSTANTS5.md, R13.7 pair 4: the source-map row for lambda0 gains the program).

~~~old
| | `checks/lzerotrace5.py`, `checks/classm5.py`; `docket68/n1star/LAMBDA0-DATA5.md`, `checks/lam0data5.py` |
```

Statuses behind the new texts. Pair 1: d's integer at the record's computational point, deduced, with exact arithmetic
~~~

~~~new
| | `checks/lzerotrace5.py`, `checks/classm5.py`; `docket68/n1star/LAMBDA0-DATA5.md`, `checks/lam0data5.py`, |
| | `checks/m22evol5.py` |
```

Statuses behind the new texts. Pair 1: d's integer at the record's computational point, deduced, with exact arithmetic
~~~

**Pair C3** (CONSTANTS5.md, R13.7's statuses: pair 3's).

~~~old
(rootavoid5, INVERSE5-SCALAR.md Theorems B.2-B.5); the point's role, computed (iotaind5 I5). Pairs 2-4 as R12.7 states
them.
~~~

~~~new
(rootavoid5, INVERSE5-SCALAR.md Theorems B.2-B.5); the point's role, computed (iotaind5 I5). Pairs 2 and 4 as R12.7
states them, and pair 3's as R12.7 states them with the stage-1 solve and the sharpened numbers added, computed in
floating point and not certified (m22evol5 13/13: the system exact, S1-S4; the solve, its convergence and the
chain, N1-N3 and CH).
~~~

**Pair C4** (CONSTANTS5.md, R13.7's Appendix D rows: the program and its output; LAMBDA0-DATA5.md's own row
changes with this section, and the main session measures every row again when it seats the pairs, as R13.7 says).

~~~old
| `docket68/n1star/checks/lam0data5.out` | `038021a1ad5ebc7df59a3720cc9da63b` |
~~~

~~~new
| `docket68/n1star/checks/lam0data5.out` | `038021a1ad5ebc7df59a3720cc9da63b` |
| `docket68/n1star/checks/m22evol5.py` | `abd935827c2a2fdc543d4e70eb6fe185` |
| `docket68/n1star/checks/m22evol5.out` | `12beb54cff95722d1e7c433c47e2922b` |
~~~

### 12.7 Program and pass count

`checks/m22evol5.py --selftest` (output `checks/m22evol5.out`, **13/13**, about 55 minutes on the loaded machine):
S1-S4 (exact), N1-N3 and CH (floating point), controls C1-C5. Imported, not copied: lam0data5.py (gauge, the order-1
mean, the mode ODEs and their solver, the envelope's c). READ: stage0bd5.py (chi's closed form), stage5.out S2 (the
mean source, recovered by S2), classm5 K1-K2 and r7fixes5 R1-R2 (the chain's steps), lzerotrace5 T7, r7fixes5 R2,
r6fixes5 F1 (the certified bounds), envelope5.out E1 (c's interval). md5: program abd935827c2a2fdc543d4e70eb6fe185
(the run's source was 6f6413adcdabbf8a006cd57f43281f45; one string literal was rewrapped afterwards to keep lines at
121 characters, the parsed program identical), output 12beb54cff95722d1e7c433c47e2922b.
[Section 13: the program extended (S4b, N3b, N4, C6, R1, R2) and rerun, 17/17; md5s in 13.7.]

## 13. The reader's confirmation of Section 12, and what it changed

*Status (2026-11-06).* An independent reader (report-vL0) CONFIRMED Section 12: no Major; the selftest reproduces
13/13 digit for digit (C4's runaway value apart); the axis factorisation holds exactly (checked symbolically, with a
control that fails); its own second discretisation (Legendre-Gauss-Lobatto in r, Legendre-Gauss in x) gives M_22 =
2.207737926 at 40 x 16, inside the band; the certified bounds stand. It found six minor points (m1-m6) and seven nits
(n1-n7). Each is seated here; the amended sites in Sections 0, 8 and 12 carry a bracketed note [Section 13, ...], the
old text kept. The program is extended and rerun: `checks/m22evol5.py --selftest`, **17/17** (S4b, N3b, N4 and C6
new; C1 and C2 now also fail N3b; the measurements R1 and R2 printed). M_22's value does not move: 2.207738 (48 x 16),
error estimate 1.4e-7, band [2.2077367, 2.2077395]; lambda0's certified bounds stand.

### 13.1 m1: what N3 sees, and N3b

N3, the first harmonic of D^(1), involves only gh_2's first harmonic, (m_1)_rth and d_th phi_1 (S4). It checks the four
gh_2 transports, not the mean equations: it is unchanged under C1 (S's sign flipped: 3.1e-6 and 2.2e-7 at mid-solve and
tau*, against 3.1e-6 and 2.3e-7) and under the reader's mutants of the mean equations, and Section 12.1's "a check on
the solved equations and their coupling" claimed too much. The mean equations are now checked by **N3b**, the harmonic-0
part of D^(1), lowered (computed, floating point). By **S4b** (exact) it is linear in m_1 and its first derivatives
alone, with no source; step (ii) sets it to zero on Sigma -- to 1.6e-16 at Nx = 16 and 20, and to 1.3e-8 at Nx = 12,
where the data's Legendre modes P_k(cos 2th), k up to 13, are not resolved (the output's parenthesis "the floating
data's floor" means this) -- and the solve does not impose it. Along the solve it is 3.8e-4, 1.6e-5, 5.9e-6 and 5.9e-6
at mid-solve for Nr = 24, 32, 40, 48 (Nx = 12), falling with Nr until Nx = 12's angular truncation is reached; at 48 x
16 it is 1.5e-7 at mid-solve and 2.7e-9 at tau*, and on 48 x 12, 48 x 16 and 32 x 20 at most 1.1e-5 (32 x 20 at
mid-solve, Nr = 32's radial truncation). C1 now fails twice: M_22 leaves the band and N3b is 0.40 at mid-solve; C2
likewise (0.46). So the mean equations, their source S and their coupling to gh_2 are checked end to end by the
contracted Bianchi identity, not only through S1-S2.

### 13.2 m2: what Section 12.5's tolerance argument shows

The Section 8 bracket says "carried through c_Y q^(1/2) and any lower-order rate, the tolerance falls below what it
reaches". Not for any rate: the tolerance is 3.0e-5 e^(-1.865 k), still at least 1.1e-7 for k <= 3. It falls below the
solve's reach for a rate of the size 12.5 illustrates (k = 10 gives 2.4e-13, about five orders below the solve's
truncation of about 1e-8 -- the one an energy-norm residual, the other the change of a point value under refinement).
The decisive point is not that number: k is not bounded, by the record or here, and neither are the Sobolev constant of
the point evaluation and the constants of the commuted energies, so no tolerance exists yet to compare a residual with.
**R1** (measured, floating point; the coefficients' sizes, not a rate in Lemma 9.1's energy) shows what a rate would
have to absorb: at th = pi/4, clear of the axis's coordinate factors, the mean equations' first-order coefficients (row
sums, normalised by the d_tau^2 coefficient) run over X*'s past from 7.8 at tau0 to 31.9 at tau*, the zero-order ones
from 15.4 to 3.6e4 at X*, the couplings to gh_2 from 0.10 to 40.4; the first-order ones alone, used as a rate, give
e^(int/2) = 2.5e7 and would take the tolerance from 3.0e-5 to 1.2e-12.

### 13.3 m3: what the bounds need, the cheaper routes, and the attempt at m_lo

*What is needed* is a certified lower bound m_lo > 0 on |M_22|, not its sign: the excess in the operator norm and the
largest entry is |M_22| for either sign (the e_phi1 eigenvalue is M_22 + (4/3) K cos s, CH), and the Frobenius step
needs M_22^2. Any m_lo helps (computed from eps1/C_app, rounded up): m_lo = 1 gives lambda0 < 0.0022636, 0.0019042
and 0.0011329, m_lo = 1/2 gives 0.0023500, 0.0019070 and 0.0011761 (operator norm, Frobenius, largest entry; the
reader's 0.0019043 at m_lo = 1 came from the rounded certified value). Section 12.5's "nothing weaker certifies
M_22's sign" therefore reads "a lower bound on |M_22|", and its point-value bullet presents as necessary what three
cheaper routes avoid or reduce:

- (i) R7.3's criterion needs only a lower bound on a supremum over Omega x S^1, so a weighted local average of
  (m_1)_phi1phi1 at s = 0 near X* -- an L^2 pairing that the energy controls directly -- can replace the point value:
  no Sobolev step and no commuted energies, at the price of W's own average, which loses about 70 per unit r near X*
  (the reader's figure), so the averaging radius must stay below about 0.03 for M_22's 2.2 to count;
- (ii) a goal-oriented (dual-weighted residual) estimate, M_22 = M_22^num + <z_num, rho> + R, z the adjoint solution
  for that functional, with R bounded by the stability constant times the product of the primal and adjoint residuals,
  so that the residuals enter squared;
- (iii) in the symmetry class X* lies on the axis, where the reduced space is three-dimensional, so s > 3/2 would
  serve for a point value.

*The attempt.* The cheapest combination is (i) with (ii): an L^2 functional and a quadratic remainder. Its three
ingredients, each tried here:

- (a) The interval evaluation over X*'s past is affordable. **R2** (measured, this machine) puts all 202 coefficient
  functions of the closed system on one space-time box in Arb balls at 2.6e-4 s, about 910 s over the 3,439,872 cells of
  48 x 16 x 4479 steps; the interpolant's jets and the residual's assembly multiply this by a constant, they do not
  change its order. So Section 12.5's "not a cost this machine can meet" was overstated (noted there).
- (b) The certified stability constant of the coupled system on X*'s past, which every route needs -- in (ii) it
  multiplies the quadratic remainder, in (i) it bounds the pairing's error, in (iii) it is the same constant -- does
  not exist. Lemma 9.1 bounds the principal part (<= 1391.72). The lower-order terms need an energy estimate for the
  coupled system of eight wave equations, the transport of phi_1 and four complex transports, with weights that
  balance the couplings to gh_2 (up to 40.4 at X*, R1), a zero-order term in the energy to absorb coefficients that
  reach 3.6e4 at X* (R1), and the transports' own rates. Neither the record nor this file contains that estimate.
  Writing it is a proof, not a computation, and its constant is what decides: R1's first-order sizes alone, used as a
  rate, give a factor of order 2.5e7, and the zero-order terms near X* add to it.
- (c) Route (ii) also needs the adjoint solve and its residual, certified as in (a); bounded, but of use only with (b).

*Precisely why it stops.* Step (b) is not a bounded computation: it is a new energy estimate, for a system whose
lower-order coefficients R1 measures in the tens and, at X*, in the tens of thousands, with a constant that nothing in
the record bounds in advance. Steps (a) and (c) are bounded but certify nothing without it. So no certified m_lo is
reached, by any of the three routes, and the bounds stated are the certified ones: 0.0024433, 0.0019079, 0.0012228.

### 13.4 m4: the pin

Nothing in Section 12 pinned M_22's value: N1 tested convergence and positivity, CH used the computed value, and the
controls only departures from the band. **N4** (computed, floating point) pins it twice. A second discretisation,
Legendre-Gauss-Lobatto in r and Legendre-Gauss in x (40 x 16, cfl 1/2), gives M_22 = 2.207737926, 1.5e-7 from the
Chebyshev value, inside the band's half-width 1.4e-6 (the reader's own implementation gave 2.207737926 there). And M_22
read from the coordinate component h_p1/(r C)^2 at the axis agrees with the readout (T - B)/a^2 to 2e-14 on every grid.
**C6** (control): the readout with T + B gives 2.902410, and N4's readout test fails. An error in the data on Sigma is
seen by N3 and N3b at tau0, which vanish only under (F1) and step (ii).

### 13.5 m5, m6: the final pair P

CONSTANTS5.md R14.7, and R15.7 after it, took up Section 12.6's pair P verbatim as their pair 3, and R14.7 records that
C1-C4 need not be applied: **C1-C4 are not to be applied.** The reader asked that P keep R13.7's status words ("in
closed form (exact), solved harmonic by harmonic (floating point)", "solved numerically", "would sharpen") and the
clause that a certified value needs a validated solve. The final P below does, and carries the pin (13.4) and n1's
Frobenius figure. It replaces R15.7's pair 3 in the final pass. Checked by content against the paper as it stands (md5
805be200b746b7cf480e88639da5508f): the old text occurs exactly once; seated, every line is at most 121 characters and no
continuation line opens a list.

~~~old
λ0 is not evaluated, and a high-frequency theorem, whose expansion parameter is λ over the
~~~

~~~new
The threshold λ0 that the proof of Theorem 1 delivers is traced term by term (supplement
  `docket68/n1star/CONSTANTS5.md`): at the numerical point, with the smooth envelope of supplement
  `checks/envelope5.py`, which has the numerics' integral, it is below 0.0024433 in the operator norm, 0.0019079 in the
  Frobenius norm and 0.0012228 in the largest entry (certified), so the wavelength 10 l5 lies more than 400 times
  beyond it. The approximant's first linear stage would sharpen these through its mean correction at the point where
  the first-order wave is largest, which the symmetry class reduces to one number (computed, `checks/classm5.py`). The
  stage's data on the initial slice are the second-order constraint expansion in closed form (exact), solved harmonic
  by harmonic (floating point; supplement `docket68/n1star/LAMBDA0-DATA5.md`, `checks/lam0data5.py`); solved
  numerically for this envelope on the point's past, the stage gives that number as 2.207738, stable under refinement
  to 1.4 × 10⁻⁷ and reproduced by a second discretisation (computed, floating point, `checks/m22evol5.py`), and with
  it the three bounds would be 0.0020789, 0.0018902 and 0.0010404. A certified value of that number needs a validated
  solve of the stage, so the sharpening is computed, not certified; the certified bounds are the ones stated. And a
  high-frequency theorem, whose expansion parameter is λ over the
~~~

### 13.6 The nits

- n1: the sharpened bounds are now computed from eps1/C_app unrounded (eps1 < s0 <= 0.030768560, lzerotrace5 T7;
  eps1 < 0.0153989 in the largest entry, r6fixes5 F1) and rounded up: 0.0020789, 0.0018902, 0.0010404 at the band's
  lower end; at M_22 = 0 the same chain gives back the certified 0.0024433, 0.0019079, 0.0012228. Section 12.3's
  0.0018903 came from the rounded certified value, and its 0.0010404 was 0.001040406 rounded down; the figure holds
  through the unrounded chain (0.00104039).
- n2: N2's change of 2.3e-8 is Nr = 40's radial truncation: the v = 2.6 run, on a narrower domain, agrees with 48 x 12
  at v = 3 to 3e-11, so the boundary's own effect is below that.
- n3: the band rounded outward is [2.2077367, 2.2077395].
- n4: the first version's term is ~ 1/S^2 and 1/C^2 ((1 + x)/(1 - x) for the S^2 division, (1 - x)/(1 + x) for the
  C^2 division).
- n5: C4's runaway value is not reproducible (98376 in Section 12's run, -203597 in the reader's, 7e4 here): it runs
  away, |M_22| ~ 1e5.
- n6: the program's docstring now gives "about an hour"; this run took 39 minutes.
- n7: moot, since 12.6's C1-C4 are not applied.

### 13.7 Program and pass count

`checks/m22evol5.py --selftest` (output `checks/m22evol5.out`, **17/17**, 39 minutes on this machine): S1-S4 and S4b
(exact); N1-N3, N3b, N4 and CH (floating point); controls C1-C6; R1 and R2 printed (measured; not checks). Imported, not
copied: lam0data5.py; python-flint for R2's Arb balls. READ as in 12.7. md5: program 8216d298edd3ef9cce8a7d91903c37a6,
output 28fc40c1ce8ffd0726afc899983f4544. The rows that R15.7's pair 5 gives for this file, the program and its output
are superseded by these.
