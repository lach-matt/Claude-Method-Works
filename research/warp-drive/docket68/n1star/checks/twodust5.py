"""twodust5.py -- FAMILIES5 section 4c (D389): the two-dust round background of the two-phase Stage 0.

Section 4b's Stage 0 closes on any round double-null background whose Ricci tensor is the two dusts' stress,

    g0 = -2 e^(2s(u,v)) du dv + R(u,v)^2 dOmega_3^2,     Ric(g0) = K_in dv^2 + K_out du^2,
    K_in R^3 = A(v),  K_out R^3 = B(u)                   (the Isaacson laws of T2),

and left the background unconstructed. Here:

  B1 (exact) the Ricci tensor of g0: off-diagonal and angular-mixed components vanish, Ric_uv = 0 and the angular
     equation are equivalent to the evolution  R_uv = -(e^(2s) + 2 R_u R_v)/R,  s_uv = 3 (e^(2s) + 2 R_u R_v)/(2 R^2),
     and the two remaining equations are the Raychaudhuri constraints
         C_u := R_uu - 2 s_u R_u + B/(3 R^2) = 0,    C_v := R_vv - 2 s_v R_v + A/(3 R^2) = 0.
  B2 (exact) the constraints propagate: modulo the evolution, d_v (R^2 C_u) = 0 and d_u (R^2 C_v) = 0 identically,
     because B depends on u alone and A on v alone. Control: with B = B(u, v), d_v (R^2 C_u) = R dB/dv / 3 (up to the
     factor), not zero. So data satisfying C_v on u = u0 and C_u on v = v0 give, through the evolution, a solution.
  B3 (exact) the mass function mu := R^2 (1 + 2 e^(-2s) R_u R_v) (g0^(ab) dR_a dR_b = 1 - mu/R^2) obeys, on solutions,
         mu_v = -(2/3) A e^(-2s) R_u,     mu_u = -(2/3) B e^(-2s) R_v:
     where R_u < 0 < R_v the ingoing dust adds mass and the outgoing dust carries it away.
  B4 (exact) Minkowski, e^(2s) = 1/2, R = (v - u)/2, solves the evolution with A = B = 0.
  B5 (computed) the characteristic problem: flat corner data, an ingoing pulse A on v in [1, 3] crossing u = -10, an
     outgoing pulse B on u in [-9, -7] crossing v = 0, data on each cone from its constraint (s = -ln 2/2 there), and the
     interior by a second-order diamond scheme for the evolution alone. The interior constraint residuals fall at
     second order with the step (ratio 4 per halving), and mu at the far corner equals its value from integrating
     B3's fluxes along the two far edges. Control: C_u with B shifted by 1/2 in u does not fall.
Labels: B1-B4 computed (exact, sympy); B5 computed (floating point). Local existence for this 1+1 semilinear
Goursat system is the standard Picard iteration on a characteristic rectangle; it is not read at source here.

    python3 checks/twodust5.py [--selftest]
"""
import math
import sys

import numpy as np
import sympy as sp

u, v, th, p1, p2 = sp.symbols('u v theta phi1 phi2', real=True)
Rf = sp.Function('R')(u, v)
sf = sp.Function('s')(u, v)
Af = sp.Function('A')(v)
Bf = sp.Function('B')(u)
F = sp.exp(2*sf) + 2*sp.diff(Rf, u)*sp.diff(Rf, v)
EVO = {sp.Derivative(Rf, u, v): -F/Rf, sp.Derivative(sf, u, v): 3*F/(2*Rf**2)}


def ricci():
    X = [u, v, th, p1, p2]
    g = sp.zeros(5)
    g[0, 1] = g[1, 0] = -sp.exp(2*sf)
    g[2, 2] = Rf**2
    g[3, 3] = Rf**2*sp.cos(th)**2
    g[4, 4] = Rf**2*sp.sin(th)**2
    gi = g.inv()
    G = [[[sp.simplify(sp.Rational(1, 2)*sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                                         - sp.diff(g[b, c], X[d])) for d in range(5)))
           for c in range(5)] for b in range(5)] for a in range(5)]
    return lambda b, c: sp.simplify(sum(sp.diff(G[a][b][c], X[a]) - sp.diff(G[a][b][a], X[c])
                                        + sum(G[a][a][d]*G[d][b][c] - G[a][c][d]*G[d][b][a] for d in range(5))
                                        for a in range(5)))


def reduce_mixed(e):
    """replace every derivative with at least one u and one v by the evolution, repeatedly"""
    for _ in range(6):
        e = e.doit()
        rep = {}
        for d in e.atoms(sp.Derivative):
            vc = dict(d.variable_count)
            if vc.get(u, 0) >= 1 and vc.get(v, 0) >= 1:
                val = EVO[sp.Derivative(d.expr, u, v)]
                if vc[u] > 1:
                    val = sp.diff(val, u, vc[u] - 1)
                if vc[v] > 1:
                    val = sp.diff(val, v, vc[v] - 1)
                rep[d] = val
        if not rep:
            break
        e = e.xreplace(rep)
    return sp.simplify(e)


