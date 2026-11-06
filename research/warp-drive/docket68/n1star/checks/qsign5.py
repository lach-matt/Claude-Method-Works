#!/usr/bin/env python3
"""qsign5: the sign of the one charge of exactly localised data on Part I's slice (FAMILIES5-R6.md section 1).

Setting (FAMILIES5-VLASOV.md section 4, Proposition L'): on a vacuum band U of Part I's Sigma_tau0 the data background
+ eps delta + c, c = O(eps^2) supported in U, satisfy the constraints up to a multiple of the one invariant KID (the
static one), with coefficient eps^2 Q(delta) + O(eps^3). A momentum seed is delta = (0, dK): dgamma = 0, dK solving the
linearised constraints, compactly supported in U. In components K_RR = G kappa, K_Rth = sqrt(G) p, K_thth = R^2 (Kt/3
+ s1), K_11 = G1 (Kt/3 + s2), K_22 = G2 (Kt/3 - s1 - s2) on gamma = G dR^2 + R^2 dOmega_3^2, K0 = kappa0 nhat nhat +
Y0 R^2 dOmega_3^2, the linearised Hamiltonian constraint fixes dkappa, M_R is a divergence (so dKt, dp come from a
stream function psi, bandconst5 B4) and M_th fixes ds2; ds1 is free. So every momentum seed is a pair (psi, s1) of
compactly supported functions, and Q = int N_s ((tr dK)^2 - |dK|^2) dvol (the momentum constraint is linear in K at
fixed gamma).

  Q1 (exact, sympy; the identity for arbitrary G, kappa0, Y0 and weight nu, exact at three rational points with explicit
     functions) with nu := N_s sqrt(G) R^3, beta := -kappa0/(3 Y0), a := -3 (1 - beta)/R, E := e^(int a), sc := sin th
     cos th, Z := ds2 + ds1/2, X := d_th psi - (3/2)(cos 2th/sc) psi, P := 8 nu E^2 R/G - (2 nu E R/sqrt G)' R E/sqrt G,
     the Q-density differs from
         -2 nu sc (Z - E psi/(2 sc^2))^2 - (3/2) nu sc (ds1 - 2 E X/(3 sc))^2 - Gamma psi^2/sin 2th,
         Gamma := 4 nu E^2 - P',
     by a divergence in (R, th): its Euler operator in psi and in s1 vanishes. Hence for every momentum seed
         Q <= - int int Gamma psi^2 / sin 2th dth dR (times the torus volume),                                   (QB)
     so Q < 0 for every nonzero momentum seed wherever Gamma > 0 (if psi = 0, Q = -int nu sc (2 (T s1)^2 +
     (3/2) s1^2) with T s1 = sc d_th s1 + (3/2) cos 2th s1). Control (must fail): the identity with 4 nu E^2 replaced by
     3 nu E^2 has a nonzero Euler operator.
  Q2 (exact, sympy) on every vacuum region of Part I's chart (g0 = -e^(2 psi_P) f dvhat^2 + 2 e^psi_P dvhat dR + R^2
     dOmega_3^2, psi_P = psi_P(vhat), f = 1 - mu/R^2, slice tau = vhat - R): N_s sqrt(G) = 1, so nu = R^3;
     Gamma/E^2 as an explicit function of (R, mu, psi_P, psi_P', psi_P''); where psi_P = 0 (outside the packet: the
     gap and outside the shell) E = sqrt(G)/R and Gamma = 4 mu/R exactly: the margin is the mass. Control (must fail):
     with P's coefficient 8 -> 6 Gamma at psi_P = 0 is not 4 mu/R.
  Q3 (computed, floating point; twobg5's background at n = 80, 160) Gamma > 0 on the seed region (region III, psi_P =
     psi_III(vhat) read as in racglobal5 R4), including its part inside the horizon; psi_P = 0 on the slice's vacuum
     points with u <= u1 (the gap and outside the shell), so Gamma = 4 mu/R > 0 there by Q2.
  Q4 (computed, floating point) the bound on explicit seeds: for racglobal5 R4's 45 stream seeds (ds1 = 0) and 30 seeds
     with ds1 != 0 (including ds1 equal to the maximiser 2 E X/(3 sc)), Q computed directly equals the integral of the
     decomposition to the quadrature's accuracy, and Q <= -int Gamma psi^2/sin 2th < 0 for every one. Control (must
     fail): the decomposition with the -Gamma psi^2/sin 2th term dropped does not reproduce Q.
  Q5 (exact, sympy; ingoing Vaidya in Part I's chart, psi_P = 0, mu = mu(vhat) arbitrary) the KID and the matter term:
     (a) (N_s, 2 Y_s) is in the kernel of the adjoint of the linearised constraint map (H, M) on Tangherlini's slice
         (the Euler operator of sqrt(gamma)(N_s DH + 2 Y_s^R DM_R) in all nine invariant fields of (dgamma diagonal,
         dK) vanishes), Y_s^R = mu/(G R^2); control: (N_s, Y_s) is not;
     (b) on the Vaidya slice data, N_s H + 2 Y_s^R M_R = 2 T(xi, n) with T the Vaidya stress (3 mu'/(2 R^3)) dvhat^2,
         xi = d_vhat: the KID pairs the constraint map with 2 T(xi, n), so exact data with matter need
         eps^2 Q/2 + O(eps^3) = int_U T(xi, n);
     (c) for radial null dust, T(xi, n) = q f sqrt(2 - f)/4 along l_out = d_vhat + (f/2) d_R and q/sqrt(2 - f) along
         l_in = -d_R: negative exactly for outgoing dust inside the horizon (f < 0); for xi future-causal (f >= 0) and
         any matter with the dominant energy condition T(xi, n) >= 0.
  Q6 (computed) on a band inside the horizon (R in [0.72, 0.9]) a momentum seed with Q < 0 and an outgoing dust profile
     q1 >= 0 there give int T1(xi, n) < 0, so the dust amplitude s* = Q/(2 int T1(xi, n)) > 0 cancels the charge at
     second order: the intermediate-value construction of exactly localised Einstein-null-dust data inside the horizon.
     Control: the same dust on a band outside the horizon gives int T1(xi, n) > 0 (no positive s*).

Labels: computed (Q1, Q2, Q5 exact; Q3, Q4, Q6 floating point). Run: python3 checks/qsign5.py   (several minutes)
"""
import importlib.util
import math
import os
import sys

