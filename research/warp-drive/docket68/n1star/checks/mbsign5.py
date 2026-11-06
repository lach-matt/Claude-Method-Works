#!/usr/bin/env python3
"""mbsign5: the sign of the canonical energy on the band -- the missing input M_b of FAMILIES5-R6.md section 1.5,
decided (FAMILIES5-MB.md).

Setting. On a vacuum band U of Part I's slice the data background + eps delta + c, c = O(eps^2) supported in U,
satisfy the vacuum constraints up to eps^2 Q(delta) + O(eps^3) times the static KID (FAMILIES5-VLASOV Proposition
L'), Q(delta) = (1/2) int (N_s D^2 H + 2 Y_s . D^2 M)[delta, delta] dvol with the record's map (H = R + (tr K)^2 -
|K|^2, M_i = D_j K^j_i - D_i tr K, K = (1/2) L_n gamma, n future) and its KID (N_s, 2 Y_s), xi = N_s n + Y_s the
static Killing field; E := -Q is the canonical energy. Every vacuum region of Part I is Tangherlini, f = 1 - mu/R^2,
in ingoing coordinates (v, R) with v = int e^(psi_P) dvhat, and Part I's slice there is v = V(R), w := V' = e^(psi_P)
(qsign5 Q2). The class: T^2 x Z2 x Z2-invariant tensors on S^3, dOmega^2 = dth^2 + sin^2 th dphi1^2 + cos^2 th dphi2^2.

  E1 (exact) The class harmonics. Scalar: P_j(cos 2th), Delta = -l(l + 2), l = 2j (the record's Lemma 1.2). Tensor
     (new): for every n >= 0, T = A dth^2 + B sin^2 th dphi1^2 + C cos^2 th dphi2^2 with A = C_n^(3/2)(u), u = cos 2th
     (Gegenbauer), B = (3u - 1) A/2 - (1 - u^2) A_u, C = -A - B is trace-free, divergence-free, regular at both axes
     (A = B at th = 0, A = C at th = pi/2) and (Delta + k_T^2) T = 0 with k_T^2 = l(l + 2) - 2, l = 2n + 2; checked for
     n = 0..3, and the divergence condition fixes B from A (so the class TT tensors are these, one per even l >= 2).
     Control (must fail): B with the derivative term's sign reversed is not divergence-free.
  E2 (exact, sympy, symbolic in w(R) and mu) The tensor sector on every class slice v = V(R) of Tangherlini (any w > 0,
     0 < f w < 2; Part I's vacuum slices are these): N_s sqrt(gamma_RR) = 1, N_s^2 - |Y_s|^2 = f; for delta gamma = 2
     R^2 H T, delta K = (R^2 P + 2 R n^R H) T (P = n(H), the normal derivative), the linearised constraints vanish
     identically, and the theta-integrated Q-density equals -2 |T|^2 T_m(xi, n) sqrt(gamma_RR) up to a d/dR, where
     T_m(xi, n) = R^3 (xi(H) P - (1/2) g(xi, n) |dH|^2) - (1/2) g(xi, n) (k_T^2 + 2) R H^2 is the flux of the conserved
     2D master current of the tensor equation (Euler operator in H and P zero; l = 2 and l = 4). So E = 2 |T|^2 int
     T_m(xi, n): positive definite in (H, P) where f > 0, indefinite where f < 0 (the (P, H_R) block has determinant
     R^6 f/(4 gamma_RR)). Control (must fail): the identity with |T|^2 halved.
  E3 (exact, rational arithmetic) M_b fails inside the horizon. With P = -(Y_s^R/N_s) H_R (E2):
     Q = -|T|^2 int (R^3 f H_R^2 + (k_T^2 + 2) R H^2) dR, the same on every slice; with H = (R - R1)^2 (R2 - R)^2 on
     [R1, R2] = [0.72, 0.89] (inside Part I's seed region, horizon 0.9067, inner edge 0.683) Q > 0, i.e. E < 0, for
     every mu in [0.80, 0.84] (Q is affine in mu; exact at both ends). A momentum-only tensor seed (H = 0) has Q =
     -|T|^2 int R^3 P^2 < 0. Control (must fail): the same construction on the band [0.92, 1.09], outside the horizon
     for every mu in [0.80, 0.84], gives Q < 0 (E > 0).
  E4 (exact, sympy; mu, k^2 symbolic) Scalar modes on the static slice gamma = dR^2/f + R^2 dOmega^2, N = sqrt(f),
     K0 = 0, Y = 0: (a) in the Regge-Wheeler-type gauge (h_RR = A S, h_ij = 2 R^2 F S gammahat; k_RR = p S, k_Rth =
     R q S', k_ij = R^2 w S gammahat; S any class harmonic, imposed through Delta S = -k^2 S), the linearised
     constraints and the two energy densities E_V = -(1/2) N D^2 R[h, h] and E_K = N (|k|^2 - (tr k)^2) are
     (radial) x (S or S') and (radial) x S^2 + (radial) x S'^2, every coefficient free of th (equal at three rational
     angles); (b) the gauge: L_X gamma for X = alpha S d_R + beta S' d_th shifts (h_RR, h_Rth/R, h_ij/R^2) as stated
     in FAMILIES5-MB.md, and the lapse direction k_psi = D^2 psi - psi Ric has z-component psi/R^2; (c) mode-free
     (functions of (R, th)): D R[L_X gamma] = 0 for every class X; the Euler operator of N D R[h] sqrt(gamma) vanishes
     in all five class components of h ((D R)^* N = 0); M[k_psi] = 0; and the Euler operator in psi of N (<k, k_psi>
     - tr k tr k_psi) sqrt(gamma) equals sqrt(gamma) (2 dN . M[k] + N div M[k]) for every class k: so E_V and E_K are
     unchanged by compactly supported spatial and lapse gauge on the constraint surface.
  E5 (exact) The kinetic energy. With Z := R^3 (w - f q), H_KI := m + 6 mu/R^2, m := k^2 - 3: Z' + (R^2 H_KI/3) q +
     R^2 M_th + (R^3/3) M_R = 0 identically; the map Z -> (q, w, p) = (-3 Z'/(R^2 H_KI), Z/R^3 + f q, ((4 - 3x) q +
     R f q' - 2 w)/f) solves both constraints identically, and E_K - 6 k^2 m Z^2/(R^3 H_KI^2) has zero Euler operator in
     Z. Control (must fail, a gauge-variant variable admitted): Z replaced by R^3 w.
  E6 (exact) The potential energy. E_V = E_red + R^4 F' C + d/dR (Euler operator zero); l := A - (2R/f) F' +
     (2 H_KI/(3 f^2)) F satisfies l' + kappa l - (2 k^2 H_KI/(9 R f^3)) F = (R/(3 f^2)) C, kappa = (k^2 + 6 + 6x)/(3 R f),
     x = mu/R^2; the map l -> (A, F) solves C identically; and with Phi := R^(3/2) f^2 l/H_KI,
         E_V = (27 m/(2 k^2)) (f Phi'^2 + Qp Phi^2/(16 R^2 H_KI^2)) + d/dR,
         Qp = 1296 x^3 + (624 m - 144) x^2 + 36 m (m - 12) x + 16 m^3 + 60 m^2,
     the Kodama-Ishibashi scalar potential at n = 3 (gmodes5 G3). Controls (must fail): l without its F-term (a gauge-
     and constraint-blind variable) does not solve C; Phi with R^(1/2) in place of R^(3/2).
  E7 (exact) Positivity on the class spectrum. Class modes have l = 2j, so m = 4j(j + 1) - 3 in {5, 21, 45, ...}:
     Qp > 0 on x in [0, 1] (m = 5: 1296 x^3 >= 0 and the quadratic's discriminant < 0; m >= 21: every coefficient
     >= 0, the constant > 0), H_KI > 0, f > 0 for R > sqrt(mu). Control (must fail, the wrong sign): the potential of
     the l-form before the S-deformation, c0 l^2, is negative near the horizon at m = 5 (a root in (0, 1) in x).
  E8 (exact) l = 0: on the constraint, E_V and E_K are d/dR's; compactly supported h_0 = L_(R F d_R) gamma, the other
     solution of the l = 0 constraint being the mass change, nowhere zero.
  E9 (exact) The master energy: for k solving the momentum constraint (the E5 parametrisation), the configuration
     master field of h = 2 N k is Phi[2 N k] = (2 k^2/3) sqrt(f) Z/(R^(3/2) H_KI); so on the static slice E =
     (27 m/(2 k^2)) |S|^2 int (Phi_t^2 + (d_r* Phi)^2 + V_S Phi^2) dr*, Kodama-Ishibashi's conserved master energy.

Labels: computed (exact; E4 (a) at three rational angles, every radial identity symbolic in R, mu, k^2). Deduced in
FAMILIES5-MB.md, not here: the transfer of E from Part I's slice to the static slice (Stokes and the second-order
Bianchi identity), the mode sum (orthogonality), the intermediate-value step (Proposition L').

Run: python3 checks/mbsign5.py [--selftest]   (--selftest: exit 1 unless every check passes and every control fails)
"""
import importlib.util
import os
import sys
import time

