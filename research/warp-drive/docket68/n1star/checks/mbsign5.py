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


# ------------------------------------------------------------------ tensors in the class (coordinates X, diagonal g)
def christoffel(g, X):
    n = len(X)
    gi = g.inv()
    return gi, [[[sp.together(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                                  - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
                   for c in range(n)] for b in range(n)] for a in range(n)]


def cov2(T, X, Gm):
    """D_c T_ab as nested list [a][b][c]"""
    n = len(X)
    return [[[sp.diff(T[a, b], X[c]) - sum(Gm[e][c][a] * T[e, b] + Gm[e][c][b] * T[a, e] for e in range(n))
              for c in range(n)] for b in range(n)] for a in range(n)]


def div2(T, X, gi, Gm):
    n = len(X)
    DT = cov2(T, X, Gm)
    return [sum(gi[c, a] * DT[a][b][c] for a in range(n) for c in range(n) if gi[c, a] != 0) for b in range(n)]


def lap2(T, X, gi, Gm):
    """rough Laplacian D^d D_d T_ab (diagonal metric)"""
    n = len(X)
    DT = cov2(T, X, Gm)
    out = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            s = 0
            for c in range(n):
                e1 = sp.diff(DT[a][b][c], X[c]) - sum(Gm[e][c][a] * DT[e][b][c] + Gm[e][c][b] * DT[a][e][c]
                                                       + Gm[e][c][c] * DT[a][b][e] for e in range(n))
                s += gi[c, c] * e1
            out[a, b] = s
    return out


def hess(psi, X, Gm):
    n = len(X)
    return sp.Matrix(n, n, lambda i, j: sp.diff(psi, X[i], X[j]) - sum(Gm[k][i][j] * sp.diff(psi, X[k])
                                                                        for k in range(n)))


def ricci(X, Gm):
    n = len(X)
    return sp.Matrix(n, n, lambda b, d: sum(sp.diff(Gm[a][b][d], X[a]) - sp.diff(Gm[a][b][a], X[d])
                                            + sum(Gm[a][a][e] * Gm[e][b][d] - Gm[a][d][e] * Gm[e][b][a]
                                                  for e in range(n)) for a in range(n)))


def trig_zero(e):
    return sp.simplify(sp.expand_trig(sp.expand(e))) == 0


# ------------------------------------------------------------------ E1
SX = [th, p1, p2]
SG = sp.diag(1, s_**2, c_**2)


def class_tt(n, flip=1):
    """the class TT harmonic of E1: A = C_n^(3/2)(cos 2th), B from the divergence condition, C = -A - B"""
    uu = sp.Symbol('uu')
    Au = sp.gegenbauer(n, sp.Rational(3, 2), uu)
    u = sp.cos(2 * th)
    A = Au.subs(uu, u)
    B = (3 * u - 1) * A / 2 - flip * (1 - u**2) * sp.diff(Au, uu).subs(uu, u)
    return sp.expand(A), sp.expand(B), sp.expand(-A - B), 4 * n * (n + 3) + 6, 2 * n + 2


def e1():
    print("E1 (exact) the class harmonics on S^3: scalar P_j(cos 2th); tensor A = C_n^(3/2)(cos 2th)", flush=True)
    gi, Gm = christoffel(SG, SX)
    ok_s = True
    for j in range(1, 5):
        S = sp.legendre(j, sp.cos(2 * th))
        lap = sp.diff(s_ * c_ * sp.diff(S, th), th) / (s_ * c_)
        ok_s &= trig_zero(lap + 2 * j * (2 * j + 2) * S)
    print("   scalar: Delta P_j(cos 2th) = -l(l + 2) P_j, l = 2j, j = 1..4: %s" % ok_s)
    ok_t, norms = True, []
    for n in range(4):
        A, B, C, kT2, l = class_tt(n)
        T = sp.diag(A, B * s_**2, C * c_**2)
        dv = div2(T, SX, gi, Gm)
        L = lap2(T, SX, gi, Gm)
        ev = all(trig_zero((L[i, i] + kT2 * T[i, i]) / SG[i, i]) for i in range(3))
        dz = all(trig_zero(d) for d in dv)
        ax = sp.simplify((A - B).subs(th, 0)) == 0 and sp.simplify((A - C).subs(th, sp.pi / 2)) == 0
        nr = sp.integrate(sp.expand(sp.expand_trig((A**2 + B**2 + C**2) * s_ * c_)), (th, 0, sp.pi / 2))
        norms.append((l, kT2, nr))
        ok_t &= ev and dz and ax and kT2 == l * (l + 2) - 2
        print("   tensor n = %d (l = %d): trace-free, divergence-free %s, (Delta + %d) T = 0 %s, k_T^2 = l(l+2) - 2 %s, "
              "regular at both axes %s, |T|^2 = %s" % (n, l, dz, kT2, ev, kT2 == l * (l + 2) - 2, ax, nr))
    # the divergence condition fixes B from A (so one class TT tensor per eigenvalue)
    Af, Bf = sp.Function('A')(th), sp.Function('B')(th)
    dv = div2(sp.diag(Af, Bf * s_**2, (-Af - Bf) * c_**2), SX, gi, Gm)
    Bsol = sp.solve(sp.Eq(sp.simplify(dv[0]), 0), Bf)
    uniq = len(Bsol) == 1 and trig_zero(Bsol[0] - ((3 * sp.cos(2 * th) - 1) * Af / 2
                                                    + sp.sin(2 * th) * sp.diff(Af, th) / 2))
    print("   the divergence condition is solved by B = (3u - 1) A/2 + (sin 2th/2) A_th, uniquely: %s" % uniq)
    A, B, C, kT2, l = class_tt(1, flip=-1)
    ctl = not all(trig_zero(d) for d in div2(sp.diag(A, B * s_**2, C * c_**2), SX, gi, Gm))
    print("   control: B with the derivative term's sign reversed (n = 1) is not divergence-free (rejected): %s" % ctl)
    report('E1', ok_s and ok_t and uniq, [('sign', ctl)])
    return norms


# ------------------------------------------------------------------ E2
R_ = sp.Symbol('R', positive=True)
WJ = sp.symbols('w0:8')
SQ = sp.Symbol('SQ', positive=True)        # sqrt(w (2 - f w)) on the slice


def slice_background():
    """the class slice v = V(R) of Tangherlini (ingoing (v, R)), w = V': gamma_RR, K_RR, n^R, N_s, Y_s^R"""
    w = sp.Function('w')(R_)
    f = 1 - mu / R_**2
    v = sp.Symbol('v')
    X5 = [v, R_, th, p1, p2]
    g5 = sp.zeros(5, 5)
    g5[0, 0], g5[0, 1], g5[1, 0] = -f, 1, 1
    g5[2, 2], g5[3, 3], g5[4, 4] = R_**2, R_**2 * s_**2, R_**2 * c_**2
    gi5, Gam = christoffel(g5, X5)
    Del = w * (2 - f * w)
    sq = sp.sqrt(Del)
    nlow = [-1 / sq, w / sq, 0, 0, 0]                       # n = -(dv - w dR)/sqrt(Del): unit, future (n^v > 0)
    nup = [sp.together(sum(gi5[a, b] * nlow[b] for b in range(5))) for a in range(5)]
    eR = [w, 1, 0, 0, 0]
    KRR = sum(eR[a] * eR[b] * (sp.diff(nlow[b], X5[a]) - sum(Gam[l][a][b] * nlow[l] for l in range(5)))
              for a in range(5) for b in range(5))
    N = -nlow[0]                                            # N = -g(xi, n), xi = d_v
    YR = (1 - f * w) / Del
    checks = dict(
        unit=sp.simplify(sum(nup[a] * nlow[a] for a in range(5)) + 1) == 0,
        future=sp.simplify(nup[0] * sq - w) == 0,
        normal=sp.simplify(sum(nlow[a] * eR[a] for a in range(5))) == 0,
        decomposition=sp.simplify(1 - N * nup[0] - w * YR) == 0 and sp.simplify(-N * nup[1] - YR) == 0,
        NsqrtG=sp.simplify(N * sq - 1) == 0,
        lapse_shift=sp.simplify(N**2 - Del * YR**2 - f) == 0,
        KRR=sp.simplify(KRR - (R_**5 * sp.diff(w, R_) - R_**2 * mu * w**3 + 3 * R_**2 * mu * w**2 + mu**2 * w**3)
                        / (R_**5 * sq)) == 0)
    return dict(w=w, f=f, Del=Del, N=N, YR=YR, nR=nup[1], KRR=KRR, sq=sq, checks=checks)


def tensor_density():
    """theta-dependent Q-density of tensor data on an abstract round slice (TA generic, B and C from E1)"""
    Gf, Kf, nf, Nf, Yf, H, P = [sp.Function(nm)(R_) for nm in ('Gf', 'Kf', 'nf', 'Nf', 'Yf', 'H', 'P')]
    TA = sp.Function('TA')(th)
    u = sp.cos(2 * th)
    TB = (3 * u - 1) * TA / 2 + sp.sin(2 * th) * sp.diff(TA, th) / 2
    TC = -TA - TB
    Tu = sp.diag(0, TA * R_**2, TB * R_**2 * s_**2, TC * R_**2 * c_**2)
    g = sp.diag(Gf, R_**2, R_**2 * s_**2, R_**2 * c_**2) + eps * 2 * H * Tu
    K = sp.diag(Kf, R_ * nf, R_ * nf * s_**2, R_ * nf * c_**2) + eps * (P + 2 * nf * H / R_) * Tu
    Hc, M = QS.constraints_fast(g, K, [R_, th, p1, p2])
    lin = [sp.simplify(sp.expand(sp.diff(e, eps).subs(eps, 0))) for e in [Hc] + M]
    dens = sp.expand((Nf * sp.diff(Hc, eps, 2).subs(eps, 0) / 2 + 2 * Yf * sp.diff(M[0], eps, 2).subs(eps, 0) / 2)
                     * sp.sqrt(Gf) * R_**3 * s_ * c_)
    return dict(lin=lin, dens=dens, F=(Gf, Kf, nf, Nf, Yf, H, P), TA=TA)


def theta_integral(dens, TA, n):
    A = class_tt(n)[0]
    acc = {}
    for term in sp.Add.make_args(dens):
        ind, dep = term.as_independent(th, as_Add=False)
        acc[dep] = acc.get(dep, 0) + ind
    out = 0
    for dep, ind in acc.items():
        d = dep.subs(TA, A).doit()
        out += ind * sp.integrate(sp.expand(sp.expand_trig(sp.expand(d))), (th, 0, sp.pi / 2))
    return out


def reduce_sq(e, bg):
    """zero test in Q(R, mu, w-jets)[SQ]/(SQ^2 - Del): every derivative of the slice functions eliminated"""
    w, Del = bg['w'], bg['Del']
    e = e.subs(sp.sqrt(Del), SQ)
    for k in range(7, 0, -1):
        e = e.subs(sp.Derivative(w, (R_, k)), WJ[k])
    e = e.subs(w, WJ[0])
    D0 = Del.subs(w, WJ[0])
    e = sp.together(e)
    num = sp.expand(sp.numer(e))
    rem = sp.rem(sp.Poly(num, SQ), sp.Poly(SQ**2 - D0, SQ))
    return all(sp.cancel(cf) == 0 for cf in rem.all_coeffs())


def field_jets_zero(e, fns, bg, order=5):
    """e linear/quadratic in the jets of fns; every coefficient zero in the SQ-reduced field"""
    e = sp.expand(e)
    reps, syms = {}, []
    for i, fn in enumerate(fns):
        for k in range(order, 0, -1):
            s = sp.Symbol('fj%d_%d' % (i, k))
            reps[sp.Derivative(fn, (R_, k))] = s
            syms.append(s)
        s = sp.Symbol('fj%d_0' % i)
        reps[fn] = s
        syms.append(s)
    e = sp.expand(e.subs(reps))
    if e == 0:
        return True
    return all(reduce_sq(cf, bg) for cf in sp.Poly(e, *syms).coeffs())


def substitute_bg(e, F, bg):
    Gf, Kf, nf, Nf, Yf = F[:5]
    e = e.subs(sp.sqrt(Gf), bg['sq'])
    e = e.subs({Gf: bg['Del'], Kf: bg['KRR'], nf: bg['nR'], Nf: bg['N'], Yf: bg['YR']})
    return e.doit()


def e2():
    print("E2 (exact; w(R), mu symbolic) the tensor sector on every class slice v = V(R): E = 2 |T|^2 int T_m(xi, n)",
          flush=True)
    bg = slice_background()
    print("   the slice: n unit, future, normal; xi = N_s n + Y_s; N_s sqrt(gamma_RR) = 1; N_s^2 - gamma_RR (Y_s^R)^2 "
          "= f; K_RR closed form: %s" % bg['checks'])
    td = tensor_density()
    print("   linearised constraints of the tensor data vanish identically (TA generic): %s"
          % all(x == 0 for x in td['lin']))
    Gf, Kf, nf, Nf, Yf, H, P = td['F']
    HR = sp.diff(H, R_)
    ok, ctl, out = True, True, {}
    for n in (0, 1):
        A, B, C, kT2, l = class_tt(n)
        nT = sp.integrate(sp.expand(sp.expand_trig((A**2 + B**2 + C**2) * s_ * c_)), (th, 0, sp.pi / 2))
        Iq = theta_integral(td['dens'], td['TA'], n)
        Tm = R_**3 * ((Nf * P + Yf * HR) * P + sp.Rational(1, 2) * Nf * (-P**2 + HR**2 / Gf)) \
            + sp.Rational(1, 2) * Nf * (kT2 + 2) * R_ * H**2
        res = {}
        for scale in (1, sp.Rational(1, 2)):
            d = substitute_bg(Iq + 2 * scale * nT * Tm * sp.sqrt(Gf), td['F'], bg)
            els = [eq.lhs for eq in euler_equations(d, [H, P], [R_])]
            res[scale] = all(field_jets_zero(e, [H, P], bg) for e in els)
        out[l] = (nT, kT2, Iq)
        ok &= res[1]
        ctl &= not res[sp.Rational(1, 2)]
        print("   l = %d (|T|^2 = %s, k_T^2 = %d): Euler operator of Q-density + 2 |T|^2 T_m(xi, n) sqrt(gamma_RR) "
              "zero in H and P: %s; control |T|^2 -> |T|^2/2 (rejected): %s" % (l, nT, kT2, res[1],
                                                                               not res[sp.Rational(1, 2)]))
    # the (P, H_R) block of T_m and its determinant
    a11, a12, a22 = bg['N'] / 2, bg['YR'] / 2, bg['N'] / (2 * bg['Del'])
    det = sp.simplify((a11 * a22 - a12**2) * bg['Del'] - bg['f'] / 4)
    print("   T_m's (P, H_R) block R^3 [[N/2, Y/2], [Y/2, N/(2 gamma_RR)]] has determinant R^6 f/(4 gamma_RR) (N > 0): "
          "%s -- positive definite iff f > 0" % (det == 0))
    report('E2', ok and all(bg['checks'].values()) and all(x == 0 for x in td['lin']) and det == 0,
           [('|T|^2/2', ctl)])
    return bg, td, out


# ------------------------------------------------------------------ E3
def e3(bg, td, out):
    print("E3 (exact) M_b fails inside the horizon: tensor seeds with E < 0 on Part I's slice", flush=True)
    Gf, Kf, nf, Nf, Yf, H, P = td['F']
    nT, kT2, Iq = out[2]
    HR = sp.diff(H, R_)
    # (a) P = -(Y/N) H_R: Q = -|T|^2 int (R^3 f H_R^2 + (k_T^2 + 2) R H^2), on every slice
    d = substitute_bg(Iq.subs(P, -Yf / Nf * HR).doit() + nT * (R_**3 * (1 - mu / R_**2) * HR**2 + (kT2 + 2) * R_ * H**2),
                      td['F'], bg)
    a_ok = field_jets_zero(euler_equations(d, [H], [R_])[0].lhs, [H], bg)
    d0 = substitute_bg(Iq.subs(H, 0).doit() + nT * R_**3 * P**2, td['F'], bg)
    b_ok = field_jets_zero(euler_equations(d0, [P], [R_])[0].lhs, [P], bg)
    print("   with P = -(Y_s^R/N_s) H_R: Q = -|T|^2 int (R^3 f H_R^2 + (k_T^2 + 2) R H^2) dR on every class slice: %s;"
          " with H = 0: Q = -|T|^2 int R^3 P^2 dR < 0: %s" % (a_ok, b_ok))

    def Qband(R1, R2, mv, Hfun=None):
        Rr = sp.Symbol('Rr')
        Hh = (Rr - R1)**2 * (R2 - Rr)**2 if Hfun is None else Hfun(Rr)
        f = 1 - mv / Rr**2
        return -nT * sp.integrate(sp.expand(Rr**3 * f * sp.diff(Hh, Rr)**2 + (kT2 + 2) * Rr * Hh**2), (Rr, R1, R2))
    R1, R2 = sp.Rational(18, 25), sp.Rational(89, 100)
    mlo, mhi = sp.Rational(4, 5), sp.Rational(21, 25)
    q_lo, q_hi = Qband(R1, R2, mlo), Qband(R1, R2, mhi)
    mv = sp.Symbol('mv')
    affine = sp.degree(sp.expand(Qband(R1, R2, mv)), mv) == 1
    inside = R2**2 < mlo                        # the band lies inside the horizon for every mu in the interval
    c_ok = q_lo > 0 and q_hi > 0 and affine and inside
    print("   H = (R - R1)^2 (R2 - R)^2 on [R1, R2] = [0.72, 0.89] (R2^2 < 0.80: inside the horizon for every mu in "
          "[0.80, 0.84]; Part I's seed region: inner edge 0.683, horizon 0.9067, mu0 = 0.8221, qsign5 Q3): Q is "
          "affine in mu %s, Q(0.80) = %s = %.6e, Q(0.84) = %s = %.6e, both > 0: E < 0 for every mu there: %s"
          % (affine, q_lo, float(q_lo), q_hi, float(q_hi), c_ok))
    qp = -nT * sp.integrate(sp.Symbol('Rr')**3 * ((sp.Symbol('Rr') - R1)**2 * (R2 - sp.Symbol('Rr'))**2)**2,
                            (sp.Symbol('Rr'), R1, R2))
    print("   the momentum-only seed P = (R - R1)^2 (R2 - R)^2, H = 0, on the same band: Q = %.6e < 0 (any mu): %s; so Q "
          "changes sign along s -> (s H, -s (Y/N) H_R + (1 - s) P), every member non-gauge (nonzero TT part)"
          % (float(qp), qp < 0))
    # control: the band moved outside the horizon
    S1, S2 = sp.Rational(23, 25), sp.Rational(109, 100)
    cq_lo, cq_hi = Qband(S1, S2, mlo), Qband(S1, S2, mhi)
    outside = S1**2 > mhi
    ctl = cq_lo < 0 and cq_hi < 0 and outside
    print("   control: the band moved to [0.92, 1.09] (0.92^2 > 0.84: outside the horizon): Q(0.80) = %.6e, Q(0.84) = "
          "%.6e, both < 0, no E < 0 seed (rejected): %s" % (float(cq_lo), float(cq_hi), ctl))
    report('E3', a_ok and b_ok and c_ok and qp < 0, [('band moved', ctl)])


# ------------------------------------------------------------------ E4: the static slice, scalar modes
X4 = [r, th, p1, p2]
G0 = sp.diag(1 / f_, r**2, r**2 * s_**2, r**2 * c_**2)
GHAT = sp.diag(0, 1, s_**2, c_**2)
SF = sp.Function('S')(th)
THPTS = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(12, 13)),
         (sp.Rational(8, 17), sp.Rational(15, 17))]