import numpy as np
import sympy as sp
from sympy.calculus.euler import euler_equations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
R, th = sp.symbols('R theta', positive=True)
PTS = [{R: sp.Rational(3, 2), th: sp.atan(sp.Rational(3, 4))}, {R: 2, th: sp.atan(sp.Rational(5, 12))},
       {R: sp.Rational(7, 3), th: sp.atan(sp.Rational(8, 15))}]


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def jet_zero(expr, fns, funcs, subder, pts=PTS):
    """expr linear in the jets of fns: substitute explicit background functions, then every jet coefficient = 0."""
    e = subder(expr)
    for nm, lam in funcs.items():
        e = e.replace(sp.Function(nm), lam)
    e = subder(e.doit())
    jets = sorted({d for d in e.atoms(sp.Derivative) if d.expr in fns}, key=str)
    js = {j: sp.Symbol('j%d' % i) for i, j in enumerate(jets)}
    z = {fn: sp.Symbol('z%d' % i) for i, fn in enumerate(fns)}
    e = e.xreplace(js).xreplace(z)
    syms = list(js.values()) + list(z.values())
    res = []
    for pt in pts:
        v = sp.expand(e.subs(pt))
        if v == 0:
            res.append(True)
            continue
        res.append(all(sp.simplify(cf) == 0 for cf in sp.Poly(v, *syms).coeffs()))
    return res


# ---------------------------------------------------------------- Q1
G_, k0_, Y0_, Nu_, Ia_ = [sp.Function(nm)(R) for nm in ('G', 'kappa0', 'Y0', 'Nu', 'Ia')]
PSI, S1 = sp.Function('psi')(R, th), sp.Function('s1')(R, th)


def seed_fields(G, k0, Y0, Ia, psi, s1):
    sc = sp.sin(th) * sp.cos(th)
    c = -(k0 + 2 * Y0) / (3 * Y0)
    beta = c + sp.Rational(2, 3)
    E = sp.exp(Ia)
    Kt = E * sp.diff(psi, th) / sc
    ph = R / sp.sqrt(G) * E * sp.diff(psi, R) / sc                       # the orthonormal K_Rth = p/R
    s2 = sc * (sp.diff(R**4 * ph, R) / (sp.sqrt(G) * R**3) - beta * sp.diff(Kt, th) + sp.diff(s1, th)
               + (sp.cot(th) - 2 * sp.tan(th)) * s1)
    return sc, c, beta, E, Kt, ph, s2


def decomposition(nu, G, E, psi, s1, s2, m_gam=1, drop_gamma=False):
    sc = sp.sin(th) * sp.cos(th)
    Z = s2 + s1 / 2
    X = sp.diff(psi, th) - sp.Rational(3, 2) * sp.cos(2 * th) / sc * psi
    P = 8 * nu * E**2 * R / G - sp.diff(2 * nu * E * R / sp.sqrt(G), R) * (R * E / sp.sqrt(G))
    Gam = 4 * m_gam * nu * E**2 - sp.diff(P, R)
    out = (-2 * nu * sc * (Z - E * psi / (2 * sc**2))**2 - sp.Rational(3, 2) * nu * sc * (s1 - 2 * E * X / (3 * sc))**2)
    if not drop_gamma:
        out = out - Gam * psi**2 / sp.sin(2 * th)
    return out, Gam


