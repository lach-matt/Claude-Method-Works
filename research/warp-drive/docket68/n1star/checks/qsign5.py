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
  Q3 (computed, floating point; twobg5's background at n = 80, 160) Gamma > 0 on the seed region ([R7] R in [0.70,
     1.861], the whole of region III on the slice; psi_P = psi_III(vhat) read as in racglobal5 R4), including its
     part inside the horizon; psi_P = 0 on the slice's vacuum points with u <= u1 (the gap and outside the shell),
     so Gamma = 4 mu/R > 0 there by Q2.
  Q4 (computed, floating point) the bound on explicit seeds: for racglobal5 R4's 45 stream seeds (ds1 = 0) and 54 seeds
     with ds1 != 0 (including ds1 equal to the maximiser 2 E X/(3 sc), and ds1 alone), Q computed directly equals the
     integral of the decomposition to the quadrature's accuracy (relative to Q, and relative to the decomposition's
     Gamma term), and Q <= -int Gamma psi^2/sin 2th < 0 for every one. Control (must fail): the decomposition with its
     -Gamma psi^2/sin 2th term dropped misses Q by about that term.
  Q5 (exact, sympy; ingoing Vaidya in Part I's chart, psi_P = 0, mu = mu(vhat) arbitrary) the KID and the matter term:
     (a) (N_s, 2 Y_s) is in the kernel of the adjoint of the linearised constraint map (H, M) on Tangherlini's slice
         (the Euler operator of sqrt(gamma)(N_s DH + 2 Y_s^R DM_R) in all nine invariant fields of (dgamma diagonal,
         dK) vanishes), Y_s^R = mu/(G R^2); control: (N_s, Y_s) is not;
     (b) on the Vaidya slice data, N_s H + 2 Y_s^R M_R = 2 T(xi, n) with T the Vaidya stress (3 mu'/(2 R^3)) dvhat^2,
         xi = d_vhat: the KID pairs the constraint map with 2 T(xi, n), so exact data with matter need
         eps^2 Q/2 + O(eps^3) = int_U T(xi, n);
     (c) for radial null dust, T(xi, n) = q f sqrt(2 - f)/4 along l_out = d_vhat + (f/2) d_R and q/sqrt(2 - f) along
         l_in = -d_R: negative exactly for outgoing dust inside the horizon (f < 0); for xi future-causal (f >= 0) and
         any matter with the dominant energy condition T(xi, n) >= 0. [R7 (c'), the round-6 verifier's m9: for any
         psi_P, with E = e^psi_P, T(xi, n)/q = E f (2 - E f)/(4 sqrt(2/E - f)) along l_out = d_vhat + (E f/2) d_R:
         its sign is f's (exact).]
  Q6 (computed) on a band inside the horizon (R in [0.72, 0.9]) a momentum seed with Q < 0 and an outgoing dust profile
     q1 >= 0 there give int T1(xi, n) < 0, so the dust amplitude s* = Q/(2 int T1(xi, n)) > 0 cancels the charge at
     second order: the intermediate-value construction of exactly localised Einstein-null-dust data inside the horizon.
     Control: the same dust on a band outside the horizon gives int T1(xi, n) > 0 (no positive s*).
  Q7 (computed, Gauss-Legendre quadrature of closed forms; R7, the round-6 verifier's m1; R8, the round-7 reader's
     nits) seeds that reach the axes. A smooth invariant momentum seed has psi = sin^2 th cos^2 th F(R, cos 2th) and
     s1 smooth in cos 2th (Kt = E psi_th/sc is then smooth and generally nonzero on the axes); for this class the
     theta flux of Q1's integrations by parts, 2 nu beta E^2 psi psi_th/sc - 2 nu E psi s1 - nu E^2 (cos 2th/sc^2)
     psi^2, vanishes at th = 0, pi/2 because psi = O(sc^2). On Tangherlini's slice in Part I's chart (psi_P = 0,
     mu = 0.82), six such seeds (random F, s1 polynomial in cos 2th, two bands, one inside the horizon) have Q equal
     to the decomposition integrated over the whole of [0, pi/2] to rounding, and Q <= -int Gamma psi^2/sin 2th < 0.
     [R8] They reach the axes on the whole band: Kt/E there is exactly +-2 env(R) L+-(R) with L+- linear of slope 1,
     so it vanishes at most at one point, and its least |L+-| over the band is printed. [R8] On [t0, pi/2 - t0] the
     integral of (Q-density - decomposition) equals the flux, top minus bottom, with the signs (+2, -2, -1), for the
     regular seeds (where it vanishes like t0^2) and for seeds with psi = O(sc), not axis-regular (where it tends to a
     nonzero limit: for them the identity on [0, pi/2] fails by the axis terms); no divergent integral is evaluated.
     Controls (must fail): each flux term with its sign flipped misses the truncated identity; the decomposition with
     4 nu E^2 -> 3 nu E^2 in Gamma, integrated as it stands, misses Q.

Labels: computed (Q1, Q2, Q5 exact; Q3, Q4, Q6, Q7 floating point; Q3's Gamma > 0 is certified by interval
arithmetic in checks/intcert5.py C1). Run: python3 checks/qsign5.py   (about a quarter of an hour under load)
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
        Rs = np.linspace(0.70, 1.861, 2323)                                # [R7] region III on the slice: [a, r1]
        F = region3_funcs(bg, Rs)
        g_over_E2 = lam(Rs, F['mu0'], F['P'], F['dP'], F['d2P'])
        Gam = g_over_E2 * np.exp(2 * F['Ia'])
        ratio = Gam / (4 * F['mu0'] / Rs * np.exp(2 * F['Ia']) * Rs**4 / (Rs**2 + F['mu0']))   # 1 at psi_P = 0
        rh = math.sqrt(F['mu0'])
        rows.append((n, float(np.min(g_over_E2)), float(np.min(ratio)), float(np.max(ratio)), rh,
                     float(np.max(np.abs(bg['psi_out']))), len(bg['psi_out'])))
        ok &= np.min(g_over_E2) > 0
    for (n, mn, rmin, rmax, rh, po, npo) in rows:
        print("   n = %d: R in [0.70, 1.861] (horizon at %.4f): min Gamma/E^2 = %.4f > 0; Gamma over its psi_P = 0 "
              "value in [%.4f, %.4f]; |psi_P| <= %.1e on %d slice points with u <= u1 - 0.1" %
              (n, rh, mn, rmin, rmax, po, npo))
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
    relg = max(abs(r[4] - r[5]) / abs(r[6]) for r in allrows if r[0] != 's1 only')
    neg = all(r[4] < 0 for r in allrows)
    bound = all(r[4] <= r[6] + 3e-3 * abs(r[4]) for r in allrows if r[0] != 's1 only')
    worst = max(allrows, key=lambda r: r[4] / abs(r[6]) if r[6] != 0 else -1e9)
    nstream = sum(1 for r in allrows if r[0] == 'stream')
    print("   %d seeds (%d stream seeds as racglobal5 R4, %d with ds1, three bands, one inside the horizon): Q < 0 for "
          "every one: %s; |Q - int decomposition| <= %.1e |Q| and <= %.1e |int Gamma psi^2/sin 2th|; Q <= -int Gamma "
          "psi^2/sin 2th for every seed with psi != 0: %s (closest: Q/|bound| = %.3f, %s seed, band %s, m = %d)" %
          (len(allrows), nstream, len(allrows) - nstream, neg, rel, relg, bound, worst[4] / abs(worst[6]), worst[0],
           worst[1], worst[2]))
    ok = neg and rel < 2e-3 and relg < 0.05 and bound
    # control: the decomposition without its Gamma term does not reproduce Q
    Rs = np.linspace(0.75, 1.75, 1201)
    F = region3_funcs(bg, Rs)
    gam = lam(Rs, F['mu0'], F['P'], F['dP'], F['d2P']) * np.exp(2 * F['Ia'])
    Th = np.linspace(math.pi / 8, 3 * math.pi / 8, 241)
    RR, TT = np.meshgrid(Rs, Th, indexing='ij')
    core = bump(RR, 0.75, 1.75) * bump(TT, math.pi / 8, 3 * math.pi / 8) * np.sin(2 * (RR - 1.25))
    qd, dd, bb = seed_Q(F, Rs, Th, core, drop_gamma=True, gam=gam)
    ctl = abs(qd - dd) / abs(bb) > 0.5
    print("   control: the decomposition without -Gamma psi^2/sin 2th misses Q by %.3f of that term (rejected): %s" %
          (abs(qd - dd) / abs(bb), ctl))
    return ok and ctl


# ---------------------------------------------------------------- Q5
def constraints_fast(g, K, X):
    """bandconst5.constraints without its per-entry simplification (same formulas: H = R + (tr K)^2 - |K|^2,
    M_i = D_j K^j_i - D_i tr K)"""
    n = len(X)
    gi = g.inv()
    Gm = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]

    def Ric(b, d):
        return sum(sp.diff(Gm[a][b][d], X[a]) - sp.diff(Gm[a][b][a], X[d])
                   + sum(Gm[a][a][e] * Gm[e][b][d] - Gm[a][d][e] * Gm[e][b][a] for e in range(n)) for a in range(n))
    Rs = sum(gi[b, d] * Ric(b, d) for b in range(n) for d in range(n) if gi[b, d] != 0)
    trK = sum(gi[i, j] * K[i, j] for i in range(n) for j in range(n))
    KK = sum(gi[i, k] * gi[j, l] * K[i, j] * K[k, l] for i in range(n) for j in range(n) for k in range(n)
             for l in range(n) if gi[i, k] != 0 and gi[j, l] != 0)
    H = Rs + trK**2 - KK

    def DK(c, a, b):
        return sp.diff(K[a, b], X[c]) - sum(Gm[e][c][a] * K[e, b] + Gm[e][c][b] * K[a, e] for e in range(n))
    M = [sum(gi[j, c] * DK(c, j, i) for j in range(n) for c in range(n) if gi[j, c] != 0) - sp.diff(trK, X[i])
         for i in range(n)]
    return H, M


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
    H, M = constraints_fast(g, K, bc.X4)
    lin = [sp.diff(e, eps).subs(eps, 0) for e in (H, M[0], M[1])]
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
    print("   (a) Euler operator of sqrt(gamma)(N_s DH + 2 Y_s^R DM_R) vanishes in all nine fields (three points, one "
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
    H, M = constraints_fast(g, K, bc.X4)
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
    # [R7] (c') any psi_P (E = e^psi_P > 0, E f < 2): xi = e^-psi d_vhat, l_out = d_vhat + (E f/2) d_R
    Es = sp.Symbol('E', positive=True)
    gmE = sp.Matrix([[-Es**2 * fs, Es], [Es, 0]])
    nE = -sp.Matrix([1, -1]) / sp.sqrt(2 / Es - fs)
    xiE = sp.Matrix([1 / Es, 0])
    loE = sp.Matrix([1, Es * fs / 2])
    TE = sp.simplify((loE.T * gmE * xiE)[0] * (loE.T * nE)[0])
    want = Es * fs * (2 - Es * fs) / (4 * sp.sqrt(2 / Es - fs))
    nulE = sp.simplify((loE.T * gmE * loE)[0]) == 0
    futE = sp.simplify((loE.T * nE)[0] + (2 - Es * fs) / (2 * sp.sqrt(2 / Es - fs))) == 0
    cE_ok = nulE and futE and sp.simplify(TE - want) == 0 and \
        sp.simplify(want.subs(Es, 1) - fs * sp.sqrt(2 - fs) / 4) == 0
    print("   (c') any psi_P (E = e^psi_P): l_out null and future (l.n = -(2 - E f)/(2 sqrt(2/E - f)) < 0): %s; "
          "T(xi, n)/q = E f (2 - E f)/(4 sqrt(2/E - f)), whose sign is f's: %s" % (nulE and futE, cE_ok))
    return a_ok and a_ctl and ein_ok and b_ok and c_ok and cE_ok


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


# ---------------------------------------------------------------- Q7
def q7():
    print("Q7 (computed) seeds that reach the axes: psi = sin^2 cos^2 F(R, cos 2th), s1 smooth in cos 2th")
    mu = sp.Rational(82, 100)
    f = 1 - mu / R**2
    G = 2 - f
    Kt0 = 3 * (f - 1) / (R * sp.sqrt(2 - f))
    k0 = (mu / R**3) * (3 - f) / (2 - f)**sp.Rational(3, 2)
    Y0 = Kt0 / 3
    Ew = sp.sqrt(G) / R                                              # E at psi_P = 0 (Q2)
    nu = R**3
    c2 = sp.cos(2 * th)
    sc = sp.sin(th) * sp.cos(th)
    cs = sp.Symbol('c')
    rng = np.random.default_rng(11)
    out, trunc, axis = [], [], []
    T0S = (0.02, 0.05, 0.1, 0.2)
    xr, wr = np.polynomial.legendre.leggauss(60)
    for band in ((sp.Rational(1), sp.Rational(7, 4)), (sp.Rational(18, 25), sp.Rational(9, 10))):
        R1, R2 = band
        env = (R - R1)**4 * (R2 - R)**4 / ((R2 - R1) / 2)**8
        Rn = float(R1) + (float(R2) - float(R1)) * (xr + 1) / 2
        WR = wr * (float(R2) - float(R1)) / 2
        for trial in range(3):
            a = [sp.Rational(int(x), 7) for x in rng.integers(-9, 10, 3)]
            b = [sp.Rational(int(x), 5) for x in rng.integers(-9, 10, 3)]
            for kind in ('regular', 'irregular'):
                if kind == 'regular':
                    Fp = env * (a[0] + 2 + a[1] * cs + a[2] * cs**2 + (R - R1))
                    psi = sc**2 * Fp.subs(cs, c2)
                else:                                                     # psi = O(sc): Kt ~ 1/sc at the axes
                    psi = sc * env * (a[0] + 2 + a[1] * c2)
                s1 = env * (b[0] + b[1] * c2 + b[2] * c2**2)
                _, cc, beta, E, Kt, ph, s2 = seed_fields(G, k0, Y0, sp.log(Ew), psi, s1)
                q = nu * sc * (2 * cc * Kt**2 + sp.Rational(2, 3) * Kt**2 - 2 * ph**2 - s1**2 - s2**2 - (s1 + s2)**2)
                dec, Gam = decomposition(nu, G, E, psi, s1, s2)
                gterm = -Gam * psi**2 / sp.sin(2 * th)
                # the theta flux of R7.1 [R8]: 2 nu beta E^2 psi psi_th/sc - 2 nu E psi s1 - nu E^2 (cos 2th/sc^2) psi^2
                Bk = [nu * beta * E**2 * psi * sp.diff(psi, th) / sc, nu * E * psi * s1, nu * E**2 * c2 * psi**2 / sc**2]
                fD = sp.lambdify([R, th], q - dec, 'numpy')
                fB = [sp.lambdify([R, th], e, 'numpy') for e in Bk]
                for t0 in T0S:
                    xt, wt = np.polynomial.legendre.leggauss(120)
                    Tn = t0 + (np.pi / 2 - 2 * t0) * (xt + 1) / 2
                    WT = wt * (np.pi / 2 - 2 * t0) / 2
                    RR, TT = np.meshgrid(Rn, Tn, indexing='ij')
                    Dl = float(np.sum(np.outer(WR, WT) * fD(RR, TT)))
                    bk = [float(np.sum(WR * (B(Rn, np.pi / 2 - t0) - B(Rn, t0)))) for B in fB]
                    trunc.append((band, trial, kind, t0, Dl, bk))
                if kind != 'regular':
                    continue
                # the whole of [0, pi/2] (regular seeds: every integrand bounded), and the decomposition with
                # 4 nu E^2 -> 3 nu E^2 in Gamma, integrated as it stands (the independent control)
                decm, _ = decomposition(nu, G, E, psi, s1, s2, m_gam=sp.Rational(3, 4))
                fq, fd, fg, fm = [sp.lambdify([R, th], e, 'numpy') for e in (q, dec, gterm, decm)]
                xt, wt = np.polynomial.legendre.leggauss(60)
                Tn = (math.pi / 2) * (xt + 1) / 2
                W = np.outer(WR, wt * (math.pi / 4))
                RR, TT = np.meshgrid(Rn, Tn, indexing='ij')
                Iq, Id, Ig, Im = [float(np.sum(W * fn(RR, TT))) for fn in (fq, fd, fg, fm)]
                out.append((band, trial, Iq, Id, Ig, Im))
                # Kt/E on the axes, exactly: Kt/E = psi_th/sc = 2 cos 2th F - 4 sc^2 F_c, so 2 F(R, 1) at th = 0
                # and -2 F(R, -1) at th = pi/2; F(R, +-1) = env L+-(R), L+- linear in R with slope 1
                for side, cval in ((0, 1), (1, -1)):
                    L = sp.expand(sp.cancel(Fp.subs(cs, cval) / env))
                    roots = [r for r in sp.solve(L, R) if R1 < r < R2]
                    mn = min(abs(L.subs(R, R1)), abs(L.subs(R, R2))) if not roots else 0
                    th_ = 1e-7 if side == 0 else math.pi / 2 - 1e-7
                    num = float((sp.diff(psi, th) / sc).subs({R: (R1 + R2) / 2, th: th_}).evalf(30))
                    exact = float(((2 if side == 0 else -2) * Fp.subs(cs, cval)).subs(R, (R1 + R2) / 2))
                    axis.append((band, trial, side, sp.degree(L, R), len(roots), float(mn), abs(num - exact)))
    rel = max(abs(o[2] - o[3]) / abs(o[2]) for o in out)
    relg = max(abs(o[2] - o[3]) / abs(o[4]) for o in out)
    neg = all(o[2] < 0 and o[2] <= o[4] + 1e-9 * abs(o[2]) for o in out)
    # the truncated identity: int over [t0, pi/2 - t0] of (q - dec) = the flux, top minus bottom, signs (+2, -2, -1)
    sg = (2, -2, -1)
    terr = max(abs(t[4] - sum(s_ * b_ for s_, b_ in zip(sg, t[5]))) / max(abs(t[4]), max(abs(x) for x in t[5]))
               for t in trunc)
    reg_t = {(t[0], t[1], t[3]): t[4] for t in trunc if t[2] == 'regular'}
    irr_t = {(t[0], t[1], t[3]): t[4] for t in trunc if t[2] == 'irregular'}
    keys = sorted({(k[0], k[1]) for k in reg_t})
    reg_decay = max(abs(reg_t[k + (0.02,)] / reg_t[k + (0.05,)]) for k in keys)        # ~ (2/5)^2 = 0.16
    irr_lim = min(abs(irr_t[k + (0.02,)] / irr_t[k + (0.05,)]) for k in keys)           # ~ 1: a nonzero limit
    irr_size = min(abs(irr_t[k + (0.02,)]) for k in keys)
    # controls: each of the three flux terms with its sign flipped misses the truncated identity somewhere
    flips = []
    for j in range(3):
        sgf = list(sg)
        sgf[j] = -sgf[j]
        flips.append(max(abs(t[4] - sum(s_ * b_ for s_, b_ in zip(sgf, t[5]))) / abs(t[4]) for t in trunc
                         if abs(t[4]) > 1e-6))
    mism = min(abs(o[2] - o[5]) / abs(o[4]) for o in out)
    deg_ok = all(x[3] == 1 for x in axis) and max(x[6] for x in axis) < 1e-5
    nroot = sum(x[4] for x in axis)
    mn_axis = min(x[5] for x in axis if x[4] == 0)
    print("   six regular seeds (two bands, one inside the horizon): Q equals the decomposition over the whole of "
          "[0, pi/2] to %.1e of Q and %.1e of its Gamma term, Q < 0 and Q <= -int Gamma psi^2/sin 2th: %s" %
          (rel, relg, neg))
    print("   they reach the axes [R8]: Kt/E on the axes is exactly 2 env(R) L+(R) at th = 0 and -2 env(R) L-(R) at "
          "th = pi/2, L+- linear in R with slope 1 (checked against psi_th/sc at 1e-7 from the axis: %s), so it "
          "vanishes at most at one point of the open band; %d of the 12 (seed, axis) pairs have that zero, and the "
          "rest have |L+-| >= %.3f on the whole band, so |Kt/E| >= %.3f env(R) there" % (deg_ok, nroot, mn_axis,
                                                                                         2 * mn_axis))
    print("   truncated to [t0, pi/2 - t0], t0 in %s, regular and axis-irregular seeds alike [R8]: int (q - dec) equals "
          "the theta flux 2 nu beta E^2 psi psi_th/sc - 2 nu E psi s1 - nu E^2 (cos 2th/sc^2) psi^2, top minus "
          "bottom, to %.1e; regular seeds: it vanishes as t0 -> 0 (ratio t0 = 0.02 to 0.05 at most %.3f, t0^2: "
          "0.16); psi = O(sc) seeds: it tends to a nonzero limit (ratio at least %.3f, size at least %.3f), so for "
          "them the identity on [0, pi/2] fails by the axis boundary terms" % (T0S, terr, reg_decay, irr_lim,
                                                                                irr_size))
    print("   controls: each flux term with its sign flipped misses the truncated identity, by up to %s of it "
          "(rejected): %s; the decomposition with 4 nu E^2 -> 3 nu E^2 in Gamma, integrated as it stands, misses Q "
          "by at least %.3f of the Gamma term (rejected): %s" %
          (", ".join("%.2f" % x for x in flips), all(x > 1e-3 for x in flips), mism, mism > 1e-3))
    return (rel < 1e-8 and relg < 1e-4 and neg and deg_ok and terr < 1e-8 and reg_decay < 0.3 and irr_lim > 0.5
            and irr_size > 1e-3 and all(x > 1e-3 for x in flips) and mism > 1e-3)


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
    res['Q7'] = q7()
    print('Q7', 'PASS' if res['Q7'] else 'FAIL', flush=True)
    return 0 if all(res.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