s0, s1 = sp.symbols('s0 s1')
JR = Jets(['A', 'F', 'p', 'q', 'w', 'a', 'b', 'c', 'e', 'z', 'Z', 'l', 'al', 'be', 'ps'])


def shat():
    """S_ij hat = D^D^S + (k^2/3) gammahat S on the unit sphere (class S), in (r, th, phi1, phi2) slots"""
    DDS = sp.diag(0, sp.diff(SF, th, 2), s_ * c_ * sp.diff(SF, th), -s_ * c_ * sp.diff(SF, th))
    return DDS + (k2 / 3) * GHAT * SF


def eig_point(e, pt, fns):
    """impose Delta S = -k^2 S, evaluate at a rational angle, radial jets as JR symbols"""
    ct = c_ / s_ - s_ / c_
    S2 = -k2 * SF - ct * sp.diff(SF, th)
    S3 = sp.diff(S2, th).subs(sp.Derivative(SF, (th, 2)), S2)
    S4 = sp.diff(S3, th).subs(sp.Derivative(SF, (th, 2)), S2)
    e = e.subs(sp.Derivative(SF, (th, 4)), S4).subs(sp.Derivative(SF, (th, 3)), S3)
    e = e.subs(sp.Derivative(SF, (th, 2)), S2).subs(sp.Derivative(SF, th), s1).subs(SF, s0)
    e = JR.from_funcs(e, fns)
    e = e.subs({sp.sin(th): pt[0], sp.cos(th): pt[1], sp.tan(th): pt[0] / pt[1], sp.cot(th): pt[1] / pt[0]})
    return sp.expand(e)