def q1():
    print("Q1 (exact) the momentum-seed charge is minus a sum of squares minus Gamma psi^2/sin 2th, up to a divergence")
    bc = load('bandconst5')
    # the linearised constraints and the quadratic part of H from the record's constraint map (bandconst5)
    eps = sp.Symbol('eps')
    dKt, dp, ds1, ds2, dkap = [sp.Function(nm)(R, th) for nm in ('dKt', 'dp', 'ds1', 'ds2', 'dkappa')]
    G1, G2 = R**2 * sp.sin(th)**2, R**2 * sp.cos(th)**2
    g = sp.diag(G_, R**2, G1, G2)
    Kt = 3 * Y0_ + eps * dKt
    K = sp.zeros(4, 4)
    K[0, 0] = G_ * (k0_ + eps * dkap)
    K[0, 1] = K[1, 0] = sp.sqrt(G_) * eps * dp
    K[1, 1] = R**2 * (Kt / 3 + eps * ds1)
    K[2, 2] = G1 * (Kt / 3 + eps * ds2)
    K[3, 3] = G2 * (Kt / 3 - eps * ds1 - eps * ds2)
    H, M, _ = bc.constraints(g, K, bc.X4)                           # bandconst5's R, theta are these symbols
    lin = [sp.expand(sp.diff(e, eps).subs(eps, 0)) for e in (H, M[0], M[1])]
    quad = sp.expand(sp.diff(H, eps, 2).subs(eps, 0) / 2)
    dk = sp.solve(sp.Eq(lin[0], 0), dkap)[0]
    sc, c, beta, E, Ktf, ph, s2f = seed_fields(G_, k0_, Y0_, Ia_, PSI, S1)
    a = (3 * c - 1) / R

    def subIa(e):
        for k in range(7, 0, -1):
            e = e.subs(sp.Derivative(Ia_, (R, k)), sp.diff(a, R, k - 1))
        return e
    funcs = {'G': sp.Lambda(R, (1 + R / 2)**2), 'kappa0': sp.Lambda(R, -(1 + R) / (2 + R**2)),
             'Y0': sp.Lambda(R, (R + 3) / (R**2 + 1)), 'Nu': sp.Lambda(R, R**3 / (1 + R**2)),
             'Ia': sp.Lambda(R, 0)}

    def at_pts(e):
        e = subIa(e)
        for nm, lam in funcs.items():
            e = e.replace(sp.Function(nm), lam)
        e = subIa(e.doit())
        return e
    # (i) the seed solves the linearised constraints: H, M_R, M_th vanish
    res = []
    for e in lin:
        e2 = e.subs(dkap, dk).subs({dKt: Ktf, dp: R * ph, ds1: S1, ds2: s2f}).doit()
        res += jet_zero(e2, [PSI, S1], {k: v for k, v in funcs.items() if k != 'Ia'}, subIa)
    # (ii) the Q-density from the record's quadratic form
    qd = Nu_ * sc * quad.subs(dkap, dk).subs({dKt: Ktf, dp: R * ph, ds1: S1, ds2: s2f}).doit()
    dec, _ = decomposition(Nu_, G_, E, PSI, S1, s2f)
    print("   the seed (psi, s1) solves the linearised H, M_R, M_th (every jet coefficient zero at three points):",
          all(res))
    el = [eq.lhs for eq in euler_equations(qd - dec, [PSI, S1], [R, th])]
    ok_id = []
    for e in el:
        ok_id += jet_zero(e, [PSI, S1], {k: v for k, v in funcs.items() if k != 'Ia'}, subIa)
    print("   Euler operator of (Q-density - decomposition) in psi and s1 vanishes at three points:", all(ok_id))
    dec_m, _ = decomposition(Nu_, G_, E, PSI, S1, s2f, m_gam=sp.Rational(3, 4))
    el_m = [eq.lhs for eq in euler_equations(qd - dec_m, [PSI, S1], [R, th])]
    ctl = not all(jet_zero(el_m[0], [PSI, S1], {k: v for k, v in funcs.items() if k != 'Ia'}, subIa))
    print("   control: with 4 nu E^2 -> 3 nu E^2 the Euler operator in psi is nonzero (rejected):", ctl)
    return all(res) and all(ok_id) and ctl


# ---------------------------------------------------------------- Q2
MU = sp.Symbol('mu', positive=True)
PP = sp.symbols('p0 p1 p2', real=True)


def gamma_formula(c8=8):
    """Gamma/E^2 on a vacuum region of Part I's chart, in (R, mu, psi_P, psi_P', psi_P'')."""
    psiP = sp.Function('psiP')(R)
    Ep = sp.exp(psiP)
    f = 1 - MU / R**2
    fR = sp.diff(f, R)
    G = 2 * Ep - Ep**2 * f
    Kt0 = 3 * (Ep * f - 1) / (Ep * R * sp.sqrt(2 / Ep - f))
    Nk = Ep**2 * f * fR / 2 - 3 * Ep * fR / 2 - sp.diff(psiP, R)            # bandconst5 B2, psi_R = f_v = 0
    kap0 = -Nk / (Ep * sp.sqrt(2 / Ep - f) * (2 - Ep * f))
    Ns = sp.exp(-psiP) / sp.sqrt(2 * sp.exp(-psiP) - f)                     # racglobal5 R3
    one = sp.simplify(Ns**2 * G - 1) == 0
    beta = -kap0 / Kt0
    a = -3 * (1 - beta) / R
    Ia = sp.Function('Ia')(R)
    E = sp.exp(Ia)
    nu = R**3
    P = c8 * nu * E**2 * R / G - sp.diff(2 * nu * E * R / sp.sqrt(G), R) * (R * E / sp.sqrt(G))
    Gam = sp.expand((4 * nu * E**2 - sp.diff(P, R)) / E**2)
    for k in range(4, 0, -1):
        Gam = Gam.subs(sp.Derivative(Ia, (R, k)), sp.diff(a, R, k - 1))
    Gam = Gam.doit().subs(sp.Derivative(psiP, (R, 2)), PP[2]).subs(sp.Derivative(psiP, R), PP[1]).subs(psiP, PP[0])
    a0 = a.subs(sp.Derivative(psiP, R), PP[1]).subs(psiP, PP[0])
    return one, Gam, a0