import sympy as sp
from sympy.calculus.euler import euler_equations

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


QS = load('qsign5')                       # constraints_fast: the record's H and M (bandconst5's formulas)
r, th = sp.symbols('r theta', positive=True)
p1, p2 = sp.symbols('p1 p2')
mu, k2 = sp.symbols('mu k2', positive=True)
eps = sp.Symbol('eps')
s_, c_ = sp.sin(th), sp.cos(th)
x_ = mu / r**2
f_ = 1 - x_
m_ = k2 - 3
HKI = m_ + 6 * x_
RESULTS = {}


def report(name, ok, controls=()):
    """controls: list of (label, rejected) -- a control passes when it is rejected (fails as it must)"""
    allc = all(c for _, c in controls)
    RESULTS[name] = ok and allc
    print('%s %s  (%.0f s)' % (name, 'PASS' if (ok and allc) else 'FAIL', time.time() - T0), flush=True)


def zero(e):
    return sp.cancel(sp.together(e)) == 0


# ------------------------------------------------------------------ jets on R
class Jets:
    """densities in R and the jets of named fields (symbols name_0, name_1, ...)"""

    def __init__(self, names, order=8):
        self.names = names
        self.J = {nm: sp.symbols('%s_0:%d' % (nm, order + 1)) for nm in names}
        self.order = order

    def D(self, e):
        out = sp.diff(e, r)
        for nm in self.names:
            J = self.J[nm]
            out += sum(sp.diff(e, J[i]) * J[i + 1] for i in range(self.order))
        return out

    def Dn(self, e, n):
        for _ in range(n):
            e = self.D(e)
        return e

    def euler(self, L, nm):
        J = self.J[nm]
        out = 0
        for i in range(self.order):
            t = sp.diff(L, J[i])
            if t != 0:
                out += (-1)**i * self.Dn(t, i)
        return out

    def from_funcs(self, e, fns):
        """replace sympy Functions of r (and their derivatives) by the jet symbols"""
        reps = {}
        for nm, fn in zip(self.names, fns):
            for i in range(self.order, 0, -1):
                reps[sp.diff(fn, r, i)] = self.J[nm][i]
            reps[fn] = self.J[nm][0]
        return e.subs(reps)

    def is_zero(self, e):
        e = sp.together(sp.expand(e))
        num = sp.expand(sp.numer(e))
        if num == 0:
            return True
        syms = [s for nm in self.names for s in self.J[nm] if num.has(s)]
        if not syms:
            return sp.cancel(num) == 0
        return all(sp.cancel(cf) == 0 for cf in sp.Poly(num, *syms).coeffs())