def angular_reduce(e, fns, label):
    """the (S, S') structure of e at three rational angles; returns the common coefficients and theta-freeness"""
    res = []
    for pt in THPTS:
        x = eig_point(e, pt, fns)
        P = sp.Poly(x, s0, s1)
        res.append({mm: sp.cancel(cf) for mm, cf in zip(P.monoms(), P.coeffs()) if sp.cancel(cf) != 0})
    keys = set().union(*[set(x) for x in res])
    free = all(sp.cancel(x.get(kk, 0) - res[0].get(kk, 0)) == 0 for kk in keys for x in res)
    return {kk: res[0].get(kk, 0) for kk in keys}, free


def e4():
    print("E4 (exact) scalar modes on the static slice: structure, gauge maps, gauge invariance", flush=True)
    names = ['A', 'F', 'p', 'q', 'w']
    A, F, p, q, w = [sp.Function(nm)(r) for nm in names]
    gh = sp.diag(1, 0, 0, 0) * A * SF + 2 * F * SF * r**2 * GHAT
    kk = sp.zeros(4, 4)
    kk[0, 0] = p * SF
    kk[0, 1] = kk[1, 0] = r * q * sp.diff(SF, th)
    kk += r**2 * w * SF * GHAT
    Hc, _ = QS.constraints_fast(G0 + eps * gh, sp.zeros(4, 4), X4)
    R1 = sp.diff(Hc, eps).subs(eps, 0)
    R2 = sp.diff(Hc, eps, 2).subs(eps, 0)
    Hk, Mk = QS.constraints_fast(G0, eps * kk, X4)
    MK = [sp.diff(x, eps).subs(eps, 0) for x in Mk]
    HK2 = sp.diff(Hk, eps, 2).subs(eps, 0)
    N = sp.sqrt(f_)
    fns = [A, F, p, q, w]
    rC, ok1 = angular_reduce(R1, fns, 'C')
    rM0, ok2 = angular_reduce(MK[0], fns, 'M_R')
    rM1, ok3 = angular_reduce(MK[1], fns, 'M_th')
    rM23 = [angular_reduce(MK[i], fns, 'M_phi') for i in (2, 3)]
    rV, ok4 = angular_reduce(-N * R2 / 2, fns, 'E_V')
    rK, ok5 = angular_reduce(-N * HK2 / 2, fns, 'E_K')
    shape = (set(rC) <= {(1, 0)} and set(rM0) <= {(1, 0)} and set(rM1) <= {(0, 1)}
             and all(set(x[0]) == set() for x in rM23) and set(rV) <= {(2, 0), (0, 2)} and set(rK) <= {(2, 0), (0, 2)})
    vol = r**3 / sp.sqrt(f_)                       # sqrt(gamma) = vol sin th cos th; int S'^2 = k^2 int S^2
    rad = dict(C=rC.get((1, 0), 0), M0=rM0.get((1, 0), 0), M1=rM1.get((0, 1), 0),
               EV=sp.expand(vol * (rV.get((2, 0), 0) + k2 * rV.get((0, 2), 0))),
               EK=sp.expand(vol * (rK.get((2, 0), 0) + k2 * rK.get((0, 2), 0))))
    print("   (a) Regge-Wheeler-type gauge: C ~ S, M_R ~ S, M_th ~ S', M_phi = 0, E_V and E_K ~ S^2, S'^2, every "
          "coefficient free of th (equal at three rational angles): %s, %s" % (shape, ok1 and ok2 and ok3 and ok4
                                                                                 and ok5))
    # (b) the gauge maps
    al, be, ps = [sp.Function(nm)(r) for nm in ('al', 'be', 'ps')]
    gi, Gm = christoffel(G0, X4)
    Xv = [al * SF, be * sp.diff(SF, th), 0, 0]
    LX = sp.Matrix(4, 4, lambda i, j: sum(Xv[k] * sp.diff(G0[i, j], X4[k]) + G0[k, j] * sp.diff(Xv[k], X4[i])
                                          + G0[i, k] * sp.diff(Xv[k], X4[j]) for k in range(4)))
    da = sp.diff(1 / f_, r) * al + 2 * sp.diff(al, r) / f_
    db = al / (r * f_) + r * sp.diff(be, r)
    dc = 2 * al / r - 2 * k2 * be / 3
    de = 2 * be
    SH = shat()
    claim = sp.diag(1, 0, 0, 0) * da * SF + r**2 * (dc * SF * GHAT + de * SH)
    claim[0, 1] = claim[1, 0] = r * db * sp.diff(SF, th)
    fb = [al, be]
    gok = all(set(angular_reduce(LX[i, j] - claim[i, j], fb, 'LX')[0]) == set() for i in range(4) for j in range(i, 4))
    Ric = ricci(X4, Gm)
    kps = hess(ps * SF, X4, Gm) - ps * SF * Ric
    zc = []
    for i in (2, 3):              # the phi-components carry the z-shift: (D^D^S)_ii + ... compare to psi/r^2 S_hat
        pass
    # z-shift: the trace-free angular part of k_psi equals r^2 (psi/r^2) (S_hat)^TF
    ang = sp.Matrix(3, 3, lambda i, j: kps[i + 1, j + 1])
    SHa = sp.Matrix(3, 3, lambda i, j: SH[i + 1, j + 1])
    gh3 = sp.diag(1, s_**2, c_**2)
    tr_ang = sum(ang[i, i] / gh3[i, i] for i in range(3)) / 3
    tf = ang - tr_ang * gh3
    zok = all(set(angular_reduce(tf[i, i] - ps * (SHa[i, i] - k2 * SF * gh3[i, i] / 3 * 0) + ps * 0, [ps], 'z')[0])
              == set() or True for i in range(3))
    tf_claim = ps * (SHa - (sum(SHa[i, i] / gh3[i, i] for i in range(3)) / 3) * gh3)
    zok = all(set(angular_reduce(tf[i, i] - tf_claim[i, i], [ps], 'z')[0]) == set() for i in range(3))
    # the spatial invariants are unchanged by the shifts
    a_, b_, c__, e_ = [sp.Function(nm)(r) for nm in ('a', 'b', 'c', 'e')]

    def inv(a, b, c, e):
        alpha = -r * f_ * (b - r * sp.diff(e, r) / 2)
        Ai = a + sp.diff(1 / f_, r) * alpha + 2 * sp.diff(alpha, r) / f_
        Fi = c / 2 - f_ * b + k2 * e / 6 + f_ * r * sp.diff(e, r) / 2
        return Ai, Fi
    I0 = inv(a_, b_, c__, e_)
    I1 = inv(a_ + da, b_ + db, c__ + dc, e_ + de)
    invok = all(sp.simplify((x1 - x0).doit()) == 0 for x0, x1 in zip(I0, I1))
    print("   (b) L_X gamma, X = alpha S d_R + beta S' d_th, shifts (a, b, c, e) by ((1/f)' alpha + 2 alpha'/f, alpha/(R "
          "f) + R beta', 2 alpha/R - (2 k^2/3) beta, 2 beta): %s; the lapse direction k_psi has trace-free angular "
          "part psi (S_hat)^TF (z-shift psi/R^2): %s; A = a + (1/f)' al + 2 al'/f (al = -R f (b - R e'/2)), F = c/2 - f "
          "b + k^2 e/6 + f R e'/2 are invariant: %s" % (gok, zok, invok))
    okc = mode_free(gi, Gm, Ric)
    report('E4', shape and ok1 and ok2 and ok3 and ok4 and ok5 and gok and zok and invok and okc)
    return rad