def q2():
    print("Q2 (exact) Part I's vacuum regions: nu = R^3, and Gamma = 4 mu/R where psi_P = 0")
    one, Gt, a0 = gamma_formula()
    f = 1 - MU / R**2
    G0 = 2 - f
    E0 = sp.sqrt(G0) / R
    a00 = sp.simplify(a0.subs({PP[0]: 0, PP[1]: 0}))
    e_ok = sp.simplify(a00 - sp.diff(sp.log(E0), R)) == 0
    g00 = sp.simplify(Gt.subs({PP[0]: 0, PP[1]: 0, PP[2]: 0}) * E0**2 - 4 * MU / R) == 0
    _, Gm, _ = gamma_formula(c8=6)
    ctl = sp.simplify(Gm.subs({PP[0]: 0, PP[1]: 0, PP[2]: 0}) * E0**2 - 4 * MU / R) != 0
    print("   N_s sqrt(G) = 1 on every vacuum region (nu = R^3): %s; at psi_P = 0, E = sqrt(G)/R: %s, Gamma = 4 mu/R: %s"
          % (one, e_ok, g00))
    print("   control: with P's coefficient 8 -> 6, Gamma at psi_P = 0 is not 4 mu/R (rejected): %s" % ctl)
    return one and e_ok and g00 and ctl, Gt


# ---------------------------------------------------------------- background (twobg5)
def background(n):
    tb = load('twobg5')
    uu, vv, Rg, S, Ru, Rv, mu = tb.run(n)
    ia = uu >= tb.U2P + 0.1
    mu0 = float(np.nanmedian(mu[ia, 0][np.isfinite(mu[ia, 0])]))
    k3 = int(np.argmin(np.abs(uu - (tb.U2P + 0.1))))
    dv = vv[1] - vv[0]
    vhp = -np.exp(2 * S[0]) / Ru[0]
    vh = np.concatenate([[0.0], np.cumsum((vhp[1:] + vhp[:-1]) / 2 * dv)])
    psi = np.log(-np.exp(2 * S[k3]) / (Ru[k3] * vhp))
    m = np.isfinite(psi)
    from scipy.interpolate import UnivariateSpline
    sp_psi = UnivariateSpline(vh[m], psi[m], k=5, s=len(vh[m]) * 1e-10)
    tau0 = -tb.AA + 0.02
    # psi_P on the slice's vacuum points with u <= u1 (outside the packet): the slice crossing of each ray u
    E_out = []
    for i in range(len(uu)):
        if uu[i] > tb.U1P - 0.1:
            continue
        tau = vh - Rg[i]
        mm = np.isfinite(tau)
        t = tau[mm]
        j = np.where(mm)[0]
        k = np.searchsorted(t, tau0)
        if k == 0 or k >= len(t):
            continue
        j0, j1 = j[k - 1], j[k]
        w = (tau0 - tau[j0]) / (tau[j1] - tau[j0])
        s_ = (1 - w) * S[i, j0] + w * S[i, j1]
        ru = (1 - w) * Ru[i, j0] + w * Ru[i, j1]
        vp = (1 - w) * vhp[j0] + w * vhp[j1]
        E_out.append(np.exp(2 * s_) / (-ru * vp))
    return dict(tb=tb, mu0=mu0, sp_psi=sp_psi, tau0=tau0, psi_out=np.log(np.array(E_out)))


def region3_funcs(bg, Rs):
    sp_psi, tau0, mu0 = bg['sp_psi'], bg['tau0'], bg['mu0']
    P = sp_psi(tau0 + Rs)
    dP = sp_psi.derivative(1)(tau0 + Rs)
    d2P = sp_psi.derivative(2)(tau0 + Rs)
    Ee = np.exp(P)
    f = 1 - mu0 / Rs**2
    fR = 2 * mu0 / Rs**3
    Nk = Ee**2 * f * fR / 2 - 3 * Ee * fR / 2 - dP
    kap = -Nk / (Ee * np.sqrt(2 / Ee - f) * (2 - Ee * f))
    KtN = 3 * (Ee * f - 1) / (Ee * Rs * np.sqrt(2 / Ee - f))
    Gn = -Ee**2 * f + 2 * Ee
    Ns = np.exp(-P) / np.sqrt(2 * np.exp(-P) - f)
    beta = -kap / KtN
    aR = -3 * (1 - beta) / Rs
    Ia = np.concatenate([[0.0], np.cumsum((aR[1:] + aR[:-1]) / 2 * np.diff(Rs))])
    Ia -= np.interp(1.25, Rs, Ia)
    return dict(P=P, dP=dP, d2P=d2P, f=f, G=Gn, Ns=Ns, beta=beta, a=aR, Ia=Ia, kap=kap, Kt=KtN, mu0=mu0,
                Y=(1 - Ee * f) / (2 - Ee * f), E_P=Ee)