def exact_checks():
    ok = {}
    Ric = ricci()
    Ruv, Rth = Ric(0, 1), Ric(2, 2)
    off = [Ric(i, j) for i, j in ((0, 2), (0, 3), (1, 2), (1, 4), (2, 3), (2, 4), (3, 4))]
    sol = sp.solve([Ruv, Rth], [sp.Derivative(Rf, u, v), sp.Derivative(sf, u, v)], dict=True)
    b1 = (len(sol) == 1 and all(sp.simplify(sol[0][k] - EVO[k]) == 0 for k in EVO)
          and all(sp.simplify(o) == 0 for o in off) and sp.simplify(Ric(3, 3)/sp.cos(th)**2 - Rth) == 0
          and sp.simplify(Ric(0, 0) - 3*(2*sp.diff(Rf, u)*sp.diff(sf, u) - sp.diff(Rf, u, 2))/Rf) == 0)
    ok["B1"] = b1
    Cu = sp.diff(Rf, u, 2) - 2*sp.diff(sf, u)*sp.diff(Rf, u) + Bf/(3*Rf**2)
    Cv = sp.diff(Rf, v, 2) - 2*sp.diff(sf, v)*sp.diff(Rf, v) + Af/(3*Rf**2)
    Buv = sp.Function('Bb')(u, v)
    Cu_bad = sp.diff(Rf, u, 2) - 2*sp.diff(sf, u)*sp.diff(Rf, u) + Buv/(3*Rf**2)
    ok["B2"] = (reduce_mixed(sp.diff(Rf**2*Cu, v)) == 0 and reduce_mixed(sp.diff(Rf**2*Cv, u)) == 0
                and reduce_mixed(sp.diff(Rf**2*Cu_bad, v)) != 0)
    mu = Rf**2*(1 + 2*sp.exp(-2*sf)*sp.diff(Rf, u)*sp.diff(Rf, v))
    du_ = reduce_mixed(sp.diff(mu, u)).subs(sp.Derivative(Rf, (u, 2)), sp.solve(Cu, sp.Derivative(Rf, (u, 2)))[0])
    dv_ = reduce_mixed(sp.diff(mu, v)).subs(sp.Derivative(Rf, (v, 2)), sp.solve(Cv, sp.Derivative(Rf, (v, 2)))[0])
    ok["B3"] = (sp.simplify(du_ + sp.Rational(2, 3)*Bf*sp.exp(-2*sf)*sp.diff(Rf, v)) == 0
                and sp.simplify(dv_ + sp.Rational(2, 3)*Af*sp.exp(-2*sf)*sp.diff(Rf, u)) == 0)
    Rm, sm = (v - u)/2, -sp.log(2)/2
    ok["B4"] = sp.simplify((sp.diff(Rm, u, v) + (sp.exp(2*sm) + 2*sp.diff(Rm, u)*sp.diff(Rm, v))/Rm)) == 0
    return ok


def bump(x, a, b):
    w = (x - a)/(b - a)
    return np.where((w > 0) & (w < 1), np.sin(np.pi*np.clip(w, 0, 1))**4, 0.0)


AMP_A, AMP_B = 2.0, 1.0
U0, U1, V0, V1 = -10.0, -3.0, 0.0, 6.0


def A_(x):
    return AMP_A*bump(x, 1.0, 3.0)


def B_(x, shift=0.0):
    return AMP_B*bump(x - shift, -9.0, -7.0)


def cone(x, src, R0, R1, n):
    """R'' = -src(x)/(3 R^2) along a cone (s constant there), RK4 on n steps"""
    h = (x[-1] - x[0])/n
    R = np.empty(n + 1)
    P = np.empty(n + 1)
    R[0], P[0] = R0, R1
    f = lambda xx, y: np.array([y[1], -src(np.array(xx))/(3*y[0]**2)])
    for k in range(n):
        y = np.array([R[k], P[k]])
        k1 = f(x[k], y); k2 = f(x[k] + h/2, y + h/2*k1); k3 = f(x[k] + h/2, y + h/2*k2); k4 = f(x[k] + h, y + h*k3)
        y = y + h/6*(k1 + 2*k2 + 2*k3 + k4)
        R[k + 1], P[k + 1] = y
    return R, P