def jet_points(e, fns, pts):
    """e linear (or quadratic) in the jets of fns (functions of r, th): zero at the points, jets free"""
    reps, syms = {}, []
    for i, fn in enumerate(fns):
        ds = sorted({d for d in e.atoms(sp.Derivative) if d.expr == fn}, key=lambda d: -len(d.variables))
        for j, d in enumerate(ds):
            s = sp.Symbol('jj%d_%d' % (i, j))
            reps[d] = s
            syms.append(s)
    for d, s in reps.items():
        e = e.subs(d, s)
    for i, fn in enumerate(fns):
        s = sp.Symbol('jz%d' % i)
        e = e.subs(fn, s)
        syms.append(s)
    out = []
    for pt in pts:
        v = sp.expand(e.subs(pt))
        out.append(v == 0 or all(sp.simplify(cf) == 0 for cf in sp.Poly(v, *syms).coeffs()))
    return all(out)


PTS2 = [{r: sp.Rational(3, 2), th: sp.atan(sp.Rational(3, 4)), mu: sp.Rational(7, 5)},
        {r: 2, th: sp.atan(sp.Rational(5, 12)), mu: sp.Rational(9, 10)},
        {r: sp.Rational(5, 2), th: sp.atan(sp.Rational(8, 15)), mu: 3}]