def q3(Gt, bgs):
    print("Q3 (computed) Gamma > 0 on Part I's seed region; psi_P = 0 on the gap and outside the shell")
    lam = sp.lambdify([R, MU] + list(PP), Gt, 'numpy')
    ok, rows = True, []
    for n, bg in bgs.items():
        Rs = np.linspace(0.70, 1.85, 2301)
        F = region3_funcs(bg, Rs)
        g_over_E2 = lam(Rs, F['mu0'], F['P'], F['dP'], F['d2P'])
        Gam = g_over_E2 * np.exp(2 * F['Ia'])
        ratio = Gam / (4 * F['mu0'] / Rs * np.exp(2 * F['Ia']) * Rs**4 / (Rs**2 + F['mu0']))   # 1 at psi_P = 0
        rh = math.sqrt(F['mu0'])
        rows.append((n, float(np.min(g_over_E2)), float(np.min(ratio)), float(np.max(ratio)), rh,
                     float(np.max(np.abs(bg['psi_out']))), len(bg['psi_out'])))
        ok &= np.min(g_over_E2) > 0
    for (n, mn, rmin, rmax, rh, po, npo) in rows:
        print("   n = %d: R in [0.70, 1.85] (horizon at %.4f): min Gamma/E^2 = %.4f > 0; Gamma over its psi_P = 0 value "
              "in [%.4f, %.4f]; |psi_P| <= %.1e on %d slice points with u <= u1 - 0.1" %
              (n, mn, rmin, rmax, rh, po, npo))
    conv = abs(rows[0][1] - rows[1][1]) < 1e-2 * abs(rows[1][1])
    small = rows[-1][5] < 1e-3 and rows[-1][5] < rows[0][5]
    print("   converged (min Gamma/E^2 to 1%%): %s; psi_P = 0 outside the packet to discretisation (falling with n; "
          "exact by twobg5 G1 (b)): %s" % (conv, small))
    return ok and conv and small


# ---------------------------------------------------------------- Q4
def bump(x, a, b):
    y = 2 * (x - a) / (b - a) - 1
    out = np.zeros_like(y)
    mm = np.abs(y) < 1
    out[mm] = np.exp(1 - 1 / (1 - y[mm]**2))
    return out


def seed_Q(F, Rs, Th, core, s1=None, s1_star=False, drop_gamma=False, gam=None):
    """Q directly and through the decomposition, for psi = core (an array on Rs x Th) and s1."""
    RR, TT = np.meshgrid(Rs, Th, indexing='ij')
    dR_, dT_ = Rs[1] - Rs[0], Th[1] - Th[0]
    d = lambda A, ax: np.gradient(A, dR_ if ax == 0 else dT_, axis=ax, edge_order=2)   # noqa: E731
    sc = np.sin(TT) * np.cos(TT)
    E = np.exp(F['Ia'])[:, None]
    G = F['G'][:, None]
    beta = F['beta'][:, None]
    c = beta - 2 / 3
    Kt = E * d(core, 1) / sc
    ph = RR / np.sqrt(G) * E * d(core, 0) / sc
    X = d(core, 1) - 1.5 * np.cos(2 * TT) / sc * core
    if s1_star:
        s1 = 2 * E * X / (3 * sc)
    if s1 is None:
        s1 = np.zeros_like(core)
    s2 = sc * (d(RR**4 * ph, 0) / (np.sqrt(G) * RR**3) - beta * d(Kt, 1) + d(s1, 1)
               + (np.cos(TT) / np.sin(TT) - 2 * np.tan(TT)) * s1)
    nu = RR**3                                                              # N_s sqrt(G) R^3, Q2
    q = nu * sc * (2 * c * Kt**2 + (2 / 3) * Kt**2 - 2 * ph**2 - s1**2 - s2**2 - (s1 + s2)**2)
    Z = s2 + s1 / 2
    dec = -2 * nu * sc * (Z - E * core / (2 * sc**2))**2 - 1.5 * nu * sc * (s1 - 2 * E * X / (3 * sc))**2
    bnd = -gam[:, None] * core**2 / np.sin(2 * TT)
    if not drop_gamma:
        dec = dec + bnd
    I = lambda A: float(np.trapezoid(np.trapezoid(A, Th, axis=1), Rs)) * (2 * math.pi)**2   # noqa: E731
    return I(q), I(dec), I(bnd)