def solve(n):
    """n steps per unit: diamond scheme for the evolution; data from the constraints on u = U0 and v = V0"""
    Nu, Nv = int(round((U1 - U0)*n)), int(round((V1 - V0)*n))
    uu, vv = np.linspace(U0, U1, Nu + 1), np.linspace(V0, V1, Nv + 1)
    du, dv = uu[1] - uu[0], vv[1] - vv[0]
    R = np.full((Nu + 1, Nv + 1), np.nan)
    S = np.full((Nu + 1, Nv + 1), -math.log(2)/2)
    R0 = (V0 - U0)/2
    R[0], _ = cone(vv, A_, R0, 0.5, Nv)
    R[:, 0], _ = cone(uu, B_, R0, -0.5, Nu)
    for i in range(1, Nu + 1):
        for j in range(1, Nv + 1):
            rs, re, rw = R[i - 1, j - 1], R[i - 1, j], R[i, j - 1]
            ss, se, sw = S[i - 1, j - 1], S[i - 1, j], S[i, j - 1]
            rn, sn = re + rw - rs, se + sw - ss
            for _ in range(3):
                rc, sc = (rs + re + rw + rn)/4, (ss + se + sw + sn)/4
                ru = (rw - rs + rn - re)/(2*du)
                rv = (re - rs + rn - rw)/(2*dv)
                Fc = math.exp(2*sc) + 2*ru*rv
                rn = re + rw - rs - du*dv*Fc/rc
                sn = se + sw - ss + du*dv*1.5*Fc/rc**2
            R[i, j], S[i, j] = rn, sn
    return uu, vv, R, S


def residuals(uu, vv, R, S, shift=0.0):
    du, dv = uu[1] - uu[0], vv[1] - vv[0]
    Ruu = (R[2:, :] - 2*R[1:-1, :] + R[:-2, :])/du**2
    Ru = (R[2:, :] - R[:-2, :])/(2*du)
    Su = (S[2:, :] - S[:-2, :])/(2*du)
    Cu = Ruu - 2*Su*Ru + B_(uu[1:-1], shift)[:, None]/(3*R[1:-1, :]**2)
    Rvv = (R[:, 2:] - 2*R[:, 1:-1] + R[:, :-2])/dv**2
    Rv = (R[:, 2:] - R[:, :-2])/(2*dv)
    Sv = (S[:, 2:] - S[:, :-2])/(2*dv)
    Cv = Rvv - 2*Sv*Rv + A_(vv[1:-1])[None, :]/(3*R[:, 1:-1]**2)
    return np.abs(Cu).max(), np.abs(Cv).max()


def mass(uu, vv, R, S):
    du, dv = uu[1] - uu[0], vv[1] - vv[0]
    Ru = np.gradient(R, du, axis=0, edge_order=2)
    Rv = np.gradient(R, dv, axis=1, edge_order=2)
    mu = R**2*(1 + 2*np.exp(-2*S)*Ru*Rv)
    fv = -(2/3)*A_(vv)*np.exp(-2*S[0])*Ru[0]           # mu_v along u = U0
    fu = -(2/3)*B_(uu)*np.exp(-2*S[:, -1])*Rv[:, -1]   # mu_u along v = V1
    trap = lambda f, h: h*(f.sum() - (f[0] + f[-1])/2)
    return mu[-1, -1], mu[0, 0] + trap(fv, dv) + trap(fu, du), mu, Ru, Rv


def numeric_checks(verbose=True):
    res = {}
    for n in (20, 40, 80):
        uu, vv, R, S = solve(n)
        res[n] = (residuals(uu, vv, R, S), residuals(uu, vv, R, S, shift=0.5), mass(uu, vv, R, S), (uu, vv, R, S))
    r20, r40, r80 = (res[n][0] for n in (20, 40, 80))
    ratios = [r20[k]/r40[k] for k in (0, 1)] + [r40[k]/r80[k] for k in (0, 1)]
    c40, c80 = res[40][1][0], res[80][1][0]
    mfar, mflux, mu, Ru, Rv = res[80][2]
    uu, vv, R, S = res[80][3]
    ok = all(3 <= q <= 6 for q in ratios) and c80 > 0.5*c40 and abs(mfar - mflux) < 1e-3*abs(mfar)
    untrapped = bool((Ru < 0).all() and (Rv > 0).all())
    if verbose:
        print("  B5: interior constraint residuals |C_u|, |C_v| at 20, 40, 80 steps per unit: %.2e %.2e, %.2e %.2e, "
              "%.2e %.2e (ratios %s)" % (r20[0], r20[1], r40[0], r40[1], r80[0], r80[1],
                                         ", ".join("%.2f" % q for q in ratios)))
        print("  B5: control, C_u with B shifted by 1/2: %.2e, %.2e (does not fall)" % (c40, c80))
        print("  B5: mu at the far corner %.6f; from the fluxes along the far edges %.6f; mu at the start %.6f; "
              "max mu %.4f; min R %.3f; untrapped throughout (R_u < 0 < R_v): %s"
              % (mfar, mflux, mu[0, 0], np.nanmax(mu), np.nanmin(R), untrapped))
    return ok


def main():
    ok = exact_checks()
    for k in ("B1", "B2", "B3", "B4"):
        print("  %s: %s" % (k, ok[k]))
    ok["B5"] = numeric_checks()
    for k, val in ok.items():
        print(k, "PASS" if val else "FAIL")
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
