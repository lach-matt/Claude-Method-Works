# LAMBDA0-DATA5 -- the stage-1 data on Sigma, the envelope, and X*'s past (workstream D, after round 8)

*Status (2026-11-06).* New; not yet read by a verifier. It takes the three blocks CONSTANTS5.md R8.2 records on
lambda0 (and R9.5 keeps): (a) S_1 and B_1, the second-order constraint expansion of the stage-1 data on Sigma; (b) the
stability constant over X*'s past; (c) an admissible envelope. Labels as in the record: **proved** (an argument
written here, every step checked), **computed** (a program, exact unless it says floating point; **certified** for Arb
balls or exact rationals), **deduced** (an argument from cited lines), **READ** (quoted or cited), **reduced to X**
(what is left, named). One program, `checks/lam0data5.py` (`--selftest`; output `checks/lam0data5.out`), every check
named and printed, six controls that mutate the computed path and fail as they must. CONSTANTS5.md, N1STAR-PROOF.md
and the paper are not edited.

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
of it, floating point or validated; a value of M_22 is therefore not claimed even approximately.

**Reduced to:** a validated solve of the stage-1 evolution (Lemma 5.3 (a)-(c), m = 1) on X*'s past from the Cauchy
data of Section 6, for envelope5's envelope, with an enclosure of the point value (m_1)_phi1phi1(X*). With the domain
of dependence of Section 9 the tolerance its residual must meet, in the reading of classm5 K5 (principal part only),
is about 7.19e-4 |M_22| in Lemma 2.3's energy, before c_Y q^(1/2) (<= 2^(1/2) x 37.8, stage1rate5 K3), the
lower-order coefficients' rates (not computed: round 6's minor 9) and the Sobolev constant of the point evaluation;
it is not met, since no approximate solution exists here. Nothing weaker suffices (R7.3, R8.2: an upper bound on m_1
cannot raise a lower bound, and the data are too small, Section 5).

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
solved data (floating point), Sections 3 and 5.

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
constant are no longer missing.