def q4(Gt, bg):
    print("Q4 (computed) the bound on explicit seeds, with and without ds1")
    lam = sp.lambdify([R, MU] + list(PP), Gt, 'numpy')
    rows, ok = [], True
    allrows = []
    for band in ((0.72, 0.9), (0.75, 1.75), (1.0, 1.75)):
        Rs = np.linspace(band[0], band[1], 1201)
        F = region3_funcs(bg, Rs)
        gam = lam(Rs, F['mu0'], F['P'], F['dP'], F['d2P']) * np.exp(2 * F['Ia'])
        Th = np.linspace(math.pi / 8, 3 * math.pi / 8, 241)
        RR, TT = np.meshgrid(Rs, Th, indexing='ij')
        env = bump(RR, band[0], band[1]) * bump(TT, math.pi / 8, 3 * math.pi / 8)
        Rc = 0.5 * (band[0] + band[1])
        for m_ in (2, 6, 24):
            for phi in (0.0, 0.8, 1.2, math.pi / 2, 2.4):
                core = env * np.sin(m_ * (math.cos(phi) * (RR - Rc) + math.sin(phi) * (TT - math.pi / 4)))
                allrows.append(('stream', band, m_, phi) + seed_Q(F, Rs, Th, core, gam=gam))
            # seeds with ds1: a second bump in s1, and s1 the pointwise maximiser
            s1 = env * np.cos(m_ * (TT - math.pi / 4)) * 3.0
            core = env * np.sin(m_ * (RR - Rc))
            allrows.append(('s1', band, m_, 0.0) + seed_Q(F, Rs, Th, core, s1=s1, gam=gam))
            allrows.append(('s1 only', band, m_, 0.0) + seed_Q(F, Rs, Th, 0 * core, s1=s1, gam=gam))
            for phi in (0.8, 2.4):
                core = env * np.sin(m_ * (math.cos(phi) * (RR - Rc) + math.sin(phi) * (TT - math.pi / 4)))
                allrows.append(('s1*', band, m_, phi) + seed_Q(F, Rs, Th, core, s1_star=True, gam=gam))
            core = env * np.sin(m_ * (TT - math.pi / 4))
            allrows.append(('s1*', band, m_, math.pi / 2) + seed_Q(F, Rs, Th, core, s1_star=True, gam=gam))
            allrows.append(('s1+', band, m_, 1.2) + seed_Q(F, Rs, Th, core, s1=-s1, gam=gam))
    rel = max(abs(r[4] - r[5]) / abs(r[4]) for r in allrows)
    neg = all(r[4] < 0 for r in allrows)
    bound = all(r[4] <= r[6] + 3e-3 * abs(r[4]) for r in allrows if r[0] != 's1 only')
    worst = max(allrows, key=lambda r: r[4] / abs(r[6]) if r[6] != 0 else -1e9)
    nstream = sum(1 for r in allrows if r[0] == 'stream')
    print("   %d seeds (%d stream seeds as racglobal5 R4, %d with ds1, three bands, one inside the horizon): Q < 0 for "
          "every one: %s; |Q - int decomposition|/|Q| <= %.1e; Q <= -int Gamma psi^2/sin 2th for every seed with "
          "psi != 0: %s (closest: Q/|bound| = %.3f, %s seed, band %s, m = %d)" %
          (len(allrows), nstream, len(allrows) - nstream, neg, rel, bound, worst[4] / abs(worst[6]), worst[0],
           worst[1], worst[2]))
    ok = neg and rel < 2e-3 and bound
    # control: the decomposition without its Gamma term does not reproduce Q
    Rs = np.linspace(0.75, 1.75, 1201)
    F = region3_funcs(bg, Rs)
    gam = lam(Rs, F['mu0'], F['P'], F['dP'], F['d2P']) * np.exp(2 * F['Ia'])
    Th = np.linspace(math.pi / 8, 3 * math.pi / 8, 241)
    RR, TT = np.meshgrid(Rs, Th, indexing='ij')
    core = bump(RR, 0.75, 1.75) * bump(TT, math.pi / 8, 3 * math.pi / 8) * np.sin(2 * (RR - 1.25))
    qd, dd, _ = seed_Q(F, Rs, Th, core, drop_gamma=True, gam=gam)
    ctl = abs(qd - dd) / abs(qd) > 1e-2
    print("   control: the decomposition without -Gamma psi^2/sin 2th misses Q by %.1f %% (rejected): %s" %
          (100 * abs(qd - dd) / abs(qd), ctl))
    return ok and ctl