def mode_free(gi, Gm, Ric):
    """E4 (c): gauge invariance of E_V and E_K on the constraint surface, for class fields of (r, th)"""
    n = 4
    N = sp.sqrt(f_)
    vol = r**3 * s_ * c_ / sp.sqrt(f_)

    def lap0(u):
        return sum(sp.diff(vol * gi[i, i] * sp.diff(u, X4[i]), X4[i]) for i in range(n)) / vol

    def divv(V):                      # V lower-index covector
        return sum(sp.diff(vol * gi[i, i] * V[i], X4[i]) for i in range(n)) / vol

    def divT(T):
        DT = cov2(T, X4, Gm)
        return [sum(gi[c, a] * DT[a][b][c] for a in range(n) for c in range(n) if gi[c, a] != 0) for b in range(n)]

    def trace(T):
        return sum(gi[i, i] * T[i, i] for i in range(n))

    def DR(h):
        return -lap0(trace(h)) + divv(divT(h)) - sum(gi[i, i] * gi[j, j] * Ric[i, j] * h[i, j] for i in range(n)
                                                       for j in range(n))

    def Mom(k):
        dk = divT(k)
        tk = trace(k)
        return [dk[i] - sp.diff(tk, X4[i]) for i in range(n)]
    Xr, Xt = sp.Function('Xr')(r, th), sp.Function('Xt')(r, th)
    Xv = [Xr, Xt, 0, 0]
    LX = sp.Matrix(4, 4, lambda i, j: sum(Xv[k] * sp.diff(G0[i, j], X4[k]) + G0[k, j] * sp.diff(Xv[k], X4[i])
                                          + G0[i, k] * sp.diff(Xv[k], X4[j]) for k in range(4)))
    i_ok = jet_points(DR(LX), [Xr, Xt], PTS2)
    hn = ['hrr', 'hrt', 'htt', 'h11', 'h22']
    hf = [sp.Function(nm)(r, th) for nm in hn]
    h = sp.Matrix([[hf[0], hf[1], 0, 0], [hf[1], hf[2], 0, 0], [0, 0, hf[3], 0], [0, 0, 0, hf[4]]])
    L = N * DR(h) * vol
    els = [eq.lhs for eq in euler_equations(L, hf, [r, th])]
    ii_ok = all(sp.simplify(e.subs(pt)) == 0 for e in els for pt in PTS2)
    ps = sp.Function('psi')(r, th)
    kps = hess(ps, X4, Gm) - ps * Ric
    iii_ok = all(jet_points(m, [ps], PTS2) for m in Mom(kps))
    kn = ['krr', 'krt', 'ktt', 'k11', 'k22']
    kf = [sp.Function(nm)(r, th) for nm in kn]
    k = sp.Matrix([[kf[0], kf[1], 0, 0], [kf[1], kf[2], 0, 0], [0, 0, kf[3], 0], [0, 0, 0, kf[4]]])
    b = N * (sum(gi[i, i] * gi[j, j] * k[i, j] * kps[i, j] for i in range(n) for j in range(n))
             - trace(k) * trace(kps)) * vol
    lhs = euler_equations(b, [ps], [r, th])[0].lhs
    M = Mom(k)
    rhs = vol * (2 * sum(gi[i, i] * sp.diff(N, X4[i]) * M[i] for i in range(n)) + N * divv(M))
    iv_ok = jet_points(lhs - rhs, kf, PTS2)
    print("   (c) mode-free, class fields of (R, th): D R[L_X gamma] = 0: %s; (D R)^* N = 0 (Euler operator of N D R[h] "
          "sqrt(gamma) zero in all five components): %s; M[k_psi] = 0: %s; Euler_psi of N(<k, k_psi> - tr k tr k_psi) "
          "sqrt(gamma) = sqrt(gamma)(2 dN.M[k] + N div M[k]): %s" % (i_ok, ii_ok, iii_ok, iv_ok), flush=True)
    return i_ok and ii_ok and iii_ok and iv_ok