# ---------------------------------------------------------------- Q5
def q5():
    print("Q5 (exact) the KID (N_s, 2 Y_s), its pairing with Vaidya's constraint map, and the dust's sign")
    bc = load('bandconst5')
    Rb, tb_ = bc.R, bc.th
    mu = sp.Symbol('mu', positive=True)
    f = 1 - mu / Rb**2
    G = 2 - f
    Kt0 = 3 * (f - 1) / (Rb * sp.sqrt(2 - f))
    kap0 = (mu / Rb**3) * (3 - f) / (2 - f)**sp.Rational(3, 2)
    Ns = 1 / sp.sqrt(2 - f)
    YR = mu / (G * Rb**2)
    eps = sp.Symbol('eps')
    names = ['hRR', 'hth', 'h11', 'h22', 'kk', 'kp', 'kt', 'k1', 'k2']
    F9 = [sp.Function(nm)(Rb, tb_) for nm in names]
    G1, G2 = Rb**2 * sp.sin(tb_)**2, Rb**2 * sp.cos(tb_)**2
    g = sp.diag(G * (1 + eps * F9[0]), Rb**2 * (1 + eps * F9[1]), G1 * (1 + eps * F9[2]), G2 * (1 + eps * F9[3]))
    K = sp.zeros(4, 4)
    K[0, 0] = G * (kap0 + eps * F9[4])
    K[0, 1] = K[1, 0] = eps * F9[5]
    K[1, 1] = Rb**2 * (Kt0 / 3 + eps * F9[6])
    K[2, 2] = G1 * (Kt0 / 3 + eps * F9[7])
    K[3, 3] = G2 * (Kt0 / 3 + eps * F9[8])
    H, M, _ = bc.constraints(g, K, bc.X4)
    lin = [sp.expand(sp.diff(e, eps).subs(eps, 0)) for e in (H, M[0], M[1])]
    sqg = sp.sqrt(G) * Rb**3 * sp.sin(tb_) * sp.cos(tb_)

    def kid_ok(cY):
        # the density is linear in the nine fields, so its Euler operator is field-free: it must vanish identically
        L = sqg * (Ns * lin[0] + cY * YR * lin[1])
        res = []
        for eq in euler_equations(L, F9, [Rb, tb_]):
            e = eq.lhs
            assert not any(d.expr in F9 for d in e.atoms(sp.Derivative))
            for pt in ({Rb: sp.Rational(3, 2), tb_: sp.atan(sp.Rational(3, 4)), mu: sp.Rational(7, 5)},
                       {Rb: sp.Rational(4, 5), tb_: sp.atan(sp.Rational(5, 12)), mu: sp.Rational(9, 10)},
                       {Rb: sp.Rational(5, 2), tb_: sp.atan(sp.Rational(8, 15)), mu: sp.Rational(3, 1)}):
                res.append(sp.simplify(e.subs(pt)) == 0)
        return all(res)
    a_ok = kid_ok(2)
    a_ctl = not kid_ok(1)
    print("   (a) Euler operator of sqrt(gamma)(N_s DH + 2 Y_s^R DM_R) vanishes in all nine fields (two points, one "
          "inside the horizon): %s; control: with Y_s^R in place of 2 Y_s^R it does not (rejected): %s" % (a_ok, a_ctl))
    # (b) ingoing Vaidya, mu = mu(vhat) along the slice (vhat = tau0 + R): data, constraint map, Vaidya stress
    m = sp.Function('m')(Rb)
    fv = 1 - m / Rb**2
    # partials of f(vhat, R) at the point: f_R = 2 m/R^3, f_vhat = -m'/R^2, with m' = dm/dR along the slice
    Gv = 2 - fv
    Ktv = 3 * (fv - 1) / (Rb * sp.sqrt(2 - fv))
    Nkv = fv * (2 * m / Rb**3) / 2 - 3 * (2 * m / Rb**3) / 2 + sp.diff(m, Rb) / (2 * Rb**2)
    kapv = -Nkv / (sp.sqrt(2 - fv) * (2 - fv))
    g = sp.diag(Gv, Rb**2, G1, G2)
    K = sp.diag(Gv * kapv, Rb**2 * Ktv / 3, G1 * Ktv / 3, G2 * Ktv / 3)
    H, M, _ = bc.constraints(g, K, bc.X4)
    pair = sp.simplify(H / sp.sqrt(2 - fv) + 2 * m / (Gv * Rb**2) * M[0])
    # T = (3 m'/(2 R^3)) dvhat dvhat (computed: the Einstein tensor of ingoing Vaidya), n^vhat = 1/sqrt(2 - f)
    vh, Rr = sp.symbols('vhat Rr')
    mm = sp.Function('mm')(vh)
    ff = 1 - mm / Rr**2
    # Einstein tensor of -f dv^2 + 2 dv dR + R^2 dOmega_3^2, (v, v) component, by the warped-product formula
    ein_vv = sp.Rational(3, 2) * sp.diff(mm, vh) / Rr**3
    full = sp.diag(-ff, 0, Rr**2, Rr**2 * sp.sin(tb_)**2, Rr**2 * sp.cos(tb_)**2)
    full[0, 1] = full[1, 0] = 1
    X5 = [vh, Rr, tb_, sp.Symbol('p1'), sp.Symbol('p2')]
    gi = full.inv()
    n5 = 5
    Gm = [[[sum(gi[a, d] * (sp.diff(full[d, b], X5[c]) + sp.diff(full[d, c], X5[b]) - sp.diff(full[b, c], X5[d]))
                for d in range(n5)) / 2 for c in range(n5)] for b in range(n5)] for a in range(n5)]

    def Ric(b, d):
        return sp.simplify(sum(sp.diff(Gm[a][b][d], X5[a]) - sp.diff(Gm[a][b][a], X5[d])
                               + sum(Gm[a][a][e] * Gm[e][b][d] - Gm[a][d][e] * Gm[e][b][a] for e in range(n5))
                               for a in range(n5)))
    Rvv = Ric(0, 0)
    ein_ok = sp.simplify(Rvv - ein_vv) == 0                     # R_vv = G_vv since g_vv R = 0 for this metric
    Tn = (sp.Rational(3, 2) * sp.diff(m, Rb) / Rb**3) * 1 * (1 / sp.sqrt(2 - fv))
    b_ok = sp.simplify(pair - 2 * Tn) == 0
    print("   (b) Einstein tensor of ingoing Vaidya G_vv = 3 m'/(2 R^3) (Ricci scalar zero): %s; on the slice data "
          "N_s H + 2 Y_s^R M_R = 2 T(xi, n): %s" % (ein_ok, b_ok))
    # (c) radial null dust
    fs = sp.Symbol('f', real=True)
    gm = sp.Matrix([[-fs, 1], [1, 0]])
    n_low = -sp.Matrix([1, -1]) / sp.sqrt(2 - fs)              # n_a = -d tau/|d tau|, future
    xi = sp.Matrix([1, 0])
    lout = sp.Matrix([1, fs / 2])
    lin_ = sp.Matrix([0, -1])
    nul = [sp.simplify((l.T * gm * l)[0]) == 0 for l in (lout, lin_)]
    T_out = sp.simplify((lout.T * gm * xi)[0] * (lout.T * n_low)[0])
    T_in = sp.simplify((lin_.T * gm * xi)[0] * (lin_.T * n_low)[0])
    fut = [sp.simplify((l.T * n_low)[0]) for l in (lout, lin_)]
    c_ok = all(nul) and sp.simplify(T_out - fs * sp.sqrt(2 - fs) / 4) == 0 and \
        sp.simplify(T_in - 1 / sp.sqrt(2 - fs)) == 0
    print("   (c) l_out, l_in null: %s, future (l.n = %s, %s < 0); T(xi, n)/q = %s (outgoing), %s (ingoing): %s" %
          (all(nul), fut[0], fut[1], T_out, T_in, c_ok))
    return a_ok and a_ctl and ein_ok and b_ok and c_ok


# ---------------------------------------------------------------- Q6
def q6(Gt, bg):
    print("Q6 (computed) inside the horizon, outgoing dust cancels the charge at second order; outside it cannot")
    lam = sp.lambdify([R, MU] + list(PP), Gt, 'numpy')
    out = {}
    for band in ((0.72, 0.9), (1.0, 1.75)):
        Rs = np.linspace(band[0], band[1], 1201)
        F = region3_funcs(bg, Rs)
        gam = lam(Rs, F['mu0'], F['P'], F['dP'], F['d2P']) * np.exp(2 * F['Ia'])
        Th = np.linspace(math.pi / 8, 3 * math.pi / 8, 241)
        RR, TT = np.meshgrid(Rs, Th, indexing='ij')
        env = bump(RR, band[0], band[1]) * bump(TT, math.pi / 8, 3 * math.pi / 8)
        core = env * np.sin(6 * (TT - math.pi / 4))
        Q, _, _ = seed_Q(F, Rs, Th, core, gam=gam)
        # outgoing null dust q1 = env: T1(xi, n) = q1 (l_out . xi)(l_out . n) in Part I's chart (psi_P != 0):
        # xi = e^-psi d_vhat, l_out = d_vhat + (e^psi f/2) d_R, n_a = -(1, -1)/(e^-psi sqrt(...)) normalised
        Ep, f = F['E_P'][:, None], F['f'][:, None]
        g = lambda u, v: -Ep**2 * f * u[0] * v[0] + Ep * (u[0] * v[1] + u[1] * v[0])                    # noqa: E731
        lo = (1.0, Ep * f / 2)
        xi = (1 / Ep, 0.0)
        ginv_tt = -(-1 * 0 + 2 * (1 / Ep) * 1 * (-1) + f * 1)          # -(g^ab dtau_a dtau_b), dtau = (1, -1)
        nl = (-1 / np.sqrt(ginv_tt), 1 / np.sqrt(ginv_tt))
        Tn = env * g(lo, xi) * (lo[0] * nl[0] + lo[1] * nl[1])
        dvol = np.sqrt(F['G'])[:, None] * RR**3 * np.sin(TT) * np.cos(TT)
        IT = float(np.trapezoid(np.trapezoid(Tn * dvol, Th, axis=1), Rs)) * (2 * math.pi)**2
        out[band] = (Q, IT, float(np.max(F['f'])), float(np.min(F['f'])))
    (Qi, ITi, fmaxi, fmini), (Qo, ITo, fmaxo, fmino) = out[(0.72, 0.9)], out[(1.0, 1.75)]
    sstar = Qi / (2 * ITi)
    ok = Qi < 0 and ITi < 0 and sstar > 0
    ctl = Qo < 0 and ITo > 0
    print("   band [0.72, 0.9] (f in [%.3f, %.3f]): Q = %.4e, int T1(xi, n) = %.4e, s* = %.4e > 0: %s" %
          (fmini, fmaxi, Qi, ITi, sstar, ok))
    print("   control: band [1.0, 1.75] (f in [%.3f, %.3f]): Q = %.4e, int T1(xi, n) = %.4e > 0, no positive s*: %s" %
          (fmino, fmaxo, Qo, ITo, ctl))
    return ok and ctl


def main():
    res = {}
    res['Q1'] = q1()
    print('Q1', 'PASS' if res['Q1'] else 'FAIL', flush=True)
    ok2, Gt = q2()
    res['Q2'] = ok2
    print('Q2', 'PASS' if ok2 else 'FAIL', flush=True)
    bgs = {80: background(80), 160: background(160)}
    res['Q3'] = q3(Gt, bgs)
    print('Q3', 'PASS' if res['Q3'] else 'FAIL', flush=True)
    res['Q4'] = q4(Gt, bgs[160])
    print('Q4', 'PASS' if res['Q4'] else 'FAIL', flush=True)
    res['Q5'] = q5()
    print('Q5', 'PASS' if res['Q5'] else 'FAIL', flush=True)
    res['Q6'] = q6(Gt, bgs[160])
    print('Q6', 'PASS' if res['Q6'] else 'FAIL', flush=True)
    return 0 if all(res.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
